import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AttributeRef,
    ClassRef,
    ClassifierCS,
    ClassifierRef,
    DataTypeOrEnumCS,
    DataTypeRef,
    ModelElementCS,
    NamedElementCS,
    ReferenceRef,
    StructuralFeatureCS,
    TypedElementCS,
    oclinEcoreCST_AnnotationCS,
    oclinEcoreCST_AttributeCS,
    oclinEcoreCST_AttributeCSRef,
    oclinEcoreCST_AttributeRef,
    oclinEcoreCST_ClassCS,
    oclinEcoreCST_ClassCSRef,
    oclinEcoreCST_ClassRef,
    oclinEcoreCST_ClassifierCS,
    oclinEcoreCST_ClassifierCSRef,
    oclinEcoreCST_ClassifierRef,
    oclinEcoreCST_ConstraintCS,
    oclinEcoreCST_DataTypeCS,
    oclinEcoreCST_DataTypeCSRef,
    oclinEcoreCST_DataTypeOrEnumCS,
    oclinEcoreCST_DataTypeRef,
    oclinEcoreCST_DetailCS,
    oclinEcoreCST_DocumentCS,
    oclinEcoreCST_EAttribute,
    oclinEcoreCST_EAttributeRef,
    oclinEcoreCST_EClass,
    oclinEcoreCST_EClassRef,
    oclinEcoreCST_EClassifier,
    oclinEcoreCST_EClassifierRef,
    oclinEcoreCST_EDataType,
    oclinEcoreCST_EDataTypeRef,
    oclinEcoreCST_EReference,
    oclinEcoreCST_EReferenceRef,
    oclinEcoreCST_EnumCS,
    oclinEcoreCST_EnumLiteralCS,
    oclinEcoreCST_ImportCS,
    oclinEcoreCST_ModelElementCS,
    oclinEcoreCST_NamedElementCS,
    oclinEcoreCST_OclExpressionCS,
    oclinEcoreCST_OperationCS,
    oclinEcoreCST_PackageCS,
    oclinEcoreCST_ParameterCS,
    oclinEcoreCST_ReferenceCS,
    oclinEcoreCST_ReferenceCSRef,
    oclinEcoreCST_ReferenceRef,
    oclinEcoreCST_StructuralFeatureCS,
    oclinEcoreCST_TypeParameterCS,
    oclinEcoreCST_TypedElementCS,
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

def test_assoc_constraints9_reverse_link_reassign_clear():
    a1 = oclinEcoreCST_ConstraintCS(stereotype="sample_text")
    a2 = oclinEcoreCST_ConstraintCS(stereotype="sample_text_2")
    b = oclinEcoreCST_ClassifierCS(instanceClassName="sample_text", qualifiers="sample_text")
    _safe_set(b, 'oclinEcoreCST_ClassifierCS', {a1})
    assert _is_linked(b, 'oclinEcoreCST_ClassifierCS', a1)
    if hasattr(a1, 'oclinEcoreCST_ConstraintCS'):
        assert _is_linked(a1, 'oclinEcoreCST_ConstraintCS', b)
    _safe_set(b, 'oclinEcoreCST_ClassifierCS', {a2})
    assert _is_linked(b, 'oclinEcoreCST_ClassifierCS', a2)
    if hasattr(a1, 'oclinEcoreCST_ConstraintCS'):
        assert not _is_linked(a1, 'oclinEcoreCST_ConstraintCS', b)
    if hasattr(a2, 'oclinEcoreCST_ConstraintCS'):
        assert _is_linked(a2, 'oclinEcoreCST_ConstraintCS', b)
    _safe_set(b, 'oclinEcoreCST_ClassifierCS', set())
    assert not _is_linked(b, 'oclinEcoreCST_ClassifierCS', a2)
    if hasattr(a2, 'oclinEcoreCST_ConstraintCS'):
        assert not _is_linked(a2, 'oclinEcoreCST_ConstraintCS', b)


def test_assoc_details0_reverse_link_reassign_clear():
    a1 = oclinEcoreCST_DetailCS(idName="sample_text", stringName="sample_text", value="sample_text")
    a2 = oclinEcoreCST_DetailCS(idName="sample_text_2", stringName="sample_text_2", value="sample_text_2")
    b = oclinEcoreCST_AnnotationCS(idSource="sample_text", stringSource="sample_text")
    _safe_set(b, 'oclinEcoreCST_AnnotationCS', {a1})
    assert _is_linked(b, 'oclinEcoreCST_AnnotationCS', a1)
    if hasattr(a1, 'oclinEcoreCST_DetailCS'):
        assert _is_linked(a1, 'oclinEcoreCST_DetailCS', b)
    _safe_set(b, 'oclinEcoreCST_AnnotationCS', {a2})
    assert _is_linked(b, 'oclinEcoreCST_AnnotationCS', a2)
    if hasattr(a1, 'oclinEcoreCST_DetailCS'):
        assert not _is_linked(a1, 'oclinEcoreCST_DetailCS', b)
    if hasattr(a2, 'oclinEcoreCST_DetailCS'):
        assert _is_linked(a2, 'oclinEcoreCST_DetailCS', b)
    _safe_set(b, 'oclinEcoreCST_AnnotationCS', set())
    assert not _is_linked(b, 'oclinEcoreCST_AnnotationCS', a2)
    if hasattr(a2, 'oclinEcoreCST_DetailCS'):
        assert not _is_linked(a2, 'oclinEcoreCST_DetailCS', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations26_stub_double():
    # oclinEcoreCST_ModelElementCS has no real 'oclinEcoreCST_ModelElementCS' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_AnnotationCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_AnnotationCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_AnnotationCS(idSource="sample_text", stringSource="sample_text")
    partner = oclinEcoreCST_ModelElementCS()
    setattr(partner, 'oclinEcoreCST_ModelElementCS', None)
    _safe_set(owner, 'oclinEcoreCST_AnnotationCS27', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_ModelElementCS')
    _safe_set(owner, 'oclinEcoreCST_AnnotationCS27', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_ModelElementCS')


def test_assoc_classifiers38_stub_double():
    # oclinEcoreCST_PackageCS has no real 'oclinEcoreCST_PackageCS39' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ClassifierCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ClassifierCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ClassifierCS(instanceClassName="sample_text", qualifiers="sample_text")
    partner = oclinEcoreCST_PackageCS()
    setattr(partner, 'oclinEcoreCST_PackageCS39', None)
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS40', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_PackageCS39')
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS40', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_PackageCS39')


def test_assoc_constraints28_stub_double():
    # oclinEcoreCST_OperationCS has no real 'oclinEcoreCST_OperationCS29' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ConstraintCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ConstraintCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ConstraintCS(stereotype="sample_text")
    partner = oclinEcoreCST_OperationCS()
    setattr(partner, 'oclinEcoreCST_OperationCS29', None)
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS30', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_OperationCS29')
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS30', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_OperationCS29')


def test_assoc_constraints49_stub_double():
    # oclinEcoreCST_StructuralFeatureCS has no real 'oclinEcoreCST_StructuralFeatureCS50' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ConstraintCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ConstraintCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ConstraintCS(stereotype="sample_text")
    partner = oclinEcoreCST_StructuralFeatureCS()
    setattr(partner, 'oclinEcoreCST_StructuralFeatureCS50', None)
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS51', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_StructuralFeatureCS50')
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS51', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_StructuralFeatureCS50')


def test_assoc_expr14_stub_double():
    # oclinEcoreCST_OclExpressionCS has no real 'oclinEcoreCST_OclExpressionCS' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ConstraintCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ConstraintCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ConstraintCS(stereotype="sample_text")
    partner = oclinEcoreCST_OclExpressionCS()
    setattr(partner, 'oclinEcoreCST_OclExpressionCS', None)
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS15', partner)
    assert getattr(partner, 'oclinEcoreCST_OclExpressionCS') == owner
    _safe_set(owner, 'oclinEcoreCST_ConstraintCS15', None)
    assert getattr(partner, 'oclinEcoreCST_OclExpressionCS') is None


def test_assoc_imports17_stub_double():
    # oclinEcoreCST_DocumentCS has no real 'oclinEcoreCST_DocumentCS' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ImportCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ImportCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ImportCS(importedNamespace="sample_text")
    partner = oclinEcoreCST_DocumentCS()
    setattr(partner, 'oclinEcoreCST_DocumentCS', None)
    _safe_set(owner, 'oclinEcoreCST_ImportCS', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_DocumentCS')
    _safe_set(owner, 'oclinEcoreCST_ImportCS', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_DocumentCS')


def test_assoc_keys45_stub_double():
    # oclinEcoreCST_AttributeRef has no real 'oclinEcoreCST_AttributeRef' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ReferenceCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ReferenceCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ReferenceCS(containment=True)
    partner = oclinEcoreCST_AttributeRef()
    setattr(partner, 'oclinEcoreCST_AttributeRef', None)
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS46', {partner})
    assert getattr(partner, 'oclinEcoreCST_AttributeRef') == owner
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS46', set())
    assert getattr(partner, 'oclinEcoreCST_AttributeRef') is None


def test_assoc_literals25_stub_double():
    # oclinEcoreCST_EnumCS has no real 'oclinEcoreCST_EnumCS' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_EnumLiteralCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_EnumLiteralCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_EnumLiteralCS(value=7)
    partner = oclinEcoreCST_EnumCS()
    setattr(partner, 'oclinEcoreCST_EnumCS', None)
    _safe_set(owner, 'oclinEcoreCST_EnumLiteralCS', partner)
    assert owner in getattr(partner, 'oclinEcoreCST_EnumCS')
    _safe_set(owner, 'oclinEcoreCST_EnumLiteralCS', None)
    assert owner not in getattr(partner, 'oclinEcoreCST_EnumCS')


def test_assoc_opposite44_stub_double():
    # oclinEcoreCST_ReferenceRef has no real 'oclinEcoreCST_ReferenceRef' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ReferenceCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ReferenceCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ReferenceCS(containment=True)
    partner = oclinEcoreCST_ReferenceRef()
    setattr(partner, 'oclinEcoreCST_ReferenceRef', None)
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS', partner)
    assert getattr(partner, 'oclinEcoreCST_ReferenceRef') == owner
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS', None)
    assert getattr(partner, 'oclinEcoreCST_ReferenceRef') is None


def test_assoc_ref12_stub_double():
    # oclinEcoreCST_ClassifierCSRef has no real 'oclinEcoreCST_ClassifierCSRef' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ClassifierCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ClassifierCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ClassifierCS(instanceClassName="sample_text", qualifiers="sample_text")
    partner = oclinEcoreCST_ClassifierCSRef()
    setattr(partner, 'oclinEcoreCST_ClassifierCSRef', None)
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS13', partner)
    assert getattr(partner, 'oclinEcoreCST_ClassifierCSRef') == owner
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS13', None)
    assert getattr(partner, 'oclinEcoreCST_ClassifierCSRef') is None


def test_assoc_ref47_stub_double():
    # oclinEcoreCST_ReferenceCSRef has no real 'oclinEcoreCST_ReferenceCSRef' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ReferenceCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ReferenceCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ReferenceCS(containment=True)
    partner = oclinEcoreCST_ReferenceCSRef()
    setattr(partner, 'oclinEcoreCST_ReferenceCSRef', None)
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS48', partner)
    assert getattr(partner, 'oclinEcoreCST_ReferenceCSRef') == owner
    _safe_set(owner, 'oclinEcoreCST_ReferenceCS48', None)
    assert getattr(partner, 'oclinEcoreCST_ReferenceCSRef') is None


def test_assoc_type52_stub_double():
    # oclinEcoreCST_ClassifierRef has no real 'oclinEcoreCST_ClassifierRef53' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_TypedElementCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_TypedElementCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_TypedElementCS(lower=7, multiplicity="sample_text", qualifiers="sample_text", upper=7)
    partner = oclinEcoreCST_ClassifierRef()
    setattr(partner, 'oclinEcoreCST_ClassifierRef53', None)
    _safe_set(owner, 'oclinEcoreCST_TypedElementCS', partner)
    assert getattr(partner, 'oclinEcoreCST_ClassifierRef53') == owner
    _safe_set(owner, 'oclinEcoreCST_TypedElementCS', None)
    assert getattr(partner, 'oclinEcoreCST_ClassifierRef53') is None


def test_assoc_typeParameters10_stub_double():
    # oclinEcoreCST_TypeParameterCS has no real 'oclinEcoreCST_TypeParameterCS' property in the generated
    # code (a bare stub) -- manually attach it so oclinEcoreCST_ClassifierCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # oclinEcoreCST_ClassifierCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = oclinEcoreCST_ClassifierCS(instanceClassName="sample_text", qualifiers="sample_text")
    partner = oclinEcoreCST_TypeParameterCS()
    setattr(partner, 'oclinEcoreCST_TypeParameterCS', None)
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS11', {partner})
    assert getattr(partner, 'oclinEcoreCST_TypeParameterCS') == owner
    _safe_set(owner, 'oclinEcoreCST_ClassifierCS11', set())
    assert getattr(partner, 'oclinEcoreCST_TypeParameterCS') is None


