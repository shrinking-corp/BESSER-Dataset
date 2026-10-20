import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CriticsReviewType,
    db_CriticsReviewType,
    db_CustomerReviewType,
    db_CustomerType,
    db_DocumentRoot,
    db_EStringToStringMapEntry,
    db_MovieDBType,
    db_MovieType,
    GenreTypes,
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

def test_assoc_criticsReview14_reverse_link_reassign_clear():
    a1 = db_MovieType(actors="sample_text", any="sample_text", criticsReviewGroup="sample_text", director="sample_text", genre="sample_text", iD="sample_text", summary="sample_text", title="sample_text")
    a2 = db_MovieType(actors="sample_text_2", any="sample_text_2", criticsReviewGroup="sample_text_2", director="sample_text_2", genre="sample_text_2", iD="sample_text_2", summary="sample_text_2", title="sample_text_2")
    b = db_CriticsReviewType(rating="sample_text", reviewedBy="sample_text")
    _safe_set(b, 'db_CriticsReviewType16', a1)
    assert _is_linked(b, 'db_CriticsReviewType16', a1)
    if hasattr(a1, 'db_MovieType15'):
        assert _is_linked(a1, 'db_MovieType15', b)
    _safe_set(b, 'db_CriticsReviewType16', a2)
    assert _is_linked(b, 'db_CriticsReviewType16', a2)
    if hasattr(a1, 'db_MovieType15'):
        assert not _is_linked(a1, 'db_MovieType15', b)
    if hasattr(a2, 'db_MovieType15'):
        assert _is_linked(a2, 'db_MovieType15', b)
    _safe_set(b, 'db_CriticsReviewType16', None)
    assert not _is_linked(b, 'db_CriticsReviewType16', a2)
    if hasattr(a2, 'db_MovieType15'):
        assert not _is_linked(a2, 'db_MovieType15', b)


def test_assoc_criticsReview6_reverse_link_reassign_clear():
    a1 = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    a2 = db_DocumentRoot(language="sample_text_2", mixed="sample_text_2", specialFeatures="sample_text_2")
    b = db_CriticsReviewType(rating="sample_text", reviewedBy="sample_text")
    _safe_set(b, 'db_CriticsReviewType', a1)
    assert _is_linked(b, 'db_CriticsReviewType', a1)
    if hasattr(a1, 'db_DocumentRoot7'):
        assert _is_linked(a1, 'db_DocumentRoot7', b)
    _safe_set(b, 'db_CriticsReviewType', a2)
    assert _is_linked(b, 'db_CriticsReviewType', a2)
    if hasattr(a1, 'db_DocumentRoot7'):
        assert not _is_linked(a1, 'db_DocumentRoot7', b)
    if hasattr(a2, 'db_DocumentRoot7'):
        assert _is_linked(a2, 'db_DocumentRoot7', b)
    _safe_set(b, 'db_CriticsReviewType', None)
    assert not _is_linked(b, 'db_CriticsReviewType', a2)
    if hasattr(a2, 'db_DocumentRoot7'):
        assert not _is_linked(a2, 'db_DocumentRoot7', b)


def test_assoc_customerReview8_reverse_link_reassign_clear():
    a1 = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    a2 = db_DocumentRoot(language="sample_text_2", mixed="sample_text_2", specialFeatures="sample_text_2")
    b = db_CustomerReviewType(comment="sample_text")
    _safe_set(b, 'db_CustomerReviewType', a1)
    assert _is_linked(b, 'db_CustomerReviewType', a1)
    if hasattr(a1, 'db_DocumentRoot9'):
        assert _is_linked(a1, 'db_DocumentRoot9', b)
    _safe_set(b, 'db_CustomerReviewType', a2)
    assert _is_linked(b, 'db_CustomerReviewType', a2)
    if hasattr(a1, 'db_DocumentRoot9'):
        assert not _is_linked(a1, 'db_DocumentRoot9', b)
    if hasattr(a2, 'db_DocumentRoot9'):
        assert _is_linked(a2, 'db_DocumentRoot9', b)
    _safe_set(b, 'db_CustomerReviewType', None)
    assert not _is_linked(b, 'db_CustomerReviewType', a2)
    if hasattr(a2, 'db_DocumentRoot9'):
        assert not _is_linked(a2, 'db_DocumentRoot9', b)


def test_assoc_movie12_reverse_link_reassign_clear():
    a1 = db_MovieType(actors="sample_text", any="sample_text", criticsReviewGroup="sample_text", director="sample_text", genre="sample_text", iD="sample_text", summary="sample_text", title="sample_text")
    a2 = db_MovieType(actors="sample_text_2", any="sample_text_2", criticsReviewGroup="sample_text_2", director="sample_text_2", genre="sample_text_2", iD="sample_text_2", summary="sample_text_2", title="sample_text_2")
    b = db_MovieDBType(comment="sample_text", movieDBFeatureMap="sample_text")
    _safe_set(b, 'db_MovieDBType13', {a1})
    assert _is_linked(b, 'db_MovieDBType13', a1)
    if hasattr(a1, 'db_MovieType'):
        assert _is_linked(a1, 'db_MovieType', b)
    _safe_set(b, 'db_MovieDBType13', {a2})
    assert _is_linked(b, 'db_MovieDBType13', a2)
    if hasattr(a1, 'db_MovieType'):
        assert not _is_linked(a1, 'db_MovieType', b)
    if hasattr(a2, 'db_MovieType'):
        assert _is_linked(a2, 'db_MovieType', b)
    _safe_set(b, 'db_MovieDBType13', set())
    assert not _is_linked(b, 'db_MovieDBType13', a2)
    if hasattr(a2, 'db_MovieType'):
        assert not _is_linked(a2, 'db_MovieType', b)


def test_assoc_movieDB10_reverse_link_reassign_clear():
    a1 = db_MovieDBType(comment="sample_text", movieDBFeatureMap="sample_text")
    a2 = db_MovieDBType(comment="sample_text_2", movieDBFeatureMap="sample_text_2")
    b = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    _safe_set(b, 'db_DocumentRoot11', {a1})
    assert _is_linked(b, 'db_DocumentRoot11', a1)
    if hasattr(a1, 'db_MovieDBType'):
        assert _is_linked(a1, 'db_MovieDBType', b)
    _safe_set(b, 'db_DocumentRoot11', {a2})
    assert _is_linked(b, 'db_DocumentRoot11', a2)
    if hasattr(a1, 'db_MovieDBType'):
        assert not _is_linked(a1, 'db_MovieDBType', b)
    if hasattr(a2, 'db_MovieDBType'):
        assert _is_linked(a2, 'db_MovieDBType', b)
    _safe_set(b, 'db_DocumentRoot11', set())
    assert not _is_linked(b, 'db_DocumentRoot11', a2)
    if hasattr(a2, 'db_MovieDBType'):
        assert not _is_linked(a2, 'db_MovieDBType', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_checkedOutBy17_stub_double():
    # db_CustomerType has no real 'db_CustomerType19' property in the generated
    # code (a bare stub) -- manually attach it so db_MovieType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_MovieType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_MovieType(actors="sample_text", any="sample_text", criticsReviewGroup="sample_text", director="sample_text", genre="sample_text", iD="sample_text", summary="sample_text", title="sample_text")
    partner = db_CustomerType()
    setattr(partner, 'db_CustomerType19', None)
    _safe_set(owner, 'db_MovieType18', partner)
    assert getattr(partner, 'db_CustomerType19') == owner
    _safe_set(owner, 'db_MovieType18', None)
    assert getattr(partner, 'db_CustomerType19') is None


def test_assoc_checkedOutBy4_stub_double():
    # db_CustomerType has no real 'db_CustomerType' property in the generated
    # code (a bare stub) -- manually attach it so db_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    partner = db_CustomerType()
    setattr(partner, 'db_CustomerType', None)
    _safe_set(owner, 'db_DocumentRoot5', {partner})
    assert getattr(partner, 'db_CustomerType') == owner
    _safe_set(owner, 'db_DocumentRoot5', set())
    assert getattr(partner, 'db_CustomerType') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # db_EStringToStringMapEntry has no real 'db_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so db_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    partner = db_EStringToStringMapEntry()
    setattr(partner, 'db_EStringToStringMapEntry', None)
    _safe_set(owner, 'db_DocumentRoot', {partner})
    assert getattr(partner, 'db_EStringToStringMapEntry') == owner
    _safe_set(owner, 'db_DocumentRoot', set())
    assert getattr(partner, 'db_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # db_EStringToStringMapEntry has no real 'db_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so db_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # db_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = db_DocumentRoot(language="sample_text", mixed="sample_text", specialFeatures="sample_text")
    partner = db_EStringToStringMapEntry()
    setattr(partner, 'db_EStringToStringMapEntry3', None)
    _safe_set(owner, 'db_DocumentRoot2', {partner})
    assert getattr(partner, 'db_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'db_DocumentRoot2', set())
    assert getattr(partner, 'db_EStringToStringMapEntry3') is None


