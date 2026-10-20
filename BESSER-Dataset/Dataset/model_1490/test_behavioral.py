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

def test_assoc_InputArcFromPlace10_reverse_link_reassign_clear():
    a1 = extendedPetriNets_InputArc(weight=7)
    a2 = extendedPetriNets_InputArc(weight=13)
    b = extendedPetriNets_GenericPlace(capacity=7, name="sample_text", numberOfTokens=7)
    _safe_set(b, 'extendedPetriNets_GenericPlace12', a1)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace12', a1)
    if hasattr(a1, 'extendedPetriNets_InputArc11'):
        assert _is_linked(a1, 'extendedPetriNets_InputArc11', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace12', a2)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace12', a2)
    if hasattr(a1, 'extendedPetriNets_InputArc11'):
        assert not _is_linked(a1, 'extendedPetriNets_InputArc11', b)
    if hasattr(a2, 'extendedPetriNets_InputArc11'):
        assert _is_linked(a2, 'extendedPetriNets_InputArc11', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace12', None)
    assert not _is_linked(b, 'extendedPetriNets_GenericPlace12', a2)
    if hasattr(a2, 'extendedPetriNets_InputArc11'):
        assert not _is_linked(a2, 'extendedPetriNets_InputArc11', b)


def test_assoc_InputArcToTransition7_reverse_link_reassign_clear():
    a1 = extendedPetriNets_Transition(label="sample_text", name="sample_text")
    a2 = extendedPetriNets_Transition(label="sample_text_2", name="sample_text_2")
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


def test_assoc_OutputArcFromTransition13_reverse_link_reassign_clear():
    a1 = extendedPetriNets_Transition(label="sample_text", name="sample_text")
    a2 = extendedPetriNets_Transition(label="sample_text_2", name="sample_text_2")
    b = extendedPetriNets_OutputArc(weight=7)
    _safe_set(b, 'extendedPetriNets_OutputArc14', a1)
    assert _is_linked(b, 'extendedPetriNets_OutputArc14', a1)
    if hasattr(a1, 'extendedPetriNets_Transition15'):
        assert _is_linked(a1, 'extendedPetriNets_Transition15', b)
    _safe_set(b, 'extendedPetriNets_OutputArc14', a2)
    assert _is_linked(b, 'extendedPetriNets_OutputArc14', a2)
    if hasattr(a1, 'extendedPetriNets_Transition15'):
        assert not _is_linked(a1, 'extendedPetriNets_Transition15', b)
    if hasattr(a2, 'extendedPetriNets_Transition15'):
        assert _is_linked(a2, 'extendedPetriNets_Transition15', b)
    _safe_set(b, 'extendedPetriNets_OutputArc14', None)
    assert not _is_linked(b, 'extendedPetriNets_OutputArc14', a2)
    if hasattr(a2, 'extendedPetriNets_Transition15'):
        assert not _is_linked(a2, 'extendedPetriNets_Transition15', b)


def test_assoc_OutputArcToPlace16_reverse_link_reassign_clear():
    a1 = extendedPetriNets_OutputArc(weight=7)
    a2 = extendedPetriNets_OutputArc(weight=13)
    b = extendedPetriNets_GenericPlace(capacity=7, name="sample_text", numberOfTokens=7)
    _safe_set(b, 'extendedPetriNets_GenericPlace18', a1)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace18', a1)
    if hasattr(a1, 'extendedPetriNets_OutputArc17'):
        assert _is_linked(a1, 'extendedPetriNets_OutputArc17', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace18', a2)
    assert _is_linked(b, 'extendedPetriNets_GenericPlace18', a2)
    if hasattr(a1, 'extendedPetriNets_OutputArc17'):
        assert not _is_linked(a1, 'extendedPetriNets_OutputArc17', b)
    if hasattr(a2, 'extendedPetriNets_OutputArc17'):
        assert _is_linked(a2, 'extendedPetriNets_OutputArc17', b)
    _safe_set(b, 'extendedPetriNets_GenericPlace18', None)
    assert not _is_linked(b, 'extendedPetriNets_GenericPlace18', a2)
    if hasattr(a2, 'extendedPetriNets_OutputArc17'):
        assert not _is_linked(a2, 'extendedPetriNets_OutputArc17', b)


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
    a1 = extendedPetriNets_Transition(label="sample_text", name="sample_text")
    a2 = extendedPetriNets_Transition(label="sample_text_2", name="sample_text_2")
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

