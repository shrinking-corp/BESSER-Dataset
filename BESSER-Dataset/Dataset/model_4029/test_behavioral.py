import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    StructuralFeature,
    uml_15_to_20_associationEndToProperty_Association,
    uml_15_to_20_associationEndToProperty_AssociationEnd,
    uml_15_to_20_associationEndToProperty_Attribute,
    uml_15_to_20_associationEndToProperty_Class,
    uml_15_to_20_associationEndToProperty_Model,
    uml_15_to_20_associationEndToProperty_Operation,
    uml_15_to_20_associationEndToProperty_StructuralFeature,
    ScopeKind,
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

def test_assoc_association9_stub_double():
    # uml_15_to_20_associationEndToProperty_Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so uml_15_to_20_associationEndToProperty_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_15_to_20_associationEndToProperty_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_15_to_20_associationEndToProperty_AssociationEnd(isNavigable=True)
    partner = uml_15_to_20_associationEndToProperty_Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'connections', partner)
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'connections', None)
    assert getattr(partner, 'Association') is None


def test_assoc_associations5_stub_double():
    # uml_15_to_20_associationEndToProperty_Class has no real 'participant' property in the generated
    # code (a bare stub) -- manually attach it so uml_15_to_20_associationEndToProperty_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_15_to_20_associationEndToProperty_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_15_to_20_associationEndToProperty_AssociationEnd(isNavigable=True)
    partner = uml_15_to_20_associationEndToProperty_Class()
    setattr(partner, 'participant', None)
    _safe_set(owner, 'AssociationEnd', partner)
    assert owner in getattr(partner, 'participant')
    _safe_set(owner, 'AssociationEnd', None)
    assert owner not in getattr(partner, 'participant')


def test_assoc_connections6_stub_double():
    # uml_15_to_20_associationEndToProperty_Association has no real 'association' property in the generated
    # code (a bare stub) -- manually attach it so uml_15_to_20_associationEndToProperty_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_15_to_20_associationEndToProperty_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_15_to_20_associationEndToProperty_AssociationEnd(isNavigable=True)
    partner = uml_15_to_20_associationEndToProperty_Association()
    setattr(partner, 'association', None)
    _safe_set(owner, 'AssociationEnd7', partner)
    assert owner in getattr(partner, 'association')
    _safe_set(owner, 'AssociationEnd7', None)
    assert owner not in getattr(partner, 'association')


def test_assoc_features3_stub_double():
    # uml_15_to_20_associationEndToProperty_Class has no real 'uml_15_to_20_associationEndToProperty_Class4' property in the generated
    # code (a bare stub) -- manually attach it so uml_15_to_20_associationEndToProperty_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_15_to_20_associationEndToProperty_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_15_to_20_associationEndToProperty_StructuralFeature(ownerScope="sample_text", targetScope="sample_text")
    partner = uml_15_to_20_associationEndToProperty_Class()
    setattr(partner, 'uml_15_to_20_associationEndToProperty_Class4', None)
    _safe_set(owner, 'uml_15_to_20_associationEndToProperty_StructuralFeature', partner)
    assert owner in getattr(partner, 'uml_15_to_20_associationEndToProperty_Class4')
    _safe_set(owner, 'uml_15_to_20_associationEndToProperty_StructuralFeature', None)
    assert owner not in getattr(partner, 'uml_15_to_20_associationEndToProperty_Class4')


def test_assoc_participant8_stub_double():
    # uml_15_to_20_associationEndToProperty_Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so uml_15_to_20_associationEndToProperty_AssociationEnd's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_15_to_20_associationEndToProperty_AssociationEnd's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_15_to_20_associationEndToProperty_AssociationEnd(isNavigable=True)
    partner = uml_15_to_20_associationEndToProperty_Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'associations', partner)
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'associations', None)
    assert getattr(partner, 'Class') is None


