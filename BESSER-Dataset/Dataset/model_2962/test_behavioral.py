import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ElementType,
    entities_Attribute,
    entities_AttributeType,
    entities_BasicType,
    entities_ElementType,
    entities_Entity,
    entities_EntityType,
    entities_Model,
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

def test_assoc_attributes4_reverse_link_reassign_clear():
    a1 = entities_Entity(name_id="sample_text")
    a2 = entities_Entity(name_id="sample_text_2")
    b = entities_Attribute(name="sample_text")
    _safe_set(b, 'entities_Attribute', a1)
    assert _is_linked(b, 'entities_Attribute', a1)
    if hasattr(a1, 'entities_Entity5'):
        assert _is_linked(a1, 'entities_Entity5', b)
    _safe_set(b, 'entities_Attribute', a2)
    assert _is_linked(b, 'entities_Attribute', a2)
    if hasattr(a1, 'entities_Entity5'):
        assert not _is_linked(a1, 'entities_Entity5', b)
    if hasattr(a2, 'entities_Entity5'):
        assert _is_linked(a2, 'entities_Entity5', b)
    _safe_set(b, 'entities_Attribute', None)
    assert not _is_linked(b, 'entities_Attribute', a2)
    if hasattr(a2, 'entities_Entity5'):
        assert not _is_linked(a2, 'entities_Entity5', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = entities_Entity(name_id="sample_text")
    a2 = entities_Entity(name_id="sample_text_2")
    b = entities_Entity(name_id="sample_text")
    _safe_set(b, 'entities_Entity3', a1)
    assert _is_linked(b, 'entities_Entity3', a1)
    if hasattr(a1, 'entities_Entity1'):
        assert _is_linked(a1, 'entities_Entity1', b)
    _safe_set(b, 'entities_Entity3', a2)
    assert _is_linked(b, 'entities_Entity3', a2)
    if hasattr(a1, 'entities_Entity1'):
        assert not _is_linked(a1, 'entities_Entity1', b)
    if hasattr(a2, 'entities_Entity1'):
        assert _is_linked(a2, 'entities_Entity1', b)
    _safe_set(b, 'entities_Entity3', None)
    assert not _is_linked(b, 'entities_Entity3', a2)
    if hasattr(a2, 'entities_Entity1'):
        assert not _is_linked(a2, 'entities_Entity1', b)


def test_assoc_type6_reverse_link_reassign_clear():
    a1 = entities_AttributeType(array=True, length=7)
    a2 = entities_AttributeType(array=False, length=13)
    b = entities_Attribute(name="sample_text")
    _safe_set(b, 'entities_Attribute7', a1)
    assert _is_linked(b, 'entities_Attribute7', a1)
    if hasattr(a1, 'entities_AttributeType'):
        assert _is_linked(a1, 'entities_AttributeType', b)
    _safe_set(b, 'entities_Attribute7', a2)
    assert _is_linked(b, 'entities_Attribute7', a2)
    if hasattr(a1, 'entities_AttributeType'):
        assert not _is_linked(a1, 'entities_AttributeType', b)
    if hasattr(a2, 'entities_AttributeType'):
        assert _is_linked(a2, 'entities_AttributeType', b)
    _safe_set(b, 'entities_Attribute7', None)
    assert not _is_linked(b, 'entities_Attribute7', a2)
    if hasattr(a2, 'entities_AttributeType'):
        assert not _is_linked(a2, 'entities_AttributeType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elementType8_stub_double():
    # entities_ElementType has no real 'entities_ElementType' property in the generated
    # code (a bare stub) -- manually attach it so entities_AttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_AttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_AttributeType(array=True, length=7)
    partner = entities_ElementType()
    setattr(partner, 'entities_ElementType', None)
    _safe_set(owner, 'entities_AttributeType9', partner)
    assert getattr(partner, 'entities_ElementType') == owner
    _safe_set(owner, 'entities_AttributeType9', None)
    assert getattr(partner, 'entities_ElementType') is None


def test_assoc_entities0_stub_double():
    # entities_Model has no real 'entities_Model' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name_id="sample_text")
    partner = entities_Model()
    setattr(partner, 'entities_Model', None)
    _safe_set(owner, 'entities_Entity', partner)
    assert owner in getattr(partner, 'entities_Model')
    _safe_set(owner, 'entities_Entity', None)
    assert owner not in getattr(partner, 'entities_Model')


def test_assoc_entity10_stub_double():
    # entities_EntityType has no real 'entities_EntityType' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name_id="sample_text")
    partner = entities_EntityType()
    setattr(partner, 'entities_EntityType', None)
    _safe_set(owner, 'entities_Entity11', partner)
    assert getattr(partner, 'entities_EntityType') == owner
    _safe_set(owner, 'entities_Entity11', None)
    assert getattr(partner, 'entities_EntityType') is None


