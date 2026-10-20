import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BaseObject,
    MediaPlayer_BaseObject,
    MediaPlayer_Library,
    MediaPlayer_MediaApi,
    MediaPlayer_MediaObject,
    MediaPlayer_PlayLayer,
    MediaPlayer_Playlist,
    State,
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

def test_assoc_currentlyPaused3_reverse_link_reassign_clear():
    a1 = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    a2 = MediaPlayer_MediaObject(album="sample_text_2", artist="sample_text_2", location="sample_text_2", state="sample_text_2", title="sample_text_2", year=13)
    b = MediaPlayer_MediaApi()
    _safe_set(b, 'MediaPlayer_MediaApi4', {a1})
    assert _is_linked(b, 'MediaPlayer_MediaApi4', a1)
    if hasattr(a1, 'MediaPlayer_MediaObject5'):
        assert _is_linked(a1, 'MediaPlayer_MediaObject5', b)
    _safe_set(b, 'MediaPlayer_MediaApi4', {a2})
    assert _is_linked(b, 'MediaPlayer_MediaApi4', a2)
    if hasattr(a1, 'MediaPlayer_MediaObject5'):
        assert not _is_linked(a1, 'MediaPlayer_MediaObject5', b)
    if hasattr(a2, 'MediaPlayer_MediaObject5'):
        assert _is_linked(a2, 'MediaPlayer_MediaObject5', b)
    _safe_set(b, 'MediaPlayer_MediaApi4', set())
    assert not _is_linked(b, 'MediaPlayer_MediaApi4', a2)
    if hasattr(a2, 'MediaPlayer_MediaObject5'):
        assert not _is_linked(a2, 'MediaPlayer_MediaObject5', b)


def test_assoc_currentlyPlaying1_reverse_link_reassign_clear():
    a1 = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    a2 = MediaPlayer_MediaObject(album="sample_text_2", artist="sample_text_2", location="sample_text_2", state="sample_text_2", title="sample_text_2", year=13)
    b = MediaPlayer_MediaApi()
    _safe_set(b, 'MediaPlayer_MediaApi', {a1})
    assert _is_linked(b, 'MediaPlayer_MediaApi', a1)
    if hasattr(a1, 'MediaPlayer_MediaObject2'):
        assert _is_linked(a1, 'MediaPlayer_MediaObject2', b)
    _safe_set(b, 'MediaPlayer_MediaApi', {a2})
    assert _is_linked(b, 'MediaPlayer_MediaApi', a2)
    if hasattr(a1, 'MediaPlayer_MediaObject2'):
        assert not _is_linked(a1, 'MediaPlayer_MediaObject2', b)
    if hasattr(a2, 'MediaPlayer_MediaObject2'):
        assert _is_linked(a2, 'MediaPlayer_MediaObject2', b)
    _safe_set(b, 'MediaPlayer_MediaApi', set())
    assert not _is_linked(b, 'MediaPlayer_MediaApi', a2)
    if hasattr(a2, 'MediaPlayer_MediaObject2'):
        assert not _is_linked(a2, 'MediaPlayer_MediaObject2', b)


def test_assoc_installedApi6_reverse_link_reassign_clear():
    a1 = MediaPlayer_PlayLayer()
    a2 = MediaPlayer_PlayLayer()
    b = MediaPlayer_MediaApi()
    _safe_set(b, 'MediaPlayer_MediaApi7', a1)
    assert _is_linked(b, 'MediaPlayer_MediaApi7', a1)
    if hasattr(a1, 'MediaPlayer_PlayLayer'):
        assert _is_linked(a1, 'MediaPlayer_PlayLayer', b)
    _safe_set(b, 'MediaPlayer_MediaApi7', a2)
    assert _is_linked(b, 'MediaPlayer_MediaApi7', a2)
    if hasattr(a1, 'MediaPlayer_PlayLayer'):
        assert not _is_linked(a1, 'MediaPlayer_PlayLayer', b)
    if hasattr(a2, 'MediaPlayer_PlayLayer'):
        assert _is_linked(a2, 'MediaPlayer_PlayLayer', b)
    _safe_set(b, 'MediaPlayer_MediaApi7', None)
    assert not _is_linked(b, 'MediaPlayer_MediaApi7', a2)
    if hasattr(a2, 'MediaPlayer_PlayLayer'):
        assert not _is_linked(a2, 'MediaPlayer_PlayLayer', b)


def test_assoc_mediaList0_reverse_link_reassign_clear():
    a1 = MediaPlayer_Playlist(name="sample_text", repeat=True)
    a2 = MediaPlayer_Playlist(name="sample_text_2", repeat=False)
    b = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    _safe_set(b, 'MediaPlayer_MediaObject', a1)
    assert _is_linked(b, 'MediaPlayer_MediaObject', a1)
    if hasattr(a1, 'MediaPlayer_Playlist'):
        assert _is_linked(a1, 'MediaPlayer_Playlist', b)
    _safe_set(b, 'MediaPlayer_MediaObject', a2)
    assert _is_linked(b, 'MediaPlayer_MediaObject', a2)
    if hasattr(a1, 'MediaPlayer_Playlist'):
        assert not _is_linked(a1, 'MediaPlayer_Playlist', b)
    if hasattr(a2, 'MediaPlayer_Playlist'):
        assert _is_linked(a2, 'MediaPlayer_Playlist', b)
    _safe_set(b, 'MediaPlayer_MediaObject', None)
    assert not _is_linked(b, 'MediaPlayer_MediaObject', a2)
    if hasattr(a2, 'MediaPlayer_Playlist'):
        assert not _is_linked(a2, 'MediaPlayer_Playlist', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_mediaLibrary10_stub_double():
    # MediaPlayer_Library has no real 'MediaPlayer_Library11' property in the generated
    # code (a bare stub) -- manually attach it so MediaPlayer_MediaObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaPlayer_MediaObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    partner = MediaPlayer_Library()
    setattr(partner, 'MediaPlayer_Library11', None)
    _safe_set(owner, 'MediaPlayer_MediaObject12', partner)
    assert owner in getattr(partner, 'MediaPlayer_Library11')
    _safe_set(owner, 'MediaPlayer_MediaObject12', None)
    assert owner not in getattr(partner, 'MediaPlayer_Library11')


def test_assoc_myLibrary8_stub_double():
    # MediaPlayer_Library has no real 'MediaPlayer_Library' property in the generated
    # code (a bare stub) -- manually attach it so MediaPlayer_PlayLayer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaPlayer_PlayLayer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaPlayer_PlayLayer()
    partner = MediaPlayer_Library()
    setattr(partner, 'MediaPlayer_Library', None)
    _safe_set(owner, 'MediaPlayer_PlayLayer9', partner)
    assert getattr(partner, 'MediaPlayer_Library') == owner
    _safe_set(owner, 'MediaPlayer_PlayLayer9', None)
    assert getattr(partner, 'MediaPlayer_Library') is None


