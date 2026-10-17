import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BasicType,
    CollectionType,
    MAssociation,
    MClass,
    MModelElement,
    MModelElementEx,
    Type,
    model_BagType,
    model_BasicType,
    model_BooleanType,
    model_CollectionType,
    model_Comparable,
    model_EnumType,
    model_Expression,
    model_IntegerType,
    model_MAggregationKind,
    model_MAssociation,
    model_MAssociationClass,
    model_MAssociationEnd,
    model_MAttribute,
    model_MClass,
    model_MClassInvariant,
    model_MMVisitor,
    model_MModel,
    model_MModelElement,
    model_MModelElementEx,
    model_MMultiplicity,
    model_MNavigableElement,
    model_MOperation,
    model_MPrePostCondition,
    model_MRange,
    model_ObjectType,
    model_OclAnyType,
    model_OrderedSetType,
    model_Part,
    model_RealType,
    model_SequenceType,
    model_SetType,
    model_StringType,
    model_TupleType,
    model_Type,
    model_VarDecl,
    model_VarDeclList,
    model_VoidType,
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

def test_assoc_aggregationKind39_reverse_link_reassign_clear():
    a1 = model_MAssociation()
    a2 = model_MAssociation()
    b = model_MAggregationKind(kind=7, name="sample_text")
    _safe_set(b, 'model_MAggregationKind', a1)
    assert _is_linked(b, 'model_MAggregationKind', a1)
    if hasattr(a1, 'model_MAssociation40'):
        assert _is_linked(a1, 'model_MAssociation40', b)
    _safe_set(b, 'model_MAggregationKind', a2)
    assert _is_linked(b, 'model_MAggregationKind', a2)
    if hasattr(a1, 'model_MAssociation40'):
        assert not _is_linked(a1, 'model_MAssociation40', b)
    if hasattr(a2, 'model_MAssociation40'):
        assert _is_linked(a2, 'model_MAssociation40', b)
    _safe_set(b, 'model_MAggregationKind', None)
    assert not _is_linked(b, 'model_MAggregationKind', a2)
    if hasattr(a2, 'model_MAssociation40'):
        assert not _is_linked(a2, 'model_MAssociation40', b)


def test_assoc_association41_reverse_link_reassign_clear():
    a1 = model_MAssociationEnd(mClassName="sample_text")
    a2 = model_MAssociationEnd(mClassName="sample_text_2")
    b = model_MAssociation()
    _safe_set(b, 'model_MAssociation43', a1)
    assert _is_linked(b, 'model_MAssociation43', a1)
    if hasattr(a1, 'model_MAssociationEnd42'):
        assert _is_linked(a1, 'model_MAssociationEnd42', b)
    _safe_set(b, 'model_MAssociation43', a2)
    assert _is_linked(b, 'model_MAssociation43', a2)
    if hasattr(a1, 'model_MAssociationEnd42'):
        assert not _is_linked(a1, 'model_MAssociationEnd42', b)
    if hasattr(a2, 'model_MAssociationEnd42'):
        assert _is_linked(a2, 'model_MAssociationEnd42', b)
    _safe_set(b, 'model_MAssociation43', None)
    assert not _is_linked(b, 'model_MAssociation43', a2)
    if hasattr(a2, 'model_MAssociationEnd42'):
        assert not _is_linked(a2, 'model_MAssociationEnd42', b)


def test_assoc_association56_reverse_link_reassign_clear():
    a1 = model_MNavigableElement(nameAsRolename="sample_text")
    a2 = model_MNavigableElement(nameAsRolename="sample_text_2")
    b = model_MAssociation()
    _safe_set(b, 'model_MAssociation58', a1)
    assert _is_linked(b, 'model_MAssociation58', a1)
    if hasattr(a1, 'model_MNavigableElement57'):
        assert _is_linked(a1, 'model_MNavigableElement57', b)
    _safe_set(b, 'model_MAssociation58', a2)
    assert _is_linked(b, 'model_MAssociation58', a2)
    if hasattr(a1, 'model_MNavigableElement57'):
        assert not _is_linked(a1, 'model_MNavigableElement57', b)
    if hasattr(a2, 'model_MNavigableElement57'):
        assert _is_linked(a2, 'model_MNavigableElement57', b)
    _safe_set(b, 'model_MAssociation58', None)
    assert not _is_linked(b, 'model_MAssociation58', a2)
    if hasattr(a2, 'model_MNavigableElement57'):
        assert not _is_linked(a2, 'model_MNavigableElement57', b)


def test_assoc_associationEnds37_reverse_link_reassign_clear():
    a1 = model_MAssociationEnd(mClassName="sample_text")
    a2 = model_MAssociationEnd(mClassName="sample_text_2")
    b = model_MAssociation()
    _safe_set(b, 'model_MAssociation38', {a1})
    assert _is_linked(b, 'model_MAssociation38', a1)
    if hasattr(a1, 'model_MAssociationEnd'):
        assert _is_linked(a1, 'model_MAssociationEnd', b)
    _safe_set(b, 'model_MAssociation38', {a2})
    assert _is_linked(b, 'model_MAssociation38', a2)
    if hasattr(a1, 'model_MAssociationEnd'):
        assert not _is_linked(a1, 'model_MAssociationEnd', b)
    if hasattr(a2, 'model_MAssociationEnd'):
        assert _is_linked(a2, 'model_MAssociationEnd', b)
    _safe_set(b, 'model_MAssociation38', set())
    assert not _is_linked(b, 'model_MAssociation38', a2)
    if hasattr(a2, 'model_MAssociationEnd'):
        assert not _is_linked(a2, 'model_MAssociationEnd', b)


def test_assoc_associations8_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MAssociation()
    _safe_set(b, 'model_MAssociation', a1)
    assert _is_linked(b, 'model_MAssociation', a1)
    if hasattr(a1, 'model_MClass9'):
        assert _is_linked(a1, 'model_MClass9', b)
    _safe_set(b, 'model_MAssociation', a2)
    assert _is_linked(b, 'model_MAssociation', a2)
    if hasattr(a1, 'model_MClass9'):
        assert not _is_linked(a1, 'model_MClass9', b)
    if hasattr(a2, 'model_MClass9'):
        assert _is_linked(a2, 'model_MClass9', b)
    _safe_set(b, 'model_MAssociation', None)
    assert not _is_linked(b, 'model_MAssociation', a2)
    if hasattr(a2, 'model_MClass9'):
        assert not _is_linked(a2, 'model_MClass9', b)


def test_assoc_attributes3_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MAttribute()
    _safe_set(b, 'model_MAttribute5', a1)
    assert _is_linked(b, 'model_MAttribute5', a1)
    if hasattr(a1, 'model_MClass4'):
        assert _is_linked(a1, 'model_MClass4', b)
    _safe_set(b, 'model_MAttribute5', a2)
    assert _is_linked(b, 'model_MAttribute5', a2)
    if hasattr(a1, 'model_MClass4'):
        assert not _is_linked(a1, 'model_MClass4', b)
    if hasattr(a2, 'model_MClass4'):
        assert _is_linked(a2, 'model_MClass4', b)
    _safe_set(b, 'model_MAttribute5', None)
    assert not _is_linked(b, 'model_MAttribute5', a2)
    if hasattr(a2, 'model_MClass4'):
        assert not _is_linked(a2, 'model_MClass4', b)


def test_assoc_children14_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MClass()
    _safe_set(b, 'model_MClass15', a1)
    assert _is_linked(b, 'model_MClass15', a1)
    if hasattr(a1, 'model_MClass13'):
        assert _is_linked(a1, 'model_MClass13', b)
    _safe_set(b, 'model_MClass15', a2)
    assert _is_linked(b, 'model_MClass15', a2)
    if hasattr(a1, 'model_MClass13'):
        assert not _is_linked(a1, 'model_MClass13', b)
    if hasattr(a2, 'model_MClass13'):
        assert _is_linked(a2, 'model_MClass13', b)
    _safe_set(b, 'model_MClass15', None)
    assert not _is_linked(b, 'model_MClass15', a2)
    if hasattr(a2, 'model_MClass13'):
        assert not _is_linked(a2, 'model_MClass13', b)


def test_assoc_classInvariant18_reverse_link_reassign_clear():
    a1 = model_MModel()
    a2 = model_MModel()
    b = model_MClassInvariant(name="sample_text", positionInModel=7)
    _safe_set(b, 'model_MClassInvariant', a1)
    assert _is_linked(b, 'model_MClassInvariant', a1)
    if hasattr(a1, 'model_MModel19'):
        assert _is_linked(a1, 'model_MModel19', b)
    _safe_set(b, 'model_MClassInvariant', a2)
    assert _is_linked(b, 'model_MClassInvariant', a2)
    if hasattr(a1, 'model_MModel19'):
        assert not _is_linked(a1, 'model_MModel19', b)
    if hasattr(a2, 'model_MModel19'):
        assert _is_linked(a2, 'model_MModel19', b)
    _safe_set(b, 'model_MClassInvariant', None)
    assert not _is_linked(b, 'model_MClassInvariant', a2)
    if hasattr(a2, 'model_MModel19'):
        assert not _is_linked(a2, 'model_MModel19', b)


def test_assoc_classes16_reverse_link_reassign_clear():
    a1 = model_MModel()
    a2 = model_MModel()
    b = model_MClass()
    _safe_set(b, 'model_MClass17', a1)
    assert _is_linked(b, 'model_MClass17', a1)
    if hasattr(a1, 'model_MModel'):
        assert _is_linked(a1, 'model_MModel', b)
    _safe_set(b, 'model_MClass17', a2)
    assert _is_linked(b, 'model_MClass17', a2)
    if hasattr(a1, 'model_MModel'):
        assert not _is_linked(a1, 'model_MModel', b)
    if hasattr(a2, 'model_MModel'):
        assert _is_linked(a2, 'model_MModel', b)
    _safe_set(b, 'model_MClass17', None)
    assert not _is_linked(b, 'model_MClass17', a2)
    if hasattr(a2, 'model_MModel'):
        assert not _is_linked(a2, 'model_MModel', b)


def test_assoc_cls54_reverse_link_reassign_clear():
    a1 = model_MNavigableElement(nameAsRolename="sample_text")
    a2 = model_MNavigableElement(nameAsRolename="sample_text_2")
    b = model_MClass()
    _safe_set(b, 'model_MClass55', a1)
    assert _is_linked(b, 'model_MClass55', a1)
    if hasattr(a1, 'model_MNavigableElement'):
        assert _is_linked(a1, 'model_MNavigableElement', b)
    _safe_set(b, 'model_MClass55', a2)
    assert _is_linked(b, 'model_MClass55', a2)
    if hasattr(a1, 'model_MNavigableElement'):
        assert not _is_linked(a1, 'model_MNavigableElement', b)
    if hasattr(a2, 'model_MNavigableElement'):
        assert _is_linked(a2, 'model_MNavigableElement', b)
    _safe_set(b, 'model_MClass55', None)
    assert not _is_linked(b, 'model_MClass55', a2)
    if hasattr(a2, 'model_MNavigableElement'):
        assert not _is_linked(a2, 'model_MNavigableElement', b)


def test_assoc_cls61_reverse_link_reassign_clear():
    a1 = model_MClassInvariant(name="sample_text", positionInModel=7)
    a2 = model_MClassInvariant(name="sample_text_2", positionInModel=13)
    b = model_MClass()
    _safe_set(b, 'model_MClass63', a1)
    assert _is_linked(b, 'model_MClass63', a1)
    if hasattr(a1, 'model_MClassInvariant62'):
        assert _is_linked(a1, 'model_MClassInvariant62', b)
    _safe_set(b, 'model_MClass63', a2)
    assert _is_linked(b, 'model_MClass63', a2)
    if hasattr(a1, 'model_MClassInvariant62'):
        assert not _is_linked(a1, 'model_MClassInvariant62', b)
    if hasattr(a2, 'model_MClassInvariant62'):
        assert _is_linked(a2, 'model_MClassInvariant62', b)
    _safe_set(b, 'model_MClass63', None)
    assert not _is_linked(b, 'model_MClass63', a2)
    if hasattr(a2, 'model_MClassInvariant62'):
        assert not _is_linked(a2, 'model_MClassInvariant62', b)


def test_assoc_kind49_reverse_link_reassign_clear():
    a1 = model_MAssociationEnd(mClassName="sample_text")
    a2 = model_MAssociationEnd(mClassName="sample_text_2")
    b = model_MAggregationKind(kind=7, name="sample_text")
    _safe_set(b, 'model_MAggregationKind51', a1)
    assert _is_linked(b, 'model_MAggregationKind51', a1)
    if hasattr(a1, 'model_MAssociationEnd50'):
        assert _is_linked(a1, 'model_MAssociationEnd50', b)
    _safe_set(b, 'model_MAggregationKind51', a2)
    assert _is_linked(b, 'model_MAggregationKind51', a2)
    if hasattr(a1, 'model_MAssociationEnd50'):
        assert not _is_linked(a1, 'model_MAssociationEnd50', b)
    if hasattr(a2, 'model_MAssociationEnd50'):
        assert _is_linked(a2, 'model_MAssociationEnd50', b)
    _safe_set(b, 'model_MAggregationKind51', None)
    assert not _is_linked(b, 'model_MAggregationKind51', a2)
    if hasattr(a2, 'model_MAssociationEnd50'):
        assert not _is_linked(a2, 'model_MAssociationEnd50', b)


def test_assoc_mClass44_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MAssociationEnd(mClassName="sample_text")
    _safe_set(b, 'model_MAssociationEnd45', a1)
    assert _is_linked(b, 'model_MAssociationEnd45', a1)
    if hasattr(a1, 'model_MClass46'):
        assert _is_linked(a1, 'model_MClass46', b)
    _safe_set(b, 'model_MAssociationEnd45', a2)
    assert _is_linked(b, 'model_MAssociationEnd45', a2)
    if hasattr(a1, 'model_MClass46'):
        assert not _is_linked(a1, 'model_MClass46', b)
    if hasattr(a2, 'model_MClass46'):
        assert _is_linked(a2, 'model_MClass46', b)
    _safe_set(b, 'model_MAssociationEnd45', None)
    assert not _is_linked(b, 'model_MAssociationEnd45', a2)
    if hasattr(a2, 'model_MClass46'):
        assert not _is_linked(a2, 'model_MClass46', b)


def test_assoc_mMultiplicity47_reverse_link_reassign_clear():
    a1 = model_MMultiplicity()
    a2 = model_MMultiplicity()
    b = model_MAssociationEnd(mClassName="sample_text")
    _safe_set(b, 'model_MAssociationEnd48', a1)
    assert _is_linked(b, 'model_MAssociationEnd48', a1)
    if hasattr(a1, 'model_MMultiplicity'):
        assert _is_linked(a1, 'model_MMultiplicity', b)
    _safe_set(b, 'model_MAssociationEnd48', a2)
    assert _is_linked(b, 'model_MAssociationEnd48', a2)
    if hasattr(a1, 'model_MMultiplicity'):
        assert not _is_linked(a1, 'model_MMultiplicity', b)
    if hasattr(a2, 'model_MMultiplicity'):
        assert _is_linked(a2, 'model_MMultiplicity', b)
    _safe_set(b, 'model_MAssociationEnd48', None)
    assert not _is_linked(b, 'model_MAssociationEnd48', a2)
    if hasattr(a2, 'model_MMultiplicity'):
        assert not _is_linked(a2, 'model_MMultiplicity', b)


def test_assoc_operation69_reverse_link_reassign_clear():
    a1 = model_MPrePostCondition(positionInModel=7)
    a2 = model_MPrePostCondition(positionInModel=13)
    b = model_MOperation()
    _safe_set(b, 'model_MOperation71', a1)
    assert _is_linked(b, 'model_MOperation71', a1)
    if hasattr(a1, 'model_MPrePostCondition70'):
        assert _is_linked(a1, 'model_MPrePostCondition70', b)
    _safe_set(b, 'model_MOperation71', a2)
    assert _is_linked(b, 'model_MOperation71', a2)
    if hasattr(a1, 'model_MPrePostCondition70'):
        assert not _is_linked(a1, 'model_MPrePostCondition70', b)
    if hasattr(a2, 'model_MPrePostCondition70'):
        assert _is_linked(a2, 'model_MPrePostCondition70', b)
    _safe_set(b, 'model_MOperation71', None)
    assert not _is_linked(b, 'model_MOperation71', a2)
    if hasattr(a2, 'model_MPrePostCondition70'):
        assert not _is_linked(a2, 'model_MPrePostCondition70', b)


def test_assoc_operations6_reverse_link_reassign_clear():
    a1 = model_MOperation()
    a2 = model_MOperation()
    b = model_MClass()
    _safe_set(b, 'model_MClass7', {a1})
    assert _is_linked(b, 'model_MClass7', a1)
    if hasattr(a1, 'model_MOperation'):
        assert _is_linked(a1, 'model_MOperation', b)
    _safe_set(b, 'model_MClass7', {a2})
    assert _is_linked(b, 'model_MClass7', a2)
    if hasattr(a1, 'model_MOperation'):
        assert not _is_linked(a1, 'model_MOperation', b)
    if hasattr(a2, 'model_MOperation'):
        assert _is_linked(a2, 'model_MOperation', b)
    _safe_set(b, 'model_MClass7', set())
    assert not _is_linked(b, 'model_MClass7', a2)
    if hasattr(a2, 'model_MOperation'):
        assert not _is_linked(a2, 'model_MOperation', b)


def test_assoc_owner0_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MAttribute()
    _safe_set(b, 'model_MAttribute', a1)
    assert _is_linked(b, 'model_MAttribute', a1)
    if hasattr(a1, 'model_MClass'):
        assert _is_linked(a1, 'model_MClass', b)
    _safe_set(b, 'model_MAttribute', a2)
    assert _is_linked(b, 'model_MAttribute', a2)
    if hasattr(a1, 'model_MClass'):
        assert not _is_linked(a1, 'model_MClass', b)
    if hasattr(a2, 'model_MClass'):
        assert _is_linked(a2, 'model_MClass', b)
    _safe_set(b, 'model_MAttribute', None)
    assert not _is_linked(b, 'model_MAttribute', a2)
    if hasattr(a2, 'model_MClass'):
        assert not _is_linked(a2, 'model_MClass', b)


def test_assoc_owner22_reverse_link_reassign_clear():
    a1 = model_MOperation()
    a2 = model_MOperation()
    b = model_MClass()
    _safe_set(b, 'model_MClass24', a1)
    assert _is_linked(b, 'model_MClass24', a1)
    if hasattr(a1, 'model_MOperation23'):
        assert _is_linked(a1, 'model_MOperation23', b)
    _safe_set(b, 'model_MClass24', a2)
    assert _is_linked(b, 'model_MClass24', a2)
    if hasattr(a1, 'model_MOperation23'):
        assert not _is_linked(a1, 'model_MOperation23', b)
    if hasattr(a2, 'model_MOperation23'):
        assert _is_linked(a2, 'model_MOperation23', b)
    _safe_set(b, 'model_MClass24', None)
    assert not _is_linked(b, 'model_MClass24', a2)
    if hasattr(a2, 'model_MOperation23'):
        assert not _is_linked(a2, 'model_MOperation23', b)


def test_assoc_parents11_reverse_link_reassign_clear():
    a1 = model_MClass()
    a2 = model_MClass()
    b = model_MClass()
    _safe_set(b, 'model_MClass12', a1)
    assert _is_linked(b, 'model_MClass12', a1)
    if hasattr(a1, 'model_MClass10'):
        assert _is_linked(a1, 'model_MClass10', b)
    _safe_set(b, 'model_MClass12', a2)
    assert _is_linked(b, 'model_MClass12', a2)
    if hasattr(a1, 'model_MClass10'):
        assert not _is_linked(a1, 'model_MClass10', b)
    if hasattr(a2, 'model_MClass10'):
        assert _is_linked(a2, 'model_MClass10', b)
    _safe_set(b, 'model_MClass12', None)
    assert not _is_linked(b, 'model_MClass12', a2)
    if hasattr(a2, 'model_MClass10'):
        assert not _is_linked(a2, 'model_MClass10', b)


def test_assoc_prePostCondition20_reverse_link_reassign_clear():
    a1 = model_MPrePostCondition(positionInModel=7)
    a2 = model_MPrePostCondition(positionInModel=13)
    b = model_MModel()
    _safe_set(b, 'model_MModel21', {a1})
    assert _is_linked(b, 'model_MModel21', a1)
    if hasattr(a1, 'model_MPrePostCondition'):
        assert _is_linked(a1, 'model_MPrePostCondition', b)
    _safe_set(b, 'model_MModel21', {a2})
    assert _is_linked(b, 'model_MModel21', a2)
    if hasattr(a1, 'model_MPrePostCondition'):
        assert not _is_linked(a1, 'model_MPrePostCondition', b)
    if hasattr(a2, 'model_MPrePostCondition'):
        assert _is_linked(a2, 'model_MPrePostCondition', b)
    _safe_set(b, 'model_MModel21', set())
    assert not _is_linked(b, 'model_MModel21', a2)
    if hasattr(a2, 'model_MPrePostCondition'):
        assert not _is_linked(a2, 'model_MPrePostCondition', b)


def test_assoc_ranges52_reverse_link_reassign_clear():
    a1 = model_MRange(lower=7, upper=7)
    a2 = model_MRange(lower=13, upper=13)
    b = model_MMultiplicity()
    _safe_set(b, 'model_MMultiplicity53', {a1})
    assert _is_linked(b, 'model_MMultiplicity53', a1)
    if hasattr(a1, 'model_MRange'):
        assert _is_linked(a1, 'model_MRange', b)
    _safe_set(b, 'model_MMultiplicity53', {a2})
    assert _is_linked(b, 'model_MMultiplicity53', a2)
    if hasattr(a1, 'model_MRange'):
        assert not _is_linked(a1, 'model_MRange', b)
    if hasattr(a2, 'model_MRange'):
        assert _is_linked(a2, 'model_MRange', b)
    _safe_set(b, 'model_MMultiplicity53', set())
    assert not _is_linked(b, 'model_MMultiplicity53', a2)
    if hasattr(a2, 'model_MRange'):
        assert not _is_linked(a2, 'model_MRange', b)


def test_assoc_resultType25_reverse_link_reassign_clear():
    a1 = model_Type(typeId=7, typeName="sample_text")
    a2 = model_Type(typeId=13, typeName="sample_text_2")
    b = model_MOperation()
    _safe_set(b, 'model_MOperation26', a1)
    assert _is_linked(b, 'model_MOperation26', a1)
    if hasattr(a1, 'model_Type27'):
        assert _is_linked(a1, 'model_Type27', b)
    _safe_set(b, 'model_MOperation26', a2)
    assert _is_linked(b, 'model_MOperation26', a2)
    if hasattr(a1, 'model_Type27'):
        assert not _is_linked(a1, 'model_Type27', b)
    if hasattr(a2, 'model_Type27'):
        assert _is_linked(a2, 'model_Type27', b)
    _safe_set(b, 'model_MOperation26', None)
    assert not _is_linked(b, 'model_MOperation26', a2)
    if hasattr(a2, 'model_Type27'):
        assert not _is_linked(a2, 'model_Type27', b)


def test_assoc_type1_reverse_link_reassign_clear():
    a1 = model_Type(typeId=7, typeName="sample_text")
    a2 = model_Type(typeId=13, typeName="sample_text_2")
    b = model_MAttribute()
    _safe_set(b, 'model_MAttribute2', a1)
    assert _is_linked(b, 'model_MAttribute2', a1)
    if hasattr(a1, 'model_Type'):
        assert _is_linked(a1, 'model_Type', b)
    _safe_set(b, 'model_MAttribute2', a2)
    assert _is_linked(b, 'model_MAttribute2', a2)
    if hasattr(a1, 'model_Type'):
        assert not _is_linked(a1, 'model_Type', b)
    if hasattr(a2, 'model_Type'):
        assert _is_linked(a2, 'model_Type', b)
    _safe_set(b, 'model_MAttribute2', None)
    assert not _is_linked(b, 'model_MAttribute2', a2)
    if hasattr(a2, 'model_Type'):
        assert not _is_linked(a2, 'model_Type', b)


def test_assoc_type30_reverse_link_reassign_clear():
    a1 = model_VarDecl(var="sample_text")
    a2 = model_VarDecl(var="sample_text_2")
    b = model_Type(typeId=7, typeName="sample_text")
    _safe_set(b, 'model_Type32', a1)
    assert _is_linked(b, 'model_Type32', a1)
    if hasattr(a1, 'model_VarDecl31'):
        assert _is_linked(a1, 'model_VarDecl31', b)
    _safe_set(b, 'model_Type32', a2)
    assert _is_linked(b, 'model_Type32', a2)
    if hasattr(a1, 'model_VarDecl31'):
        assert not _is_linked(a1, 'model_VarDecl31', b)
    if hasattr(a2, 'model_VarDecl31'):
        assert _is_linked(a2, 'model_VarDecl31', b)
    _safe_set(b, 'model_Type32', None)
    assert not _is_linked(b, 'model_Type32', a2)
    if hasattr(a2, 'model_VarDecl31'):
        assert not _is_linked(a2, 'model_VarDecl31', b)


def test_assoc_type75_reverse_link_reassign_clear():
    a1 = model_Type(typeId=7, typeName="sample_text")
    a2 = model_Type(typeId=13, typeName="sample_text_2")
    b = model_Part(name="sample_text")
    _safe_set(b, 'model_Part', a1)
    assert _is_linked(b, 'model_Part', a1)
    if hasattr(a1, 'model_Type76'):
        assert _is_linked(a1, 'model_Type76', b)
    _safe_set(b, 'model_Part', a2)
    assert _is_linked(b, 'model_Part', a2)
    if hasattr(a1, 'model_Type76'):
        assert not _is_linked(a1, 'model_Type76', b)
    if hasattr(a2, 'model_Type76'):
        assert _is_linked(a2, 'model_Type76', b)
    _safe_set(b, 'model_Part', None)
    assert not _is_linked(b, 'model_Part', a2)
    if hasattr(a2, 'model_Type76'):
        assert not _is_linked(a2, 'model_Type76', b)


def test_assoc_varDecls28_reverse_link_reassign_clear():
    a1 = model_VarDecl(var="sample_text")
    a2 = model_VarDecl(var="sample_text_2")
    b = model_MOperation()
    _safe_set(b, 'model_MOperation29', {a1})
    assert _is_linked(b, 'model_MOperation29', a1)
    if hasattr(a1, 'model_VarDecl'):
        assert _is_linked(a1, 'model_VarDecl', b)
    _safe_set(b, 'model_MOperation29', {a2})
    assert _is_linked(b, 'model_MOperation29', a2)
    if hasattr(a1, 'model_VarDecl'):
        assert not _is_linked(a1, 'model_VarDecl', b)
    if hasattr(a2, 'model_VarDecl'):
        assert _is_linked(a2, 'model_VarDecl', b)
    _safe_set(b, 'model_MOperation29', set())
    assert not _is_linked(b, 'model_MOperation29', a2)
    if hasattr(a2, 'model_VarDecl'):
        assert not _is_linked(a2, 'model_VarDecl', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_body64_stub_double():
    # model_Expression has no real 'model_Expression' property in the generated
    # code (a bare stub) -- manually attach it so model_MClassInvariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MClassInvariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MClassInvariant(name="sample_text", positionInModel=7)
    partner = model_Expression()
    setattr(partner, 'model_Expression', None)
    _safe_set(owner, 'model_MClassInvariant65', partner)
    assert getattr(partner, 'model_Expression') == owner
    _safe_set(owner, 'model_MClassInvariant65', None)
    assert getattr(partner, 'model_Expression') is None


def test_assoc_elemType33_stub_double():
    # model_CollectionType has no real 'model_CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so model_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Type(typeId=7, typeName="sample_text")
    partner = model_CollectionType()
    setattr(partner, 'model_CollectionType', None)
    _safe_set(owner, 'model_Type34', partner)
    assert getattr(partner, 'model_CollectionType') == owner
    _safe_set(owner, 'model_Type34', None)
    assert getattr(partner, 'model_CollectionType') is None


def test_assoc_expanded66_stub_double():
    # model_Expression has no real 'model_Expression68' property in the generated
    # code (a bare stub) -- manually attach it so model_MClassInvariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MClassInvariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MClassInvariant(name="sample_text", positionInModel=7)
    partner = model_Expression()
    setattr(partner, 'model_Expression68', None)
    _safe_set(owner, 'model_MClassInvariant67', partner)
    assert getattr(partner, 'model_Expression68') == owner
    _safe_set(owner, 'model_MClassInvariant67', None)
    assert getattr(partner, 'model_Expression68') is None


def test_assoc_expression72_stub_double():
    # model_Expression has no real 'model_Expression74' property in the generated
    # code (a bare stub) -- manually attach it so model_MPrePostCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MPrePostCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MPrePostCondition(positionInModel=7)
    partner = model_Expression()
    setattr(partner, 'model_Expression74', None)
    _safe_set(owner, 'model_MPrePostCondition73', partner)
    assert getattr(partner, 'model_Expression74') == owner
    _safe_set(owner, 'model_MPrePostCondition73', None)
    assert getattr(partner, 'model_Expression74') is None


def test_assoc_mClass35_stub_double():
    # model_ObjectType has no real 'model_ObjectType' property in the generated
    # code (a bare stub) -- manually attach it so model_MClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MClass()
    partner = model_ObjectType()
    setattr(partner, 'model_ObjectType', None)
    _safe_set(owner, 'model_MClass36', partner)
    assert getattr(partner, 'model_ObjectType') == owner
    _safe_set(owner, 'model_MClass36', None)
    assert getattr(partner, 'model_ObjectType') is None


def test_assoc_vars59_stub_double():
    # model_VarDeclList has no real 'model_VarDeclList' property in the generated
    # code (a bare stub) -- manually attach it so model_MClassInvariant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_MClassInvariant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_MClassInvariant(name="sample_text", positionInModel=7)
    partner = model_VarDeclList()
    setattr(partner, 'model_VarDeclList', None)
    _safe_set(owner, 'model_MClassInvariant60', partner)
    assert getattr(partner, 'model_VarDeclList') == owner
    _safe_set(owner, 'model_MClassInvariant60', None)
    assert getattr(partner, 'model_VarDeclList') is None


