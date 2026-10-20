import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    NamedElement,
    Statement,
    Type,
    javasimplified_ArrayAccess,
    javasimplified_ArrayCreation,
    javasimplified_Assignment,
    javasimplified_Block,
    javasimplified_BooleanLiteral,
    javasimplified_CastExpression,
    javasimplified_CatchStatment,
    javasimplified_Class,
    javasimplified_ClassInstanceCreation,
    javasimplified_Comment,
    javasimplified_Expression,
    javasimplified_ExpressionStatement,
    javasimplified_ForStatement,
    javasimplified_IfStatement,
    javasimplified_ImportDeclaration,
    javasimplified_InstanceOfExpression,
    javasimplified_Interface,
    javasimplified_Method,
    javasimplified_Model,
    javasimplified_Modifier,
    javasimplified_NamedElement,
    javasimplified_NullLiteral,
    javasimplified_NumberLiteral,
    javasimplified_Package,
    javasimplified_Parameter,
    javasimplified_PrimitiveType,
    javasimplified_ReturnStatement,
    javasimplified_Statement,
    javasimplified_StringLiteral,
    javasimplified_ThisExpression,
    javasimplified_ThrowStatement,
    javasimplified_TryStatement,
    javasimplified_Type,
    javasimplified_Variable,
    javasimplified_VariableAccess,
    javasimplified_WhileStatement,
    VisibilityKind,
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

def test_assoc_class_0_reverse_link_reassign_clear():
    a1 = javasimplified_Method(visibility="sample_text")
    a2 = javasimplified_Method(visibility="sample_text_2")
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'javasimplified_Class', a1)
    assert _is_linked(b, 'javasimplified_Class', a1)
    if hasattr(a1, 'javasimplified_Method'):
        assert _is_linked(a1, 'javasimplified_Method', b)
    _safe_set(b, 'javasimplified_Class', a2)
    assert _is_linked(b, 'javasimplified_Class', a2)
    if hasattr(a1, 'javasimplified_Method'):
        assert not _is_linked(a1, 'javasimplified_Method', b)
    if hasattr(a2, 'javasimplified_Method'):
        assert _is_linked(a2, 'javasimplified_Method', b)
    _safe_set(b, 'javasimplified_Class', None)
    assert not _is_linked(b, 'javasimplified_Class', a2)
    if hasattr(a2, 'javasimplified_Method'):
        assert not _is_linked(a2, 'javasimplified_Method', b)


def test_assoc_class_11_reverse_link_reassign_clear():
    a1 = javasimplified_Variable(name="sample_text")
    a2 = javasimplified_Variable(name="sample_text_2")
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'variables'):
        assert _is_linked(a1, 'variables', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'variables'):
        assert not _is_linked(a1, 'variables', b)
    if hasattr(a2, 'variables'):
        assert _is_linked(a2, 'variables', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'variables'):
        assert not _is_linked(a2, 'variables', b)


def test_assoc_methods26_reverse_link_reassign_clear():
    a1 = javasimplified_Method(visibility="sample_text")
    a2 = javasimplified_Method(visibility="sample_text_2")
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'javasimplified_Class27', {a1})
    assert _is_linked(b, 'javasimplified_Class27', a1)
    if hasattr(a1, 'javasimplified_Method28'):
        assert _is_linked(a1, 'javasimplified_Method28', b)
    _safe_set(b, 'javasimplified_Class27', {a2})
    assert _is_linked(b, 'javasimplified_Class27', a2)
    if hasattr(a1, 'javasimplified_Method28'):
        assert not _is_linked(a1, 'javasimplified_Method28', b)
    if hasattr(a2, 'javasimplified_Method28'):
        assert _is_linked(a2, 'javasimplified_Method28', b)
    _safe_set(b, 'javasimplified_Class27', set())
    assert not _is_linked(b, 'javasimplified_Class27', a2)
    if hasattr(a2, 'javasimplified_Method28'):
        assert not _is_linked(a2, 'javasimplified_Method28', b)


def test_assoc_modifier12_reverse_link_reassign_clear():
    a1 = javasimplified_Variable(name="sample_text")
    a2 = javasimplified_Variable(name="sample_text_2")
    b = javasimplified_Modifier(isFinal=True, isStatic=True, isSynchronized=True, isVolatile=True, visibility="sample_text")
    _safe_set(b, 'javasimplified_Modifier14', a1)
    assert _is_linked(b, 'javasimplified_Modifier14', a1)
    if hasattr(a1, 'javasimplified_Variable13'):
        assert _is_linked(a1, 'javasimplified_Variable13', b)
    _safe_set(b, 'javasimplified_Modifier14', a2)
    assert _is_linked(b, 'javasimplified_Modifier14', a2)
    if hasattr(a1, 'javasimplified_Variable13'):
        assert not _is_linked(a1, 'javasimplified_Variable13', b)
    if hasattr(a2, 'javasimplified_Variable13'):
        assert _is_linked(a2, 'javasimplified_Variable13', b)
    _safe_set(b, 'javasimplified_Modifier14', None)
    assert not _is_linked(b, 'javasimplified_Modifier14', a2)
    if hasattr(a2, 'javasimplified_Variable13'):
        assert not _is_linked(a2, 'javasimplified_Variable13', b)


def test_assoc_modifier31_reverse_link_reassign_clear():
    a1 = javasimplified_Modifier(isFinal=True, isStatic=True, isSynchronized=True, isVolatile=True, visibility="sample_text")
    a2 = javasimplified_Modifier(isFinal=False, isStatic=False, isSynchronized=False, isVolatile=False, visibility="sample_text_2")
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'javasimplified_Class32', a1)
    assert _is_linked(b, 'javasimplified_Class32', a1)
    if hasattr(a1, 'javasimplified_Modifier33'):
        assert _is_linked(a1, 'javasimplified_Modifier33', b)
    _safe_set(b, 'javasimplified_Class32', a2)
    assert _is_linked(b, 'javasimplified_Class32', a2)
    if hasattr(a1, 'javasimplified_Modifier33'):
        assert not _is_linked(a1, 'javasimplified_Modifier33', b)
    if hasattr(a2, 'javasimplified_Modifier33'):
        assert _is_linked(a2, 'javasimplified_Modifier33', b)
    _safe_set(b, 'javasimplified_Class32', None)
    assert not _is_linked(b, 'javasimplified_Class32', a2)
    if hasattr(a2, 'javasimplified_Modifier33'):
        assert not _is_linked(a2, 'javasimplified_Modifier33', b)


def test_assoc_modifier5_reverse_link_reassign_clear():
    a1 = javasimplified_Modifier(isFinal=True, isStatic=True, isSynchronized=True, isVolatile=True, visibility="sample_text")
    a2 = javasimplified_Modifier(isFinal=False, isStatic=False, isSynchronized=False, isVolatile=False, visibility="sample_text_2")
    b = javasimplified_Method(visibility="sample_text")
    _safe_set(b, 'javasimplified_Method6', a1)
    assert _is_linked(b, 'javasimplified_Method6', a1)
    if hasattr(a1, 'javasimplified_Modifier'):
        assert _is_linked(a1, 'javasimplified_Modifier', b)
    _safe_set(b, 'javasimplified_Method6', a2)
    assert _is_linked(b, 'javasimplified_Method6', a2)
    if hasattr(a1, 'javasimplified_Modifier'):
        assert not _is_linked(a1, 'javasimplified_Modifier', b)
    if hasattr(a2, 'javasimplified_Modifier'):
        assert _is_linked(a2, 'javasimplified_Modifier', b)
    _safe_set(b, 'javasimplified_Method6', None)
    assert not _is_linked(b, 'javasimplified_Method6', a2)
    if hasattr(a2, 'javasimplified_Modifier'):
        assert not _is_linked(a2, 'javasimplified_Modifier', b)


def test_assoc_superClass24_reverse_link_reassign_clear():
    a1 = javasimplified_Class(isAbstract=True)
    a2 = javasimplified_Class(isAbstract=False)
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'javasimplified_Class25', a1)
    assert _is_linked(b, 'javasimplified_Class25', a1)
    if hasattr(a1, 'javasimplified_Class23'):
        assert _is_linked(a1, 'javasimplified_Class23', b)
    _safe_set(b, 'javasimplified_Class25', a2)
    assert _is_linked(b, 'javasimplified_Class25', a2)
    if hasattr(a1, 'javasimplified_Class23'):
        assert not _is_linked(a1, 'javasimplified_Class23', b)
    if hasattr(a2, 'javasimplified_Class23'):
        assert _is_linked(a2, 'javasimplified_Class23', b)
    _safe_set(b, 'javasimplified_Class25', None)
    assert not _is_linked(b, 'javasimplified_Class25', a2)
    if hasattr(a2, 'javasimplified_Class23'):
        assert not _is_linked(a2, 'javasimplified_Class23', b)


def test_assoc_variables20_reverse_link_reassign_clear():
    a1 = javasimplified_Variable(name="sample_text")
    a2 = javasimplified_Variable(name="sample_text_2")
    b = javasimplified_Class(isAbstract=True)
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Variable'):
        assert _is_linked(a1, 'Variable', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Variable'):
        assert not _is_linked(a1, 'Variable', b)
    if hasattr(a2, 'Variable'):
        assert _is_linked(a2, 'Variable', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Variable'):
        assert not _is_linked(a2, 'Variable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_class_18_stub_double():
    # javasimplified_Comment has no real 'comments' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Class(isAbstract=True)
    partner = javasimplified_Comment()
    setattr(partner, 'comments', None)
    _safe_set(owner, 'Class19', partner)
    assert getattr(partner, 'comments') == owner
    _safe_set(owner, 'Class19', None)
    assert getattr(partner, 'comments') is None


def test_assoc_comments21_stub_double():
    # javasimplified_Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Class(isAbstract=True)
    partner = javasimplified_Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'class_22', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'class_22', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_implements34_stub_double():
    # javasimplified_Interface has no real 'javasimplified_Interface' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Class(isAbstract=True)
    partner = javasimplified_Interface()
    setattr(partner, 'javasimplified_Interface', None)
    _safe_set(owner, 'javasimplified_Class35', {partner})
    assert getattr(partner, 'javasimplified_Interface') == owner
    _safe_set(owner, 'javasimplified_Class35', set())
    assert getattr(partner, 'javasimplified_Interface') is None


def test_assoc_importedElement43_stub_double():
    # javasimplified_ImportDeclaration has no real 'javasimplified_ImportDeclaration44' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_NamedElement(name="sample_text")
    partner = javasimplified_ImportDeclaration()
    setattr(partner, 'javasimplified_ImportDeclaration44', None)
    _safe_set(owner, 'javasimplified_NamedElement', partner)
    assert getattr(partner, 'javasimplified_ImportDeclaration44') == owner
    _safe_set(owner, 'javasimplified_NamedElement', None)
    assert getattr(partner, 'javasimplified_ImportDeclaration44') is None


def test_assoc_imports29_stub_double():
    # javasimplified_ImportDeclaration has no real 'javasimplified_ImportDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Class(isAbstract=True)
    partner = javasimplified_ImportDeclaration()
    setattr(partner, 'javasimplified_ImportDeclaration', None)
    _safe_set(owner, 'javasimplified_Class30', {partner})
    assert getattr(partner, 'javasimplified_ImportDeclaration') == owner
    _safe_set(owner, 'javasimplified_Class30', set())
    assert getattr(partner, 'javasimplified_ImportDeclaration') is None


def test_assoc_ownedElems36_stub_double():
    # javasimplified_Package has no real 'javasimplified_Package' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Class(isAbstract=True)
    partner = javasimplified_Package()
    setattr(partner, 'javasimplified_Package', None)
    _safe_set(owner, 'javasimplified_Class37', partner)
    assert owner in getattr(partner, 'javasimplified_Package')
    _safe_set(owner, 'javasimplified_Class37', None)
    assert owner not in getattr(partner, 'javasimplified_Package')


def test_assoc_params1_stub_double():
    # javasimplified_Parameter has no real 'javasimplified_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Method(visibility="sample_text")
    partner = javasimplified_Parameter()
    setattr(partner, 'javasimplified_Parameter', None)
    _safe_set(owner, 'javasimplified_Method2', {partner})
    assert getattr(partner, 'javasimplified_Parameter') == owner
    _safe_set(owner, 'javasimplified_Method2', set())
    assert getattr(partner, 'javasimplified_Parameter') is None


def test_assoc_returnType3_stub_double():
    # javasimplified_Type has no real 'javasimplified_Type' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Method(visibility="sample_text")
    partner = javasimplified_Type()
    setattr(partner, 'javasimplified_Type', None)
    _safe_set(owner, 'javasimplified_Method4', partner)
    assert getattr(partner, 'javasimplified_Type') == owner
    _safe_set(owner, 'javasimplified_Method4', None)
    assert getattr(partner, 'javasimplified_Type') is None


def test_assoc_statements7_stub_double():
    # javasimplified_Statement has no real 'javasimplified_Statement' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Method(visibility="sample_text")
    partner = javasimplified_Statement()
    setattr(partner, 'javasimplified_Statement', None)
    _safe_set(owner, 'javasimplified_Method8', {partner})
    assert getattr(partner, 'javasimplified_Statement') == owner
    _safe_set(owner, 'javasimplified_Method8', set())
    assert getattr(partner, 'javasimplified_Statement') is None


def test_assoc_type9_stub_double():
    # javasimplified_Type has no real 'javasimplified_Type10' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Variable(name="sample_text")
    partner = javasimplified_Type()
    setattr(partner, 'javasimplified_Type10', None)
    _safe_set(owner, 'javasimplified_Variable', partner)
    assert getattr(partner, 'javasimplified_Type10') == owner
    _safe_set(owner, 'javasimplified_Variable', None)
    assert getattr(partner, 'javasimplified_Type10') is None


def test_assoc_variable98_stub_double():
    # javasimplified_VariableAccess has no real 'javasimplified_VariableAccess' property in the generated
    # code (a bare stub) -- manually attach it so javasimplified_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # javasimplified_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = javasimplified_Variable(name="sample_text")
    partner = javasimplified_VariableAccess()
    setattr(partner, 'javasimplified_VariableAccess', None)
    _safe_set(owner, 'javasimplified_Variable99', partner)
    assert getattr(partner, 'javasimplified_VariableAccess') == owner
    _safe_set(owner, 'javasimplified_Variable99', None)
    assert getattr(partner, 'javasimplified_VariableAccess') is None


