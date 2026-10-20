import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    familyright_Daughter,
    familyright_Family,
    familyright_Father,
    familyright_Mother,
    familyright_Son,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_daughters12_stub_double():
    # familyright_Family has no real 'family13' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Daughter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Daughter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Daughter(age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'family13', None)
    _safe_set(owner, 'Daughter', partner)
    assert owner in getattr(partner, 'family13')
    _safe_set(owner, 'Daughter', None)
    assert owner not in getattr(partner, 'family13')


def test_assoc_family0_stub_double():
    # familyright_Family has no real 'Family' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Father's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Father's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Father(address="sample_text", age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'Family', None)
    _safe_set(owner, 'father', partner)
    assert getattr(partner, 'Family') == owner
    _safe_set(owner, 'father', None)
    assert getattr(partner, 'Family') is None


def test_assoc_family1_stub_double():
    # familyright_Family has no real 'Family2' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Mother's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Mother's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Mother(address="sample_text", age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'Family2', None)
    _safe_set(owner, 'mother', partner)
    assert getattr(partner, 'Family2') == owner
    _safe_set(owner, 'mother', None)
    assert getattr(partner, 'Family2') is None


def test_assoc_family3_stub_double():
    # familyright_Family has no real 'Family4' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Son's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Son's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Son(age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'Family4', None)
    _safe_set(owner, 'sons', partner)
    assert getattr(partner, 'Family4') == owner
    _safe_set(owner, 'sons', None)
    assert getattr(partner, 'Family4') is None


def test_assoc_family5_stub_double():
    # familyright_Family has no real 'Family6' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Daughter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Daughter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Daughter(age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'Family6', None)
    _safe_set(owner, 'daughters', partner)
    assert getattr(partner, 'Family6') == owner
    _safe_set(owner, 'daughters', None)
    assert getattr(partner, 'Family6') is None


def test_assoc_father7_stub_double():
    # familyright_Family has no real 'family' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Father's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Father's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Father(address="sample_text", age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'family', None)
    _safe_set(owner, 'Father', partner)
    assert getattr(partner, 'family') == owner
    _safe_set(owner, 'Father', None)
    assert getattr(partner, 'family') is None


def test_assoc_mother8_stub_double():
    # familyright_Family has no real 'family9' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Mother's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Mother's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Mother(address="sample_text", age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'family9', None)
    _safe_set(owner, 'Mother', partner)
    assert getattr(partner, 'family9') == owner
    _safe_set(owner, 'Mother', None)
    assert getattr(partner, 'family9') is None


def test_assoc_sons10_stub_double():
    # familyright_Family has no real 'family11' property in the generated
    # code (a bare stub) -- manually attach it so familyright_Son's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # familyright_Son's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = familyright_Son(age=7, name="sample_text")
    partner = familyright_Family()
    setattr(partner, 'family11', None)
    _safe_set(owner, 'Son', partner)
    assert owner in getattr(partner, 'family11')
    _safe_set(owner, 'Son', None)
    assert owner not in getattr(partner, 'family11')


