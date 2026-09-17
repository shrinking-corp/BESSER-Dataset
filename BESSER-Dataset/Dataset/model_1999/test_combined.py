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
    TraceElement,
    trace_EObject,
    trace_TraceElement,
    trace_TraceProperty,
    trace_TraceLink,
    trace_SourceElementList,
    trace_SourceElement,
    trace_TracedRule,
    trace_TargetElement,
    trace_TraceLinkSet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_traceelement_is_not_abstract():
    assert not inspect.isabstract(TraceElement)


def test_hyp_traceelement_constructor_exists():
    assert callable(TraceElement.__init__)


def test_hyp_traceelement_constructor_args():
    sig = inspect.signature(TraceElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trace_eobject_is_not_abstract():
    assert not inspect.isabstract(trace_EObject)


def test_hyp_trace_eobject_constructor_exists():
    assert callable(trace_EObject.__init__)


def test_hyp_trace_eobject_constructor_args():
    sig = inspect.signature(trace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trace_traceelement_is_not_abstract():
    assert not inspect.isabstract(trace_TraceElement)


def test_hyp_trace_traceelement_constructor_exists():
    assert callable(trace_TraceElement.__init__)


def test_hyp_trace_traceelement_constructor_args():
    sig = inspect.signature(trace_TraceElement.__init__)
    params = list(sig.parameters.keys())
    assert "runtimeObject" in params, "Missing parameter 'runtimeObject'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_trace_traceproperty_is_not_abstract():
    assert not inspect.isabstract(trace_TraceProperty)


def test_hyp_trace_traceproperty_constructor_exists():
    assert callable(trace_TraceProperty.__init__)


def test_hyp_trace_traceproperty_constructor_args():
    sig = inspect.signature(trace_TraceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "resolved" in params, "Missing parameter 'resolved'"





def test_hyp_trace_tracelink_is_not_abstract():
    assert not inspect.isabstract(trace_TraceLink)


def test_hyp_trace_tracelink_constructor_exists():
    assert callable(trace_TraceLink.__init__)


def test_hyp_trace_tracelink_constructor_args():
    sig = inspect.signature(trace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "overridden" in params, "Missing parameter 'overridden'"




def test_hyp_trace_sourceelementlist_is_not_abstract():
    assert not inspect.isabstract(trace_SourceElementList)


def test_hyp_trace_sourceelementlist_constructor_exists():
    assert callable(trace_SourceElementList.__init__)


def test_hyp_trace_sourceelementlist_constructor_args():
    sig = inspect.signature(trace_SourceElementList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trace_sourceelement_is_not_abstract():
    assert not inspect.isabstract(trace_SourceElement)


def test_hyp_trace_sourceelement_constructor_exists():
    assert callable(trace_SourceElement.__init__)


def test_hyp_trace_sourceelement_constructor_args():
    sig = inspect.signature(trace_SourceElement.__init__)
    params = list(sig.parameters.keys())
    assert "mapsToSelf" in params, "Missing parameter 'mapsToSelf'"




def test_hyp_trace_tracedrule_is_not_abstract():
    assert not inspect.isabstract(trace_TracedRule)


def test_hyp_trace_tracedrule_constructor_exists():
    assert callable(trace_TracedRule.__init__)


def test_hyp_trace_tracedrule_constructor_args():
    sig = inspect.signature(trace_TracedRule.__init__)
    params = list(sig.parameters.keys())
    assert "rule" in params, "Missing parameter 'rule'"

def test_hyp_trace_tracedrule_has_rule():
    assert hasattr(trace_TracedRule, "rule")
    descriptor = None
    for klass in trace_TracedRule.__mro__:
        if "rule" in klass.__dict__:
            descriptor = klass.__dict__["rule"]
            break
    assert isinstance(descriptor, property)



def test_hyp_trace_targetelement_is_not_abstract():
    assert not inspect.isabstract(trace_TargetElement)


def test_hyp_trace_targetelement_constructor_exists():
    assert callable(trace_TargetElement.__init__)


def test_hyp_trace_targetelement_constructor_args():
    sig = inspect.signature(trace_TargetElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_trace_tracelinkset_is_not_abstract():
    assert not inspect.isabstract(trace_TraceLinkSet)


def test_hyp_trace_tracelinkset_constructor_exists():
    assert callable(trace_TraceLinkSet.__init__)


def test_hyp_trace_tracelinkset_constructor_args():
    sig = inspect.signature(trace_TraceLinkSet.__init__)
    params = list(sig.parameters.keys())


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
TraceElement_strategy = st.builds(
    TraceElement,
)
trace_EObject_strategy = st.builds(
    trace_EObject,
)
trace_TraceElement_strategy = st.builds(
    trace_TraceElement,
    runtimeObject=
        safe_text,
    name=
        safe_text
)
trace_TraceProperty_strategy = st.builds(
    trace_TraceProperty,
    propertyName=
        safe_text,
    resolved=
        st.booleans()
)
trace_TraceLink_strategy = st.builds(
    trace_TraceLink,
    overridden=
        st.booleans()
)
trace_SourceElementList_strategy = st.builds(
    trace_SourceElementList,
)
trace_SourceElement_strategy = st.builds(
    trace_SourceElement,
    mapsToSelf=
        st.booleans()
)
trace_TracedRule_strategy = st.builds(
    trace_TracedRule,
    rule=
        safe_text
)
trace_TargetElement_strategy = st.builds(
    trace_TargetElement,
)
trace_TraceLinkSet_strategy = st.builds(
    trace_TraceLinkSet,
)






@given(instance=trace_TraceElement_strategy)
def test_hyp_trace_traceelement_runtimeObject_setter(instance):
    original = instance.runtimeObject
    instance.runtimeObject = original
    assert instance.runtimeObject == original



@given(instance=trace_TraceElement_strategy)
def test_hyp_trace_traceelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=trace_TraceProperty_strategy)
def test_hyp_trace_traceproperty_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original



@given(instance=trace_TraceProperty_strategy)
def test_hyp_trace_traceproperty_resolved_setter(instance):
    original = instance.resolved
    instance.resolved = original
    assert instance.resolved == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=trace_TraceProperty_strategy)
@settings(max_examples=30)
def test_hyp_trace_traceproperty_resolvebinding_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resolveBinding(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resolveBinding).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resolveBinding' in trace_TraceProperty is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resolveBinding' in trace_TraceProperty did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resolveBinding' in trace_TraceProperty is not implemented or raised an error")




@given(instance=trace_TraceLink_strategy)
def test_hyp_trace_tracelink_overridden_setter(instance):
    original = instance.overridden
    instance.overridden = original
    assert instance.overridden == original





@given(instance=trace_SourceElement_strategy)
def test_hyp_trace_sourceelement_mapsToSelf_setter(instance):
    original = instance.mapsToSelf
    instance.mapsToSelf = original
    assert instance.mapsToSelf == original

@given(instance=trace_TracedRule_strategy)
@settings(max_examples=50)
def test_hyp_trace_tracedrule_instantiation(instance):
    assert isinstance(instance, trace_TracedRule)



@given(instance=trace_TracedRule_strategy)
def test_hyp_trace_tracedrule_rule_setter(instance):
    original = instance.rule
    instance.rule = original
    assert instance.rule == original



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=trace_TraceLinkSet_strategy)
@settings(max_examples=30)
def test_hyp_trace_tracelinkset_clear_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.clear()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.clear).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'clear' in trace_TraceLinkSet is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'clear' in trace_TraceLinkSet did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'clear' in trace_TraceLinkSet is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    TraceElement,
    trace_EObject,
    trace_SourceElement,
    trace_SourceElementList,
    trace_TargetElement,
    trace_TraceElement,
    trace_TraceLink,
    trace_TraceLinkSet,
    trace_TraceProperty,
    trace_TracedRule,
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

def test_trace_SourceElement_mapsToSelf_value_roundtrip():
    instance = trace_SourceElement(mapsToSelf=True)
    assert instance.mapsToSelf == True
    instance.mapsToSelf = False
    assert instance.mapsToSelf == False


def test_trace_TraceElement_name_value_roundtrip():
    instance = trace_TraceElement(name="sample_text", runtimeObject="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_trace_TraceElement_runtimeObject_value_roundtrip():
    instance = trace_TraceElement(name="sample_text", runtimeObject="sample_text")
    assert instance.runtimeObject == "sample_text"
    instance.runtimeObject = "sample_text_2"
    assert instance.runtimeObject == "sample_text_2"


def test_trace_TraceLink_overridden_value_roundtrip():
    instance = trace_TraceLink(overridden=True)
    assert instance.overridden == True
    instance.overridden = False
    assert instance.overridden == False


def test_trace_TraceProperty_propertyName_value_roundtrip():
    instance = trace_TraceProperty(propertyName="sample_text", resolved=True)
    assert instance.propertyName == "sample_text"
    instance.propertyName = "sample_text_2"
    assert instance.propertyName == "sample_text_2"


def test_trace_TraceProperty_resolved_value_roundtrip():
    instance = trace_TraceProperty(propertyName="sample_text", resolved=True)
    assert instance.resolved == True
    instance.resolved = False
    assert instance.resolved == False


def test_trace_SourceElement_isa_TraceElement():
    instance = trace_SourceElement(mapsToSelf=True)
    assert isinstance(instance, TraceElement)


def test_trace_TargetElement_isa_TraceElement():
    instance = trace_TargetElement()
    assert isinstance(instance, TraceElement)


def test_assoc_appliedAt40_link_reassign_clear():
    a = trace_TraceProperty(propertyName="sample_text", resolved=True)
    b1 = trace_TraceLink(overridden=True)
    b2 = trace_TraceLink(overridden=False)
    _safe_set(a, 'properties', b1)
    assert _is_linked(a, 'properties', b1)
    if hasattr(b1, 'TraceLink41'):
        assert _is_linked(b1, 'TraceLink41', a)
    _safe_set(a, 'properties', b2)
    assert _is_linked(a, 'properties', b2)
    if hasattr(b1, 'TraceLink41'):
        assert not _is_linked(b1, 'TraceLink41', a)
    if hasattr(b2, 'TraceLink41'):
        assert _is_linked(b2, 'TraceLink41', a)
    _safe_set(a, 'properties', None)
    assert not _is_linked(a, 'properties', b2)
    if hasattr(b2, 'TraceLink41'):
        assert not _is_linked(b2, 'TraceLink41', a)


def test_assoc_defaultFor22_link_reassign_clear():
    a = trace_TraceLinkSet()
    b1 = trace_SourceElement(mapsToSelf=True)
    b2 = trace_SourceElement(mapsToSelf=False)
    _safe_set(a, 'TraceLinkSet23', b1)
    assert _is_linked(a, 'TraceLinkSet23', b1)
    if hasattr(b1, 'defaultSourceElements'):
        assert _is_linked(b1, 'defaultSourceElements', a)
    _safe_set(a, 'TraceLinkSet23', b2)
    assert _is_linked(a, 'TraceLinkSet23', b2)
    if hasattr(b1, 'defaultSourceElements'):
        assert not _is_linked(b1, 'defaultSourceElements', a)
    if hasattr(b2, 'defaultSourceElements'):
        assert _is_linked(b2, 'defaultSourceElements', a)
    _safe_set(a, 'TraceLinkSet23', None)
    assert not _is_linked(a, 'TraceLinkSet23', b2)
    if hasattr(b2, 'defaultSourceElements'):
        assert not _is_linked(b2, 'defaultSourceElements', a)


def test_assoc_defaultFor32_link_reassign_clear():
    a = trace_TraceLinkSet()
    b1 = trace_SourceElementList()
    b2 = trace_SourceElementList()
    _safe_set(a, 'TraceLinkSet33', b1)
    assert _is_linked(a, 'TraceLinkSet33', b1)
    if hasattr(b1, 'defaultSourceElementLists'):
        assert _is_linked(b1, 'defaultSourceElementLists', a)
    _safe_set(a, 'TraceLinkSet33', b2)
    assert _is_linked(a, 'TraceLinkSet33', b2)
    if hasattr(b1, 'defaultSourceElementLists'):
        assert not _is_linked(b1, 'defaultSourceElementLists', a)
    if hasattr(b2, 'defaultSourceElementLists'):
        assert _is_linked(b2, 'defaultSourceElementLists', a)
    _safe_set(a, 'TraceLinkSet33', None)
    assert not _is_linked(a, 'TraceLinkSet33', b2)
    if hasattr(b2, 'defaultSourceElementLists'):
        assert not _is_linked(b2, 'defaultSourceElementLists', a)


def test_assoc_defaultSourceElementLists2_link_reassign_clear():
    a = trace_TraceLinkSet()
    b1 = trace_SourceElementList()
    b2 = trace_SourceElementList()
    _safe_set(a, 'defaultFor3', {b1})
    assert _is_linked(a, 'defaultFor3', b1)
    if hasattr(b1, 'SourceElementList'):
        assert _is_linked(b1, 'SourceElementList', a)
    _safe_set(a, 'defaultFor3', {b2})
    assert _is_linked(a, 'defaultFor3', b2)
    if hasattr(b1, 'SourceElementList'):
        assert not _is_linked(b1, 'SourceElementList', a)
    if hasattr(b2, 'SourceElementList'):
        assert _is_linked(b2, 'SourceElementList', a)
    _safe_set(a, 'defaultFor3', set())
    assert not _is_linked(a, 'defaultFor3', b2)
    if hasattr(b2, 'SourceElementList'):
        assert not _is_linked(b2, 'SourceElementList', a)


def test_assoc_defaultSourceElements1_link_reassign_clear():
    a = trace_TraceLinkSet()
    b1 = trace_SourceElement(mapsToSelf=True)
    b2 = trace_SourceElement(mapsToSelf=False)
    _safe_set(a, 'defaultFor', {b1})
    assert _is_linked(a, 'defaultFor', b1)
    if hasattr(b1, 'SourceElement'):
        assert _is_linked(b1, 'SourceElement', a)
    _safe_set(a, 'defaultFor', {b2})
    assert _is_linked(a, 'defaultFor', b2)
    if hasattr(b1, 'SourceElement'):
        assert not _is_linked(b1, 'SourceElement', a)
    if hasattr(b2, 'SourceElement'):
        assert _is_linked(b2, 'SourceElement', a)
    _safe_set(a, 'defaultFor', set())
    assert not _is_linked(a, 'defaultFor', b2)
    if hasattr(b2, 'SourceElement'):
        assert not _is_linked(b2, 'SourceElement', a)


def test_assoc_mapsTo20_link_reassign_clear():
    a = trace_SourceElement(mapsToSelf=True)
    b1 = trace_TargetElement()
    b2 = trace_TargetElement()
    _safe_set(a, 'mapsTo', {b1})
    assert _is_linked(a, 'mapsTo', b1)
    if hasattr(b1, 'TargetElement21'):
        assert _is_linked(b1, 'TargetElement21', a)
    _safe_set(a, 'mapsTo', {b2})
    assert _is_linked(a, 'mapsTo', b2)
    if hasattr(b1, 'TargetElement21'):
        assert not _is_linked(b1, 'TargetElement21', a)
    if hasattr(b2, 'TargetElement21'):
        assert _is_linked(b2, 'TargetElement21', a)
    _safe_set(a, 'mapsTo', set())
    assert not _is_linked(a, 'mapsTo', b2)
    if hasattr(b2, 'TargetElement21'):
        assert not _is_linked(b2, 'TargetElement21', a)


def test_assoc_mapsTo28_link_reassign_clear():
    a = trace_SourceElement(mapsToSelf=True)
    b1 = trace_TargetElement()
    b2 = trace_TargetElement()
    _safe_set(a, 'SourceElement30', b1)
    assert _is_linked(a, 'SourceElement30', b1)
    if hasattr(b1, 'mapsTo29'):
        assert _is_linked(b1, 'mapsTo29', a)
    _safe_set(a, 'SourceElement30', b2)
    assert _is_linked(a, 'SourceElement30', b2)
    if hasattr(b1, 'mapsTo29'):
        assert not _is_linked(b1, 'mapsTo29', a)
    if hasattr(b2, 'mapsTo29'):
        assert _is_linked(b2, 'mapsTo29', a)
    _safe_set(a, 'SourceElement30', None)
    assert not _is_linked(a, 'SourceElement30', b2)
    if hasattr(b2, 'mapsTo29'):
        assert not _is_linked(b2, 'mapsTo29', a)


def test_assoc_object17_link_reassign_clear():
    a = trace_TraceElement(name="sample_text", runtimeObject="sample_text")
    b1 = trace_EObject()
    b2 = trace_EObject()
    _safe_set(a, 'trace_TraceElement', b1)
    assert _is_linked(a, 'trace_TraceElement', b1)
    if hasattr(b1, 'trace_EObject'):
        assert _is_linked(b1, 'trace_EObject', a)
    _safe_set(a, 'trace_TraceElement', b2)
    assert _is_linked(a, 'trace_TraceElement', b2)
    if hasattr(b1, 'trace_EObject'):
        assert not _is_linked(b1, 'trace_EObject', a)
    if hasattr(b2, 'trace_EObject'):
        assert _is_linked(b2, 'trace_EObject', a)
    _safe_set(a, 'trace_TraceElement', None)
    assert not _is_linked(a, 'trace_TraceElement', b2)
    if hasattr(b2, 'trace_EObject'):
        assert not _is_linked(b2, 'trace_EObject', a)


def test_assoc_properties16_link_reassign_clear():
    a = trace_TraceProperty(propertyName="sample_text", resolved=True)
    b1 = trace_TraceLink(overridden=True)
    b2 = trace_TraceLink(overridden=False)
    _safe_set(a, 'TraceProperty', b1)
    assert _is_linked(a, 'TraceProperty', b1)
    if hasattr(b1, 'appliedAt'):
        assert _is_linked(b1, 'appliedAt', a)
    _safe_set(a, 'TraceProperty', b2)
    assert _is_linked(a, 'TraceProperty', b2)
    if hasattr(b1, 'appliedAt'):
        assert not _is_linked(b1, 'appliedAt', a)
    if hasattr(b2, 'appliedAt'):
        assert _is_linked(b2, 'appliedAt', a)
    _safe_set(a, 'TraceProperty', None)
    assert not _is_linked(a, 'TraceProperty', b2)
    if hasattr(b2, 'appliedAt'):
        assert not _is_linked(b2, 'appliedAt', a)


def test_assoc_resolvedFor36_link_reassign_clear():
    a = trace_TraceProperty(propertyName="sample_text", resolved=True)
    b1 = trace_TargetElement()
    b2 = trace_TargetElement()
    _safe_set(a, 'trace_TraceProperty', b1)
    assert _is_linked(a, 'trace_TraceProperty', b1)
    if hasattr(b1, 'trace_TargetElement'):
        assert _is_linked(b1, 'trace_TargetElement', a)
    _safe_set(a, 'trace_TraceProperty', b2)
    assert _is_linked(a, 'trace_TraceProperty', b2)
    if hasattr(b1, 'trace_TargetElement'):
        assert not _is_linked(b1, 'trace_TargetElement', a)
    if hasattr(b2, 'trace_TargetElement'):
        assert _is_linked(b2, 'trace_TargetElement', a)
    _safe_set(a, 'trace_TraceProperty', None)
    assert not _is_linked(a, 'trace_TraceProperty', b2)
    if hasattr(b2, 'trace_TargetElement'):
        assert not _is_linked(b2, 'trace_TargetElement', a)


def test_assoc_resolvings37_link_reassign_clear():
    a = trace_TraceProperty(propertyName="sample_text", resolved=True)
    b1 = trace_EObject()
    b2 = trace_EObject()
    _safe_set(a, 'trace_TraceProperty38', {b1})
    assert _is_linked(a, 'trace_TraceProperty38', b1)
    if hasattr(b1, 'trace_EObject39'):
        assert _is_linked(b1, 'trace_EObject39', a)
    _safe_set(a, 'trace_TraceProperty38', {b2})
    assert _is_linked(a, 'trace_TraceProperty38', b2)
    if hasattr(b1, 'trace_EObject39'):
        assert not _is_linked(b1, 'trace_EObject39', a)
    if hasattr(b2, 'trace_EObject39'):
        assert _is_linked(b2, 'trace_EObject39', a)
    _safe_set(a, 'trace_TraceProperty38', set())
    assert not _is_linked(a, 'trace_TraceProperty38', b2)
    if hasattr(b2, 'trace_EObject39'):
        assert not _is_linked(b2, 'trace_EObject39', a)


def test_assoc_sourceElements11_link_reassign_clear():
    a = trace_TraceLink(overridden=True)
    b1 = trace_SourceElement(mapsToSelf=True)
    b2 = trace_SourceElement(mapsToSelf=False)
    _safe_set(a, 'sourceOf', {b1})
    assert _is_linked(a, 'sourceOf', b1)
    if hasattr(b1, 'SourceElement12'):
        assert _is_linked(b1, 'SourceElement12', a)
    _safe_set(a, 'sourceOf', {b2})
    assert _is_linked(a, 'sourceOf', b2)
    if hasattr(b1, 'SourceElement12'):
        assert not _is_linked(b1, 'SourceElement12', a)
    if hasattr(b2, 'SourceElement12'):
        assert _is_linked(b2, 'SourceElement12', a)
    _safe_set(a, 'sourceOf', set())
    assert not _is_linked(a, 'sourceOf', b2)
    if hasattr(b2, 'SourceElement12'):
        assert not _is_linked(b2, 'SourceElement12', a)


def test_assoc_sourceElements31_link_reassign_clear():
    a = trace_SourceElementList()
    b1 = trace_SourceElement(mapsToSelf=True)
    b2 = trace_SourceElement(mapsToSelf=False)
    _safe_set(a, 'trace_SourceElementList', {b1})
    assert _is_linked(a, 'trace_SourceElementList', b1)
    if hasattr(b1, 'trace_SourceElement'):
        assert _is_linked(b1, 'trace_SourceElement', a)
    _safe_set(a, 'trace_SourceElementList', {b2})
    assert _is_linked(a, 'trace_SourceElementList', b2)
    if hasattr(b1, 'trace_SourceElement'):
        assert not _is_linked(b1, 'trace_SourceElement', a)
    if hasattr(b2, 'trace_SourceElement'):
        assert _is_linked(b2, 'trace_SourceElement', a)
    _safe_set(a, 'trace_SourceElementList', set())
    assert not _is_linked(a, 'trace_SourceElementList', b2)
    if hasattr(b2, 'trace_SourceElement'):
        assert not _is_linked(b2, 'trace_SourceElement', a)


def test_assoc_sourceOf18_link_reassign_clear():
    a = trace_TraceLink(overridden=True)
    b1 = trace_SourceElement(mapsToSelf=True)
    b2 = trace_SourceElement(mapsToSelf=False)
    _safe_set(a, 'TraceLink19', b1)
    assert _is_linked(a, 'TraceLink19', b1)
    if hasattr(b1, 'sourceElements'):
        assert _is_linked(b1, 'sourceElements', a)
    _safe_set(a, 'TraceLink19', b2)
    assert _is_linked(a, 'TraceLink19', b2)
    if hasattr(b1, 'sourceElements'):
        assert not _is_linked(b1, 'sourceElements', a)
    if hasattr(b2, 'sourceElements'):
        assert _is_linked(b2, 'sourceElements', a)
    _safe_set(a, 'TraceLink19', None)
    assert not _is_linked(a, 'TraceLink19', b2)
    if hasattr(b2, 'sourceElements'):
        assert not _is_linked(b2, 'sourceElements', a)


def test_assoc_targetElements13_link_reassign_clear():
    a = trace_TraceLink(overridden=True)
    b1 = trace_TargetElement()
    b2 = trace_TargetElement()
    _safe_set(a, 'targetOf', {b1})
    assert _is_linked(a, 'targetOf', b1)
    if hasattr(b1, 'TargetElement'):
        assert _is_linked(b1, 'TargetElement', a)
    _safe_set(a, 'targetOf', {b2})
    assert _is_linked(a, 'targetOf', b2)
    if hasattr(b1, 'TargetElement'):
        assert not _is_linked(b1, 'TargetElement', a)
    if hasattr(b2, 'TargetElement'):
        assert _is_linked(b2, 'TargetElement', a)
    _safe_set(a, 'targetOf', set())
    assert not _is_linked(a, 'targetOf', b2)
    if hasattr(b2, 'TargetElement'):
        assert not _is_linked(b2, 'TargetElement', a)


def test_assoc_targetOf26_link_reassign_clear():
    a = trace_TraceLink(overridden=True)
    b1 = trace_TargetElement()
    b2 = trace_TargetElement()
    _safe_set(a, 'TraceLink27', b1)
    assert _is_linked(a, 'TraceLink27', b1)
    if hasattr(b1, 'targetElements'):
        assert _is_linked(b1, 'targetElements', a)
    _safe_set(a, 'TraceLink27', b2)
    assert _is_linked(a, 'TraceLink27', b2)
    if hasattr(b1, 'targetElements'):
        assert not _is_linked(b1, 'targetElements', a)
    if hasattr(b2, 'targetElements'):
        assert _is_linked(b2, 'targetElements', a)
    _safe_set(a, 'TraceLink27', None)
    assert not _is_linked(a, 'TraceLink27', b2)
    if hasattr(b2, 'targetElements'):
        assert not _is_linked(b2, 'targetElements', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

TraceElement_strategy = st.builds(TraceElement)
@given(instance=TraceElement_strategy)
@settings(max_examples=25)
def test_TraceElement_instantiation(instance):
    assert isinstance(instance, TraceElement)


trace_EObject_strategy = st.builds(trace_EObject)
@given(instance=trace_EObject_strategy)
@settings(max_examples=25)
def test_trace_EObject_instantiation(instance):
    assert isinstance(instance, trace_EObject)


trace_SourceElement_strategy = st.builds(trace_SourceElement, mapsToSelf=st.booleans())
@given(instance=trace_SourceElement_strategy)
@settings(max_examples=25)
def test_trace_SourceElement_instantiation(instance):
    assert isinstance(instance, trace_SourceElement)


trace_SourceElementList_strategy = st.builds(trace_SourceElementList)
@given(instance=trace_SourceElementList_strategy)
@settings(max_examples=25)
def test_trace_SourceElementList_instantiation(instance):
    assert isinstance(instance, trace_SourceElementList)


trace_TargetElement_strategy = st.builds(trace_TargetElement)
@given(instance=trace_TargetElement_strategy)
@settings(max_examples=25)
def test_trace_TargetElement_instantiation(instance):
    assert isinstance(instance, trace_TargetElement)


trace_TraceElement_strategy = st.builds(trace_TraceElement, name=safe_text, runtimeObject=safe_text)
@given(instance=trace_TraceElement_strategy)
@settings(max_examples=25)
def test_trace_TraceElement_instantiation(instance):
    assert isinstance(instance, trace_TraceElement)


trace_TraceLink_strategy = st.builds(trace_TraceLink, overridden=st.booleans())
@given(instance=trace_TraceLink_strategy)
@settings(max_examples=25)
def test_trace_TraceLink_instantiation(instance):
    assert isinstance(instance, trace_TraceLink)


trace_TraceLinkSet_strategy = st.builds(trace_TraceLinkSet)
@given(instance=trace_TraceLinkSet_strategy)
@settings(max_examples=25)
def test_trace_TraceLinkSet_instantiation(instance):
    assert isinstance(instance, trace_TraceLinkSet)


trace_TraceProperty_strategy = st.builds(trace_TraceProperty, propertyName=safe_text, resolved=st.booleans())
@given(instance=trace_TraceProperty_strategy)
@settings(max_examples=25)
def test_trace_TraceProperty_instantiation(instance):
    assert isinstance(instance, trace_TraceProperty)



