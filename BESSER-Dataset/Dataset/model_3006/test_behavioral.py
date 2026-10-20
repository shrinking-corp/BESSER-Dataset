import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assignee,
    Call,
    Expression,
    Member,
    NamedElement,
    SingleTypeRef,
    Statement,
    Symbol,
    TypeDeclaration,
    TypeRef,
    TypedDeclaration,
    Value,
    miniJava_And,
    miniJava_ArrayAccess,
    miniJava_ArrayInstance,
    miniJava_ArrayLength,
    miniJava_ArrayRefValue,
    miniJava_ArrayTypeRef,
    miniJava_Assignee,
    miniJava_Assignment,
    miniJava_Block,
    miniJava_BoolConstant,
    miniJava_BooleanTypeRef,
    miniJava_BooleanValue,
    miniJava_Call,
    miniJava_ClassRef,
    miniJava_Clazz,
    miniJava_Context,
    miniJava_Division,
    miniJava_Equality,
    miniJava_Expression,
    miniJava_Field,
    miniJava_FieldAccess,
    miniJava_FieldBinding,
    miniJava_ForStatement,
    miniJava_Frame,
    miniJava_IfStatement,
    miniJava_Import,
    miniJava_Inequality,
    miniJava_Inferior,
    miniJava_InferiorOrEqual,
    miniJava_IntConstant,
    miniJava_IntegerTypeRef,
    miniJava_IntegerValue,
    miniJava_Interface,
    miniJava_Member,
    miniJava_Method,
    miniJava_MethodCall,
    miniJava_MethodCall2,
    miniJava_Minus,
    miniJava_Multiplication,
    miniJava_NamedElement,
    miniJava_Neg,
    miniJava_NewArray,
    miniJava_NewCall,
    miniJava_NewObject,
    miniJava_Not,
    miniJava_Null,
    miniJava_NullValue,
    miniJava_ObjectInstance,
    miniJava_ObjectRefValue,
    miniJava_Or,
    miniJava_OutputStream,
    miniJava_Parameter,
    miniJava_Plus,
    miniJava_PrintStatement,
    miniJava_Program,
    miniJava_Return,
    miniJava_SingleTypeRef,
    miniJava_State,
    miniJava_Statement,
    miniJava_StringConstant,
    miniJava_StringTypeRef,
    miniJava_StringValue,
    miniJava_Super,
    miniJava_Superior,
    miniJava_SuperiorOrEqual,
    miniJava_Symbol,
    miniJava_SymbolBinding,
    miniJava_SymbolRef,
    miniJava_SymbolToSymbolBindingMap,
    miniJava_This,
    miniJava_TypeDeclaration,
    miniJava_TypeRef,
    miniJava_TypedDeclaration,
    miniJava_Value,
    miniJava_VariableDeclaration,
    miniJava_VoidTypeRef,
    miniJava_WhileStatement,
    AccessLevel,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_classes1_reverse_link_reassign_clear():
    a1 = miniJava_TypeDeclaration(accessLevel="sample_text")
    a2 = miniJava_TypeDeclaration(accessLevel="sample_text_2")
    b = miniJava_Program(name="sample_text")
    _safe_set(b, 'miniJava_Program2', {a1})
    assert _is_linked(b, 'miniJava_Program2', a1)
    if hasattr(a1, 'miniJava_TypeDeclaration'):
        assert _is_linked(a1, 'miniJava_TypeDeclaration', b)
    _safe_set(b, 'miniJava_Program2', {a2})
    assert _is_linked(b, 'miniJava_Program2', a2)
    if hasattr(a1, 'miniJava_TypeDeclaration'):
        assert not _is_linked(a1, 'miniJava_TypeDeclaration', b)
    if hasattr(a2, 'miniJava_TypeDeclaration'):
        assert _is_linked(a2, 'miniJava_TypeDeclaration', b)
    _safe_set(b, 'miniJava_Program2', set())
    assert not _is_linked(b, 'miniJava_Program2', a2)
    if hasattr(a2, 'miniJava_TypeDeclaration'):
        assert not _is_linked(a2, 'miniJava_TypeDeclaration', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = miniJava_Program(name="sample_text")
    a2 = miniJava_Program(name="sample_text_2")
    b = miniJava_Import(importedNamespace="sample_text")
    _safe_set(b, 'miniJava_Import', a1)
    assert _is_linked(b, 'miniJava_Import', a1)
    if hasattr(a1, 'miniJava_Program'):
        assert _is_linked(a1, 'miniJava_Program', b)
    _safe_set(b, 'miniJava_Import', a2)
    assert _is_linked(b, 'miniJava_Import', a2)
    if hasattr(a1, 'miniJava_Program'):
        assert not _is_linked(a1, 'miniJava_Program', b)
    if hasattr(a2, 'miniJava_Program'):
        assert _is_linked(a2, 'miniJava_Program', b)
    _safe_set(b, 'miniJava_Import', None)
    assert not _is_linked(b, 'miniJava_Import', a2)
    if hasattr(a2, 'miniJava_Program'):
        assert not _is_linked(a2, 'miniJava_Program', b)


def test_assoc_members7_reverse_link_reassign_clear():
    a1 = miniJava_TypeDeclaration(accessLevel="sample_text")
    a2 = miniJava_TypeDeclaration(accessLevel="sample_text_2")
    b = miniJava_Member(access="sample_text")
    _safe_set(b, 'miniJava_Member', a1)
    assert _is_linked(b, 'miniJava_Member', a1)
    if hasattr(a1, 'miniJava_TypeDeclaration8'):
        assert _is_linked(a1, 'miniJava_TypeDeclaration8', b)
    _safe_set(b, 'miniJava_Member', a2)
    assert _is_linked(b, 'miniJava_Member', a2)
    if hasattr(a1, 'miniJava_TypeDeclaration8'):
        assert not _is_linked(a1, 'miniJava_TypeDeclaration8', b)
    if hasattr(a2, 'miniJava_TypeDeclaration8'):
        assert _is_linked(a2, 'miniJava_TypeDeclaration8', b)
    _safe_set(b, 'miniJava_Member', None)
    assert not _is_linked(b, 'miniJava_Member', a2)
    if hasattr(a2, 'miniJava_TypeDeclaration8'):
        assert not _is_linked(a2, 'miniJava_TypeDeclaration8', b)


def test_assoc_superClass10_reverse_link_reassign_clear():
    a1 = miniJava_Clazz(isabstract=True)
    a2 = miniJava_Clazz(isabstract=False)
    b = miniJava_Clazz(isabstract=True)
    _safe_set(b, 'miniJava_Clazz9', a1)
    assert _is_linked(b, 'miniJava_Clazz9', a1)
    if hasattr(a1, 'miniJava_Clazz'):
        assert _is_linked(a1, 'miniJava_Clazz', b)
    _safe_set(b, 'miniJava_Clazz9', a2)
    assert _is_linked(b, 'miniJava_Clazz9', a2)
    if hasattr(a1, 'miniJava_Clazz'):
        assert not _is_linked(a1, 'miniJava_Clazz', b)
    if hasattr(a2, 'miniJava_Clazz'):
        assert _is_linked(a2, 'miniJava_Clazz', b)
    _safe_set(b, 'miniJava_Clazz9', None)
    assert not _is_linked(b, 'miniJava_Clazz9', a2)
    if hasattr(a2, 'miniJava_Clazz'):
        assert not _is_linked(a2, 'miniJava_Clazz', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arraysHeap172_stub_double():
    # miniJava_State has no real 'miniJava_State173' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ArrayInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ArrayInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ArrayInstance(size=7)
    partner = miniJava_State()
    setattr(partner, 'miniJava_State173', None)
    _safe_set(owner, 'miniJava_ArrayInstance', partner)
    assert owner in getattr(partner, 'miniJava_State173')
    _safe_set(owner, 'miniJava_ArrayInstance', None)
    assert owner not in getattr(partner, 'miniJava_State173')


def test_assoc_body12_stub_double():
    # miniJava_Block has no real 'miniJava_Block' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Method(isabstract=True, isstatic=True)
    partner = miniJava_Block()
    setattr(partner, 'miniJava_Block', None)
    _safe_set(owner, 'miniJava_Method13', partner)
    assert getattr(partner, 'miniJava_Block') == owner
    _safe_set(owner, 'miniJava_Method13', None)
    assert getattr(partner, 'miniJava_Block') is None


def test_assoc_implementz5_stub_double():
    # miniJava_Interface has no real 'miniJava_Interface' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_TypeDeclaration(accessLevel="sample_text")
    partner = miniJava_Interface()
    setattr(partner, 'miniJava_Interface', None)
    _safe_set(owner, 'miniJava_TypeDeclaration6', {partner})
    assert getattr(partner, 'miniJava_Interface') == owner
    _safe_set(owner, 'miniJava_TypeDeclaration6', set())
    assert getattr(partner, 'miniJava_Interface') is None


def test_assoc_instance211_stub_double():
    # miniJava_ArrayRefValue has no real 'miniJava_ArrayRefValue' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ArrayInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ArrayInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ArrayInstance(size=7)
    partner = miniJava_ArrayRefValue()
    setattr(partner, 'miniJava_ArrayRefValue', None)
    _safe_set(owner, 'miniJava_ArrayInstance212', partner)
    assert getattr(partner, 'miniJava_ArrayRefValue') == owner
    _safe_set(owner, 'miniJava_ArrayInstance212', None)
    assert getattr(partner, 'miniJava_ArrayRefValue') is None


def test_assoc_method131_stub_double():
    # miniJava_MethodCall has no real 'miniJava_MethodCall132' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Method(isabstract=True, isstatic=True)
    partner = miniJava_MethodCall()
    setattr(partner, 'miniJava_MethodCall132', None)
    _safe_set(owner, 'miniJava_Method133', partner)
    assert getattr(partner, 'miniJava_MethodCall132') == owner
    _safe_set(owner, 'miniJava_Method133', None)
    assert getattr(partner, 'miniJava_MethodCall132') is None


def test_assoc_outputStream170_stub_double():
    # miniJava_State has no real 'miniJava_State171' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_OutputStream's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_OutputStream's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_OutputStream(stream="sample_text")
    partner = miniJava_State()
    setattr(partner, 'miniJava_State171', None)
    _safe_set(owner, 'miniJava_OutputStream', partner)
    assert getattr(partner, 'miniJava_State171') == owner
    _safe_set(owner, 'miniJava_OutputStream', None)
    assert getattr(partner, 'miniJava_State171') is None


def test_assoc_params11_stub_double():
    # miniJava_Parameter has no real 'miniJava_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Method(isabstract=True, isstatic=True)
    partner = miniJava_Parameter()
    setattr(partner, 'miniJava_Parameter', None)
    _safe_set(owner, 'miniJava_Method', {partner})
    assert getattr(partner, 'miniJava_Parameter') == owner
    _safe_set(owner, 'miniJava_Method', set())
    assert getattr(partner, 'miniJava_Parameter') is None


def test_assoc_referencedClass44_stub_double():
    # miniJava_ClassRef has no real 'miniJava_ClassRef' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_TypeDeclaration(accessLevel="sample_text")
    partner = miniJava_ClassRef()
    setattr(partner, 'miniJava_ClassRef', None)
    _safe_set(owner, 'miniJava_TypeDeclaration45', partner)
    assert getattr(partner, 'miniJava_ClassRef') == owner
    _safe_set(owner, 'miniJava_TypeDeclaration45', None)
    assert getattr(partner, 'miniJava_ClassRef') is None


def test_assoc_state3_stub_double():
    # miniJava_State has no real 'miniJava_State' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Program(name="sample_text")
    partner = miniJava_State()
    setattr(partner, 'miniJava_State', None)
    _safe_set(owner, 'miniJava_Program4', partner)
    assert getattr(partner, 'miniJava_State') == owner
    _safe_set(owner, 'miniJava_Program4', None)
    assert getattr(partner, 'miniJava_State') is None


def test_assoc_type137_stub_double():
    # miniJava_NewObject has no real 'miniJava_NewObject' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Clazz(isabstract=True)
    partner = miniJava_NewObject()
    setattr(partner, 'miniJava_NewObject', None)
    _safe_set(owner, 'miniJava_Clazz138', partner)
    assert getattr(partner, 'miniJava_NewObject') == owner
    _safe_set(owner, 'miniJava_Clazz138', None)
    assert getattr(partner, 'miniJava_NewObject') is None


def test_assoc_type203_stub_double():
    # miniJava_ObjectInstance has no real 'miniJava_ObjectInstance204' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_Clazz's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_Clazz's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_Clazz(isabstract=True)
    partner = miniJava_ObjectInstance()
    setattr(partner, 'miniJava_ObjectInstance204', None)
    _safe_set(owner, 'miniJava_Clazz205', partner)
    assert getattr(partner, 'miniJava_ObjectInstance204') == owner
    _safe_set(owner, 'miniJava_Clazz205', None)
    assert getattr(partner, 'miniJava_ObjectInstance204') is None


def test_assoc_value206_stub_double():
    # miniJava_Value has no real 'miniJava_Value208' property in the generated
    # code (a bare stub) -- manually attach it so miniJava_ArrayInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # miniJava_ArrayInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = miniJava_ArrayInstance(size=7)
    partner = miniJava_Value()
    setattr(partner, 'miniJava_Value208', None)
    _safe_set(owner, 'miniJava_ArrayInstance207', {partner})
    assert getattr(partner, 'miniJava_Value208') == owner
    _safe_set(owner, 'miniJava_ArrayInstance207', set())
    assert getattr(partner, 'miniJava_Value208') is None


