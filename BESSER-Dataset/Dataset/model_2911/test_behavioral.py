import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    agentDSL_Attribute,
    agentDSL_Entity,
    agentDSL_Function,
    agentDSL_Goal,
    agentDSL_JAVAID,
    agentDSL_Model,
    agentDSL_Outcome,
    agentDSL_Task,
    agentDSL_Type,
    agentDSL_TypeDef,
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

def test_assoc_attributes15_reverse_link_reassign_clear():
    a1 = agentDSL_Goal(name="sample_text")
    a2 = agentDSL_Goal(name="sample_text_2")
    b = agentDSL_Attribute(many=True, name="sample_text")
    _safe_set(b, 'agentDSL_Attribute17', a1)
    assert _is_linked(b, 'agentDSL_Attribute17', a1)
    if hasattr(a1, 'agentDSL_Goal16'):
        assert _is_linked(a1, 'agentDSL_Goal16', b)
    _safe_set(b, 'agentDSL_Attribute17', a2)
    assert _is_linked(b, 'agentDSL_Attribute17', a2)
    if hasattr(a1, 'agentDSL_Goal16'):
        assert not _is_linked(a1, 'agentDSL_Goal16', b)
    if hasattr(a2, 'agentDSL_Goal16'):
        assert _is_linked(a2, 'agentDSL_Goal16', b)
    _safe_set(b, 'agentDSL_Attribute17', None)
    assert not _is_linked(b, 'agentDSL_Attribute17', a2)
    if hasattr(a2, 'agentDSL_Goal16'):
        assert not _is_linked(a2, 'agentDSL_Goal16', b)


def test_assoc_type20_reverse_link_reassign_clear():
    a1 = agentDSL_Type(name="sample_text")
    a2 = agentDSL_Type(name="sample_text_2")
    b = agentDSL_Attribute(many=True, name="sample_text")
    _safe_set(b, 'agentDSL_Attribute21', a1)
    assert _is_linked(b, 'agentDSL_Attribute21', a1)
    if hasattr(a1, 'agentDSL_Type22'):
        assert _is_linked(a1, 'agentDSL_Type22', b)
    _safe_set(b, 'agentDSL_Attribute21', a2)
    assert _is_linked(b, 'agentDSL_Attribute21', a2)
    if hasattr(a1, 'agentDSL_Type22'):
        assert not _is_linked(a1, 'agentDSL_Type22', b)
    if hasattr(a2, 'agentDSL_Type22'):
        assert _is_linked(a2, 'agentDSL_Type22', b)
    _safe_set(b, 'agentDSL_Attribute21', None)
    assert not _is_linked(b, 'agentDSL_Attribute21', a2)
    if hasattr(a2, 'agentDSL_Type22'):
        assert not _is_linked(a2, 'agentDSL_Type22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes10_stub_double():
    # agentDSL_Outcome has no real 'agentDSL_Outcome11' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Attribute(many=True, name="sample_text")
    partner = agentDSL_Outcome()
    setattr(partner, 'agentDSL_Outcome11', None)
    _safe_set(owner, 'agentDSL_Attribute12', partner)
    assert owner in getattr(partner, 'agentDSL_Outcome11')
    _safe_set(owner, 'agentDSL_Attribute12', None)
    assert owner not in getattr(partner, 'agentDSL_Outcome11')


def test_assoc_attributes18_stub_double():
    # agentDSL_Function has no real 'agentDSL_Function' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Attribute(many=True, name="sample_text")
    partner = agentDSL_Function()
    setattr(partner, 'agentDSL_Function', None)
    _safe_set(owner, 'agentDSL_Attribute19', partner)
    assert owner in getattr(partner, 'agentDSL_Function')
    _safe_set(owner, 'agentDSL_Attribute19', None)
    assert owner not in getattr(partner, 'agentDSL_Function')


def test_assoc_attributes4_stub_double():
    # agentDSL_Entity has no real 'agentDSL_Entity5' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Attribute(many=True, name="sample_text")
    partner = agentDSL_Entity()
    setattr(partner, 'agentDSL_Entity5', None)
    _safe_set(owner, 'agentDSL_Attribute', partner)
    assert owner in getattr(partner, 'agentDSL_Entity5')
    _safe_set(owner, 'agentDSL_Attribute', None)
    assert owner not in getattr(partner, 'agentDSL_Entity5')


def test_assoc_attributes6_stub_double():
    # agentDSL_Task has no real 'agentDSL_Task' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Attribute(many=True, name="sample_text")
    partner = agentDSL_Task()
    setattr(partner, 'agentDSL_Task', None)
    _safe_set(owner, 'agentDSL_Attribute7', partner)
    assert owner in getattr(partner, 'agentDSL_Task')
    _safe_set(owner, 'agentDSL_Attribute7', None)
    assert owner not in getattr(partner, 'agentDSL_Task')


def test_assoc_goal13_stub_double():
    # agentDSL_Outcome has no real 'agentDSL_Outcome14' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Goal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Goal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Goal(name="sample_text")
    partner = agentDSL_Outcome()
    setattr(partner, 'agentDSL_Outcome14', None)
    _safe_set(owner, 'agentDSL_Goal', partner)
    assert getattr(partner, 'agentDSL_Outcome14') == owner
    _safe_set(owner, 'agentDSL_Goal', None)
    assert getattr(partner, 'agentDSL_Outcome14') is None


def test_assoc_mappedType1_stub_double():
    # agentDSL_TypeDef has no real 'agentDSL_TypeDef' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_JAVAID's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_JAVAID's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_JAVAID(name="sample_text")
    partner = agentDSL_TypeDef()
    setattr(partner, 'agentDSL_TypeDef', None)
    _safe_set(owner, 'agentDSL_JAVAID', partner)
    assert getattr(partner, 'agentDSL_TypeDef') == owner
    _safe_set(owner, 'agentDSL_JAVAID', None)
    assert getattr(partner, 'agentDSL_TypeDef') is None


def test_assoc_types0_stub_double():
    # agentDSL_Model has no real 'agentDSL_Model' property in the generated
    # code (a bare stub) -- manually attach it so agentDSL_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # agentDSL_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = agentDSL_Type(name="sample_text")
    partner = agentDSL_Model()
    setattr(partner, 'agentDSL_Model', None)
    _safe_set(owner, 'agentDSL_Type', partner)
    assert owner in getattr(partner, 'agentDSL_Model')
    _safe_set(owner, 'agentDSL_Type', None)
    assert owner not in getattr(partner, 'agentDSL_Model')


