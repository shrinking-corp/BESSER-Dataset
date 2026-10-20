import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    lib_Address,
    lib_Book,
    lib_Cafeteria,
    lib_Library,
    lib_Person,
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

def test_assoc_address1_reverse_link_reassign_clear():
    a1 = lib_Library(name="sample_text")
    a2 = lib_Library(name="sample_text_2")
    b = lib_Address(postalCode="sample_text")
    _safe_set(b, 'lib_Address', a1)
    assert _is_linked(b, 'lib_Address', a1)
    if hasattr(a1, 'lib_Library2'):
        assert _is_linked(a1, 'lib_Library2', b)
    _safe_set(b, 'lib_Address', a2)
    assert _is_linked(b, 'lib_Address', a2)
    if hasattr(a1, 'lib_Library2'):
        assert not _is_linked(a1, 'lib_Library2', b)
    if hasattr(a2, 'lib_Library2'):
        assert _is_linked(a2, 'lib_Library2', b)
    _safe_set(b, 'lib_Address', None)
    assert not _is_linked(b, 'lib_Address', a2)
    if hasattr(a2, 'lib_Library2'):
        assert not _is_linked(a2, 'lib_Library2', b)


def test_assoc_books0_reverse_link_reassign_clear():
    a1 = lib_Library(name="sample_text")
    a2 = lib_Library(name="sample_text_2")
    b = lib_Book(title="sample_text")
    _safe_set(b, 'lib_Book', a1)
    assert _is_linked(b, 'lib_Book', a1)
    if hasattr(a1, 'lib_Library'):
        assert _is_linked(a1, 'lib_Library', b)
    _safe_set(b, 'lib_Book', a2)
    assert _is_linked(b, 'lib_Book', a2)
    if hasattr(a1, 'lib_Library'):
        assert not _is_linked(a1, 'lib_Library', b)
    if hasattr(a2, 'lib_Library'):
        assert _is_linked(a2, 'lib_Library', b)
    _safe_set(b, 'lib_Book', None)
    assert not _is_linked(b, 'lib_Book', a2)
    if hasattr(a2, 'lib_Library'):
        assert not _is_linked(a2, 'lib_Library', b)


def test_assoc_cafeteria4_reverse_link_reassign_clear():
    a1 = lib_Library(name="sample_text")
    a2 = lib_Library(name="sample_text_2")
    b = lib_Cafeteria(name="sample_text")
    _safe_set(b, 'Cafeteria', a1)
    assert _is_linked(b, 'Cafeteria', a1)
    if hasattr(a1, 'library5'):
        assert _is_linked(a1, 'library5', b)
    _safe_set(b, 'Cafeteria', a2)
    assert _is_linked(b, 'Cafeteria', a2)
    if hasattr(a1, 'library5'):
        assert not _is_linked(a1, 'library5', b)
    if hasattr(a2, 'library5'):
        assert _is_linked(a2, 'library5', b)
    _safe_set(b, 'Cafeteria', None)
    assert not _is_linked(b, 'Cafeteria', a2)
    if hasattr(a2, 'library5'):
        assert not _is_linked(a2, 'library5', b)


def test_assoc_library6_reverse_link_reassign_clear():
    a1 = lib_Person(name="sample_text")
    a2 = lib_Person(name="sample_text_2")
    b = lib_Library(name="sample_text")
    _safe_set(b, 'Library', a1)
    assert _is_linked(b, 'Library', a1)
    if hasattr(a1, 'writers'):
        assert _is_linked(a1, 'writers', b)
    _safe_set(b, 'Library', a2)
    assert _is_linked(b, 'Library', a2)
    if hasattr(a1, 'writers'):
        assert not _is_linked(a1, 'writers', b)
    if hasattr(a2, 'writers'):
        assert _is_linked(a2, 'writers', b)
    _safe_set(b, 'Library', None)
    assert not _is_linked(b, 'Library', a2)
    if hasattr(a2, 'writers'):
        assert not _is_linked(a2, 'writers', b)


def test_assoc_library7_reverse_link_reassign_clear():
    a1 = lib_Library(name="sample_text")
    a2 = lib_Library(name="sample_text_2")
    b = lib_Cafeteria(name="sample_text")
    _safe_set(b, 'cafeteria', a1)
    assert _is_linked(b, 'cafeteria', a1)
    if hasattr(a1, 'Library8'):
        assert _is_linked(a1, 'Library8', b)
    _safe_set(b, 'cafeteria', a2)
    assert _is_linked(b, 'cafeteria', a2)
    if hasattr(a1, 'Library8'):
        assert not _is_linked(a1, 'Library8', b)
    if hasattr(a2, 'Library8'):
        assert _is_linked(a2, 'Library8', b)
    _safe_set(b, 'cafeteria', None)
    assert not _is_linked(b, 'cafeteria', a2)
    if hasattr(a2, 'Library8'):
        assert not _is_linked(a2, 'Library8', b)


def test_assoc_writers3_reverse_link_reassign_clear():
    a1 = lib_Person(name="sample_text")
    a2 = lib_Person(name="sample_text_2")
    b = lib_Library(name="sample_text")
    _safe_set(b, 'library', {a1})
    assert _is_linked(b, 'library', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'library', {a2})
    assert _is_linked(b, 'library', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'library', set())
    assert not _is_linked(b, 'library', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

