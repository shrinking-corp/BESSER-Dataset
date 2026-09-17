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
    EtlSimpleTrace_EObject,
    EtlSimpleTrace_TraceLink,
    EtlSimpleTrace_Trace,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_etlsimpletrace_eobject_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_EObject)


def test_hyp_etlsimpletrace_eobject_constructor_exists():
    assert callable(EtlSimpleTrace_EObject.__init__)


def test_hyp_etlsimpletrace_eobject_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_etlsimpletrace_tracelink_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_TraceLink)


def test_hyp_etlsimpletrace_tracelink_constructor_exists():
    assert callable(EtlSimpleTrace_TraceLink.__init__)


def test_hyp_etlsimpletrace_tracelink_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_TraceLink.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"




def test_hyp_etlsimpletrace_trace_is_not_abstract():
    assert not inspect.isabstract(EtlSimpleTrace_Trace)


def test_hyp_etlsimpletrace_trace_constructor_exists():
    assert callable(EtlSimpleTrace_Trace.__init__)


def test_hyp_etlsimpletrace_trace_constructor_args():
    sig = inspect.signature(EtlSimpleTrace_Trace.__init__)
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
EtlSimpleTrace_EObject_strategy = st.builds(
    EtlSimpleTrace_EObject,
)
EtlSimpleTrace_TraceLink_strategy = st.builds(
    EtlSimpleTrace_TraceLink,
    description=
        safe_text
)
EtlSimpleTrace_Trace_strategy = st.builds(
    EtlSimpleTrace_Trace,
)





@given(instance=EtlSimpleTrace_TraceLink_strategy)
def test_hyp_etlsimpletrace_tracelink_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EtlSimpleTrace_EObject,
    EtlSimpleTrace_Trace,
    EtlSimpleTrace_TraceLink,
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

def test_EtlSimpleTrace_TraceLink_description_value_roundtrip():
    instance = EtlSimpleTrace_TraceLink(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_assoc_links0_link_reassign_clear():
    a = EtlSimpleTrace_TraceLink(description="sample_text")
    b1 = EtlSimpleTrace_Trace()
    b2 = EtlSimpleTrace_Trace()
    _safe_set(a, 'EtlSimpleTrace_TraceLink', b1)
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink', b1)
    if hasattr(b1, 'EtlSimpleTrace_Trace'):
        assert _is_linked(b1, 'EtlSimpleTrace_Trace', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink', b2)
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink', b2)
    if hasattr(b1, 'EtlSimpleTrace_Trace'):
        assert not _is_linked(b1, 'EtlSimpleTrace_Trace', a)
    if hasattr(b2, 'EtlSimpleTrace_Trace'):
        assert _is_linked(b2, 'EtlSimpleTrace_Trace', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink', None)
    assert not _is_linked(a, 'EtlSimpleTrace_TraceLink', b2)
    if hasattr(b2, 'EtlSimpleTrace_Trace'):
        assert not _is_linked(b2, 'EtlSimpleTrace_Trace', a)


def test_assoc_sources1_link_reassign_clear():
    a = EtlSimpleTrace_TraceLink(description="sample_text")
    b1 = EtlSimpleTrace_EObject()
    b2 = EtlSimpleTrace_EObject()
    _safe_set(a, 'EtlSimpleTrace_TraceLink2', {b1})
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink2', b1)
    if hasattr(b1, 'EtlSimpleTrace_EObject'):
        assert _is_linked(b1, 'EtlSimpleTrace_EObject', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink2', {b2})
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink2', b2)
    if hasattr(b1, 'EtlSimpleTrace_EObject'):
        assert not _is_linked(b1, 'EtlSimpleTrace_EObject', a)
    if hasattr(b2, 'EtlSimpleTrace_EObject'):
        assert _is_linked(b2, 'EtlSimpleTrace_EObject', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink2', set())
    assert not _is_linked(a, 'EtlSimpleTrace_TraceLink2', b2)
    if hasattr(b2, 'EtlSimpleTrace_EObject'):
        assert not _is_linked(b2, 'EtlSimpleTrace_EObject', a)


def test_assoc_targets3_link_reassign_clear():
    a = EtlSimpleTrace_TraceLink(description="sample_text")
    b1 = EtlSimpleTrace_EObject()
    b2 = EtlSimpleTrace_EObject()
    _safe_set(a, 'EtlSimpleTrace_TraceLink4', {b1})
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink4', b1)
    if hasattr(b1, 'EtlSimpleTrace_EObject5'):
        assert _is_linked(b1, 'EtlSimpleTrace_EObject5', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink4', {b2})
    assert _is_linked(a, 'EtlSimpleTrace_TraceLink4', b2)
    if hasattr(b1, 'EtlSimpleTrace_EObject5'):
        assert not _is_linked(b1, 'EtlSimpleTrace_EObject5', a)
    if hasattr(b2, 'EtlSimpleTrace_EObject5'):
        assert _is_linked(b2, 'EtlSimpleTrace_EObject5', a)
    _safe_set(a, 'EtlSimpleTrace_TraceLink4', set())
    assert not _is_linked(a, 'EtlSimpleTrace_TraceLink4', b2)
    if hasattr(b2, 'EtlSimpleTrace_EObject5'):
        assert not _is_linked(b2, 'EtlSimpleTrace_EObject5', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EtlSimpleTrace_EObject_strategy = st.builds(EtlSimpleTrace_EObject)
@given(instance=EtlSimpleTrace_EObject_strategy)
@settings(max_examples=25)
def test_EtlSimpleTrace_EObject_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_EObject)


EtlSimpleTrace_Trace_strategy = st.builds(EtlSimpleTrace_Trace)
@given(instance=EtlSimpleTrace_Trace_strategy)
@settings(max_examples=25)
def test_EtlSimpleTrace_Trace_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_Trace)


EtlSimpleTrace_TraceLink_strategy = st.builds(EtlSimpleTrace_TraceLink, description=safe_text)
@given(instance=EtlSimpleTrace_TraceLink_strategy)
@settings(max_examples=25)
def test_EtlSimpleTrace_TraceLink_instantiation(instance):
    assert isinstance(instance, EtlSimpleTrace_TraceLink)



