# Aurora routine workspace

This repository is a sandbox for building and testing routines with the
[Aurora framework](https://aurorabot.app/). It ships with a mirrored copy of the
public documentation so you can reference the APIs while you work, but the
project itself is focused on code rather than documentation scraping.

## Repository layout

The important top-level directories are:

| Path | Purpose |
| ---- | ------- |
| `scripts/AuroraRoutines/` | Sample routines, load order metadata, and other runtime helpers. |
| `scripts/download_aurora_docs.py` | Utility script for refreshing the offline documentation mirror. |
| `data/` | Input data used by tooling (for example the curated best practices path list). |
| `docs/` | Markdown notes maintained alongside the codebase, including best practices and the changelog. |
| `offline-docs/` | Static HTML export of the official Aurora documentation kept for quick reference. |

## Working with the offline docs

The mirrored site lives under `offline-docs/`. The HTML was captured directly
from the live documentation and assumes it is served from the web root. To
browse it locally you can point a tiny HTTP server at the directory:

```bash
python3 -m http.server --directory offline-docs 9000
```

and then open <http://localhost:9000/> in your browser.

To update the mirror, run the downloader script from a machine with internet
access:

```bash
python3 scripts/download_aurora_docs.py offline-docs
```

The script prints every fetched URL as it runs, making it straightforward to
spot missing pages or assets. Pass `--format markdown` if you want to refresh
the Markdown notes under `docs/best-practices/` instead.
