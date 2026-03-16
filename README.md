# JAPER Technology Developer Resources

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI](https://img.shields.io/badge/Assisted-Development-2b2bff?logo=openai&logoColor=white)](https://www.japer.technology)

This repository augments [developer.japer.io](https://developer.japer.io) for Git-centric users who want JAPER Technology documentation in a versioned, reviewable, automation-friendly format.

It provides a lightweight workflow to:
- fetch the latest JAPER API collection from `developer.japer.io`
- store the source collection as JSON in `docs/japer_api_collection.json`
- generate a Git-friendly endpoint index in `docs/ENDPOINTS.md`
- track refresh history in `docs/UPDATE_LOG.md`

## Primary resources

- [Developer portal](https://developer.japer.io) - official API docs and integration guides
- [Endpoint reference](docs/ENDPOINTS.md) - generated Markdown tables for service status, device management, customer validation, encryption, and decryption APIs
- [API collection snapshot](docs/japer_api_collection.json) - fetched source data used to generate the endpoint reference
- [Update log](docs/UPDATE_LOG.md) - timestamped record of documentation refreshes

## Why this repository exists

`developer.japer.io` is the source of truth, while this repository makes the same information easier to consume through normal Git workflows:
- review changes in pull requests
- diff API documentation over time
- pin snapshots in automation pipelines
- browse endpoint summaries directly from GitHub

## Repository layout

- `scripts/fetch_api_docs.py` - downloads the latest JAPER API collection
- `scripts/generate_endpoints_md.py` - converts the collection into Markdown tables
- `scripts/update_docs.sh` - runs the full refresh pipeline and appends to the update log
- `docs/ENDPOINTS.md` - generated endpoint reference
- `docs/japer_api_collection.json` - fetched API collection snapshot
- `docs/UPDATE_LOG.md` - update history
- `tests/` - validation for the documentation tooling

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Refresh the docs

Run the full update flow:

```bash
bash scripts/update_docs.sh
```

Or run the steps individually:

```bash
python scripts/fetch_api_docs.py
python scripts/generate_endpoints_md.py
```

## What gets generated

After a refresh:
- `docs/japer_api_collection.json` contains the latest fetched collection
- `docs/ENDPOINTS.md` contains a readable Markdown endpoint summary
- `docs/UPDATE_LOG.md` receives a new UTC timestamp entry

## Contact

- Eric Mourant - eric.mourant@japer.technology
