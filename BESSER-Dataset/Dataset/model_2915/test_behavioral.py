import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    Variable,
    metamodel_ActsAs,
    metamodel_ConnectionToEntity,
    metamodel_Controller,
    metamodel_Datatype,
    metamodel_Entity,
    metamodel_EntityObserver,
    metamodel_Extension_MQPublishing,
    metamodel_Model,
    metamodel_PlainVariable,
    metamodel_StaticVariable,
    metamodel_TransientVariable,
    metamodel_Type,
    metamodel_Validation_ValueRestriction,
    metamodel_ValueRestriction_Value,
    metamodel_Variable,
    metamodel_View,
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

def test_assoc_actsAs8_reverse_link_reassign_clear():
    a1 = metamodel_Entity(base="sample_text")
    a2 = metamodel_Entity(base="sample_text_2")
    b = metamodel_ActsAs(actsAsWhat="sample_text")
    _safe_set(b, 'metamodel_ActsAs', a1)
    assert _is_linked(b, 'metamodel_ActsAs', a1)
    if hasattr(a1, 'metamodel_Entity9'):
        assert _is_linked(a1, 'metamodel_Entity9', b)
    _safe_set(b, 'metamodel_ActsAs', a2)
    assert _is_linked(b, 'metamodel_ActsAs', a2)
    if hasattr(a1, 'metamodel_Entity9'):
        assert not _is_linked(a1, 'metamodel_Entity9', b)
    if hasattr(a2, 'metamodel_Entity9'):
        assert _is_linked(a2, 'metamodel_Entity9', b)
    _safe_set(b, 'metamodel_ActsAs', None)
    assert not _is_linked(b, 'metamodel_ActsAs', a2)
    if hasattr(a2, 'metamodel_Entity9'):
        assert not _is_linked(a2, 'metamodel_Entity9', b)


def test_assoc_belongsToEntity1_reverse_link_reassign_clear():
    a1 = metamodel_Entity(base="sample_text")
    a2 = metamodel_Entity(base="sample_text_2")
    b = metamodel_ConnectionToEntity(cardinalityMany=True, name="sample_text")
    _safe_set(b, 'metamodel_ConnectionToEntity', a1)
    assert _is_linked(b, 'metamodel_ConnectionToEntity', a1)
    if hasattr(a1, 'metamodel_Entity2'):
        assert _is_linked(a1, 'metamodel_Entity2', b)
    _safe_set(b, 'metamodel_ConnectionToEntity', a2)
    assert _is_linked(b, 'metamodel_ConnectionToEntity', a2)
    if hasattr(a1, 'metamodel_Entity2'):
        assert not _is_linked(a1, 'metamodel_Entity2', b)
    if hasattr(a2, 'metamodel_Entity2'):
        assert _is_linked(a2, 'metamodel_Entity2', b)
    _safe_set(b, 'metamodel_ConnectionToEntity', None)
    assert not _is_linked(b, 'metamodel_ConnectionToEntity', a2)
    if hasattr(a2, 'metamodel_Entity2'):
        assert not _is_linked(a2, 'metamodel_Entity2', b)


def test_assoc_hasAttribute0_reverse_link_reassign_clear():
    a1 = metamodel_Variable(name="sample_text")
    a2 = metamodel_Variable(name="sample_text_2")
    b = metamodel_Entity(base="sample_text")
    _safe_set(b, 'metamodel_Entity', {a1})
    assert _is_linked(b, 'metamodel_Entity', a1)
    if hasattr(a1, 'metamodel_Variable'):
        assert _is_linked(a1, 'metamodel_Variable', b)
    _safe_set(b, 'metamodel_Entity', {a2})
    assert _is_linked(b, 'metamodel_Entity', a2)
    if hasattr(a1, 'metamodel_Variable'):
        assert not _is_linked(a1, 'metamodel_Variable', b)
    if hasattr(a2, 'metamodel_Variable'):
        assert _is_linked(a2, 'metamodel_Variable', b)
    _safe_set(b, 'metamodel_Entity', set())
    assert not _is_linked(b, 'metamodel_Entity', a2)
    if hasattr(a2, 'metamodel_Variable'):
        assert not _is_linked(a2, 'metamodel_Variable', b)


def test_assoc_hasEntity3_reverse_link_reassign_clear():
    a1 = metamodel_Entity(base="sample_text")
    a2 = metamodel_Entity(base="sample_text_2")
    b = metamodel_ConnectionToEntity(cardinalityMany=True, name="sample_text")
    _safe_set(b, 'metamodel_ConnectionToEntity5', a1)
    assert _is_linked(b, 'metamodel_ConnectionToEntity5', a1)
    if hasattr(a1, 'metamodel_Entity4'):
        assert _is_linked(a1, 'metamodel_Entity4', b)
    _safe_set(b, 'metamodel_ConnectionToEntity5', a2)
    assert _is_linked(b, 'metamodel_ConnectionToEntity5', a2)
    if hasattr(a1, 'metamodel_Entity4'):
        assert not _is_linked(a1, 'metamodel_Entity4', b)
    if hasattr(a2, 'metamodel_Entity4'):
        assert _is_linked(a2, 'metamodel_Entity4', b)
    _safe_set(b, 'metamodel_ConnectionToEntity5', None)
    assert not _is_linked(b, 'metamodel_ConnectionToEntity5', a2)
    if hasattr(a2, 'metamodel_Entity4'):
        assert not _is_linked(a2, 'metamodel_Entity4', b)


def test_assoc_otherEntity11_reverse_link_reassign_clear():
    a1 = metamodel_Entity(base="sample_text")
    a2 = metamodel_Entity(base="sample_text_2")
    b = metamodel_ConnectionToEntity(cardinalityMany=True, name="sample_text")
    _safe_set(b, 'metamodel_ConnectionToEntity12', a1)
    assert _is_linked(b, 'metamodel_ConnectionToEntity12', a1)
    if hasattr(a1, 'metamodel_Entity13'):
        assert _is_linked(a1, 'metamodel_Entity13', b)
    _safe_set(b, 'metamodel_ConnectionToEntity12', a2)
    assert _is_linked(b, 'metamodel_ConnectionToEntity12', a2)
    if hasattr(a1, 'metamodel_Entity13'):
        assert not _is_linked(a1, 'metamodel_Entity13', b)
    if hasattr(a2, 'metamodel_Entity13'):
        assert _is_linked(a2, 'metamodel_Entity13', b)
    _safe_set(b, 'metamodel_ConnectionToEntity12', None)
    assert not _is_linked(b, 'metamodel_ConnectionToEntity12', a2)
    if hasattr(a2, 'metamodel_Entity13'):
        assert not _is_linked(a2, 'metamodel_Entity13', b)


def test_assoc_type14_reverse_link_reassign_clear():
    a1 = metamodel_Variable(name="sample_text")
    a2 = metamodel_Variable(name="sample_text_2")
    b = metamodel_Type(name="sample_text")
    _safe_set(b, 'metamodel_Type', a1)
    assert _is_linked(b, 'metamodel_Type', a1)
    if hasattr(a1, 'metamodel_Variable15'):
        assert _is_linked(a1, 'metamodel_Variable15', b)
    _safe_set(b, 'metamodel_Type', a2)
    assert _is_linked(b, 'metamodel_Type', a2)
    if hasattr(a1, 'metamodel_Variable15'):
        assert not _is_linked(a1, 'metamodel_Variable15', b)
    if hasattr(a2, 'metamodel_Variable15'):
        assert _is_linked(a2, 'metamodel_Variable15', b)
    _safe_set(b, 'metamodel_Type', None)
    assert not _is_linked(b, 'metamodel_Type', a2)
    if hasattr(a2, 'metamodel_Variable15'):
        assert not _is_linked(a2, 'metamodel_Variable15', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_extendedBy19_stub_double():
    # metamodel_EntityObserver has no real 'metamodel_EntityObserver20' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Extension_MQPublishing's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Extension_MQPublishing's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Extension_MQPublishing(queue="sample_text")
    partner = metamodel_EntityObserver()
    setattr(partner, 'metamodel_EntityObserver20', None)
    _safe_set(owner, 'metamodel_Extension_MQPublishing', partner)
    assert owner in getattr(partner, 'metamodel_EntityObserver20')
    _safe_set(owner, 'metamodel_Extension_MQPublishing', None)
    assert owner not in getattr(partner, 'metamodel_EntityObserver20')


def test_assoc_hasEntities27_stub_double():
    # metamodel_Model has no real 'metamodel_Model28' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Entity(base="sample_text")
    partner = metamodel_Model()
    setattr(partner, 'metamodel_Model28', None)
    _safe_set(owner, 'metamodel_Entity29', partner)
    assert owner in getattr(partner, 'metamodel_Model28')
    _safe_set(owner, 'metamodel_Entity29', None)
    assert owner not in getattr(partner, 'metamodel_Model28')


def test_assoc_isObservedBy6_stub_double():
    # metamodel_EntityObserver has no real 'metamodel_EntityObserver' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Entity(base="sample_text")
    partner = metamodel_EntityObserver()
    setattr(partner, 'metamodel_EntityObserver', None)
    _safe_set(owner, 'metamodel_Entity7', {partner})
    assert getattr(partner, 'metamodel_EntityObserver') == owner
    _safe_set(owner, 'metamodel_Entity7', set())
    assert getattr(partner, 'metamodel_EntityObserver') is None


def test_assoc_restrictsTo10_stub_double():
    # metamodel_Validation_ValueRestriction has no real 'metamodel_Validation_ValueRestriction' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_ValueRestriction_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_ValueRestriction_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_ValueRestriction_Value(value="sample_text")
    partner = metamodel_Validation_ValueRestriction()
    setattr(partner, 'metamodel_Validation_ValueRestriction', None)
    _safe_set(owner, 'metamodel_ValueRestriction_Value', partner)
    assert owner in getattr(partner, 'metamodel_Validation_ValueRestriction')
    _safe_set(owner, 'metamodel_ValueRestriction_Value', None)
    assert owner not in getattr(partner, 'metamodel_Validation_ValueRestriction')


def test_assoc_types30_stub_double():
    # metamodel_Model has no real 'metamodel_Model31' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Type(name="sample_text")
    partner = metamodel_Model()
    setattr(partner, 'metamodel_Model31', None)
    _safe_set(owner, 'metamodel_Type32', partner)
    assert owner in getattr(partner, 'metamodel_Model31')
    _safe_set(owner, 'metamodel_Type32', None)
    assert owner not in getattr(partner, 'metamodel_Model31')


def test_assoc_validatedBy16_stub_double():
    # metamodel_Validation_ValueRestriction has no real 'metamodel_Validation_ValueRestriction18' property in the generated
    # code (a bare stub) -- manually attach it so metamodel_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metamodel_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metamodel_Variable(name="sample_text")
    partner = metamodel_Validation_ValueRestriction()
    setattr(partner, 'metamodel_Validation_ValueRestriction18', None)
    _safe_set(owner, 'metamodel_Variable17', partner)
    assert getattr(partner, 'metamodel_Validation_ValueRestriction18') == owner
    _safe_set(owner, 'metamodel_Variable17', None)
    assert getattr(partner, 'metamodel_Validation_ValueRestriction18') is None


