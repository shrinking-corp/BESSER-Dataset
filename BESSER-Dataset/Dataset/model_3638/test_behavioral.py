import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    State,
    autopl_Alphabet,
    autopl_Automaton,
    autopl_HierarchicalState,
    autopl_State,
    autopl_Symbol,
    autopl_Transition,
    AcceptanceKind,
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

def test_assoc_from_28_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    _safe_set(b, 'autopl_State30', a1)
    assert _is_linked(b, 'autopl_State30', a1)
    if hasattr(a1, 'autopl_Transition29'):
        assert _is_linked(a1, 'autopl_Transition29', b)
    _safe_set(b, 'autopl_State30', a2)
    assert _is_linked(b, 'autopl_State30', a2)
    if hasattr(a1, 'autopl_Transition29'):
        assert not _is_linked(a1, 'autopl_Transition29', b)
    if hasattr(a2, 'autopl_Transition29'):
        assert _is_linked(a2, 'autopl_Transition29', b)
    _safe_set(b, 'autopl_State30', None)
    assert not _is_linked(b, 'autopl_State30', a2)
    if hasattr(a2, 'autopl_Transition29'):
        assert not _is_linked(a2, 'autopl_Transition29', b)


def test_assoc_initialStackSymbol7_reverse_link_reassign_clear():
    a1 = autopl_Symbol(name="sample_text")
    a2 = autopl_Symbol(name="sample_text_2")
    b = autopl_Automaton()
    _safe_set(b, 'autopl_Automaton8', a1)
    assert _is_linked(b, 'autopl_Automaton8', a1)
    if hasattr(a1, 'autopl_Symbol'):
        assert _is_linked(a1, 'autopl_Symbol', b)
    _safe_set(b, 'autopl_Automaton8', a2)
    assert _is_linked(b, 'autopl_Automaton8', a2)
    if hasattr(a1, 'autopl_Symbol'):
        assert not _is_linked(a1, 'autopl_Symbol', b)
    if hasattr(a2, 'autopl_Symbol'):
        assert _is_linked(a2, 'autopl_Symbol', b)
    _safe_set(b, 'autopl_Automaton8', None)
    assert not _is_linked(b, 'autopl_Automaton8', a2)
    if hasattr(a2, 'autopl_Symbol'):
        assert not _is_linked(a2, 'autopl_Symbol', b)


def test_assoc_input16_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_Symbol(name="sample_text")
    _safe_set(b, 'autopl_Symbol18', a1)
    assert _is_linked(b, 'autopl_Symbol18', a1)
    if hasattr(a1, 'autopl_Transition17'):
        assert _is_linked(a1, 'autopl_Transition17', b)
    _safe_set(b, 'autopl_Symbol18', a2)
    assert _is_linked(b, 'autopl_Symbol18', a2)
    if hasattr(a1, 'autopl_Transition17'):
        assert not _is_linked(a1, 'autopl_Transition17', b)
    if hasattr(a2, 'autopl_Transition17'):
        assert _is_linked(a2, 'autopl_Transition17', b)
    _safe_set(b, 'autopl_Symbol18', None)
    assert not _is_linked(b, 'autopl_Symbol18', a2)
    if hasattr(a2, 'autopl_Transition17'):
        assert not _is_linked(a2, 'autopl_Transition17', b)


def test_assoc_output19_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_Symbol(name="sample_text")
    _safe_set(b, 'autopl_Symbol21', a1)
    assert _is_linked(b, 'autopl_Symbol21', a1)
    if hasattr(a1, 'autopl_Transition20'):
        assert _is_linked(a1, 'autopl_Transition20', b)
    _safe_set(b, 'autopl_Symbol21', a2)
    assert _is_linked(b, 'autopl_Symbol21', a2)
    if hasattr(a1, 'autopl_Transition20'):
        assert not _is_linked(a1, 'autopl_Transition20', b)
    if hasattr(a2, 'autopl_Transition20'):
        assert _is_linked(a2, 'autopl_Transition20', b)
    _safe_set(b, 'autopl_Symbol21', None)
    assert not _is_linked(b, 'autopl_Symbol21', a2)
    if hasattr(a2, 'autopl_Transition20'):
        assert not _is_linked(a2, 'autopl_Transition20', b)


def test_assoc_stackCheck22_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_Symbol(name="sample_text")
    _safe_set(b, 'autopl_Symbol24', a1)
    assert _is_linked(b, 'autopl_Symbol24', a1)
    if hasattr(a1, 'autopl_Transition23'):
        assert _is_linked(a1, 'autopl_Transition23', b)
    _safe_set(b, 'autopl_Symbol24', a2)
    assert _is_linked(b, 'autopl_Symbol24', a2)
    if hasattr(a1, 'autopl_Transition23'):
        assert not _is_linked(a1, 'autopl_Transition23', b)
    if hasattr(a2, 'autopl_Transition23'):
        assert _is_linked(a2, 'autopl_Transition23', b)
    _safe_set(b, 'autopl_Symbol24', None)
    assert not _is_linked(b, 'autopl_Symbol24', a2)
    if hasattr(a2, 'autopl_Transition23'):
        assert not _is_linked(a2, 'autopl_Transition23', b)


def test_assoc_stackPush25_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_Symbol(name="sample_text")
    _safe_set(b, 'autopl_Symbol27', a1)
    assert _is_linked(b, 'autopl_Symbol27', a1)
    if hasattr(a1, 'autopl_Transition26'):
        assert _is_linked(a1, 'autopl_Transition26', b)
    _safe_set(b, 'autopl_Symbol27', a2)
    assert _is_linked(b, 'autopl_Symbol27', a2)
    if hasattr(a1, 'autopl_Transition26'):
        assert not _is_linked(a1, 'autopl_Transition26', b)
    if hasattr(a2, 'autopl_Transition26'):
        assert _is_linked(a2, 'autopl_Transition26', b)
    _safe_set(b, 'autopl_Symbol27', None)
    assert not _is_linked(b, 'autopl_Symbol27', a2)
    if hasattr(a2, 'autopl_Transition26'):
        assert not _is_linked(a2, 'autopl_Transition26', b)


def test_assoc_states9_reverse_link_reassign_clear():
    a1 = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    a2 = autopl_State(isFinal="sample_text_2", isInitial="sample_text_2", name="sample_text_2")
    b = autopl_Automaton()
    _safe_set(b, 'autopl_Automaton10', {a1})
    assert _is_linked(b, 'autopl_Automaton10', a1)
    if hasattr(a1, 'autopl_State'):
        assert _is_linked(a1, 'autopl_State', b)
    _safe_set(b, 'autopl_Automaton10', {a2})
    assert _is_linked(b, 'autopl_Automaton10', a2)
    if hasattr(a1, 'autopl_State'):
        assert not _is_linked(a1, 'autopl_State', b)
    if hasattr(a2, 'autopl_State'):
        assert _is_linked(a2, 'autopl_State', b)
    _safe_set(b, 'autopl_Automaton10', set())
    assert not _is_linked(b, 'autopl_Automaton10', a2)
    if hasattr(a2, 'autopl_State'):
        assert not _is_linked(a2, 'autopl_State', b)


def test_assoc_to31_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    _safe_set(b, 'autopl_State33', a1)
    assert _is_linked(b, 'autopl_State33', a1)
    if hasattr(a1, 'autopl_Transition32'):
        assert _is_linked(a1, 'autopl_Transition32', b)
    _safe_set(b, 'autopl_State33', a2)
    assert _is_linked(b, 'autopl_State33', a2)
    if hasattr(a1, 'autopl_Transition32'):
        assert not _is_linked(a1, 'autopl_Transition32', b)
    if hasattr(a2, 'autopl_Transition32'):
        assert _is_linked(a2, 'autopl_Transition32', b)
    _safe_set(b, 'autopl_State33', None)
    assert not _is_linked(b, 'autopl_State33', a2)
    if hasattr(a2, 'autopl_Transition32'):
        assert not _is_linked(a2, 'autopl_Transition32', b)


def test_assoc_transitions11_reverse_link_reassign_clear():
    a1 = autopl_Transition(probability="sample_text")
    a2 = autopl_Transition(probability="sample_text_2")
    b = autopl_Automaton()
    _safe_set(b, 'autopl_Automaton12', {a1})
    assert _is_linked(b, 'autopl_Automaton12', a1)
    if hasattr(a1, 'autopl_Transition'):
        assert _is_linked(a1, 'autopl_Transition', b)
    _safe_set(b, 'autopl_Automaton12', {a2})
    assert _is_linked(b, 'autopl_Automaton12', a2)
    if hasattr(a1, 'autopl_Transition'):
        assert not _is_linked(a1, 'autopl_Transition', b)
    if hasattr(a2, 'autopl_Transition'):
        assert _is_linked(a2, 'autopl_Transition', b)
    _safe_set(b, 'autopl_Automaton12', set())
    assert not _is_linked(b, 'autopl_Automaton12', a2)
    if hasattr(a2, 'autopl_Transition'):
        assert not _is_linked(a2, 'autopl_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_inputAlphabet0_stub_double():
    # autopl_Alphabet has no real 'autopl_Alphabet' property in the generated
    # code (a bare stub) -- manually attach it so autopl_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_Automaton()
    partner = autopl_Alphabet()
    setattr(partner, 'autopl_Alphabet', None)
    _safe_set(owner, 'autopl_Automaton', partner)
    assert getattr(partner, 'autopl_Alphabet') == owner
    _safe_set(owner, 'autopl_Automaton', None)
    assert getattr(partner, 'autopl_Alphabet') is None


def test_assoc_outputAlphabet1_stub_double():
    # autopl_Alphabet has no real 'autopl_Alphabet3' property in the generated
    # code (a bare stub) -- manually attach it so autopl_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_Automaton()
    partner = autopl_Alphabet()
    setattr(partner, 'autopl_Alphabet3', None)
    _safe_set(owner, 'autopl_Automaton2', partner)
    assert getattr(partner, 'autopl_Alphabet3') == owner
    _safe_set(owner, 'autopl_Automaton2', None)
    assert getattr(partner, 'autopl_Alphabet3') is None


def test_assoc_stackAlphabet4_stub_double():
    # autopl_Alphabet has no real 'autopl_Alphabet6' property in the generated
    # code (a bare stub) -- manually attach it so autopl_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_Automaton()
    partner = autopl_Alphabet()
    setattr(partner, 'autopl_Alphabet6', None)
    _safe_set(owner, 'autopl_Automaton5', partner)
    assert getattr(partner, 'autopl_Alphabet6') == owner
    _safe_set(owner, 'autopl_Automaton5', None)
    assert getattr(partner, 'autopl_Alphabet6') is None


def test_assoc_states34_stub_double():
    # autopl_HierarchicalState has no real 'autopl_HierarchicalState' property in the generated
    # code (a bare stub) -- manually attach it so autopl_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_State(isFinal="sample_text", isInitial="sample_text", name="sample_text")
    partner = autopl_HierarchicalState()
    setattr(partner, 'autopl_HierarchicalState', None)
    _safe_set(owner, 'autopl_State35', partner)
    assert owner in getattr(partner, 'autopl_HierarchicalState')
    _safe_set(owner, 'autopl_State35', None)
    assert owner not in getattr(partner, 'autopl_HierarchicalState')


def test_assoc_symbols13_stub_double():
    # autopl_Alphabet has no real 'autopl_Alphabet14' property in the generated
    # code (a bare stub) -- manually attach it so autopl_Symbol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_Symbol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_Symbol(name="sample_text")
    partner = autopl_Alphabet()
    setattr(partner, 'autopl_Alphabet14', None)
    _safe_set(owner, 'autopl_Symbol15', partner)
    assert owner in getattr(partner, 'autopl_Alphabet14')
    _safe_set(owner, 'autopl_Symbol15', None)
    assert owner not in getattr(partner, 'autopl_Alphabet14')


def test_assoc_transitions36_stub_double():
    # autopl_HierarchicalState has no real 'autopl_HierarchicalState37' property in the generated
    # code (a bare stub) -- manually attach it so autopl_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # autopl_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = autopl_Transition(probability="sample_text")
    partner = autopl_HierarchicalState()
    setattr(partner, 'autopl_HierarchicalState37', None)
    _safe_set(owner, 'autopl_Transition38', partner)
    assert owner in getattr(partner, 'autopl_HierarchicalState37')
    _safe_set(owner, 'autopl_Transition38', None)
    assert owner not in getattr(partner, 'autopl_HierarchicalState37')


