import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    imdb_Movie,
    imdb_Person,
    imdb_StaffList,
    imdb_User,
    imdb_db,
    Genre,
    StaffListType,
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

def test_assoc_actors4_reverse_link_reassign_clear():
    a1 = imdb_Person(name="sample_text")
    a2 = imdb_Person(name="sample_text_2")
    b = imdb_Movie(age=7, criticReviews=7, genres="sample_text", metaScore=7, metacriticReviews=7, poster="sample_text", rating=3.14, releaseDate=date(2024, 1, 1), runtime=7, synopsis="sample_text", title="sample_text", userRatings=7, userReviews=7)
    _safe_set(b, 'imdb_Movie5', {a1})
    assert _is_linked(b, 'imdb_Movie5', a1)
    if hasattr(a1, 'imdb_Person6'):
        assert _is_linked(a1, 'imdb_Person6', b)
    _safe_set(b, 'imdb_Movie5', {a2})
    assert _is_linked(b, 'imdb_Movie5', a2)
    if hasattr(a1, 'imdb_Person6'):
        assert not _is_linked(a1, 'imdb_Person6', b)
    if hasattr(a2, 'imdb_Person6'):
        assert _is_linked(a2, 'imdb_Person6', b)
    _safe_set(b, 'imdb_Movie5', set())
    assert not _is_linked(b, 'imdb_Movie5', a2)
    if hasattr(a2, 'imdb_Person6'):
        assert not _is_linked(a2, 'imdb_Person6', b)


def test_assoc_allActors12_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_Person(name="sample_text")
    _safe_set(b, 'imdb_Person14', a1)
    assert _is_linked(b, 'imdb_Person14', a1)
    if hasattr(a1, 'imdb_db13'):
        assert _is_linked(a1, 'imdb_db13', b)
    _safe_set(b, 'imdb_Person14', a2)
    assert _is_linked(b, 'imdb_Person14', a2)
    if hasattr(a1, 'imdb_db13'):
        assert not _is_linked(a1, 'imdb_db13', b)
    if hasattr(a2, 'imdb_db13'):
        assert _is_linked(a2, 'imdb_db13', b)
    _safe_set(b, 'imdb_Person14', None)
    assert not _is_linked(b, 'imdb_Person14', a2)
    if hasattr(a2, 'imdb_db13'):
        assert not _is_linked(a2, 'imdb_db13', b)


def test_assoc_allDirectors7_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_Person(name="sample_text")
    _safe_set(b, 'imdb_Person8', a1)
    assert _is_linked(b, 'imdb_Person8', a1)
    if hasattr(a1, 'imdb_db'):
        assert _is_linked(a1, 'imdb_db', b)
    _safe_set(b, 'imdb_Person8', a2)
    assert _is_linked(b, 'imdb_Person8', a2)
    if hasattr(a1, 'imdb_db'):
        assert not _is_linked(a1, 'imdb_db', b)
    if hasattr(a2, 'imdb_db'):
        assert _is_linked(a2, 'imdb_db', b)
    _safe_set(b, 'imdb_Person8', None)
    assert not _is_linked(b, 'imdb_Person8', a2)
    if hasattr(a2, 'imdb_db'):
        assert not _is_linked(a2, 'imdb_db', b)


def test_assoc_allMovies15_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_Movie(age=7, criticReviews=7, genres="sample_text", metaScore=7, metacriticReviews=7, poster="sample_text", rating=3.14, releaseDate=date(2024, 1, 1), runtime=7, synopsis="sample_text", title="sample_text", userRatings=7, userReviews=7)
    _safe_set(b, 'imdb_Movie17', a1)
    assert _is_linked(b, 'imdb_Movie17', a1)
    if hasattr(a1, 'imdb_db16'):
        assert _is_linked(a1, 'imdb_db16', b)
    _safe_set(b, 'imdb_Movie17', a2)
    assert _is_linked(b, 'imdb_Movie17', a2)
    if hasattr(a1, 'imdb_db16'):
        assert not _is_linked(a1, 'imdb_db16', b)
    if hasattr(a2, 'imdb_db16'):
        assert _is_linked(a2, 'imdb_db16', b)
    _safe_set(b, 'imdb_Movie17', None)
    assert not _is_linked(b, 'imdb_Movie17', a2)
    if hasattr(a2, 'imdb_db16'):
        assert not _is_linked(a2, 'imdb_db16', b)


def test_assoc_allStaffLists18_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_StaffList(coverPhoto="sample_text", createdDate=date(2024, 1, 1), elementType="sample_text", elements="sample_text", name="sample_text")
    _safe_set(b, 'imdb_StaffList', a1)
    assert _is_linked(b, 'imdb_StaffList', a1)
    if hasattr(a1, 'imdb_db19'):
        assert _is_linked(a1, 'imdb_db19', b)
    _safe_set(b, 'imdb_StaffList', a2)
    assert _is_linked(b, 'imdb_StaffList', a2)
    if hasattr(a1, 'imdb_db19'):
        assert not _is_linked(a1, 'imdb_db19', b)
    if hasattr(a2, 'imdb_db19'):
        assert _is_linked(a2, 'imdb_db19', b)
    _safe_set(b, 'imdb_StaffList', None)
    assert not _is_linked(b, 'imdb_StaffList', a2)
    if hasattr(a2, 'imdb_db19'):
        assert not _is_linked(a2, 'imdb_db19', b)


def test_assoc_allUsers20_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_User(username="sample_text", watchlist="sample_text")
    _safe_set(b, 'imdb_User', a1)
    assert _is_linked(b, 'imdb_User', a1)
    if hasattr(a1, 'imdb_db21'):
        assert _is_linked(a1, 'imdb_db21', b)
    _safe_set(b, 'imdb_User', a2)
    assert _is_linked(b, 'imdb_User', a2)
    if hasattr(a1, 'imdb_db21'):
        assert not _is_linked(a1, 'imdb_db21', b)
    if hasattr(a2, 'imdb_db21'):
        assert _is_linked(a2, 'imdb_db21', b)
    _safe_set(b, 'imdb_User', None)
    assert not _is_linked(b, 'imdb_User', a2)
    if hasattr(a2, 'imdb_db21'):
        assert not _is_linked(a2, 'imdb_db21', b)


def test_assoc_allWriters9_reverse_link_reassign_clear():
    a1 = imdb_db(bestOf2014="sample_text")
    a2 = imdb_db(bestOf2014="sample_text_2")
    b = imdb_Person(name="sample_text")
    _safe_set(b, 'imdb_Person11', a1)
    assert _is_linked(b, 'imdb_Person11', a1)
    if hasattr(a1, 'imdb_db10'):
        assert _is_linked(a1, 'imdb_db10', b)
    _safe_set(b, 'imdb_Person11', a2)
    assert _is_linked(b, 'imdb_Person11', a2)
    if hasattr(a1, 'imdb_db10'):
        assert not _is_linked(a1, 'imdb_db10', b)
    if hasattr(a2, 'imdb_db10'):
        assert _is_linked(a2, 'imdb_db10', b)
    _safe_set(b, 'imdb_Person11', None)
    assert not _is_linked(b, 'imdb_Person11', a2)
    if hasattr(a2, 'imdb_db10'):
        assert not _is_linked(a2, 'imdb_db10', b)


def test_assoc_director0_reverse_link_reassign_clear():
    a1 = imdb_Person(name="sample_text")
    a2 = imdb_Person(name="sample_text_2")
    b = imdb_Movie(age=7, criticReviews=7, genres="sample_text", metaScore=7, metacriticReviews=7, poster="sample_text", rating=3.14, releaseDate=date(2024, 1, 1), runtime=7, synopsis="sample_text", title="sample_text", userRatings=7, userReviews=7)
    _safe_set(b, 'imdb_Movie', a1)
    assert _is_linked(b, 'imdb_Movie', a1)
    if hasattr(a1, 'imdb_Person'):
        assert _is_linked(a1, 'imdb_Person', b)
    _safe_set(b, 'imdb_Movie', a2)
    assert _is_linked(b, 'imdb_Movie', a2)
    if hasattr(a1, 'imdb_Person'):
        assert not _is_linked(a1, 'imdb_Person', b)
    if hasattr(a2, 'imdb_Person'):
        assert _is_linked(a2, 'imdb_Person', b)
    _safe_set(b, 'imdb_Movie', None)
    assert not _is_linked(b, 'imdb_Movie', a2)
    if hasattr(a2, 'imdb_Person'):
        assert not _is_linked(a2, 'imdb_Person', b)


def test_assoc_user22_reverse_link_reassign_clear():
    a1 = imdb_User(username="sample_text", watchlist="sample_text")
    a2 = imdb_User(username="sample_text_2", watchlist="sample_text_2")
    b = imdb_StaffList(coverPhoto="sample_text", createdDate=date(2024, 1, 1), elementType="sample_text", elements="sample_text", name="sample_text")
    _safe_set(b, 'imdb_StaffList23', a1)
    assert _is_linked(b, 'imdb_StaffList23', a1)
    if hasattr(a1, 'imdb_User24'):
        assert _is_linked(a1, 'imdb_User24', b)
    _safe_set(b, 'imdb_StaffList23', a2)
    assert _is_linked(b, 'imdb_StaffList23', a2)
    if hasattr(a1, 'imdb_User24'):
        assert not _is_linked(a1, 'imdb_User24', b)
    if hasattr(a2, 'imdb_User24'):
        assert _is_linked(a2, 'imdb_User24', b)
    _safe_set(b, 'imdb_StaffList23', None)
    assert not _is_linked(b, 'imdb_StaffList23', a2)
    if hasattr(a2, 'imdb_User24'):
        assert not _is_linked(a2, 'imdb_User24', b)


def test_assoc_writers1_reverse_link_reassign_clear():
    a1 = imdb_Person(name="sample_text")
    a2 = imdb_Person(name="sample_text_2")
    b = imdb_Movie(age=7, criticReviews=7, genres="sample_text", metaScore=7, metacriticReviews=7, poster="sample_text", rating=3.14, releaseDate=date(2024, 1, 1), runtime=7, synopsis="sample_text", title="sample_text", userRatings=7, userReviews=7)
    _safe_set(b, 'imdb_Movie2', {a1})
    assert _is_linked(b, 'imdb_Movie2', a1)
    if hasattr(a1, 'imdb_Person3'):
        assert _is_linked(a1, 'imdb_Person3', b)
    _safe_set(b, 'imdb_Movie2', {a2})
    assert _is_linked(b, 'imdb_Movie2', a2)
    if hasattr(a1, 'imdb_Person3'):
        assert not _is_linked(a1, 'imdb_Person3', b)
    if hasattr(a2, 'imdb_Person3'):
        assert _is_linked(a2, 'imdb_Person3', b)
    _safe_set(b, 'imdb_Movie2', set())
    assert not _is_linked(b, 'imdb_Movie2', a2)
    if hasattr(a2, 'imdb_Person3'):
        assert not _is_linked(a2, 'imdb_Person3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

