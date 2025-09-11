"""Fetch Japer API collection and save to docs.

Usage:
    python scripts/fetch_api_docs.py

The script retrieves the latest API collection from the Japer developer
endpoint and stores the JSON response at ``docs/japer_api_collection.json``.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import requests

URL = "https://developer.japer.io/api/collections/5724568/S1Zw8qoK?segregateAuth=true&versionTag=latest"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "docs" / "japer_api_collection.json"

# Expected top-level categories in the Postman collection.
EXPECTED_CATEGORIES: set[str] = {
    "Ping",
    "Devices",
    "Encryptions",
    "Decryptions",
    "Validations",
}


def validate_categories(data: dict, expected: set[str] = EXPECTED_CATEGORIES) -> None:
    """Ensure all expected categories are present in the collection.

    Parameters
    ----------
    data:
        Parsed JSON of the Postman collection.
    expected:
        Names of categories expected at the top level of the collection.

    Raises
    ------
    ValueError
        If any expected categories are missing.
    """

    available = {item.get("name") for item in data.get("item", [])}
    missing = sorted(expected - available)
    if missing:
        raise ValueError(
            "Missing categories in API collection: " + ", ".join(missing)
        )


def main() -> int:
    print(f"requests version: {requests.__version__}")
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        print(f"HTTP request failed: {exc}", file=sys.stderr)
        return 1

    try:
        data = response.json()
    except ValueError as exc:
        print(f"Failed to parse JSON: {exc}", file=sys.stderr)
        return 1

    try:
        validate_categories(data)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
