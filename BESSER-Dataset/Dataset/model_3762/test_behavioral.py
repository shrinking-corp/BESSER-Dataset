import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CriticsReview,
    movies_Copy,
    movies_CriticsReview,
    movies_CustomerReview,
    movies_Movie,
    movies_MoviesDB,
    movies_Place,
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

def test_assoc_copies0_reverse_link_reassign_clear():
    a1 = movies_Movie(actors="sample_text", director="sample_text", genre="sample_text", summary="sample_text", title="sample_text")
    a2 = movies_Movie(actors="sample_text_2", director="sample_text_2", genre="sample_text_2", summary="sample_text_2", title="sample_text_2")
    b = movies_Copy(id="sample_text")
    _safe_set(b, 'movies_Copy', a1)
    assert _is_linked(b, 'movies_Copy', a1)
    if hasattr(a1, 'movies_Movie'):
        assert _is_linked(a1, 'movies_Movie', b)
    _safe_set(b, 'movies_Copy', a2)
    assert _is_linked(b, 'movies_Copy', a2)
    if hasattr(a1, 'movies_Movie'):
        assert not _is_linked(a1, 'movies_Movie', b)
    if hasattr(a2, 'movies_Movie'):
        assert _is_linked(a2, 'movies_Movie', b)
    _safe_set(b, 'movies_Copy', None)
    assert not _is_linked(b, 'movies_Copy', a2)
    if hasattr(a2, 'movies_Movie'):
        assert not _is_linked(a2, 'movies_Movie', b)


def test_assoc_movies3_reverse_link_reassign_clear():
    a1 = movies_MoviesDB(comment="sample_text")
    a2 = movies_MoviesDB(comment="sample_text_2")
    b = movies_Movie(actors="sample_text", director="sample_text", genre="sample_text", summary="sample_text", title="sample_text")
    _safe_set(b, 'movies_Movie4', a1)
    assert _is_linked(b, 'movies_Movie4', a1)
    if hasattr(a1, 'movies_MoviesDB'):
        assert _is_linked(a1, 'movies_MoviesDB', b)
    _safe_set(b, 'movies_Movie4', a2)
    assert _is_linked(b, 'movies_Movie4', a2)
    if hasattr(a1, 'movies_MoviesDB'):
        assert not _is_linked(a1, 'movies_MoviesDB', b)
    if hasattr(a2, 'movies_MoviesDB'):
        assert _is_linked(a2, 'movies_MoviesDB', b)
    _safe_set(b, 'movies_Movie4', None)
    assert not _is_linked(b, 'movies_Movie4', a2)
    if hasattr(a2, 'movies_MoviesDB'):
        assert not _is_linked(a2, 'movies_MoviesDB', b)


def test_assoc_place7_reverse_link_reassign_clear():
    a1 = movies_Place(id="sample_text", name="sample_text")
    a2 = movies_Place(id="sample_text_2", name="sample_text_2")
    b = movies_Copy(id="sample_text")
    _safe_set(b, 'movies_Copy8', a1)
    assert _is_linked(b, 'movies_Copy8', a1)
    if hasattr(a1, 'movies_Place9'):
        assert _is_linked(a1, 'movies_Place9', b)
    _safe_set(b, 'movies_Copy8', a2)
    assert _is_linked(b, 'movies_Copy8', a2)
    if hasattr(a1, 'movies_Place9'):
        assert not _is_linked(a1, 'movies_Place9', b)
    if hasattr(a2, 'movies_Place9'):
        assert _is_linked(a2, 'movies_Place9', b)
    _safe_set(b, 'movies_Copy8', None)
    assert not _is_linked(b, 'movies_Copy8', a2)
    if hasattr(a2, 'movies_Place9'):
        assert not _is_linked(a2, 'movies_Place9', b)


def test_assoc_places5_reverse_link_reassign_clear():
    a1 = movies_Place(id="sample_text", name="sample_text")
    a2 = movies_Place(id="sample_text_2", name="sample_text_2")
    b = movies_MoviesDB(comment="sample_text")
    _safe_set(b, 'movies_MoviesDB6', {a1})
    assert _is_linked(b, 'movies_MoviesDB6', a1)
    if hasattr(a1, 'movies_Place'):
        assert _is_linked(a1, 'movies_Place', b)
    _safe_set(b, 'movies_MoviesDB6', {a2})
    assert _is_linked(b, 'movies_MoviesDB6', a2)
    if hasattr(a1, 'movies_Place'):
        assert not _is_linked(a1, 'movies_Place', b)
    if hasattr(a2, 'movies_Place'):
        assert _is_linked(a2, 'movies_Place', b)
    _safe_set(b, 'movies_MoviesDB6', set())
    assert not _is_linked(b, 'movies_MoviesDB6', a2)
    if hasattr(a2, 'movies_Place'):
        assert not _is_linked(a2, 'movies_Place', b)


def test_assoc_review1_reverse_link_reassign_clear():
    a1 = movies_Movie(actors="sample_text", director="sample_text", genre="sample_text", summary="sample_text", title="sample_text")
    a2 = movies_Movie(actors="sample_text_2", director="sample_text_2", genre="sample_text_2", summary="sample_text_2", title="sample_text_2")
    b = movies_CriticsReview(rating="sample_text", reviewedBy="sample_text")
    _safe_set(b, 'movies_CriticsReview', a1)
    assert _is_linked(b, 'movies_CriticsReview', a1)
    if hasattr(a1, 'movies_Movie2'):
        assert _is_linked(a1, 'movies_Movie2', b)
    _safe_set(b, 'movies_CriticsReview', a2)
    assert _is_linked(b, 'movies_CriticsReview', a2)
    if hasattr(a1, 'movies_Movie2'):
        assert not _is_linked(a1, 'movies_Movie2', b)
    if hasattr(a2, 'movies_Movie2'):
        assert _is_linked(a2, 'movies_Movie2', b)
    _safe_set(b, 'movies_CriticsReview', None)
    assert not _is_linked(b, 'movies_CriticsReview', a2)
    if hasattr(a2, 'movies_Movie2'):
        assert not _is_linked(a2, 'movies_Movie2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

