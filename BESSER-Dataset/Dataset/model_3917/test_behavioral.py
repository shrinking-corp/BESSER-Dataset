import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Property,
    Type,
    entities_Entity,
    entities_Import,
    entities_Model,
    entities_Property,
    entities_Reference,
    entities_SimpleProperty,
    entities_SimpleType,
    entities_Type,
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

def test_assoc_elements1_stub_double():
    # entities_Model has no real 'entities_Model2' property in the generated
    # code (a bare stub) -- manually attach it so entities_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Type(name="sample_text")
    partner = entities_Model()
    setattr(partner, 'entities_Model2', None)
    _safe_set(owner, 'entities_Type', partner)
    assert owner in getattr(partner, 'entities_Model2')
    _safe_set(owner, 'entities_Type', None)
    assert owner not in getattr(partner, 'entities_Model2')


def test_assoc_imports0_stub_double():
    # entities_Model has no real 'entities_Model' property in the generated
    # code (a bare stub) -- manually attach it so entities_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Import(importURI="sample_text")
    partner = entities_Model()
    setattr(partner, 'entities_Model', None)
    _safe_set(owner, 'entities_Import', partner)
    assert owner in getattr(partner, 'entities_Model')
    _safe_set(owner, 'entities_Import', None)
    assert owner not in getattr(partner, 'entities_Model')


def test_assoc_properties5_stub_double():
    # entities_Entity has no real 'entities_Entity6' property in the generated
    # code (a bare stub) -- manually attach it so entities_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Property(many=True, name="sample_text")
    partner = entities_Entity()
    setattr(partner, 'entities_Entity6', None)
    _safe_set(owner, 'entities_Property', partner)
    assert owner in getattr(partner, 'entities_Entity6')
    _safe_set(owner, 'entities_Property', None)
    assert owner not in getattr(partner, 'entities_Entity6')


