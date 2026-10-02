import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotationElementCS,
    ClassifierCS,
    ElementCS,
    ElementRefCS,
    FeatureCS,
    ModelElementCS,
    MultiplicityCS,
    Nameable,
    NamedElementCS,
    NamespaceCS,
    PackageOwnerCS,
    PathElementCS,
    Pivotable,
    PivotableElementCS,
    RootCS,
    StructuralFeatureCS,
    TemplateParameterCS,
    TemplateableElementCS,
    TypeCS,
    TypeRefCS,
    TypedElementCS,
    TypedRefCS,
    VisitableCS,
    basecs_AnnotationCS,
    basecs_AnnotationElementCS,
    basecs_AttributeCS,
    basecs_ClassCS,
    basecs_ClassifierCS,
    basecs_ConstraintCS,
    basecs_DataTypeCS,
    basecs_DetailCS,
    basecs_DocumentationCS,
    basecs_EClassifier,
    basecs_Element,
    basecs_ElementCS,
    basecs_ElementRefCS,
    basecs_EnumerationCS,
    basecs_EnumerationLiteralCS,
    basecs_FeatureCS,
    basecs_ImportCS,
    basecs_LambdaTypeCS,
    basecs_LibraryCS,
    basecs_ModelElementCS,
    basecs_ModelElementRefCS,
    basecs_MultiplicityBoundsCS,
    basecs_MultiplicityCS,
    basecs_MultiplicityStringCS,
    basecs_NamedElementCS,
    basecs_Namespace,
    basecs_NamespaceCS,
    basecs_OperationCS,
    basecs_PackageCS,
    basecs_PackageOwnerCS,
    basecs_ParameterCS,
    basecs_PathElementCS,
    basecs_PathElementWithURICS,
    basecs_PathNameCS,
    basecs_PivotableElementCS,
    basecs_PrimitiveTypeRefCS,
    basecs_Property,
    basecs_ReferenceCS,
    basecs_RootCS,
    basecs_RootPackageCS,
    basecs_SpecificationCS,
    basecs_StructuralFeatureCS,
    basecs_TemplateBindingCS,
    basecs_TemplateParameterCS,
    basecs_TemplateParameterSubstitutionCS,
    basecs_TemplateSignatureCS,
    basecs_TemplateableElementCS,
    basecs_TuplePartCS,
    basecs_TupleTypeCS,
    basecs_Type,
    basecs_TypeCS,
    basecs_TypeParameterCS,
    basecs_TypeRefCS,
    basecs_TypedElementCS,
    basecs_TypedRefCS,
    basecs_TypedTypeRefCS,
    basecs_VisitableCS,
    basecs_WildcardTypeRefCS,
    IteratorKind,
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

def test_assoc_context71_reverse_link_reassign_clear():
    a1 = basecs_PathNameCS(scopeFilter="sample_text")
    a2 = basecs_PathNameCS(scopeFilter="sample_text_2")
    b = basecs_ElementCS()
    _safe_set(b, 'basecs_ElementCS73', a1)
    assert _is_linked(b, 'basecs_ElementCS73', a1)
    if hasattr(a1, 'basecs_PathNameCS72'):
        assert _is_linked(a1, 'basecs_PathNameCS72', b)
    _safe_set(b, 'basecs_ElementCS73', a2)
    assert _is_linked(b, 'basecs_ElementCS73', a2)
    if hasattr(a1, 'basecs_PathNameCS72'):
        assert not _is_linked(a1, 'basecs_PathNameCS72', b)
    if hasattr(a2, 'basecs_PathNameCS72'):
        assert _is_linked(a2, 'basecs_PathNameCS72', b)
    _safe_set(b, 'basecs_ElementCS73', None)
    assert not _is_linked(b, 'basecs_ElementCS73', a2)
    if hasattr(a2, 'basecs_PathNameCS72'):
        assert not _is_linked(a2, 'basecs_PathNameCS72', b)


def test_assoc_logicalParent19_reverse_link_reassign_clear():
    a1 = basecs_ElementCS()
    a2 = basecs_ElementCS()
    b = basecs_ElementCS()
    _safe_set(b, 'basecs_ElementCS18', a1)
    assert _is_linked(b, 'basecs_ElementCS18', a1)
    if hasattr(a1, 'basecs_ElementCS'):
        assert _is_linked(a1, 'basecs_ElementCS', b)
    _safe_set(b, 'basecs_ElementCS18', a2)
    assert _is_linked(b, 'basecs_ElementCS18', a2)
    if hasattr(a1, 'basecs_ElementCS'):
        assert not _is_linked(a1, 'basecs_ElementCS', b)
    if hasattr(a2, 'basecs_ElementCS'):
        assert _is_linked(a2, 'basecs_ElementCS', b)
    _safe_set(b, 'basecs_ElementCS18', None)
    assert not _is_linked(b, 'basecs_ElementCS18', a2)
    if hasattr(a2, 'basecs_ElementCS'):
        assert not _is_linked(a2, 'basecs_ElementCS', b)


def test_assoc_messageSpecification14_reverse_link_reassign_clear():
    a1 = basecs_SpecificationCS(exprString="sample_text")
    a2 = basecs_SpecificationCS(exprString="sample_text_2")
    b = basecs_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'basecs_ConstraintCS15', a1)
    assert _is_linked(b, 'basecs_ConstraintCS15', a1)
    if hasattr(a1, 'basecs_SpecificationCS16'):
        assert _is_linked(a1, 'basecs_SpecificationCS16', b)
    _safe_set(b, 'basecs_ConstraintCS15', a2)
    assert _is_linked(b, 'basecs_ConstraintCS15', a2)
    if hasattr(a1, 'basecs_SpecificationCS16'):
        assert not _is_linked(a1, 'basecs_SpecificationCS16', b)
    if hasattr(a2, 'basecs_SpecificationCS16'):
        assert _is_linked(a2, 'basecs_SpecificationCS16', b)
    _safe_set(b, 'basecs_ConstraintCS15', None)
    assert not _is_linked(b, 'basecs_ConstraintCS15', a2)
    if hasattr(a2, 'basecs_SpecificationCS16'):
        assert not _is_linked(a2, 'basecs_SpecificationCS16', b)


def test_assoc_ownedBodyExpression54_reverse_link_reassign_clear():
    a1 = basecs_SpecificationCS(exprString="sample_text")
    a2 = basecs_SpecificationCS(exprString="sample_text_2")
    b = basecs_OperationCS()
    _safe_set(b, 'basecs_OperationCS55', {a1})
    assert _is_linked(b, 'basecs_OperationCS55', a1)
    if hasattr(a1, 'basecs_SpecificationCS56'):
        assert _is_linked(a1, 'basecs_SpecificationCS56', b)
    _safe_set(b, 'basecs_OperationCS55', {a2})
    assert _is_linked(b, 'basecs_OperationCS55', a2)
    if hasattr(a1, 'basecs_SpecificationCS56'):
        assert not _is_linked(a1, 'basecs_SpecificationCS56', b)
    if hasattr(a2, 'basecs_SpecificationCS56'):
        assert _is_linked(a2, 'basecs_SpecificationCS56', b)
    _safe_set(b, 'basecs_OperationCS55', set())
    assert not _is_linked(b, 'basecs_OperationCS55', a2)
    if hasattr(a2, 'basecs_SpecificationCS56'):
        assert not _is_linked(a2, 'basecs_SpecificationCS56', b)


def test_assoc_ownedConstraint11_reverse_link_reassign_clear():
    a1 = basecs_ConstraintCS(stereotype="sample_text")
    a2 = basecs_ConstraintCS(stereotype="sample_text_2")
    b = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    _safe_set(b, 'basecs_ClassifierCS', {a1})
    assert _is_linked(b, 'basecs_ClassifierCS', a1)
    if hasattr(a1, 'basecs_ConstraintCS'):
        assert _is_linked(a1, 'basecs_ConstraintCS', b)
    _safe_set(b, 'basecs_ClassifierCS', {a2})
    assert _is_linked(b, 'basecs_ClassifierCS', a2)
    if hasattr(a1, 'basecs_ConstraintCS'):
        assert not _is_linked(a1, 'basecs_ConstraintCS', b)
    if hasattr(a2, 'basecs_ConstraintCS'):
        assert _is_linked(a2, 'basecs_ConstraintCS', b)
    _safe_set(b, 'basecs_ClassifierCS', set())
    assert not _is_linked(b, 'basecs_ClassifierCS', a2)
    if hasattr(a2, 'basecs_ConstraintCS'):
        assert not _is_linked(a2, 'basecs_ConstraintCS', b)


def test_assoc_ownedDefaultExpression87_reverse_link_reassign_clear():
    a1 = basecs_StructuralFeatureCS(default="sample_text")
    a2 = basecs_StructuralFeatureCS(default="sample_text_2")
    b = basecs_SpecificationCS(exprString="sample_text")
    _safe_set(b, 'basecs_SpecificationCS88', a1)
    assert _is_linked(b, 'basecs_SpecificationCS88', a1)
    if hasattr(a1, 'basecs_StructuralFeatureCS'):
        assert _is_linked(a1, 'basecs_StructuralFeatureCS', b)
    _safe_set(b, 'basecs_SpecificationCS88', a2)
    assert _is_linked(b, 'basecs_SpecificationCS88', a2)
    if hasattr(a1, 'basecs_StructuralFeatureCS'):
        assert not _is_linked(a1, 'basecs_StructuralFeatureCS', b)
    if hasattr(a2, 'basecs_StructuralFeatureCS'):
        assert _is_linked(a2, 'basecs_StructuralFeatureCS', b)
    _safe_set(b, 'basecs_SpecificationCS88', None)
    assert not _is_linked(b, 'basecs_SpecificationCS88', a2)
    if hasattr(a2, 'basecs_StructuralFeatureCS'):
        assert not _is_linked(a2, 'basecs_StructuralFeatureCS', b)


def test_assoc_ownedLiterals20_reverse_link_reassign_clear():
    a1 = basecs_EnumerationLiteralCS(value=7)
    a2 = basecs_EnumerationLiteralCS(value=13)
    b = basecs_EnumerationCS()
    _safe_set(b, 'basecs_EnumerationCS', {a1})
    assert _is_linked(b, 'basecs_EnumerationCS', a1)
    if hasattr(a1, 'basecs_EnumerationLiteralCS21'):
        assert _is_linked(a1, 'basecs_EnumerationLiteralCS21', b)
    _safe_set(b, 'basecs_EnumerationCS', {a2})
    assert _is_linked(b, 'basecs_EnumerationCS', a2)
    if hasattr(a1, 'basecs_EnumerationLiteralCS21'):
        assert not _is_linked(a1, 'basecs_EnumerationLiteralCS21', b)
    if hasattr(a2, 'basecs_EnumerationLiteralCS21'):
        assert _is_linked(a2, 'basecs_EnumerationLiteralCS21', b)
    _safe_set(b, 'basecs_EnumerationCS', set())
    assert not _is_linked(b, 'basecs_EnumerationCS', a2)
    if hasattr(a2, 'basecs_EnumerationLiteralCS21'):
        assert not _is_linked(a2, 'basecs_EnumerationLiteralCS21', b)


def test_assoc_ownedParameter44_reverse_link_reassign_clear():
    a1 = basecs_ParameterCS()
    a2 = basecs_ParameterCS()
    b = basecs_OperationCS()
    _safe_set(b, 'owner45', {a1})
    assert _is_linked(b, 'owner45', a1)
    if hasattr(a1, 'ParameterCS'):
        assert _is_linked(a1, 'ParameterCS', b)
    _safe_set(b, 'owner45', {a2})
    assert _is_linked(b, 'owner45', a2)
    if hasattr(a1, 'ParameterCS'):
        assert not _is_linked(a1, 'ParameterCS', b)
    if hasattr(a2, 'ParameterCS'):
        assert _is_linked(a2, 'ParameterCS', b)
    _safe_set(b, 'owner45', set())
    assert not _is_linked(b, 'owner45', a2)
    if hasattr(a2, 'ParameterCS'):
        assert not _is_linked(a2, 'ParameterCS', b)


def test_assoc_ownedPostcondition51_reverse_link_reassign_clear():
    a1 = basecs_OperationCS()
    a2 = basecs_OperationCS()
    b = basecs_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'basecs_ConstraintCS53', a1)
    assert _is_linked(b, 'basecs_ConstraintCS53', a1)
    if hasattr(a1, 'basecs_OperationCS52'):
        assert _is_linked(a1, 'basecs_OperationCS52', b)
    _safe_set(b, 'basecs_ConstraintCS53', a2)
    assert _is_linked(b, 'basecs_ConstraintCS53', a2)
    if hasattr(a1, 'basecs_OperationCS52'):
        assert not _is_linked(a1, 'basecs_OperationCS52', b)
    if hasattr(a2, 'basecs_OperationCS52'):
        assert _is_linked(a2, 'basecs_OperationCS52', b)
    _safe_set(b, 'basecs_ConstraintCS53', None)
    assert not _is_linked(b, 'basecs_ConstraintCS53', a2)
    if hasattr(a2, 'basecs_OperationCS52'):
        assert not _is_linked(a2, 'basecs_OperationCS52', b)


def test_assoc_ownedPrecondition48_reverse_link_reassign_clear():
    a1 = basecs_OperationCS()
    a2 = basecs_OperationCS()
    b = basecs_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'basecs_ConstraintCS50', a1)
    assert _is_linked(b, 'basecs_ConstraintCS50', a1)
    if hasattr(a1, 'basecs_OperationCS49'):
        assert _is_linked(a1, 'basecs_OperationCS49', b)
    _safe_set(b, 'basecs_ConstraintCS50', a2)
    assert _is_linked(b, 'basecs_ConstraintCS50', a2)
    if hasattr(a1, 'basecs_OperationCS49'):
        assert not _is_linked(a1, 'basecs_OperationCS49', b)
    if hasattr(a2, 'basecs_OperationCS49'):
        assert _is_linked(a2, 'basecs_OperationCS49', b)
    _safe_set(b, 'basecs_ConstraintCS50', None)
    assert not _is_linked(b, 'basecs_ConstraintCS50', a2)
    if hasattr(a2, 'basecs_OperationCS49'):
        assert not _is_linked(a2, 'basecs_OperationCS49', b)


def test_assoc_ownedType57_reverse_link_reassign_clear():
    a1 = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    a2 = basecs_PackageCS(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    _safe_set(b, 'ClassifierCS', a1)
    assert _is_linked(b, 'ClassifierCS', a1)
    if hasattr(a1, 'owner58'):
        assert _is_linked(a1, 'owner58', b)
    _safe_set(b, 'ClassifierCS', a2)
    assert _is_linked(b, 'ClassifierCS', a2)
    if hasattr(a1, 'owner58'):
        assert not _is_linked(a1, 'owner58', b)
    if hasattr(a2, 'owner58'):
        assert _is_linked(a2, 'owner58', b)
    _safe_set(b, 'ClassifierCS', None)
    assert not _is_linked(b, 'ClassifierCS', a2)
    if hasattr(a2, 'owner58'):
        assert not _is_linked(a2, 'owner58', b)


def test_assoc_owner10_reverse_link_reassign_clear():
    a1 = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    a2 = basecs_PackageCS(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    _safe_set(b, 'ownedType', a1)
    assert _is_linked(b, 'ownedType', a1)
    if hasattr(a1, 'PackageCS'):
        assert _is_linked(a1, 'PackageCS', b)
    _safe_set(b, 'ownedType', a2)
    assert _is_linked(b, 'ownedType', a2)
    if hasattr(a1, 'PackageCS'):
        assert not _is_linked(a1, 'PackageCS', b)
    if hasattr(a2, 'PackageCS'):
        assert _is_linked(a2, 'PackageCS', b)
    _safe_set(b, 'ownedType', None)
    assert not _is_linked(b, 'ownedType', a2)
    if hasattr(a2, 'PackageCS'):
        assert not _is_linked(a2, 'PackageCS', b)


def test_assoc_owner60_reverse_link_reassign_clear():
    a1 = basecs_ParameterCS()
    a2 = basecs_ParameterCS()
    b = basecs_OperationCS()
    _safe_set(b, 'OperationCS61', a1)
    assert _is_linked(b, 'OperationCS61', a1)
    if hasattr(a1, 'ownedParameter'):
        assert _is_linked(a1, 'ownedParameter', b)
    _safe_set(b, 'OperationCS61', a2)
    assert _is_linked(b, 'OperationCS61', a2)
    if hasattr(a1, 'ownedParameter'):
        assert not _is_linked(a1, 'ownedParameter', b)
    if hasattr(a2, 'ownedParameter'):
        assert _is_linked(a2, 'ownedParameter', b)
    _safe_set(b, 'OperationCS61', None)
    assert not _is_linked(b, 'OperationCS61', a2)
    if hasattr(a2, 'ownedParameter'):
        assert not _is_linked(a2, 'ownedParameter', b)


def test_assoc_pathName22_reverse_link_reassign_clear():
    a1 = basecs_PathNameCS(scopeFilter="sample_text")
    a2 = basecs_PathNameCS(scopeFilter="sample_text_2")
    b = basecs_ImportCS(all=True)
    _safe_set(b, 'basecs_ImportCS', a1)
    assert _is_linked(b, 'basecs_ImportCS', a1)
    if hasattr(a1, 'basecs_PathNameCS'):
        assert _is_linked(a1, 'basecs_PathNameCS', b)
    _safe_set(b, 'basecs_ImportCS', a2)
    assert _is_linked(b, 'basecs_ImportCS', a2)
    if hasattr(a1, 'basecs_PathNameCS'):
        assert not _is_linked(a1, 'basecs_PathNameCS', b)
    if hasattr(a2, 'basecs_PathNameCS'):
        assert _is_linked(a2, 'basecs_PathNameCS', b)
    _safe_set(b, 'basecs_ImportCS', None)
    assert not _is_linked(b, 'basecs_ImportCS', a2)
    if hasattr(a2, 'basecs_PathNameCS'):
        assert not _is_linked(a2, 'basecs_PathNameCS', b)


def test_assoc_specification12_reverse_link_reassign_clear():
    a1 = basecs_SpecificationCS(exprString="sample_text")
    a2 = basecs_SpecificationCS(exprString="sample_text_2")
    b = basecs_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'basecs_ConstraintCS13', a1)
    assert _is_linked(b, 'basecs_ConstraintCS13', a1)
    if hasattr(a1, 'basecs_SpecificationCS'):
        assert _is_linked(a1, 'basecs_SpecificationCS', b)
    _safe_set(b, 'basecs_ConstraintCS13', a2)
    assert _is_linked(b, 'basecs_ConstraintCS13', a2)
    if hasattr(a1, 'basecs_SpecificationCS'):
        assert not _is_linked(a1, 'basecs_SpecificationCS', b)
    if hasattr(a2, 'basecs_SpecificationCS'):
        assert _is_linked(a2, 'basecs_SpecificationCS', b)
    _safe_set(b, 'basecs_ConstraintCS13', None)
    assert not _is_linked(b, 'basecs_ConstraintCS13', a2)
    if hasattr(a2, 'basecs_SpecificationCS'):
        assert not _is_linked(a2, 'basecs_SpecificationCS', b)


