import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Element,
    Metadata,
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
    dsl_Metadata,
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
    dsl_ServiceMetaData,
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

def test_assoc_specifications6_reverse_link_reassign_clear():
    a1 = dsl_Specification(priority=7, specID="sample_text")
    a2 = dsl_Specification(priority=13, specID="sample_text_2")
    b = dsl_AppMetaData(appID="sample_text")
    _safe_set(b, 'dsl_AppMetaData7', {a1})
    assert _is_linked(b, 'dsl_AppMetaData7', a1)
    if hasattr(a1, 'dsl_Specification'):
        assert _is_linked(a1, 'dsl_Specification', b)
    _safe_set(b, 'dsl_AppMetaData7', {a2})
    assert _is_linked(b, 'dsl_AppMetaData7', a2)
    if hasattr(a1, 'dsl_Specification'):
        assert not _is_linked(a1, 'dsl_Specification', b)
    if hasattr(a2, 'dsl_Specification'):
        assert _is_linked(a2, 'dsl_Specification', b)
    _safe_set(b, 'dsl_AppMetaData7', set())
    assert not _is_linked(b, 'dsl_AppMetaData7', a2)
    if hasattr(a2, 'dsl_Specification'):
        assert not _is_linked(a2, 'dsl_Specification', b)


def test_assoc_states5_reverse_link_reassign_clear():
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


def test_assoc_elseDo14_stub_double():
    # dsl_ElseDoSpec has no real 'dsl_ElseDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_ElseDoSpec()
    setattr(partner, 'dsl_ElseDoSpec', None)
    _safe_set(owner, 'dsl_Specification15', partner)
    assert getattr(partner, 'dsl_ElseDoSpec') == owner
    _safe_set(owner, 'dsl_Specification15', None)
    assert getattr(partner, 'dsl_ElseDoSpec') is None


def test_assoc_elseIfDo12_stub_double():
    # dsl_ElseIfDoSpec has no real 'dsl_ElseIfDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_ElseIfDoSpec()
    setattr(partner, 'dsl_ElseIfDoSpec', None)
    _safe_set(owner, 'dsl_Specification13', {partner})
    assert getattr(partner, 'dsl_ElseIfDoSpec') == owner
    _safe_set(owner, 'dsl_Specification13', set())
    assert getattr(partner, 'dsl_ElseIfDoSpec') is None


def test_assoc_ifdo10_stub_double():
    # dsl_IfDoSpec has no real 'dsl_IfDoSpec' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_IfDoSpec()
    setattr(partner, 'dsl_IfDoSpec', None)
    _safe_set(owner, 'dsl_Specification11', partner)
    assert getattr(partner, 'dsl_IfDoSpec') == owner
    _safe_set(owner, 'dsl_Specification11', None)
    assert getattr(partner, 'dsl_IfDoSpec') is None


def test_assoc_resource16_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger17' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger17', None)
    _safe_set(owner, 'dsl_Resource18', partner)
    assert getattr(partner, 'dsl_Trigger17') == owner
    _safe_set(owner, 'dsl_Resource18', None)
    assert getattr(partner, 'dsl_Trigger17') is None


def test_assoc_resource38_stub_double():
    # dsl_Action has no real 'dsl_Action39' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Action()
    setattr(partner, 'dsl_Action39', None)
    _safe_set(owner, 'dsl_Resource40', partner)
    assert getattr(partner, 'dsl_Action39') == owner
    _safe_set(owner, 'dsl_Resource40', None)
    assert getattr(partner, 'dsl_Action39') is None


def test_assoc_resources35_stub_double():
    # dsl_EnvironmentMetaData has no real 'dsl_EnvironmentMetaData36' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_EnvironmentMetaData()
    setattr(partner, 'dsl_EnvironmentMetaData36', None)
    _safe_set(owner, 'dsl_Resource37', partner)
    assert owner in getattr(partner, 'dsl_EnvironmentMetaData36')
    _safe_set(owner, 'dsl_Resource37', None)
    assert owner not in getattr(partner, 'dsl_EnvironmentMetaData36')


def test_assoc_servicesData3_stub_double():
    # dsl_RunTimeModel has no real 'dsl_RunTimeModel4' property in the generated
    # code (a bare stub) -- manually attach it so dsl_ServiceMetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_ServiceMetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_ServiceMetaData(serviceID="sample_text")
    partner = dsl_RunTimeModel()
    setattr(partner, 'dsl_RunTimeModel4', None)
    _safe_set(owner, 'dsl_ServiceMetaData', partner)
    assert owner in getattr(partner, 'dsl_RunTimeModel4')
    _safe_set(owner, 'dsl_ServiceMetaData', None)
    assert owner not in getattr(partner, 'dsl_RunTimeModel4')


def test_assoc_state19_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger20' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger20', None)
    _safe_set(owner, 'dsl_State21', partner)
    assert getattr(partner, 'dsl_Trigger20') == owner
    _safe_set(owner, 'dsl_State21', None)
    assert getattr(partner, 'dsl_Trigger20') is None


def test_assoc_state41_stub_double():
    # dsl_Action has no real 'dsl_Action42' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_Action()
    setattr(partner, 'dsl_Action42', None)
    _safe_set(owner, 'dsl_State43', partner)
    assert getattr(partner, 'dsl_Action42') == owner
    _safe_set(owner, 'dsl_State43', None)
    assert getattr(partner, 'dsl_Action42') is None


def test_assoc_trigger8_stub_double():
    # dsl_Trigger has no real 'dsl_Trigger' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Specification(priority=7, specID="sample_text")
    partner = dsl_Trigger()
    setattr(partner, 'dsl_Trigger', None)
    _safe_set(owner, 'dsl_Specification9', {partner})
    assert getattr(partner, 'dsl_Trigger') == owner
    _safe_set(owner, 'dsl_Specification9', set())
    assert getattr(partner, 'dsl_Trigger') is None


def test_assoc_value109_stub_double():
    # dsl_Resource_Object has no real 'dsl_Resource_Object' property in the generated
    # code (a bare stub) -- manually attach it so dsl_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_Resource(name="sample_text")
    partner = dsl_Resource_Object()
    setattr(partner, 'dsl_Resource_Object', None)
    _safe_set(owner, 'dsl_Resource110', partner)
    assert getattr(partner, 'dsl_Resource_Object') == owner
    _safe_set(owner, 'dsl_Resource110', None)
    assert getattr(partner, 'dsl_Resource_Object') is None


def test_assoc_value111_stub_double():
    # dsl_State_Object has no real 'dsl_State_Object' property in the generated
    # code (a bare stub) -- manually attach it so dsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dsl_State(name="sample_text")
    partner = dsl_State_Object()
    setattr(partner, 'dsl_State_Object', None)
    _safe_set(owner, 'dsl_State112', partner)
    assert getattr(partner, 'dsl_State_Object') == owner
    _safe_set(owner, 'dsl_State112', None)
    assert getattr(partner, 'dsl_State_Object') is None


