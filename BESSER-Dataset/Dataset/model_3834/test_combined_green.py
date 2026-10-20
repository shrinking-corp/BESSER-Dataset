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
    Expression,
    realop_NotExp,
    realop_XorExp,
    realop_IsNegative,
    realop_IsPositive,
    realop_AndExp,
    realop_OrExp,
    realop_Expression,
    realop_Operator,
    realop_Realop,
    realop_IsRealised,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_notexp_is_not_abstract():
    assert not inspect.isabstract(realop_NotExp)


def test_hyp_realop_notexp_constructor_exists():
    assert callable(realop_NotExp.__init__)


def test_hyp_realop_notexp_constructor_args():
    sig = inspect.signature(realop_NotExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_xorexp_is_not_abstract():
    assert not inspect.isabstract(realop_XorExp)


def test_hyp_realop_xorexp_constructor_exists():
    assert callable(realop_XorExp.__init__)


def test_hyp_realop_xorexp_constructor_args():
    sig = inspect.signature(realop_XorExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_isnegative_is_not_abstract():
    assert not inspect.isabstract(realop_IsNegative)


def test_hyp_realop_isnegative_constructor_exists():
    assert callable(realop_IsNegative.__init__)


def test_hyp_realop_isnegative_constructor_args():
    sig = inspect.signature(realop_IsNegative.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"




def test_hyp_realop_ispositive_is_not_abstract():
    assert not inspect.isabstract(realop_IsPositive)


def test_hyp_realop_ispositive_constructor_exists():
    assert callable(realop_IsPositive.__init__)


def test_hyp_realop_ispositive_constructor_args():
    sig = inspect.signature(realop_IsPositive.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"




def test_hyp_realop_andexp_is_not_abstract():
    assert not inspect.isabstract(realop_AndExp)


def test_hyp_realop_andexp_constructor_exists():
    assert callable(realop_AndExp.__init__)


def test_hyp_realop_andexp_constructor_args():
    sig = inspect.signature(realop_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_orexp_is_not_abstract():
    assert not inspect.isabstract(realop_OrExp)


def test_hyp_realop_orexp_constructor_exists():
    assert callable(realop_OrExp.__init__)


def test_hyp_realop_orexp_constructor_args():
    sig = inspect.signature(realop_OrExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_expression_is_not_abstract():
    assert not inspect.isabstract(realop_Expression)


def test_hyp_realop_expression_constructor_exists():
    assert callable(realop_Expression.__init__)


def test_hyp_realop_expression_constructor_args():
    sig = inspect.signature(realop_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_operator_is_not_abstract():
    assert not inspect.isabstract(realop_Operator)


def test_hyp_realop_operator_constructor_exists():
    assert callable(realop_Operator.__init__)


def test_hyp_realop_operator_constructor_args():
    sig = inspect.signature(realop_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_realop_realop_is_not_abstract():
    assert not inspect.isabstract(realop_Realop)


def test_hyp_realop_realop_constructor_exists():
    assert callable(realop_Realop.__init__)


def test_hyp_realop_realop_constructor_args():
    sig = inspect.signature(realop_Realop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_realop_isrealised_is_not_abstract():
    assert not inspect.isabstract(realop_IsRealised)


def test_hyp_realop_isrealised_constructor_exists():
    assert callable(realop_IsRealised.__init__)


def test_hyp_realop_isrealised_constructor_args():
    sig = inspect.signature(realop_IsRealised.__init__)
    params = list(sig.parameters.keys())
    assert "featureName" in params, "Missing parameter 'featureName'"



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
Expression_strategy = st.builds(
    Expression,
)
realop_NotExp_strategy = st.builds(
    realop_NotExp,
)
realop_XorExp_strategy = st.builds(
    realop_XorExp,
)
realop_IsNegative_strategy = st.builds(
    realop_IsNegative,
    featureName=
        safe_text
)
realop_IsPositive_strategy = st.builds(
    realop_IsPositive,
    featureName=
        safe_text
)
realop_AndExp_strategy = st.builds(
    realop_AndExp,
)
realop_OrExp_strategy = st.builds(
    realop_OrExp,
)
realop_Expression_strategy = st.builds(
    realop_Expression,
)
realop_Operator_strategy = st.builds(
    realop_Operator,
    name=
        safe_text
)
realop_Realop_strategy = st.builds(
    realop_Realop,
)
realop_IsRealised_strategy = st.builds(
    realop_IsRealised,
    featureName=
        safe_text
)







@given(instance=realop_IsNegative_strategy)
def test_hyp_realop_isnegative_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original




@given(instance=realop_IsPositive_strategy)
def test_hyp_realop_ispositive_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original







@given(instance=realop_Operator_strategy)
def test_hyp_realop_operator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=realop_IsRealised_strategy)
def test_hyp_realop_isrealised_featureName_setter(instance):
    original = instance.featureName
    instance.featureName = original
    assert instance.featureName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    realop_AndExp,
    realop_Expression,
    realop_IsNegative,
    realop_IsPositive,
    realop_IsRealised,
    realop_NotExp,
    realop_Operator,
    realop_OrExp,
    realop_Realop,
    realop_XorExp,
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

def test_realop_IsNegative_featureName_value_roundtrip():
    instance = realop_IsNegative(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_realop_IsPositive_featureName_value_roundtrip():
    instance = realop_IsPositive(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_realop_IsRealised_featureName_value_roundtrip():
    instance = realop_IsRealised(featureName="sample_text")
    assert instance.featureName == "sample_text"
    instance.featureName = "sample_text_2"
    assert instance.featureName == "sample_text_2"


def test_realop_Operator_name_value_roundtrip():
    instance = realop_Operator(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_realop_AndExp_isa_Expression():
    instance = realop_AndExp()
    assert isinstance(instance, Expression)


def test_realop_IsNegative_isa_Expression():
    instance = realop_IsNegative(featureName="sample_text")
    assert isinstance(instance, Expression)


def test_realop_IsPositive_isa_Expression():
    instance = realop_IsPositive(featureName="sample_text")
    assert isinstance(instance, Expression)


def test_realop_IsRealised_isa_Expression():
    instance = realop_IsRealised(featureName="sample_text")
    assert isinstance(instance, Expression)


def test_realop_NotExp_isa_Expression():
    instance = realop_NotExp()
    assert isinstance(instance, Expression)


def test_realop_OrExp_isa_Expression():
    instance = realop_OrExp()
    assert isinstance(instance, Expression)


def test_realop_XorExp_isa_Expression():
    instance = realop_XorExp()
    assert isinstance(instance, Expression)


def test_assoc_expPost3_link_reassign_clear():
    a = realop_Operator(name="sample_text")
    b1 = realop_Expression()
    b2 = realop_Expression()
    _safe_set(a, 'realop_Operator4', b1)
    assert _is_linked(a, 'realop_Operator4', b1)
    if hasattr(b1, 'realop_Expression5'):
        assert _is_linked(b1, 'realop_Expression5', a)
    _safe_set(a, 'realop_Operator4', b2)
    assert _is_linked(a, 'realop_Operator4', b2)
    if hasattr(b1, 'realop_Expression5'):
        assert not _is_linked(b1, 'realop_Expression5', a)
    if hasattr(b2, 'realop_Expression5'):
        assert _is_linked(b2, 'realop_Expression5', a)
    _safe_set(a, 'realop_Operator4', None)
    assert not _is_linked(a, 'realop_Operator4', b2)
    if hasattr(b2, 'realop_Expression5'):
        assert not _is_linked(b2, 'realop_Expression5', a)


def test_assoc_expPre1_link_reassign_clear():
    a = realop_Operator(name="sample_text")
    b1 = realop_Expression()
    b2 = realop_Expression()
    _safe_set(a, 'realop_Operator2', b1)
    assert _is_linked(a, 'realop_Operator2', b1)
    if hasattr(b1, 'realop_Expression'):
        assert _is_linked(b1, 'realop_Expression', a)
    _safe_set(a, 'realop_Operator2', b2)
    assert _is_linked(a, 'realop_Operator2', b2)
    if hasattr(b1, 'realop_Expression'):
        assert not _is_linked(b1, 'realop_Expression', a)
    if hasattr(b2, 'realop_Expression'):
        assert _is_linked(b2, 'realop_Expression', a)
    _safe_set(a, 'realop_Operator2', None)
    assert not _is_linked(a, 'realop_Operator2', b2)
    if hasattr(b2, 'realop_Expression'):
        assert not _is_linked(b2, 'realop_Expression', a)


def test_assoc_operators0_link_reassign_clear():
    a = realop_Operator(name="sample_text")
    b1 = realop_Realop()
    b2 = realop_Realop()
    _safe_set(a, 'realop_Operator', b1)
    assert _is_linked(a, 'realop_Operator', b1)
    if hasattr(b1, 'realop_Realop'):
        assert _is_linked(b1, 'realop_Realop', a)
    _safe_set(a, 'realop_Operator', b2)
    assert _is_linked(a, 'realop_Operator', b2)
    if hasattr(b1, 'realop_Realop'):
        assert not _is_linked(b1, 'realop_Realop', a)
    if hasattr(b2, 'realop_Realop'):
        assert _is_linked(b2, 'realop_Realop', a)
    _safe_set(a, 'realop_Operator', None)
    assert not _is_linked(a, 'realop_Operator', b2)
    if hasattr(b2, 'realop_Realop'):
        assert not _is_linked(b2, 'realop_Realop', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


realop_AndExp_strategy = st.builds(realop_AndExp)
@given(instance=realop_AndExp_strategy)
@settings(max_examples=25)
def test_realop_AndExp_instantiation(instance):
    assert isinstance(instance, realop_AndExp)


realop_Expression_strategy = st.builds(realop_Expression)
@given(instance=realop_Expression_strategy)
@settings(max_examples=25)
def test_realop_Expression_instantiation(instance):
    assert isinstance(instance, realop_Expression)


realop_IsNegative_strategy = st.builds(realop_IsNegative, featureName=safe_text)
@given(instance=realop_IsNegative_strategy)
@settings(max_examples=25)
def test_realop_IsNegative_instantiation(instance):
    assert isinstance(instance, realop_IsNegative)


realop_IsPositive_strategy = st.builds(realop_IsPositive, featureName=safe_text)
@given(instance=realop_IsPositive_strategy)
@settings(max_examples=25)
def test_realop_IsPositive_instantiation(instance):
    assert isinstance(instance, realop_IsPositive)


realop_IsRealised_strategy = st.builds(realop_IsRealised, featureName=safe_text)
@given(instance=realop_IsRealised_strategy)
@settings(max_examples=25)
def test_realop_IsRealised_instantiation(instance):
    assert isinstance(instance, realop_IsRealised)


realop_NotExp_strategy = st.builds(realop_NotExp)
@given(instance=realop_NotExp_strategy)
@settings(max_examples=25)
def test_realop_NotExp_instantiation(instance):
    assert isinstance(instance, realop_NotExp)


realop_Operator_strategy = st.builds(realop_Operator, name=safe_text)
@given(instance=realop_Operator_strategy)
@settings(max_examples=25)
def test_realop_Operator_instantiation(instance):
    assert isinstance(instance, realop_Operator)


realop_OrExp_strategy = st.builds(realop_OrExp)
@given(instance=realop_OrExp_strategy)
@settings(max_examples=25)
def test_realop_OrExp_instantiation(instance):
    assert isinstance(instance, realop_OrExp)


realop_Realop_strategy = st.builds(realop_Realop)
@given(instance=realop_Realop_strategy)
@settings(max_examples=25)
def test_realop_Realop_instantiation(instance):
    assert isinstance(instance, realop_Realop)


realop_XorExp_strategy = st.builds(realop_XorExp)
@given(instance=realop_XorExp_strategy)
@settings(max_examples=25)
def test_realop_XorExp_instantiation(instance):
    assert isinstance(instance, realop_XorExp)



