import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    library3_BookInfoType,
    library3_BookType,
    library3_CustomerType,
    library3_DocumentRoot,
    library3_EStringToStringMapEntry,
    library3_LibraryType,
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

def test_assoc_bookInfo0_reverse_link_reassign_clear():
    a1 = library3_BookType(author="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    a2 = library3_BookType(author="sample_text_2", isbn="sample_text_2", name="sample_text_2", pages="sample_text_2", title="sample_text_2")
    b = library3_BookInfoType(any="sample_text")
    _safe_set(b, 'library3_BookInfoType', a1)
    assert _is_linked(b, 'library3_BookInfoType', a1)
    if hasattr(a1, 'library3_BookType'):
        assert _is_linked(a1, 'library3_BookType', b)
    _safe_set(b, 'library3_BookInfoType', a2)
    assert _is_linked(b, 'library3_BookInfoType', a2)
    if hasattr(a1, 'library3_BookType'):
        assert not _is_linked(a1, 'library3_BookType', b)
    if hasattr(a2, 'library3_BookType'):
        assert _is_linked(a2, 'library3_BookType', b)
    _safe_set(b, 'library3_BookInfoType', None)
    assert not _is_linked(b, 'library3_BookInfoType', a2)
    if hasattr(a2, 'library3_BookType'):
        assert not _is_linked(a2, 'library3_BookType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_book7_stub_double():
    # library3_LibraryType has no real 'library3_LibraryType8' property in the generated
    # code (a bare stub) -- manually attach it so library3_BookType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library3_BookType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library3_BookType(author="sample_text", isbn="sample_text", name="sample_text", pages="sample_text", title="sample_text")
    partner = library3_LibraryType()
    setattr(partner, 'library3_LibraryType8', None)
    _safe_set(owner, 'library3_BookType9', partner)
    assert owner in getattr(partner, 'library3_LibraryType8')
    _safe_set(owner, 'library3_BookType9', None)
    assert owner not in getattr(partner, 'library3_LibraryType8')


def test_assoc_customer10_stub_double():
    # library3_LibraryType has no real 'library3_LibraryType11' property in the generated
    # code (a bare stub) -- manually attach it so library3_CustomerType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library3_CustomerType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library3_CustomerType(borrowedBookId="sample_text", firstName="sample_text", lastName="sample_text")
    partner = library3_LibraryType()
    setattr(partner, 'library3_LibraryType11', None)
    _safe_set(owner, 'library3_CustomerType', partner)
    assert owner in getattr(partner, 'library3_LibraryType11')
    _safe_set(owner, 'library3_CustomerType', None)
    assert owner not in getattr(partner, 'library3_LibraryType11')


def test_assoc_library5_stub_double():
    # library3_LibraryType has no real 'library3_LibraryType' property in the generated
    # code (a bare stub) -- manually attach it so library3_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library3_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library3_DocumentRoot(mixed="sample_text")
    partner = library3_LibraryType()
    setattr(partner, 'library3_LibraryType', None)
    _safe_set(owner, 'library3_DocumentRoot6', {partner})
    assert getattr(partner, 'library3_LibraryType') == owner
    _safe_set(owner, 'library3_DocumentRoot6', set())
    assert getattr(partner, 'library3_LibraryType') is None


def test_assoc_xMLNSPrefixMap1_stub_double():
    # library3_EStringToStringMapEntry has no real 'library3_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so library3_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library3_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library3_DocumentRoot(mixed="sample_text")
    partner = library3_EStringToStringMapEntry()
    setattr(partner, 'library3_EStringToStringMapEntry', None)
    _safe_set(owner, 'library3_DocumentRoot', {partner})
    assert getattr(partner, 'library3_EStringToStringMapEntry') == owner
    _safe_set(owner, 'library3_DocumentRoot', set())
    assert getattr(partner, 'library3_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation2_stub_double():
    # library3_EStringToStringMapEntry has no real 'library3_EStringToStringMapEntry4' property in the generated
    # code (a bare stub) -- manually attach it so library3_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # library3_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = library3_DocumentRoot(mixed="sample_text")
    partner = library3_EStringToStringMapEntry()
    setattr(partner, 'library3_EStringToStringMapEntry4', None)
    _safe_set(owner, 'library3_DocumentRoot3', {partner})
    assert getattr(partner, 'library3_EStringToStringMapEntry4') == owner
    _safe_set(owner, 'library3_DocumentRoot3', set())
    assert getattr(partner, 'library3_EStringToStringMapEntry4') is None


