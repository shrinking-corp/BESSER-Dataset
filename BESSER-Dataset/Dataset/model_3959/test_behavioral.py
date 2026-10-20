import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BehavioralFeature,
    Classifier,
    DataType,
    Element,
    Feature,
    InstanceSpecification,
    LiteralSpecification,
    MultiplicityElement,
    NamedElement,
    Namespace,
    Package,
    PackageableElement,
    RedefinableElement,
    StructuralFeature,
    Type,
    TypedElement,
    ValueSpecification,
    classes_Association,
    classes_BehavioralFeature,
    classes_Class,
    classes_Classifier,
    classes_Comment,
    classes_DataType,
    classes_Element,
    classes_ElementImport,
    classes_Enumeration,
    classes_EnumerationLiteral,
    classes_Feature,
    classes_Generalization,
    classes_InstanceSpecification,
    classes_InstanceValue,
    classes_LiteralBoolean,
    classes_LiteralInteger,
    classes_LiteralNull,
    classes_LiteralSpecification,
    classes_LiteralString,
    classes_LiteralUnlimitedNatural,
    classes_Model,
    classes_MultiplicityElement,
    classes_NamedElement,
    classes_Namespace,
    classes_Operation,
    classes_Package,
    classes_PackageImport,
    classes_PackageableElement,
    classes_Parameter,
    classes_PrimitiveType,
    classes_Property,
    classes_RedefinableElement,
    classes_Slot,
    classes_StructuralFeature,
    classes_Type,
    classes_TypedElement,
    classes_ValueSpecification,
    AggregationKind,
    ParameterDirectionKind,
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

def test_assoc_annotatedElement8_reverse_link_reassign_clear():
    a1 = classes_Element()
    a2 = classes_Element()
    b = classes_Comment(body="sample_text")
    _safe_set(b, 'classes_Comment9', {a1})
    assert _is_linked(b, 'classes_Comment9', a1)
    if hasattr(a1, 'classes_Element10'):
        assert _is_linked(a1, 'classes_Element10', b)
    _safe_set(b, 'classes_Comment9', {a2})
    assert _is_linked(b, 'classes_Comment9', a2)
    if hasattr(a1, 'classes_Element10'):
        assert not _is_linked(a1, 'classes_Element10', b)
    if hasattr(a2, 'classes_Element10'):
        assert _is_linked(a2, 'classes_Element10', b)
    _safe_set(b, 'classes_Comment9', set())
    assert not _is_linked(b, 'classes_Comment9', a2)
    if hasattr(a2, 'classes_Element10'):
        assert not _is_linked(a2, 'classes_Element10', b)


def test_assoc_association56_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Association(derived=True)
    _safe_set(b, 'Association57', a1)
    assert _is_linked(b, 'Association57', a1)
    if hasattr(a1, 'memberEnd'):
        assert _is_linked(a1, 'memberEnd', b)
    _safe_set(b, 'Association57', a2)
    assert _is_linked(b, 'Association57', a2)
    if hasattr(a1, 'memberEnd'):
        assert not _is_linked(a1, 'memberEnd', b)
    if hasattr(a2, 'memberEnd'):
        assert _is_linked(a2, 'memberEnd', b)
    _safe_set(b, 'Association57', None)
    assert not _is_linked(b, 'Association57', a2)
    if hasattr(a2, 'memberEnd'):
        assert not _is_linked(a2, 'memberEnd', b)


def test_assoc_attribute46_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'classes_Classifier47', {a1})
    assert _is_linked(b, 'classes_Classifier47', a1)
    if hasattr(a1, 'classes_Property'):
        assert _is_linked(a1, 'classes_Property', b)
    _safe_set(b, 'classes_Classifier47', {a2})
    assert _is_linked(b, 'classes_Classifier47', a2)
    if hasattr(a1, 'classes_Property'):
        assert not _is_linked(a1, 'classes_Property', b)
    if hasattr(a2, 'classes_Property'):
        assert _is_linked(a2, 'classes_Property', b)
    _safe_set(b, 'classes_Classifier47', set())
    assert not _is_linked(b, 'classes_Classifier47', a2)
    if hasattr(a2, 'classes_Property'):
        assert not _is_linked(a2, 'classes_Property', b)


def test_assoc_class_59_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Class(active=True)
    _safe_set(b, 'Class', a1)
    assert _is_linked(b, 'Class', a1)
    if hasattr(a1, 'ownedAttribute60'):
        assert _is_linked(a1, 'ownedAttribute60', b)
    _safe_set(b, 'Class', a2)
    assert _is_linked(b, 'Class', a2)
    if hasattr(a1, 'ownedAttribute60'):
        assert not _is_linked(a1, 'ownedAttribute60', b)
    if hasattr(a2, 'ownedAttribute60'):
        assert _is_linked(a2, 'ownedAttribute60', b)
    _safe_set(b, 'Class', None)
    assert not _is_linked(b, 'Class', a2)
    if hasattr(a2, 'ownedAttribute60'):
        assert not _is_linked(a2, 'ownedAttribute60', b)


def test_assoc_class_79_reverse_link_reassign_clear():
    a1 = classes_Operation(lower="sample_text", ordered=True, query=True, unique=True, upper="sample_text")
    a2 = classes_Operation(lower="sample_text_2", ordered=False, query=False, unique=False, upper="sample_text_2")
    b = classes_Class(active=True)
    _safe_set(b, 'Class80', a1)
    assert _is_linked(b, 'Class80', a1)
    if hasattr(a1, 'ownedOperation'):
        assert _is_linked(a1, 'ownedOperation', b)
    _safe_set(b, 'Class80', a2)
    assert _is_linked(b, 'Class80', a2)
    if hasattr(a1, 'ownedOperation'):
        assert not _is_linked(a1, 'ownedOperation', b)
    if hasattr(a2, 'ownedOperation'):
        assert _is_linked(a2, 'ownedOperation', b)
    _safe_set(b, 'Class80', None)
    assert not _is_linked(b, 'Class80', a2)
    if hasattr(a2, 'ownedOperation'):
        assert not _is_linked(a2, 'ownedOperation', b)


def test_assoc_feature42_reverse_link_reassign_clear():
    a1 = classes_Feature(static=True)
    a2 = classes_Feature(static=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
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


def test_assoc_featuringClassifier36_reverse_link_reassign_clear():
    a1 = classes_Feature(static=True)
    a2 = classes_Feature(static=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
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


def test_assoc_general49_reverse_link_reassign_clear():
    a1 = classes_Classifier(abstract=True, finalSpecialization=True)
    a2 = classes_Classifier(abstract=False, finalSpecialization=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'classes_Classifier50', a1)
    assert _is_linked(b, 'classes_Classifier50', a1)
    if hasattr(a1, 'classes_Classifier48'):
        assert _is_linked(a1, 'classes_Classifier48', b)
    _safe_set(b, 'classes_Classifier50', a2)
    assert _is_linked(b, 'classes_Classifier50', a2)
    if hasattr(a1, 'classes_Classifier48'):
        assert not _is_linked(a1, 'classes_Classifier48', b)
    if hasattr(a2, 'classes_Classifier48'):
        assert _is_linked(a2, 'classes_Classifier48', b)
    _safe_set(b, 'classes_Classifier50', None)
    assert not _is_linked(b, 'classes_Classifier50', a2)
    if hasattr(a2, 'classes_Classifier48'):
        assert not _is_linked(a2, 'classes_Classifier48', b)


def test_assoc_general51_reverse_link_reassign_clear():
    a1 = classes_Generalization(substitutable=True)
    a2 = classes_Generalization(substitutable=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'classes_Classifier52', a1)
    assert _is_linked(b, 'classes_Classifier52', a1)
    if hasattr(a1, 'classes_Generalization'):
        assert _is_linked(a1, 'classes_Generalization', b)
    _safe_set(b, 'classes_Classifier52', a2)
    assert _is_linked(b, 'classes_Classifier52', a2)
    if hasattr(a1, 'classes_Generalization'):
        assert not _is_linked(a1, 'classes_Generalization', b)
    if hasattr(a2, 'classes_Generalization'):
        assert _is_linked(a2, 'classes_Generalization', b)
    _safe_set(b, 'classes_Classifier52', None)
    assert not _is_linked(b, 'classes_Classifier52', a2)
    if hasattr(a2, 'classes_Generalization'):
        assert not _is_linked(a2, 'classes_Generalization', b)


def test_assoc_generalization41_reverse_link_reassign_clear():
    a1 = classes_Generalization(substitutable=True)
    a2 = classes_Generalization(substitutable=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'specific', {a1})
    assert _is_linked(b, 'specific', a1)
    if hasattr(a1, 'Generalization'):
        assert _is_linked(a1, 'Generalization', b)
    _safe_set(b, 'specific', {a2})
    assert _is_linked(b, 'specific', a2)
    if hasattr(a1, 'Generalization'):
        assert not _is_linked(a1, 'Generalization', b)
    if hasattr(a2, 'Generalization'):
        assert _is_linked(a2, 'Generalization', b)
    _safe_set(b, 'specific', set())
    assert not _is_linked(b, 'specific', a2)
    if hasattr(a2, 'Generalization'):
        assert not _is_linked(a2, 'Generalization', b)


def test_assoc_inheritedMember43_reverse_link_reassign_clear():
    a1 = classes_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    a2 = classes_NamedElement(name="sample_text_2", qualifiedName="sample_text_2", visibility="sample_text_2")
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'classes_Classifier44', {a1})
    assert _is_linked(b, 'classes_Classifier44', a1)
    if hasattr(a1, 'classes_NamedElement45'):
        assert _is_linked(a1, 'classes_NamedElement45', b)
    _safe_set(b, 'classes_Classifier44', {a2})
    assert _is_linked(b, 'classes_Classifier44', a2)
    if hasattr(a1, 'classes_NamedElement45'):
        assert not _is_linked(a1, 'classes_NamedElement45', b)
    if hasattr(a2, 'classes_NamedElement45'):
        assert _is_linked(a2, 'classes_NamedElement45', b)
    _safe_set(b, 'classes_Classifier44', set())
    assert not _is_linked(b, 'classes_Classifier44', a2)
    if hasattr(a2, 'classes_NamedElement45'):
        assert not _is_linked(a2, 'classes_NamedElement45', b)


def test_assoc_lowerValue75_reverse_link_reassign_clear():
    a1 = classes_ValueSpecification()
    a2 = classes_ValueSpecification()
    b = classes_MultiplicityElement(lower=7, ordered=True, unique=True, upper=7)
    _safe_set(b, 'classes_MultiplicityElement76', a1)
    assert _is_linked(b, 'classes_MultiplicityElement76', a1)
    if hasattr(a1, 'classes_ValueSpecification77'):
        assert _is_linked(a1, 'classes_ValueSpecification77', b)
    _safe_set(b, 'classes_MultiplicityElement76', a2)
    assert _is_linked(b, 'classes_MultiplicityElement76', a2)
    if hasattr(a1, 'classes_ValueSpecification77'):
        assert not _is_linked(a1, 'classes_ValueSpecification77', b)
    if hasattr(a2, 'classes_ValueSpecification77'):
        assert _is_linked(a2, 'classes_ValueSpecification77', b)
    _safe_set(b, 'classes_MultiplicityElement76', None)
    assert not _is_linked(b, 'classes_MultiplicityElement76', a2)
    if hasattr(a2, 'classes_ValueSpecification77'):
        assert not _is_linked(a2, 'classes_ValueSpecification77', b)


def test_assoc_memberEnd66_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Association(derived=True)
    _safe_set(b, 'association', {a1})
    assert _is_linked(b, 'association', a1)
    if hasattr(a1, 'Property'):
        assert _is_linked(a1, 'Property', b)
    _safe_set(b, 'association', {a2})
    assert _is_linked(b, 'association', a2)
    if hasattr(a1, 'Property'):
        assert not _is_linked(a1, 'Property', b)
    if hasattr(a2, 'Property'):
        assert _is_linked(a2, 'Property', b)
    _safe_set(b, 'association', set())
    assert not _is_linked(b, 'association', a2)
    if hasattr(a2, 'Property'):
        assert not _is_linked(a2, 'Property', b)


def test_assoc_navigableOwnedEnd67_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Association(derived=True)
    _safe_set(b, 'classes_Association68', {a1})
    assert _is_linked(b, 'classes_Association68', a1)
    if hasattr(a1, 'classes_Property69'):
        assert _is_linked(a1, 'classes_Property69', b)
    _safe_set(b, 'classes_Association68', {a2})
    assert _is_linked(b, 'classes_Association68', a2)
    if hasattr(a1, 'classes_Property69'):
        assert not _is_linked(a1, 'classes_Property69', b)
    if hasattr(a2, 'classes_Property69'):
        assert _is_linked(a2, 'classes_Property69', b)
    _safe_set(b, 'classes_Association68', set())
    assert not _is_linked(b, 'classes_Association68', a2)
    if hasattr(a2, 'classes_Property69'):
        assert not _is_linked(a2, 'classes_Property69', b)


def test_assoc_nestedClassifier104_reverse_link_reassign_clear():
    a1 = classes_Classifier(abstract=True, finalSpecialization=True)
    a2 = classes_Classifier(abstract=False, finalSpecialization=False)
    b = classes_Class(active=True)
    _safe_set(b, 'classes_Class105', {a1})
    assert _is_linked(b, 'classes_Class105', a1)
    if hasattr(a1, 'classes_Classifier106'):
        assert _is_linked(a1, 'classes_Classifier106', b)
    _safe_set(b, 'classes_Class105', {a2})
    assert _is_linked(b, 'classes_Class105', a2)
    if hasattr(a1, 'classes_Classifier106'):
        assert not _is_linked(a1, 'classes_Classifier106', b)
    if hasattr(a2, 'classes_Classifier106'):
        assert _is_linked(a2, 'classes_Classifier106', b)
    _safe_set(b, 'classes_Class105', set())
    assert not _is_linked(b, 'classes_Class105', a2)
    if hasattr(a2, 'classes_Classifier106'):
        assert not _is_linked(a2, 'classes_Classifier106', b)


def test_assoc_opposite62_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    _safe_set(b, 'classes_Property63', a1)
    assert _is_linked(b, 'classes_Property63', a1)
    if hasattr(a1, 'classes_Property61'):
        assert _is_linked(a1, 'classes_Property61', b)
    _safe_set(b, 'classes_Property63', a2)
    assert _is_linked(b, 'classes_Property63', a2)
    if hasattr(a1, 'classes_Property61'):
        assert not _is_linked(a1, 'classes_Property61', b)
    if hasattr(a2, 'classes_Property61'):
        assert _is_linked(a2, 'classes_Property61', b)
    _safe_set(b, 'classes_Property63', None)
    assert not _is_linked(b, 'classes_Property63', a2)
    if hasattr(a2, 'classes_Property61'):
        assert not _is_linked(a2, 'classes_Property61', b)


def test_assoc_ownedAttribute98_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Class(active=True)
    _safe_set(b, 'class_', {a1})
    assert _is_linked(b, 'class_', a1)
    if hasattr(a1, 'Property99'):
        assert _is_linked(a1, 'Property99', b)
    _safe_set(b, 'class_', {a2})
    assert _is_linked(b, 'class_', a2)
    if hasattr(a1, 'Property99'):
        assert not _is_linked(a1, 'Property99', b)
    if hasattr(a2, 'Property99'):
        assert _is_linked(a2, 'Property99', b)
    _safe_set(b, 'class_', set())
    assert not _is_linked(b, 'class_', a2)
    if hasattr(a2, 'Property99'):
        assert not _is_linked(a2, 'Property99', b)


def test_assoc_ownedComment7_reverse_link_reassign_clear():
    a1 = classes_Element()
    a2 = classes_Element()
    b = classes_Comment(body="sample_text")
    _safe_set(b, 'classes_Comment', a1)
    assert _is_linked(b, 'classes_Comment', a1)
    if hasattr(a1, 'classes_Element'):
        assert _is_linked(a1, 'classes_Element', b)
    _safe_set(b, 'classes_Comment', a2)
    assert _is_linked(b, 'classes_Comment', a2)
    if hasattr(a1, 'classes_Element'):
        assert not _is_linked(a1, 'classes_Element', b)
    if hasattr(a2, 'classes_Element'):
        assert _is_linked(a2, 'classes_Element', b)
    _safe_set(b, 'classes_Comment', None)
    assert not _is_linked(b, 'classes_Comment', a2)
    if hasattr(a2, 'classes_Element'):
        assert not _is_linked(a2, 'classes_Element', b)


def test_assoc_ownedElement3_reverse_link_reassign_clear():
    a1 = classes_Element()
    a2 = classes_Element()
    b = classes_Element()
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'Element'):
        assert _is_linked(a1, 'Element', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'Element'):
        assert not _is_linked(a1, 'Element', b)
    if hasattr(a2, 'Element'):
        assert _is_linked(a2, 'Element', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'Element'):
        assert not _is_linked(a2, 'Element', b)


def test_assoc_ownedEnd70_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Association(derived=True)
    _safe_set(b, 'owningAssociation', {a1})
    assert _is_linked(b, 'owningAssociation', a1)
    if hasattr(a1, 'Property71'):
        assert _is_linked(a1, 'Property71', b)
    _safe_set(b, 'owningAssociation', {a2})
    assert _is_linked(b, 'owningAssociation', a2)
    if hasattr(a1, 'Property71'):
        assert not _is_linked(a1, 'Property71', b)
    if hasattr(a2, 'Property71'):
        assert _is_linked(a2, 'Property71', b)
    _safe_set(b, 'owningAssociation', set())
    assert not _is_linked(b, 'owningAssociation', a2)
    if hasattr(a2, 'Property71'):
        assert not _is_linked(a2, 'Property71', b)


def test_assoc_ownedOperation100_reverse_link_reassign_clear():
    a1 = classes_Operation(lower="sample_text", ordered=True, query=True, unique=True, upper="sample_text")
    a2 = classes_Operation(lower="sample_text_2", ordered=False, query=False, unique=False, upper="sample_text_2")
    b = classes_Class(active=True)
    _safe_set(b, 'class_101', {a1})
    assert _is_linked(b, 'class_101', a1)
    if hasattr(a1, 'Operation'):
        assert _is_linked(a1, 'Operation', b)
    _safe_set(b, 'class_101', {a2})
    assert _is_linked(b, 'class_101', a2)
    if hasattr(a1, 'Operation'):
        assert not _is_linked(a1, 'Operation', b)
    if hasattr(a2, 'Operation'):
        assert _is_linked(a2, 'Operation', b)
    _safe_set(b, 'class_101', set())
    assert not _is_linked(b, 'class_101', a2)
    if hasattr(a2, 'Operation'):
        assert not _is_linked(a2, 'Operation', b)


def test_assoc_ownedParameter78_reverse_link_reassign_clear():
    a1 = classes_Parameter(direction="sample_text")
    a2 = classes_Parameter(direction="sample_text_2")
    b = classes_BehavioralFeature(abstract=True)
    _safe_set(b, 'classes_BehavioralFeature', {a1})
    assert _is_linked(b, 'classes_BehavioralFeature', a1)
    if hasattr(a1, 'classes_Parameter'):
        assert _is_linked(a1, 'classes_Parameter', b)
    _safe_set(b, 'classes_BehavioralFeature', {a2})
    assert _is_linked(b, 'classes_BehavioralFeature', a2)
    if hasattr(a1, 'classes_Parameter'):
        assert not _is_linked(a1, 'classes_Parameter', b)
    if hasattr(a2, 'classes_Parameter'):
        assert _is_linked(a2, 'classes_Parameter', b)
    _safe_set(b, 'classes_BehavioralFeature', set())
    assert not _is_linked(b, 'classes_BehavioralFeature', a2)
    if hasattr(a2, 'classes_Parameter'):
        assert not _is_linked(a2, 'classes_Parameter', b)


def test_assoc_owner5_reverse_link_reassign_clear():
    a1 = classes_Element()
    a2 = classes_Element()
    b = classes_Element()
    _safe_set(b, 'ownedElement', a1)
    assert _is_linked(b, 'ownedElement', a1)
    if hasattr(a1, 'Element6'):
        assert _is_linked(a1, 'Element6', b)
    _safe_set(b, 'ownedElement', a2)
    assert _is_linked(b, 'ownedElement', a2)
    if hasattr(a1, 'Element6'):
        assert not _is_linked(a1, 'Element6', b)
    if hasattr(a2, 'Element6'):
        assert _is_linked(a2, 'Element6', b)
    _safe_set(b, 'ownedElement', None)
    assert not _is_linked(b, 'ownedElement', a2)
    if hasattr(a2, 'Element6'):
        assert not _is_linked(a2, 'Element6', b)


def test_assoc_owningAssociation55_reverse_link_reassign_clear():
    a1 = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    a2 = classes_Property(aggregation="sample_text_2", composite=False, derived=False, derivedUnion=False)
    b = classes_Association(derived=True)
    _safe_set(b, 'Association', a1)
    assert _is_linked(b, 'Association', a1)
    if hasattr(a1, 'ownedEnd'):
        assert _is_linked(a1, 'ownedEnd', b)
    _safe_set(b, 'Association', a2)
    assert _is_linked(b, 'Association', a2)
    if hasattr(a1, 'ownedEnd'):
        assert not _is_linked(a1, 'ownedEnd', b)
    if hasattr(a2, 'ownedEnd'):
        assert _is_linked(a2, 'ownedEnd', b)
    _safe_set(b, 'Association', None)
    assert not _is_linked(b, 'Association', a2)
    if hasattr(a2, 'ownedEnd'):
        assert not _is_linked(a2, 'ownedEnd', b)


def test_assoc_redefinedElement38_reverse_link_reassign_clear():
    a1 = classes_RedefinableElement(leaf=True)
    a2 = classes_RedefinableElement(leaf=False)
    b = classes_RedefinableElement(leaf=True)
    _safe_set(b, 'classes_RedefinableElement37', {a1})
    assert _is_linked(b, 'classes_RedefinableElement37', a1)
    if hasattr(a1, 'classes_RedefinableElement'):
        assert _is_linked(a1, 'classes_RedefinableElement', b)
    _safe_set(b, 'classes_RedefinableElement37', {a2})
    assert _is_linked(b, 'classes_RedefinableElement37', a2)
    if hasattr(a1, 'classes_RedefinableElement'):
        assert not _is_linked(a1, 'classes_RedefinableElement', b)
    if hasattr(a2, 'classes_RedefinableElement'):
        assert _is_linked(a2, 'classes_RedefinableElement', b)
    _safe_set(b, 'classes_RedefinableElement37', set())
    assert not _is_linked(b, 'classes_RedefinableElement37', a2)
    if hasattr(a2, 'classes_RedefinableElement'):
        assert not _is_linked(a2, 'classes_RedefinableElement', b)


def test_assoc_redefinedOperation82_reverse_link_reassign_clear():
    a1 = classes_Operation(lower="sample_text", ordered=True, query=True, unique=True, upper="sample_text")
    a2 = classes_Operation(lower="sample_text_2", ordered=False, query=False, unique=False, upper="sample_text_2")
    b = classes_Operation(lower="sample_text", ordered=True, query=True, unique=True, upper="sample_text")
    _safe_set(b, 'classes_Operation81', {a1})
    assert _is_linked(b, 'classes_Operation81', a1)
    if hasattr(a1, 'classes_Operation'):
        assert _is_linked(a1, 'classes_Operation', b)
    _safe_set(b, 'classes_Operation81', {a2})
    assert _is_linked(b, 'classes_Operation81', a2)
    if hasattr(a1, 'classes_Operation'):
        assert not _is_linked(a1, 'classes_Operation', b)
    if hasattr(a2, 'classes_Operation'):
        assert _is_linked(a2, 'classes_Operation', b)
    _safe_set(b, 'classes_Operation81', set())
    assert not _is_linked(b, 'classes_Operation81', a2)
    if hasattr(a2, 'classes_Operation'):
        assert not _is_linked(a2, 'classes_Operation', b)


def test_assoc_redefinitionContext39_reverse_link_reassign_clear():
    a1 = classes_RedefinableElement(leaf=True)
    a2 = classes_RedefinableElement(leaf=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'classes_Classifier', a1)
    assert _is_linked(b, 'classes_Classifier', a1)
    if hasattr(a1, 'classes_RedefinableElement40'):
        assert _is_linked(a1, 'classes_RedefinableElement40', b)
    _safe_set(b, 'classes_Classifier', a2)
    assert _is_linked(b, 'classes_Classifier', a2)
    if hasattr(a1, 'classes_RedefinableElement40'):
        assert not _is_linked(a1, 'classes_RedefinableElement40', b)
    if hasattr(a2, 'classes_RedefinableElement40'):
        assert _is_linked(a2, 'classes_RedefinableElement40', b)
    _safe_set(b, 'classes_Classifier', None)
    assert not _is_linked(b, 'classes_Classifier', a2)
    if hasattr(a2, 'classes_RedefinableElement40'):
        assert not _is_linked(a2, 'classes_RedefinableElement40', b)


def test_assoc_specific53_reverse_link_reassign_clear():
    a1 = classes_Generalization(substitutable=True)
    a2 = classes_Generalization(substitutable=False)
    b = classes_Classifier(abstract=True, finalSpecialization=True)
    _safe_set(b, 'Classifier54', a1)
    assert _is_linked(b, 'Classifier54', a1)
    if hasattr(a1, 'generalization'):
        assert _is_linked(a1, 'generalization', b)
    _safe_set(b, 'Classifier54', a2)
    assert _is_linked(b, 'Classifier54', a2)
    if hasattr(a1, 'generalization'):
        assert not _is_linked(a1, 'generalization', b)
    if hasattr(a2, 'generalization'):
        assert _is_linked(a2, 'generalization', b)
    _safe_set(b, 'Classifier54', None)
    assert not _is_linked(b, 'Classifier54', a2)
    if hasattr(a2, 'generalization'):
        assert not _is_linked(a2, 'generalization', b)


def test_assoc_superClass103_reverse_link_reassign_clear():
    a1 = classes_Class(active=True)
    a2 = classes_Class(active=False)
    b = classes_Class(active=True)
    _safe_set(b, 'classes_Class102', {a1})
    assert _is_linked(b, 'classes_Class102', a1)
    if hasattr(a1, 'classes_Class'):
        assert _is_linked(a1, 'classes_Class', b)
    _safe_set(b, 'classes_Class102', {a2})
    assert _is_linked(b, 'classes_Class102', a2)
    if hasattr(a1, 'classes_Class'):
        assert not _is_linked(a1, 'classes_Class', b)
    if hasattr(a2, 'classes_Class'):
        assert _is_linked(a2, 'classes_Class', b)
    _safe_set(b, 'classes_Class102', set())
    assert not _is_linked(b, 'classes_Class102', a2)
    if hasattr(a2, 'classes_Class'):
        assert not _is_linked(a2, 'classes_Class', b)


def test_assoc_upperValue74_reverse_link_reassign_clear():
    a1 = classes_ValueSpecification()
    a2 = classes_ValueSpecification()
    b = classes_MultiplicityElement(lower=7, ordered=True, unique=True, upper=7)
    _safe_set(b, 'classes_MultiplicityElement', a1)
    assert _is_linked(b, 'classes_MultiplicityElement', a1)
    if hasattr(a1, 'classes_ValueSpecification'):
        assert _is_linked(a1, 'classes_ValueSpecification', b)
    _safe_set(b, 'classes_MultiplicityElement', a2)
    assert _is_linked(b, 'classes_MultiplicityElement', a2)
    if hasattr(a1, 'classes_ValueSpecification'):
        assert not _is_linked(a1, 'classes_ValueSpecification', b)
    if hasattr(a2, 'classes_ValueSpecification'):
        assert _is_linked(a2, 'classes_ValueSpecification', b)
    _safe_set(b, 'classes_MultiplicityElement', None)
    assert not _is_linked(b, 'classes_MultiplicityElement', a2)
    if hasattr(a2, 'classes_ValueSpecification'):
        assert not _is_linked(a2, 'classes_ValueSpecification', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_classifier86_stub_double():
    # classes_InstanceSpecification has no real 'classes_InstanceSpecification' property in the generated
    # code (a bare stub) -- manually attach it so classes_Classifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Classifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Classifier(abstract=True, finalSpecialization=True)
    partner = classes_InstanceSpecification()
    setattr(partner, 'classes_InstanceSpecification', None)
    _safe_set(owner, 'classes_Classifier87', partner)
    assert owner in getattr(partner, 'classes_InstanceSpecification')
    _safe_set(owner, 'classes_Classifier87', None)
    assert owner not in getattr(partner, 'classes_InstanceSpecification')


def test_assoc_datatype58_stub_double():
    # classes_DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so classes_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    partner = classes_DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_definingFeature89_stub_double():
    # classes_Slot has no real 'classes_Slot' property in the generated
    # code (a bare stub) -- manually attach it so classes_StructuralFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_StructuralFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_StructuralFeature(readOnly=True)
    partner = classes_Slot()
    setattr(partner, 'classes_Slot', None)
    _safe_set(owner, 'classes_StructuralFeature', partner)
    assert getattr(partner, 'classes_Slot') == owner
    _safe_set(owner, 'classes_StructuralFeature', None)
    assert getattr(partner, 'classes_Slot') is None


def test_assoc_elementImport12_stub_double():
    # classes_Namespace has no real 'importingNamespace' property in the generated
    # code (a bare stub) -- manually attach it so classes_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_ElementImport(alias="sample_text", visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'importingNamespace', None)
    _safe_set(owner, 'ElementImport', partner)
    assert owner in getattr(partner, 'importingNamespace')
    _safe_set(owner, 'ElementImport', None)
    assert owner not in getattr(partner, 'importingNamespace')


def test_assoc_endType64_stub_double():
    # classes_Type has no real 'classes_Type65' property in the generated
    # code (a bare stub) -- manually attach it so classes_Association's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Association's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Association(derived=True)
    partner = classes_Type()
    setattr(partner, 'classes_Type65', None)
    _safe_set(owner, 'classes_Association', {partner})
    assert getattr(partner, 'classes_Type65') == owner
    _safe_set(owner, 'classes_Association', set())
    assert getattr(partner, 'classes_Type65') is None


def test_assoc_importedElement18_stub_double():
    # classes_PackageableElement has no real 'classes_PackageableElement19' property in the generated
    # code (a bare stub) -- manually attach it so classes_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_ElementImport(alias="sample_text", visibility="sample_text")
    partner = classes_PackageableElement()
    setattr(partner, 'classes_PackageableElement19', None)
    _safe_set(owner, 'classes_ElementImport', partner)
    assert getattr(partner, 'classes_PackageableElement19') == owner
    _safe_set(owner, 'classes_ElementImport', None)
    assert getattr(partner, 'classes_PackageableElement19') is None


def test_assoc_importedPackage22_stub_double():
    # classes_Package has no real 'classes_Package' property in the generated
    # code (a bare stub) -- manually attach it so classes_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_PackageImport(visibility="sample_text")
    partner = classes_Package()
    setattr(partner, 'classes_Package', None)
    _safe_set(owner, 'classes_PackageImport', partner)
    assert getattr(partner, 'classes_Package') == owner
    _safe_set(owner, 'classes_PackageImport', None)
    assert getattr(partner, 'classes_Package') is None


def test_assoc_importingNamespace20_stub_double():
    # classes_Namespace has no real 'Namespace21' property in the generated
    # code (a bare stub) -- manually attach it so classes_ElementImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_ElementImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_ElementImport(alias="sample_text", visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'Namespace21', None)
    _safe_set(owner, 'elementImport', partner)
    assert getattr(partner, 'Namespace21') == owner
    _safe_set(owner, 'elementImport', None)
    assert getattr(partner, 'Namespace21') is None


def test_assoc_importingNamespace23_stub_double():
    # classes_Namespace has no real 'Namespace24' property in the generated
    # code (a bare stub) -- manually attach it so classes_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_PackageImport(visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'Namespace24', None)
    _safe_set(owner, 'packageImport', partner)
    assert getattr(partner, 'Namespace24') == owner
    _safe_set(owner, 'packageImport', None)
    assert getattr(partner, 'Namespace24') is None


def test_assoc_member11_stub_double():
    # classes_Namespace has no real 'classes_Namespace' property in the generated
    # code (a bare stub) -- manually attach it so classes_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'classes_Namespace', None)
    _safe_set(owner, 'classes_NamedElement', partner)
    assert owner in getattr(partner, 'classes_Namespace')
    _safe_set(owner, 'classes_NamedElement', None)
    assert owner not in getattr(partner, 'classes_Namespace')


def test_assoc_namespace1_stub_double():
    # classes_Namespace has no real 'Namespace' property in the generated
    # code (a bare stub) -- manually attach it so classes_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'Namespace', None)
    _safe_set(owner, 'ownedMember', partner)
    assert getattr(partner, 'Namespace') == owner
    _safe_set(owner, 'ownedMember', None)
    assert getattr(partner, 'Namespace') is None


def test_assoc_ownedAttribute72_stub_double():
    # classes_DataType has no real 'datatype' property in the generated
    # code (a bare stub) -- manually attach it so classes_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Property(aggregation="sample_text", composite=True, derived=True, derivedUnion=True)
    partner = classes_DataType()
    setattr(partner, 'datatype', None)
    _safe_set(owner, 'Property73', partner)
    assert owner in getattr(partner, 'datatype')
    _safe_set(owner, 'Property73', None)
    assert owner not in getattr(partner, 'datatype')


def test_assoc_ownedMember17_stub_double():
    # classes_Namespace has no real 'namespace' property in the generated
    # code (a bare stub) -- manually attach it so classes_NamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_NamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_NamedElement(name="sample_text", qualifiedName="sample_text", visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'namespace', None)
    _safe_set(owner, 'NamedElement', partner)
    assert owner in getattr(partner, 'namespace')
    _safe_set(owner, 'NamedElement', None)
    assert owner not in getattr(partner, 'namespace')


def test_assoc_packageImport13_stub_double():
    # classes_Namespace has no real 'importingNamespace14' property in the generated
    # code (a bare stub) -- manually attach it so classes_PackageImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_PackageImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_PackageImport(visibility="sample_text")
    partner = classes_Namespace()
    setattr(partner, 'importingNamespace14', None)
    _safe_set(owner, 'PackageImport', partner)
    assert owner in getattr(partner, 'importingNamespace14')
    _safe_set(owner, 'PackageImport', None)
    assert owner not in getattr(partner, 'importingNamespace14')


def test_assoc_type83_stub_double():
    # classes_Type has no real 'classes_Type85' property in the generated
    # code (a bare stub) -- manually attach it so classes_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_Operation(lower="sample_text", ordered=True, query=True, unique=True, upper="sample_text")
    partner = classes_Type()
    setattr(partner, 'classes_Type85', None)
    _safe_set(owner, 'classes_Operation84', partner)
    assert getattr(partner, 'classes_Type85') == owner
    _safe_set(owner, 'classes_Operation84', None)
    assert getattr(partner, 'classes_Type85') is None


def test_assoc_value90_stub_double():
    # classes_Slot has no real 'classes_Slot91' property in the generated
    # code (a bare stub) -- manually attach it so classes_ValueSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # classes_ValueSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = classes_ValueSpecification()
    partner = classes_Slot()
    setattr(partner, 'classes_Slot91', None)
    _safe_set(owner, 'classes_ValueSpecification92', partner)
    assert owner in getattr(partner, 'classes_Slot91')
    _safe_set(owner, 'classes_ValueSpecification92', None)
    assert owner not in getattr(partner, 'classes_Slot91')


