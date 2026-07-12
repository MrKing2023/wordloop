#!/usr/bin/env python3
"""Extract one exam-tagged base lexicon from ECDICT CSV.

This script deliberately exports dictionary facts only. It does not invent example
sentences, accepted answers or usage notes. Those are produced by a separate,
auditable AI content pipeline.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from common import parse_exchange, parse_int, parse_pos, parse_tags, split_lines, word_id, write_json


def load_exam_config(path: Path, exam: str) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    try:
        return data["exams"][exam]
    except KeyError as exc:
        raise SystemExit(f"Unknown exam '{exam}'. Available: {', '.join(data.get('exams', {}))}") from exc


def frequency_key(entry: dict) -> tuple:
    frq = entry.get("frequency", {}).get("modern") or 10**9
    bnc = entry.get("frequency", {}).get("bnc") or 10**9
    return (frq, bnc, entry["word"])


def extract(input_path: Path, exam: str, config_path: Path, limit: int | None = None) -> dict:
    config = load_exam_config(config_path, exam)
    wanted = {config["sourceTag"].lower(), *[x.lower() for x in config.get("aliases", [])]}
    entries: list[dict] = []
    seen: set[str] = set()

    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"word", "phonetic", "definition", "translation", "pos", "tag", "bnc", "frq", "exchange"}
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"ECDICT CSV is missing columns: {', '.join(sorted(missing))}")

        for row in reader:
            tags = set(parse_tags(row.get("tag")))
            if not tags.intersection(wanted):
                continue
            word = (row.get("word") or "").strip()
            key = word_id(word)
            if not word or not key or key in seen:
                continue
            seen.add(key)
            entry = {
                "id": key,
                "word": word,
                "phonetic": (row.get("phonetic") or "").strip(),
                "partsOfSpeech": parse_pos(row.get("pos")),
                "definitionsEn": split_lines(row.get("definition")),
                "meaningsZh": split_lines(row.get("translation")),
                "examTags": parse_tags(row.get("tag")),
                "frequency": {"bnc": parse_int(row.get("bnc")), "modern": parse_int(row.get("frq"))},
                "forms": parse_exchange(row.get("exchange")),
                "source": {"dataset": "ECDICT", "sourceTag": config["sourceTag"]},
            }
            entries.append(entry)

    entries.sort(key=frequency_key)
    if limit:
        entries = entries[:limit]
    return {
        "schemaVersion": 1,
        "deck": {"id": exam, "name": config["name"], "sourceTag": config["sourceTag"], "entryCount": len(entries)},
        "entries": entries,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path, help="Path to ECDICT CSV")
    parser.add_argument("--exam", required=True, choices=["cet6", "kaoyan", "ielts"])
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config") / "exams.json")
    parser.add_argument("--limit", type=int, default=None, help="Optional trial batch size")
    args = parser.parse_args()
    data = extract(args.input, args.exam, args.config, args.limit)
    write_json(args.output, data)
    print(f"Wrote {data['deck']['entryCount']} entries to {args.output}")


if __name__ == "__main__":
    main()
