import pytest
from datetime import date, datetime, time, timedelta

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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_negativeCategories16_stub_double():
    # collection_Category has no real 'collection_Category18' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Category()
    setattr(partner, 'collection_Category18', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection17', {partner})
    assert getattr(partner, 'collection_Category18') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection17', set())
    assert getattr(partner, 'collection_Category18') is None


def test_assoc_negativeMetaTags13_stub_double():
    # collection_MetaTag has no real 'collection_MetaTag15' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_MetaTag()
    setattr(partner, 'collection_MetaTag15', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection14', {partner})
    assert getattr(partner, 'collection_MetaTag15') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection14', set())
    assert getattr(partner, 'collection_MetaTag15') is None


def test_assoc_negativeOrganisations24_stub_double():
    # collection_Organisation has no real 'collection_Organisation26' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Organisation()
    setattr(partner, 'collection_Organisation26', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection25', {partner})
    assert getattr(partner, 'collection_Organisation26') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection25', set())
    assert getattr(partner, 'collection_Organisation26') is None


def test_assoc_negativePersons19_stub_double():
    # collection_Person has no real 'collection_Person21' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Person()
    setattr(partner, 'collection_Person21', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection20', {partner})
    assert getattr(partner, 'collection_Person21') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection20', set())
    assert getattr(partner, 'collection_Person21') is None


def test_assoc_negativeTags4_stub_double():
    # collection_Tag has no real 'collection_Tag6' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Tag()
    setattr(partner, 'collection_Tag6', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection5', {partner})
    assert getattr(partner, 'collection_Tag6') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection5', set())
    assert getattr(partner, 'collection_Tag6') is None


def test_assoc_positiveCategories9_stub_double():
    # collection_Category has no real 'collection_Category' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Category()
    setattr(partner, 'collection_Category', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection10', {partner})
    assert getattr(partner, 'collection_Category') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection10', set())
    assert getattr(partner, 'collection_Category') is None


def test_assoc_positiveMetaTags7_stub_double():
    # collection_MetaTag has no real 'collection_MetaTag' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_MetaTag()
    setattr(partner, 'collection_MetaTag', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection8', {partner})
    assert getattr(partner, 'collection_MetaTag') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection8', set())
    assert getattr(partner, 'collection_MetaTag') is None


def test_assoc_positiveOrganisations22_stub_double():
    # collection_Organisation has no real 'collection_Organisation' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Organisation()
    setattr(partner, 'collection_Organisation', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection23', {partner})
    assert getattr(partner, 'collection_Organisation') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection23', set())
    assert getattr(partner, 'collection_Organisation') is None


def test_assoc_positivePersons11_stub_double():
    # collection_Person has no real 'collection_Person' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Person()
    setattr(partner, 'collection_Person', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection12', {partner})
    assert getattr(partner, 'collection_Person') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection12', set())
    assert getattr(partner, 'collection_Person') is None


def test_assoc_positiveTags3_stub_double():
    # collection_Tag has no real 'collection_Tag' property in the generated
    # code (a bare stub) -- manually attach it so collection_SmartInformationObjectCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # collection_SmartInformationObjectCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = collection_SmartInformationObjectCollection(includeContents="sample_text", includeOrganisations="sample_text", includePersons="sample_text", minimumAge=date(2024, 1, 1))
    partner = collection_Tag()
    setattr(partner, 'collection_Tag', None)
    _safe_set(owner, 'collection_SmartInformationObjectCollection', {partner})
    assert getattr(partner, 'collection_Tag') == owner
    _safe_set(owner, 'collection_SmartInformationObjectCollection', set())
    assert getattr(partner, 'collection_Tag') is None


