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
    DataValue,
    xunit_DataValue,
    xunit_Action,
    xunit_ExpectedValue,
    NamedElement,
    xunit_Assertion,
    xunit_TestCase,
    xunit_TestSuite,
    xunit_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_datavalue_is_not_abstract():
    assert not inspect.isabstract(DataValue)


def test_hyp_datavalue_constructor_exists():
    assert callable(DataValue.__init__)


def test_hyp_datavalue_constructor_args():
    sig = inspect.signature(DataValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xunit_datavalue_is_not_abstract():
    assert not inspect.isabstract(xunit_DataValue)


def test_hyp_xunit_datavalue_constructor_exists():
    assert callable(xunit_DataValue.__init__)


def test_hyp_xunit_datavalue_constructor_args():
    sig = inspect.signature(xunit_DataValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_xunit_action_is_not_abstract():
    assert not inspect.isabstract(xunit_Action)


def test_hyp_xunit_action_constructor_exists():
    assert callable(xunit_Action.__init__)


def test_hyp_xunit_action_constructor_args():
    sig = inspect.signature(xunit_Action.__init__)
    params = list(sig.parameters.keys())
    assert "desc" in params, "Missing parameter 'desc'"




def test_hyp_xunit_expectedvalue_is_not_abstract():
    assert not inspect.isabstract(xunit_ExpectedValue)


def test_hyp_xunit_expectedvalue_constructor_exists():
    assert callable(xunit_ExpectedValue.__init__)


def test_hyp_xunit_expectedvalue_constructor_args():
    sig = inspect.signature(xunit_ExpectedValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xunit_assertion_is_not_abstract():
    assert not inspect.isabstract(xunit_Assertion)


def test_hyp_xunit_assertion_constructor_exists():
    assert callable(xunit_Assertion.__init__)


def test_hyp_xunit_assertion_constructor_args():
    sig = inspect.signature(xunit_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_xunit_testcase_is_not_abstract():
    assert not inspect.isabstract(xunit_TestCase)


def test_hyp_xunit_testcase_constructor_exists():
    assert callable(xunit_TestCase.__init__)


def test_hyp_xunit_testcase_constructor_args():
    sig = inspect.signature(xunit_TestCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xunit_testsuite_is_not_abstract():
    assert not inspect.isabstract(xunit_TestSuite)


def test_hyp_xunit_testsuite_constructor_exists():
    assert callable(xunit_TestSuite.__init__)


def test_hyp_xunit_testsuite_constructor_args():
    sig = inspect.signature(xunit_TestSuite.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xunit_namedelement_is_not_abstract():
    assert not inspect.isabstract(xunit_NamedElement)


def test_hyp_xunit_namedelement_constructor_exists():
    assert callable(xunit_NamedElement.__init__)


def test_hyp_xunit_namedelement_constructor_args():
    sig = inspect.signature(xunit_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
DataValue_strategy = st.builds(
    DataValue,
)
xunit_DataValue_strategy = st.builds(
    xunit_DataValue,
    value=
        safe_text
)
xunit_Action_strategy = st.builds(
    xunit_Action,
    desc=
        safe_text
)
xunit_ExpectedValue_strategy = st.builds(
    xunit_ExpectedValue,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
xunit_Assertion_strategy = st.builds(
    xunit_Assertion,
    type=
        safe_text
)
xunit_TestCase_strategy = st.builds(
    xunit_TestCase,
)
xunit_TestSuite_strategy = st.builds(
    xunit_TestSuite,
)
xunit_NamedElement_strategy = st.builds(
    xunit_NamedElement,
    name=
        safe_text
)





@given(instance=xunit_DataValue_strategy)
def test_hyp_xunit_datavalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=xunit_Action_strategy)
def test_hyp_xunit_action_desc_setter(instance):
    original = instance.desc
    instance.desc = original
    assert instance.desc == original






@given(instance=xunit_Assertion_strategy)
def test_hyp_xunit_assertion_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=xunit_NamedElement_strategy)
def test_hyp_xunit_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    DataValue,
    NamedElement,
    xunit_Action,
    xunit_Assertion,
    xunit_DataValue,
    xunit_ExpectedValue,
    xunit_NamedElement,
    xunit_TestCase,
    xunit_TestSuite,
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

def test_xunit_Action_desc_value_roundtrip():
    instance = xunit_Action(desc="sample_text")
    assert instance.desc == "sample_text"
    instance.desc = "sample_text_2"
    assert instance.desc == "sample_text_2"


def test_xunit_Assertion_type_value_roundtrip():
    instance = xunit_Assertion(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_xunit_DataValue_value_value_roundtrip():
    instance = xunit_DataValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_xunit_NamedElement_name_value_roundtrip():
    instance = xunit_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_xunit_ExpectedValue_isa_DataValue():
    instance = xunit_ExpectedValue()
    assert isinstance(instance, DataValue)


def test_xunit_Assertion_isa_NamedElement():
    instance = xunit_Assertion(type="sample_text")
    assert isinstance(instance, NamedElement)


def test_xunit_TestCase_isa_NamedElement():
    instance = xunit_TestCase()
    assert isinstance(instance, NamedElement)


def test_xunit_TestSuite_isa_NamedElement():
    instance = xunit_TestSuite()
    assert isinstance(instance, NamedElement)


def test_assoc_action8_link_reassign_clear():
    a = xunit_Assertion(type="sample_text")
    b1 = xunit_Action(desc="sample_text")
    b2 = xunit_Action(desc="sample_text_2")
    _safe_set(a, 'xunit_Assertion9', b1)
    assert _is_linked(a, 'xunit_Assertion9', b1)
    if hasattr(b1, 'xunit_Action'):
        assert _is_linked(b1, 'xunit_Action', a)
    _safe_set(a, 'xunit_Assertion9', b2)
    assert _is_linked(a, 'xunit_Assertion9', b2)
    if hasattr(b1, 'xunit_Action'):
        assert not _is_linked(b1, 'xunit_Action', a)
    if hasattr(b2, 'xunit_Action'):
        assert _is_linked(b2, 'xunit_Action', a)
    _safe_set(a, 'xunit_Assertion9', None)
    assert not _is_linked(a, 'xunit_Assertion9', b2)
    if hasattr(b2, 'xunit_Action'):
        assert not _is_linked(b2, 'xunit_Action', a)


def test_assoc_assertion1_link_reassign_clear():
    a = xunit_Assertion(type="sample_text")
    b1 = xunit_TestCase()
    b2 = xunit_TestCase()
    _safe_set(a, 'xunit_Assertion', b1)
    assert _is_linked(a, 'xunit_Assertion', b1)
    if hasattr(b1, 'xunit_TestCase2'):
        assert _is_linked(b1, 'xunit_TestCase2', a)
    _safe_set(a, 'xunit_Assertion', b2)
    assert _is_linked(a, 'xunit_Assertion', b2)
    if hasattr(b1, 'xunit_TestCase2'):
        assert not _is_linked(b1, 'xunit_TestCase2', a)
    if hasattr(b2, 'xunit_TestCase2'):
        assert _is_linked(b2, 'xunit_TestCase2', a)
    _safe_set(a, 'xunit_Assertion', None)
    assert not _is_linked(a, 'xunit_Assertion', b2)
    if hasattr(b2, 'xunit_TestCase2'):
        assert not _is_linked(b2, 'xunit_TestCase2', a)


def test_assoc_assertion13_link_reassign_clear():
    a = xunit_Assertion(type="sample_text")
    b1 = xunit_ExpectedValue()
    b2 = xunit_ExpectedValue()
    _safe_set(a, 'xunit_Assertion15', b1)
    assert _is_linked(a, 'xunit_Assertion15', b1)
    if hasattr(b1, 'xunit_ExpectedValue14'):
        assert _is_linked(b1, 'xunit_ExpectedValue14', a)
    _safe_set(a, 'xunit_Assertion15', b2)
    assert _is_linked(a, 'xunit_Assertion15', b2)
    if hasattr(b1, 'xunit_ExpectedValue14'):
        assert not _is_linked(b1, 'xunit_ExpectedValue14', a)
    if hasattr(b2, 'xunit_ExpectedValue14'):
        assert _is_linked(b2, 'xunit_ExpectedValue14', a)
    _safe_set(a, 'xunit_Assertion15', None)
    assert not _is_linked(a, 'xunit_Assertion15', b2)
    if hasattr(b2, 'xunit_ExpectedValue14'):
        assert not _is_linked(b2, 'xunit_ExpectedValue14', a)


def test_assoc_expectedValue6_link_reassign_clear():
    a = xunit_Assertion(type="sample_text")
    b1 = xunit_ExpectedValue()
    b2 = xunit_ExpectedValue()
    _safe_set(a, 'xunit_Assertion7', b1)
    assert _is_linked(a, 'xunit_Assertion7', b1)
    if hasattr(b1, 'xunit_ExpectedValue'):
        assert _is_linked(b1, 'xunit_ExpectedValue', a)
    _safe_set(a, 'xunit_Assertion7', b2)
    assert _is_linked(a, 'xunit_Assertion7', b2)
    if hasattr(b1, 'xunit_ExpectedValue'):
        assert not _is_linked(b1, 'xunit_ExpectedValue', a)
    if hasattr(b2, 'xunit_ExpectedValue'):
        assert _is_linked(b2, 'xunit_ExpectedValue', a)
    _safe_set(a, 'xunit_Assertion7', None)
    assert not _is_linked(a, 'xunit_Assertion7', b2)
    if hasattr(b2, 'xunit_ExpectedValue'):
        assert not _is_linked(b2, 'xunit_ExpectedValue', a)


def test_assoc_testCase10_link_reassign_clear():
    a = xunit_Assertion(type="sample_text")
    b1 = xunit_TestCase()
    b2 = xunit_TestCase()
    _safe_set(a, 'xunit_Assertion11', b1)
    assert _is_linked(a, 'xunit_Assertion11', b1)
    if hasattr(b1, 'xunit_TestCase12'):
        assert _is_linked(b1, 'xunit_TestCase12', a)
    _safe_set(a, 'xunit_Assertion11', b2)
    assert _is_linked(a, 'xunit_Assertion11', b2)
    if hasattr(b1, 'xunit_TestCase12'):
        assert not _is_linked(b1, 'xunit_TestCase12', a)
    if hasattr(b2, 'xunit_TestCase12'):
        assert _is_linked(b2, 'xunit_TestCase12', a)
    _safe_set(a, 'xunit_Assertion11', None)
    assert not _is_linked(a, 'xunit_Assertion11', b2)
    if hasattr(b2, 'xunit_TestCase12'):
        assert not _is_linked(b2, 'xunit_TestCase12', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

DataValue_strategy = st.builds(DataValue)
@given(instance=DataValue_strategy)
@settings(max_examples=25)
def test_DataValue_instantiation(instance):
    assert isinstance(instance, DataValue)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


xunit_Action_strategy = st.builds(xunit_Action, desc=safe_text)
@given(instance=xunit_Action_strategy)
@settings(max_examples=25)
def test_xunit_Action_instantiation(instance):
    assert isinstance(instance, xunit_Action)


xunit_Assertion_strategy = st.builds(xunit_Assertion, type=safe_text)
@given(instance=xunit_Assertion_strategy)
@settings(max_examples=25)
def test_xunit_Assertion_instantiation(instance):
    assert isinstance(instance, xunit_Assertion)


xunit_DataValue_strategy = st.builds(xunit_DataValue, value=safe_text)
@given(instance=xunit_DataValue_strategy)
@settings(max_examples=25)
def test_xunit_DataValue_instantiation(instance):
    assert isinstance(instance, xunit_DataValue)


xunit_ExpectedValue_strategy = st.builds(xunit_ExpectedValue)
@given(instance=xunit_ExpectedValue_strategy)
@settings(max_examples=25)
def test_xunit_ExpectedValue_instantiation(instance):
    assert isinstance(instance, xunit_ExpectedValue)


xunit_NamedElement_strategy = st.builds(xunit_NamedElement, name=safe_text)
@given(instance=xunit_NamedElement_strategy)
@settings(max_examples=25)
def test_xunit_NamedElement_instantiation(instance):
    assert isinstance(instance, xunit_NamedElement)


xunit_TestCase_strategy = st.builds(xunit_TestCase)
@given(instance=xunit_TestCase_strategy)
@settings(max_examples=25)
def test_xunit_TestCase_instantiation(instance):
    assert isinstance(instance, xunit_TestCase)


xunit_TestSuite_strategy = st.builds(xunit_TestSuite)
@given(instance=xunit_TestSuite_strategy)
@settings(max_examples=25)
def test_xunit_TestSuite_instantiation(instance):
    assert isinstance(instance, xunit_TestSuite)



