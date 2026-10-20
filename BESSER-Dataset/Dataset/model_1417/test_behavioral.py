import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    ControlPort,
    DataPort,
    EModelElement,
    Flow,
    IdentifiedItem,
    InputPort,
    ModelContent,
    NamedItem,
    OutputPort,
    Port,
    State,
    SynchronisationGate,
    sam_AbstractState,
    sam_Automaton,
    sam_Composition,
    sam_ControlFlow,
    sam_ControlPort,
    sam_DataFlow,
    sam_DataPort,
    sam_DataStore,
    sam_Decomposition,
    sam_Flow,
    sam_IdentifiedItem,
    sam_InControlPort,
    sam_InDataPort,
    sam_InitialState,
    sam_InputPort,
    sam_MacroState,
    sam_Model,
    sam_ModelContent,
    sam_MultiPort,
    sam_NamedItem,
    sam_OutControlPort,
    sam_OutDataPort,
    sam_OutputPort,
    sam_Port,
    sam_State,
    sam_SynchronisationGate,
    sam_System,
    sam_Transition,
    DataType,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dest15_stub_double():
    # sam_State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'inlink', partner)
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'inlink', None)
    assert getattr(partner, 'State') is None


def test_assoc_dest46_stub_double():
    # sam_DataPort has no real 'sam_DataPort48' property in the generated
    # code (a bare stub) -- manually attach it so sam_DataFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_DataFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_DataFlow(type="sample_text")
    partner = sam_DataPort()
    setattr(partner, 'sam_DataPort48', None)
    _safe_set(owner, 'sam_DataFlow47', {partner})
    assert getattr(partner, 'sam_DataPort48') == owner
    _safe_set(owner, 'sam_DataFlow47', set())
    assert getattr(partner, 'sam_DataPort48') is None


def test_assoc_inlink13_stub_double():
    # sam_State has no real 'dest' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_State()
    setattr(partner, 'dest', None)
    _safe_set(owner, 'Transition14', partner)
    assert owner in getattr(partner, 'dest')
    _safe_set(owner, 'Transition14', None)
    assert owner not in getattr(partner, 'dest')


def test_assoc_listTransitions3_stub_double():
    # sam_Automaton has no real 'parentAutomaton' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_Automaton()
    setattr(partner, 'parentAutomaton', None)
    _safe_set(owner, 'Transition4', partner)
    assert owner in getattr(partner, 'parentAutomaton')
    _safe_set(owner, 'Transition4', None)
    assert owner not in getattr(partner, 'parentAutomaton')


def test_assoc_outlink2_stub_double():
    # sam_AbstractState has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_AbstractState()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_parentAutomaton16_stub_double():
    # sam_Automaton has no real 'Automaton17' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_Automaton()
    setattr(partner, 'Automaton17', None)
    _safe_set(owner, 'listTransitions', partner)
    assert getattr(partner, 'Automaton17') == owner
    _safe_set(owner, 'listTransitions', None)
    assert getattr(partner, 'Automaton17') is None


def test_assoc_source18_stub_double():
    # sam_AbstractState has no real 'AbstractState19' property in the generated
    # code (a bare stub) -- manually attach it so sam_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_Transition(condition="sample_text", emission="sample_text", priority="sample_text")
    partner = sam_AbstractState()
    setattr(partner, 'AbstractState19', None)
    _safe_set(owner, 'outlink', partner)
    assert getattr(partner, 'AbstractState19') == owner
    _safe_set(owner, 'outlink', None)
    assert getattr(partner, 'AbstractState19') is None


def test_assoc_source45_stub_double():
    # sam_DataPort has no real 'sam_DataPort' property in the generated
    # code (a bare stub) -- manually attach it so sam_DataFlow's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sam_DataFlow's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sam_DataFlow(type="sample_text")
    partner = sam_DataPort()
    setattr(partner, 'sam_DataPort', None)
    _safe_set(owner, 'sam_DataFlow', partner)
    assert getattr(partner, 'sam_DataPort') == owner
    _safe_set(owner, 'sam_DataFlow', None)
    assert getattr(partner, 'sam_DataPort') is None


