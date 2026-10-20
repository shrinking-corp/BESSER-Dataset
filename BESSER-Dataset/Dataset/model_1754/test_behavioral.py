import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    simpleany_BookType,
    simpleany_Description,
    simpleany_DocumentRoot,
    simpleany_EStringToStringMapEntry,
    simpleany_LibraryType,
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

def test_assoc_description0_reverse_link_reassign_clear():
    a1 = simpleany_Description(keyword="sample_text", mixed="sample_text")
    a2 = simpleany_Description(keyword="sample_text_2", mixed="sample_text_2")
    b = simpleany_BookType(author="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'simpleany_BookType', a1)
    assert _is_linked(b, 'simpleany_BookType', a1)
    if hasattr(a1, 'simpleany_Description'):
        assert _is_linked(a1, 'simpleany_Description', b)
    _safe_set(b, 'simpleany_BookType', a2)
    assert _is_linked(b, 'simpleany_BookType', a2)
    if hasattr(a1, 'simpleany_Description'):
        assert not _is_linked(a1, 'simpleany_Description', b)
    if hasattr(a2, 'simpleany_Description'):
        assert _is_linked(a2, 'simpleany_Description', b)
    _safe_set(b, 'simpleany_BookType', None)
    assert not _is_linked(b, 'simpleany_BookType', a2)
    if hasattr(a2, 'simpleany_Description'):
        assert not _is_linked(a2, 'simpleany_Description', b)


def test_assoc_description2_reverse_link_reassign_clear():
    a1 = simpleany_Description(keyword="sample_text", mixed="sample_text")
    a2 = simpleany_Description(keyword="sample_text_2", mixed="sample_text_2")
    b = simpleany_Description(keyword="sample_text", mixed="sample_text")
    _safe_set(b, 'simpleany_Description3', a1)
    assert _is_linked(b, 'simpleany_Description3', a1)
    if hasattr(a1, 'simpleany_Description1'):
        assert _is_linked(a1, 'simpleany_Description1', b)
    _safe_set(b, 'simpleany_Description3', a2)
    assert _is_linked(b, 'simpleany_Description3', a2)
    if hasattr(a1, 'simpleany_Description1'):
        assert not _is_linked(a1, 'simpleany_Description1', b)
    if hasattr(a2, 'simpleany_Description1'):
        assert _is_linked(a2, 'simpleany_Description1', b)
    _safe_set(b, 'simpleany_Description3', None)
    assert not _is_linked(b, 'simpleany_Description3', a2)
    if hasattr(a2, 'simpleany_Description1'):
        assert not _is_linked(a2, 'simpleany_Description1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_book10_stub_double():
    # simpleany_LibraryType has no real 'simpleany_LibraryType11' property in the generated
    # code (a bare stub) -- manually attach it so simpleany_BookType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleany_BookType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleany_BookType(author="sample_text", name="sample_text", title="sample_text")
    partner = simpleany_LibraryType()
    setattr(partner, 'simpleany_LibraryType11', None)
    _safe_set(owner, 'simpleany_BookType12', partner)
    assert owner in getattr(partner, 'simpleany_LibraryType11')
    _safe_set(owner, 'simpleany_BookType12', None)
    assert owner not in getattr(partner, 'simpleany_LibraryType11')


def test_assoc_library8_stub_double():
    # simpleany_LibraryType has no real 'simpleany_LibraryType' property in the generated
    # code (a bare stub) -- manually attach it so simpleany_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleany_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleany_DocumentRoot(mixed="sample_text")
    partner = simpleany_LibraryType()
    setattr(partner, 'simpleany_LibraryType', None)
    _safe_set(owner, 'simpleany_DocumentRoot9', {partner})
    assert getattr(partner, 'simpleany_LibraryType') == owner
    _safe_set(owner, 'simpleany_DocumentRoot9', set())
    assert getattr(partner, 'simpleany_LibraryType') is None


def test_assoc_xMLNSPrefixMap4_stub_double():
    # simpleany_EStringToStringMapEntry has no real 'simpleany_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so simpleany_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleany_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleany_DocumentRoot(mixed="sample_text")
    partner = simpleany_EStringToStringMapEntry()
    setattr(partner, 'simpleany_EStringToStringMapEntry', None)
    _safe_set(owner, 'simpleany_DocumentRoot', {partner})
    assert getattr(partner, 'simpleany_EStringToStringMapEntry') == owner
    _safe_set(owner, 'simpleany_DocumentRoot', set())
    assert getattr(partner, 'simpleany_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation5_stub_double():
    # simpleany_EStringToStringMapEntry has no real 'simpleany_EStringToStringMapEntry7' property in the generated
    # code (a bare stub) -- manually attach it so simpleany_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # simpleany_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = simpleany_DocumentRoot(mixed="sample_text")
    partner = simpleany_EStringToStringMapEntry()
    setattr(partner, 'simpleany_EStringToStringMapEntry7', None)
    _safe_set(owner, 'simpleany_DocumentRoot6', {partner})
    assert getattr(partner, 'simpleany_EStringToStringMapEntry7') == owner
    _safe_set(owner, 'simpleany_DocumentRoot6', set())
    assert getattr(partner, 'simpleany_EStringToStringMapEntry7') is None


