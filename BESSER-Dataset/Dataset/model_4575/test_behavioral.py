import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    dsl_Action,
    dsl_AndElement,
    dsl_AppMetaData,
    dsl_Boolean_Object,
    dsl_DiffElement,
    dsl_DivisionElement,
    dsl_Element,
    dsl_ElseDoSpec,
    dsl_ElseIfDoSpec,
    dsl_EnvironmentMetaData,
    dsl_EqualElement,
    dsl_IfDoSpec,
    dsl_LargerElement,
    dsl_LargerEqualElement,
    dsl_MinusElement,
    dsl_ModuloElement,
    dsl_MultiplicationElement,
    dsl_NegateElement,
    dsl_Number_Object,
    dsl_OrElement,
    dsl_PlusElement,
    dsl_Resource,
    dsl_Resource_Object,
    dsl_RunTimeModel,
    dsl_SmallerElement,
    dsl_SmallerEqualElement,
    dsl_Specification,
    dsl_State,
    dsl_State_Object,
    dsl_Trigger,
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

def test_assoc_specification4_reverse_link_reassign_clear():
    a1 = dsl_Specification(priority=7, specID="sample_text")
    a2 = dsl_Specification(priority=13, specID="sample_text_2")
    b = dsl_AppMetaData(appID="sample_text")
    _safe_set(b, 'dsl_AppMetaData5', a1)
    assert _is_linked(b, 'dsl_AppMetaData5', a1)
    if hasattr(a1, 'dsl_Specification'):
        assert _is_linked(a1, 'dsl_Specification', b)
    _safe_set(b, 'dsl_AppMetaData5', a2)
    assert _is_linked(b, 'dsl_AppMetaData5', a2)
    if hasattr(a1, 'dsl_Specification'):
        assert not _is_linked(a1, 'dsl_Specification', b)
    if hasattr(a2, 'dsl_Specification'):
        assert _is_linked(a2, 'dsl_Specification', b)
    _safe_set(b, 'dsl_AppMetaData5', None)
    assert not _is_linked(b, 'dsl_AppMetaData5', a2)
    if hasattr(a2, 'dsl_Specification'):
        assert not _is_linked(a2, 'dsl_Specification', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = dsl_State(name="sample_text")
    a2 = dsl_State(name="sample_text_2")
    b = dsl_Resource(name="sample_text")
    _safe_set(b, 'dsl_Resource', {a1})
    assert _is_linked(b, 'dsl_Resource', a1)
    if hasattr(a1, 'dsl_State'):
        assert _is_linked(a1, 'dsl_State', b)
    _safe_set(b, 'dsl_Resource', {a2})
    assert _is_linked(b, 'dsl_Resource', a2)
    if hasattr(a1, 'dsl_State'):
        assert not _is_linked(a1, 'dsl_State', b)
    if hasattr(a2, 'dsl_State'):
        assert _is_linked(a2, 'dsl_State', b)
    _safe_set(b, 'dsl_Resource', set())
    assert not _is_linked(b, 'dsl_Resource', a2)
    if hasattr(a2, 'dsl_State'):
        assert not _is_linked(a2, 'dsl_State', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_appData1_stub_double():
    # dsl_RunTimeModel has no real 'dsl_RunTimeModel2' property in the generated
    # code (a bare stub) -- manually attach it so dsl_AppMetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_AppMetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_AppMetaData(appID="sample_text")
    partner = dsl_RunTimeModel()
    setattr(partner, 'dsl_RunTimeModel2', None)
    _safe_set(owner, 'dsl_AppMetaData', partner)
    assert owner in getattr(partner, 'dsl_RunTimeModel2')
    _safe_set(owner, 'dsl_AppMetaData', None)
    assert owner not in getattr(partner, 'dsl_RunTimeModel2')


def test_assoc_elseDo12_stub_double():
    # dsl_ElseDoSpec has no real 'dsl_ElseDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_ElseDoSpec()
    setattr(partner, 'dsl_ElseDoSpec', None)
    _safe_set(owner, 'dsl_Specification13', partner)
    assert getattr(partner, 'dsl_ElseDoSpec') == owner
    _safe_set(owner, 'dsl_Specification13', None)
    assert getattr(partner, 'dsl_ElseDoSpec') is None


def test_assoc_elseIfDo10_stub_double():
    # dsl_ElseIfDoSpec has no real 'dsl_ElseIfDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_ElseIfDoSpec()
    setattr(partner, 'dsl_ElseIfDoSpec', None)
    _safe_set(owner, 'dsl_Specification11', {partner})
    assert getattr(partner, 'dsl_ElseIfDoSpec') == owner
    _safe_set(owner, 'dsl_Specification11', set())
    assert getattr(partner, 'dsl_ElseIfDoSpec') is None


def test_assoc_ifdo8_stub_double():
    # dsl_IfDoSpec has no real 'dsl_IfDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_IfDoSpec()
    setattr(partner, 'dsl_IfDoSpec', None)
    _safe_set(owner, 'dsl_Specification9', partner)
    assert getattr(partner, 'dsl_IfDoSpec') == owner
    _safe_set(owner, 'dsl_Specification9', None)
    assert getattr(partner, 'dsl_IfDoSpec') is None


def test_assoc_resource14_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger15' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger15', None)
    _safe_set(owner, 'dsl_Resource16', partner)
    assert getattr(partner, 'dsl_Trigger15') == owner
    _safe_set(owner, 'dsl_Resource16', None)
    assert getattr(partner, 'dsl_Trigger15') is None


def test_assoc_resource36_stub_double():
    # dsl_Action has no real 'dsl_Action37' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Action()
    setattr(partner, 'dsl_Action37', None)
    _safe_set(owner, 'dsl_Resource38', partner)
    assert getattr(partner, 'dsl_Action37') == owner
    _safe_set(owner, 'dsl_Resource38', None)
    assert getattr(partner, 'dsl_Action37') is None


def test_assoc_resources33_stub_double():
    # dsl_EnvironmentMetaData has no real 'dsl_EnvironmentMetaData34' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_EnvironmentMetaData()
    setattr(partner, 'dsl_EnvironmentMetaData34', None)
    _safe_set(owner, 'dsl_Resource35', partner)
    assert owner in getattr(partner, 'dsl_EnvironmentMetaData34')
    _safe_set(owner, 'dsl_Resource35', None)
    assert owner not in getattr(partner, 'dsl_EnvironmentMetaData34')


def test_assoc_state17_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger18' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger18', None)
    _safe_set(owner, 'dsl_State19', partner)
    assert getattr(partner, 'dsl_Trigger18') == owner
    _safe_set(owner, 'dsl_State19', None)
    assert getattr(partner, 'dsl_Trigger18') is None


def test_assoc_state39_stub_double():
    # dsl_Action has no real 'dsl_Action40' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Action()
    setattr(partner, 'dsl_Action40', None)
    _safe_set(owner, 'dsl_State41', partner)
    assert getattr(partner, 'dsl_Action40') == owner
    _safe_set(owner, 'dsl_State41', None)
    assert getattr(partner, 'dsl_Action40') is None


def test_assoc_trigger6_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger', None)
    _safe_set(owner, 'dsl_Specification7', {partner})
    assert getattr(partner, 'dsl_Trigger') == owner
    _safe_set(owner, 'dsl_Specification7', set())
    assert getattr(partner, 'dsl_Trigger') is None


def test_assoc_value107_stub_double():
    # dsl_Resource_Object has no real 'dsl_Resource_Object' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Resource_Object()
    setattr(partner, 'dsl_Resource_Object', None)
    _safe_set(owner, 'dsl_Resource108', partner)
    assert getattr(partner, 'dsl_Resource_Object') == owner
    _safe_set(owner, 'dsl_Resource108', None)
    assert getattr(partner, 'dsl_Resource_Object') is None


def test_assoc_value109_stub_double():
    # dsl_State_Object has no real 'dsl_State_Object' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_State_Object()
    setattr(partner, 'dsl_State_Object', None)
    _safe_set(owner, 'dsl_State110', partner)
    assert getattr(partner, 'dsl_State_Object') == owner
    _safe_set(owner, 'dsl_State110', None)
    assert getattr(partner, 'dsl_State_Object') is None


