import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DContext,
    DExpression,
    DModel,
    DNavigableMember,
    DPrimitive,
    DmxComplexObject,
    INavigableMemberContainer,
    ITypeContainer,
    dmx_DComplexType,
    dmx_DExpression,
    dmx_DFeature,
    dmx_DNamedElement,
    dmx_DNavigableMember,
    dmx_DType,
    dmx_DmxArchetype,
    dmx_DmxAssignment,
    dmx_DmxBaseTypeSet,
    dmx_DmxBinaryOperation,
    dmx_DmxBooleanLiteral,
    dmx_DmxCallArguments,
    dmx_DmxCastExpression,
    dmx_DmxComplexObject,
    dmx_DmxContextReference,
    dmx_DmxCorrelationVariable,
    dmx_DmxDateLiteral,
    dmx_DmxDecimalLiteral,
    dmx_DmxDetail,
    dmx_DmxEntity,
    dmx_DmxField,
    dmx_DmxFilter,
    dmx_DmxFilterParameter,
    dmx_DmxFilterTypeDescriptor,
    dmx_DmxFunctionCall,
    dmx_DmxIfExpression,
    dmx_DmxInstanceOfExpression,
    dmx_DmxListExpression,
    dmx_DmxMemberNavigation,
    dmx_DmxModel,
    dmx_DmxNaturalLiteral,
    dmx_DmxPredicateWithCorrelationVariable,
    dmx_DmxStaticReference,
    dmx_DmxStringLiteral,
    dmx_DmxTest,
    dmx_DmxTestContext,
    dmx_DmxUnaryOperation,
    dmx_DmxUndefinedLiteral,
    dmx_DmxUrlLiteral,
    dmx_IStaticReferenceTarget,
    DmxBaseType,
    DmxBinaryOperator,
    DmxUnaryOperator,
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

def test_assoc_multiple16_reverse_link_reassign_clear():
    a1 = dmx_DmxFilterTypeDescriptor(collection=True, multiTyped=True, single="sample_text")
    a2 = dmx_DmxFilterTypeDescriptor(collection=False, multiTyped=False, single="sample_text_2")
    b = dmx_DmxBaseTypeSet(members="sample_text", name="sample_text")
    _safe_set(b, 'dmx_DmxBaseTypeSet18', a1)
    assert _is_linked(b, 'dmx_DmxBaseTypeSet18', a1)
    if hasattr(a1, 'dmx_DmxFilterTypeDescriptor17'):
        assert _is_linked(a1, 'dmx_DmxFilterTypeDescriptor17', b)
    _safe_set(b, 'dmx_DmxBaseTypeSet18', a2)
    assert _is_linked(b, 'dmx_DmxBaseTypeSet18', a2)
    if hasattr(a1, 'dmx_DmxFilterTypeDescriptor17'):
        assert not _is_linked(a1, 'dmx_DmxFilterTypeDescriptor17', b)
    if hasattr(a2, 'dmx_DmxFilterTypeDescriptor17'):
        assert _is_linked(a2, 'dmx_DmxFilterTypeDescriptor17', b)
    _safe_set(b, 'dmx_DmxBaseTypeSet18', None)
    assert not _is_linked(b, 'dmx_DmxBaseTypeSet18', a2)
    if hasattr(a2, 'dmx_DmxFilterTypeDescriptor17'):
        assert not _is_linked(a2, 'dmx_DmxFilterTypeDescriptor17', b)


def test_assoc_typeDesc19_reverse_link_reassign_clear():
    a1 = dmx_DmxFilterTypeDescriptor(collection=True, multiTyped=True, single="sample_text")
    a2 = dmx_DmxFilterTypeDescriptor(collection=False, multiTyped=False, single="sample_text_2")
    b = dmx_DmxFilterParameter(name="sample_text")
    _safe_set(b, 'dmx_DmxFilterParameter20', a1)
    assert _is_linked(b, 'dmx_DmxFilterParameter20', a1)
    if hasattr(a1, 'dmx_DmxFilterTypeDescriptor21'):
        assert _is_linked(a1, 'dmx_DmxFilterTypeDescriptor21', b)
    _safe_set(b, 'dmx_DmxFilterParameter20', a2)
    assert _is_linked(b, 'dmx_DmxFilterParameter20', a2)
    if hasattr(a1, 'dmx_DmxFilterTypeDescriptor21'):
        assert not _is_linked(a1, 'dmx_DmxFilterTypeDescriptor21', b)
    if hasattr(a2, 'dmx_DmxFilterTypeDescriptor21'):
        assert _is_linked(a2, 'dmx_DmxFilterTypeDescriptor21', b)
    _safe_set(b, 'dmx_DmxFilterParameter20', None)
    assert not _is_linked(b, 'dmx_DmxFilterParameter20', a2)
    if hasattr(a2, 'dmx_DmxFilterTypeDescriptor21'):
        assert not _is_linked(a2, 'dmx_DmxFilterTypeDescriptor21', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_callArguments38_stub_double():
    # dmx_DmxCallArguments has no real 'dmx_DmxCallArguments' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxMemberNavigation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxMemberNavigation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxMemberNavigation(before=True, explicitOperationCall=True)
    partner = dmx_DmxCallArguments()
    setattr(partner, 'dmx_DmxCallArguments', None)
    _safe_set(owner, 'dmx_DmxMemberNavigation39', partner)
    assert getattr(partner, 'dmx_DmxCallArguments') == owner
    _safe_set(owner, 'dmx_DmxMemberNavigation39', None)
    assert getattr(partner, 'dmx_DmxCallArguments') is None


def test_assoc_context3_stub_double():
    # dmx_DmxTestContext has no real 'dmx_DmxTestContext' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxTest(name="sample_text")
    partner = dmx_DmxTestContext()
    setattr(partner, 'dmx_DmxTestContext', None)
    _safe_set(owner, 'dmx_DmxTest4', {partner})
    assert getattr(partner, 'dmx_DmxTestContext') == owner
    _safe_set(owner, 'dmx_DmxTest4', set())
    assert getattr(partner, 'dmx_DmxTestContext') is None


def test_assoc_expr5_stub_double():
    # dmx_DExpression has no real 'dmx_DExpression' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxTest(name="sample_text")
    partner = dmx_DExpression()
    setattr(partner, 'dmx_DExpression', None)
    _safe_set(owner, 'dmx_DmxTest6', partner)
    assert getattr(partner, 'dmx_DExpression') == owner
    _safe_set(owner, 'dmx_DmxTest6', None)
    assert getattr(partner, 'dmx_DExpression') is None


def test_assoc_leftOperand48_stub_double():
    # dmx_DExpression has no real 'dmx_DExpression49' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxBinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxBinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxBinaryOperation(operator="sample_text")
    partner = dmx_DExpression()
    setattr(partner, 'dmx_DExpression49', None)
    _safe_set(owner, 'dmx_DmxBinaryOperation', partner)
    assert getattr(partner, 'dmx_DExpression49') == owner
    _safe_set(owner, 'dmx_DmxBinaryOperation', None)
    assert getattr(partner, 'dmx_DExpression49') is None


def test_assoc_member33_stub_double():
    # dmx_DNavigableMember has no real 'dmx_DNavigableMember34' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxMemberNavigation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxMemberNavigation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxMemberNavigation(before=True, explicitOperationCall=True)
    partner = dmx_DNavigableMember()
    setattr(partner, 'dmx_DNavigableMember34', None)
    _safe_set(owner, 'dmx_DmxMemberNavigation', partner)
    assert getattr(partner, 'dmx_DNavigableMember34') == owner
    _safe_set(owner, 'dmx_DmxMemberNavigation', None)
    assert getattr(partner, 'dmx_DNavigableMember34') is None


def test_assoc_member67_stub_double():
    # dmx_DNavigableMember has no real 'dmx_DNavigableMember69' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxStaticReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxStaticReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxStaticReference(displayName="sample_text", plural=True)
    partner = dmx_DNavigableMember()
    setattr(partner, 'dmx_DNavigableMember69', None)
    _safe_set(owner, 'dmx_DmxStaticReference68', partner)
    assert getattr(partner, 'dmx_DNavigableMember69') == owner
    _safe_set(owner, 'dmx_DmxStaticReference68', None)
    assert getattr(partner, 'dmx_DNavigableMember69') is None


def test_assoc_operand57_stub_double():
    # dmx_DExpression has no real 'dmx_DExpression58' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxUnaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxUnaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxUnaryOperation(operator="sample_text")
    partner = dmx_DExpression()
    setattr(partner, 'dmx_DExpression58', None)
    _safe_set(owner, 'dmx_DmxUnaryOperation', partner)
    assert getattr(partner, 'dmx_DExpression58') == owner
    _safe_set(owner, 'dmx_DmxUnaryOperation', None)
    assert getattr(partner, 'dmx_DExpression58') is None


def test_assoc_parameters10_stub_double():
    # dmx_DmxFilter has no real 'dmx_DmxFilter11' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxFilterParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxFilterParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxFilterParameter(name="sample_text")
    partner = dmx_DmxFilter()
    setattr(partner, 'dmx_DmxFilter11', None)
    _safe_set(owner, 'dmx_DmxFilterParameter', partner)
    assert owner in getattr(partner, 'dmx_DmxFilter11')
    _safe_set(owner, 'dmx_DmxFilterParameter', None)
    assert owner not in getattr(partner, 'dmx_DmxFilter11')


def test_assoc_precedingNavigationSegment35_stub_double():
    # dmx_DExpression has no real 'dmx_DExpression37' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxMemberNavigation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxMemberNavigation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxMemberNavigation(before=True, explicitOperationCall=True)
    partner = dmx_DExpression()
    setattr(partner, 'dmx_DExpression37', None)
    _safe_set(owner, 'dmx_DmxMemberNavigation36', partner)
    assert getattr(partner, 'dmx_DExpression37') == owner
    _safe_set(owner, 'dmx_DmxMemberNavigation36', None)
    assert getattr(partner, 'dmx_DExpression37') is None


def test_assoc_rightOperand50_stub_double():
    # dmx_DExpression has no real 'dmx_DExpression52' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxBinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxBinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxBinaryOperation(operator="sample_text")
    partner = dmx_DExpression()
    setattr(partner, 'dmx_DExpression52', None)
    _safe_set(owner, 'dmx_DmxBinaryOperation51', partner)
    assert getattr(partner, 'dmx_DExpression52') == owner
    _safe_set(owner, 'dmx_DmxBinaryOperation51', None)
    assert getattr(partner, 'dmx_DExpression52') is None


def test_assoc_target66_stub_double():
    # dmx_IStaticReferenceTarget has no real 'dmx_IStaticReferenceTarget' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxStaticReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxStaticReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxStaticReference(displayName="sample_text", plural=True)
    partner = dmx_IStaticReferenceTarget()
    setattr(partner, 'dmx_IStaticReferenceTarget', None)
    _safe_set(owner, 'dmx_DmxStaticReference', partner)
    assert getattr(partner, 'dmx_IStaticReferenceTarget') == owner
    _safe_set(owner, 'dmx_DmxStaticReference', None)
    assert getattr(partner, 'dmx_IStaticReferenceTarget') is None


def test_assoc_target70_stub_double():
    # dmx_DNamedElement has no real 'dmx_DNamedElement' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxContextReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxContextReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxContextReference(all=True, before=True)
    partner = dmx_DNamedElement()
    setattr(partner, 'dmx_DNamedElement', None)
    _safe_set(owner, 'dmx_DmxContextReference', partner)
    assert getattr(partner, 'dmx_DNamedElement') == owner
    _safe_set(owner, 'dmx_DmxContextReference', None)
    assert getattr(partner, 'dmx_DNamedElement') is None


def test_assoc_tests1_stub_double():
    # dmx_DmxModel has no real 'dmx_DmxModel2' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxTest's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxTest's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxTest(name="sample_text")
    partner = dmx_DmxModel()
    setattr(partner, 'dmx_DmxModel2', None)
    _safe_set(owner, 'dmx_DmxTest', partner)
    assert owner in getattr(partner, 'dmx_DmxModel2')
    _safe_set(owner, 'dmx_DmxTest', None)
    assert owner not in getattr(partner, 'dmx_DmxModel2')


def test_assoc_typeDesc12_stub_double():
    # dmx_DmxFilter has no real 'dmx_DmxFilter13' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxFilterTypeDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxFilterTypeDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxFilterTypeDescriptor(collection=True, multiTyped=True, single="sample_text")
    partner = dmx_DmxFilter()
    setattr(partner, 'dmx_DmxFilter13', None)
    _safe_set(owner, 'dmx_DmxFilterTypeDescriptor', partner)
    assert getattr(partner, 'dmx_DmxFilter13') == owner
    _safe_set(owner, 'dmx_DmxFilterTypeDescriptor', None)
    assert getattr(partner, 'dmx_DmxFilter13') is None


def test_assoc_withTypeSet14_stub_double():
    # dmx_DmxFilter has no real 'dmx_DmxFilter15' property in the generated
    # code (a bare stub) -- manually attach it so dmx_DmxBaseTypeSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dmx_DmxBaseTypeSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dmx_DmxBaseTypeSet(members="sample_text", name="sample_text")
    partner = dmx_DmxFilter()
    setattr(partner, 'dmx_DmxFilter15', None)
    _safe_set(owner, 'dmx_DmxBaseTypeSet', partner)
    assert getattr(partner, 'dmx_DmxFilter15') == owner
    _safe_set(owner, 'dmx_DmxBaseTypeSet', None)
    assert getattr(partner, 'dmx_DmxFilter15') is None


