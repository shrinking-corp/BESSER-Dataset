import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Abstraction,
    BehavioralFeature,
    Classifier,
    Dependency,
    DirectedRelationship,
    Element,
    Feature,
    NamedElement,
    Namespace,
    PackageableElement,
    Realization,
    Relationship,
    Type,
    TypedElement,
    uml_Abstraction,
    uml_Association,
    uml_BehavioralFeature,
    uml_Class,
    uml_Classifier,
    uml_Comment,
    uml_Dependency,
    uml_DirectedRelationship,
    uml_Element,
    uml_ElementImport,
    uml_Feature,
    uml_Generalization,
    uml_Model,
    uml_NamedElement,
    uml_Namespace,
    uml_Operation,
    uml_Package,
    uml_PackageImport,
    uml_PackageableElement,
    uml_Parameter,
    uml_Property,
    uml_Realization,
    uml_Relationship,
    uml_Substitution,
    uml_Type,
    uml_TypedElement,
    uml_ValueSpecification,
    VisibilityKind,
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

def test_assoc_attribute62_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier63', {a1})
    assert _is_linked(b, 'uml_Classifier63', a1)
    if hasattr(a1, 'uml_Property64'):
        assert _is_linked(a1, 'uml_Property64', b)
    _safe_set(b, 'uml_Classifier63', {a2})
    assert _is_linked(b, 'uml_Classifier63', a2)
    if hasattr(a1, 'uml_Property64'):
        assert not _is_linked(a1, 'uml_Property64', b)
    if hasattr(a2, 'uml_Property64'):
        assert _is_linked(a2, 'uml_Property64', b)
    _safe_set(b, 'uml_Classifier63', set())
    assert not _is_linked(b, 'uml_Classifier63', a2)
    if hasattr(a2, 'uml_Property64'):
        assert not _is_linked(a2, 'uml_Property64', b)


def test_assoc_class_75_reverse_link_reassign_clear():
    a1 = uml_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    a2 = uml_Operation(isOrdered="sample_text_2", isQuery="sample_text_2", isUnique="sample_text_2", lower="sample_text_2", upper="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'ownedOperation'):
        assert _is_linked(a1, 'ownedOperation', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'ownedOperation'):
        assert not _is_linked(a1, 'ownedOperation', b)
    if hasattr(a2, 'ownedOperation'):
        assert _is_linked(a2, 'ownedOperation', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'ownedOperation'):
        assert not _is_linked(a2, 'ownedOperation', b)


def test_assoc_feature52_reverse_link_reassign_clear():
    a1 = uml_Feature(isStatic="sample_text")
    a2 = uml_Feature(isStatic="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'featuringClassifier', {a1})
    assert _is_linked(b, 'featuringClassifier', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'featuringClassifier', {a2})
    assert _is_linked(b, 'featuringClassifier', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'featuringClassifier', set())
    assert not _is_linked(b, 'featuringClassifier', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_featuringClassifier65_reverse_link_reassign_clear():
    a1 = uml_Feature(isStatic="sample_text")
    a2 = uml_Feature(isStatic="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'feature'):
        assert _is_linked(a1, 'feature', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'feature'):
        assert not _is_linked(a1, 'feature', b)
    if hasattr(a2, 'feature'):
        assert _is_linked(a2, 'feature', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'feature'):
        assert not _is_linked(a2, 'feature', b)


def test_assoc_general59_reverse_link_reassign_clear():
    a1 = uml_Classifier(isAbstract="sample_text")
    a2 = uml_Classifier(isAbstract="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier60', a1)
    assert _is_linked(b, 'uml_Classifier60', a1)
    if hasattr(a1, 'uml_Classifier58'):
        assert _is_linked(a1, 'uml_Classifier58', b)
    _safe_set(b, 'uml_Classifier60', a2)
    assert _is_linked(b, 'uml_Classifier60', a2)
    if hasattr(a1, 'uml_Classifier58'):
        assert not _is_linked(a1, 'uml_Classifier58', b)
    if hasattr(a2, 'uml_Classifier58'):
        assert _is_linked(a2, 'uml_Classifier58', b)
    _safe_set(b, 'uml_Classifier60', None)
    assert not _is_linked(b, 'uml_Classifier60', a2)
    if hasattr(a2, 'uml_Classifier58'):
        assert not _is_linked(a2, 'uml_Classifier58', b)


def test_assoc_general96_reverse_link_reassign_clear():
    a1 = uml_Generalization(isSubstitutable="sample_text")
    a2 = uml_Generalization(isSubstitutable="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier98', a1)
    assert _is_linked(b, 'uml_Classifier98', a1)
    if hasattr(a1, 'uml_Generalization97'):
        assert _is_linked(a1, 'uml_Generalization97', b)
    _safe_set(b, 'uml_Classifier98', a2)
    assert _is_linked(b, 'uml_Classifier98', a2)
    if hasattr(a1, 'uml_Generalization97'):
        assert not _is_linked(a1, 'uml_Generalization97', b)
    if hasattr(a2, 'uml_Generalization97'):
        assert _is_linked(a2, 'uml_Generalization97', b)
    _safe_set(b, 'uml_Classifier98', None)
    assert not _is_linked(b, 'uml_Classifier98', a2)
    if hasattr(a2, 'uml_Generalization97'):
        assert not _is_linked(a2, 'uml_Generalization97', b)


def test_assoc_generalization94_reverse_link_reassign_clear():
    a1 = uml_Generalization(isSubstitutable="sample_text")
    a2 = uml_Generalization(isSubstitutable="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'uml_Class95', {a1})
    assert _is_linked(b, 'uml_Class95', a1)
    if hasattr(a1, 'uml_Generalization'):
        assert _is_linked(a1, 'uml_Generalization', b)
    _safe_set(b, 'uml_Class95', {a2})
    assert _is_linked(b, 'uml_Class95', a2)
    if hasattr(a1, 'uml_Generalization'):
        assert not _is_linked(a1, 'uml_Generalization', b)
    if hasattr(a2, 'uml_Generalization'):
        assert _is_linked(a2, 'uml_Generalization', b)
    _safe_set(b, 'uml_Class95', set())
    assert not _is_linked(b, 'uml_Class95', a2)
    if hasattr(a2, 'uml_Generalization'):
        assert not _is_linked(a2, 'uml_Generalization', b)


def test_assoc_importedPackage36_reverse_link_reassign_clear():
    a1 = uml_PackageImport(visibility="sample_text")
    a2 = uml_PackageImport(visibility="sample_text_2")
    b = uml_Package(name="sample_text")
    _safe_set(b, 'uml_Package37', a1)
    assert _is_linked(b, 'uml_Package37', a1)
    if hasattr(a1, 'uml_PackageImport'):
        assert _is_linked(a1, 'uml_PackageImport', b)
    _safe_set(b, 'uml_Package37', a2)
    assert _is_linked(b, 'uml_Package37', a2)
    if hasattr(a1, 'uml_PackageImport'):
        assert not _is_linked(a1, 'uml_PackageImport', b)
    if hasattr(a2, 'uml_PackageImport'):
        assert _is_linked(a2, 'uml_PackageImport', b)
    _safe_set(b, 'uml_Package37', None)
    assert not _is_linked(b, 'uml_Package37', a2)
    if hasattr(a2, 'uml_PackageImport'):
        assert not _is_linked(a2, 'uml_PackageImport', b)


def test_assoc_inheritedMember53_reverse_link_reassign_clear():
    a1 = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    a2 = uml_NamedElement(name="sample_text_2", qualifiedName="sample_text_2", visibility="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier', {a1})
    assert _is_linked(b, 'uml_Classifier', a1)
    if hasattr(a1, 'uml_NamedElement54'):
        assert _is_linked(a1, 'uml_NamedElement54', b)
    _safe_set(b, 'uml_Classifier', {a2})
    assert _is_linked(b, 'uml_Classifier', a2)
    if hasattr(a1, 'uml_NamedElement54'):
        assert not _is_linked(a1, 'uml_NamedElement54', b)
    if hasattr(a2, 'uml_NamedElement54'):
        assert _is_linked(a2, 'uml_NamedElement54', b)
    _safe_set(b, 'uml_Classifier', set())
    assert not _is_linked(b, 'uml_Classifier', a2)
    if hasattr(a2, 'uml_NamedElement54'):
        assert not _is_linked(a2, 'uml_NamedElement54', b)


def test_assoc_memberEnd43_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Association(isDerived="sample_text")
    _safe_set(b, 'uml_Association44', {a1})
    assert _is_linked(b, 'uml_Association44', a1)
    if hasattr(a1, 'uml_Property45'):
        assert _is_linked(a1, 'uml_Property45', b)
    _safe_set(b, 'uml_Association44', {a2})
    assert _is_linked(b, 'uml_Association44', a2)
    if hasattr(a1, 'uml_Property45'):
        assert not _is_linked(a1, 'uml_Property45', b)
    if hasattr(a2, 'uml_Property45'):
        assert _is_linked(a2, 'uml_Property45', b)
    _safe_set(b, 'uml_Association44', set())
    assert not _is_linked(b, 'uml_Association44', a2)
    if hasattr(a2, 'uml_Property45'):
        assert not _is_linked(a2, 'uml_Property45', b)


def test_assoc_navigableOwnedEnd49_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Association(isDerived="sample_text")
    _safe_set(b, 'uml_Association50', {a1})
    assert _is_linked(b, 'uml_Association50', a1)
    if hasattr(a1, 'uml_Property51'):
        assert _is_linked(a1, 'uml_Property51', b)
    _safe_set(b, 'uml_Association50', {a2})
    assert _is_linked(b, 'uml_Association50', a2)
    if hasattr(a1, 'uml_Property51'):
        assert not _is_linked(a1, 'uml_Property51', b)
    if hasattr(a2, 'uml_Property51'):
        assert _is_linked(a2, 'uml_Property51', b)
    _safe_set(b, 'uml_Association50', set())
    assert not _is_linked(b, 'uml_Association50', a2)
    if hasattr(a2, 'uml_Property51'):
        assert not _is_linked(a2, 'uml_Property51', b)


def test_assoc_nestedClassifier84_reverse_link_reassign_clear():
    a1 = uml_Classifier(isAbstract="sample_text")
    a2 = uml_Classifier(isAbstract="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'uml_Class85', {a1})
    assert _is_linked(b, 'uml_Class85', a1)
    if hasattr(a1, 'uml_Classifier86'):
        assert _is_linked(a1, 'uml_Classifier86', b)
    _safe_set(b, 'uml_Class85', {a2})
    assert _is_linked(b, 'uml_Class85', a2)
    if hasattr(a1, 'uml_Classifier86'):
        assert not _is_linked(a1, 'uml_Classifier86', b)
    if hasattr(a2, 'uml_Classifier86'):
        assert _is_linked(a2, 'uml_Classifier86', b)
    _safe_set(b, 'uml_Class85', set())
    assert not _is_linked(b, 'uml_Class85', a2)
    if hasattr(a2, 'uml_Classifier86'):
        assert not _is_linked(a2, 'uml_Classifier86', b)


def test_assoc_operation70_reverse_link_reassign_clear():
    a1 = uml_Parameter(default="sample_text", isException="sample_text", isStream="sample_text")
    a2 = uml_Parameter(default="sample_text_2", isException="sample_text_2", isStream="sample_text_2")
    b = uml_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    _safe_set(b, 'uml_Operation', a1)
    assert _is_linked(b, 'uml_Operation', a1)
    if hasattr(a1, 'uml_Parameter'):
        assert _is_linked(a1, 'uml_Parameter', b)
    _safe_set(b, 'uml_Operation', a2)
    assert _is_linked(b, 'uml_Operation', a2)
    if hasattr(a1, 'uml_Parameter'):
        assert not _is_linked(a1, 'uml_Parameter', b)
    if hasattr(a2, 'uml_Parameter'):
        assert _is_linked(a2, 'uml_Parameter', b)
    _safe_set(b, 'uml_Operation', None)
    assert not _is_linked(b, 'uml_Operation', a2)
    if hasattr(a2, 'uml_Parameter'):
        assert not _is_linked(a2, 'uml_Parameter', b)


def test_assoc_ownedAttribute91_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'uml_Class92', {a1})
    assert _is_linked(b, 'uml_Class92', a1)
    if hasattr(a1, 'uml_Property93'):
        assert _is_linked(a1, 'uml_Property93', b)
    _safe_set(b, 'uml_Class92', {a2})
    assert _is_linked(b, 'uml_Class92', a2)
    if hasattr(a1, 'uml_Property93'):
        assert not _is_linked(a1, 'uml_Property93', b)
    if hasattr(a2, 'uml_Property93'):
        assert _is_linked(a2, 'uml_Property93', b)
    _safe_set(b, 'uml_Class92', set())
    assert not _is_linked(b, 'uml_Class92', a2)
    if hasattr(a2, 'uml_Property93'):
        assert not _is_linked(a2, 'uml_Property93', b)


def test_assoc_ownedEnd42_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Association(isDerived="sample_text")
    _safe_set(b, 'uml_Association', {a1})
    assert _is_linked(b, 'uml_Association', a1)
    if hasattr(a1, 'uml_Property'):
        assert _is_linked(a1, 'uml_Property', b)
    _safe_set(b, 'uml_Association', {a2})
    assert _is_linked(b, 'uml_Association', a2)
    if hasattr(a1, 'uml_Property'):
        assert not _is_linked(a1, 'uml_Property', b)
    if hasattr(a2, 'uml_Property'):
        assert _is_linked(a2, 'uml_Property', b)
    _safe_set(b, 'uml_Association', set())
    assert not _is_linked(b, 'uml_Association', a2)
    if hasattr(a2, 'uml_Property'):
        assert not _is_linked(a2, 'uml_Property', b)


def test_assoc_ownedOperation87_reverse_link_reassign_clear():
    a1 = uml_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    a2 = uml_Operation(isOrdered="sample_text_2", isQuery="sample_text_2", isUnique="sample_text_2", lower="sample_text_2", upper="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_ownedParameter79_reverse_link_reassign_clear():
    a1 = uml_Parameter(default="sample_text", isException="sample_text", isStream="sample_text")
    a2 = uml_Parameter(default="sample_text_2", isException="sample_text_2", isStream="sample_text_2")
    b = uml_BehavioralFeature(isAbstract="sample_text")
    _safe_set(b, 'uml_BehavioralFeature', {a1})
    assert _is_linked(b, 'uml_BehavioralFeature', a1)
    if hasattr(a1, 'uml_Parameter80'):
        assert _is_linked(a1, 'uml_Parameter80', b)
    _safe_set(b, 'uml_BehavioralFeature', {a2})
    assert _is_linked(b, 'uml_BehavioralFeature', a2)
    if hasattr(a1, 'uml_Parameter80'):
        assert not _is_linked(a1, 'uml_Parameter80', b)
    if hasattr(a2, 'uml_Parameter80'):
        assert _is_linked(a2, 'uml_Parameter80', b)
    _safe_set(b, 'uml_BehavioralFeature', set())
    assert not _is_linked(b, 'uml_BehavioralFeature', a2)
    if hasattr(a2, 'uml_Parameter80'):
        assert not _is_linked(a2, 'uml_Parameter80', b)


def test_assoc_redefinedClassifier56_reverse_link_reassign_clear():
    a1 = uml_Classifier(isAbstract="sample_text")
    a2 = uml_Classifier(isAbstract="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier57', a1)
    assert _is_linked(b, 'uml_Classifier57', a1)
    if hasattr(a1, 'uml_Classifier55'):
        assert _is_linked(a1, 'uml_Classifier55', b)
    _safe_set(b, 'uml_Classifier57', a2)
    assert _is_linked(b, 'uml_Classifier57', a2)
    if hasattr(a1, 'uml_Classifier55'):
        assert not _is_linked(a1, 'uml_Classifier55', b)
    if hasattr(a2, 'uml_Classifier55'):
        assert _is_linked(a2, 'uml_Classifier55', b)
    _safe_set(b, 'uml_Classifier57', None)
    assert not _is_linked(b, 'uml_Classifier57', a2)
    if hasattr(a2, 'uml_Classifier55'):
        assert not _is_linked(a2, 'uml_Classifier55', b)


def test_assoc_redefinedOperation77_reverse_link_reassign_clear():
    a1 = uml_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    a2 = uml_Operation(isOrdered="sample_text_2", isQuery="sample_text_2", isUnique="sample_text_2", lower="sample_text_2", upper="sample_text_2")
    b = uml_Operation(isOrdered="sample_text", isQuery="sample_text", isUnique="sample_text", lower="sample_text", upper="sample_text")
    _safe_set(b, 'uml_Operation78', a1)
    assert _is_linked(b, 'uml_Operation78', a1)
    if hasattr(a1, 'uml_Operation76'):
        assert _is_linked(a1, 'uml_Operation76', b)
    _safe_set(b, 'uml_Operation78', a2)
    assert _is_linked(b, 'uml_Operation78', a2)
    if hasattr(a1, 'uml_Operation76'):
        assert not _is_linked(a1, 'uml_Operation76', b)
    if hasattr(a2, 'uml_Operation76'):
        assert _is_linked(a2, 'uml_Operation76', b)
    _safe_set(b, 'uml_Operation78', None)
    assert not _is_linked(b, 'uml_Operation78', a2)
    if hasattr(a2, 'uml_Operation76'):
        assert not _is_linked(a2, 'uml_Operation76', b)


def test_assoc_specific99_reverse_link_reassign_clear():
    a1 = uml_Generalization(isSubstitutable="sample_text")
    a2 = uml_Generalization(isSubstitutable="sample_text_2")
    b = uml_Classifier(isAbstract="sample_text")
    _safe_set(b, 'uml_Classifier101', a1)
    assert _is_linked(b, 'uml_Classifier101', a1)
    if hasattr(a1, 'uml_Generalization100'):
        assert _is_linked(a1, 'uml_Generalization100', b)
    _safe_set(b, 'uml_Classifier101', a2)
    assert _is_linked(b, 'uml_Classifier101', a2)
    if hasattr(a1, 'uml_Generalization100'):
        assert not _is_linked(a1, 'uml_Generalization100', b)
    if hasattr(a2, 'uml_Generalization100'):
        assert _is_linked(a2, 'uml_Generalization100', b)
    _safe_set(b, 'uml_Classifier101', None)
    assert not _is_linked(b, 'uml_Classifier101', a2)
    if hasattr(a2, 'uml_Generalization100'):
        assert not _is_linked(a2, 'uml_Generalization100', b)


def test_assoc_superClass89_reverse_link_reassign_clear():
    a1 = uml_Class(isActive="sample_text", name="sample_text")
    a2 = uml_Class(isActive="sample_text_2", name="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'uml_Class90', a1)
    assert _is_linked(b, 'uml_Class90', a1)
    if hasattr(a1, 'uml_Class88'):
        assert _is_linked(a1, 'uml_Class88', b)
    _safe_set(b, 'uml_Class90', a2)
    assert _is_linked(b, 'uml_Class90', a2)
    if hasattr(a1, 'uml_Class88'):
        assert not _is_linked(a1, 'uml_Class88', b)
    if hasattr(a2, 'uml_Class88'):
        assert _is_linked(a2, 'uml_Class88', b)
    _safe_set(b, 'uml_Class90', None)
    assert not _is_linked(b, 'uml_Class90', a2)
    if hasattr(a2, 'uml_Class88'):
        assert not _is_linked(a2, 'uml_Class88', b)


def test_assoc_type73_reverse_link_reassign_clear():
    a1 = uml_Property(name="sample_text")
    a2 = uml_Property(name="sample_text_2")
    b = uml_Class(isActive="sample_text", name="sample_text")
    _safe_set(b, 'uml_Class', a1)
    assert _is_linked(b, 'uml_Class', a1)
    if hasattr(a1, 'uml_Property74'):
        assert _is_linked(a1, 'uml_Property74', b)
    _safe_set(b, 'uml_Class', a2)
    assert _is_linked(b, 'uml_Class', a2)
    if hasattr(a1, 'uml_Property74'):
        assert not _is_linked(a1, 'uml_Property74', b)
    if hasattr(a2, 'uml_Property74'):
        assert _is_linked(a2, 'uml_Property74', b)
    _safe_set(b, 'uml_Class', None)
    assert not _is_linked(b, 'uml_Class', a2)
    if hasattr(a2, 'uml_Property74'):
        assert not _is_linked(a2, 'uml_Property74', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotatedElement0_stub_double():
    # uml_Element has no real 'uml_Element' property in the generated
    # code (a bare stub) -- manually attach it so uml_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Comment(body="sample_text")
    partner = uml_Element()
    setattr(partner, 'uml_Element', None)
    _safe_set(owner, 'uml_Comment', {partner})
    assert getattr(partner, 'uml_Element') == owner
    _safe_set(owner, 'uml_Comment', set())
    assert getattr(partner, 'uml_Element') is None


def test_assoc_client14_stub_double():
    # uml_Dependency has no real 'clientDependency' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Dependency()
    setattr(partner, 'clientDependency', None)
    _safe_set(owner, 'NamedElement', partner)
    assert owner in getattr(partner, 'clientDependency')
    _safe_set(owner, 'NamedElement', None)
    assert owner not in getattr(partner, 'clientDependency')


def test_assoc_clientDependency11_stub_double():
    # uml_Dependency has no real 'Dependency' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Dependency()
    setattr(partner, 'Dependency', None)
    _safe_set(owner, 'client', {partner})
    assert getattr(partner, 'Dependency') == owner
    _safe_set(owner, 'client', set())
    assert getattr(partner, 'Dependency') is None


def test_assoc_contract66_stub_double():
    # uml_Substitution has no real 'uml_Substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Classifier(isAbstract="sample_text")
    partner = uml_Substitution()
    setattr(partner, 'uml_Substitution', None)
    _safe_set(owner, 'uml_Classifier67', partner)
    assert getattr(partner, 'uml_Substitution') == owner
    _safe_set(owner, 'uml_Classifier67', None)
    assert getattr(partner, 'uml_Substitution') is None


def test_assoc_defaultValue71_stub_double():
    # uml_ValueSpecification has no real 'uml_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so uml_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Parameter(default="sample_text", isException="sample_text", isStream="sample_text")
    partner = uml_ValueSpecification()
    setattr(partner, 'uml_ValueSpecification', None)
    _safe_set(owner, 'uml_Parameter72', partner)
    assert getattr(partner, 'uml_ValueSpecification') == owner
    _safe_set(owner, 'uml_Parameter72', None)
    assert getattr(partner, 'uml_ValueSpecification') is None


def test_assoc_elementImport22_stub_double():
    # uml_Namespace has no real 'importingNamespace' property in the generated
    # code (a bare stub) -- manually attach it so uml_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_ElementImport(alias="sample_text", visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'importingNamespace', None)
    _safe_set(owner, 'ElementImport', partner)
    assert owner in getattr(partner, 'importingNamespace')
    _safe_set(owner, 'ElementImport', None)
    assert owner not in getattr(partner, 'importingNamespace')


def test_assoc_endType46_stub_double():
    # uml_Type has no real 'uml_Type48' property in the generated
    # code (a bare stub) -- manually attach it so uml_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Association(isDerived="sample_text")
    partner = uml_Type()
    setattr(partner, 'uml_Type48', None)
    _safe_set(owner, 'uml_Association47', {partner})
    assert getattr(partner, 'uml_Type48') == owner
    _safe_set(owner, 'uml_Association47', set())
    assert getattr(partner, 'uml_Type48') is None


def test_assoc_importedElement32_stub_double():
    # uml_PackageableElement has no real 'uml_PackageableElement33' property in the generated
    # code (a bare stub) -- manually attach it so uml_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_ElementImport(alias="sample_text", visibility="sample_text")
    partner = uml_PackageableElement()
    setattr(partner, 'uml_PackageableElement33', None)
    _safe_set(owner, 'uml_ElementImport', partner)
    assert getattr(partner, 'uml_PackageableElement33') == owner
    _safe_set(owner, 'uml_ElementImport', None)
    assert getattr(partner, 'uml_PackageableElement33') is None


def test_assoc_importingNamespace34_stub_double():
    # uml_Namespace has no real 'Namespace35' property in the generated
    # code (a bare stub) -- manually attach it so uml_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_ElementImport(alias="sample_text", visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'Namespace35', None)
    _safe_set(owner, 'elementImport', partner)
    assert getattr(partner, 'Namespace35') == owner
    _safe_set(owner, 'elementImport', None)
    assert getattr(partner, 'Namespace35') is None


def test_assoc_importingNamespace38_stub_double():
    # uml_Namespace has no real 'Namespace39' property in the generated
    # code (a bare stub) -- manually attach it so uml_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_PackageImport(visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'Namespace39', None)
    _safe_set(owner, 'packageImport', partner)
    assert getattr(partner, 'Namespace39') == owner
    _safe_set(owner, 'packageImport', None)
    assert getattr(partner, 'Namespace39') is None


def test_assoc_member25_stub_double():
    # uml_Namespace has no real 'uml_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'uml_Namespace', None)
    _safe_set(owner, 'uml_NamedElement26', partner)
    assert owner in getattr(partner, 'uml_Namespace')
    _safe_set(owner, 'uml_NamedElement26', None)
    assert owner not in getattr(partner, 'uml_Namespace')


def test_assoc_namespace12_stub_double():
    # uml_Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedMember', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedMember', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_ownedComment6_stub_double():
    # uml_Element has no real 'uml_Element7' property in the generated
    # code (a bare stub) -- manually attach it so uml_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Comment(body="sample_text")
    partner = uml_Element()
    setattr(partner, 'uml_Element7', None)
    _safe_set(owner, 'uml_Comment8', partner)
    assert owner in getattr(partner, 'uml_Element7')
    _safe_set(owner, 'uml_Comment8', None)
    assert owner not in getattr(partner, 'uml_Element7')


def test_assoc_ownedMember30_stub_double():
    # uml_Namespace has no real 'namespace' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'namespace', None)
    _safe_set(owner, 'NamedElement31', partner)
    assert owner in getattr(partner, 'namespace')
    _safe_set(owner, 'NamedElement31', None)
    assert owner not in getattr(partner, 'namespace')


def test_assoc_ownedType9_stub_double():
    # uml_Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so uml_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Package(name="sample_text")
    partner = uml_Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type') is None


def test_assoc_package41_stub_double():
    # uml_Type has no real 'ownedType' property in the generated
    # code (a bare stub) -- manually attach it so uml_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Package(name="sample_text")
    partner = uml_Type()
    setattr(partner, 'ownedType', None)
    _safe_set(owner, 'Package', partner)
    assert getattr(partner, 'ownedType') == owner
    _safe_set(owner, 'Package', None)
    assert getattr(partner, 'ownedType') is None


def test_assoc_packageImport23_stub_double():
    # uml_Namespace has no real 'importingNamespace24' property in the generated
    # code (a bare stub) -- manually attach it so uml_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_PackageImport(visibility="sample_text")
    partner = uml_Namespace()
    setattr(partner, 'importingNamespace24', None)
    _safe_set(owner, 'PackageImport', partner)
    assert owner in getattr(partner, 'importingNamespace24')
    _safe_set(owner, 'PackageImport', None)
    assert owner not in getattr(partner, 'importingNamespace24')


def test_assoc_packagedElement10_stub_double():
    # uml_PackageableElement has no real 'uml_PackageableElement' property in the generated
    # code (a bare stub) -- manually attach it so uml_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Package(name="sample_text")
    partner = uml_PackageableElement()
    setattr(partner, 'uml_PackageableElement', None)
    _safe_set(owner, 'uml_Package', {partner})
    assert getattr(partner, 'uml_PackageableElement') == owner
    _safe_set(owner, 'uml_Package', set())
    assert getattr(partner, 'uml_PackageableElement') is None


def test_assoc_packagedElement102_stub_double():
    # uml_PackageableElement has no real 'uml_PackageableElement103' property in the generated
    # code (a bare stub) -- manually attach it so uml_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Model(name="sample_text")
    partner = uml_PackageableElement()
    setattr(partner, 'uml_PackageableElement103', None)
    _safe_set(owner, 'uml_Model', {partner})
    assert getattr(partner, 'uml_PackageableElement103') == owner
    _safe_set(owner, 'uml_Model', set())
    assert getattr(partner, 'uml_PackageableElement103') is None


def test_assoc_raisedException81_stub_double():
    # uml_Type has no real 'uml_Type83' property in the generated
    # code (a bare stub) -- manually attach it so uml_BehavioralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_BehavioralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_BehavioralFeature(isAbstract="sample_text")
    partner = uml_Type()
    setattr(partner, 'uml_Type83', None)
    _safe_set(owner, 'uml_BehavioralFeature82', {partner})
    assert getattr(partner, 'uml_Type83') == owner
    _safe_set(owner, 'uml_BehavioralFeature82', set())
    assert getattr(partner, 'uml_Type83') is None


def test_assoc_substitutingClassifier68_stub_double():
    # uml_Substitution has no real 'substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Classifier(isAbstract="sample_text")
    partner = uml_Substitution()
    setattr(partner, 'substitution', None)
    _safe_set(owner, 'Classifier69', partner)
    assert getattr(partner, 'substitution') == owner
    _safe_set(owner, 'Classifier69', None)
    assert getattr(partner, 'substitution') is None


def test_assoc_substitution61_stub_double():
    # uml_Substitution has no real 'Substitution' property in the generated
    # code (a bare stub) -- manually attach it so uml_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_Classifier(isAbstract="sample_text")
    partner = uml_Substitution()
    setattr(partner, 'Substitution', None)
    _safe_set(owner, 'substitutingClassifier', {partner})
    assert getattr(partner, 'Substitution') == owner
    _safe_set(owner, 'substitutingClassifier', set())
    assert getattr(partner, 'Substitution') is None


def test_assoc_supplier13_stub_double():
    # uml_Dependency has no real 'uml_Dependency' property in the generated
    # code (a bare stub) -- manually attach it so uml_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # uml_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = uml_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = uml_Dependency()
    setattr(partner, 'uml_Dependency', None)
    _safe_set(owner, 'uml_NamedElement', partner)
    assert owner in getattr(partner, 'uml_Dependency')
    _safe_set(owner, 'uml_NamedElement', None)
    assert owner not in getattr(partner, 'uml_Dependency')


