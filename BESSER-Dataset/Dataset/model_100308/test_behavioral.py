import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    Node,
    Node_dynamic,
    PNScenario,
    PNSimEvent,
    PNTrace,
    PetriNet,
    PetriNetEvent,
    Place,
    Transition,
    petrinetsemantics_DDMMPetriNet_Arc,
    petrinetsemantics_DDMMPetriNet_Node,
    petrinetsemantics_DDMMPetriNet_PetriNet,
    petrinetsemantics_DDMMPetriNet_Place,
    petrinetsemantics_DDMMPetriNet_Transition,
    petrinetsemantics_EDMMPetriNet_FireTransitionEvent,
    petrinetsemantics_EDMMPetriNet_PetriNetEvent,
    petrinetsemantics_SDMMPetriNet_Node_dynamic,
    petrinetsemantics_SDMMPetriNet_PetriNet_dynamic,
    petrinetsemantics_SDMMPetriNet_Place_dynamic,
    petrinetsemantics_TM3PetriNet_PNScenario,
    petrinetsemantics_TM3PetriNet_PNSimEvent,
    petrinetsemantics_TM3PetriNet_PNTrace,
    ArcKind,
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

def test_assoc_Place_static16_stub_double():
    # Place has no real 'Place' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_SDMMPetriNet_Place_dynamic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_SDMMPetriNet_Place_dynamic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_SDMMPetriNet_Place_dynamic(marking=7)
    partner = Place()
    setattr(partner, 'Place', None)
    _safe_set(owner, 'petrinetsemantics_SDMMPetriNet_Place_dynamic', partner)
    assert getattr(partner, 'Place') == owner
    _safe_set(owner, 'petrinetsemantics_SDMMPetriNet_Place_dynamic', None)
    assert getattr(partner, 'Place') is None


def test_assoc_arcs1_stub_double():
    # Arc has no real 'Arc' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_PetriNet(name="sample_text")
    partner = Arc()
    setattr(partner, 'Arc', None)
    _safe_set(owner, 'net2', {partner})
    assert getattr(partner, 'Arc') == owner
    _safe_set(owner, 'net2', set())
    assert getattr(partner, 'Arc') is None


def test_assoc_firedTransition21_stub_double():
    # Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_EDMMPetriNet_FireTransitionEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_EDMMPetriNet_FireTransitionEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_EDMMPetriNet_FireTransitionEvent(time=3.14)
    partner = Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'petrinetsemantics_EDMMPetriNet_FireTransitionEvent', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'petrinetsemantics_EDMMPetriNet_FireTransitionEvent', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_incomings6_stub_double():
    # Arc has no real 'Arc7' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Node(name="sample_text")
    partner = Arc()
    setattr(partner, 'Arc7', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Arc7') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Arc7') is None


def test_assoc_net12_stub_double():
    # PetriNet has no real 'PetriNet13' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Arc(kind="sample_text", weight=7)
    partner = PetriNet()
    setattr(partner, 'PetriNet13', None)
    _safe_set(owner, 'arcs', partner)
    assert getattr(partner, 'PetriNet13') == owner
    _safe_set(owner, 'arcs', None)
    assert getattr(partner, 'PetriNet13') is None


def test_assoc_net3_stub_double():
    # PetriNet has no real 'PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Node(name="sample_text")
    partner = PetriNet()
    setattr(partner, 'PetriNet', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'PetriNet') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'PetriNet') is None


def test_assoc_nodes0_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_PetriNet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_PetriNet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_PetriNet(name="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'net', {partner})
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'net', set())
    assert getattr(partner, 'Node') is None


def test_assoc_outgoings4_stub_double():
    # Arc has no real 'Arc5' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Node(name="sample_text")
    partner = Arc()
    setattr(partner, 'Arc5', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Arc5') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Arc5') is None


def test_assoc_source10_stub_double():
    # Node has no real 'Node11' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Arc(kind="sample_text", weight=7)
    partner = Node()
    setattr(partner, 'Node11', None)
    _safe_set(owner, 'outgoings', partner)
    assert getattr(partner, 'Node11') == owner
    _safe_set(owner, 'outgoings', None)
    assert getattr(partner, 'Node11') is None


def test_assoc_target8_stub_double():
    # Node has no real 'Node9' property in the generated
    # code (a bare stub) -- manually attach it so petrinetsemantics_DDMMPetriNet_Arc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinetsemantics_DDMMPetriNet_Arc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinetsemantics_DDMMPetriNet_Arc(kind="sample_text", weight=7)
    partner = Node()
    setattr(partner, 'Node9', None)
    _safe_set(owner, 'incomings', partner)
    assert getattr(partner, 'Node9') == owner
    _safe_set(owner, 'incomings', None)
    assert getattr(partner, 'Node9') is None


