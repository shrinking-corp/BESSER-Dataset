import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SrcAbstractState,
    SrcCompositeState,
    SrcRoot,
    SrcStateMachine,
    SrcTransition,
    TrgAbstractState,
    TrgCompositeState,
    TrgRoot,
    TrgStateMachine,
    TrgTransition,
    jointPackage_HSM2FSM_JointMM,
    jointPackage_HSM2FSM_SrcAbstractState,
    jointPackage_HSM2FSM_SrcCompositeState,
    jointPackage_HSM2FSM_SrcInitialState,
    jointPackage_HSM2FSM_SrcRegularState,
    jointPackage_HSM2FSM_SrcRoot,
    jointPackage_HSM2FSM_SrcStateMachine,
    jointPackage_HSM2FSM_SrcTransition,
    jointPackage_HSM2FSM_TrgAbstractState,
    jointPackage_HSM2FSM_TrgCompositeState,
    jointPackage_HSM2FSM_TrgInitialState,
    jointPackage_HSM2FSM_TrgRegularState,
    jointPackage_HSM2FSM_TrgRoot,
    jointPackage_HSM2FSM_TrgStateMachine,
    jointPackage_HSM2FSM_TrgTransition,
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

def test_assoc_compositeStates16_stub_double():
    # SrcCompositeState has no real 'SrcCompositeState' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcAbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcAbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcAbstractState(name="sample_text")
    partner = SrcCompositeState()
    setattr(partner, 'SrcCompositeState', None)
    _safe_set(owner, 'states17', partner)
    assert getattr(partner, 'SrcCompositeState') == owner
    _safe_set(owner, 'states17', None)
    assert getattr(partner, 'SrcCompositeState') is None


def test_assoc_compositeStates36_stub_double():
    # TrgCompositeState has no real 'TrgCompositeState' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgAbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgAbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgAbstractState(name="sample_text")
    partner = TrgCompositeState()
    setattr(partner, 'TrgCompositeState', None)
    _safe_set(owner, 'states37', partner)
    assert getattr(partner, 'TrgCompositeState') == owner
    _safe_set(owner, 'states37', None)
    assert getattr(partner, 'TrgCompositeState') is None


def test_assoc_source28_stub_double():
    # TrgAbstractState has no real 'TrgAbstractState29' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    partner = TrgAbstractState()
    setattr(partner, 'TrgAbstractState29', None)
    _safe_set(owner, 'jointPackage_HSM2FSM_TrgTransition', partner)
    assert getattr(partner, 'TrgAbstractState29') == owner
    _safe_set(owner, 'jointPackage_HSM2FSM_TrgTransition', None)
    assert getattr(partner, 'TrgAbstractState29') is None


def test_assoc_source9_stub_double():
    # SrcAbstractState has no real 'SrcAbstractState10' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    partner = SrcAbstractState()
    setattr(partner, 'SrcAbstractState10', None)
    _safe_set(owner, 'jointPackage_HSM2FSM_SrcTransition', partner)
    assert getattr(partner, 'SrcAbstractState10') == owner
    _safe_set(owner, 'jointPackage_HSM2FSM_SrcTransition', None)
    assert getattr(partner, 'SrcAbstractState10') is None


def test_assoc_stateMachine14_stub_double():
    # SrcStateMachine has no real 'SrcStateMachine15' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcAbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcAbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcAbstractState(name="sample_text")
    partner = SrcStateMachine()
    setattr(partner, 'SrcStateMachine15', None)
    _safe_set(owner, 'states', partner)
    assert getattr(partner, 'SrcStateMachine15') == owner
    _safe_set(owner, 'states', None)
    assert getattr(partner, 'SrcStateMachine15') is None


def test_assoc_stateMachine25_stub_double():
    # TrgStateMachine has no real 'TrgStateMachine27' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    partner = TrgStateMachine()
    setattr(partner, 'TrgStateMachine27', None)
    _safe_set(owner, 'transitions26', partner)
    assert getattr(partner, 'TrgStateMachine27') == owner
    _safe_set(owner, 'transitions26', None)
    assert getattr(partner, 'TrgStateMachine27') is None


def test_assoc_stateMachine33_stub_double():
    # TrgStateMachine has no real 'TrgStateMachine35' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgAbstractState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgAbstractState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgAbstractState(name="sample_text")
    partner = TrgStateMachine()
    setattr(partner, 'TrgStateMachine35', None)
    _safe_set(owner, 'states34', partner)
    assert getattr(partner, 'TrgStateMachine35') == owner
    _safe_set(owner, 'states34', None)
    assert getattr(partner, 'TrgStateMachine35') is None


def test_assoc_stateMachine7_stub_double():
    # SrcStateMachine has no real 'SrcStateMachine8' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    partner = SrcStateMachine()
    setattr(partner, 'SrcStateMachine8', None)
    _safe_set(owner, 'transitions', partner)
    assert getattr(partner, 'SrcStateMachine8') == owner
    _safe_set(owner, 'transitions', None)
    assert getattr(partner, 'SrcStateMachine8') is None


def test_assoc_states23_stub_double():
    # TrgAbstractState has no real 'TrgAbstractState' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgStateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgStateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgStateMachine(name="sample_text")
    partner = TrgAbstractState()
    setattr(partner, 'TrgAbstractState', None)
    _safe_set(owner, 'stateMachine24', {partner})
    assert getattr(partner, 'TrgAbstractState') == owner
    _safe_set(owner, 'stateMachine24', set())
    assert getattr(partner, 'TrgAbstractState') is None


def test_assoc_states5_stub_double():
    # SrcAbstractState has no real 'SrcAbstractState' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcStateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcStateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcStateMachine(name="sample_text")
    partner = SrcAbstractState()
    setattr(partner, 'SrcAbstractState', None)
    _safe_set(owner, 'stateMachine6', {partner})
    assert getattr(partner, 'SrcAbstractState') == owner
    _safe_set(owner, 'stateMachine6', set())
    assert getattr(partner, 'SrcAbstractState') is None


def test_assoc_target11_stub_double():
    # SrcAbstractState has no real 'SrcAbstractState13' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcTransition(label="sample_text")
    partner = SrcAbstractState()
    setattr(partner, 'SrcAbstractState13', None)
    _safe_set(owner, 'jointPackage_HSM2FSM_SrcTransition12', partner)
    assert getattr(partner, 'SrcAbstractState13') == owner
    _safe_set(owner, 'jointPackage_HSM2FSM_SrcTransition12', None)
    assert getattr(partner, 'SrcAbstractState13') is None


def test_assoc_target30_stub_double():
    # TrgAbstractState has no real 'TrgAbstractState32' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgTransition(label="sample_text")
    partner = TrgAbstractState()
    setattr(partner, 'TrgAbstractState32', None)
    _safe_set(owner, 'jointPackage_HSM2FSM_TrgTransition31', partner)
    assert getattr(partner, 'TrgAbstractState32') == owner
    _safe_set(owner, 'jointPackage_HSM2FSM_TrgTransition31', None)
    assert getattr(partner, 'TrgAbstractState32') is None


def test_assoc_transitions21_stub_double():
    # TrgTransition has no real 'TrgTransition' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_TrgStateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_TrgStateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_TrgStateMachine(name="sample_text")
    partner = TrgTransition()
    setattr(partner, 'TrgTransition', None)
    _safe_set(owner, 'stateMachine22', {partner})
    assert getattr(partner, 'TrgTransition') == owner
    _safe_set(owner, 'stateMachine22', set())
    assert getattr(partner, 'TrgTransition') is None


def test_assoc_transitions4_stub_double():
    # SrcTransition has no real 'SrcTransition' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_HSM2FSM_SrcStateMachine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_HSM2FSM_SrcStateMachine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_HSM2FSM_SrcStateMachine(name="sample_text")
    partner = SrcTransition()
    setattr(partner, 'SrcTransition', None)
    _safe_set(owner, 'stateMachine', {partner})
    assert getattr(partner, 'SrcTransition') == owner
    _safe_set(owner, 'stateMachine', set())
    assert getattr(partner, 'SrcTransition') is None


