#!/usr/bin/env python3
"""Validate a WordLoop base lexicon JSON file."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import write_json


def validate(data: dict) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    entries = data.get("entries")
    if not isinstance(entries, list):
        return {"valid": False, "errors": [{"message": "entries must be a list"}], "warnings": [], "stats": {}}

    ids: set[str] = set()
    words: set[str] = set()
    for index, entry in enumerate(entries):
        location = {"index": index, "id": entry.get("id"), "word": entry.get("word")}
        for field in ("id", "word", "examTags"):
            if not entry.get(field):
                errors.append({**location, "message": f"missing required field: {field}"})
        if entry.get("id") in ids:
            errors.append({**location, "message": "duplicate id"})
        ids.add(entry.get("id"))
        normalized_word = str(entry.get("word") or "").lower()
        if normalized_word in words:
            warnings.append({**location, "message": "duplicate word ignoring case"})
        words.add(normalized_word)
        if not entry.get("phonetic"):
            warnings.append({**location, "message": "missing phonetic"})
        if not entry.get("meaningsZh"):
            warnings.append({**location, "message": "missing Chinese meaning"})
        if not entry.get("definitionsEn"):
            warnings.append({**location, "message": "missing English definition"})

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "stats": {"entries": len(entries), "errors": len(errors), "warnings": len(warnings)},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    report = validate(data)
    if args.report:
        write_json(args.report, report)
    print(json.dumps(report["stats"], ensure_ascii=False))
    raise SystemExit(0 if report["valid"] else 1)


if __name__ == "__main__":
    main()
