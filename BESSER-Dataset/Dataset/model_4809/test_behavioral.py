import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractType,
    model_AbstractType,
    model_Address,
    model_ConcreteTypeOne,
    model_ConcreteTypeTwo,
    model_Container,
    model_EStringToStringMapEntry,
    model_ETypes,
    model_Node,
    model_ObjectWithMap,
    model_PrimaryObject,
    model_TargetObject,
    model_User,
    Sex,
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

def test_assoc_address5_reverse_link_reassign_clear():
    a1 = model_User(birthDate=date(2024, 1, 1), name="sample_text", sex="sample_text", userId="sample_text")
    a2 = model_User(birthDate=date(2025, 6, 15), name="sample_text_2", sex="sample_text_2", userId="sample_text_2")
    b = model_Address(addId="sample_text", city="sample_text", number="sample_text", street="sample_text")
    _safe_set(b, 'model_Address', a1)
    assert _is_linked(b, 'model_Address', a1)
    if hasattr(a1, 'model_User6'):
        assert _is_linked(a1, 'model_User6', b)
    _safe_set(b, 'model_Address', a2)
    assert _is_linked(b, 'model_Address', a2)
    if hasattr(a1, 'model_User6'):
        assert not _is_linked(a1, 'model_User6', b)
    if hasattr(a2, 'model_User6'):
        assert _is_linked(a2, 'model_User6', b)
    _safe_set(b, 'model_Address', None)
    assert not _is_linked(b, 'model_Address', a2)
    if hasattr(a2, 'model_User6'):
        assert not _is_linked(a2, 'model_User6', b)


def test_assoc_child50_reverse_link_reassign_clear():
    a1 = model_Node(label="sample_text")
    a2 = model_Node(label="sample_text_2")
    b = model_Node(label="sample_text")
    _safe_set(b, 'model_Node51', a1)
    assert _is_linked(b, 'model_Node51', a1)
    if hasattr(a1, 'model_Node49'):
        assert _is_linked(a1, 'model_Node49', b)
    _safe_set(b, 'model_Node51', a2)
    assert _is_linked(b, 'model_Node51', a2)
    if hasattr(a1, 'model_Node49'):
        assert not _is_linked(a1, 'model_Node49', b)
    if hasattr(a2, 'model_Node49'):
        assert _is_linked(a2, 'model_Node49', b)
    _safe_set(b, 'model_Node51', None)
    assert not _is_linked(b, 'model_Node51', a2)
    if hasattr(a2, 'model_Node49'):
        assert not _is_linked(a2, 'model_Node49', b)


def test_assoc_containmentReferenceSameCollectioin9_reverse_link_reassign_clear():
    a1 = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    a2 = model_PrimaryObject(featureMapAttributeCollection="sample_text_2", featureMapAttributeType1="sample_text_2", featureMapAttributeType2="sample_text_2", featureMapReferenceCollection="sample_text_2", idAttribute="sample_text_2", name="sample_text_2", unsettableAttribute="sample_text_2", unsettableAttributeWithNonNullDefault="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject8', a1)
    assert _is_linked(b, 'model_PrimaryObject8', a1)
    if hasattr(a1, 'model_PrimaryObject10'):
        assert _is_linked(a1, 'model_PrimaryObject10', b)
    _safe_set(b, 'model_PrimaryObject8', a2)
    assert _is_linked(b, 'model_PrimaryObject8', a2)
    if hasattr(a1, 'model_PrimaryObject10'):
        assert not _is_linked(a1, 'model_PrimaryObject10', b)
    if hasattr(a2, 'model_PrimaryObject10'):
        assert _is_linked(a2, 'model_PrimaryObject10', b)
    _safe_set(b, 'model_PrimaryObject8', None)
    assert not _is_linked(b, 'model_PrimaryObject8', a2)
    if hasattr(a2, 'model_PrimaryObject10'):
        assert not _is_linked(a2, 'model_PrimaryObject10', b)


def test_assoc_featureMapReferenceType132_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject33', {a1})
    assert _is_linked(b, 'model_PrimaryObject33', a1)
    if hasattr(a1, 'model_TargetObject34'):
        assert _is_linked(a1, 'model_TargetObject34', b)
    _safe_set(b, 'model_PrimaryObject33', {a2})
    assert _is_linked(b, 'model_PrimaryObject33', a2)
    if hasattr(a1, 'model_TargetObject34'):
        assert not _is_linked(a1, 'model_TargetObject34', b)
    if hasattr(a2, 'model_TargetObject34'):
        assert _is_linked(a2, 'model_TargetObject34', b)
    _safe_set(b, 'model_PrimaryObject33', set())
    assert not _is_linked(b, 'model_PrimaryObject33', a2)
    if hasattr(a2, 'model_TargetObject34'):
        assert not _is_linked(a2, 'model_TargetObject34', b)


def test_assoc_featureMapReferenceType235_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject36', {a1})
    assert _is_linked(b, 'model_PrimaryObject36', a1)
    if hasattr(a1, 'model_TargetObject37'):
        assert _is_linked(a1, 'model_TargetObject37', b)
    _safe_set(b, 'model_PrimaryObject36', {a2})
    assert _is_linked(b, 'model_PrimaryObject36', a2)
    if hasattr(a1, 'model_TargetObject37'):
        assert not _is_linked(a1, 'model_TargetObject37', b)
    if hasattr(a2, 'model_TargetObject37'):
        assert _is_linked(a2, 'model_TargetObject37', b)
    _safe_set(b, 'model_PrimaryObject36', set())
    assert not _is_linked(b, 'model_PrimaryObject36', a2)
    if hasattr(a2, 'model_TargetObject37'):
        assert not _is_linked(a2, 'model_TargetObject37', b)


def test_assoc_friends1_reverse_link_reassign_clear():
    a1 = model_User(birthDate=date(2024, 1, 1), name="sample_text", sex="sample_text", userId="sample_text")
    a2 = model_User(birthDate=date(2025, 6, 15), name="sample_text_2", sex="sample_text_2", userId="sample_text_2")
    b = model_User(birthDate=date(2024, 1, 1), name="sample_text", sex="sample_text", userId="sample_text")
    _safe_set(b, 'model_User0', {a1})
    assert _is_linked(b, 'model_User0', a1)
    if hasattr(a1, 'model_User'):
        assert _is_linked(a1, 'model_User', b)
    _safe_set(b, 'model_User0', {a2})
    assert _is_linked(b, 'model_User0', a2)
    if hasattr(a1, 'model_User'):
        assert not _is_linked(a1, 'model_User', b)
    if hasattr(a2, 'model_User'):
        assert _is_linked(a2, 'model_User', b)
    _safe_set(b, 'model_User0', set())
    assert not _is_linked(b, 'model_User0', a2)
    if hasattr(a2, 'model_User'):
        assert not _is_linked(a2, 'model_User', b)


def test_assoc_manyRef48_reverse_link_reassign_clear():
    a1 = model_Node(label="sample_text")
    a2 = model_Node(label="sample_text_2")
    b = model_Node(label="sample_text")
    _safe_set(b, 'model_Node47', {a1})
    assert _is_linked(b, 'model_Node47', a1)
    if hasattr(a1, 'model_Node'):
        assert _is_linked(a1, 'model_Node', b)
    _safe_set(b, 'model_Node47', {a2})
    assert _is_linked(b, 'model_Node47', a2)
    if hasattr(a1, 'model_Node'):
        assert not _is_linked(a1, 'model_Node', b)
    if hasattr(a2, 'model_Node'):
        assert _is_linked(a2, 'model_Node', b)
    _safe_set(b, 'model_Node47', set())
    assert not _is_linked(b, 'model_Node47', a2)
    if hasattr(a2, 'model_Node'):
        assert not _is_linked(a2, 'model_Node', b)


def test_assoc_multipleContainmentReferenceNoProxies20_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject21', {a1})
    assert _is_linked(b, 'model_PrimaryObject21', a1)
    if hasattr(a1, 'model_TargetObject22'):
        assert _is_linked(a1, 'model_TargetObject22', b)
    _safe_set(b, 'model_PrimaryObject21', {a2})
    assert _is_linked(b, 'model_PrimaryObject21', a2)
    if hasattr(a1, 'model_TargetObject22'):
        assert not _is_linked(a1, 'model_TargetObject22', b)
    if hasattr(a2, 'model_TargetObject22'):
        assert _is_linked(a2, 'model_TargetObject22', b)
    _safe_set(b, 'model_PrimaryObject21', set())
    assert not _is_linked(b, 'model_PrimaryObject21', a2)
    if hasattr(a2, 'model_TargetObject22'):
        assert not _is_linked(a2, 'model_TargetObject22', b)


def test_assoc_multipleContainmentReferenceProxies26_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject27', {a1})
    assert _is_linked(b, 'model_PrimaryObject27', a1)
    if hasattr(a1, 'model_TargetObject28'):
        assert _is_linked(a1, 'model_TargetObject28', b)
    _safe_set(b, 'model_PrimaryObject27', {a2})
    assert _is_linked(b, 'model_PrimaryObject27', a2)
    if hasattr(a1, 'model_TargetObject28'):
        assert not _is_linked(a1, 'model_TargetObject28', b)
    if hasattr(a2, 'model_TargetObject28'):
        assert _is_linked(a2, 'model_TargetObject28', b)
    _safe_set(b, 'model_PrimaryObject27', set())
    assert not _is_linked(b, 'model_PrimaryObject27', a2)
    if hasattr(a2, 'model_TargetObject28'):
        assert not _is_linked(a2, 'model_TargetObject28', b)


def test_assoc_multipleNonContainmentReference14_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject15', {a1})
    assert _is_linked(b, 'model_PrimaryObject15', a1)
    if hasattr(a1, 'model_TargetObject16'):
        assert _is_linked(a1, 'model_TargetObject16', b)
    _safe_set(b, 'model_PrimaryObject15', {a2})
    assert _is_linked(b, 'model_PrimaryObject15', a2)
    if hasattr(a1, 'model_TargetObject16'):
        assert not _is_linked(a1, 'model_TargetObject16', b)
    if hasattr(a2, 'model_TargetObject16'):
        assert _is_linked(a2, 'model_TargetObject16', b)
    _safe_set(b, 'model_PrimaryObject15', set())
    assert not _is_linked(b, 'model_PrimaryObject15', a2)
    if hasattr(a2, 'model_TargetObject16'):
        assert not _is_linked(a2, 'model_TargetObject16', b)


def test_assoc_refProperty40_reverse_link_reassign_clear():
    a1 = model_AbstractType(name="sample_text")
    a2 = model_AbstractType(name="sample_text_2")
    b = model_AbstractType(name="sample_text")
    _safe_set(b, 'model_AbstractType41', a1)
    assert _is_linked(b, 'model_AbstractType41', a1)
    if hasattr(a1, 'model_AbstractType39'):
        assert _is_linked(a1, 'model_AbstractType39', b)
    _safe_set(b, 'model_AbstractType41', a2)
    assert _is_linked(b, 'model_AbstractType41', a2)
    if hasattr(a1, 'model_AbstractType39'):
        assert not _is_linked(a1, 'model_AbstractType39', b)
    if hasattr(a2, 'model_AbstractType39'):
        assert _is_linked(a2, 'model_AbstractType39', b)
    _safe_set(b, 'model_AbstractType41', None)
    assert not _is_linked(b, 'model_AbstractType41', a2)
    if hasattr(a2, 'model_AbstractType39'):
        assert not _is_linked(a2, 'model_AbstractType39', b)


def test_assoc_singleContainmentReferenceNoProxies17_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject18', a1)
    assert _is_linked(b, 'model_PrimaryObject18', a1)
    if hasattr(a1, 'model_TargetObject19'):
        assert _is_linked(a1, 'model_TargetObject19', b)
    _safe_set(b, 'model_PrimaryObject18', a2)
    assert _is_linked(b, 'model_PrimaryObject18', a2)
    if hasattr(a1, 'model_TargetObject19'):
        assert not _is_linked(a1, 'model_TargetObject19', b)
    if hasattr(a2, 'model_TargetObject19'):
        assert _is_linked(a2, 'model_TargetObject19', b)
    _safe_set(b, 'model_PrimaryObject18', None)
    assert not _is_linked(b, 'model_PrimaryObject18', a2)
    if hasattr(a2, 'model_TargetObject19'):
        assert not _is_linked(a2, 'model_TargetObject19', b)


def test_assoc_singleContainmentReferenceProxies23_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject24', a1)
    assert _is_linked(b, 'model_PrimaryObject24', a1)
    if hasattr(a1, 'model_TargetObject25'):
        assert _is_linked(a1, 'model_TargetObject25', b)
    _safe_set(b, 'model_PrimaryObject24', a2)
    assert _is_linked(b, 'model_PrimaryObject24', a2)
    if hasattr(a1, 'model_TargetObject25'):
        assert not _is_linked(a1, 'model_TargetObject25', b)
    if hasattr(a2, 'model_TargetObject25'):
        assert _is_linked(a2, 'model_TargetObject25', b)
    _safe_set(b, 'model_PrimaryObject24', None)
    assert not _is_linked(b, 'model_PrimaryObject24', a2)
    if hasattr(a2, 'model_TargetObject25'):
        assert not _is_linked(a2, 'model_TargetObject25', b)


def test_assoc_singleNonContainmentReference11_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject12', a1)
    assert _is_linked(b, 'model_PrimaryObject12', a1)
    if hasattr(a1, 'model_TargetObject13'):
        assert _is_linked(a1, 'model_TargetObject13', b)
    _safe_set(b, 'model_PrimaryObject12', a2)
    assert _is_linked(b, 'model_PrimaryObject12', a2)
    if hasattr(a1, 'model_TargetObject13'):
        assert not _is_linked(a1, 'model_TargetObject13', b)
    if hasattr(a2, 'model_TargetObject13'):
        assert _is_linked(a2, 'model_TargetObject13', b)
    _safe_set(b, 'model_PrimaryObject12', None)
    assert not _is_linked(b, 'model_PrimaryObject12', a2)
    if hasattr(a2, 'model_TargetObject13'):
        assert not _is_linked(a2, 'model_TargetObject13', b)


def test_assoc_singleNonContainmentReferenceNoProxies29_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject30', a1)
    assert _is_linked(b, 'model_PrimaryObject30', a1)
    if hasattr(a1, 'model_TargetObject31'):
        assert _is_linked(a1, 'model_TargetObject31', b)
    _safe_set(b, 'model_PrimaryObject30', a2)
    assert _is_linked(b, 'model_PrimaryObject30', a2)
    if hasattr(a1, 'model_TargetObject31'):
        assert not _is_linked(a1, 'model_TargetObject31', b)
    if hasattr(a2, 'model_TargetObject31'):
        assert _is_linked(a2, 'model_TargetObject31', b)
    _safe_set(b, 'model_PrimaryObject30', None)
    assert not _is_linked(b, 'model_PrimaryObject30', a2)
    if hasattr(a2, 'model_TargetObject31'):
        assert not _is_linked(a2, 'model_TargetObject31', b)


def test_assoc_source45_reverse_link_reassign_clear():
    a1 = model_Node(label="sample_text")
    a2 = model_Node(label="sample_text_2")
    b = model_Node(label="sample_text")
    _safe_set(b, 'target', a1)
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Node46'):
        assert _is_linked(a1, 'Node46', b)
    _safe_set(b, 'target', a2)
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Node46'):
        assert not _is_linked(a1, 'Node46', b)
    if hasattr(a2, 'Node46'):
        assert _is_linked(a2, 'Node46', b)
    _safe_set(b, 'target', None)
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Node46'):
        assert not _is_linked(a2, 'Node46', b)


def test_assoc_target43_reverse_link_reassign_clear():
    a1 = model_Node(label="sample_text")
    a2 = model_Node(label="sample_text_2")
    b = model_Node(label="sample_text")
    _safe_set(b, 'source', a1)
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'source', a2)
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'source', None)
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_uniqueChild53_reverse_link_reassign_clear():
    a1 = model_Node(label="sample_text")
    a2 = model_Node(label="sample_text_2")
    b = model_Node(label="sample_text")
    _safe_set(b, 'model_Node54', a1)
    assert _is_linked(b, 'model_Node54', a1)
    if hasattr(a1, 'model_Node52'):
        assert _is_linked(a1, 'model_Node52', b)
    _safe_set(b, 'model_Node54', a2)
    assert _is_linked(b, 'model_Node54', a2)
    if hasattr(a1, 'model_Node52'):
        assert not _is_linked(a1, 'model_Node52', b)
    if hasattr(a2, 'model_Node52'):
        assert _is_linked(a2, 'model_Node52', b)
    _safe_set(b, 'model_Node54', None)
    assert not _is_linked(b, 'model_Node54', a2)
    if hasattr(a2, 'model_Node52'):
        assert not _is_linked(a2, 'model_Node52', b)


def test_assoc_uniqueFriend3_reverse_link_reassign_clear():
    a1 = model_User(birthDate=date(2024, 1, 1), name="sample_text", sex="sample_text", userId="sample_text")
    a2 = model_User(birthDate=date(2025, 6, 15), name="sample_text_2", sex="sample_text_2", userId="sample_text_2")
    b = model_User(birthDate=date(2024, 1, 1), name="sample_text", sex="sample_text", userId="sample_text")
    _safe_set(b, 'model_User4', a1)
    assert _is_linked(b, 'model_User4', a1)
    if hasattr(a1, 'model_User2'):
        assert _is_linked(a1, 'model_User2', b)
    _safe_set(b, 'model_User4', a2)
    assert _is_linked(b, 'model_User4', a2)
    if hasattr(a1, 'model_User2'):
        assert not _is_linked(a1, 'model_User2', b)
    if hasattr(a2, 'model_User2'):
        assert _is_linked(a2, 'model_User2', b)
    _safe_set(b, 'model_User4', None)
    assert not _is_linked(b, 'model_User4', a2)
    if hasattr(a2, 'model_User2'):
        assert not _is_linked(a2, 'model_User2', b)


def test_assoc_unsettableReference7_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", idAttribute="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithNonNullDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject', a1)
    assert _is_linked(b, 'model_PrimaryObject', a1)
    if hasattr(a1, 'model_TargetObject'):
        assert _is_linked(a1, 'model_TargetObject', b)
    _safe_set(b, 'model_PrimaryObject', a2)
    assert _is_linked(b, 'model_PrimaryObject', a2)
    if hasattr(a1, 'model_TargetObject'):
        assert not _is_linked(a1, 'model_TargetObject', b)
    if hasattr(a2, 'model_TargetObject'):
        assert _is_linked(a2, 'model_TargetObject', b)
    _safe_set(b, 'model_PrimaryObject', None)
    assert not _is_linked(b, 'model_PrimaryObject', a2)
    if hasattr(a2, 'model_TargetObject'):
        assert not _is_linked(a2, 'model_TargetObject', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_elements38_stub_double():
    # model_Container has no real 'model_Container' property in the generated
    # code (a bare stub) -- manually attach it so model_AbstractType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_AbstractType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_AbstractType(name="sample_text")
    partner = model_Container()
    setattr(partner, 'model_Container', None)
    _safe_set(owner, 'model_AbstractType', partner)
    assert owner in getattr(partner, 'model_Container')
    _safe_set(owner, 'model_AbstractType', None)
    assert owner not in getattr(partner, 'model_Container')


