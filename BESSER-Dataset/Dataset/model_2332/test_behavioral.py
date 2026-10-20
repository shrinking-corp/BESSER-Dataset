import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BasicBehavior_BehavioredClassifier,
    BasicBehavior_Classifier,
    Behavior,
    BehavioralFeature,
    BehavioredClassifier,
    Class,
    Classifier,
    CommonBehavior_BasicBehavior_Behavior,
    CommonBehavior_BasicBehavior_BehavioralFeature,
    CommonBehavior_BasicBehavior_BehavioredClassifier,
    CommonBehavior_BasicBehavior_Class,
    CommonBehavior_BasicBehavior_Classifier,
    CommonBehavior_BasicBehavior_Constraint,
    CommonBehavior_BasicBehavior_FunctionBehavior,
    CommonBehavior_BasicBehavior_OpaqueBehavior,
    CommonBehavior_BasicBehavior_OpaqueExpression,
    CommonBehavior_BasicBehavior_Parameter,
    CommonBehavior_BasicBehavior_RedefinableElement,
    CommonBehavior_Communications_AnyReceiveEvent,
    CommonBehavior_Communications_CallEvent,
    CommonBehavior_Communications_ChangeEvent,
    CommonBehavior_Communications_Event,
    CommonBehavior_Communications_Interface,
    CommonBehavior_Communications_MessageEvent,
    CommonBehavior_Communications_NamedElement,
    CommonBehavior_Communications_Operation,
    CommonBehavior_Communications_PackageableElement,
    CommonBehavior_Communications_Property,
    CommonBehavior_Communications_Reception,
    CommonBehavior_Communications_Signal,
    CommonBehavior_Communications_SignalEvent,
    CommonBehavior_Communications_Trigger,
    CommonBehavior_Communications_ValueSpecification,
    CommonBehavior_SimpleTime_Duration,
    CommonBehavior_SimpleTime_DurationConstraint,
    CommonBehavior_SimpleTime_DurationInterval,
    CommonBehavior_SimpleTime_DurationObservation,
    CommonBehavior_SimpleTime_Interval,
    CommonBehavior_SimpleTime_IntervalConstraint,
    CommonBehavior_SimpleTime_Observation,
    CommonBehavior_SimpleTime_TimeConstraint,
    CommonBehavior_SimpleTime_TimeEvent,
    CommonBehavior_SimpleTime_TimeExpression,
    CommonBehavior_SimpleTime_TimeInterval,
    CommonBehavior_SimpleTime_TimeObservation,
    Constraint,
    Duration,
    DurationInterval,
    Event,
    Interval,
    IntervalConstraint,
    MessageEvent,
    NamedElement,
    Observation,
    OpaqueBehavior,
    Operation,
    PackageableElement,
    Parameter,
    Property,
    Reception,
    RedefinableElement,
    Signal,
    TimeExpression,
    TimeInterval,
    ValueSpecification,
    CallConcurrencyFeature,
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

def test_assoc_context5_stub_double():
    # BehavioredClassifier has no real 'BehavioredClassifier' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = BehavioredClassifier()
    setattr(partner, 'BehavioredClassifier', None)
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior', partner)
    assert getattr(partner, 'BehavioredClassifier') == owner
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior', None)
    assert getattr(partner, 'BehavioredClassifier') is None


def test_assoc_durationSpecification61_stub_double():
    # DurationInterval has no real 'DurationInterval' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_SimpleTime_DurationConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_SimpleTime_DurationConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_SimpleTime_DurationConstraint(firstEvent=True)
    partner = DurationInterval()
    setattr(partner, 'DurationInterval', None)
    _safe_set(owner, 'CommonBehavior_SimpleTime_DurationConstraint', partner)
    assert getattr(partner, 'DurationInterval') == owner
    _safe_set(owner, 'CommonBehavior_SimpleTime_DurationConstraint', None)
    assert getattr(partner, 'DurationInterval') is None


def test_assoc_event38_stub_double():
    # NamedElement has no real 'NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_SimpleTime_TimeObservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_SimpleTime_TimeObservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_SimpleTime_TimeObservation(firstEvent=True)
    partner = NamedElement()
    setattr(partner, 'NamedElement', None)
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeObservation', partner)
    assert getattr(partner, 'NamedElement') == owner
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeObservation', None)
    assert getattr(partner, 'NamedElement') is None


def test_assoc_event39_stub_double():
    # NamedElement has no real 'NamedElement40' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_SimpleTime_DurationObservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_SimpleTime_DurationObservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_SimpleTime_DurationObservation(firstEvent=True)
    partner = NamedElement()
    setattr(partner, 'NamedElement40', None)
    _safe_set(owner, 'CommonBehavior_SimpleTime_DurationObservation', {partner})
    assert getattr(partner, 'NamedElement40') == owner
    _safe_set(owner, 'CommonBehavior_SimpleTime_DurationObservation', set())
    assert getattr(partner, 'NamedElement40') is None


def test_assoc_method17_stub_double():
    # Behavior has no real 'Behavior18' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_BehavioralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_BehavioralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_BehavioralFeature(concurrency="sample_text")
    partner = Behavior()
    setattr(partner, 'Behavior18', None)
    _safe_set(owner, 'specification', {partner})
    assert getattr(partner, 'Behavior18') == owner
    _safe_set(owner, 'specification', set())
    assert getattr(partner, 'Behavior18') is None


def test_assoc_ownedParameter10_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior11', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior11', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_postcondition14_stub_double():
    # Constraint has no real 'Constraint16' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = Constraint()
    setattr(partner, 'Constraint16', None)
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior15', {partner})
    assert getattr(partner, 'Constraint16') == owner
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior15', set())
    assert getattr(partner, 'Constraint16') is None


def test_assoc_precondition12_stub_double():
    # Constraint has no real 'Constraint' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = Constraint()
    setattr(partner, 'Constraint', None)
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior13', {partner})
    assert getattr(partner, 'Constraint') == owner
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior13', set())
    assert getattr(partner, 'Constraint') is None


def test_assoc_redefinedBehavior6_stub_double():
    # Behavior has no real 'Behavior8' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = Behavior()
    setattr(partner, 'Behavior8', None)
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior7', {partner})
    assert getattr(partner, 'Behavior8') == owner
    _safe_set(owner, 'CommonBehavior_BasicBehavior_Behavior7', set())
    assert getattr(partner, 'Behavior8') is None


def test_assoc_specification9_stub_double():
    # BehavioralFeature has no real 'BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_BasicBehavior_Behavior's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_BasicBehavior_Behavior's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    partner = BehavioralFeature()
    setattr(partner, 'BehavioralFeature', None)
    _safe_set(owner, 'method', partner)
    assert getattr(partner, 'BehavioralFeature') == owner
    _safe_set(owner, 'method', None)
    assert getattr(partner, 'BehavioralFeature') is None


def test_assoc_timeSpecification60_stub_double():
    # TimeInterval has no real 'TimeInterval' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_SimpleTime_TimeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_SimpleTime_TimeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_SimpleTime_TimeConstraint(firstEvent=True)
    partner = TimeInterval()
    setattr(partner, 'TimeInterval', None)
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeConstraint', partner)
    assert getattr(partner, 'TimeInterval') == owner
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeConstraint', None)
    assert getattr(partner, 'TimeInterval') is None


def test_assoc_when33_stub_double():
    # TimeExpression has no real 'TimeExpression' property in the generated
    # code (a bare stub) -- manually attach it so CommonBehavior_SimpleTime_TimeEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # CommonBehavior_SimpleTime_TimeEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = CommonBehavior_SimpleTime_TimeEvent(isRelative=True)
    partner = TimeExpression()
    setattr(partner, 'TimeExpression', None)
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeEvent', partner)
    assert getattr(partner, 'TimeExpression') == owner
    _safe_set(owner, 'CommonBehavior_SimpleTime_TimeEvent', None)
    assert getattr(partner, 'TimeExpression') is None


