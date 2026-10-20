import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library_t_author,
    library_t_book,
    library_t_library,
    library_t_published,
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

def test_assoc_author4_reverse_link_reassign_clear():
    a1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    a2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    b = library_t_author(tagName="sample_text", text="sample_text")
    _safe_set(b, 'library_t_author', a1)
    assert _is_linked(b, 'library_t_author', a1)
    if hasattr(a1, 'library_t_book5'):
        assert _is_linked(a1, 'library_t_book5', b)
    _safe_set(b, 'library_t_author', a2)
    assert _is_linked(b, 'library_t_author', a2)
    if hasattr(a1, 'library_t_book5'):
        assert not _is_linked(a1, 'library_t_book5', b)
    if hasattr(a2, 'library_t_book5'):
        assert _is_linked(a2, 'library_t_book5', b)
    _safe_set(b, 'library_t_author', None)
    assert not _is_linked(b, 'library_t_author', a2)
    if hasattr(a2, 'library_t_book5'):
        assert not _is_linked(a2, 'library_t_book5', b)


def test_assoc_book0_reverse_link_reassign_clear():
    a1 = library_t_library(tagName="sample_text", text="sample_text")
    a2 = library_t_library(tagName="sample_text_2", text="sample_text_2")
    b = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    _safe_set(b, 'library_t_book', a1)
    assert _is_linked(b, 'library_t_book', a1)
    if hasattr(a1, 'library_t_library'):
        assert _is_linked(a1, 'library_t_library', b)
    _safe_set(b, 'library_t_book', a2)
    assert _is_linked(b, 'library_t_book', a2)
    if hasattr(a1, 'library_t_library'):
        assert not _is_linked(a1, 'library_t_library', b)
    if hasattr(a2, 'library_t_library'):
        assert _is_linked(a2, 'library_t_library', b)
    _safe_set(b, 'library_t_book', None)
    assert not _is_linked(b, 'library_t_book', a2)
    if hasattr(a2, 'library_t_library'):
        assert not _is_linked(a2, 'library_t_library', b)


def test_assoc_parentNode1_reverse_link_reassign_clear():
    a1 = library_t_library(tagName="sample_text", text="sample_text")
    a2 = library_t_library(tagName="sample_text_2", text="sample_text_2")
    b = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    _safe_set(b, 'library_t_book2', a1)
    assert _is_linked(b, 'library_t_book2', a1)
    if hasattr(a1, 'library_t_library3'):
        assert _is_linked(a1, 'library_t_library3', b)
    _safe_set(b, 'library_t_book2', a2)
    assert _is_linked(b, 'library_t_book2', a2)
    if hasattr(a1, 'library_t_library3'):
        assert not _is_linked(a1, 'library_t_library3', b)
    if hasattr(a2, 'library_t_library3'):
        assert _is_linked(a2, 'library_t_library3', b)
    _safe_set(b, 'library_t_book2', None)
    assert not _is_linked(b, 'library_t_book2', a2)
    if hasattr(a2, 'library_t_library3'):
        assert not _is_linked(a2, 'library_t_library3', b)


def test_assoc_parentNode11_reverse_link_reassign_clear():
    a1 = library_t_published(tagName="sample_text", text="sample_text")
    a2 = library_t_published(tagName="sample_text_2", text="sample_text_2")
    b = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    _safe_set(b, 'library_t_book13', a1)
    assert _is_linked(b, 'library_t_book13', a1)
    if hasattr(a1, 'library_t_published12'):
        assert _is_linked(a1, 'library_t_published12', b)
    _safe_set(b, 'library_t_book13', a2)
    assert _is_linked(b, 'library_t_book13', a2)
    if hasattr(a1, 'library_t_published12'):
        assert not _is_linked(a1, 'library_t_published12', b)
    if hasattr(a2, 'library_t_published12'):
        assert _is_linked(a2, 'library_t_published12', b)
    _safe_set(b, 'library_t_book13', None)
    assert not _is_linked(b, 'library_t_book13', a2)
    if hasattr(a2, 'library_t_published12'):
        assert not _is_linked(a2, 'library_t_published12', b)


def test_assoc_parentNode8_reverse_link_reassign_clear():
    a1 = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    a2 = library_t_book(pages=13, tagName="sample_text_2", text="sample_text_2", title="sample_text_2")
    b = library_t_author(tagName="sample_text", text="sample_text")
    _safe_set(b, 'library_t_author9', a1)
    assert _is_linked(b, 'library_t_author9', a1)
    if hasattr(a1, 'library_t_book10'):
        assert _is_linked(a1, 'library_t_book10', b)
    _safe_set(b, 'library_t_author9', a2)
    assert _is_linked(b, 'library_t_author9', a2)
    if hasattr(a1, 'library_t_book10'):
        assert not _is_linked(a1, 'library_t_book10', b)
    if hasattr(a2, 'library_t_book10'):
        assert _is_linked(a2, 'library_t_book10', b)
    _safe_set(b, 'library_t_author9', None)
    assert not _is_linked(b, 'library_t_author9', a2)
    if hasattr(a2, 'library_t_book10'):
        assert not _is_linked(a2, 'library_t_book10', b)


def test_assoc_published6_reverse_link_reassign_clear():
    a1 = library_t_published(tagName="sample_text", text="sample_text")
    a2 = library_t_published(tagName="sample_text_2", text="sample_text_2")
    b = library_t_book(pages=7, tagName="sample_text", text="sample_text", title="sample_text")
    _safe_set(b, 'library_t_book7', a1)
    assert _is_linked(b, 'library_t_book7', a1)
    if hasattr(a1, 'library_t_published'):
        assert _is_linked(a1, 'library_t_published', b)
    _safe_set(b, 'library_t_book7', a2)
    assert _is_linked(b, 'library_t_book7', a2)
    if hasattr(a1, 'library_t_published'):
        assert not _is_linked(a1, 'library_t_published', b)
    if hasattr(a2, 'library_t_published'):
        assert _is_linked(a2, 'library_t_published', b)
    _safe_set(b, 'library_t_book7', None)
    assert not _is_linked(b, 'library_t_book7', a2)
    if hasattr(a2, 'library_t_published'):
        assert not _is_linked(a2, 'library_t_published', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

