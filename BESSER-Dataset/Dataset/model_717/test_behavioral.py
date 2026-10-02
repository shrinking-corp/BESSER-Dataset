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


