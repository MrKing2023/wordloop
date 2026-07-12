#!/usr/bin/env python3
"""Validate WordLoop v4.2 exam-library release files."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUBLIC = ROOT / "public"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_lexicon(path: Path, expected: int, required_tag: str) -> set[str]:
    data = load(path)
    entries = data.get("entries", [])
    assert data.get("entryCount") == expected == len(entries), (path, len(entries))
    ids = [entry.get("id") for entry in entries]
    words = [str(entry.get("word", "")).lower() for entry in entries]
    assert not [key for key, count in Counter(ids).items() if count > 1]
    assert not [key for key, count in Counter(words).items() if count > 1]
    for entry in entries:
        assert entry.get("id") and entry.get("word")
        assert required_tag in entry.get("examTags", [])
        assert isinstance(entry.get("meaningsZh", []), list)
    return set(words)


def validate_cards(path: Path, expected: int, library_id: str, lexicon_words: set[str]) -> None:
    data = load(path)
    cards = data.get("cards", [])
    assert data.get("cardCount") == expected == len(cards), (path, len(cards))
    ids = [card.get("id") for card in cards]
    words = [str(card.get("word", "")).lower() for card in cards]
    sentences = [card.get("sentenceEn") for card in cards]
    assert not [key for key, count in Counter(ids).items() if count > 1]
    assert not [key for key, count in Counter(words).items() if count > 1]
    assert not [key for key, count in Counter(sentences).items() if count > 1]
    required = [
        "word", "pronunciation", "partOfSpeech", "meaningZh", "sentenceEn",
        "sentenceZh", "clozeAnswer", "usageNotes", "collocations",
        "relatedExpressions", "wordFamily", "extraExamples",
    ]
    for card in cards:
        assert card.get("libraryId") == library_id
        assert card.get("word", "").lower() in lexicon_words
        for key in required:
            assert card.get(key), (card.get("word"), key)
        assert card["clozePrefix"] + card["clozeAnswer"] + card["clozeSuffix"] == card["sentenceEn"]
        assert card["clozeAnswer"] in card["acceptedAnswers"]
        assert len(card["collocations"]) >= 3
        assert len(card["relatedExpressions"]) >= 2
        assert len(card["extraExamples"]) >= 1
        assert card.get("quality", {}).get("reviewStatus") == "curated"


def main() -> None:
    cet6_words = validate_lexicon(PUBLIC / "data/cet6/cet6_lexicon.json", 5407, "cet6")
    validate_cards(PUBLIC / "data/cet6/cet6_cards_100.json", 100, "cet6", cet6_words)
    kaoyan_words = validate_lexicon(PUBLIC / "data/kaoyan/kaoyan_lexicon.json", 4112, "ky")
    validate_cards(PUBLIC / "data/kaoyan/kaoyan_cards_100.json", 100, "kaoyan", kaoyan_words)
    manifest = load(PUBLIC / "data/library_manifest.json")
    by_id = {item["id"]: item for item in manifest["libraries"]}
    assert by_id["cet6"]["status"] == "ready" and by_id["cet6"]["cardCount"] == 100
    assert by_id["kaoyan"]["status"] == "ready"
    assert by_id["kaoyan"]["baseEntryCount"] == 4112
    assert by_id["kaoyan"]["cardCount"] == 100
    print("WordLoop v4.2 release validation passed")
    print("CET-6: 5407 base entries + 100 curated cards")
    print("Kaoyan: 4112 core entries + 100 curated cards")


if __name__ == "__main__":
    main()
