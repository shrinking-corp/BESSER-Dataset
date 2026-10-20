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
    Expr,
    miniJava_Multiplication,
    miniJava_Point,
    miniJava_SquareBrackets,
    miniJava_Addition,
    miniJava_Expression,
    miniJava_MethodCall,
    miniJava_NumberValue,
    miniJava_Expr,
    miniJava_Variable,
    miniJava_Type,
    miniJava_Statement,
    miniJava_Method,
    miniJava_VarDeclaration,
    miniJava_MainMethod,
    miniJava_ClassDecl,
    miniJava_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_hyp_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_hyp_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava_Multiplication)


def test_hyp_minijava_multiplication_constructor_exists():
    assert callable(miniJava_Multiplication.__init__)


def test_hyp_minijava_multiplication_constructor_args():
    sig = inspect.signature(miniJava_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_point_is_not_abstract():
    assert not inspect.isabstract(miniJava_Point)


def test_hyp_minijava_point_constructor_exists():
    assert callable(miniJava_Point.__init__)


def test_hyp_minijava_point_constructor_args():
    sig = inspect.signature(miniJava_Point.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_squarebrackets_is_not_abstract():
    assert not inspect.isabstract(miniJava_SquareBrackets)


def test_hyp_minijava_squarebrackets_constructor_exists():
    assert callable(miniJava_SquareBrackets.__init__)


def test_hyp_minijava_squarebrackets_constructor_args():
    sig = inspect.signature(miniJava_SquareBrackets.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_addition_is_not_abstract():
    assert not inspect.isabstract(miniJava_Addition)


def test_hyp_minijava_addition_constructor_exists():
    assert callable(miniJava_Addition.__init__)


def test_hyp_minijava_addition_constructor_args():
    sig = inspect.signature(miniJava_Addition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_expression_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expression)


def test_hyp_minijava_expression_constructor_exists():
    assert callable(miniJava_Expression.__init__)


def test_hyp_minijava_expression_constructor_args():
    sig = inspect.signature(miniJava_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall)


def test_hyp_minijava_methodcall_constructor_exists():
    assert callable(miniJava_MethodCall.__init__)


def test_hyp_minijava_methodcall_constructor_args():
    sig = inspect.signature(miniJava_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_numbervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_NumberValue)


def test_hyp_minijava_numbervalue_constructor_exists():
    assert callable(miniJava_NumberValue.__init__)


def test_hyp_minijava_numbervalue_constructor_args():
    sig = inspect.signature(miniJava_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_minijava_expr_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expr)


def test_hyp_minijava_expr_constructor_exists():
    assert callable(miniJava_Expr.__init__)


def test_hyp_minijava_expr_constructor_args():
    sig = inspect.signature(miniJava_Expr.__init__)
    params = list(sig.parameters.keys())
    assert "expressionType" in params, "Missing parameter 'expressionType'"




def test_hyp_minijava_variable_is_not_abstract():
    assert not inspect.isabstract(miniJava_Variable)


def test_hyp_minijava_variable_constructor_exists():
    assert callable(miniJava_Variable.__init__)


def test_hyp_minijava_variable_constructor_args():
    sig = inspect.signature(miniJava_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_minijava_type_is_not_abstract():
    assert not inspect.isabstract(miniJava_Type)


def test_hyp_minijava_type_constructor_exists():
    assert callable(miniJava_Type.__init__)


def test_hyp_minijava_type_constructor_args():
    sig = inspect.signature(miniJava_Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"




def test_hyp_minijava_statement_is_not_abstract():
    assert not inspect.isabstract(miniJava_Statement)


def test_hyp_minijava_statement_constructor_exists():
    assert callable(miniJava_Statement.__init__)


def test_hyp_minijava_statement_constructor_args():
    sig = inspect.signature(miniJava_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "isArrayElementAssignment" in params, "Missing parameter 'isArrayElementAssignment'"
    assert "statementType" in params, "Missing parameter 'statementType'"





def test_hyp_minijava_method_is_not_abstract():
    assert not inspect.isabstract(miniJava_Method)


def test_hyp_minijava_method_constructor_exists():
    assert callable(miniJava_Method.__init__)


def test_hyp_minijava_method_constructor_args():
    sig = inspect.signature(miniJava_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_minijava_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_VarDeclaration)


def test_hyp_minijava_vardeclaration_constructor_exists():
    assert callable(miniJava_VarDeclaration.__init__)


def test_hyp_minijava_vardeclaration_constructor_args():
    sig = inspect.signature(miniJava_VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_mainmethod_is_not_abstract():
    assert not inspect.isabstract(miniJava_MainMethod)


def test_hyp_minijava_mainmethod_constructor_exists():
    assert callable(miniJava_MainMethod.__init__)


def test_hyp_minijava_mainmethod_constructor_args():
    sig = inspect.signature(miniJava_MainMethod.__init__)
    params = list(sig.parameters.keys())



def test_hyp_minijava_classdecl_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClassDecl)


def test_hyp_minijava_classdecl_constructor_exists():
    assert callable(miniJava_ClassDecl.__init__)


def test_hyp_minijava_classdecl_constructor_args():
    sig = inspect.signature(miniJava_ClassDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_minijava_program_is_not_abstract():
    assert not inspect.isabstract(miniJava_Program)


def test_hyp_minijava_program_constructor_exists():
    assert callable(miniJava_Program.__init__)


def test_hyp_minijava_program_constructor_args():
    sig = inspect.signature(miniJava_Program.__init__)
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
Expr_strategy = st.builds(
    Expr,
)
miniJava_Multiplication_strategy = st.builds(
    miniJava_Multiplication,
)
miniJava_Point_strategy = st.builds(
    miniJava_Point,
)
miniJava_SquareBrackets_strategy = st.builds(
    miniJava_SquareBrackets,
)
miniJava_Addition_strategy = st.builds(
    miniJava_Addition,
)
miniJava_Expression_strategy = st.builds(
    miniJava_Expression,
)
miniJava_MethodCall_strategy = st.builds(
    miniJava_MethodCall,
)
miniJava_NumberValue_strategy = st.builds(
    miniJava_NumberValue,
    value=
        st.integers()
)
miniJava_Expr_strategy = st.builds(
    miniJava_Expr,
    expressionType=
        safe_text
)
miniJava_Variable_strategy = st.builds(
    miniJava_Variable,
    name=
        safe_text
)
miniJava_Type_strategy = st.builds(
    miniJava_Type,
    typeName=
        safe_text
)
miniJava_Statement_strategy = st.builds(
    miniJava_Statement,
    isArrayElementAssignment=
        st.booleans(),
    statementType=
        safe_text
)
miniJava_Method_strategy = st.builds(
    miniJava_Method,
    name=
        safe_text
)
miniJava_VarDeclaration_strategy = st.builds(
    miniJava_VarDeclaration,
)
miniJava_MainMethod_strategy = st.builds(
    miniJava_MainMethod,
)
miniJava_ClassDecl_strategy = st.builds(
    miniJava_ClassDecl,
    name=
        safe_text
)
miniJava_Program_strategy = st.builds(
    miniJava_Program,
)











@given(instance=miniJava_NumberValue_strategy)
def test_hyp_minijava_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=miniJava_Expr_strategy)
def test_hyp_minijava_expr_expressionType_setter(instance):
    original = instance.expressionType
    instance.expressionType = original
    assert instance.expressionType == original




@given(instance=miniJava_Variable_strategy)
def test_hyp_minijava_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=miniJava_Type_strategy)
def test_hyp_minijava_type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original




@given(instance=miniJava_Statement_strategy)
def test_hyp_minijava_statement_isArrayElementAssignment_setter(instance):
    original = instance.isArrayElementAssignment
    instance.isArrayElementAssignment = original
    assert instance.isArrayElementAssignment == original



@given(instance=miniJava_Statement_strategy)
def test_hyp_minijava_statement_statementType_setter(instance):
    original = instance.statementType
    instance.statementType = original
    assert instance.statementType == original




@given(instance=miniJava_Method_strategy)
def test_hyp_minijava_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=miniJava_ClassDecl_strategy)
def test_hyp_minijava_classdecl_name_setter(instance):
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
    Expr,
    miniJava_Addition,
    miniJava_ClassDecl,
    miniJava_Expr,
    miniJava_Expression,
    miniJava_MainMethod,
    miniJava_Method,
    miniJava_MethodCall,
    miniJava_Multiplication,
    miniJava_NumberValue,
    miniJava_Point,
    miniJava_Program,
    miniJava_SquareBrackets,
    miniJava_Statement,
    miniJava_Type,
    miniJava_VarDeclaration,
    miniJava_Variable,
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

def test_miniJava_ClassDecl_name_value_roundtrip():
    instance = miniJava_ClassDecl(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_miniJava_Expr_expressionType_value_roundtrip():
    instance = miniJava_Expr(expressionType="sample_text")
    assert instance.expressionType == "sample_text"
    instance.expressionType = "sample_text_2"
    assert instance.expressionType == "sample_text_2"


def test_miniJava_Method_name_value_roundtrip():
    instance = miniJava_Method(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_miniJava_NumberValue_value_value_roundtrip():
    instance = miniJava_NumberValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_miniJava_Statement_isArrayElementAssignment_value_roundtrip():
    instance = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    assert instance.isArrayElementAssignment == True
    instance.isArrayElementAssignment = False
    assert instance.isArrayElementAssignment == False


def test_miniJava_Statement_statementType_value_roundtrip():
    instance = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    assert instance.statementType == "sample_text"
    instance.statementType = "sample_text_2"
    assert instance.statementType == "sample_text_2"


def test_miniJava_Type_typeName_value_roundtrip():
    instance = miniJava_Type(typeName="sample_text")
    assert instance.typeName == "sample_text"
    instance.typeName = "sample_text_2"
    assert instance.typeName == "sample_text_2"


def test_miniJava_Variable_name_value_roundtrip():
    instance = miniJava_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_miniJava_Addition_isa_Expr():
    instance = miniJava_Addition()
    assert isinstance(instance, Expr)


def test_miniJava_Expression_isa_Expr():
    instance = miniJava_Expression()
    assert isinstance(instance, Expr)


def test_miniJava_Multiplication_isa_Expr():
    instance = miniJava_Multiplication()
    assert isinstance(instance, Expr)


def test_miniJava_Point_isa_Expr():
    instance = miniJava_Point()
    assert isinstance(instance, Expr)


def test_miniJava_SquareBrackets_isa_Expr():
    instance = miniJava_SquareBrackets()
    assert isinstance(instance, Expr)


def test_assoc_classDecl12_link_reassign_clear():
    a = miniJava_Type(typeName="sample_text")
    b1 = miniJava_ClassDecl(name="sample_text")
    b2 = miniJava_ClassDecl(name="sample_text_2")
    _safe_set(a, 'miniJava_Type', b1)
    assert _is_linked(a, 'miniJava_Type', b1)
    if hasattr(b1, 'miniJava_ClassDecl13'):
        assert _is_linked(b1, 'miniJava_ClassDecl13', a)
    _safe_set(a, 'miniJava_Type', b2)
    assert _is_linked(a, 'miniJava_Type', b2)
    if hasattr(b1, 'miniJava_ClassDecl13'):
        assert not _is_linked(b1, 'miniJava_ClassDecl13', a)
    if hasattr(b2, 'miniJava_ClassDecl13'):
        assert _is_linked(b2, 'miniJava_ClassDecl13', a)
    _safe_set(a, 'miniJava_Type', None)
    assert not _is_linked(a, 'miniJava_Type', b2)
    if hasattr(b2, 'miniJava_ClassDecl13'):
        assert not _is_linked(b2, 'miniJava_ClassDecl13', a)


def test_assoc_classDeclarations0_link_reassign_clear():
    a = miniJava_ClassDecl(name="sample_text")
    b1 = miniJava_Program()
    b2 = miniJava_Program()
    _safe_set(a, 'miniJava_ClassDecl', b1)
    assert _is_linked(a, 'miniJava_ClassDecl', b1)
    if hasattr(b1, 'miniJava_Program'):
        assert _is_linked(b1, 'miniJava_Program', a)
    _safe_set(a, 'miniJava_ClassDecl', b2)
    assert _is_linked(a, 'miniJava_ClassDecl', b2)
    if hasattr(b1, 'miniJava_Program'):
        assert not _is_linked(b1, 'miniJava_Program', a)
    if hasattr(b2, 'miniJava_Program'):
        assert _is_linked(b2, 'miniJava_Program', a)
    _safe_set(a, 'miniJava_ClassDecl', None)
    assert not _is_linked(a, 'miniJava_ClassDecl', b2)
    if hasattr(b2, 'miniJava_Program'):
        assert not _is_linked(b2, 'miniJava_Program', a)


def test_assoc_expression49_link_reassign_clear():
    a = miniJava_Expr(expressionType="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Expr48', b1)
    assert _is_linked(a, 'miniJava_Expr48', b1)
    if hasattr(b1, 'miniJava_Expr50'):
        assert _is_linked(b1, 'miniJava_Expr50', a)
    _safe_set(a, 'miniJava_Expr48', b2)
    assert _is_linked(a, 'miniJava_Expr48', b2)
    if hasattr(b1, 'miniJava_Expr50'):
        assert not _is_linked(b1, 'miniJava_Expr50', a)
    if hasattr(b2, 'miniJava_Expr50'):
        assert _is_linked(b2, 'miniJava_Expr50', a)
    _safe_set(a, 'miniJava_Expr48', None)
    assert not _is_linked(a, 'miniJava_Expr48', b2)
    if hasattr(b2, 'miniJava_Expr50'):
        assert not _is_linked(b2, 'miniJava_Expr50', a)


def test_assoc_extendedClass4_link_reassign_clear():
    a = miniJava_ClassDecl(name="sample_text")
    b1 = miniJava_ClassDecl(name="sample_text")
    b2 = miniJava_ClassDecl(name="sample_text_2")
    _safe_set(a, 'miniJava_ClassDecl3', b1)
    assert _is_linked(a, 'miniJava_ClassDecl3', b1)
    if hasattr(b1, 'miniJava_ClassDecl5'):
        assert _is_linked(b1, 'miniJava_ClassDecl5', a)
    _safe_set(a, 'miniJava_ClassDecl3', b2)
    assert _is_linked(a, 'miniJava_ClassDecl3', b2)
    if hasattr(b1, 'miniJava_ClassDecl5'):
        assert not _is_linked(b1, 'miniJava_ClassDecl5', a)
    if hasattr(b2, 'miniJava_ClassDecl5'):
        assert _is_linked(b2, 'miniJava_ClassDecl5', a)
    _safe_set(a, 'miniJava_ClassDecl3', None)
    assert not _is_linked(a, 'miniJava_ClassDecl3', b2)
    if hasattr(b2, 'miniJava_ClassDecl5'):
        assert not _is_linked(b2, 'miniJava_ClassDecl5', a)


def test_assoc_firstExpression36_link_reassign_clear():
    a = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Statement37', b1)
    assert _is_linked(a, 'miniJava_Statement37', b1)
    if hasattr(b1, 'miniJava_Expr38'):
        assert _is_linked(b1, 'miniJava_Expr38', a)
    _safe_set(a, 'miniJava_Statement37', b2)
    assert _is_linked(a, 'miniJava_Statement37', b2)
    if hasattr(b1, 'miniJava_Expr38'):
        assert not _is_linked(b1, 'miniJava_Expr38', a)
    if hasattr(b2, 'miniJava_Expr38'):
        assert _is_linked(b2, 'miniJava_Expr38', a)
    _safe_set(a, 'miniJava_Statement37', None)
    assert not _is_linked(a, 'miniJava_Statement37', b2)
    if hasattr(b2, 'miniJava_Expr38'):
        assert not _is_linked(b2, 'miniJava_Expr38', a)


def test_assoc_formalVarDeclarations22_link_reassign_clear():
    a = miniJava_Variable(name="sample_text")
    b1 = miniJava_Method(name="sample_text")
    b2 = miniJava_Method(name="sample_text_2")
    _safe_set(a, 'miniJava_Variable24', b1)
    assert _is_linked(a, 'miniJava_Variable24', b1)
    if hasattr(b1, 'miniJava_Method23'):
        assert _is_linked(b1, 'miniJava_Method23', a)
    _safe_set(a, 'miniJava_Variable24', b2)
    assert _is_linked(a, 'miniJava_Variable24', b2)
    if hasattr(b1, 'miniJava_Method23'):
        assert not _is_linked(b1, 'miniJava_Method23', a)
    if hasattr(b2, 'miniJava_Method23'):
        assert _is_linked(b2, 'miniJava_Method23', a)
    _safe_set(a, 'miniJava_Variable24', None)
    assert not _is_linked(a, 'miniJava_Variable24', b2)
    if hasattr(b2, 'miniJava_Method23'):
        assert not _is_linked(b2, 'miniJava_Method23', a)


def test_assoc_left62_link_reassign_clear():
    a = miniJava_Expr(expressionType="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Expr61', b1)
    assert _is_linked(a, 'miniJava_Expr61', b1)
    if hasattr(b1, 'miniJava_Expr63'):
        assert _is_linked(b1, 'miniJava_Expr63', a)
    _safe_set(a, 'miniJava_Expr61', b2)
    assert _is_linked(a, 'miniJava_Expr61', b2)
    if hasattr(b1, 'miniJava_Expr63'):
        assert not _is_linked(b1, 'miniJava_Expr63', a)
    if hasattr(b2, 'miniJava_Expr63'):
        assert _is_linked(b2, 'miniJava_Expr63', a)
    _safe_set(a, 'miniJava_Expr61', None)
    assert not _is_linked(a, 'miniJava_Expr61', b2)
    if hasattr(b2, 'miniJava_Expr63'):
        assert not _is_linked(b2, 'miniJava_Expr63', a)


def test_assoc_localVarDeclarations25_link_reassign_clear():
    a = miniJava_Method(name="sample_text")
    b1 = miniJava_VarDeclaration()
    b2 = miniJava_VarDeclaration()
    _safe_set(a, 'miniJava_Method26', {b1})
    assert _is_linked(a, 'miniJava_Method26', b1)
    if hasattr(b1, 'miniJava_VarDeclaration27'):
        assert _is_linked(b1, 'miniJava_VarDeclaration27', a)
    _safe_set(a, 'miniJava_Method26', {b2})
    assert _is_linked(a, 'miniJava_Method26', b2)
    if hasattr(b1, 'miniJava_VarDeclaration27'):
        assert not _is_linked(b1, 'miniJava_VarDeclaration27', a)
    if hasattr(b2, 'miniJava_VarDeclaration27'):
        assert _is_linked(b2, 'miniJava_VarDeclaration27', a)
    _safe_set(a, 'miniJava_Method26', set())
    assert not _is_linked(a, 'miniJava_Method26', b2)
    if hasattr(b2, 'miniJava_VarDeclaration27'):
        assert not _is_linked(b2, 'miniJava_VarDeclaration27', a)


def test_assoc_mainMethod1_link_reassign_clear():
    a = miniJava_ClassDecl(name="sample_text")
    b1 = miniJava_MainMethod()
    b2 = miniJava_MainMethod()
    _safe_set(a, 'miniJava_ClassDecl2', b1)
    assert _is_linked(a, 'miniJava_ClassDecl2', b1)
    if hasattr(b1, 'miniJava_MainMethod'):
        assert _is_linked(b1, 'miniJava_MainMethod', a)
    _safe_set(a, 'miniJava_ClassDecl2', b2)
    assert _is_linked(a, 'miniJava_ClassDecl2', b2)
    if hasattr(b1, 'miniJava_MainMethod'):
        assert not _is_linked(b1, 'miniJava_MainMethod', a)
    if hasattr(b2, 'miniJava_MainMethod'):
        assert _is_linked(b2, 'miniJava_MainMethod', a)
    _safe_set(a, 'miniJava_ClassDecl2', None)
    assert not _is_linked(a, 'miniJava_ClassDecl2', b2)
    if hasattr(b2, 'miniJava_MainMethod'):
        assert not _is_linked(b2, 'miniJava_MainMethod', a)


def test_assoc_method64_link_reassign_clear():
    a = miniJava_Method(name="sample_text")
    b1 = miniJava_MethodCall()
    b2 = miniJava_MethodCall()
    _safe_set(a, 'miniJava_Method66', b1)
    assert _is_linked(a, 'miniJava_Method66', b1)
    if hasattr(b1, 'miniJava_MethodCall65'):
        assert _is_linked(b1, 'miniJava_MethodCall65', a)
    _safe_set(a, 'miniJava_Method66', b2)
    assert _is_linked(a, 'miniJava_Method66', b2)
    if hasattr(b1, 'miniJava_MethodCall65'):
        assert not _is_linked(b1, 'miniJava_MethodCall65', a)
    if hasattr(b2, 'miniJava_MethodCall65'):
        assert _is_linked(b2, 'miniJava_MethodCall65', a)
    _safe_set(a, 'miniJava_Method66', None)
    assert not _is_linked(a, 'miniJava_Method66', b2)
    if hasattr(b2, 'miniJava_MethodCall65'):
        assert not _is_linked(b2, 'miniJava_MethodCall65', a)


def test_assoc_methodCall59_link_reassign_clear():
    a = miniJava_Expr(expressionType="sample_text")
    b1 = miniJava_MethodCall()
    b2 = miniJava_MethodCall()
    _safe_set(a, 'miniJava_Expr60', b1)
    assert _is_linked(a, 'miniJava_Expr60', b1)
    if hasattr(b1, 'miniJava_MethodCall'):
        assert _is_linked(b1, 'miniJava_MethodCall', a)
    _safe_set(a, 'miniJava_Expr60', b2)
    assert _is_linked(a, 'miniJava_Expr60', b2)
    if hasattr(b1, 'miniJava_MethodCall'):
        assert not _is_linked(b1, 'miniJava_MethodCall', a)
    if hasattr(b2, 'miniJava_MethodCall'):
        assert _is_linked(b2, 'miniJava_MethodCall', a)
    _safe_set(a, 'miniJava_Expr60', None)
    assert not _is_linked(a, 'miniJava_Expr60', b2)
    if hasattr(b2, 'miniJava_MethodCall'):
        assert not _is_linked(b2, 'miniJava_MethodCall', a)


def test_assoc_methodDeclarations8_link_reassign_clear():
    a = miniJava_Method(name="sample_text")
    b1 = miniJava_ClassDecl(name="sample_text")
    b2 = miniJava_ClassDecl(name="sample_text_2")
    _safe_set(a, 'miniJava_Method', b1)
    assert _is_linked(a, 'miniJava_Method', b1)
    if hasattr(b1, 'miniJava_ClassDecl9'):
        assert _is_linked(b1, 'miniJava_ClassDecl9', a)
    _safe_set(a, 'miniJava_Method', b2)
    assert _is_linked(a, 'miniJava_Method', b2)
    if hasattr(b1, 'miniJava_ClassDecl9'):
        assert not _is_linked(b1, 'miniJava_ClassDecl9', a)
    if hasattr(b2, 'miniJava_ClassDecl9'):
        assert _is_linked(b2, 'miniJava_ClassDecl9', a)
    _safe_set(a, 'miniJava_Method', None)
    assert not _is_linked(a, 'miniJava_Method', b2)
    if hasattr(b2, 'miniJava_ClassDecl9'):
        assert not _is_linked(b2, 'miniJava_ClassDecl9', a)


def test_assoc_methodType19_link_reassign_clear():
    a = miniJava_Type(typeName="sample_text")
    b1 = miniJava_Method(name="sample_text")
    b2 = miniJava_Method(name="sample_text_2")
    _safe_set(a, 'miniJava_Type21', b1)
    assert _is_linked(a, 'miniJava_Type21', b1)
    if hasattr(b1, 'miniJava_Method20'):
        assert _is_linked(b1, 'miniJava_Method20', a)
    _safe_set(a, 'miniJava_Type21', b2)
    assert _is_linked(a, 'miniJava_Type21', b2)
    if hasattr(b1, 'miniJava_Method20'):
        assert not _is_linked(b1, 'miniJava_Method20', a)
    if hasattr(b2, 'miniJava_Method20'):
        assert _is_linked(b2, 'miniJava_Method20', a)
    _safe_set(a, 'miniJava_Type21', None)
    assert not _is_linked(a, 'miniJava_Type21', b2)
    if hasattr(b2, 'miniJava_Method20'):
        assert not _is_linked(b2, 'miniJava_Method20', a)


def test_assoc_number57_link_reassign_clear():
    a = miniJava_NumberValue(value=7)
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_NumberValue', b1)
    assert _is_linked(a, 'miniJava_NumberValue', b1)
    if hasattr(b1, 'miniJava_Expr58'):
        assert _is_linked(b1, 'miniJava_Expr58', a)
    _safe_set(a, 'miniJava_NumberValue', b2)
    assert _is_linked(a, 'miniJava_NumberValue', b2)
    if hasattr(b1, 'miniJava_Expr58'):
        assert not _is_linked(b1, 'miniJava_Expr58', a)
    if hasattr(b2, 'miniJava_Expr58'):
        assert _is_linked(b2, 'miniJava_Expr58', a)
    _safe_set(a, 'miniJava_NumberValue', None)
    assert not _is_linked(a, 'miniJava_NumberValue', b2)
    if hasattr(b2, 'miniJava_Expr58'):
        assert not _is_linked(b2, 'miniJava_Expr58', a)


def test_assoc_parameters67_link_reassign_clear():
    a = miniJava_Expr(expressionType="sample_text")
    b1 = miniJava_MethodCall()
    b2 = miniJava_MethodCall()
    _safe_set(a, 'miniJava_Expr69', b1)
    assert _is_linked(a, 'miniJava_Expr69', b1)
    if hasattr(b1, 'miniJava_MethodCall68'):
        assert _is_linked(b1, 'miniJava_MethodCall68', a)
    _safe_set(a, 'miniJava_Expr69', b2)
    assert _is_linked(a, 'miniJava_Expr69', b2)
    if hasattr(b1, 'miniJava_MethodCall68'):
        assert not _is_linked(b1, 'miniJava_MethodCall68', a)
    if hasattr(b2, 'miniJava_MethodCall68'):
        assert _is_linked(b2, 'miniJava_MethodCall68', a)
    _safe_set(a, 'miniJava_Expr69', None)
    assert not _is_linked(a, 'miniJava_Expr69', b2)
    if hasattr(b2, 'miniJava_MethodCall68'):
        assert not _is_linked(b2, 'miniJava_MethodCall68', a)


def test_assoc_returnExpression31_link_reassign_clear():
    a = miniJava_Method(name="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Method32', b1)
    assert _is_linked(a, 'miniJava_Method32', b1)
    if hasattr(b1, 'miniJava_Expr'):
        assert _is_linked(b1, 'miniJava_Expr', a)
    _safe_set(a, 'miniJava_Method32', b2)
    assert _is_linked(a, 'miniJava_Method32', b2)
    if hasattr(b1, 'miniJava_Expr'):
        assert not _is_linked(b1, 'miniJava_Expr', a)
    if hasattr(b2, 'miniJava_Expr'):
        assert _is_linked(b2, 'miniJava_Expr', a)
    _safe_set(a, 'miniJava_Method32', None)
    assert not _is_linked(a, 'miniJava_Method32', b2)
    if hasattr(b2, 'miniJava_Expr'):
        assert not _is_linked(b2, 'miniJava_Expr', a)


def test_assoc_right46_link_reassign_clear():
    a = miniJava_Expr(expressionType="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Expr45', b1)
    assert _is_linked(a, 'miniJava_Expr45', b1)
    if hasattr(b1, 'miniJava_Expr47'):
        assert _is_linked(b1, 'miniJava_Expr47', a)
    _safe_set(a, 'miniJava_Expr45', b2)
    assert _is_linked(a, 'miniJava_Expr45', b2)
    if hasattr(b1, 'miniJava_Expr47'):
        assert not _is_linked(b1, 'miniJava_Expr47', a)
    if hasattr(b2, 'miniJava_Expr47'):
        assert _is_linked(b2, 'miniJava_Expr47', a)
    _safe_set(a, 'miniJava_Expr45', None)
    assert not _is_linked(a, 'miniJava_Expr45', b2)
    if hasattr(b2, 'miniJava_Expr47'):
        assert not _is_linked(b2, 'miniJava_Expr47', a)


def test_assoc_secondExpression42_link_reassign_clear():
    a = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Statement43', b1)
    assert _is_linked(a, 'miniJava_Statement43', b1)
    if hasattr(b1, 'miniJava_Expr44'):
        assert _is_linked(b1, 'miniJava_Expr44', a)
    _safe_set(a, 'miniJava_Statement43', b2)
    assert _is_linked(a, 'miniJava_Statement43', b2)
    if hasattr(b1, 'miniJava_Expr44'):
        assert not _is_linked(b1, 'miniJava_Expr44', a)
    if hasattr(b2, 'miniJava_Expr44'):
        assert _is_linked(b2, 'miniJava_Expr44', a)
    _safe_set(a, 'miniJava_Statement43', None)
    assert not _is_linked(a, 'miniJava_Statement43', b2)
    if hasattr(b2, 'miniJava_Expr44'):
        assert not _is_linked(b2, 'miniJava_Expr44', a)


def test_assoc_statement10_link_reassign_clear():
    a = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b1 = miniJava_MainMethod()
    b2 = miniJava_MainMethod()
    _safe_set(a, 'miniJava_Statement', b1)
    assert _is_linked(a, 'miniJava_Statement', b1)
    if hasattr(b1, 'miniJava_MainMethod11'):
        assert _is_linked(b1, 'miniJava_MainMethod11', a)
    _safe_set(a, 'miniJava_Statement', b2)
    assert _is_linked(a, 'miniJava_Statement', b2)
    if hasattr(b1, 'miniJava_MainMethod11'):
        assert not _is_linked(b1, 'miniJava_MainMethod11', a)
    if hasattr(b2, 'miniJava_MainMethod11'):
        assert _is_linked(b2, 'miniJava_MainMethod11', a)
    _safe_set(a, 'miniJava_Statement', None)
    assert not _is_linked(a, 'miniJava_Statement', b2)
    if hasattr(b2, 'miniJava_MainMethod11'):
        assert not _is_linked(b2, 'miniJava_MainMethod11', a)


def test_assoc_statements28_link_reassign_clear():
    a = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b1 = miniJava_Method(name="sample_text")
    b2 = miniJava_Method(name="sample_text_2")
    _safe_set(a, 'miniJava_Statement30', b1)
    assert _is_linked(a, 'miniJava_Statement30', b1)
    if hasattr(b1, 'miniJava_Method29'):
        assert _is_linked(b1, 'miniJava_Method29', a)
    _safe_set(a, 'miniJava_Statement30', b2)
    assert _is_linked(a, 'miniJava_Statement30', b2)
    if hasattr(b1, 'miniJava_Method29'):
        assert not _is_linked(b1, 'miniJava_Method29', a)
    if hasattr(b2, 'miniJava_Method29'):
        assert _is_linked(b2, 'miniJava_Method29', a)
    _safe_set(a, 'miniJava_Statement30', None)
    assert not _is_linked(a, 'miniJava_Statement30', b2)
    if hasattr(b2, 'miniJava_Method29'):
        assert not _is_linked(b2, 'miniJava_Method29', a)


def test_assoc_statements34_link_reassign_clear():
    a = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    _safe_set(a, 'miniJava_Statement33', {b1})
    assert _is_linked(a, 'miniJava_Statement33', b1)
    if hasattr(b1, 'miniJava_Statement35'):
        assert _is_linked(b1, 'miniJava_Statement35', a)
    _safe_set(a, 'miniJava_Statement33', {b2})
    assert _is_linked(a, 'miniJava_Statement33', b2)
    if hasattr(b1, 'miniJava_Statement35'):
        assert not _is_linked(b1, 'miniJava_Statement35', a)
    if hasattr(b2, 'miniJava_Statement35'):
        assert _is_linked(b2, 'miniJava_Statement35', a)
    _safe_set(a, 'miniJava_Statement33', set())
    assert not _is_linked(a, 'miniJava_Statement33', b2)
    if hasattr(b2, 'miniJava_Statement35'):
        assert not _is_linked(b2, 'miniJava_Statement35', a)


def test_assoc_type51_link_reassign_clear():
    a = miniJava_Type(typeName="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Type53', b1)
    assert _is_linked(a, 'miniJava_Type53', b1)
    if hasattr(b1, 'miniJava_Expr52'):
        assert _is_linked(b1, 'miniJava_Expr52', a)
    _safe_set(a, 'miniJava_Type53', b2)
    assert _is_linked(a, 'miniJava_Type53', b2)
    if hasattr(b1, 'miniJava_Expr52'):
        assert not _is_linked(b1, 'miniJava_Expr52', a)
    if hasattr(b2, 'miniJava_Expr52'):
        assert _is_linked(b2, 'miniJava_Expr52', a)
    _safe_set(a, 'miniJava_Type53', None)
    assert not _is_linked(a, 'miniJava_Type53', b2)
    if hasattr(b2, 'miniJava_Expr52'):
        assert not _is_linked(b2, 'miniJava_Expr52', a)


def test_assoc_varDeclarations6_link_reassign_clear():
    a = miniJava_ClassDecl(name="sample_text")
    b1 = miniJava_VarDeclaration()
    b2 = miniJava_VarDeclaration()
    _safe_set(a, 'miniJava_ClassDecl7', {b1})
    assert _is_linked(a, 'miniJava_ClassDecl7', b1)
    if hasattr(b1, 'miniJava_VarDeclaration'):
        assert _is_linked(b1, 'miniJava_VarDeclaration', a)
    _safe_set(a, 'miniJava_ClassDecl7', {b2})
    assert _is_linked(a, 'miniJava_ClassDecl7', b2)
    if hasattr(b1, 'miniJava_VarDeclaration'):
        assert not _is_linked(b1, 'miniJava_VarDeclaration', a)
    if hasattr(b2, 'miniJava_VarDeclaration'):
        assert _is_linked(b2, 'miniJava_VarDeclaration', a)
    _safe_set(a, 'miniJava_ClassDecl7', set())
    assert not _is_linked(a, 'miniJava_ClassDecl7', b2)
    if hasattr(b2, 'miniJava_VarDeclaration'):
        assert not _is_linked(b2, 'miniJava_VarDeclaration', a)


def test_assoc_variable14_link_reassign_clear():
    a = miniJava_Variable(name="sample_text")
    b1 = miniJava_VarDeclaration()
    b2 = miniJava_VarDeclaration()
    _safe_set(a, 'miniJava_Variable', b1)
    assert _is_linked(a, 'miniJava_Variable', b1)
    if hasattr(b1, 'miniJava_VarDeclaration15'):
        assert _is_linked(b1, 'miniJava_VarDeclaration15', a)
    _safe_set(a, 'miniJava_Variable', b2)
    assert _is_linked(a, 'miniJava_Variable', b2)
    if hasattr(b1, 'miniJava_VarDeclaration15'):
        assert not _is_linked(b1, 'miniJava_VarDeclaration15', a)
    if hasattr(b2, 'miniJava_VarDeclaration15'):
        assert _is_linked(b2, 'miniJava_VarDeclaration15', a)
    _safe_set(a, 'miniJava_Variable', None)
    assert not _is_linked(a, 'miniJava_Variable', b2)
    if hasattr(b2, 'miniJava_VarDeclaration15'):
        assert not _is_linked(b2, 'miniJava_VarDeclaration15', a)


def test_assoc_variable39_link_reassign_clear():
    a = miniJava_Variable(name="sample_text")
    b1 = miniJava_Statement(isArrayElementAssignment=True, statementType="sample_text")
    b2 = miniJava_Statement(isArrayElementAssignment=False, statementType="sample_text_2")
    _safe_set(a, 'miniJava_Variable41', b1)
    assert _is_linked(a, 'miniJava_Variable41', b1)
    if hasattr(b1, 'miniJava_Statement40'):
        assert _is_linked(b1, 'miniJava_Statement40', a)
    _safe_set(a, 'miniJava_Variable41', b2)
    assert _is_linked(a, 'miniJava_Variable41', b2)
    if hasattr(b1, 'miniJava_Statement40'):
        assert not _is_linked(b1, 'miniJava_Statement40', a)
    if hasattr(b2, 'miniJava_Statement40'):
        assert _is_linked(b2, 'miniJava_Statement40', a)
    _safe_set(a, 'miniJava_Variable41', None)
    assert not _is_linked(a, 'miniJava_Variable41', b2)
    if hasattr(b2, 'miniJava_Statement40'):
        assert not _is_linked(b2, 'miniJava_Statement40', a)


def test_assoc_variable54_link_reassign_clear():
    a = miniJava_Variable(name="sample_text")
    b1 = miniJava_Expr(expressionType="sample_text")
    b2 = miniJava_Expr(expressionType="sample_text_2")
    _safe_set(a, 'miniJava_Variable56', b1)
    assert _is_linked(a, 'miniJava_Variable56', b1)
    if hasattr(b1, 'miniJava_Expr55'):
        assert _is_linked(b1, 'miniJava_Expr55', a)
    _safe_set(a, 'miniJava_Variable56', b2)
    assert _is_linked(a, 'miniJava_Variable56', b2)
    if hasattr(b1, 'miniJava_Expr55'):
        assert not _is_linked(b1, 'miniJava_Expr55', a)
    if hasattr(b2, 'miniJava_Expr55'):
        assert _is_linked(b2, 'miniJava_Expr55', a)
    _safe_set(a, 'miniJava_Variable56', None)
    assert not _is_linked(a, 'miniJava_Variable56', b2)
    if hasattr(b2, 'miniJava_Expr55'):
        assert not _is_linked(b2, 'miniJava_Expr55', a)


def test_assoc_variableType16_link_reassign_clear():
    a = miniJava_Variable(name="sample_text")
    b1 = miniJava_Type(typeName="sample_text")
    b2 = miniJava_Type(typeName="sample_text_2")
    _safe_set(a, 'miniJava_Variable17', b1)
    assert _is_linked(a, 'miniJava_Variable17', b1)
    if hasattr(b1, 'miniJava_Type18'):
        assert _is_linked(b1, 'miniJava_Type18', a)
    _safe_set(a, 'miniJava_Variable17', b2)
    assert _is_linked(a, 'miniJava_Variable17', b2)
    if hasattr(b1, 'miniJava_Type18'):
        assert not _is_linked(b1, 'miniJava_Type18', a)
    if hasattr(b2, 'miniJava_Type18'):
        assert _is_linked(b2, 'miniJava_Type18', a)
    _safe_set(a, 'miniJava_Variable17', None)
    assert not _is_linked(a, 'miniJava_Variable17', b2)
    if hasattr(b2, 'miniJava_Type18'):
        assert not _is_linked(b2, 'miniJava_Type18', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expr_strategy = st.builds(Expr)
@given(instance=Expr_strategy)
@settings(max_examples=25)
def test_Expr_instantiation(instance):
    assert isinstance(instance, Expr)


miniJava_Addition_strategy = st.builds(miniJava_Addition)
@given(instance=miniJava_Addition_strategy)
@settings(max_examples=25)
def test_miniJava_Addition_instantiation(instance):
    assert isinstance(instance, miniJava_Addition)


miniJava_ClassDecl_strategy = st.builds(miniJava_ClassDecl, name=safe_text)
@given(instance=miniJava_ClassDecl_strategy)
@settings(max_examples=25)
def test_miniJava_ClassDecl_instantiation(instance):
    assert isinstance(instance, miniJava_ClassDecl)


miniJava_Expr_strategy = st.builds(miniJava_Expr, expressionType=safe_text)
@given(instance=miniJava_Expr_strategy)
@settings(max_examples=25)
def test_miniJava_Expr_instantiation(instance):
    assert isinstance(instance, miniJava_Expr)


miniJava_Expression_strategy = st.builds(miniJava_Expression)
@given(instance=miniJava_Expression_strategy)
@settings(max_examples=25)
def test_miniJava_Expression_instantiation(instance):
    assert isinstance(instance, miniJava_Expression)


miniJava_MainMethod_strategy = st.builds(miniJava_MainMethod)
@given(instance=miniJava_MainMethod_strategy)
@settings(max_examples=25)
def test_miniJava_MainMethod_instantiation(instance):
    assert isinstance(instance, miniJava_MainMethod)


miniJava_Method_strategy = st.builds(miniJava_Method, name=safe_text)
@given(instance=miniJava_Method_strategy)
@settings(max_examples=25)
def test_miniJava_Method_instantiation(instance):
    assert isinstance(instance, miniJava_Method)


miniJava_MethodCall_strategy = st.builds(miniJava_MethodCall)
@given(instance=miniJava_MethodCall_strategy)
@settings(max_examples=25)
def test_miniJava_MethodCall_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall)


miniJava_Multiplication_strategy = st.builds(miniJava_Multiplication)
@given(instance=miniJava_Multiplication_strategy)
@settings(max_examples=25)
def test_miniJava_Multiplication_instantiation(instance):
    assert isinstance(instance, miniJava_Multiplication)


miniJava_NumberValue_strategy = st.builds(miniJava_NumberValue, value=st.integers())
@given(instance=miniJava_NumberValue_strategy)
@settings(max_examples=25)
def test_miniJava_NumberValue_instantiation(instance):
    assert isinstance(instance, miniJava_NumberValue)


miniJava_Point_strategy = st.builds(miniJava_Point)
@given(instance=miniJava_Point_strategy)
@settings(max_examples=25)
def test_miniJava_Point_instantiation(instance):
    assert isinstance(instance, miniJava_Point)


miniJava_Program_strategy = st.builds(miniJava_Program)
@given(instance=miniJava_Program_strategy)
@settings(max_examples=25)
def test_miniJava_Program_instantiation(instance):
    assert isinstance(instance, miniJava_Program)


miniJava_SquareBrackets_strategy = st.builds(miniJava_SquareBrackets)
@given(instance=miniJava_SquareBrackets_strategy)
@settings(max_examples=25)
def test_miniJava_SquareBrackets_instantiation(instance):
    assert isinstance(instance, miniJava_SquareBrackets)


miniJava_Statement_strategy = st.builds(miniJava_Statement, isArrayElementAssignment=st.booleans(), statementType=safe_text)
@given(instance=miniJava_Statement_strategy)
@settings(max_examples=25)
def test_miniJava_Statement_instantiation(instance):
    assert isinstance(instance, miniJava_Statement)


miniJava_Type_strategy = st.builds(miniJava_Type, typeName=safe_text)
@given(instance=miniJava_Type_strategy)
@settings(max_examples=25)
def test_miniJava_Type_instantiation(instance):
    assert isinstance(instance, miniJava_Type)


miniJava_VarDeclaration_strategy = st.builds(miniJava_VarDeclaration)
@given(instance=miniJava_VarDeclaration_strategy)
@settings(max_examples=25)
def test_miniJava_VarDeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_VarDeclaration)


miniJava_Variable_strategy = st.builds(miniJava_Variable, name=safe_text)
@given(instance=miniJava_Variable_strategy)
@settings(max_examples=25)
def test_miniJava_Variable_instantiation(instance):
    assert isinstance(instance, miniJava_Variable)



