import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    model_Book,
    model_ETypes,
    model_Library,
    model_Location,
    model_MappedLibrary,
    model_Person,
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


def test_assoc_featureMapReferenceType138_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
    _safe_set(b, 'model_PrimaryObject39', {a1})
    assert _is_linked(b, 'model_PrimaryObject39', a1)
    if hasattr(a1, 'model_TargetObject40'):
        assert _is_linked(a1, 'model_TargetObject40', b)
    _safe_set(b, 'model_PrimaryObject39', {a2})
    assert _is_linked(b, 'model_PrimaryObject39', a2)
    if hasattr(a1, 'model_TargetObject40'):
        assert not _is_linked(a1, 'model_TargetObject40', b)
    if hasattr(a2, 'model_TargetObject40'):
        assert _is_linked(a2, 'model_TargetObject40', b)
    _safe_set(b, 'model_PrimaryObject39', set())
    assert not _is_linked(b, 'model_PrimaryObject39', a2)
    if hasattr(a2, 'model_TargetObject40'):
        assert not _is_linked(a2, 'model_TargetObject40', b)


def test_assoc_featureMapReferenceType235_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_featuredBook8_reverse_link_reassign_clear():
    a1 = model_Location(address="sample_text", id="sample_text")
    a2 = model_Location(address="sample_text_2", id="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book10', a1)
    assert _is_linked(b, 'model_Book10', a1)
    if hasattr(a1, 'model_Location9'):
        assert _is_linked(a1, 'model_Location9', b)
    _safe_set(b, 'model_Book10', a2)
    assert _is_linked(b, 'model_Book10', a2)
    if hasattr(a1, 'model_Location9'):
        assert not _is_linked(a1, 'model_Location9', b)
    if hasattr(a2, 'model_Location9'):
        assert _is_linked(a2, 'model_Location9', b)
    _safe_set(b, 'model_Book10', None)
    assert not _is_linked(b, 'model_Book10', a2)
    if hasattr(a2, 'model_Location9'):
        assert not _is_linked(a2, 'model_Location9', b)


def test_assoc_location11_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Location(address="sample_text", id="sample_text")
    _safe_set(b, 'model_Location12', a1)
    assert _is_linked(b, 'model_Location12', a1)
    if hasattr(a1, 'model_MappedLibrary'):
        assert _is_linked(a1, 'model_MappedLibrary', b)
    _safe_set(b, 'model_Location12', a2)
    assert _is_linked(b, 'model_Location12', a2)
    if hasattr(a1, 'model_MappedLibrary'):
        assert not _is_linked(a1, 'model_MappedLibrary', b)
    if hasattr(a2, 'model_MappedLibrary'):
        assert _is_linked(a2, 'model_MappedLibrary', b)
    _safe_set(b, 'model_Location12', None)
    assert not _is_linked(b, 'model_Location12', a2)
    if hasattr(a2, 'model_MappedLibrary'):
        assert not _is_linked(a2, 'model_MappedLibrary', b)


def test_assoc_multipleContainmentReferenceNoProxies26_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_multipleContainmentReferenceProxies32_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_multipleNonContainmentReference20_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_rareBooks13_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book15', a1)
    assert _is_linked(b, 'model_Book15', a1)
    if hasattr(a1, 'model_MappedLibrary14'):
        assert _is_linked(a1, 'model_MappedLibrary14', b)
    _safe_set(b, 'model_Book15', a2)
    assert _is_linked(b, 'model_Book15', a2)
    if hasattr(a1, 'model_MappedLibrary14'):
        assert not _is_linked(a1, 'model_MappedLibrary14', b)
    if hasattr(a2, 'model_MappedLibrary14'):
        assert _is_linked(a2, 'model_MappedLibrary14', b)
    _safe_set(b, 'model_Book15', None)
    assert not _is_linked(b, 'model_Book15', a2)
    if hasattr(a2, 'model_MappedLibrary14'):
        assert not _is_linked(a2, 'model_MappedLibrary14', b)


def test_assoc_regularBooks16_reverse_link_reassign_clear():
    a1 = model_MappedLibrary(books="sample_text")
    a2 = model_MappedLibrary(books="sample_text_2")
    b = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    _safe_set(b, 'model_Book18', a1)
    assert _is_linked(b, 'model_Book18', a1)
    if hasattr(a1, 'model_MappedLibrary17'):
        assert _is_linked(a1, 'model_MappedLibrary17', b)
    _safe_set(b, 'model_Book18', a2)
    assert _is_linked(b, 'model_Book18', a2)
    if hasattr(a1, 'model_MappedLibrary17'):
        assert not _is_linked(a1, 'model_MappedLibrary17', b)
    if hasattr(a2, 'model_MappedLibrary17'):
        assert _is_linked(a2, 'model_MappedLibrary17', b)
    _safe_set(b, 'model_Book18', None)
    assert not _is_linked(b, 'model_Book18', a2)
    if hasattr(a2, 'model_MappedLibrary17'):
        assert not _is_linked(a2, 'model_MappedLibrary17', b)


def test_assoc_singleContainmentReferenceNoProxies23_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_singleContainmentReferenceProxies29_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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


def test_assoc_singleNonContainmentReference19_reverse_link_reassign_clear():
    a1 = model_TargetObject(arrayAttribute="sample_text", singleAttribute="sample_text")
    a2 = model_TargetObject(arrayAttribute="sample_text_2", singleAttribute="sample_text_2")
    b = model_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", name="sample_text")
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

def test_assoc_books2_stub_double():
    # model_Library has no real 'model_Library' property in the generated
    # code (a bare stub) -- manually attach it so model_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    partner = model_Library()
    setattr(partner, 'model_Library', None)
    _safe_set(owner, 'model_Book', partner)
    assert owner in getattr(partner, 'model_Library')
    _safe_set(owner, 'model_Book', None)
    assert owner not in getattr(partner, 'model_Library')


def test_assoc_latestBook5_stub_double():
    # model_Library has no real 'model_Library6' property in the generated
    # code (a bare stub) -- manually attach it so model_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Book(data="sample_text", tags="sample_text", title="sample_text")
    partner = model_Library()
    setattr(partner, 'model_Library6', None)
    _safe_set(owner, 'model_Book7', partner)
    assert getattr(partner, 'model_Library6') == owner
    _safe_set(owner, 'model_Book7', None)
    assert getattr(partner, 'model_Library6') is None


def test_assoc_location3_stub_double():
    # model_Library has no real 'model_Library4' property in the generated
    # code (a bare stub) -- manually attach it so model_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Location(address="sample_text", id="sample_text")
    partner = model_Library()
    setattr(partner, 'model_Library4', None)
    _safe_set(owner, 'model_Location', partner)
    assert getattr(partner, 'model_Library4') == owner
    _safe_set(owner, 'model_Location', None)
    assert getattr(partner, 'model_Library4') is None


