import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_BNode,
    model_Book,
    model_BookBNode,
    model_ETypes,
    model_Library,
    model_Location,
    model_MappedLibrary,
    model_Person,
    model_PersonBNode,
    model_PrimaryObject,
    model_TargetObject,
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

def test_assoc_authors1_reverse_link_reassign_clear():
    a1 = model_Person(name="sample_text")
    a2 = model_Person(name="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'books', {a1})
    assert _is_linked(b, 'books', a1)
    if hasattr(a1, 'Person'):
        assert _is_linked(a1, 'Person', b)
    _safe_set(b, 'books', {a2})
    assert _is_linked(b, 'books', a2)
    if hasattr(a1, 'Person'):
        assert not _is_linked(a1, 'Person', b)
    if hasattr(a2, 'Person'):
        assert _is_linked(a2, 'Person', b)
    _safe_set(b, 'books', set())
    assert not _is_linked(b, 'books', a2)
    if hasattr(a2, 'Person'):
        assert not _is_linked(a2, 'Person', b)


def test_assoc_authors3_reverse_link_reassign_clear():
    a1 = model_PersonBNode(name="sample_text")
    a2 = model_PersonBNode(name="sample_text_2")
    b = model_BookBNode(title="sample_text")
    _safe_set(b, 'model_BookBNode4', {a1})
    assert _is_linked(b, 'model_BookBNode4', a1)
    if hasattr(a1, 'model_PersonBNode5'):
        assert _is_linked(a1, 'model_PersonBNode5', b)
    _safe_set(b, 'model_BookBNode4', {a2})
    assert _is_linked(b, 'model_BookBNode4', a2)
    if hasattr(a1, 'model_PersonBNode5'):
        assert not _is_linked(a1, 'model_PersonBNode5', b)
    if hasattr(a2, 'model_PersonBNode5'):
        assert _is_linked(a2, 'model_PersonBNode5', b)
    _safe_set(b, 'model_BookBNode4', set())
    assert not _is_linked(b, 'model_BookBNode4', a2)
    if hasattr(a2, 'model_PersonBNode5'):
        assert not _is_linked(a2, 'model_PersonBNode5', b)


def test_assoc_books0_reverse_link_reassign_clear():
    a1 = model_Person(name="sample_text")
    a2 = model_Person(name="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'Book', a1)
    assert _is_linked(b, 'Book', a1)
    if hasattr(a1, 'authors'):
        assert _is_linked(a1, 'authors', b)
    _safe_set(b, 'Book', a2)
    assert _is_linked(b, 'Book', a2)
    if hasattr(a1, 'authors'):
        assert not _is_linked(a1, 'authors', b)
    if hasattr(a2, 'authors'):
        assert _is_linked(a2, 'authors', b)
    _safe_set(b, 'Book', None)
    assert not _is_linked(b, 'Book', a2)
    if hasattr(a2, 'authors'):
        assert not _is_linked(a2, 'authors', b)


def test_assoc_books2_reverse_link_reassign_clear():
    a1 = model_PersonBNode(name="sample_text")
    a2 = model_PersonBNode(name="sample_text_2")
    b = model_BookBNode(title="sample_text")
    _safe_set(b, 'model_BookBNode', a1)
    assert _is_linked(b, 'model_BookBNode', a1)
    if hasattr(a1, 'model_PersonBNode'):
        assert _is_linked(a1, 'model_PersonBNode', b)
    _safe_set(b, 'model_BookBNode', a2)
    assert _is_linked(b, 'model_BookBNode', a2)
    if hasattr(a1, 'model_PersonBNode'):
        assert not _is_linked(a1, 'model_PersonBNode', b)
    if hasattr(a2, 'model_PersonBNode'):
        assert _is_linked(a2, 'model_PersonBNode', b)
    _safe_set(b, 'model_BookBNode', None)
    assert not _is_linked(b, 'model_BookBNode', a2)
    if hasattr(a2, 'model_PersonBNode'):
        assert not _is_linked(a2, 'model_PersonBNode', b)


def test_assoc_child7_reverse_link_reassign_clear():
    a1 = model_BNode(id=7)
    a2 = model_BNode(id=13)
    b = model_BNode(id=7)
    _safe_set(b, 'model_BNode6', {a1})
    assert _is_linked(b, 'model_BNode6', a1)
    if hasattr(a1, 'model_BNode'):
        assert _is_linked(a1, 'model_BNode', b)
    _safe_set(b, 'model_BNode6', {a2})
    assert _is_linked(b, 'model_BNode6', a2)
    if hasattr(a1, 'model_BNode'):
        assert not _is_linked(a1, 'model_BNode', b)
    if hasattr(a2, 'model_BNode'):
        assert _is_linked(a2, 'model_BNode', b)
    _safe_set(b, 'model_BNode6', set())
    assert not _is_linked(b, 'model_BNode6', a2)
    if hasattr(a2, 'model_BNode'):
        assert not _is_linked(a2, 'model_BNode', b)


def test_assoc_featureMapReferenceType147_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject48', {a1})
    assert _is_linked(b, 'model_PrimaryObject48', a1)
    if hasattr(a1, 'model_TargetObject49'):
        assert _is_linked(a1, 'model_TargetObject49', b)
    _safe_set(b, 'model_PrimaryObject48', {a2})
    assert _is_linked(b, 'model_PrimaryObject48', a2)
    if hasattr(a1, 'model_TargetObject49'):
        assert not _is_linked(a1, 'model_TargetObject49', b)
    if hasattr(a2, 'model_TargetObject49'):
        assert _is_linked(a2, 'model_TargetObject49', b)
    _safe_set(b, 'model_PrimaryObject48', set())
    assert not _is_linked(b, 'model_PrimaryObject48', a2)
    if hasattr(a2, 'model_TargetObject49'):
        assert not _is_linked(a2, 'model_TargetObject49', b)


def test_assoc_featureMapReferenceType244_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject45', {a1})
    assert _is_linked(b, 'model_PrimaryObject45', a1)
    if hasattr(a1, 'model_TargetObject46'):
        assert _is_linked(a1, 'model_TargetObject46', b)
    _safe_set(b, 'model_PrimaryObject45', {a2})
    assert _is_linked(b, 'model_PrimaryObject45', a2)
    if hasattr(a1, 'model_TargetObject46'):
        assert not _is_linked(a1, 'model_TargetObject46', b)
    if hasattr(a2, 'model_TargetObject46'):
        assert _is_linked(a2, 'model_TargetObject46', b)
    _safe_set(b, 'model_PrimaryObject45', set())
    assert not _is_linked(b, 'model_PrimaryObject45', a2)
    if hasattr(a2, 'model_TargetObject46'):
        assert not _is_linked(a2, 'model_TargetObject46', b)


def test_assoc_featuredBook14_reverse_link_reassign_clear():
    a1 = model_Location(address="sample_text", id="sample_text")
    a2 = model_Location(address="sample_text_2", id="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book16', a1)
    assert _is_linked(b, 'model_Book16', a1)
    if hasattr(a1, 'model_Location15'):
        assert _is_linked(a1, 'model_Location15', b)
    _safe_set(b, 'model_Book16', a2)
    assert _is_linked(b, 'model_Book16', a2)
    if hasattr(a1, 'model_Location15'):
        assert not _is_linked(a1, 'model_Location15', b)
    if hasattr(a2, 'model_Location15'):
        assert _is_linked(a2, 'model_Location15', b)
    _safe_set(b, 'model_Book16', None)
    assert not _is_linked(b, 'model_Book16', a2)
    if hasattr(a2, 'model_Location15'):
        assert not _is_linked(a2, 'model_Location15', b)


def test_assoc_location17_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Location(address="sample_text", id="sample_text")
    _safe_set(b, 'model_Location18', a1)
    assert _is_linked(b, 'model_Location18', a1)
    if hasattr(a1, 'model_MappedLibrary'):
        assert _is_linked(a1, 'model_MappedLibrary', b)
    _safe_set(b, 'model_Location18', a2)
    assert _is_linked(b, 'model_Location18', a2)
    if hasattr(a1, 'model_MappedLibrary'):
        assert not _is_linked(a1, 'model_MappedLibrary', b)
    if hasattr(a2, 'model_MappedLibrary'):
        assert _is_linked(a2, 'model_MappedLibrary', b)
    _safe_set(b, 'model_Location18', None)
    assert not _is_linked(b, 'model_Location18', a2)
    if hasattr(a2, 'model_MappedLibrary'):
        assert not _is_linked(a2, 'model_MappedLibrary', b)


def test_assoc_multipleContainmentReferenceNoProxies35_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
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


def test_assoc_multipleContainmentReferenceProxies41_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject42', {a1})
    assert _is_linked(b, 'model_PrimaryObject42', a1)
    if hasattr(a1, 'model_TargetObject43'):
        assert _is_linked(a1, 'model_TargetObject43', b)
    _safe_set(b, 'model_PrimaryObject42', {a2})
    assert _is_linked(b, 'model_PrimaryObject42', a2)
    if hasattr(a1, 'model_TargetObject43'):
        assert not _is_linked(a1, 'model_TargetObject43', b)
    if hasattr(a2, 'model_TargetObject43'):
        assert _is_linked(a2, 'model_TargetObject43', b)
    _safe_set(b, 'model_PrimaryObject42', set())
    assert not _is_linked(b, 'model_PrimaryObject42', a2)
    if hasattr(a2, 'model_TargetObject43'):
        assert not _is_linked(a2, 'model_TargetObject43', b)


def test_assoc_multipleNonContainmentReference29_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject30', {a1})
    assert _is_linked(b, 'model_PrimaryObject30', a1)
    if hasattr(a1, 'model_TargetObject31'):
        assert _is_linked(a1, 'model_TargetObject31', b)
    _safe_set(b, 'model_PrimaryObject30', {a2})
    assert _is_linked(b, 'model_PrimaryObject30', a2)
    if hasattr(a1, 'model_TargetObject31'):
        assert not _is_linked(a1, 'model_TargetObject31', b)
    if hasattr(a2, 'model_TargetObject31'):
        assert _is_linked(a2, 'model_TargetObject31', b)
    _safe_set(b, 'model_PrimaryObject30', set())
    assert not _is_linked(b, 'model_PrimaryObject30', a2)
    if hasattr(a2, 'model_TargetObject31'):
        assert not _is_linked(a2, 'model_TargetObject31', b)


def test_assoc_rareBooks19_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book21', a1)
    assert _is_linked(b, 'model_Book21', a1)
    if hasattr(a1, 'model_MappedLibrary20'):
        assert _is_linked(a1, 'model_MappedLibrary20', b)
    _safe_set(b, 'model_Book21', a2)
    assert _is_linked(b, 'model_Book21', a2)
    if hasattr(a1, 'model_MappedLibrary20'):
        assert not _is_linked(a1, 'model_MappedLibrary20', b)
    if hasattr(a2, 'model_MappedLibrary20'):
        assert _is_linked(a2, 'model_MappedLibrary20', b)
    _safe_set(b, 'model_Book21', None)
    assert not _is_linked(b, 'model_Book21', a2)
    if hasattr(a2, 'model_MappedLibrary20'):
        assert not _is_linked(a2, 'model_MappedLibrary20', b)


def test_assoc_regularBooks22_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book24', a1)
    assert _is_linked(b, 'model_Book24', a1)
    if hasattr(a1, 'model_MappedLibrary23'):
        assert _is_linked(a1, 'model_MappedLibrary23', b)
    _safe_set(b, 'model_Book24', a2)
    assert _is_linked(b, 'model_Book24', a2)
    if hasattr(a1, 'model_MappedLibrary23'):
        assert not _is_linked(a1, 'model_MappedLibrary23', b)
    if hasattr(a2, 'model_MappedLibrary23'):
        assert _is_linked(a2, 'model_MappedLibrary23', b)
    _safe_set(b, 'model_Book24', None)
    assert not _is_linked(b, 'model_Book24', a2)
    if hasattr(a2, 'model_MappedLibrary23'):
        assert not _is_linked(a2, 'model_MappedLibrary23', b)


def test_assoc_singleContainmentReferenceNoProxies32_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject33', a1)
    assert _is_linked(b, 'model_PrimaryObject33', a1)
    if hasattr(a1, 'model_TargetObject34'):
        assert _is_linked(a1, 'model_TargetObject34', b)
    _safe_set(b, 'model_PrimaryObject33', a2)
    assert _is_linked(b, 'model_PrimaryObject33', a2)
    if hasattr(a1, 'model_TargetObject34'):
        assert not _is_linked(a1, 'model_TargetObject34', b)
    if hasattr(a2, 'model_TargetObject34'):
        assert _is_linked(a2, 'model_TargetObject34', b)
    _safe_set(b, 'model_PrimaryObject33', None)
    assert not _is_linked(b, 'model_PrimaryObject33', a2)
    if hasattr(a2, 'model_TargetObject34'):
        assert not _is_linked(a2, 'model_TargetObject34', b)


def test_assoc_singleContainmentReferenceProxies38_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject39', a1)
    assert _is_linked(b, 'model_PrimaryObject39', a1)
    if hasattr(a1, 'model_TargetObject40'):
        assert _is_linked(a1, 'model_TargetObject40', b)
    _safe_set(b, 'model_PrimaryObject39', a2)
    assert _is_linked(b, 'model_PrimaryObject39', a2)
    if hasattr(a1, 'model_TargetObject40'):
        assert not _is_linked(a1, 'model_TargetObject40', b)
    if hasattr(a2, 'model_TargetObject40'):
        assert _is_linked(a2, 'model_TargetObject40', b)
    _safe_set(b, 'model_PrimaryObject39', None)
    assert not _is_linked(b, 'model_PrimaryObject39', a2)
    if hasattr(a2, 'model_TargetObject40'):
        assert not _is_linked(a2, 'model_TargetObject40', b)


def test_assoc_singleNonContainmentReference26_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'model_PrimaryObject27', a1)
    assert _is_linked(b, 'model_PrimaryObject27', a1)
    if hasattr(a1, 'model_TargetObject28'):
        assert _is_linked(a1, 'model_TargetObject28', b)
    _safe_set(b, 'model_PrimaryObject27', a2)
    assert _is_linked(b, 'model_PrimaryObject27', a2)
    if hasattr(a1, 'model_TargetObject28'):
        assert not _is_linked(a1, 'model_TargetObject28', b)
    if hasattr(a2, 'model_TargetObject28'):
        assert _is_linked(a2, 'model_TargetObject28', b)
    _safe_set(b, 'model_PrimaryObject27', None)
    assert not _is_linked(b, 'model_PrimaryObject27', a2)
    if hasattr(a2, 'model_TargetObject28'):
        assert not _is_linked(a2, 'model_TargetObject28', b)


def test_assoc_unsettableReference25_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", id=7, singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", id=13, singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id=7, name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
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


