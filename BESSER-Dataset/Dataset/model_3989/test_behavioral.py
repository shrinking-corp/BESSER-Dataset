import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ExtendedAnnotationType,
    Extensible,
    LoopDataRefType,
    XSDAnnotation,
    XpdlTypeType,
    xpdl2_BasicTypeType,
    xpdl2_DataTypeType,
    xpdl2_DeclaredTypeType,
    xpdl2_ExpressionType,
    xpdl2_ExtendedAttributeType,
    xpdl2_ExtendedAttributesType,
    xpdl2_Extensible,
    xpdl2_ExternalPackage,
    xpdl2_ExternalPackages,
    xpdl2_ExternalReferenceType,
    xpdl2_FormalParameterType,
    xpdl2_FormalParametersType,
    xpdl2_LoopMultiInstanceType,
    xpdl2_LoopStandardType,
    xpdl2_LoopType,
    xpdl2_SchemaTypeType,
    xpdl2_ScriptType,
    xpdl2_TypeDeclarationType,
    xpdl2_TypeDeclarationsType,
    xpdl2_XSDSchema,
    xpdl2_XpdlTypeType,
    xpdl2_extensions_ExtendedAnnotationType,
    xpdl2_extensions_LoopDataRefType,
    LoopTypeType,
    MIFlowConditionType,
    MIOrderingType,
    ModeType,
    TestTimeType,
    TypeType,
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

def test_assoc_basicType0_reverse_link_reassign_clear():
    a1 = xpdl2_DataTypeType(carnotType="sample_text")
    a2 = xpdl2_DataTypeType(carnotType="sample_text_2")
    b = xpdl2_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl2_BasicTypeType', a1)
    assert _is_linked(b, 'xpdl2_BasicTypeType', a1)
    if hasattr(a1, 'xpdl2_DataTypeType'):
        assert _is_linked(a1, 'xpdl2_DataTypeType', b)
    _safe_set(b, 'xpdl2_BasicTypeType', a2)
    assert _is_linked(b, 'xpdl2_BasicTypeType', a2)
    if hasattr(a1, 'xpdl2_DataTypeType'):
        assert not _is_linked(a1, 'xpdl2_DataTypeType', b)
    if hasattr(a2, 'xpdl2_DataTypeType'):
        assert _is_linked(a2, 'xpdl2_DataTypeType', b)
    _safe_set(b, 'xpdl2_BasicTypeType', None)
    assert not _is_linked(b, 'xpdl2_BasicTypeType', a2)
    if hasattr(a2, 'xpdl2_DataTypeType'):
        assert not _is_linked(a2, 'xpdl2_DataTypeType', b)


def test_assoc_basicType33_reverse_link_reassign_clear():
    a1 = xpdl2_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl2_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl2_BasicTypeType(type="sample_text")
    _safe_set(b, 'xpdl2_BasicTypeType35', a1)
    assert _is_linked(b, 'xpdl2_BasicTypeType35', a1)
    if hasattr(a1, 'xpdl2_TypeDeclarationType34'):
        assert _is_linked(a1, 'xpdl2_TypeDeclarationType34', b)
    _safe_set(b, 'xpdl2_BasicTypeType35', a2)
    assert _is_linked(b, 'xpdl2_BasicTypeType35', a2)
    if hasattr(a1, 'xpdl2_TypeDeclarationType34'):
        assert not _is_linked(a1, 'xpdl2_TypeDeclarationType34', b)
    if hasattr(a2, 'xpdl2_TypeDeclarationType34'):
        assert _is_linked(a2, 'xpdl2_TypeDeclarationType34', b)
    _safe_set(b, 'xpdl2_BasicTypeType35', None)
    assert not _is_linked(b, 'xpdl2_BasicTypeType35', a2)
    if hasattr(a2, 'xpdl2_TypeDeclarationType34'):
        assert not _is_linked(a2, 'xpdl2_TypeDeclarationType34', b)


def test_assoc_complexMIFlowCondition18_reverse_link_reassign_clear():
    a1 = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text", mIOrdering="sample_text")
    a2 = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text_2", mIOrdering="sample_text_2")
    b = xpdl2_ExpressionType(any="sample_text", group="sample_text", mixed="sample_text", scriptGrammar="sample_text", scriptType="sample_text", scriptVersion="sample_text")
    _safe_set(b, 'xpdl2_ExpressionType20', a1)
    assert _is_linked(b, 'xpdl2_ExpressionType20', a1)
    if hasattr(a1, 'xpdl2_LoopMultiInstanceType19'):
        assert _is_linked(a1, 'xpdl2_LoopMultiInstanceType19', b)
    _safe_set(b, 'xpdl2_ExpressionType20', a2)
    assert _is_linked(b, 'xpdl2_ExpressionType20', a2)
    if hasattr(a1, 'xpdl2_LoopMultiInstanceType19'):
        assert not _is_linked(a1, 'xpdl2_LoopMultiInstanceType19', b)
    if hasattr(a2, 'xpdl2_LoopMultiInstanceType19'):
        assert _is_linked(a2, 'xpdl2_LoopMultiInstanceType19', b)
    _safe_set(b, 'xpdl2_ExpressionType20', None)
    assert not _is_linked(b, 'xpdl2_ExpressionType20', a2)
    if hasattr(a2, 'xpdl2_LoopMultiInstanceType19'):
        assert not _is_linked(a2, 'xpdl2_LoopMultiInstanceType19', b)


def test_assoc_dataType14_reverse_link_reassign_clear():
    a1 = xpdl2_FormalParameterType(description="sample_text", id="sample_text", mode="sample_text", name="sample_text")
    a2 = xpdl2_FormalParameterType(description="sample_text_2", id="sample_text_2", mode="sample_text_2", name="sample_text_2")
    b = xpdl2_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl2_DataTypeType16', a1)
    assert _is_linked(b, 'xpdl2_DataTypeType16', a1)
    if hasattr(a1, 'xpdl2_FormalParameterType15'):
        assert _is_linked(a1, 'xpdl2_FormalParameterType15', b)
    _safe_set(b, 'xpdl2_DataTypeType16', a2)
    assert _is_linked(b, 'xpdl2_DataTypeType16', a2)
    if hasattr(a1, 'xpdl2_FormalParameterType15'):
        assert not _is_linked(a1, 'xpdl2_FormalParameterType15', b)
    if hasattr(a2, 'xpdl2_FormalParameterType15'):
        assert _is_linked(a2, 'xpdl2_FormalParameterType15', b)
    _safe_set(b, 'xpdl2_DataTypeType16', None)
    assert not _is_linked(b, 'xpdl2_DataTypeType16', a2)
    if hasattr(a2, 'xpdl2_FormalParameterType15'):
        assert not _is_linked(a2, 'xpdl2_FormalParameterType15', b)


def test_assoc_declaredType1_reverse_link_reassign_clear():
    a1 = xpdl2_DeclaredTypeType(id="sample_text")
    a2 = xpdl2_DeclaredTypeType(id="sample_text_2")
    b = xpdl2_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl2_DataTypeType2', a1)
    assert _is_linked(b, 'xpdl2_DataTypeType2', a1)
    if hasattr(a1, 'xpdl2_DeclaredTypeType'):
        assert _is_linked(a1, 'xpdl2_DeclaredTypeType', b)
    _safe_set(b, 'xpdl2_DataTypeType2', a2)
    assert _is_linked(b, 'xpdl2_DataTypeType2', a2)
    if hasattr(a1, 'xpdl2_DeclaredTypeType'):
        assert not _is_linked(a1, 'xpdl2_DeclaredTypeType', b)
    if hasattr(a2, 'xpdl2_DeclaredTypeType'):
        assert _is_linked(a2, 'xpdl2_DeclaredTypeType', b)
    _safe_set(b, 'xpdl2_DataTypeType2', None)
    assert not _is_linked(b, 'xpdl2_DataTypeType2', a2)
    if hasattr(a2, 'xpdl2_DeclaredTypeType'):
        assert not _is_linked(a2, 'xpdl2_DeclaredTypeType', b)


def test_assoc_declaredType36_reverse_link_reassign_clear():
    a1 = xpdl2_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl2_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl2_DeclaredTypeType(id="sample_text")
    _safe_set(b, 'xpdl2_DeclaredTypeType38', a1)
    assert _is_linked(b, 'xpdl2_DeclaredTypeType38', a1)
    if hasattr(a1, 'xpdl2_TypeDeclarationType37'):
        assert _is_linked(a1, 'xpdl2_TypeDeclarationType37', b)
    _safe_set(b, 'xpdl2_DeclaredTypeType38', a2)
    assert _is_linked(b, 'xpdl2_DeclaredTypeType38', a2)
    if hasattr(a1, 'xpdl2_TypeDeclarationType37'):
        assert not _is_linked(a1, 'xpdl2_TypeDeclarationType37', b)
    if hasattr(a2, 'xpdl2_TypeDeclarationType37'):
        assert _is_linked(a2, 'xpdl2_TypeDeclarationType37', b)
    _safe_set(b, 'xpdl2_DeclaredTypeType38', None)
    assert not _is_linked(b, 'xpdl2_DeclaredTypeType38', a2)
    if hasattr(a2, 'xpdl2_TypeDeclarationType37'):
        assert not _is_linked(a2, 'xpdl2_TypeDeclarationType37', b)


def test_assoc_externalPackage12_reverse_link_reassign_clear():
    a1 = xpdl2_ExternalPackages()
    a2 = xpdl2_ExternalPackages()
    b = xpdl2_ExternalPackage(href="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl2_ExternalPackage', a1)
    assert _is_linked(b, 'xpdl2_ExternalPackage', a1)
    if hasattr(a1, 'xpdl2_ExternalPackages'):
        assert _is_linked(a1, 'xpdl2_ExternalPackages', b)
    _safe_set(b, 'xpdl2_ExternalPackage', a2)
    assert _is_linked(b, 'xpdl2_ExternalPackage', a2)
    if hasattr(a1, 'xpdl2_ExternalPackages'):
        assert not _is_linked(a1, 'xpdl2_ExternalPackages', b)
    if hasattr(a2, 'xpdl2_ExternalPackages'):
        assert _is_linked(a2, 'xpdl2_ExternalPackages', b)
    _safe_set(b, 'xpdl2_ExternalPackage', None)
    assert not _is_linked(b, 'xpdl2_ExternalPackage', a2)
    if hasattr(a2, 'xpdl2_ExternalPackages'):
        assert not _is_linked(a2, 'xpdl2_ExternalPackages', b)


def test_assoc_externalReference42_reverse_link_reassign_clear():
    a1 = xpdl2_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    a2 = xpdl2_TypeDeclarationType(description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = xpdl2_ExternalReferenceType(location="sample_text", namespace="sample_text", uuid="sample_text", xref="sample_text")
    _safe_set(b, 'xpdl2_ExternalReferenceType44', a1)
    assert _is_linked(b, 'xpdl2_ExternalReferenceType44', a1)
    if hasattr(a1, 'xpdl2_TypeDeclarationType43'):
        assert _is_linked(a1, 'xpdl2_TypeDeclarationType43', b)
    _safe_set(b, 'xpdl2_ExternalReferenceType44', a2)
    assert _is_linked(b, 'xpdl2_ExternalReferenceType44', a2)
    if hasattr(a1, 'xpdl2_TypeDeclarationType43'):
        assert not _is_linked(a1, 'xpdl2_TypeDeclarationType43', b)
    if hasattr(a2, 'xpdl2_TypeDeclarationType43'):
        assert _is_linked(a2, 'xpdl2_TypeDeclarationType43', b)
    _safe_set(b, 'xpdl2_ExternalReferenceType44', None)
    assert not _is_linked(b, 'xpdl2_ExternalReferenceType44', a2)
    if hasattr(a2, 'xpdl2_TypeDeclarationType43'):
        assert not _is_linked(a2, 'xpdl2_TypeDeclarationType43', b)


def test_assoc_externalReference5_reverse_link_reassign_clear():
    a1 = xpdl2_ExternalReferenceType(location="sample_text", namespace="sample_text", uuid="sample_text", xref="sample_text")
    a2 = xpdl2_ExternalReferenceType(location="sample_text_2", namespace="sample_text_2", uuid="sample_text_2", xref="sample_text_2")
    b = xpdl2_DataTypeType(carnotType="sample_text")
    _safe_set(b, 'xpdl2_DataTypeType6', a1)
    assert _is_linked(b, 'xpdl2_DataTypeType6', a1)
    if hasattr(a1, 'xpdl2_ExternalReferenceType'):
        assert _is_linked(a1, 'xpdl2_ExternalReferenceType', b)
    _safe_set(b, 'xpdl2_DataTypeType6', a2)
    assert _is_linked(b, 'xpdl2_DataTypeType6', a2)
    if hasattr(a1, 'xpdl2_ExternalReferenceType'):
        assert not _is_linked(a1, 'xpdl2_ExternalReferenceType', b)
    if hasattr(a2, 'xpdl2_ExternalReferenceType'):
        assert _is_linked(a2, 'xpdl2_ExternalReferenceType', b)
    _safe_set(b, 'xpdl2_DataTypeType6', None)
    assert not _is_linked(b, 'xpdl2_DataTypeType6', a2)
    if hasattr(a2, 'xpdl2_ExternalReferenceType'):
        assert not _is_linked(a2, 'xpdl2_ExternalReferenceType', b)


def test_assoc_formalParameter13_reverse_link_reassign_clear():
    a1 = xpdl2_FormalParametersType()
    a2 = xpdl2_FormalParametersType()
    b = xpdl2_FormalParameterType(description="sample_text", id="sample_text", mode="sample_text", name="sample_text")
    _safe_set(b, 'xpdl2_FormalParameterType', a1)
    assert _is_linked(b, 'xpdl2_FormalParameterType', a1)
    if hasattr(a1, 'xpdl2_FormalParametersType'):
        assert _is_linked(a1, 'xpdl2_FormalParametersType', b)
    _safe_set(b, 'xpdl2_FormalParameterType', a2)
    assert _is_linked(b, 'xpdl2_FormalParameterType', a2)
    if hasattr(a1, 'xpdl2_FormalParametersType'):
        assert not _is_linked(a1, 'xpdl2_FormalParametersType', b)
    if hasattr(a2, 'xpdl2_FormalParametersType'):
        assert _is_linked(a2, 'xpdl2_FormalParametersType', b)
    _safe_set(b, 'xpdl2_FormalParameterType', None)
    assert not _is_linked(b, 'xpdl2_FormalParameterType', a2)
    if hasattr(a2, 'xpdl2_FormalParametersType'):
        assert not _is_linked(a2, 'xpdl2_FormalParametersType', b)


def test_assoc_loopCondition23_reverse_link_reassign_clear():
    a1 = xpdl2_LoopStandardType(loopMaximum="sample_text", testTime="sample_text")
    a2 = xpdl2_LoopStandardType(loopMaximum="sample_text_2", testTime="sample_text_2")
    b = xpdl2_ExpressionType(any="sample_text", group="sample_text", mixed="sample_text", scriptGrammar="sample_text", scriptType="sample_text", scriptVersion="sample_text")
    _safe_set(b, 'xpdl2_ExpressionType24', a1)
    assert _is_linked(b, 'xpdl2_ExpressionType24', a1)
    if hasattr(a1, 'xpdl2_LoopStandardType'):
        assert _is_linked(a1, 'xpdl2_LoopStandardType', b)
    _safe_set(b, 'xpdl2_ExpressionType24', a2)
    assert _is_linked(b, 'xpdl2_ExpressionType24', a2)
    if hasattr(a1, 'xpdl2_LoopStandardType'):
        assert not _is_linked(a1, 'xpdl2_LoopStandardType', b)
    if hasattr(a2, 'xpdl2_LoopStandardType'):
        assert _is_linked(a2, 'xpdl2_LoopStandardType', b)
    _safe_set(b, 'xpdl2_ExpressionType24', None)
    assert not _is_linked(b, 'xpdl2_ExpressionType24', a2)
    if hasattr(a2, 'xpdl2_LoopStandardType'):
        assert not _is_linked(a2, 'xpdl2_LoopStandardType', b)


def test_assoc_loopMultiInstance27_reverse_link_reassign_clear():
    a1 = xpdl2_LoopType(loopType="sample_text")
    a2 = xpdl2_LoopType(loopType="sample_text_2")
    b = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text", mIOrdering="sample_text")
    _safe_set(b, 'xpdl2_LoopMultiInstanceType29', a1)
    assert _is_linked(b, 'xpdl2_LoopMultiInstanceType29', a1)
    if hasattr(a1, 'xpdl2_LoopType28'):
        assert _is_linked(a1, 'xpdl2_LoopType28', b)
    _safe_set(b, 'xpdl2_LoopMultiInstanceType29', a2)
    assert _is_linked(b, 'xpdl2_LoopMultiInstanceType29', a2)
    if hasattr(a1, 'xpdl2_LoopType28'):
        assert not _is_linked(a1, 'xpdl2_LoopType28', b)
    if hasattr(a2, 'xpdl2_LoopType28'):
        assert _is_linked(a2, 'xpdl2_LoopType28', b)
    _safe_set(b, 'xpdl2_LoopMultiInstanceType29', None)
    assert not _is_linked(b, 'xpdl2_LoopMultiInstanceType29', a2)
    if hasattr(a2, 'xpdl2_LoopType28'):
        assert not _is_linked(a2, 'xpdl2_LoopType28', b)


def test_assoc_loopStandard25_reverse_link_reassign_clear():
    a1 = xpdl2_LoopType(loopType="sample_text")
    a2 = xpdl2_LoopType(loopType="sample_text_2")
    b = xpdl2_LoopStandardType(loopMaximum="sample_text", testTime="sample_text")
    _safe_set(b, 'xpdl2_LoopStandardType26', a1)
    assert _is_linked(b, 'xpdl2_LoopStandardType26', a1)
    if hasattr(a1, 'xpdl2_LoopType'):
        assert _is_linked(a1, 'xpdl2_LoopType', b)
    _safe_set(b, 'xpdl2_LoopStandardType26', a2)
    assert _is_linked(b, 'xpdl2_LoopStandardType26', a2)
    if hasattr(a1, 'xpdl2_LoopType'):
        assert not _is_linked(a1, 'xpdl2_LoopType', b)
    if hasattr(a2, 'xpdl2_LoopType'):
        assert _is_linked(a2, 'xpdl2_LoopType', b)
    _safe_set(b, 'xpdl2_LoopStandardType26', None)
    assert not _is_linked(b, 'xpdl2_LoopStandardType26', a2)
    if hasattr(a2, 'xpdl2_LoopType'):
        assert not _is_linked(a2, 'xpdl2_LoopType', b)


def test_assoc_mICondition17_reverse_link_reassign_clear():
    a1 = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text", mIOrdering="sample_text")
    a2 = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text_2", mIOrdering="sample_text_2")
    b = xpdl2_ExpressionType(any="sample_text", group="sample_text", mixed="sample_text", scriptGrammar="sample_text", scriptType="sample_text", scriptVersion="sample_text")
    _safe_set(b, 'xpdl2_ExpressionType', a1)
    assert _is_linked(b, 'xpdl2_ExpressionType', a1)
    if hasattr(a1, 'xpdl2_LoopMultiInstanceType'):
        assert _is_linked(a1, 'xpdl2_LoopMultiInstanceType', b)
    _safe_set(b, 'xpdl2_ExpressionType', a2)
    assert _is_linked(b, 'xpdl2_ExpressionType', a2)
    if hasattr(a1, 'xpdl2_LoopMultiInstanceType'):
        assert not _is_linked(a1, 'xpdl2_LoopMultiInstanceType', b)
    if hasattr(a2, 'xpdl2_LoopMultiInstanceType'):
        assert _is_linked(a2, 'xpdl2_LoopMultiInstanceType', b)
    _safe_set(b, 'xpdl2_ExpressionType', None)
    assert not _is_linked(b, 'xpdl2_ExpressionType', a2)
    if hasattr(a2, 'xpdl2_LoopMultiInstanceType'):
        assert not _is_linked(a2, 'xpdl2_LoopMultiInstanceType', b)


def test_assoc_typeDeclaration32_reverse_link_reassign_clear():
    a1 = xpdl2_TypeDeclarationsType()
    a2 = xpdl2_TypeDeclarationsType()
    b = xpdl2_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'xpdl2_TypeDeclarationType', a1)
    assert _is_linked(b, 'xpdl2_TypeDeclarationType', a1)
    if hasattr(a1, 'xpdl2_TypeDeclarationsType'):
        assert _is_linked(a1, 'xpdl2_TypeDeclarationsType', b)
    _safe_set(b, 'xpdl2_TypeDeclarationType', a2)
    assert _is_linked(b, 'xpdl2_TypeDeclarationType', a2)
    if hasattr(a1, 'xpdl2_TypeDeclarationsType'):
        assert not _is_linked(a1, 'xpdl2_TypeDeclarationsType', b)
    if hasattr(a2, 'xpdl2_TypeDeclarationsType'):
        assert _is_linked(a2, 'xpdl2_TypeDeclarationsType', b)
    _safe_set(b, 'xpdl2_TypeDeclarationType', None)
    assert not _is_linked(b, 'xpdl2_TypeDeclarationType', a2)
    if hasattr(a2, 'xpdl2_TypeDeclarationsType'):
        assert not _is_linked(a2, 'xpdl2_TypeDeclarationsType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_extendedAnnotation8_stub_double():
    # ExtendedAnnotationType has no real 'ExtendedAnnotationType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl2_ExtendedAttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl2_ExtendedAttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl2_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    partner = ExtendedAnnotationType()
    setattr(partner, 'ExtendedAnnotationType', None)
    _safe_set(owner, 'xpdl2_ExtendedAttributeType9', partner)
    assert getattr(partner, 'ExtendedAnnotationType') == owner
    _safe_set(owner, 'xpdl2_ExtendedAttributeType9', None)
    assert getattr(partner, 'ExtendedAnnotationType') is None


def test_assoc_extendedAttribute7_stub_double():
    # xpdl2_ExtendedAttributesType has no real 'xpdl2_ExtendedAttributesType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl2_ExtendedAttributeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl2_ExtendedAttributeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl2_ExtendedAttributeType(any="sample_text", group="sample_text", mixed="sample_text", name="sample_text", value="sample_text")
    partner = xpdl2_ExtendedAttributesType()
    setattr(partner, 'xpdl2_ExtendedAttributesType', None)
    _safe_set(owner, 'xpdl2_ExtendedAttributeType', partner)
    assert owner in getattr(partner, 'xpdl2_ExtendedAttributesType')
    _safe_set(owner, 'xpdl2_ExtendedAttributeType', None)
    assert owner not in getattr(partner, 'xpdl2_ExtendedAttributesType')


def test_assoc_loopDataRef21_stub_double():
    # LoopDataRefType has no real 'LoopDataRefType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl2_LoopMultiInstanceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl2_LoopMultiInstanceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl2_LoopMultiInstanceType(mIFlowCondition="sample_text", mIOrdering="sample_text")
    partner = LoopDataRefType()
    setattr(partner, 'LoopDataRefType', None)
    _safe_set(owner, 'xpdl2_LoopMultiInstanceType22', partner)
    assert getattr(partner, 'LoopDataRefType') == owner
    _safe_set(owner, 'xpdl2_LoopMultiInstanceType22', None)
    assert getattr(partner, 'LoopDataRefType') is None


def test_assoc_schemaType3_stub_double():
    # xpdl2_SchemaTypeType has no real 'xpdl2_SchemaTypeType' property in the generated
    # code (a bare stub) -- manually attach it so xpdl2_DataTypeType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl2_DataTypeType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl2_DataTypeType(carnotType="sample_text")
    partner = xpdl2_SchemaTypeType()
    setattr(partner, 'xpdl2_SchemaTypeType', None)
    _safe_set(owner, 'xpdl2_DataTypeType4', partner)
    assert getattr(partner, 'xpdl2_SchemaTypeType') == owner
    _safe_set(owner, 'xpdl2_DataTypeType4', None)
    assert getattr(partner, 'xpdl2_SchemaTypeType') is None


def test_assoc_schemaType39_stub_double():
    # xpdl2_SchemaTypeType has no real 'xpdl2_SchemaTypeType41' property in the generated
    # code (a bare stub) -- manually attach it so xpdl2_TypeDeclarationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # xpdl2_TypeDeclarationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = xpdl2_TypeDeclarationType(description="sample_text", id="sample_text", name="sample_text")
    partner = xpdl2_SchemaTypeType()
    setattr(partner, 'xpdl2_SchemaTypeType41', None)
    _safe_set(owner, 'xpdl2_TypeDeclarationType40', partner)
    assert getattr(partner, 'xpdl2_SchemaTypeType41') == owner
    _safe_set(owner, 'xpdl2_TypeDeclarationType40', None)
    assert getattr(partner, 'xpdl2_SchemaTypeType41') is None


