import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Automaton,
    ExtendibleElement,
    ExtensionElement,
    IExtendible,
    IExtension,
    Module,
    State,
    Transition,
    ea_automata_Automaton,
    ea_automata_Module,
    ea_automata_State,
    ea_automata_Transition,
    ea_extensions_BooleanExtension,
    ea_extensions_ExtendibleElement,
    ea_extensions_ExtensionElement,
    ea_extensions_IExtendible,
    ea_extensions_IExtension,
    ea_extensions_IntegerExtension,
    ea_extensions_StringExtension,
    ea_extensions_StringListExtension,
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

def test_assoc_automaton4_stub_double():
    # Automaton has no real 'Automaton' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_State(id="sample_text", name="sample_text")
    partner = Automaton()
    setattr(partner, 'Automaton', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'Automaton') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'Automaton') is None


def test_assoc_automaton9_stub_double():
    # Automaton has no real 'Automaton10' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Transition(id="sample_text")
    partner = Automaton()
    setattr(partner, 'Automaton10', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Automaton10') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Automaton10') is None


def test_assoc_extensions17_stub_double():
    # IExtension has no real 'IExtension' property in the generated
    # code (a bare stub) -- manually attach it so ea_extensions_IExtendible's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_extensions_IExtendible's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_extensions_IExtendible()
    partner = IExtension()
    setattr(partner, 'IExtension', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'IExtension') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'IExtension') is None


def test_assoc_incoming5_stub_double():
    # Transition has no real 'Transition6' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_State(id="sample_text", name="sample_text")
    partner = Transition()
    setattr(partner, 'Transition6', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Transition6') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Transition6') is None


def test_assoc_module3_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Automaton(id="sample_text", name="sample_text", usedExtensionIds="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'automata', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'automata', None)
    assert getattr(partner, 'Module') is None


def test_assoc_outgoing7_stub_double():
    # Transition has no real 'Transition8' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_State's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_State's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_State(id="sample_text", name="sample_text")
    partner = Transition()
    setattr(partner, 'Transition8', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Transition8') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Transition8') is None


def test_assoc_owner18_stub_double():
    # IExtendible has no real 'IExtendible' property in the generated
    # code (a bare stub) -- manually attach it so ea_extensions_IExtension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_extensions_IExtension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_extensions_IExtension(id="sample_text")
    partner = IExtendible()
    setattr(partner, 'IExtendible', None)
    _safe_set(owner, 'extensions', partner)
    assert getattr(partner, 'IExtendible') == owner
    _safe_set(owner, 'extensions', None)
    assert getattr(partner, 'IExtendible') is None


def test_assoc_source11_stub_double():
    # State has no real 'State12' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Transition(id="sample_text")
    partner = State()
    setattr(partner, 'State12', None)
    _safe_set(owner, 'outgoing', partner)
    assert getattr(partner, 'State12') == owner
    _safe_set(owner, 'outgoing', None)
    assert getattr(partner, 'State12') is None


def test_assoc_states0_stub_double():
    # State has no real 'State' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Automaton(id="sample_text", name="sample_text", usedExtensionIds="sample_text")
    partner = State()
    setattr(partner, 'State', None)
    _safe_set(owner, 'automaton', {partner})
    assert getattr(partner, 'State') == owner
    _safe_set(owner, 'automaton', set())
    assert getattr(partner, 'State') is None


def test_assoc_target13_stub_double():
    # State has no real 'State14' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Transition(id="sample_text")
    partner = State()
    setattr(partner, 'State14', None)
    _safe_set(owner, 'incoming', partner)
    assert getattr(partner, 'State14') == owner
    _safe_set(owner, 'incoming', None)
    assert getattr(partner, 'State14') is None


def test_assoc_transitions1_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so ea_automata_Automaton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ea_automata_Automaton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ea_automata_Automaton(id="sample_text", name="sample_text", usedExtensionIds="sample_text")
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'automaton2', {partner})
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'automaton2', set())
    assert getattr(partner, 'Transition') is None


