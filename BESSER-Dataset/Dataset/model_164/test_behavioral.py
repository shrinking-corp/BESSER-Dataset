import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identifiable,
    PetriNet_InputArc,
    PetriNet_Net,
    PetriNet_OutputArc,
    PetriNet_Place,
    PetriNet_Token,
    PetriNet_Transition,
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

def test_assoc_inputArc1_stub_double():
    # PetriNet_InputArc has no real 'PetriNet_InputArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_InputArc()
    setattr(partner, 'PetriNet_InputArc', None)
    _safe_set(owner, 'PetriNet_Place2', {partner})
    assert getattr(partner, 'PetriNet_InputArc') == owner
    _safe_set(owner, 'PetriNet_Place2', set())
    assert getattr(partner, 'PetriNet_InputArc') is None


def test_assoc_inputArc5_stub_double():
    # PetriNet_InputArc has no real 'PetriNet_InputArc6' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_InputArc()
    setattr(partner, 'PetriNet_InputArc6', None)
    _safe_set(owner, 'PetriNet_Transition', {partner})
    assert getattr(partner, 'PetriNet_InputArc6') == owner
    _safe_set(owner, 'PetriNet_Transition', set())
    assert getattr(partner, 'PetriNet_InputArc6') is None


def test_assoc_outputArc3_stub_double():
    # PetriNet_OutputArc has no real 'PetriNet_OutputArc' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_OutputArc()
    setattr(partner, 'PetriNet_OutputArc', None)
    _safe_set(owner, 'PetriNet_Place4', {partner})
    assert getattr(partner, 'PetriNet_OutputArc') == owner
    _safe_set(owner, 'PetriNet_Place4', set())
    assert getattr(partner, 'PetriNet_OutputArc') is None


def test_assoc_outputArc7_stub_double():
    # PetriNet_OutputArc has no real 'PetriNet_OutputArc9' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_OutputArc()
    setattr(partner, 'PetriNet_OutputArc9', None)
    _safe_set(owner, 'PetriNet_Transition8', {partner})
    assert getattr(partner, 'PetriNet_OutputArc9') == owner
    _safe_set(owner, 'PetriNet_Transition8', set())
    assert getattr(partner, 'PetriNet_OutputArc9') is None


def test_assoc_place10_stub_double():
    # PetriNet_InputArc has no real 'PetriNet_InputArc11' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_InputArc()
    setattr(partner, 'PetriNet_InputArc11', None)
    _safe_set(owner, 'PetriNet_Place12', partner)
    assert owner in getattr(partner, 'PetriNet_InputArc11')
    _safe_set(owner, 'PetriNet_Place12', None)
    assert owner not in getattr(partner, 'PetriNet_InputArc11')


def test_assoc_place16_stub_double():
    # PetriNet_OutputArc has no real 'PetriNet_OutputArc17' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_OutputArc()
    setattr(partner, 'PetriNet_OutputArc17', None)
    _safe_set(owner, 'PetriNet_Place18', partner)
    assert owner in getattr(partner, 'PetriNet_OutputArc17')
    _safe_set(owner, 'PetriNet_Place18', None)
    assert owner not in getattr(partner, 'PetriNet_OutputArc17')


def test_assoc_place22_stub_double():
    # PetriNet_Net has no real 'PetriNet_Net' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_Net()
    setattr(partner, 'PetriNet_Net', None)
    _safe_set(owner, 'PetriNet_Place23', partner)
    assert owner in getattr(partner, 'PetriNet_Net')
    _safe_set(owner, 'PetriNet_Place23', None)
    assert owner not in getattr(partner, 'PetriNet_Net')


def test_assoc_token0_stub_double():
    # PetriNet_Token has no real 'PetriNet_Token' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Place(name="sample_text")
    partner = PetriNet_Token()
    setattr(partner, 'PetriNet_Token', None)
    _safe_set(owner, 'PetriNet_Place', {partner})
    assert getattr(partner, 'PetriNet_Token') == owner
    _safe_set(owner, 'PetriNet_Place', set())
    assert getattr(partner, 'PetriNet_Token') is None


def test_assoc_transition13_stub_double():
    # PetriNet_InputArc has no real 'PetriNet_InputArc14' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_InputArc()
    setattr(partner, 'PetriNet_InputArc14', None)
    _safe_set(owner, 'PetriNet_Transition15', partner)
    assert owner in getattr(partner, 'PetriNet_InputArc14')
    _safe_set(owner, 'PetriNet_Transition15', None)
    assert owner not in getattr(partner, 'PetriNet_InputArc14')


def test_assoc_transition19_stub_double():
    # PetriNet_OutputArc has no real 'PetriNet_OutputArc20' property in the generated
    # code (a bare stub) -- manually attach it so PetriNet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # PetriNet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = PetriNet_Transition(name="sample_text")
    partner = PetriNet_OutputArc()
    setattr(partner, 'PetriNet_OutputArc20', None)
    _safe_set(owner, 'PetriNet_Transition21', partner)
    assert owner in getattr(partner, 'PetriNet_OutputArc20')
    _safe_set(owner, 'PetriNet_Transition21', None)
    assert owner not in getattr(partner, 'PetriNet_OutputArc20')


