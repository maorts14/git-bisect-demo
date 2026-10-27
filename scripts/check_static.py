#!/usr/bin/env python3
"""Dependency-free fast checks intended for every commit."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FEATURES = ROOT / "app" / "features.json"


def main() -> None:
    data = json.loads(FEATURES.read_text(encoding="utf-8"))
    features = data.get("features")
    if not isinstance(features, dict):
        raise SystemExit("app/features.json must contain a features object")
    if not all(isinstance(name, str) and isinstance(enabled, bool) for name, enabled in features.items()):
        raise SystemExit("each feature must be a string mapped to true or false")
    print("fast static checks passed")


if __name__ == "__main__":
    main()
