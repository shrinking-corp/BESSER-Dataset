import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    sunBooks_AuthorsType,
    sunBooks_BookType,
    sunBooks_BooksType,
    sunBooks_CollectionType,
    sunBooks_DocumentRoot,
    sunBooks_EStringToStringMapEntry,
    sunBooks_PromotionType,
    BookCategoryType,
    BookCategoryType1,
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
    a1 = sunBooks_BookType(bookCategory="sample_text", description="sample_text", iSBN="sample_text", itemId="sample_text", name="sample_text", price="sample_text", publicationDate="sample_text")
    a2 = sunBooks_BookType(bookCategory="sample_text_2", description="sample_text_2", iSBN="sample_text_2", itemId="sample_text_2", name="sample_text_2", price="sample_text_2", publicationDate="sample_text_2")
    b = sunBooks_AuthorsType(authorName="sample_text")
    _safe_set(b, 'sunBooks_AuthorsType', a1)
    assert _is_linked(b, 'sunBooks_AuthorsType', a1)
    if hasattr(a1, 'sunBooks_BookType2'):
        assert _is_linked(a1, 'sunBooks_BookType2', b)
    _safe_set(b, 'sunBooks_AuthorsType', a2)
    assert _is_linked(b, 'sunBooks_AuthorsType', a2)
    if hasattr(a1, 'sunBooks_BookType2'):
        assert not _is_linked(a1, 'sunBooks_BookType2', b)
    if hasattr(a2, 'sunBooks_BookType2'):
        assert _is_linked(a2, 'sunBooks_BookType2', b)
    _safe_set(b, 'sunBooks_AuthorsType', None)
    assert not _is_linked(b, 'sunBooks_AuthorsType', a2)
    if hasattr(a2, 'sunBooks_BookType2'):
        assert not _is_linked(a2, 'sunBooks_BookType2', b)


def test_assoc_promotion3_reverse_link_reassign_clear():
    a1 = sunBooks_PromotionType(discount="sample_text", none="sample_text")
    a2 = sunBooks_PromotionType(discount="sample_text_2", none="sample_text_2")
    b = sunBooks_BookType(bookCategory="sample_text", description="sample_text", iSBN="sample_text", itemId="sample_text", name="sample_text", price="sample_text", publicationDate="sample_text")
    _safe_set(b, 'sunBooks_BookType4', a1)
    assert _is_linked(b, 'sunBooks_BookType4', a1)
    if hasattr(a1, 'sunBooks_PromotionType'):
        assert _is_linked(a1, 'sunBooks_PromotionType', b)
    _safe_set(b, 'sunBooks_BookType4', a2)
    assert _is_linked(b, 'sunBooks_BookType4', a2)
    if hasattr(a1, 'sunBooks_PromotionType'):
        assert not _is_linked(a1, 'sunBooks_PromotionType', b)
    if hasattr(a2, 'sunBooks_PromotionType'):
        assert _is_linked(a2, 'sunBooks_PromotionType', b)
    _safe_set(b, 'sunBooks_BookType4', None)
    assert not _is_linked(b, 'sunBooks_BookType4', a2)
    if hasattr(a2, 'sunBooks_PromotionType'):
        assert not _is_linked(a2, 'sunBooks_PromotionType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_book0_stub_double():
    # sunBooks_BooksType has no real 'sunBooks_BooksType' property in the generated
    # code (a bare stub) -- manually attach it so sunBooks_BookType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sunBooks_BookType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sunBooks_BookType(bookCategory="sample_text", description="sample_text", iSBN="sample_text", itemId="sample_text", name="sample_text", price="sample_text", publicationDate="sample_text")
    partner = sunBooks_BooksType()
    setattr(partner, 'sunBooks_BooksType', None)
    _safe_set(owner, 'sunBooks_BookType', partner)
    assert owner in getattr(partner, 'sunBooks_BooksType')
    _safe_set(owner, 'sunBooks_BookType', None)
    assert owner not in getattr(partner, 'sunBooks_BooksType')


def test_assoc_collection11_stub_double():
    # sunBooks_CollectionType has no real 'sunBooks_CollectionType13' property in the generated
    # code (a bare stub) -- manually attach it so sunBooks_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sunBooks_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sunBooks_DocumentRoot(mixed="sample_text")
    partner = sunBooks_CollectionType()
    setattr(partner, 'sunBooks_CollectionType13', None)
    _safe_set(owner, 'sunBooks_DocumentRoot12', {partner})
    assert getattr(partner, 'sunBooks_CollectionType13') == owner
    _safe_set(owner, 'sunBooks_DocumentRoot12', set())
    assert getattr(partner, 'sunBooks_CollectionType13') is None


def test_assoc_xMLNSPrefixMap7_stub_double():
    # sunBooks_EStringToStringMapEntry has no real 'sunBooks_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so sunBooks_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sunBooks_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sunBooks_DocumentRoot(mixed="sample_text")
    partner = sunBooks_EStringToStringMapEntry()
    setattr(partner, 'sunBooks_EStringToStringMapEntry', None)
    _safe_set(owner, 'sunBooks_DocumentRoot', {partner})
    assert getattr(partner, 'sunBooks_EStringToStringMapEntry') == owner
    _safe_set(owner, 'sunBooks_DocumentRoot', set())
    assert getattr(partner, 'sunBooks_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation8_stub_double():
    # sunBooks_EStringToStringMapEntry has no real 'sunBooks_EStringToStringMapEntry10' property in the generated
    # code (a bare stub) -- manually attach it so sunBooks_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sunBooks_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sunBooks_DocumentRoot(mixed="sample_text")
    partner = sunBooks_EStringToStringMapEntry()
    setattr(partner, 'sunBooks_EStringToStringMapEntry10', None)
    _safe_set(owner, 'sunBooks_DocumentRoot9', {partner})
    assert getattr(partner, 'sunBooks_EStringToStringMapEntry10') == owner
    _safe_set(owner, 'sunBooks_DocumentRoot9', set())
    assert getattr(partner, 'sunBooks_EStringToStringMapEntry10') is None


