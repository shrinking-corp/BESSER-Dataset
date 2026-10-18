"""Shared ast.parse-with-SyntaxError-handling helper."""
from __future__ import annotations

import ast


def safe_parse(source: str) -> tuple[ast.Module | None, str | None]:
    """Parses `source`, returning (tree, None) on success or
    (None, error_message) on a SyntaxError. error_message is formatted as
    "{exc.msg} (line {exc.lineno})" -- the format already used independently
    in more than one script before this was consolidated. Callers that only
    need a bool can check `tree is not None`."""
    try:
        return ast.parse(source), None
    except SyntaxError as exc:
        return None, f"{exc.msg} (line {exc.lineno})"
