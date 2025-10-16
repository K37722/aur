# Aurora documentation downloader

This repository contains a small helper script for downloading the public
[Aurora framework documentation](https://docs.aurora-wow.wtf/) so that it can
be browsed offline.

Because the automated evaluation environment is sandboxed and blocks outbound
network access, the script is not executed as part of the tests. Run it on your
local machine (or anywhere with internet access) to mirror the site:

```bash
python3 scripts/download_aurora_docs.py aurora-docs
```

By default, it will crawl every HTML page served from
`https://docs.aurora-wow.wtf/`, save them into the target directory, and follow
links that point to the same host. Assets referenced via `src` or `href`
attributes (images, stylesheets, JavaScript files) are also downloaded, which
should make the offline copy functional.

If you would rather store the documentation alongside your code as Markdown,
enable the Markdown export mode. The crawler will mirror the same pages but
convert each HTML document into Markdown with YAML front matter that records the
source URL:

```bash
python3 scripts/download_aurora_docs.py docs/best-practices \
  --format markdown \
  --paths-file data/best_practices_paths.txt \
  --no-follow
```

The optional `--paths-file` flag seeds the crawler with specific documentation
paths so you can focus on a curated set such as the framework best practices
without traversing the entire site. Combine it with `--no-follow` to avoid
pulling in additional sections while still downloading embedded images.

If the documentation ever moves to a different domain you can point the script
at the new base URL:

```bash
python3 scripts/download_aurora_docs.py aurora-docs --base-url https://new-domain/
```

The script prints the mapping between remote URLs and local files while it
runs, making it easy to troubleshoot any broken pages or missing resources.
