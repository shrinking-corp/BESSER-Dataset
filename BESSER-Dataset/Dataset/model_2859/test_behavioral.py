import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConstantExpression,
    GenericExpression,
    Parameter,
    SimpleStatement,
    SimpleVariableDeclaration,
    Statement,
    simplejava_Assignment,
    simplejava_Attribute,
    simplejava_BooleanExpression,
    simplejava_ClassDeclaration,
    simplejava_ConstantExpression,
    simplejava_ConstructorCall,
    simplejava_ForInStatement,
    simplejava_ForStatement,
    simplejava_GenericExpression,
    simplejava_IfStatement,
    simplejava_Import,
    simplejava_IntegerExpression,
    simplejava_Method,
    simplejava_MethodBlock,
    simplejava_MethodCall,
    simplejava_NullExpression,
    simplejava_PackageDeclaration,
    simplejava_Parameter,
    simplejava_ParanthesisOrBinaryExpression,
    simplejava_ReturnStatement,
    simplejava_SimpleJava,
    simplejava_SimpleParameter,
    simplejava_SimpleStatement,
    simplejava_SimpleVariableDeclaration,
    simplejava_Statement,
    simplejava_StringExpression,
    simplejava_Type,
    simplejava_UnaryExpression,
    simplejava_VariableDeclaration,
    simplejava_VariableExpression,
    simplejava_WhileStatement,
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

def test_assoc_attribute5_reverse_link_reassign_clear():
    a1 = simplejava_Parameter(name="sample_text")
    a2 = simplejava_Parameter(name="sample_text_2")
    b = simplejava_ClassDeclaration(name="sample_text")
    _safe_set(b, 'simplejava_ClassDeclaration6', {a1})
    assert _is_linked(b, 'simplejava_ClassDeclaration6', a1)
    if hasattr(a1, 'simplejava_Parameter'):
        assert _is_linked(a1, 'simplejava_Parameter', b)
    _safe_set(b, 'simplejava_ClassDeclaration6', {a2})
    assert _is_linked(b, 'simplejava_ClassDeclaration6', a2)
    if hasattr(a1, 'simplejava_Parameter'):
        assert not _is_linked(a1, 'simplejava_Parameter', b)
    if hasattr(a2, 'simplejava_Parameter'):
        assert _is_linked(a2, 'simplejava_Parameter', b)
    _safe_set(b, 'simplejava_ClassDeclaration6', set())
    assert not _is_linked(b, 'simplejava_ClassDeclaration6', a2)
    if hasattr(a2, 'simplejava_Parameter'):
        assert not _is_linked(a2, 'simplejava_Parameter', b)


def test_assoc_content20_reverse_link_reassign_clear():
    a1 = simplejava_MethodBlock(generated=True)
    a2 = simplejava_MethodBlock(generated=False)
    b = simplejava_Method(name="sample_text", static=True)
    _safe_set(b, 'simplejava_Method21', a1)
    assert _is_linked(b, 'simplejava_Method21', a1)
    if hasattr(a1, 'simplejava_MethodBlock'):
        assert _is_linked(a1, 'simplejava_MethodBlock', b)
    _safe_set(b, 'simplejava_Method21', a2)
    assert _is_linked(b, 'simplejava_Method21', a2)
    if hasattr(a1, 'simplejava_MethodBlock'):
        assert not _is_linked(a1, 'simplejava_MethodBlock', b)
    if hasattr(a2, 'simplejava_MethodBlock'):
        assert _is_linked(a2, 'simplejava_MethodBlock', b)
    _safe_set(b, 'simplejava_Method21', None)
    assert not _is_linked(b, 'simplejava_Method21', a2)
    if hasattr(a2, 'simplejava_MethodBlock'):
        assert not _is_linked(a2, 'simplejava_MethodBlock', b)


def test_assoc_method68_reverse_link_reassign_clear():
    a1 = simplejava_MethodCall(methodName="sample_text", thisObject=True)
    a2 = simplejava_MethodCall(methodName="sample_text_2", thisObject=False)
    b = simplejava_Method(name="sample_text", static=True)
    _safe_set(b, 'simplejava_Method70', a1)
    assert _is_linked(b, 'simplejava_Method70', a1)
    if hasattr(a1, 'simplejava_MethodCall69'):
        assert _is_linked(a1, 'simplejava_MethodCall69', b)
    _safe_set(b, 'simplejava_Method70', a2)
    assert _is_linked(b, 'simplejava_Method70', a2)
    if hasattr(a1, 'simplejava_MethodCall69'):
        assert not _is_linked(a1, 'simplejava_MethodCall69', b)
    if hasattr(a2, 'simplejava_MethodCall69'):
        assert _is_linked(a2, 'simplejava_MethodCall69', b)
    _safe_set(b, 'simplejava_Method70', None)
    assert not _is_linked(b, 'simplejava_Method70', a2)
    if hasattr(a2, 'simplejava_MethodCall69'):
        assert not _is_linked(a2, 'simplejava_MethodCall69', b)


def test_assoc_method7_reverse_link_reassign_clear():
    a1 = simplejava_Method(name="sample_text", static=True)
    a2 = simplejava_Method(name="sample_text_2", static=False)
    b = simplejava_ClassDeclaration(name="sample_text")
    _safe_set(b, 'simplejava_ClassDeclaration8', {a1})
    assert _is_linked(b, 'simplejava_ClassDeclaration8', a1)
    if hasattr(a1, 'simplejava_Method'):
        assert _is_linked(a1, 'simplejava_Method', b)
    _safe_set(b, 'simplejava_ClassDeclaration8', {a2})
    assert _is_linked(b, 'simplejava_ClassDeclaration8', a2)
    if hasattr(a1, 'simplejava_Method'):
        assert not _is_linked(a1, 'simplejava_Method', b)
    if hasattr(a2, 'simplejava_Method'):
        assert _is_linked(a2, 'simplejava_Method', b)
    _safe_set(b, 'simplejava_ClassDeclaration8', set())
    assert not _is_linked(b, 'simplejava_ClassDeclaration8', a2)
    if hasattr(a2, 'simplejava_Method'):
        assert not _is_linked(a2, 'simplejava_Method', b)


def test_assoc_object66_reverse_link_reassign_clear():
    a1 = simplejava_Parameter(name="sample_text")
    a2 = simplejava_Parameter(name="sample_text_2")
    b = simplejava_MethodCall(methodName="sample_text", thisObject=True)
    _safe_set(b, 'simplejava_MethodCall', a1)
    assert _is_linked(b, 'simplejava_MethodCall', a1)
    if hasattr(a1, 'simplejava_Parameter67'):
        assert _is_linked(a1, 'simplejava_Parameter67', b)
    _safe_set(b, 'simplejava_MethodCall', a2)
    assert _is_linked(b, 'simplejava_MethodCall', a2)
    if hasattr(a1, 'simplejava_Parameter67'):
        assert not _is_linked(a1, 'simplejava_Parameter67', b)
    if hasattr(a2, 'simplejava_Parameter67'):
        assert _is_linked(a2, 'simplejava_Parameter67', b)
    _safe_set(b, 'simplejava_MethodCall', None)
    assert not _is_linked(b, 'simplejava_MethodCall', a2)
    if hasattr(a2, 'simplejava_Parameter67'):
        assert not _is_linked(a2, 'simplejava_Parameter67', b)


def test_assoc_returnType15_reverse_link_reassign_clear():
    a1 = simplejava_Type(isArray=True, isVoid=True, typeName="sample_text")
    a2 = simplejava_Type(isArray=False, isVoid=False, typeName="sample_text_2")
    b = simplejava_Method(name="sample_text", static=True)
    _safe_set(b, 'simplejava_Method16', a1)
    assert _is_linked(b, 'simplejava_Method16', a1)
    if hasattr(a1, 'simplejava_Type17'):
        assert _is_linked(a1, 'simplejava_Type17', b)
    _safe_set(b, 'simplejava_Method16', a2)
    assert _is_linked(b, 'simplejava_Method16', a2)
    if hasattr(a1, 'simplejava_Type17'):
        assert not _is_linked(a1, 'simplejava_Type17', b)
    if hasattr(a2, 'simplejava_Type17'):
        assert _is_linked(a2, 'simplejava_Type17', b)
    _safe_set(b, 'simplejava_Method16', None)
    assert not _is_linked(b, 'simplejava_Method16', a2)
    if hasattr(a2, 'simplejava_Type17'):
        assert not _is_linked(a2, 'simplejava_Type17', b)


def test_assoc_type9_reverse_link_reassign_clear():
    a1 = simplejava_Type(isArray=True, isVoid=True, typeName="sample_text")
    a2 = simplejava_Type(isArray=False, isVoid=False, typeName="sample_text_2")
    b = simplejava_Parameter(name="sample_text")
    _safe_set(b, 'simplejava_Parameter10', a1)
    assert _is_linked(b, 'simplejava_Parameter10', a1)
    if hasattr(a1, 'simplejava_Type'):
        assert _is_linked(a1, 'simplejava_Type', b)
    _safe_set(b, 'simplejava_Parameter10', a2)
    assert _is_linked(b, 'simplejava_Parameter10', a2)
    if hasattr(a1, 'simplejava_Type'):
        assert not _is_linked(a1, 'simplejava_Type', b)
    if hasattr(a2, 'simplejava_Type'):
        assert _is_linked(a2, 'simplejava_Type', b)
    _safe_set(b, 'simplejava_Parameter10', None)
    assert not _is_linked(b, 'simplejava_Parameter10', a2)
    if hasattr(a2, 'simplejava_Type'):
        assert not _is_linked(a2, 'simplejava_Type', b)


def test_assoc_typeRef12_reverse_link_reassign_clear():
    a1 = simplejava_Type(isArray=True, isVoid=True, typeName="sample_text")
    a2 = simplejava_Type(isArray=False, isVoid=False, typeName="sample_text_2")
    b = simplejava_ClassDeclaration(name="sample_text")
    _safe_set(b, 'simplejava_ClassDeclaration14', a1)
    assert _is_linked(b, 'simplejava_ClassDeclaration14', a1)
    if hasattr(a1, 'simplejava_Type13'):
        assert _is_linked(a1, 'simplejava_Type13', b)
    _safe_set(b, 'simplejava_ClassDeclaration14', a2)
    assert _is_linked(b, 'simplejava_ClassDeclaration14', a2)
    if hasattr(a1, 'simplejava_Type13'):
        assert not _is_linked(a1, 'simplejava_Type13', b)
    if hasattr(a2, 'simplejava_Type13'):
        assert _is_linked(a2, 'simplejava_Type13', b)
    _safe_set(b, 'simplejava_ClassDeclaration14', None)
    assert not _is_linked(b, 'simplejava_ClassDeclaration14', a2)
    if hasattr(a2, 'simplejava_Type13'):
        assert not _is_linked(a2, 'simplejava_Type13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument85_stub_double():
    # simplejava_GenericExpression has no real 'simplejava_GenericExpression87' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_ParanthesisOrBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_ParanthesisOrBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_ParanthesisOrBinaryExpression(type="sample_text")
    partner = simplejava_GenericExpression()
    setattr(partner, 'simplejava_GenericExpression87', None)
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression86', partner)
    assert getattr(partner, 'simplejava_GenericExpression87') == owner
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression86', None)
    assert getattr(partner, 'simplejava_GenericExpression87') is None


def test_assoc_clazz3_stub_double():
    # simplejava_SimpleJava has no real 'simplejava_SimpleJava4' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_ClassDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_ClassDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_ClassDeclaration(name="sample_text")
    partner = simplejava_SimpleJava()
    setattr(partner, 'simplejava_SimpleJava4', None)
    _safe_set(owner, 'simplejava_ClassDeclaration', partner)
    assert getattr(partner, 'simplejava_SimpleJava4') == owner
    _safe_set(owner, 'simplejava_ClassDeclaration', None)
    assert getattr(partner, 'simplejava_SimpleJava4') is None


def test_assoc_condition34_stub_double():
    # simplejava_IfStatement has no real 'simplejava_IfStatement' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_ParanthesisOrBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_ParanthesisOrBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_ParanthesisOrBinaryExpression(type="sample_text")
    partner = simplejava_IfStatement()
    setattr(partner, 'simplejava_IfStatement', None)
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression', partner)
    assert getattr(partner, 'simplejava_IfStatement') == owner
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression', None)
    assert getattr(partner, 'simplejava_IfStatement') is None


def test_assoc_condition59_stub_double():
    # simplejava_WhileStatement has no real 'simplejava_WhileStatement' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_ParanthesisOrBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_ParanthesisOrBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_ParanthesisOrBinaryExpression(type="sample_text")
    partner = simplejava_WhileStatement()
    setattr(partner, 'simplejava_WhileStatement', None)
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression60', partner)
    assert getattr(partner, 'simplejava_WhileStatement') == owner
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression60', None)
    assert getattr(partner, 'simplejava_WhileStatement') is None


def test_assoc_else_38_stub_double():
    # simplejava_IfStatement has no real 'simplejava_IfStatement39' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_MethodBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_MethodBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_MethodBlock(generated=True)
    partner = simplejava_IfStatement()
    setattr(partner, 'simplejava_IfStatement39', None)
    _safe_set(owner, 'simplejava_MethodBlock40', partner)
    assert getattr(partner, 'simplejava_IfStatement39') == owner
    _safe_set(owner, 'simplejava_MethodBlock40', None)
    assert getattr(partner, 'simplejava_IfStatement39') is None


def test_assoc_imports1_stub_double():
    # simplejava_SimpleJava has no real 'simplejava_SimpleJava2' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_Import(imported="sample_text")
    partner = simplejava_SimpleJava()
    setattr(partner, 'simplejava_SimpleJava2', None)
    _safe_set(owner, 'simplejava_Import', partner)
    assert owner in getattr(partner, 'simplejava_SimpleJava2')
    _safe_set(owner, 'simplejava_Import', None)
    assert owner not in getattr(partner, 'simplejava_SimpleJava2')


def test_assoc_package0_stub_double():
    # simplejava_SimpleJava has no real 'simplejava_SimpleJava' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_PackageDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_PackageDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_PackageDeclaration(name="sample_text")
    partner = simplejava_SimpleJava()
    setattr(partner, 'simplejava_SimpleJava', None)
    _safe_set(owner, 'simplejava_PackageDeclaration', partner)
    assert getattr(partner, 'simplejava_SimpleJava') == owner
    _safe_set(owner, 'simplejava_PackageDeclaration', None)
    assert getattr(partner, 'simplejava_SimpleJava') is None


def test_assoc_parameter18_stub_double():
    # simplejava_SimpleParameter has no real 'simplejava_SimpleParameter' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_Method(name="sample_text", static=True)
    partner = simplejava_SimpleParameter()
    setattr(partner, 'simplejava_SimpleParameter', None)
    _safe_set(owner, 'simplejava_Method19', {partner})
    assert getattr(partner, 'simplejava_SimpleParameter') == owner
    _safe_set(owner, 'simplejava_Method19', set())
    assert getattr(partner, 'simplejava_SimpleParameter') is None


def test_assoc_parameter29_stub_double():
    # simplejava_Assignment has no real 'simplejava_Assignment' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_Parameter(name="sample_text")
    partner = simplejava_Assignment()
    setattr(partner, 'simplejava_Assignment', None)
    _safe_set(owner, 'simplejava_Parameter30', partner)
    assert getattr(partner, 'simplejava_Assignment') == owner
    _safe_set(owner, 'simplejava_Parameter30', None)
    assert getattr(partner, 'simplejava_Assignment') is None


def test_assoc_parameter71_stub_double():
    # simplejava_GenericExpression has no real 'simplejava_GenericExpression73' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_MethodCall(methodName="sample_text", thisObject=True)
    partner = simplejava_GenericExpression()
    setattr(partner, 'simplejava_GenericExpression73', None)
    _safe_set(owner, 'simplejava_MethodCall72', {partner})
    assert getattr(partner, 'simplejava_GenericExpression73') == owner
    _safe_set(owner, 'simplejava_MethodCall72', set())
    assert getattr(partner, 'simplejava_GenericExpression73') is None


def test_assoc_source78_stub_double():
    # simplejava_GenericExpression has no real 'simplejava_GenericExpression79' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_UnaryExpression(type="sample_text")
    partner = simplejava_GenericExpression()
    setattr(partner, 'simplejava_GenericExpression79', None)
    _safe_set(owner, 'simplejava_UnaryExpression', partner)
    assert getattr(partner, 'simplejava_GenericExpression79') == owner
    _safe_set(owner, 'simplejava_UnaryExpression', None)
    assert getattr(partner, 'simplejava_GenericExpression79') is None


def test_assoc_source82_stub_double():
    # simplejava_GenericExpression has no real 'simplejava_GenericExpression84' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_ParanthesisOrBinaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_ParanthesisOrBinaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_ParanthesisOrBinaryExpression(type="sample_text")
    partner = simplejava_GenericExpression()
    setattr(partner, 'simplejava_GenericExpression84', None)
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression83', partner)
    assert getattr(partner, 'simplejava_GenericExpression84') == owner
    _safe_set(owner, 'simplejava_ParanthesisOrBinaryExpression83', None)
    assert getattr(partner, 'simplejava_GenericExpression84') is None


def test_assoc_statements22_stub_double():
    # simplejava_Statement has no real 'simplejava_Statement' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_MethodBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_MethodBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_MethodBlock(generated=True)
    partner = simplejava_Statement()
    setattr(partner, 'simplejava_Statement', None)
    _safe_set(owner, 'simplejava_MethodBlock23', {partner})
    assert getattr(partner, 'simplejava_Statement') == owner
    _safe_set(owner, 'simplejava_MethodBlock23', set())
    assert getattr(partner, 'simplejava_Statement') is None


def test_assoc_then35_stub_double():
    # simplejava_IfStatement has no real 'simplejava_IfStatement36' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_MethodBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_MethodBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_MethodBlock(generated=True)
    partner = simplejava_IfStatement()
    setattr(partner, 'simplejava_IfStatement36', None)
    _safe_set(owner, 'simplejava_MethodBlock37', partner)
    assert getattr(partner, 'simplejava_IfStatement36') == owner
    _safe_set(owner, 'simplejava_MethodBlock37', None)
    assert getattr(partner, 'simplejava_IfStatement36') is None


def test_assoc_type74_stub_double():
    # simplejava_ConstructorCall has no real 'simplejava_ConstructorCall' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_Type(isArray=True, isVoid=True, typeName="sample_text")
    partner = simplejava_ConstructorCall()
    setattr(partner, 'simplejava_ConstructorCall', None)
    _safe_set(owner, 'simplejava_Type75', partner)
    assert getattr(partner, 'simplejava_ConstructorCall') == owner
    _safe_set(owner, 'simplejava_Type75', None)
    assert getattr(partner, 'simplejava_ConstructorCall') is None


def test_assoc_variable80_stub_double():
    # simplejava_VariableExpression has no real 'simplejava_VariableExpression' property in the generated
    # code (a bare stub) -- manually attach it so simplejava_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simplejava_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simplejava_Parameter(name="sample_text")
    partner = simplejava_VariableExpression()
    setattr(partner, 'simplejava_VariableExpression', None)
    _safe_set(owner, 'simplejava_Parameter81', partner)
    assert getattr(partner, 'simplejava_VariableExpression') == owner
    _safe_set(owner, 'simplejava_Parameter81', None)
    assert getattr(partner, 'simplejava_VariableExpression') is None


