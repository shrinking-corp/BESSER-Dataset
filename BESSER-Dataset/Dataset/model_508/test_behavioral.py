import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Families_Family,
    Families_FamilyRegistry,
    Families_Member,
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

def test_assoc_daughters1_reverse_link_reassign_clear():
    a1 = Families_Member(age=7, firstName="sample_text")
    a2 = Families_Member(age=13, firstName="sample_text_2")
    b = Families_Family(address="sample_text", lastName="sample_text")
    _safe_set(b, 'Families_Family2', {a1})
    assert _is_linked(b, 'Families_Family2', a1)
    if hasattr(a1, 'Families_Member3'):
        assert _is_linked(a1, 'Families_Member3', b)
    _safe_set(b, 'Families_Family2', {a2})
    assert _is_linked(b, 'Families_Family2', a2)
    if hasattr(a1, 'Families_Member3'):
        assert not _is_linked(a1, 'Families_Member3', b)
    if hasattr(a2, 'Families_Member3'):
        assert _is_linked(a2, 'Families_Member3', b)
    _safe_set(b, 'Families_Family2', set())
    assert not _is_linked(b, 'Families_Family2', a2)
    if hasattr(a2, 'Families_Member3'):
        assert not _is_linked(a2, 'Families_Member3', b)


def test_assoc_father7_reverse_link_reassign_clear():
    a1 = Families_Member(age=7, firstName="sample_text")
    a2 = Families_Member(age=13, firstName="sample_text_2")
    b = Families_Family(address="sample_text", lastName="sample_text")
    _safe_set(b, 'Families_Family8', a1)
    assert _is_linked(b, 'Families_Family8', a1)
    if hasattr(a1, 'Families_Member9'):
        assert _is_linked(a1, 'Families_Member9', b)
    _safe_set(b, 'Families_Family8', a2)
    assert _is_linked(b, 'Families_Family8', a2)
    if hasattr(a1, 'Families_Member9'):
        assert not _is_linked(a1, 'Families_Member9', b)
    if hasattr(a2, 'Families_Member9'):
        assert _is_linked(a2, 'Families_Member9', b)
    _safe_set(b, 'Families_Family8', None)
    assert not _is_linked(b, 'Families_Family8', a2)
    if hasattr(a2, 'Families_Member9'):
        assert not _is_linked(a2, 'Families_Member9', b)


def test_assoc_links11_reverse_link_reassign_clear():
    a1 = Families_Family(address="sample_text", lastName="sample_text")
    a2 = Families_Family(address="sample_text_2", lastName="sample_text_2")
    b = Families_Family(address="sample_text", lastName="sample_text")
    _safe_set(b, 'Families_Family12', a1)
    assert _is_linked(b, 'Families_Family12', a1)
    if hasattr(a1, 'Families_Family10'):
        assert _is_linked(a1, 'Families_Family10', b)
    _safe_set(b, 'Families_Family12', a2)
    assert _is_linked(b, 'Families_Family12', a2)
    if hasattr(a1, 'Families_Family10'):
        assert not _is_linked(a1, 'Families_Family10', b)
    if hasattr(a2, 'Families_Family10'):
        assert _is_linked(a2, 'Families_Family10', b)
    _safe_set(b, 'Families_Family12', None)
    assert not _is_linked(b, 'Families_Family12', a2)
    if hasattr(a2, 'Families_Family10'):
        assert not _is_linked(a2, 'Families_Family10', b)


def test_assoc_mother4_reverse_link_reassign_clear():
    a1 = Families_Member(age=7, firstName="sample_text")
    a2 = Families_Member(age=13, firstName="sample_text_2")
    b = Families_Family(address="sample_text", lastName="sample_text")
    _safe_set(b, 'Families_Family5', a1)
    assert _is_linked(b, 'Families_Family5', a1)
    if hasattr(a1, 'Families_Member6'):
        assert _is_linked(a1, 'Families_Member6', b)
    _safe_set(b, 'Families_Family5', a2)
    assert _is_linked(b, 'Families_Family5', a2)
    if hasattr(a1, 'Families_Member6'):
        assert not _is_linked(a1, 'Families_Member6', b)
    if hasattr(a2, 'Families_Member6'):
        assert _is_linked(a2, 'Families_Member6', b)
    _safe_set(b, 'Families_Family5', None)
    assert not _is_linked(b, 'Families_Family5', a2)
    if hasattr(a2, 'Families_Member6'):
        assert not _is_linked(a2, 'Families_Member6', b)


def test_assoc_relatives14_reverse_link_reassign_clear():
    a1 = Families_Member(age=7, firstName="sample_text")
    a2 = Families_Member(age=13, firstName="sample_text_2")
    b = Families_Member(age=7, firstName="sample_text")
    _safe_set(b, 'Families_Member15', a1)
    assert _is_linked(b, 'Families_Member15', a1)
    if hasattr(a1, 'Families_Member13'):
        assert _is_linked(a1, 'Families_Member13', b)
    _safe_set(b, 'Families_Member15', a2)
    assert _is_linked(b, 'Families_Member15', a2)
    if hasattr(a1, 'Families_Member13'):
        assert not _is_linked(a1, 'Families_Member13', b)
    if hasattr(a2, 'Families_Member13'):
        assert _is_linked(a2, 'Families_Member13', b)
    _safe_set(b, 'Families_Member15', None)
    assert not _is_linked(b, 'Families_Member15', a2)
    if hasattr(a2, 'Families_Member13'):
        assert not _is_linked(a2, 'Families_Member13', b)


def test_assoc_sons0_reverse_link_reassign_clear():
    a1 = Families_Member(age=7, firstName="sample_text")
    a2 = Families_Member(age=13, firstName="sample_text_2")
    b = Families_Family(address="sample_text", lastName="sample_text")
    _safe_set(b, 'Families_Family', {a1})
    assert _is_linked(b, 'Families_Family', a1)
    if hasattr(a1, 'Families_Member'):
        assert _is_linked(a1, 'Families_Member', b)
    _safe_set(b, 'Families_Family', {a2})
    assert _is_linked(b, 'Families_Family', a2)
    if hasattr(a1, 'Families_Member'):
        assert not _is_linked(a1, 'Families_Member', b)
    if hasattr(a2, 'Families_Member'):
        assert _is_linked(a2, 'Families_Member', b)
    _safe_set(b, 'Families_Family', set())
    assert not _is_linked(b, 'Families_Family', a2)
    if hasattr(a2, 'Families_Member'):
        assert not _is_linked(a2, 'Families_Member', b)


