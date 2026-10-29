"""Helpers for loading the mock JSON datasets that ship with the project."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_json(filename):
    """Load a JSON file from the project's ``data/`` folder.

    The path is resolved relative to this file, so it works no matter which
    directory the app is started from.
    """
    with open(DATA_DIR / filename, encoding="utf-8") as f:
        return json.load(f)
