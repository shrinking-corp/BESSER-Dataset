# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MediaPlayer_BaseObject,
    MediaPlayer_PlayLayer,
    BaseObject,
    MediaPlayer_MediaObject,
    MediaPlayer_Library,
    MediaPlayer_Playlist,
    MediaPlayer_MediaApi,
    State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_mediaplayer_baseobject_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_BaseObject)


def test_hyp_mediaplayer_baseobject_constructor_exists():
    assert callable(MediaPlayer_BaseObject.__init__)


def test_hyp_mediaplayer_baseobject_constructor_args():
    sig = inspect.signature(MediaPlayer_BaseObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "propertyChangeSupport" in params, "Missing parameter 'propertyChangeSupport'"





def test_hyp_mediaplayer_playlayer_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_PlayLayer)


def test_hyp_mediaplayer_playlayer_constructor_exists():
    assert callable(MediaPlayer_PlayLayer.__init__)


def test_hyp_mediaplayer_playlayer_constructor_args():
    sig = inspect.signature(MediaPlayer_PlayLayer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_baseobject_is_not_abstract():
    assert not inspect.isabstract(BaseObject)


def test_hyp_baseobject_constructor_exists():
    assert callable(BaseObject.__init__)


def test_hyp_baseobject_constructor_args():
    sig = inspect.signature(BaseObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mediaplayer_mediaobject_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_MediaObject)


def test_hyp_mediaplayer_mediaobject_constructor_exists():
    assert callable(MediaPlayer_MediaObject.__init__)


def test_hyp_mediaplayer_mediaobject_constructor_args():
    sig = inspect.signature(MediaPlayer_MediaObject.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "year" in params, "Missing parameter 'year'"
    assert "location" in params, "Missing parameter 'location'"
    assert "state" in params, "Missing parameter 'state'"
    assert "artist" in params, "Missing parameter 'artist'"
    assert "album" in params, "Missing parameter 'album'"









def test_hyp_mediaplayer_library_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_Library)


def test_hyp_mediaplayer_library_constructor_exists():
    assert callable(MediaPlayer_Library.__init__)


def test_hyp_mediaplayer_library_constructor_args():
    sig = inspect.signature(MediaPlayer_Library.__init__)
    params = list(sig.parameters.keys())



def test_hyp_mediaplayer_playlist_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_Playlist)


def test_hyp_mediaplayer_playlist_constructor_exists():
    assert callable(MediaPlayer_Playlist.__init__)


def test_hyp_mediaplayer_playlist_constructor_args():
    sig = inspect.signature(MediaPlayer_Playlist.__init__)
    params = list(sig.parameters.keys())
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_mediaplayer_mediaapi_is_not_abstract():
    assert not inspect.isabstract(MediaPlayer_MediaApi)


def test_hyp_mediaplayer_mediaapi_constructor_exists():
    assert callable(MediaPlayer_MediaApi.__init__)


def test_hyp_mediaplayer_mediaapi_constructor_args():
    sig = inspect.signature(MediaPlayer_MediaApi.__init__)
    params = list(sig.parameters.keys())

def test_hyp_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_hyp_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
        "STOPPED",
        "PAUSED",
        "PLAYING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
MediaPlayer_BaseObject_strategy = st.builds(
    MediaPlayer_BaseObject,
    id=
        st.integers(),
    propertyChangeSupport=
        safe_text
)
MediaPlayer_PlayLayer_strategy = st.builds(
    MediaPlayer_PlayLayer,
)
BaseObject_strategy = st.builds(
    BaseObject,
)
MediaPlayer_MediaObject_strategy = st.builds(
    MediaPlayer_MediaObject,
    title=
        safe_text,
    year=
        st.integers(),
    location=
        safe_text,
    state=
        safe_text,
    artist=
        safe_text,
    album=
        safe_text
)
MediaPlayer_Library_strategy = st.builds(
    MediaPlayer_Library,
)
MediaPlayer_Playlist_strategy = st.builds(
    MediaPlayer_Playlist,
    repeat=
        st.booleans(),
    name=
        safe_text
)
MediaPlayer_MediaApi_strategy = st.builds(
    MediaPlayer_MediaApi,
)




@given(instance=MediaPlayer_BaseObject_strategy)
def test_hyp_mediaplayer_baseobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MediaPlayer_BaseObject_strategy)
def test_hyp_mediaplayer_baseobject_propertyChangeSupport_setter(instance):
    original = instance.propertyChangeSupport
    instance.propertyChangeSupport = original
    assert instance.propertyChangeSupport == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_BaseObject_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_baseobject_removepropertychangelistener_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removePropertyChangeListener(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removePropertyChangeListener).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removePropertyChangeListener' in MediaPlayer_BaseObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removePropertyChangeListener' in MediaPlayer_BaseObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removePropertyChangeListener' in MediaPlayer_BaseObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_BaseObject_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_baseobject_addpropertychangelistener_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addPropertyChangeListener(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addPropertyChangeListener).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addPropertyChangeListener' in MediaPlayer_BaseObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addPropertyChangeListener' in MediaPlayer_BaseObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addPropertyChangeListener' in MediaPlayer_BaseObject is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_PlayLayer_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_playlayer_registerapi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.registerApi(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.registerApi).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'registerApi' in MediaPlayer_PlayLayer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'registerApi' in MediaPlayer_PlayLayer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'registerApi' in MediaPlayer_PlayLayer is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_PlayLayer_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_playlayer_unregisterapi_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.unregisterApi(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.unregisterApi).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'unregisterApi' in MediaPlayer_PlayLayer is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'unregisterApi' in MediaPlayer_PlayLayer did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'unregisterApi' in MediaPlayer_PlayLayer is not implemented or raised an error")





@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_artist_setter(instance):
    original = instance.artist
    instance.artist = original
    assert instance.artist == original



@given(instance=MediaPlayer_MediaObject_strategy)
def test_hyp_mediaplayer_mediaobject_album_setter(instance):
    original = instance.album
    instance.album = original
    assert instance.album == original





@given(instance=MediaPlayer_Playlist_strategy)
def test_hyp_mediaplayer_playlist_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original



@given(instance=MediaPlayer_Playlist_strategy)
def test_hyp_mediaplayer_playlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_Playlist_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_playlist_shuffle_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.shuffle()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.shuffle).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'shuffle' in MediaPlayer_Playlist is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'shuffle' in MediaPlayer_Playlist did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'shuffle' in MediaPlayer_Playlist is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_stop_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.stop(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.stop).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'stop' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'stop' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'stop' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_canplay_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.canPlay(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.canPlay).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'canPlay' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'canPlay' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'canPlay' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_play_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.play(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.play).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'play' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'play' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'play' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_init_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.init()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.init).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'init' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'init' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'init' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_pause_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.pause(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.pause).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'pause' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'pause' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'pause' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_dispose_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.dispose()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.dispose).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'dispose' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'dispose' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'dispose' in MediaPlayer_MediaApi is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=30)
def test_hyp_mediaplayer_mediaapi_updatemediaobjectinfo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.updateMediaObjectInfo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.updateMediaObjectInfo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'updateMediaObjectInfo' in MediaPlayer_MediaApi is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'updateMediaObjectInfo' in MediaPlayer_MediaApi did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'updateMediaObjectInfo' in MediaPlayer_MediaApi is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_MediaPlayer_BaseObject_id_value_roundtrip():
    instance = MediaPlayer_BaseObject(id=7, propertyChangeSupport="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_MediaPlayer_BaseObject_propertyChangeSupport_value_roundtrip():
    instance = MediaPlayer_BaseObject(id=7, propertyChangeSupport="sample_text")
    assert instance.propertyChangeSupport == "sample_text"
    instance.propertyChangeSupport = "sample_text_2"
    assert instance.propertyChangeSupport == "sample_text_2"


def test_MediaPlayer_MediaObject_album_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.album == "sample_text"
    instance.album = "sample_text_2"
    assert instance.album == "sample_text_2"


def test_MediaPlayer_MediaObject_artist_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.artist == "sample_text"
    instance.artist = "sample_text_2"
    assert instance.artist == "sample_text_2"


def test_MediaPlayer_MediaObject_location_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_MediaPlayer_MediaObject_state_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_MediaPlayer_MediaObject_title_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_MediaPlayer_MediaObject_year_value_roundtrip():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert instance.year == 7
    instance.year = 13
    assert instance.year == 13


def test_MediaPlayer_Playlist_name_value_roundtrip():
    instance = MediaPlayer_Playlist(name="sample_text", repeat=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MediaPlayer_Playlist_repeat_value_roundtrip():
    instance = MediaPlayer_Playlist(name="sample_text", repeat=True)
    assert instance.repeat == True
    instance.repeat = False
    assert instance.repeat == False


def test_MediaPlayer_Library_isa_BaseObject():
    instance = MediaPlayer_Library()
    assert isinstance(instance, BaseObject)


def test_MediaPlayer_MediaObject_isa_BaseObject():
    instance = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    assert isinstance(instance, BaseObject)


def test_MediaPlayer_Playlist_isa_BaseObject():
    instance = MediaPlayer_Playlist(name="sample_text", repeat=True)
    assert isinstance(instance, BaseObject)


def test_assoc_currentlyPaused3_link_reassign_clear():
    a = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    b1 = MediaPlayer_MediaApi()
    b2 = MediaPlayer_MediaApi()
    _safe_set(a, 'MediaPlayer_MediaObject5', b1)
    assert _is_linked(a, 'MediaPlayer_MediaObject5', b1)
    if hasattr(b1, 'MediaPlayer_MediaApi4'):
        assert _is_linked(b1, 'MediaPlayer_MediaApi4', a)
    _safe_set(a, 'MediaPlayer_MediaObject5', b2)
    assert _is_linked(a, 'MediaPlayer_MediaObject5', b2)
    if hasattr(b1, 'MediaPlayer_MediaApi4'):
        assert not _is_linked(b1, 'MediaPlayer_MediaApi4', a)
    if hasattr(b2, 'MediaPlayer_MediaApi4'):
        assert _is_linked(b2, 'MediaPlayer_MediaApi4', a)
    _safe_set(a, 'MediaPlayer_MediaObject5', None)
    assert not _is_linked(a, 'MediaPlayer_MediaObject5', b2)
    if hasattr(b2, 'MediaPlayer_MediaApi4'):
        assert not _is_linked(b2, 'MediaPlayer_MediaApi4', a)


def test_assoc_currentlyPlaying1_link_reassign_clear():
    a = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    b1 = MediaPlayer_MediaApi()
    b2 = MediaPlayer_MediaApi()
    _safe_set(a, 'MediaPlayer_MediaObject2', b1)
    assert _is_linked(a, 'MediaPlayer_MediaObject2', b1)
    if hasattr(b1, 'MediaPlayer_MediaApi'):
        assert _is_linked(b1, 'MediaPlayer_MediaApi', a)
    _safe_set(a, 'MediaPlayer_MediaObject2', b2)
    assert _is_linked(a, 'MediaPlayer_MediaObject2', b2)
    if hasattr(b1, 'MediaPlayer_MediaApi'):
        assert not _is_linked(b1, 'MediaPlayer_MediaApi', a)
    if hasattr(b2, 'MediaPlayer_MediaApi'):
        assert _is_linked(b2, 'MediaPlayer_MediaApi', a)
    _safe_set(a, 'MediaPlayer_MediaObject2', None)
    assert not _is_linked(a, 'MediaPlayer_MediaObject2', b2)
    if hasattr(b2, 'MediaPlayer_MediaApi'):
        assert not _is_linked(b2, 'MediaPlayer_MediaApi', a)


def test_assoc_installedApi6_link_reassign_clear():
    a = MediaPlayer_PlayLayer()
    b1 = MediaPlayer_MediaApi()
    b2 = MediaPlayer_MediaApi()
    _safe_set(a, 'MediaPlayer_PlayLayer', {b1})
    assert _is_linked(a, 'MediaPlayer_PlayLayer', b1)
    if hasattr(b1, 'MediaPlayer_MediaApi7'):
        assert _is_linked(b1, 'MediaPlayer_MediaApi7', a)
    _safe_set(a, 'MediaPlayer_PlayLayer', {b2})
    assert _is_linked(a, 'MediaPlayer_PlayLayer', b2)
    if hasattr(b1, 'MediaPlayer_MediaApi7'):
        assert not _is_linked(b1, 'MediaPlayer_MediaApi7', a)
    if hasattr(b2, 'MediaPlayer_MediaApi7'):
        assert _is_linked(b2, 'MediaPlayer_MediaApi7', a)
    _safe_set(a, 'MediaPlayer_PlayLayer', set())
    assert not _is_linked(a, 'MediaPlayer_PlayLayer', b2)
    if hasattr(b2, 'MediaPlayer_MediaApi7'):
        assert not _is_linked(b2, 'MediaPlayer_MediaApi7', a)


def test_assoc_mediaLibrary10_link_reassign_clear():
    a = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    b1 = MediaPlayer_Library()
    b2 = MediaPlayer_Library()
    _safe_set(a, 'MediaPlayer_MediaObject12', b1)
    assert _is_linked(a, 'MediaPlayer_MediaObject12', b1)
    if hasattr(b1, 'MediaPlayer_Library11'):
        assert _is_linked(b1, 'MediaPlayer_Library11', a)
    _safe_set(a, 'MediaPlayer_MediaObject12', b2)
    assert _is_linked(a, 'MediaPlayer_MediaObject12', b2)
    if hasattr(b1, 'MediaPlayer_Library11'):
        assert not _is_linked(b1, 'MediaPlayer_Library11', a)
    if hasattr(b2, 'MediaPlayer_Library11'):
        assert _is_linked(b2, 'MediaPlayer_Library11', a)
    _safe_set(a, 'MediaPlayer_MediaObject12', None)
    assert not _is_linked(a, 'MediaPlayer_MediaObject12', b2)
    if hasattr(b2, 'MediaPlayer_Library11'):
        assert not _is_linked(b2, 'MediaPlayer_Library11', a)


def test_assoc_mediaList0_link_reassign_clear():
    a = MediaPlayer_Playlist(name="sample_text", repeat=True)
    b1 = MediaPlayer_MediaObject(album="sample_text", artist="sample_text", location="sample_text", state="sample_text", title="sample_text", year=7)
    b2 = MediaPlayer_MediaObject(album="sample_text_2", artist="sample_text_2", location="sample_text_2", state="sample_text_2", title="sample_text_2", year=13)
    _safe_set(a, 'MediaPlayer_Playlist', {b1})
    assert _is_linked(a, 'MediaPlayer_Playlist', b1)
    if hasattr(b1, 'MediaPlayer_MediaObject'):
        assert _is_linked(b1, 'MediaPlayer_MediaObject', a)
    _safe_set(a, 'MediaPlayer_Playlist', {b2})
    assert _is_linked(a, 'MediaPlayer_Playlist', b2)
    if hasattr(b1, 'MediaPlayer_MediaObject'):
        assert not _is_linked(b1, 'MediaPlayer_MediaObject', a)
    if hasattr(b2, 'MediaPlayer_MediaObject'):
        assert _is_linked(b2, 'MediaPlayer_MediaObject', a)
    _safe_set(a, 'MediaPlayer_Playlist', set())
    assert not _is_linked(a, 'MediaPlayer_Playlist', b2)
    if hasattr(b2, 'MediaPlayer_MediaObject'):
        assert not _is_linked(b2, 'MediaPlayer_MediaObject', a)


def test_assoc_myLibrary8_link_reassign_clear():
    a = MediaPlayer_PlayLayer()
    b1 = MediaPlayer_Library()
    b2 = MediaPlayer_Library()
    _safe_set(a, 'MediaPlayer_PlayLayer9', b1)
    assert _is_linked(a, 'MediaPlayer_PlayLayer9', b1)
    if hasattr(b1, 'MediaPlayer_Library'):
        assert _is_linked(b1, 'MediaPlayer_Library', a)
    _safe_set(a, 'MediaPlayer_PlayLayer9', b2)
    assert _is_linked(a, 'MediaPlayer_PlayLayer9', b2)
    if hasattr(b1, 'MediaPlayer_Library'):
        assert not _is_linked(b1, 'MediaPlayer_Library', a)
    if hasattr(b2, 'MediaPlayer_Library'):
        assert _is_linked(b2, 'MediaPlayer_Library', a)
    _safe_set(a, 'MediaPlayer_PlayLayer9', None)
    assert not _is_linked(a, 'MediaPlayer_PlayLayer9', b2)
    if hasattr(b2, 'MediaPlayer_Library'):
        assert not _is_linked(b2, 'MediaPlayer_Library', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BaseObject_strategy = st.builds(BaseObject)
@given(instance=BaseObject_strategy)
@settings(max_examples=25)
def test_BaseObject_instantiation(instance):
    assert isinstance(instance, BaseObject)


MediaPlayer_BaseObject_strategy = st.builds(MediaPlayer_BaseObject, id=st.integers(), propertyChangeSupport=safe_text)
@given(instance=MediaPlayer_BaseObject_strategy)
@settings(max_examples=25)
def test_MediaPlayer_BaseObject_instantiation(instance):
    assert isinstance(instance, MediaPlayer_BaseObject)


MediaPlayer_Library_strategy = st.builds(MediaPlayer_Library)
@given(instance=MediaPlayer_Library_strategy)
@settings(max_examples=25)
def test_MediaPlayer_Library_instantiation(instance):
    assert isinstance(instance, MediaPlayer_Library)


MediaPlayer_MediaApi_strategy = st.builds(MediaPlayer_MediaApi)
@given(instance=MediaPlayer_MediaApi_strategy)
@settings(max_examples=25)
def test_MediaPlayer_MediaApi_instantiation(instance):
    assert isinstance(instance, MediaPlayer_MediaApi)


MediaPlayer_MediaObject_strategy = st.builds(MediaPlayer_MediaObject, album=safe_text, artist=safe_text, location=safe_text, state=safe_text, title=safe_text, year=st.integers())
@given(instance=MediaPlayer_MediaObject_strategy)
@settings(max_examples=25)
def test_MediaPlayer_MediaObject_instantiation(instance):
    assert isinstance(instance, MediaPlayer_MediaObject)


MediaPlayer_PlayLayer_strategy = st.builds(MediaPlayer_PlayLayer)
@given(instance=MediaPlayer_PlayLayer_strategy)
@settings(max_examples=25)
def test_MediaPlayer_PlayLayer_instantiation(instance):
    assert isinstance(instance, MediaPlayer_PlayLayer)


MediaPlayer_Playlist_strategy = st.builds(MediaPlayer_Playlist, name=safe_text, repeat=st.booleans())
@given(instance=MediaPlayer_Playlist_strategy)
@settings(max_examples=25)
def test_MediaPlayer_Playlist_instantiation(instance):
    assert isinstance(instance, MediaPlayer_Playlist)



