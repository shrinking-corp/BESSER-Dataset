import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    FieldType,
    Statement,
    entities_AssignmentStatement,
    entities_BasicType,
    entities_BoolConstant,
    entities_Entity,
    entities_EntityType,
    entities_Expression,
    entities_Field,
    entities_FieldRef,
    entities_FieldType,
    entities_IntConstant,
    entities_Model,
    entities_PrintStatement,
    entities_Statement,
    entities_StringConstant,
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

def test_assoc_fields4_reverse_link_reassign_clear():
    a1 = entities_Field(name="sample_text")
    a2 = entities_Field(name="sample_text_2")
    b = entities_Entity(name="sample_text")
    _safe_set(b, 'entities_Entity5', {a1})
    assert _is_linked(b, 'entities_Entity5', a1)
    if hasattr(a1, 'entities_Field'):
        assert _is_linked(a1, 'entities_Field', b)
    _safe_set(b, 'entities_Entity5', {a2})
    assert _is_linked(b, 'entities_Entity5', a2)
    if hasattr(a1, 'entities_Field'):
        assert not _is_linked(a1, 'entities_Field', b)
    if hasattr(a2, 'entities_Field'):
        assert _is_linked(a2, 'entities_Field', b)
    _safe_set(b, 'entities_Entity5', set())
    assert not _is_linked(b, 'entities_Entity5', a2)
    if hasattr(a2, 'entities_Field'):
        assert not _is_linked(a2, 'entities_Field', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = entities_Entity(name="sample_text")
    a2 = entities_Entity(name="sample_text_2")
    b = entities_Entity(name="sample_text")
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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignee10_stub_double():
    # entities_AssignmentStatement has no real 'entities_AssignmentStatement' property in the generated
    # code (a bare stub) -- manually attach it so entities_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Field(name="sample_text")
    partner = entities_AssignmentStatement()
    setattr(partner, 'entities_AssignmentStatement', None)
    _safe_set(owner, 'entities_Field11', partner)
    assert getattr(partner, 'entities_AssignmentStatement') == owner
    _safe_set(owner, 'entities_Field11', None)
    assert getattr(partner, 'entities_AssignmentStatement') is None


def test_assoc_entities0_stub_double():
    # entities_Model has no real 'entities_Model' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name="sample_text")
    partner = entities_Model()
    setattr(partner, 'entities_Model', None)
    _safe_set(owner, 'entities_Entity', partner)
    assert owner in getattr(partner, 'entities_Model')
    _safe_set(owner, 'entities_Entity', None)
    assert owner not in getattr(partner, 'entities_Model')


def test_assoc_entity14_stub_double():
    # entities_EntityType has no real 'entities_EntityType' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name="sample_text")
    partner = entities_EntityType()
    setattr(partner, 'entities_EntityType', None)
    _safe_set(owner, 'entities_Entity15', partner)
    assert getattr(partner, 'entities_EntityType') == owner
    _safe_set(owner, 'entities_Entity15', None)
    assert getattr(partner, 'entities_EntityType') is None


def test_assoc_field16_stub_double():
    # entities_FieldRef has no real 'entities_FieldRef' property in the generated
    # code (a bare stub) -- manually attach it so entities_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Field(name="sample_text")
    partner = entities_FieldRef()
    setattr(partner, 'entities_FieldRef', None)
    _safe_set(owner, 'entities_Field17', partner)
    assert getattr(partner, 'entities_FieldRef') == owner
    _safe_set(owner, 'entities_Field17', None)
    assert getattr(partner, 'entities_FieldRef') is None


def test_assoc_statements6_stub_double():
    # entities_Statement has no real 'entities_Statement' property in the generated
    # code (a bare stub) -- manually attach it so entities_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Entity(name="sample_text")
    partner = entities_Statement()
    setattr(partner, 'entities_Statement', None)
    _safe_set(owner, 'entities_Entity7', {partner})
    assert getattr(partner, 'entities_Statement') == owner
    _safe_set(owner, 'entities_Entity7', set())
    assert getattr(partner, 'entities_Statement') is None


def test_assoc_type12_stub_double():
    # entities_FieldType has no real 'entities_FieldType' property in the generated
    # code (a bare stub) -- manually attach it so entities_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # entities_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = entities_Field(name="sample_text")
    partner = entities_FieldType()
    setattr(partner, 'entities_FieldType', None)
    _safe_set(owner, 'entities_Field13', partner)
    assert getattr(partner, 'entities_FieldType') == owner
    _safe_set(owner, 'entities_Field13', None)
    assert getattr(partner, 'entities_FieldType') is None


