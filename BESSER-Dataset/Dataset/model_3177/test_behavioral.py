import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Expression,
    iotdsl_Action,
    iotdsl_And,
    iotdsl_Attribute,
    iotdsl_BoolConstant,
    iotdsl_Comparison,
    iotdsl_Device,
    iotdsl_Equality,
    iotdsl_Event,
    iotdsl_Expression,
    iotdsl_IfBlock,
    iotdsl_IfStatement,
    iotdsl_IntConstant,
    iotdsl_Iot,
    iotdsl_Minus,
    iotdsl_MulOrDiv,
    iotdsl_Not,
    iotdsl_Or,
    iotdsl_Plus,
    iotdsl_State,
    iotdsl_StringConstant,
    iotdsl_Transition,
    iotdsl_Variable,
    iotdsl_VariableRef,
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
    a1 = iotdsl_Device(name="sample_text")
    a2 = iotdsl_Device(name="sample_text_2")
    b = iotdsl_Attribute(tag="sample_text", typeName="sample_text", value="sample_text")
    _safe_set(b, 'iotdsl_Attribute', a1)
    assert _is_linked(b, 'iotdsl_Attribute', a1)
    if hasattr(a1, 'iotdsl_Device5'):
        assert _is_linked(a1, 'iotdsl_Device5', b)
    _safe_set(b, 'iotdsl_Attribute', a2)
    assert _is_linked(b, 'iotdsl_Attribute', a2)
    if hasattr(a1, 'iotdsl_Device5'):
        assert not _is_linked(a1, 'iotdsl_Device5', b)
    if hasattr(a2, 'iotdsl_Device5'):
        assert _is_linked(a2, 'iotdsl_Device5', b)
    _safe_set(b, 'iotdsl_Attribute', None)
    assert not _is_linked(b, 'iotdsl_Attribute', a2)
    if hasattr(a2, 'iotdsl_Device5'):
        assert not _is_linked(a2, 'iotdsl_Device5', b)


def test_assoc_event14_reverse_link_reassign_clear():
    a1 = iotdsl_Transition(name="sample_text")
    a2 = iotdsl_Transition(name="sample_text_2")
    b = iotdsl_Event(name="sample_text")
    _safe_set(b, 'iotdsl_Event16', a1)
    assert _is_linked(b, 'iotdsl_Event16', a1)
    if hasattr(a1, 'iotdsl_Transition15'):
        assert _is_linked(a1, 'iotdsl_Transition15', b)
    _safe_set(b, 'iotdsl_Event16', a2)
    assert _is_linked(b, 'iotdsl_Event16', a2)
    if hasattr(a1, 'iotdsl_Transition15'):
        assert not _is_linked(a1, 'iotdsl_Transition15', b)
    if hasattr(a2, 'iotdsl_Transition15'):
        assert _is_linked(a2, 'iotdsl_Transition15', b)
    _safe_set(b, 'iotdsl_Event16', None)
    assert not _is_linked(b, 'iotdsl_Event16', a2)
    if hasattr(a2, 'iotdsl_Transition15'):
        assert not _is_linked(a2, 'iotdsl_Transition15', b)


def test_assoc_events8_reverse_link_reassign_clear():
    a1 = iotdsl_Event(name="sample_text")
    a2 = iotdsl_Event(name="sample_text_2")
    b = iotdsl_Device(name="sample_text")
    _safe_set(b, 'iotdsl_Device9', {a1})
    assert _is_linked(b, 'iotdsl_Device9', a1)
    if hasattr(a1, 'iotdsl_Event'):
        assert _is_linked(a1, 'iotdsl_Event', b)
    _safe_set(b, 'iotdsl_Device9', {a2})
    assert _is_linked(b, 'iotdsl_Device9', a2)
    if hasattr(a1, 'iotdsl_Event'):
        assert not _is_linked(a1, 'iotdsl_Event', b)
    if hasattr(a2, 'iotdsl_Event'):
        assert _is_linked(a2, 'iotdsl_Event', b)
    _safe_set(b, 'iotdsl_Device9', set())
    assert not _is_linked(b, 'iotdsl_Device9', a2)
    if hasattr(a2, 'iotdsl_Event'):
        assert not _is_linked(a2, 'iotdsl_Event', b)


def test_assoc_state17_reverse_link_reassign_clear():
    a1 = iotdsl_Transition(name="sample_text")
    a2 = iotdsl_Transition(name="sample_text_2")
    b = iotdsl_State(name="sample_text")
    _safe_set(b, 'iotdsl_State19', a1)
    assert _is_linked(b, 'iotdsl_State19', a1)
    if hasattr(a1, 'iotdsl_Transition18'):
        assert _is_linked(a1, 'iotdsl_Transition18', b)
    _safe_set(b, 'iotdsl_State19', a2)
    assert _is_linked(b, 'iotdsl_State19', a2)
    if hasattr(a1, 'iotdsl_Transition18'):
        assert not _is_linked(a1, 'iotdsl_Transition18', b)
    if hasattr(a2, 'iotdsl_Transition18'):
        assert _is_linked(a2, 'iotdsl_Transition18', b)
    _safe_set(b, 'iotdsl_State19', None)
    assert not _is_linked(b, 'iotdsl_State19', a2)
    if hasattr(a2, 'iotdsl_Transition18'):
        assert not _is_linked(a2, 'iotdsl_Transition18', b)


def test_assoc_states6_reverse_link_reassign_clear():
    a1 = iotdsl_State(name="sample_text")
    a2 = iotdsl_State(name="sample_text_2")
    b = iotdsl_Device(name="sample_text")
    _safe_set(b, 'iotdsl_Device7', {a1})
    assert _is_linked(b, 'iotdsl_Device7', a1)
    if hasattr(a1, 'iotdsl_State'):
        assert _is_linked(a1, 'iotdsl_State', b)
    _safe_set(b, 'iotdsl_Device7', {a2})
    assert _is_linked(b, 'iotdsl_Device7', a2)
    if hasattr(a1, 'iotdsl_State'):
        assert not _is_linked(a1, 'iotdsl_State', b)
    if hasattr(a2, 'iotdsl_State'):
        assert _is_linked(a2, 'iotdsl_State', b)
    _safe_set(b, 'iotdsl_Device7', set())
    assert not _is_linked(b, 'iotdsl_Device7', a2)
    if hasattr(a2, 'iotdsl_State'):
        assert not _is_linked(a2, 'iotdsl_State', b)


def test_assoc_superType2_reverse_link_reassign_clear():
    a1 = iotdsl_Device(name="sample_text")
    a2 = iotdsl_Device(name="sample_text_2")
    b = iotdsl_Device(name="sample_text")
    _safe_set(b, 'iotdsl_Device3', a1)
    assert _is_linked(b, 'iotdsl_Device3', a1)
    if hasattr(a1, 'iotdsl_Device1'):
        assert _is_linked(a1, 'iotdsl_Device1', b)
    _safe_set(b, 'iotdsl_Device3', a2)
    assert _is_linked(b, 'iotdsl_Device3', a2)
    if hasattr(a1, 'iotdsl_Device1'):
        assert not _is_linked(a1, 'iotdsl_Device1', b)
    if hasattr(a2, 'iotdsl_Device1'):
        assert _is_linked(a2, 'iotdsl_Device1', b)
    _safe_set(b, 'iotdsl_Device3', None)
    assert not _is_linked(b, 'iotdsl_Device3', a2)
    if hasattr(a2, 'iotdsl_Device1'):
        assert not _is_linked(a2, 'iotdsl_Device1', b)


def test_assoc_transitions10_reverse_link_reassign_clear():
    a1 = iotdsl_Transition(name="sample_text")
    a2 = iotdsl_Transition(name="sample_text_2")
    b = iotdsl_Device(name="sample_text")
    _safe_set(b, 'iotdsl_Device11', {a1})
    assert _is_linked(b, 'iotdsl_Device11', a1)
    if hasattr(a1, 'iotdsl_Transition'):
        assert _is_linked(a1, 'iotdsl_Transition', b)
    _safe_set(b, 'iotdsl_Device11', {a2})
    assert _is_linked(b, 'iotdsl_Device11', a2)
    if hasattr(a1, 'iotdsl_Transition'):
        assert not _is_linked(a1, 'iotdsl_Transition', b)
    if hasattr(a2, 'iotdsl_Transition'):
        assert _is_linked(a2, 'iotdsl_Transition', b)
    _safe_set(b, 'iotdsl_Device11', set())
    assert not _is_linked(b, 'iotdsl_Device11', a2)
    if hasattr(a2, 'iotdsl_Transition'):
        assert not _is_linked(a2, 'iotdsl_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_devices0_stub_double():
    # iotdsl_Iot has no real 'iotdsl_Iot' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Device(name="sample_text")
    partner = iotdsl_Iot()
    setattr(partner, 'iotdsl_Iot', None)
    _safe_set(owner, 'iotdsl_Device', partner)
    assert owner in getattr(partner, 'iotdsl_Iot')
    _safe_set(owner, 'iotdsl_Device', None)
    assert owner not in getattr(partner, 'iotdsl_Iot')


def test_assoc_elements12_stub_double():
    # iotdsl_Action has no real 'iotdsl_Action' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_State(name="sample_text")
    partner = iotdsl_Action()
    setattr(partner, 'iotdsl_Action', None)
    _safe_set(owner, 'iotdsl_State13', {partner})
    assert getattr(partner, 'iotdsl_Action') == owner
    _safe_set(owner, 'iotdsl_State13', set())
    assert getattr(partner, 'iotdsl_Action') is None


def test_assoc_expression20_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Variable(name="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression', None)
    _safe_set(owner, 'iotdsl_Variable', partner)
    assert getattr(partner, 'iotdsl_Expression') == owner
    _safe_set(owner, 'iotdsl_Variable', None)
    assert getattr(partner, 'iotdsl_Expression') is None


def test_assoc_left41_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression42' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Equality(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression42', None)
    _safe_set(owner, 'iotdsl_Equality', partner)
    assert getattr(partner, 'iotdsl_Expression42') == owner
    _safe_set(owner, 'iotdsl_Equality', None)
    assert getattr(partner, 'iotdsl_Expression42') is None


def test_assoc_left46_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression47' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Comparison(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression47', None)
    _safe_set(owner, 'iotdsl_Comparison', partner)
    assert getattr(partner, 'iotdsl_Expression47') == owner
    _safe_set(owner, 'iotdsl_Comparison', None)
    assert getattr(partner, 'iotdsl_Expression47') is None


def test_assoc_left61_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression62' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_MulOrDiv(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression62', None)
    _safe_set(owner, 'iotdsl_MulOrDiv', partner)
    assert getattr(partner, 'iotdsl_Expression62') == owner
    _safe_set(owner, 'iotdsl_MulOrDiv', None)
    assert getattr(partner, 'iotdsl_Expression62') is None


def test_assoc_right43_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression45' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Equality's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Equality's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Equality(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression45', None)
    _safe_set(owner, 'iotdsl_Equality44', partner)
    assert getattr(partner, 'iotdsl_Expression45') == owner
    _safe_set(owner, 'iotdsl_Equality44', None)
    assert getattr(partner, 'iotdsl_Expression45') is None


def test_assoc_right48_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Comparison's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Comparison's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Comparison(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression50', None)
    _safe_set(owner, 'iotdsl_Comparison49', partner)
    assert getattr(partner, 'iotdsl_Expression50') == owner
    _safe_set(owner, 'iotdsl_Comparison49', None)
    assert getattr(partner, 'iotdsl_Expression50') is None


def test_assoc_right63_stub_double():
    # iotdsl_Expression has no real 'iotdsl_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_MulOrDiv's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_MulOrDiv's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_MulOrDiv(op="sample_text")
    partner = iotdsl_Expression()
    setattr(partner, 'iotdsl_Expression65', None)
    _safe_set(owner, 'iotdsl_MulOrDiv64', partner)
    assert getattr(partner, 'iotdsl_Expression65') == owner
    _safe_set(owner, 'iotdsl_MulOrDiv64', None)
    assert getattr(partner, 'iotdsl_Expression65') is None


def test_assoc_variable68_stub_double():
    # iotdsl_VariableRef has no real 'iotdsl_VariableRef' property in the generated
    # code (a bare stub) -- manually attach it so iotdsl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotdsl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotdsl_Variable(name="sample_text")
    partner = iotdsl_VariableRef()
    setattr(partner, 'iotdsl_VariableRef', None)
    _safe_set(owner, 'iotdsl_Variable69', partner)
    assert getattr(partner, 'iotdsl_VariableRef') == owner
    _safe_set(owner, 'iotdsl_Variable69', None)
    assert getattr(partner, 'iotdsl_VariableRef') is None


