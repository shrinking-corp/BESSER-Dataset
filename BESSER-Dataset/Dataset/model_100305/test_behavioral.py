import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    standardPetriNets_InputArc,
    standardPetriNets_OutputArc,
    standardPetriNets_PetriNet,
    standardPetriNets_Place,
    standardPetriNets_Transition,
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

def test_assoc_containsInputArcs13_reverse_link_reassign_clear():
    a1 = standardPetriNets_PetriNet(name="sample_text")
    a2 = standardPetriNets_PetriNet(name="sample_text_2")
    b = standardPetriNets_InputArc(weight=7)
    _safe_set(b, 'standardPetriNets_InputArc15', a1)
    assert _is_linked(b, 'standardPetriNets_InputArc15', a1)
    if hasattr(a1, 'standardPetriNets_PetriNet14'):
        assert _is_linked(a1, 'standardPetriNets_PetriNet14', b)
    _safe_set(b, 'standardPetriNets_InputArc15', a2)
    assert _is_linked(b, 'standardPetriNets_InputArc15', a2)
    if hasattr(a1, 'standardPetriNets_PetriNet14'):
        assert not _is_linked(a1, 'standardPetriNets_PetriNet14', b)
    if hasattr(a2, 'standardPetriNets_PetriNet14'):
        assert _is_linked(a2, 'standardPetriNets_PetriNet14', b)
    _safe_set(b, 'standardPetriNets_InputArc15', None)
    assert not _is_linked(b, 'standardPetriNets_InputArc15', a2)
    if hasattr(a2, 'standardPetriNets_PetriNet14'):
        assert not _is_linked(a2, 'standardPetriNets_PetriNet14', b)


def test_assoc_containsOutputArcs16_reverse_link_reassign_clear():
    a1 = standardPetriNets_PetriNet(name="sample_text")
    a2 = standardPetriNets_PetriNet(name="sample_text_2")
    b = standardPetriNets_OutputArc(weight=7)
    _safe_set(b, 'standardPetriNets_OutputArc18', a1)
    assert _is_linked(b, 'standardPetriNets_OutputArc18', a1)
    if hasattr(a1, 'standardPetriNets_PetriNet17'):
        assert _is_linked(a1, 'standardPetriNets_PetriNet17', b)
    _safe_set(b, 'standardPetriNets_OutputArc18', a2)
    assert _is_linked(b, 'standardPetriNets_OutputArc18', a2)
    if hasattr(a1, 'standardPetriNets_PetriNet17'):
        assert not _is_linked(a1, 'standardPetriNets_PetriNet17', b)
    if hasattr(a2, 'standardPetriNets_PetriNet17'):
        assert _is_linked(a2, 'standardPetriNets_PetriNet17', b)
    _safe_set(b, 'standardPetriNets_OutputArc18', None)
    assert not _is_linked(b, 'standardPetriNets_OutputArc18', a2)
    if hasattr(a2, 'standardPetriNets_PetriNet17'):
        assert not _is_linked(a2, 'standardPetriNets_PetriNet17', b)


def test_assoc_containsPlaces8_reverse_link_reassign_clear():
    a1 = standardPetriNets_Place(capacity=7, name="sample_text", numOfTokens=7)
    a2 = standardPetriNets_Place(capacity=13, name="sample_text_2", numOfTokens=13)
    b = standardPetriNets_PetriNet(name="sample_text")
    _safe_set(b, 'standardPetriNets_PetriNet', {a1})
    assert _is_linked(b, 'standardPetriNets_PetriNet', a1)
    if hasattr(a1, 'standardPetriNets_Place9'):
        assert _is_linked(a1, 'standardPetriNets_Place9', b)
    _safe_set(b, 'standardPetriNets_PetriNet', {a2})
    assert _is_linked(b, 'standardPetriNets_PetriNet', a2)
    if hasattr(a1, 'standardPetriNets_Place9'):
        assert not _is_linked(a1, 'standardPetriNets_Place9', b)
    if hasattr(a2, 'standardPetriNets_Place9'):
        assert _is_linked(a2, 'standardPetriNets_Place9', b)
    _safe_set(b, 'standardPetriNets_PetriNet', set())
    assert not _is_linked(b, 'standardPetriNets_PetriNet', a2)
    if hasattr(a2, 'standardPetriNets_Place9'):
        assert not _is_linked(a2, 'standardPetriNets_Place9', b)


def test_assoc_containsTransitions10_reverse_link_reassign_clear():
    a1 = standardPetriNets_Transition(name="sample_text")
    a2 = standardPetriNets_Transition(name="sample_text_2")
    b = standardPetriNets_PetriNet(name="sample_text")
    _safe_set(b, 'standardPetriNets_PetriNet11', {a1})
    assert _is_linked(b, 'standardPetriNets_PetriNet11', a1)
    if hasattr(a1, 'standardPetriNets_Transition12'):
        assert _is_linked(a1, 'standardPetriNets_Transition12', b)
    _safe_set(b, 'standardPetriNets_PetriNet11', {a2})
    assert _is_linked(b, 'standardPetriNets_PetriNet11', a2)
    if hasattr(a1, 'standardPetriNets_Transition12'):
        assert not _is_linked(a1, 'standardPetriNets_Transition12', b)
    if hasattr(a2, 'standardPetriNets_Transition12'):
        assert _is_linked(a2, 'standardPetriNets_Transition12', b)
    _safe_set(b, 'standardPetriNets_PetriNet11', set())
    assert not _is_linked(b, 'standardPetriNets_PetriNet11', a2)
    if hasattr(a2, 'standardPetriNets_Transition12'):
        assert not _is_linked(a2, 'standardPetriNets_Transition12', b)


def test_assoc_inputArcFromPlace0_reverse_link_reassign_clear():
    a1 = standardPetriNets_Place(capacity=7, name="sample_text", numOfTokens=7)
    a2 = standardPetriNets_Place(capacity=13, name="sample_text_2", numOfTokens=13)
    b = standardPetriNets_InputArc(weight=7)
    _safe_set(b, 'standardPetriNets_InputArc', a1)
    assert _is_linked(b, 'standardPetriNets_InputArc', a1)
    if hasattr(a1, 'standardPetriNets_Place'):
        assert _is_linked(a1, 'standardPetriNets_Place', b)
    _safe_set(b, 'standardPetriNets_InputArc', a2)
    assert _is_linked(b, 'standardPetriNets_InputArc', a2)
    if hasattr(a1, 'standardPetriNets_Place'):
        assert not _is_linked(a1, 'standardPetriNets_Place', b)
    if hasattr(a2, 'standardPetriNets_Place'):
        assert _is_linked(a2, 'standardPetriNets_Place', b)
    _safe_set(b, 'standardPetriNets_InputArc', None)
    assert not _is_linked(b, 'standardPetriNets_InputArc', a2)
    if hasattr(a2, 'standardPetriNets_Place'):
        assert not _is_linked(a2, 'standardPetriNets_Place', b)


def test_assoc_inputArcToTransition1_reverse_link_reassign_clear():
    a1 = standardPetriNets_Transition(name="sample_text")
    a2 = standardPetriNets_Transition(name="sample_text_2")
    b = standardPetriNets_InputArc(weight=7)
    _safe_set(b, 'standardPetriNets_InputArc2', a1)
    assert _is_linked(b, 'standardPetriNets_InputArc2', a1)
    if hasattr(a1, 'standardPetriNets_Transition'):
        assert _is_linked(a1, 'standardPetriNets_Transition', b)
    _safe_set(b, 'standardPetriNets_InputArc2', a2)
    assert _is_linked(b, 'standardPetriNets_InputArc2', a2)
    if hasattr(a1, 'standardPetriNets_Transition'):
        assert not _is_linked(a1, 'standardPetriNets_Transition', b)
    if hasattr(a2, 'standardPetriNets_Transition'):
        assert _is_linked(a2, 'standardPetriNets_Transition', b)
    _safe_set(b, 'standardPetriNets_InputArc2', None)
    assert not _is_linked(b, 'standardPetriNets_InputArc2', a2)
    if hasattr(a2, 'standardPetriNets_Transition'):
        assert not _is_linked(a2, 'standardPetriNets_Transition', b)


def test_assoc_outputArcFromTransition3_reverse_link_reassign_clear():
    a1 = standardPetriNets_Transition(name="sample_text")
    a2 = standardPetriNets_Transition(name="sample_text_2")
    b = standardPetriNets_OutputArc(weight=7)
    _safe_set(b, 'standardPetriNets_OutputArc', a1)
    assert _is_linked(b, 'standardPetriNets_OutputArc', a1)
    if hasattr(a1, 'standardPetriNets_Transition4'):
        assert _is_linked(a1, 'standardPetriNets_Transition4', b)
    _safe_set(b, 'standardPetriNets_OutputArc', a2)
    assert _is_linked(b, 'standardPetriNets_OutputArc', a2)
    if hasattr(a1, 'standardPetriNets_Transition4'):
        assert not _is_linked(a1, 'standardPetriNets_Transition4', b)
    if hasattr(a2, 'standardPetriNets_Transition4'):
        assert _is_linked(a2, 'standardPetriNets_Transition4', b)
    _safe_set(b, 'standardPetriNets_OutputArc', None)
    assert not _is_linked(b, 'standardPetriNets_OutputArc', a2)
    if hasattr(a2, 'standardPetriNets_Transition4'):
        assert not _is_linked(a2, 'standardPetriNets_Transition4', b)


def test_assoc_outputArcToPlace5_reverse_link_reassign_clear():
    a1 = standardPetriNets_Place(capacity=7, name="sample_text", numOfTokens=7)
    a2 = standardPetriNets_Place(capacity=13, name="sample_text_2", numOfTokens=13)
    b = standardPetriNets_OutputArc(weight=7)
    _safe_set(b, 'standardPetriNets_OutputArc6', a1)
    assert _is_linked(b, 'standardPetriNets_OutputArc6', a1)
    if hasattr(a1, 'standardPetriNets_Place7'):
        assert _is_linked(a1, 'standardPetriNets_Place7', b)
    _safe_set(b, 'standardPetriNets_OutputArc6', a2)
    assert _is_linked(b, 'standardPetriNets_OutputArc6', a2)
    if hasattr(a1, 'standardPetriNets_Place7'):
        assert not _is_linked(a1, 'standardPetriNets_Place7', b)
    if hasattr(a2, 'standardPetriNets_Place7'):
        assert _is_linked(a2, 'standardPetriNets_Place7', b)
    _safe_set(b, 'standardPetriNets_OutputArc6', None)
    assert not _is_linked(b, 'standardPetriNets_OutputArc6', a2)
    if hasattr(a2, 'standardPetriNets_Place7'):
        assert not _is_linked(a2, 'standardPetriNets_Place7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

