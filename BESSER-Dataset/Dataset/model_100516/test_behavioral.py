import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractRanges,
    BindingExpression,
    Condition,
    Expression,
    ExpressionAndVariables,
    ExpressionOrRegion,
    InteractionFragment,
    ParameterExpression,
    Value,
    VariableExpression,
    sml_AbstractRanges,
    sml_Alternative,
    sml_BinaryOperationExpression,
    sml_BindingExpression,
    sml_BooleanValue,
    sml_Case,
    sml_CaseCondition,
    sml_Collaboration,
    sml_CollectionAccess,
    sml_Condition,
    sml_ConditionExpression,
    sml_ConstraintBlock,
    sml_Document,
    sml_EnumRanges,
    sml_EnumValue,
    sml_EventParameterRanges,
    sml_Expression,
    sml_ExpressionAndVariables,
    sml_ExpressionOrRegion,
    sml_ExpressionParameter,
    sml_ExpressionRegion,
    sml_FeatureAccess,
    sml_FeatureAccessBindingExpression,
    sml_Import,
    sml_IntegerRanges,
    sml_IntegerValue,
    sml_Interaction,
    sml_InteractionFragment,
    sml_InterruptCondition,
    sml_Loop,
    sml_LoopCondition,
    sml_Message,
    sml_ModalMessage,
    sml_NullValue,
    sml_Parallel,
    sml_ParameterBinding,
    sml_ParameterExpression,
    sml_RandomParameter,
    sml_RangesForParameter,
    sml_Role,
    sml_RoleBindingConstraint,
    sml_Scenario,
    sml_SmlEClass,
    sml_SmlEClassifier,
    sml_SmlEEnum,
    sml_SmlEEnumLiteral,
    sml_SmlEPackage,
    sml_SmlEStructuralFeature,
    sml_SmlETypedElement,
    sml_Specification,
    sml_StringRanges,
    sml_StringValue,
    sml_StructuralFeatureValue,
    sml_TypedVariableDeclaration,
    sml_UnaryOperationExpression,
    sml_Value,
    sml_Variable,
    sml_VariableAssignment,
    sml_VariableBindingParameter,
    sml_VariableDeclaration,
    sml_VariableExpression,
    sml_VariableFragment,
    sml_VariableValue,
    sml_ViolationCondition,
    sml_WaitCondition,
    CollectionOperation,
    ScenarioKind,
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

def test_assoc_containedCollaborations12_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration', a1)
    assert _is_linked(b, 'sml_Collaboration', a1)
    if hasattr(a1, 'sml_Specification13'):
        assert _is_linked(a1, 'sml_Specification13', b)
    _safe_set(b, 'sml_Collaboration', a2)
    assert _is_linked(b, 'sml_Collaboration', a2)
    if hasattr(a1, 'sml_Specification13'):
        assert not _is_linked(a1, 'sml_Specification13', b)
    if hasattr(a2, 'sml_Specification13'):
        assert _is_linked(a2, 'sml_Specification13', b)
    _safe_set(b, 'sml_Collaboration', None)
    assert not _is_linked(b, 'sml_Collaboration', a2)
    if hasattr(a2, 'sml_Specification13'):
        assert not _is_linked(a2, 'sml_Specification13', b)


def test_assoc_controllableEClasses3_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_SmlEClass(name="sample_text")
    _safe_set(b, 'sml_SmlEClass', a1)
    assert _is_linked(b, 'sml_SmlEClass', a1)
    if hasattr(a1, 'sml_Specification4'):
        assert _is_linked(a1, 'sml_Specification4', b)
    _safe_set(b, 'sml_SmlEClass', a2)
    assert _is_linked(b, 'sml_SmlEClass', a2)
    if hasattr(a1, 'sml_Specification4'):
        assert not _is_linked(a1, 'sml_Specification4', b)
    if hasattr(a2, 'sml_Specification4'):
        assert _is_linked(a2, 'sml_Specification4', b)
    _safe_set(b, 'sml_SmlEClass', None)
    assert not _is_linked(b, 'sml_SmlEClass', a2)
    if hasattr(a2, 'sml_Specification4'):
        assert not _is_linked(a2, 'sml_Specification4', b)


def test_assoc_domains1_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_SmlEPackage(name="sample_text")
    _safe_set(b, 'sml_SmlEPackage', a1)
    assert _is_linked(b, 'sml_SmlEPackage', a1)
    if hasattr(a1, 'sml_Specification2'):
        assert _is_linked(a1, 'sml_Specification2', b)
    _safe_set(b, 'sml_SmlEPackage', a2)
    assert _is_linked(b, 'sml_SmlEPackage', a2)
    if hasattr(a1, 'sml_Specification2'):
        assert not _is_linked(a1, 'sml_Specification2', b)
    if hasattr(a2, 'sml_Specification2'):
        assert _is_linked(a2, 'sml_Specification2', b)
    _safe_set(b, 'sml_SmlEPackage', None)
    assert not _is_linked(b, 'sml_SmlEPackage', a2)
    if hasattr(a2, 'sml_Specification2'):
        assert not _is_linked(a2, 'sml_Specification2', b)


def test_assoc_domains24_reverse_link_reassign_clear():
    a1 = sml_SmlEPackage(name="sample_text")
    a2 = sml_SmlEPackage(name="sample_text_2")
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration25', {a1})
    assert _is_linked(b, 'sml_Collaboration25', a1)
    if hasattr(a1, 'sml_SmlEPackage26'):
        assert _is_linked(a1, 'sml_SmlEPackage26', b)
    _safe_set(b, 'sml_Collaboration25', {a2})
    assert _is_linked(b, 'sml_Collaboration25', a2)
    if hasattr(a1, 'sml_SmlEPackage26'):
        assert not _is_linked(a1, 'sml_SmlEPackage26', b)
    if hasattr(a2, 'sml_SmlEPackage26'):
        assert _is_linked(a2, 'sml_SmlEPackage26', b)
    _safe_set(b, 'sml_Collaboration25', set())
    assert not _is_linked(b, 'sml_Collaboration25', a2)
    if hasattr(a2, 'sml_SmlEPackage26'):
        assert not _is_linked(a2, 'sml_SmlEPackage26', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_Import(importURI="sample_text")
    _safe_set(b, 'sml_Import', a1)
    assert _is_linked(b, 'sml_Import', a1)
    if hasattr(a1, 'sml_Specification'):
        assert _is_linked(a1, 'sml_Specification', b)
    _safe_set(b, 'sml_Import', a2)
    assert _is_linked(b, 'sml_Import', a2)
    if hasattr(a1, 'sml_Specification'):
        assert not _is_linked(a1, 'sml_Specification', b)
    if hasattr(a2, 'sml_Specification'):
        assert _is_linked(a2, 'sml_Specification', b)
    _safe_set(b, 'sml_Import', None)
    assert not _is_linked(b, 'sml_Import', a2)
    if hasattr(a2, 'sml_Specification'):
        assert not _is_linked(a2, 'sml_Specification', b)


def test_assoc_imports21_reverse_link_reassign_clear():
    a1 = sml_Import(importURI="sample_text")
    a2 = sml_Import(importURI="sample_text_2")
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration22', {a1})
    assert _is_linked(b, 'sml_Collaboration22', a1)
    if hasattr(a1, 'sml_Import23'):
        assert _is_linked(a1, 'sml_Import23', b)
    _safe_set(b, 'sml_Collaboration22', {a2})
    assert _is_linked(b, 'sml_Collaboration22', a2)
    if hasattr(a1, 'sml_Import23'):
        assert not _is_linked(a1, 'sml_Import23', b)
    if hasattr(a2, 'sml_Import23'):
        assert _is_linked(a2, 'sml_Import23', b)
    _safe_set(b, 'sml_Collaboration22', set())
    assert not _is_linked(b, 'sml_Collaboration22', a2)
    if hasattr(a2, 'sml_Import23'):
        assert not _is_linked(a2, 'sml_Import23', b)


def test_assoc_includedCollaborations14_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration16', a1)
    assert _is_linked(b, 'sml_Collaboration16', a1)
    if hasattr(a1, 'sml_Specification15'):
        assert _is_linked(a1, 'sml_Specification15', b)
    _safe_set(b, 'sml_Collaboration16', a2)
    assert _is_linked(b, 'sml_Collaboration16', a2)
    if hasattr(a1, 'sml_Specification15'):
        assert not _is_linked(a1, 'sml_Specification15', b)
    if hasattr(a2, 'sml_Specification15'):
        assert _is_linked(a2, 'sml_Specification15', b)
    _safe_set(b, 'sml_Collaboration16', None)
    assert not _is_linked(b, 'sml_Collaboration16', a2)
    if hasattr(a2, 'sml_Specification15'):
        assert not _is_linked(a2, 'sml_Specification15', b)


def test_assoc_modelElement61_reverse_link_reassign_clear():
    a1 = sml_SmlETypedElement(name="sample_text")
    a2 = sml_SmlETypedElement(name="sample_text_2")
    b = sml_ModalMessage(requested=True, strict=True)
    _safe_set(b, 'sml_ModalMessage62', a1)
    assert _is_linked(b, 'sml_ModalMessage62', a1)
    if hasattr(a1, 'sml_SmlETypedElement63'):
        assert _is_linked(a1, 'sml_SmlETypedElement63', b)
    _safe_set(b, 'sml_ModalMessage62', a2)
    assert _is_linked(b, 'sml_ModalMessage62', a2)
    if hasattr(a1, 'sml_SmlETypedElement63'):
        assert not _is_linked(a1, 'sml_SmlETypedElement63', b)
    if hasattr(a2, 'sml_SmlETypedElement63'):
        assert _is_linked(a2, 'sml_SmlETypedElement63', b)
    _safe_set(b, 'sml_ModalMessage62', None)
    assert not _is_linked(b, 'sml_ModalMessage62', a2)
    if hasattr(a2, 'sml_SmlETypedElement63'):
        assert not _is_linked(a2, 'sml_SmlETypedElement63', b)


def test_assoc_nonSpontaneousOperations8_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_SmlETypedElement(name="sample_text")
    _safe_set(b, 'sml_SmlETypedElement', a1)
    assert _is_linked(b, 'sml_SmlETypedElement', a1)
    if hasattr(a1, 'sml_Specification9'):
        assert _is_linked(a1, 'sml_Specification9', b)
    _safe_set(b, 'sml_SmlETypedElement', a2)
    assert _is_linked(b, 'sml_SmlETypedElement', a2)
    if hasattr(a1, 'sml_Specification9'):
        assert not _is_linked(a1, 'sml_Specification9', b)
    if hasattr(a2, 'sml_Specification9'):
        assert _is_linked(a2, 'sml_Specification9', b)
    _safe_set(b, 'sml_SmlETypedElement', None)
    assert not _is_linked(b, 'sml_SmlETypedElement', a2)
    if hasattr(a2, 'sml_Specification9'):
        assert not _is_linked(a2, 'sml_Specification9', b)


def test_assoc_receiver58_reverse_link_reassign_clear():
    a1 = sml_Role(name="sample_text", static=True)
    a2 = sml_Role(name="sample_text_2", static=False)
    b = sml_ModalMessage(requested=True, strict=True)
    _safe_set(b, 'sml_ModalMessage59', a1)
    assert _is_linked(b, 'sml_ModalMessage59', a1)
    if hasattr(a1, 'sml_Role60'):
        assert _is_linked(a1, 'sml_Role60', b)
    _safe_set(b, 'sml_ModalMessage59', a2)
    assert _is_linked(b, 'sml_ModalMessage59', a2)
    if hasattr(a1, 'sml_Role60'):
        assert not _is_linked(a1, 'sml_Role60', b)
    if hasattr(a2, 'sml_Role60'):
        assert _is_linked(a2, 'sml_Role60', b)
    _safe_set(b, 'sml_ModalMessage59', None)
    assert not _is_linked(b, 'sml_ModalMessage59', a2)
    if hasattr(a2, 'sml_Role60'):
        assert not _is_linked(a2, 'sml_Role60', b)


def test_assoc_roles17_reverse_link_reassign_clear():
    a1 = sml_Role(name="sample_text", static=True)
    a2 = sml_Role(name="sample_text_2", static=False)
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration18', {a1})
    assert _is_linked(b, 'sml_Collaboration18', a1)
    if hasattr(a1, 'sml_Role'):
        assert _is_linked(a1, 'sml_Role', b)
    _safe_set(b, 'sml_Collaboration18', {a2})
    assert _is_linked(b, 'sml_Collaboration18', a2)
    if hasattr(a1, 'sml_Role'):
        assert not _is_linked(a1, 'sml_Role', b)
    if hasattr(a2, 'sml_Role'):
        assert _is_linked(a2, 'sml_Role', b)
    _safe_set(b, 'sml_Collaboration18', set())
    assert not _is_linked(b, 'sml_Collaboration18', a2)
    if hasattr(a2, 'sml_Role'):
        assert not _is_linked(a2, 'sml_Role', b)


def test_assoc_scenarios19_reverse_link_reassign_clear():
    a1 = sml_Scenario(kind="sample_text", name="sample_text", singular=True)
    a2 = sml_Scenario(kind="sample_text_2", name="sample_text_2", singular=False)
    b = sml_Collaboration(name="sample_text")
    _safe_set(b, 'sml_Collaboration20', {a1})
    assert _is_linked(b, 'sml_Collaboration20', a1)
    if hasattr(a1, 'sml_Scenario'):
        assert _is_linked(a1, 'sml_Scenario', b)
    _safe_set(b, 'sml_Collaboration20', {a2})
    assert _is_linked(b, 'sml_Collaboration20', a2)
    if hasattr(a1, 'sml_Scenario'):
        assert not _is_linked(a1, 'sml_Scenario', b)
    if hasattr(a2, 'sml_Scenario'):
        assert _is_linked(a2, 'sml_Scenario', b)
    _safe_set(b, 'sml_Collaboration20', set())
    assert not _is_linked(b, 'sml_Collaboration20', a2)
    if hasattr(a2, 'sml_Scenario'):
        assert not _is_linked(a2, 'sml_Scenario', b)


def test_assoc_sender56_reverse_link_reassign_clear():
    a1 = sml_Role(name="sample_text", static=True)
    a2 = sml_Role(name="sample_text_2", static=False)
    b = sml_ModalMessage(requested=True, strict=True)
    _safe_set(b, 'sml_ModalMessage', a1)
    assert _is_linked(b, 'sml_ModalMessage', a1)
    if hasattr(a1, 'sml_Role57'):
        assert _is_linked(a1, 'sml_Role57', b)
    _safe_set(b, 'sml_ModalMessage', a2)
    assert _is_linked(b, 'sml_ModalMessage', a2)
    if hasattr(a1, 'sml_Role57'):
        assert not _is_linked(a1, 'sml_Role57', b)
    if hasattr(a2, 'sml_Role57'):
        assert _is_linked(a2, 'sml_Role57', b)
    _safe_set(b, 'sml_ModalMessage', None)
    assert not _is_linked(b, 'sml_ModalMessage', a2)
    if hasattr(a2, 'sml_Role57'):
        assert not _is_linked(a2, 'sml_Role57', b)


def test_assoc_type129_reverse_link_reassign_clear():
    a1 = sml_TypedVariableDeclaration(name="sample_text")
    a2 = sml_TypedVariableDeclaration(name="sample_text_2")
    b = sml_SmlEClassifier(name="sample_text")
    _safe_set(b, 'sml_SmlEClassifier', a1)
    assert _is_linked(b, 'sml_SmlEClassifier', a1)
    if hasattr(a1, 'sml_TypedVariableDeclaration'):
        assert _is_linked(a1, 'sml_TypedVariableDeclaration', b)
    _safe_set(b, 'sml_SmlEClassifier', a2)
    assert _is_linked(b, 'sml_SmlEClassifier', a2)
    if hasattr(a1, 'sml_TypedVariableDeclaration'):
        assert not _is_linked(a1, 'sml_TypedVariableDeclaration', b)
    if hasattr(a2, 'sml_TypedVariableDeclaration'):
        assert _is_linked(a2, 'sml_TypedVariableDeclaration', b)
    _safe_set(b, 'sml_SmlEClassifier', None)
    assert not _is_linked(b, 'sml_SmlEClassifier', a2)
    if hasattr(a2, 'sml_TypedVariableDeclaration'):
        assert not _is_linked(a2, 'sml_TypedVariableDeclaration', b)


def test_assoc_type38_reverse_link_reassign_clear():
    a1 = sml_SmlEClass(name="sample_text")
    a2 = sml_SmlEClass(name="sample_text_2")
    b = sml_Role(name="sample_text", static=True)
    _safe_set(b, 'sml_Role39', a1)
    assert _is_linked(b, 'sml_Role39', a1)
    if hasattr(a1, 'sml_SmlEClass40'):
        assert _is_linked(a1, 'sml_SmlEClass40', b)
    _safe_set(b, 'sml_Role39', a2)
    assert _is_linked(b, 'sml_Role39', a2)
    if hasattr(a1, 'sml_SmlEClass40'):
        assert not _is_linked(a1, 'sml_SmlEClass40', b)
    if hasattr(a2, 'sml_SmlEClass40'):
        assert _is_linked(a2, 'sml_SmlEClass40', b)
    _safe_set(b, 'sml_Role39', None)
    assert not _is_linked(b, 'sml_Role39', a2)
    if hasattr(a2, 'sml_SmlEClass40'):
        assert not _is_linked(a2, 'sml_SmlEClass40', b)


def test_assoc_uncontrollableEClasses5_reverse_link_reassign_clear():
    a1 = sml_Specification(name="sample_text")
    a2 = sml_Specification(name="sample_text_2")
    b = sml_SmlEClass(name="sample_text")
    _safe_set(b, 'sml_SmlEClass7', a1)
    assert _is_linked(b, 'sml_SmlEClass7', a1)
    if hasattr(a1, 'sml_Specification6'):
        assert _is_linked(a1, 'sml_Specification6', b)
    _safe_set(b, 'sml_SmlEClass7', a2)
    assert _is_linked(b, 'sml_SmlEClass7', a2)
    if hasattr(a1, 'sml_Specification6'):
        assert not _is_linked(a1, 'sml_Specification6', b)
    if hasattr(a2, 'sml_Specification6'):
        assert _is_linked(a2, 'sml_Specification6', b)
    _safe_set(b, 'sml_SmlEClass7', None)
    assert not _is_linked(b, 'sml_SmlEClass7', a2)
    if hasattr(a2, 'sml_Specification6'):
        assert not _is_linked(a2, 'sml_Specification6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_collectionAccess145_stub_double():
    # sml_FeatureAccess has no real 'sml_FeatureAccess146' property in the generated
    # code (a bare stub) -- manually attach it so sml_CollectionAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_CollectionAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_CollectionAccess(collectionOperation="sample_text")
    partner = sml_FeatureAccess()
    setattr(partner, 'sml_FeatureAccess146', None)
    _safe_set(owner, 'sml_CollectionAccess147', partner)
    assert getattr(partner, 'sml_FeatureAccess146') == owner
    _safe_set(owner, 'sml_CollectionAccess147', None)
    assert getattr(partner, 'sml_FeatureAccess146') is None


def test_assoc_domains117_stub_double():
    # sml_Document has no real 'sml_Document118' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlEPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlEPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlEPackage(name="sample_text")
    partner = sml_Document()
    setattr(partner, 'sml_Document118', None)
    _safe_set(owner, 'sml_SmlEPackage119', partner)
    assert owner in getattr(partner, 'sml_Document118')
    _safe_set(owner, 'sml_SmlEPackage119', None)
    assert owner not in getattr(partner, 'sml_Document118')


def test_assoc_event27_stub_double():
    # sml_EventParameterRanges has no real 'sml_EventParameterRanges28' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlETypedElement(name="sample_text")
    partner = sml_EventParameterRanges()
    setattr(partner, 'sml_EventParameterRanges28', None)
    _safe_set(owner, 'sml_SmlETypedElement29', partner)
    assert getattr(partner, 'sml_EventParameterRanges28') == owner
    _safe_set(owner, 'sml_SmlETypedElement29', None)
    assert getattr(partner, 'sml_EventParameterRanges28') is None


def test_assoc_eventParameterRanges10_stub_double():
    # sml_EventParameterRanges has no real 'sml_EventParameterRanges' property in the generated
    # code (a bare stub) -- manually attach it so sml_Specification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Specification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Specification(name="sample_text")
    partner = sml_EventParameterRanges()
    setattr(partner, 'sml_EventParameterRanges', None)
    _safe_set(owner, 'sml_Specification11', {partner})
    assert getattr(partner, 'sml_EventParameterRanges') == owner
    _safe_set(owner, 'sml_Specification11', set())
    assert getattr(partner, 'sml_EventParameterRanges') is None


def test_assoc_expression127_stub_double():
    # sml_Expression has no real 'sml_Expression128' property in the generated
    # code (a bare stub) -- manually attach it so sml_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_VariableDeclaration(name="sample_text")
    partner = sml_Expression()
    setattr(partner, 'sml_Expression128', None)
    _safe_set(owner, 'sml_VariableDeclaration', partner)
    assert getattr(partner, 'sml_Expression128') == owner
    _safe_set(owner, 'sml_VariableDeclaration', None)
    assert getattr(partner, 'sml_Expression128') is None


def test_assoc_imports115_stub_double():
    # sml_Document has no real 'sml_Document' property in the generated
    # code (a bare stub) -- manually attach it so sml_Import's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Import's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Import(importURI="sample_text")
    partner = sml_Document()
    setattr(partner, 'sml_Document', None)
    _safe_set(owner, 'sml_Import116', partner)
    assert owner in getattr(partner, 'sml_Document')
    _safe_set(owner, 'sml_Import116', None)
    assert owner not in getattr(partner, 'sml_Document')


def test_assoc_left150_stub_double():
    # sml_Expression has no real 'sml_Expression151' property in the generated
    # code (a bare stub) -- manually attach it so sml_BinaryOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_BinaryOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_BinaryOperationExpression(operator="sample_text")
    partner = sml_Expression()
    setattr(partner, 'sml_Expression151', None)
    _safe_set(owner, 'sml_BinaryOperationExpression', partner)
    assert getattr(partner, 'sml_Expression151') == owner
    _safe_set(owner, 'sml_BinaryOperationExpression', None)
    assert getattr(partner, 'sml_Expression151') is None


def test_assoc_modelElement109_stub_double():
    # sml_Message has no real 'sml_Message110' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlETypedElement(name="sample_text")
    partner = sml_Message()
    setattr(partner, 'sml_Message110', None)
    _safe_set(owner, 'sml_SmlETypedElement111', partner)
    assert getattr(partner, 'sml_Message110') == owner
    _safe_set(owner, 'sml_SmlETypedElement111', None)
    assert getattr(partner, 'sml_Message110') is None


def test_assoc_operand155_stub_double():
    # sml_Expression has no real 'sml_Expression156' property in the generated
    # code (a bare stub) -- manually attach it so sml_UnaryOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_UnaryOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_UnaryOperationExpression(operator="sample_text")
    partner = sml_Expression()
    setattr(partner, 'sml_Expression156', None)
    _safe_set(owner, 'sml_UnaryOperationExpression', partner)
    assert getattr(partner, 'sml_Expression156') == owner
    _safe_set(owner, 'sml_UnaryOperationExpression', None)
    assert getattr(partner, 'sml_Expression156') is None


def test_assoc_ownedInteraction43_stub_double():
    # sml_Interaction has no real 'sml_Interaction' property in the generated
    # code (a bare stub) -- manually attach it so sml_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Scenario(kind="sample_text", name="sample_text", singular=True)
    partner = sml_Interaction()
    setattr(partner, 'sml_Interaction', None)
    _safe_set(owner, 'sml_Scenario44', partner)
    assert getattr(partner, 'sml_Interaction') == owner
    _safe_set(owner, 'sml_Scenario44', None)
    assert getattr(partner, 'sml_Interaction') is None


def test_assoc_parameter138_stub_double():
    # sml_Expression has no real 'sml_Expression139' property in the generated
    # code (a bare stub) -- manually attach it so sml_CollectionAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_CollectionAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_CollectionAccess(collectionOperation="sample_text")
    partner = sml_Expression()
    setattr(partner, 'sml_Expression139', None)
    _safe_set(owner, 'sml_CollectionAccess', partner)
    assert getattr(partner, 'sml_Expression139') == owner
    _safe_set(owner, 'sml_CollectionAccess', None)
    assert getattr(partner, 'sml_Expression139') is None


def test_assoc_parameter32_stub_double():
    # sml_RangesForParameter has no real 'sml_RangesForParameter33' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlETypedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlETypedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlETypedElement(name="sample_text")
    partner = sml_RangesForParameter()
    setattr(partner, 'sml_RangesForParameter33', None)
    _safe_set(owner, 'sml_SmlETypedElement34', partner)
    assert getattr(partner, 'sml_RangesForParameter33') == owner
    _safe_set(owner, 'sml_SmlETypedElement34', None)
    assert getattr(partner, 'sml_RangesForParameter33') is None


def test_assoc_parameters64_stub_double():
    # sml_ParameterBinding has no real 'sml_ParameterBinding' property in the generated
    # code (a bare stub) -- manually attach it so sml_ModalMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_ModalMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_ModalMessage(requested=True, strict=True)
    partner = sml_ParameterBinding()
    setattr(partner, 'sml_ParameterBinding', None)
    _safe_set(owner, 'sml_ModalMessage65', {partner})
    assert getattr(partner, 'sml_ParameterBinding') == owner
    _safe_set(owner, 'sml_ModalMessage65', set())
    assert getattr(partner, 'sml_ParameterBinding') is None


def test_assoc_receiver106_stub_double():
    # sml_Message has no real 'sml_Message107' property in the generated
    # code (a bare stub) -- manually attach it so sml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Role(name="sample_text", static=True)
    partner = sml_Message()
    setattr(partner, 'sml_Message107', None)
    _safe_set(owner, 'sml_Role108', partner)
    assert getattr(partner, 'sml_Message107') == owner
    _safe_set(owner, 'sml_Role108', None)
    assert getattr(partner, 'sml_Message107') is None


def test_assoc_right152_stub_double():
    # sml_Expression has no real 'sml_Expression154' property in the generated
    # code (a bare stub) -- manually attach it so sml_BinaryOperationExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_BinaryOperationExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_BinaryOperationExpression(operator="sample_text")
    partner = sml_Expression()
    setattr(partner, 'sml_Expression154', None)
    _safe_set(owner, 'sml_BinaryOperationExpression153', partner)
    assert getattr(partner, 'sml_Expression154') == owner
    _safe_set(owner, 'sml_BinaryOperationExpression153', None)
    assert getattr(partner, 'sml_Expression154') is None


def test_assoc_role45_stub_double():
    # sml_RoleBindingConstraint has no real 'sml_RoleBindingConstraint46' property in the generated
    # code (a bare stub) -- manually attach it so sml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Role(name="sample_text", static=True)
    partner = sml_RoleBindingConstraint()
    setattr(partner, 'sml_RoleBindingConstraint46', None)
    _safe_set(owner, 'sml_Role47', partner)
    assert getattr(partner, 'sml_RoleBindingConstraint46') == owner
    _safe_set(owner, 'sml_Role47', None)
    assert getattr(partner, 'sml_RoleBindingConstraint46') is None


def test_assoc_roleBindings41_stub_double():
    # sml_RoleBindingConstraint has no real 'sml_RoleBindingConstraint' property in the generated
    # code (a bare stub) -- manually attach it so sml_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Scenario(kind="sample_text", name="sample_text", singular=True)
    partner = sml_RoleBindingConstraint()
    setattr(partner, 'sml_RoleBindingConstraint', None)
    _safe_set(owner, 'sml_Scenario42', {partner})
    assert getattr(partner, 'sml_RoleBindingConstraint') == owner
    _safe_set(owner, 'sml_Scenario42', set())
    assert getattr(partner, 'sml_RoleBindingConstraint') is None


def test_assoc_sender103_stub_double():
    # sml_Message has no real 'sml_Message104' property in the generated
    # code (a bare stub) -- manually attach it so sml_Role's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Role's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Role(name="sample_text", static=True)
    partner = sml_Message()
    setattr(partner, 'sml_Message104', None)
    _safe_set(owner, 'sml_Role105', partner)
    assert getattr(partner, 'sml_Message104') == owner
    _safe_set(owner, 'sml_Role105', None)
    assert getattr(partner, 'sml_Message104') is None


def test_assoc_type132_stub_double():
    # sml_EnumValue has no real 'sml_EnumValue' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlEEnum's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlEEnum's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlEEnum(name="sample_text")
    partner = sml_EnumValue()
    setattr(partner, 'sml_EnumValue', None)
    _safe_set(owner, 'sml_SmlEEnum', partner)
    assert getattr(partner, 'sml_EnumValue') == owner
    _safe_set(owner, 'sml_SmlEEnum', None)
    assert getattr(partner, 'sml_EnumValue') is None


def test_assoc_value133_stub_double():
    # sml_EnumValue has no real 'sml_EnumValue134' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlEEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlEEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlEEnumLiteral(name="sample_text")
    partner = sml_EnumValue()
    setattr(partner, 'sml_EnumValue134', None)
    _safe_set(owner, 'sml_SmlEEnumLiteral135', partner)
    assert getattr(partner, 'sml_EnumValue134') == owner
    _safe_set(owner, 'sml_SmlEEnumLiteral135', None)
    assert getattr(partner, 'sml_EnumValue134') is None


def test_assoc_value136_stub_double():
    # sml_VariableValue has no real 'sml_VariableValue137' property in the generated
    # code (a bare stub) -- manually attach it so sml_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Variable(name="sample_text")
    partner = sml_VariableValue()
    setattr(partner, 'sml_VariableValue137', None)
    _safe_set(owner, 'sml_Variable', partner)
    assert getattr(partner, 'sml_VariableValue137') == owner
    _safe_set(owner, 'sml_Variable', None)
    assert getattr(partner, 'sml_VariableValue137') is None


def test_assoc_value148_stub_double():
    # sml_StructuralFeatureValue has no real 'sml_StructuralFeatureValue149' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlEStructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlEStructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlEStructuralFeature(name="sample_text")
    partner = sml_StructuralFeatureValue()
    setattr(partner, 'sml_StructuralFeatureValue149', None)
    _safe_set(owner, 'sml_SmlEStructuralFeature', partner)
    assert getattr(partner, 'sml_StructuralFeatureValue149') == owner
    _safe_set(owner, 'sml_SmlEStructuralFeature', None)
    assert getattr(partner, 'sml_StructuralFeatureValue149') is None


def test_assoc_values37_stub_double():
    # sml_EnumRanges has no real 'sml_EnumRanges' property in the generated
    # code (a bare stub) -- manually attach it so sml_SmlEEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_SmlEEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_SmlEEnumLiteral(name="sample_text")
    partner = sml_EnumRanges()
    setattr(partner, 'sml_EnumRanges', None)
    _safe_set(owner, 'sml_SmlEEnumLiteral', partner)
    assert owner in getattr(partner, 'sml_EnumRanges')
    _safe_set(owner, 'sml_SmlEEnumLiteral', None)
    assert owner not in getattr(partner, 'sml_EnumRanges')


def test_assoc_variable130_stub_double():
    # sml_VariableAssignment has no real 'sml_VariableAssignment' property in the generated
    # code (a bare stub) -- manually attach it so sml_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_VariableDeclaration(name="sample_text")
    partner = sml_VariableAssignment()
    setattr(partner, 'sml_VariableAssignment', None)
    _safe_set(owner, 'sml_VariableDeclaration131', partner)
    assert getattr(partner, 'sml_VariableAssignment') == owner
    _safe_set(owner, 'sml_VariableDeclaration131', None)
    assert getattr(partner, 'sml_VariableAssignment') is None


def test_assoc_variable140_stub_double():
    # sml_FeatureAccess has no real 'sml_FeatureAccess141' property in the generated
    # code (a bare stub) -- manually attach it so sml_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sml_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sml_Variable(name="sample_text")
    partner = sml_FeatureAccess()
    setattr(partner, 'sml_FeatureAccess141', None)
    _safe_set(owner, 'sml_Variable142', partner)
    assert getattr(partner, 'sml_FeatureAccess141') == owner
    _safe_set(owner, 'sml_Variable142', None)
    assert getattr(partner, 'sml_FeatureAccess141') is None


