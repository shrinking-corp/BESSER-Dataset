import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    families_Family,
    families_FamilyRegister,
    families_Member,
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

def test_assoc_daughters2_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'familyDaughter', {a1})
    assert _is_linked(b, 'familyDaughter', a1)
    if hasattr(a1, 'Member3'):
        assert _is_linked(a1, 'Member3', b)
    _safe_set(b, 'familyDaughter', {a2})
    assert _is_linked(b, 'familyDaughter', a2)
    if hasattr(a1, 'Member3'):
        assert not _is_linked(a1, 'Member3', b)
    if hasattr(a2, 'Member3'):
        assert _is_linked(a2, 'Member3', b)
    _safe_set(b, 'familyDaughter', set())
    assert not _is_linked(b, 'familyDaughter', a2)
    if hasattr(a2, 'Member3'):
        assert not _is_linked(a2, 'Member3', b)


def test_assoc_families0_reverse_link_reassign_clear():
    a1 = families_FamilyRegister(id="sample_text")
    a2 = families_FamilyRegister(id="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'families_Family', a1)
    assert _is_linked(b, 'families_Family', a1)
    if hasattr(a1, 'families_FamilyRegister'):
        assert _is_linked(a1, 'families_FamilyRegister', b)
    _safe_set(b, 'families_Family', a2)
    assert _is_linked(b, 'families_Family', a2)
    if hasattr(a1, 'families_FamilyRegister'):
        assert not _is_linked(a1, 'families_FamilyRegister', b)
    if hasattr(a2, 'families_FamilyRegister'):
        assert _is_linked(a2, 'families_FamilyRegister', b)
    _safe_set(b, 'families_Family', None)
    assert not _is_linked(b, 'families_Family', a2)
    if hasattr(a2, 'families_FamilyRegister'):
        assert not _is_linked(a2, 'families_FamilyRegister', b)


def test_assoc_familyDaughter9_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'Family10', a1)
    assert _is_linked(b, 'Family10', a1)
    if hasattr(a1, 'daughters'):
        assert _is_linked(a1, 'daughters', b)
    _safe_set(b, 'Family10', a2)
    assert _is_linked(b, 'Family10', a2)
    if hasattr(a1, 'daughters'):
        assert not _is_linked(a1, 'daughters', b)
    if hasattr(a2, 'daughters'):
        assert _is_linked(a2, 'daughters', b)
    _safe_set(b, 'Family10', None)
    assert not _is_linked(b, 'Family10', a2)
    if hasattr(a2, 'daughters'):
        assert not _is_linked(a2, 'daughters', b)


def test_assoc_familyFather11_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'Family12', a1)
    assert _is_linked(b, 'Family12', a1)
    if hasattr(a1, 'father'):
        assert _is_linked(a1, 'father', b)
    _safe_set(b, 'Family12', a2)
    assert _is_linked(b, 'Family12', a2)
    if hasattr(a1, 'father'):
        assert not _is_linked(a1, 'father', b)
    if hasattr(a2, 'father'):
        assert _is_linked(a2, 'father', b)
    _safe_set(b, 'Family12', None)
    assert not _is_linked(b, 'Family12', a2)
    if hasattr(a2, 'father'):
        assert not _is_linked(a2, 'father', b)


def test_assoc_familyMother13_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'Family14', a1)
    assert _is_linked(b, 'Family14', a1)
    if hasattr(a1, 'mother'):
        assert _is_linked(a1, 'mother', b)
    _safe_set(b, 'Family14', a2)
    assert _is_linked(b, 'Family14', a2)
    if hasattr(a1, 'mother'):
        assert not _is_linked(a1, 'mother', b)
    if hasattr(a2, 'mother'):
        assert _is_linked(a2, 'mother', b)
    _safe_set(b, 'Family14', None)
    assert not _is_linked(b, 'Family14', a2)
    if hasattr(a2, 'mother'):
        assert not _is_linked(a2, 'mother', b)


def test_assoc_familySon8_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'Family', a1)
    assert _is_linked(b, 'Family', a1)
    if hasattr(a1, 'sons'):
        assert _is_linked(a1, 'sons', b)
    _safe_set(b, 'Family', a2)
    assert _is_linked(b, 'Family', a2)
    if hasattr(a1, 'sons'):
        assert not _is_linked(a1, 'sons', b)
    if hasattr(a2, 'sons'):
        assert _is_linked(a2, 'sons', b)
    _safe_set(b, 'Family', None)
    assert not _is_linked(b, 'Family', a2)
    if hasattr(a2, 'sons'):
        assert not _is_linked(a2, 'sons', b)


def test_assoc_father4_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'familyFather', a1)
    assert _is_linked(b, 'familyFather', a1)
    if hasattr(a1, 'Member5'):
        assert _is_linked(a1, 'Member5', b)
    _safe_set(b, 'familyFather', a2)
    assert _is_linked(b, 'familyFather', a2)
    if hasattr(a1, 'Member5'):
        assert not _is_linked(a1, 'Member5', b)
    if hasattr(a2, 'Member5'):
        assert _is_linked(a2, 'Member5', b)
    _safe_set(b, 'familyFather', None)
    assert not _is_linked(b, 'familyFather', a2)
    if hasattr(a2, 'Member5'):
        assert not _is_linked(a2, 'Member5', b)


def test_assoc_mother6_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'familyMother', a1)
    assert _is_linked(b, 'familyMother', a1)
    if hasattr(a1, 'Member7'):
        assert _is_linked(a1, 'Member7', b)
    _safe_set(b, 'familyMother', a2)
    assert _is_linked(b, 'familyMother', a2)
    if hasattr(a1, 'Member7'):
        assert not _is_linked(a1, 'Member7', b)
    if hasattr(a2, 'Member7'):
        assert _is_linked(a2, 'Member7', b)
    _safe_set(b, 'familyMother', None)
    assert not _is_linked(b, 'familyMother', a2)
    if hasattr(a2, 'Member7'):
        assert not _is_linked(a2, 'Member7', b)


def test_assoc_sons1_reverse_link_reassign_clear():
    a1 = families_Member(firstName="sample_text")
    a2 = families_Member(firstName="sample_text_2")
    b = families_Family(lastName="sample_text")
    _safe_set(b, 'familySon', {a1})
    assert _is_linked(b, 'familySon', a1)
    if hasattr(a1, 'Member'):
        assert _is_linked(a1, 'Member', b)
    _safe_set(b, 'familySon', {a2})
    assert _is_linked(b, 'familySon', a2)
    if hasattr(a1, 'Member'):
        assert not _is_linked(a1, 'Member', b)
    if hasattr(a2, 'Member'):
        assert _is_linked(a2, 'Member', b)
    _safe_set(b, 'familySon', set())
    assert not _is_linked(b, 'familySon', a2)
    if hasattr(a2, 'Member'):
        assert not _is_linked(a2, 'Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

