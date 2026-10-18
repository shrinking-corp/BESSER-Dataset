"""Shared report rendering/writing."""
from __future__ import annotations

import json
from pathlib import Path


def render_status_table(by_status: dict[str, int]) -> list[str]:
    """Renders the "## Breakdown by status" table every report script
    builds, sorted by count descending. Returns a list of lines (no
    trailing blank line) -- callers append this into their own
    render_markdown_report()'s line list."""
    lines = ["## Breakdown by status", "", "| Status | Count |", "|---|---|"]
    for status, count in sorted(by_status.items(), key=lambda kv: -kv[1]):
        lines.append(f"| {status} | {count} |")
    return lines


def write_reports(reports_dir: Path, report_name: str, report: dict, markdown: str) -> tuple[Path, Path]:
    """Writes `<report_name>.json` and `<report_name>.md` (UTF-8) into
    reports_dir. Returns (json_path, md_path)."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / f"{report_name}.json"
    md_path = reports_dir / f"{report_name}.md"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")
    return json_path, md_path
