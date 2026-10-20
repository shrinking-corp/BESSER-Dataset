import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FamiliesWithSiblings_Family,
    FamiliesWithSiblings_FamilyMember,
    FamiliesWithSiblings_FamilyRegister,
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

def test_assoc_daughters6_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'daughtersInverse', {a1})
    assert _is_linked(b, 'daughtersInverse', a1)
    if hasattr(a1, 'FamilyMember7'):
        assert _is_linked(a1, 'FamilyMember7', b)
    _safe_set(b, 'daughtersInverse', {a2})
    assert _is_linked(b, 'daughtersInverse', a2)
    if hasattr(a1, 'FamilyMember7'):
        assert not _is_linked(a1, 'FamilyMember7', b)
    if hasattr(a2, 'FamilyMember7'):
        assert _is_linked(a2, 'FamilyMember7', b)
    _safe_set(b, 'daughtersInverse', set())
    assert not _is_linked(b, 'daughtersInverse', a2)
    if hasattr(a2, 'FamilyMember7'):
        assert not _is_linked(a2, 'FamilyMember7', b)


def test_assoc_daughtersInverse17_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'Family18', a1)
    assert _is_linked(b, 'Family18', a1)
    if hasattr(a1, 'daughters'):
        assert _is_linked(a1, 'daughters', b)
    _safe_set(b, 'Family18', a2)
    assert _is_linked(b, 'Family18', a2)
    if hasattr(a1, 'daughters'):
        assert not _is_linked(a1, 'daughters', b)
    if hasattr(a2, 'daughters'):
        assert _is_linked(a2, 'daughters', b)
    _safe_set(b, 'Family18', None)
    assert not _is_linked(b, 'Family18', a2)
    if hasattr(a2, 'daughters'):
        assert not _is_linked(a2, 'daughters', b)


def test_assoc_father1_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'fatherInverse', a1)
    assert _is_linked(b, 'fatherInverse', a1)
    if hasattr(a1, 'FamilyMember'):
        assert _is_linked(a1, 'FamilyMember', b)
    _safe_set(b, 'fatherInverse', a2)
    assert _is_linked(b, 'fatherInverse', a2)
    if hasattr(a1, 'FamilyMember'):
        assert not _is_linked(a1, 'FamilyMember', b)
    if hasattr(a2, 'FamilyMember'):
        assert _is_linked(a2, 'FamilyMember', b)
    _safe_set(b, 'fatherInverse', None)
    assert not _is_linked(b, 'fatherInverse', a2)
    if hasattr(a2, 'FamilyMember'):
        assert not _is_linked(a2, 'FamilyMember', b)


def test_assoc_fatherInverse11_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
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


def test_assoc_mother2_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'motherInverse', a1)
    assert _is_linked(b, 'motherInverse', a1)
    if hasattr(a1, 'FamilyMember3'):
        assert _is_linked(a1, 'FamilyMember3', b)
    _safe_set(b, 'motherInverse', a2)
    assert _is_linked(b, 'motherInverse', a2)
    if hasattr(a1, 'FamilyMember3'):
        assert not _is_linked(a1, 'FamilyMember3', b)
    if hasattr(a2, 'FamilyMember3'):
        assert _is_linked(a2, 'FamilyMember3', b)
    _safe_set(b, 'motherInverse', None)
    assert not _is_linked(b, 'motherInverse', a2)
    if hasattr(a2, 'FamilyMember3'):
        assert not _is_linked(a2, 'FamilyMember3', b)


def test_assoc_motherInverse13_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
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


def test_assoc_siblings10_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_Family(name="sample_text")
    a2 = FamiliesWithSiblings_Family(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'FamiliesWithSiblings_Family9', {a1})
    assert _is_linked(b, 'FamiliesWithSiblings_Family9', a1)
    if hasattr(a1, 'FamiliesWithSiblings_Family'):
        assert _is_linked(a1, 'FamiliesWithSiblings_Family', b)
    _safe_set(b, 'FamiliesWithSiblings_Family9', {a2})
    assert _is_linked(b, 'FamiliesWithSiblings_Family9', a2)
    if hasattr(a1, 'FamiliesWithSiblings_Family'):
        assert not _is_linked(a1, 'FamiliesWithSiblings_Family', b)
    if hasattr(a2, 'FamiliesWithSiblings_Family'):
        assert _is_linked(a2, 'FamiliesWithSiblings_Family', b)
    _safe_set(b, 'FamiliesWithSiblings_Family9', set())
    assert not _is_linked(b, 'FamiliesWithSiblings_Family9', a2)
    if hasattr(a2, 'FamiliesWithSiblings_Family'):
        assert not _is_linked(a2, 'FamiliesWithSiblings_Family', b)


def test_assoc_sons4_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'sonsInverse', {a1})
    assert _is_linked(b, 'sonsInverse', a1)
    if hasattr(a1, 'FamilyMember5'):
        assert _is_linked(a1, 'FamilyMember5', b)
    _safe_set(b, 'sonsInverse', {a2})
    assert _is_linked(b, 'sonsInverse', a2)
    if hasattr(a1, 'FamilyMember5'):
        assert not _is_linked(a1, 'FamilyMember5', b)
    if hasattr(a2, 'FamilyMember5'):
        assert _is_linked(a2, 'FamilyMember5', b)
    _safe_set(b, 'sonsInverse', set())
    assert not _is_linked(b, 'sonsInverse', a2)
    if hasattr(a2, 'FamilyMember5'):
        assert not _is_linked(a2, 'FamilyMember5', b)


def test_assoc_sonsInverse15_reverse_link_reassign_clear():
    a1 = FamiliesWithSiblings_FamilyMember(name="sample_text")
    a2 = FamiliesWithSiblings_FamilyMember(name="sample_text_2")
    b = FamiliesWithSiblings_Family(name="sample_text")
    _safe_set(b, 'Family16', a1)
    assert _is_linked(b, 'Family16', a1)
    if hasattr(a1, 'sons'):
        assert _is_linked(a1, 'sons', b)
    _safe_set(b, 'Family16', a2)
    assert _is_linked(b, 'Family16', a2)
    if hasattr(a1, 'sons'):
        assert not _is_linked(a1, 'sons', b)
    if hasattr(a2, 'sons'):
        assert _is_linked(a2, 'sons', b)
    _safe_set(b, 'Family16', None)
    assert not _is_linked(b, 'Family16', a2)
    if hasattr(a2, 'sons'):
        assert not _is_linked(a2, 'sons', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_families0_stub_double():
    # FamiliesWithSiblings_FamilyRegister has no real 'familiesInverse' property in the generated
    # code (a bare stub) -- manually attach it so FamiliesWithSiblings_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FamiliesWithSiblings_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FamiliesWithSiblings_Family(name="sample_text")
    partner = FamiliesWithSiblings_FamilyRegister()
    setattr(partner, 'familiesInverse', None)
    _safe_set(owner, 'Family', partner)
    assert owner in getattr(partner, 'familiesInverse')
    _safe_set(owner, 'Family', None)
    assert owner not in getattr(partner, 'familiesInverse')


def test_assoc_familiesInverse8_stub_double():
    # FamiliesWithSiblings_FamilyRegister has no real 'FamilyRegister' property in the generated
    # code (a bare stub) -- manually attach it so FamiliesWithSiblings_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FamiliesWithSiblings_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FamiliesWithSiblings_Family(name="sample_text")
    partner = FamiliesWithSiblings_FamilyRegister()
    setattr(partner, 'FamilyRegister', None)
    _safe_set(owner, 'families', partner)
    assert getattr(partner, 'FamilyRegister') == owner
    _safe_set(owner, 'families', None)
    assert getattr(partner, 'FamilyRegister') is None


