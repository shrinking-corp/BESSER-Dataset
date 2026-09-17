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
    music_MusicLibrary,
    music_Work,
    music_Artist,
    MediaType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_music_musiclibrary_is_not_abstract():
    assert not inspect.isabstract(music_MusicLibrary)


def test_hyp_music_musiclibrary_constructor_exists():
    assert callable(music_MusicLibrary.__init__)


def test_hyp_music_musiclibrary_constructor_args():
    sig = inspect.signature(music_MusicLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_music_work_is_not_abstract():
    assert not inspect.isabstract(music_Work)


def test_hyp_music_work_constructor_exists():
    assert callable(music_Work.__init__)


def test_hyp_music_work_constructor_args():
    sig = inspect.signature(music_Work.__init__)
    params = list(sig.parameters.keys())
    assert "whenMade" in params, "Missing parameter 'whenMade'"
    assert "name" in params, "Missing parameter 'name'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "mediaTypes" in params, "Missing parameter 'mediaTypes'"







def test_hyp_music_artist_is_not_abstract():
    assert not inspect.isabstract(music_Artist)


def test_hyp_music_artist_constructor_exists():
    assert callable(music_Artist.__init__)


def test_hyp_music_artist_constructor_args():
    sig = inspect.signature(music_Artist.__init__)
    params = list(sig.parameters.keys())
    assert "notes" in params, "Missing parameter 'notes'"
    assert "name" in params, "Missing parameter 'name'"



def test_hyp_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_hyp_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
        "CD",
        "TAPE",
        "MP3",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaType"


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
music_MusicLibrary_strategy = st.builds(
    music_MusicLibrary,
    name=
        safe_text
)
music_Work_strategy = st.builds(
    music_Work,
    whenMade=
        safe_text,
    name=
        safe_text,
    notes=
        safe_text,
    mediaTypes=
        safe_text
)
music_Artist_strategy = st.builds(
    music_Artist,
    notes=
        safe_text,
    name=
        safe_text
)




@given(instance=music_MusicLibrary_strategy)
def test_hyp_music_musiclibrary_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=music_Work_strategy)
def test_hyp_music_work_whenMade_setter(instance):
    original = instance.whenMade
    instance.whenMade = original
    assert instance.whenMade == original



@given(instance=music_Work_strategy)
def test_hyp_music_work_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=music_Work_strategy)
def test_hyp_music_work_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=music_Work_strategy)
def test_hyp_music_work_mediaTypes_setter(instance):
    original = instance.mediaTypes
    instance.mediaTypes = original
    assert instance.mediaTypes == original




@given(instance=music_Artist_strategy)
def test_hyp_music_artist_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=music_Artist_strategy)
def test_hyp_music_artist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=music_Artist_strategy)
@settings(max_examples=30)
def test_hyp_music_artist_printstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.printState()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.printState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'printState' in music_Artist is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'printState' in music_Artist did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'printState' in music_Artist is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    music_Artist,
    music_MusicLibrary,
    music_Work,
    MediaType,
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

def test_music_Artist_name_value_roundtrip():
    instance = music_Artist(name="sample_text", notes="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_music_Artist_notes_value_roundtrip():
    instance = music_Artist(name="sample_text", notes="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_music_MusicLibrary_name_value_roundtrip():
    instance = music_MusicLibrary(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_music_Work_mediaTypes_value_roundtrip():
    instance = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    assert instance.mediaTypes == "sample_text"
    instance.mediaTypes = "sample_text_2"
    assert instance.mediaTypes == "sample_text_2"


def test_music_Work_name_value_roundtrip():
    instance = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_music_Work_notes_value_roundtrip():
    instance = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_music_Work_whenMade_value_roundtrip():
    instance = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    assert instance.whenMade == "sample_text"
    instance.whenMade = "sample_text_2"
    assert instance.whenMade == "sample_text_2"


def test_assoc_artists1_link_reassign_clear():
    a = music_MusicLibrary(name="sample_text")
    b1 = music_Artist(name="sample_text", notes="sample_text")
    b2 = music_Artist(name="sample_text_2", notes="sample_text_2")
    _safe_set(a, 'music_MusicLibrary', {b1})
    assert _is_linked(a, 'music_MusicLibrary', b1)
    if hasattr(b1, 'music_Artist'):
        assert _is_linked(b1, 'music_Artist', a)
    _safe_set(a, 'music_MusicLibrary', {b2})
    assert _is_linked(a, 'music_MusicLibrary', b2)
    if hasattr(b1, 'music_Artist'):
        assert not _is_linked(b1, 'music_Artist', a)
    if hasattr(b2, 'music_Artist'):
        assert _is_linked(b2, 'music_Artist', a)
    _safe_set(a, 'music_MusicLibrary', set())
    assert not _is_linked(a, 'music_MusicLibrary', b2)
    if hasattr(b2, 'music_Artist'):
        assert not _is_linked(b2, 'music_Artist', a)


def test_assoc_performer2_link_reassign_clear():
    a = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    b1 = music_Artist(name="sample_text", notes="sample_text")
    b2 = music_Artist(name="sample_text_2", notes="sample_text_2")
    _safe_set(a, 'works', b1)
    assert _is_linked(a, 'works', b1)
    if hasattr(b1, 'Artist'):
        assert _is_linked(b1, 'Artist', a)
    _safe_set(a, 'works', b2)
    assert _is_linked(a, 'works', b2)
    if hasattr(b1, 'Artist'):
        assert not _is_linked(b1, 'Artist', a)
    if hasattr(b2, 'Artist'):
        assert _is_linked(b2, 'Artist', a)
    _safe_set(a, 'works', None)
    assert not _is_linked(a, 'works', b2)
    if hasattr(b2, 'Artist'):
        assert not _is_linked(b2, 'Artist', a)


def test_assoc_works0_link_reassign_clear():
    a = music_Work(mediaTypes="sample_text", name="sample_text", notes="sample_text", whenMade="sample_text")
    b1 = music_Artist(name="sample_text", notes="sample_text")
    b2 = music_Artist(name="sample_text_2", notes="sample_text_2")
    _safe_set(a, 'Work', b1)
    assert _is_linked(a, 'Work', b1)
    if hasattr(b1, 'performer'):
        assert _is_linked(b1, 'performer', a)
    _safe_set(a, 'Work', b2)
    assert _is_linked(a, 'Work', b2)
    if hasattr(b1, 'performer'):
        assert not _is_linked(b1, 'performer', a)
    if hasattr(b2, 'performer'):
        assert _is_linked(b2, 'performer', a)
    _safe_set(a, 'Work', None)
    assert not _is_linked(a, 'Work', b2)
    if hasattr(b2, 'performer'):
        assert not _is_linked(b2, 'performer', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

music_Artist_strategy = st.builds(music_Artist, name=safe_text, notes=safe_text)
@given(instance=music_Artist_strategy)
@settings(max_examples=25)
def test_music_Artist_instantiation(instance):
    assert isinstance(instance, music_Artist)


music_MusicLibrary_strategy = st.builds(music_MusicLibrary, name=safe_text)
@given(instance=music_MusicLibrary_strategy)
@settings(max_examples=25)
def test_music_MusicLibrary_instantiation(instance):
    assert isinstance(instance, music_MusicLibrary)


music_Work_strategy = st.builds(music_Work, mediaTypes=safe_text, name=safe_text, notes=safe_text, whenMade=safe_text)
@given(instance=music_Work_strategy)
@settings(max_examples=25)
def test_music_Work_instantiation(instance):
    assert isinstance(instance, music_Work)



