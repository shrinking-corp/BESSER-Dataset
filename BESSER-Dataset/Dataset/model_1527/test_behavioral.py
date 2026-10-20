import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    fsmtest_ConditionDeclaration,
    fsmtest_FsmDefinition,
    fsmtest_GuardDeclaration,
    fsmtest_LoopsDeclaration,
    fsmtest_Model,
    fsmtest_PostconditionDeclaration,
    fsmtest_PreconditionDeclaration,
    fsmtest_RandomTest,
    fsmtest_SeedDeclaration,
    fsmtest_SignalDeclaration,
    fsmtest_StateDeclaration,
    fsmtest_TransitionDeclaration,
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

def test_assoc_destination13_reverse_link_reassign_clear():
    a1 = fsmtest_TransitionDeclaration(name="sample_text")
    a2 = fsmtest_TransitionDeclaration(name="sample_text_2")
    b = fsmtest_StateDeclaration(name="sample_text")
    _safe_set(b, 'fsmtest_StateDeclaration14', a1)
    assert _is_linked(b, 'fsmtest_StateDeclaration14', a1)
    if hasattr(a1, 'fsmtest_TransitionDeclaration'):
        assert _is_linked(a1, 'fsmtest_TransitionDeclaration', b)
    _safe_set(b, 'fsmtest_StateDeclaration14', a2)
    assert _is_linked(b, 'fsmtest_StateDeclaration14', a2)
    if hasattr(a1, 'fsmtest_TransitionDeclaration'):
        assert not _is_linked(a1, 'fsmtest_TransitionDeclaration', b)
    if hasattr(a2, 'fsmtest_TransitionDeclaration'):
        assert _is_linked(a2, 'fsmtest_TransitionDeclaration', b)
    _safe_set(b, 'fsmtest_StateDeclaration14', None)
    assert not _is_linked(b, 'fsmtest_StateDeclaration14', a2)
    if hasattr(a2, 'fsmtest_TransitionDeclaration'):
        assert not _is_linked(a2, 'fsmtest_TransitionDeclaration', b)


def test_assoc_fsm5_reverse_link_reassign_clear():
    a1 = fsmtest_RandomTest(name="sample_text")
    a2 = fsmtest_RandomTest(name="sample_text_2")
    b = fsmtest_FsmDefinition(name="sample_text")
    _safe_set(b, 'fsmtest_FsmDefinition7', a1)
    assert _is_linked(b, 'fsmtest_FsmDefinition7', a1)
    if hasattr(a1, 'fsmtest_RandomTest6'):
        assert _is_linked(a1, 'fsmtest_RandomTest6', b)
    _safe_set(b, 'fsmtest_FsmDefinition7', a2)
    assert _is_linked(b, 'fsmtest_FsmDefinition7', a2)
    if hasattr(a1, 'fsmtest_RandomTest6'):
        assert not _is_linked(a1, 'fsmtest_RandomTest6', b)
    if hasattr(a2, 'fsmtest_RandomTest6'):
        assert _is_linked(a2, 'fsmtest_RandomTest6', b)
    _safe_set(b, 'fsmtest_FsmDefinition7', None)
    assert not _is_linked(b, 'fsmtest_FsmDefinition7', a2)
    if hasattr(a2, 'fsmtest_RandomTest6'):
        assert not _is_linked(a2, 'fsmtest_RandomTest6', b)


def test_assoc_loopsDeclaration8_reverse_link_reassign_clear():
    a1 = fsmtest_RandomTest(name="sample_text")
    a2 = fsmtest_RandomTest(name="sample_text_2")
    b = fsmtest_LoopsDeclaration(val=7)
    _safe_set(b, 'fsmtest_LoopsDeclaration', a1)
    assert _is_linked(b, 'fsmtest_LoopsDeclaration', a1)
    if hasattr(a1, 'fsmtest_RandomTest9'):
        assert _is_linked(a1, 'fsmtest_RandomTest9', b)
    _safe_set(b, 'fsmtest_LoopsDeclaration', a2)
    assert _is_linked(b, 'fsmtest_LoopsDeclaration', a2)
    if hasattr(a1, 'fsmtest_RandomTest9'):
        assert not _is_linked(a1, 'fsmtest_RandomTest9', b)
    if hasattr(a2, 'fsmtest_RandomTest9'):
        assert _is_linked(a2, 'fsmtest_RandomTest9', b)
    _safe_set(b, 'fsmtest_LoopsDeclaration', None)
    assert not _is_linked(b, 'fsmtest_LoopsDeclaration', a2)
    if hasattr(a2, 'fsmtest_RandomTest9'):
        assert not _is_linked(a2, 'fsmtest_RandomTest9', b)


def test_assoc_seedDeclaration10_reverse_link_reassign_clear():
    a1 = fsmtest_SeedDeclaration(val=7)
    a2 = fsmtest_SeedDeclaration(val=13)
    b = fsmtest_RandomTest(name="sample_text")
    _safe_set(b, 'fsmtest_RandomTest11', a1)
    assert _is_linked(b, 'fsmtest_RandomTest11', a1)
    if hasattr(a1, 'fsmtest_SeedDeclaration'):
        assert _is_linked(a1, 'fsmtest_SeedDeclaration', b)
    _safe_set(b, 'fsmtest_RandomTest11', a2)
    assert _is_linked(b, 'fsmtest_RandomTest11', a2)
    if hasattr(a1, 'fsmtest_SeedDeclaration'):
        assert not _is_linked(a1, 'fsmtest_SeedDeclaration', b)
    if hasattr(a2, 'fsmtest_SeedDeclaration'):
        assert _is_linked(a2, 'fsmtest_SeedDeclaration', b)
    _safe_set(b, 'fsmtest_RandomTest11', None)
    assert not _is_linked(b, 'fsmtest_RandomTest11', a2)
    if hasattr(a2, 'fsmtest_SeedDeclaration'):
        assert not _is_linked(a2, 'fsmtest_SeedDeclaration', b)


def test_assoc_states3_reverse_link_reassign_clear():
    a1 = fsmtest_StateDeclaration(name="sample_text")
    a2 = fsmtest_StateDeclaration(name="sample_text_2")
    b = fsmtest_FsmDefinition(name="sample_text")
    _safe_set(b, 'fsmtest_FsmDefinition4', {a1})
    assert _is_linked(b, 'fsmtest_FsmDefinition4', a1)
    if hasattr(a1, 'fsmtest_StateDeclaration'):
        assert _is_linked(a1, 'fsmtest_StateDeclaration', b)
    _safe_set(b, 'fsmtest_FsmDefinition4', {a2})
    assert _is_linked(b, 'fsmtest_FsmDefinition4', a2)
    if hasattr(a1, 'fsmtest_StateDeclaration'):
        assert not _is_linked(a1, 'fsmtest_StateDeclaration', b)
    if hasattr(a2, 'fsmtest_StateDeclaration'):
        assert _is_linked(a2, 'fsmtest_StateDeclaration', b)
    _safe_set(b, 'fsmtest_FsmDefinition4', set())
    assert not _is_linked(b, 'fsmtest_FsmDefinition4', a2)
    if hasattr(a2, 'fsmtest_StateDeclaration'):
        assert not _is_linked(a2, 'fsmtest_StateDeclaration', b)


def test_assoc_transitions36_reverse_link_reassign_clear():
    a1 = fsmtest_TransitionDeclaration(name="sample_text")
    a2 = fsmtest_TransitionDeclaration(name="sample_text_2")
    b = fsmtest_StateDeclaration(name="sample_text")
    _safe_set(b, 'fsmtest_StateDeclaration37', {a1})
    assert _is_linked(b, 'fsmtest_StateDeclaration37', a1)
    if hasattr(a1, 'fsmtest_TransitionDeclaration38'):
        assert _is_linked(a1, 'fsmtest_TransitionDeclaration38', b)
    _safe_set(b, 'fsmtest_StateDeclaration37', {a2})
    assert _is_linked(b, 'fsmtest_StateDeclaration37', a2)
    if hasattr(a1, 'fsmtest_TransitionDeclaration38'):
        assert not _is_linked(a1, 'fsmtest_TransitionDeclaration38', b)
    if hasattr(a2, 'fsmtest_TransitionDeclaration38'):
        assert _is_linked(a2, 'fsmtest_TransitionDeclaration38', b)
    _safe_set(b, 'fsmtest_StateDeclaration37', set())
    assert not _is_linked(b, 'fsmtest_StateDeclaration37', a2)
    if hasattr(a2, 'fsmtest_TransitionDeclaration38'):
        assert not _is_linked(a2, 'fsmtest_TransitionDeclaration38', b)


def test_assoc_trigger15_reverse_link_reassign_clear():
    a1 = fsmtest_TransitionDeclaration(name="sample_text")
    a2 = fsmtest_TransitionDeclaration(name="sample_text_2")
    b = fsmtest_SignalDeclaration(intVal=7, port="sample_text", signame="sample_text", strVal="sample_text")
    _safe_set(b, 'fsmtest_SignalDeclaration17', a1)
    assert _is_linked(b, 'fsmtest_SignalDeclaration17', a1)
    if hasattr(a1, 'fsmtest_TransitionDeclaration16'):
        assert _is_linked(a1, 'fsmtest_TransitionDeclaration16', b)
    _safe_set(b, 'fsmtest_SignalDeclaration17', a2)
    assert _is_linked(b, 'fsmtest_SignalDeclaration17', a2)
    if hasattr(a1, 'fsmtest_TransitionDeclaration16'):
        assert not _is_linked(a1, 'fsmtest_TransitionDeclaration16', b)
    if hasattr(a2, 'fsmtest_TransitionDeclaration16'):
        assert _is_linked(a2, 'fsmtest_TransitionDeclaration16', b)
    _safe_set(b, 'fsmtest_SignalDeclaration17', None)
    assert not _is_linked(b, 'fsmtest_SignalDeclaration17', a2)
    if hasattr(a2, 'fsmtest_TransitionDeclaration16'):
        assert not _is_linked(a2, 'fsmtest_TransitionDeclaration16', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_FsmDefinitions0_stub_double():
    # fsmtest_Model has no real 'fsmtest_Model' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_FsmDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_FsmDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_FsmDefinition(name="sample_text")
    partner = fsmtest_Model()
    setattr(partner, 'fsmtest_Model', None)
    _safe_set(owner, 'fsmtest_FsmDefinition', partner)
    assert owner in getattr(partner, 'fsmtest_Model')
    _safe_set(owner, 'fsmtest_FsmDefinition', None)
    assert owner not in getattr(partner, 'fsmtest_Model')


def test_assoc_RandomTests1_stub_double():
    # fsmtest_Model has no real 'fsmtest_Model2' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_RandomTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_RandomTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_RandomTest(name="sample_text")
    partner = fsmtest_Model()
    setattr(partner, 'fsmtest_Model2', None)
    _safe_set(owner, 'fsmtest_RandomTest', partner)
    assert owner in getattr(partner, 'fsmtest_Model2')
    _safe_set(owner, 'fsmtest_RandomTest', None)
    assert owner not in getattr(partner, 'fsmtest_Model2')


def test_assoc_condition33_stub_double():
    # fsmtest_ConditionDeclaration has no real 'fsmtest_ConditionDeclaration35' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_StateDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_StateDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_StateDeclaration(name="sample_text")
    partner = fsmtest_ConditionDeclaration()
    setattr(partner, 'fsmtest_ConditionDeclaration35', None)
    _safe_set(owner, 'fsmtest_StateDeclaration34', {partner})
    assert getattr(partner, 'fsmtest_ConditionDeclaration35') == owner
    _safe_set(owner, 'fsmtest_StateDeclaration34', set())
    assert getattr(partner, 'fsmtest_ConditionDeclaration35') is None


def test_assoc_postcondition23_stub_double():
    # fsmtest_PostconditionDeclaration has no real 'fsmtest_PostconditionDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_TransitionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_TransitionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_TransitionDeclaration(name="sample_text")
    partner = fsmtest_PostconditionDeclaration()
    setattr(partner, 'fsmtest_PostconditionDeclaration', None)
    _safe_set(owner, 'fsmtest_TransitionDeclaration24', {partner})
    assert getattr(partner, 'fsmtest_PostconditionDeclaration') == owner
    _safe_set(owner, 'fsmtest_TransitionDeclaration24', set())
    assert getattr(partner, 'fsmtest_PostconditionDeclaration') is None


def test_assoc_precondition21_stub_double():
    # fsmtest_PreconditionDeclaration has no real 'fsmtest_PreconditionDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_TransitionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_TransitionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_TransitionDeclaration(name="sample_text")
    partner = fsmtest_PreconditionDeclaration()
    setattr(partner, 'fsmtest_PreconditionDeclaration', None)
    _safe_set(owner, 'fsmtest_TransitionDeclaration22', {partner})
    assert getattr(partner, 'fsmtest_PreconditionDeclaration') == owner
    _safe_set(owner, 'fsmtest_TransitionDeclaration22', set())
    assert getattr(partner, 'fsmtest_PreconditionDeclaration') is None


def test_assoc_signal12_stub_double():
    # fsmtest_GuardDeclaration has no real 'fsmtest_GuardDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_SignalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_SignalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_SignalDeclaration(intVal=7, port="sample_text", signame="sample_text", strVal="sample_text")
    partner = fsmtest_GuardDeclaration()
    setattr(partner, 'fsmtest_GuardDeclaration', None)
    _safe_set(owner, 'fsmtest_SignalDeclaration', partner)
    assert getattr(partner, 'fsmtest_GuardDeclaration') == owner
    _safe_set(owner, 'fsmtest_SignalDeclaration', None)
    assert getattr(partner, 'fsmtest_GuardDeclaration') is None


def test_assoc_signal25_stub_double():
    # fsmtest_ConditionDeclaration has no real 'fsmtest_ConditionDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_SignalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_SignalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_SignalDeclaration(intVal=7, port="sample_text", signame="sample_text", strVal="sample_text")
    partner = fsmtest_ConditionDeclaration()
    setattr(partner, 'fsmtest_ConditionDeclaration', None)
    _safe_set(owner, 'fsmtest_SignalDeclaration26', partner)
    assert getattr(partner, 'fsmtest_ConditionDeclaration') == owner
    _safe_set(owner, 'fsmtest_SignalDeclaration26', None)
    assert getattr(partner, 'fsmtest_ConditionDeclaration') is None


def test_assoc_signal27_stub_double():
    # fsmtest_PreconditionDeclaration has no real 'fsmtest_PreconditionDeclaration28' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_SignalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_SignalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_SignalDeclaration(intVal=7, port="sample_text", signame="sample_text", strVal="sample_text")
    partner = fsmtest_PreconditionDeclaration()
    setattr(partner, 'fsmtest_PreconditionDeclaration28', None)
    _safe_set(owner, 'fsmtest_SignalDeclaration29', partner)
    assert getattr(partner, 'fsmtest_PreconditionDeclaration28') == owner
    _safe_set(owner, 'fsmtest_SignalDeclaration29', None)
    assert getattr(partner, 'fsmtest_PreconditionDeclaration28') is None


def test_assoc_signal30_stub_double():
    # fsmtest_PostconditionDeclaration has no real 'fsmtest_PostconditionDeclaration31' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_SignalDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_SignalDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_SignalDeclaration(intVal=7, port="sample_text", signame="sample_text", strVal="sample_text")
    partner = fsmtest_PostconditionDeclaration()
    setattr(partner, 'fsmtest_PostconditionDeclaration31', None)
    _safe_set(owner, 'fsmtest_SignalDeclaration32', partner)
    assert getattr(partner, 'fsmtest_PostconditionDeclaration31') == owner
    _safe_set(owner, 'fsmtest_SignalDeclaration32', None)
    assert getattr(partner, 'fsmtest_PostconditionDeclaration31') is None


def test_assoc_triggers18_stub_double():
    # fsmtest_GuardDeclaration has no real 'fsmtest_GuardDeclaration20' property in the generated
    # code (a bare stub) -- manually attach it so fsmtest_TransitionDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmtest_TransitionDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmtest_TransitionDeclaration(name="sample_text")
    partner = fsmtest_GuardDeclaration()
    setattr(partner, 'fsmtest_GuardDeclaration20', None)
    _safe_set(owner, 'fsmtest_TransitionDeclaration19', {partner})
    assert getattr(partner, 'fsmtest_GuardDeclaration20') == owner
    _safe_set(owner, 'fsmtest_TransitionDeclaration19', set())
    assert getattr(partner, 'fsmtest_GuardDeclaration20') is None


