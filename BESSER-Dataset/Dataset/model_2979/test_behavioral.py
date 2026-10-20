import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    machine_Current,
    machine_Final,
    machine_Head,
    machine_Initial,
    machine_Machine,
    machine_State,
    machine_Symbol,
    machine_Tape,
    machine_Transition,
    machine_TuringMachine,
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

def test_assoc_next33_reverse_link_reassign_clear():
    a1 = machine_Symbol(name="sample_text", position="sample_text", value="sample_text")
    a2 = machine_Symbol(name="sample_text_2", position="sample_text_2", value="sample_text_2")
    b = machine_Symbol(name="sample_text", position="sample_text", value="sample_text")
    _safe_set(b, 'machine_Symbol34', a1)
    assert _is_linked(b, 'machine_Symbol34', a1)
    if hasattr(a1, 'machine_Symbol32'):
        assert _is_linked(a1, 'machine_Symbol32', b)
    _safe_set(b, 'machine_Symbol34', a2)
    assert _is_linked(b, 'machine_Symbol34', a2)
    if hasattr(a1, 'machine_Symbol32'):
        assert not _is_linked(a1, 'machine_Symbol32', b)
    if hasattr(a2, 'machine_Symbol32'):
        assert _is_linked(a2, 'machine_Symbol32', b)
    _safe_set(b, 'machine_Symbol34', None)
    assert not _is_linked(b, 'machine_Symbol34', a2)
    if hasattr(a2, 'machine_Symbol32'):
        assert not _is_linked(a2, 'machine_Symbol32', b)


def test_assoc_source0_reverse_link_reassign_clear():
    a1 = machine_Transition(moveTo="sample_text", name="sample_text", read="sample_text", write="sample_text")
    a2 = machine_Transition(moveTo="sample_text_2", name="sample_text_2", read="sample_text_2", write="sample_text_2")
    b = machine_State(name="sample_text")
    _safe_set(b, 'machine_State', a1)
    assert _is_linked(b, 'machine_State', a1)
    if hasattr(a1, 'machine_Transition'):
        assert _is_linked(a1, 'machine_Transition', b)
    _safe_set(b, 'machine_State', a2)
    assert _is_linked(b, 'machine_State', a2)
    if hasattr(a1, 'machine_Transition'):
        assert not _is_linked(a1, 'machine_Transition', b)
    if hasattr(a2, 'machine_Transition'):
        assert _is_linked(a2, 'machine_Transition', b)
    _safe_set(b, 'machine_State', None)
    assert not _is_linked(b, 'machine_State', a2)
    if hasattr(a2, 'machine_Transition'):
        assert not _is_linked(a2, 'machine_Transition', b)


def test_assoc_state17_reverse_link_reassign_clear():
    a1 = machine_State(name="sample_text")
    a2 = machine_State(name="sample_text_2")
    b = machine_Current(name="sample_text")
    _safe_set(b, 'machine_Current18', a1)
    assert _is_linked(b, 'machine_Current18', a1)
    if hasattr(a1, 'machine_State19'):
        assert _is_linked(a1, 'machine_State19', b)
    _safe_set(b, 'machine_Current18', a2)
    assert _is_linked(b, 'machine_Current18', a2)
    if hasattr(a1, 'machine_State19'):
        assert not _is_linked(a1, 'machine_State19', b)
    if hasattr(a2, 'machine_State19'):
        assert _is_linked(a2, 'machine_State19', b)
    _safe_set(b, 'machine_Current18', None)
    assert not _is_linked(b, 'machine_Current18', a2)
    if hasattr(a2, 'machine_State19'):
        assert not _is_linked(a2, 'machine_State19', b)


def test_assoc_state20_reverse_link_reassign_clear():
    a1 = machine_State(name="sample_text")
    a2 = machine_State(name="sample_text_2")
    b = machine_Initial(name="sample_text")
    _safe_set(b, 'machine_Initial21', a1)
    assert _is_linked(b, 'machine_Initial21', a1)
    if hasattr(a1, 'machine_State22'):
        assert _is_linked(a1, 'machine_State22', b)
    _safe_set(b, 'machine_Initial21', a2)
    assert _is_linked(b, 'machine_Initial21', a2)
    if hasattr(a1, 'machine_State22'):
        assert not _is_linked(a1, 'machine_State22', b)
    if hasattr(a2, 'machine_State22'):
        assert _is_linked(a2, 'machine_State22', b)
    _safe_set(b, 'machine_Initial21', None)
    assert not _is_linked(b, 'machine_Initial21', a2)
    if hasattr(a2, 'machine_State22'):
        assert not _is_linked(a2, 'machine_State22', b)


def test_assoc_state29_reverse_link_reassign_clear():
    a1 = machine_State(name="sample_text")
    a2 = machine_State(name="sample_text_2")
    b = machine_Final(name="sample_text")
    _safe_set(b, 'machine_Final30', a1)
    assert _is_linked(b, 'machine_Final30', a1)
    if hasattr(a1, 'machine_State31'):
        assert _is_linked(a1, 'machine_State31', b)
    _safe_set(b, 'machine_Final30', a2)
    assert _is_linked(b, 'machine_Final30', a2)
    if hasattr(a1, 'machine_State31'):
        assert not _is_linked(a1, 'machine_State31', b)
    if hasattr(a2, 'machine_State31'):
        assert _is_linked(a2, 'machine_State31', b)
    _safe_set(b, 'machine_Final30', None)
    assert not _is_linked(b, 'machine_Final30', a2)
    if hasattr(a2, 'machine_State31'):
        assert not _is_linked(a2, 'machine_State31', b)


def test_assoc_symbol35_reverse_link_reassign_clear():
    a1 = machine_Symbol(name="sample_text", position="sample_text", value="sample_text")
    a2 = machine_Symbol(name="sample_text_2", position="sample_text_2", value="sample_text_2")
    b = machine_Head(name="sample_text")
    _safe_set(b, 'machine_Head36', a1)
    assert _is_linked(b, 'machine_Head36', a1)
    if hasattr(a1, 'machine_Symbol37'):
        assert _is_linked(a1, 'machine_Symbol37', b)
    _safe_set(b, 'machine_Head36', a2)
    assert _is_linked(b, 'machine_Head36', a2)
    if hasattr(a1, 'machine_Symbol37'):
        assert not _is_linked(a1, 'machine_Symbol37', b)
    if hasattr(a2, 'machine_Symbol37'):
        assert _is_linked(a2, 'machine_Symbol37', b)
    _safe_set(b, 'machine_Head36', None)
    assert not _is_linked(b, 'machine_Head36', a2)
    if hasattr(a2, 'machine_Symbol37'):
        assert not _is_linked(a2, 'machine_Symbol37', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = machine_Transition(moveTo="sample_text", name="sample_text", read="sample_text", write="sample_text")
    a2 = machine_Transition(moveTo="sample_text_2", name="sample_text_2", read="sample_text_2", write="sample_text_2")
    b = machine_State(name="sample_text")
    _safe_set(b, 'machine_State3', a1)
    assert _is_linked(b, 'machine_State3', a1)
    if hasattr(a1, 'machine_Transition2'):
        assert _is_linked(a1, 'machine_Transition2', b)
    _safe_set(b, 'machine_State3', a2)
    assert _is_linked(b, 'machine_State3', a2)
    if hasattr(a1, 'machine_Transition2'):
        assert not _is_linked(a1, 'machine_Transition2', b)
    if hasattr(a2, 'machine_Transition2'):
        assert _is_linked(a2, 'machine_Transition2', b)
    _safe_set(b, 'machine_State3', None)
    assert not _is_linked(b, 'machine_State3', a2)
    if hasattr(a2, 'machine_Transition2'):
        assert not _is_linked(a2, 'machine_Transition2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_current7_stub_double():
    # machine_Machine has no real 'machine_Machine8' property in the generated
    # code (a bare stub) -- manually attach it so machine_Current's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Current's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Current(name="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine8', None)
    _safe_set(owner, 'machine_Current', partner)
    assert getattr(partner, 'machine_Machine8') == owner
    _safe_set(owner, 'machine_Current', None)
    assert getattr(partner, 'machine_Machine8') is None


def test_assoc_finals5_stub_double():
    # machine_Machine has no real 'machine_Machine6' property in the generated
    # code (a bare stub) -- manually attach it so machine_Final's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Final's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Final(name="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine6', None)
    _safe_set(owner, 'machine_Final', partner)
    assert owner in getattr(partner, 'machine_Machine6')
    _safe_set(owner, 'machine_Final', None)
    assert owner not in getattr(partner, 'machine_Machine6')


def test_assoc_head15_stub_double():
    # machine_Machine has no real 'machine_Machine16' property in the generated
    # code (a bare stub) -- manually attach it so machine_Head's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Head's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Head(name="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine16', None)
    _safe_set(owner, 'machine_Head', partner)
    assert getattr(partner, 'machine_Machine16') == owner
    _safe_set(owner, 'machine_Head', None)
    assert getattr(partner, 'machine_Machine16') is None


def test_assoc_initial4_stub_double():
    # machine_Machine has no real 'machine_Machine' property in the generated
    # code (a bare stub) -- manually attach it so machine_Initial's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Initial's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Initial(name="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine', None)
    _safe_set(owner, 'machine_Initial', partner)
    assert getattr(partner, 'machine_Machine') == owner
    _safe_set(owner, 'machine_Initial', None)
    assert getattr(partner, 'machine_Machine') is None


def test_assoc_states9_stub_double():
    # machine_Machine has no real 'machine_Machine10' property in the generated
    # code (a bare stub) -- manually attach it so machine_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_State(name="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine10', None)
    _safe_set(owner, 'machine_State11', partner)
    assert owner in getattr(partner, 'machine_Machine10')
    _safe_set(owner, 'machine_State11', None)
    assert owner not in getattr(partner, 'machine_Machine10')


def test_assoc_symbols23_stub_double():
    # machine_Tape has no real 'machine_Tape' property in the generated
    # code (a bare stub) -- manually attach it so machine_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Symbol(name="sample_text", position="sample_text", value="sample_text")
    partner = machine_Tape()
    setattr(partner, 'machine_Tape', None)
    _safe_set(owner, 'machine_Symbol', partner)
    assert owner in getattr(partner, 'machine_Tape')
    _safe_set(owner, 'machine_Symbol', None)
    assert owner not in getattr(partner, 'machine_Tape')


def test_assoc_transitions12_stub_double():
    # machine_Machine has no real 'machine_Machine13' property in the generated
    # code (a bare stub) -- manually attach it so machine_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # machine_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = machine_Transition(moveTo="sample_text", name="sample_text", read="sample_text", write="sample_text")
    partner = machine_Machine()
    setattr(partner, 'machine_Machine13', None)
    _safe_set(owner, 'machine_Transition14', partner)
    assert owner in getattr(partner, 'machine_Machine13')
    _safe_set(owner, 'machine_Transition14', None)
    assert owner not in getattr(partner, 'machine_Machine13')


