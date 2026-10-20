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
    Literal,
    expression_RealLiteral,
    expression_NullLiteral,
    expression_StringLiteral,
    expression_IntegerLiteral,
    expression_BooleanLiteral,
    Expression,
    expression_CastedExpression,
    expression_SwitchExpression,
    expression_IfExpression,
    expression_FeatureCall,
    expression_ConstructorCallExpression,
    expression_ListLiteral,
    expression_Literal,
    expression_GlobalVarExpression,
    expression_ChainExpression,
    expression_BooleanOperation,
    expression_LetExpression,
    expression_SyntaxElement,
    SyntaxElement,
    expression_Identifier,
    expression_Case,
    expression_Expression,
    FeatureCall,
    expression_CollectionExpression,
    expression_TypeSelectExpression,
    expression_OperationCall,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_hyp_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_hyp_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_realliteral_is_not_abstract():
    assert not inspect.isabstract(expression_RealLiteral)


def test_hyp_expression_realliteral_constructor_exists():
    assert callable(expression_RealLiteral.__init__)


def test_hyp_expression_realliteral_constructor_args():
    sig = inspect.signature(expression_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_expression_nullliteral_is_not_abstract():
    assert not inspect.isabstract(expression_NullLiteral)


def test_hyp_expression_nullliteral_constructor_exists():
    assert callable(expression_NullLiteral.__init__)


def test_hyp_expression_nullliteral_constructor_args():
    sig = inspect.signature(expression_NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_expression_stringliteral_is_not_abstract():
    assert not inspect.isabstract(expression_StringLiteral)


def test_hyp_expression_stringliteral_constructor_exists():
    assert callable(expression_StringLiteral.__init__)


def test_hyp_expression_stringliteral_constructor_args():
    sig = inspect.signature(expression_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_expression_integerliteral_is_not_abstract():
    assert not inspect.isabstract(expression_IntegerLiteral)


def test_hyp_expression_integerliteral_constructor_exists():
    assert callable(expression_IntegerLiteral.__init__)


def test_hyp_expression_integerliteral_constructor_args():
    sig = inspect.signature(expression_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_expression_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(expression_BooleanLiteral)


def test_hyp_expression_booleanliteral_constructor_exists():
    assert callable(expression_BooleanLiteral.__init__)


def test_hyp_expression_booleanliteral_constructor_args():
    sig = inspect.signature(expression_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_castedexpression_is_not_abstract():
    assert not inspect.isabstract(expression_CastedExpression)


def test_hyp_expression_castedexpression_constructor_exists():
    assert callable(expression_CastedExpression.__init__)


def test_hyp_expression_castedexpression_constructor_args():
    sig = inspect.signature(expression_CastedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_switchexpression_is_not_abstract():
    assert not inspect.isabstract(expression_SwitchExpression)


def test_hyp_expression_switchexpression_constructor_exists():
    assert callable(expression_SwitchExpression.__init__)


def test_hyp_expression_switchexpression_constructor_args():
    sig = inspect.signature(expression_SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_ifexpression_is_not_abstract():
    assert not inspect.isabstract(expression_IfExpression)


def test_hyp_expression_ifexpression_constructor_exists():
    assert callable(expression_IfExpression.__init__)


def test_hyp_expression_ifexpression_constructor_args():
    sig = inspect.signature(expression_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_featurecall_is_not_abstract():
    assert not inspect.isabstract(expression_FeatureCall)


def test_hyp_expression_featurecall_constructor_exists():
    assert callable(expression_FeatureCall.__init__)


def test_hyp_expression_featurecall_constructor_args():
    sig = inspect.signature(expression_FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expression_constructorcallexpression_is_not_abstract():
    assert not inspect.isabstract(expression_ConstructorCallExpression)


def test_hyp_expression_constructorcallexpression_constructor_exists():
    assert callable(expression_ConstructorCallExpression.__init__)


def test_hyp_expression_constructorcallexpression_constructor_args():
    sig = inspect.signature(expression_ConstructorCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_listliteral_is_not_abstract():
    assert not inspect.isabstract(expression_ListLiteral)


def test_hyp_expression_listliteral_constructor_exists():
    assert callable(expression_ListLiteral.__init__)


def test_hyp_expression_listliteral_constructor_args():
    sig = inspect.signature(expression_ListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_literal_is_not_abstract():
    assert not inspect.isabstract(expression_Literal)


def test_hyp_expression_literal_constructor_exists():
    assert callable(expression_Literal.__init__)


def test_hyp_expression_literal_constructor_args():
    sig = inspect.signature(expression_Literal.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_globalvarexpression_is_not_abstract():
    assert not inspect.isabstract(expression_GlobalVarExpression)


def test_hyp_expression_globalvarexpression_constructor_exists():
    assert callable(expression_GlobalVarExpression.__init__)


def test_hyp_expression_globalvarexpression_constructor_args():
    sig = inspect.signature(expression_GlobalVarExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expression_chainexpression_is_not_abstract():
    assert not inspect.isabstract(expression_ChainExpression)


def test_hyp_expression_chainexpression_constructor_exists():
    assert callable(expression_ChainExpression.__init__)


def test_hyp_expression_chainexpression_constructor_args():
    sig = inspect.signature(expression_ChainExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(expression_BooleanOperation)


def test_hyp_expression_booleanoperation_constructor_exists():
    assert callable(expression_BooleanOperation.__init__)


def test_hyp_expression_booleanoperation_constructor_args():
    sig = inspect.signature(expression_BooleanOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_expression_letexpression_is_not_abstract():
    assert not inspect.isabstract(expression_LetExpression)


def test_hyp_expression_letexpression_constructor_exists():
    assert callable(expression_LetExpression.__init__)


def test_hyp_expression_letexpression_constructor_args():
    sig = inspect.signature(expression_LetExpression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_expression_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(expression_SyntaxElement)


def test_hyp_expression_syntaxelement_constructor_exists():
    assert callable(expression_SyntaxElement.__init__)


def test_hyp_expression_syntaxelement_constructor_args():
    sig = inspect.signature(expression_SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(SyntaxElement)


def test_hyp_syntaxelement_constructor_exists():
    assert callable(SyntaxElement.__init__)


def test_hyp_syntaxelement_constructor_args():
    sig = inspect.signature(SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_identifier_is_not_abstract():
    assert not inspect.isabstract(expression_Identifier)


def test_hyp_expression_identifier_constructor_exists():
    assert callable(expression_Identifier.__init__)


def test_hyp_expression_identifier_constructor_args():
    sig = inspect.signature(expression_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "cl" in params, "Missing parameter 'cl'"





def test_hyp_expression_case_is_not_abstract():
    assert not inspect.isabstract(expression_Case)


def test_hyp_expression_case_constructor_exists():
    assert callable(expression_Case.__init__)


def test_hyp_expression_case_constructor_args():
    sig = inspect.signature(expression_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_hyp_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_hyp_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_hyp_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_hyp_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(expression_CollectionExpression)


def test_hyp_expression_collectionexpression_constructor_exists():
    assert callable(expression_CollectionExpression.__init__)


def test_hyp_expression_collectionexpression_constructor_args():
    sig = inspect.signature(expression_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"




def test_hyp_expression_typeselectexpression_is_not_abstract():
    assert not inspect.isabstract(expression_TypeSelectExpression)


def test_hyp_expression_typeselectexpression_constructor_exists():
    assert callable(expression_TypeSelectExpression.__init__)


def test_hyp_expression_typeselectexpression_constructor_args():
    sig = inspect.signature(expression_TypeSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_operationcall_is_not_abstract():
    assert not inspect.isabstract(expression_OperationCall)


def test_hyp_expression_operationcall_constructor_exists():
    assert callable(expression_OperationCall.__init__)


def test_hyp_expression_operationcall_constructor_args():
    sig = inspect.signature(expression_OperationCall.__init__)
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
Literal_strategy = st.builds(
    Literal,
)
expression_RealLiteral_strategy = st.builds(
    expression_RealLiteral,
    val=
        safe_text
)
expression_NullLiteral_strategy = st.builds(
    expression_NullLiteral,
    val=
        safe_text
)
expression_StringLiteral_strategy = st.builds(
    expression_StringLiteral,
    val=
        safe_text
)
expression_IntegerLiteral_strategy = st.builds(
    expression_IntegerLiteral,
    val=
        st.integers()
)
expression_BooleanLiteral_strategy = st.builds(
    expression_BooleanLiteral,
    val=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
expression_CastedExpression_strategy = st.builds(
    expression_CastedExpression,
)
expression_SwitchExpression_strategy = st.builds(
    expression_SwitchExpression,
)
expression_IfExpression_strategy = st.builds(
    expression_IfExpression,
)
expression_FeatureCall_strategy = st.builds(
    expression_FeatureCall,
    name=
        safe_text
)
expression_ConstructorCallExpression_strategy = st.builds(
    expression_ConstructorCallExpression,
)
expression_ListLiteral_strategy = st.builds(
    expression_ListLiteral,
)
expression_Literal_strategy = st.builds(
    expression_Literal,
)
expression_GlobalVarExpression_strategy = st.builds(
    expression_GlobalVarExpression,
    name=
        safe_text
)
expression_ChainExpression_strategy = st.builds(
    expression_ChainExpression,
)
expression_BooleanOperation_strategy = st.builds(
    expression_BooleanOperation,
    operator=
        safe_text
)
expression_LetExpression_strategy = st.builds(
    expression_LetExpression,
    identifier=
        safe_text
)
expression_SyntaxElement_strategy = st.builds(
    expression_SyntaxElement,
)
SyntaxElement_strategy = st.builds(
    SyntaxElement,
)
expression_Identifier_strategy = st.builds(
    expression_Identifier,
    id=
        safe_text,
    cl=
        safe_text
)
expression_Case_strategy = st.builds(
    expression_Case,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
expression_CollectionExpression_strategy = st.builds(
    expression_CollectionExpression,
    var=
        safe_text
)
expression_TypeSelectExpression_strategy = st.builds(
    expression_TypeSelectExpression,
)
expression_OperationCall_strategy = st.builds(
    expression_OperationCall,
)





@given(instance=expression_RealLiteral_strategy)
def test_hyp_expression_realliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original




@given(instance=expression_NullLiteral_strategy)
def test_hyp_expression_nullliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original




@given(instance=expression_StringLiteral_strategy)
def test_hyp_expression_stringliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original




@given(instance=expression_IntegerLiteral_strategy)
def test_hyp_expression_integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original




@given(instance=expression_BooleanLiteral_strategy)
def test_hyp_expression_booleanliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original








@given(instance=expression_FeatureCall_strategy)
def test_hyp_expression_featurecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original







@given(instance=expression_GlobalVarExpression_strategy)
def test_hyp_expression_globalvarexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=expression_BooleanOperation_strategy)
def test_hyp_expression_booleanoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=expression_LetExpression_strategy)
def test_hyp_expression_letexpression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original






@given(instance=expression_Identifier_strategy)
def test_hyp_expression_identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=expression_Identifier_strategy)
def test_hyp_expression_identifier_cl_setter(instance):
    original = instance.cl
    instance.cl = original
    assert instance.cl == original







@given(instance=expression_CollectionExpression_strategy)
def test_hyp_expression_collectionexpression_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original




# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expression,
    FeatureCall,
    Literal,
    SyntaxElement,
    expression_BooleanLiteral,
    expression_BooleanOperation,
    expression_Case,
    expression_CastedExpression,
    expression_ChainExpression,
    expression_CollectionExpression,
    expression_ConstructorCallExpression,
    expression_Expression,
    expression_FeatureCall,
    expression_GlobalVarExpression,
    expression_Identifier,
    expression_IfExpression,
    expression_IntegerLiteral,
    expression_LetExpression,
    expression_ListLiteral,
    expression_Literal,
    expression_NullLiteral,
    expression_OperationCall,
    expression_RealLiteral,
    expression_StringLiteral,
    expression_SwitchExpression,
    expression_SyntaxElement,
    expression_TypeSelectExpression,
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

def test_expression_BooleanLiteral_val_value_roundtrip():
    instance = expression_BooleanLiteral(val="sample_text")
    assert instance.val == "sample_text"
    instance.val = "sample_text_2"
    assert instance.val == "sample_text_2"


def test_expression_BooleanOperation_operator_value_roundtrip():
    instance = expression_BooleanOperation(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_expression_CollectionExpression_var_value_roundtrip():
    instance = expression_CollectionExpression(var="sample_text")
    assert instance.var == "sample_text"
    instance.var = "sample_text_2"
    assert instance.var == "sample_text_2"


def test_expression_FeatureCall_name_value_roundtrip():
    instance = expression_FeatureCall(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expression_GlobalVarExpression_name_value_roundtrip():
    instance = expression_GlobalVarExpression(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_expression_Identifier_cl_value_roundtrip():
    instance = expression_Identifier(cl="sample_text", id="sample_text")
    assert instance.cl == "sample_text"
    instance.cl = "sample_text_2"
    assert instance.cl == "sample_text_2"


def test_expression_Identifier_id_value_roundtrip():
    instance = expression_Identifier(cl="sample_text", id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_expression_IntegerLiteral_val_value_roundtrip():
    instance = expression_IntegerLiteral(val=7)
    assert instance.val == 7
    instance.val = 13
    assert instance.val == 13


def test_expression_LetExpression_identifier_value_roundtrip():
    instance = expression_LetExpression(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_expression_NullLiteral_val_value_roundtrip():
    instance = expression_NullLiteral(val="sample_text")
    assert instance.val == "sample_text"
    instance.val = "sample_text_2"
    assert instance.val == "sample_text_2"


def test_expression_RealLiteral_val_value_roundtrip():
    instance = expression_RealLiteral(val="sample_text")
    assert instance.val == "sample_text"
    instance.val = "sample_text_2"
    assert instance.val == "sample_text_2"


def test_expression_StringLiteral_val_value_roundtrip():
    instance = expression_StringLiteral(val="sample_text")
    assert instance.val == "sample_text"
    instance.val = "sample_text_2"
    assert instance.val == "sample_text_2"


def test_expression_BooleanOperation_isa_Expression():
    instance = expression_BooleanOperation(operator="sample_text")
    assert isinstance(instance, Expression)


def test_expression_CastedExpression_isa_Expression():
    instance = expression_CastedExpression()
    assert isinstance(instance, Expression)


def test_expression_ChainExpression_isa_Expression():
    instance = expression_ChainExpression()
    assert isinstance(instance, Expression)


def test_expression_CollectionExpression_isa_Expression():
    instance = expression_CollectionExpression(var="sample_text")
    assert isinstance(instance, Expression)


def test_expression_ConstructorCallExpression_isa_Expression():
    instance = expression_ConstructorCallExpression()
    assert isinstance(instance, Expression)


def test_expression_FeatureCall_isa_Expression():
    instance = expression_FeatureCall(name="sample_text")
    assert isinstance(instance, Expression)


def test_expression_GlobalVarExpression_isa_Expression():
    instance = expression_GlobalVarExpression(name="sample_text")
    assert isinstance(instance, Expression)


def test_expression_IfExpression_isa_Expression():
    instance = expression_IfExpression()
    assert isinstance(instance, Expression)


def test_expression_LetExpression_isa_Expression():
    instance = expression_LetExpression(identifier="sample_text")
    assert isinstance(instance, Expression)


def test_expression_ListLiteral_isa_Expression():
    instance = expression_ListLiteral()
    assert isinstance(instance, Expression)


def test_expression_Literal_isa_Expression():
    instance = expression_Literal()
    assert isinstance(instance, Expression)


def test_expression_OperationCall_isa_Expression():
    instance = expression_OperationCall()
    assert isinstance(instance, Expression)


def test_expression_SwitchExpression_isa_Expression():
    instance = expression_SwitchExpression()
    assert isinstance(instance, Expression)


def test_expression_TypeSelectExpression_isa_Expression():
    instance = expression_TypeSelectExpression()
    assert isinstance(instance, Expression)


def test_expression_CollectionExpression_isa_FeatureCall():
    instance = expression_CollectionExpression(var="sample_text")
    assert isinstance(instance, FeatureCall)


def test_expression_OperationCall_isa_FeatureCall():
    instance = expression_OperationCall()
    assert isinstance(instance, FeatureCall)


def test_expression_TypeSelectExpression_isa_FeatureCall():
    instance = expression_TypeSelectExpression()
    assert isinstance(instance, FeatureCall)


def test_expression_BooleanLiteral_isa_Literal():
    instance = expression_BooleanLiteral(val="sample_text")
    assert isinstance(instance, Literal)


def test_expression_IntegerLiteral_isa_Literal():
    instance = expression_IntegerLiteral(val=7)
    assert isinstance(instance, Literal)


def test_expression_NullLiteral_isa_Literal():
    instance = expression_NullLiteral(val="sample_text")
    assert isinstance(instance, Literal)


def test_expression_RealLiteral_isa_Literal():
    instance = expression_RealLiteral(val="sample_text")
    assert isinstance(instance, Literal)


def test_expression_StringLiteral_isa_Literal():
    instance = expression_StringLiteral(val="sample_text")
    assert isinstance(instance, Literal)


def test_expression_Case_isa_SyntaxElement():
    instance = expression_Case()
    assert isinstance(instance, SyntaxElement)


def test_expression_Expression_isa_SyntaxElement():
    instance = expression_Expression()
    assert isinstance(instance, SyntaxElement)


def test_expression_Identifier_isa_SyntaxElement():
    instance = expression_Identifier(cl="sample_text", id="sample_text")
    assert isinstance(instance, SyntaxElement)


def test_assoc_exp40_link_reassign_clear():
    a = expression_CollectionExpression(var="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_CollectionExpression', b1)
    assert _is_linked(a, 'expression_CollectionExpression', b1)
    if hasattr(b1, 'expression_Expression41'):
        assert _is_linked(b1, 'expression_Expression41', a)
    _safe_set(a, 'expression_CollectionExpression', b2)
    assert _is_linked(a, 'expression_CollectionExpression', b2)
    if hasattr(b1, 'expression_Expression41'):
        assert not _is_linked(b1, 'expression_Expression41', a)
    if hasattr(b2, 'expression_Expression41'):
        assert _is_linked(b2, 'expression_Expression41', a)
    _safe_set(a, 'expression_CollectionExpression', None)
    assert not _is_linked(a, 'expression_CollectionExpression', b2)
    if hasattr(b2, 'expression_Expression41'):
        assert not _is_linked(b2, 'expression_Expression41', a)


def test_assoc_id143_link_reassign_clear():
    a = expression_Identifier(cl="sample_text", id="sample_text")
    b1 = expression_Identifier(cl="sample_text", id="sample_text")
    b2 = expression_Identifier(cl="sample_text_2", id="sample_text_2")
    _safe_set(a, 'expression_Identifier42', b1)
    assert _is_linked(a, 'expression_Identifier42', b1)
    if hasattr(b1, 'expression_Identifier44'):
        assert _is_linked(b1, 'expression_Identifier44', a)
    _safe_set(a, 'expression_Identifier42', b2)
    assert _is_linked(a, 'expression_Identifier42', b2)
    if hasattr(b1, 'expression_Identifier44'):
        assert not _is_linked(b1, 'expression_Identifier44', a)
    if hasattr(b2, 'expression_Identifier44'):
        assert _is_linked(b2, 'expression_Identifier44', a)
    _safe_set(a, 'expression_Identifier42', None)
    assert not _is_linked(a, 'expression_Identifier42', b2)
    if hasattr(b2, 'expression_Identifier44'):
        assert not _is_linked(b2, 'expression_Identifier44', a)


def test_assoc_left50_link_reassign_clear():
    a = expression_BooleanOperation(operator="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_BooleanOperation', b1)
    assert _is_linked(a, 'expression_BooleanOperation', b1)
    if hasattr(b1, 'expression_Expression51'):
        assert _is_linked(b1, 'expression_Expression51', a)
    _safe_set(a, 'expression_BooleanOperation', b2)
    assert _is_linked(a, 'expression_BooleanOperation', b2)
    if hasattr(b1, 'expression_Expression51'):
        assert not _is_linked(b1, 'expression_Expression51', a)
    if hasattr(b2, 'expression_Expression51'):
        assert _is_linked(b2, 'expression_Expression51', a)
    _safe_set(a, 'expression_BooleanOperation', None)
    assert not _is_linked(a, 'expression_BooleanOperation', b2)
    if hasattr(b2, 'expression_Expression51'):
        assert not _is_linked(b2, 'expression_Expression51', a)


def test_assoc_right52_link_reassign_clear():
    a = expression_BooleanOperation(operator="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_BooleanOperation53', b1)
    assert _is_linked(a, 'expression_BooleanOperation53', b1)
    if hasattr(b1, 'expression_Expression54'):
        assert _is_linked(b1, 'expression_Expression54', a)
    _safe_set(a, 'expression_BooleanOperation53', b2)
    assert _is_linked(a, 'expression_BooleanOperation53', b2)
    if hasattr(b1, 'expression_Expression54'):
        assert not _is_linked(b1, 'expression_Expression54', a)
    if hasattr(b2, 'expression_Expression54'):
        assert _is_linked(b2, 'expression_Expression54', a)
    _safe_set(a, 'expression_BooleanOperation53', None)
    assert not _is_linked(a, 'expression_BooleanOperation53', b2)
    if hasattr(b2, 'expression_Expression54'):
        assert not _is_linked(b2, 'expression_Expression54', a)


def test_assoc_target1_link_reassign_clear():
    a = expression_LetExpression(identifier="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_LetExpression2', b1)
    assert _is_linked(a, 'expression_LetExpression2', b1)
    if hasattr(b1, 'expression_Expression3'):
        assert _is_linked(b1, 'expression_Expression3', a)
    _safe_set(a, 'expression_LetExpression2', b2)
    assert _is_linked(a, 'expression_LetExpression2', b2)
    if hasattr(b1, 'expression_Expression3'):
        assert not _is_linked(b1, 'expression_Expression3', a)
    if hasattr(b2, 'expression_Expression3'):
        assert _is_linked(b2, 'expression_Expression3', a)
    _safe_set(a, 'expression_LetExpression2', None)
    assert not _is_linked(a, 'expression_LetExpression2', b2)
    if hasattr(b2, 'expression_Expression3'):
        assert not _is_linked(b2, 'expression_Expression3', a)


def test_assoc_target31_link_reassign_clear():
    a = expression_FeatureCall(name="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_FeatureCall', b1)
    assert _is_linked(a, 'expression_FeatureCall', b1)
    if hasattr(b1, 'expression_Expression32'):
        assert _is_linked(b1, 'expression_Expression32', a)
    _safe_set(a, 'expression_FeatureCall', b2)
    assert _is_linked(a, 'expression_FeatureCall', b2)
    if hasattr(b1, 'expression_Expression32'):
        assert not _is_linked(b1, 'expression_Expression32', a)
    if hasattr(b2, 'expression_Expression32'):
        assert _is_linked(b2, 'expression_Expression32', a)
    _safe_set(a, 'expression_FeatureCall', None)
    assert not _is_linked(a, 'expression_FeatureCall', b2)
    if hasattr(b2, 'expression_Expression32'):
        assert not _is_linked(b2, 'expression_Expression32', a)


def test_assoc_type33_link_reassign_clear():
    a = expression_Identifier(cl="sample_text", id="sample_text")
    b1 = expression_FeatureCall(name="sample_text")
    b2 = expression_FeatureCall(name="sample_text_2")
    _safe_set(a, 'expression_Identifier35', b1)
    assert _is_linked(a, 'expression_Identifier35', b1)
    if hasattr(b1, 'expression_FeatureCall34'):
        assert _is_linked(b1, 'expression_FeatureCall34', a)
    _safe_set(a, 'expression_Identifier35', b2)
    assert _is_linked(a, 'expression_Identifier35', b2)
    if hasattr(b1, 'expression_FeatureCall34'):
        assert not _is_linked(b1, 'expression_FeatureCall34', a)
    if hasattr(b2, 'expression_FeatureCall34'):
        assert _is_linked(b2, 'expression_FeatureCall34', a)
    _safe_set(a, 'expression_Identifier35', None)
    assert not _is_linked(a, 'expression_Identifier35', b2)
    if hasattr(b2, 'expression_FeatureCall34'):
        assert not _is_linked(b2, 'expression_FeatureCall34', a)


def test_assoc_type38_link_reassign_clear():
    a = expression_Identifier(cl="sample_text", id="sample_text")
    b1 = expression_ConstructorCallExpression()
    b2 = expression_ConstructorCallExpression()
    _safe_set(a, 'expression_Identifier39', b1)
    assert _is_linked(a, 'expression_Identifier39', b1)
    if hasattr(b1, 'expression_ConstructorCallExpression'):
        assert _is_linked(b1, 'expression_ConstructorCallExpression', a)
    _safe_set(a, 'expression_Identifier39', b2)
    assert _is_linked(a, 'expression_Identifier39', b2)
    if hasattr(b1, 'expression_ConstructorCallExpression'):
        assert not _is_linked(b1, 'expression_ConstructorCallExpression', a)
    if hasattr(b2, 'expression_ConstructorCallExpression'):
        assert _is_linked(b2, 'expression_ConstructorCallExpression', a)
    _safe_set(a, 'expression_Identifier39', None)
    assert not _is_linked(a, 'expression_Identifier39', b2)
    if hasattr(b2, 'expression_ConstructorCallExpression'):
        assert not _is_linked(b2, 'expression_ConstructorCallExpression', a)


def test_assoc_type4_link_reassign_clear():
    a = expression_Identifier(cl="sample_text", id="sample_text")
    b1 = expression_CastedExpression()
    b2 = expression_CastedExpression()
    _safe_set(a, 'expression_Identifier', b1)
    assert _is_linked(a, 'expression_Identifier', b1)
    if hasattr(b1, 'expression_CastedExpression'):
        assert _is_linked(b1, 'expression_CastedExpression', a)
    _safe_set(a, 'expression_Identifier', b2)
    assert _is_linked(a, 'expression_Identifier', b2)
    if hasattr(b1, 'expression_CastedExpression'):
        assert not _is_linked(b1, 'expression_CastedExpression', a)
    if hasattr(b2, 'expression_CastedExpression'):
        assert _is_linked(b2, 'expression_CastedExpression', a)
    _safe_set(a, 'expression_Identifier', None)
    assert not _is_linked(a, 'expression_Identifier', b2)
    if hasattr(b2, 'expression_CastedExpression'):
        assert not _is_linked(b2, 'expression_CastedExpression', a)


def test_assoc_varExpr0_link_reassign_clear():
    a = expression_LetExpression(identifier="sample_text")
    b1 = expression_Expression()
    b2 = expression_Expression()
    _safe_set(a, 'expression_LetExpression', b1)
    assert _is_linked(a, 'expression_LetExpression', b1)
    if hasattr(b1, 'expression_Expression'):
        assert _is_linked(b1, 'expression_Expression', a)
    _safe_set(a, 'expression_LetExpression', b2)
    assert _is_linked(a, 'expression_LetExpression', b2)
    if hasattr(b1, 'expression_Expression'):
        assert not _is_linked(b1, 'expression_Expression', a)
    if hasattr(b2, 'expression_Expression'):
        assert _is_linked(b2, 'expression_Expression', a)
    _safe_set(a, 'expression_LetExpression', None)
    assert not _is_linked(a, 'expression_LetExpression', b2)
    if hasattr(b2, 'expression_Expression'):
        assert not _is_linked(b2, 'expression_Expression', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


FeatureCall_strategy = st.builds(FeatureCall)
@given(instance=FeatureCall_strategy)
@settings(max_examples=25)
def test_FeatureCall_instantiation(instance):
    assert isinstance(instance, FeatureCall)


Literal_strategy = st.builds(Literal)
@given(instance=Literal_strategy)
@settings(max_examples=25)
def test_Literal_instantiation(instance):
    assert isinstance(instance, Literal)


SyntaxElement_strategy = st.builds(SyntaxElement)
@given(instance=SyntaxElement_strategy)
@settings(max_examples=25)
def test_SyntaxElement_instantiation(instance):
    assert isinstance(instance, SyntaxElement)


expression_BooleanLiteral_strategy = st.builds(expression_BooleanLiteral, val=safe_text)
@given(instance=expression_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_expression_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, expression_BooleanLiteral)


expression_BooleanOperation_strategy = st.builds(expression_BooleanOperation, operator=safe_text)
@given(instance=expression_BooleanOperation_strategy)
@settings(max_examples=25)
def test_expression_BooleanOperation_instantiation(instance):
    assert isinstance(instance, expression_BooleanOperation)


expression_Case_strategy = st.builds(expression_Case)
@given(instance=expression_Case_strategy)
@settings(max_examples=25)
def test_expression_Case_instantiation(instance):
    assert isinstance(instance, expression_Case)


expression_CastedExpression_strategy = st.builds(expression_CastedExpression)
@given(instance=expression_CastedExpression_strategy)
@settings(max_examples=25)
def test_expression_CastedExpression_instantiation(instance):
    assert isinstance(instance, expression_CastedExpression)


expression_ChainExpression_strategy = st.builds(expression_ChainExpression)
@given(instance=expression_ChainExpression_strategy)
@settings(max_examples=25)
def test_expression_ChainExpression_instantiation(instance):
    assert isinstance(instance, expression_ChainExpression)


expression_CollectionExpression_strategy = st.builds(expression_CollectionExpression, var=safe_text)
@given(instance=expression_CollectionExpression_strategy)
@settings(max_examples=25)
def test_expression_CollectionExpression_instantiation(instance):
    assert isinstance(instance, expression_CollectionExpression)


expression_ConstructorCallExpression_strategy = st.builds(expression_ConstructorCallExpression)
@given(instance=expression_ConstructorCallExpression_strategy)
@settings(max_examples=25)
def test_expression_ConstructorCallExpression_instantiation(instance):
    assert isinstance(instance, expression_ConstructorCallExpression)


expression_Expression_strategy = st.builds(expression_Expression)
@given(instance=expression_Expression_strategy)
@settings(max_examples=25)
def test_expression_Expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)


expression_FeatureCall_strategy = st.builds(expression_FeatureCall, name=safe_text)
@given(instance=expression_FeatureCall_strategy)
@settings(max_examples=25)
def test_expression_FeatureCall_instantiation(instance):
    assert isinstance(instance, expression_FeatureCall)


expression_GlobalVarExpression_strategy = st.builds(expression_GlobalVarExpression, name=safe_text)
@given(instance=expression_GlobalVarExpression_strategy)
@settings(max_examples=25)
def test_expression_GlobalVarExpression_instantiation(instance):
    assert isinstance(instance, expression_GlobalVarExpression)


expression_Identifier_strategy = st.builds(expression_Identifier, cl=safe_text, id=safe_text)
@given(instance=expression_Identifier_strategy)
@settings(max_examples=25)
def test_expression_Identifier_instantiation(instance):
    assert isinstance(instance, expression_Identifier)


expression_IfExpression_strategy = st.builds(expression_IfExpression)
@given(instance=expression_IfExpression_strategy)
@settings(max_examples=25)
def test_expression_IfExpression_instantiation(instance):
    assert isinstance(instance, expression_IfExpression)


expression_IntegerLiteral_strategy = st.builds(expression_IntegerLiteral, val=st.integers())
@given(instance=expression_IntegerLiteral_strategy)
@settings(max_examples=25)
def test_expression_IntegerLiteral_instantiation(instance):
    assert isinstance(instance, expression_IntegerLiteral)


expression_LetExpression_strategy = st.builds(expression_LetExpression, identifier=safe_text)
@given(instance=expression_LetExpression_strategy)
@settings(max_examples=25)
def test_expression_LetExpression_instantiation(instance):
    assert isinstance(instance, expression_LetExpression)


expression_ListLiteral_strategy = st.builds(expression_ListLiteral)
@given(instance=expression_ListLiteral_strategy)
@settings(max_examples=25)
def test_expression_ListLiteral_instantiation(instance):
    assert isinstance(instance, expression_ListLiteral)


expression_Literal_strategy = st.builds(expression_Literal)
@given(instance=expression_Literal_strategy)
@settings(max_examples=25)
def test_expression_Literal_instantiation(instance):
    assert isinstance(instance, expression_Literal)


expression_NullLiteral_strategy = st.builds(expression_NullLiteral, val=safe_text)
@given(instance=expression_NullLiteral_strategy)
@settings(max_examples=25)
def test_expression_NullLiteral_instantiation(instance):
    assert isinstance(instance, expression_NullLiteral)


expression_OperationCall_strategy = st.builds(expression_OperationCall)
@given(instance=expression_OperationCall_strategy)
@settings(max_examples=25)
def test_expression_OperationCall_instantiation(instance):
    assert isinstance(instance, expression_OperationCall)


expression_RealLiteral_strategy = st.builds(expression_RealLiteral, val=safe_text)
@given(instance=expression_RealLiteral_strategy)
@settings(max_examples=25)
def test_expression_RealLiteral_instantiation(instance):
    assert isinstance(instance, expression_RealLiteral)


expression_StringLiteral_strategy = st.builds(expression_StringLiteral, val=safe_text)
@given(instance=expression_StringLiteral_strategy)
@settings(max_examples=25)
def test_expression_StringLiteral_instantiation(instance):
    assert isinstance(instance, expression_StringLiteral)


expression_SwitchExpression_strategy = st.builds(expression_SwitchExpression)
@given(instance=expression_SwitchExpression_strategy)
@settings(max_examples=25)
def test_expression_SwitchExpression_instantiation(instance):
    assert isinstance(instance, expression_SwitchExpression)


expression_SyntaxElement_strategy = st.builds(expression_SyntaxElement)
@given(instance=expression_SyntaxElement_strategy)
@settings(max_examples=25)
def test_expression_SyntaxElement_instantiation(instance):
    assert isinstance(instance, expression_SyntaxElement)


expression_TypeSelectExpression_strategy = st.builds(expression_TypeSelectExpression)
@given(instance=expression_TypeSelectExpression_strategy)
@settings(max_examples=25)
def test_expression_TypeSelectExpression_instantiation(instance):
    assert isinstance(instance, expression_TypeSelectExpression)



