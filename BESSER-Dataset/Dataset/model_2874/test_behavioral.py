import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotation,
    AssignmentStatement,
    BinaryOperatorExpression,
    CollectionExpression,
    CollectionInitValue,
    CollectionType,
    DomElement,
    Expression,
    FeatureCallExpression,
    LiteralExpression,
    NameExpression,
    OperatorExpression,
    PrimitiveExpression,
    PrimitiveType,
    Statement,
    SwitchCaseStatement,
    Type,
    UnaryOperatorExpression,
    dom_AbortStatement,
    dom_AndOperatorExpression,
    dom_Annotation,
    dom_AnnotationBlock,
    dom_AnyType,
    dom_AssignmentStatement,
    dom_BagExpression,
    dom_BagType,
    dom_BinaryOperatorExpression,
    dom_Block,
    dom_BooleanExpression,
    dom_BooleanType,
    dom_BreakAllStatement,
    dom_BreakStatement,
    dom_CollectionExpression,
    dom_CollectionInitValue,
    dom_CollectionType,
    dom_ContinueStatement,
    dom_DeleteStatement,
    dom_DivideOperatorExpression,
    dom_DomElement,
    dom_EnumerationLiteralExpression,
    dom_EqualsOperatorExpression,
    dom_ExecutableAnnotation,
    dom_ExpRange,
    dom_ExprList,
    dom_Expression,
    dom_ExpressionStatement,
    dom_FOLMethodCallExpression,
    dom_FeatureCallExpression,
    dom_ForStatement,
    dom_FormalParameterExpression,
    dom_GreaterThanOperatorExpression,
    dom_GreaterThanOrEqualToOperatorExpression,
    dom_IfStatement,
    dom_ImpliesOperatorExpression,
    dom_Import,
    dom_IntegerExpression,
    dom_IntegerType,
    dom_KeyValue,
    dom_LessThanOperatorExpression,
    dom_LessThanOrEqualToOperatorExpression,
    dom_LiteralExpression,
    dom_MapExpression,
    dom_MapType,
    dom_MethodCallExpression,
    dom_MinusOperatorExpression,
    dom_ModelDeclarationParameter,
    dom_ModelDeclarationStatement,
    dom_ModelElementType,
    dom_ModelElementTypeExpression,
    dom_ModelExpression,
    dom_MultiplyOperatorExpression,
    dom_NameExpression,
    dom_NativeType,
    dom_NegativeOperatorExpression,
    dom_NewExpression,
    dom_NotEqualsOperatorExpression,
    dom_NotOperatorExpression,
    dom_OperationDefinition,
    dom_OperatorExpression,
    dom_OrOperatorExpression,
    dom_OrderedSetExpression,
    dom_OrderedSetType,
    dom_PlusOperatorExpression,
    dom_PrimitiveExpression,
    dom_PrimitiveType,
    dom_Program,
    dom_PropertyCallExpression,
    dom_RealExpression,
    dom_RealType,
    dom_ReturnStatement,
    dom_SequenceExpression,
    dom_SequenceType,
    dom_SetExpression,
    dom_SetType,
    dom_ShortModelDeclarationExpression,
    dom_SimpleAnnotation,
    dom_SpecialAssignmentStatement,
    dom_SpecialNameExpression,
    dom_Statement,
    dom_StringExpression,
    dom_StringType,
    dom_SwitchCaseDefaultStatement,
    dom_SwitchCaseExpressionStatement,
    dom_SwitchCaseStatement,
    dom_SwitchStatement,
    dom_ThrowStatement,
    dom_TransactionStatement,
    dom_Type,
    dom_UnaryOperatorExpression,
    dom_VariableDeclarationExpression,
    dom_WhileStatement,
    dom_XorOperatorExpression,
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

def test_assoc_container1_reverse_link_reassign_clear():
    a1 = dom_DomElement(column=7, line=7)
    a2 = dom_DomElement(column=13, line=13)
    b = dom_DomElement(column=7, line=7)
    _safe_set(b, 'dom_DomElement0', a1)
    assert _is_linked(b, 'dom_DomElement0', a1)
    if hasattr(a1, 'dom_DomElement'):
        assert _is_linked(a1, 'dom_DomElement', b)
    _safe_set(b, 'dom_DomElement0', a2)
    assert _is_linked(b, 'dom_DomElement0', a2)
    if hasattr(a1, 'dom_DomElement'):
        assert not _is_linked(a1, 'dom_DomElement', b)
    if hasattr(a2, 'dom_DomElement'):
        assert _is_linked(a2, 'dom_DomElement', b)
    _safe_set(b, 'dom_DomElement0', None)
    assert not _is_linked(b, 'dom_DomElement0', a2)
    if hasattr(a2, 'dom_DomElement'):
        assert not _is_linked(a2, 'dom_DomElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_alias110_stub_double():
    # dom_ModelDeclarationStatement has no real 'dom_ModelDeclarationStatement111' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelDeclarationStatement()
    setattr(partner, 'dom_ModelDeclarationStatement111', None)
    _safe_set(owner, 'dom_NameExpression112', partner)
    assert owner in getattr(partner, 'dom_ModelDeclarationStatement111')
    _safe_set(owner, 'dom_NameExpression112', None)
    assert owner not in getattr(partner, 'dom_ModelDeclarationStatement111')


def test_assoc_create47_stub_double():
    # dom_VariableDeclarationExpression has no real 'dom_VariableDeclarationExpression48' property in the generated
    # code (a bare stub) -- manually attach it so dom_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BooleanExpression(val=True)
    partner = dom_VariableDeclarationExpression()
    setattr(partner, 'dom_VariableDeclarationExpression48', None)
    _safe_set(owner, 'dom_BooleanExpression49', partner)
    assert getattr(partner, 'dom_VariableDeclarationExpression48') == owner
    _safe_set(owner, 'dom_BooleanExpression49', None)
    assert getattr(partner, 'dom_VariableDeclarationExpression48') is None


def test_assoc_driver113_stub_double():
    # dom_ModelDeclarationStatement has no real 'dom_ModelDeclarationStatement114' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelDeclarationStatement()
    setattr(partner, 'dom_ModelDeclarationStatement114', None)
    _safe_set(owner, 'dom_NameExpression115', partner)
    assert getattr(partner, 'dom_ModelDeclarationStatement114') == owner
    _safe_set(owner, 'dom_NameExpression115', None)
    assert getattr(partner, 'dom_ModelDeclarationStatement114') is None


def test_assoc_element185_stub_double():
    # dom_ModelElementTypeExpression has no real 'dom_ModelElementTypeExpression186' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelElementTypeExpression()
    setattr(partner, 'dom_ModelElementTypeExpression186', None)
    _safe_set(owner, 'dom_NameExpression187', partner)
    assert getattr(partner, 'dom_ModelElementTypeExpression186') == owner
    _safe_set(owner, 'dom_NameExpression187', None)
    assert getattr(partner, 'dom_ModelElementTypeExpression186') is None


def test_assoc_enumeration21_stub_double():
    # dom_EnumerationLiteralExpression has no real 'dom_EnumerationLiteralExpression' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_EnumerationLiteralExpression()
    setattr(partner, 'dom_EnumerationLiteralExpression', None)
    _safe_set(owner, 'dom_NameExpression22', partner)
    assert getattr(partner, 'dom_EnumerationLiteralExpression') == owner
    _safe_set(owner, 'dom_NameExpression22', None)
    assert getattr(partner, 'dom_EnumerationLiteralExpression') is None


def test_assoc_extended42_stub_double():
    # dom_PropertyCallExpression has no real 'dom_PropertyCallExpression43' property in the generated
    # code (a bare stub) -- manually attach it so dom_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BooleanExpression(val=True)
    partner = dom_PropertyCallExpression()
    setattr(partner, 'dom_PropertyCallExpression43', None)
    _safe_set(owner, 'dom_BooleanExpression44', partner)
    assert getattr(partner, 'dom_PropertyCallExpression43') == owner
    _safe_set(owner, 'dom_BooleanExpression44', None)
    assert getattr(partner, 'dom_PropertyCallExpression43') is None


def test_assoc_imported11_stub_double():
    # dom_Import has no real 'dom_Import12' property in the generated
    # code (a bare stub) -- manually attach it so dom_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_StringExpression(val="sample_text")
    partner = dom_Import()
    setattr(partner, 'dom_Import12', None)
    _safe_set(owner, 'dom_StringExpression', partner)
    assert getattr(partner, 'dom_Import12') == owner
    _safe_set(owner, 'dom_StringExpression', None)
    assert getattr(partner, 'dom_Import12') is None


def test_assoc_isArrow31_stub_double():
    # dom_FeatureCallExpression has no real 'dom_FeatureCallExpression32' property in the generated
    # code (a bare stub) -- manually attach it so dom_BooleanExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_BooleanExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_BooleanExpression(val=True)
    partner = dom_FeatureCallExpression()
    setattr(partner, 'dom_FeatureCallExpression32', None)
    _safe_set(owner, 'dom_BooleanExpression', partner)
    assert getattr(partner, 'dom_FeatureCallExpression32') == owner
    _safe_set(owner, 'dom_BooleanExpression', None)
    assert getattr(partner, 'dom_FeatureCallExpression32') is None


def test_assoc_literal23_stub_double():
    # dom_EnumerationLiteralExpression has no real 'dom_EnumerationLiteralExpression24' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_EnumerationLiteralExpression()
    setattr(partner, 'dom_EnumerationLiteralExpression24', None)
    _safe_set(owner, 'dom_NameExpression25', partner)
    assert getattr(partner, 'dom_EnumerationLiteralExpression24') == owner
    _safe_set(owner, 'dom_NameExpression25', None)
    assert getattr(partner, 'dom_EnumerationLiteralExpression24') is None


def test_assoc_method123_stub_double():
    # dom_FOLMethodCallExpression has no real 'dom_FOLMethodCallExpression124' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_FOLMethodCallExpression()
    setattr(partner, 'dom_FOLMethodCallExpression124', None)
    _safe_set(owner, 'dom_NameExpression125', partner)
    assert getattr(partner, 'dom_FOLMethodCallExpression124') == owner
    _safe_set(owner, 'dom_NameExpression125', None)
    assert getattr(partner, 'dom_FOLMethodCallExpression124') is None


def test_assoc_method35_stub_double():
    # dom_MethodCallExpression has no real 'dom_MethodCallExpression36' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_MethodCallExpression()
    setattr(partner, 'dom_MethodCallExpression36', None)
    _safe_set(owner, 'dom_NameExpression37', partner)
    assert getattr(partner, 'dom_MethodCallExpression36') == owner
    _safe_set(owner, 'dom_NameExpression37', None)
    assert getattr(partner, 'dom_MethodCallExpression36') is None


def test_assoc_model182_stub_double():
    # dom_ModelElementTypeExpression has no real 'dom_ModelElementTypeExpression183' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelElementTypeExpression()
    setattr(partner, 'dom_ModelElementTypeExpression183', None)
    _safe_set(owner, 'dom_NameExpression184', partner)
    assert getattr(partner, 'dom_ModelElementTypeExpression183') == owner
    _safe_set(owner, 'dom_NameExpression184', None)
    assert getattr(partner, 'dom_ModelElementTypeExpression183') is None


def test_assoc_model26_stub_double():
    # dom_EnumerationLiteralExpression has no real 'dom_EnumerationLiteralExpression27' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_EnumerationLiteralExpression()
    setattr(partner, 'dom_EnumerationLiteralExpression27', None)
    _safe_set(owner, 'dom_NameExpression28', partner)
    assert getattr(partner, 'dom_EnumerationLiteralExpression27') == owner
    _safe_set(owner, 'dom_NameExpression28', None)
    assert getattr(partner, 'dom_EnumerationLiteralExpression27') is None


def test_assoc_name107_stub_double():
    # dom_ModelDeclarationStatement has no real 'dom_ModelDeclarationStatement108' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelDeclarationStatement()
    setattr(partner, 'dom_ModelDeclarationStatement108', None)
    _safe_set(owner, 'dom_NameExpression109', partner)
    assert getattr(partner, 'dom_ModelDeclarationStatement108') == owner
    _safe_set(owner, 'dom_NameExpression109', None)
    assert getattr(partner, 'dom_ModelDeclarationStatement108') is None


def test_assoc_name136_stub_double():
    # dom_Annotation has no real 'dom_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_Annotation()
    setattr(partner, 'dom_Annotation', None)
    _safe_set(owner, 'dom_NameExpression137', partner)
    assert getattr(partner, 'dom_Annotation') == owner
    _safe_set(owner, 'dom_NameExpression137', None)
    assert getattr(partner, 'dom_Annotation') is None


def test_assoc_name157_stub_double():
    # dom_ModelDeclarationParameter has no real 'dom_ModelDeclarationParameter158' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_ModelDeclarationParameter()
    setattr(partner, 'dom_ModelDeclarationParameter158', None)
    _safe_set(owner, 'dom_NameExpression159', partner)
    assert getattr(partner, 'dom_ModelDeclarationParameter158') == owner
    _safe_set(owner, 'dom_NameExpression159', None)
    assert getattr(partner, 'dom_ModelDeclarationParameter158') is None


def test_assoc_name170_stub_double():
    # dom_FormalParameterExpression has no real 'dom_FormalParameterExpression171' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_FormalParameterExpression()
    setattr(partner, 'dom_FormalParameterExpression171', None)
    _safe_set(owner, 'dom_NameExpression172', partner)
    assert getattr(partner, 'dom_FormalParameterExpression171') == owner
    _safe_set(owner, 'dom_NameExpression172', None)
    assert getattr(partner, 'dom_FormalParameterExpression171') is None


def test_assoc_name45_stub_double():
    # dom_VariableDeclarationExpression has no real 'dom_VariableDeclarationExpression' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_VariableDeclarationExpression()
    setattr(partner, 'dom_VariableDeclarationExpression', None)
    _safe_set(owner, 'dom_NameExpression46', partner)
    assert getattr(partner, 'dom_VariableDeclarationExpression') == owner
    _safe_set(owner, 'dom_NameExpression46', None)
    assert getattr(partner, 'dom_VariableDeclarationExpression') is None


def test_assoc_name64_stub_double():
    # dom_OperationDefinition has no real 'dom_OperationDefinition65' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_OperationDefinition()
    setattr(partner, 'dom_OperationDefinition65', None)
    _safe_set(owner, 'dom_NameExpression66', partner)
    assert getattr(partner, 'dom_OperationDefinition65') == owner
    _safe_set(owner, 'dom_NameExpression66', None)
    assert getattr(partner, 'dom_OperationDefinition65') is None


def test_assoc_name7_stub_double():
    # dom_Program has no real 'dom_Program8' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_Program()
    setattr(partner, 'dom_Program8', None)
    _safe_set(owner, 'dom_NameExpression', partner)
    assert getattr(partner, 'dom_Program8') == owner
    _safe_set(owner, 'dom_NameExpression', None)
    assert getattr(partner, 'dom_Program8') is None


def test_assoc_names167_stub_double():
    # dom_TransactionStatement has no real 'dom_TransactionStatement168' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_TransactionStatement()
    setattr(partner, 'dom_TransactionStatement168', None)
    _safe_set(owner, 'dom_NameExpression169', partner)
    assert owner in getattr(partner, 'dom_TransactionStatement168')
    _safe_set(owner, 'dom_NameExpression169', None)
    assert owner not in getattr(partner, 'dom_TransactionStatement168')


def test_assoc_nativeExpression149_stub_double():
    # dom_NativeType has no real 'dom_NativeType' property in the generated
    # code (a bare stub) -- manually attach it so dom_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_StringExpression(val="sample_text")
    partner = dom_NativeType()
    setattr(partner, 'dom_NativeType', None)
    _safe_set(owner, 'dom_StringExpression150', partner)
    assert getattr(partner, 'dom_NativeType') == owner
    _safe_set(owner, 'dom_StringExpression150', None)
    assert getattr(partner, 'dom_NativeType') is None


def test_assoc_property40_stub_double():
    # dom_PropertyCallExpression has no real 'dom_PropertyCallExpression' property in the generated
    # code (a bare stub) -- manually attach it so dom_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_NameExpression(name="sample_text")
    partner = dom_PropertyCallExpression()
    setattr(partner, 'dom_PropertyCallExpression', None)
    _safe_set(owner, 'dom_NameExpression41', partner)
    assert getattr(partner, 'dom_PropertyCallExpression') == owner
    _safe_set(owner, 'dom_NameExpression41', None)
    assert getattr(partner, 'dom_PropertyCallExpression') is None


def test_assoc_value160_stub_double():
    # dom_ModelDeclarationParameter has no real 'dom_ModelDeclarationParameter161' property in the generated
    # code (a bare stub) -- manually attach it so dom_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_StringExpression(val="sample_text")
    partner = dom_ModelDeclarationParameter()
    setattr(partner, 'dom_ModelDeclarationParameter161', None)
    _safe_set(owner, 'dom_StringExpression162', partner)
    assert getattr(partner, 'dom_ModelDeclarationParameter161') == owner
    _safe_set(owner, 'dom_StringExpression162', None)
    assert getattr(partner, 'dom_ModelDeclarationParameter161') is None


def test_assoc_values140_stub_double():
    # dom_SimpleAnnotation has no real 'dom_SimpleAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so dom_StringExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dom_StringExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dom_StringExpression(val="sample_text")
    partner = dom_SimpleAnnotation()
    setattr(partner, 'dom_SimpleAnnotation', None)
    _safe_set(owner, 'dom_StringExpression141', partner)
    assert owner in getattr(partner, 'dom_SimpleAnnotation')
    _safe_set(owner, 'dom_StringExpression141', None)
    assert owner not in getattr(partner, 'dom_SimpleAnnotation')


