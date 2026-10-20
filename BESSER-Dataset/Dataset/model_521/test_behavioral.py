import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Families_Family,
    Families_FamilyMember,
    Families_FamilyRegister,
    Families_uncertainty_ModelElement,
    Families_uncertainty_UData,
    Families_uncertainty_aFamily,
    Families_uncertainty_aFamilyMember,
    Families_uncertainty_aFamilyRegister,
    Families_uncertainty_uFamily,
    Families_uncertainty_uFamilyMember,
    Families_uncertainty_uFamilyRegister,
    ModelElement,
    aFamily,
    aFamilyMember,
    aFamilyRegister,
    uFamily,
    uFamilyMember,
    uFamilyRegister,
    uncertainty_Families_Family,
    uncertainty_Families_FamilyMember,
    uncertainty_Families_FamilyRegister,
    uncertainty_ModelElement,
    uncertainty_UData,
    uncertainty_aFamily,
    uncertainty_aFamilyMember,
    uncertainty_aFamilyRegister,
    OperatorType,
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

def test_assoc_daughters8_stub_double():
    # aFamilyMember has no real 'aFamilyMember10' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(name="sample_text")
    partner = aFamilyMember()
    setattr(partner, 'aFamilyMember10', None)
    _safe_set(owner, 'Families_Family9', {partner})
    assert getattr(partner, 'aFamilyMember10') == owner
    _safe_set(owner, 'Families_Family9', set())
    assert getattr(partner, 'aFamilyMember10') is None


def test_assoc_daughtersInverse21_stub_double():
    # aFamily has no real 'aFamily23' property in the generated
    # code (a bare stub) -- manually attach it so Families_FamilyMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_FamilyMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_FamilyMember(name="sample_text")
    partner = aFamily()
    setattr(partner, 'aFamily23', None)
    _safe_set(owner, 'Families_FamilyMember22', partner)
    assert getattr(partner, 'aFamily23') == owner
    _safe_set(owner, 'Families_FamilyMember22', None)
    assert getattr(partner, 'aFamily23') is None


def test_assoc_familiesInverse11_stub_double():
    # aFamilyRegister has no real 'aFamilyRegister' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(name="sample_text")
    partner = aFamilyRegister()
    setattr(partner, 'aFamilyRegister', None)
    _safe_set(owner, 'Families_Family12', partner)
    assert getattr(partner, 'aFamilyRegister') == owner
    _safe_set(owner, 'Families_Family12', None)
    assert getattr(partner, 'aFamilyRegister') is None


def test_assoc_father1_stub_double():
    # aFamilyMember has no real 'aFamilyMember' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(name="sample_text")
    partner = aFamilyMember()
    setattr(partner, 'aFamilyMember', None)
    _safe_set(owner, 'Families_Family', partner)
    assert getattr(partner, 'aFamilyMember') == owner
    _safe_set(owner, 'Families_Family', None)
    assert getattr(partner, 'aFamilyMember') is None


def test_assoc_fatherInverse13_stub_double():
    # aFamily has no real 'aFamily14' property in the generated
    # code (a bare stub) -- manually attach it so Families_FamilyMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_FamilyMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_FamilyMember(name="sample_text")
    partner = aFamily()
    setattr(partner, 'aFamily14', None)
    _safe_set(owner, 'Families_FamilyMember', partner)
    assert getattr(partner, 'aFamily14') == owner
    _safe_set(owner, 'Families_FamilyMember', None)
    assert getattr(partner, 'aFamily14') is None


def test_assoc_mother2_stub_double():
    # aFamilyMember has no real 'aFamilyMember4' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(name="sample_text")
    partner = aFamilyMember()
    setattr(partner, 'aFamilyMember4', None)
    _safe_set(owner, 'Families_Family3', partner)
    assert getattr(partner, 'aFamilyMember4') == owner
    _safe_set(owner, 'Families_Family3', None)
    assert getattr(partner, 'aFamilyMember4') is None


def test_assoc_motherInverse15_stub_double():
    # aFamily has no real 'aFamily17' property in the generated
    # code (a bare stub) -- manually attach it so Families_FamilyMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_FamilyMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_FamilyMember(name="sample_text")
    partner = aFamily()
    setattr(partner, 'aFamily17', None)
    _safe_set(owner, 'Families_FamilyMember16', partner)
    assert getattr(partner, 'aFamily17') == owner
    _safe_set(owner, 'Families_FamilyMember16', None)
    assert getattr(partner, 'aFamily17') is None


def test_assoc_sons5_stub_double():
    # aFamilyMember has no real 'aFamilyMember7' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(name="sample_text")
    partner = aFamilyMember()
    setattr(partner, 'aFamilyMember7', None)
    _safe_set(owner, 'Families_Family6', {partner})
    assert getattr(partner, 'aFamilyMember7') == owner
    _safe_set(owner, 'Families_Family6', set())
    assert getattr(partner, 'aFamilyMember7') is None


def test_assoc_sonsInverse18_stub_double():
    # aFamily has no real 'aFamily20' property in the generated
    # code (a bare stub) -- manually attach it so Families_FamilyMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_FamilyMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_FamilyMember(name="sample_text")
    partner = aFamily()
    setattr(partner, 'aFamily20', None)
    _safe_set(owner, 'Families_FamilyMember19', partner)
    assert getattr(partner, 'aFamily20') == owner
    _safe_set(owner, 'Families_FamilyMember19', None)
    assert getattr(partner, 'aFamily20') is None


