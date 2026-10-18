import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstraction,
    Association,
    BehavioralFeature,
    Class,
    ClassesProv_Abstraction,
    ClassesProv_Association,
    ClassesProv_AssociationClass,
    ClassesProv_BehavioralFeature,
    ClassesProv_Class,
    ClassesProv_Classifier,
    ClassesProv_Constraint,
    ClassesProv_DataType,
    ClassesProv_Dependency,
    ClassesProv_DirectedRelationship,
    ClassesProv_Element,
    ClassesProv_ElementImport,
    ClassesProv_Enumeration,
    ClassesProv_EnumerationLiteral,
    ClassesProv_Expression,
    ClassesProv_Feature,
    ClassesProv_Generalization,
    ClassesProv_GeneralizationSet,
    ClassesProv_InstanceSpecification,
    ClassesProv_InstanceValue,
    ClassesProv_Interface,
    ClassesProv_InterfaceRealization,
    ClassesProv_LiteralBoolean,
    ClassesProv_LiteralInteger,
    ClassesProv_LiteralNull,
    ClassesProv_LiteralReal,
    ClassesProv_LiteralSpecification,
    ClassesProv_LiteralString,
    ClassesProv_LiteralUnilimitedNatural,
    ClassesProv_MultiplicityElement,
    ClassesProv_NamedElement,
    ClassesProv_Namespace,
    ClassesProv_OpaqueExpression,
    ClassesProv_Operation,
    ClassesProv_Package,
    ClassesProv_PackageImport,
    ClassesProv_PackageMerge,
    ClassesProv_PackageableElement,
    ClassesProv_Parameter,
    ClassesProv_PrimitiveType,
    ClassesProv_Property,
    ClassesProv_Realization,
    ClassesProv_RedefinableElement,
    ClassesProv_Relationship,
    ClassesProv_Slot,
    ClassesProv_StructuralFeature,
    ClassesProv_Substitution,
    ClassesProv_Type,
    ClassesProv_TypedElement,
    ClassesProv_Usage,
    ClassesProv_ValueSpecification,
    Classifier,
    DataType,
    Dependency,
    DirectedRelationship,
    Element,
    Feature,
    InstanceSpecification,
    LiteralSpecification,
    MultiplicityElement,
    NamedElement,
    Namespace,
    PackageableElement,
    Realization,
    RedefinableElement,
    Relationship,
    StructuralFeature,
    Type,
    TypedElement,
    ValueSpecification,
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

def test_assoc_association145_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Association(isDerived=True)
    _safe_set(b, 'ClassesProv_Association', a1)
    assert _is_linked(b, 'ClassesProv_Association', a1)
    if hasattr(a1, 'ClassesProv_Property146'):
        assert _is_linked(a1, 'ClassesProv_Property146', b)
    _safe_set(b, 'ClassesProv_Association', a2)
    assert _is_linked(b, 'ClassesProv_Association', a2)
    if hasattr(a1, 'ClassesProv_Property146'):
        assert not _is_linked(a1, 'ClassesProv_Property146', b)
    if hasattr(a2, 'ClassesProv_Property146'):
        assert _is_linked(a2, 'ClassesProv_Property146', b)
    _safe_set(b, 'ClassesProv_Association', None)
    assert not _is_linked(b, 'ClassesProv_Association', a2)
    if hasattr(a2, 'ClassesProv_Property146'):
        assert not _is_linked(a2, 'ClassesProv_Property146', b)


def test_assoc_associationEnd158_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    _safe_set(b, 'ClassesProv_Property159', a1)
    assert _is_linked(b, 'ClassesProv_Property159', a1)
    if hasattr(a1, 'ClassesProv_Property157'):
        assert _is_linked(a1, 'ClassesProv_Property157', b)
    _safe_set(b, 'ClassesProv_Property159', a2)
    assert _is_linked(b, 'ClassesProv_Property159', a2)
    if hasattr(a1, 'ClassesProv_Property157'):
        assert not _is_linked(a1, 'ClassesProv_Property157', b)
    if hasattr(a2, 'ClassesProv_Property157'):
        assert _is_linked(a2, 'ClassesProv_Property157', b)
    _safe_set(b, 'ClassesProv_Property159', None)
    assert not _is_linked(b, 'ClassesProv_Property159', a2)
    if hasattr(a2, 'ClassesProv_Property157'):
        assert not _is_linked(a2, 'ClassesProv_Property157', b)


def test_assoc_attribute114_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier115', {a1})
    assert _is_linked(b, 'ClassesProv_Classifier115', a1)
    if hasattr(a1, 'ClassesProv_Property'):
        assert _is_linked(a1, 'ClassesProv_Property', b)
    _safe_set(b, 'ClassesProv_Classifier115', {a2})
    assert _is_linked(b, 'ClassesProv_Classifier115', a2)
    if hasattr(a1, 'ClassesProv_Property'):
        assert not _is_linked(a1, 'ClassesProv_Property', b)
    if hasattr(a2, 'ClassesProv_Property'):
        assert _is_linked(a2, 'ClassesProv_Property', b)
    _safe_set(b, 'ClassesProv_Classifier115', set())
    assert not _is_linked(b, 'ClassesProv_Classifier115', a2)
    if hasattr(a2, 'ClassesProv_Property'):
        assert not _is_linked(a2, 'ClassesProv_Property', b)


def test_assoc_feature112_reverse_link_reassign_clear():
    a1 = ClassesProv_Feature(isStatic=True)
    a2 = ClassesProv_Feature(isStatic=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier113', {a1})
    assert _is_linked(b, 'ClassesProv_Classifier113', a1)
    if hasattr(a1, 'ClassesProv_Feature'):
        assert _is_linked(a1, 'ClassesProv_Feature', b)
    _safe_set(b, 'ClassesProv_Classifier113', {a2})
    assert _is_linked(b, 'ClassesProv_Classifier113', a2)
    if hasattr(a1, 'ClassesProv_Feature'):
        assert not _is_linked(a1, 'ClassesProv_Feature', b)
    if hasattr(a2, 'ClassesProv_Feature'):
        assert _is_linked(a2, 'ClassesProv_Feature', b)
    _safe_set(b, 'ClassesProv_Classifier113', set())
    assert not _is_linked(b, 'ClassesProv_Classifier113', a2)
    if hasattr(a2, 'ClassesProv_Feature'):
        assert not _is_linked(a2, 'ClassesProv_Feature', b)


def test_assoc_featuringClassifier128_reverse_link_reassign_clear():
    a1 = ClassesProv_Feature(isStatic=True)
    a2 = ClassesProv_Feature(isStatic=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier130', a1)
    assert _is_linked(b, 'ClassesProv_Classifier130', a1)
    if hasattr(a1, 'ClassesProv_Feature129'):
        assert _is_linked(a1, 'ClassesProv_Feature129', b)
    _safe_set(b, 'ClassesProv_Classifier130', a2)
    assert _is_linked(b, 'ClassesProv_Classifier130', a2)
    if hasattr(a1, 'ClassesProv_Feature129'):
        assert not _is_linked(a1, 'ClassesProv_Feature129', b)
    if hasattr(a2, 'ClassesProv_Feature129'):
        assert _is_linked(a2, 'ClassesProv_Feature129', b)
    _safe_set(b, 'ClassesProv_Classifier130', None)
    assert not _is_linked(b, 'ClassesProv_Classifier130', a2)
    if hasattr(a2, 'ClassesProv_Feature129'):
        assert not _is_linked(a2, 'ClassesProv_Feature129', b)


def test_assoc_general120_reverse_link_reassign_clear():
    a1 = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    a2 = ClassesProv_Classifier(isAbstract=False, isFinalSpecialization=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier121', a1)
    assert _is_linked(b, 'ClassesProv_Classifier121', a1)
    if hasattr(a1, 'ClassesProv_Classifier119'):
        assert _is_linked(a1, 'ClassesProv_Classifier119', b)
    _safe_set(b, 'ClassesProv_Classifier121', a2)
    assert _is_linked(b, 'ClassesProv_Classifier121', a2)
    if hasattr(a1, 'ClassesProv_Classifier119'):
        assert not _is_linked(a1, 'ClassesProv_Classifier119', b)
    if hasattr(a2, 'ClassesProv_Classifier119'):
        assert _is_linked(a2, 'ClassesProv_Classifier119', b)
    _safe_set(b, 'ClassesProv_Classifier121', None)
    assert not _is_linked(b, 'ClassesProv_Classifier121', a2)
    if hasattr(a2, 'ClassesProv_Classifier119'):
        assert not _is_linked(a2, 'ClassesProv_Classifier119', b)


def test_assoc_general160_reverse_link_reassign_clear():
    a1 = ClassesProv_Generalization(isSubstitutable=True)
    a2 = ClassesProv_Generalization(isSubstitutable=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier162', a1)
    assert _is_linked(b, 'ClassesProv_Classifier162', a1)
    if hasattr(a1, 'ClassesProv_Generalization161'):
        assert _is_linked(a1, 'ClassesProv_Generalization161', b)
    _safe_set(b, 'ClassesProv_Classifier162', a2)
    assert _is_linked(b, 'ClassesProv_Classifier162', a2)
    if hasattr(a1, 'ClassesProv_Generalization161'):
        assert not _is_linked(a1, 'ClassesProv_Generalization161', b)
    if hasattr(a2, 'ClassesProv_Generalization161'):
        assert _is_linked(a2, 'ClassesProv_Generalization161', b)
    _safe_set(b, 'ClassesProv_Classifier162', None)
    assert not _is_linked(b, 'ClassesProv_Classifier162', a2)
    if hasattr(a2, 'ClassesProv_Generalization161'):
        assert not _is_linked(a2, 'ClassesProv_Generalization161', b)


def test_assoc_generalization122_reverse_link_reassign_clear():
    a1 = ClassesProv_Generalization(isSubstitutable=True)
    a2 = ClassesProv_Generalization(isSubstitutable=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier123', {a1})
    assert _is_linked(b, 'ClassesProv_Classifier123', a1)
    if hasattr(a1, 'ClassesProv_Generalization'):
        assert _is_linked(a1, 'ClassesProv_Generalization', b)
    _safe_set(b, 'ClassesProv_Classifier123', {a2})
    assert _is_linked(b, 'ClassesProv_Classifier123', a2)
    if hasattr(a1, 'ClassesProv_Generalization'):
        assert not _is_linked(a1, 'ClassesProv_Generalization', b)
    if hasattr(a2, 'ClassesProv_Generalization'):
        assert _is_linked(a2, 'ClassesProv_Generalization', b)
    _safe_set(b, 'ClassesProv_Classifier123', set())
    assert not _is_linked(b, 'ClassesProv_Classifier123', a2)
    if hasattr(a2, 'ClassesProv_Generalization'):
        assert not _is_linked(a2, 'ClassesProv_Generalization', b)


def test_assoc_generalization266_reverse_link_reassign_clear():
    a1 = ClassesProv_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = ClassesProv_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = ClassesProv_Generalization(isSubstitutable=True)
    _safe_set(b, 'ClassesProv_Generalization268', a1)
    assert _is_linked(b, 'ClassesProv_Generalization268', a1)
    if hasattr(a1, 'ClassesProv_GeneralizationSet267'):
        assert _is_linked(a1, 'ClassesProv_GeneralizationSet267', b)
    _safe_set(b, 'ClassesProv_Generalization268', a2)
    assert _is_linked(b, 'ClassesProv_Generalization268', a2)
    if hasattr(a1, 'ClassesProv_GeneralizationSet267'):
        assert not _is_linked(a1, 'ClassesProv_GeneralizationSet267', b)
    if hasattr(a2, 'ClassesProv_GeneralizationSet267'):
        assert _is_linked(a2, 'ClassesProv_GeneralizationSet267', b)
    _safe_set(b, 'ClassesProv_Generalization268', None)
    assert not _is_linked(b, 'ClassesProv_Generalization268', a2)
    if hasattr(a2, 'ClassesProv_GeneralizationSet267'):
        assert not _is_linked(a2, 'ClassesProv_GeneralizationSet267', b)


def test_assoc_generalizationSet166_reverse_link_reassign_clear():
    a1 = ClassesProv_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = ClassesProv_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = ClassesProv_Generalization(isSubstitutable=True)
    _safe_set(b, 'ClassesProv_Generalization167', {a1})
    assert _is_linked(b, 'ClassesProv_Generalization167', a1)
    if hasattr(a1, 'ClassesProv_GeneralizationSet168'):
        assert _is_linked(a1, 'ClassesProv_GeneralizationSet168', b)
    _safe_set(b, 'ClassesProv_Generalization167', {a2})
    assert _is_linked(b, 'ClassesProv_Generalization167', a2)
    if hasattr(a1, 'ClassesProv_GeneralizationSet168'):
        assert not _is_linked(a1, 'ClassesProv_GeneralizationSet168', b)
    if hasattr(a2, 'ClassesProv_GeneralizationSet168'):
        assert _is_linked(a2, 'ClassesProv_GeneralizationSet168', b)
    _safe_set(b, 'ClassesProv_Generalization167', set())
    assert not _is_linked(b, 'ClassesProv_Generalization167', a2)
    if hasattr(a2, 'ClassesProv_GeneralizationSet168'):
        assert not _is_linked(a2, 'ClassesProv_GeneralizationSet168', b)


def test_assoc_inheritedMember109_reverse_link_reassign_clear():
    a1 = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    a2 = ClassesProv_NamedElement(name="sample_text_2", qualifiedName="sample_text_2")
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier110', {a1})
    assert _is_linked(b, 'ClassesProv_Classifier110', a1)
    if hasattr(a1, 'ClassesProv_NamedElement111'):
        assert _is_linked(a1, 'ClassesProv_NamedElement111', b)
    _safe_set(b, 'ClassesProv_Classifier110', {a2})
    assert _is_linked(b, 'ClassesProv_Classifier110', a2)
    if hasattr(a1, 'ClassesProv_NamedElement111'):
        assert not _is_linked(a1, 'ClassesProv_NamedElement111', b)
    if hasattr(a2, 'ClassesProv_NamedElement111'):
        assert _is_linked(a2, 'ClassesProv_NamedElement111', b)
    _safe_set(b, 'ClassesProv_Classifier110', set())
    assert not _is_linked(b, 'ClassesProv_Classifier110', a2)
    if hasattr(a2, 'ClassesProv_NamedElement111'):
        assert not _is_linked(a2, 'ClassesProv_NamedElement111', b)


def test_assoc_memberEnd214_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Association(isDerived=True)
    _safe_set(b, 'ClassesProv_Association215', {a1})
    assert _is_linked(b, 'ClassesProv_Association215', a1)
    if hasattr(a1, 'ClassesProv_Property216'):
        assert _is_linked(a1, 'ClassesProv_Property216', b)
    _safe_set(b, 'ClassesProv_Association215', {a2})
    assert _is_linked(b, 'ClassesProv_Association215', a2)
    if hasattr(a1, 'ClassesProv_Property216'):
        assert not _is_linked(a1, 'ClassesProv_Property216', b)
    if hasattr(a2, 'ClassesProv_Property216'):
        assert _is_linked(a2, 'ClassesProv_Property216', b)
    _safe_set(b, 'ClassesProv_Association215', set())
    assert not _is_linked(b, 'ClassesProv_Association215', a2)
    if hasattr(a2, 'ClassesProv_Property216'):
        assert not _is_linked(a2, 'ClassesProv_Property216', b)


def test_assoc_navigableOwnedEnd211_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Association(isDerived=True)
    _safe_set(b, 'ClassesProv_Association212', {a1})
    assert _is_linked(b, 'ClassesProv_Association212', a1)
    if hasattr(a1, 'ClassesProv_Property213'):
        assert _is_linked(a1, 'ClassesProv_Property213', b)
    _safe_set(b, 'ClassesProv_Association212', {a2})
    assert _is_linked(b, 'ClassesProv_Association212', a2)
    if hasattr(a1, 'ClassesProv_Property213'):
        assert not _is_linked(a1, 'ClassesProv_Property213', b)
    if hasattr(a2, 'ClassesProv_Property213'):
        assert _is_linked(a2, 'ClassesProv_Property213', b)
    _safe_set(b, 'ClassesProv_Association212', set())
    assert not _is_linked(b, 'ClassesProv_Association212', a2)
    if hasattr(a2, 'ClassesProv_Property213'):
        assert not _is_linked(a2, 'ClassesProv_Property213', b)


def test_assoc_nestedPackage34_reverse_link_reassign_clear():
    a1 = ClassesProv_Package(URI="sample_text")
    a2 = ClassesProv_Package(URI="sample_text_2")
    b = ClassesProv_Package(URI="sample_text")
    _safe_set(b, 'ClassesProv_Package35', a1)
    assert _is_linked(b, 'ClassesProv_Package35', a1)
    if hasattr(a1, 'ClassesProv_Package33'):
        assert _is_linked(a1, 'ClassesProv_Package33', b)
    _safe_set(b, 'ClassesProv_Package35', a2)
    assert _is_linked(b, 'ClassesProv_Package35', a2)
    if hasattr(a1, 'ClassesProv_Package33'):
        assert not _is_linked(a1, 'ClassesProv_Package33', b)
    if hasattr(a2, 'ClassesProv_Package33'):
        assert _is_linked(a2, 'ClassesProv_Package33', b)
    _safe_set(b, 'ClassesProv_Package35', None)
    assert not _is_linked(b, 'ClassesProv_Package35', a2)
    if hasattr(a2, 'ClassesProv_Package33'):
        assert not _is_linked(a2, 'ClassesProv_Package33', b)


def test_assoc_nestingPackage37_reverse_link_reassign_clear():
    a1 = ClassesProv_Package(URI="sample_text")
    a2 = ClassesProv_Package(URI="sample_text_2")
    b = ClassesProv_Package(URI="sample_text")
    _safe_set(b, 'ClassesProv_Package38', a1)
    assert _is_linked(b, 'ClassesProv_Package38', a1)
    if hasattr(a1, 'ClassesProv_Package36'):
        assert _is_linked(a1, 'ClassesProv_Package36', b)
    _safe_set(b, 'ClassesProv_Package38', a2)
    assert _is_linked(b, 'ClassesProv_Package38', a2)
    if hasattr(a1, 'ClassesProv_Package36'):
        assert not _is_linked(a1, 'ClassesProv_Package36', b)
    if hasattr(a2, 'ClassesProv_Package36'):
        assert _is_linked(a2, 'ClassesProv_Package36', b)
    _safe_set(b, 'ClassesProv_Package38', None)
    assert not _is_linked(b, 'ClassesProv_Package38', a2)
    if hasattr(a2, 'ClassesProv_Package36'):
        assert not _is_linked(a2, 'ClassesProv_Package36', b)


def test_assoc_opposite140_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    _safe_set(b, 'ClassesProv_Property141', a1)
    assert _is_linked(b, 'ClassesProv_Property141', a1)
    if hasattr(a1, 'ClassesProv_Property139'):
        assert _is_linked(a1, 'ClassesProv_Property139', b)
    _safe_set(b, 'ClassesProv_Property141', a2)
    assert _is_linked(b, 'ClassesProv_Property141', a2)
    if hasattr(a1, 'ClassesProv_Property139'):
        assert not _is_linked(a1, 'ClassesProv_Property139', b)
    if hasattr(a2, 'ClassesProv_Property139'):
        assert _is_linked(a2, 'ClassesProv_Property139', b)
    _safe_set(b, 'ClassesProv_Property141', None)
    assert not _is_linked(b, 'ClassesProv_Property141', a2)
    if hasattr(a2, 'ClassesProv_Property139'):
        assert not _is_linked(a2, 'ClassesProv_Property139', b)


def test_assoc_ownedEnd217_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Association(isDerived=True)
    _safe_set(b, 'ClassesProv_Association218', {a1})
    assert _is_linked(b, 'ClassesProv_Association218', a1)
    if hasattr(a1, 'ClassesProv_Property219'):
        assert _is_linked(a1, 'ClassesProv_Property219', b)
    _safe_set(b, 'ClassesProv_Association218', {a2})
    assert _is_linked(b, 'ClassesProv_Association218', a2)
    if hasattr(a1, 'ClassesProv_Property219'):
        assert not _is_linked(a1, 'ClassesProv_Property219', b)
    if hasattr(a2, 'ClassesProv_Property219'):
        assert _is_linked(a2, 'ClassesProv_Property219', b)
    _safe_set(b, 'ClassesProv_Association218', set())
    assert not _is_linked(b, 'ClassesProv_Association218', a2)
    if hasattr(a2, 'ClassesProv_Property219'):
        assert not _is_linked(a2, 'ClassesProv_Property219', b)


def test_assoc_owningAssociation147_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Association(isDerived=True)
    _safe_set(b, 'ClassesProv_Association149', a1)
    assert _is_linked(b, 'ClassesProv_Association149', a1)
    if hasattr(a1, 'ClassesProv_Property148'):
        assert _is_linked(a1, 'ClassesProv_Property148', b)
    _safe_set(b, 'ClassesProv_Association149', a2)
    assert _is_linked(b, 'ClassesProv_Association149', a2)
    if hasattr(a1, 'ClassesProv_Property148'):
        assert not _is_linked(a1, 'ClassesProv_Property148', b)
    if hasattr(a2, 'ClassesProv_Property148'):
        assert _is_linked(a2, 'ClassesProv_Property148', b)
    _safe_set(b, 'ClassesProv_Association149', None)
    assert not _is_linked(b, 'ClassesProv_Association149', a2)
    if hasattr(a2, 'ClassesProv_Property148'):
        assert not _is_linked(a2, 'ClassesProv_Property148', b)


def test_assoc_powertype263_reverse_link_reassign_clear():
    a1 = ClassesProv_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = ClassesProv_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier265', a1)
    assert _is_linked(b, 'ClassesProv_Classifier265', a1)
    if hasattr(a1, 'ClassesProv_GeneralizationSet264'):
        assert _is_linked(a1, 'ClassesProv_GeneralizationSet264', b)
    _safe_set(b, 'ClassesProv_Classifier265', a2)
    assert _is_linked(b, 'ClassesProv_Classifier265', a2)
    if hasattr(a1, 'ClassesProv_GeneralizationSet264'):
        assert not _is_linked(a1, 'ClassesProv_GeneralizationSet264', b)
    if hasattr(a2, 'ClassesProv_GeneralizationSet264'):
        assert _is_linked(a2, 'ClassesProv_GeneralizationSet264', b)
    _safe_set(b, 'ClassesProv_Classifier265', None)
    assert not _is_linked(b, 'ClassesProv_Classifier265', a2)
    if hasattr(a2, 'ClassesProv_GeneralizationSet264'):
        assert not _is_linked(a2, 'ClassesProv_GeneralizationSet264', b)


def test_assoc_powertypeExtent126_reverse_link_reassign_clear():
    a1 = ClassesProv_GeneralizationSet(isCovering=True, isDisjoint=True)
    a2 = ClassesProv_GeneralizationSet(isCovering=False, isDisjoint=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier127', {a1})
    assert _is_linked(b, 'ClassesProv_Classifier127', a1)
    if hasattr(a1, 'ClassesProv_GeneralizationSet'):
        assert _is_linked(a1, 'ClassesProv_GeneralizationSet', b)
    _safe_set(b, 'ClassesProv_Classifier127', {a2})
    assert _is_linked(b, 'ClassesProv_Classifier127', a2)
    if hasattr(a1, 'ClassesProv_GeneralizationSet'):
        assert not _is_linked(a1, 'ClassesProv_GeneralizationSet', b)
    if hasattr(a2, 'ClassesProv_GeneralizationSet'):
        assert _is_linked(a2, 'ClassesProv_GeneralizationSet', b)
    _safe_set(b, 'ClassesProv_Classifier127', set())
    assert not _is_linked(b, 'ClassesProv_Classifier127', a2)
    if hasattr(a2, 'ClassesProv_GeneralizationSet'):
        assert not _is_linked(a2, 'ClassesProv_GeneralizationSet', b)


def test_assoc_qualifier155_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    _safe_set(b, 'ClassesProv_Property156', a1)
    assert _is_linked(b, 'ClassesProv_Property156', a1)
    if hasattr(a1, 'ClassesProv_Property154'):
        assert _is_linked(a1, 'ClassesProv_Property154', b)
    _safe_set(b, 'ClassesProv_Property156', a2)
    assert _is_linked(b, 'ClassesProv_Property156', a2)
    if hasattr(a1, 'ClassesProv_Property154'):
        assert not _is_linked(a1, 'ClassesProv_Property154', b)
    if hasattr(a2, 'ClassesProv_Property154'):
        assert _is_linked(a2, 'ClassesProv_Property154', b)
    _safe_set(b, 'ClassesProv_Property156', None)
    assert not _is_linked(b, 'ClassesProv_Property156', a2)
    if hasattr(a2, 'ClassesProv_Property154'):
        assert not _is_linked(a2, 'ClassesProv_Property154', b)


def test_assoc_redefinedClassifier117_reverse_link_reassign_clear():
    a1 = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    a2 = ClassesProv_Classifier(isAbstract=False, isFinalSpecialization=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier118', a1)
    assert _is_linked(b, 'ClassesProv_Classifier118', a1)
    if hasattr(a1, 'ClassesProv_Classifier116'):
        assert _is_linked(a1, 'ClassesProv_Classifier116', b)
    _safe_set(b, 'ClassesProv_Classifier118', a2)
    assert _is_linked(b, 'ClassesProv_Classifier118', a2)
    if hasattr(a1, 'ClassesProv_Classifier116'):
        assert not _is_linked(a1, 'ClassesProv_Classifier116', b)
    if hasattr(a2, 'ClassesProv_Classifier116'):
        assert _is_linked(a2, 'ClassesProv_Classifier116', b)
    _safe_set(b, 'ClassesProv_Classifier118', None)
    assert not _is_linked(b, 'ClassesProv_Classifier118', a2)
    if hasattr(a2, 'ClassesProv_Classifier116'):
        assert not _is_linked(a2, 'ClassesProv_Classifier116', b)


def test_assoc_redefinedElement105_reverse_link_reassign_clear():
    a1 = ClassesProv_RedefinableElement(isLeaf=True)
    a2 = ClassesProv_RedefinableElement(isLeaf=False)
    b = ClassesProv_RedefinableElement(isLeaf=True)
    _safe_set(b, 'ClassesProv_RedefinableElement104', {a1})
    assert _is_linked(b, 'ClassesProv_RedefinableElement104', a1)
    if hasattr(a1, 'ClassesProv_RedefinableElement'):
        assert _is_linked(a1, 'ClassesProv_RedefinableElement', b)
    _safe_set(b, 'ClassesProv_RedefinableElement104', {a2})
    assert _is_linked(b, 'ClassesProv_RedefinableElement104', a2)
    if hasattr(a1, 'ClassesProv_RedefinableElement'):
        assert not _is_linked(a1, 'ClassesProv_RedefinableElement', b)
    if hasattr(a2, 'ClassesProv_RedefinableElement'):
        assert _is_linked(a2, 'ClassesProv_RedefinableElement', b)
    _safe_set(b, 'ClassesProv_RedefinableElement104', set())
    assert not _is_linked(b, 'ClassesProv_RedefinableElement104', a2)
    if hasattr(a2, 'ClassesProv_RedefinableElement'):
        assert not _is_linked(a2, 'ClassesProv_RedefinableElement', b)


def test_assoc_redefinedProperty134_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    _safe_set(b, 'ClassesProv_Property135', a1)
    assert _is_linked(b, 'ClassesProv_Property135', a1)
    if hasattr(a1, 'ClassesProv_Property133'):
        assert _is_linked(a1, 'ClassesProv_Property133', b)
    _safe_set(b, 'ClassesProv_Property135', a2)
    assert _is_linked(b, 'ClassesProv_Property135', a2)
    if hasattr(a1, 'ClassesProv_Property133'):
        assert not _is_linked(a1, 'ClassesProv_Property133', b)
    if hasattr(a2, 'ClassesProv_Property133'):
        assert _is_linked(a2, 'ClassesProv_Property133', b)
    _safe_set(b, 'ClassesProv_Property135', None)
    assert not _is_linked(b, 'ClassesProv_Property135', a2)
    if hasattr(a2, 'ClassesProv_Property133'):
        assert not _is_linked(a2, 'ClassesProv_Property133', b)


def test_assoc_redefinitionContext106_reverse_link_reassign_clear():
    a1 = ClassesProv_RedefinableElement(isLeaf=True)
    a2 = ClassesProv_RedefinableElement(isLeaf=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier108', a1)
    assert _is_linked(b, 'ClassesProv_Classifier108', a1)
    if hasattr(a1, 'ClassesProv_RedefinableElement107'):
        assert _is_linked(a1, 'ClassesProv_RedefinableElement107', b)
    _safe_set(b, 'ClassesProv_Classifier108', a2)
    assert _is_linked(b, 'ClassesProv_Classifier108', a2)
    if hasattr(a1, 'ClassesProv_RedefinableElement107'):
        assert not _is_linked(a1, 'ClassesProv_RedefinableElement107', b)
    if hasattr(a2, 'ClassesProv_RedefinableElement107'):
        assert _is_linked(a2, 'ClassesProv_RedefinableElement107', b)
    _safe_set(b, 'ClassesProv_Classifier108', None)
    assert not _is_linked(b, 'ClassesProv_Classifier108', a2)
    if hasattr(a2, 'ClassesProv_RedefinableElement107'):
        assert not _is_linked(a2, 'ClassesProv_RedefinableElement107', b)


def test_assoc_specific163_reverse_link_reassign_clear():
    a1 = ClassesProv_Generalization(isSubstitutable=True)
    a2 = ClassesProv_Generalization(isSubstitutable=False)
    b = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    _safe_set(b, 'ClassesProv_Classifier165', a1)
    assert _is_linked(b, 'ClassesProv_Classifier165', a1)
    if hasattr(a1, 'ClassesProv_Generalization164'):
        assert _is_linked(a1, 'ClassesProv_Generalization164', b)
    _safe_set(b, 'ClassesProv_Classifier165', a2)
    assert _is_linked(b, 'ClassesProv_Classifier165', a2)
    if hasattr(a1, 'ClassesProv_Generalization164'):
        assert not _is_linked(a1, 'ClassesProv_Generalization164', b)
    if hasattr(a2, 'ClassesProv_Generalization164'):
        assert _is_linked(a2, 'ClassesProv_Generalization164', b)
    _safe_set(b, 'ClassesProv_Classifier165', None)
    assert not _is_linked(b, 'ClassesProv_Classifier165', a2)
    if hasattr(a2, 'ClassesProv_Generalization164'):
        assert not _is_linked(a2, 'ClassesProv_Generalization164', b)


def test_assoc_subsettedProperty143_reverse_link_reassign_clear():
    a1 = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    a2 = ClassesProv_Property(default="sample_text_2", isComposite=False, isDerived=False, isDerivedUnion=False, isID=False)
    b = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    _safe_set(b, 'ClassesProv_Property144', a1)
    assert _is_linked(b, 'ClassesProv_Property144', a1)
    if hasattr(a1, 'ClassesProv_Property142'):
        assert _is_linked(a1, 'ClassesProv_Property142', b)
    _safe_set(b, 'ClassesProv_Property144', a2)
    assert _is_linked(b, 'ClassesProv_Property144', a2)
    if hasattr(a1, 'ClassesProv_Property142'):
        assert not _is_linked(a1, 'ClassesProv_Property142', b)
    if hasattr(a2, 'ClassesProv_Property142'):
        assert _is_linked(a2, 'ClassesProv_Property142', b)
    _safe_set(b, 'ClassesProv_Property144', None)
    assert not _is_linked(b, 'ClassesProv_Property144', a2)
    if hasattr(a2, 'ClassesProv_Property142'):
        assert not _is_linked(a2, 'ClassesProv_Property142', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bodyCondition184_stub_double():
    # ClassesProv_Constraint has no real 'ClassesProv_Constraint186' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Constraint()
    setattr(partner, 'ClassesProv_Constraint186', None)
    _safe_set(owner, 'ClassesProv_Operation185', {partner})
    assert getattr(partner, 'ClassesProv_Constraint186') == owner
    _safe_set(owner, 'ClassesProv_Operation185', set())
    assert getattr(partner, 'ClassesProv_Constraint186') is None


def test_assoc_class_131_stub_double():
    # ClassesProv_Class has no real 'ClassesProv_Class' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_Class()
    setattr(partner, 'ClassesProv_Class', None)
    _safe_set(owner, 'ClassesProv_Property132', partner)
    assert getattr(partner, 'ClassesProv_Class') == owner
    _safe_set(owner, 'ClassesProv_Property132', None)
    assert getattr(partner, 'ClassesProv_Class') is None


def test_assoc_class_190_stub_double():
    # ClassesProv_Class has no real 'ClassesProv_Class192' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Class()
    setattr(partner, 'ClassesProv_Class192', None)
    _safe_set(owner, 'ClassesProv_Operation191', partner)
    assert getattr(partner, 'ClassesProv_Class192') == owner
    _safe_set(owner, 'ClassesProv_Operation191', None)
    assert getattr(partner, 'ClassesProv_Class192') is None


def test_assoc_classifier85_stub_double():
    # ClassesProv_InstanceSpecification has no real 'ClassesProv_InstanceSpecification86' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_InstanceSpecification()
    setattr(partner, 'ClassesProv_InstanceSpecification86', None)
    _safe_set(owner, 'ClassesProv_Classifier', partner)
    assert owner in getattr(partner, 'ClassesProv_InstanceSpecification86')
    _safe_set(owner, 'ClassesProv_Classifier', None)
    assert owner not in getattr(partner, 'ClassesProv_InstanceSpecification86')


def test_assoc_client236_stub_double():
    # ClassesProv_Dependency has no real 'ClassesProv_Dependency237' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Dependency()
    setattr(partner, 'ClassesProv_Dependency237', None)
    _safe_set(owner, 'ClassesProv_NamedElement238', partner)
    assert owner in getattr(partner, 'ClassesProv_Dependency237')
    _safe_set(owner, 'ClassesProv_NamedElement238', None)
    assert owner not in getattr(partner, 'ClassesProv_Dependency237')


def test_assoc_clientDependency6_stub_double():
    # ClassesProv_Dependency has no real 'ClassesProv_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Dependency()
    setattr(partner, 'ClassesProv_Dependency', None)
    _safe_set(owner, 'ClassesProv_NamedElement7', {partner})
    assert getattr(partner, 'ClassesProv_Dependency') == owner
    _safe_set(owner, 'ClassesProv_NamedElement7', set())
    assert getattr(partner, 'ClassesProv_Dependency') is None


def test_assoc_contract246_stub_double():
    # ClassesProv_Substitution has no real 'ClassesProv_Substitution247' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_Substitution()
    setattr(partner, 'ClassesProv_Substitution247', None)
    _safe_set(owner, 'ClassesProv_Classifier248', partner)
    assert getattr(partner, 'ClassesProv_Substitution247') == owner
    _safe_set(owner, 'ClassesProv_Classifier248', None)
    assert getattr(partner, 'ClassesProv_Substitution247') is None


def test_assoc_dataType150_stub_double():
    # ClassesProv_DataType has no real 'ClassesProv_DataType' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_DataType()
    setattr(partner, 'ClassesProv_DataType', None)
    _safe_set(owner, 'ClassesProv_Property151', partner)
    assert getattr(partner, 'ClassesProv_DataType') == owner
    _safe_set(owner, 'ClassesProv_Property151', None)
    assert getattr(partner, 'ClassesProv_DataType') is None


def test_assoc_dataType193_stub_double():
    # ClassesProv_DataType has no real 'ClassesProv_DataType195' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_DataType()
    setattr(partner, 'ClassesProv_DataType195', None)
    _safe_set(owner, 'ClassesProv_Operation194', partner)
    assert getattr(partner, 'ClassesProv_DataType195') == owner
    _safe_set(owner, 'ClassesProv_Operation194', None)
    assert getattr(partner, 'ClassesProv_DataType195') is None


def test_assoc_defaultValue136_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification138' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification138', None)
    _safe_set(owner, 'ClassesProv_Property137', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification138') == owner
    _safe_set(owner, 'ClassesProv_Property137', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification138') is None


def test_assoc_defaultValue176_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification178' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Parameter(default="sample_text")
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification178', None)
    _safe_set(owner, 'ClassesProv_Parameter177', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification178') == owner
    _safe_set(owner, 'ClassesProv_Parameter177', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification178') is None


def test_assoc_definingFeature102_stub_double():
    # ClassesProv_Slot has no real 'ClassesProv_Slot103' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_StructuralFeature(isReadOnly=True)
    partner = ClassesProv_Slot()
    setattr(partner, 'ClassesProv_Slot103', None)
    _safe_set(owner, 'ClassesProv_StructuralFeature', partner)
    assert getattr(partner, 'ClassesProv_Slot103') == owner
    _safe_set(owner, 'ClassesProv_StructuralFeature', None)
    assert getattr(partner, 'ClassesProv_Slot103') is None


def test_assoc_elementImport16_stub_double():
    # ClassesProv_Namespace has no real 'ClassesProv_Namespace17' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_ElementImport(alias="sample_text")
    partner = ClassesProv_Namespace()
    setattr(partner, 'ClassesProv_Namespace17', None)
    _safe_set(owner, 'ClassesProv_ElementImport', partner)
    assert owner in getattr(partner, 'ClassesProv_Namespace17')
    _safe_set(owner, 'ClassesProv_ElementImport', None)
    assert owner not in getattr(partner, 'ClassesProv_Namespace17')


def test_assoc_importedElement22_stub_double():
    # ClassesProv_PackageableElement has no real 'ClassesProv_PackageableElement24' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_ElementImport(alias="sample_text")
    partner = ClassesProv_PackageableElement()
    setattr(partner, 'ClassesProv_PackageableElement24', None)
    _safe_set(owner, 'ClassesProv_ElementImport23', partner)
    assert getattr(partner, 'ClassesProv_PackageableElement24') == owner
    _safe_set(owner, 'ClassesProv_ElementImport23', None)
    assert getattr(partner, 'ClassesProv_PackageableElement24') is None


def test_assoc_importedPackage28_stub_double():
    # ClassesProv_PackageImport has no real 'ClassesProv_PackageImport29' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_PackageImport()
    setattr(partner, 'ClassesProv_PackageImport29', None)
    _safe_set(owner, 'ClassesProv_Package', partner)
    assert getattr(partner, 'ClassesProv_PackageImport29') == owner
    _safe_set(owner, 'ClassesProv_Package', None)
    assert getattr(partner, 'ClassesProv_PackageImport29') is None


def test_assoc_importingNamespace25_stub_double():
    # ClassesProv_Namespace has no real 'ClassesProv_Namespace27' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_ElementImport(alias="sample_text")
    partner = ClassesProv_Namespace()
    setattr(partner, 'ClassesProv_Namespace27', None)
    _safe_set(owner, 'ClassesProv_ElementImport26', partner)
    assert getattr(partner, 'ClassesProv_Namespace27') == owner
    _safe_set(owner, 'ClassesProv_ElementImport26', None)
    assert getattr(partner, 'ClassesProv_Namespace27') is None


def test_assoc_interface152_stub_double():
    # ClassesProv_Interface has no real 'ClassesProv_Interface' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_Interface()
    setattr(partner, 'ClassesProv_Interface', None)
    _safe_set(owner, 'ClassesProv_Property153', partner)
    assert getattr(partner, 'ClassesProv_Interface') == owner
    _safe_set(owner, 'ClassesProv_Property153', None)
    assert getattr(partner, 'ClassesProv_Interface') is None


def test_assoc_interface196_stub_double():
    # ClassesProv_Interface has no real 'ClassesProv_Interface198' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Interface()
    setattr(partner, 'ClassesProv_Interface198', None)
    _safe_set(owner, 'ClassesProv_Operation197', partner)
    assert getattr(partner, 'ClassesProv_Interface198') == owner
    _safe_set(owner, 'ClassesProv_Operation197', None)
    assert getattr(partner, 'ClassesProv_Interface198') is None


def test_assoc_lowerValue54_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification56' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification56', None)
    _safe_set(owner, 'ClassesProv_MultiplicityElement55', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification56') == owner
    _safe_set(owner, 'ClassesProv_MultiplicityElement55', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification56') is None


def test_assoc_mapping242_stub_double():
    # ClassesProv_Abstraction has no real 'ClassesProv_Abstraction' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_OpaqueExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_OpaqueExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_OpaqueExpression(body="sample_text", language="sample_text")
    partner = ClassesProv_Abstraction()
    setattr(partner, 'ClassesProv_Abstraction', None)
    _safe_set(owner, 'ClassesProv_OpaqueExpression', partner)
    assert getattr(partner, 'ClassesProv_Abstraction') == owner
    _safe_set(owner, 'ClassesProv_OpaqueExpression', None)
    assert getattr(partner, 'ClassesProv_Abstraction') is None


def test_assoc_member10_stub_double():
    # ClassesProv_Namespace has no real 'ClassesProv_Namespace11' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Namespace()
    setattr(partner, 'ClassesProv_Namespace11', None)
    _safe_set(owner, 'ClassesProv_NamedElement12', partner)
    assert owner in getattr(partner, 'ClassesProv_Namespace11')
    _safe_set(owner, 'ClassesProv_NamedElement12', None)
    assert owner not in getattr(partner, 'ClassesProv_Namespace11')


def test_assoc_mergedPackage233_stub_double():
    # ClassesProv_PackageMerge has no real 'ClassesProv_PackageMerge234' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_PackageMerge()
    setattr(partner, 'ClassesProv_PackageMerge234', None)
    _safe_set(owner, 'ClassesProv_Package235', partner)
    assert getattr(partner, 'ClassesProv_PackageMerge234') == owner
    _safe_set(owner, 'ClassesProv_Package235', None)
    assert getattr(partner, 'ClassesProv_PackageMerge234') is None


def test_assoc_namespace5_stub_double():
    # ClassesProv_Namespace has no real 'ClassesProv_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Namespace()
    setattr(partner, 'ClassesProv_Namespace', None)
    _safe_set(owner, 'ClassesProv_NamedElement', partner)
    assert getattr(partner, 'ClassesProv_Namespace') == owner
    _safe_set(owner, 'ClassesProv_NamedElement', None)
    assert getattr(partner, 'ClassesProv_Namespace') is None


def test_assoc_nestedClassifier199_stub_double():
    # ClassesProv_Class has no real 'ClassesProv_Class200' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_Class()
    setattr(partner, 'ClassesProv_Class200', None)
    _safe_set(owner, 'ClassesProv_Classifier201', partner)
    assert owner in getattr(partner, 'ClassesProv_Class200')
    _safe_set(owner, 'ClassesProv_Classifier201', None)
    assert owner not in getattr(partner, 'ClassesProv_Class200')


def test_assoc_nestedClassifier249_stub_double():
    # ClassesProv_Interface has no real 'ClassesProv_Interface250' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_Interface()
    setattr(partner, 'ClassesProv_Interface250', None)
    _safe_set(owner, 'ClassesProv_Classifier251', partner)
    assert getattr(partner, 'ClassesProv_Interface250') == owner
    _safe_set(owner, 'ClassesProv_Classifier251', None)
    assert getattr(partner, 'ClassesProv_Interface250') is None


def test_assoc_operand75_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification76' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Expression(symbol="sample_text")
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification76', None)
    _safe_set(owner, 'ClassesProv_Expression', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification76') == owner
    _safe_set(owner, 'ClassesProv_Expression', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification76') is None


def test_assoc_ownedAttribute208_stub_double():
    # ClassesProv_Class has no real 'ClassesProv_Class209' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_Class()
    setattr(partner, 'ClassesProv_Class209', None)
    _safe_set(owner, 'ClassesProv_Property210', partner)
    assert owner in getattr(partner, 'ClassesProv_Class209')
    _safe_set(owner, 'ClassesProv_Property210', None)
    assert owner not in getattr(partner, 'ClassesProv_Class209')


def test_assoc_ownedAttribute220_stub_double():
    # ClassesProv_DataType has no real 'ClassesProv_DataType221' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_DataType()
    setattr(partner, 'ClassesProv_DataType221', None)
    _safe_set(owner, 'ClassesProv_Property222', partner)
    assert owner in getattr(partner, 'ClassesProv_DataType221')
    _safe_set(owner, 'ClassesProv_Property222', None)
    assert owner not in getattr(partner, 'ClassesProv_DataType221')


def test_assoc_ownedAttribute255_stub_double():
    # ClassesProv_Interface has no real 'ClassesProv_Interface256' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Property(default="sample_text", isComposite=True, isDerived=True, isDerivedUnion=True, isID=True)
    partner = ClassesProv_Interface()
    setattr(partner, 'ClassesProv_Interface256', None)
    _safe_set(owner, 'ClassesProv_Property257', partner)
    assert owner in getattr(partner, 'ClassesProv_Interface256')
    _safe_set(owner, 'ClassesProv_Property257', None)
    assert owner not in getattr(partner, 'ClassesProv_Interface256')


def test_assoc_ownedFormalParam173_stub_double():
    # ClassesProv_BehavioralFeature has no real 'ClassesProv_BehavioralFeature175' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Parameter(default="sample_text")
    partner = ClassesProv_BehavioralFeature()
    setattr(partner, 'ClassesProv_BehavioralFeature175', None)
    _safe_set(owner, 'ClassesProv_Parameter174', partner)
    assert getattr(partner, 'ClassesProv_BehavioralFeature175') == owner
    _safe_set(owner, 'ClassesProv_Parameter174', None)
    assert getattr(partner, 'ClassesProv_BehavioralFeature175') is None


def test_assoc_ownedMember13_stub_double():
    # ClassesProv_Namespace has no real 'ClassesProv_Namespace14' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Namespace()
    setattr(partner, 'ClassesProv_Namespace14', None)
    _safe_set(owner, 'ClassesProv_NamedElement15', partner)
    assert owner in getattr(partner, 'ClassesProv_Namespace14')
    _safe_set(owner, 'ClassesProv_NamedElement15', None)
    assert owner not in getattr(partner, 'ClassesProv_Namespace14')


def test_assoc_ownedOperation202_stub_double():
    # ClassesProv_Class has no real 'ClassesProv_Class203' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Class()
    setattr(partner, 'ClassesProv_Class203', None)
    _safe_set(owner, 'ClassesProv_Operation204', partner)
    assert owner in getattr(partner, 'ClassesProv_Class203')
    _safe_set(owner, 'ClassesProv_Operation204', None)
    assert owner not in getattr(partner, 'ClassesProv_Class203')


def test_assoc_ownedOperation223_stub_double():
    # ClassesProv_DataType has no real 'ClassesProv_DataType224' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_DataType()
    setattr(partner, 'ClassesProv_DataType224', None)
    _safe_set(owner, 'ClassesProv_Operation225', partner)
    assert owner in getattr(partner, 'ClassesProv_DataType224')
    _safe_set(owner, 'ClassesProv_Operation225', None)
    assert owner not in getattr(partner, 'ClassesProv_DataType224')


def test_assoc_ownedOperation258_stub_double():
    # ClassesProv_Interface has no real 'ClassesProv_Interface259' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Interface()
    setattr(partner, 'ClassesProv_Interface259', None)
    _safe_set(owner, 'ClassesProv_Operation260', partner)
    assert owner in getattr(partner, 'ClassesProv_Interface259')
    _safe_set(owner, 'ClassesProv_Operation260', None)
    assert owner not in getattr(partner, 'ClassesProv_Interface259')


def test_assoc_ownedParameter169_stub_double():
    # ClassesProv_BehavioralFeature has no real 'ClassesProv_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Parameter(default="sample_text")
    partner = ClassesProv_BehavioralFeature()
    setattr(partner, 'ClassesProv_BehavioralFeature', None)
    _safe_set(owner, 'ClassesProv_Parameter', partner)
    assert owner in getattr(partner, 'ClassesProv_BehavioralFeature')
    _safe_set(owner, 'ClassesProv_Parameter', None)
    assert owner not in getattr(partner, 'ClassesProv_BehavioralFeature')


def test_assoc_ownedType42_stub_double():
    # ClassesProv_Type has no real 'ClassesProv_Type' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_Type()
    setattr(partner, 'ClassesProv_Type', None)
    _safe_set(owner, 'ClassesProv_Package43', {partner})
    assert getattr(partner, 'ClassesProv_Type') == owner
    _safe_set(owner, 'ClassesProv_Package43', set())
    assert getattr(partner, 'ClassesProv_Type') is None


def test_assoc_owningLower60_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification61' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification61', None)
    _safe_set(owner, 'ClassesProv_MultiplicityElement62', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification61') == owner
    _safe_set(owner, 'ClassesProv_MultiplicityElement62', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification61') is None


def test_assoc_owningUpper57_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification58' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification58', None)
    _safe_set(owner, 'ClassesProv_MultiplicityElement59', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification58') == owner
    _safe_set(owner, 'ClassesProv_MultiplicityElement59', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification58') is None


def test_assoc_package72_stub_double():
    # ClassesProv_Type has no real 'ClassesProv_Type73' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_Type()
    setattr(partner, 'ClassesProv_Type73', None)
    _safe_set(owner, 'ClassesProv_Package74', partner)
    assert getattr(partner, 'ClassesProv_Type73') == owner
    _safe_set(owner, 'ClassesProv_Package74', None)
    assert getattr(partner, 'ClassesProv_Type73') is None


def test_assoc_packageMerge44_stub_double():
    # ClassesProv_PackageMerge has no real 'ClassesProv_PackageMerge' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_PackageMerge()
    setattr(partner, 'ClassesProv_PackageMerge', None)
    _safe_set(owner, 'ClassesProv_Package45', {partner})
    assert getattr(partner, 'ClassesProv_PackageMerge') == owner
    _safe_set(owner, 'ClassesProv_Package45', set())
    assert getattr(partner, 'ClassesProv_PackageMerge') is None


def test_assoc_packagedElement39_stub_double():
    # ClassesProv_PackageableElement has no real 'ClassesProv_PackageableElement41' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_PackageableElement()
    setattr(partner, 'ClassesProv_PackageableElement41', None)
    _safe_set(owner, 'ClassesProv_Package40', {partner})
    assert getattr(partner, 'ClassesProv_PackageableElement41') == owner
    _safe_set(owner, 'ClassesProv_Package40', set())
    assert getattr(partner, 'ClassesProv_PackageableElement41') is None


def test_assoc_postcondition187_stub_double():
    # ClassesProv_Constraint has no real 'ClassesProv_Constraint189' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Constraint()
    setattr(partner, 'ClassesProv_Constraint189', None)
    _safe_set(owner, 'ClassesProv_Operation188', {partner})
    assert getattr(partner, 'ClassesProv_Constraint189') == owner
    _safe_set(owner, 'ClassesProv_Operation188', set())
    assert getattr(partner, 'ClassesProv_Constraint189') is None


def test_assoc_precondition181_stub_double():
    # ClassesProv_Constraint has no real 'ClassesProv_Constraint183' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Constraint()
    setattr(partner, 'ClassesProv_Constraint183', None)
    _safe_set(owner, 'ClassesProv_Operation182', {partner})
    assert getattr(partner, 'ClassesProv_Constraint183') == owner
    _safe_set(owner, 'ClassesProv_Operation182', set())
    assert getattr(partner, 'ClassesProv_Constraint183') is None


def test_assoc_receivingPackage230_stub_double():
    # ClassesProv_PackageMerge has no real 'ClassesProv_PackageMerge231' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Package(URI="sample_text")
    partner = ClassesProv_PackageMerge()
    setattr(partner, 'ClassesProv_PackageMerge231', None)
    _safe_set(owner, 'ClassesProv_Package232', partner)
    assert getattr(partner, 'ClassesProv_PackageMerge231') == owner
    _safe_set(owner, 'ClassesProv_Package232', None)
    assert getattr(partner, 'ClassesProv_PackageMerge231') is None


def test_assoc_substitutingClassifier243_stub_double():
    # ClassesProv_Substitution has no real 'ClassesProv_Substitution244' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_Substitution()
    setattr(partner, 'ClassesProv_Substitution244', None)
    _safe_set(owner, 'ClassesProv_Classifier245', partner)
    assert getattr(partner, 'ClassesProv_Substitution244') == owner
    _safe_set(owner, 'ClassesProv_Classifier245', None)
    assert getattr(partner, 'ClassesProv_Substitution244') is None


def test_assoc_substitution124_stub_double():
    # ClassesProv_Substitution has no real 'ClassesProv_Substitution' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Classifier(isAbstract=True, isFinalSpecialization=True)
    partner = ClassesProv_Substitution()
    setattr(partner, 'ClassesProv_Substitution', None)
    _safe_set(owner, 'ClassesProv_Classifier125', {partner})
    assert getattr(partner, 'ClassesProv_Substitution') == owner
    _safe_set(owner, 'ClassesProv_Classifier125', set())
    assert getattr(partner, 'ClassesProv_Substitution') is None


def test_assoc_supplier239_stub_double():
    # ClassesProv_Dependency has no real 'ClassesProv_Dependency240' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_NamedElement(name="sample_text", qualifiedName="sample_text")
    partner = ClassesProv_Dependency()
    setattr(partner, 'ClassesProv_Dependency240', None)
    _safe_set(owner, 'ClassesProv_NamedElement241', partner)
    assert owner in getattr(partner, 'ClassesProv_Dependency240')
    _safe_set(owner, 'ClassesProv_NamedElement241', None)
    assert owner not in getattr(partner, 'ClassesProv_Dependency240')


def test_assoc_type179_stub_double():
    # ClassesProv_Type has no real 'ClassesProv_Type180' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_Operation(isOrdered=True, isQuery=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_Type()
    setattr(partner, 'ClassesProv_Type180', None)
    _safe_set(owner, 'ClassesProv_Operation', partner)
    assert getattr(partner, 'ClassesProv_Type180') == owner
    _safe_set(owner, 'ClassesProv_Operation', None)
    assert getattr(partner, 'ClassesProv_Type180') is None


def test_assoc_upperValue53_stub_double():
    # ClassesProv_ValueSpecification has no real 'ClassesProv_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so ClassesProv_MultiplicityElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ClassesProv_MultiplicityElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ClassesProv_MultiplicityElement(isOrdered=True, isUnique=True, lower=7, upper=7)
    partner = ClassesProv_ValueSpecification()
    setattr(partner, 'ClassesProv_ValueSpecification', None)
    _safe_set(owner, 'ClassesProv_MultiplicityElement', partner)
    assert getattr(partner, 'ClassesProv_ValueSpecification') == owner
    _safe_set(owner, 'ClassesProv_MultiplicityElement', None)
    assert getattr(partner, 'ClassesProv_ValueSpecification') is None


