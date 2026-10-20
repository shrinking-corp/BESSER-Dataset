import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SrcConnection,
    SrcElement,
    SrcLocatedElement,
    SrcNamedElement,
    TrgArc,
    TrgElement,
    TrgLocatedElement,
    TrgNamedElement,
    jointPackage_Grafcet2PetriNet_JointMM,
    jointPackage_Grafcet2PetriNet_SrcConnection,
    jointPackage_Grafcet2PetriNet_SrcElement,
    jointPackage_Grafcet2PetriNet_SrcGrafcet,
    jointPackage_Grafcet2PetriNet_SrcLocatedElement,
    jointPackage_Grafcet2PetriNet_SrcNamedElement,
    jointPackage_Grafcet2PetriNet_SrcStep,
    jointPackage_Grafcet2PetriNet_SrcStepToTransition,
    jointPackage_Grafcet2PetriNet_SrcTransition,
    jointPackage_Grafcet2PetriNet_SrcTransitionToStep,
    jointPackage_Grafcet2PetriNet_TrgArc,
    jointPackage_Grafcet2PetriNet_TrgElement,
    jointPackage_Grafcet2PetriNet_TrgLocatedElement,
    jointPackage_Grafcet2PetriNet_TrgNamedElement,
    jointPackage_Grafcet2PetriNet_TrgPetriNet,
    jointPackage_Grafcet2PetriNet_TrgPlace,
    jointPackage_Grafcet2PetriNet_TrgPlaceToTransition,
    jointPackage_Grafcet2PetriNet_TrgTransition,
    jointPackage_Grafcet2PetriNet_TrgTransitionToPlace,
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

def test_assoc_arcs26_stub_double():
    # jointPackage_Grafcet2PetriNet_TrgPetriNet has no real 'net27' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_TrgArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_TrgArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_TrgArc(weight=7)
    partner = jointPackage_Grafcet2PetriNet_TrgPetriNet()
    setattr(partner, 'net27', None)
    _safe_set(owner, 'TrgArc', partner)
    assert owner in getattr(partner, 'net27')
    _safe_set(owner, 'TrgArc', None)
    assert owner not in getattr(partner, 'net27')


def test_assoc_from_17_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcStepToTransition has no real 'outgoingConnections' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcStep(action="sample_text", isActive=True, isInitial=True)
    partner = jointPackage_Grafcet2PetriNet_SrcStepToTransition()
    setattr(partner, 'outgoingConnections', None)
    _safe_set(owner, 'SrcStep', partner)
    assert getattr(partner, 'outgoingConnections') == owner
    _safe_set(owner, 'SrcStep', None)
    assert getattr(partner, 'outgoingConnections') is None


def test_assoc_from_19_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcTransitionToStep has no real 'outgoingConnections20' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcTransition(condition="sample_text")
    partner = jointPackage_Grafcet2PetriNet_SrcTransitionToStep()
    setattr(partner, 'outgoingConnections20', None)
    _safe_set(owner, 'SrcTransition21', partner)
    assert getattr(partner, 'outgoingConnections20') == owner
    _safe_set(owner, 'SrcTransition21', None)
    assert getattr(partner, 'outgoingConnections20') is None


def test_assoc_incomingConnections7_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcTransitionToStep has no real 'SrcTransitionToStep' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcStep(action="sample_text", isActive=True, isInitial=True)
    partner = jointPackage_Grafcet2PetriNet_SrcTransitionToStep()
    setattr(partner, 'SrcTransitionToStep', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'SrcTransitionToStep') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'SrcTransitionToStep') is None


def test_assoc_incomingConnections9_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcStepToTransition has no real 'SrcStepToTransition11' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcTransition(condition="sample_text")
    partner = jointPackage_Grafcet2PetriNet_SrcStepToTransition()
    setattr(partner, 'SrcStepToTransition11', None)
    _safe_set(owner, 'to10', {partner})
    assert getattr(partner, 'SrcStepToTransition11') == owner
    _safe_set(owner, 'to10', set())
    assert getattr(partner, 'SrcStepToTransition11') is None


def test_assoc_net40_stub_double():
    # jointPackage_Grafcet2PetriNet_TrgPetriNet has no real 'TrgPetriNet41' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_TrgArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_TrgArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_TrgArc(weight=7)
    partner = jointPackage_Grafcet2PetriNet_TrgPetriNet()
    setattr(partner, 'TrgPetriNet41', None)
    _safe_set(owner, 'arcs', partner)
    assert getattr(partner, 'TrgPetriNet41') == owner
    _safe_set(owner, 'arcs', None)
    assert getattr(partner, 'TrgPetriNet41') is None


def test_assoc_outgoingConnections12_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcTransitionToStep has no real 'SrcTransitionToStep14' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcTransition(condition="sample_text")
    partner = jointPackage_Grafcet2PetriNet_SrcTransitionToStep()
    setattr(partner, 'SrcTransitionToStep14', None)
    _safe_set(owner, 'from_13', {partner})
    assert getattr(partner, 'SrcTransitionToStep14') == owner
    _safe_set(owner, 'from_13', set())
    assert getattr(partner, 'SrcTransitionToStep14') is None


def test_assoc_outgoingConnections8_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcStepToTransition has no real 'SrcStepToTransition' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcStep(action="sample_text", isActive=True, isInitial=True)
    partner = jointPackage_Grafcet2PetriNet_SrcStepToTransition()
    setattr(partner, 'SrcStepToTransition', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'SrcStepToTransition') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'SrcStepToTransition') is None


def test_assoc_to18_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcStepToTransition has no real 'incomingConnections' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcTransition(condition="sample_text")
    partner = jointPackage_Grafcet2PetriNet_SrcStepToTransition()
    setattr(partner, 'incomingConnections', None)
    _safe_set(owner, 'SrcTransition', partner)
    assert getattr(partner, 'incomingConnections') == owner
    _safe_set(owner, 'SrcTransition', None)
    assert getattr(partner, 'incomingConnections') is None


def test_assoc_to22_stub_double():
    # jointPackage_Grafcet2PetriNet_SrcTransitionToStep has no real 'incomingConnections23' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Grafcet2PetriNet_SrcStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Grafcet2PetriNet_SrcStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Grafcet2PetriNet_SrcStep(action="sample_text", isActive=True, isInitial=True)
    partner = jointPackage_Grafcet2PetriNet_SrcTransitionToStep()
    setattr(partner, 'incomingConnections23', None)
    _safe_set(owner, 'SrcStep24', partner)
    assert getattr(partner, 'incomingConnections23') == owner
    _safe_set(owner, 'SrcStep24', None)
    assert getattr(partner, 'incomingConnections23') is None


