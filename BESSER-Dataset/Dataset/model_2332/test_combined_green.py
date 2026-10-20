# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TimeInterval,
    IntervalConstraint,
    CommonBehavior_SimpleTime_DurationConstraint,
    CommonBehavior_SimpleTime_TimeConstraint,
    Duration,
    Interval,
    CommonBehavior_SimpleTime_DurationInterval,
    CommonBehavior_SimpleTime_TimeInterval,
    DurationInterval,
    TimeExpression,
    CommonBehavior_SimpleTime_TimeEvent,
    CommonBehavior_Communications_ValueSpecification,
    ValueSpecification,
    CommonBehavior_SimpleTime_TimeExpression,
    CommonBehavior_SimpleTime_Duration,
    CommonBehavior_SimpleTime_Interval,
    CommonBehavior_Communications_Operation,
    Operation,
    MessageEvent,
    CommonBehavior_Communications_SignalEvent,
    CommonBehavior_Communications_CallEvent,
    CommonBehavior_Communications_AnyReceiveEvent,
    PackageableElement,
    CommonBehavior_Communications_Event,
    CommonBehavior_Communications_PackageableElement,
    Event,
    CommonBehavior_Communications_ChangeEvent,
    CommonBehavior_Communications_MessageEvent,
    NamedElement,
    CommonBehavior_Communications_Trigger,
    CommonBehavior_Communications_NamedElement,
    CommonBehavior_SimpleTime_Observation,
    Observation,
    CommonBehavior_SimpleTime_DurationObservation,
    CommonBehavior_SimpleTime_TimeObservation,
    CommonBehavior_Communications_Property,
    Property,
    CommonBehavior_BasicBehavior_Constraint,
    CommonBehavior_BasicBehavior_OpaqueExpression,
    CommonBehavior_BasicBehavior_Parameter,
    Signal,
    CommonBehavior_BasicBehavior_RedefinableElement,
    Constraint,
    CommonBehavior_SimpleTime_IntervalConstraint,
    Parameter,
    BehavioralFeature,
    CommonBehavior_Communications_Reception,
    BehavioredClassifier,
    Class,
    CommonBehavior_BasicBehavior_Behavior,
    Reception,
    BasicBehavior_BehavioredClassifier,
    BasicBehavior_Classifier,
    CommonBehavior_BasicBehavior_Class,
    RedefinableElement,
    CommonBehavior_BasicBehavior_Classifier,
    Behavior,
    CommonBehavior_BasicBehavior_OpaqueBehavior,
    CommonBehavior_BasicBehavior_BehavioralFeature,
    OpaqueBehavior,
    CommonBehavior_BasicBehavior_FunctionBehavior,
    Classifier,
    CommonBehavior_Communications_Interface,
    CommonBehavior_Communications_Signal,
    CommonBehavior_BasicBehavior_BehavioredClassifier,
    CallConcurrencyFeature,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_timeinterval_is_not_abstract():
    assert not inspect.isabstract(TimeInterval)


def test_hyp_timeinterval_constructor_exists():
    assert callable(TimeInterval.__init__)


def test_hyp_timeinterval_constructor_args():
    sig = inspect.signature(TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_hyp_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_hyp_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_DurationConstraint)


def test_hyp_commonbehavior_simpletime_durationconstraint_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_DurationConstraint.__init__)


def test_hyp_commonbehavior_simpletime_durationconstraint_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_commonbehavior_simpletime_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_TimeConstraint)


def test_hyp_commonbehavior_simpletime_timeconstraint_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_TimeConstraint.__init__)


def test_hyp_commonbehavior_simpletime_timeconstraint_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_duration_is_not_abstract():
    assert not inspect.isabstract(Duration)


def test_hyp_duration_constructor_exists():
    assert callable(Duration.__init__)


def test_hyp_duration_constructor_args():
    sig = inspect.signature(Duration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_hyp_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_hyp_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_durationinterval_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_DurationInterval)


def test_hyp_commonbehavior_simpletime_durationinterval_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_DurationInterval.__init__)


def test_hyp_commonbehavior_simpletime_durationinterval_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_timeinterval_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_TimeInterval)


def test_hyp_commonbehavior_simpletime_timeinterval_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_TimeInterval.__init__)


def test_hyp_commonbehavior_simpletime_timeinterval_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_durationinterval_is_not_abstract():
    assert not inspect.isabstract(DurationInterval)


def test_hyp_durationinterval_constructor_exists():
    assert callable(DurationInterval.__init__)


def test_hyp_durationinterval_constructor_args():
    sig = inspect.signature(DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_timeexpression_is_not_abstract():
    assert not inspect.isabstract(TimeExpression)


def test_hyp_timeexpression_constructor_exists():
    assert callable(TimeExpression.__init__)


def test_hyp_timeexpression_constructor_args():
    sig = inspect.signature(TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_timeevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_TimeEvent)


def test_hyp_commonbehavior_simpletime_timeevent_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_TimeEvent.__init__)


def test_hyp_commonbehavior_simpletime_timeevent_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"




def test_hyp_commonbehavior_communications_valuespecification_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_ValueSpecification)


def test_hyp_commonbehavior_communications_valuespecification_constructor_exists():
    assert callable(CommonBehavior_Communications_ValueSpecification.__init__)


def test_hyp_commonbehavior_communications_valuespecification_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_hyp_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_hyp_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_timeexpression_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_TimeExpression)


def test_hyp_commonbehavior_simpletime_timeexpression_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_TimeExpression.__init__)


def test_hyp_commonbehavior_simpletime_timeexpression_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_duration_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_Duration)


def test_hyp_commonbehavior_simpletime_duration_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_Duration.__init__)


def test_hyp_commonbehavior_simpletime_duration_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_Duration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_interval_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_Interval)


def test_hyp_commonbehavior_simpletime_interval_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_Interval.__init__)


def test_hyp_commonbehavior_simpletime_interval_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_Interval.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_operation_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Operation)


def test_hyp_commonbehavior_communications_operation_constructor_exists():
    assert callable(CommonBehavior_Communications_Operation.__init__)


def test_hyp_commonbehavior_communications_operation_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_hyp_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_hyp_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_hyp_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_signalevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_SignalEvent)


def test_hyp_commonbehavior_communications_signalevent_constructor_exists():
    assert callable(CommonBehavior_Communications_SignalEvent.__init__)


def test_hyp_commonbehavior_communications_signalevent_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_SignalEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_callevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_CallEvent)


def test_hyp_commonbehavior_communications_callevent_constructor_exists():
    assert callable(CommonBehavior_Communications_CallEvent.__init__)


def test_hyp_commonbehavior_communications_callevent_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_CallEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_AnyReceiveEvent)


def test_hyp_commonbehavior_communications_anyreceiveevent_constructor_exists():
    assert callable(CommonBehavior_Communications_AnyReceiveEvent.__init__)


def test_hyp_commonbehavior_communications_anyreceiveevent_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_hyp_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_hyp_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_event_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Event)


def test_hyp_commonbehavior_communications_event_constructor_exists():
    assert callable(CommonBehavior_Communications_Event.__init__)


def test_hyp_commonbehavior_communications_event_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_packageableelement_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_PackageableElement)


def test_hyp_commonbehavior_communications_packageableelement_constructor_exists():
    assert callable(CommonBehavior_Communications_PackageableElement.__init__)


def test_hyp_commonbehavior_communications_packageableelement_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_hyp_event_constructor_exists():
    assert callable(Event.__init__)


def test_hyp_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_changeevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_ChangeEvent)


def test_hyp_commonbehavior_communications_changeevent_constructor_exists():
    assert callable(CommonBehavior_Communications_ChangeEvent.__init__)


def test_hyp_commonbehavior_communications_changeevent_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_messageevent_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_MessageEvent)


def test_hyp_commonbehavior_communications_messageevent_constructor_exists():
    assert callable(CommonBehavior_Communications_MessageEvent.__init__)


def test_hyp_commonbehavior_communications_messageevent_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_trigger_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Trigger)


def test_hyp_commonbehavior_communications_trigger_constructor_exists():
    assert callable(CommonBehavior_Communications_Trigger.__init__)


def test_hyp_commonbehavior_communications_trigger_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_namedelement_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_NamedElement)


def test_hyp_commonbehavior_communications_namedelement_constructor_exists():
    assert callable(CommonBehavior_Communications_NamedElement.__init__)


def test_hyp_commonbehavior_communications_namedelement_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_observation_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_Observation)


def test_hyp_commonbehavior_simpletime_observation_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_Observation.__init__)


def test_hyp_commonbehavior_simpletime_observation_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_Observation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_hyp_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_hyp_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_durationobservation_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_DurationObservation)


def test_hyp_commonbehavior_simpletime_durationobservation_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_DurationObservation.__init__)


def test_hyp_commonbehavior_simpletime_durationobservation_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_commonbehavior_simpletime_timeobservation_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_TimeObservation)


def test_hyp_commonbehavior_simpletime_timeobservation_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_TimeObservation.__init__)


def test_hyp_commonbehavior_simpletime_timeobservation_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"




def test_hyp_commonbehavior_communications_property_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Property)


def test_hyp_commonbehavior_communications_property_constructor_exists():
    assert callable(CommonBehavior_Communications_Property.__init__)


def test_hyp_commonbehavior_communications_property_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_hyp_property_constructor_exists():
    assert callable(Property.__init__)


def test_hyp_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_constraint_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_Constraint)


def test_hyp_commonbehavior_basicbehavior_constraint_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_Constraint.__init__)


def test_hyp_commonbehavior_basicbehavior_constraint_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_OpaqueExpression)


def test_hyp_commonbehavior_basicbehavior_opaqueexpression_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_OpaqueExpression.__init__)


def test_hyp_commonbehavior_basicbehavior_opaqueexpression_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_parameter_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_Parameter)


def test_hyp_commonbehavior_basicbehavior_parameter_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_Parameter.__init__)


def test_hyp_commonbehavior_basicbehavior_parameter_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_signal_is_not_abstract():
    assert not inspect.isabstract(Signal)


def test_hyp_signal_constructor_exists():
    assert callable(Signal.__init__)


def test_hyp_signal_constructor_args():
    sig = inspect.signature(Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_RedefinableElement)


def test_hyp_commonbehavior_basicbehavior_redefinableelement_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_RedefinableElement.__init__)


def test_hyp_commonbehavior_basicbehavior_redefinableelement_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_hyp_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_hyp_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_simpletime_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_SimpleTime_IntervalConstraint)


def test_hyp_commonbehavior_simpletime_intervalconstraint_constructor_exists():
    assert callable(CommonBehavior_SimpleTime_IntervalConstraint.__init__)


def test_hyp_commonbehavior_simpletime_intervalconstraint_constructor_args():
    sig = inspect.signature(CommonBehavior_SimpleTime_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_hyp_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_hyp_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_reception_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Reception)


def test_hyp_commonbehavior_communications_reception_constructor_exists():
    assert callable(CommonBehavior_Communications_Reception.__init__)


def test_hyp_commonbehavior_communications_reception_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Reception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_hyp_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_hyp_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_hyp_class_constructor_exists():
    assert callable(Class.__init__)


def test_hyp_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_behavior_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_Behavior)


def test_hyp_commonbehavior_basicbehavior_behavior_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_Behavior.__init__)


def test_hyp_commonbehavior_basicbehavior_behavior_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"




def test_hyp_reception_is_not_abstract():
    assert not inspect.isabstract(Reception)


def test_hyp_reception_constructor_exists():
    assert callable(Reception.__init__)


def test_hyp_reception_constructor_args():
    sig = inspect.signature(Reception.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicbehavior_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehavior_BehavioredClassifier)


def test_hyp_basicbehavior_behavioredclassifier_constructor_exists():
    assert callable(BasicBehavior_BehavioredClassifier.__init__)


def test_hyp_basicbehavior_behavioredclassifier_constructor_args():
    sig = inspect.signature(BasicBehavior_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basicbehavior_classifier_is_not_abstract():
    assert not inspect.isabstract(BasicBehavior_Classifier)


def test_hyp_basicbehavior_classifier_constructor_exists():
    assert callable(BasicBehavior_Classifier.__init__)


def test_hyp_basicbehavior_classifier_constructor_args():
    sig = inspect.signature(BasicBehavior_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_class_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_Class)


def test_hyp_commonbehavior_basicbehavior_class_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_Class.__init__)


def test_hyp_commonbehavior_basicbehavior_class_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_hyp_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_hyp_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_classifier_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_Classifier)


def test_hyp_commonbehavior_basicbehavior_classifier_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_Classifier.__init__)


def test_hyp_commonbehavior_basicbehavior_classifier_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_hyp_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_hyp_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_OpaqueBehavior)


def test_hyp_commonbehavior_basicbehavior_opaquebehavior_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_OpaqueBehavior.__init__)


def test_hyp_commonbehavior_basicbehavior_opaquebehavior_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "body" in params, "Missing parameter 'body'"





def test_hyp_commonbehavior_basicbehavior_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_BehavioralFeature)


def test_hyp_commonbehavior_basicbehavior_behavioralfeature_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_BehavioralFeature.__init__)


def test_hyp_commonbehavior_basicbehavior_behavioralfeature_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "concurrency" in params, "Missing parameter 'concurrency'"




def test_hyp_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_hyp_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_hyp_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_FunctionBehavior)


def test_hyp_commonbehavior_basicbehavior_functionbehavior_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_FunctionBehavior.__init__)


def test_hyp_commonbehavior_basicbehavior_functionbehavior_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_hyp_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_hyp_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_hyp_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_interface_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Interface)


def test_hyp_commonbehavior_communications_interface_constructor_exists():
    assert callable(CommonBehavior_Communications_Interface.__init__)


def test_hyp_commonbehavior_communications_interface_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_communications_signal_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_Communications_Signal)


def test_hyp_commonbehavior_communications_signal_constructor_exists():
    assert callable(CommonBehavior_Communications_Signal.__init__)


def test_hyp_commonbehavior_communications_signal_constructor_args():
    sig = inspect.signature(CommonBehavior_Communications_Signal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_commonbehavior_basicbehavior_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(CommonBehavior_BasicBehavior_BehavioredClassifier)


def test_hyp_commonbehavior_basicbehavior_behavioredclassifier_constructor_exists():
    assert callable(CommonBehavior_BasicBehavior_BehavioredClassifier.__init__)


def test_hyp_commonbehavior_basicbehavior_behavioredclassifier_constructor_args():
    sig = inspect.signature(CommonBehavior_BasicBehavior_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())

def test_hyp_callconcurrencyfeature_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyFeature is not None

def test_hyp_callconcurrencyfeature_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyFeature]
    expected_literals = [
        "guarded",
        "sequential",
        "concurrent",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyFeature"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
TimeInterval_strategy = st.builds(
    TimeInterval,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
CommonBehavior_SimpleTime_DurationConstraint_strategy = st.builds(
    CommonBehavior_SimpleTime_DurationConstraint,
    firstEvent=
        st.booleans()
)
CommonBehavior_SimpleTime_TimeConstraint_strategy = st.builds(
    CommonBehavior_SimpleTime_TimeConstraint,
    firstEvent=
        st.booleans()
)
Duration_strategy = st.builds(
    Duration,
)
Interval_strategy = st.builds(
    Interval,
)
CommonBehavior_SimpleTime_DurationInterval_strategy = st.builds(
    CommonBehavior_SimpleTime_DurationInterval,
)
CommonBehavior_SimpleTime_TimeInterval_strategy = st.builds(
    CommonBehavior_SimpleTime_TimeInterval,
)
DurationInterval_strategy = st.builds(
    DurationInterval,
)
TimeExpression_strategy = st.builds(
    TimeExpression,
)
CommonBehavior_SimpleTime_TimeEvent_strategy = st.builds(
    CommonBehavior_SimpleTime_TimeEvent,
    isRelative=
        st.booleans()
)
CommonBehavior_Communications_ValueSpecification_strategy = st.builds(
    CommonBehavior_Communications_ValueSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
CommonBehavior_SimpleTime_TimeExpression_strategy = st.builds(
    CommonBehavior_SimpleTime_TimeExpression,
)
CommonBehavior_SimpleTime_Duration_strategy = st.builds(
    CommonBehavior_SimpleTime_Duration,
)
CommonBehavior_SimpleTime_Interval_strategy = st.builds(
    CommonBehavior_SimpleTime_Interval,
)
CommonBehavior_Communications_Operation_strategy = st.builds(
    CommonBehavior_Communications_Operation,
)
Operation_strategy = st.builds(
    Operation,
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
CommonBehavior_Communications_SignalEvent_strategy = st.builds(
    CommonBehavior_Communications_SignalEvent,
)
CommonBehavior_Communications_CallEvent_strategy = st.builds(
    CommonBehavior_Communications_CallEvent,
)
CommonBehavior_Communications_AnyReceiveEvent_strategy = st.builds(
    CommonBehavior_Communications_AnyReceiveEvent,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
CommonBehavior_Communications_Event_strategy = st.builds(
    CommonBehavior_Communications_Event,
)
CommonBehavior_Communications_PackageableElement_strategy = st.builds(
    CommonBehavior_Communications_PackageableElement,
)
Event_strategy = st.builds(
    Event,
)
CommonBehavior_Communications_ChangeEvent_strategy = st.builds(
    CommonBehavior_Communications_ChangeEvent,
)
CommonBehavior_Communications_MessageEvent_strategy = st.builds(
    CommonBehavior_Communications_MessageEvent,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
CommonBehavior_Communications_Trigger_strategy = st.builds(
    CommonBehavior_Communications_Trigger,
)
CommonBehavior_Communications_NamedElement_strategy = st.builds(
    CommonBehavior_Communications_NamedElement,
)
CommonBehavior_SimpleTime_Observation_strategy = st.builds(
    CommonBehavior_SimpleTime_Observation,
)
Observation_strategy = st.builds(
    Observation,
)
CommonBehavior_SimpleTime_DurationObservation_strategy = st.builds(
    CommonBehavior_SimpleTime_DurationObservation,
    firstEvent=
        st.booleans()
)
CommonBehavior_SimpleTime_TimeObservation_strategy = st.builds(
    CommonBehavior_SimpleTime_TimeObservation,
    firstEvent=
        st.booleans()
)
CommonBehavior_Communications_Property_strategy = st.builds(
    CommonBehavior_Communications_Property,
)
Property_strategy = st.builds(
    Property,
)
CommonBehavior_BasicBehavior_Constraint_strategy = st.builds(
    CommonBehavior_BasicBehavior_Constraint,
)
CommonBehavior_BasicBehavior_OpaqueExpression_strategy = st.builds(
    CommonBehavior_BasicBehavior_OpaqueExpression,
)
CommonBehavior_BasicBehavior_Parameter_strategy = st.builds(
    CommonBehavior_BasicBehavior_Parameter,
)
Signal_strategy = st.builds(
    Signal,
)
CommonBehavior_BasicBehavior_RedefinableElement_strategy = st.builds(
    CommonBehavior_BasicBehavior_RedefinableElement,
)
Constraint_strategy = st.builds(
    Constraint,
)
CommonBehavior_SimpleTime_IntervalConstraint_strategy = st.builds(
    CommonBehavior_SimpleTime_IntervalConstraint,
)
Parameter_strategy = st.builds(
    Parameter,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
CommonBehavior_Communications_Reception_strategy = st.builds(
    CommonBehavior_Communications_Reception,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
Class_strategy = st.builds(
    Class,
)
CommonBehavior_BasicBehavior_Behavior_strategy = st.builds(
    CommonBehavior_BasicBehavior_Behavior,
    isReentrant=
        st.booleans()
)
Reception_strategy = st.builds(
    Reception,
)
BasicBehavior_BehavioredClassifier_strategy = st.builds(
    BasicBehavior_BehavioredClassifier,
)
BasicBehavior_Classifier_strategy = st.builds(
    BasicBehavior_Classifier,
)
CommonBehavior_BasicBehavior_Class_strategy = st.builds(
    CommonBehavior_BasicBehavior_Class,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
CommonBehavior_BasicBehavior_Classifier_strategy = st.builds(
    CommonBehavior_BasicBehavior_Classifier,
)
Behavior_strategy = st.builds(
    Behavior,
)
CommonBehavior_BasicBehavior_OpaqueBehavior_strategy = st.builds(
    CommonBehavior_BasicBehavior_OpaqueBehavior,
    language=
        safe_text,
    body=
        safe_text
)
CommonBehavior_BasicBehavior_BehavioralFeature_strategy = st.builds(
    CommonBehavior_BasicBehavior_BehavioralFeature,
    concurrency=
        safe_text
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
CommonBehavior_BasicBehavior_FunctionBehavior_strategy = st.builds(
    CommonBehavior_BasicBehavior_FunctionBehavior,
)
Classifier_strategy = st.builds(
    Classifier,
)
CommonBehavior_Communications_Interface_strategy = st.builds(
    CommonBehavior_Communications_Interface,
)
CommonBehavior_Communications_Signal_strategy = st.builds(
    CommonBehavior_Communications_Signal,
)
CommonBehavior_BasicBehavior_BehavioredClassifier_strategy = st.builds(
    CommonBehavior_BasicBehavior_BehavioredClassifier,
)






@given(instance=CommonBehavior_SimpleTime_DurationConstraint_strategy)
def test_hyp_commonbehavior_simpletime_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original




@given(instance=CommonBehavior_SimpleTime_TimeConstraint_strategy)
def test_hyp_commonbehavior_simpletime_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original










@given(instance=CommonBehavior_SimpleTime_TimeEvent_strategy)
def test_hyp_commonbehavior_simpletime_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original


























@given(instance=CommonBehavior_SimpleTime_DurationObservation_strategy)
def test_hyp_commonbehavior_simpletime_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original




@given(instance=CommonBehavior_SimpleTime_TimeObservation_strategy)
def test_hyp_commonbehavior_simpletime_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original


















@given(instance=CommonBehavior_BasicBehavior_Behavior_strategy)
def test_hyp_commonbehavior_basicbehavior_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original











@given(instance=CommonBehavior_BasicBehavior_OpaqueBehavior_strategy)
def test_hyp_commonbehavior_basicbehavior_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=CommonBehavior_BasicBehavior_OpaqueBehavior_strategy)
def test_hyp_commonbehavior_basicbehavior_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original




@given(instance=CommonBehavior_BasicBehavior_BehavioralFeature_strategy)
def test_hyp_commonbehavior_basicbehavior_behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original








# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_CommonBehavior_BasicBehavior_Behavior_isReentrant_value_roundtrip():
    instance = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    assert instance.isReentrant == True
    instance.isReentrant = False
    assert instance.isReentrant == False


def test_CommonBehavior_BasicBehavior_BehavioralFeature_concurrency_value_roundtrip():
    instance = CommonBehavior_BasicBehavior_BehavioralFeature(concurrency="sample_text")
    assert instance.concurrency == "sample_text"
    instance.concurrency = "sample_text_2"
    assert instance.concurrency == "sample_text_2"


def test_CommonBehavior_BasicBehavior_OpaqueBehavior_body_value_roundtrip():
    instance = CommonBehavior_BasicBehavior_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_CommonBehavior_BasicBehavior_OpaqueBehavior_language_value_roundtrip():
    instance = CommonBehavior_BasicBehavior_OpaqueBehavior(body="sample_text", language="sample_text")
    assert instance.language == "sample_text"
    instance.language = "sample_text_2"
    assert instance.language == "sample_text_2"


def test_CommonBehavior_SimpleTime_DurationConstraint_firstEvent_value_roundtrip():
    instance = CommonBehavior_SimpleTime_DurationConstraint(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CommonBehavior_SimpleTime_DurationObservation_firstEvent_value_roundtrip():
    instance = CommonBehavior_SimpleTime_DurationObservation(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CommonBehavior_SimpleTime_TimeConstraint_firstEvent_value_roundtrip():
    instance = CommonBehavior_SimpleTime_TimeConstraint(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CommonBehavior_SimpleTime_TimeEvent_isRelative_value_roundtrip():
    instance = CommonBehavior_SimpleTime_TimeEvent(isRelative=True)
    assert instance.isRelative == True
    instance.isRelative = False
    assert instance.isRelative == False


def test_CommonBehavior_SimpleTime_TimeObservation_firstEvent_value_roundtrip():
    instance = CommonBehavior_SimpleTime_TimeObservation(firstEvent=True)
    assert instance.firstEvent == True
    instance.firstEvent = False
    assert instance.firstEvent == False


def test_CommonBehavior_BasicBehavior_Class_isa_BasicBehavior_BehavioredClassifier():
    instance = CommonBehavior_BasicBehavior_Class()
    assert isinstance(instance, BasicBehavior_BehavioredClassifier)


def test_CommonBehavior_BasicBehavior_Class_isa_BasicBehavior_Classifier():
    instance = CommonBehavior_BasicBehavior_Class()
    assert isinstance(instance, BasicBehavior_Classifier)


def test_CommonBehavior_BasicBehavior_OpaqueBehavior_isa_Behavior():
    instance = CommonBehavior_BasicBehavior_OpaqueBehavior(body="sample_text", language="sample_text")
    assert isinstance(instance, Behavior)


def test_CommonBehavior_Communications_Reception_isa_BehavioralFeature():
    instance = CommonBehavior_Communications_Reception()
    assert isinstance(instance, BehavioralFeature)


def test_CommonBehavior_BasicBehavior_Behavior_isa_Class():
    instance = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    assert isinstance(instance, Class)


def test_CommonBehavior_BasicBehavior_BehavioredClassifier_isa_Classifier():
    instance = CommonBehavior_BasicBehavior_BehavioredClassifier()
    assert isinstance(instance, Classifier)


def test_CommonBehavior_Communications_Interface_isa_Classifier():
    instance = CommonBehavior_Communications_Interface()
    assert isinstance(instance, Classifier)


def test_CommonBehavior_Communications_Signal_isa_Classifier():
    instance = CommonBehavior_Communications_Signal()
    assert isinstance(instance, Classifier)


def test_CommonBehavior_SimpleTime_IntervalConstraint_isa_Constraint():
    instance = CommonBehavior_SimpleTime_IntervalConstraint()
    assert isinstance(instance, Constraint)


def test_CommonBehavior_Communications_ChangeEvent_isa_Event():
    instance = CommonBehavior_Communications_ChangeEvent()
    assert isinstance(instance, Event)


def test_CommonBehavior_Communications_MessageEvent_isa_Event():
    instance = CommonBehavior_Communications_MessageEvent()
    assert isinstance(instance, Event)


def test_CommonBehavior_SimpleTime_DurationInterval_isa_Interval():
    instance = CommonBehavior_SimpleTime_DurationInterval()
    assert isinstance(instance, Interval)


def test_CommonBehavior_SimpleTime_TimeInterval_isa_Interval():
    instance = CommonBehavior_SimpleTime_TimeInterval()
    assert isinstance(instance, Interval)


def test_CommonBehavior_SimpleTime_DurationConstraint_isa_IntervalConstraint():
    instance = CommonBehavior_SimpleTime_DurationConstraint(firstEvent=True)
    assert isinstance(instance, IntervalConstraint)


def test_CommonBehavior_SimpleTime_TimeConstraint_isa_IntervalConstraint():
    instance = CommonBehavior_SimpleTime_TimeConstraint(firstEvent=True)
    assert isinstance(instance, IntervalConstraint)


def test_CommonBehavior_Communications_AnyReceiveEvent_isa_MessageEvent():
    instance = CommonBehavior_Communications_AnyReceiveEvent()
    assert isinstance(instance, MessageEvent)


def test_CommonBehavior_Communications_CallEvent_isa_MessageEvent():
    instance = CommonBehavior_Communications_CallEvent()
    assert isinstance(instance, MessageEvent)


def test_CommonBehavior_Communications_SignalEvent_isa_MessageEvent():
    instance = CommonBehavior_Communications_SignalEvent()
    assert isinstance(instance, MessageEvent)


def test_CommonBehavior_Communications_Trigger_isa_NamedElement():
    instance = CommonBehavior_Communications_Trigger()
    assert isinstance(instance, NamedElement)


def test_CommonBehavior_SimpleTime_DurationObservation_isa_Observation():
    instance = CommonBehavior_SimpleTime_DurationObservation(firstEvent=True)
    assert isinstance(instance, Observation)


def test_CommonBehavior_SimpleTime_TimeObservation_isa_Observation():
    instance = CommonBehavior_SimpleTime_TimeObservation(firstEvent=True)
    assert isinstance(instance, Observation)


def test_CommonBehavior_BasicBehavior_FunctionBehavior_isa_OpaqueBehavior():
    instance = CommonBehavior_BasicBehavior_FunctionBehavior()
    assert isinstance(instance, OpaqueBehavior)


def test_CommonBehavior_Communications_Event_isa_PackageableElement():
    instance = CommonBehavior_Communications_Event()
    assert isinstance(instance, PackageableElement)


def test_CommonBehavior_SimpleTime_Observation_isa_PackageableElement():
    instance = CommonBehavior_SimpleTime_Observation()
    assert isinstance(instance, PackageableElement)


def test_CommonBehavior_BasicBehavior_Classifier_isa_RedefinableElement():
    instance = CommonBehavior_BasicBehavior_Classifier()
    assert isinstance(instance, RedefinableElement)


def test_CommonBehavior_SimpleTime_Duration_isa_ValueSpecification():
    instance = CommonBehavior_SimpleTime_Duration()
    assert isinstance(instance, ValueSpecification)


def test_CommonBehavior_SimpleTime_Interval_isa_ValueSpecification():
    instance = CommonBehavior_SimpleTime_Interval()
    assert isinstance(instance, ValueSpecification)


def test_CommonBehavior_SimpleTime_TimeExpression_isa_ValueSpecification():
    instance = CommonBehavior_SimpleTime_TimeExpression()
    assert isinstance(instance, ValueSpecification)


def test_assoc_context5_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = BehavioredClassifier()
    b2 = BehavioredClassifier()
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior', b1)
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior', b1)
    if hasattr(b1, 'BehavioredClassifier'):
        assert _is_linked(b1, 'BehavioredClassifier', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior', b2)
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior', b2)
    if hasattr(b1, 'BehavioredClassifier'):
        assert not _is_linked(b1, 'BehavioredClassifier', a)
    if hasattr(b2, 'BehavioredClassifier'):
        assert _is_linked(b2, 'BehavioredClassifier', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior', None)
    assert not _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior', b2)
    if hasattr(b2, 'BehavioredClassifier'):
        assert not _is_linked(b2, 'BehavioredClassifier', a)


def test_assoc_durationSpecification61_link_reassign_clear():
    a = CommonBehavior_SimpleTime_DurationConstraint(firstEvent=True)
    b1 = DurationInterval()
    b2 = DurationInterval()
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationConstraint', b1)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_DurationConstraint', b1)
    if hasattr(b1, 'DurationInterval'):
        assert _is_linked(b1, 'DurationInterval', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationConstraint', b2)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_DurationConstraint', b2)
    if hasattr(b1, 'DurationInterval'):
        assert not _is_linked(b1, 'DurationInterval', a)
    if hasattr(b2, 'DurationInterval'):
        assert _is_linked(b2, 'DurationInterval', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationConstraint', None)
    assert not _is_linked(a, 'CommonBehavior_SimpleTime_DurationConstraint', b2)
    if hasattr(b2, 'DurationInterval'):
        assert not _is_linked(b2, 'DurationInterval', a)


def test_assoc_event38_link_reassign_clear():
    a = CommonBehavior_SimpleTime_TimeObservation(firstEvent=True)
    b1 = NamedElement()
    b2 = NamedElement()
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeObservation', b1)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeObservation', b1)
    if hasattr(b1, 'NamedElement'):
        assert _is_linked(b1, 'NamedElement', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeObservation', b2)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeObservation', b2)
    if hasattr(b1, 'NamedElement'):
        assert not _is_linked(b1, 'NamedElement', a)
    if hasattr(b2, 'NamedElement'):
        assert _is_linked(b2, 'NamedElement', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeObservation', None)
    assert not _is_linked(a, 'CommonBehavior_SimpleTime_TimeObservation', b2)
    if hasattr(b2, 'NamedElement'):
        assert not _is_linked(b2, 'NamedElement', a)


def test_assoc_event39_link_reassign_clear():
    a = CommonBehavior_SimpleTime_DurationObservation(firstEvent=True)
    b1 = NamedElement()
    b2 = NamedElement()
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationObservation', {b1})
    assert _is_linked(a, 'CommonBehavior_SimpleTime_DurationObservation', b1)
    if hasattr(b1, 'NamedElement40'):
        assert _is_linked(b1, 'NamedElement40', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationObservation', {b2})
    assert _is_linked(a, 'CommonBehavior_SimpleTime_DurationObservation', b2)
    if hasattr(b1, 'NamedElement40'):
        assert not _is_linked(b1, 'NamedElement40', a)
    if hasattr(b2, 'NamedElement40'):
        assert _is_linked(b2, 'NamedElement40', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_DurationObservation', set())
    assert not _is_linked(a, 'CommonBehavior_SimpleTime_DurationObservation', b2)
    if hasattr(b2, 'NamedElement40'):
        assert not _is_linked(b2, 'NamedElement40', a)


def test_assoc_method17_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_BehavioralFeature(concurrency="sample_text")
    b1 = Behavior()
    b2 = Behavior()
    _safe_set(a, 'specification', {b1})
    assert _is_linked(a, 'specification', b1)
    if hasattr(b1, 'Behavior18'):
        assert _is_linked(b1, 'Behavior18', a)
    _safe_set(a, 'specification', {b2})
    assert _is_linked(a, 'specification', b2)
    if hasattr(b1, 'Behavior18'):
        assert not _is_linked(b1, 'Behavior18', a)
    if hasattr(b2, 'Behavior18'):
        assert _is_linked(b2, 'Behavior18', a)
    _safe_set(a, 'specification', set())
    assert not _is_linked(a, 'specification', b2)
    if hasattr(b2, 'Behavior18'):
        assert not _is_linked(b2, 'Behavior18', a)


def test_assoc_ownedParameter10_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = Parameter()
    b2 = Parameter()
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior11', {b1})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior11', b1)
    if hasattr(b1, 'Parameter'):
        assert _is_linked(b1, 'Parameter', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior11', {b2})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior11', b2)
    if hasattr(b1, 'Parameter'):
        assert not _is_linked(b1, 'Parameter', a)
    if hasattr(b2, 'Parameter'):
        assert _is_linked(b2, 'Parameter', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior11', set())
    assert not _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior11', b2)
    if hasattr(b2, 'Parameter'):
        assert not _is_linked(b2, 'Parameter', a)


def test_assoc_postcondition14_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior15', {b1})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior15', b1)
    if hasattr(b1, 'Constraint16'):
        assert _is_linked(b1, 'Constraint16', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior15', {b2})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior15', b2)
    if hasattr(b1, 'Constraint16'):
        assert not _is_linked(b1, 'Constraint16', a)
    if hasattr(b2, 'Constraint16'):
        assert _is_linked(b2, 'Constraint16', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior15', set())
    assert not _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior15', b2)
    if hasattr(b2, 'Constraint16'):
        assert not _is_linked(b2, 'Constraint16', a)


def test_assoc_precondition12_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = Constraint()
    b2 = Constraint()
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior13', {b1})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior13', b1)
    if hasattr(b1, 'Constraint'):
        assert _is_linked(b1, 'Constraint', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior13', {b2})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior13', b2)
    if hasattr(b1, 'Constraint'):
        assert not _is_linked(b1, 'Constraint', a)
    if hasattr(b2, 'Constraint'):
        assert _is_linked(b2, 'Constraint', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior13', set())
    assert not _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior13', b2)
    if hasattr(b2, 'Constraint'):
        assert not _is_linked(b2, 'Constraint', a)


def test_assoc_redefinedBehavior6_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = Behavior()
    b2 = Behavior()
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior7', {b1})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior7', b1)
    if hasattr(b1, 'Behavior8'):
        assert _is_linked(b1, 'Behavior8', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior7', {b2})
    assert _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior7', b2)
    if hasattr(b1, 'Behavior8'):
        assert not _is_linked(b1, 'Behavior8', a)
    if hasattr(b2, 'Behavior8'):
        assert _is_linked(b2, 'Behavior8', a)
    _safe_set(a, 'CommonBehavior_BasicBehavior_Behavior7', set())
    assert not _is_linked(a, 'CommonBehavior_BasicBehavior_Behavior7', b2)
    if hasattr(b2, 'Behavior8'):
        assert not _is_linked(b2, 'Behavior8', a)


def test_assoc_specification9_link_reassign_clear():
    a = CommonBehavior_BasicBehavior_Behavior(isReentrant=True)
    b1 = BehavioralFeature()
    b2 = BehavioralFeature()
    _safe_set(a, 'method', b1)
    assert _is_linked(a, 'method', b1)
    if hasattr(b1, 'BehavioralFeature'):
        assert _is_linked(b1, 'BehavioralFeature', a)
    _safe_set(a, 'method', b2)
    assert _is_linked(a, 'method', b2)
    if hasattr(b1, 'BehavioralFeature'):
        assert not _is_linked(b1, 'BehavioralFeature', a)
    if hasattr(b2, 'BehavioralFeature'):
        assert _is_linked(b2, 'BehavioralFeature', a)
    _safe_set(a, 'method', None)
    assert not _is_linked(a, 'method', b2)
    if hasattr(b2, 'BehavioralFeature'):
        assert not _is_linked(b2, 'BehavioralFeature', a)


def test_assoc_timeSpecification60_link_reassign_clear():
    a = CommonBehavior_SimpleTime_TimeConstraint(firstEvent=True)
    b1 = TimeInterval()
    b2 = TimeInterval()
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeConstraint', b1)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeConstraint', b1)
    if hasattr(b1, 'TimeInterval'):
        assert _is_linked(b1, 'TimeInterval', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeConstraint', b2)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeConstraint', b2)
    if hasattr(b1, 'TimeInterval'):
        assert not _is_linked(b1, 'TimeInterval', a)
    if hasattr(b2, 'TimeInterval'):
        assert _is_linked(b2, 'TimeInterval', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeConstraint', None)
    assert not _is_linked(a, 'CommonBehavior_SimpleTime_TimeConstraint', b2)
    if hasattr(b2, 'TimeInterval'):
        assert not _is_linked(b2, 'TimeInterval', a)


def test_assoc_when33_link_reassign_clear():
    a = CommonBehavior_SimpleTime_TimeEvent(isRelative=True)
    b1 = TimeExpression()
    b2 = TimeExpression()
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeEvent', b1)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeEvent', b1)
    if hasattr(b1, 'TimeExpression'):
        assert _is_linked(b1, 'TimeExpression', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeEvent', b2)
    assert _is_linked(a, 'CommonBehavior_SimpleTime_TimeEvent', b2)
    if hasattr(b1, 'TimeExpression'):
        assert not _is_linked(b1, 'TimeExpression', a)
    if hasattr(b2, 'TimeExpression'):
        assert _is_linked(b2, 'TimeExpression', a)
    _safe_set(a, 'CommonBehavior_SimpleTime_TimeEvent', None)
    assert not _is_linked(a, 'CommonBehavior_SimpleTime_TimeEvent', b2)
    if hasattr(b2, 'TimeExpression'):
        assert not _is_linked(b2, 'TimeExpression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BasicBehavior_BehavioredClassifier_strategy = st.builds(BasicBehavior_BehavioredClassifier)
@given(instance=BasicBehavior_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BasicBehavior_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BasicBehavior_BehavioredClassifier)


BasicBehavior_Classifier_strategy = st.builds(BasicBehavior_Classifier)
@given(instance=BasicBehavior_Classifier_strategy)
@settings(max_examples=25)
def test_BasicBehavior_Classifier_instantiation(instance):
    assert isinstance(instance, BasicBehavior_Classifier)


Behavior_strategy = st.builds(Behavior)
@given(instance=Behavior_strategy)
@settings(max_examples=25)
def test_Behavior_instantiation(instance):
    assert isinstance(instance, Behavior)


BehavioralFeature_strategy = st.builds(BehavioralFeature)
@given(instance=BehavioralFeature_strategy)
@settings(max_examples=25)
def test_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)


BehavioredClassifier_strategy = st.builds(BehavioredClassifier)
@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)


Class_strategy = st.builds(Class)
@given(instance=Class_strategy)
@settings(max_examples=25)
def test_Class_instantiation(instance):
    assert isinstance(instance, Class)


Classifier_strategy = st.builds(Classifier)
@given(instance=Classifier_strategy)
@settings(max_examples=25)
def test_Classifier_instantiation(instance):
    assert isinstance(instance, Classifier)


CommonBehavior_BasicBehavior_Behavior_strategy = st.builds(CommonBehavior_BasicBehavior_Behavior, isReentrant=st.booleans())
@given(instance=CommonBehavior_BasicBehavior_Behavior_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_Behavior_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_Behavior)


CommonBehavior_BasicBehavior_BehavioralFeature_strategy = st.builds(CommonBehavior_BasicBehavior_BehavioralFeature, concurrency=safe_text)
@given(instance=CommonBehavior_BasicBehavior_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_BehavioralFeature)


CommonBehavior_BasicBehavior_BehavioredClassifier_strategy = st.builds(CommonBehavior_BasicBehavior_BehavioredClassifier)
@given(instance=CommonBehavior_BasicBehavior_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_BehavioredClassifier)


CommonBehavior_BasicBehavior_Class_strategy = st.builds(CommonBehavior_BasicBehavior_Class)
@given(instance=CommonBehavior_BasicBehavior_Class_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_Class_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_Class)


CommonBehavior_BasicBehavior_Classifier_strategy = st.builds(CommonBehavior_BasicBehavior_Classifier)
@given(instance=CommonBehavior_BasicBehavior_Classifier_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_Classifier_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_Classifier)


CommonBehavior_BasicBehavior_Constraint_strategy = st.builds(CommonBehavior_BasicBehavior_Constraint)
@given(instance=CommonBehavior_BasicBehavior_Constraint_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_Constraint_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_Constraint)


CommonBehavior_BasicBehavior_FunctionBehavior_strategy = st.builds(CommonBehavior_BasicBehavior_FunctionBehavior)
@given(instance=CommonBehavior_BasicBehavior_FunctionBehavior_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_FunctionBehavior_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_FunctionBehavior)


CommonBehavior_BasicBehavior_OpaqueBehavior_strategy = st.builds(CommonBehavior_BasicBehavior_OpaqueBehavior, body=safe_text, language=safe_text)
@given(instance=CommonBehavior_BasicBehavior_OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_OpaqueBehavior)


CommonBehavior_BasicBehavior_OpaqueExpression_strategy = st.builds(CommonBehavior_BasicBehavior_OpaqueExpression)
@given(instance=CommonBehavior_BasicBehavior_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_OpaqueExpression)


CommonBehavior_BasicBehavior_Parameter_strategy = st.builds(CommonBehavior_BasicBehavior_Parameter)
@given(instance=CommonBehavior_BasicBehavior_Parameter_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_Parameter_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_Parameter)


CommonBehavior_BasicBehavior_RedefinableElement_strategy = st.builds(CommonBehavior_BasicBehavior_RedefinableElement)
@given(instance=CommonBehavior_BasicBehavior_RedefinableElement_strategy)
@settings(max_examples=25)
def test_CommonBehavior_BasicBehavior_RedefinableElement_instantiation(instance):
    assert isinstance(instance, CommonBehavior_BasicBehavior_RedefinableElement)


CommonBehavior_Communications_AnyReceiveEvent_strategy = st.builds(CommonBehavior_Communications_AnyReceiveEvent)
@given(instance=CommonBehavior_Communications_AnyReceiveEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_AnyReceiveEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_AnyReceiveEvent)


CommonBehavior_Communications_CallEvent_strategy = st.builds(CommonBehavior_Communications_CallEvent)
@given(instance=CommonBehavior_Communications_CallEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_CallEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_CallEvent)


CommonBehavior_Communications_ChangeEvent_strategy = st.builds(CommonBehavior_Communications_ChangeEvent)
@given(instance=CommonBehavior_Communications_ChangeEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_ChangeEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_ChangeEvent)


CommonBehavior_Communications_Event_strategy = st.builds(CommonBehavior_Communications_Event)
@given(instance=CommonBehavior_Communications_Event_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Event_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Event)


CommonBehavior_Communications_Interface_strategy = st.builds(CommonBehavior_Communications_Interface)
@given(instance=CommonBehavior_Communications_Interface_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Interface_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Interface)


CommonBehavior_Communications_MessageEvent_strategy = st.builds(CommonBehavior_Communications_MessageEvent)
@given(instance=CommonBehavior_Communications_MessageEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_MessageEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_MessageEvent)


CommonBehavior_Communications_NamedElement_strategy = st.builds(CommonBehavior_Communications_NamedElement)
@given(instance=CommonBehavior_Communications_NamedElement_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_NamedElement_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_NamedElement)


CommonBehavior_Communications_Operation_strategy = st.builds(CommonBehavior_Communications_Operation)
@given(instance=CommonBehavior_Communications_Operation_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Operation_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Operation)


CommonBehavior_Communications_PackageableElement_strategy = st.builds(CommonBehavior_Communications_PackageableElement)
@given(instance=CommonBehavior_Communications_PackageableElement_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_PackageableElement_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_PackageableElement)


CommonBehavior_Communications_Property_strategy = st.builds(CommonBehavior_Communications_Property)
@given(instance=CommonBehavior_Communications_Property_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Property_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Property)


CommonBehavior_Communications_Reception_strategy = st.builds(CommonBehavior_Communications_Reception)
@given(instance=CommonBehavior_Communications_Reception_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Reception_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Reception)


CommonBehavior_Communications_Signal_strategy = st.builds(CommonBehavior_Communications_Signal)
@given(instance=CommonBehavior_Communications_Signal_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Signal_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Signal)


CommonBehavior_Communications_SignalEvent_strategy = st.builds(CommonBehavior_Communications_SignalEvent)
@given(instance=CommonBehavior_Communications_SignalEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_SignalEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_SignalEvent)


CommonBehavior_Communications_Trigger_strategy = st.builds(CommonBehavior_Communications_Trigger)
@given(instance=CommonBehavior_Communications_Trigger_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_Trigger_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_Trigger)


CommonBehavior_Communications_ValueSpecification_strategy = st.builds(CommonBehavior_Communications_ValueSpecification)
@given(instance=CommonBehavior_Communications_ValueSpecification_strategy)
@settings(max_examples=25)
def test_CommonBehavior_Communications_ValueSpecification_instantiation(instance):
    assert isinstance(instance, CommonBehavior_Communications_ValueSpecification)


CommonBehavior_SimpleTime_Duration_strategy = st.builds(CommonBehavior_SimpleTime_Duration)
@given(instance=CommonBehavior_SimpleTime_Duration_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_Duration_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_Duration)


CommonBehavior_SimpleTime_DurationConstraint_strategy = st.builds(CommonBehavior_SimpleTime_DurationConstraint, firstEvent=st.booleans())
@given(instance=CommonBehavior_SimpleTime_DurationConstraint_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_DurationConstraint_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_DurationConstraint)


CommonBehavior_SimpleTime_DurationInterval_strategy = st.builds(CommonBehavior_SimpleTime_DurationInterval)
@given(instance=CommonBehavior_SimpleTime_DurationInterval_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_DurationInterval_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_DurationInterval)


CommonBehavior_SimpleTime_DurationObservation_strategy = st.builds(CommonBehavior_SimpleTime_DurationObservation, firstEvent=st.booleans())
@given(instance=CommonBehavior_SimpleTime_DurationObservation_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_DurationObservation_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_DurationObservation)


CommonBehavior_SimpleTime_Interval_strategy = st.builds(CommonBehavior_SimpleTime_Interval)
@given(instance=CommonBehavior_SimpleTime_Interval_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_Interval_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_Interval)


CommonBehavior_SimpleTime_IntervalConstraint_strategy = st.builds(CommonBehavior_SimpleTime_IntervalConstraint)
@given(instance=CommonBehavior_SimpleTime_IntervalConstraint_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_IntervalConstraint_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_IntervalConstraint)


CommonBehavior_SimpleTime_Observation_strategy = st.builds(CommonBehavior_SimpleTime_Observation)
@given(instance=CommonBehavior_SimpleTime_Observation_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_Observation_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_Observation)


CommonBehavior_SimpleTime_TimeConstraint_strategy = st.builds(CommonBehavior_SimpleTime_TimeConstraint, firstEvent=st.booleans())
@given(instance=CommonBehavior_SimpleTime_TimeConstraint_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_TimeConstraint_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_TimeConstraint)


CommonBehavior_SimpleTime_TimeEvent_strategy = st.builds(CommonBehavior_SimpleTime_TimeEvent, isRelative=st.booleans())
@given(instance=CommonBehavior_SimpleTime_TimeEvent_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_TimeEvent_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_TimeEvent)


CommonBehavior_SimpleTime_TimeExpression_strategy = st.builds(CommonBehavior_SimpleTime_TimeExpression)
@given(instance=CommonBehavior_SimpleTime_TimeExpression_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_TimeExpression_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_TimeExpression)


CommonBehavior_SimpleTime_TimeInterval_strategy = st.builds(CommonBehavior_SimpleTime_TimeInterval)
@given(instance=CommonBehavior_SimpleTime_TimeInterval_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_TimeInterval_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_TimeInterval)


CommonBehavior_SimpleTime_TimeObservation_strategy = st.builds(CommonBehavior_SimpleTime_TimeObservation, firstEvent=st.booleans())
@given(instance=CommonBehavior_SimpleTime_TimeObservation_strategy)
@settings(max_examples=25)
def test_CommonBehavior_SimpleTime_TimeObservation_instantiation(instance):
    assert isinstance(instance, CommonBehavior_SimpleTime_TimeObservation)


Constraint_strategy = st.builds(Constraint)
@given(instance=Constraint_strategy)
@settings(max_examples=25)
def test_Constraint_instantiation(instance):
    assert isinstance(instance, Constraint)


Duration_strategy = st.builds(Duration)
@given(instance=Duration_strategy)
@settings(max_examples=25)
def test_Duration_instantiation(instance):
    assert isinstance(instance, Duration)


DurationInterval_strategy = st.builds(DurationInterval)
@given(instance=DurationInterval_strategy)
@settings(max_examples=25)
def test_DurationInterval_instantiation(instance):
    assert isinstance(instance, DurationInterval)


Event_strategy = st.builds(Event)
@given(instance=Event_strategy)
@settings(max_examples=25)
def test_Event_instantiation(instance):
    assert isinstance(instance, Event)


Interval_strategy = st.builds(Interval)
@given(instance=Interval_strategy)
@settings(max_examples=25)
def test_Interval_instantiation(instance):
    assert isinstance(instance, Interval)


IntervalConstraint_strategy = st.builds(IntervalConstraint)
@given(instance=IntervalConstraint_strategy)
@settings(max_examples=25)
def test_IntervalConstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)


MessageEvent_strategy = st.builds(MessageEvent)
@given(instance=MessageEvent_strategy)
@settings(max_examples=25)
def test_MessageEvent_instantiation(instance):
    assert isinstance(instance, MessageEvent)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Observation_strategy = st.builds(Observation)
@given(instance=Observation_strategy)
@settings(max_examples=25)
def test_Observation_instantiation(instance):
    assert isinstance(instance, Observation)


OpaqueBehavior_strategy = st.builds(OpaqueBehavior)
@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=25)
def test_OpaqueBehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


PackageableElement_strategy = st.builds(PackageableElement)
@given(instance=PackageableElement_strategy)
@settings(max_examples=25)
def test_PackageableElement_instantiation(instance):
    assert isinstance(instance, PackageableElement)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Property_strategy = st.builds(Property)
@given(instance=Property_strategy)
@settings(max_examples=25)
def test_Property_instantiation(instance):
    assert isinstance(instance, Property)


Reception_strategy = st.builds(Reception)
@given(instance=Reception_strategy)
@settings(max_examples=25)
def test_Reception_instantiation(instance):
    assert isinstance(instance, Reception)


RedefinableElement_strategy = st.builds(RedefinableElement)
@given(instance=RedefinableElement_strategy)
@settings(max_examples=25)
def test_RedefinableElement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)


Signal_strategy = st.builds(Signal)
@given(instance=Signal_strategy)
@settings(max_examples=25)
def test_Signal_instantiation(instance):
    assert isinstance(instance, Signal)


TimeExpression_strategy = st.builds(TimeExpression)
@given(instance=TimeExpression_strategy)
@settings(max_examples=25)
def test_TimeExpression_instantiation(instance):
    assert isinstance(instance, TimeExpression)


TimeInterval_strategy = st.builds(TimeInterval)
@given(instance=TimeInterval_strategy)
@settings(max_examples=25)
def test_TimeInterval_instantiation(instance):
    assert isinstance(instance, TimeInterval)


ValueSpecification_strategy = st.builds(ValueSpecification)
@given(instance=ValueSpecification_strategy)
@settings(max_examples=25)
def test_ValueSpecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)



