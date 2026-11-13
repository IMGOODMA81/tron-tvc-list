#!/usr/bin/env python3
"""Validate tokenlist.json against tokenlist.schema.json.

Usage:
    pip install jsonschema
    python scripts/validate_tokenlist.py [path/to/tokenlist.json]

Every entry is checked individually, so errors name the entry and the field.
The file may hold a single token entry, an array of entries, or an object whose
"tokens" array holds the entries. Exits 0 when every entry is valid, 1 when
validation fails, and 2 when a file cannot be read or parsed.
"""

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "tokenlist.schema.json"
DEFAULT_LIST_PATH = REPO_ROOT / "tokenlist.json"


def labelled_entries(document):
    """Each token entry paired with the path that locates it in the document."""
    if isinstance(document, list):
        return [("[{}]".format(index), entry) for index, entry in enumerate(document)]
    if isinstance(document, dict) and isinstance(document.get("tokens"), list):
        return [
            ("tokens[{}]".format(index), entry)
            for index, entry in enumerate(document["tokens"])
        ]
    return [("(root)", document)]


def duplicate_addresses(entries):
    """Addresses that appear more than once, compared case-insensitively."""
    seen = set()
    duplicates = []
    for _, entry in entries:
        address = entry.get("address") if isinstance(entry, dict) else None
        if not isinstance(address, str) or not address.strip():
            continue
        key = address.lower()
        if key in seen and address not in duplicates:
            duplicates.append(address)
        seen.add(key)
    return duplicates


def read_json(path, label):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("error: {} not found at {}".format(label, path), file=sys.stderr)
    except json.JSONDecodeError as error:
        print("error: {} is not valid JSON: {}".format(label, error), file=sys.stderr)
    return None


def main(argv):
    list_path = Path(argv[1]).resolve() if len(argv) > 1 else DEFAULT_LIST_PATH

    schema = read_json(SCHEMA_PATH, "schema")
    document = read_json(list_path, "token list")
    if schema is None or document is None:
        return 2

    validator = Draft202012Validator(schema)
    entries = labelled_entries(document)
    duplicates = duplicate_addresses(entries)

    problems = []
    for label, entry in entries:
        errors = sorted(
            validator.iter_errors(entry),
            key=lambda error: [str(part) for part in error.absolute_path],
        )
        for error in errors:
            field_path = "/".join(str(part) for part in error.absolute_path)
            location = "{}.{}".format(label, field_path) if field_path else label
            problems.append("{}: {}".format(location, error.message))
    problems.extend("duplicate address: {}".format(address) for address in duplicates)

    if not problems:
        print("{}: {} token {} valid".format(
            list_path.name,
            len(entries),
            "entry" if len(entries) == 1 else "entries",
        ))
        return 0

    for problem in problems:
        print("{}: {}".format(list_path.name, problem), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
