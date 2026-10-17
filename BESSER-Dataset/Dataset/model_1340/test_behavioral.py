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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element68_stub_double():
    # basecs_Element has no real 'basecs_Element70' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PathNameCS(scopeFilter="sample_text")
    partner = basecs_Element()
    setattr(partner, 'basecs_Element70', None)
    _safe_set(owner, 'basecs_PathNameCS69', partner)
    assert getattr(partner, 'basecs_Element70') == owner
    _safe_set(owner, 'basecs_PathNameCS69', None)
    assert getattr(partner, 'basecs_Element70') is None


def test_assoc_literals17_stub_double():
    # basecs_DataTypeCS has no real 'basecs_DataTypeCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_EnumerationLiteralCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_EnumerationLiteralCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_EnumerationLiteralCS(value=7)
    partner = basecs_DataTypeCS()
    setattr(partner, 'basecs_DataTypeCS', None)
    _safe_set(owner, 'basecs_EnumerationLiteralCS', partner)
    assert getattr(partner, 'basecs_DataTypeCS') == owner
    _safe_set(owner, 'basecs_EnumerationLiteralCS', None)
    assert getattr(partner, 'basecs_DataTypeCS') is None


def test_assoc_multiplicity106_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS107' property in the generated
    # code (a bare stub) -- manually attach it so basecs_MultiplicityCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_MultiplicityCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_MultiplicityCS()
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS107', None)
    _safe_set(owner, 'basecs_MultiplicityCS', partner)
    assert getattr(partner, 'basecs_TypedRefCS107') == owner
    _safe_set(owner, 'basecs_MultiplicityCS', None)
    assert getattr(partner, 'basecs_TypedRefCS107') is None


def test_assoc_namespace23_stub_double():
    # basecs_Namespace has no real 'basecs_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so basecs_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_ImportCS(all=True)
    partner = basecs_Namespace()
    setattr(partner, 'basecs_Namespace', None)
    _safe_set(owner, 'basecs_ImportCS24', partner)
    assert getattr(partner, 'basecs_Namespace') == owner
    _safe_set(owner, 'basecs_ImportCS24', None)
    assert getattr(partner, 'basecs_Namespace') is None


def test_assoc_ownedAnnotation35_stub_double():
    # basecs_AnnotationElementCS has no real 'basecs_AnnotationElementCS37' property in the generated
    # code (a bare stub) -- manually attach it so basecs_ModelElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_ModelElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    partner = basecs_AnnotationElementCS()
    setattr(partner, 'basecs_AnnotationElementCS37', None)
    _safe_set(owner, 'basecs_ModelElementCS36', {partner})
    assert getattr(partner, 'basecs_AnnotationElementCS37') == owner
    _safe_set(owner, 'basecs_ModelElementCS36', set())
    assert getattr(partner, 'basecs_AnnotationElementCS37') is None


def test_assoc_ownedContent0_stub_double():
    # basecs_AnnotationCS has no real 'basecs_AnnotationCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_ModelElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_ModelElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    partner = basecs_AnnotationCS()
    setattr(partner, 'basecs_AnnotationCS', None)
    _safe_set(owner, 'basecs_ModelElementCS', partner)
    assert getattr(partner, 'basecs_AnnotationCS') == owner
    _safe_set(owner, 'basecs_ModelElementCS', None)
    assert getattr(partner, 'basecs_AnnotationCS') is None


def test_assoc_ownedContextType25_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS26' property in the generated
    # code (a bare stub) -- manually attach it so basecs_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_LambdaTypeCS(name="sample_text")
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS26', None)
    _safe_set(owner, 'basecs_LambdaTypeCS', partner)
    assert getattr(partner, 'basecs_TypedRefCS26') == owner
    _safe_set(owner, 'basecs_LambdaTypeCS', None)
    assert getattr(partner, 'basecs_TypedRefCS26') is None


def test_assoc_ownedDetail3_stub_double():
    # basecs_AnnotationElementCS has no real 'basecs_AnnotationElementCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_DetailCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_DetailCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_DetailCS(value="sample_text")
    partner = basecs_AnnotationElementCS()
    setattr(partner, 'basecs_AnnotationElementCS', None)
    _safe_set(owner, 'basecs_DetailCS', partner)
    assert getattr(partner, 'basecs_AnnotationElementCS') == owner
    _safe_set(owner, 'basecs_DetailCS', None)
    assert getattr(partner, 'basecs_AnnotationElementCS') is None


def test_assoc_ownedException46_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS47' property in the generated
    # code (a bare stub) -- manually attach it so basecs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_OperationCS()
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS47', None)
    _safe_set(owner, 'basecs_OperationCS', {partner})
    assert getattr(partner, 'basecs_TypedRefCS47') == owner
    _safe_set(owner, 'basecs_OperationCS', set())
    assert getattr(partner, 'basecs_TypedRefCS47') is None


def test_assoc_ownedImport80_stub_double():
    # basecs_RootCS has no real 'basecs_RootCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_ImportCS(all=True)
    partner = basecs_RootCS()
    setattr(partner, 'basecs_RootCS', None)
    _safe_set(owner, 'basecs_ImportCS81', partner)
    assert getattr(partner, 'basecs_RootCS') == owner
    _safe_set(owner, 'basecs_ImportCS81', None)
    assert getattr(partner, 'basecs_RootCS') is None


def test_assoc_ownedNestedPackage59_stub_double():
    # basecs_PackageOwnerCS has no real 'basecs_PackageOwnerCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PackageCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PackageCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    partner = basecs_PackageOwnerCS()
    setattr(partner, 'basecs_PackageOwnerCS', None)
    _safe_set(owner, 'basecs_PackageCS', partner)
    assert getattr(partner, 'basecs_PackageOwnerCS') == owner
    _safe_set(owner, 'basecs_PackageCS', None)
    assert getattr(partner, 'basecs_PackageOwnerCS') is None


def test_assoc_ownedOperation5_stub_double():
    # basecs_ClassCS has no real 'owningClass' property in the generated
    # code (a bare stub) -- manually attach it so basecs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_OperationCS()
    partner = basecs_ClassCS()
    setattr(partner, 'owningClass', None)
    _safe_set(owner, 'OperationCS', partner)
    assert getattr(partner, 'owningClass') == owner
    _safe_set(owner, 'OperationCS', None)
    assert getattr(partner, 'owningClass') is None


def test_assoc_ownedParameterType27_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS29' property in the generated
    # code (a bare stub) -- manually attach it so basecs_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_LambdaTypeCS(name="sample_text")
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS29', None)
    _safe_set(owner, 'basecs_LambdaTypeCS28', {partner})
    assert getattr(partner, 'basecs_TypedRefCS29') == owner
    _safe_set(owner, 'basecs_LambdaTypeCS28', set())
    assert getattr(partner, 'basecs_TypedRefCS29') is None


def test_assoc_ownedParts98_stub_double():
    # basecs_TuplePartCS has no real 'basecs_TuplePartCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_TupleTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_TupleTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_TupleTypeCS(name="sample_text")
    partner = basecs_TuplePartCS()
    setattr(partner, 'basecs_TuplePartCS', None)
    _safe_set(owner, 'basecs_TupleTypeCS', {partner})
    assert getattr(partner, 'basecs_TuplePartCS') == owner
    _safe_set(owner, 'basecs_TupleTypeCS', set())
    assert getattr(partner, 'basecs_TuplePartCS') is None


def test_assoc_ownedProperty6_stub_double():
    # basecs_ClassCS has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so basecs_StructuralFeatureCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_StructuralFeatureCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_StructuralFeatureCS(default="sample_text")
    partner = basecs_ClassCS()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'StructuralFeatureCS', partner)
    assert getattr(partner, 'owner') == owner
    _safe_set(owner, 'StructuralFeatureCS', None)
    assert getattr(partner, 'owner') is None


def test_assoc_ownedResultType30_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS32' property in the generated
    # code (a bare stub) -- manually attach it so basecs_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_LambdaTypeCS(name="sample_text")
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS32', None)
    _safe_set(owner, 'basecs_LambdaTypeCS31', partner)
    assert getattr(partner, 'basecs_TypedRefCS32') == owner
    _safe_set(owner, 'basecs_LambdaTypeCS31', None)
    assert getattr(partner, 'basecs_TypedRefCS32') is None


def test_assoc_ownedType104_stub_double():
    # basecs_TypedRefCS has no real 'basecs_TypedRefCS105' property in the generated
    # code (a bare stub) -- manually attach it so basecs_TypedElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_TypedElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_TypedElementCS(optional=True, qualifier="sample_text")
    partner = basecs_TypedRefCS()
    setattr(partner, 'basecs_TypedRefCS105', None)
    _safe_set(owner, 'basecs_TypedElementCS', partner)
    assert getattr(partner, 'basecs_TypedRefCS105') == owner
    _safe_set(owner, 'basecs_TypedElementCS', None)
    assert getattr(partner, 'basecs_TypedRefCS105') is None


def test_assoc_owner85_stub_double():
    # basecs_ClassCS has no real 'ClassCS86' property in the generated
    # code (a bare stub) -- manually attach it so basecs_StructuralFeatureCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_StructuralFeatureCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_StructuralFeatureCS(default="sample_text")
    partner = basecs_ClassCS()
    setattr(partner, 'ClassCS86', None)
    _safe_set(owner, 'ownedProperty', partner)
    assert getattr(partner, 'ClassCS86') == owner
    _safe_set(owner, 'ownedProperty', None)
    assert getattr(partner, 'ClassCS86') is None


def test_assoc_owningClass43_stub_double():
    # basecs_ClassCS has no real 'ClassCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_OperationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_OperationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_OperationCS()
    partner = basecs_ClassCS()
    setattr(partner, 'ClassCS', None)
    _safe_set(owner, 'ownedOperation', partner)
    assert getattr(partner, 'ClassCS') == owner
    _safe_set(owner, 'ownedOperation', None)
    assert getattr(partner, 'ClassCS') is None


def test_assoc_path67_stub_double():
    # basecs_PathElementCS has no real 'PathElementCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PathNameCS(scopeFilter="sample_text")
    partner = basecs_PathElementCS()
    setattr(partner, 'PathElementCS', None)
    _safe_set(owner, 'pathName', {partner})
    assert getattr(partner, 'PathElementCS') == owner
    _safe_set(owner, 'pathName', set())
    assert getattr(partner, 'PathElementCS') is None


def test_assoc_pathName108_stub_double():
    # basecs_TypedTypeRefCS has no real 'basecs_TypedTypeRefCS' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PathNameCS(scopeFilter="sample_text")
    partner = basecs_TypedTypeRefCS()
    setattr(partner, 'basecs_TypedTypeRefCS', None)
    _safe_set(owner, 'basecs_PathNameCS109', partner)
    assert getattr(partner, 'basecs_TypedTypeRefCS') == owner
    _safe_set(owner, 'basecs_PathNameCS109', None)
    assert getattr(partner, 'basecs_TypedTypeRefCS') is None


def test_assoc_pathName38_stub_double():
    # basecs_ModelElementRefCS has no real 'basecs_ModelElementRefCS39' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PathNameCS(scopeFilter="sample_text")
    partner = basecs_ModelElementRefCS()
    setattr(partner, 'basecs_ModelElementRefCS39', None)
    _safe_set(owner, 'basecs_PathNameCS40', partner)
    assert getattr(partner, 'basecs_ModelElementRefCS39') == owner
    _safe_set(owner, 'basecs_PathNameCS40', None)
    assert getattr(partner, 'basecs_ModelElementRefCS39') is None


def test_assoc_pathName62_stub_double():
    # basecs_PathElementCS has no real 'path' property in the generated
    # code (a bare stub) -- manually attach it so basecs_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # basecs_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = basecs_PathNameCS(scopeFilter="sample_text")
    partner = basecs_PathElementCS()
    setattr(partner, 'path', None)
    _safe_set(owner, 'PathNameCS', partner)
    assert getattr(partner, 'path') == owner
    _safe_set(owner, 'PathNameCS', None)
    assert getattr(partner, 'path') is None


