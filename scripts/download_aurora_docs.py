#!/usr/bin/env python3
"""Download the Aurora framework documentation site for offline use.

The sandbox used to evaluate this repository has no outbound network access,
so the script cannot be executed during automated tests. Run it on a local
machine (or any environment with internet access) to mirror
``https://docs.aurora-wow.wtf`` and keep an offline copy of the HTML pages and
static assets.
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, urljoin, urlsplit, urlunsplit
from urllib.request import Request, urlopen

USER_AGENT = "aur-doc-downloader/1.0 (+https://docs.aurora-wow.wtf/)"


class LinkExtractor(HTMLParser):
    """Extract href and src attributes from HTML documents."""

    def __init__(self) -> None:
        super().__init__()
        self.links: set[tuple[str, str]] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attribute_names = {"a": "href", "link": "href", "script": "src", "img": "src"}
        attr_name = attribute_names.get(tag)
        if not attr_name:
            return
        for name, value in attrs:
            if name == attr_name and value:
                self.links.add((value, tag))


SAFE_PATH_CHARS = "/:@!$&'()*+,;=-._~%"


def normalize_path(path: str) -> str:
    """Percent-encode a URL path while keeping already-encoded segments intact."""

    # ``quote`` leaves existing ``%xx`` sequences untouched when ``%`` is marked as safe.
    return quote(path or "/", safe=SAFE_PATH_CHARS)


def resolve_candidate(base_url: str, base_netloc: str, candidate: str) -> str | None:
    """Return a normalized absolute URL within the documentation host."""

    absolute = urljoin(base_url, candidate)
    parsed = urlsplit(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc != base_netloc:
        return None
    normalized_path = normalize_path(parsed.path)
    normalized = urlunsplit((parsed.scheme, parsed.netloc, normalized_path, "", ""))
    return normalized


def url_to_path(
    output_dir: Path,
    url: str,
    base_netloc: str,
    output_format: str,
    content_type: str,
) -> Path:
    """Translate a URL into a path within the output directory."""

    parsed = urlsplit(url)
    if parsed.netloc != base_netloc:
        raise ValueError(f"Unexpected host: {parsed.netloc}")

    path = normalize_path(parsed.path)
    if not path or path.endswith("/"):
        suffix = ".md" if output_format == "markdown" and should_parse_html(content_type) else ".html"
        relative = Path(path.lstrip("/")) / f"index{suffix}"
    else:
        relative = Path(path.lstrip("/"))
        if relative.suffix == "":
            suffix = ".md" if output_format == "markdown" and should_parse_html(content_type) else ".html"
            relative = relative / f"index{suffix}"
        elif output_format == "markdown" and should_parse_html(content_type):
            relative = relative.with_suffix(".md")

    return output_dir / relative


def fetch(url: str, referer: str | None) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    if referer:
        request.add_header("Referer", referer)
    with urlopen(request) as response:
        content_type = response.headers.get("Content-Type", "application/octet-stream")
        data = response.read()
        return data, content_type


def should_parse_html(content_type: str) -> bool:
    return content_type.split(";", 1)[0].strip().lower() == "text/html"


@dataclass
class CrawlItem:
    url: str
    referer: str | None


class MarkdownConverter(HTMLParser):
    """Convert HTML fragments into a lightly formatted Markdown string."""

    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.trailing_newlines = 0
        self.list_stack: list[dict[str, int | str]] = []
        self.anchor_stack: list[dict[str, str | bool | int]] = []
        self.skip_depth = 0
        self.in_code_block = False
        self.inline_code = 0

    def _refresh_trailing_newlines(self) -> None:
        if not self.parts:
            self.trailing_newlines = 0
            return
        last = self.parts[-1]
        if last.endswith("\n"):
            self.trailing_newlines = len(last) - len(last.rstrip("\n"))
        else:
            self.trailing_newlines = 0

    def write(self, text: str) -> None:
        if not text:
            return
        self.parts.append(text)
        if text.endswith("\n"):
            self.trailing_newlines = len(text) - len(text.rstrip("\n"))
        else:
            self.trailing_newlines = 0

    def ensure_newlines(self, count: int) -> None:
        if not self.parts or count == 0:
            return
        if self.trailing_newlines >= count:
            return
        needed = count - self.trailing_newlines
        self.parts.append("\n" * needed)
        self.trailing_newlines = count

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v for k, v in attrs}
        if tag in {"script", "style"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        if tag in {"p", "section", "article", "div"}:
            self.ensure_newlines(2)
        elif tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            level = int(tag[1])
            level = max(1, min(level, 6))
            self.ensure_newlines(2)
            self.write("#" * level + " ")
        elif tag == "br":
            self.write("  \n")
        elif tag in {"strong", "b"}:
            self.write("**")
        elif tag in {"em", "i"}:
            self.write("*")
        elif tag == "code":
            if self.in_code_block:
                return
            self.inline_code += 1
            self.write("`")
        elif tag == "pre":
            self.ensure_newlines(2)
            self.write("```\n")
            self.in_code_block = True
        elif tag == "ul":
            self.ensure_newlines(2)
            self.list_stack.append({"type": "ul", "index": 0})
        elif tag == "ol":
            self.ensure_newlines(2)
            self.list_stack.append({"type": "ol", "index": 0})
        elif tag == "li":
            if self.list_stack:
                self.ensure_newlines(1)
                indent = "  " * (len(self.list_stack) - 1)
                current = self.list_stack[-1]
                if current["type"] == "ol":
                    current["index"] = int(current.get("index", 0)) + 1
                    prefix = f"{current['index']}. "
                else:
                    prefix = "- "
                self.write(indent + prefix)
        elif tag == "a":
            href = attrs_dict.get("href", "") or ""
            start_index = len(self.parts)
            self.anchor_stack.append({"href": href, "has_text": False, "index": start_index})
            self.write("[")
        elif tag == "img":
            alt = attrs_dict.get("alt", "") or ""
            src = attrs_dict.get("src", "") or ""
            self.write(f"![{alt}]({src})")
            if self.anchor_stack:
                self.anchor_stack[-1]["has_text"] = True
        elif tag == "blockquote":
            self.ensure_newlines(2)
            self.write("> ")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"}:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag in {"p", "section", "article", "div"}:
            self.ensure_newlines(2)
        elif tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            self.ensure_newlines(2)
        elif tag in {"strong", "b"}:
            self.write("**")
        elif tag in {"em", "i"}:
            self.write("*")
        elif tag == "code":
            if self.in_code_block:
                return
            if self.inline_code:
                self.write("`")
                self.inline_code = max(self.inline_code - 1, 0)
        elif tag == "pre":
            if self.in_code_block:
                self.ensure_newlines(1)
                self.write("```\n")
                self.ensure_newlines(2)
                self.in_code_block = False
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.ensure_newlines(2)
        elif tag == "li":
            self.ensure_newlines(1)
        elif tag == "a":
            if not self.anchor_stack:
                return
            anchor = self.anchor_stack.pop()
            href = anchor.get("href", "")
            if anchor.get("has_text"):
                self.write(f"]({href})")
            else:
                start_index = int(anchor.get("index", len(self.parts)))
                if start_index < len(self.parts):
                    self.parts = self.parts[:start_index]
                    self._refresh_trailing_newlines()
                self.write(f"<{href}>")
        elif tag == "blockquote":
            self.ensure_newlines(2)

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if not data:
            return
        if self.in_code_block or self.inline_code:
            text = data
        else:
            text = re.sub(r"\s+", " ", data)
        text = unescape(text)
        if not self.in_code_block and not self.inline_code:
            text = text.replace("\xa0", " ")
        if self.anchor_stack and text.strip():
            self.anchor_stack[-1]["has_text"] = True
        self.write(text)

    def handle_entityref(self, name: str) -> None:
        self.handle_data(unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        if name.startswith("x"):
            value = chr(int(name[1:], 16))
        else:
            value = chr(int(name))
        self.handle_data(value)

    def get_markdown(self) -> str:
        content = "".join(self.parts)
        return content.strip("\n") + "\n"


def extract_title(html: str) -> str | None:
    match = re.search(r"<title>(.*?)</title>", html, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    title = unescape(match.group(1)).strip()
    return re.sub(r"\s+\|.*", "", title).strip() or None


def html_to_markdown(source_url: str, html: str) -> str:
    converter = MarkdownConverter()
    converter.feed(html)
    converter.close()
    body = converter.get_markdown()
    title = extract_title(html)
    timestamp = datetime.now(timezone.utc).isoformat()
    front_matter = ["---"]
    if title:
        front_matter.append(f"title: {title}")
    front_matter.append(f"source: {source_url}")
    front_matter.append(f"downloaded: {timestamp}")
    front_matter.append("---\n")
    return "\n".join(front_matter) + body


def load_seed_paths(path: Path | None) -> list[str]:
    if path is None:
        return []
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        lines.append(stripped)
    return lines


def crawl(
    base_url: str,
    output_dir: Path,
    output_format: str,
    seeds: Iterable[str] | None = None,
    follow_links: bool = True,
) -> None:
    parsed_base = urlsplit(base_url)
    if parsed_base.scheme not in {"http", "https"}:
        raise ValueError("Only HTTP and HTTPS URLs are supported")

    base_netloc = parsed_base.netloc
    normalized_start = urlunsplit((parsed_base.scheme, parsed_base.netloc, parsed_base.path or "/", "", ""))

    queue: collections.deque[CrawlItem] = collections.deque()
    initial_seeds = list(seeds or [])
    if initial_seeds:
        for entry in initial_seeds:
            candidate = resolve_candidate(normalized_start, base_netloc, entry)
            if candidate:
                queue.append(CrawlItem(candidate, None))
    else:
        queue.append(CrawlItem(normalized_start, None))
    seen: set[str] = set()

    while queue:
        item = queue.popleft()
        if item.url in seen:
            continue
        seen.add(item.url)

        try:
            data, content_type = fetch(item.url, item.referer)
        except Exception as exc:  # pragma: no cover - depends on external network
            print(f"Failed to fetch {item.url}: {exc}", file=sys.stderr)
            continue

        target_path = url_to_path(output_dir, item.url, base_netloc, output_format, content_type)
        target_path.parent.mkdir(parents=True, exist_ok=True)
        if output_format == "markdown" and should_parse_html(content_type):
            html = data.decode("utf-8", errors="ignore")
            markdown = html_to_markdown(item.url, html)
            target_path.write_text(markdown, encoding="utf-8")
        else:
            target_path.write_bytes(data)
        print(f"Saved {item.url} -> {target_path.relative_to(output_dir)}")

        if should_parse_html(content_type):
            parser = LinkExtractor()
            try:
                parser.feed(data.decode("utf-8", errors="ignore"))
            except Exception as exc:  # pragma: no cover - parser errors depend on content
                print(f"Failed to parse HTML from {item.url}: {exc}", file=sys.stderr)
                continue

            for link, tag in parser.links:
                candidate = resolve_candidate(item.url, base_netloc, link)
                if not candidate or candidate in seen:
                    continue
                if output_format == "markdown" and tag in {"link", "script"}:
                    continue
                if not follow_links and tag == "a":
                    continue
                queue.append(CrawlItem(candidate, item.url))


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download the Aurora documentation for offline viewing")
    parser.add_argument("output", nargs="?", default="offline-docs", help="Directory to store the downloaded files")
    parser.add_argument("--base-url", default="https://docs.aurora-wow.wtf/", help="Root documentation URL to crawl")
    parser.add_argument("--format", choices=["html", "markdown"], default="html", help="Format used to save HTML documents")
    parser.add_argument("--paths-file", help="File that lists documentation paths to download (one per line)")
    parser.add_argument("--no-follow", action="store_true", help="Do not crawl hyperlinks beyond the provided seed paths")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    seeds: list[str] | None = None
    if args.paths_file:
        seeds = load_seed_paths(Path(args.paths_file).expanduser())

    try:
        crawl(
            args.base_url,
            output_dir,
            args.format,
            seeds=seeds,
            follow_links=not args.no_follow,
        )
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
