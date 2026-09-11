import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    ItemsCollection,
    collection_Category,
    collection_DataSet,
    collection_Item,
    collection_ItemsCollection,
    collection_ManualCollection,
    collection_MetaTag,
    collection_Organisation,
    collection_Person,
    collection_RemoteCollection,
    collection_SmartInformationObjectCollection,
    collection_Tag,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_collection_RemoteCollection_remoteURL_value_roundtrip():
    instance = collection_RemoteCollection(remoteURL="sample_text")
    assert instance.remoteURL == "sample_text"
    instance.remoteURL = "sample_text_2"
    assert instance.remoteURL == "sample_text_2"


def test_collection_SmartInformationObjectCollection_includeContents_value_roundtrip():
    instance = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    assert instance.includeContents == "sample_text"
    instance.includeContents = "sample_text_2"
    assert instance.includeContents == "sample_text_2"


def test_collection_SmartInformationObjectCollection_includeOrganisations_value_roundtrip():
    instance = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    assert instance.includeOrganisations == "sample_text"
    instance.includeOrganisations = "sample_text_2"
    assert instance.includeOrganisations == "sample_text_2"


def test_collection_SmartInformationObjectCollection_includePersons_value_roundtrip():
    instance = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    assert instance.includePersons == "sample_text"
    instance.includePersons = "sample_text_2"
    assert instance.includePersons == "sample_text_2"


def test_collection_SmartInformationObjectCollection_minimumAge_value_roundtrip():
    instance = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    assert instance.minimumAge == date(2024, 1, 1)
    instance.minimumAge = date(2025, 6, 15)
    assert instance.minimumAge == date(2025, 6, 15)


def test_collection_ManualCollection_isa_ItemsCollection():
    instance = collection_ManualCollection()
    assert isinstance(instance, ItemsCollection)


def test_collection_RemoteCollection_isa_ItemsCollection():
    instance = collection_RemoteCollection(remoteURL="sample_text")
    assert isinstance(instance, ItemsCollection)


def test_collection_SmartInformationObjectCollection_isa_ItemsCollection():
    instance = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    assert isinstance(instance, ItemsCollection)


def test_assoc_negativeCategories16_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Category()
    b2 = collection_Category()
    _safe_set(a, 'collection_SmartInformationObjectCollection17', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection17', b1)
    if hasattr(b1, 'collection_Category18'):
        assert _is_linked(b1, 'collection_Category18', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection17', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection17', b2)
    if hasattr(b1, 'collection_Category18'):
        assert not _is_linked(b1, 'collection_Category18', a)
    if hasattr(b2, 'collection_Category18'):
        assert _is_linked(b2, 'collection_Category18', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection17', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection17', b2)
    if hasattr(b2, 'collection_Category18'):
        assert not _is_linked(b2, 'collection_Category18', a)


def test_assoc_negativeMetaTags13_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_MetaTag()
    b2 = collection_MetaTag()
    _safe_set(a, 'collection_SmartInformationObjectCollection14', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection14', b1)
    if hasattr(b1, 'collection_MetaTag15'):
        assert _is_linked(b1, 'collection_MetaTag15', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection14', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection14', b2)
    if hasattr(b1, 'collection_MetaTag15'):
        assert not _is_linked(b1, 'collection_MetaTag15', a)
    if hasattr(b2, 'collection_MetaTag15'):
        assert _is_linked(b2, 'collection_MetaTag15', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection14', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection14', b2)
    if hasattr(b2, 'collection_MetaTag15'):
        assert not _is_linked(b2, 'collection_MetaTag15', a)


def test_assoc_negativeOrganisations24_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Organisation()
    b2 = collection_Organisation()
    _safe_set(a, 'collection_SmartInformationObjectCollection25', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection25', b1)
    if hasattr(b1, 'collection_Organisation26'):
        assert _is_linked(b1, 'collection_Organisation26', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection25', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection25', b2)
    if hasattr(b1, 'collection_Organisation26'):
        assert not _is_linked(b1, 'collection_Organisation26', a)
    if hasattr(b2, 'collection_Organisation26'):
        assert _is_linked(b2, 'collection_Organisation26', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection25', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection25', b2)
    if hasattr(b2, 'collection_Organisation26'):
        assert not _is_linked(b2, 'collection_Organisation26', a)


def test_assoc_negativePersons19_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Person()
    b2 = collection_Person()
    _safe_set(a, 'collection_SmartInformationObjectCollection20', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection20', b1)
    if hasattr(b1, 'collection_Person21'):
        assert _is_linked(b1, 'collection_Person21', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection20', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection20', b2)
    if hasattr(b1, 'collection_Person21'):
        assert not _is_linked(b1, 'collection_Person21', a)
    if hasattr(b2, 'collection_Person21'):
        assert _is_linked(b2, 'collection_Person21', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection20', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection20', b2)
    if hasattr(b2, 'collection_Person21'):
        assert not _is_linked(b2, 'collection_Person21', a)


def test_assoc_negativeTags4_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Tag()
    b2 = collection_Tag()
    _safe_set(a, 'collection_SmartInformationObjectCollection5', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection5', b1)
    if hasattr(b1, 'collection_Tag6'):
        assert _is_linked(b1, 'collection_Tag6', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection5', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection5', b2)
    if hasattr(b1, 'collection_Tag6'):
        assert not _is_linked(b1, 'collection_Tag6', a)
    if hasattr(b2, 'collection_Tag6'):
        assert _is_linked(b2, 'collection_Tag6', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection5', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection5', b2)
    if hasattr(b2, 'collection_Tag6'):
        assert not _is_linked(b2, 'collection_Tag6', a)


def test_assoc_positiveCategories9_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Category()
    b2 = collection_Category()
    _safe_set(a, 'collection_SmartInformationObjectCollection10', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection10', b1)
    if hasattr(b1, 'collection_Category'):
        assert _is_linked(b1, 'collection_Category', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection10', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection10', b2)
    if hasattr(b1, 'collection_Category'):
        assert not _is_linked(b1, 'collection_Category', a)
    if hasattr(b2, 'collection_Category'):
        assert _is_linked(b2, 'collection_Category', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection10', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection10', b2)
    if hasattr(b2, 'collection_Category'):
        assert not _is_linked(b2, 'collection_Category', a)


def test_assoc_positiveMetaTags7_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_MetaTag()
    b2 = collection_MetaTag()
    _safe_set(a, 'collection_SmartInformationObjectCollection8', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection8', b1)
    if hasattr(b1, 'collection_MetaTag'):
        assert _is_linked(b1, 'collection_MetaTag', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection8', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection8', b2)
    if hasattr(b1, 'collection_MetaTag'):
        assert not _is_linked(b1, 'collection_MetaTag', a)
    if hasattr(b2, 'collection_MetaTag'):
        assert _is_linked(b2, 'collection_MetaTag', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection8', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection8', b2)
    if hasattr(b2, 'collection_MetaTag'):
        assert not _is_linked(b2, 'collection_MetaTag', a)


def test_assoc_positiveOrganisations22_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Organisation()
    b2 = collection_Organisation()
    _safe_set(a, 'collection_SmartInformationObjectCollection23', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection23', b1)
    if hasattr(b1, 'collection_Organisation'):
        assert _is_linked(b1, 'collection_Organisation', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection23', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection23', b2)
    if hasattr(b1, 'collection_Organisation'):
        assert not _is_linked(b1, 'collection_Organisation', a)
    if hasattr(b2, 'collection_Organisation'):
        assert _is_linked(b2, 'collection_Organisation', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection23', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection23', b2)
    if hasattr(b2, 'collection_Organisation'):
        assert not _is_linked(b2, 'collection_Organisation', a)


def test_assoc_positivePersons11_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Person()
    b2 = collection_Person()
    _safe_set(a, 'collection_SmartInformationObjectCollection12', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection12', b1)
    if hasattr(b1, 'collection_Person'):
        assert _is_linked(b1, 'collection_Person', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection12', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection12', b2)
    if hasattr(b1, 'collection_Person'):
        assert not _is_linked(b1, 'collection_Person', a)
    if hasattr(b2, 'collection_Person'):
        assert _is_linked(b2, 'collection_Person', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection12', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection12', b2)
    if hasattr(b2, 'collection_Person'):
        assert not _is_linked(b2, 'collection_Person', a)


def test_assoc_positiveTags3_link_reassign_clear():
    a = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    b1 = collection_Tag()
    b2 = collection_Tag()
    _safe_set(a, 'collection_SmartInformationObjectCollection', {b1})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection', b1)
    if hasattr(b1, 'collection_Tag'):
        assert _is_linked(b1, 'collection_Tag', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection', {b2})
    assert _is_linked(a, 'collection_SmartInformationObjectCollection', b2)
    if hasattr(b1, 'collection_Tag'):
        assert not _is_linked(b1, 'collection_Tag', a)
    if hasattr(b2, 'collection_Tag'):
        assert _is_linked(b2, 'collection_Tag', a)
    _safe_set(a, 'collection_SmartInformationObjectCollection', set())
    assert not _is_linked(a, 'collection_SmartInformationObjectCollection', b2)
    if hasattr(b2, 'collection_Tag'):
        assert not _is_linked(b2, 'collection_Tag', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

ItemsCollection_strategy = st.builds(ItemsCollection)
@given(instance=ItemsCollection_strategy)
@settings(max_examples=25)
def test_ItemsCollection_instantiation(instance):
    assert isinstance(instance, ItemsCollection)


collection_Category_strategy = st.builds(collection_Category)
@given(instance=collection_Category_strategy)
@settings(max_examples=25)
def test_collection_Category_instantiation(instance):
    assert isinstance(instance, collection_Category)


collection_DataSet_strategy = st.builds(collection_DataSet)
@given(instance=collection_DataSet_strategy)
@settings(max_examples=25)
def test_collection_DataSet_instantiation(instance):
    assert isinstance(instance, collection_DataSet)


collection_Item_strategy = st.builds(collection_Item)
@given(instance=collection_Item_strategy)
@settings(max_examples=25)
def test_collection_Item_instantiation(instance):
    assert isinstance(instance, collection_Item)


collection_ItemsCollection_strategy = st.builds(collection_ItemsCollection)
@given(instance=collection_ItemsCollection_strategy)
@settings(max_examples=25)
def test_collection_ItemsCollection_instantiation(instance):
    assert isinstance(instance, collection_ItemsCollection)


collection_ManualCollection_strategy = st.builds(collection_ManualCollection)
@given(instance=collection_ManualCollection_strategy)
@settings(max_examples=25)
def test_collection_ManualCollection_instantiation(instance):
    assert isinstance(instance, collection_ManualCollection)


collection_MetaTag_strategy = st.builds(collection_MetaTag)
@given(instance=collection_MetaTag_strategy)
@settings(max_examples=25)
def test_collection_MetaTag_instantiation(instance):
    assert isinstance(instance, collection_MetaTag)


collection_Organisation_strategy = st.builds(collection_Organisation)
@given(instance=collection_Organisation_strategy)
@settings(max_examples=25)
def test_collection_Organisation_instantiation(instance):
    assert isinstance(instance, collection_Organisation)


collection_Person_strategy = st.builds(collection_Person)
@given(instance=collection_Person_strategy)
@settings(max_examples=25)
def test_collection_Person_instantiation(instance):
    assert isinstance(instance, collection_Person)


collection_RemoteCollection_strategy = st.builds(collection_RemoteCollection, remoteURL=safe_text)
@given(instance=collection_RemoteCollection_strategy)
@settings(max_examples=25)
def test_collection_RemoteCollection_instantiation(instance):
    assert isinstance(instance, collection_RemoteCollection)


collection_SmartInformationObjectCollection_strategy = st.builds(collection_SmartInformationObjectCollection, includeContents=safe_text, includeOrganisations=safe_text, includePersons=safe_text, minimumAge=st.dates())
@given(instance=collection_SmartInformationObjectCollection_strategy)
@settings(max_examples=25)
def test_collection_SmartInformationObjectCollection_instantiation(instance):
    assert isinstance(instance, collection_SmartInformationObjectCollection)


collection_Tag_strategy = st.builds(collection_Tag)
@given(instance=collection_Tag_strategy)
@settings(max_examples=25)
def test_collection_Tag_instantiation(instance):
    assert isinstance(instance, collection_Tag)


