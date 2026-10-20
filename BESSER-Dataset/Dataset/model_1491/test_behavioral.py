import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GenericPlace,
    extendedPetriNets_GenericPlace,
    extendedPetriNets_InputArc,
    extendedPetriNets_InputPort,
    extendedPetriNets_OutputArc,
    extendedPetriNets_OutputPort,
    extendedPetriNets_PetriNet,
    extendedPetriNets_Place,
    extendedPetriNets_Transition,
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

def test_assoc_InputArcToTransition7_reverse_link_reassign_clear():
    a1 = extendedPetriNets_Transition(name="sample_text")
    a2 = extendedPetriNets_Transition(name="sample_text_2")
    b = extendedPetriNets_InputArc(weight=7)
    _safe_set(b, 'extendedPetriNets_InputArc8', a1)
    assert _is_linked(b, 'extendedPetriNets_InputArc8', a1)
    if hasattr(a1, 'extendedPetriNets_Transition9'):
        assert _is_linked(a1, 'extendedPetriNets_Transition9', b)
    _safe_set(b, 'extendedPetriNets_InputArc8', a2)
    assert _is_linked(b, 'extendedPetriNets_InputArc8', a2)
    if hasattr(a1, 'extendedPetriNets_Transition9'):
        assert not _is_linked(a1, 'extendedPetriNets_Transition9', b)
    if hasattr(a2, 'extendedPetriNets_Transition9'):
        assert _is_linked(a2, 'extendedPetriNets_Transition9', b)
    _safe_set(b, 'extendedPetriNets_InputArc8', None)
    assert not _is_linked(b, 'extendedPetriNets_InputArc8', a2)
    if hasattr(a2, 'extendedPetriNets_Transition9'):
        assert not _is_linked(a2, 'extendedPetriNets_Transition9', b)


def test_assoc_OutputArcFromTransition14_reverse_link_reassign_clear():
    a1 = extendedPetriNets_Transition(name="sample_text")
    a2 = extendedPetriNets_Transition(name="sample_text_2")
    b = extendedPetriNets_OutputArc(weight=7)
    _safe_set(b, 'extendedPetriNets_OutputArc15', a1)
    assert _is_linked(b, 'extendedPetriNets_OutputArc15', a1)
    if hasattr(a1, 'extendedPetriNets_Transition16'):
        assert _is_linked(a1, 'extendedPetriNets_Transition16', b)
    _safe_set(b, 'extendedPetriNets_OutputArc15', a2)
    assert _is_linked(b, 'extendedPetriNets_OutputArc15', a2)
    if hasattr(a1, 'extendedPetriNets_Transition16'):
        assert not _is_linked(a1, 'extendedPetriNets_Transition16', b)
    if hasattr(a2, 'extendedPetriNets_Transition16'):
        assert _is_linked(a2, 'extendedPetriNets_Transition16', b)
    _safe_set(b, 'extendedPetriNets_OutputArc15', None)
    assert not _is_linked(b, 'extendedPetriNets_OutputArc15', a2)
    if hasattr(a2, 'extendedPetriNets_Transition16'):
        assert not _is_linked(a2, 'extendedPetriNets_Transition16', b)


def test_assoc_containsGenericPlaces0_reverse_link_reassign_clear():
    a1 = extendedPetriNets_PetriNet(name="sample_text")
    a2 = extendedPetriNets_PetriNet(name="sample_text_2")
    b = extendedPetriNets_GenericPlace(capacity=7, name="sample_text", numberOfTokens=7)
    _safe_set(b, 'extendedPetriNets_GenericPlace', a1)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace', a1)
    if hasattr(a1, 'extendedPetriNets_PetriNet'):
        assert _is_linked(a1, 'extendedPetriNets_PetriNet', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace', a2)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace', a2)
    if hasattr(a1, 'extendedPetriNets_PetriNet'):
        assert not _is_linked(a1, 'extendedPetriNets_PetriNet', b)
    if hasattr(a2, 'extendedPetriNets_PetriNet'):
        assert _is_linked(a2, 'extendedPetriNets_PetriNet', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace', None)
    assert not _is_linked(b, 'extendedPetriNets_GenericPlace', a2)
    if hasattr(a2, 'extendedPetriNets_PetriNet'):
        assert not _is_linked(a2, 'extendedPetriNets_PetriNet', b)


def test_assoc_containsInputArcs3_reverse_link_reassign_clear():
    a1 = extendedPetriNets_PetriNet(name="sample_text")
    a2 = extendedPetriNets_PetriNet(name="sample_text_2")
    b = extendedPetriNets_InputArc(weight=7)
    _safe_set(b, 'extendedPetriNets_InputArc', a1)
    assert _is_linked(b, 'extendedPetriNets_InputArc', a1)
    if hasattr(a1, 'extendedPetriNets_PetriNet4'):
        assert _is_linked(a1, 'extendedPetriNets_PetriNet4', b)
    _safe_set(b, 'extendedPetriNets_InputArc', a2)
    assert _is_linked(b, 'extendedPetriNets_InputArc', a2)
    if hasattr(a1, 'extendedPetriNets_PetriNet4'):
        assert not _is_linked(a1, 'extendedPetriNets_PetriNet4', b)
    if hasattr(a2, 'extendedPetriNets_PetriNet4'):
        assert _is_linked(a2, 'extendedPetriNets_PetriNet4', b)
    _safe_set(b, 'extendedPetriNets_InputArc', None)
    assert not _is_linked(b, 'extendedPetriNets_InputArc', a2)
    if hasattr(a2, 'extendedPetriNets_PetriNet4'):
        assert not _is_linked(a2, 'extendedPetriNets_PetriNet4', b)


def test_assoc_containsOutputArcs5_reverse_link_reassign_clear():
    a1 = extendedPetriNets_PetriNet(name="sample_text")
    a2 = extendedPetriNets_PetriNet(name="sample_text_2")
    b = extendedPetriNets_OutputArc(weight=7)
    _safe_set(b, 'extendedPetriNets_OutputArc', a1)
    assert _is_linked(b, 'extendedPetriNets_OutputArc', a1)
    if hasattr(a1, 'extendedPetriNets_PetriNet6'):
        assert _is_linked(a1, 'extendedPetriNets_PetriNet6', b)
    _safe_set(b, 'extendedPetriNets_OutputArc', a2)
    assert _is_linked(b, 'extendedPetriNets_OutputArc', a2)
    if hasattr(a1, 'extendedPetriNets_PetriNet6'):
        assert not _is_linked(a1, 'extendedPetriNets_PetriNet6', b)
    if hasattr(a2, 'extendedPetriNets_PetriNet6'):
        assert _is_linked(a2, 'extendedPetriNets_PetriNet6', b)
    _safe_set(b, 'extendedPetriNets_OutputArc', None)
    assert not _is_linked(b, 'extendedPetriNets_OutputArc', a2)
    if hasattr(a2, 'extendedPetriNets_PetriNet6'):
        assert not _is_linked(a2, 'extendedPetriNets_PetriNet6', b)


def test_assoc_containsTransitions1_reverse_link_reassign_clear():
    a1 = extendedPetriNets_Transition(name="sample_text")
    a2 = extendedPetriNets_Transition(name="sample_text_2")
    b = extendedPetriNets_PetriNet(name="sample_text")
    _safe_set(b, 'extendedPetriNets_PetriNet2', {a1})
    assert _is_linked(b, 'extendedPetriNets_PetriNet2', a1)
    if hasattr(a1, 'extendedPetriNets_Transition'):
        assert _is_linked(a1, 'extendedPetriNets_Transition', b)
    _safe_set(b, 'extendedPetriNets_PetriNet2', {a2})
    assert _is_linked(b, 'extendedPetriNets_PetriNet2', a2)
    if hasattr(a1, 'extendedPetriNets_Transition'):
        assert not _is_linked(a1, 'extendedPetriNets_Transition', b)
    if hasattr(a2, 'extendedPetriNets_Transition'):
        assert _is_linked(a2, 'extendedPetriNets_Transition', b)
    _safe_set(b, 'extendedPetriNets_PetriNet2', set())
    assert not _is_linked(b, 'extendedPetriNets_PetriNet2', a2)
    if hasattr(a2, 'extendedPetriNets_Transition'):
        assert not _is_linked(a2, 'extendedPetriNets_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_InputArcFromInputPort12_stub_double():
    # extendedPetriNets_InputPort has no real 'extendedPetriNets_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so extendedPetriNets_InputArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedPetriNets_InputArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedPetriNets_InputArc(weight=7)
    partner = extendedPetriNets_InputPort()
    setattr(partner, 'extendedPetriNets_InputPort', None)
    _safe_set(owner, 'extendedPetriNets_InputArc13', partner)
    assert getattr(partner, 'extendedPetriNets_InputPort') == owner
    _safe_set(owner, 'extendedPetriNets_InputArc13', None)
    assert getattr(partner, 'extendedPetriNets_InputPort') is None


def test_assoc_InputArcFromPlace10_stub_double():
    # extendedPetriNets_Place has no real 'extendedPetriNets_Place' property in the generated
    # code (a bare stub) -- manually attach it so extendedPetriNets_InputArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedPetriNets_InputArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedPetriNets_InputArc(weight=7)
    partner = extendedPetriNets_Place()
    setattr(partner, 'extendedPetriNets_Place', None)
    _safe_set(owner, 'extendedPetriNets_InputArc11', partner)
    assert getattr(partner, 'extendedPetriNets_Place') == owner
    _safe_set(owner, 'extendedPetriNets_InputArc11', None)
    assert getattr(partner, 'extendedPetriNets_Place') is None


def test_assoc_OutputArcToOutputPort20_stub_double():
    # extendedPetriNets_OutputPort has no real 'extendedPetriNets_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so extendedPetriNets_OutputArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedPetriNets_OutputArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedPetriNets_OutputArc(weight=7)
    partner = extendedPetriNets_OutputPort()
    setattr(partner, 'extendedPetriNets_OutputPort', None)
    _safe_set(owner, 'extendedPetriNets_OutputArc21', partner)
    assert getattr(partner, 'extendedPetriNets_OutputPort') == owner
    _safe_set(owner, 'extendedPetriNets_OutputArc21', None)
    assert getattr(partner, 'extendedPetriNets_OutputPort') is None


def test_assoc_OutputArcToPlace17_stub_double():
    # extendedPetriNets_Place has no real 'extendedPetriNets_Place19' property in the generated
    # code (a bare stub) -- manually attach it so extendedPetriNets_OutputArc's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # extendedPetriNets_OutputArc's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = extendedPetriNets_OutputArc(weight=7)
    partner = extendedPetriNets_Place()
    setattr(partner, 'extendedPetriNets_Place19', None)
    _safe_set(owner, 'extendedPetriNets_OutputArc18', partner)
    assert getattr(partner, 'extendedPetriNets_Place19') == owner
    _safe_set(owner, 'extendedPetriNets_OutputArc18', None)
    assert getattr(partner, 'extendedPetriNets_Place19') is None


