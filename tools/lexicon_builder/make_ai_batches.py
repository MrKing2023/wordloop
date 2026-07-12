#!/usr/bin/env python3
"""Create JSONL batches for controlled AI learning-card generation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def compact_entry(entry: dict) -> dict:
    return {
        "id": entry.get("id"),
        "word": entry.get("word"),
        "phonetic": entry.get("phonetic"),
        "partsOfSpeech": entry.get("partsOfSpeech", []),
        "meaningsZh": entry.get("meaningsZh", [])[:4],
        "definitionsEn": entry.get("definitionsEn", [])[:4],
        "examTags": entry.get("examTags", []),
        "forms": entry.get("forms", {}),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--prompt-version", default="wordloop-card-v1")
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for offset in range(0, len(entries), args.batch_size):
            batch = entries[offset:offset + args.batch_size]
            payload = {
                "batchId": f"{data.get('deck', {}).get('id', 'deck')}-{offset // args.batch_size + 1:04d}",
                "promptVersion": args.prompt_version,
                "task": "Generate multiple candidate learning cards per sense. Return strict JSON only.",
                "qualityRules": [
                    "Use only the supplied sense",
                    "Generate 4-6 candidate English sentences",
                    "Translate the selected sentence separately into Chinese",
                    "Prefer a constrained collocation suitable for cloze",
                    "List plausible alternative answers",
                    "Mark low-uniqueness items for translation mode",
                ],
                "entries": [compact_entry(x) for x in batch],
            }
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    print(f"Wrote {(len(entries) + args.batch_size - 1) // args.batch_size} batches to {args.output}")


if __name__ == "__main__":
    main()
