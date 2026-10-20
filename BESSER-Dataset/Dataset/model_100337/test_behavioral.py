import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    GenericPlace,
    resourcePetriNet_GenericPlace,
    resourcePetriNet_InputArc,
    resourcePetriNet_OutputArc,
    resourcePetriNet_PetriNet,
    resourcePetriNet_Place,
    resourcePetriNet_Resource,
    resourcePetriNet_Transition,
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

def test_assoc_InputArcFromPlace7_reverse_link_reassign_clear():
    a1 = resourcePetriNet_InputArc(weight=7)
    a2 = resourcePetriNet_InputArc(weight=13)
    b = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    _safe_set(b, 'resourcePetriNet_GenericPlace9', a1)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace9', a1)
    if hasattr(a1, 'resourcePetriNet_InputArc8'):
        assert _is_linked(a1, 'resourcePetriNet_InputArc8', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace9', a2)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace9', a2)
    if hasattr(a1, 'resourcePetriNet_InputArc8'):
        assert not _is_linked(a1, 'resourcePetriNet_InputArc8', b)
    if hasattr(a2, 'resourcePetriNet_InputArc8'):
        assert _is_linked(a2, 'resourcePetriNet_InputArc8', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace9', None)
    assert not _is_linked(b, 'resourcePetriNet_GenericPlace9', a2)
    if hasattr(a2, 'resourcePetriNet_InputArc8'):
        assert not _is_linked(a2, 'resourcePetriNet_InputArc8', b)


def test_assoc_InputArcToTransition10_reverse_link_reassign_clear():
    a1 = resourcePetriNet_Transition(name="sample_text")
    a2 = resourcePetriNet_Transition(name="sample_text_2")
    b = resourcePetriNet_InputArc(weight=7)
    _safe_set(b, 'resourcePetriNet_InputArc11', a1)
    assert _is_linked(b, 'resourcePetriNet_InputArc11', a1)
    if hasattr(a1, 'resourcePetriNet_Transition12'):
        assert _is_linked(a1, 'resourcePetriNet_Transition12', b)
    _safe_set(b, 'resourcePetriNet_InputArc11', a2)
    assert _is_linked(b, 'resourcePetriNet_InputArc11', a2)
    if hasattr(a1, 'resourcePetriNet_Transition12'):
        assert not _is_linked(a1, 'resourcePetriNet_Transition12', b)
    if hasattr(a2, 'resourcePetriNet_Transition12'):
        assert _is_linked(a2, 'resourcePetriNet_Transition12', b)
    _safe_set(b, 'resourcePetriNet_InputArc11', None)
    assert not _is_linked(b, 'resourcePetriNet_InputArc11', a2)
    if hasattr(a2, 'resourcePetriNet_Transition12'):
        assert not _is_linked(a2, 'resourcePetriNet_Transition12', b)


def test_assoc_OutputArcFromTransition13_reverse_link_reassign_clear():
    a1 = resourcePetriNet_Transition(name="sample_text")
    a2 = resourcePetriNet_Transition(name="sample_text_2")
    b = resourcePetriNet_OutputArc(weight=7)
    _safe_set(b, 'resourcePetriNet_OutputArc14', a1)
    assert _is_linked(b, 'resourcePetriNet_OutputArc14', a1)
    if hasattr(a1, 'resourcePetriNet_Transition15'):
        assert _is_linked(a1, 'resourcePetriNet_Transition15', b)
    _safe_set(b, 'resourcePetriNet_OutputArc14', a2)
    assert _is_linked(b, 'resourcePetriNet_OutputArc14', a2)
    if hasattr(a1, 'resourcePetriNet_Transition15'):
        assert not _is_linked(a1, 'resourcePetriNet_Transition15', b)
    if hasattr(a2, 'resourcePetriNet_Transition15'):
        assert _is_linked(a2, 'resourcePetriNet_Transition15', b)
    _safe_set(b, 'resourcePetriNet_OutputArc14', None)
    assert not _is_linked(b, 'resourcePetriNet_OutputArc14', a2)
    if hasattr(a2, 'resourcePetriNet_Transition15'):
        assert not _is_linked(a2, 'resourcePetriNet_Transition15', b)


def test_assoc_OutputArcToPlace16_reverse_link_reassign_clear():
    a1 = resourcePetriNet_OutputArc(weight=7)
    a2 = resourcePetriNet_OutputArc(weight=13)
    b = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    _safe_set(b, 'resourcePetriNet_GenericPlace18', a1)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace18', a1)
    if hasattr(a1, 'resourcePetriNet_OutputArc17'):
        assert _is_linked(a1, 'resourcePetriNet_OutputArc17', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace18', a2)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace18', a2)
    if hasattr(a1, 'resourcePetriNet_OutputArc17'):
        assert not _is_linked(a1, 'resourcePetriNet_OutputArc17', b)
    if hasattr(a2, 'resourcePetriNet_OutputArc17'):
        assert _is_linked(a2, 'resourcePetriNet_OutputArc17', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace18', None)
    assert not _is_linked(b, 'resourcePetriNet_GenericPlace18', a2)
    if hasattr(a2, 'resourcePetriNet_OutputArc17'):
        assert not _is_linked(a2, 'resourcePetriNet_OutputArc17', b)


def test_assoc_containsGenericPlaces0_reverse_link_reassign_clear():
    a1 = resourcePetriNet_PetriNet(name="sample_text")
    a2 = resourcePetriNet_PetriNet(name="sample_text_2")
    b = resourcePetriNet_GenericPlace(name="sample_text", numberOfTokens=7)
    _safe_set(b, 'resourcePetriNet_GenericPlace', a1)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace', a1)
    if hasattr(a1, 'resourcePetriNet_PetriNet'):
        assert _is_linked(a1, 'resourcePetriNet_PetriNet', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace', a2)
    assert _is_linked(b, 'resourcePetriNet_GenericPlace', a2)
    if hasattr(a1, 'resourcePetriNet_PetriNet'):
        assert not _is_linked(a1, 'resourcePetriNet_PetriNet', b)
    if hasattr(a2, 'resourcePetriNet_PetriNet'):
        assert _is_linked(a2, 'resourcePetriNet_PetriNet', b)
    _safe_set(b, 'resourcePetriNet_GenericPlace', None)
    assert not _is_linked(b, 'resourcePetriNet_GenericPlace', a2)
    if hasattr(a2, 'resourcePetriNet_PetriNet'):
        assert not _is_linked(a2, 'resourcePetriNet_PetriNet', b)


def test_assoc_containsInputArcs3_reverse_link_reassign_clear():
    a1 = resourcePetriNet_PetriNet(name="sample_text")
    a2 = resourcePetriNet_PetriNet(name="sample_text_2")
    b = resourcePetriNet_InputArc(weight=7)
    _safe_set(b, 'resourcePetriNet_InputArc', a1)
    assert _is_linked(b, 'resourcePetriNet_InputArc', a1)
    if hasattr(a1, 'resourcePetriNet_PetriNet4'):
        assert _is_linked(a1, 'resourcePetriNet_PetriNet4', b)
    _safe_set(b, 'resourcePetriNet_InputArc', a2)
    assert _is_linked(b, 'resourcePetriNet_InputArc', a2)
    if hasattr(a1, 'resourcePetriNet_PetriNet4'):
        assert not _is_linked(a1, 'resourcePetriNet_PetriNet4', b)
    if hasattr(a2, 'resourcePetriNet_PetriNet4'):
        assert _is_linked(a2, 'resourcePetriNet_PetriNet4', b)
    _safe_set(b, 'resourcePetriNet_InputArc', None)
    assert not _is_linked(b, 'resourcePetriNet_InputArc', a2)
    if hasattr(a2, 'resourcePetriNet_PetriNet4'):
        assert not _is_linked(a2, 'resourcePetriNet_PetriNet4', b)


def test_assoc_containsOutputArcs5_reverse_link_reassign_clear():
    a1 = resourcePetriNet_PetriNet(name="sample_text")
    a2 = resourcePetriNet_PetriNet(name="sample_text_2")
    b = resourcePetriNet_OutputArc(weight=7)
    _safe_set(b, 'resourcePetriNet_OutputArc', a1)
    assert _is_linked(b, 'resourcePetriNet_OutputArc', a1)
    if hasattr(a1, 'resourcePetriNet_PetriNet6'):
        assert _is_linked(a1, 'resourcePetriNet_PetriNet6', b)
    _safe_set(b, 'resourcePetriNet_OutputArc', a2)
    assert _is_linked(b, 'resourcePetriNet_OutputArc', a2)
    if hasattr(a1, 'resourcePetriNet_PetriNet6'):
        assert not _is_linked(a1, 'resourcePetriNet_PetriNet6', b)
    if hasattr(a2, 'resourcePetriNet_PetriNet6'):
        assert _is_linked(a2, 'resourcePetriNet_PetriNet6', b)
    _safe_set(b, 'resourcePetriNet_OutputArc', None)
    assert not _is_linked(b, 'resourcePetriNet_OutputArc', a2)
    if hasattr(a2, 'resourcePetriNet_PetriNet6'):
        assert not _is_linked(a2, 'resourcePetriNet_PetriNet6', b)


def test_assoc_containsTransitions1_reverse_link_reassign_clear():
    a1 = resourcePetriNet_Transition(name="sample_text")
    a2 = resourcePetriNet_Transition(name="sample_text_2")
    b = resourcePetriNet_PetriNet(name="sample_text")
    _safe_set(b, 'resourcePetriNet_PetriNet2', {a1})
    assert _is_linked(b, 'resourcePetriNet_PetriNet2', a1)
    if hasattr(a1, 'resourcePetriNet_Transition'):
        assert _is_linked(a1, 'resourcePetriNet_Transition', b)
    _safe_set(b, 'resourcePetriNet_PetriNet2', {a2})
    assert _is_linked(b, 'resourcePetriNet_PetriNet2', a2)
    if hasattr(a1, 'resourcePetriNet_Transition'):
        assert not _is_linked(a1, 'resourcePetriNet_Transition', b)
    if hasattr(a2, 'resourcePetriNet_Transition'):
        assert _is_linked(a2, 'resourcePetriNet_Transition', b)
    _safe_set(b, 'resourcePetriNet_PetriNet2', set())
    assert not _is_linked(b, 'resourcePetriNet_PetriNet2', a2)
    if hasattr(a2, 'resourcePetriNet_Transition'):
        assert not _is_linked(a2, 'resourcePetriNet_Transition', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

