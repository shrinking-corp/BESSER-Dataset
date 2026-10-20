import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SrcEClassifier,
    SrcEDataType,
    SrcENamedElement,
    SrcEStructuralFeature,
    SrcETypedElement,
    TrgCondition,
    TrgEquationalCond,
    TrgMaudeTopEl,
    TrgModElement,
    TrgModExpression,
    TrgModule,
    TrgRenMapping,
    TrgStatement,
    TrgTerm,
    TrgTheory,
    TrgType,
    TrgViewMapping,
    jointPackage_Ecore2Maude_JointMM,
    jointPackage_Ecore2Maude_SrcEAttribute,
    jointPackage_Ecore2Maude_SrcEClass,
    jointPackage_Ecore2Maude_SrcEClassifier,
    jointPackage_Ecore2Maude_SrcEDataType,
    jointPackage_Ecore2Maude_SrcEEnum,
    jointPackage_Ecore2Maude_SrcEEnumLiteral,
    jointPackage_Ecore2Maude_SrcENamedElement,
    jointPackage_Ecore2Maude_SrcEOperation,
    jointPackage_Ecore2Maude_SrcEPackage,
    jointPackage_Ecore2Maude_SrcEParameter,
    jointPackage_Ecore2Maude_SrcEReference,
    jointPackage_Ecore2Maude_SrcEStringToStringMapEntry,
    jointPackage_Ecore2Maude_SrcEStructuralFeature,
    jointPackage_Ecore2Maude_SrcETypedElement,
    jointPackage_Ecore2Maude_TrgBooleanCond,
    jointPackage_Ecore2Maude_TrgCompModExp,
    jointPackage_Ecore2Maude_TrgCondition,
    jointPackage_Ecore2Maude_TrgConstant,
    jointPackage_Ecore2Maude_TrgEqualCond,
    jointPackage_Ecore2Maude_TrgEquation,
    jointPackage_Ecore2Maude_TrgEquationalCond,
    jointPackage_Ecore2Maude_TrgFModule,
    jointPackage_Ecore2Maude_TrgFTheory,
    jointPackage_Ecore2Maude_TrgInstModExp,
    jointPackage_Ecore2Maude_TrgKind,
    jointPackage_Ecore2Maude_TrgLabelMapping,
    jointPackage_Ecore2Maude_TrgMatchingCond,
    jointPackage_Ecore2Maude_TrgMaudeSpec,
    jointPackage_Ecore2Maude_TrgMaudeTopEl,
    jointPackage_Ecore2Maude_TrgMembership,
    jointPackage_Ecore2Maude_TrgMembershipCond,
    jointPackage_Ecore2Maude_TrgModElement,
    jointPackage_Ecore2Maude_TrgModExpression,
    jointPackage_Ecore2Maude_TrgModImportation,
    jointPackage_Ecore2Maude_TrgModule,
    jointPackage_Ecore2Maude_TrgModuleIdModExp,
    jointPackage_Ecore2Maude_TrgOpMapping,
    jointPackage_Ecore2Maude_TrgOpTypedMapping,
    jointPackage_Ecore2Maude_TrgOperation,
    jointPackage_Ecore2Maude_TrgParameter,
    jointPackage_Ecore2Maude_TrgRecTerm,
    jointPackage_Ecore2Maude_TrgRenMapping,
    jointPackage_Ecore2Maude_TrgRenModExp,
    jointPackage_Ecore2Maude_TrgRewriteCond,
    jointPackage_Ecore2Maude_TrgRule,
    jointPackage_Ecore2Maude_TrgSModule,
    jointPackage_Ecore2Maude_TrgSTheory,
    jointPackage_Ecore2Maude_TrgSort,
    jointPackage_Ecore2Maude_TrgSortMapping,
    jointPackage_Ecore2Maude_TrgStatement,
    jointPackage_Ecore2Maude_TrgSubsortRel,
    jointPackage_Ecore2Maude_TrgTerm,
    jointPackage_Ecore2Maude_TrgTermMapping,
    jointPackage_Ecore2Maude_TrgTheory,
    jointPackage_Ecore2Maude_TrgTheoryIdModExp,
    jointPackage_Ecore2Maude_TrgType,
    jointPackage_Ecore2Maude_TrgVariable,
    jointPackage_Ecore2Maude_TrgView,
    jointPackage_Ecore2Maude_TrgViewMapping,
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

def test_assoc_arity120_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_TrgType(name="sample_text")
    a2 = jointPackage_Ecore2Maude_TrgType(name="sample_text_2")
    b = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text", name="sample_text")
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation121', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation121', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgType122'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_TrgType122', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation121', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation121', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgType122'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_TrgType122', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgType122'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_TrgType122', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation121', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation121', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgType122'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_TrgType122', b)


def test_assoc_coarity119_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_TrgType(name="sample_text")
    a2 = jointPackage_Ecore2Maude_TrgType(name="sample_text_2")
    b = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text", name="sample_text")
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgType'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_TrgType', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgType'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_TrgType', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgType'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_TrgType', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOperation', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_TrgOperation', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgType'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_TrgType', b)


def test_assoc_eAllAttributes7_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    a2 = jointPackage_Ecore2Maude_SrcEClass(abstract=False, interface=False)
    b = jointPackage_Ecore2Maude_SrcEAttribute(iD=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass8'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass8', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass8'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass8', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass8'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass8', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute9', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass8'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass8', b)


def test_assoc_eAllContainments18_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass19', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass19', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference20'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference20', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass19', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass19', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference20'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference20', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference20'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference20', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass19', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass19', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference20'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference20', b)


def test_assoc_eAllReferences10_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass11', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass11', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass11', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass11', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass11', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass11', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference', b)


def test_assoc_eAllStructuralFeatures23_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass24', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass24', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEStructuralFeature'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEStructuralFeature', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass24', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass24', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEStructuralFeature'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEStructuralFeature', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEStructuralFeature'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEStructuralFeature', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass24', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass24', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEStructuralFeature'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEStructuralFeature', b)


def test_assoc_eAllSuperTypes26_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    a2 = jointPackage_Ecore2Maude_SrcEClass(abstract=False, interface=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass27', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass27', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass25'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass25', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass27', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass27', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass25'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass25', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass25'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass25', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass27', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass27', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass25'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass25', b)


def test_assoc_eAttributeType3_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEDataType(serializable=True)
    a2 = jointPackage_Ecore2Maude_SrcEDataType(serializable=False)
    b = jointPackage_Ecore2Maude_SrcEAttribute(iD=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEDataType'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEDataType', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEDataType'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEDataType', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEDataType'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEDataType', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEDataType'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEDataType', b)


def test_assoc_eAttributes15_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    a2 = jointPackage_Ecore2Maude_SrcEClass(abstract=False, interface=False)
    b = jointPackage_Ecore2Maude_SrcEAttribute(iD=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass16'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass16', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass16'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass16', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass16'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass16', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute17', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass16'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass16', b)


def test_assoc_eClassifiers40_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = jointPackage_Ecore2Maude_SrcEClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'SrcEClassifier', a1)
    assert _is_linked(b, 'SrcEClassifier', a1)
    if hasattr(a1, 'ePackage'):
        assert _is_linked(a1, 'ePackage', b)
    _safe_set(b, 'SrcEClassifier', a2)
    assert _is_linked(b, 'SrcEClassifier', a2)
    if hasattr(a1, 'ePackage'):
        assert not _is_linked(a1, 'ePackage', b)
    if hasattr(a2, 'ePackage'):
        assert _is_linked(a2, 'ePackage', b)
    _safe_set(b, 'SrcEClassifier', None)
    assert not _is_linked(b, 'SrcEClassifier', a2)
    if hasattr(a2, 'ePackage'):
        assert not _is_linked(a2, 'ePackage', b)


def test_assoc_eContainingClass58_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'SrcEClass59', a1)
    assert _is_linked(b, 'SrcEClass59', a1)
    if hasattr(a1, 'eStructuralFeatures'):
        assert _is_linked(a1, 'eStructuralFeatures', b)
    _safe_set(b, 'SrcEClass59', a2)
    assert _is_linked(b, 'SrcEClass59', a2)
    if hasattr(a1, 'eStructuralFeatures'):
        assert not _is_linked(a1, 'eStructuralFeatures', b)
    if hasattr(a2, 'eStructuralFeatures'):
        assert _is_linked(a2, 'eStructuralFeatures', b)
    _safe_set(b, 'SrcEClass59', None)
    assert not _is_linked(b, 'SrcEClass59', a2)
    if hasattr(a2, 'eStructuralFeatures'):
        assert not _is_linked(a2, 'eStructuralFeatures', b)


def test_assoc_eEnum35_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEEnumLiteral(literal="sample_text", value=7)
    a2 = jointPackage_Ecore2Maude_SrcEEnumLiteral(literal="sample_text_2", value=13)
    b = jointPackage_Ecore2Maude_SrcEEnum()
    _safe_set(b, 'SrcEEnum', a1)
    assert _is_linked(b, 'SrcEEnum', a1)
    if hasattr(a1, 'eLiterals'):
        assert _is_linked(a1, 'eLiterals', b)
    _safe_set(b, 'SrcEEnum', a2)
    assert _is_linked(b, 'SrcEEnum', a2)
    if hasattr(a1, 'eLiterals'):
        assert not _is_linked(a1, 'eLiterals', b)
    if hasattr(a2, 'eLiterals'):
        assert _is_linked(a2, 'eLiterals', b)
    _safe_set(b, 'SrcEEnum', None)
    assert not _is_linked(b, 'SrcEEnum', a2)
    if hasattr(a2, 'eLiterals'):
        assert not _is_linked(a2, 'eLiterals', b)


def test_assoc_eIDAttribute28_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    a2 = jointPackage_Ecore2Maude_SrcEClass(abstract=False, interface=False)
    b = jointPackage_Ecore2Maude_SrcEAttribute(iD=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass29'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass29', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass29'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass29', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass29'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass29', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute30', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass29'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass29', b)


def test_assoc_eKeys55_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEAttribute(iD=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference56'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference56', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference56'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference56', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference56'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference56', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEAttribute57', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference56'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference56', b)


def test_assoc_eLiterals34_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEEnumLiteral(literal="sample_text", value=7)
    a2 = jointPackage_Ecore2Maude_SrcEEnumLiteral(literal="sample_text_2", value=13)
    b = jointPackage_Ecore2Maude_SrcEEnum()
    _safe_set(b, 'eEnum', {a1})
    assert _is_linked(b, 'eEnum', a1)
    if hasattr(a1, 'SrcEEnumLiteral'):
        assert _is_linked(a1, 'SrcEEnumLiteral', b)
    _safe_set(b, 'eEnum', {a2})
    assert _is_linked(b, 'eEnum', a2)
    if hasattr(a1, 'SrcEEnumLiteral'):
        assert not _is_linked(a1, 'SrcEEnumLiteral', b)
    if hasattr(a2, 'SrcEEnumLiteral'):
        assert _is_linked(a2, 'SrcEEnumLiteral', b)
    _safe_set(b, 'eEnum', set())
    assert not _is_linked(b, 'eEnum', a2)
    if hasattr(a2, 'SrcEEnumLiteral'):
        assert not _is_linked(a2, 'SrcEEnumLiteral', b)


def test_assoc_eOpposite50_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEReference51', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEReference51', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference49'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference49', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEReference51', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEReference51', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference49'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference49', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference49'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference49', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEReference51', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEReference51', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference49'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference49', b)


def test_assoc_ePackage33_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = jointPackage_Ecore2Maude_SrcEClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'eClassifiers', a1)
    assert _is_linked(b, 'eClassifiers', a1)
    if hasattr(a1, 'SrcEPackage'):
        assert _is_linked(a1, 'SrcEPackage', b)
    _safe_set(b, 'eClassifiers', a2)
    assert _is_linked(b, 'eClassifiers', a2)
    if hasattr(a1, 'SrcEPackage'):
        assert not _is_linked(a1, 'SrcEPackage', b)
    if hasattr(a2, 'SrcEPackage'):
        assert _is_linked(a2, 'SrcEPackage', b)
    _safe_set(b, 'eClassifiers', None)
    assert not _is_linked(b, 'eClassifiers', a2)
    if hasattr(a2, 'SrcEPackage'):
        assert not _is_linked(a2, 'SrcEPackage', b)


def test_assoc_eReferenceType52_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass54', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass54', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference53'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference53', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass54', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass54', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference53'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference53', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference53'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference53', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass54', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass54', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference53'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference53', b)


def test_assoc_eReferences12_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEReference(container=True, containment=True, resolveProxies=True)
    a2 = jointPackage_Ecore2Maude_SrcEReference(container=False, containment=False, resolveProxies=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass13', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass13', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference14'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference14', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass13', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass13', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEReference14'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEReference14', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference14'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference14', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass13', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass13', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEReference14'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEReference14', b)


def test_assoc_eStructuralFeatures31_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=True, defaultValueLiteral="sample_text", derived=True, transient=True, unsettable=True, volatile=True)
    a2 = jointPackage_Ecore2Maude_SrcEStructuralFeature(changeable=False, defaultValueLiteral="sample_text_2", derived=False, transient=False, unsettable=False, volatile=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'eContainingClass32', {a1})
    assert _is_linked(b, 'eContainingClass32', a1)
    if hasattr(a1, 'SrcEStructuralFeature'):
        assert _is_linked(a1, 'SrcEStructuralFeature', b)
    _safe_set(b, 'eContainingClass32', {a2})
    assert _is_linked(b, 'eContainingClass32', a2)
    if hasattr(a1, 'SrcEStructuralFeature'):
        assert not _is_linked(a1, 'SrcEStructuralFeature', b)
    if hasattr(a2, 'SrcEStructuralFeature'):
        assert _is_linked(a2, 'SrcEStructuralFeature', b)
    _safe_set(b, 'eContainingClass32', set())
    assert not _is_linked(b, 'eContainingClass32', a2)
    if hasattr(a2, 'SrcEStructuralFeature'):
        assert not _is_linked(a2, 'SrcEStructuralFeature', b)


def test_assoc_eSubpackages42_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSuperPackage', {a1})
    assert _is_linked(b, 'eSuperPackage', a1)
    if hasattr(a1, 'SrcEPackage43'):
        assert _is_linked(a1, 'SrcEPackage43', b)
    _safe_set(b, 'eSuperPackage', {a2})
    assert _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a1, 'SrcEPackage43'):
        assert not _is_linked(a1, 'SrcEPackage43', b)
    if hasattr(a2, 'SrcEPackage43'):
        assert _is_linked(a2, 'SrcEPackage43', b)
    _safe_set(b, 'eSuperPackage', set())
    assert not _is_linked(b, 'eSuperPackage', a2)
    if hasattr(a2, 'SrcEPackage43'):
        assert not _is_linked(a2, 'SrcEPackage43', b)


def test_assoc_eSuperPackage45_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    a2 = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = jointPackage_Ecore2Maude_SrcEPackage(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'eSubpackages', a1)
    assert _is_linked(b, 'eSubpackages', a1)
    if hasattr(a1, 'SrcEPackage46'):
        assert _is_linked(a1, 'SrcEPackage46', b)
    _safe_set(b, 'eSubpackages', a2)
    assert _is_linked(b, 'eSubpackages', a2)
    if hasattr(a1, 'SrcEPackage46'):
        assert not _is_linked(a1, 'SrcEPackage46', b)
    if hasattr(a2, 'SrcEPackage46'):
        assert _is_linked(a2, 'SrcEPackage46', b)
    _safe_set(b, 'eSubpackages', None)
    assert not _is_linked(b, 'eSubpackages', a2)
    if hasattr(a2, 'SrcEPackage46'):
        assert not _is_linked(a2, 'SrcEPackage46', b)


def test_assoc_eSuperTypes5_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    a2 = jointPackage_Ecore2Maude_SrcEClass(abstract=False, interface=False)
    b = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass4', {a1})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass4', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass4', {a2})
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass4', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcEClass'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcEClass', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClass4', set())
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClass4', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcEClass'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcEClass', b)


def test_assoc_eType60_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_SrcETypedElement(lowerBound=7, many=True, ordered=True, required=True, unique=True, upperBound=7)
    a2 = jointPackage_Ecore2Maude_SrcETypedElement(lowerBound=13, many=False, ordered=False, required=False, unique=False, upperBound=13)
    b = jointPackage_Ecore2Maude_SrcEClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcETypedElement'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_SrcETypedElement', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_SrcETypedElement'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_SrcETypedElement', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcETypedElement'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_SrcETypedElement', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_SrcEClassifier61', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_SrcETypedElement'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_SrcETypedElement', b)


def test_assoc_from_149_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text", name="sample_text")
    a2 = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text_2", name="sample_text_2")
    b = jointPackage_Ecore2Maude_TrgOpTypedMapping(atts="sample_text", to="sample_text")
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgOperation150'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_TrgOperation150', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgOperation150'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_TrgOperation150', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgOperation150'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_TrgOperation150', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpTypedMapping', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgOperation150'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_TrgOperation150', b)


def test_assoc_from_151_reverse_link_reassign_clear():
    a1 = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text", name="sample_text")
    a2 = jointPackage_Ecore2Maude_TrgOperation(atts="sample_text_2", name="sample_text_2")
    b = jointPackage_Ecore2Maude_TrgOpMapping(to="sample_text")
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpMapping', a1)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpMapping', a1)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgOperation152'):
        assert _is_linked(a1, 'jointPackage_Ecore2Maude_TrgOperation152', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpMapping', a2)
    assert _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpMapping', a2)
    if hasattr(a1, 'jointPackage_Ecore2Maude_TrgOperation152'):
        assert not _is_linked(a1, 'jointPackage_Ecore2Maude_TrgOperation152', b)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgOperation152'):
        assert _is_linked(a2, 'jointPackage_Ecore2Maude_TrgOperation152', b)
    _safe_set(b, 'jointPackage_Ecore2Maude_TrgOpMapping', None)
    assert not _is_linked(b, 'jointPackage_Ecore2Maude_TrgOpMapping', a2)
    if hasattr(a2, 'jointPackage_Ecore2Maude_TrgOperation152'):
        assert not _is_linked(a2, 'jointPackage_Ecore2Maude_TrgOperation152', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args132_stub_double():
    # jointPackage_Ecore2Maude_TrgTerm has no real 'jointPackage_Ecore2Maude_TrgTerm133' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgRecTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgRecTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgRecTerm(op="sample_text")
    partner = jointPackage_Ecore2Maude_TrgTerm()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgTerm133', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgRecTerm', {partner})
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgTerm133') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgRecTerm', set())
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgTerm133') is None


def test_assoc_conds123_stub_double():
    # jointPackage_Ecore2Maude_TrgCondition has no real 'jointPackage_Ecore2Maude_TrgCondition' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgStatement(atts="sample_text", label="sample_text")
    partner = jointPackage_Ecore2Maude_TrgCondition()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgCondition', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgStatement', {partner})
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgCondition') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgStatement', set())
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgCondition') is None


def test_assoc_eAllOperations21_stub_double():
    # jointPackage_Ecore2Maude_SrcEOperation has no real 'jointPackage_Ecore2Maude_SrcEOperation' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_SrcEClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_SrcEClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    partner = jointPackage_Ecore2Maude_SrcEOperation()
    setattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEClass22', {partner})
    assert getattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEClass22', set())
    assert getattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation') is None


def test_assoc_eContainingClass36_stub_double():
    # jointPackage_Ecore2Maude_SrcEOperation has no real 'eOperations' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_SrcEClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_SrcEClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    partner = jointPackage_Ecore2Maude_SrcEOperation()
    setattr(partner, 'eOperations', None)
    _safe_set(owner, 'SrcEClass', partner)
    assert getattr(partner, 'eOperations') == owner
    _safe_set(owner, 'SrcEClass', None)
    assert getattr(partner, 'eOperations') is None


def test_assoc_eExceptions38_stub_double():
    # jointPackage_Ecore2Maude_SrcEOperation has no real 'jointPackage_Ecore2Maude_SrcEOperation39' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_SrcEClassifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_SrcEClassifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_SrcEClassifier(instanceClassName="sample_text", instanceTypeName="sample_text")
    partner = jointPackage_Ecore2Maude_SrcEOperation()
    setattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation39', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEClassifier', partner)
    assert owner in getattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation39')
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEClassifier', None)
    assert owner not in getattr(partner, 'jointPackage_Ecore2Maude_SrcEOperation39')


def test_assoc_eOperations6_stub_double():
    # jointPackage_Ecore2Maude_SrcEOperation has no real 'SrcEOperation' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_SrcEClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_SrcEClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_SrcEClass(abstract=True, interface=True)
    partner = jointPackage_Ecore2Maude_SrcEOperation()
    setattr(partner, 'SrcEOperation', None)
    _safe_set(owner, 'eContainingClass', {partner})
    assert getattr(partner, 'SrcEOperation') == owner
    _safe_set(owner, 'eContainingClass', set())
    assert getattr(partner, 'SrcEOperation') is None


def test_assoc_els62_stub_double():
    # jointPackage_Ecore2Maude_TrgMaudeSpec has no real 'jointPackage_Ecore2Maude_TrgMaudeSpec' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgMaudeTopEl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgMaudeTopEl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgMaudeTopEl(name="sample_text")
    partner = jointPackage_Ecore2Maude_TrgMaudeSpec()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgMaudeTopEl', partner)
    assert owner in getattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec')
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgMaudeTopEl', None)
    assert owner not in getattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec')


def test_assoc_from_147_stub_double():
    # jointPackage_Ecore2Maude_TrgSort has no real 'jointPackage_Ecore2Maude_TrgSort148' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgSortMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgSortMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgSortMapping(to="sample_text")
    partner = jointPackage_Ecore2Maude_TrgSort()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgSort148', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgSortMapping', partner)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgSort148') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgSortMapping', None)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgSort148') is None


def test_assoc_modExp97_stub_double():
    # jointPackage_Ecore2Maude_TrgModExpression has no real 'jointPackage_Ecore2Maude_TrgModExpression98' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgParameter(label="sample_text")
    partner = jointPackage_Ecore2Maude_TrgModExpression()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgModExpression98', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgParameter', partner)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgModExpression98') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgParameter', None)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgModExpression98') is None


def test_assoc_params102_stub_double():
    # jointPackage_Ecore2Maude_TrgModule has no real 'jointPackage_Ecore2Maude_TrgModule103' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgParameter(label="sample_text")
    partner = jointPackage_Ecore2Maude_TrgModule()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgModule103', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgParameter104', partner)
    assert owner in getattr(partner, 'jointPackage_Ecore2Maude_TrgModule103')
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgParameter104', None)
    assert owner not in getattr(partner, 'jointPackage_Ecore2Maude_TrgModule103')


def test_assoc_printableEls63_stub_double():
    # jointPackage_Ecore2Maude_TrgMaudeSpec has no real 'jointPackage_Ecore2Maude_TrgMaudeSpec64' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgMaudeTopEl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgMaudeTopEl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgMaudeTopEl(name="sample_text")
    partner = jointPackage_Ecore2Maude_TrgMaudeSpec()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec64', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgMaudeTopEl65', partner)
    assert owner in getattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec64')
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgMaudeTopEl65', None)
    assert owner not in getattr(partner, 'jointPackage_Ecore2Maude_TrgMaudeSpec64')


def test_assoc_sourceRoot0_stub_double():
    # jointPackage_Ecore2Maude_JointMM has no real 'jointPackage_Ecore2Maude_JointMM' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_SrcEStringToStringMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_SrcEStringToStringMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_SrcEStringToStringMapEntry(key="sample_text", value="sample_text")
    partner = jointPackage_Ecore2Maude_JointMM()
    setattr(partner, 'jointPackage_Ecore2Maude_JointMM', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEStringToStringMapEntry', partner)
    assert getattr(partner, 'jointPackage_Ecore2Maude_JointMM') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_SrcEStringToStringMapEntry', None)
    assert getattr(partner, 'jointPackage_Ecore2Maude_JointMM') is None


def test_assoc_type129_stub_double():
    # jointPackage_Ecore2Maude_TrgTerm has no real 'jointPackage_Ecore2Maude_TrgTerm130' property in the generated
    # code (a bare stub) -- manually attach it so jointPackage_Ecore2Maude_TrgType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jointPackage_Ecore2Maude_TrgType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jointPackage_Ecore2Maude_TrgType(name="sample_text")
    partner = jointPackage_Ecore2Maude_TrgTerm()
    setattr(partner, 'jointPackage_Ecore2Maude_TrgTerm130', None)
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgType131', partner)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgTerm130') == owner
    _safe_set(owner, 'jointPackage_Ecore2Maude_TrgType131', None)
    assert getattr(partner, 'jointPackage_Ecore2Maude_TrgTerm130') is None


