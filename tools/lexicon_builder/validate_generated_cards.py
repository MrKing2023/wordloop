#!/usr/bin/env python3
"""Validate generated WordLoop learning cards before publication."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import write_json


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", str(text or "").strip().lower())


def validate_card(card: dict, index: int) -> list[dict]:
    issues: list[dict] = []
    required = ["word", "sentenceEn", "sentenceZh", "clozeAnswer", "acceptedAnswers"]
    for field in required:
        if not card.get(field):
            issues.append({"index": index, "word": card.get("word"), "severity": "error", "message": f"missing {field}"})
    sentence = normalize(card.get("sentenceEn", ""))
    answer = normalize(card.get("clozeAnswer", ""))
    if answer and sentence.count(answer) != 1:
        issues.append({"index": index, "word": card.get("word"), "severity": "error", "message": "cloze answer must appear exactly once in sentenceEn"})
    accepted = [normalize(x) for x in card.get("acceptedAnswers", [])]
    if answer and answer not in accepted:
        issues.append({"index": index, "word": card.get("word"), "severity": "error", "message": "acceptedAnswers does not include clozeAnswer"})
    if len(sentence.split()) > 28:
        issues.append({"index": index, "word": card.get("word"), "severity": "warning", "message": "sentence is longer than 28 words"})
    if not re.search(r"[。！？]$", str(card.get("sentenceZh", "")).strip()):
        issues.append({"index": index, "word": card.get("word"), "severity": "warning", "message": "Chinese translation has no ending punctuation"})
    return issues


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    cards = data.get("cards", data if isinstance(data, list) else [])
    issues = [issue for i, card in enumerate(cards) for issue in validate_card(card, i)]
    report = {
        "valid": not any(x["severity"] == "error" for x in issues),
        "stats": {"cards": len(cards), "errors": sum(x["severity"] == "error" for x in issues), "warnings": sum(x["severity"] == "warning" for x in issues)},
        "issues": issues,
    }
    write_json(args.report, report)
    print(json.dumps(report["stats"], ensure_ascii=False))
    raise SystemExit(0 if report["valid"] else 1)


if __name__ == "__main__":
    main()
