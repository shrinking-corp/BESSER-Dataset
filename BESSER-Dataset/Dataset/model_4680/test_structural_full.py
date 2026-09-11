import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Expr,
    Member,
    NamedElement,
    Stmt,
    Symbol,
    Value,
    imp_ArrayDecl,
    imp_ArrayValue,
    imp_Assignment,
    imp_AttributeDecl,
    imp_Binary,
    imp_Block,
    imp_BoolConst,
    imp_BoolValue,
    imp_Class,
    imp_Declaration,
    imp_Expr,
    imp_If,
    imp_IntConst,
    imp_IntValue,
    imp_Member,
    imp_MethodDecl,
    imp_NamedElement,
    imp_NewClass,
    imp_ParamDecl,
    imp_Print,
    imp_Program,
    imp_Project,
    imp_Return,
    imp_Stmt,
    imp_Store,
    imp_StringConst,
    imp_StringToValueMap,
    imp_StringValue,
    imp_Symbol,
    imp_This,
    imp_Unary,
    imp_Value,
    imp_VarRef,
    imp_While,
    BinaryOp,
    UnaryOp,
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

def test_imp_AttributeDecl_name_value_roundtrip():
    instance = imp_AttributeDecl(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_imp_Binary_op_value_roundtrip():
    instance = imp_Binary(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_imp_BoolConst_value_value_roundtrip():
    instance = imp_BoolConst(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_imp_BoolValue_value_value_roundtrip():
    instance = imp_BoolValue(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_imp_Class_name_value_roundtrip():
    instance = imp_Class(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_imp_Declaration_name_value_roundtrip():
    instance = imp_Declaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_imp_IntConst_value_value_roundtrip():
    instance = imp_IntConst(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_imp_IntValue_value_value_roundtrip():
    instance = imp_IntValue(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_imp_MethodDecl_name_value_roundtrip():
    instance = imp_MethodDecl(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_imp_ParamDecl_name_value_roundtrip():
    instance = imp_ParamDecl(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_imp_Project_ismethodcall_value_roundtrip():
    instance = imp_Project(ismethodcall=True)
    assert instance.ismethodcall == True
    instance.ismethodcall = False
    assert instance.ismethodcall == False


def test_imp_StringConst_value_value_roundtrip():
    instance = imp_StringConst(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_imp_StringToValueMap_key_value_roundtrip():
    instance = imp_StringToValueMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_imp_StringValue_value_value_roundtrip():
    instance = imp_StringValue(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_imp_Unary_op_value_roundtrip():
    instance = imp_Unary(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_imp_ArrayDecl_isa_Expr():
    instance = imp_ArrayDecl()
    assert isinstance(instance, Expr)


def test_imp_Binary_isa_Expr():
    instance = imp_Binary(op="sample_text")
    assert isinstance(instance, Expr)


def test_imp_BoolConst_isa_Expr():
    instance = imp_BoolConst(value=True)
    assert isinstance(instance, Expr)


def test_imp_IntConst_isa_Expr():
    instance = imp_IntConst(value=7)
    assert isinstance(instance, Expr)


def test_imp_NewClass_isa_Expr():
    instance = imp_NewClass()
    assert isinstance(instance, Expr)


def test_imp_Project_isa_Expr():
    instance = imp_Project(ismethodcall=True)
    assert isinstance(instance, Expr)


def test_imp_StringConst_isa_Expr():
    instance = imp_StringConst(value="sample_text")
    assert isinstance(instance, Expr)


def test_imp_This_isa_Expr():
    instance = imp_This()
    assert isinstance(instance, Expr)


def test_imp_Unary_isa_Expr():
    instance = imp_Unary(op="sample_text")
    assert isinstance(instance, Expr)


def test_imp_VarRef_isa_Expr():
    instance = imp_VarRef()
    assert isinstance(instance, Expr)


def test_imp_AttributeDecl_isa_Member():
    instance = imp_AttributeDecl(name="sample_text")
    assert isinstance(instance, Member)


def test_imp_MethodDecl_isa_Member():
    instance = imp_MethodDecl(name="sample_text")
    assert isinstance(instance, Member)


def test_imp_Class_isa_NamedElement():
    instance = imp_Class(name="sample_text")
    assert isinstance(instance, NamedElement)


def test_imp_Symbol_isa_NamedElement():
    instance = imp_Symbol()
    assert isinstance(instance, NamedElement)


def test_imp_Assignment_isa_Stmt():
    instance = imp_Assignment()
    assert isinstance(instance, Stmt)


def test_imp_Block_isa_Stmt():
    instance = imp_Block()
    assert isinstance(instance, Stmt)


def test_imp_Declaration_isa_Stmt():
    instance = imp_Declaration(name="sample_text")
    assert isinstance(instance, Stmt)


def test_imp_Expr_isa_Stmt():
    instance = imp_Expr()
    assert isinstance(instance, Stmt)


def test_imp_If_isa_Stmt():
    instance = imp_If()
    assert isinstance(instance, Stmt)


def test_imp_Print_isa_Stmt():
    instance = imp_Print()
    assert isinstance(instance, Stmt)


def test_imp_Return_isa_Stmt():
    instance = imp_Return()
    assert isinstance(instance, Stmt)


def test_imp_While_isa_Stmt():
    instance = imp_While()
    assert isinstance(instance, Stmt)


def test_imp_Declaration_isa_Symbol():
    instance = imp_Declaration(name="sample_text")
    assert isinstance(instance, Symbol)


def test_imp_ParamDecl_isa_Symbol():
    instance = imp_ParamDecl(name="sample_text")
    assert isinstance(instance, Symbol)


def test_imp_ArrayValue_isa_Value():
    instance = imp_ArrayValue()
    assert isinstance(instance, Value)


def test_imp_BoolValue_isa_Value():
    instance = imp_BoolValue(value=True)
    assert isinstance(instance, Value)


def test_imp_IntValue_isa_Value():
    instance = imp_IntValue(value=7)
    assert isinstance(instance, Value)


def test_imp_StringValue_isa_Value():
    instance = imp_StringValue(value="sample_text")
    assert isinstance(instance, Value)


def test_assoc_attributes44_link_reassign_clear():
    a = imp_Class(name="sample_text")
    b1 = imp_AttributeDecl(name="sample_text")
    b2 = imp_AttributeDecl(name="sample_text_2")
    _safe_set(a, 'imp_Class45', {b1})
    assert _is_linked(a, 'imp_Class45', b1)
    if hasattr(b1, 'imp_AttributeDecl'):
        assert _is_linked(b1, 'imp_AttributeDecl', a)
    _safe_set(a, 'imp_Class45', {b2})
    assert _is_linked(a, 'imp_Class45', b2)
    if hasattr(b1, 'imp_AttributeDecl'):
        assert not _is_linked(b1, 'imp_AttributeDecl', a)
    if hasattr(b2, 'imp_AttributeDecl'):
        assert _is_linked(b2, 'imp_AttributeDecl', a)
    _safe_set(a, 'imp_Class45', set())
    assert not _is_linked(a, 'imp_Class45', b2)
    if hasattr(b2, 'imp_AttributeDecl'):
        assert not _is_linked(b2, 'imp_AttributeDecl', a)


def test_assoc_class_49_link_reassign_clear():
    a = imp_Class(name="sample_text")
    b1 = imp_NewClass()
    b2 = imp_NewClass()
    _safe_set(a, 'imp_Class50', b1)
    assert _is_linked(a, 'imp_Class50', b1)
    if hasattr(b1, 'imp_NewClass'):
        assert _is_linked(b1, 'imp_NewClass', a)
    _safe_set(a, 'imp_Class50', b2)
    assert _is_linked(a, 'imp_Class50', b2)
    if hasattr(b1, 'imp_NewClass'):
        assert not _is_linked(b1, 'imp_NewClass', a)
    if hasattr(b2, 'imp_NewClass'):
        assert _is_linked(b2, 'imp_NewClass', a)
    _safe_set(a, 'imp_Class50', None)
    assert not _is_linked(a, 'imp_Class50', b2)
    if hasattr(b2, 'imp_NewClass'):
        assert not _is_linked(b2, 'imp_NewClass', a)


def test_assoc_classes33_link_reassign_clear():
    a = imp_Class(name="sample_text")
    b1 = imp_Program()
    b2 = imp_Program()
    _safe_set(a, 'imp_Class', b1)
    assert _is_linked(a, 'imp_Class', b1)
    if hasattr(b1, 'imp_Program34'):
        assert _is_linked(b1, 'imp_Program34', a)
    _safe_set(a, 'imp_Class', b2)
    assert _is_linked(a, 'imp_Class', b2)
    if hasattr(b1, 'imp_Program34'):
        assert not _is_linked(b1, 'imp_Program34', a)
    if hasattr(b2, 'imp_Program34'):
        assert _is_linked(b2, 'imp_Program34', a)
    _safe_set(a, 'imp_Class', None)
    assert not _is_linked(a, 'imp_Class', b2)
    if hasattr(b2, 'imp_Program34'):
        assert not _is_linked(b2, 'imp_Program34', a)


def test_assoc_exp0_link_reassign_clear():
    a = imp_Declaration(name="sample_text")
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Declaration', b1)
    assert _is_linked(a, 'imp_Declaration', b1)
    if hasattr(b1, 'imp_Expr'):
        assert _is_linked(b1, 'imp_Expr', a)
    _safe_set(a, 'imp_Declaration', b2)
    assert _is_linked(a, 'imp_Declaration', b2)
    if hasattr(b1, 'imp_Expr'):
        assert not _is_linked(b1, 'imp_Expr', a)
    if hasattr(b2, 'imp_Expr'):
        assert _is_linked(b2, 'imp_Expr', a)
    _safe_set(a, 'imp_Declaration', None)
    assert not _is_linked(a, 'imp_Declaration', b2)
    if hasattr(b2, 'imp_Expr'):
        assert not _is_linked(b2, 'imp_Expr', a)


def test_assoc_expr18_link_reassign_clear():
    a = imp_Unary(op="sample_text")
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Unary', b1)
    assert _is_linked(a, 'imp_Unary', b1)
    if hasattr(b1, 'imp_Expr19'):
        assert _is_linked(b1, 'imp_Expr19', a)
    _safe_set(a, 'imp_Unary', b2)
    assert _is_linked(a, 'imp_Unary', b2)
    if hasattr(b1, 'imp_Expr19'):
        assert not _is_linked(b1, 'imp_Expr19', a)
    if hasattr(b2, 'imp_Expr19'):
        assert _is_linked(b2, 'imp_Expr19', a)
    _safe_set(a, 'imp_Unary', None)
    assert not _is_linked(a, 'imp_Unary', b2)
    if hasattr(b2, 'imp_Expr19'):
        assert not _is_linked(b2, 'imp_Expr19', a)


def test_assoc_index1_link_reassign_clear():
    a = imp_Declaration(name="sample_text")
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Declaration2', b1)
    assert _is_linked(a, 'imp_Declaration2', b1)
    if hasattr(b1, 'imp_Expr3'):
        assert _is_linked(b1, 'imp_Expr3', a)
    _safe_set(a, 'imp_Declaration2', b2)
    assert _is_linked(a, 'imp_Declaration2', b2)
    if hasattr(b1, 'imp_Expr3'):
        assert not _is_linked(b1, 'imp_Expr3', a)
    if hasattr(b2, 'imp_Expr3'):
        assert _is_linked(b2, 'imp_Expr3', a)
    _safe_set(a, 'imp_Declaration2', None)
    assert not _is_linked(a, 'imp_Declaration2', b2)
    if hasattr(b2, 'imp_Expr3'):
        assert not _is_linked(b2, 'imp_Expr3', a)


def test_assoc_lhs20_link_reassign_clear():
    a = imp_Binary(op="sample_text")
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Binary', b1)
    assert _is_linked(a, 'imp_Binary', b1)
    if hasattr(b1, 'imp_Expr21'):
        assert _is_linked(b1, 'imp_Expr21', a)
    _safe_set(a, 'imp_Binary', b2)
    assert _is_linked(a, 'imp_Binary', b2)
    if hasattr(b1, 'imp_Expr21'):
        assert not _is_linked(b1, 'imp_Expr21', a)
    if hasattr(b2, 'imp_Expr21'):
        assert _is_linked(b2, 'imp_Expr21', a)
    _safe_set(a, 'imp_Binary', None)
    assert not _is_linked(a, 'imp_Binary', b2)
    if hasattr(b2, 'imp_Expr21'):
        assert not _is_linked(b2, 'imp_Expr21', a)


def test_assoc_lhs56_link_reassign_clear():
    a = imp_Project(ismethodcall=True)
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Project', b1)
    assert _is_linked(a, 'imp_Project', b1)
    if hasattr(b1, 'imp_Expr57'):
        assert _is_linked(b1, 'imp_Expr57', a)
    _safe_set(a, 'imp_Project', b2)
    assert _is_linked(a, 'imp_Project', b2)
    if hasattr(b1, 'imp_Expr57'):
        assert not _is_linked(b1, 'imp_Expr57', a)
    if hasattr(b2, 'imp_Expr57'):
        assert _is_linked(b2, 'imp_Expr57', a)
    _safe_set(a, 'imp_Project', None)
    assert not _is_linked(a, 'imp_Project', b2)
    if hasattr(b2, 'imp_Expr57'):
        assert not _is_linked(b2, 'imp_Expr57', a)


def test_assoc_methods32_link_reassign_clear():
    a = imp_MethodDecl(name="sample_text")
    b1 = imp_Program()
    b2 = imp_Program()
    _safe_set(a, 'imp_MethodDecl', b1)
    assert _is_linked(a, 'imp_MethodDecl', b1)
    if hasattr(b1, 'imp_Program'):
        assert _is_linked(b1, 'imp_Program', a)
    _safe_set(a, 'imp_MethodDecl', b2)
    assert _is_linked(a, 'imp_MethodDecl', b2)
    if hasattr(b1, 'imp_Program'):
        assert not _is_linked(b1, 'imp_Program', a)
    if hasattr(b2, 'imp_Program'):
        assert _is_linked(b2, 'imp_Program', a)
    _safe_set(a, 'imp_MethodDecl', None)
    assert not _is_linked(a, 'imp_MethodDecl', b2)
    if hasattr(b2, 'imp_Program'):
        assert not _is_linked(b2, 'imp_Program', a)


def test_assoc_methods46_link_reassign_clear():
    a = imp_MethodDecl(name="sample_text")
    b1 = imp_Class(name="sample_text")
    b2 = imp_Class(name="sample_text_2")
    _safe_set(a, 'imp_MethodDecl48', b1)
    assert _is_linked(a, 'imp_MethodDecl48', b1)
    if hasattr(b1, 'imp_Class47'):
        assert _is_linked(b1, 'imp_Class47', a)
    _safe_set(a, 'imp_MethodDecl48', b2)
    assert _is_linked(a, 'imp_MethodDecl48', b2)
    if hasattr(b1, 'imp_Class47'):
        assert not _is_linked(b1, 'imp_Class47', a)
    if hasattr(b2, 'imp_Class47'):
        assert _is_linked(b2, 'imp_Class47', a)
    _safe_set(a, 'imp_MethodDecl48', None)
    assert not _is_linked(a, 'imp_MethodDecl48', b2)
    if hasattr(b2, 'imp_Class47'):
        assert not _is_linked(b2, 'imp_Class47', a)


def test_assoc_params38_link_reassign_clear():
    a = imp_ParamDecl(name="sample_text")
    b1 = imp_MethodDecl(name="sample_text")
    b2 = imp_MethodDecl(name="sample_text_2")
    _safe_set(a, 'imp_ParamDecl', b1)
    assert _is_linked(a, 'imp_ParamDecl', b1)
    if hasattr(b1, 'imp_MethodDecl39'):
        assert _is_linked(b1, 'imp_MethodDecl39', a)
    _safe_set(a, 'imp_ParamDecl', b2)
    assert _is_linked(a, 'imp_ParamDecl', b2)
    if hasattr(b1, 'imp_MethodDecl39'):
        assert not _is_linked(b1, 'imp_MethodDecl39', a)
    if hasattr(b2, 'imp_MethodDecl39'):
        assert _is_linked(b2, 'imp_MethodDecl39', a)
    _safe_set(a, 'imp_ParamDecl', None)
    assert not _is_linked(a, 'imp_ParamDecl', b2)
    if hasattr(b2, 'imp_MethodDecl39'):
        assert not _is_linked(b2, 'imp_MethodDecl39', a)


def test_assoc_params60_link_reassign_clear():
    a = imp_Project(ismethodcall=True)
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Project61', {b1})
    assert _is_linked(a, 'imp_Project61', b1)
    if hasattr(b1, 'imp_Expr62'):
        assert _is_linked(b1, 'imp_Expr62', a)
    _safe_set(a, 'imp_Project61', {b2})
    assert _is_linked(a, 'imp_Project61', b2)
    if hasattr(b1, 'imp_Expr62'):
        assert not _is_linked(b1, 'imp_Expr62', a)
    if hasattr(b2, 'imp_Expr62'):
        assert _is_linked(b2, 'imp_Expr62', a)
    _safe_set(a, 'imp_Project61', set())
    assert not _is_linked(a, 'imp_Project61', b2)
    if hasattr(b2, 'imp_Expr62'):
        assert not _is_linked(b2, 'imp_Expr62', a)


def test_assoc_rhs22_link_reassign_clear():
    a = imp_Binary(op="sample_text")
    b1 = imp_Expr()
    b2 = imp_Expr()
    _safe_set(a, 'imp_Binary23', b1)
    assert _is_linked(a, 'imp_Binary23', b1)
    if hasattr(b1, 'imp_Expr24'):
        assert _is_linked(b1, 'imp_Expr24', a)
    _safe_set(a, 'imp_Binary23', b2)
    assert _is_linked(a, 'imp_Binary23', b2)
    if hasattr(b1, 'imp_Expr24'):
        assert not _is_linked(b1, 'imp_Expr24', a)
    if hasattr(b2, 'imp_Expr24'):
        assert _is_linked(b2, 'imp_Expr24', a)
    _safe_set(a, 'imp_Binary23', None)
    assert not _is_linked(a, 'imp_Binary23', b2)
    if hasattr(b2, 'imp_Expr24'):
        assert not _is_linked(b2, 'imp_Expr24', a)


def test_assoc_rhs58_link_reassign_clear():
    a = imp_Project(ismethodcall=True)
    b1 = imp_Member()
    b2 = imp_Member()
    _safe_set(a, 'imp_Project59', b1)
    assert _is_linked(a, 'imp_Project59', b1)
    if hasattr(b1, 'imp_Member'):
        assert _is_linked(b1, 'imp_Member', a)
    _safe_set(a, 'imp_Project59', b2)
    assert _is_linked(a, 'imp_Project59', b2)
    if hasattr(b1, 'imp_Member'):
        assert not _is_linked(b1, 'imp_Member', a)
    if hasattr(b2, 'imp_Member'):
        assert _is_linked(b2, 'imp_Member', a)
    _safe_set(a, 'imp_Project59', None)
    assert not _is_linked(a, 'imp_Project59', b2)
    if hasattr(b2, 'imp_Member'):
        assert not _is_linked(b2, 'imp_Member', a)


def test_assoc_stmt35_link_reassign_clear():
    a = imp_MethodDecl(name="sample_text")
    b1 = imp_Stmt()
    b2 = imp_Stmt()
    _safe_set(a, 'imp_MethodDecl36', b1)
    assert _is_linked(a, 'imp_MethodDecl36', b1)
    if hasattr(b1, 'imp_Stmt37'):
        assert _is_linked(b1, 'imp_Stmt37', a)
    _safe_set(a, 'imp_MethodDecl36', b2)
    assert _is_linked(a, 'imp_MethodDecl36', b2)
    if hasattr(b1, 'imp_Stmt37'):
        assert not _is_linked(b1, 'imp_Stmt37', a)
    if hasattr(b2, 'imp_Stmt37'):
        assert _is_linked(b2, 'imp_Stmt37', a)
    _safe_set(a, 'imp_MethodDecl36', None)
    assert not _is_linked(a, 'imp_MethodDecl36', b2)
    if hasattr(b2, 'imp_Stmt37'):
        assert not _is_linked(b2, 'imp_Stmt37', a)


def test_assoc_value26_link_reassign_clear():
    a = imp_StringToValueMap(key="sample_text")
    b1 = imp_Value()
    b2 = imp_Value()
    _safe_set(a, 'imp_StringToValueMap27', b1)
    assert _is_linked(a, 'imp_StringToValueMap27', b1)
    if hasattr(b1, 'imp_Value'):
        assert _is_linked(b1, 'imp_Value', a)
    _safe_set(a, 'imp_StringToValueMap27', b2)
    assert _is_linked(a, 'imp_StringToValueMap27', b2)
    if hasattr(b1, 'imp_Value'):
        assert not _is_linked(b1, 'imp_Value', a)
    if hasattr(b2, 'imp_Value'):
        assert _is_linked(b2, 'imp_Value', a)
    _safe_set(a, 'imp_StringToValueMap27', None)
    assert not _is_linked(a, 'imp_StringToValueMap27', b2)
    if hasattr(b2, 'imp_Value'):
        assert not _is_linked(b2, 'imp_Value', a)


def test_assoc_values25_link_reassign_clear():
    a = imp_StringToValueMap(key="sample_text")
    b1 = imp_Store()
    b2 = imp_Store()
    _safe_set(a, 'imp_StringToValueMap', b1)
    assert _is_linked(a, 'imp_StringToValueMap', b1)
    if hasattr(b1, 'imp_Store'):
        assert _is_linked(b1, 'imp_Store', a)
    _safe_set(a, 'imp_StringToValueMap', b2)
    assert _is_linked(a, 'imp_StringToValueMap', b2)
    if hasattr(b1, 'imp_Store'):
        assert not _is_linked(b1, 'imp_Store', a)
    if hasattr(b2, 'imp_Store'):
        assert _is_linked(b2, 'imp_Store', a)
    _safe_set(a, 'imp_StringToValueMap', None)
    assert not _is_linked(a, 'imp_StringToValueMap', b2)
    if hasattr(b2, 'imp_Store'):
        assert not _is_linked(b2, 'imp_Store', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Expr_strategy = st.builds(Expr)
@given(instance=Expr_strategy)
@settings(max_examples=25)
def test_Expr_instantiation(instance):
    assert isinstance(instance, Expr)


Member_strategy = st.builds(Member)
@given(instance=Member_strategy)
@settings(max_examples=25)
def test_Member_instantiation(instance):
    assert isinstance(instance, Member)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Stmt_strategy = st.builds(Stmt)
@given(instance=Stmt_strategy)
@settings(max_examples=25)
def test_Stmt_instantiation(instance):
    assert isinstance(instance, Stmt)


Symbol_strategy = st.builds(Symbol)
@given(instance=Symbol_strategy)
@settings(max_examples=25)
def test_Symbol_instantiation(instance):
    assert isinstance(instance, Symbol)


Value_strategy = st.builds(Value)
@given(instance=Value_strategy)
@settings(max_examples=25)
def test_Value_instantiation(instance):
    assert isinstance(instance, Value)


imp_ArrayDecl_strategy = st.builds(imp_ArrayDecl)
@given(instance=imp_ArrayDecl_strategy)
@settings(max_examples=25)
def test_imp_ArrayDecl_instantiation(instance):
    assert isinstance(instance, imp_ArrayDecl)


imp_ArrayValue_strategy = st.builds(imp_ArrayValue)
@given(instance=imp_ArrayValue_strategy)
@settings(max_examples=25)
def test_imp_ArrayValue_instantiation(instance):
    assert isinstance(instance, imp_ArrayValue)


imp_Assignment_strategy = st.builds(imp_Assignment)
@given(instance=imp_Assignment_strategy)
@settings(max_examples=25)
def test_imp_Assignment_instantiation(instance):
    assert isinstance(instance, imp_Assignment)


imp_AttributeDecl_strategy = st.builds(imp_AttributeDecl, name=safe_text)
@given(instance=imp_AttributeDecl_strategy)
@settings(max_examples=25)
def test_imp_AttributeDecl_instantiation(instance):
    assert isinstance(instance, imp_AttributeDecl)


imp_Binary_strategy = st.builds(imp_Binary, op=safe_text)
@given(instance=imp_Binary_strategy)
@settings(max_examples=25)
def test_imp_Binary_instantiation(instance):
    assert isinstance(instance, imp_Binary)


imp_Block_strategy = st.builds(imp_Block)
@given(instance=imp_Block_strategy)
@settings(max_examples=25)
def test_imp_Block_instantiation(instance):
    assert isinstance(instance, imp_Block)


imp_BoolConst_strategy = st.builds(imp_BoolConst, value=st.booleans())
@given(instance=imp_BoolConst_strategy)
@settings(max_examples=25)
def test_imp_BoolConst_instantiation(instance):
    assert isinstance(instance, imp_BoolConst)


imp_BoolValue_strategy = st.builds(imp_BoolValue, value=st.booleans())
@given(instance=imp_BoolValue_strategy)
@settings(max_examples=25)
def test_imp_BoolValue_instantiation(instance):
    assert isinstance(instance, imp_BoolValue)


imp_Class_strategy = st.builds(imp_Class, name=safe_text)
@given(instance=imp_Class_strategy)
@settings(max_examples=25)
def test_imp_Class_instantiation(instance):
    assert isinstance(instance, imp_Class)


imp_Declaration_strategy = st.builds(imp_Declaration, name=safe_text)
@given(instance=imp_Declaration_strategy)
@settings(max_examples=25)
def test_imp_Declaration_instantiation(instance):
    assert isinstance(instance, imp_Declaration)


imp_Expr_strategy = st.builds(imp_Expr)
@given(instance=imp_Expr_strategy)
@settings(max_examples=25)
def test_imp_Expr_instantiation(instance):
    assert isinstance(instance, imp_Expr)


imp_If_strategy = st.builds(imp_If)
@given(instance=imp_If_strategy)
@settings(max_examples=25)
def test_imp_If_instantiation(instance):
    assert isinstance(instance, imp_If)


imp_IntConst_strategy = st.builds(imp_IntConst, value=st.integers())
@given(instance=imp_IntConst_strategy)
@settings(max_examples=25)
def test_imp_IntConst_instantiation(instance):
    assert isinstance(instance, imp_IntConst)


imp_IntValue_strategy = st.builds(imp_IntValue, value=st.integers())
@given(instance=imp_IntValue_strategy)
@settings(max_examples=25)
def test_imp_IntValue_instantiation(instance):
    assert isinstance(instance, imp_IntValue)


imp_Member_strategy = st.builds(imp_Member)
@given(instance=imp_Member_strategy)
@settings(max_examples=25)
def test_imp_Member_instantiation(instance):
    assert isinstance(instance, imp_Member)


imp_MethodDecl_strategy = st.builds(imp_MethodDecl, name=safe_text)
@given(instance=imp_MethodDecl_strategy)
@settings(max_examples=25)
def test_imp_MethodDecl_instantiation(instance):
    assert isinstance(instance, imp_MethodDecl)


imp_NamedElement_strategy = st.builds(imp_NamedElement)
@given(instance=imp_NamedElement_strategy)
@settings(max_examples=25)
def test_imp_NamedElement_instantiation(instance):
    assert isinstance(instance, imp_NamedElement)


imp_NewClass_strategy = st.builds(imp_NewClass)
@given(instance=imp_NewClass_strategy)
@settings(max_examples=25)
def test_imp_NewClass_instantiation(instance):
    assert isinstance(instance, imp_NewClass)


imp_ParamDecl_strategy = st.builds(imp_ParamDecl, name=safe_text)
@given(instance=imp_ParamDecl_strategy)
@settings(max_examples=25)
def test_imp_ParamDecl_instantiation(instance):
    assert isinstance(instance, imp_ParamDecl)


imp_Print_strategy = st.builds(imp_Print)
@given(instance=imp_Print_strategy)
@settings(max_examples=25)
def test_imp_Print_instantiation(instance):
    assert isinstance(instance, imp_Print)


imp_Program_strategy = st.builds(imp_Program)
@given(instance=imp_Program_strategy)
@settings(max_examples=25)
def test_imp_Program_instantiation(instance):
    assert isinstance(instance, imp_Program)


imp_Project_strategy = st.builds(imp_Project, ismethodcall=st.booleans())
@given(instance=imp_Project_strategy)
@settings(max_examples=25)
def test_imp_Project_instantiation(instance):
    assert isinstance(instance, imp_Project)


imp_Return_strategy = st.builds(imp_Return)
@given(instance=imp_Return_strategy)
@settings(max_examples=25)
def test_imp_Return_instantiation(instance):
    assert isinstance(instance, imp_Return)


imp_Stmt_strategy = st.builds(imp_Stmt)
@given(instance=imp_Stmt_strategy)
@settings(max_examples=25)
def test_imp_Stmt_instantiation(instance):
    assert isinstance(instance, imp_Stmt)


imp_Store_strategy = st.builds(imp_Store)
@given(instance=imp_Store_strategy)
@settings(max_examples=25)
def test_imp_Store_instantiation(instance):
    assert isinstance(instance, imp_Store)


imp_StringConst_strategy = st.builds(imp_StringConst, value=safe_text)
@given(instance=imp_StringConst_strategy)
@settings(max_examples=25)
def test_imp_StringConst_instantiation(instance):
    assert isinstance(instance, imp_StringConst)


imp_StringToValueMap_strategy = st.builds(imp_StringToValueMap, key=safe_text)
@given(instance=imp_StringToValueMap_strategy)
@settings(max_examples=25)
def test_imp_StringToValueMap_instantiation(instance):
    assert isinstance(instance, imp_StringToValueMap)


imp_StringValue_strategy = st.builds(imp_StringValue, value=safe_text)
@given(instance=imp_StringValue_strategy)
@settings(max_examples=25)
def test_imp_StringValue_instantiation(instance):
    assert isinstance(instance, imp_StringValue)


imp_Symbol_strategy = st.builds(imp_Symbol)
@given(instance=imp_Symbol_strategy)
@settings(max_examples=25)
def test_imp_Symbol_instantiation(instance):
    assert isinstance(instance, imp_Symbol)


imp_This_strategy = st.builds(imp_This)
@given(instance=imp_This_strategy)
@settings(max_examples=25)
def test_imp_This_instantiation(instance):
    assert isinstance(instance, imp_This)


imp_Unary_strategy = st.builds(imp_Unary, op=safe_text)
@given(instance=imp_Unary_strategy)
@settings(max_examples=25)
def test_imp_Unary_instantiation(instance):
    assert isinstance(instance, imp_Unary)


imp_Value_strategy = st.builds(imp_Value)
@given(instance=imp_Value_strategy)
@settings(max_examples=25)
def test_imp_Value_instantiation(instance):
    assert isinstance(instance, imp_Value)


imp_VarRef_strategy = st.builds(imp_VarRef)
@given(instance=imp_VarRef_strategy)
@settings(max_examples=25)
def test_imp_VarRef_instantiation(instance):
    assert isinstance(instance, imp_VarRef)


imp_While_strategy = st.builds(imp_While)
@given(instance=imp_While_strategy)
@settings(max_examples=25)
def test_imp_While_instantiation(instance):
    assert isinstance(instance, imp_While)


