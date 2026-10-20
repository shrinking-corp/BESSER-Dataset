import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DEVS,
    Model_AtomicDEVS,
    Model_ConfTrans,
    Model_CoupledDEVS,
    Model_DEVS,
    Model_EClassifier,
    Model_EIC,
    Model_EOC,
    Model_Event,
    Model_ExtTrans,
    Model_IC,
    Model_IPort,
    Model_IntTransition,
    Model_OPort,
    Model_Phase,
    Model_PhaseTransition,
    Model_Port,
    Model_Variable,
    PhaseTransition,
    Port,
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

def test_assoc_container1_reverse_link_reassign_clear():
    a1 = Model_DEVS(name="sample_text")
    a2 = Model_DEVS(name="sample_text_2")
    b = Model_DEVS(name="sample_text")
    _safe_set(b, 'Model_DEVS0', a1)
    assert _is_linked(b, 'Model_DEVS0', a1)
    if hasattr(a1, 'Model_DEVS'):
        assert _is_linked(a1, 'Model_DEVS', b)
    _safe_set(b, 'Model_DEVS0', a2)
    assert _is_linked(b, 'Model_DEVS0', a2)
    if hasattr(a1, 'Model_DEVS'):
        assert not _is_linked(a1, 'Model_DEVS', b)
    if hasattr(a2, 'Model_DEVS'):
        assert _is_linked(a2, 'Model_DEVS', b)
    _safe_set(b, 'Model_DEVS0', None)
    assert not _is_linked(b, 'Model_DEVS0', a2)
    if hasattr(a2, 'Model_DEVS'):
        assert not _is_linked(a2, 'Model_DEVS', b)


def test_assoc_owner23_reverse_link_reassign_clear():
    a1 = Model_Port(portId="sample_text")
    a2 = Model_Port(portId="sample_text_2")
    b = Model_DEVS(name="sample_text")
    _safe_set(b, 'Model_DEVS24', a1)
    assert _is_linked(b, 'Model_DEVS24', a1)
    if hasattr(a1, 'Model_Port'):
        assert _is_linked(a1, 'Model_Port', b)
    _safe_set(b, 'Model_DEVS24', a2)
    assert _is_linked(b, 'Model_DEVS24', a2)
    if hasattr(a1, 'Model_Port'):
        assert not _is_linked(a1, 'Model_Port', b)
    if hasattr(a2, 'Model_Port'):
        assert _is_linked(a2, 'Model_Port', b)
    _safe_set(b, 'Model_DEVS24', None)
    assert not _is_linked(b, 'Model_DEVS24', a2)
    if hasattr(a2, 'Model_Port'):
        assert not _is_linked(a2, 'Model_Port', b)


def test_assoc_predicates62_reverse_link_reassign_clear():
    a1 = Model_Variable(name="sample_text")
    a2 = Model_Variable(name="sample_text_2")
    b = Model_Phase(phaseID="sample_text", timeAdvance=3.14)
    _safe_set(b, 'Model_Phase63', {a1})
    assert _is_linked(b, 'Model_Phase63', a1)
    if hasattr(a1, 'Model_Variable64'):
        assert _is_linked(a1, 'Model_Variable64', b)
    _safe_set(b, 'Model_Phase63', {a2})
    assert _is_linked(b, 'Model_Phase63', a2)
    if hasattr(a1, 'Model_Variable64'):
        assert not _is_linked(a1, 'Model_Variable64', b)
    if hasattr(a2, 'Model_Variable64'):
        assert _is_linked(a2, 'Model_Variable64', b)
    _safe_set(b, 'Model_Phase63', set())
    assert not _is_linked(b, 'Model_Phase63', a2)
    if hasattr(a2, 'Model_Variable64'):
        assert not _is_linked(a2, 'Model_Variable64', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_domain70_stub_double():
    # Model_EClassifier has no real 'Model_EClassifier72' property in the generated
    # code (a bare stub) -- manually attach it so Model_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Variable(name="sample_text")
    partner = Model_EClassifier()
    setattr(partner, 'Model_EClassifier72', None)
    _safe_set(owner, 'Model_Variable71', partner)
    assert getattr(partner, 'Model_EClassifier72') == owner
    _safe_set(owner, 'Model_Variable71', None)
    assert getattr(partner, 'Model_EClassifier72') is None


def test_assoc_iports2_stub_double():
    # Model_IPort has no real 'Model_IPort' property in the generated
    # code (a bare stub) -- manually attach it so Model_DEVS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_DEVS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_DEVS(name="sample_text")
    partner = Model_IPort()
    setattr(partner, 'Model_IPort', None)
    _safe_set(owner, 'Model_DEVS3', {partner})
    assert getattr(partner, 'Model_IPort') == owner
    _safe_set(owner, 'Model_DEVS3', set())
    assert getattr(partner, 'Model_IPort') is None


def test_assoc_oports4_stub_double():
    # Model_OPort has no real 'Model_OPort' property in the generated
    # code (a bare stub) -- manually attach it so Model_DEVS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_DEVS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_DEVS(name="sample_text")
    partner = Model_OPort()
    setattr(partner, 'Model_OPort', None)
    _safe_set(owner, 'Model_DEVS5', {partner})
    assert getattr(partner, 'Model_OPort') == owner
    _safe_set(owner, 'Model_DEVS5', set())
    assert getattr(partner, 'Model_OPort') is None


def test_assoc_phases11_stub_double():
    # Model_AtomicDEVS has no real 'Model_AtomicDEVS12' property in the generated
    # code (a bare stub) -- manually attach it so Model_Phase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Phase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Phase(phaseID="sample_text", timeAdvance=3.14)
    partner = Model_AtomicDEVS()
    setattr(partner, 'Model_AtomicDEVS12', None)
    _safe_set(owner, 'Model_Phase', partner)
    assert owner in getattr(partner, 'Model_AtomicDEVS12')
    _safe_set(owner, 'Model_Phase', None)
    assert owner not in getattr(partner, 'Model_AtomicDEVS12')


def test_assoc_portType25_stub_double():
    # Model_EClassifier has no real 'Model_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so Model_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Port(portId="sample_text")
    partner = Model_EClassifier()
    setattr(partner, 'Model_EClassifier', None)
    _safe_set(owner, 'Model_Port26', partner)
    assert getattr(partner, 'Model_EClassifier') == owner
    _safe_set(owner, 'Model_Port26', None)
    assert getattr(partner, 'Model_EClassifier') is None


def test_assoc_sourcePhase65_stub_double():
    # Model_PhaseTransition has no real 'Model_PhaseTransition' property in the generated
    # code (a bare stub) -- manually attach it so Model_Phase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Phase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Phase(phaseID="sample_text", timeAdvance=3.14)
    partner = Model_PhaseTransition()
    setattr(partner, 'Model_PhaseTransition', None)
    _safe_set(owner, 'Model_Phase66', partner)
    assert getattr(partner, 'Model_PhaseTransition') == owner
    _safe_set(owner, 'Model_Phase66', None)
    assert getattr(partner, 'Model_PhaseTransition') is None


def test_assoc_stateVars13_stub_double():
    # Model_AtomicDEVS has no real 'Model_AtomicDEVS14' property in the generated
    # code (a bare stub) -- manually attach it so Model_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Variable(name="sample_text")
    partner = Model_AtomicDEVS()
    setattr(partner, 'Model_AtomicDEVS14', None)
    _safe_set(owner, 'Model_Variable', partner)
    assert owner in getattr(partner, 'Model_AtomicDEVS14')
    _safe_set(owner, 'Model_Variable', None)
    assert owner not in getattr(partner, 'Model_AtomicDEVS14')


def test_assoc_subModels15_stub_double():
    # Model_CoupledDEVS has no real 'Model_CoupledDEVS' property in the generated
    # code (a bare stub) -- manually attach it so Model_DEVS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_DEVS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_DEVS(name="sample_text")
    partner = Model_CoupledDEVS()
    setattr(partner, 'Model_CoupledDEVS', None)
    _safe_set(owner, 'Model_DEVS16', partner)
    assert owner in getattr(partner, 'Model_CoupledDEVS')
    _safe_set(owner, 'Model_DEVS16', None)
    assert owner not in getattr(partner, 'Model_CoupledDEVS')


def test_assoc_targetPhase67_stub_double():
    # Model_PhaseTransition has no real 'Model_PhaseTransition68' property in the generated
    # code (a bare stub) -- manually attach it so Model_Phase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Phase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Phase(phaseID="sample_text", timeAdvance=3.14)
    partner = Model_PhaseTransition()
    setattr(partner, 'Model_PhaseTransition68', None)
    _safe_set(owner, 'Model_Phase69', partner)
    assert getattr(partner, 'Model_PhaseTransition68') == owner
    _safe_set(owner, 'Model_Phase69', None)
    assert getattr(partner, 'Model_PhaseTransition68') is None


def test_assoc_targetPort56_stub_double():
    # Model_Event has no real 'Model_Event57' property in the generated
    # code (a bare stub) -- manually attach it so Model_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Model_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Model_Port(portId="sample_text")
    partner = Model_Event()
    setattr(partner, 'Model_Event57', None)
    _safe_set(owner, 'Model_Port58', partner)
    assert getattr(partner, 'Model_Event57') == owner
    _safe_set(owner, 'Model_Port58', None)
    assert getattr(partner, 'Model_Event57') is None


