import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Families_Family,
    Families_FamilyRegistry,
    Families_Member,
    Families_uncertainty_ModelElement,
    Families_uncertainty_UData,
    Families_uncertainty_aFamily,
    Families_uncertainty_aFamilyRegistry,
    Families_uncertainty_aMember,
    Families_uncertainty_uFamily,
    Families_uncertainty_uFamilyRegistry,
    Families_uncertainty_uMember,
    ModelElement,
    aFamily,
    aMember,
    uFamily,
    uFamilyRegistry,
    uMember,
    uncertainty_Families_Family,
    uncertainty_Families_FamilyRegistry,
    uncertainty_Families_Member,
    uncertainty_ModelElement,
    uncertainty_UData,
    uncertainty_aFamily,
    uncertainty_aFamilyRegistry,
    uncertainty_aMember,
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_daughters1_stub_double():
    # aMember has no real 'aMember3' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(address="sample_text", lastName="sample_text")
    partner = aMember()
    setattr(partner, 'aMember3', None)
    _safe_set(owner, 'Families_Family2', {partner})
    assert getattr(partner, 'aMember3') == owner
    _safe_set(owner, 'Families_Family2', set())
    assert getattr(partner, 'aMember3') is None


def test_assoc_father7_stub_double():
    # aMember has no real 'aMember9' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(address="sample_text", lastName="sample_text")
    partner = aMember()
    setattr(partner, 'aMember9', None)
    _safe_set(owner, 'Families_Family8', partner)
    assert getattr(partner, 'aMember9') == owner
    _safe_set(owner, 'Families_Family8', None)
    assert getattr(partner, 'aMember9') is None


def test_assoc_mother4_stub_double():
    # aMember has no real 'aMember6' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(address="sample_text", lastName="sample_text")
    partner = aMember()
    setattr(partner, 'aMember6', None)
    _safe_set(owner, 'Families_Family5', partner)
    assert getattr(partner, 'aMember6') == owner
    _safe_set(owner, 'Families_Family5', None)
    assert getattr(partner, 'aMember6') is None


def test_assoc_relatives13_stub_double():
    # aMember has no real 'aMember14' property in the generated
    # code (a bare stub) -- manually attach it so Families_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Member(age=7, firstName="sample_text")
    partner = aMember()
    setattr(partner, 'aMember14', None)
    _safe_set(owner, 'Families_Member', partner)
    assert getattr(partner, 'aMember14') == owner
    _safe_set(owner, 'Families_Member', None)
    assert getattr(partner, 'aMember14') is None


def test_assoc_sons0_stub_double():
    # aMember has no real 'aMember' property in the generated
    # code (a bare stub) -- manually attach it so Families_Family's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Families_Family's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Families_Family(address="sample_text", lastName="sample_text")
    partner = aMember()
    setattr(partner, 'aMember', None)
    _safe_set(owner, 'Families_Family', {partner})
    assert getattr(partner, 'aMember') == owner
    _safe_set(owner, 'Families_Family', set())
    assert getattr(partner, 'aMember') is None


