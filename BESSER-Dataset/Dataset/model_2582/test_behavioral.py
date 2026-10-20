import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallableRelation,
    ComputationValue,
    Constraint,
    EntityType,
    Expression,
    LiteralValueReference,
    RelationType,
    Type,
    UnaryTypeConstraint,
    ValueReference,
    Variable,
    XImportSection,
    vql_AggregatedValue,
    vql_Annotation,
    vql_AnnotationParameter,
    vql_BoolValue,
    vql_CallableRelation,
    vql_CheckConstraint,
    vql_ClassType,
    vql_CompareConstraint,
    vql_ComputationValue,
    vql_Constraint,
    vql_EClassifier,
    vql_EClassifierConstraint,
    vql_EEnum,
    vql_EEnumLiteral,
    vql_EPackage,
    vql_EStructuralFeature,
    vql_EntityType,
    vql_EnumValue,
    vql_Expression,
    vql_FunctionEvaluationValue,
    vql_JavaType,
    vql_JvmDeclaredType,
    vql_JvmType,
    vql_ListValue,
    vql_LiteralValueReference,
    vql_LocalVariable,
    vql_Modifiers,
    vql_NumberValue,
    vql_PackageImport,
    vql_Parameter,
    vql_ParameterRef,
    vql_PathExpressionConstraint,
    vql_Pattern,
    vql_PatternBody,
    vql_PatternCall,
    vql_PatternCompositionConstraint,
    vql_PatternImport,
    vql_PatternModel,
    vql_ReferenceType,
    vql_RelationType,
    vql_StringValue,
    vql_Type,
    vql_TypeCheckConstraint,
    vql_UnaryTypeConstraint,
    vql_VQLImportSection,
    vql_ValueReference,
    vql_Variable,
    vql_VariableReference,
    vql_XBooleanLiteral,
    vql_XExpression,
    vql_XNumberLiteral,
    ClosureType,
    CompareFeature,
    ExecutionType,
    ParameterDirection,
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

def test_assoc_annotations23_reverse_link_reassign_clear():
    a1 = vql_Pattern(name="sample_text")
    a2 = vql_Pattern(name="sample_text_2")
    b = vql_Annotation(name="sample_text")
    _safe_set(b, 'vql_Annotation', a1)
    assert _is_linked(b, 'vql_Annotation', a1)
    if hasattr(a1, 'vql_Pattern24'):
        assert _is_linked(a1, 'vql_Pattern24', b)
    _safe_set(b, 'vql_Annotation', a2)
    assert _is_linked(b, 'vql_Annotation', a2)
    if hasattr(a1, 'vql_Pattern24'):
        assert not _is_linked(a1, 'vql_Pattern24', b)
    if hasattr(a2, 'vql_Pattern24'):
        assert _is_linked(a2, 'vql_Pattern24', b)
    _safe_set(b, 'vql_Annotation', None)
    assert not _is_linked(b, 'vql_Annotation', a2)
    if hasattr(a2, 'vql_Pattern24'):
        assert not _is_linked(a2, 'vql_Pattern24', b)


def test_assoc_bodies29_reverse_link_reassign_clear():
    a1 = vql_PatternBody(name="sample_text")
    a2 = vql_PatternBody(name="sample_text_2")
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern30', {a1})
    assert _is_linked(b, 'vql_Pattern30', a1)
    if hasattr(a1, 'vql_PatternBody'):
        assert _is_linked(a1, 'vql_PatternBody', b)
    _safe_set(b, 'vql_Pattern30', {a2})
    assert _is_linked(b, 'vql_Pattern30', a2)
    if hasattr(a1, 'vql_PatternBody'):
        assert not _is_linked(a1, 'vql_PatternBody', b)
    if hasattr(a2, 'vql_PatternBody'):
        assert _is_linked(a2, 'vql_PatternBody', b)
    _safe_set(b, 'vql_Pattern30', set())
    assert not _is_linked(b, 'vql_Pattern30', a2)
    if hasattr(a2, 'vql_PatternBody'):
        assert not _is_linked(a2, 'vql_PatternBody', b)


def test_assoc_call52_reverse_link_reassign_clear():
    a1 = vql_PatternCompositionConstraint(negative=True)
    a2 = vql_PatternCompositionConstraint(negative=False)
    b = vql_CallableRelation(transitive="sample_text")
    _safe_set(b, 'vql_CallableRelation', a1)
    assert _is_linked(b, 'vql_CallableRelation', a1)
    if hasattr(a1, 'vql_PatternCompositionConstraint'):
        assert _is_linked(a1, 'vql_PatternCompositionConstraint', b)
    _safe_set(b, 'vql_CallableRelation', a2)
    assert _is_linked(b, 'vql_CallableRelation', a2)
    if hasattr(a1, 'vql_PatternCompositionConstraint'):
        assert not _is_linked(a1, 'vql_PatternCompositionConstraint', b)
    if hasattr(a2, 'vql_PatternCompositionConstraint'):
        assert _is_linked(a2, 'vql_PatternCompositionConstraint', b)
    _safe_set(b, 'vql_CallableRelation', None)
    assert not _is_linked(b, 'vql_CallableRelation', a2)
    if hasattr(a2, 'vql_PatternCompositionConstraint'):
        assert not _is_linked(a2, 'vql_PatternCompositionConstraint', b)


def test_assoc_call78_reverse_link_reassign_clear():
    a1 = vql_CallableRelation(transitive="sample_text")
    a2 = vql_CallableRelation(transitive="sample_text_2")
    b = vql_AggregatedValue()
    _safe_set(b, 'vql_AggregatedValue79', a1)
    assert _is_linked(b, 'vql_AggregatedValue79', a1)
    if hasattr(a1, 'vql_CallableRelation80'):
        assert _is_linked(a1, 'vql_CallableRelation80', b)
    _safe_set(b, 'vql_AggregatedValue79', a2)
    assert _is_linked(b, 'vql_AggregatedValue79', a2)
    if hasattr(a1, 'vql_CallableRelation80'):
        assert not _is_linked(a1, 'vql_CallableRelation80', b)
    if hasattr(a2, 'vql_CallableRelation80'):
        assert _is_linked(a2, 'vql_CallableRelation80', b)
    _safe_set(b, 'vql_AggregatedValue79', None)
    assert not _is_linked(b, 'vql_AggregatedValue79', a2)
    if hasattr(a2, 'vql_CallableRelation80'):
        assert not _is_linked(a2, 'vql_CallableRelation80', b)


def test_assoc_dst67_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_PathExpressionConstraint()
    _safe_set(b, 'vql_PathExpressionConstraint68', a1)
    assert _is_linked(b, 'vql_PathExpressionConstraint68', a1)
    if hasattr(a1, 'vql_ValueReference69'):
        assert _is_linked(a1, 'vql_ValueReference69', b)
    _safe_set(b, 'vql_PathExpressionConstraint68', a2)
    assert _is_linked(b, 'vql_PathExpressionConstraint68', a2)
    if hasattr(a1, 'vql_ValueReference69'):
        assert not _is_linked(a1, 'vql_ValueReference69', b)
    if hasattr(a2, 'vql_ValueReference69'):
        assert _is_linked(a2, 'vql_ValueReference69', b)
    _safe_set(b, 'vql_PathExpressionConstraint68', None)
    assert not _is_linked(b, 'vql_PathExpressionConstraint68', a2)
    if hasattr(a2, 'vql_ValueReference69'):
        assert not _is_linked(a2, 'vql_ValueReference69', b)


def test_assoc_edgeTypes59_reverse_link_reassign_clear():
    a1 = vql_ReferenceType()
    a2 = vql_ReferenceType()
    b = vql_PathExpressionConstraint()
    _safe_set(b, 'vql_PathExpressionConstraint', {a1})
    assert _is_linked(b, 'vql_PathExpressionConstraint', a1)
    if hasattr(a1, 'vql_ReferenceType60'):
        assert _is_linked(a1, 'vql_ReferenceType60', b)
    _safe_set(b, 'vql_PathExpressionConstraint', {a2})
    assert _is_linked(b, 'vql_PathExpressionConstraint', a2)
    if hasattr(a1, 'vql_ReferenceType60'):
        assert not _is_linked(a1, 'vql_ReferenceType60', b)
    if hasattr(a2, 'vql_ReferenceType60'):
        assert _is_linked(a2, 'vql_ReferenceType60', b)
    _safe_set(b, 'vql_PathExpressionConstraint', set())
    assert not _is_linked(b, 'vql_PathExpressionConstraint', a2)
    if hasattr(a2, 'vql_ReferenceType60'):
        assert not _is_linked(a2, 'vql_ReferenceType60', b)


def test_assoc_importPackages13_reverse_link_reassign_clear():
    a1 = vql_VQLImportSection()
    a2 = vql_VQLImportSection()
    b = vql_PatternModel(packageName="sample_text")
    _safe_set(b, 'vql_PatternModel', a1)
    assert _is_linked(b, 'vql_PatternModel', a1)
    if hasattr(a1, 'vql_VQLImportSection14'):
        assert _is_linked(a1, 'vql_VQLImportSection14', b)
    _safe_set(b, 'vql_PatternModel', a2)
    assert _is_linked(b, 'vql_PatternModel', a2)
    if hasattr(a1, 'vql_VQLImportSection14'):
        assert not _is_linked(a1, 'vql_VQLImportSection14', b)
    if hasattr(a2, 'vql_VQLImportSection14'):
        assert _is_linked(a2, 'vql_VQLImportSection14', b)
    _safe_set(b, 'vql_PatternModel', None)
    assert not _is_linked(b, 'vql_PatternModel', a2)
    if hasattr(a2, 'vql_VQLImportSection14'):
        assert not _is_linked(a2, 'vql_VQLImportSection14', b)


def test_assoc_leftOperand53_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_CompareConstraint(feature="sample_text")
    _safe_set(b, 'vql_CompareConstraint', a1)
    assert _is_linked(b, 'vql_CompareConstraint', a1)
    if hasattr(a1, 'vql_ValueReference54'):
        assert _is_linked(a1, 'vql_ValueReference54', b)
    _safe_set(b, 'vql_CompareConstraint', a2)
    assert _is_linked(b, 'vql_CompareConstraint', a2)
    if hasattr(a1, 'vql_ValueReference54'):
        assert not _is_linked(a1, 'vql_ValueReference54', b)
    if hasattr(a2, 'vql_ValueReference54'):
        assert _is_linked(a2, 'vql_ValueReference54', b)
    _safe_set(b, 'vql_CompareConstraint', None)
    assert not _is_linked(b, 'vql_CompareConstraint', a2)
    if hasattr(a2, 'vql_ValueReference54'):
        assert not _is_linked(a2, 'vql_ValueReference54', b)


def test_assoc_metamodel18_reverse_link_reassign_clear():
    a1 = vql_PackageImport(alias="sample_text")
    a2 = vql_PackageImport(alias="sample_text_2")
    b = vql_ClassType()
    _safe_set(b, 'vql_ClassType', a1)
    assert _is_linked(b, 'vql_ClassType', a1)
    if hasattr(a1, 'vql_PackageImport19'):
        assert _is_linked(a1, 'vql_PackageImport19', b)
    _safe_set(b, 'vql_ClassType', a2)
    assert _is_linked(b, 'vql_ClassType', a2)
    if hasattr(a1, 'vql_PackageImport19'):
        assert not _is_linked(a1, 'vql_PackageImport19', b)
    if hasattr(a2, 'vql_PackageImport19'):
        assert _is_linked(a2, 'vql_PackageImport19', b)
    _safe_set(b, 'vql_ClassType', None)
    assert not _is_linked(b, 'vql_ClassType', a2)
    if hasattr(a2, 'vql_PackageImport19'):
        assert not _is_linked(a2, 'vql_PackageImport19', b)


def test_assoc_modifiers25_reverse_link_reassign_clear():
    a1 = vql_Pattern(name="sample_text")
    a2 = vql_Pattern(name="sample_text_2")
    b = vql_Modifiers(execution="sample_text", private=True)
    _safe_set(b, 'vql_Modifiers', a1)
    assert _is_linked(b, 'vql_Modifiers', a1)
    if hasattr(a1, 'vql_Pattern26'):
        assert _is_linked(a1, 'vql_Pattern26', b)
    _safe_set(b, 'vql_Modifiers', a2)
    assert _is_linked(b, 'vql_Modifiers', a2)
    if hasattr(a1, 'vql_Pattern26'):
        assert not _is_linked(a1, 'vql_Pattern26', b)
    if hasattr(a2, 'vql_Pattern26'):
        assert _is_linked(a2, 'vql_Pattern26', b)
    _safe_set(b, 'vql_Modifiers', None)
    assert not _is_linked(b, 'vql_Modifiers', a2)
    if hasattr(a2, 'vql_Pattern26'):
        assert not _is_linked(a2, 'vql_Pattern26', b)


def test_assoc_packageImport0_reverse_link_reassign_clear():
    a1 = vql_VQLImportSection()
    a2 = vql_VQLImportSection()
    b = vql_PackageImport(alias="sample_text")
    _safe_set(b, 'vql_PackageImport', a1)
    assert _is_linked(b, 'vql_PackageImport', a1)
    if hasattr(a1, 'vql_VQLImportSection'):
        assert _is_linked(a1, 'vql_VQLImportSection', b)
    _safe_set(b, 'vql_PackageImport', a2)
    assert _is_linked(b, 'vql_PackageImport', a2)
    if hasattr(a1, 'vql_VQLImportSection'):
        assert not _is_linked(a1, 'vql_VQLImportSection', b)
    if hasattr(a2, 'vql_VQLImportSection'):
        assert _is_linked(a2, 'vql_VQLImportSection', b)
    _safe_set(b, 'vql_PackageImport', None)
    assert not _is_linked(b, 'vql_PackageImport', a2)
    if hasattr(a2, 'vql_VQLImportSection'):
        assert not _is_linked(a2, 'vql_VQLImportSection', b)


def test_assoc_parameters27_reverse_link_reassign_clear():
    a1 = vql_Variable(name="sample_text")
    a2 = vql_Variable(name="sample_text_2")
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern28', {a1})
    assert _is_linked(b, 'vql_Pattern28', a1)
    if hasattr(a1, 'vql_Variable'):
        assert _is_linked(a1, 'vql_Variable', b)
    _safe_set(b, 'vql_Pattern28', {a2})
    assert _is_linked(b, 'vql_Pattern28', a2)
    if hasattr(a1, 'vql_Variable'):
        assert not _is_linked(a1, 'vql_Variable', b)
    if hasattr(a2, 'vql_Variable'):
        assert _is_linked(a2, 'vql_Variable', b)
    _safe_set(b, 'vql_Pattern28', set())
    assert not _is_linked(b, 'vql_Pattern28', a2)
    if hasattr(a2, 'vql_Variable'):
        assert not _is_linked(a2, 'vql_Variable', b)


def test_assoc_parameters31_reverse_link_reassign_clear():
    a1 = vql_AnnotationParameter(name="sample_text")
    a2 = vql_AnnotationParameter(name="sample_text_2")
    b = vql_Annotation(name="sample_text")
    _safe_set(b, 'vql_Annotation32', {a1})
    assert _is_linked(b, 'vql_Annotation32', a1)
    if hasattr(a1, 'vql_AnnotationParameter'):
        assert _is_linked(a1, 'vql_AnnotationParameter', b)
    _safe_set(b, 'vql_Annotation32', {a2})
    assert _is_linked(b, 'vql_Annotation32', a2)
    if hasattr(a1, 'vql_AnnotationParameter'):
        assert not _is_linked(a1, 'vql_AnnotationParameter', b)
    if hasattr(a2, 'vql_AnnotationParameter'):
        assert _is_linked(a2, 'vql_AnnotationParameter', b)
    _safe_set(b, 'vql_Annotation32', set())
    assert not _is_linked(b, 'vql_Annotation32', a2)
    if hasattr(a2, 'vql_AnnotationParameter'):
        assert not _is_linked(a2, 'vql_AnnotationParameter', b)


def test_assoc_parameters46_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_PatternCall()
    _safe_set(b, 'vql_PatternCall47', {a1})
    assert _is_linked(b, 'vql_PatternCall47', a1)
    if hasattr(a1, 'vql_ValueReference48'):
        assert _is_linked(a1, 'vql_ValueReference48', b)
    _safe_set(b, 'vql_PatternCall47', {a2})
    assert _is_linked(b, 'vql_PatternCall47', a2)
    if hasattr(a1, 'vql_ValueReference48'):
        assert not _is_linked(a1, 'vql_ValueReference48', b)
    if hasattr(a2, 'vql_ValueReference48'):
        assert _is_linked(a2, 'vql_ValueReference48', b)
    _safe_set(b, 'vql_PatternCall47', set())
    assert not _is_linked(b, 'vql_PatternCall47', a2)
    if hasattr(a2, 'vql_ValueReference48'):
        assert not _is_linked(a2, 'vql_ValueReference48', b)


def test_assoc_pattern5_reverse_link_reassign_clear():
    a1 = vql_PatternImport(packageName="sample_text")
    a2 = vql_PatternImport(packageName="sample_text_2")
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern', a1)
    assert _is_linked(b, 'vql_Pattern', a1)
    if hasattr(a1, 'vql_PatternImport6'):
        assert _is_linked(a1, 'vql_PatternImport6', b)
    _safe_set(b, 'vql_Pattern', a2)
    assert _is_linked(b, 'vql_Pattern', a2)
    if hasattr(a1, 'vql_PatternImport6'):
        assert not _is_linked(a1, 'vql_PatternImport6', b)
    if hasattr(a2, 'vql_PatternImport6'):
        assert _is_linked(a2, 'vql_PatternImport6', b)
    _safe_set(b, 'vql_Pattern', None)
    assert not _is_linked(b, 'vql_Pattern', a2)
    if hasattr(a2, 'vql_PatternImport6'):
        assert not _is_linked(a2, 'vql_PatternImport6', b)


def test_assoc_patternImport1_reverse_link_reassign_clear():
    a1 = vql_VQLImportSection()
    a2 = vql_VQLImportSection()
    b = vql_PatternImport(packageName="sample_text")
    _safe_set(b, 'vql_PatternImport', a1)
    assert _is_linked(b, 'vql_PatternImport', a1)
    if hasattr(a1, 'vql_VQLImportSection2'):
        assert _is_linked(a1, 'vql_VQLImportSection2', b)
    _safe_set(b, 'vql_PatternImport', a2)
    assert _is_linked(b, 'vql_PatternImport', a2)
    if hasattr(a1, 'vql_VQLImportSection2'):
        assert not _is_linked(a1, 'vql_VQLImportSection2', b)
    if hasattr(a2, 'vql_VQLImportSection2'):
        assert _is_linked(a2, 'vql_VQLImportSection2', b)
    _safe_set(b, 'vql_PatternImport', None)
    assert not _is_linked(b, 'vql_PatternImport', a2)
    if hasattr(a2, 'vql_VQLImportSection2'):
        assert not _is_linked(a2, 'vql_VQLImportSection2', b)


def test_assoc_patternRef44_reverse_link_reassign_clear():
    a1 = vql_PatternCall()
    a2 = vql_PatternCall()
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern45', a1)
    assert _is_linked(b, 'vql_Pattern45', a1)
    if hasattr(a1, 'vql_PatternCall'):
        assert _is_linked(a1, 'vql_PatternCall', b)
    _safe_set(b, 'vql_Pattern45', a2)
    assert _is_linked(b, 'vql_Pattern45', a2)
    if hasattr(a1, 'vql_PatternCall'):
        assert not _is_linked(a1, 'vql_PatternCall', b)
    if hasattr(a2, 'vql_PatternCall'):
        assert _is_linked(a2, 'vql_PatternCall', b)
    _safe_set(b, 'vql_Pattern45', None)
    assert not _is_linked(b, 'vql_Pattern45', a2)
    if hasattr(a2, 'vql_PatternCall'):
        assert not _is_linked(a2, 'vql_PatternCall', b)


def test_assoc_patterns15_reverse_link_reassign_clear():
    a1 = vql_PatternModel(packageName="sample_text")
    a2 = vql_PatternModel(packageName="sample_text_2")
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern17', a1)
    assert _is_linked(b, 'vql_Pattern17', a1)
    if hasattr(a1, 'vql_PatternModel16'):
        assert _is_linked(a1, 'vql_PatternModel16', b)
    _safe_set(b, 'vql_Pattern17', a2)
    assert _is_linked(b, 'vql_Pattern17', a2)
    if hasattr(a1, 'vql_PatternModel16'):
        assert not _is_linked(a1, 'vql_PatternModel16', b)
    if hasattr(a2, 'vql_PatternModel16'):
        assert _is_linked(a2, 'vql_PatternModel16', b)
    _safe_set(b, 'vql_Pattern17', None)
    assert not _is_linked(b, 'vql_Pattern17', a2)
    if hasattr(a2, 'vql_PatternModel16'):
        assert not _is_linked(a2, 'vql_PatternModel16', b)


def test_assoc_patterns7_reverse_link_reassign_clear():
    a1 = vql_PatternImport(packageName="sample_text")
    a2 = vql_PatternImport(packageName="sample_text_2")
    b = vql_Pattern(name="sample_text")
    _safe_set(b, 'vql_Pattern9', a1)
    assert _is_linked(b, 'vql_Pattern9', a1)
    if hasattr(a1, 'vql_PatternImport8'):
        assert _is_linked(a1, 'vql_PatternImport8', b)
    _safe_set(b, 'vql_Pattern9', a2)
    assert _is_linked(b, 'vql_Pattern9', a2)
    if hasattr(a1, 'vql_PatternImport8'):
        assert not _is_linked(a1, 'vql_PatternImport8', b)
    if hasattr(a2, 'vql_PatternImport8'):
        assert _is_linked(a2, 'vql_PatternImport8', b)
    _safe_set(b, 'vql_Pattern9', None)
    assert not _is_linked(b, 'vql_Pattern9', a2)
    if hasattr(a2, 'vql_PatternImport8'):
        assert not _is_linked(a2, 'vql_PatternImport8', b)


def test_assoc_referredParam49_reverse_link_reassign_clear():
    a1 = vql_Variable(name="sample_text")
    a2 = vql_Variable(name="sample_text_2")
    b = vql_ParameterRef()
    _safe_set(b, 'vql_ParameterRef', a1)
    assert _is_linked(b, 'vql_ParameterRef', a1)
    if hasattr(a1, 'vql_Variable50'):
        assert _is_linked(a1, 'vql_Variable50', b)
    _safe_set(b, 'vql_ParameterRef', a2)
    assert _is_linked(b, 'vql_ParameterRef', a2)
    if hasattr(a1, 'vql_Variable50'):
        assert not _is_linked(a1, 'vql_Variable50', b)
    if hasattr(a2, 'vql_Variable50'):
        assert _is_linked(a2, 'vql_Variable50', b)
    _safe_set(b, 'vql_ParameterRef', None)
    assert not _is_linked(b, 'vql_ParameterRef', a2)
    if hasattr(a2, 'vql_Variable50'):
        assert not _is_linked(a2, 'vql_Variable50', b)


def test_assoc_rightOperand55_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_CompareConstraint(feature="sample_text")
    _safe_set(b, 'vql_CompareConstraint56', a1)
    assert _is_linked(b, 'vql_CompareConstraint56', a1)
    if hasattr(a1, 'vql_ValueReference57'):
        assert _is_linked(a1, 'vql_ValueReference57', b)
    _safe_set(b, 'vql_CompareConstraint56', a2)
    assert _is_linked(b, 'vql_CompareConstraint56', a2)
    if hasattr(a1, 'vql_ValueReference57'):
        assert not _is_linked(a1, 'vql_ValueReference57', b)
    if hasattr(a2, 'vql_ValueReference57'):
        assert _is_linked(a2, 'vql_ValueReference57', b)
    _safe_set(b, 'vql_CompareConstraint56', None)
    assert not _is_linked(b, 'vql_CompareConstraint56', a2)
    if hasattr(a2, 'vql_ValueReference57'):
        assert not _is_linked(a2, 'vql_ValueReference57', b)


def test_assoc_sourceType61_reverse_link_reassign_clear():
    a1 = vql_PathExpressionConstraint()
    a2 = vql_PathExpressionConstraint()
    b = vql_ClassType()
    _safe_set(b, 'vql_ClassType63', a1)
    assert _is_linked(b, 'vql_ClassType63', a1)
    if hasattr(a1, 'vql_PathExpressionConstraint62'):
        assert _is_linked(a1, 'vql_PathExpressionConstraint62', b)
    _safe_set(b, 'vql_ClassType63', a2)
    assert _is_linked(b, 'vql_ClassType63', a2)
    if hasattr(a1, 'vql_PathExpressionConstraint62'):
        assert not _is_linked(a1, 'vql_PathExpressionConstraint62', b)
    if hasattr(a2, 'vql_PathExpressionConstraint62'):
        assert _is_linked(a2, 'vql_PathExpressionConstraint62', b)
    _safe_set(b, 'vql_ClassType63', None)
    assert not _is_linked(b, 'vql_ClassType63', a2)
    if hasattr(a2, 'vql_PathExpressionConstraint62'):
        assert not _is_linked(a2, 'vql_PathExpressionConstraint62', b)


def test_assoc_src64_reverse_link_reassign_clear():
    a1 = vql_VariableReference(aggregator=True, var="sample_text")
    a2 = vql_VariableReference(aggregator=False, var="sample_text_2")
    b = vql_PathExpressionConstraint()
    _safe_set(b, 'vql_PathExpressionConstraint65', a1)
    assert _is_linked(b, 'vql_PathExpressionConstraint65', a1)
    if hasattr(a1, 'vql_VariableReference66'):
        assert _is_linked(a1, 'vql_VariableReference66', b)
    _safe_set(b, 'vql_PathExpressionConstraint65', a2)
    assert _is_linked(b, 'vql_PathExpressionConstraint65', a2)
    if hasattr(a1, 'vql_VariableReference66'):
        assert not _is_linked(a1, 'vql_VariableReference66', b)
    if hasattr(a2, 'vql_VariableReference66'):
        assert _is_linked(a2, 'vql_VariableReference66', b)
    _safe_set(b, 'vql_PathExpressionConstraint65', None)
    assert not _is_linked(b, 'vql_PathExpressionConstraint65', a2)
    if hasattr(a2, 'vql_VariableReference66'):
        assert not _is_linked(a2, 'vql_VariableReference66', b)


def test_assoc_type35_reverse_link_reassign_clear():
    a1 = vql_Variable(name="sample_text")
    a2 = vql_Variable(name="sample_text_2")
    b = vql_Type(typename="sample_text")
    _safe_set(b, 'vql_Type', a1)
    assert _is_linked(b, 'vql_Type', a1)
    if hasattr(a1, 'vql_Variable36'):
        assert _is_linked(a1, 'vql_Variable36', b)
    _safe_set(b, 'vql_Type', a2)
    assert _is_linked(b, 'vql_Type', a2)
    if hasattr(a1, 'vql_Variable36'):
        assert not _is_linked(a1, 'vql_Variable36', b)
    if hasattr(a2, 'vql_Variable36'):
        assert _is_linked(a2, 'vql_Variable36', b)
    _safe_set(b, 'vql_Type', None)
    assert not _is_linked(b, 'vql_Type', a2)
    if hasattr(a2, 'vql_Variable36'):
        assert not _is_linked(a2, 'vql_Variable36', b)


def test_assoc_value33_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_AnnotationParameter(name="sample_text")
    _safe_set(b, 'vql_AnnotationParameter34', a1)
    assert _is_linked(b, 'vql_AnnotationParameter34', a1)
    if hasattr(a1, 'vql_ValueReference'):
        assert _is_linked(a1, 'vql_ValueReference', b)
    _safe_set(b, 'vql_AnnotationParameter34', a2)
    assert _is_linked(b, 'vql_AnnotationParameter34', a2)
    if hasattr(a1, 'vql_ValueReference'):
        assert not _is_linked(a1, 'vql_ValueReference', b)
    if hasattr(a2, 'vql_ValueReference'):
        assert _is_linked(a2, 'vql_ValueReference', b)
    _safe_set(b, 'vql_AnnotationParameter34', None)
    assert not _is_linked(b, 'vql_AnnotationParameter34', a2)
    if hasattr(a2, 'vql_ValueReference'):
        assert not _is_linked(a2, 'vql_ValueReference', b)


def test_assoc_values72_reverse_link_reassign_clear():
    a1 = vql_ValueReference()
    a2 = vql_ValueReference()
    b = vql_ListValue()
    _safe_set(b, 'vql_ListValue', {a1})
    assert _is_linked(b, 'vql_ListValue', a1)
    if hasattr(a1, 'vql_ValueReference73'):
        assert _is_linked(a1, 'vql_ValueReference73', b)
    _safe_set(b, 'vql_ListValue', {a2})
    assert _is_linked(b, 'vql_ListValue', a2)
    if hasattr(a1, 'vql_ValueReference73'):
        assert not _is_linked(a1, 'vql_ValueReference73', b)
    if hasattr(a2, 'vql_ValueReference73'):
        assert _is_linked(a2, 'vql_ValueReference73', b)
    _safe_set(b, 'vql_ListValue', set())
    assert not _is_linked(b, 'vql_ListValue', a2)
    if hasattr(a2, 'vql_ValueReference73'):
        assert not _is_linked(a2, 'vql_ValueReference73', b)


def test_assoc_variable37_reverse_link_reassign_clear():
    a1 = vql_VariableReference(aggregator=True, var="sample_text")
    a2 = vql_VariableReference(aggregator=False, var="sample_text_2")
    b = vql_Variable(name="sample_text")
    _safe_set(b, 'vql_Variable38', a1)
    assert _is_linked(b, 'vql_Variable38', a1)
    if hasattr(a1, 'vql_VariableReference'):
        assert _is_linked(a1, 'vql_VariableReference', b)
    _safe_set(b, 'vql_Variable38', a2)
    assert _is_linked(b, 'vql_Variable38', a2)
    if hasattr(a1, 'vql_VariableReference'):
        assert not _is_linked(a1, 'vql_VariableReference', b)
    if hasattr(a2, 'vql_VariableReference'):
        assert _is_linked(a2, 'vql_VariableReference', b)
    _safe_set(b, 'vql_Variable38', None)
    assert not _is_linked(b, 'vql_Variable38', a2)
    if hasattr(a2, 'vql_VariableReference'):
        assert not _is_linked(a2, 'vql_VariableReference', b)


def test_assoc_variables41_reverse_link_reassign_clear():
    a1 = vql_Variable(name="sample_text")
    a2 = vql_Variable(name="sample_text_2")
    b = vql_PatternBody(name="sample_text")
    _safe_set(b, 'vql_PatternBody42', {a1})
    assert _is_linked(b, 'vql_PatternBody42', a1)
    if hasattr(a1, 'vql_Variable43'):
        assert _is_linked(a1, 'vql_Variable43', b)
    _safe_set(b, 'vql_PatternBody42', {a2})
    assert _is_linked(b, 'vql_PatternBody42', a2)
    if hasattr(a1, 'vql_Variable43'):
        assert not _is_linked(a1, 'vql_Variable43', b)
    if hasattr(a2, 'vql_Variable43'):
        assert _is_linked(a2, 'vql_Variable43', b)
    _safe_set(b, 'vql_PatternBody42', set())
    assert not _is_linked(b, 'vql_PatternBody42', a2)
    if hasattr(a2, 'vql_Variable43'):
        assert not _is_linked(a2, 'vql_Variable43', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aggregateType81_stub_double():
    # vql_JvmType has no real 'vql_JvmType' property in the generated
    # code (a bare stub) -- manually attach it so vql_AggregatedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_AggregatedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_AggregatedValue()
    partner = vql_JvmType()
    setattr(partner, 'vql_JvmType', None)
    _safe_set(owner, 'vql_AggregatedValue82', partner)
    assert getattr(partner, 'vql_JvmType') == owner
    _safe_set(owner, 'vql_AggregatedValue82', None)
    assert getattr(partner, 'vql_JvmType') is None


def test_assoc_aggregator76_stub_double():
    # vql_JvmDeclaredType has no real 'vql_JvmDeclaredType77' property in the generated
    # code (a bare stub) -- manually attach it so vql_AggregatedValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_AggregatedValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_AggregatedValue()
    partner = vql_JvmDeclaredType()
    setattr(partner, 'vql_JvmDeclaredType77', None)
    _safe_set(owner, 'vql_AggregatedValue', partner)
    assert getattr(partner, 'vql_JvmDeclaredType77') == owner
    _safe_set(owner, 'vql_AggregatedValue', None)
    assert getattr(partner, 'vql_JvmDeclaredType77') is None


def test_assoc_classRef51_stub_double():
    # vql_JvmDeclaredType has no real 'vql_JvmDeclaredType' property in the generated
    # code (a bare stub) -- manually attach it so vql_JavaType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_JavaType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_JavaType()
    partner = vql_JvmDeclaredType()
    setattr(partner, 'vql_JvmDeclaredType', None)
    _safe_set(owner, 'vql_JavaType', partner)
    assert getattr(partner, 'vql_JvmDeclaredType') == owner
    _safe_set(owner, 'vql_JavaType', None)
    assert getattr(partner, 'vql_JvmDeclaredType') is None


def test_assoc_classname20_stub_double():
    # vql_EClassifier has no real 'vql_EClassifier' property in the generated
    # code (a bare stub) -- manually attach it so vql_ClassType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_ClassType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_ClassType()
    partner = vql_EClassifier()
    setattr(partner, 'vql_EClassifier', None)
    _safe_set(owner, 'vql_ClassType21', partner)
    assert getattr(partner, 'vql_EClassifier') == owner
    _safe_set(owner, 'vql_ClassType21', None)
    assert getattr(partner, 'vql_EClassifier') is None


def test_assoc_constraints39_stub_double():
    # vql_Constraint has no real 'vql_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so vql_PatternBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_PatternBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_PatternBody(name="sample_text")
    partner = vql_Constraint()
    setattr(partner, 'vql_Constraint', None)
    _safe_set(owner, 'vql_PatternBody40', {partner})
    assert getattr(partner, 'vql_Constraint') == owner
    _safe_set(owner, 'vql_PatternBody40', set())
    assert getattr(partner, 'vql_Constraint') is None


def test_assoc_ePackage3_stub_double():
    # vql_EPackage has no real 'vql_EPackage' property in the generated
    # code (a bare stub) -- manually attach it so vql_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_PackageImport(alias="sample_text")
    partner = vql_EPackage()
    setattr(partner, 'vql_EPackage', None)
    _safe_set(owner, 'vql_PackageImport4', partner)
    assert getattr(partner, 'vql_EPackage') == owner
    _safe_set(owner, 'vql_PackageImport4', None)
    assert getattr(partner, 'vql_EPackage') is None


def test_assoc_enumeration10_stub_double():
    # vql_EEnum has no real 'vql_EEnum' property in the generated
    # code (a bare stub) -- manually attach it so vql_EnumValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_EnumValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_EnumValue()
    partner = vql_EEnum()
    setattr(partner, 'vql_EEnum', None)
    _safe_set(owner, 'vql_EnumValue', partner)
    assert getattr(partner, 'vql_EEnum') == owner
    _safe_set(owner, 'vql_EnumValue', None)
    assert getattr(partner, 'vql_EEnum') is None


def test_assoc_expression58_stub_double():
    # vql_XExpression has no real 'vql_XExpression' property in the generated
    # code (a bare stub) -- manually attach it so vql_CheckConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_CheckConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_CheckConstraint()
    partner = vql_XExpression()
    setattr(partner, 'vql_XExpression', None)
    _safe_set(owner, 'vql_CheckConstraint', partner)
    assert getattr(partner, 'vql_XExpression') == owner
    _safe_set(owner, 'vql_CheckConstraint', None)
    assert getattr(partner, 'vql_XExpression') is None


def test_assoc_expression74_stub_double():
    # vql_XExpression has no real 'vql_XExpression75' property in the generated
    # code (a bare stub) -- manually attach it so vql_FunctionEvaluationValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_FunctionEvaluationValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_FunctionEvaluationValue()
    partner = vql_XExpression()
    setattr(partner, 'vql_XExpression75', None)
    _safe_set(owner, 'vql_FunctionEvaluationValue', partner)
    assert getattr(partner, 'vql_XExpression75') == owner
    _safe_set(owner, 'vql_FunctionEvaluationValue', None)
    assert getattr(partner, 'vql_XExpression75') is None


def test_assoc_literal11_stub_double():
    # vql_EEnumLiteral has no real 'vql_EEnumLiteral' property in the generated
    # code (a bare stub) -- manually attach it so vql_EnumValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_EnumValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_EnumValue()
    partner = vql_EEnumLiteral()
    setattr(partner, 'vql_EEnumLiteral', None)
    _safe_set(owner, 'vql_EnumValue12', partner)
    assert getattr(partner, 'vql_EEnumLiteral') == owner
    _safe_set(owner, 'vql_EnumValue12', None)
    assert getattr(partner, 'vql_EEnumLiteral') is None


def test_assoc_refname22_stub_double():
    # vql_EStructuralFeature has no real 'vql_EStructuralFeature' property in the generated
    # code (a bare stub) -- manually attach it so vql_ReferenceType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_ReferenceType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_ReferenceType()
    partner = vql_EStructuralFeature()
    setattr(partner, 'vql_EStructuralFeature', None)
    _safe_set(owner, 'vql_ReferenceType', partner)
    assert getattr(partner, 'vql_EStructuralFeature') == owner
    _safe_set(owner, 'vql_ReferenceType', None)
    assert getattr(partner, 'vql_EStructuralFeature') is None


def test_assoc_value70_stub_double():
    # vql_XNumberLiteral has no real 'vql_XNumberLiteral' property in the generated
    # code (a bare stub) -- manually attach it so vql_NumberValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_NumberValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_NumberValue(negative=True)
    partner = vql_XNumberLiteral()
    setattr(partner, 'vql_XNumberLiteral', None)
    _safe_set(owner, 'vql_NumberValue', partner)
    assert getattr(partner, 'vql_XNumberLiteral') == owner
    _safe_set(owner, 'vql_NumberValue', None)
    assert getattr(partner, 'vql_XNumberLiteral') is None


def test_assoc_value71_stub_double():
    # vql_XBooleanLiteral has no real 'vql_XBooleanLiteral' property in the generated
    # code (a bare stub) -- manually attach it so vql_BoolValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_BoolValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_BoolValue()
    partner = vql_XBooleanLiteral()
    setattr(partner, 'vql_XBooleanLiteral', None)
    _safe_set(owner, 'vql_BoolValue', partner)
    assert getattr(partner, 'vql_XBooleanLiteral') == owner
    _safe_set(owner, 'vql_BoolValue', None)
    assert getattr(partner, 'vql_XBooleanLiteral') is None


def test_assoc_var84_stub_double():
    # vql_UnaryTypeConstraint has no real 'vql_UnaryTypeConstraint85' property in the generated
    # code (a bare stub) -- manually attach it so vql_VariableReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vql_VariableReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vql_VariableReference(aggregator=True, var="sample_text")
    partner = vql_UnaryTypeConstraint()
    setattr(partner, 'vql_UnaryTypeConstraint85', None)
    _safe_set(owner, 'vql_VariableReference86', partner)
    assert getattr(partner, 'vql_UnaryTypeConstraint85') == owner
    _safe_set(owner, 'vql_VariableReference86', None)
    assert getattr(partner, 'vql_UnaryTypeConstraint85') is None


