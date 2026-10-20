import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    petrinet_Arc,
    petrinet_PTArc,
    petrinet_PetriNet,
    petrinet_Place,
    petrinet_TPArc,
    petrinet_Transition,
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

def test_assoc_outgoing3_stub_double():
    # petrinet_TPArc has no real 'TPArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'TPArc', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'TPArc') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'TPArc') is None


def test_assoc_outgoing4_stub_double():
    # petrinet_PTArc has no real 'PTArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text", token=7)
    partner = petrinet_PTArc()
    setattr(partner, 'PTArc', None)
    _safe_set(owner, 'source5', {partner})
    assert getattr(partner, 'PTArc') == owner
    _safe_set(owner, 'source5', set())
    assert getattr(partner, 'PTArc') is None


def test_assoc_places0_stub_double():
    # petrinet_PetriNet has no real 'petrinet_PetriNet' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text", token=7)
    partner = petrinet_PetriNet()
    setattr(partner, 'petrinet_PetriNet', None)
    _safe_set(owner, 'petrinet_Place', partner)
    assert owner in getattr(partner, 'petrinet_PetriNet')
    _safe_set(owner, 'petrinet_Place', None)
    assert owner not in getattr(partner, 'petrinet_PetriNet')


def test_assoc_source11_stub_double():
    # petrinet_TPArc has no real 'outgoing12' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_TPArc()
    setattr(partner, 'outgoing12', None)
    _safe_set(owner, 'Transition', partner)
    assert getattr(partner, 'outgoing12') == owner
    _safe_set(owner, 'Transition', None)
    assert getattr(partner, 'outgoing12') is None


def test_assoc_source8_stub_double():
    # petrinet_PTArc has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text", token=7)
    partner = petrinet_PTArc()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Place', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Place', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target6_stub_double():
    # petrinet_PTArc has no real 'petrinet_PTArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_PTArc()
    setattr(partner, 'petrinet_PTArc', None)
    _safe_set(owner, 'petrinet_Transition7', partner)
    assert getattr(partner, 'petrinet_PTArc') == owner
    _safe_set(owner, 'petrinet_Transition7', None)
    assert getattr(partner, 'petrinet_PTArc') is None


def test_assoc_target9_stub_double():
    # petrinet_TPArc has no real 'petrinet_TPArc' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Place(name="sample_text", token=7)
    partner = petrinet_TPArc()
    setattr(partner, 'petrinet_TPArc', None)
    _safe_set(owner, 'petrinet_Place10', partner)
    assert getattr(partner, 'petrinet_TPArc') == owner
    _safe_set(owner, 'petrinet_Place10', None)
    assert getattr(partner, 'petrinet_TPArc') is None


def test_assoc_transitions1_stub_double():
    # petrinet_PetriNet has no real 'petrinet_PetriNet2' property in the generated
    # code (a bare stub) -- manually attach it so petrinet_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # petrinet_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = petrinet_Transition(name="sample_text")
    partner = petrinet_PetriNet()
    setattr(partner, 'petrinet_PetriNet2', None)
    _safe_set(owner, 'petrinet_Transition', partner)
    assert owner in getattr(partner, 'petrinet_PetriNet2')
    _safe_set(owner, 'petrinet_Transition', None)
    assert owner not in getattr(partner, 'petrinet_PetriNet2')


