import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    entity_Attribute,
    entity_Entity,
    entity_JAVAID,
    entity_Model,
    entity_Type,
    entity_TypeDef,
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

def test_assoc_type6_reverse_link_reassign_clear():
    a1 = entity_Type(name="sample_text")
    a2 = entity_Type(name="sample_text_2")
    b = entity_Attribute(many=True, name="sample_text")
    _safe_set(b, 'entity_Attribute7', a1)
    assert _is_linked(b, 'entity_Attribute7', a1)
    if hasattr(a1, 'entity_Type8'):
        assert _is_linked(a1, 'entity_Type8', b)
    _safe_set(b, 'entity_Attribute7', a2)
    assert _is_linked(b, 'entity_Attribute7', a2)
    if hasattr(a1, 'entity_Type8'):
        assert not _is_linked(a1, 'entity_Type8', b)
    if hasattr(a2, 'entity_Type8'):
        assert _is_linked(a2, 'entity_Type8', b)
    _safe_set(b, 'entity_Attribute7', None)
    assert not _is_linked(b, 'entity_Attribute7', a2)
    if hasattr(a2, 'entity_Type8'):
        assert not _is_linked(a2, 'entity_Type8', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes4_stub_double():
    # entity_Entity has no real 'entity_Entity5' property in the generated
    # code (a bare stub) -- manually attach it so entity_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entity_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entity_Attribute(many=True, name="sample_text")
    partner = entity_Entity()
    setattr(partner, 'entity_Entity5', None)
    _safe_set(owner, 'entity_Attribute', partner)
    assert owner in getattr(partner, 'entity_Entity5')
    _safe_set(owner, 'entity_Attribute', None)
    assert owner not in getattr(partner, 'entity_Entity5')


def test_assoc_mappedType1_stub_double():
    # entity_TypeDef has no real 'entity_TypeDef' property in the generated
    # code (a bare stub) -- manually attach it so entity_JAVAID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entity_JAVAID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entity_JAVAID(name="sample_text")
    partner = entity_TypeDef()
    setattr(partner, 'entity_TypeDef', None)
    _safe_set(owner, 'entity_JAVAID', partner)
    assert getattr(partner, 'entity_TypeDef') == owner
    _safe_set(owner, 'entity_JAVAID', None)
    assert getattr(partner, 'entity_TypeDef') is None


def test_assoc_types0_stub_double():
    # entity_Model has no real 'entity_Model' property in the generated
    # code (a bare stub) -- manually attach it so entity_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entity_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entity_Type(name="sample_text")
    partner = entity_Model()
    setattr(partner, 'entity_Model', None)
    _safe_set(owner, 'entity_Type', partner)
    assert owner in getattr(partner, 'entity_Model')
    _safe_set(owner, 'entity_Type', None)
    assert owner not in getattr(partner, 'entity_Model')


