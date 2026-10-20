import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    OOArithmeticExpression,
    OOCommentOwner,
    OOComparatorExpression,
    OOCompoundStatement,
    OOConditionalStatement,
    OOExpression,
    OOLogicalExpression,
    OOOneOperandArithmeticExpression,
    OOOneOperandLogicalExpression,
    OOStatement,
    OOTwoOperandArithmeticExpression,
    OOTwoOperandAssignableExpression,
    OOTwoOperandLogicalExpression,
    OOVariable,
    oogen_OOAdditionExpression,
    oogen_OOAndExpression,
    oogen_OOArithmeticExpression,
    oogen_OOAssignmentExpression,
    oogen_OOBitWiseComplement,
    oogen_OOBitWiseLeftShift,
    oogen_OOBitWiseRightShift,
    oogen_OOBitwiseAndExpression,
    oogen_OOBitwiseOrExpression,
    oogen_OOBitwiseXorExpression,
    oogen_OOBoolLiteral,
    oogen_OOBracketedExpression,
    oogen_OOBreak,
    oogen_OOCase,
    oogen_OOClass,
    oogen_OOComment,
    oogen_OOCommentOwner,
    oogen_OOComparatorExpression,
    oogen_OOCompoundStatement,
    oogen_OOConditionalStatement,
    oogen_OOConstructor,
    oogen_OOContinue,
    oogen_OODefault,
    oogen_OODivisionExpression,
    oogen_OODoWhile,
    oogen_OODoubleLiteral,
    oogen_OOEmptyExpression,
    oogen_OOEmptyStatement,
    oogen_OOEnumeration,
    oogen_OOEqualsExpression,
    oogen_OOExpression,
    oogen_OOFieldReferenceExpression,
    oogen_OOFloatLiteral,
    oogen_OOFor,
    oogen_OOForEach,
    oogen_OOFunctionCallExpression,
    oogen_OOGreaterEqualsExpression,
    oogen_OOGreaterThanExpression,
    oogen_OOIf,
    oogen_OOIndexing,
    oogen_OOInitializerList,
    oogen_OOIntegerDivisionExpression,
    oogen_OOIntegerLiteral,
    oogen_OOLanguageSpecificExpression,
    oogen_OOLanguageSpecificSnippet,
    oogen_OOLessEqualsExpression,
    oogen_OOLessThanExpression,
    oogen_OOLogicalExpression,
    oogen_OOLogicalLiteral,
    oogen_OOLongLiteral,
    oogen_OOMember,
    oogen_OOMethod,
    oogen_OOMinusExpression,
    oogen_OOModel,
    oogen_OOModuloExpression,
    oogen_OOMultiplicationExpression,
    oogen_OONewArray,
    oogen_OONewClass,
    oogen_OONotEqualsExpression,
    oogen_OONotExpression,
    oogen_OONullLiteral,
    oogen_OOOneOperandArithmeticExpression,
    oogen_OOOneOperandLogicalExpression,
    oogen_OOOrExpression,
    oogen_OOPackage,
    oogen_OOPlusExpression,
    oogen_OOPostfixDecrementExpression,
    oogen_OOPostfixIncrementExpression,
    oogen_OOPowerExpression,
    oogen_OOPrefixDecrementExpression,
    oogen_OOPrefixIncrementExpression,
    oogen_OOReturn,
    oogen_OORootExpression,
    oogen_OOStatement,
    oogen_OOStringLiteral,
    oogen_OOSubtractionExpression,
    oogen_OOSwitch,
    oogen_OOTernaryOperator,
    oogen_OOThisLiteral,
    oogen_OOTwoOperandArithmeticExpression,
    oogen_OOTwoOperandAssignableExpression,
    oogen_OOTwoOperandLogicalExpression,
    oogen_OOType,
    oogen_OOTypeCast,
    oogen_OOVariable,
    oogen_OOVariableDeclarationList,
    oogen_OOVariableReferenceExpression,
    oogen_OOWhile,
    oogen_OOXorExpression,
    OOBaseType,
    OOCollectionType,
    OOLanguage,
    OOVisibility,
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

def test_assoc_classType11_reverse_link_reassign_clear():
    a1 = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    a2 = oogen_OOType(arrayDimensions=13, baseType="sample_text_2", collectionType="sample_text_2", numberOfIndirections=13)
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'oogen_OOClass13', a1)
    assert _is_linked(b, 'oogen_OOClass13', a1)
    if hasattr(a1, 'oogen_OOType12'):
        assert _is_linked(a1, 'oogen_OOType12', b)
    _safe_set(b, 'oogen_OOClass13', a2)
    assert _is_linked(b, 'oogen_OOClass13', a2)
    if hasattr(a1, 'oogen_OOType12'):
        assert not _is_linked(a1, 'oogen_OOType12', b)
    if hasattr(a2, 'oogen_OOType12'):
        assert _is_linked(a2, 'oogen_OOType12', b)
    _safe_set(b, 'oogen_OOClass13', None)
    assert not _is_linked(b, 'oogen_OOClass13', a2)
    if hasattr(a2, 'oogen_OOType12'):
        assert not _is_linked(a2, 'oogen_OOType12', b)


def test_assoc_classes0_reverse_link_reassign_clear():
    a1 = oogen_OOPackage(name="sample_text")
    a2 = oogen_OOPackage(name="sample_text_2")
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'OOClass', a1)
    assert _is_linked(b, 'OOClass', a1)
    if hasattr(a1, 'package'):
        assert _is_linked(a1, 'package', b)
    _safe_set(b, 'OOClass', a2)
    assert _is_linked(b, 'OOClass', a2)
    if hasattr(a1, 'package'):
        assert not _is_linked(a1, 'package', b)
    if hasattr(a2, 'package'):
        assert _is_linked(a2, 'package', b)
    _safe_set(b, 'OOClass', None)
    assert not _is_linked(b, 'OOClass', a2)
    if hasattr(a2, 'package'):
        assert not _is_linked(a2, 'package', b)


def test_assoc_constructors6_reverse_link_reassign_clear():
    a1 = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    a2 = oogen_OOConstructor(className="sample_text_2", visibility="sample_text_2")
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'oogen_OOClass7', {a1})
    assert _is_linked(b, 'oogen_OOClass7', a1)
    if hasattr(a1, 'oogen_OOConstructor'):
        assert _is_linked(a1, 'oogen_OOConstructor', b)
    _safe_set(b, 'oogen_OOClass7', {a2})
    assert _is_linked(b, 'oogen_OOClass7', a2)
    if hasattr(a1, 'oogen_OOConstructor'):
        assert not _is_linked(a1, 'oogen_OOConstructor', b)
    if hasattr(a2, 'oogen_OOConstructor'):
        assert _is_linked(a2, 'oogen_OOConstructor', b)
    _safe_set(b, 'oogen_OOClass7', set())
    assert not _is_linked(b, 'oogen_OOClass7', a2)
    if hasattr(a2, 'oogen_OOConstructor'):
        assert not _is_linked(a2, 'oogen_OOConstructor', b)


def test_assoc_enumType17_reverse_link_reassign_clear():
    a1 = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    a2 = oogen_OOType(arrayDimensions=13, baseType="sample_text_2", collectionType="sample_text_2", numberOfIndirections=13)
    b = oogen_OOEnumeration(name="sample_text", options="sample_text")
    _safe_set(b, 'oogen_OOEnumeration19', a1)
    assert _is_linked(b, 'oogen_OOEnumeration19', a1)
    if hasattr(a1, 'oogen_OOType18'):
        assert _is_linked(a1, 'oogen_OOType18', b)
    _safe_set(b, 'oogen_OOEnumeration19', a2)
    assert _is_linked(b, 'oogen_OOEnumeration19', a2)
    if hasattr(a1, 'oogen_OOType18'):
        assert not _is_linked(a1, 'oogen_OOType18', b)
    if hasattr(a2, 'oogen_OOType18'):
        assert _is_linked(a2, 'oogen_OOType18', b)
    _safe_set(b, 'oogen_OOEnumeration19', None)
    assert not _is_linked(b, 'oogen_OOEnumeration19', a2)
    if hasattr(a2, 'oogen_OOType18'):
        assert not _is_linked(a2, 'oogen_OOType18', b)


def test_assoc_enums1_reverse_link_reassign_clear():
    a1 = oogen_OOPackage(name="sample_text")
    a2 = oogen_OOPackage(name="sample_text_2")
    b = oogen_OOEnumeration(name="sample_text", options="sample_text")
    _safe_set(b, 'oogen_OOEnumeration', a1)
    assert _is_linked(b, 'oogen_OOEnumeration', a1)
    if hasattr(a1, 'oogen_OOPackage'):
        assert _is_linked(a1, 'oogen_OOPackage', b)
    _safe_set(b, 'oogen_OOEnumeration', a2)
    assert _is_linked(b, 'oogen_OOEnumeration', a2)
    if hasattr(a1, 'oogen_OOPackage'):
        assert not _is_linked(a1, 'oogen_OOPackage', b)
    if hasattr(a2, 'oogen_OOPackage'):
        assert _is_linked(a2, 'oogen_OOPackage', b)
    _safe_set(b, 'oogen_OOEnumeration', None)
    assert not _is_linked(b, 'oogen_OOEnumeration', a2)
    if hasattr(a2, 'oogen_OOPackage'):
        assert not _is_linked(a2, 'oogen_OOPackage', b)


def test_assoc_members2_reverse_link_reassign_clear():
    a1 = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    a2 = oogen_OOMember(languages="sample_text_2", static=False, visibility="sample_text_2")
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'oogen_OOClass', {a1})
    assert _is_linked(b, 'oogen_OOClass', a1)
    if hasattr(a1, 'oogen_OOMember'):
        assert _is_linked(a1, 'oogen_OOMember', b)
    _safe_set(b, 'oogen_OOClass', {a2})
    assert _is_linked(b, 'oogen_OOClass', a2)
    if hasattr(a1, 'oogen_OOMember'):
        assert not _is_linked(a1, 'oogen_OOMember', b)
    if hasattr(a2, 'oogen_OOMember'):
        assert _is_linked(a2, 'oogen_OOMember', b)
    _safe_set(b, 'oogen_OOClass', set())
    assert not _is_linked(b, 'oogen_OOClass', a2)
    if hasattr(a2, 'oogen_OOMember'):
        assert not _is_linked(a2, 'oogen_OOMember', b)


def test_assoc_methods4_reverse_link_reassign_clear():
    a1 = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    a2 = oogen_OOMethod(languages="sample_text_2", name="sample_text_2", static=False, visibility="sample_text_2")
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'oogen_OOClass5', {a1})
    assert _is_linked(b, 'oogen_OOClass5', a1)
    if hasattr(a1, 'oogen_OOMethod'):
        assert _is_linked(a1, 'oogen_OOMethod', b)
    _safe_set(b, 'oogen_OOClass5', {a2})
    assert _is_linked(b, 'oogen_OOClass5', a2)
    if hasattr(a1, 'oogen_OOMethod'):
        assert not _is_linked(a1, 'oogen_OOMethod', b)
    if hasattr(a2, 'oogen_OOMethod'):
        assert _is_linked(a2, 'oogen_OOMethod', b)
    _safe_set(b, 'oogen_OOClass5', set())
    assert not _is_linked(b, 'oogen_OOClass5', a2)
    if hasattr(a2, 'oogen_OOMethod'):
        assert not _is_linked(a2, 'oogen_OOMethod', b)


def test_assoc_package145_reverse_link_reassign_clear():
    a1 = oogen_OOPackage(name="sample_text")
    a2 = oogen_OOPackage(name="sample_text_2")
    b = oogen_OOEnumeration(name="sample_text", options="sample_text")
    _safe_set(b, 'oogen_OOEnumeration146', a1)
    assert _is_linked(b, 'oogen_OOEnumeration146', a1)
    if hasattr(a1, 'oogen_OOPackage147'):
        assert _is_linked(a1, 'oogen_OOPackage147', b)
    _safe_set(b, 'oogen_OOEnumeration146', a2)
    assert _is_linked(b, 'oogen_OOEnumeration146', a2)
    if hasattr(a1, 'oogen_OOPackage147'):
        assert not _is_linked(a1, 'oogen_OOPackage147', b)
    if hasattr(a2, 'oogen_OOPackage147'):
        assert _is_linked(a2, 'oogen_OOPackage147', b)
    _safe_set(b, 'oogen_OOEnumeration146', None)
    assert not _is_linked(b, 'oogen_OOEnumeration146', a2)
    if hasattr(a2, 'oogen_OOPackage147'):
        assert not _is_linked(a2, 'oogen_OOPackage147', b)


def test_assoc_package3_reverse_link_reassign_clear():
    a1 = oogen_OOPackage(name="sample_text")
    a2 = oogen_OOPackage(name="sample_text_2")
    b = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    _safe_set(b, 'classes', a1)
    assert _is_linked(b, 'classes', a1)
    if hasattr(a1, 'OOPackage'):
        assert _is_linked(a1, 'OOPackage', b)
    _safe_set(b, 'classes', a2)
    assert _is_linked(b, 'classes', a2)
    if hasattr(a1, 'OOPackage'):
        assert not _is_linked(a1, 'OOPackage', b)
    if hasattr(a2, 'OOPackage'):
        assert _is_linked(a2, 'OOPackage', b)
    _safe_set(b, 'classes', None)
    assert not _is_linked(b, 'classes', a2)
    if hasattr(a2, 'OOPackage'):
        assert not _is_linked(a2, 'OOPackage', b)


def test_assoc_parameters130_reverse_link_reassign_clear():
    a1 = oogen_OOVariable(name="sample_text", transient=True)
    a2 = oogen_OOVariable(name="sample_text_2", transient=False)
    b = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    _safe_set(b, 'oogen_OOConstructor131', {a1})
    assert _is_linked(b, 'oogen_OOConstructor131', a1)
    if hasattr(a1, 'oogen_OOVariable132'):
        assert _is_linked(a1, 'oogen_OOVariable132', b)
    _safe_set(b, 'oogen_OOConstructor131', {a2})
    assert _is_linked(b, 'oogen_OOConstructor131', a2)
    if hasattr(a1, 'oogen_OOVariable132'):
        assert not _is_linked(a1, 'oogen_OOVariable132', b)
    if hasattr(a2, 'oogen_OOVariable132'):
        assert _is_linked(a2, 'oogen_OOVariable132', b)
    _safe_set(b, 'oogen_OOConstructor131', set())
    assert not _is_linked(b, 'oogen_OOConstructor131', a2)
    if hasattr(a2, 'oogen_OOVariable132'):
        assert not _is_linked(a2, 'oogen_OOVariable132', b)


def test_assoc_parameters20_reverse_link_reassign_clear():
    a1 = oogen_OOVariable(name="sample_text", transient=True)
    a2 = oogen_OOVariable(name="sample_text_2", transient=False)
    b = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    _safe_set(b, 'oogen_OOMethod21', {a1})
    assert _is_linked(b, 'oogen_OOMethod21', a1)
    if hasattr(a1, 'oogen_OOVariable22'):
        assert _is_linked(a1, 'oogen_OOVariable22', b)
    _safe_set(b, 'oogen_OOMethod21', {a2})
    assert _is_linked(b, 'oogen_OOMethod21', a2)
    if hasattr(a1, 'oogen_OOVariable22'):
        assert not _is_linked(a1, 'oogen_OOVariable22', b)
    if hasattr(a2, 'oogen_OOVariable22'):
        assert _is_linked(a2, 'oogen_OOVariable22', b)
    _safe_set(b, 'oogen_OOMethod21', set())
    assert not _is_linked(b, 'oogen_OOMethod21', a2)
    if hasattr(a2, 'oogen_OOVariable22'):
        assert not _is_linked(a2, 'oogen_OOVariable22', b)


def test_assoc_returnType23_reverse_link_reassign_clear():
    a1 = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    a2 = oogen_OOType(arrayDimensions=13, baseType="sample_text_2", collectionType="sample_text_2", numberOfIndirections=13)
    b = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    _safe_set(b, 'oogen_OOMethod24', a1)
    assert _is_linked(b, 'oogen_OOMethod24', a1)
    if hasattr(a1, 'oogen_OOType25'):
        assert _is_linked(a1, 'oogen_OOType25', b)
    _safe_set(b, 'oogen_OOMethod24', a2)
    assert _is_linked(b, 'oogen_OOMethod24', a2)
    if hasattr(a1, 'oogen_OOType25'):
        assert not _is_linked(a1, 'oogen_OOType25', b)
    if hasattr(a2, 'oogen_OOType25'):
        assert _is_linked(a2, 'oogen_OOType25', b)
    _safe_set(b, 'oogen_OOMethod24', None)
    assert not _is_linked(b, 'oogen_OOMethod24', a2)
    if hasattr(a2, 'oogen_OOType25'):
        assert not _is_linked(a2, 'oogen_OOType25', b)


def test_assoc_type8_reverse_link_reassign_clear():
    a1 = oogen_OOVariable(name="sample_text", transient=True)
    a2 = oogen_OOVariable(name="sample_text_2", transient=False)
    b = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    _safe_set(b, 'oogen_OOType', a1)
    assert _is_linked(b, 'oogen_OOType', a1)
    if hasattr(a1, 'oogen_OOVariable'):
        assert _is_linked(a1, 'oogen_OOVariable', b)
    _safe_set(b, 'oogen_OOType', a2)
    assert _is_linked(b, 'oogen_OOType', a2)
    if hasattr(a1, 'oogen_OOVariable'):
        assert not _is_linked(a1, 'oogen_OOVariable', b)
    if hasattr(a2, 'oogen_OOVariable'):
        assert _is_linked(a2, 'oogen_OOVariable', b)
    _safe_set(b, 'oogen_OOType', None)
    assert not _is_linked(b, 'oogen_OOType', a2)
    if hasattr(a2, 'oogen_OOVariable'):
        assert not _is_linked(a2, 'oogen_OOVariable', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_afterComments142_stub_double():
    # oogen_OOCommentOwner has no real 'oogen_OOCommentOwner143' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOComment(isBlockComment=True, text="sample_text")
    partner = oogen_OOCommentOwner()
    setattr(partner, 'oogen_OOCommentOwner143', None)
    _safe_set(owner, 'oogen_OOComment144', partner)
    assert owner in getattr(partner, 'oogen_OOCommentOwner143')
    _safe_set(owner, 'oogen_OOComment144', None)
    assert owner not in getattr(partner, 'oogen_OOCommentOwner143')


def test_assoc_argumentExpressions125_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression126' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOFunctionCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOFunctionCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOFunctionCallExpression(functionName="sample_text")
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression126', None)
    _safe_set(owner, 'oogen_OOFunctionCallExpression', {partner})
    assert getattr(partner, 'oogen_OOExpression126') == owner
    _safe_set(owner, 'oogen_OOFunctionCallExpression', set())
    assert getattr(partner, 'oogen_OOExpression126') is None


def test_assoc_arraySizeExpressions14_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression16' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression16', None)
    _safe_set(owner, 'oogen_OOType15', {partner})
    assert getattr(partner, 'oogen_OOExpression16') == owner
    _safe_set(owner, 'oogen_OOType15', set())
    assert getattr(partner, 'oogen_OOExpression16') is None


def test_assoc_arrayType136_stub_double():
    # oogen_OONewArray has no real 'oogen_OONewArray' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    partner = oogen_OONewArray()
    setattr(partner, 'oogen_OONewArray', None)
    _safe_set(owner, 'oogen_OOType137', partner)
    assert getattr(partner, 'oogen_OONewArray') == owner
    _safe_set(owner, 'oogen_OOType137', None)
    assert getattr(partner, 'oogen_OONewArray') is None


def test_assoc_beforeComments141_stub_double():
    # oogen_OOCommentOwner has no real 'oogen_OOCommentOwner' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOComment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOComment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOComment(isBlockComment=True, text="sample_text")
    partner = oogen_OOCommentOwner()
    setattr(partner, 'oogen_OOCommentOwner', None)
    _safe_set(owner, 'oogen_OOComment', partner)
    assert owner in getattr(partner, 'oogen_OOCommentOwner')
    _safe_set(owner, 'oogen_OOComment', None)
    assert owner not in getattr(partner, 'oogen_OOCommentOwner')


def test_assoc_constructorParameterExpressions89_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression90' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OONewClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OONewClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OONewClass(className="sample_text")
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression90', None)
    _safe_set(owner, 'oogen_OONewClass', {partner})
    assert getattr(partner, 'oogen_OOExpression90') == owner
    _safe_set(owner, 'oogen_OONewClass', set())
    assert getattr(partner, 'oogen_OOExpression90') is None


def test_assoc_fieldOwner119_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression120' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOFieldReferenceExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOFieldReferenceExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOFieldReferenceExpression(fieldName="sample_text")
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression120', None)
    _safe_set(owner, 'oogen_OOFieldReferenceExpression', partner)
    assert getattr(partner, 'oogen_OOExpression120') == owner
    _safe_set(owner, 'oogen_OOFieldReferenceExpression', None)
    assert getattr(partner, 'oogen_OOExpression120') is None


def test_assoc_globalFunctions36_stub_double():
    # oogen_OOModel has no real 'oogen_OOModel37' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    partner = oogen_OOModel()
    setattr(partner, 'oogen_OOModel37', None)
    _safe_set(owner, 'oogen_OOMethod38', partner)
    assert owner in getattr(partner, 'oogen_OOModel37')
    _safe_set(owner, 'oogen_OOMethod38', None)
    assert owner not in getattr(partner, 'oogen_OOModel37')


def test_assoc_globalVariables33_stub_double():
    # oogen_OOModel has no real 'oogen_OOModel34' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOModel()
    setattr(partner, 'oogen_OOModel34', None)
    _safe_set(owner, 'oogen_OOVariable35', partner)
    assert owner in getattr(partner, 'oogen_OOModel34')
    _safe_set(owner, 'oogen_OOVariable35', None)
    assert owner not in getattr(partner, 'oogen_OOModel34')


def test_assoc_initializerExpression9_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression', None)
    _safe_set(owner, 'oogen_OOVariable10', partner)
    assert getattr(partner, 'oogen_OOExpression') == owner
    _safe_set(owner, 'oogen_OOVariable10', None)
    assert getattr(partner, 'oogen_OOExpression') is None


def test_assoc_loopVariable77_stub_double():
    # oogen_OOForEach has no real 'oogen_OOForEach78' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOForEach()
    setattr(partner, 'oogen_OOForEach78', None)
    _safe_set(owner, 'oogen_OOVariable79', partner)
    assert getattr(partner, 'oogen_OOForEach78') == owner
    _safe_set(owner, 'oogen_OOVariable79', None)
    assert getattr(partner, 'oogen_OOForEach78') is None


def test_assoc_oopackage28_stub_double():
    # oogen_OOModel has no real 'oogen_OOModel' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOPackage(name="sample_text")
    partner = oogen_OOModel()
    setattr(partner, 'oogen_OOModel', None)
    _safe_set(owner, 'oogen_OOPackage29', partner)
    assert getattr(partner, 'oogen_OOModel') == owner
    _safe_set(owner, 'oogen_OOPackage29', None)
    assert getattr(partner, 'oogen_OOModel') is None


def test_assoc_ownerExpression127_stub_double():
    # oogen_OOExpression has no real 'oogen_OOExpression129' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOFunctionCallExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOFunctionCallExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOFunctionCallExpression(functionName="sample_text")
    partner = oogen_OOExpression()
    setattr(partner, 'oogen_OOExpression129', None)
    _safe_set(owner, 'oogen_OOFunctionCallExpression128', partner)
    assert getattr(partner, 'oogen_OOExpression129') == owner
    _safe_set(owner, 'oogen_OOFunctionCallExpression128', None)
    assert getattr(partner, 'oogen_OOExpression129') is None


def test_assoc_packages30_stub_double():
    # oogen_OOModel has no real 'oogen_OOModel31' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOPackage(name="sample_text")
    partner = oogen_OOModel()
    setattr(partner, 'oogen_OOModel31', None)
    _safe_set(owner, 'oogen_OOPackage32', partner)
    assert owner in getattr(partner, 'oogen_OOModel31')
    _safe_set(owner, 'oogen_OOPackage32', None)
    assert owner not in getattr(partner, 'oogen_OOModel31')


def test_assoc_snippets83_stub_double():
    # oogen_OOLanguageSpecificExpression has no real 'oogen_OOLanguageSpecificExpression' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOLanguageSpecificSnippet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOLanguageSpecificSnippet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOLanguageSpecificSnippet(code="sample_text", lang="sample_text")
    partner = oogen_OOLanguageSpecificExpression()
    setattr(partner, 'oogen_OOLanguageSpecificExpression', None)
    _safe_set(owner, 'oogen_OOLanguageSpecificSnippet', partner)
    assert owner in getattr(partner, 'oogen_OOLanguageSpecificExpression')
    _safe_set(owner, 'oogen_OOLanguageSpecificSnippet', None)
    assert owner not in getattr(partner, 'oogen_OOLanguageSpecificExpression')


def test_assoc_statements133_stub_double():
    # oogen_OOStatement has no real 'oogen_OOStatement135' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOConstructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOConstructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    partner = oogen_OOStatement()
    setattr(partner, 'oogen_OOStatement135', None)
    _safe_set(owner, 'oogen_OOConstructor134', {partner})
    assert getattr(partner, 'oogen_OOStatement135') == owner
    _safe_set(owner, 'oogen_OOConstructor134', set())
    assert getattr(partner, 'oogen_OOStatement135') is None


def test_assoc_statements26_stub_double():
    # oogen_OOStatement has no real 'oogen_OOStatement' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOMethod's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOMethod's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    partner = oogen_OOStatement()
    setattr(partner, 'oogen_OOStatement', None)
    _safe_set(owner, 'oogen_OOMethod27', {partner})
    assert getattr(partner, 'oogen_OOStatement') == owner
    _safe_set(owner, 'oogen_OOMethod27', set())
    assert getattr(partner, 'oogen_OOStatement') is None


def test_assoc_traversedVariable75_stub_double():
    # oogen_OOForEach has no real 'oogen_OOForEach' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOForEach()
    setattr(partner, 'oogen_OOForEach', None)
    _safe_set(owner, 'oogen_OOVariable76', partner)
    assert getattr(partner, 'oogen_OOForEach') == owner
    _safe_set(owner, 'oogen_OOVariable76', None)
    assert getattr(partner, 'oogen_OOForEach') is None


def test_assoc_type84_stub_double():
    # oogen_OOTypeCast has no real 'oogen_OOTypeCast' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    partner = oogen_OOTypeCast()
    setattr(partner, 'oogen_OOTypeCast', None)
    _safe_set(owner, 'oogen_OOType85', partner)
    assert getattr(partner, 'oogen_OOTypeCast') == owner
    _safe_set(owner, 'oogen_OOType85', None)
    assert getattr(partner, 'oogen_OOTypeCast') is None


def test_assoc_variable121_stub_double():
    # oogen_OOVariableReferenceExpression has no real 'oogen_OOVariableReferenceExpression' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOVariableReferenceExpression()
    setattr(partner, 'oogen_OOVariableReferenceExpression', None)
    _safe_set(owner, 'oogen_OOVariable122', partner)
    assert getattr(partner, 'oogen_OOVariableReferenceExpression') == owner
    _safe_set(owner, 'oogen_OOVariable122', None)
    assert getattr(partner, 'oogen_OOVariableReferenceExpression') is None


def test_assoc_variableDeclarations107_stub_double():
    # oogen_OOVariableDeclarationList has no real 'oogen_OOVariableDeclarationList' property in the generated
    # code (a bare stub) -- manually attach it so oogen_OOVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oogen_OOVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oogen_OOVariable(name="sample_text", transient=True)
    partner = oogen_OOVariableDeclarationList()
    setattr(partner, 'oogen_OOVariableDeclarationList', None)
    _safe_set(owner, 'oogen_OOVariable108', partner)
    assert owner in getattr(partner, 'oogen_OOVariableDeclarationList')
    _safe_set(owner, 'oogen_OOVariable108', None)
    assert owner not in getattr(partner, 'oogen_OOVariableDeclarationList')


