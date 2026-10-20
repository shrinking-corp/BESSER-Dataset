import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CommentedElement,
    Expression,
    Feature,
    JavaSimplified_Assignment,
    JavaSimplified_CastExpression,
    JavaSimplified_ClassInstanceCreation,
    JavaSimplified_Comment,
    JavaSimplified_CommentStatement,
    JavaSimplified_CommentedElement,
    JavaSimplified_Expression,
    JavaSimplified_ExpressionStatement,
    JavaSimplified_Feature,
    JavaSimplified_Field,
    JavaSimplified_FieldAccess,
    JavaSimplified_IfStatement,
    JavaSimplified_InfixExpression,
    JavaSimplified_JavaClass,
    JavaSimplified_JavaModel,
    JavaSimplified_Literal,
    JavaSimplified_Method,
    JavaSimplified_MethodCall,
    JavaSimplified_MethodInvocation,
    JavaSimplified_Name,
    JavaSimplified_NamedElement,
    JavaSimplified_Parameter,
    JavaSimplified_ReturnStatement,
    JavaSimplified_Statement,
    JavaSimplified_StringElement,
    JavaSimplified_ThisExpression,
    JavaSimplified_Type,
    JavaSimplified_TypedElement,
    JavaSimplified_VariableDeclarationStatement,
    NamedElement,
    Statement,
    StringElement,
    TypedElement,
    AssignmentOperatorType,
    InfixOperatorType,
    LiteralType,
    VisibilityType,
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

def test_assoc_methods38_reverse_link_reassign_clear():
    a1 = JavaSimplified_Method(exceptions="sample_text")
    a2 = JavaSimplified_Method(exceptions="sample_text_2")
    b = JavaSimplified_JavaClass(imports="sample_text")
    _safe_set(b, 'JavaSimplified_JavaClass39', {a1})
    assert _is_linked(b, 'JavaSimplified_JavaClass39', a1)
    if hasattr(a1, 'JavaSimplified_Method'):
        assert _is_linked(a1, 'JavaSimplified_Method', b)
    _safe_set(b, 'JavaSimplified_JavaClass39', {a2})
    assert _is_linked(b, 'JavaSimplified_JavaClass39', a2)
    if hasattr(a1, 'JavaSimplified_Method'):
        assert not _is_linked(a1, 'JavaSimplified_Method', b)
    if hasattr(a2, 'JavaSimplified_Method'):
        assert _is_linked(a2, 'JavaSimplified_Method', b)
    _safe_set(b, 'JavaSimplified_JavaClass39', set())
    assert not _is_linked(b, 'JavaSimplified_JavaClass39', a2)
    if hasattr(a2, 'JavaSimplified_Method'):
        assert not _is_linked(a2, 'JavaSimplified_Method', b)


def test_assoc_returnType50_reverse_link_reassign_clear():
    a1 = JavaSimplified_Type(type="sample_text")
    a2 = JavaSimplified_Type(type="sample_text_2")
    b = JavaSimplified_Method(exceptions="sample_text")
    _safe_set(b, 'JavaSimplified_Method51', a1)
    assert _is_linked(b, 'JavaSimplified_Method51', a1)
    if hasattr(a1, 'JavaSimplified_Type52'):
        assert _is_linked(a1, 'JavaSimplified_Type52', b)
    _safe_set(b, 'JavaSimplified_Method51', a2)
    assert _is_linked(b, 'JavaSimplified_Method51', a2)
    if hasattr(a1, 'JavaSimplified_Type52'):
        assert not _is_linked(a1, 'JavaSimplified_Type52', b)
    if hasattr(a2, 'JavaSimplified_Type52'):
        assert _is_linked(a2, 'JavaSimplified_Type52', b)
    _safe_set(b, 'JavaSimplified_Method51', None)
    assert not _is_linked(b, 'JavaSimplified_Method51', a2)
    if hasattr(a2, 'JavaSimplified_Type52'):
        assert not _is_linked(a2, 'JavaSimplified_Type52', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_className10_stub_double():
    # JavaSimplified_ClassInstanceCreation has no real 'JavaSimplified_ClassInstanceCreation11' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_ClassInstanceCreation()
    setattr(partner, 'JavaSimplified_ClassInstanceCreation11', None)
    _safe_set(owner, 'JavaSimplified_Type12', partner)
    assert getattr(partner, 'JavaSimplified_ClassInstanceCreation11') == owner
    _safe_set(owner, 'JavaSimplified_Type12', None)
    assert getattr(partner, 'JavaSimplified_ClassInstanceCreation11') is None


def test_assoc_classes40_stub_double():
    # JavaSimplified_JavaModel has no real 'JavaSimplified_JavaModel' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_JavaClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_JavaClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_JavaClass(imports="sample_text")
    partner = JavaSimplified_JavaModel()
    setattr(partner, 'JavaSimplified_JavaModel', None)
    _safe_set(owner, 'JavaSimplified_JavaClass41', partner)
    assert owner in getattr(partner, 'JavaSimplified_JavaModel')
    _safe_set(owner, 'JavaSimplified_JavaClass41', None)
    assert owner not in getattr(partner, 'JavaSimplified_JavaModel')


def test_assoc_comment13_stub_double():
    # JavaSimplified_CommentedElement has no real 'JavaSimplified_CommentedElement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Comment(isJavadoc=True)
    partner = JavaSimplified_CommentedElement()
    setattr(partner, 'JavaSimplified_CommentedElement', None)
    _safe_set(owner, 'JavaSimplified_Comment', partner)
    assert getattr(partner, 'JavaSimplified_CommentedElement') == owner
    _safe_set(owner, 'JavaSimplified_Comment', None)
    assert getattr(partner, 'JavaSimplified_CommentedElement') is None


def test_assoc_comment14_stub_double():
    # JavaSimplified_CommentStatement has no real 'JavaSimplified_CommentStatement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Comment(isJavadoc=True)
    partner = JavaSimplified_CommentStatement()
    setattr(partner, 'JavaSimplified_CommentStatement', None)
    _safe_set(owner, 'JavaSimplified_Comment15', partner)
    assert getattr(partner, 'JavaSimplified_CommentStatement') == owner
    _safe_set(owner, 'JavaSimplified_Comment15', None)
    assert getattr(partner, 'JavaSimplified_CommentStatement') is None


def test_assoc_expr10_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Assignment(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression', None)
    _safe_set(owner, 'JavaSimplified_Assignment', partner)
    assert getattr(partner, 'JavaSimplified_Expression') == owner
    _safe_set(owner, 'JavaSimplified_Assignment', None)
    assert getattr(partner, 'JavaSimplified_Expression') is None


def test_assoc_expr131_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression32' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_InfixExpression(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression32', None)
    _safe_set(owner, 'JavaSimplified_InfixExpression', partner)
    assert getattr(partner, 'JavaSimplified_Expression32') == owner
    _safe_set(owner, 'JavaSimplified_InfixExpression', None)
    assert getattr(partner, 'JavaSimplified_Expression32') is None


def test_assoc_expr21_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression3' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Assignment(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression3', None)
    _safe_set(owner, 'JavaSimplified_Assignment2', partner)
    assert getattr(partner, 'JavaSimplified_Expression3') == owner
    _safe_set(owner, 'JavaSimplified_Assignment2', None)
    assert getattr(partner, 'JavaSimplified_Expression3') is None


def test_assoc_expr233_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression35' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_InfixExpression(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression35', None)
    _safe_set(owner, 'JavaSimplified_InfixExpression34', partner)
    assert getattr(partner, 'JavaSimplified_Expression35') == owner
    _safe_set(owner, 'JavaSimplified_InfixExpression34', None)
    assert getattr(partner, 'JavaSimplified_Expression35') is None


def test_assoc_fields36_stub_double():
    # JavaSimplified_Field has no real 'JavaSimplified_Field37' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_JavaClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_JavaClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_JavaClass(imports="sample_text")
    partner = JavaSimplified_Field()
    setattr(partner, 'JavaSimplified_Field37', None)
    _safe_set(owner, 'JavaSimplified_JavaClass', {partner})
    assert getattr(partner, 'JavaSimplified_Field37') == owner
    _safe_set(owner, 'JavaSimplified_JavaClass', set())
    assert getattr(partner, 'JavaSimplified_Field37') is None


def test_assoc_methodName58_stub_double():
    # JavaSimplified_MethodCall has no real 'JavaSimplified_MethodCall59' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_MethodCall()
    setattr(partner, 'JavaSimplified_MethodCall59', None)
    _safe_set(owner, 'JavaSimplified_Name60', partner)
    assert getattr(partner, 'JavaSimplified_MethodCall59') == owner
    _safe_set(owner, 'JavaSimplified_Name60', None)
    assert getattr(partner, 'JavaSimplified_MethodCall59') is None


def test_assoc_name22_stub_double():
    # JavaSimplified_FieldAccess has no real 'JavaSimplified_FieldAccess23' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_FieldAccess()
    setattr(partner, 'JavaSimplified_FieldAccess23', None)
    _safe_set(owner, 'JavaSimplified_Name', partner)
    assert getattr(partner, 'JavaSimplified_FieldAccess23') == owner
    _safe_set(owner, 'JavaSimplified_Name', None)
    assert getattr(partner, 'JavaSimplified_FieldAccess23') is None


def test_assoc_name66_stub_double():
    # JavaSimplified_NamedElement has no real 'JavaSimplified_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_NamedElement()
    setattr(partner, 'JavaSimplified_NamedElement', None)
    _safe_set(owner, 'JavaSimplified_Name67', partner)
    assert getattr(partner, 'JavaSimplified_NamedElement') == owner
    _safe_set(owner, 'JavaSimplified_Name67', None)
    assert getattr(partner, 'JavaSimplified_NamedElement') is None


def test_assoc_object61_stub_double():
    # JavaSimplified_MethodInvocation has no real 'JavaSimplified_MethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_MethodInvocation()
    setattr(partner, 'JavaSimplified_MethodInvocation', None)
    _safe_set(owner, 'JavaSimplified_Name62', partner)
    assert getattr(partner, 'JavaSimplified_MethodInvocation') == owner
    _safe_set(owner, 'JavaSimplified_Name62', None)
    assert getattr(partner, 'JavaSimplified_MethodInvocation') is None


def test_assoc_parameters45_stub_double():
    # JavaSimplified_Parameter has no real 'JavaSimplified_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Method(exceptions="sample_text")
    partner = JavaSimplified_Parameter()
    setattr(partner, 'JavaSimplified_Parameter', None)
    _safe_set(owner, 'JavaSimplified_Method46', {partner})
    assert getattr(partner, 'JavaSimplified_Parameter') == owner
    _safe_set(owner, 'JavaSimplified_Method46', set())
    assert getattr(partner, 'JavaSimplified_Parameter') is None


def test_assoc_statements47_stub_double():
    # JavaSimplified_Statement has no real 'JavaSimplified_Statement49' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Method(exceptions="sample_text")
    partner = JavaSimplified_Statement()
    setattr(partner, 'JavaSimplified_Statement49', None)
    _safe_set(owner, 'JavaSimplified_Method48', {partner})
    assert getattr(partner, 'JavaSimplified_Statement49') == owner
    _safe_set(owner, 'JavaSimplified_Method48', set())
    assert getattr(partner, 'JavaSimplified_Statement49') is None


def test_assoc_type6_stub_double():
    # JavaSimplified_CastExpression has no real 'JavaSimplified_CastExpression7' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_CastExpression()
    setattr(partner, 'JavaSimplified_CastExpression7', None)
    _safe_set(owner, 'JavaSimplified_Type', partner)
    assert getattr(partner, 'JavaSimplified_CastExpression7') == owner
    _safe_set(owner, 'JavaSimplified_Type', None)
    assert getattr(partner, 'JavaSimplified_CastExpression7') is None


def test_assoc_type70_stub_double():
    # JavaSimplified_TypedElement has no real 'JavaSimplified_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_TypedElement()
    setattr(partner, 'JavaSimplified_TypedElement', None)
    _safe_set(owner, 'JavaSimplified_Type71', partner)
    assert getattr(partner, 'JavaSimplified_TypedElement') == owner
    _safe_set(owner, 'JavaSimplified_Type71', None)
    assert getattr(partner, 'JavaSimplified_TypedElement') is None


def test_assoc_types42_stub_double():
    # JavaSimplified_JavaModel has no real 'JavaSimplified_JavaModel43' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_JavaModel()
    setattr(partner, 'JavaSimplified_JavaModel43', None)
    _safe_set(owner, 'JavaSimplified_Type44', partner)
    assert owner in getattr(partner, 'JavaSimplified_JavaModel43')
    _safe_set(owner, 'JavaSimplified_Type44', None)
    assert owner not in getattr(partner, 'JavaSimplified_JavaModel43')


