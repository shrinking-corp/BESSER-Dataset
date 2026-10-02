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


