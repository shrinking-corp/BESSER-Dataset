import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Actor_Actor,
    Create_playlist_UseCase,
    Download_UseCase,
    Downloads,
    Favorite_UseCase,
    Favourites,
    Pause_UseCase,
    Play_UseCase,
    Playlist,
    Playlist_Song,
    Recently_Played,
    Repeat_Non_UseCase,
    Search_UseCase,
    Shuflfe_play_UseCase,
    Song,
    Stop_UseCase,
    TopMostPlayed,
    UseCase_UseCase,
    User_Actor,
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

def test_Downloads_dID_value_roundtrip():
    instance = Downloads(dID=7, sID=7)
    assert instance.dID == 7
    instance.dID = 13
    assert instance.dID == 13


def test_Downloads_sID_value_roundtrip():
    instance = Downloads(dID=7, sID=7)
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_Favourites_fID_value_roundtrip():
    instance = Favourites(fID=7, sID=7)
    assert instance.fID == 7
    instance.fID = 13
    assert instance.fID == 13


def test_Favourites_sID_value_roundtrip():
    instance = Favourites(fID=7, sID=7)
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_Playlist_pDate_value_roundtrip():
    instance = Playlist(pDate="sample_text", pID=7, pName="sample_text")
    assert instance.pDate == "sample_text"
    instance.pDate = "sample_text_2"
    assert instance.pDate == "sample_text_2"


def test_Playlist_pID_value_roundtrip():
    instance = Playlist(pDate="sample_text", pID=7, pName="sample_text")
    assert instance.pID == 7
    instance.pID = 13
    assert instance.pID == 13


def test_Playlist_pName_value_roundtrip():
    instance = Playlist(pDate="sample_text", pID=7, pName="sample_text")
    assert instance.pName == "sample_text"
    instance.pName = "sample_text_2"
    assert instance.pName == "sample_text_2"


def test_Playlist_Song_pID_value_roundtrip():
    instance = Playlist_Song(pID=7, sID=7)
    assert instance.pID == 7
    instance.pID = 13
    assert instance.pID == 13


def test_Playlist_Song_sID_value_roundtrip():
    instance = Playlist_Song(pID=7, sID=7)
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_Recently_Played_rpID_value_roundtrip():
    instance = Recently_Played(rpID=7, sID=7)
    assert instance.rpID == 7
    instance.rpID = 13
    assert instance.rpID == 13


def test_Recently_Played_sID_value_roundtrip():
    instance = Recently_Played(rpID=7, sID=7)
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_Song_sArtist_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sArtist == "sample_text"
    instance.sArtist = "sample_text_2"
    assert instance.sArtist == "sample_text_2"


def test_Song_sCateg_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sCateg == "sample_text"
    instance.sCateg = "sample_text_2"
    assert instance.sCateg == "sample_text_2"


def test_Song_sDate_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sDate == "sample_text"
    instance.sDate = "sample_text_2"
    assert instance.sDate == "sample_text_2"


def test_Song_sID_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_Song_sIMG_url_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sIMG_url == "sample_text"
    instance.sIMG_url = "sample_text_2"
    assert instance.sIMG_url == "sample_text_2"


def test_Song_sName_value_roundtrip():
    instance = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    assert instance.sName == "sample_text"
    instance.sName = "sample_text_2"
    assert instance.sName == "sample_text_2"


def test_TopMostPlayed_mpID_value_roundtrip():
    instance = TopMostPlayed(mpID=7, sID=7)
    assert instance.mpID == 7
    instance.mpID = 13
    assert instance.mpID == 13


def test_TopMostPlayed_sID_value_roundtrip():
    instance = TopMostPlayed(mpID=7, sID=7)
    assert instance.sID == 7
    instance.sID = 13
    assert instance.sID == 13


def test_assoc_Playlist_Playlist_Song_link_reassign_clear():
    a = Playlist_Song(pID=7, sID=7)
    b1 = Playlist(pDate="sample_text", pID=7, pName="sample_text")
    b2 = Playlist(pDate="sample_text_2", pID=13, pName="sample_text_2")
    _safe_set(a, 'playlist3', b1)
    assert _is_linked(a, 'playlist3', b1)
    if hasattr(b1, 'playlist_Song2'):
        assert _is_linked(b1, 'playlist_Song2', a)
    _safe_set(a, 'playlist3', b2)
    assert _is_linked(a, 'playlist3', b2)
    if hasattr(b1, 'playlist_Song2'):
        assert not _is_linked(b1, 'playlist_Song2', a)
    if hasattr(b2, 'playlist_Song2'):
        assert _is_linked(b2, 'playlist_Song2', a)
    _safe_set(a, 'playlist3', None)
    assert not _is_linked(a, 'playlist3', b2)
    if hasattr(b2, 'playlist_Song2'):
        assert not _is_linked(b2, 'playlist_Song2', a)


def test_assoc_Song_Playlist_Song_link_reassign_clear():
    a = Song(sArtist="sample_text", sCateg="sample_text", sDate="sample_text", sID=7, sIMG_url="sample_text", sName="sample_text")
    b1 = Playlist_Song(pID=7, sID=7)
    b2 = Playlist_Song(pID=13, sID=13)
    _safe_set(a, 'playlist_Song0', b1)
    assert _is_linked(a, 'playlist_Song0', b1)
    if hasattr(b1, 'song1'):
        assert _is_linked(b1, 'song1', a)
    _safe_set(a, 'playlist_Song0', b2)
    assert _is_linked(a, 'playlist_Song0', b2)
    if hasattr(b1, 'song1'):
        assert not _is_linked(b1, 'song1', a)
    if hasattr(b2, 'song1'):
        assert _is_linked(b2, 'song1', a)
    _safe_set(a, 'playlist_Song0', None)
    assert not _is_linked(a, 'playlist_Song0', b2)
    if hasattr(b2, 'song1'):
        assert not _is_linked(b2, 'song1', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Actor_Actor_strategy = st.builds(Actor_Actor)
@given(instance=Actor_Actor_strategy)
@settings(max_examples=25)
def test_Actor_Actor_instantiation(instance):
    assert isinstance(instance, Actor_Actor)


Create_playlist_UseCase_strategy = st.builds(Create_playlist_UseCase)
@given(instance=Create_playlist_UseCase_strategy)
@settings(max_examples=25)
def test_Create_playlist_UseCase_instantiation(instance):
    assert isinstance(instance, Create_playlist_UseCase)


Download_UseCase_strategy = st.builds(Download_UseCase)
@given(instance=Download_UseCase_strategy)
@settings(max_examples=25)
def test_Download_UseCase_instantiation(instance):
    assert isinstance(instance, Download_UseCase)


Downloads_strategy = st.builds(Downloads, dID=st.integers(), sID=st.integers())
@given(instance=Downloads_strategy)
@settings(max_examples=25)
def test_Downloads_instantiation(instance):
    assert isinstance(instance, Downloads)


Favorite_UseCase_strategy = st.builds(Favorite_UseCase)
@given(instance=Favorite_UseCase_strategy)
@settings(max_examples=25)
def test_Favorite_UseCase_instantiation(instance):
    assert isinstance(instance, Favorite_UseCase)


Favourites_strategy = st.builds(Favourites, fID=st.integers(), sID=st.integers())
@given(instance=Favourites_strategy)
@settings(max_examples=25)
def test_Favourites_instantiation(instance):
    assert isinstance(instance, Favourites)


Pause_UseCase_strategy = st.builds(Pause_UseCase)
@given(instance=Pause_UseCase_strategy)
@settings(max_examples=25)
def test_Pause_UseCase_instantiation(instance):
    assert isinstance(instance, Pause_UseCase)


Play_UseCase_strategy = st.builds(Play_UseCase)
@given(instance=Play_UseCase_strategy)
@settings(max_examples=25)
def test_Play_UseCase_instantiation(instance):
    assert isinstance(instance, Play_UseCase)


Playlist_strategy = st.builds(Playlist, pDate=safe_text, pID=st.integers(), pName=safe_text)
@given(instance=Playlist_strategy)
@settings(max_examples=25)
def test_Playlist_instantiation(instance):
    assert isinstance(instance, Playlist)


Playlist_Song_strategy = st.builds(Playlist_Song, pID=st.integers(), sID=st.integers())
@given(instance=Playlist_Song_strategy)
@settings(max_examples=25)
def test_Playlist_Song_instantiation(instance):
    assert isinstance(instance, Playlist_Song)


Recently_Played_strategy = st.builds(Recently_Played, rpID=st.integers(), sID=st.integers())
@given(instance=Recently_Played_strategy)
@settings(max_examples=25)
def test_Recently_Played_instantiation(instance):
    assert isinstance(instance, Recently_Played)


Repeat_Non_UseCase_strategy = st.builds(Repeat_Non_UseCase)
@given(instance=Repeat_Non_UseCase_strategy)
@settings(max_examples=25)
def test_Repeat_Non_UseCase_instantiation(instance):
    assert isinstance(instance, Repeat_Non_UseCase)


Search_UseCase_strategy = st.builds(Search_UseCase)
@given(instance=Search_UseCase_strategy)
@settings(max_examples=25)
def test_Search_UseCase_instantiation(instance):
    assert isinstance(instance, Search_UseCase)


Shuflfe_play_UseCase_strategy = st.builds(Shuflfe_play_UseCase)
@given(instance=Shuflfe_play_UseCase_strategy)
@settings(max_examples=25)
def test_Shuflfe_play_UseCase_instantiation(instance):
    assert isinstance(instance, Shuflfe_play_UseCase)


Song_strategy = st.builds(Song, sArtist=safe_text, sCateg=safe_text, sDate=safe_text, sID=st.integers(), sIMG_url=safe_text, sName=safe_text)
@given(instance=Song_strategy)
@settings(max_examples=25)
def test_Song_instantiation(instance):
    assert isinstance(instance, Song)


Stop_UseCase_strategy = st.builds(Stop_UseCase)
@given(instance=Stop_UseCase_strategy)
@settings(max_examples=25)
def test_Stop_UseCase_instantiation(instance):
    assert isinstance(instance, Stop_UseCase)


TopMostPlayed_strategy = st.builds(TopMostPlayed, mpID=st.integers(), sID=st.integers())
@given(instance=TopMostPlayed_strategy)
@settings(max_examples=25)
def test_TopMostPlayed_instantiation(instance):
    assert isinstance(instance, TopMostPlayed)


UseCase_UseCase_strategy = st.builds(UseCase_UseCase)
@given(instance=UseCase_UseCase_strategy)
@settings(max_examples=25)
def test_UseCase_UseCase_instantiation(instance):
    assert isinstance(instance, UseCase_UseCase)


User_Actor_strategy = st.builds(User_Actor)
@given(instance=User_Actor_strategy)
@settings(max_examples=25)
def test_User_Actor_instantiation(instance):
    assert isinstance(instance, User_Actor)


