# Aurora best practice documentation bundle

This directory is intended to store a Markdown export of the Aurora framework
best practice guides. The repository already includes a complete HTML mirror of
the public documentation under `offline-docs/`, so you can browse the content
immediately. Use this folder when you want a Markdown version that can be
annotated alongside the codebase.

Use the downloader script to mirror the curated set of pages listed in
`data/best_practices_paths.txt` into this folder:

```bash
python3 scripts/download_aurora_docs.py docs/best-practices \
  --format markdown \
  --paths-file data/best_practices_paths.txt \
  --no-follow
```

The `--format markdown` flag converts each documentation page to Markdown so it
can be committed and annotated alongside source code. The `--no-follow` option
keeps the crawler focused on the provided list instead of traversing the entire
site, while still downloading images that are embedded in the selected pages.

Feel free to update `data/best_practices_paths.txt` with additional sections as
your project grows. Once the command finishes you can review the generated
Markdown and commit it to version control.
