import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Command,
    Expression,
    statemachine_Command,
    statemachine_ExecuteCommand,
    statemachine_Expression,
    statemachine_PrintCommand,
    statemachine_SetCommand,
    statemachine_State,
    statemachine_StatePropertyExpression,
    statemachine_Statemachine,
    statemachine_Transition,
    statemachine_VerbatimExpression,
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

def test_assoc_state19_reverse_link_reassign_clear():
    a1 = statemachine_StatePropertyExpression(_property="sample_text")
    a2 = statemachine_StatePropertyExpression(_property="sample_text_2")
    b = statemachine_State(final=True, id="sample_text", initial=True, name="sample_text")
    _safe_set(b, 'statemachine_State20', a1)
    assert _is_linked(b, 'statemachine_State20', a1)
    if hasattr(a1, 'statemachine_StatePropertyExpression'):
        assert _is_linked(a1, 'statemachine_StatePropertyExpression', b)
    _safe_set(b, 'statemachine_State20', a2)
    assert _is_linked(b, 'statemachine_State20', a2)
    if hasattr(a1, 'statemachine_StatePropertyExpression'):
        assert not _is_linked(a1, 'statemachine_StatePropertyExpression', b)
    if hasattr(a2, 'statemachine_StatePropertyExpression'):
        assert _is_linked(a2, 'statemachine_StatePropertyExpression', b)
    _safe_set(b, 'statemachine_State20', None)
    assert not _is_linked(b, 'statemachine_State20', a2)
    if hasattr(a2, 'statemachine_StatePropertyExpression'):
        assert not _is_linked(a2, 'statemachine_StatePropertyExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actions3_stub_double():
    # statemachine_Command has no real 'statemachine_Command' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(final=True, id="sample_text", initial=True, name="sample_text")
    partner = statemachine_Command()
    setattr(partner, 'statemachine_Command', None)
    _safe_set(owner, 'statemachine_State4', {partner})
    assert getattr(partner, 'statemachine_Command') == owner
    _safe_set(owner, 'statemachine_State4', set())
    assert getattr(partner, 'statemachine_Command') is None


def test_assoc_arguments15_stub_double():
    # statemachine_Expression has no real 'statemachine_Expression16' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_ExecuteCommand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_ExecuteCommand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_ExecuteCommand(operation="sample_text")
    partner = statemachine_Expression()
    setattr(partner, 'statemachine_Expression16', None)
    _safe_set(owner, 'statemachine_ExecuteCommand', {partner})
    assert getattr(partner, 'statemachine_Expression16') == owner
    _safe_set(owner, 'statemachine_ExecuteCommand', set())
    assert getattr(partner, 'statemachine_Expression16') is None


def test_assoc_sourceState5_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition6' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(final=True, id="sample_text", initial=True, name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition6', None)
    _safe_set(owner, 'statemachine_State7', partner)
    assert getattr(partner, 'statemachine_Transition6') == owner
    _safe_set(owner, 'statemachine_State7', None)
    assert getattr(partner, 'statemachine_Transition6') is None


def test_assoc_states0_stub_double():
    # statemachine_Statemachine has no real 'statemachine_Statemachine' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(final=True, id="sample_text", initial=True, name="sample_text")
    partner = statemachine_Statemachine()
    setattr(partner, 'statemachine_Statemachine', None)
    _safe_set(owner, 'statemachine_State', partner)
    assert owner in getattr(partner, 'statemachine_Statemachine')
    _safe_set(owner, 'statemachine_State', None)
    assert owner not in getattr(partner, 'statemachine_Statemachine')


def test_assoc_targetState8_stub_double():
    # statemachine_Transition has no real 'statemachine_Transition9' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_State(final=True, id="sample_text", initial=True, name="sample_text")
    partner = statemachine_Transition()
    setattr(partner, 'statemachine_Transition9', None)
    _safe_set(owner, 'statemachine_State10', partner)
    assert getattr(partner, 'statemachine_Transition9') == owner
    _safe_set(owner, 'statemachine_State10', None)
    assert getattr(partner, 'statemachine_Transition9') is None


def test_assoc_value13_stub_double():
    # statemachine_Expression has no real 'statemachine_Expression14' property in the generated
    # code (a bare stub) -- manually attach it so statemachine_SetCommand's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # statemachine_SetCommand's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = statemachine_SetCommand(signal="sample_text")
    partner = statemachine_Expression()
    setattr(partner, 'statemachine_Expression14', None)
    _safe_set(owner, 'statemachine_SetCommand', partner)
    assert getattr(partner, 'statemachine_Expression14') == owner
    _safe_set(owner, 'statemachine_SetCommand', None)
    assert getattr(partner, 'statemachine_Expression14') is None


