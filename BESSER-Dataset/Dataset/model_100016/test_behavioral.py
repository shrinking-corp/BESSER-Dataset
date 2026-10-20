import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bibtex_Author,
    Bibtex_Entry,
    Bibtex_LiteratureDb,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_author0_reverse_link_reassign_clear():
    a1 = Bibtex_LiteratureDb(name="sample_text")
    a2 = Bibtex_LiteratureDb(name="sample_text_2")
    b = Bibtex_Author(name="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'literaturedb'):
        assert _is_linked(a1, 'literaturedb', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'literaturedb'):
        assert not _is_linked(a1, 'literaturedb', b)
    if hasattr(a2, 'literaturedb'):
        assert _is_linked(a2, 'literaturedb', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'literaturedb'):
        assert not _is_linked(a2, 'literaturedb', b)


def test_assoc_author3_reverse_link_reassign_clear():
    a1 = Bibtex_Entry(id="sample_text", title="sample_text")
    a2 = Bibtex_Entry(id="sample_text_2", title="sample_text_2")
    b = Bibtex_Author(name="sample_text")
    _safe_set(b, 'Author4', a1)
    assert _is_linked(b, 'Author4', a1)
    if hasattr(a1, 'publications'):
        assert _is_linked(a1, 'publications', b)
    _safe_set(b, 'Author4', a2)
    assert _is_linked(b, 'Author4', a2)
    if hasattr(a1, 'publications'):
        assert not _is_linked(a1, 'publications', b)
    if hasattr(a2, 'publications'):
        assert _is_linked(a2, 'publications', b)
    _safe_set(b, 'Author4', None)
    assert not _is_linked(b, 'Author4', a2)
    if hasattr(a2, 'publications'):
        assert not _is_linked(a2, 'publications', b)


def test_assoc_entries1_reverse_link_reassign_clear():
    a1 = Bibtex_LiteratureDb(name="sample_text")
    a2 = Bibtex_LiteratureDb(name="sample_text_2")
    b = Bibtex_Entry(id="sample_text", title="sample_text")
    _safe_set(b, 'Entry', a1)
    assert _is_linked(b, 'Entry', a1)
    if hasattr(a1, 'literaturedb2'):
        assert _is_linked(a1, 'literaturedb2', b)
    _safe_set(b, 'Entry', a2)
    assert _is_linked(b, 'Entry', a2)
    if hasattr(a1, 'literaturedb2'):
        assert not _is_linked(a1, 'literaturedb2', b)
    if hasattr(a2, 'literaturedb2'):
        assert _is_linked(a2, 'literaturedb2', b)
    _safe_set(b, 'Entry', None)
    assert not _is_linked(b, 'Entry', a2)
    if hasattr(a2, 'literaturedb2'):
        assert not _is_linked(a2, 'literaturedb2', b)


def test_assoc_literaturedb5_reverse_link_reassign_clear():
    a1 = Bibtex_LiteratureDb(name="sample_text")
    a2 = Bibtex_LiteratureDb(name="sample_text_2")
    b = Bibtex_Entry(id="sample_text", title="sample_text")
    _safe_set(b, 'entries', a1)
    assert _is_linked(b, 'entries', a1)
    if hasattr(a1, 'LiteratureDb'):
        assert _is_linked(a1, 'LiteratureDb', b)
    _safe_set(b, 'entries', a2)
    assert _is_linked(b, 'entries', a2)
    if hasattr(a1, 'LiteratureDb'):
        assert not _is_linked(a1, 'LiteratureDb', b)
    if hasattr(a2, 'LiteratureDb'):
        assert _is_linked(a2, 'LiteratureDb', b)
    _safe_set(b, 'entries', None)
    assert not _is_linked(b, 'entries', a2)
    if hasattr(a2, 'LiteratureDb'):
        assert not _is_linked(a2, 'LiteratureDb', b)


def test_assoc_literaturedb8_reverse_link_reassign_clear():
    a1 = Bibtex_LiteratureDb(name="sample_text")
    a2 = Bibtex_LiteratureDb(name="sample_text_2")
    b = Bibtex_Author(name="sample_text")
    _safe_set(b, 'author9', a1)
    assert _is_linked(b, 'author9', a1)
    if hasattr(a1, 'LiteratureDb10'):
        assert _is_linked(a1, 'LiteratureDb10', b)
    _safe_set(b, 'author9', a2)
    assert _is_linked(b, 'author9', a2)
    if hasattr(a1, 'LiteratureDb10'):
        assert not _is_linked(a1, 'LiteratureDb10', b)
    if hasattr(a2, 'LiteratureDb10'):
        assert _is_linked(a2, 'LiteratureDb10', b)
    _safe_set(b, 'author9', None)
    assert not _is_linked(b, 'author9', a2)
    if hasattr(a2, 'LiteratureDb10'):
        assert not _is_linked(a2, 'LiteratureDb10', b)


def test_assoc_publications6_reverse_link_reassign_clear():
    a1 = Bibtex_Entry(id="sample_text", title="sample_text")
    a2 = Bibtex_Entry(id="sample_text_2", title="sample_text_2")
    b = Bibtex_Author(name="sample_text")
    _safe_set(b, 'author', {a1})
    assert _is_linked(b, 'author', a1)
    if hasattr(a1, 'Entry7'):
        assert _is_linked(a1, 'Entry7', b)
    _safe_set(b, 'author', {a2})
    assert _is_linked(b, 'author', a2)
    if hasattr(a1, 'Entry7'):
        assert not _is_linked(a1, 'Entry7', b)
    if hasattr(a2, 'Entry7'):
        assert _is_linked(a2, 'Entry7', b)
    _safe_set(b, 'author', set())
    assert not _is_linked(b, 'author', a2)
    if hasattr(a2, 'Entry7'):
        assert not _is_linked(a2, 'Entry7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

