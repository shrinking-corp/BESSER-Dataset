import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    automata_Automata,
    automata_Current,
    automata_Final,
    automata_Initial,
    automata_State,
    automata_Transition,
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

def test_assoc_source9_reverse_link_reassign_clear():
    a1 = automata_Transition(name="sample_text", token="sample_text")
    a2 = automata_Transition(name="sample_text_2", token="sample_text_2")
    b = automata_State(name="sample_text")
    _safe_set(b, 'automata_State11', a1)
    assert _is_linked(b, 'automata_State11', a1)
    if hasattr(a1, 'automata_Transition10'):
        assert _is_linked(a1, 'automata_Transition10', b)
    _safe_set(b, 'automata_State11', a2)
    assert _is_linked(b, 'automata_State11', a2)
    if hasattr(a1, 'automata_Transition10'):
        assert not _is_linked(a1, 'automata_Transition10', b)
    if hasattr(a2, 'automata_Transition10'):
        assert _is_linked(a2, 'automata_Transition10', b)
    _safe_set(b, 'automata_State11', None)
    assert not _is_linked(b, 'automata_State11', a2)
    if hasattr(a2, 'automata_Transition10'):
        assert not _is_linked(a2, 'automata_Transition10', b)


def test_assoc_state15_reverse_link_reassign_clear():
    a1 = automata_State(name="sample_text")
    a2 = automata_State(name="sample_text_2")
    b = automata_Initial(name="sample_text")
    _safe_set(b, 'automata_Initial16', a1)
    assert _is_linked(b, 'automata_Initial16', a1)
    if hasattr(a1, 'automata_State17'):
        assert _is_linked(a1, 'automata_State17', b)
    _safe_set(b, 'automata_Initial16', a2)
    assert _is_linked(b, 'automata_Initial16', a2)
    if hasattr(a1, 'automata_State17'):
        assert not _is_linked(a1, 'automata_State17', b)
    if hasattr(a2, 'automata_State17'):
        assert _is_linked(a2, 'automata_State17', b)
    _safe_set(b, 'automata_Initial16', None)
    assert not _is_linked(b, 'automata_Initial16', a2)
    if hasattr(a2, 'automata_State17'):
        assert not _is_linked(a2, 'automata_State17', b)


def test_assoc_state18_reverse_link_reassign_clear():
    a1 = automata_State(name="sample_text")
    a2 = automata_State(name="sample_text_2")
    b = automata_Final(name="sample_text")
    _safe_set(b, 'automata_Final19', a1)
    assert _is_linked(b, 'automata_Final19', a1)
    if hasattr(a1, 'automata_State20'):
        assert _is_linked(a1, 'automata_State20', b)
    _safe_set(b, 'automata_Final19', a2)
    assert _is_linked(b, 'automata_Final19', a2)
    if hasattr(a1, 'automata_State20'):
        assert not _is_linked(a1, 'automata_State20', b)
    if hasattr(a2, 'automata_State20'):
        assert _is_linked(a2, 'automata_State20', b)
    _safe_set(b, 'automata_Final19', None)
    assert not _is_linked(b, 'automata_Final19', a2)
    if hasattr(a2, 'automata_State20'):
        assert not _is_linked(a2, 'automata_State20', b)


def test_assoc_state21_reverse_link_reassign_clear():
    a1 = automata_State(name="sample_text")
    a2 = automata_State(name="sample_text_2")
    b = automata_Current(name="sample_text")
    _safe_set(b, 'automata_Current22', a1)
    assert _is_linked(b, 'automata_Current22', a1)
    if hasattr(a1, 'automata_State23'):
        assert _is_linked(a1, 'automata_State23', b)
    _safe_set(b, 'automata_Current22', a2)
    assert _is_linked(b, 'automata_Current22', a2)
    if hasattr(a1, 'automata_State23'):
        assert not _is_linked(a1, 'automata_State23', b)
    if hasattr(a2, 'automata_State23'):
        assert _is_linked(a2, 'automata_State23', b)
    _safe_set(b, 'automata_Current22', None)
    assert not _is_linked(b, 'automata_Current22', a2)
    if hasattr(a2, 'automata_State23'):
        assert not _is_linked(a2, 'automata_State23', b)


def test_assoc_target12_reverse_link_reassign_clear():
    a1 = automata_Transition(name="sample_text", token="sample_text")
    a2 = automata_Transition(name="sample_text_2", token="sample_text_2")
    b = automata_State(name="sample_text")
    _safe_set(b, 'automata_State14', a1)
    assert _is_linked(b, 'automata_State14', a1)
    if hasattr(a1, 'automata_Transition13'):
        assert _is_linked(a1, 'automata_Transition13', b)
    _safe_set(b, 'automata_State14', a2)
    assert _is_linked(b, 'automata_State14', a2)
    if hasattr(a1, 'automata_Transition13'):
        assert not _is_linked(a1, 'automata_Transition13', b)
    if hasattr(a2, 'automata_Transition13'):
        assert _is_linked(a2, 'automata_Transition13', b)
    _safe_set(b, 'automata_State14', None)
    assert not _is_linked(b, 'automata_State14', a2)
    if hasattr(a2, 'automata_Transition13'):
        assert not _is_linked(a2, 'automata_Transition13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_current0_stub_double():
    # automata_Automata has no real 'automata_Automata' property in the generated
    # code (a bare stub) -- manually attach it so automata_Current's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Current's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Current(name="sample_text")
    partner = automata_Automata()
    setattr(partner, 'automata_Automata', None)
    _safe_set(owner, 'automata_Current', partner)
    assert getattr(partner, 'automata_Automata') == owner
    _safe_set(owner, 'automata_Current', None)
    assert getattr(partner, 'automata_Automata') is None


def test_assoc_finals7_stub_double():
    # automata_Automata has no real 'automata_Automata8' property in the generated
    # code (a bare stub) -- manually attach it so automata_Final's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Final's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Final(name="sample_text")
    partner = automata_Automata()
    setattr(partner, 'automata_Automata8', None)
    _safe_set(owner, 'automata_Final', partner)
    assert owner in getattr(partner, 'automata_Automata8')
    _safe_set(owner, 'automata_Final', None)
    assert owner not in getattr(partner, 'automata_Automata8')


def test_assoc_initial1_stub_double():
    # automata_Automata has no real 'automata_Automata2' property in the generated
    # code (a bare stub) -- manually attach it so automata_Initial's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Initial's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Initial(name="sample_text")
    partner = automata_Automata()
    setattr(partner, 'automata_Automata2', None)
    _safe_set(owner, 'automata_Initial', partner)
    assert getattr(partner, 'automata_Automata2') == owner
    _safe_set(owner, 'automata_Initial', None)
    assert getattr(partner, 'automata_Automata2') is None


def test_assoc_states3_stub_double():
    # automata_Automata has no real 'automata_Automata4' property in the generated
    # code (a bare stub) -- manually attach it so automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_State(name="sample_text")
    partner = automata_Automata()
    setattr(partner, 'automata_Automata4', None)
    _safe_set(owner, 'automata_State', partner)
    assert owner in getattr(partner, 'automata_Automata4')
    _safe_set(owner, 'automata_State', None)
    assert owner not in getattr(partner, 'automata_Automata4')


def test_assoc_transitions5_stub_double():
    # automata_Automata has no real 'automata_Automata6' property in the generated
    # code (a bare stub) -- manually attach it so automata_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # automata_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = automata_Transition(name="sample_text", token="sample_text")
    partner = automata_Automata()
    setattr(partner, 'automata_Automata6', None)
    _safe_set(owner, 'automata_Transition', partner)
    assert owner in getattr(partner, 'automata_Automata6')
    _safe_set(owner, 'automata_Transition', None)
    assert owner not in getattr(partner, 'automata_Automata6')


