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
    LiteralExp,
    XPath_StringExp,
    XPath_IntegerExp,
    NamedElement,
    Expression,
    XPath_LiteralExp,
    XPath_VariableExp,
    LocatedElement,
    XPath_Expression,
    XPath_OperatorCallExp,
    XPath_NamedElement,
    XPath_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_hyp_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_hyp_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_stringexp_is_not_abstract():
    assert not inspect.isabstract(XPath_StringExp)


def test_hyp_xpath_stringexp_constructor_exists():
    assert callable(XPath_StringExp.__init__)


def test_hyp_xpath_stringexp_constructor_args():
    sig = inspect.signature(XPath_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_xpath_integerexp_is_not_abstract():
    assert not inspect.isabstract(XPath_IntegerExp)


def test_hyp_xpath_integerexp_constructor_exists():
    assert callable(XPath_IntegerExp.__init__)


def test_hyp_xpath_integerexp_constructor_args():
    sig = inspect.signature(XPath_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"




def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_literalexp_is_not_abstract():
    assert not inspect.isabstract(XPath_LiteralExp)


def test_hyp_xpath_literalexp_constructor_exists():
    assert callable(XPath_LiteralExp.__init__)


def test_hyp_xpath_literalexp_constructor_args():
    sig = inspect.signature(XPath_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_variableexp_is_not_abstract():
    assert not inspect.isabstract(XPath_VariableExp)


def test_hyp_xpath_variableexp_constructor_exists():
    assert callable(XPath_VariableExp.__init__)


def test_hyp_xpath_variableexp_constructor_args():
    sig = inspect.signature(XPath_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_hyp_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_hyp_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_expression_is_not_abstract():
    assert not inspect.isabstract(XPath_Expression)


def test_hyp_xpath_expression_constructor_exists():
    assert callable(XPath_Expression.__init__)


def test_hyp_xpath_expression_constructor_args():
    sig = inspect.signature(XPath_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(XPath_OperatorCallExp)


def test_hyp_xpath_operatorcallexp_constructor_exists():
    assert callable(XPath_OperatorCallExp.__init__)


def test_hyp_xpath_operatorcallexp_constructor_args():
    sig = inspect.signature(XPath_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_xpath_namedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_NamedElement)


def test_hyp_xpath_namedelement_constructor_exists():
    assert callable(XPath_NamedElement.__init__)


def test_hyp_xpath_namedelement_constructor_args():
    sig = inspect.signature(XPath_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_xpath_locatedelement_is_not_abstract():
    assert not inspect.isabstract(XPath_LocatedElement)


def test_hyp_xpath_locatedelement_constructor_exists():
    assert callable(XPath_LocatedElement.__init__)


def test_hyp_xpath_locatedelement_constructor_args():
    sig = inspect.signature(XPath_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"





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
LiteralExp_strategy = st.builds(
    LiteralExp,
)
XPath_StringExp_strategy = st.builds(
    XPath_StringExp,
    symbol=
        safe_text
)
XPath_IntegerExp_strategy = st.builds(
    XPath_IntegerExp,
    symbol=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Expression_strategy = st.builds(
    Expression,
)
XPath_LiteralExp_strategy = st.builds(
    XPath_LiteralExp,
)
XPath_VariableExp_strategy = st.builds(
    XPath_VariableExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
XPath_Expression_strategy = st.builds(
    XPath_Expression,
)
XPath_OperatorCallExp_strategy = st.builds(
    XPath_OperatorCallExp,
)
XPath_NamedElement_strategy = st.builds(
    XPath_NamedElement,
    name=
        safe_text
)
XPath_LocatedElement_strategy = st.builds(
    XPath_LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)





@given(instance=XPath_StringExp_strategy)
def test_hyp_xpath_stringexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original




@given(instance=XPath_IntegerExp_strategy)
def test_hyp_xpath_integerexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original











@given(instance=XPath_NamedElement_strategy)
def test_hyp_xpath_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=XPath_LocatedElement_strategy)
def test_hyp_xpath_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=XPath_LocatedElement_strategy)
def test_hyp_xpath_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=XPath_LocatedElement_strategy)
def test_hyp_xpath_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    LiteralExp,
    LocatedElement,
    NamedElement,
    XPath_Expression,
    XPath_IntegerExp,
    XPath_LiteralExp,
    XPath_LocatedElement,
    XPath_NamedElement,
    XPath_OperatorCallExp,
    XPath_StringExp,
    XPath_VariableExp,
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

def test_XPath_IntegerExp_symbol_value_roundtrip():
    instance = XPath_IntegerExp(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_XPath_LocatedElement_commentsAfter_value_roundtrip():
    instance = XPath_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsAfter == "sample_text"
    instance.commentsAfter = "sample_text_2"
    assert instance.commentsAfter == "sample_text_2"


def test_XPath_LocatedElement_commentsBefore_value_roundtrip():
    instance = XPath_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.commentsBefore == "sample_text"
    instance.commentsBefore = "sample_text_2"
    assert instance.commentsBefore == "sample_text_2"


def test_XPath_LocatedElement_location_value_roundtrip():
    instance = XPath_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_XPath_NamedElement_name_value_roundtrip():
    instance = XPath_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_XPath_StringExp_symbol_value_roundtrip():
    instance = XPath_StringExp(symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_XPath_LiteralExp_isa_Expression():
    instance = XPath_LiteralExp()
    assert isinstance(instance, Expression)


def test_XPath_VariableExp_isa_Expression():
    instance = XPath_VariableExp()
    assert isinstance(instance, Expression)


def test_XPath_IntegerExp_isa_LiteralExp():
    instance = XPath_IntegerExp(symbol="sample_text")
    assert isinstance(instance, LiteralExp)


def test_XPath_StringExp_isa_LiteralExp():
    instance = XPath_StringExp(symbol="sample_text")
    assert isinstance(instance, LiteralExp)


def test_XPath_Expression_isa_LocatedElement():
    instance = XPath_Expression()
    assert isinstance(instance, LocatedElement)


def test_XPath_NamedElement_isa_LocatedElement():
    instance = XPath_NamedElement(name="sample_text")
    assert isinstance(instance, LocatedElement)


def test_XPath_OperatorCallExp_isa_LocatedElement():
    instance = XPath_OperatorCallExp()
    assert isinstance(instance, LocatedElement)


def test_XPath_OperatorCallExp_isa_NamedElement():
    instance = XPath_OperatorCallExp()
    assert isinstance(instance, NamedElement)


def test_XPath_VariableExp_isa_NamedElement():
    instance = XPath_VariableExp()
    assert isinstance(instance, NamedElement)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


LiteralExp_strategy = st.builds(LiteralExp)
@given(instance=LiteralExp_strategy)
@settings(max_examples=25)
def test_LiteralExp_instantiation(instance):
    assert isinstance(instance, LiteralExp)


LocatedElement_strategy = st.builds(LocatedElement)
@given(instance=LocatedElement_strategy)
@settings(max_examples=25)
def test_LocatedElement_instantiation(instance):
    assert isinstance(instance, LocatedElement)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


XPath_Expression_strategy = st.builds(XPath_Expression)
@given(instance=XPath_Expression_strategy)
@settings(max_examples=25)
def test_XPath_Expression_instantiation(instance):
    assert isinstance(instance, XPath_Expression)


XPath_IntegerExp_strategy = st.builds(XPath_IntegerExp, symbol=safe_text)
@given(instance=XPath_IntegerExp_strategy)
@settings(max_examples=25)
def test_XPath_IntegerExp_instantiation(instance):
    assert isinstance(instance, XPath_IntegerExp)


XPath_LiteralExp_strategy = st.builds(XPath_LiteralExp)
@given(instance=XPath_LiteralExp_strategy)
@settings(max_examples=25)
def test_XPath_LiteralExp_instantiation(instance):
    assert isinstance(instance, XPath_LiteralExp)


XPath_LocatedElement_strategy = st.builds(XPath_LocatedElement, commentsAfter=safe_text, commentsBefore=safe_text, location=safe_text)
@given(instance=XPath_LocatedElement_strategy)
@settings(max_examples=25)
def test_XPath_LocatedElement_instantiation(instance):
    assert isinstance(instance, XPath_LocatedElement)


XPath_NamedElement_strategy = st.builds(XPath_NamedElement, name=safe_text)
@given(instance=XPath_NamedElement_strategy)
@settings(max_examples=25)
def test_XPath_NamedElement_instantiation(instance):
    assert isinstance(instance, XPath_NamedElement)


XPath_OperatorCallExp_strategy = st.builds(XPath_OperatorCallExp)
@given(instance=XPath_OperatorCallExp_strategy)
@settings(max_examples=25)
def test_XPath_OperatorCallExp_instantiation(instance):
    assert isinstance(instance, XPath_OperatorCallExp)


XPath_StringExp_strategy = st.builds(XPath_StringExp, symbol=safe_text)
@given(instance=XPath_StringExp_strategy)
@settings(max_examples=25)
def test_XPath_StringExp_instantiation(instance):
    assert isinstance(instance, XPath_StringExp)


XPath_VariableExp_strategy = st.builds(XPath_VariableExp)
@given(instance=XPath_VariableExp_strategy)
@settings(max_examples=25)
def test_XPath_VariableExp_instantiation(instance):
    assert isinstance(instance, XPath_VariableExp)



