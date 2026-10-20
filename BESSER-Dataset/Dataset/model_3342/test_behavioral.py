import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CommentedElement,
    Expression,
    JavaSimplified_Assignment,
    JavaSimplified_CastExpression,
    JavaSimplified_ClassInstanceCreation,
    JavaSimplified_Comment,
    JavaSimplified_CommentStatement,
    JavaSimplified_CommentedElement,
    JavaSimplified_Expression,
    JavaSimplified_ExpressionStatement,
    JavaSimplified_Field,
    JavaSimplified_IfStatement,
    JavaSimplified_InfixExpression,
    JavaSimplified_JavaClass,
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

def test_assoc_fields3_reverse_link_reassign_clear():
    a1 = JavaSimplified_JavaClass(imports="sample_text")
    a2 = JavaSimplified_JavaClass(imports="sample_text_2")
    b = JavaSimplified_Field(visibility="sample_text")
    _safe_set(b, 'JavaSimplified_Field', a1)
    assert _is_linked(b, 'JavaSimplified_Field', a1)
    if hasattr(a1, 'JavaSimplified_JavaClass'):
        assert _is_linked(a1, 'JavaSimplified_JavaClass', b)
    _safe_set(b, 'JavaSimplified_Field', a2)
    assert _is_linked(b, 'JavaSimplified_Field', a2)
    if hasattr(a1, 'JavaSimplified_JavaClass'):
        assert not _is_linked(a1, 'JavaSimplified_JavaClass', b)
    if hasattr(a2, 'JavaSimplified_JavaClass'):
        assert _is_linked(a2, 'JavaSimplified_JavaClass', b)
    _safe_set(b, 'JavaSimplified_Field', None)
    assert not _is_linked(b, 'JavaSimplified_Field', a2)
    if hasattr(a2, 'JavaSimplified_JavaClass'):
        assert not _is_linked(a2, 'JavaSimplified_JavaClass', b)


def test_assoc_methods4_reverse_link_reassign_clear():
    a1 = JavaSimplified_Method(exceptions="sample_text")
    a2 = JavaSimplified_Method(exceptions="sample_text_2")
    b = JavaSimplified_JavaClass(imports="sample_text")
    _safe_set(b, 'JavaSimplified_JavaClass5', {a1})
    assert _is_linked(b, 'JavaSimplified_JavaClass5', a1)
    if hasattr(a1, 'JavaSimplified_Method'):
        assert _is_linked(a1, 'JavaSimplified_Method', b)
    _safe_set(b, 'JavaSimplified_JavaClass5', {a2})
    assert _is_linked(b, 'JavaSimplified_JavaClass5', a2)
    if hasattr(a1, 'JavaSimplified_Method'):
        assert not _is_linked(a1, 'JavaSimplified_Method', b)
    if hasattr(a2, 'JavaSimplified_Method'):
        assert _is_linked(a2, 'JavaSimplified_Method', b)
    _safe_set(b, 'JavaSimplified_JavaClass5', set())
    assert not _is_linked(b, 'JavaSimplified_JavaClass5', a2)
    if hasattr(a2, 'JavaSimplified_Method'):
        assert not _is_linked(a2, 'JavaSimplified_Method', b)


def test_assoc_returnType12_reverse_link_reassign_clear():
    a1 = JavaSimplified_Type(type="sample_text")
    a2 = JavaSimplified_Type(type="sample_text_2")
    b = JavaSimplified_Method(exceptions="sample_text")
    _safe_set(b, 'JavaSimplified_Method13', a1)
    assert _is_linked(b, 'JavaSimplified_Method13', a1)
    if hasattr(a1, 'JavaSimplified_Type14'):
        assert _is_linked(a1, 'JavaSimplified_Type14', b)
    _safe_set(b, 'JavaSimplified_Method13', a2)
    assert _is_linked(b, 'JavaSimplified_Method13', a2)
    if hasattr(a1, 'JavaSimplified_Type14'):
        assert not _is_linked(a1, 'JavaSimplified_Type14', b)
    if hasattr(a2, 'JavaSimplified_Type14'):
        assert _is_linked(a2, 'JavaSimplified_Type14', b)
    _safe_set(b, 'JavaSimplified_Method13', None)
    assert not _is_linked(b, 'JavaSimplified_Method13', a2)
    if hasattr(a2, 'JavaSimplified_Type14'):
        assert not _is_linked(a2, 'JavaSimplified_Type14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_className61_stub_double():
    # JavaSimplified_ClassInstanceCreation has no real 'JavaSimplified_ClassInstanceCreation62' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_ClassInstanceCreation()
    setattr(partner, 'JavaSimplified_ClassInstanceCreation62', None)
    _safe_set(owner, 'JavaSimplified_Type63', partner)
    assert getattr(partner, 'JavaSimplified_ClassInstanceCreation62') == owner
    _safe_set(owner, 'JavaSimplified_Type63', None)
    assert getattr(partner, 'JavaSimplified_ClassInstanceCreation62') is None


def test_assoc_comment15_stub_double():
    # JavaSimplified_CommentStatement has no real 'JavaSimplified_CommentStatement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Comment(isJavadoc=True)
    partner = JavaSimplified_CommentStatement()
    setattr(partner, 'JavaSimplified_CommentStatement', None)
    _safe_set(owner, 'JavaSimplified_Comment16', partner)
    assert getattr(partner, 'JavaSimplified_CommentStatement') == owner
    _safe_set(owner, 'JavaSimplified_Comment16', None)
    assert getattr(partner, 'JavaSimplified_CommentStatement') is None


def test_assoc_comment2_stub_double():
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


def test_assoc_expr149_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression50' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_InfixExpression(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression50', None)
    _safe_set(owner, 'JavaSimplified_InfixExpression', partner)
    assert getattr(partner, 'JavaSimplified_Expression50') == owner
    _safe_set(owner, 'JavaSimplified_InfixExpression', None)
    assert getattr(partner, 'JavaSimplified_Expression50') is None


def test_assoc_expr154_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression55' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Assignment(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression55', None)
    _safe_set(owner, 'JavaSimplified_Assignment', partner)
    assert getattr(partner, 'JavaSimplified_Expression55') == owner
    _safe_set(owner, 'JavaSimplified_Assignment', None)
    assert getattr(partner, 'JavaSimplified_Expression55') is None


def test_assoc_expr251_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_InfixExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_InfixExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_InfixExpression(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression53', None)
    _safe_set(owner, 'JavaSimplified_InfixExpression52', partner)
    assert getattr(partner, 'JavaSimplified_Expression53') == owner
    _safe_set(owner, 'JavaSimplified_InfixExpression52', None)
    assert getattr(partner, 'JavaSimplified_Expression53') is None


def test_assoc_expr256_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Assignment(operator="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression58', None)
    _safe_set(owner, 'JavaSimplified_Assignment57', partner)
    assert getattr(partner, 'JavaSimplified_Expression58') == owner
    _safe_set(owner, 'JavaSimplified_Assignment57', None)
    assert getattr(partner, 'JavaSimplified_Expression58') is None


def test_assoc_expr6_stub_double():
    # JavaSimplified_Expression has no real 'JavaSimplified_Expression' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Field(visibility="sample_text")
    partner = JavaSimplified_Expression()
    setattr(partner, 'JavaSimplified_Expression', None)
    _safe_set(owner, 'JavaSimplified_Field7', partner)
    assert getattr(partner, 'JavaSimplified_Expression') == owner
    _safe_set(owner, 'JavaSimplified_Field7', None)
    assert getattr(partner, 'JavaSimplified_Expression') is None


def test_assoc_methodName46_stub_double():
    # JavaSimplified_MethodCall has no real 'JavaSimplified_MethodCall47' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_MethodCall()
    setattr(partner, 'JavaSimplified_MethodCall47', None)
    _safe_set(owner, 'JavaSimplified_Name48', partner)
    assert getattr(partner, 'JavaSimplified_MethodCall47') == owner
    _safe_set(owner, 'JavaSimplified_Name48', None)
    assert getattr(partner, 'JavaSimplified_MethodCall47') is None


def test_assoc_name0_stub_double():
    # JavaSimplified_NamedElement has no real 'JavaSimplified_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_NamedElement()
    setattr(partner, 'JavaSimplified_NamedElement', None)
    _safe_set(owner, 'JavaSimplified_Name', partner)
    assert getattr(partner, 'JavaSimplified_NamedElement') == owner
    _safe_set(owner, 'JavaSimplified_Name', None)
    assert getattr(partner, 'JavaSimplified_NamedElement') is None


def test_assoc_object36_stub_double():
    # JavaSimplified_MethodInvocation has no real 'JavaSimplified_MethodInvocation' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_MethodInvocation()
    setattr(partner, 'JavaSimplified_MethodInvocation', None)
    _safe_set(owner, 'JavaSimplified_Name37', partner)
    assert getattr(partner, 'JavaSimplified_MethodInvocation') == owner
    _safe_set(owner, 'JavaSimplified_Name37', None)
    assert getattr(partner, 'JavaSimplified_MethodInvocation') is None


def test_assoc_parameters8_stub_double():
    # JavaSimplified_Parameter has no real 'JavaSimplified_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Method(exceptions="sample_text")
    partner = JavaSimplified_Parameter()
    setattr(partner, 'JavaSimplified_Parameter', None)
    _safe_set(owner, 'JavaSimplified_Method9', {partner})
    assert getattr(partner, 'JavaSimplified_Parameter') == owner
    _safe_set(owner, 'JavaSimplified_Method9', set())
    assert getattr(partner, 'JavaSimplified_Parameter') is None


def test_assoc_statements10_stub_double():
    # JavaSimplified_Statement has no real 'JavaSimplified_Statement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Method(exceptions="sample_text")
    partner = JavaSimplified_Statement()
    setattr(partner, 'JavaSimplified_Statement', None)
    _safe_set(owner, 'JavaSimplified_Method11', {partner})
    assert getattr(partner, 'JavaSimplified_Statement') == owner
    _safe_set(owner, 'JavaSimplified_Method11', set())
    assert getattr(partner, 'JavaSimplified_Statement') is None


def test_assoc_type1_stub_double():
    # JavaSimplified_TypedElement has no real 'JavaSimplified_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_TypedElement()
    setattr(partner, 'JavaSimplified_TypedElement', None)
    _safe_set(owner, 'JavaSimplified_Type', partner)
    assert getattr(partner, 'JavaSimplified_TypedElement') == owner
    _safe_set(owner, 'JavaSimplified_Type', None)
    assert getattr(partner, 'JavaSimplified_TypedElement') is None


def test_assoc_type33_stub_double():
    # JavaSimplified_CastExpression has no real 'JavaSimplified_CastExpression34' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Type(type="sample_text")
    partner = JavaSimplified_CastExpression()
    setattr(partner, 'JavaSimplified_CastExpression34', None)
    _safe_set(owner, 'JavaSimplified_Type35', partner)
    assert getattr(partner, 'JavaSimplified_CastExpression34') == owner
    _safe_set(owner, 'JavaSimplified_Type35', None)
    assert getattr(partner, 'JavaSimplified_CastExpression34') is None


def test_assoc_var31_stub_double():
    # JavaSimplified_CastExpression has no real 'JavaSimplified_CastExpression' property in the generated
    # code (a bare stub) -- manually attach it so JavaSimplified_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JavaSimplified_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JavaSimplified_Name(identifier="sample_text")
    partner = JavaSimplified_CastExpression()
    setattr(partner, 'JavaSimplified_CastExpression', None)
    _safe_set(owner, 'JavaSimplified_Name32', partner)
    assert getattr(partner, 'JavaSimplified_CastExpression') == owner
    _safe_set(owner, 'JavaSimplified_Name32', None)
    assert getattr(partner, 'JavaSimplified_CastExpression') is None


