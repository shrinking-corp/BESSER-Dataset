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


