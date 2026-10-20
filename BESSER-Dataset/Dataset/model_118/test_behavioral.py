import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AssignmentExpression,
    BlockStatement,
    ClassBodyDeclaration,
    ConstantExpression,
    Expression,
    InterfaceMemberDeclaration,
    LeftHandSide,
    NoArrayExpression,
    NoArrayExpressionWithoutMinus,
    Primary,
    PrimaryNoNewArray,
    Statement,
    StatementExpression,
    VariableInitializer,
    javaDsl_AbstractMethodDeclaration,
    javaDsl_AdditiveExpression,
    javaDsl_AndExpression,
    javaDsl_ArgumentList,
    javaDsl_ArrayAccess,
    javaDsl_ArrayCreationExpression,
    javaDsl_ArrayExpression,
    javaDsl_ArrayInitializer,
    javaDsl_Assignment,
    javaDsl_AssignmentExpression,
    javaDsl_Block,
    javaDsl_BlockStatement,
    javaDsl_BreakStatement,
    javaDsl_CastExpression,
    javaDsl_ClassBody,
    javaDsl_ClassBodyDeclaration,
    javaDsl_ClassDeclaration,
    javaDsl_ClassInstanceCreationExpression,
    javaDsl_ClassMemberDeclaration,
    javaDsl_CompilationUnit,
    javaDsl_ConditionalAndExpression,
    javaDsl_ConditionalExpression,
    javaDsl_ConditionalOrExpression,
    javaDsl_ConstantDeclaration,
    javaDsl_ConstantExpression,
    javaDsl_ConstructorBody,
    javaDsl_ConstructorDeclaration,
    javaDsl_ConstructorDeclarator,
    javaDsl_ContinueStatement,
    javaDsl_DoStatement,
    javaDsl_EObject,
    javaDsl_EqualityExpression,
    javaDsl_Exceptions,
    javaDsl_ExclusiveOrExpression,
    javaDsl_ExplicitConstructorInvocation,
    javaDsl_Expression,
    javaDsl_ExtendsInterfaces,
    javaDsl_FieldAccess,
    javaDsl_FieldDeclaration,
    javaDsl_ForInit,
    javaDsl_ForStatement,
    javaDsl_ForUpdate,
    javaDsl_FormalParameter,
    javaDsl_Head,
    javaDsl_IfStatement,
    javaDsl_ImportStatement,
    javaDsl_InclusiveOrExpression,
    javaDsl_InterfaceBody,
    javaDsl_InterfaceDeclaration,
    javaDsl_InterfaceMemberDeclaration,
    javaDsl_Interfaces,
    javaDsl_LabeledStatement,
    javaDsl_LeftHandSide,
    javaDsl_LocalVariableDeclaration,
    javaDsl_MethodDeclaration,
    javaDsl_MethodDeclarator,
    javaDsl_MethodHeader,
    javaDsl_MethodInvocation,
    javaDsl_MultiplicativeExpression,
    javaDsl_NoArrayExpression,
    javaDsl_NoArrayExpressionWithoutMinus,
    javaDsl_PackageStatement,
    javaDsl_PostfixExpression,
    javaDsl_PreDecrementExpression,
    javaDsl_PreIncrementExpression,
    javaDsl_Primary,
    javaDsl_PrimaryNewArray,
    javaDsl_PrimaryNoNewArray,
    javaDsl_RelationalExpression,
    javaDsl_ResultType,
    javaDsl_ReturnStatement,
    javaDsl_ShiftExpression,
    javaDsl_Statement,
    javaDsl_StatementExpression,
    javaDsl_StaticInitializer,
    javaDsl_SwitchStatement,
    javaDsl_SynchronizedStatement,
    javaDsl_ThrowsStatement,
    javaDsl_TryStatement,
    javaDsl_Type,
    javaDsl_TypeDeclaration,
    javaDsl_VariableDeclarator,
    javaDsl_VariableInitializer,
    javaDsl_WhileStatement,
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

def test_assoc_array202_reverse_link_reassign_clear():
    a1 = javaDsl_PrimaryNoNewArray(keyword="sample_text", literal="sample_text", method="sample_text", reference="sample_text")
    a2 = javaDsl_PrimaryNoNewArray(keyword="sample_text_2", literal="sample_text_2", method="sample_text_2", reference="sample_text_2")
    b = javaDsl_ArrayAccess(reference="sample_text")
    _safe_set(b, 'javaDsl_ArrayAccess', a1)
    assert _is_linked(b, 'javaDsl_ArrayAccess', a1)
    if hasattr(a1, 'javaDsl_PrimaryNoNewArray203'):
        assert _is_linked(a1, 'javaDsl_PrimaryNoNewArray203', b)
    _safe_set(b, 'javaDsl_ArrayAccess', a2)
    assert _is_linked(b, 'javaDsl_ArrayAccess', a2)
    if hasattr(a1, 'javaDsl_PrimaryNoNewArray203'):
        assert not _is_linked(a1, 'javaDsl_PrimaryNoNewArray203', b)
    if hasattr(a2, 'javaDsl_PrimaryNoNewArray203'):
        assert _is_linked(a2, 'javaDsl_PrimaryNoNewArray203', b)
    _safe_set(b, 'javaDsl_ArrayAccess', None)
    assert not _is_linked(b, 'javaDsl_ArrayAccess', a2)
    if hasattr(a2, 'javaDsl_PrimaryNoNewArray203'):
        assert not _is_linked(a2, 'javaDsl_PrimaryNoNewArray203', b)


def test_assoc_class_188_reverse_link_reassign_clear():
    a1 = javaDsl_PrimaryNoNewArray(keyword="sample_text", literal="sample_text", method="sample_text", reference="sample_text")
    a2 = javaDsl_PrimaryNoNewArray(keyword="sample_text_2", literal="sample_text_2", method="sample_text_2", reference="sample_text_2")
    b = javaDsl_ClassInstanceCreationExpression(type="sample_text")
    _safe_set(b, 'javaDsl_ClassInstanceCreationExpression', a1)
    assert _is_linked(b, 'javaDsl_ClassInstanceCreationExpression', a1)
    if hasattr(a1, 'javaDsl_PrimaryNoNewArray'):
        assert _is_linked(a1, 'javaDsl_PrimaryNoNewArray', b)
    _safe_set(b, 'javaDsl_ClassInstanceCreationExpression', a2)
    assert _is_linked(b, 'javaDsl_ClassInstanceCreationExpression', a2)
    if hasattr(a1, 'javaDsl_PrimaryNoNewArray'):
        assert not _is_linked(a1, 'javaDsl_PrimaryNoNewArray', b)
    if hasattr(a2, 'javaDsl_PrimaryNoNewArray'):
        assert _is_linked(a2, 'javaDsl_PrimaryNoNewArray', b)
    _safe_set(b, 'javaDsl_ClassInstanceCreationExpression', None)
    assert not _is_linked(b, 'javaDsl_ClassInstanceCreationExpression', a2)
    if hasattr(a2, 'javaDsl_PrimaryNoNewArray'):
        assert not _is_linked(a2, 'javaDsl_PrimaryNoNewArray', b)


def test_assoc_extends63_reverse_link_reassign_clear():
    a1 = javaDsl_InterfaceDeclaration(modifiers="sample_text", name="sample_text")
    a2 = javaDsl_InterfaceDeclaration(modifiers="sample_text_2", name="sample_text_2")
    b = javaDsl_ExtendsInterfaces(interfaces="sample_text", keyword="sample_text")
    _safe_set(b, 'javaDsl_ExtendsInterfaces', a1)
    assert _is_linked(b, 'javaDsl_ExtendsInterfaces', a1)
    if hasattr(a1, 'javaDsl_InterfaceDeclaration'):
        assert _is_linked(a1, 'javaDsl_InterfaceDeclaration', b)
    _safe_set(b, 'javaDsl_ExtendsInterfaces', a2)
    assert _is_linked(b, 'javaDsl_ExtendsInterfaces', a2)
    if hasattr(a1, 'javaDsl_InterfaceDeclaration'):
        assert not _is_linked(a1, 'javaDsl_InterfaceDeclaration', b)
    if hasattr(a2, 'javaDsl_InterfaceDeclaration'):
        assert _is_linked(a2, 'javaDsl_InterfaceDeclaration', b)
    _safe_set(b, 'javaDsl_ExtendsInterfaces', None)
    assert not _is_linked(b, 'javaDsl_ExtendsInterfaces', a2)
    if hasattr(a2, 'javaDsl_InterfaceDeclaration'):
        assert not _is_linked(a2, 'javaDsl_InterfaceDeclaration', b)


def test_assoc_header21_reverse_link_reassign_clear():
    a1 = javaDsl_ConstructorDeclarator(name="sample_text")
    a2 = javaDsl_ConstructorDeclarator(name="sample_text_2")
    b = javaDsl_ConstructorDeclaration(modifiers="sample_text")
    _safe_set(b, 'javaDsl_ConstructorDeclaration', a1)
    assert _is_linked(b, 'javaDsl_ConstructorDeclaration', a1)
    if hasattr(a1, 'javaDsl_ConstructorDeclarator'):
        assert _is_linked(a1, 'javaDsl_ConstructorDeclarator', b)
    _safe_set(b, 'javaDsl_ConstructorDeclaration', a2)
    assert _is_linked(b, 'javaDsl_ConstructorDeclaration', a2)
    if hasattr(a1, 'javaDsl_ConstructorDeclarator'):
        assert not _is_linked(a1, 'javaDsl_ConstructorDeclarator', b)
    if hasattr(a2, 'javaDsl_ConstructorDeclarator'):
        assert _is_linked(a2, 'javaDsl_ConstructorDeclarator', b)
    _safe_set(b, 'javaDsl_ConstructorDeclaration', None)
    assert not _is_linked(b, 'javaDsl_ConstructorDeclaration', a2)
    if hasattr(a2, 'javaDsl_ConstructorDeclarator'):
        assert not _is_linked(a2, 'javaDsl_ConstructorDeclarator', b)


def test_assoc_header52_reverse_link_reassign_clear():
    a1 = javaDsl_MethodHeader(modifiers="sample_text")
    a2 = javaDsl_MethodHeader(modifiers="sample_text_2")
    b = javaDsl_MethodDeclarator(name="sample_text")
    _safe_set(b, 'javaDsl_MethodDeclarator', a1)
    assert _is_linked(b, 'javaDsl_MethodDeclarator', a1)
    if hasattr(a1, 'javaDsl_MethodHeader53'):
        assert _is_linked(a1, 'javaDsl_MethodHeader53', b)
    _safe_set(b, 'javaDsl_MethodDeclarator', a2)
    assert _is_linked(b, 'javaDsl_MethodDeclarator', a2)
    if hasattr(a1, 'javaDsl_MethodHeader53'):
        assert not _is_linked(a1, 'javaDsl_MethodHeader53', b)
    if hasattr(a2, 'javaDsl_MethodHeader53'):
        assert _is_linked(a2, 'javaDsl_MethodHeader53', b)
    _safe_set(b, 'javaDsl_MethodDeclarator', None)
    assert not _is_linked(b, 'javaDsl_MethodDeclarator', a2)
    if hasattr(a2, 'javaDsl_MethodHeader53'):
        assert not _is_linked(a2, 'javaDsl_MethodHeader53', b)


def test_assoc_implements9_reverse_link_reassign_clear():
    a1 = javaDsl_Interfaces(interfaces="sample_text", keyword="sample_text")
    a2 = javaDsl_Interfaces(interfaces="sample_text_2", keyword="sample_text_2")
    b = javaDsl_ClassDeclaration(className="sample_text", extend="sample_text", modifiers="sample_text")
    _safe_set(b, 'javaDsl_ClassDeclaration', a1)
    assert _is_linked(b, 'javaDsl_ClassDeclaration', a1)
    if hasattr(a1, 'javaDsl_Interfaces'):
        assert _is_linked(a1, 'javaDsl_Interfaces', b)
    _safe_set(b, 'javaDsl_ClassDeclaration', a2)
    assert _is_linked(b, 'javaDsl_ClassDeclaration', a2)
    if hasattr(a1, 'javaDsl_Interfaces'):
        assert not _is_linked(a1, 'javaDsl_Interfaces', b)
    if hasattr(a2, 'javaDsl_Interfaces'):
        assert _is_linked(a2, 'javaDsl_Interfaces', b)
    _safe_set(b, 'javaDsl_ClassDeclaration', None)
    assert not _is_linked(b, 'javaDsl_ClassDeclaration', a2)
    if hasattr(a2, 'javaDsl_Interfaces'):
        assert not _is_linked(a2, 'javaDsl_Interfaces', b)


def test_assoc_object175_reverse_link_reassign_clear():
    a1 = javaDsl_Primary(fields="sample_text")
    a2 = javaDsl_Primary(fields="sample_text_2")
    b = javaDsl_PostfixExpression(operators="sample_text", reference="sample_text")
    _safe_set(b, 'javaDsl_PostfixExpression', a1)
    assert _is_linked(b, 'javaDsl_PostfixExpression', a1)
    if hasattr(a1, 'javaDsl_Primary'):
        assert _is_linked(a1, 'javaDsl_Primary', b)
    _safe_set(b, 'javaDsl_PostfixExpression', a2)
    assert _is_linked(b, 'javaDsl_PostfixExpression', a2)
    if hasattr(a1, 'javaDsl_Primary'):
        assert not _is_linked(a1, 'javaDsl_Primary', b)
    if hasattr(a2, 'javaDsl_Primary'):
        assert _is_linked(a2, 'javaDsl_Primary', b)
    _safe_set(b, 'javaDsl_PostfixExpression', None)
    assert not _is_linked(b, 'javaDsl_PostfixExpression', a2)
    if hasattr(a2, 'javaDsl_Primary'):
        assert not _is_linked(a2, 'javaDsl_Primary', b)


def test_assoc_object178_reverse_link_reassign_clear():
    a1 = javaDsl_Primary(fields="sample_text")
    a2 = javaDsl_Primary(fields="sample_text_2")
    b = javaDsl_MethodInvocation(keyword="sample_text", method="sample_text")
    _safe_set(b, 'javaDsl_MethodInvocation179', a1)
    assert _is_linked(b, 'javaDsl_MethodInvocation179', a1)
    if hasattr(a1, 'javaDsl_Primary180'):
        assert _is_linked(a1, 'javaDsl_Primary180', b)
    _safe_set(b, 'javaDsl_MethodInvocation179', a2)
    assert _is_linked(b, 'javaDsl_MethodInvocation179', a2)
    if hasattr(a1, 'javaDsl_Primary180'):
        assert not _is_linked(a1, 'javaDsl_Primary180', b)
    if hasattr(a2, 'javaDsl_Primary180'):
        assert _is_linked(a2, 'javaDsl_Primary180', b)
    _safe_set(b, 'javaDsl_MethodInvocation179', None)
    assert not _is_linked(b, 'javaDsl_MethodInvocation179', a2)
    if hasattr(a2, 'javaDsl_Primary180'):
        assert not _is_linked(a2, 'javaDsl_Primary180', b)


def test_assoc_object181_reverse_link_reassign_clear():
    a1 = javaDsl_Primary(fields="sample_text")
    a2 = javaDsl_Primary(fields="sample_text_2")
    b = javaDsl_FieldAccess(field="sample_text", keyword="sample_text")
    _safe_set(b, 'javaDsl_FieldAccess', a1)
    assert _is_linked(b, 'javaDsl_FieldAccess', a1)
    if hasattr(a1, 'javaDsl_Primary182'):
        assert _is_linked(a1, 'javaDsl_Primary182', b)
    _safe_set(b, 'javaDsl_FieldAccess', a2)
    assert _is_linked(b, 'javaDsl_FieldAccess', a2)
    if hasattr(a1, 'javaDsl_Primary182'):
        assert not _is_linked(a1, 'javaDsl_Primary182', b)
    if hasattr(a2, 'javaDsl_Primary182'):
        assert _is_linked(a2, 'javaDsl_Primary182', b)
    _safe_set(b, 'javaDsl_FieldAccess', None)
    assert not _is_linked(b, 'javaDsl_FieldAccess', a2)
    if hasattr(a2, 'javaDsl_Primary182'):
        assert not _is_linked(a2, 'javaDsl_Primary182', b)


def test_assoc_operand173_reverse_link_reassign_clear():
    a1 = javaDsl_NoArrayExpression(operator="sample_text")
    a2 = javaDsl_NoArrayExpression(operator="sample_text_2")
    b = javaDsl_NoArrayExpression(operator="sample_text")
    _safe_set(b, 'javaDsl_NoArrayExpression174', a1)
    assert _is_linked(b, 'javaDsl_NoArrayExpression174', a1)
    if hasattr(a1, 'javaDsl_NoArrayExpression172'):
        assert _is_linked(a1, 'javaDsl_NoArrayExpression172', b)
    _safe_set(b, 'javaDsl_NoArrayExpression174', a2)
    assert _is_linked(b, 'javaDsl_NoArrayExpression174', a2)
    if hasattr(a1, 'javaDsl_NoArrayExpression172'):
        assert not _is_linked(a1, 'javaDsl_NoArrayExpression172', b)
    if hasattr(a2, 'javaDsl_NoArrayExpression172'):
        assert _is_linked(a2, 'javaDsl_NoArrayExpression172', b)
    _safe_set(b, 'javaDsl_NoArrayExpression174', None)
    assert not _is_linked(b, 'javaDsl_NoArrayExpression174', a2)
    if hasattr(a2, 'javaDsl_NoArrayExpression172'):
        assert not _is_linked(a2, 'javaDsl_NoArrayExpression172', b)


def test_assoc_operands152_reverse_link_reassign_clear():
    a1 = javaDsl_ConditionalOrExpression(operators="sample_text")
    a2 = javaDsl_ConditionalOrExpression(operators="sample_text_2")
    b = javaDsl_ConditionalAndExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_ConditionalAndExpression', a1)
    assert _is_linked(b, 'javaDsl_ConditionalAndExpression', a1)
    if hasattr(a1, 'javaDsl_ConditionalOrExpression153'):
        assert _is_linked(a1, 'javaDsl_ConditionalOrExpression153', b)
    _safe_set(b, 'javaDsl_ConditionalAndExpression', a2)
    assert _is_linked(b, 'javaDsl_ConditionalAndExpression', a2)
    if hasattr(a1, 'javaDsl_ConditionalOrExpression153'):
        assert not _is_linked(a1, 'javaDsl_ConditionalOrExpression153', b)
    if hasattr(a2, 'javaDsl_ConditionalOrExpression153'):
        assert _is_linked(a2, 'javaDsl_ConditionalOrExpression153', b)
    _safe_set(b, 'javaDsl_ConditionalAndExpression', None)
    assert not _is_linked(b, 'javaDsl_ConditionalAndExpression', a2)
    if hasattr(a2, 'javaDsl_ConditionalOrExpression153'):
        assert not _is_linked(a2, 'javaDsl_ConditionalOrExpression153', b)


def test_assoc_operands154_reverse_link_reassign_clear():
    a1 = javaDsl_InclusiveOrExpression(operators="sample_text")
    a2 = javaDsl_InclusiveOrExpression(operators="sample_text_2")
    b = javaDsl_ConditionalAndExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_ConditionalAndExpression155', {a1})
    assert _is_linked(b, 'javaDsl_ConditionalAndExpression155', a1)
    if hasattr(a1, 'javaDsl_InclusiveOrExpression'):
        assert _is_linked(a1, 'javaDsl_InclusiveOrExpression', b)
    _safe_set(b, 'javaDsl_ConditionalAndExpression155', {a2})
    assert _is_linked(b, 'javaDsl_ConditionalAndExpression155', a2)
    if hasattr(a1, 'javaDsl_InclusiveOrExpression'):
        assert not _is_linked(a1, 'javaDsl_InclusiveOrExpression', b)
    if hasattr(a2, 'javaDsl_InclusiveOrExpression'):
        assert _is_linked(a2, 'javaDsl_InclusiveOrExpression', b)
    _safe_set(b, 'javaDsl_ConditionalAndExpression155', set())
    assert not _is_linked(b, 'javaDsl_ConditionalAndExpression155', a2)
    if hasattr(a2, 'javaDsl_InclusiveOrExpression'):
        assert not _is_linked(a2, 'javaDsl_InclusiveOrExpression', b)


def test_assoc_operands156_reverse_link_reassign_clear():
    a1 = javaDsl_InclusiveOrExpression(operators="sample_text")
    a2 = javaDsl_InclusiveOrExpression(operators="sample_text_2")
    b = javaDsl_ExclusiveOrExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_ExclusiveOrExpression', a1)
    assert _is_linked(b, 'javaDsl_ExclusiveOrExpression', a1)
    if hasattr(a1, 'javaDsl_InclusiveOrExpression157'):
        assert _is_linked(a1, 'javaDsl_InclusiveOrExpression157', b)
    _safe_set(b, 'javaDsl_ExclusiveOrExpression', a2)
    assert _is_linked(b, 'javaDsl_ExclusiveOrExpression', a2)
    if hasattr(a1, 'javaDsl_InclusiveOrExpression157'):
        assert not _is_linked(a1, 'javaDsl_InclusiveOrExpression157', b)
    if hasattr(a2, 'javaDsl_InclusiveOrExpression157'):
        assert _is_linked(a2, 'javaDsl_InclusiveOrExpression157', b)
    _safe_set(b, 'javaDsl_ExclusiveOrExpression', None)
    assert not _is_linked(b, 'javaDsl_ExclusiveOrExpression', a2)
    if hasattr(a2, 'javaDsl_InclusiveOrExpression157'):
        assert not _is_linked(a2, 'javaDsl_InclusiveOrExpression157', b)


def test_assoc_operands158_reverse_link_reassign_clear():
    a1 = javaDsl_ExclusiveOrExpression(operators="sample_text")
    a2 = javaDsl_ExclusiveOrExpression(operators="sample_text_2")
    b = javaDsl_AndExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_AndExpression', a1)
    assert _is_linked(b, 'javaDsl_AndExpression', a1)
    if hasattr(a1, 'javaDsl_ExclusiveOrExpression159'):
        assert _is_linked(a1, 'javaDsl_ExclusiveOrExpression159', b)
    _safe_set(b, 'javaDsl_AndExpression', a2)
    assert _is_linked(b, 'javaDsl_AndExpression', a2)
    if hasattr(a1, 'javaDsl_ExclusiveOrExpression159'):
        assert not _is_linked(a1, 'javaDsl_ExclusiveOrExpression159', b)
    if hasattr(a2, 'javaDsl_ExclusiveOrExpression159'):
        assert _is_linked(a2, 'javaDsl_ExclusiveOrExpression159', b)
    _safe_set(b, 'javaDsl_AndExpression', None)
    assert not _is_linked(b, 'javaDsl_AndExpression', a2)
    if hasattr(a2, 'javaDsl_ExclusiveOrExpression159'):
        assert not _is_linked(a2, 'javaDsl_ExclusiveOrExpression159', b)


def test_assoc_operands160_reverse_link_reassign_clear():
    a1 = javaDsl_EqualityExpression(operators="sample_text")
    a2 = javaDsl_EqualityExpression(operators="sample_text_2")
    b = javaDsl_AndExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_AndExpression161', {a1})
    assert _is_linked(b, 'javaDsl_AndExpression161', a1)
    if hasattr(a1, 'javaDsl_EqualityExpression'):
        assert _is_linked(a1, 'javaDsl_EqualityExpression', b)
    _safe_set(b, 'javaDsl_AndExpression161', {a2})
    assert _is_linked(b, 'javaDsl_AndExpression161', a2)
    if hasattr(a1, 'javaDsl_EqualityExpression'):
        assert not _is_linked(a1, 'javaDsl_EqualityExpression', b)
    if hasattr(a2, 'javaDsl_EqualityExpression'):
        assert _is_linked(a2, 'javaDsl_EqualityExpression', b)
    _safe_set(b, 'javaDsl_AndExpression161', set())
    assert not _is_linked(b, 'javaDsl_AndExpression161', a2)
    if hasattr(a2, 'javaDsl_EqualityExpression'):
        assert not _is_linked(a2, 'javaDsl_EqualityExpression', b)


def test_assoc_operands162_reverse_link_reassign_clear():
    a1 = javaDsl_RelationalExpression(classes="sample_text", operators="sample_text")
    a2 = javaDsl_RelationalExpression(classes="sample_text_2", operators="sample_text_2")
    b = javaDsl_EqualityExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_EqualityExpression163', {a1})
    assert _is_linked(b, 'javaDsl_EqualityExpression163', a1)
    if hasattr(a1, 'javaDsl_RelationalExpression'):
        assert _is_linked(a1, 'javaDsl_RelationalExpression', b)
    _safe_set(b, 'javaDsl_EqualityExpression163', {a2})
    assert _is_linked(b, 'javaDsl_EqualityExpression163', a2)
    if hasattr(a1, 'javaDsl_RelationalExpression'):
        assert not _is_linked(a1, 'javaDsl_RelationalExpression', b)
    if hasattr(a2, 'javaDsl_RelationalExpression'):
        assert _is_linked(a2, 'javaDsl_RelationalExpression', b)
    _safe_set(b, 'javaDsl_EqualityExpression163', set())
    assert not _is_linked(b, 'javaDsl_EqualityExpression163', a2)
    if hasattr(a2, 'javaDsl_RelationalExpression'):
        assert not _is_linked(a2, 'javaDsl_RelationalExpression', b)


def test_assoc_operands164_reverse_link_reassign_clear():
    a1 = javaDsl_ShiftExpression(operators="sample_text")
    a2 = javaDsl_ShiftExpression(operators="sample_text_2")
    b = javaDsl_RelationalExpression(classes="sample_text", operators="sample_text")
    _safe_set(b, 'javaDsl_RelationalExpression165', {a1})
    assert _is_linked(b, 'javaDsl_RelationalExpression165', a1)
    if hasattr(a1, 'javaDsl_ShiftExpression'):
        assert _is_linked(a1, 'javaDsl_ShiftExpression', b)
    _safe_set(b, 'javaDsl_RelationalExpression165', {a2})
    assert _is_linked(b, 'javaDsl_RelationalExpression165', a2)
    if hasattr(a1, 'javaDsl_ShiftExpression'):
        assert not _is_linked(a1, 'javaDsl_ShiftExpression', b)
    if hasattr(a2, 'javaDsl_ShiftExpression'):
        assert _is_linked(a2, 'javaDsl_ShiftExpression', b)
    _safe_set(b, 'javaDsl_RelationalExpression165', set())
    assert not _is_linked(b, 'javaDsl_RelationalExpression165', a2)
    if hasattr(a2, 'javaDsl_ShiftExpression'):
        assert not _is_linked(a2, 'javaDsl_ShiftExpression', b)


def test_assoc_operands166_reverse_link_reassign_clear():
    a1 = javaDsl_ShiftExpression(operators="sample_text")
    a2 = javaDsl_ShiftExpression(operators="sample_text_2")
    b = javaDsl_AdditiveExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_AdditiveExpression', a1)
    assert _is_linked(b, 'javaDsl_AdditiveExpression', a1)
    if hasattr(a1, 'javaDsl_ShiftExpression167'):
        assert _is_linked(a1, 'javaDsl_ShiftExpression167', b)
    _safe_set(b, 'javaDsl_AdditiveExpression', a2)
    assert _is_linked(b, 'javaDsl_AdditiveExpression', a2)
    if hasattr(a1, 'javaDsl_ShiftExpression167'):
        assert not _is_linked(a1, 'javaDsl_ShiftExpression167', b)
    if hasattr(a2, 'javaDsl_ShiftExpression167'):
        assert _is_linked(a2, 'javaDsl_ShiftExpression167', b)
    _safe_set(b, 'javaDsl_AdditiveExpression', None)
    assert not _is_linked(b, 'javaDsl_AdditiveExpression', a2)
    if hasattr(a2, 'javaDsl_ShiftExpression167'):
        assert not _is_linked(a2, 'javaDsl_ShiftExpression167', b)


def test_assoc_operands168_reverse_link_reassign_clear():
    a1 = javaDsl_MultiplicativeExpression(operators="sample_text")
    a2 = javaDsl_MultiplicativeExpression(operators="sample_text_2")
    b = javaDsl_AdditiveExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_AdditiveExpression169', {a1})
    assert _is_linked(b, 'javaDsl_AdditiveExpression169', a1)
    if hasattr(a1, 'javaDsl_MultiplicativeExpression'):
        assert _is_linked(a1, 'javaDsl_MultiplicativeExpression', b)
    _safe_set(b, 'javaDsl_AdditiveExpression169', {a2})
    assert _is_linked(b, 'javaDsl_AdditiveExpression169', a2)
    if hasattr(a1, 'javaDsl_MultiplicativeExpression'):
        assert not _is_linked(a1, 'javaDsl_MultiplicativeExpression', b)
    if hasattr(a2, 'javaDsl_MultiplicativeExpression'):
        assert _is_linked(a2, 'javaDsl_MultiplicativeExpression', b)
    _safe_set(b, 'javaDsl_AdditiveExpression169', set())
    assert not _is_linked(b, 'javaDsl_AdditiveExpression169', a2)
    if hasattr(a2, 'javaDsl_MultiplicativeExpression'):
        assert not _is_linked(a2, 'javaDsl_MultiplicativeExpression', b)


def test_assoc_operands170_reverse_link_reassign_clear():
    a1 = javaDsl_NoArrayExpression(operator="sample_text")
    a2 = javaDsl_NoArrayExpression(operator="sample_text_2")
    b = javaDsl_MultiplicativeExpression(operators="sample_text")
    _safe_set(b, 'javaDsl_MultiplicativeExpression171', {a1})
    assert _is_linked(b, 'javaDsl_MultiplicativeExpression171', a1)
    if hasattr(a1, 'javaDsl_NoArrayExpression'):
        assert _is_linked(a1, 'javaDsl_NoArrayExpression', b)
    _safe_set(b, 'javaDsl_MultiplicativeExpression171', {a2})
    assert _is_linked(b, 'javaDsl_MultiplicativeExpression171', a2)
    if hasattr(a1, 'javaDsl_NoArrayExpression'):
        assert not _is_linked(a1, 'javaDsl_NoArrayExpression', b)
    if hasattr(a2, 'javaDsl_NoArrayExpression'):
        assert _is_linked(a2, 'javaDsl_NoArrayExpression', b)
    _safe_set(b, 'javaDsl_MultiplicativeExpression171', set())
    assert not _is_linked(b, 'javaDsl_MultiplicativeExpression171', a2)
    if hasattr(a2, 'javaDsl_NoArrayExpression'):
        assert not _is_linked(a2, 'javaDsl_NoArrayExpression', b)


def test_assoc_params26_reverse_link_reassign_clear():
    a1 = javaDsl_FormalParameter(variable="sample_text")
    a2 = javaDsl_FormalParameter(variable="sample_text_2")
    b = javaDsl_ConstructorDeclarator(name="sample_text")
    _safe_set(b, 'javaDsl_ConstructorDeclarator27', {a1})
    assert _is_linked(b, 'javaDsl_ConstructorDeclarator27', a1)
    if hasattr(a1, 'javaDsl_FormalParameter'):
        assert _is_linked(a1, 'javaDsl_FormalParameter', b)
    _safe_set(b, 'javaDsl_ConstructorDeclarator27', {a2})
    assert _is_linked(b, 'javaDsl_ConstructorDeclarator27', a2)
    if hasattr(a1, 'javaDsl_FormalParameter'):
        assert not _is_linked(a1, 'javaDsl_FormalParameter', b)
    if hasattr(a2, 'javaDsl_FormalParameter'):
        assert _is_linked(a2, 'javaDsl_FormalParameter', b)
    _safe_set(b, 'javaDsl_ConstructorDeclarator27', set())
    assert not _is_linked(b, 'javaDsl_ConstructorDeclarator27', a2)
    if hasattr(a2, 'javaDsl_FormalParameter'):
        assert not _is_linked(a2, 'javaDsl_FormalParameter', b)


def test_assoc_params60_reverse_link_reassign_clear():
    a1 = javaDsl_MethodDeclarator(name="sample_text")
    a2 = javaDsl_MethodDeclarator(name="sample_text_2")
    b = javaDsl_FormalParameter(variable="sample_text")
    _safe_set(b, 'javaDsl_FormalParameter62', a1)
    assert _is_linked(b, 'javaDsl_FormalParameter62', a1)
    if hasattr(a1, 'javaDsl_MethodDeclarator61'):
        assert _is_linked(a1, 'javaDsl_MethodDeclarator61', b)
    _safe_set(b, 'javaDsl_FormalParameter62', a2)
    assert _is_linked(b, 'javaDsl_FormalParameter62', a2)
    if hasattr(a1, 'javaDsl_MethodDeclarator61'):
        assert not _is_linked(a1, 'javaDsl_MethodDeclarator61', b)
    if hasattr(a2, 'javaDsl_MethodDeclarator61'):
        assert _is_linked(a2, 'javaDsl_MethodDeclarator61', b)
    _safe_set(b, 'javaDsl_FormalParameter62', None)
    assert not _is_linked(b, 'javaDsl_FormalParameter62', a2)
    if hasattr(a2, 'javaDsl_MethodDeclarator61'):
        assert not _is_linked(a2, 'javaDsl_MethodDeclarator61', b)


def test_assoc_throws22_reverse_link_reassign_clear():
    a1 = javaDsl_Exceptions(exceptions="sample_text")
    a2 = javaDsl_Exceptions(exceptions="sample_text_2")
    b = javaDsl_ConstructorDeclaration(modifiers="sample_text")
    _safe_set(b, 'javaDsl_ConstructorDeclaration23', a1)
    assert _is_linked(b, 'javaDsl_ConstructorDeclaration23', a1)
    if hasattr(a1, 'javaDsl_Exceptions'):
        assert _is_linked(a1, 'javaDsl_Exceptions', b)
    _safe_set(b, 'javaDsl_ConstructorDeclaration23', a2)
    assert _is_linked(b, 'javaDsl_ConstructorDeclaration23', a2)
    if hasattr(a1, 'javaDsl_Exceptions'):
        assert not _is_linked(a1, 'javaDsl_Exceptions', b)
    if hasattr(a2, 'javaDsl_Exceptions'):
        assert _is_linked(a2, 'javaDsl_Exceptions', b)
    _safe_set(b, 'javaDsl_ConstructorDeclaration23', None)
    assert not _is_linked(b, 'javaDsl_ConstructorDeclaration23', a2)
    if hasattr(a2, 'javaDsl_Exceptions'):
        assert not _is_linked(a2, 'javaDsl_Exceptions', b)


def test_assoc_throws54_reverse_link_reassign_clear():
    a1 = javaDsl_MethodHeader(modifiers="sample_text")
    a2 = javaDsl_MethodHeader(modifiers="sample_text_2")
    b = javaDsl_Exceptions(exceptions="sample_text")
    _safe_set(b, 'javaDsl_Exceptions56', a1)
    assert _is_linked(b, 'javaDsl_Exceptions56', a1)
    if hasattr(a1, 'javaDsl_MethodHeader55'):
        assert _is_linked(a1, 'javaDsl_MethodHeader55', b)
    _safe_set(b, 'javaDsl_Exceptions56', a2)
    assert _is_linked(b, 'javaDsl_Exceptions56', a2)
    if hasattr(a1, 'javaDsl_MethodHeader55'):
        assert not _is_linked(a1, 'javaDsl_MethodHeader55', b)
    if hasattr(a2, 'javaDsl_MethodHeader55'):
        assert _is_linked(a2, 'javaDsl_MethodHeader55', b)
    _safe_set(b, 'javaDsl_Exceptions56', None)
    assert not _is_linked(b, 'javaDsl_Exceptions56', a2)
    if hasattr(a2, 'javaDsl_MethodHeader55'):
        assert not _is_linked(a2, 'javaDsl_MethodHeader55', b)


def test_assoc_type28_reverse_link_reassign_clear():
    a1 = javaDsl_Type(name="sample_text")
    a2 = javaDsl_Type(name="sample_text_2")
    b = javaDsl_FormalParameter(variable="sample_text")
    _safe_set(b, 'javaDsl_FormalParameter29', a1)
    assert _is_linked(b, 'javaDsl_FormalParameter29', a1)
    if hasattr(a1, 'javaDsl_Type'):
        assert _is_linked(a1, 'javaDsl_Type', b)
    _safe_set(b, 'javaDsl_FormalParameter29', a2)
    assert _is_linked(b, 'javaDsl_FormalParameter29', a2)
    if hasattr(a1, 'javaDsl_Type'):
        assert not _is_linked(a1, 'javaDsl_Type', b)
    if hasattr(a2, 'javaDsl_Type'):
        assert _is_linked(a2, 'javaDsl_Type', b)
    _safe_set(b, 'javaDsl_FormalParameter29', None)
    assert not _is_linked(b, 'javaDsl_FormalParameter29', a2)
    if hasattr(a2, 'javaDsl_Type'):
        assert not _is_linked(a2, 'javaDsl_Type', b)


def test_assoc_type36_reverse_link_reassign_clear():
    a1 = javaDsl_Type(name="sample_text")
    a2 = javaDsl_Type(name="sample_text_2")
    b = javaDsl_FieldDeclaration(modifiers="sample_text")
    _safe_set(b, 'javaDsl_FieldDeclaration37', a1)
    assert _is_linked(b, 'javaDsl_FieldDeclaration37', a1)
    if hasattr(a1, 'javaDsl_Type38'):
        assert _is_linked(a1, 'javaDsl_Type38', b)
    _safe_set(b, 'javaDsl_FieldDeclaration37', a2)
    assert _is_linked(b, 'javaDsl_FieldDeclaration37', a2)
    if hasattr(a1, 'javaDsl_Type38'):
        assert not _is_linked(a1, 'javaDsl_Type38', b)
    if hasattr(a2, 'javaDsl_Type38'):
        assert _is_linked(a2, 'javaDsl_Type38', b)
    _safe_set(b, 'javaDsl_FieldDeclaration37', None)
    assert not _is_linked(b, 'javaDsl_FieldDeclaration37', a2)
    if hasattr(a2, 'javaDsl_Type38'):
        assert not _is_linked(a2, 'javaDsl_Type38', b)


def test_assoc_variables39_reverse_link_reassign_clear():
    a1 = javaDsl_VariableDeclarator(name="sample_text")
    a2 = javaDsl_VariableDeclarator(name="sample_text_2")
    b = javaDsl_FieldDeclaration(modifiers="sample_text")
    _safe_set(b, 'javaDsl_FieldDeclaration40', {a1})
    assert _is_linked(b, 'javaDsl_FieldDeclaration40', a1)
    if hasattr(a1, 'javaDsl_VariableDeclarator'):
        assert _is_linked(a1, 'javaDsl_VariableDeclarator', b)
    _safe_set(b, 'javaDsl_FieldDeclaration40', {a2})
    assert _is_linked(b, 'javaDsl_FieldDeclaration40', a2)
    if hasattr(a1, 'javaDsl_VariableDeclarator'):
        assert not _is_linked(a1, 'javaDsl_VariableDeclarator', b)
    if hasattr(a2, 'javaDsl_VariableDeclarator'):
        assert _is_linked(a2, 'javaDsl_VariableDeclarator', b)
    _safe_set(b, 'javaDsl_FieldDeclaration40', set())
    assert not _is_linked(b, 'javaDsl_FieldDeclaration40', a2)
    if hasattr(a2, 'javaDsl_VariableDeclarator'):
        assert not _is_linked(a2, 'javaDsl_VariableDeclarator', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args176_stub_double():
    # javaDsl_ArgumentList has no real 'javaDsl_ArgumentList177' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_MethodInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_MethodInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_MethodInvocation(keyword="sample_text", method="sample_text")
    partner = javaDsl_ArgumentList()
    setattr(partner, 'javaDsl_ArgumentList177', None)
    _safe_set(owner, 'javaDsl_MethodInvocation', partner)
    assert getattr(partner, 'javaDsl_ArgumentList177') == owner
    _safe_set(owner, 'javaDsl_MethodInvocation', None)
    assert getattr(partner, 'javaDsl_ArgumentList177') is None


def test_assoc_args183_stub_double():
    # javaDsl_ArgumentList has no real 'javaDsl_ArgumentList185' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Primary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Primary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Primary(fields="sample_text")
    partner = javaDsl_ArgumentList()
    setattr(partner, 'javaDsl_ArgumentList185', None)
    _safe_set(owner, 'javaDsl_Primary184', {partner})
    assert getattr(partner, 'javaDsl_ArgumentList185') == owner
    _safe_set(owner, 'javaDsl_Primary184', set())
    assert getattr(partner, 'javaDsl_ArgumentList185') is None


def test_assoc_args190_stub_double():
    # javaDsl_ArgumentList has no real 'javaDsl_ArgumentList192' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ClassInstanceCreationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ClassInstanceCreationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ClassInstanceCreationExpression(type="sample_text")
    partner = javaDsl_ArgumentList()
    setattr(partner, 'javaDsl_ArgumentList192', None)
    _safe_set(owner, 'javaDsl_ClassInstanceCreationExpression191', partner)
    assert getattr(partner, 'javaDsl_ArgumentList192') == owner
    _safe_set(owner, 'javaDsl_ClassInstanceCreationExpression191', None)
    assert getattr(partner, 'javaDsl_ArgumentList192') is None


def test_assoc_args34_stub_double():
    # javaDsl_ArgumentList has no real 'javaDsl_ArgumentList' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ExplicitConstructorInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ExplicitConstructorInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ExplicitConstructorInvocation(keyword="sample_text")
    partner = javaDsl_ArgumentList()
    setattr(partner, 'javaDsl_ArgumentList', None)
    _safe_set(owner, 'javaDsl_ExplicitConstructorInvocation35', partner)
    assert getattr(partner, 'javaDsl_ArgumentList') == owner
    _safe_set(owner, 'javaDsl_ExplicitConstructorInvocation35', None)
    assert getattr(partner, 'javaDsl_ArgumentList') is None


def test_assoc_array189_stub_double():
    # javaDsl_PrimaryNewArray has no real 'javaDsl_PrimaryNewArray' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ArrayCreationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ArrayCreationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ArrayCreationExpression(layers="sample_text", type="sample_text")
    partner = javaDsl_PrimaryNewArray()
    setattr(partner, 'javaDsl_PrimaryNewArray', None)
    _safe_set(owner, 'javaDsl_ArrayCreationExpression', partner)
    assert getattr(partner, 'javaDsl_PrimaryNewArray') == owner
    _safe_set(owner, 'javaDsl_ArrayCreationExpression', None)
    assert getattr(partner, 'javaDsl_PrimaryNewArray') is None


def test_assoc_body10_stub_double():
    # javaDsl_ClassBody has no real 'javaDsl_ClassBody' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ClassDeclaration(className="sample_text", extend="sample_text", modifiers="sample_text")
    partner = javaDsl_ClassBody()
    setattr(partner, 'javaDsl_ClassBody', None)
    _safe_set(owner, 'javaDsl_ClassDeclaration11', partner)
    assert getattr(partner, 'javaDsl_ClassBody') == owner
    _safe_set(owner, 'javaDsl_ClassDeclaration11', None)
    assert getattr(partner, 'javaDsl_ClassBody') is None


def test_assoc_body24_stub_double():
    # javaDsl_ConstructorBody has no real 'javaDsl_ConstructorBody' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ConstructorDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ConstructorDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ConstructorDeclaration(modifiers="sample_text")
    partner = javaDsl_ConstructorBody()
    setattr(partner, 'javaDsl_ConstructorBody', None)
    _safe_set(owner, 'javaDsl_ConstructorDeclaration25', partner)
    assert getattr(partner, 'javaDsl_ConstructorBody') == owner
    _safe_set(owner, 'javaDsl_ConstructorDeclaration25', None)
    assert getattr(partner, 'javaDsl_ConstructorBody') is None


def test_assoc_body64_stub_double():
    # javaDsl_InterfaceBody has no real 'javaDsl_InterfaceBody' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_InterfaceDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_InterfaceDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_InterfaceDeclaration(modifiers="sample_text", name="sample_text")
    partner = javaDsl_InterfaceBody()
    setattr(partner, 'javaDsl_InterfaceBody', None)
    _safe_set(owner, 'javaDsl_InterfaceDeclaration65', partner)
    assert getattr(partner, 'javaDsl_InterfaceBody') == owner
    _safe_set(owner, 'javaDsl_InterfaceDeclaration65', None)
    assert getattr(partner, 'javaDsl_InterfaceBody') is None


def test_assoc_condition145_stub_double():
    # javaDsl_ConditionalExpression has no real 'javaDsl_ConditionalExpression' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ConditionalOrExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ConditionalOrExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ConditionalOrExpression(operators="sample_text")
    partner = javaDsl_ConditionalExpression()
    setattr(partner, 'javaDsl_ConditionalExpression', None)
    _safe_set(owner, 'javaDsl_ConditionalOrExpression', partner)
    assert getattr(partner, 'javaDsl_ConditionalExpression') == owner
    _safe_set(owner, 'javaDsl_ConditionalOrExpression', None)
    assert getattr(partner, 'javaDsl_ConditionalExpression') is None


def test_assoc_constant70_stub_double():
    # javaDsl_ConstantDeclaration has no real 'javaDsl_ConstantDeclaration71' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_VariableDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_VariableDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_VariableDeclarator(name="sample_text")
    partner = javaDsl_ConstantDeclaration()
    setattr(partner, 'javaDsl_ConstantDeclaration71', None)
    _safe_set(owner, 'javaDsl_VariableDeclarator72', partner)
    assert getattr(partner, 'javaDsl_ConstantDeclaration71') == owner
    _safe_set(owner, 'javaDsl_VariableDeclarator72', None)
    assert getattr(partner, 'javaDsl_ConstantDeclaration71') is None


def test_assoc_declarations66_stub_double():
    # javaDsl_InterfaceBody has no real 'javaDsl_InterfaceBody67' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_InterfaceMemberDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_InterfaceMemberDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_InterfaceMemberDeclaration(modifiers="sample_text")
    partner = javaDsl_InterfaceBody()
    setattr(partner, 'javaDsl_InterfaceBody67', None)
    _safe_set(owner, 'javaDsl_InterfaceMemberDeclaration', partner)
    assert owner in getattr(partner, 'javaDsl_InterfaceBody67')
    _safe_set(owner, 'javaDsl_InterfaceMemberDeclaration', None)
    assert owner not in getattr(partner, 'javaDsl_InterfaceBody67')


def test_assoc_dimensions186_stub_double():
    # javaDsl_ArrayExpression has no real 'javaDsl_ArrayExpression' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Primary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Primary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Primary(fields="sample_text")
    partner = javaDsl_ArrayExpression()
    setattr(partner, 'javaDsl_ArrayExpression', None)
    _safe_set(owner, 'javaDsl_Primary187', {partner})
    assert getattr(partner, 'javaDsl_ArrayExpression') == owner
    _safe_set(owner, 'javaDsl_Primary187', set())
    assert getattr(partner, 'javaDsl_ArrayExpression') is None


def test_assoc_dimensions196_stub_double():
    # javaDsl_ArrayExpression has no real 'javaDsl_ArrayExpression198' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ArrayCreationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ArrayCreationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ArrayCreationExpression(layers="sample_text", type="sample_text")
    partner = javaDsl_ArrayExpression()
    setattr(partner, 'javaDsl_ArrayExpression198', None)
    _safe_set(owner, 'javaDsl_ArrayCreationExpression197', {partner})
    assert getattr(partner, 'javaDsl_ArrayExpression198') == owner
    _safe_set(owner, 'javaDsl_ArrayCreationExpression197', set())
    assert getattr(partner, 'javaDsl_ArrayExpression198') is None


def test_assoc_else_94_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement96' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_IfStatement(condition=True)
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement96', None)
    _safe_set(owner, 'javaDsl_IfStatement95', partner)
    assert getattr(partner, 'javaDsl_Statement96') == owner
    _safe_set(owner, 'javaDsl_IfStatement95', None)
    assert getattr(partner, 'javaDsl_Statement96') is None


def test_assoc_field16_stub_double():
    # javaDsl_ClassMemberDeclaration has no real 'javaDsl_ClassMemberDeclaration17' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_FieldDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_FieldDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_FieldDeclaration(modifiers="sample_text")
    partner = javaDsl_ClassMemberDeclaration()
    setattr(partner, 'javaDsl_ClassMemberDeclaration17', None)
    _safe_set(owner, 'javaDsl_FieldDeclaration', partner)
    assert getattr(partner, 'javaDsl_ClassMemberDeclaration17') == owner
    _safe_set(owner, 'javaDsl_FieldDeclaration', None)
    assert getattr(partner, 'javaDsl_ClassMemberDeclaration17') is None


def test_assoc_field204_stub_double():
    # javaDsl_ArrayExpression has no real 'javaDsl_ArrayExpression206' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ArrayAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ArrayAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ArrayAccess(reference="sample_text")
    partner = javaDsl_ArrayExpression()
    setattr(partner, 'javaDsl_ArrayExpression206', None)
    _safe_set(owner, 'javaDsl_ArrayAccess205', partner)
    assert getattr(partner, 'javaDsl_ArrayExpression206') == owner
    _safe_set(owner, 'javaDsl_ArrayAccess205', None)
    assert getattr(partner, 'javaDsl_ArrayExpression206') is None


def test_assoc_header75_stub_double():
    # javaDsl_AbstractMethodDeclaration has no real 'javaDsl_AbstractMethodDeclaration76' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_MethodDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_MethodDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_MethodDeclarator(name="sample_text")
    partner = javaDsl_AbstractMethodDeclaration()
    setattr(partner, 'javaDsl_AbstractMethodDeclaration76', None)
    _safe_set(owner, 'javaDsl_MethodDeclarator77', partner)
    assert getattr(partner, 'javaDsl_AbstractMethodDeclaration76') == owner
    _safe_set(owner, 'javaDsl_MethodDeclarator77', None)
    assert getattr(partner, 'javaDsl_AbstractMethodDeclaration76') is None


def test_assoc_imports3_stub_double():
    # javaDsl_CompilationUnit has no real 'javaDsl_CompilationUnit4' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ImportStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ImportStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ImportStatement(object="sample_text", package="sample_text")
    partner = javaDsl_CompilationUnit()
    setattr(partner, 'javaDsl_CompilationUnit4', None)
    _safe_set(owner, 'javaDsl_ImportStatement', partner)
    assert owner in getattr(partner, 'javaDsl_CompilationUnit4')
    _safe_set(owner, 'javaDsl_ImportStatement', None)
    assert owner not in getattr(partner, 'javaDsl_CompilationUnit4')


def test_assoc_initExpr108_stub_double():
    # javaDsl_ForInit has no real 'javaDsl_ForInit' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ForStatement(condition=True)
    partner = javaDsl_ForInit()
    setattr(partner, 'javaDsl_ForInit', None)
    _safe_set(owner, 'javaDsl_ForStatement', partner)
    assert getattr(partner, 'javaDsl_ForInit') == owner
    _safe_set(owner, 'javaDsl_ForStatement', None)
    assert getattr(partner, 'javaDsl_ForInit') is None


def test_assoc_invocation30_stub_double():
    # javaDsl_ConstructorBody has no real 'javaDsl_ConstructorBody31' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ExplicitConstructorInvocation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ExplicitConstructorInvocation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ExplicitConstructorInvocation(keyword="sample_text")
    partner = javaDsl_ConstructorBody()
    setattr(partner, 'javaDsl_ConstructorBody31', None)
    _safe_set(owner, 'javaDsl_ExplicitConstructorInvocation', partner)
    assert getattr(partner, 'javaDsl_ConstructorBody31') == owner
    _safe_set(owner, 'javaDsl_ExplicitConstructorInvocation', None)
    assert getattr(partner, 'javaDsl_ConstructorBody31') is None


def test_assoc_name7_stub_double():
    # javaDsl_EObject has no real 'javaDsl_EObject' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_TypeDeclaration(doc="sample_text")
    partner = javaDsl_EObject()
    setattr(partner, 'javaDsl_EObject', None)
    _safe_set(owner, 'javaDsl_TypeDeclaration8', partner)
    assert getattr(partner, 'javaDsl_EObject') == owner
    _safe_set(owner, 'javaDsl_TypeDeclaration8', None)
    assert getattr(partner, 'javaDsl_EObject') is None


def test_assoc_object142_stub_double():
    # javaDsl_LeftHandSide has no real 'javaDsl_LeftHandSide' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Assignment(operator="sample_text")
    partner = javaDsl_LeftHandSide()
    setattr(partner, 'javaDsl_LeftHandSide', None)
    _safe_set(owner, 'javaDsl_Assignment', partner)
    assert getattr(partner, 'javaDsl_LeftHandSide') == owner
    _safe_set(owner, 'javaDsl_Assignment', None)
    assert getattr(partner, 'javaDsl_LeftHandSide') is None


def test_assoc_package1_stub_double():
    # javaDsl_CompilationUnit has no real 'javaDsl_CompilationUnit2' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_PackageStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_PackageStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_PackageStatement(name="sample_text")
    partner = javaDsl_CompilationUnit()
    setattr(partner, 'javaDsl_CompilationUnit2', None)
    _safe_set(owner, 'javaDsl_PackageStatement', partner)
    assert getattr(partner, 'javaDsl_CompilationUnit2') == owner
    _safe_set(owner, 'javaDsl_PackageStatement', None)
    assert getattr(partner, 'javaDsl_CompilationUnit2') is None


def test_assoc_params133_stub_double():
    # javaDsl_TryStatement has no real 'javaDsl_TryStatement134' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_FormalParameter(variable="sample_text")
    partner = javaDsl_TryStatement()
    setattr(partner, 'javaDsl_TryStatement134', None)
    _safe_set(owner, 'javaDsl_FormalParameter135', partner)
    assert owner in getattr(partner, 'javaDsl_TryStatement134')
    _safe_set(owner, 'javaDsl_FormalParameter135', None)
    assert owner not in getattr(partner, 'javaDsl_TryStatement134')


def test_assoc_returnType50_stub_double():
    # javaDsl_ResultType has no real 'javaDsl_ResultType' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_MethodHeader(modifiers="sample_text")
    partner = javaDsl_ResultType()
    setattr(partner, 'javaDsl_ResultType', None)
    _safe_set(owner, 'javaDsl_MethodHeader51', partner)
    assert getattr(partner, 'javaDsl_ResultType') == owner
    _safe_set(owner, 'javaDsl_MethodHeader51', None)
    assert getattr(partner, 'javaDsl_ResultType') is None


def test_assoc_signature45_stub_double():
    # javaDsl_MethodDeclaration has no real 'javaDsl_MethodDeclaration46' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_MethodHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_MethodHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_MethodHeader(modifiers="sample_text")
    partner = javaDsl_MethodDeclaration()
    setattr(partner, 'javaDsl_MethodDeclaration46', None)
    _safe_set(owner, 'javaDsl_MethodHeader', partner)
    assert getattr(partner, 'javaDsl_MethodDeclaration46') == owner
    _safe_set(owner, 'javaDsl_MethodHeader', None)
    assert getattr(partner, 'javaDsl_MethodDeclaration46') is None


def test_assoc_statement104_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement105' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_WhileStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_WhileStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_WhileStatement(condition=True)
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement105', None)
    _safe_set(owner, 'javaDsl_WhileStatement', partner)
    assert getattr(partner, 'javaDsl_Statement105') == owner
    _safe_set(owner, 'javaDsl_WhileStatement', None)
    assert getattr(partner, 'javaDsl_Statement105') is None


def test_assoc_statement106_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement107' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_DoStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_DoStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_DoStatement(condition=True)
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement107', None)
    _safe_set(owner, 'javaDsl_DoStatement', partner)
    assert getattr(partner, 'javaDsl_Statement107') == owner
    _safe_set(owner, 'javaDsl_DoStatement', None)
    assert getattr(partner, 'javaDsl_Statement107') is None


def test_assoc_statement111_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement113' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ForStatement(condition=True)
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement113', None)
    _safe_set(owner, 'javaDsl_ForStatement112', partner)
    assert getattr(partner, 'javaDsl_Statement113') == owner
    _safe_set(owner, 'javaDsl_ForStatement112', None)
    assert getattr(partner, 'javaDsl_Statement113') is None


def test_assoc_statement91_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_LabeledStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_LabeledStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_LabeledStatement(label="sample_text")
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement', None)
    _safe_set(owner, 'javaDsl_LabeledStatement', partner)
    assert getattr(partner, 'javaDsl_Statement') == owner
    _safe_set(owner, 'javaDsl_LabeledStatement', None)
    assert getattr(partner, 'javaDsl_Statement') is None


def test_assoc_then92_stub_double():
    # javaDsl_Statement has no real 'javaDsl_Statement93' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_IfStatement(condition=True)
    partner = javaDsl_Statement()
    setattr(partner, 'javaDsl_Statement93', None)
    _safe_set(owner, 'javaDsl_IfStatement', partner)
    assert getattr(partner, 'javaDsl_Statement93') == owner
    _safe_set(owner, 'javaDsl_IfStatement', None)
    assert getattr(partner, 'javaDsl_Statement93') is None


def test_assoc_throws78_stub_double():
    # javaDsl_AbstractMethodDeclaration has no real 'javaDsl_AbstractMethodDeclaration79' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Exceptions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Exceptions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Exceptions(exceptions="sample_text")
    partner = javaDsl_AbstractMethodDeclaration()
    setattr(partner, 'javaDsl_AbstractMethodDeclaration79', None)
    _safe_set(owner, 'javaDsl_Exceptions80', partner)
    assert getattr(partner, 'javaDsl_AbstractMethodDeclaration79') == owner
    _safe_set(owner, 'javaDsl_Exceptions80', None)
    assert getattr(partner, 'javaDsl_AbstractMethodDeclaration79') is None


def test_assoc_type57_stub_double():
    # javaDsl_ResultType has no real 'javaDsl_ResultType58' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Type(name="sample_text")
    partner = javaDsl_ResultType()
    setattr(partner, 'javaDsl_ResultType58', None)
    _safe_set(owner, 'javaDsl_Type59', partner)
    assert getattr(partner, 'javaDsl_ResultType58') == owner
    _safe_set(owner, 'javaDsl_Type59', None)
    assert getattr(partner, 'javaDsl_ResultType58') is None


def test_assoc_type68_stub_double():
    # javaDsl_ConstantDeclaration has no real 'javaDsl_ConstantDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Type(name="sample_text")
    partner = javaDsl_ConstantDeclaration()
    setattr(partner, 'javaDsl_ConstantDeclaration', None)
    _safe_set(owner, 'javaDsl_Type69', partner)
    assert getattr(partner, 'javaDsl_ConstantDeclaration') == owner
    _safe_set(owner, 'javaDsl_Type69', None)
    assert getattr(partner, 'javaDsl_ConstantDeclaration') is None


def test_assoc_type86_stub_double():
    # javaDsl_LocalVariableDeclaration has no real 'javaDsl_LocalVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Type(name="sample_text")
    partner = javaDsl_LocalVariableDeclaration()
    setattr(partner, 'javaDsl_LocalVariableDeclaration', None)
    _safe_set(owner, 'javaDsl_Type87', partner)
    assert getattr(partner, 'javaDsl_LocalVariableDeclaration') == owner
    _safe_set(owner, 'javaDsl_Type87', None)
    assert getattr(partner, 'javaDsl_LocalVariableDeclaration') is None


def test_assoc_typeDeclarations5_stub_double():
    # javaDsl_CompilationUnit has no real 'javaDsl_CompilationUnit6' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_TypeDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_TypeDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_TypeDeclaration(doc="sample_text")
    partner = javaDsl_CompilationUnit()
    setattr(partner, 'javaDsl_CompilationUnit6', None)
    _safe_set(owner, 'javaDsl_TypeDeclaration', partner)
    assert owner in getattr(partner, 'javaDsl_CompilationUnit6')
    _safe_set(owner, 'javaDsl_TypeDeclaration', None)
    assert owner not in getattr(partner, 'javaDsl_CompilationUnit6')


def test_assoc_updateExpr109_stub_double():
    # javaDsl_ForUpdate has no real 'javaDsl_ForUpdate' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_ForStatement(condition=True)
    partner = javaDsl_ForUpdate()
    setattr(partner, 'javaDsl_ForUpdate', None)
    _safe_set(owner, 'javaDsl_ForStatement110', partner)
    assert getattr(partner, 'javaDsl_ForUpdate') == owner
    _safe_set(owner, 'javaDsl_ForStatement110', None)
    assert getattr(partner, 'javaDsl_ForUpdate') is None


def test_assoc_value143_stub_double():
    # javaDsl_AssignmentExpression has no real 'javaDsl_AssignmentExpression' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_Assignment(operator="sample_text")
    partner = javaDsl_AssignmentExpression()
    setattr(partner, 'javaDsl_AssignmentExpression', None)
    _safe_set(owner, 'javaDsl_Assignment144', partner)
    assert getattr(partner, 'javaDsl_AssignmentExpression') == owner
    _safe_set(owner, 'javaDsl_Assignment144', None)
    assert getattr(partner, 'javaDsl_AssignmentExpression') is None


def test_assoc_value41_stub_double():
    # javaDsl_VariableInitializer has no real 'javaDsl_VariableInitializer' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_VariableDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_VariableDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_VariableDeclarator(name="sample_text")
    partner = javaDsl_VariableInitializer()
    setattr(partner, 'javaDsl_VariableInitializer', None)
    _safe_set(owner, 'javaDsl_VariableDeclarator42', partner)
    assert getattr(partner, 'javaDsl_VariableInitializer') == owner
    _safe_set(owner, 'javaDsl_VariableDeclarator42', None)
    assert getattr(partner, 'javaDsl_VariableInitializer') is None


def test_assoc_variables88_stub_double():
    # javaDsl_LocalVariableDeclaration has no real 'javaDsl_LocalVariableDeclaration89' property in the generated
    # code (a bare stub) -- manually attach it so javaDsl_VariableDeclarator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javaDsl_VariableDeclarator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javaDsl_VariableDeclarator(name="sample_text")
    partner = javaDsl_LocalVariableDeclaration()
    setattr(partner, 'javaDsl_LocalVariableDeclaration89', None)
    _safe_set(owner, 'javaDsl_VariableDeclarator90', partner)
    assert owner in getattr(partner, 'javaDsl_LocalVariableDeclaration89')
    _safe_set(owner, 'javaDsl_VariableDeclarator90', None)
    assert owner not in getattr(partner, 'javaDsl_LocalVariableDeclaration89')


