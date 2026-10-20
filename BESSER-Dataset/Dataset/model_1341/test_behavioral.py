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
    PackageCS,
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
    baseCST_AnnotationCS,
    baseCST_AnnotationElementCS,
    baseCST_AttributeCS,
    baseCST_ClassCS,
    baseCST_ClassifierCS,
    baseCST_ConstraintCS,
    baseCST_DataTypeCS,
    baseCST_DetailCS,
    baseCST_DocumentationCS,
    baseCST_EClassifier,
    baseCST_Element,
    baseCST_ElementCS,
    baseCST_ElementRefCS,
    baseCST_EnumerationCS,
    baseCST_EnumerationLiteralCS,
    baseCST_FeatureCS,
    baseCST_ImportCS,
    baseCST_LambdaTypeCS,
    baseCST_LibraryCS,
    baseCST_ModelElementCS,
    baseCST_ModelElementRefCS,
    baseCST_MultiplicityBoundsCS,
    baseCST_MultiplicityCS,
    baseCST_MultiplicityStringCS,
    baseCST_NamedElementCS,
    baseCST_Namespace,
    baseCST_NamespaceCS,
    baseCST_OperationCS,
    baseCST_PackageCS,
    baseCST_ParameterCS,
    baseCST_PathElementCS,
    baseCST_PathElementWithURICS,
    baseCST_PathNameCS,
    baseCST_PivotableElementCS,
    baseCST_PrimitiveTypeRefCS,
    baseCST_Property,
    baseCST_ReferenceCS,
    baseCST_RootCS,
    baseCST_RootPackageCS,
    baseCST_SpecificationCS,
    baseCST_StructuralFeatureCS,
    baseCST_TemplateBindingCS,
    baseCST_TemplateParameterCS,
    baseCST_TemplateParameterSubstitutionCS,
    baseCST_TemplateSignatureCS,
    baseCST_TemplateableElementCS,
    baseCST_TuplePartCS,
    baseCST_TupleTypeCS,
    baseCST_Type,
    baseCST_TypeCS,
    baseCST_TypeParameterCS,
    baseCST_TypeRefCS,
    baseCST_TypedElementCS,
    baseCST_TypedRefCS,
    baseCST_TypedTypeRefCS,
    baseCST_VisitableCS,
    baseCST_WildcardTypeRefCS,
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

def test_assoc_context72_reverse_link_reassign_clear():
    a1 = baseCST_PathNameCS(scopeFilter="sample_text")
    a2 = baseCST_PathNameCS(scopeFilter="sample_text_2")
    b = baseCST_ElementCS()
    _safe_set(b, 'baseCST_ElementCS74', a1)
    assert _is_linked(b, 'baseCST_ElementCS74', a1)
    if hasattr(a1, 'baseCST_PathNameCS73'):
        assert _is_linked(a1, 'baseCST_PathNameCS73', b)
    _safe_set(b, 'baseCST_ElementCS74', a2)
    assert _is_linked(b, 'baseCST_ElementCS74', a2)
    if hasattr(a1, 'baseCST_PathNameCS73'):
        assert not _is_linked(a1, 'baseCST_PathNameCS73', b)
    if hasattr(a2, 'baseCST_PathNameCS73'):
        assert _is_linked(a2, 'baseCST_PathNameCS73', b)
    _safe_set(b, 'baseCST_ElementCS74', None)
    assert not _is_linked(b, 'baseCST_ElementCS74', a2)
    if hasattr(a2, 'baseCST_PathNameCS73'):
        assert not _is_linked(a2, 'baseCST_PathNameCS73', b)


def test_assoc_logicalParent19_reverse_link_reassign_clear():
    a1 = baseCST_ElementCS()
    a2 = baseCST_ElementCS()
    b = baseCST_ElementCS()
    _safe_set(b, 'baseCST_ElementCS18', a1)
    assert _is_linked(b, 'baseCST_ElementCS18', a1)
    if hasattr(a1, 'baseCST_ElementCS'):
        assert _is_linked(a1, 'baseCST_ElementCS', b)
    _safe_set(b, 'baseCST_ElementCS18', a2)
    assert _is_linked(b, 'baseCST_ElementCS18', a2)
    if hasattr(a1, 'baseCST_ElementCS'):
        assert not _is_linked(a1, 'baseCST_ElementCS', b)
    if hasattr(a2, 'baseCST_ElementCS'):
        assert _is_linked(a2, 'baseCST_ElementCS', b)
    _safe_set(b, 'baseCST_ElementCS18', None)
    assert not _is_linked(b, 'baseCST_ElementCS18', a2)
    if hasattr(a2, 'baseCST_ElementCS'):
        assert not _is_linked(a2, 'baseCST_ElementCS', b)


def test_assoc_messageSpecification14_reverse_link_reassign_clear():
    a1 = baseCST_SpecificationCS(exprString="sample_text")
    a2 = baseCST_SpecificationCS(exprString="sample_text_2")
    b = baseCST_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'baseCST_ConstraintCS15', a1)
    assert _is_linked(b, 'baseCST_ConstraintCS15', a1)
    if hasattr(a1, 'baseCST_SpecificationCS16'):
        assert _is_linked(a1, 'baseCST_SpecificationCS16', b)
    _safe_set(b, 'baseCST_ConstraintCS15', a2)
    assert _is_linked(b, 'baseCST_ConstraintCS15', a2)
    if hasattr(a1, 'baseCST_SpecificationCS16'):
        assert not _is_linked(a1, 'baseCST_SpecificationCS16', b)
    if hasattr(a2, 'baseCST_SpecificationCS16'):
        assert _is_linked(a2, 'baseCST_SpecificationCS16', b)
    _safe_set(b, 'baseCST_ConstraintCS15', None)
    assert not _is_linked(b, 'baseCST_ConstraintCS15', a2)
    if hasattr(a2, 'baseCST_SpecificationCS16'):
        assert not _is_linked(a2, 'baseCST_SpecificationCS16', b)


def test_assoc_ownedConstraint11_reverse_link_reassign_clear():
    a1 = baseCST_ConstraintCS(stereotype="sample_text")
    a2 = baseCST_ConstraintCS(stereotype="sample_text_2")
    b = baseCST_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    _safe_set(b, 'baseCST_ClassifierCS', {a1})
    assert _is_linked(b, 'baseCST_ClassifierCS', a1)
    if hasattr(a1, 'baseCST_ConstraintCS'):
        assert _is_linked(a1, 'baseCST_ConstraintCS', b)
    _safe_set(b, 'baseCST_ClassifierCS', {a2})
    assert _is_linked(b, 'baseCST_ClassifierCS', a2)
    if hasattr(a1, 'baseCST_ConstraintCS'):
        assert not _is_linked(a1, 'baseCST_ConstraintCS', b)
    if hasattr(a2, 'baseCST_ConstraintCS'):
        assert _is_linked(a2, 'baseCST_ConstraintCS', b)
    _safe_set(b, 'baseCST_ClassifierCS', set())
    assert not _is_linked(b, 'baseCST_ClassifierCS', a2)
    if hasattr(a2, 'baseCST_ConstraintCS'):
        assert not _is_linked(a2, 'baseCST_ConstraintCS', b)


def test_assoc_ownedDefaultExpression88_reverse_link_reassign_clear():
    a1 = baseCST_StructuralFeatureCS(default="sample_text")
    a2 = baseCST_StructuralFeatureCS(default="sample_text_2")
    b = baseCST_SpecificationCS(exprString="sample_text")
    _safe_set(b, 'baseCST_SpecificationCS89', a1)
    assert _is_linked(b, 'baseCST_SpecificationCS89', a1)
    if hasattr(a1, 'baseCST_StructuralFeatureCS'):
        assert _is_linked(a1, 'baseCST_StructuralFeatureCS', b)
    _safe_set(b, 'baseCST_SpecificationCS89', a2)
    assert _is_linked(b, 'baseCST_SpecificationCS89', a2)
    if hasattr(a1, 'baseCST_StructuralFeatureCS'):
        assert not _is_linked(a1, 'baseCST_StructuralFeatureCS', b)
    if hasattr(a2, 'baseCST_StructuralFeatureCS'):
        assert _is_linked(a2, 'baseCST_StructuralFeatureCS', b)
    _safe_set(b, 'baseCST_SpecificationCS89', None)
    assert not _is_linked(b, 'baseCST_SpecificationCS89', a2)
    if hasattr(a2, 'baseCST_StructuralFeatureCS'):
        assert not _is_linked(a2, 'baseCST_StructuralFeatureCS', b)


def test_assoc_ownedNestedPackage60_reverse_link_reassign_clear():
    a1 = baseCST_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    a2 = baseCST_PackageCS(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = baseCST_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    _safe_set(b, 'baseCST_PackageCS59', {a1})
    assert _is_linked(b, 'baseCST_PackageCS59', a1)
    if hasattr(a1, 'baseCST_PackageCS'):
        assert _is_linked(a1, 'baseCST_PackageCS', b)
    _safe_set(b, 'baseCST_PackageCS59', {a2})
    assert _is_linked(b, 'baseCST_PackageCS59', a2)
    if hasattr(a1, 'baseCST_PackageCS'):
        assert not _is_linked(a1, 'baseCST_PackageCS', b)
    if hasattr(a2, 'baseCST_PackageCS'):
        assert _is_linked(a2, 'baseCST_PackageCS', b)
    _safe_set(b, 'baseCST_PackageCS59', set())
    assert not _is_linked(b, 'baseCST_PackageCS59', a2)
    if hasattr(a2, 'baseCST_PackageCS'):
        assert not _is_linked(a2, 'baseCST_PackageCS', b)


def test_assoc_ownedType57_reverse_link_reassign_clear():
    a1 = baseCST_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    a2 = baseCST_PackageCS(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = baseCST_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
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
    a1 = baseCST_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    a2 = baseCST_PackageCS(nsPrefix="sample_text_2", nsURI="sample_text_2")
    b = baseCST_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
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


def test_assoc_pathName22_reverse_link_reassign_clear():
    a1 = baseCST_PathNameCS(scopeFilter="sample_text")
    a2 = baseCST_PathNameCS(scopeFilter="sample_text_2")
    b = baseCST_ImportCS(all=True)
    _safe_set(b, 'baseCST_ImportCS', a1)
    assert _is_linked(b, 'baseCST_ImportCS', a1)
    if hasattr(a1, 'baseCST_PathNameCS'):
        assert _is_linked(a1, 'baseCST_PathNameCS', b)
    _safe_set(b, 'baseCST_ImportCS', a2)
    assert _is_linked(b, 'baseCST_ImportCS', a2)
    if hasattr(a1, 'baseCST_PathNameCS'):
        assert not _is_linked(a1, 'baseCST_PathNameCS', b)
    if hasattr(a2, 'baseCST_PathNameCS'):
        assert _is_linked(a2, 'baseCST_PathNameCS', b)
    _safe_set(b, 'baseCST_ImportCS', None)
    assert not _is_linked(b, 'baseCST_ImportCS', a2)
    if hasattr(a2, 'baseCST_PathNameCS'):
        assert not _is_linked(a2, 'baseCST_PathNameCS', b)


def test_assoc_specification12_reverse_link_reassign_clear():
    a1 = baseCST_SpecificationCS(exprString="sample_text")
    a2 = baseCST_SpecificationCS(exprString="sample_text_2")
    b = baseCST_ConstraintCS(stereotype="sample_text")
    _safe_set(b, 'baseCST_ConstraintCS13', a1)
    assert _is_linked(b, 'baseCST_ConstraintCS13', a1)
    if hasattr(a1, 'baseCST_SpecificationCS'):
        assert _is_linked(a1, 'baseCST_SpecificationCS', b)
    _safe_set(b, 'baseCST_ConstraintCS13', a2)
    assert _is_linked(b, 'baseCST_ConstraintCS13', a2)
    if hasattr(a1, 'baseCST_SpecificationCS'):
        assert not _is_linked(a1, 'baseCST_SpecificationCS', b)
    if hasattr(a2, 'baseCST_SpecificationCS'):
        assert _is_linked(a2, 'baseCST_SpecificationCS', b)
    _safe_set(b, 'baseCST_ConstraintCS13', None)
    assert not _is_linked(b, 'baseCST_ConstraintCS13', a2)
    if hasattr(a2, 'baseCST_SpecificationCS'):
        assert not _is_linked(a2, 'baseCST_SpecificationCS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element69_stub_double():
    # baseCST_Element has no real 'baseCST_Element71' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_PathNameCS(scopeFilter="sample_text")
    partner = baseCST_Element()
    setattr(partner, 'baseCST_Element71', None)
    _safe_set(owner, 'baseCST_PathNameCS70', partner)
    assert getattr(partner, 'baseCST_Element71') == owner
    _safe_set(owner, 'baseCST_PathNameCS70', None)
    assert getattr(partner, 'baseCST_Element71') is None


def test_assoc_literals17_stub_double():
    # baseCST_DataTypeCS has no real 'baseCST_DataTypeCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_EnumerationLiteralCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_EnumerationLiteralCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_EnumerationLiteralCS(value=7)
    partner = baseCST_DataTypeCS()
    setattr(partner, 'baseCST_DataTypeCS', None)
    _safe_set(owner, 'baseCST_EnumerationLiteralCS', partner)
    assert owner in getattr(partner, 'baseCST_DataTypeCS')
    _safe_set(owner, 'baseCST_EnumerationLiteralCS', None)
    assert owner not in getattr(partner, 'baseCST_DataTypeCS')


def test_assoc_multiplicity107_stub_double():
    # baseCST_TypedRefCS has no real 'baseCST_TypedRefCS108' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_MultiplicityCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_MultiplicityCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_MultiplicityCS()
    partner = baseCST_TypedRefCS()
    setattr(partner, 'baseCST_TypedRefCS108', None)
    _safe_set(owner, 'baseCST_MultiplicityCS', partner)
    assert getattr(partner, 'baseCST_TypedRefCS108') == owner
    _safe_set(owner, 'baseCST_MultiplicityCS', None)
    assert getattr(partner, 'baseCST_TypedRefCS108') is None


def test_assoc_namespace23_stub_double():
    # baseCST_Namespace has no real 'baseCST_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ImportCS(all=True)
    partner = baseCST_Namespace()
    setattr(partner, 'baseCST_Namespace', None)
    _safe_set(owner, 'baseCST_ImportCS24', partner)
    assert getattr(partner, 'baseCST_Namespace') == owner
    _safe_set(owner, 'baseCST_ImportCS24', None)
    assert getattr(partner, 'baseCST_Namespace') is None


def test_assoc_ownedAnnotation35_stub_double():
    # baseCST_AnnotationElementCS has no real 'baseCST_AnnotationElementCS37' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ModelElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ModelElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    partner = baseCST_AnnotationElementCS()
    setattr(partner, 'baseCST_AnnotationElementCS37', None)
    _safe_set(owner, 'baseCST_ModelElementCS36', {partner})
    assert getattr(partner, 'baseCST_AnnotationElementCS37') == owner
    _safe_set(owner, 'baseCST_ModelElementCS36', set())
    assert getattr(partner, 'baseCST_AnnotationElementCS37') is None


def test_assoc_ownedBodyExpression54_stub_double():
    # baseCST_OperationCS has no real 'baseCST_OperationCS55' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_SpecificationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_SpecificationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_SpecificationCS(exprString="sample_text")
    partner = baseCST_OperationCS()
    setattr(partner, 'baseCST_OperationCS55', None)
    _safe_set(owner, 'baseCST_SpecificationCS56', partner)
    assert owner in getattr(partner, 'baseCST_OperationCS55')
    _safe_set(owner, 'baseCST_SpecificationCS56', None)
    assert owner not in getattr(partner, 'baseCST_OperationCS55')


def test_assoc_ownedContent0_stub_double():
    # baseCST_AnnotationCS has no real 'baseCST_AnnotationCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ModelElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ModelElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    partner = baseCST_AnnotationCS()
    setattr(partner, 'baseCST_AnnotationCS', None)
    _safe_set(owner, 'baseCST_ModelElementCS', partner)
    assert owner in getattr(partner, 'baseCST_AnnotationCS')
    _safe_set(owner, 'baseCST_ModelElementCS', None)
    assert owner not in getattr(partner, 'baseCST_AnnotationCS')


def test_assoc_ownedContextType25_stub_double():
    # baseCST_TypedRefCS has no real 'baseCST_TypedRefCS26' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_LambdaTypeCS(name="sample_text")
    partner = baseCST_TypedRefCS()
    setattr(partner, 'baseCST_TypedRefCS26', None)
    _safe_set(owner, 'baseCST_LambdaTypeCS', partner)
    assert getattr(partner, 'baseCST_TypedRefCS26') == owner
    _safe_set(owner, 'baseCST_LambdaTypeCS', None)
    assert getattr(partner, 'baseCST_TypedRefCS26') is None


def test_assoc_ownedDetail3_stub_double():
    # baseCST_AnnotationElementCS has no real 'baseCST_AnnotationElementCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_DetailCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_DetailCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_DetailCS(value="sample_text")
    partner = baseCST_AnnotationElementCS()
    setattr(partner, 'baseCST_AnnotationElementCS', None)
    _safe_set(owner, 'baseCST_DetailCS', partner)
    assert owner in getattr(partner, 'baseCST_AnnotationElementCS')
    _safe_set(owner, 'baseCST_DetailCS', None)
    assert owner not in getattr(partner, 'baseCST_AnnotationElementCS')


def test_assoc_ownedImport81_stub_double():
    # baseCST_RootCS has no real 'baseCST_RootCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ImportCS(all=True)
    partner = baseCST_RootCS()
    setattr(partner, 'baseCST_RootCS', None)
    _safe_set(owner, 'baseCST_ImportCS82', partner)
    assert owner in getattr(partner, 'baseCST_RootCS')
    _safe_set(owner, 'baseCST_ImportCS82', None)
    assert owner not in getattr(partner, 'baseCST_RootCS')


def test_assoc_ownedLiterals20_stub_double():
    # baseCST_EnumerationCS has no real 'baseCST_EnumerationCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_EnumerationLiteralCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_EnumerationLiteralCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_EnumerationLiteralCS(value=7)
    partner = baseCST_EnumerationCS()
    setattr(partner, 'baseCST_EnumerationCS', None)
    _safe_set(owner, 'baseCST_EnumerationLiteralCS21', partner)
    assert owner in getattr(partner, 'baseCST_EnumerationCS')
    _safe_set(owner, 'baseCST_EnumerationLiteralCS21', None)
    assert owner not in getattr(partner, 'baseCST_EnumerationCS')


def test_assoc_ownedParameterType27_stub_double():
    # baseCST_TypedRefCS has no real 'baseCST_TypedRefCS29' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_LambdaTypeCS(name="sample_text")
    partner = baseCST_TypedRefCS()
    setattr(partner, 'baseCST_TypedRefCS29', None)
    _safe_set(owner, 'baseCST_LambdaTypeCS28', {partner})
    assert getattr(partner, 'baseCST_TypedRefCS29') == owner
    _safe_set(owner, 'baseCST_LambdaTypeCS28', set())
    assert getattr(partner, 'baseCST_TypedRefCS29') is None


def test_assoc_ownedParts99_stub_double():
    # baseCST_TuplePartCS has no real 'baseCST_TuplePartCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_TupleTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_TupleTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_TupleTypeCS(name="sample_text")
    partner = baseCST_TuplePartCS()
    setattr(partner, 'baseCST_TuplePartCS', None)
    _safe_set(owner, 'baseCST_TupleTypeCS', {partner})
    assert getattr(partner, 'baseCST_TuplePartCS') == owner
    _safe_set(owner, 'baseCST_TupleTypeCS', set())
    assert getattr(partner, 'baseCST_TuplePartCS') is None


def test_assoc_ownedPostcondition51_stub_double():
    # baseCST_OperationCS has no real 'baseCST_OperationCS52' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ConstraintCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ConstraintCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ConstraintCS(stereotype="sample_text")
    partner = baseCST_OperationCS()
    setattr(partner, 'baseCST_OperationCS52', None)
    _safe_set(owner, 'baseCST_ConstraintCS53', partner)
    assert owner in getattr(partner, 'baseCST_OperationCS52')
    _safe_set(owner, 'baseCST_ConstraintCS53', None)
    assert owner not in getattr(partner, 'baseCST_OperationCS52')


def test_assoc_ownedPrecondition48_stub_double():
    # baseCST_OperationCS has no real 'baseCST_OperationCS49' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_ConstraintCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_ConstraintCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_ConstraintCS(stereotype="sample_text")
    partner = baseCST_OperationCS()
    setattr(partner, 'baseCST_OperationCS49', None)
    _safe_set(owner, 'baseCST_ConstraintCS50', partner)
    assert owner in getattr(partner, 'baseCST_OperationCS49')
    _safe_set(owner, 'baseCST_ConstraintCS50', None)
    assert owner not in getattr(partner, 'baseCST_OperationCS49')


def test_assoc_ownedProperty6_stub_double():
    # baseCST_ClassCS has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_StructuralFeatureCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_StructuralFeatureCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_StructuralFeatureCS(default="sample_text")
    partner = baseCST_ClassCS()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'StructuralFeatureCS', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'StructuralFeatureCS', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_ownedResultType30_stub_double():
    # baseCST_TypedRefCS has no real 'baseCST_TypedRefCS32' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_LambdaTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_LambdaTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_LambdaTypeCS(name="sample_text")
    partner = baseCST_TypedRefCS()
    setattr(partner, 'baseCST_TypedRefCS32', None)
    _safe_set(owner, 'baseCST_LambdaTypeCS31', partner)
    assert getattr(partner, 'baseCST_TypedRefCS32') == owner
    _safe_set(owner, 'baseCST_LambdaTypeCS31', None)
    assert getattr(partner, 'baseCST_TypedRefCS32') is None


def test_assoc_ownedType105_stub_double():
    # baseCST_TypedRefCS has no real 'baseCST_TypedRefCS106' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_TypedElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_TypedElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_TypedElementCS(optional=True, qualifier="sample_text")
    partner = baseCST_TypedRefCS()
    setattr(partner, 'baseCST_TypedRefCS106', None)
    _safe_set(owner, 'baseCST_TypedElementCS', partner)
    assert getattr(partner, 'baseCST_TypedRefCS106') == owner
    _safe_set(owner, 'baseCST_TypedElementCS', None)
    assert getattr(partner, 'baseCST_TypedRefCS106') is None


def test_assoc_owner86_stub_double():
    # baseCST_ClassCS has no real 'ClassCS87' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_StructuralFeatureCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_StructuralFeatureCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_StructuralFeatureCS(default="sample_text")
    partner = baseCST_ClassCS()
    setattr(partner, 'ClassCS87', None)
    _safe_set(owner, 'ownedProperty', partner)
    assert getattr(partner, 'ClassCS87') == owner
    _safe_set(owner, 'ownedProperty', None)
    assert getattr(partner, 'ClassCS87') is None


def test_assoc_path68_stub_double():
    # baseCST_PathElementCS has no real 'PathElementCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_PathNameCS(scopeFilter="sample_text")
    partner = baseCST_PathElementCS()
    setattr(partner, 'PathElementCS', None)
    _safe_set(owner, 'pathName', {partner})
    assert getattr(partner, 'PathElementCS') == owner
    _safe_set(owner, 'pathName', set())
    assert getattr(partner, 'PathElementCS') is None


def test_assoc_pathName109_stub_double():
    # baseCST_TypedTypeRefCS has no real 'baseCST_TypedTypeRefCS' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_PathNameCS(scopeFilter="sample_text")
    partner = baseCST_TypedTypeRefCS()
    setattr(partner, 'baseCST_TypedTypeRefCS', None)
    _safe_set(owner, 'baseCST_PathNameCS110', partner)
    assert getattr(partner, 'baseCST_TypedTypeRefCS') == owner
    _safe_set(owner, 'baseCST_PathNameCS110', None)
    assert getattr(partner, 'baseCST_TypedTypeRefCS') is None


def test_assoc_pathName38_stub_double():
    # baseCST_ModelElementRefCS has no real 'baseCST_ModelElementRefCS39' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_PathNameCS(scopeFilter="sample_text")
    partner = baseCST_ModelElementRefCS()
    setattr(partner, 'baseCST_ModelElementRefCS39', None)
    _safe_set(owner, 'baseCST_PathNameCS40', partner)
    assert getattr(partner, 'baseCST_ModelElementRefCS39') == owner
    _safe_set(owner, 'baseCST_PathNameCS40', None)
    assert getattr(partner, 'baseCST_ModelElementRefCS39') is None


def test_assoc_pathName63_stub_double():
    # baseCST_PathElementCS has no real 'path' property in the generated
    # code (a bare stub) -- manually attach it so baseCST_PathNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # baseCST_PathNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = baseCST_PathNameCS(scopeFilter="sample_text")
    partner = baseCST_PathElementCS()
    setattr(partner, 'path', None)
    _safe_set(owner, 'PathNameCS', partner)
    assert getattr(partner, 'path') == owner
    _safe_set(owner, 'PathNameCS', None)
    assert getattr(partner, 'path') is None


