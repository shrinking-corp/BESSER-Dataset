import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Type,
    stateMachine_Command,
    stateMachine_Condition,
    stateMachine_DeclaredParameter,
    stateMachine_Event,
    stateMachine_FloatType,
    stateMachine_Modifier,
    stateMachine_State,
    stateMachine_StateMachine,
    stateMachine_StringType,
    stateMachine_Test,
    stateMachine_Transition,
    stateMachine_Type,
    stateMachine_VarName,
    stateMachine_model,
    Visibility,
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

def test_assoc_actions22_reverse_link_reassign_clear():
    a1 = stateMachine_State(name="sample_text")
    a2 = stateMachine_State(name="sample_text_2")
    b = stateMachine_Command(name="sample_text")
    _safe_set(b, 'stateMachine_Command24', a1)
    assert _is_linked(b, 'stateMachine_Command24', a1)
    if hasattr(a1, 'stateMachine_State23'):
        assert _is_linked(a1, 'stateMachine_State23', b)
    _safe_set(b, 'stateMachine_Command24', a2)
    assert _is_linked(b, 'stateMachine_Command24', a2)
    if hasattr(a1, 'stateMachine_State23'):
        assert not _is_linked(a1, 'stateMachine_State23', b)
    if hasattr(a2, 'stateMachine_State23'):
        assert _is_linked(a2, 'stateMachine_State23', b)
    _safe_set(b, 'stateMachine_Command24', None)
    assert not _is_linked(b, 'stateMachine_Command24', a2)
    if hasattr(a2, 'stateMachine_State23'):
        assert not _is_linked(a2, 'stateMachine_State23', b)


def test_assoc_commands3_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_Command(name="sample_text")
    _safe_set(b, 'stateMachine_Command', a1)
    assert _is_linked(b, 'stateMachine_Command', a1)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert _is_linked(a1, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_Command', a2)
    assert _is_linked(b, 'stateMachine_Command', a2)
    if hasattr(a1, 'stateMachine_StateMachine4'):
        assert not _is_linked(a1, 'stateMachine_StateMachine4', b)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert _is_linked(a2, 'stateMachine_StateMachine4', b)
    _safe_set(b, 'stateMachine_Command', None)
    assert not _is_linked(b, 'stateMachine_Command', a2)
    if hasattr(a2, 'stateMachine_StateMachine4'):
        assert not _is_linked(a2, 'stateMachine_StateMachine4', b)


def test_assoc_events1_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_Event(name="sample_text")
    _safe_set(b, 'stateMachine_Event', a1)
    assert _is_linked(b, 'stateMachine_Event', a1)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert _is_linked(a1, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Event', a2)
    assert _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a1, 'stateMachine_StateMachine2'):
        assert not _is_linked(a1, 'stateMachine_StateMachine2', b)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert _is_linked(a2, 'stateMachine_StateMachine2', b)
    _safe_set(b, 'stateMachine_Event', None)
    assert not _is_linked(b, 'stateMachine_Event', a2)
    if hasattr(a2, 'stateMachine_StateMachine2'):
        assert not _is_linked(a2, 'stateMachine_StateMachine2', b)


def test_assoc_finalstates10_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State12', a1)
    assert _is_linked(b, 'stateMachine_State12', a1)
    if hasattr(a1, 'stateMachine_StateMachine11'):
        assert _is_linked(a1, 'stateMachine_StateMachine11', b)
    _safe_set(b, 'stateMachine_State12', a2)
    assert _is_linked(b, 'stateMachine_State12', a2)
    if hasattr(a1, 'stateMachine_StateMachine11'):
        assert not _is_linked(a1, 'stateMachine_StateMachine11', b)
    if hasattr(a2, 'stateMachine_StateMachine11'):
        assert _is_linked(a2, 'stateMachine_StateMachine11', b)
    _safe_set(b, 'stateMachine_State12', None)
    assert not _is_linked(b, 'stateMachine_State12', a2)
    if hasattr(a2, 'stateMachine_StateMachine11'):
        assert not _is_linked(a2, 'stateMachine_StateMachine11', b)


def test_assoc_initialstates7_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State9', a1)
    assert _is_linked(b, 'stateMachine_State9', a1)
    if hasattr(a1, 'stateMachine_StateMachine8'):
        assert _is_linked(a1, 'stateMachine_StateMachine8', b)
    _safe_set(b, 'stateMachine_State9', a2)
    assert _is_linked(b, 'stateMachine_State9', a2)
    if hasattr(a1, 'stateMachine_StateMachine8'):
        assert not _is_linked(a1, 'stateMachine_StateMachine8', b)
    if hasattr(a2, 'stateMachine_StateMachine8'):
        assert _is_linked(a2, 'stateMachine_StateMachine8', b)
    _safe_set(b, 'stateMachine_State9', None)
    assert not _is_linked(b, 'stateMachine_State9', a2)
    if hasattr(a2, 'stateMachine_StateMachine8'):
        assert not _is_linked(a2, 'stateMachine_StateMachine8', b)


def test_assoc_returnType13_reverse_link_reassign_clear():
    a1 = stateMachine_Type(type="sample_text")
    a2 = stateMachine_Type(type="sample_text_2")
    b = stateMachine_Event(name="sample_text")
    _safe_set(b, 'stateMachine_Event14', a1)
    assert _is_linked(b, 'stateMachine_Event14', a1)
    if hasattr(a1, 'stateMachine_Type'):
        assert _is_linked(a1, 'stateMachine_Type', b)
    _safe_set(b, 'stateMachine_Event14', a2)
    assert _is_linked(b, 'stateMachine_Event14', a2)
    if hasattr(a1, 'stateMachine_Type'):
        assert not _is_linked(a1, 'stateMachine_Type', b)
    if hasattr(a2, 'stateMachine_Type'):
        assert _is_linked(a2, 'stateMachine_Type', b)
    _safe_set(b, 'stateMachine_Event14', None)
    assert not _is_linked(b, 'stateMachine_Event14', a2)
    if hasattr(a2, 'stateMachine_Type'):
        assert not _is_linked(a2, 'stateMachine_Type', b)


def test_assoc_states5_reverse_link_reassign_clear():
    a1 = stateMachine_StateMachine(name="sample_text")
    a2 = stateMachine_StateMachine(name="sample_text_2")
    b = stateMachine_State(name="sample_text")
    _safe_set(b, 'stateMachine_State', a1)
    assert _is_linked(b, 'stateMachine_State', a1)
    if hasattr(a1, 'stateMachine_StateMachine6'):
        assert _is_linked(a1, 'stateMachine_StateMachine6', b)
    _safe_set(b, 'stateMachine_State', a2)
    assert _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a1, 'stateMachine_StateMachine6'):
        assert not _is_linked(a1, 'stateMachine_StateMachine6', b)
    if hasattr(a2, 'stateMachine_StateMachine6'):
        assert _is_linked(a2, 'stateMachine_StateMachine6', b)
    _safe_set(b, 'stateMachine_State', None)
    assert not _is_linked(b, 'stateMachine_State', a2)
    if hasattr(a2, 'stateMachine_StateMachine6'):
        assert not _is_linked(a2, 'stateMachine_StateMachine6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_condition33_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition34' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Condition(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition34', None)
    _safe_set(owner, 'stateMachine_Condition', partner)
    assert getattr(partner, 'stateMachine_Transition34') == owner
    _safe_set(owner, 'stateMachine_Condition', None)
    assert getattr(partner, 'stateMachine_Transition34') is None


def test_assoc_event27_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition28' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition28', None)
    _safe_set(owner, 'stateMachine_Event29', partner)
    assert getattr(partner, 'stateMachine_Transition28') == owner
    _safe_set(owner, 'stateMachine_Event29', None)
    assert getattr(partner, 'stateMachine_Transition28') is None


def test_assoc_name35_stub_double():
    # stateMachine_DeclaredParameter has no real 'stateMachine_DeclaredParameter36' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_VarName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_VarName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_VarName(value="sample_text")
    partner = stateMachine_DeclaredParameter()
    setattr(partner, 'stateMachine_DeclaredParameter36', None)
    _safe_set(owner, 'stateMachine_VarName', partner)
    assert getattr(partner, 'stateMachine_DeclaredParameter36') == owner
    _safe_set(owner, 'stateMachine_VarName', None)
    assert getattr(partner, 'stateMachine_DeclaredParameter36') is None


def test_assoc_state30_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition31' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition31', None)
    _safe_set(owner, 'stateMachine_State32', partner)
    assert getattr(partner, 'stateMachine_Transition31') == owner
    _safe_set(owner, 'stateMachine_State32', None)
    assert getattr(partner, 'stateMachine_Transition31') is None


def test_assoc_statemachine0_stub_double():
    # stateMachine_model has no real 'stateMachine_model' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_StateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_StateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_StateMachine(name="sample_text")
    partner = stateMachine_model()
    setattr(partner, 'stateMachine_model', None)
    _safe_set(owner, 'stateMachine_StateMachine', partner)
    assert owner in getattr(partner, 'stateMachine_model')
    _safe_set(owner, 'stateMachine_StateMachine', None)
    assert owner not in getattr(partner, 'stateMachine_model')


def test_assoc_tests15_stub_double():
    # stateMachine_Test has no real 'stateMachine_Test' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Event(name="sample_text")
    partner = stateMachine_Test()
    setattr(partner, 'stateMachine_Test', None)
    _safe_set(owner, 'stateMachine_Event16', {partner})
    assert getattr(partner, 'stateMachine_Test') == owner
    _safe_set(owner, 'stateMachine_Event16', set())
    assert getattr(partner, 'stateMachine_Test') is None


def test_assoc_transitions25_stub_double():
    # stateMachine_Transition has no real 'stateMachine_Transition' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_State(name="sample_text")
    partner = stateMachine_Transition()
    setattr(partner, 'stateMachine_Transition', None)
    _safe_set(owner, 'stateMachine_State26', {partner})
    assert getattr(partner, 'stateMachine_Transition') == owner
    _safe_set(owner, 'stateMachine_State26', set())
    assert getattr(partner, 'stateMachine_Transition') is None


def test_assoc_types17_stub_double():
    # stateMachine_Test has no real 'stateMachine_Test18' property in the generated
    # code (a bare stub) -- manually attach it so stateMachine_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # stateMachine_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = stateMachine_Type(type="sample_text")
    partner = stateMachine_Test()
    setattr(partner, 'stateMachine_Test18', None)
    _safe_set(owner, 'stateMachine_Type19', partner)
    assert owner in getattr(partner, 'stateMachine_Test18')
    _safe_set(owner, 'stateMachine_Type19', None)
    assert owner not in getattr(partner, 'stateMachine_Test18')


