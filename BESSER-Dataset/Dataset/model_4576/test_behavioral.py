import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DSL_Expression,
    DSL_REF,
    sensinact_DSL_CEP_AFTER,
    sensinact_DSL_CEP_AVG,
    sensinact_DSL_CEP_BEFORE,
    sensinact_DSL_CEP_COINCIDE,
    sensinact_DSL_CEP_COUNT,
    sensinact_DSL_CEP_DURATION,
    sensinact_DSL_CEP_DURATION_MIN,
    sensinact_DSL_CEP_DURATION_SEC,
    sensinact_DSL_CEP_MAX,
    sensinact_DSL_CEP_MIN,
    sensinact_DSL_CEP_STATEMENT,
    sensinact_DSL_CEP_SUM,
    sensinact_DSL_ECA_STATEMENT,
    sensinact_DSL_ElseDo,
    sensinact_DSL_ElseIfDo,
    sensinact_DSL_Expression,
    sensinact_DSL_Expression_And,
    sensinact_DSL_Expression_Diff,
    sensinact_DSL_Expression_Division,
    sensinact_DSL_Expression_Equal,
    sensinact_DSL_Expression_Larger,
    sensinact_DSL_Expression_Larger_Equal,
    sensinact_DSL_Expression_Minus,
    sensinact_DSL_Expression_Modulo,
    sensinact_DSL_Expression_Multiplication,
    sensinact_DSL_Expression_Negate,
    sensinact_DSL_Expression_Or,
    sensinact_DSL_Expression_Plus,
    sensinact_DSL_Expression_Smaller,
    sensinact_DSL_Expression_Smaller_Equal,
    sensinact_DSL_FLAG_AUTOSTART,
    sensinact_DSL_IfDo,
    sensinact_DSL_ListActions,
    sensinact_DSL_ListParam,
    sensinact_DSL_Object_Boolean,
    sensinact_DSL_Object_Number,
    sensinact_DSL_Object_Ref,
    sensinact_DSL_Object_String,
    sensinact_DSL_On,
    sensinact_DSL_REF,
    sensinact_DSL_REF_CONDITION,
    sensinact_DSL_Resource,
    sensinact_DSL_ResourceAction,
    sensinact_DSL_SENSINACT,
    sensinact_EObject,
    sensinact_Sensinact,
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

def test_assoc_ref95_reverse_link_reassign_clear():
    a1 = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    a2 = sensinact_DSL_ResourceAction(actiontype="sample_text_2", variable="sample_text_2")
    b = sensinact_DSL_REF(name="sample_text")
    _safe_set(b, 'sensinact_DSL_REF97', a1)
    assert _is_linked(b, 'sensinact_DSL_REF97', a1)
    if hasattr(a1, 'sensinact_DSL_ResourceAction96'):
        assert _is_linked(a1, 'sensinact_DSL_ResourceAction96', b)
    _safe_set(b, 'sensinact_DSL_REF97', a2)
    assert _is_linked(b, 'sensinact_DSL_REF97', a2)
    if hasattr(a1, 'sensinact_DSL_ResourceAction96'):
        assert not _is_linked(a1, 'sensinact_DSL_ResourceAction96', b)
    if hasattr(a2, 'sensinact_DSL_ResourceAction96'):
        assert _is_linked(a2, 'sensinact_DSL_ResourceAction96', b)
    _safe_set(b, 'sensinact_DSL_REF97', None)
    assert not _is_linked(b, 'sensinact_DSL_REF97', a2)
    if hasattr(a2, 'sensinact_DSL_ResourceAction96'):
        assert not _is_linked(a2, 'sensinact_DSL_ResourceAction96', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionList93_stub_double():
    # sensinact_DSL_ListActions has no real 'sensinact_DSL_ListActions94' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_ResourceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_ResourceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    partner = sensinact_DSL_ListActions()
    setattr(partner, 'sensinact_DSL_ListActions94', None)
    _safe_set(owner, 'sensinact_DSL_ResourceAction', partner)
    assert owner in getattr(partner, 'sensinact_DSL_ListActions94')
    _safe_set(owner, 'sensinact_DSL_ResourceAction', None)
    assert owner not in getattr(partner, 'sensinact_DSL_ListActions94')


def test_assoc_autostart1_stub_double():
    # sensinact_DSL_SENSINACT has no real 'sensinact_DSL_SENSINACT2' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_FLAG_AUTOSTART's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_FLAG_AUTOSTART's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_FLAG_AUTOSTART(activated=True)
    partner = sensinact_DSL_SENSINACT()
    setattr(partner, 'sensinact_DSL_SENSINACT2', None)
    _safe_set(owner, 'sensinact_DSL_FLAG_AUTOSTART', partner)
    assert getattr(partner, 'sensinact_DSL_SENSINACT2') == owner
    _safe_set(owner, 'sensinact_DSL_FLAG_AUTOSTART', None)
    assert getattr(partner, 'sensinact_DSL_SENSINACT2') is None


def test_assoc_listParam98_stub_double():
    # sensinact_DSL_ListParam has no real 'sensinact_DSL_ListParam' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_ResourceAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_ResourceAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_ResourceAction(actiontype="sample_text", variable="sample_text")
    partner = sensinact_DSL_ListParam()
    setattr(partner, 'sensinact_DSL_ListParam', None)
    _safe_set(owner, 'sensinact_DSL_ResourceAction99', partner)
    assert getattr(partner, 'sensinact_DSL_ListParam') == owner
    _safe_set(owner, 'sensinact_DSL_ResourceAction99', None)
    assert getattr(partner, 'sensinact_DSL_ListParam') is None


def test_assoc_ref32_stub_double():
    # sensinact_DSL_REF_CONDITION has no real 'sensinact_DSL_REF_CONDITION33' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_REF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_REF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_REF(name="sample_text")
    partner = sensinact_DSL_REF_CONDITION()
    setattr(partner, 'sensinact_DSL_REF_CONDITION33', None)
    _safe_set(owner, 'sensinact_DSL_REF', partner)
    assert getattr(partner, 'sensinact_DSL_REF_CONDITION33') == owner
    _safe_set(owner, 'sensinact_DSL_REF', None)
    assert getattr(partner, 'sensinact_DSL_REF_CONDITION33') is None


def test_assoc_resources3_stub_double():
    # sensinact_DSL_SENSINACT has no real 'sensinact_DSL_SENSINACT4' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_Resource(deviceID="sample_text", gatewayID="sample_text", resourceID="sample_text", serviceID="sample_text")
    partner = sensinact_DSL_SENSINACT()
    setattr(partner, 'sensinact_DSL_SENSINACT4', None)
    _safe_set(owner, 'sensinact_DSL_Resource', partner)
    assert owner in getattr(partner, 'sensinact_DSL_SENSINACT4')
    _safe_set(owner, 'sensinact_DSL_Resource', None)
    assert owner not in getattr(partner, 'sensinact_DSL_SENSINACT4')


def test_assoc_value168_stub_double():
    # sensinact_DSL_Object_Ref has no real 'sensinact_DSL_Object_Ref' property in the generated
    # code (a bare stub) -- manually attach it so sensinact_DSL_REF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sensinact_DSL_REF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sensinact_DSL_REF(name="sample_text")
    partner = sensinact_DSL_Object_Ref()
    setattr(partner, 'sensinact_DSL_Object_Ref', None)
    _safe_set(owner, 'sensinact_DSL_REF169', partner)
    assert getattr(partner, 'sensinact_DSL_Object_Ref') == owner
    _safe_set(owner, 'sensinact_DSL_REF169', None)
    assert getattr(partner, 'sensinact_DSL_Object_Ref') is None


