#!/usr/bin/env python3
# MIT License
# 
# Copyright (c) 2025 Japer Technology Pty. Ltd.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Generate Markdown table of API endpoints from Postman collection."""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse
import sys


def load_collection(path: Path) -> dict:
    """Load JSON file ignoring leading comment block."""
    content = path.read_text(encoding="utf-8")
    if content.lstrip().startswith("/*"):
        end = content.find("*/")
        if end != -1:
            content = content[end + 2:]
    return json.loads(content)


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


def get_raw_url(req: dict, item_name: str) -> str | None:
    """Return the raw URL from a Postman request object.

    Handles both string and dict formats for the ``url`` field. If the field
    is a dict, the ``raw`` value is extracted. When no usable URL is found a
    warning is emitted and ``None`` is returned.
    """

    url_field = req.get("url")
    if isinstance(url_field, dict):
        raw = url_field.get("raw")
        if raw:
            return raw
        print(f"Warning: '{item_name}' missing raw URL; skipping", file=sys.stderr)
        return None
    if isinstance(url_field, str):
        return url_field
    print(f"Warning: '{item_name}' missing URL; skipping", file=sys.stderr)
    return None


def main() -> int:
    data = load_collection(COLLECTION_PATH)
    endpoints: dict[str, list[tuple[str, str, str, str]]] = {v: [] for v in CATEGORY_MAP.values()}

    for path, item in traverse(data.get("item", []), []):
        if not path:
            continue
        top = path[0]
        category = CATEGORY_MAP.get(top)
        if not category:
            continue
        req = item["request"]
        name = item.get("name", "")
        method = req.get("method", "")
        raw_url = get_raw_url(req, name)
        if not raw_url:
            continue
        parsed = urlparse(raw_url)
        path_str = parsed.path
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
