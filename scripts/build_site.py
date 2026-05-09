#!/usr/bin/env python3
"""Build the Markdown curriculum into a small static site."""

from __future__ import annotations

import argparse
import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
ASSET_SOURCE = ROOT / "scripts" / "site_assets"
WEEK_FILE_ORDER = [
    "README.md",
    "science.md",
    "keywords.md",
    "robotics.md",
    "teacher-notes.md",
    "resources.md",
]


@dataclass(frozen=True)
class SiteItem:
    source: Path
    output: Path
    url: str
    title: str
    group: str
    kind: str


def posix(path: Path) -> str:
    return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def first_heading(path: Path) -> str:
    if path.suffix.lower() == ".pdf":
        return path.stem.replace("-", " ").title()
    for line in read_text(path).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def markdown_output_path(source: Path) -> Path:
    rel = source.relative_to(ROOT)
    if rel.name == "README.md":
        if rel.parent == Path("."):
            return SITE / "index.html"
        return SITE / rel.parent / "index.html"
    return SITE / rel.with_suffix(".html")


def collect_markdown_sources() -> list[Path]:
    paths: list[Path] = []
    seen: set[Path] = set()

    def add(path: Path) -> None:
        if path.exists() and path not in seen:
            paths.append(path)
            seen.add(path)

    add(ROOT / "README.md")
    add(ROOT / "AGENTS.md")

    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        for path in sorted(docs_dir.rglob("*.md")):
            add(path)

    for week_dir in sorted(ROOT.glob("W[0-9][0-9]")):
        for name in WEEK_FILE_ORDER:
            add(week_dir / name)
        for path in sorted(week_dir.glob("*.md")):
            add(path)

    return paths


def group_name(path: Path) -> str:
    rel = path.relative_to(ROOT)
    if len(rel.parts) == 1:
        return "Project"
    if rel.parts[0] == "docs":
        return "Docs"
    if rel.parts[0] == "reference":
        return "Reference"
    if rel.parts[0].startswith("W"):
        readme = ROOT / rel.parts[0] / "README.md"
        return first_heading(readme) if readme.exists() else rel.parts[0]
    return rel.parts[0]


def collect_site_items() -> tuple[list[SiteItem], dict[Path, Path]]:
    md_sources = collect_markdown_sources()
    output_by_source = {path: markdown_output_path(path) for path in md_sources}
    items = [
        SiteItem(
            source=path,
            output=output_by_source[path],
            url=posix(output_by_source[path].relative_to(SITE)),
            title=first_heading(path),
            group=group_name(path),
            kind="markdown",
        )
        for path in md_sources
    ]

    reference_dir = ROOT / "reference"
    if reference_dir.exists():
        for path in sorted(reference_dir.rglob("*")):
            if path.is_file():
                output = SITE / path.relative_to(ROOT)
                items.append(
                    SiteItem(
                        source=path,
                        output=output,
                        url=posix(output.relative_to(SITE)),
                        title=first_heading(path),
                        group="Reference",
                        kind=path.suffix.lower().lstrip(".") or "file",
                    )
                )

    return items, output_by_source


def is_external_url(url: str) -> bool:
    scheme = urlsplit(url).scheme
    return scheme in {"http", "https", "mailto", "tel"}


def make_link_resolver(current_source: Path, current_output: Path, output_by_source: dict[Path, Path]):
    def resolve(url: str) -> str:
        if not url or url.startswith("#") or is_external_url(url):
            return url

        split = urlsplit(url)
        if split.scheme or split.netloc:
            return url

        raw_path = split.path
        if not raw_path:
            return url

        target = (current_source.parent / raw_path).resolve()
        try:
            target.relative_to(ROOT)
        except ValueError:
            return url

        if target in output_by_source:
            destination = output_by_source[target]
        elif target.exists():
            destination = SITE / target.relative_to(ROOT)
        else:
            return url

        rel_url = relpath(destination, current_output.parent)
        return urlunsplit(("", "", rel_url, split.query, split.fragment))

    return resolve


def relpath(target: Path, start: Path) -> str:
    import os

    return Path(os.path.relpath(target, start)).as_posix()


def render_inline(text: str, resolve_link) -> str:
    parts = re.split(r"(`[^`]*`)", text)
    rendered: list[str] = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) >= 2:
            rendered.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue

        escaped = html.escape(part)
        escaped = escaped.replace("&lt;br&gt;", "<br>").replace("&lt;br/&gt;", "<br>").replace("&lt;br /&gt;", "<br>")

        def image(match: re.Match[str]) -> str:
            alt = match.group(1)
            url = resolve_link(html.unescape(match.group(2).strip()))
            return f'<img src="{html.escape(url, quote=True)}" alt="{alt}">'

        def link(match: re.Match[str]) -> str:
            label = match.group(1)
            url = resolve_link(html.unescape(match.group(2).strip()))
            return f'<a href="{html.escape(url, quote=True)}">{label}</a>'

        escaped = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image, escaped)
        escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, escaped)
        escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
        escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
        rendered.append(escaped)

    return "".join(rendered)


def table_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$", line))


def split_table_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def render_table(lines: list[str], resolve_link) -> str:
    header = split_table_row(lines[0])
    body = [split_table_row(line) for line in lines[2:]]
    html_lines = ["<table>", "<thead><tr>"]
    for cell in header:
        html_lines.append(f"<th>{render_inline(cell, resolve_link)}</th>")
    html_lines.append("</tr></thead>")
    html_lines.append("<tbody>")
    for row in body:
        html_lines.append("<tr>")
        for cell in row:
            html_lines.append(f"<td>{render_inline(cell, resolve_link)}</td>")
        html_lines.append("</tr>")
    html_lines.append("</tbody></table>")
    return "\n".join(html_lines)


def special_block_start(line: str, next_line: str | None = None) -> bool:
    stripped = line.strip()
    return bool(
        not stripped
        or stripped.startswith("```")
        or stripped.startswith("#")
        or stripped.startswith(">")
        or re.match(r"^\s*[-*]\s+", line)
        or re.match(r"^\s*\d+\.\s+", line)
        or (stripped.startswith("|") and next_line is not None and table_separator(next_line))
    )


def render_list(lines: list[str], ordered: bool, resolve_link) -> str:
    tag = "ol" if ordered else "ul"
    html_lines = [f"<{tag}>"]
    pattern = r"^\s*\d+\.\s+(.*)$" if ordered else r"^\s*[-*]\s+(.*)$"
    for line in lines:
        match = re.match(pattern, line)
        if match:
            html_lines.append(f"<li>{render_inline(match.group(1), resolve_link)}</li>")
    html_lines.append(f"</{tag}>")
    return "\n".join(html_lines)


def render_markdown(text: str, resolve_link) -> str:
    lines = text.splitlines()
    blocks: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            language = stripped[3:].strip()
            code: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            i += 1
            class_name = f' class="language-{html.escape(language)}"' if language else ""
            blocks.append(f"<pre><code{class_name}>{html.escape(chr(10).join(code))}</code></pre>")
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and table_separator(lines[i + 1]):
            table_lines = [line, lines[i + 1]]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            blocks.append(render_table(table_lines, resolve_link))
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{render_inline(heading.group(2), resolve_link)}</h{level}>")
            i += 1
            continue

        if re.match(r"^\s*[-*]\s+", line):
            list_lines: list[str] = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                list_lines.append(lines[i])
                i += 1
            blocks.append(render_list(list_lines, False, resolve_link))
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            list_lines = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                list_lines.append(lines[i])
                i += 1
            blocks.append(render_list(list_lines, True, resolve_link))
            continue

        if stripped.startswith(">"):
            quote_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append(f"<blockquote><p>{render_inline(' '.join(quote_lines), resolve_link)}</p></blockquote>")
            continue

        paragraph = [line.strip()]
        i += 1
        while i < len(lines):
            next_line = lines[i + 1] if i + 1 < len(lines) else None
            if special_block_start(lines[i], next_line):
                break
            paragraph.append(lines[i].strip())
            i += 1
        blocks.append(f"<p>{render_inline(' '.join(paragraph), resolve_link)}</p>")

    return "\n".join(blocks)


def nav_html(items: list[SiteItem], current: SiteItem) -> str:
    groups: list[str] = []
    seen: set[str] = set()
    for item in items:
        if item.group not in seen:
            groups.append(item.group)
            seen.add(item.group)

    parts: list[str] = []
    for group in groups:
        group_items = [item for item in items if item.group == group]
        parts.append('<section class="nav-group">')
        parts.append(f'<div class="nav-group-title">{html.escape(group)}</div>')
        for item in group_items:
            active = " active" if item.source == current.source else ""
            href = relpath(item.output, current.output.parent)
            label = item.title
            if item.kind != "markdown":
                label = f"{label} ({item.kind.upper()})"
            parts.append(f'<a class="nav-link{active}" href="{html.escape(href, quote=True)}">{html.escape(label)}</a>')
        parts.append("</section>")
    return "\n".join(parts)


def page_html(item: SiteItem, content: str, navigation: str) -> str:
    css = relpath(SITE / "assets" / "site.css", item.output.parent)
    js = relpath(SITE / "assets" / "site.js", item.output.parent)
    title = html.escape(item.title)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="{html.escape(css, quote=True)}">
</head>
<body>
  <button class="site-action menu-button" type="button" data-open-menu aria-controls="site-nav" aria-expanded="false">Contents</button>
  <button class="site-action print-button" type="button" data-print>Print</button>
  <div class="drawer-backdrop" data-backdrop></div>
  <aside class="nav-drawer" id="site-nav" data-drawer aria-hidden="true">
    <div class="drawer-head">
      <div class="drawer-title">Documents</div>
      <button class="drawer-close" type="button" data-close-menu>Close</button>
    </div>
    {navigation}
  </aside>
  <main class="page-shell">
    <article class="document">
{content}
    </article>
  </main>
  <script src="{html.escape(js, quote=True)}"></script>
</body>
</html>
"""


def copy_assets() -> None:
    asset_target = SITE / "assets"
    asset_target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ASSET_SOURCE / "site.css", asset_target / "site.css")
    shutil.copy2(ASSET_SOURCE / "site.js", asset_target / "site.js")


def build() -> None:
    items, output_by_source = collect_site_items()
    markdown_items = [item for item in items if item.kind == "markdown"]

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    copy_assets()

    for item in items:
        if item.kind == "markdown":
            resolve_link = make_link_resolver(item.source, item.output, output_by_source)
            content = render_markdown(read_text(item.source), resolve_link)
            navigation = nav_html(items, item)
            item.output.parent.mkdir(parents=True, exist_ok=True)
            item.output.write_text(page_html(item, content, navigation), encoding="utf-8")
        else:
            item.output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.source, item.output)

    print(f"Built {len(markdown_items)} document pages into {SITE.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static curriculum site.")
    parser.parse_args()
    build()


if __name__ == "__main__":
    main()
