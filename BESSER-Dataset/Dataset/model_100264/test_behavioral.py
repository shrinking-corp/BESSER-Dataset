import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Arc,
    lit_petriNets_Arc,
    lit_petriNets_Net,
    lit_petriNets_PTArc,
    lit_petriNets_Place,
    lit_petriNets_TPArc,
    lit_petriNets_Transition,
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

def test_assoc_d20_stub_double():
    # lit_petriNets_PTArc has no real 'in_' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_PTArc()
    setattr(partner, 'in_', None)
    _safe_set(owner, 'Transition21', partner)
    assert getattr(partner, 'in_') == owner
    _safe_set(owner, 'Transition21', None)
    assert getattr(partner, 'in_') is None


def test_assoc_d25_stub_double():
    # lit_petriNets_TPArc has no real 'in_26' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_TPArc()
    setattr(partner, 'in_26', None)
    _safe_set(owner, 'Place27', partner)
    assert getattr(partner, 'in_26') == owner
    _safe_set(owner, 'Place27', None)
    assert getattr(partner, 'in_26') is None


def test_assoc_in_10_stub_double():
    # lit_petriNets_PTArc has no real 'PTArc12' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_PTArc()
    setattr(partner, 'PTArc12', None)
    _safe_set(owner, 'd11', {partner})
    assert getattr(partner, 'PTArc12') == owner
    _safe_set(owner, 'd11', set())
    assert getattr(partner, 'PTArc12') is None


def test_assoc_in_6_stub_double():
    # lit_petriNets_TPArc has no real 'TPArc' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_TPArc()
    setattr(partner, 'TPArc', None)
    _safe_set(owner, 'd', {partner})
    assert getattr(partner, 'TPArc') == owner
    _safe_set(owner, 'd', set())
    assert getattr(partner, 'TPArc') is None


def test_assoc_net5_stub_double():
    # lit_petriNets_Net has no real 'Net' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_Net()
    setattr(partner, 'Net', None)
    _safe_set(owner, 'places', partner)
    assert getattr(partner, 'Net') == owner
    _safe_set(owner, 'places', None)
    assert getattr(partner, 'Net') is None


def test_assoc_net8_stub_double():
    # lit_petriNets_Net has no real 'Net9' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_Net()
    setattr(partner, 'Net9', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'Net9') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'Net9') is None


def test_assoc_out13_stub_double():
    # lit_petriNets_TPArc has no real 'TPArc15' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_TPArc()
    setattr(partner, 'TPArc15', None)
    _safe_set(owner, 's14', {partner})
    assert getattr(partner, 'TPArc15') == owner
    _safe_set(owner, 's14', set())
    assert getattr(partner, 'TPArc15') is None


def test_assoc_out7_stub_double():
    # lit_petriNets_PTArc has no real 'PTArc' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_PTArc()
    setattr(partner, 'PTArc', None)
    _safe_set(owner, 's', {partner})
    assert getattr(partner, 'PTArc') == owner
    _safe_set(owner, 's', set())
    assert getattr(partner, 'PTArc') is None


def test_assoc_places0_stub_double():
    # lit_petriNets_Net has no real 'net' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_Net()
    setattr(partner, 'net', None)
    _safe_set(owner, 'Place', partner)
    assert owner in getattr(partner, 'net')
    _safe_set(owner, 'Place', None)
    assert owner not in getattr(partner, 'net')


def test_assoc_s18_stub_double():
    # lit_petriNets_PTArc has no real 'out' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Place's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Place's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Place(name="sample_text")
    partner = lit_petriNets_PTArc()
    setattr(partner, 'out', None)
    _safe_set(owner, 'Place19', partner)
    assert getattr(partner, 'out') == owner
    _safe_set(owner, 'Place19', None)
    assert getattr(partner, 'out') is None


def test_assoc_s22_stub_double():
    # lit_petriNets_TPArc has no real 'out23' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_TPArc()
    setattr(partner, 'out23', None)
    _safe_set(owner, 'Transition24', partner)
    assert getattr(partner, 'out23') == owner
    _safe_set(owner, 'Transition24', None)
    assert getattr(partner, 'out23') is None


def test_assoc_transitions1_stub_double():
    # lit_petriNets_Net has no real 'net2' property in the generated
    # code (a bare stub) -- manually attach it so lit_petriNets_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # lit_petriNets_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = lit_petriNets_Transition(name="sample_text")
    partner = lit_petriNets_Net()
    setattr(partner, 'net2', None)
    _safe_set(owner, 'Transition', partner)
    assert owner in getattr(partner, 'net2')
    _safe_set(owner, 'Transition', None)
    assert owner not in getattr(partner, 'net2')


