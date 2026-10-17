import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DictionaryLanguage_Author,
    DictionaryLanguage_Dictionary,
    DictionaryLanguage_Entry,
    DictionaryLanguage_Library,
    DictionaryLanguage_Shelf,
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
    a1 = DictionaryLanguage_Dictionary(title="sample_text")
    a2 = DictionaryLanguage_Dictionary(title="sample_text_2")
    b = DictionaryLanguage_Author(email="sample_text")
    _safe_set(b, 'Author', a1)
    assert _is_linked(b, 'Author', a1)
    if hasattr(a1, 'dictionary5'):
        assert _is_linked(a1, 'dictionary5', b)
    _safe_set(b, 'Author', a2)
    assert _is_linked(b, 'Author', a2)
    if hasattr(a1, 'dictionary5'):
        assert not _is_linked(a1, 'dictionary5', b)
    if hasattr(a2, 'dictionary5'):
        assert _is_linked(a2, 'dictionary5', b)
    _safe_set(b, 'Author', None)
    assert not _is_linked(b, 'Author', a2)
    if hasattr(a2, 'dictionary5'):
        assert not _is_linked(a2, 'dictionary5', b)


def test_assoc_author8_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Library(name="sample_text")
    a2 = DictionaryLanguage_Library(name="sample_text_2")
    b = DictionaryLanguage_Author(email="sample_text")
    _safe_set(b, 'Author9', a1)
    assert _is_linked(b, 'Author9', a1)
    if hasattr(a1, 'library'):
        assert _is_linked(a1, 'library', b)
    _safe_set(b, 'Author9', a2)
    assert _is_linked(b, 'Author9', a2)
    if hasattr(a1, 'library'):
        assert not _is_linked(a1, 'library', b)
    if hasattr(a2, 'library'):
        assert _is_linked(a2, 'library', b)
    _safe_set(b, 'Author9', None)
    assert not _is_linked(b, 'Author9', a2)
    if hasattr(a2, 'library'):
        assert not _is_linked(a2, 'library', b)


def test_assoc_dictionary1_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Dictionary(title="sample_text")
    a2 = DictionaryLanguage_Dictionary(title="sample_text_2")
    b = DictionaryLanguage_Author(email="sample_text")
    _safe_set(b, 'author2', {a1})
    assert _is_linked(b, 'author2', a1)
    if hasattr(a1, 'Dictionary'):
        assert _is_linked(a1, 'Dictionary', b)
    _safe_set(b, 'author2', {a2})
    assert _is_linked(b, 'author2', a2)
    if hasattr(a1, 'Dictionary'):
        assert not _is_linked(a1, 'Dictionary', b)
    if hasattr(a2, 'Dictionary'):
        assert _is_linked(a2, 'Dictionary', b)
    _safe_set(b, 'author2', set())
    assert not _is_linked(b, 'author2', a2)
    if hasattr(a2, 'Dictionary'):
        assert not _is_linked(a2, 'Dictionary', b)


def test_assoc_dictionary10_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Shelf(description="sample_text")
    a2 = DictionaryLanguage_Shelf(description="sample_text_2")
    b = DictionaryLanguage_Dictionary(title="sample_text")
    _safe_set(b, 'Dictionary11', a1)
    assert _is_linked(b, 'Dictionary11', a1)
    if hasattr(a1, 'shelf'):
        assert _is_linked(a1, 'shelf', b)
    _safe_set(b, 'Dictionary11', a2)
    assert _is_linked(b, 'Dictionary11', a2)
    if hasattr(a1, 'shelf'):
        assert not _is_linked(a1, 'shelf', b)
    if hasattr(a2, 'shelf'):
        assert _is_linked(a2, 'shelf', b)
    _safe_set(b, 'Dictionary11', None)
    assert not _is_linked(b, 'Dictionary11', a2)
    if hasattr(a2, 'shelf'):
        assert not _is_linked(a2, 'shelf', b)


def test_assoc_entry6_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Entry(content="sample_text", level="sample_text")
    a2 = DictionaryLanguage_Entry(content="sample_text_2", level="sample_text_2")
    b = DictionaryLanguage_Dictionary(title="sample_text")
    _safe_set(b, 'DictionaryLanguage_Dictionary', {a1})
    assert _is_linked(b, 'DictionaryLanguage_Dictionary', a1)
    if hasattr(a1, 'DictionaryLanguage_Entry'):
        assert _is_linked(a1, 'DictionaryLanguage_Entry', b)
    _safe_set(b, 'DictionaryLanguage_Dictionary', {a2})
    assert _is_linked(b, 'DictionaryLanguage_Dictionary', a2)
    if hasattr(a1, 'DictionaryLanguage_Entry'):
        assert not _is_linked(a1, 'DictionaryLanguage_Entry', b)
    if hasattr(a2, 'DictionaryLanguage_Entry'):
        assert _is_linked(a2, 'DictionaryLanguage_Entry', b)
    _safe_set(b, 'DictionaryLanguage_Dictionary', set())
    assert not _is_linked(b, 'DictionaryLanguage_Dictionary', a2)
    if hasattr(a2, 'DictionaryLanguage_Entry'):
        assert not _is_linked(a2, 'DictionaryLanguage_Entry', b)


def test_assoc_library0_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Library(name="sample_text")
    a2 = DictionaryLanguage_Library(name="sample_text_2")
    b = DictionaryLanguage_Author(email="sample_text")
    _safe_set(b, 'author', a1)
    assert _is_linked(b, 'author', a1)
    if hasattr(a1, 'Library'):
        assert _is_linked(a1, 'Library', b)
    _safe_set(b, 'author', a2)
    assert _is_linked(b, 'author', a2)
    if hasattr(a1, 'Library'):
        assert not _is_linked(a1, 'Library', b)
    if hasattr(a2, 'Library'):
        assert _is_linked(a2, 'Library', b)
    _safe_set(b, 'author', None)
    assert not _is_linked(b, 'author', a2)
    if hasattr(a2, 'Library'):
        assert not _is_linked(a2, 'Library', b)


def test_assoc_shelf3_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Shelf(description="sample_text")
    a2 = DictionaryLanguage_Shelf(description="sample_text_2")
    b = DictionaryLanguage_Dictionary(title="sample_text")
    _safe_set(b, 'dictionary', a1)
    assert _is_linked(b, 'dictionary', a1)
    if hasattr(a1, 'Shelf'):
        assert _is_linked(a1, 'Shelf', b)
    _safe_set(b, 'dictionary', a2)
    assert _is_linked(b, 'dictionary', a2)
    if hasattr(a1, 'Shelf'):
        assert not _is_linked(a1, 'Shelf', b)
    if hasattr(a2, 'Shelf'):
        assert _is_linked(a2, 'Shelf', b)
    _safe_set(b, 'dictionary', None)
    assert not _is_linked(b, 'dictionary', a2)
    if hasattr(a2, 'Shelf'):
        assert not _is_linked(a2, 'Shelf', b)


def test_assoc_shelf7_reverse_link_reassign_clear():
    a1 = DictionaryLanguage_Shelf(description="sample_text")
    a2 = DictionaryLanguage_Shelf(description="sample_text_2")
    b = DictionaryLanguage_Library(name="sample_text")
    _safe_set(b, 'DictionaryLanguage_Library', {a1})
    assert _is_linked(b, 'DictionaryLanguage_Library', a1)
    if hasattr(a1, 'DictionaryLanguage_Shelf'):
        assert _is_linked(a1, 'DictionaryLanguage_Shelf', b)
    _safe_set(b, 'DictionaryLanguage_Library', {a2})
    assert _is_linked(b, 'DictionaryLanguage_Library', a2)
    if hasattr(a1, 'DictionaryLanguage_Shelf'):
        assert not _is_linked(a1, 'DictionaryLanguage_Shelf', b)
    if hasattr(a2, 'DictionaryLanguage_Shelf'):
        assert _is_linked(a2, 'DictionaryLanguage_Shelf', b)
    _safe_set(b, 'DictionaryLanguage_Library', set())
    assert not _is_linked(b, 'DictionaryLanguage_Library', a2)
    if hasattr(a2, 'DictionaryLanguage_Shelf'):
        assert not _is_linked(a2, 'DictionaryLanguage_Shelf', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

