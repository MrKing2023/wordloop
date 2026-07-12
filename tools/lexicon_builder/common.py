from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


def split_lines(value: str | None) -> list[str]:
    if not value:
        return []
    return [line.strip() for line in re.split(r"[\r\n]+", value) if line.strip()]


def parse_int(value: str | None) -> int | None:
    try:
        number = int(str(value).strip())
        return number if number > 0 else None
    except (TypeError, ValueError):
        return None


def parse_tags(value: str | None) -> list[str]:
    return sorted(set(str(value or "").lower().split()))


def parse_pos(value: str | None) -> list[str]:
    result: list[str] = []
    for part in str(value or "").split("/"):
        key = part.split(":", 1)[0].strip()
        if key and key not in result:
            result.append(key)
    return result


def parse_exchange(value: str | None) -> dict[str, str]:
    result: dict[str, str] = {}
    for part in str(value or "").split("/"):
        if ":" not in part:
            continue
        key, item = part.split(":", 1)
        key, item = key.strip(), item.strip()
        if key and item:
            result[key] = item
    return result


def word_id(word: str) -> str:
    normalized = re.sub(r"[^a-z0-9'-]+", "-", word.strip().lower())
    return normalized.strip("-")


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
