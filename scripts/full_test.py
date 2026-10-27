#!/usr/bin/env python3
"""Deliberately small expensive-test stand-in for the batch-CI demo."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    data = json.loads(Path("app/features.json").read_text(encoding="utf-8"))
    forbidden = data["features"].get("broken_feature")
    if forbidden is True:
        print("FULL CI FAILED: broken_feature must never be enabled")
        return 1
    print("full integration suite passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
