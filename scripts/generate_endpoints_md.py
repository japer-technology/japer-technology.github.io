#!/usr/bin/env python3
"""Generate Markdown table of API endpoints from Postman collection."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parents[1]
COLLECTION_PATH = REPO_ROOT / "docs" / "japer_api_collection.json"
OUTPUT_PATH = REPO_ROOT / "docs" / "ENDPOINTS.md"

CATEGORY_MAP = {
    "Ping": "Service Status",
    "Devices": "Device Management",
    "Validations": "Customer Validation",
    "Encryptions": "Data Encryption",
    "Decryptions": "Data Decryption",
}

CATEGORY_ORDER = [
    "Service Status",
    "Device Management",
    "Customer Validation",
    "Data Encryption",
    "Data Decryption",
]


def traverse(items, lineage):
    for item in items:
        name = item.get("name", "")
        if "request" in item:
            yield lineage + [name], item
        if "item" in item:
            yield from traverse(item["item"], lineage + [name])


def main() -> int:
    with COLLECTION_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    endpoints: dict[str, list[tuple[str, str, str, str]]] = {v: [] for v in CATEGORY_MAP.values()}

    for path, item in traverse(data.get("item", []), []):
        if not path:
            continue
        top = path[0]
        category = CATEGORY_MAP.get(top)
        if not category:
            continue
        req = item["request"]
        method = req.get("method", "")
        raw_url = req.get("url", "")
        parsed = urlparse(raw_url)
        path_str = parsed.path
        name = item.get("name", "")
        postman_id = item.get("_postman_id", "")
        link = f"https://developer.japer.io#{postman_id}" if postman_id else ""
        endpoints[category].append((name, method, path_str, link))

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        f.write("# API Endpoints\n\n")
        for category in CATEGORY_ORDER:
            rows = endpoints.get(category)
            if not rows:
                continue
            f.write(f"## {category}\n\n")
            f.write("| Endpoint | Method | Path | Docs |\n")
            f.write("| --- | --- | --- | --- |\n")
            for name, method, path_str, link in rows:
                f.write(f"| {name} | {method} | `{path_str}` | [link]({link}) |\n")
            f.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
