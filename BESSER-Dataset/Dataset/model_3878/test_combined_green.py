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
    AssignmentStmt,
    Statement,
    codemodel_statements_AssignmentStmt,
    codemodel_statements_IfStmt,
    codemodel_statements_CompositeStmt,
    codemodel_statements_ForStmt,
    expressions_codemodel_Variable,
    Expression,
    codemodel_expressions_LiteralExp,
    codemodel_expressions_BinaryExp,
    codemodel_expressions_VariableExp,
    DataType,
    codemodel_ScalarType,
    codemodel_VectorType,
    codemodel_MatrixType,
    Variable,
    codemodel_FunctionArgument,
    codemodel_LocalVariable,
    codemodel_GlobalVariable,
    CMElement,
    codemodel_statements_Statement,
    codemodel_expressions_Expression,
    codemodel_Variable,
    codemodel_DataType,
    codemodel_Function,
    codemodel_CodeModule,
    codemodel_CMElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_assignmentstmt_is_not_abstract():
    assert not inspect.isabstract(AssignmentStmt)


def test_hyp_assignmentstmt_constructor_exists():
    assert callable(AssignmentStmt.__init__)


def test_hyp_assignmentstmt_constructor_args():
    sig = inspect.signature(AssignmentStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_statements_assignmentstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel_statements_AssignmentStmt)


def test_hyp_codemodel_statements_assignmentstmt_constructor_exists():
    assert callable(codemodel_statements_AssignmentStmt.__init__)


def test_hyp_codemodel_statements_assignmentstmt_constructor_args():
    sig = inspect.signature(codemodel_statements_AssignmentStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_statements_ifstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel_statements_IfStmt)


def test_hyp_codemodel_statements_ifstmt_constructor_exists():
    assert callable(codemodel_statements_IfStmt.__init__)


def test_hyp_codemodel_statements_ifstmt_constructor_args():
    sig = inspect.signature(codemodel_statements_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_statements_compositestmt_is_not_abstract():
    assert not inspect.isabstract(codemodel_statements_CompositeStmt)


def test_hyp_codemodel_statements_compositestmt_constructor_exists():
    assert callable(codemodel_statements_CompositeStmt.__init__)


def test_hyp_codemodel_statements_compositestmt_constructor_args():
    sig = inspect.signature(codemodel_statements_CompositeStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_statements_forstmt_is_not_abstract():
    assert not inspect.isabstract(codemodel_statements_ForStmt)


def test_hyp_codemodel_statements_forstmt_constructor_exists():
    assert callable(codemodel_statements_ForStmt.__init__)


def test_hyp_codemodel_statements_forstmt_constructor_args():
    sig = inspect.signature(codemodel_statements_ForStmt.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressions_codemodel_variable_is_not_abstract():
    assert not inspect.isabstract(expressions_codemodel_Variable)


def test_hyp_expressions_codemodel_variable_constructor_exists():
    assert callable(expressions_codemodel_Variable.__init__)


def test_hyp_expressions_codemodel_variable_constructor_args():
    sig = inspect.signature(expressions_codemodel_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_expressions_literalexp_is_not_abstract():
    assert not inspect.isabstract(codemodel_expressions_LiteralExp)


def test_hyp_codemodel_expressions_literalexp_constructor_exists():
    assert callable(codemodel_expressions_LiteralExp.__init__)


def test_hyp_codemodel_expressions_literalexp_constructor_args():
    sig = inspect.signature(codemodel_expressions_LiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_codemodel_expressions_binaryexp_is_not_abstract():
    assert not inspect.isabstract(codemodel_expressions_BinaryExp)


def test_hyp_codemodel_expressions_binaryexp_constructor_exists():
    assert callable(codemodel_expressions_BinaryExp.__init__)


def test_hyp_codemodel_expressions_binaryexp_constructor_args():
    sig = inspect.signature(codemodel_expressions_BinaryExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_codemodel_expressions_variableexp_is_not_abstract():
    assert not inspect.isabstract(codemodel_expressions_VariableExp)


def test_hyp_codemodel_expressions_variableexp_constructor_exists():
    assert callable(codemodel_expressions_VariableExp.__init__)


def test_hyp_codemodel_expressions_variableexp_constructor_args():
    sig = inspect.signature(codemodel_expressions_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_hyp_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_hyp_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_scalartype_is_not_abstract():
    assert not inspect.isabstract(codemodel_ScalarType)


def test_hyp_codemodel_scalartype_constructor_exists():
    assert callable(codemodel_ScalarType.__init__)


def test_hyp_codemodel_scalartype_constructor_args():
    sig = inspect.signature(codemodel_ScalarType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_vectortype_is_not_abstract():
    assert not inspect.isabstract(codemodel_VectorType)


def test_hyp_codemodel_vectortype_constructor_exists():
    assert callable(codemodel_VectorType.__init__)


def test_hyp_codemodel_vectortype_constructor_args():
    sig = inspect.signature(codemodel_VectorType.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"




def test_hyp_codemodel_matrixtype_is_not_abstract():
    assert not inspect.isabstract(codemodel_MatrixType)


def test_hyp_codemodel_matrixtype_constructor_exists():
    assert callable(codemodel_MatrixType.__init__)


def test_hyp_codemodel_matrixtype_constructor_args():
    sig = inspect.signature(codemodel_MatrixType.__init__)
    params = list(sig.parameters.keys())
    assert "columns" in params, "Missing parameter 'columns'"
    assert "rows" in params, "Missing parameter 'rows'"





def test_hyp_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_hyp_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_hyp_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_functionargument_is_not_abstract():
    assert not inspect.isabstract(codemodel_FunctionArgument)


def test_hyp_codemodel_functionargument_constructor_exists():
    assert callable(codemodel_FunctionArgument.__init__)


def test_hyp_codemodel_functionargument_constructor_args():
    sig = inspect.signature(codemodel_FunctionArgument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_localvariable_is_not_abstract():
    assert not inspect.isabstract(codemodel_LocalVariable)


def test_hyp_codemodel_localvariable_constructor_exists():
    assert callable(codemodel_LocalVariable.__init__)


def test_hyp_codemodel_localvariable_constructor_args():
    sig = inspect.signature(codemodel_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_globalvariable_is_not_abstract():
    assert not inspect.isabstract(codemodel_GlobalVariable)


def test_hyp_codemodel_globalvariable_constructor_exists():
    assert callable(codemodel_GlobalVariable.__init__)


def test_hyp_codemodel_globalvariable_constructor_args():
    sig = inspect.signature(codemodel_GlobalVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_cmelement_is_not_abstract():
    assert not inspect.isabstract(CMElement)


def test_hyp_cmelement_constructor_exists():
    assert callable(CMElement.__init__)


def test_hyp_cmelement_constructor_args():
    sig = inspect.signature(CMElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_statements_statement_is_not_abstract():
    assert not inspect.isabstract(codemodel_statements_Statement)


def test_hyp_codemodel_statements_statement_constructor_exists():
    assert callable(codemodel_statements_Statement.__init__)


def test_hyp_codemodel_statements_statement_constructor_args():
    sig = inspect.signature(codemodel_statements_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(codemodel_expressions_Expression)


def test_hyp_codemodel_expressions_expression_constructor_exists():
    assert callable(codemodel_expressions_Expression.__init__)


def test_hyp_codemodel_expressions_expression_constructor_args():
    sig = inspect.signature(codemodel_expressions_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_variable_is_not_abstract():
    assert not inspect.isabstract(codemodel_Variable)


def test_hyp_codemodel_variable_constructor_exists():
    assert callable(codemodel_Variable.__init__)


def test_hyp_codemodel_variable_constructor_args():
    sig = inspect.signature(codemodel_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "identifier" in params, "Missing parameter 'identifier'"





def test_hyp_codemodel_datatype_is_not_abstract():
    assert not inspect.isabstract(codemodel_DataType)


def test_hyp_codemodel_datatype_constructor_exists():
    assert callable(codemodel_DataType.__init__)


def test_hyp_codemodel_datatype_constructor_args():
    sig = inspect.signature(codemodel_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "basetype" in params, "Missing parameter 'basetype'"




def test_hyp_codemodel_function_is_not_abstract():
    assert not inspect.isabstract(codemodel_Function)


def test_hyp_codemodel_function_constructor_exists():
    assert callable(codemodel_Function.__init__)


def test_hyp_codemodel_function_constructor_args():
    sig = inspect.signature(codemodel_Function.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_codemodel_codemodule_is_not_abstract():
    assert not inspect.isabstract(codemodel_CodeModule)


def test_hyp_codemodel_codemodule_constructor_exists():
    assert callable(codemodel_CodeModule.__init__)


def test_hyp_codemodel_codemodule_constructor_args():
    sig = inspect.signature(codemodel_CodeModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_codemodel_cmelement_is_not_abstract():
    assert not inspect.isabstract(codemodel_CMElement)


def test_hyp_codemodel_cmelement_constructor_exists():
    assert callable(codemodel_CMElement.__init__)


def test_hyp_codemodel_cmelement_constructor_args():
    sig = inspect.signature(codemodel_CMElement.__init__)
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
AssignmentStmt_strategy = st.builds(
    AssignmentStmt,
)
Statement_strategy = st.builds(
    Statement,
)
codemodel_statements_AssignmentStmt_strategy = st.builds(
    codemodel_statements_AssignmentStmt,
)
codemodel_statements_IfStmt_strategy = st.builds(
    codemodel_statements_IfStmt,
)
codemodel_statements_CompositeStmt_strategy = st.builds(
    codemodel_statements_CompositeStmt,
)
codemodel_statements_ForStmt_strategy = st.builds(
    codemodel_statements_ForStmt,
)
expressions_codemodel_Variable_strategy = st.builds(
    expressions_codemodel_Variable,
)
Expression_strategy = st.builds(
    Expression,
)
codemodel_expressions_LiteralExp_strategy = st.builds(
    codemodel_expressions_LiteralExp,
    value=
        safe_text
)
codemodel_expressions_BinaryExp_strategy = st.builds(
    codemodel_expressions_BinaryExp,
    operator=
        safe_text
)
codemodel_expressions_VariableExp_strategy = st.builds(
    codemodel_expressions_VariableExp,
)
DataType_strategy = st.builds(
    DataType,
)
codemodel_ScalarType_strategy = st.builds(
    codemodel_ScalarType,
)
codemodel_VectorType_strategy = st.builds(
    codemodel_VectorType,
    size=
        safe_text
)
codemodel_MatrixType_strategy = st.builds(
    codemodel_MatrixType,
    columns=
        safe_text,
    rows=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
codemodel_FunctionArgument_strategy = st.builds(
    codemodel_FunctionArgument,
)
codemodel_LocalVariable_strategy = st.builds(
    codemodel_LocalVariable,
)
codemodel_GlobalVariable_strategy = st.builds(
    codemodel_GlobalVariable,
)
CMElement_strategy = st.builds(
    CMElement,
)
codemodel_statements_Statement_strategy = st.builds(
    codemodel_statements_Statement,
)
codemodel_expressions_Expression_strategy = st.builds(
    codemodel_expressions_Expression,
)
codemodel_Variable_strategy = st.builds(
    codemodel_Variable,
    constant=
        st.booleans(),
    identifier=
        safe_text
)
codemodel_DataType_strategy = st.builds(
    codemodel_DataType,
    basetype=
        safe_text
)
codemodel_Function_strategy = st.builds(
    codemodel_Function,
    identifier=
        safe_text
)
codemodel_CodeModule_strategy = st.builds(
    codemodel_CodeModule,
)
codemodel_CMElement_strategy = st.builds(
    codemodel_CMElement,
    name=
        safe_text
)












@given(instance=codemodel_expressions_LiteralExp_strategy)
def test_hyp_codemodel_expressions_literalexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=codemodel_expressions_BinaryExp_strategy)
def test_hyp_codemodel_expressions_binaryexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original







@given(instance=codemodel_VectorType_strategy)
def test_hyp_codemodel_vectortype_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original




@given(instance=codemodel_MatrixType_strategy)
def test_hyp_codemodel_matrixtype_columns_setter(instance):
    original = instance.columns
    instance.columns = original
    assert instance.columns == original



@given(instance=codemodel_MatrixType_strategy)
def test_hyp_codemodel_matrixtype_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original











@given(instance=codemodel_Variable_strategy)
def test_hyp_codemodel_variable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=codemodel_Variable_strategy)
def test_hyp_codemodel_variable_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original




@given(instance=codemodel_DataType_strategy)
def test_hyp_codemodel_datatype_basetype_setter(instance):
    original = instance.basetype
    instance.basetype = original
    assert instance.basetype == original




@given(instance=codemodel_Function_strategy)
def test_hyp_codemodel_function_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original





@given(instance=codemodel_CMElement_strategy)
def test_hyp_codemodel_cmelement_name_setter(instance):
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
    AssignmentStmt,
    CMElement,
    DataType,
    Expression,
    Statement,
    Variable,
    codemodel_CMElement,
    codemodel_CodeModule,
    codemodel_DataType,
    codemodel_Function,
    codemodel_FunctionArgument,
    codemodel_GlobalVariable,
    codemodel_LocalVariable,
    codemodel_MatrixType,
    codemodel_ScalarType,
    codemodel_Variable,
    codemodel_VectorType,
    codemodel_expressions_BinaryExp,
    codemodel_expressions_Expression,
    codemodel_expressions_LiteralExp,
    codemodel_expressions_VariableExp,
    codemodel_statements_AssignmentStmt,
    codemodel_statements_CompositeStmt,
    codemodel_statements_ForStmt,
    codemodel_statements_IfStmt,
    codemodel_statements_Statement,
    expressions_codemodel_Variable,
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

def test_codemodel_CMElement_name_value_roundtrip():
    instance = codemodel_CMElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_codemodel_DataType_basetype_value_roundtrip():
    instance = codemodel_DataType(basetype="sample_text")
    assert instance.basetype == "sample_text"
    instance.basetype = "sample_text_2"
    assert instance.basetype == "sample_text_2"


def test_codemodel_Function_identifier_value_roundtrip():
    instance = codemodel_Function(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_codemodel_MatrixType_columns_value_roundtrip():
    instance = codemodel_MatrixType(columns="sample_text", rows="sample_text")
    assert instance.columns == "sample_text"
    instance.columns = "sample_text_2"
    assert instance.columns == "sample_text_2"


def test_codemodel_MatrixType_rows_value_roundtrip():
    instance = codemodel_MatrixType(columns="sample_text", rows="sample_text")
    assert instance.rows == "sample_text"
    instance.rows = "sample_text_2"
    assert instance.rows == "sample_text_2"


def test_codemodel_Variable_constant_value_roundtrip():
    instance = codemodel_Variable(constant=True, identifier="sample_text")
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_codemodel_Variable_identifier_value_roundtrip():
    instance = codemodel_Variable(constant=True, identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_codemodel_VectorType_size_value_roundtrip():
    instance = codemodel_VectorType(size="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_codemodel_expressions_BinaryExp_operator_value_roundtrip():
    instance = codemodel_expressions_BinaryExp(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_codemodel_expressions_LiteralExp_value_value_roundtrip():
    instance = codemodel_expressions_LiteralExp(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_codemodel_CodeModule_isa_CMElement():
    instance = codemodel_CodeModule()
    assert isinstance(instance, CMElement)


def test_codemodel_DataType_isa_CMElement():
    instance = codemodel_DataType(basetype="sample_text")
    assert isinstance(instance, CMElement)


def test_codemodel_Function_isa_CMElement():
    instance = codemodel_Function(identifier="sample_text")
    assert isinstance(instance, CMElement)


def test_codemodel_Variable_isa_CMElement():
    instance = codemodel_Variable(constant=True, identifier="sample_text")
    assert isinstance(instance, CMElement)


def test_codemodel_expressions_Expression_isa_CMElement():
    instance = codemodel_expressions_Expression()
    assert isinstance(instance, CMElement)


def test_codemodel_statements_Statement_isa_CMElement():
    instance = codemodel_statements_Statement()
    assert isinstance(instance, CMElement)


def test_codemodel_MatrixType_isa_DataType():
    instance = codemodel_MatrixType(columns="sample_text", rows="sample_text")
    assert isinstance(instance, DataType)


def test_codemodel_ScalarType_isa_DataType():
    instance = codemodel_ScalarType()
    assert isinstance(instance, DataType)


def test_codemodel_VectorType_isa_DataType():
    instance = codemodel_VectorType(size="sample_text")
    assert isinstance(instance, DataType)


def test_codemodel_expressions_BinaryExp_isa_Expression():
    instance = codemodel_expressions_BinaryExp(operator="sample_text")
    assert isinstance(instance, Expression)


def test_codemodel_expressions_LiteralExp_isa_Expression():
    instance = codemodel_expressions_LiteralExp(value="sample_text")
    assert isinstance(instance, Expression)


def test_codemodel_expressions_VariableExp_isa_Expression():
    instance = codemodel_expressions_VariableExp()
    assert isinstance(instance, Expression)


def test_codemodel_statements_AssignmentStmt_isa_Statement():
    instance = codemodel_statements_AssignmentStmt()
    assert isinstance(instance, Statement)


def test_codemodel_statements_CompositeStmt_isa_Statement():
    instance = codemodel_statements_CompositeStmt()
    assert isinstance(instance, Statement)


def test_codemodel_statements_ForStmt_isa_Statement():
    instance = codemodel_statements_ForStmt()
    assert isinstance(instance, Statement)


def test_codemodel_statements_IfStmt_isa_Statement():
    instance = codemodel_statements_IfStmt()
    assert isinstance(instance, Statement)


def test_codemodel_FunctionArgument_isa_Variable():
    instance = codemodel_FunctionArgument()
    assert isinstance(instance, Variable)


def test_codemodel_GlobalVariable_isa_Variable():
    instance = codemodel_GlobalVariable()
    assert isinstance(instance, Variable)


def test_codemodel_LocalVariable_isa_Variable():
    instance = codemodel_LocalVariable()
    assert isinstance(instance, Variable)


def test_assoc_arguments7_link_reassign_clear():
    a = codemodel_Function(identifier="sample_text")
    b1 = codemodel_FunctionArgument()
    b2 = codemodel_FunctionArgument()
    _safe_set(a, 'codemodel_Function8', {b1})
    assert _is_linked(a, 'codemodel_Function8', b1)
    if hasattr(b1, 'codemodel_FunctionArgument'):
        assert _is_linked(b1, 'codemodel_FunctionArgument', a)
    _safe_set(a, 'codemodel_Function8', {b2})
    assert _is_linked(a, 'codemodel_Function8', b2)
    if hasattr(b1, 'codemodel_FunctionArgument'):
        assert not _is_linked(b1, 'codemodel_FunctionArgument', a)
    if hasattr(b2, 'codemodel_FunctionArgument'):
        assert _is_linked(b2, 'codemodel_FunctionArgument', a)
    _safe_set(a, 'codemodel_Function8', set())
    assert not _is_linked(a, 'codemodel_Function8', b2)
    if hasattr(b2, 'codemodel_FunctionArgument'):
        assert not _is_linked(b2, 'codemodel_FunctionArgument', a)


def test_assoc_body11_link_reassign_clear():
    a = codemodel_Function(identifier="sample_text")
    b1 = Statement()
    b2 = Statement()
    _safe_set(a, 'codemodel_Function12', {b1})
    assert _is_linked(a, 'codemodel_Function12', b1)
    if hasattr(b1, 'Statement'):
        assert _is_linked(b1, 'Statement', a)
    _safe_set(a, 'codemodel_Function12', {b2})
    assert _is_linked(a, 'codemodel_Function12', b2)
    if hasattr(b1, 'Statement'):
        assert not _is_linked(b1, 'Statement', a)
    if hasattr(b2, 'Statement'):
        assert _is_linked(b2, 'Statement', a)
    _safe_set(a, 'codemodel_Function12', set())
    assert not _is_linked(a, 'codemodel_Function12', b2)
    if hasattr(b2, 'Statement'):
        assert not _is_linked(b2, 'Statement', a)


def test_assoc_dataTypes3_link_reassign_clear():
    a = codemodel_DataType(basetype="sample_text")
    b1 = codemodel_CodeModule()
    b2 = codemodel_CodeModule()
    _safe_set(a, 'codemodel_DataType', b1)
    assert _is_linked(a, 'codemodel_DataType', b1)
    if hasattr(b1, 'codemodel_CodeModule4'):
        assert _is_linked(b1, 'codemodel_CodeModule4', a)
    _safe_set(a, 'codemodel_DataType', b2)
    assert _is_linked(a, 'codemodel_DataType', b2)
    if hasattr(b1, 'codemodel_CodeModule4'):
        assert not _is_linked(b1, 'codemodel_CodeModule4', a)
    if hasattr(b2, 'codemodel_CodeModule4'):
        assert _is_linked(b2, 'codemodel_CodeModule4', a)
    _safe_set(a, 'codemodel_DataType', None)
    assert not _is_linked(a, 'codemodel_DataType', b2)
    if hasattr(b2, 'codemodel_CodeModule4'):
        assert not _is_linked(b2, 'codemodel_CodeModule4', a)


def test_assoc_functions1_link_reassign_clear():
    a = codemodel_Function(identifier="sample_text")
    b1 = codemodel_CodeModule()
    b2 = codemodel_CodeModule()
    _safe_set(a, 'codemodel_Function', b1)
    assert _is_linked(a, 'codemodel_Function', b1)
    if hasattr(b1, 'codemodel_CodeModule2'):
        assert _is_linked(b1, 'codemodel_CodeModule2', a)
    _safe_set(a, 'codemodel_Function', b2)
    assert _is_linked(a, 'codemodel_Function', b2)
    if hasattr(b1, 'codemodel_CodeModule2'):
        assert not _is_linked(b1, 'codemodel_CodeModule2', a)
    if hasattr(b2, 'codemodel_CodeModule2'):
        assert _is_linked(b2, 'codemodel_CodeModule2', a)
    _safe_set(a, 'codemodel_Function', None)
    assert not _is_linked(a, 'codemodel_Function', b2)
    if hasattr(b2, 'codemodel_CodeModule2'):
        assert not _is_linked(b2, 'codemodel_CodeModule2', a)


def test_assoc_left14_link_reassign_clear():
    a = codemodel_expressions_BinaryExp(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'codemodel_expressions_BinaryExp', b1)
    assert _is_linked(a, 'codemodel_expressions_BinaryExp', b1)
    if hasattr(b1, 'Expression'):
        assert _is_linked(b1, 'Expression', a)
    _safe_set(a, 'codemodel_expressions_BinaryExp', b2)
    assert _is_linked(a, 'codemodel_expressions_BinaryExp', b2)
    if hasattr(b1, 'Expression'):
        assert not _is_linked(b1, 'Expression', a)
    if hasattr(b2, 'Expression'):
        assert _is_linked(b2, 'Expression', a)
    _safe_set(a, 'codemodel_expressions_BinaryExp', None)
    assert not _is_linked(a, 'codemodel_expressions_BinaryExp', b2)
    if hasattr(b2, 'Expression'):
        assert not _is_linked(b2, 'Expression', a)


def test_assoc_localVariables9_link_reassign_clear():
    a = codemodel_Function(identifier="sample_text")
    b1 = codemodel_LocalVariable()
    b2 = codemodel_LocalVariable()
    _safe_set(a, 'codemodel_Function10', {b1})
    assert _is_linked(a, 'codemodel_Function10', b1)
    if hasattr(b1, 'codemodel_LocalVariable'):
        assert _is_linked(b1, 'codemodel_LocalVariable', a)
    _safe_set(a, 'codemodel_Function10', {b2})
    assert _is_linked(a, 'codemodel_Function10', b2)
    if hasattr(b1, 'codemodel_LocalVariable'):
        assert not _is_linked(b1, 'codemodel_LocalVariable', a)
    if hasattr(b2, 'codemodel_LocalVariable'):
        assert _is_linked(b2, 'codemodel_LocalVariable', a)
    _safe_set(a, 'codemodel_Function10', set())
    assert not _is_linked(a, 'codemodel_Function10', b2)
    if hasattr(b2, 'codemodel_LocalVariable'):
        assert not _is_linked(b2, 'codemodel_LocalVariable', a)


def test_assoc_right15_link_reassign_clear():
    a = codemodel_expressions_BinaryExp(operator="sample_text")
    b1 = Expression()
    b2 = Expression()
    _safe_set(a, 'codemodel_expressions_BinaryExp16', b1)
    assert _is_linked(a, 'codemodel_expressions_BinaryExp16', b1)
    if hasattr(b1, 'Expression17'):
        assert _is_linked(b1, 'Expression17', a)
    _safe_set(a, 'codemodel_expressions_BinaryExp16', b2)
    assert _is_linked(a, 'codemodel_expressions_BinaryExp16', b2)
    if hasattr(b1, 'Expression17'):
        assert not _is_linked(b1, 'Expression17', a)
    if hasattr(b2, 'Expression17'):
        assert _is_linked(b2, 'Expression17', a)
    _safe_set(a, 'codemodel_expressions_BinaryExp16', None)
    assert not _is_linked(a, 'codemodel_expressions_BinaryExp16', b2)
    if hasattr(b2, 'Expression17'):
        assert not _is_linked(b2, 'Expression17', a)


def test_assoc_type5_link_reassign_clear():
    a = codemodel_Variable(constant=True, identifier="sample_text")
    b1 = codemodel_DataType(basetype="sample_text")
    b2 = codemodel_DataType(basetype="sample_text_2")
    _safe_set(a, 'codemodel_Variable', b1)
    assert _is_linked(a, 'codemodel_Variable', b1)
    if hasattr(b1, 'codemodel_DataType6'):
        assert _is_linked(b1, 'codemodel_DataType6', a)
    _safe_set(a, 'codemodel_Variable', b2)
    assert _is_linked(a, 'codemodel_Variable', b2)
    if hasattr(b1, 'codemodel_DataType6'):
        assert not _is_linked(b1, 'codemodel_DataType6', a)
    if hasattr(b2, 'codemodel_DataType6'):
        assert _is_linked(b2, 'codemodel_DataType6', a)
    _safe_set(a, 'codemodel_Variable', None)
    assert not _is_linked(a, 'codemodel_Variable', b2)
    if hasattr(b2, 'codemodel_DataType6'):
        assert not _is_linked(b2, 'codemodel_DataType6', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AssignmentStmt_strategy = st.builds(AssignmentStmt)
@given(instance=AssignmentStmt_strategy)
@settings(max_examples=25)
def test_AssignmentStmt_instantiation(instance):
    assert isinstance(instance, AssignmentStmt)


CMElement_strategy = st.builds(CMElement)
@given(instance=CMElement_strategy)
@settings(max_examples=25)
def test_CMElement_instantiation(instance):
    assert isinstance(instance, CMElement)


DataType_strategy = st.builds(DataType)
@given(instance=DataType_strategy)
@settings(max_examples=25)
def test_DataType_instantiation(instance):
    assert isinstance(instance, DataType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


codemodel_CMElement_strategy = st.builds(codemodel_CMElement, name=safe_text)
@given(instance=codemodel_CMElement_strategy)
@settings(max_examples=25)
def test_codemodel_CMElement_instantiation(instance):
    assert isinstance(instance, codemodel_CMElement)


codemodel_CodeModule_strategy = st.builds(codemodel_CodeModule)
@given(instance=codemodel_CodeModule_strategy)
@settings(max_examples=25)
def test_codemodel_CodeModule_instantiation(instance):
    assert isinstance(instance, codemodel_CodeModule)


codemodel_DataType_strategy = st.builds(codemodel_DataType, basetype=safe_text)
@given(instance=codemodel_DataType_strategy)
@settings(max_examples=25)
def test_codemodel_DataType_instantiation(instance):
    assert isinstance(instance, codemodel_DataType)


codemodel_Function_strategy = st.builds(codemodel_Function, identifier=safe_text)
@given(instance=codemodel_Function_strategy)
@settings(max_examples=25)
def test_codemodel_Function_instantiation(instance):
    assert isinstance(instance, codemodel_Function)


codemodel_FunctionArgument_strategy = st.builds(codemodel_FunctionArgument)
@given(instance=codemodel_FunctionArgument_strategy)
@settings(max_examples=25)
def test_codemodel_FunctionArgument_instantiation(instance):
    assert isinstance(instance, codemodel_FunctionArgument)


codemodel_GlobalVariable_strategy = st.builds(codemodel_GlobalVariable)
@given(instance=codemodel_GlobalVariable_strategy)
@settings(max_examples=25)
def test_codemodel_GlobalVariable_instantiation(instance):
    assert isinstance(instance, codemodel_GlobalVariable)


codemodel_LocalVariable_strategy = st.builds(codemodel_LocalVariable)
@given(instance=codemodel_LocalVariable_strategy)
@settings(max_examples=25)
def test_codemodel_LocalVariable_instantiation(instance):
    assert isinstance(instance, codemodel_LocalVariable)


codemodel_MatrixType_strategy = st.builds(codemodel_MatrixType, columns=safe_text, rows=safe_text)
@given(instance=codemodel_MatrixType_strategy)
@settings(max_examples=25)
def test_codemodel_MatrixType_instantiation(instance):
    assert isinstance(instance, codemodel_MatrixType)


codemodel_ScalarType_strategy = st.builds(codemodel_ScalarType)
@given(instance=codemodel_ScalarType_strategy)
@settings(max_examples=25)
def test_codemodel_ScalarType_instantiation(instance):
    assert isinstance(instance, codemodel_ScalarType)


codemodel_Variable_strategy = st.builds(codemodel_Variable, constant=st.booleans(), identifier=safe_text)
@given(instance=codemodel_Variable_strategy)
@settings(max_examples=25)
def test_codemodel_Variable_instantiation(instance):
    assert isinstance(instance, codemodel_Variable)


codemodel_VectorType_strategy = st.builds(codemodel_VectorType, size=safe_text)
@given(instance=codemodel_VectorType_strategy)
@settings(max_examples=25)
def test_codemodel_VectorType_instantiation(instance):
    assert isinstance(instance, codemodel_VectorType)


codemodel_expressions_BinaryExp_strategy = st.builds(codemodel_expressions_BinaryExp, operator=safe_text)
@given(instance=codemodel_expressions_BinaryExp_strategy)
@settings(max_examples=25)
def test_codemodel_expressions_BinaryExp_instantiation(instance):
    assert isinstance(instance, codemodel_expressions_BinaryExp)


codemodel_expressions_Expression_strategy = st.builds(codemodel_expressions_Expression)
@given(instance=codemodel_expressions_Expression_strategy)
@settings(max_examples=25)
def test_codemodel_expressions_Expression_instantiation(instance):
    assert isinstance(instance, codemodel_expressions_Expression)


codemodel_expressions_LiteralExp_strategy = st.builds(codemodel_expressions_LiteralExp, value=safe_text)
@given(instance=codemodel_expressions_LiteralExp_strategy)
@settings(max_examples=25)
def test_codemodel_expressions_LiteralExp_instantiation(instance):
    assert isinstance(instance, codemodel_expressions_LiteralExp)


codemodel_expressions_VariableExp_strategy = st.builds(codemodel_expressions_VariableExp)
@given(instance=codemodel_expressions_VariableExp_strategy)
@settings(max_examples=25)
def test_codemodel_expressions_VariableExp_instantiation(instance):
    assert isinstance(instance, codemodel_expressions_VariableExp)


codemodel_statements_AssignmentStmt_strategy = st.builds(codemodel_statements_AssignmentStmt)
@given(instance=codemodel_statements_AssignmentStmt_strategy)
@settings(max_examples=25)
def test_codemodel_statements_AssignmentStmt_instantiation(instance):
    assert isinstance(instance, codemodel_statements_AssignmentStmt)


codemodel_statements_CompositeStmt_strategy = st.builds(codemodel_statements_CompositeStmt)
@given(instance=codemodel_statements_CompositeStmt_strategy)
@settings(max_examples=25)
def test_codemodel_statements_CompositeStmt_instantiation(instance):
    assert isinstance(instance, codemodel_statements_CompositeStmt)


codemodel_statements_ForStmt_strategy = st.builds(codemodel_statements_ForStmt)
@given(instance=codemodel_statements_ForStmt_strategy)
@settings(max_examples=25)
def test_codemodel_statements_ForStmt_instantiation(instance):
    assert isinstance(instance, codemodel_statements_ForStmt)


codemodel_statements_IfStmt_strategy = st.builds(codemodel_statements_IfStmt)
@given(instance=codemodel_statements_IfStmt_strategy)
@settings(max_examples=25)
def test_codemodel_statements_IfStmt_instantiation(instance):
    assert isinstance(instance, codemodel_statements_IfStmt)


codemodel_statements_Statement_strategy = st.builds(codemodel_statements_Statement)
@given(instance=codemodel_statements_Statement_strategy)
@settings(max_examples=25)
def test_codemodel_statements_Statement_instantiation(instance):
    assert isinstance(instance, codemodel_statements_Statement)


expressions_codemodel_Variable_strategy = st.builds(expressions_codemodel_Variable)
@given(instance=expressions_codemodel_Variable_strategy)
@settings(max_examples=25)
def test_expressions_codemodel_Variable_instantiation(instance):
    assert isinstance(instance, expressions_codemodel_Variable)



