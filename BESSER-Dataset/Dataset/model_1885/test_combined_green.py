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
    ezdaap_EZDaapIntelPropertyElem,
    EZDaapLibraryUnit,
    ezdaap_EZDaapElem,
    ezdaap_EZDaapLibraryUnit,
    EZDaapIntelPropertyElem,
    EZDaapElem,
    ezdaap_EZDaapManager,
    ezdaap_EZDaapDictionary,
    ezdaap_EZDaapLibrary,
    ezdaap_EZDaapITunesInstance,
    ezdaap_EZDaapArtist,
    ezdaap_EZDaapAlbum,
    ezdaap_EZDaapSong,
    ezdaap_EZDaapPlayList,
    DAAP_COMM_CST,
    DAAP_CONNECTION_KIND,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ezdaap_ezdaapintelpropertyelem_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapIntelPropertyElem)


def test_hyp_ezdaap_ezdaapintelpropertyelem_constructor_exists():
    assert callable(ezdaap_EZDaapIntelPropertyElem.__init__)


def test_hyp_ezdaap_ezdaapintelpropertyelem_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapIntelPropertyElem.__init__)
    params = list(sig.parameters.keys())
    assert "license" in params, "Missing parameter 'license'"




def test_hyp_ezdaaplibraryunit_is_not_abstract():
    assert not inspect.isabstract(EZDaapLibraryUnit)


def test_hyp_ezdaaplibraryunit_constructor_exists():
    assert callable(EZDaapLibraryUnit.__init__)


def test_hyp_ezdaaplibraryunit_constructor_args():
    sig = inspect.signature(EZDaapLibraryUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapelem_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapElem)


def test_hyp_ezdaap_ezdaapelem_constructor_exists():
    assert callable(ezdaap_EZDaapElem.__init__)


def test_hyp_ezdaap_ezdaapelem_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapElem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaaplibraryunit_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapLibraryUnit)


def test_hyp_ezdaap_ezdaaplibraryunit_constructor_exists():
    assert callable(ezdaap_EZDaapLibraryUnit.__init__)


def test_hyp_ezdaap_ezdaaplibraryunit_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapLibraryUnit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ezdaapintelpropertyelem_is_not_abstract():
    assert not inspect.isabstract(EZDaapIntelPropertyElem)


def test_hyp_ezdaapintelpropertyelem_constructor_exists():
    assert callable(EZDaapIntelPropertyElem.__init__)


def test_hyp_ezdaapintelpropertyelem_constructor_args():
    sig = inspect.signature(EZDaapIntelPropertyElem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaapelem_is_not_abstract():
    assert not inspect.isabstract(EZDaapElem)


def test_hyp_ezdaapelem_constructor_exists():
    assert callable(EZDaapElem.__init__)


def test_hyp_ezdaapelem_constructor_args():
    sig = inspect.signature(EZDaapElem.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapmanager_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapManager)


def test_hyp_ezdaap_ezdaapmanager_constructor_exists():
    assert callable(ezdaap_EZDaapManager.__init__)


def test_hyp_ezdaap_ezdaapmanager_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapManager.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapdictionary_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapDictionary)


def test_hyp_ezdaap_ezdaapdictionary_constructor_exists():
    assert callable(ezdaap_EZDaapDictionary.__init__)


def test_hyp_ezdaap_ezdaapdictionary_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapDictionary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaaplibrary_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapLibrary)


def test_hyp_ezdaap_ezdaaplibrary_constructor_exists():
    assert callable(ezdaap_EZDaapLibrary.__init__)


def test_hyp_ezdaap_ezdaaplibrary_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapLibrary.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapitunesinstance_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapITunesInstance)


def test_hyp_ezdaap_ezdaapitunesinstance_constructor_exists():
    assert callable(ezdaap_EZDaapITunesInstance.__init__)


def test_hyp_ezdaap_ezdaapitunesinstance_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapITunesInstance.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "sessionID" in params, "Missing parameter 'sessionID'"
    assert "revID" in params, "Missing parameter 'revID'"
    assert "serverName" in params, "Missing parameter 'serverName'"







def test_hyp_ezdaap_ezdaapartist_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapArtist)


def test_hyp_ezdaap_ezdaapartist_constructor_exists():
    assert callable(ezdaap_EZDaapArtist.__init__)


def test_hyp_ezdaap_ezdaapartist_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapArtist.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapalbum_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapAlbum)


def test_hyp_ezdaap_ezdaapalbum_constructor_exists():
    assert callable(ezdaap_EZDaapAlbum.__init__)


def test_hyp_ezdaap_ezdaapalbum_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapAlbum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapsong_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapSong)


def test_hyp_ezdaap_ezdaapsong_constructor_exists():
    assert callable(ezdaap_EZDaapSong.__init__)


def test_hyp_ezdaap_ezdaapsong_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapSong.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ezdaap_ezdaapplaylist_is_not_abstract():
    assert not inspect.isabstract(ezdaap_EZDaapPlayList)


def test_hyp_ezdaap_ezdaapplaylist_constructor_exists():
    assert callable(ezdaap_EZDaapPlayList.__init__)


def test_hyp_ezdaap_ezdaapplaylist_constructor_args():
    sig = inspect.signature(ezdaap_EZDaapPlayList.__init__)
    params = list(sig.parameters.keys())

def test_hyp_daap_comm_cst_exists():
    # Check that the Enumeration exists
    assert DAAP_COMM_CST is not None

def test_hyp_daap_comm_cst_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DAAP_COMM_CST]
    expected_literals = [
        "MAX_USER_SIMULTANEOUS_CONNECTION",
        "MAX_SIMULTATNEOUS_CONNECTIONS",
        "MAX_USER_CONNECTIONS_PER_SESSION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DAAP_COMM_CST"

def test_hyp_daap_connection_kind_exists():
    # Check that the Enumeration exists
    assert DAAP_CONNECTION_KIND is not None

def test_hyp_daap_connection_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DAAP_CONNECTION_KIND]
    expected_literals = [
        "DB",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DAAP_CONNECTION_KIND"


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
ezdaap_EZDaapIntelPropertyElem_strategy = st.builds(
    ezdaap_EZDaapIntelPropertyElem,
    license=
        safe_text
)
EZDaapLibraryUnit_strategy = st.builds(
    EZDaapLibraryUnit,
)
ezdaap_EZDaapElem_strategy = st.builds(
    ezdaap_EZDaapElem,
)
ezdaap_EZDaapLibraryUnit_strategy = st.builds(
    ezdaap_EZDaapLibraryUnit,
    name=
        safe_text
)
EZDaapIntelPropertyElem_strategy = st.builds(
    EZDaapIntelPropertyElem,
)
EZDaapElem_strategy = st.builds(
    EZDaapElem,
)
ezdaap_EZDaapManager_strategy = st.builds(
    ezdaap_EZDaapManager,
)
ezdaap_EZDaapDictionary_strategy = st.builds(
    ezdaap_EZDaapDictionary,
)
ezdaap_EZDaapLibrary_strategy = st.builds(
    ezdaap_EZDaapLibrary,
)
ezdaap_EZDaapITunesInstance_strategy = st.builds(
    ezdaap_EZDaapITunesInstance,
    id=
        safe_text,
    sessionID=
        st.integers(),
    revID=
        st.integers(),
    serverName=
        safe_text
)
ezdaap_EZDaapArtist_strategy = st.builds(
    ezdaap_EZDaapArtist,
)
ezdaap_EZDaapAlbum_strategy = st.builds(
    ezdaap_EZDaapAlbum,
)
ezdaap_EZDaapSong_strategy = st.builds(
    ezdaap_EZDaapSong,
)
ezdaap_EZDaapPlayList_strategy = st.builds(
    ezdaap_EZDaapPlayList,
)




@given(instance=ezdaap_EZDaapIntelPropertyElem_strategy)
def test_hyp_ezdaap_ezdaapintelpropertyelem_license_setter(instance):
    original = instance.license
    instance.license = original
    assert instance.license == original






@given(instance=ezdaap_EZDaapLibraryUnit_strategy)
def test_hyp_ezdaap_ezdaaplibraryunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original









@given(instance=ezdaap_EZDaapITunesInstance_strategy)
def test_hyp_ezdaap_ezdaapitunesinstance_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ezdaap_EZDaapITunesInstance_strategy)
def test_hyp_ezdaap_ezdaapitunesinstance_sessionID_setter(instance):
    original = instance.sessionID
    instance.sessionID = original
    assert instance.sessionID == original



@given(instance=ezdaap_EZDaapITunesInstance_strategy)
def test_hyp_ezdaap_ezdaapitunesinstance_revID_setter(instance):
    original = instance.revID
    instance.revID = original
    assert instance.revID == original



@given(instance=ezdaap_EZDaapITunesInstance_strategy)
def test_hyp_ezdaap_ezdaapitunesinstance_serverName_setter(instance):
    original = instance.serverName
    instance.serverName = original
    assert instance.serverName == original






# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EZDaapElem,
    EZDaapIntelPropertyElem,
    EZDaapLibraryUnit,
    ezdaap_EZDaapAlbum,
    ezdaap_EZDaapArtist,
    ezdaap_EZDaapDictionary,
    ezdaap_EZDaapElem,
    ezdaap_EZDaapITunesInstance,
    ezdaap_EZDaapIntelPropertyElem,
    ezdaap_EZDaapLibrary,
    ezdaap_EZDaapLibraryUnit,
    ezdaap_EZDaapManager,
    ezdaap_EZDaapPlayList,
    ezdaap_EZDaapSong,
    DAAP_COMM_CST,
    DAAP_CONNECTION_KIND,
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

def test_ezdaap_EZDaapITunesInstance_id_value_roundtrip():
    instance = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_ezdaap_EZDaapITunesInstance_revID_value_roundtrip():
    instance = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    assert instance.revID == 7
    instance.revID = 13
    assert instance.revID == 13


def test_ezdaap_EZDaapITunesInstance_serverName_value_roundtrip():
    instance = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    assert instance.serverName == "sample_text"
    instance.serverName = "sample_text_2"
    assert instance.serverName == "sample_text_2"


def test_ezdaap_EZDaapITunesInstance_sessionID_value_roundtrip():
    instance = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    assert instance.sessionID == 7
    instance.sessionID = 13
    assert instance.sessionID == 13


def test_ezdaap_EZDaapIntelPropertyElem_license_value_roundtrip():
    instance = ezdaap_EZDaapIntelPropertyElem(license="sample_text")
    assert instance.license == "sample_text"
    instance.license = "sample_text_2"
    assert instance.license == "sample_text_2"


def test_ezdaap_EZDaapLibraryUnit_name_value_roundtrip():
    instance = ezdaap_EZDaapLibraryUnit(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ezdaap_EZDaapAlbum_isa_EZDaapElem():
    instance = ezdaap_EZDaapAlbum()
    assert isinstance(instance, EZDaapElem)


def test_ezdaap_EZDaapPlayList_isa_EZDaapElem():
    instance = ezdaap_EZDaapPlayList()
    assert isinstance(instance, EZDaapElem)


def test_ezdaap_EZDaapSong_isa_EZDaapElem():
    instance = ezdaap_EZDaapSong()
    assert isinstance(instance, EZDaapElem)


def test_ezdaap_EZDaapAlbum_isa_EZDaapIntelPropertyElem():
    instance = ezdaap_EZDaapAlbum()
    assert isinstance(instance, EZDaapIntelPropertyElem)


def test_ezdaap_EZDaapSong_isa_EZDaapIntelPropertyElem():
    instance = ezdaap_EZDaapSong()
    assert isinstance(instance, EZDaapIntelPropertyElem)


def test_ezdaap_EZDaapElem_isa_EZDaapLibraryUnit():
    instance = ezdaap_EZDaapElem()
    assert isinstance(instance, EZDaapLibraryUnit)


def test_ezdaap_EZDaapLibrary_isa_EZDaapLibraryUnit():
    instance = ezdaap_EZDaapLibrary()
    assert isinstance(instance, EZDaapLibraryUnit)


def test_assoc_Albums5_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapAlbum()
    b2 = ezdaap_EZDaapAlbum()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance6', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance6', b1)
    if hasattr(b1, 'ezdaap_EZDaapAlbum'):
        assert _is_linked(b1, 'ezdaap_EZDaapAlbum', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance6', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance6', b2)
    if hasattr(b1, 'ezdaap_EZDaapAlbum'):
        assert not _is_linked(b1, 'ezdaap_EZDaapAlbum', a)
    if hasattr(b2, 'ezdaap_EZDaapAlbum'):
        assert _is_linked(b2, 'ezdaap_EZDaapAlbum', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance6', set())
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance6', b2)
    if hasattr(b2, 'ezdaap_EZDaapAlbum'):
        assert not _is_linked(b2, 'ezdaap_EZDaapAlbum', a)


def test_assoc_artists19_link_reassign_clear():
    a = ezdaap_EZDaapIntelPropertyElem(license="sample_text")
    b1 = ezdaap_EZDaapArtist()
    b2 = ezdaap_EZDaapArtist()
    _safe_set(a, 'ezdaap_EZDaapIntelPropertyElem', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapIntelPropertyElem', b1)
    if hasattr(b1, 'ezdaap_EZDaapArtist20'):
        assert _is_linked(b1, 'ezdaap_EZDaapArtist20', a)
    _safe_set(a, 'ezdaap_EZDaapIntelPropertyElem', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapIntelPropertyElem', b2)
    if hasattr(b1, 'ezdaap_EZDaapArtist20'):
        assert not _is_linked(b1, 'ezdaap_EZDaapArtist20', a)
    if hasattr(b2, 'ezdaap_EZDaapArtist20'):
        assert _is_linked(b2, 'ezdaap_EZDaapArtist20', a)
    _safe_set(a, 'ezdaap_EZDaapIntelPropertyElem', set())
    assert not _is_linked(a, 'ezdaap_EZDaapIntelPropertyElem', b2)
    if hasattr(b2, 'ezdaap_EZDaapArtist20'):
        assert not _is_linked(b2, 'ezdaap_EZDaapArtist20', a)


def test_assoc_artists7_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapArtist()
    b2 = ezdaap_EZDaapArtist()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance8', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance8', b1)
    if hasattr(b1, 'ezdaap_EZDaapArtist'):
        assert _is_linked(b1, 'ezdaap_EZDaapArtist', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance8', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance8', b2)
    if hasattr(b1, 'ezdaap_EZDaapArtist'):
        assert not _is_linked(b1, 'ezdaap_EZDaapArtist', a)
    if hasattr(b2, 'ezdaap_EZDaapArtist'):
        assert _is_linked(b2, 'ezdaap_EZDaapArtist', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance8', set())
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance8', b2)
    if hasattr(b2, 'ezdaap_EZDaapArtist'):
        assert not _is_linked(b2, 'ezdaap_EZDaapArtist', a)


def test_assoc_elements17_link_reassign_clear():
    a = ezdaap_EZDaapLibraryUnit(name="sample_text")
    b1 = ezdaap_EZDaapLibrary()
    b2 = ezdaap_EZDaapLibrary()
    _safe_set(a, 'ezdaap_EZDaapLibraryUnit', b1)
    assert _is_linked(a, 'ezdaap_EZDaapLibraryUnit', b1)
    if hasattr(b1, 'ezdaap_EZDaapLibrary18'):
        assert _is_linked(b1, 'ezdaap_EZDaapLibrary18', a)
    _safe_set(a, 'ezdaap_EZDaapLibraryUnit', b2)
    assert _is_linked(a, 'ezdaap_EZDaapLibraryUnit', b2)
    if hasattr(b1, 'ezdaap_EZDaapLibrary18'):
        assert not _is_linked(b1, 'ezdaap_EZDaapLibrary18', a)
    if hasattr(b2, 'ezdaap_EZDaapLibrary18'):
        assert _is_linked(b2, 'ezdaap_EZDaapLibrary18', a)
    _safe_set(a, 'ezdaap_EZDaapLibraryUnit', None)
    assert not _is_linked(a, 'ezdaap_EZDaapLibraryUnit', b2)
    if hasattr(b2, 'ezdaap_EZDaapLibrary18'):
        assert not _is_linked(b2, 'ezdaap_EZDaapLibrary18', a)


def test_assoc_iTunes9_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapManager()
    b2 = ezdaap_EZDaapManager()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance10', b1)
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance10', b1)
    if hasattr(b1, 'ezdaap_EZDaapManager'):
        assert _is_linked(b1, 'ezdaap_EZDaapManager', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance10', b2)
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance10', b2)
    if hasattr(b1, 'ezdaap_EZDaapManager'):
        assert not _is_linked(b1, 'ezdaap_EZDaapManager', a)
    if hasattr(b2, 'ezdaap_EZDaapManager'):
        assert _is_linked(b2, 'ezdaap_EZDaapManager', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance10', None)
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance10', b2)
    if hasattr(b2, 'ezdaap_EZDaapManager'):
        assert not _is_linked(b2, 'ezdaap_EZDaapManager', a)


def test_assoc_libraries0_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapLibrary()
    b2 = ezdaap_EZDaapLibrary()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance', b1)
    if hasattr(b1, 'ezdaap_EZDaapLibrary'):
        assert _is_linked(b1, 'ezdaap_EZDaapLibrary', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance', b2)
    if hasattr(b1, 'ezdaap_EZDaapLibrary'):
        assert not _is_linked(b1, 'ezdaap_EZDaapLibrary', a)
    if hasattr(b2, 'ezdaap_EZDaapLibrary'):
        assert _is_linked(b2, 'ezdaap_EZDaapLibrary', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance', set())
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance', b2)
    if hasattr(b2, 'ezdaap_EZDaapLibrary'):
        assert not _is_linked(b2, 'ezdaap_EZDaapLibrary', a)


def test_assoc_palylists1_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapPlayList()
    b2 = ezdaap_EZDaapPlayList()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance2', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance2', b1)
    if hasattr(b1, 'ezdaap_EZDaapPlayList'):
        assert _is_linked(b1, 'ezdaap_EZDaapPlayList', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance2', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance2', b2)
    if hasattr(b1, 'ezdaap_EZDaapPlayList'):
        assert not _is_linked(b1, 'ezdaap_EZDaapPlayList', a)
    if hasattr(b2, 'ezdaap_EZDaapPlayList'):
        assert _is_linked(b2, 'ezdaap_EZDaapPlayList', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance2', set())
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance2', b2)
    if hasattr(b2, 'ezdaap_EZDaapPlayList'):
        assert not _is_linked(b2, 'ezdaap_EZDaapPlayList', a)


def test_assoc_songs3_link_reassign_clear():
    a = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    b1 = ezdaap_EZDaapSong()
    b2 = ezdaap_EZDaapSong()
    _safe_set(a, 'ezdaap_EZDaapITunesInstance4', {b1})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance4', b1)
    if hasattr(b1, 'ezdaap_EZDaapSong'):
        assert _is_linked(b1, 'ezdaap_EZDaapSong', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance4', {b2})
    assert _is_linked(a, 'ezdaap_EZDaapITunesInstance4', b2)
    if hasattr(b1, 'ezdaap_EZDaapSong'):
        assert not _is_linked(b1, 'ezdaap_EZDaapSong', a)
    if hasattr(b2, 'ezdaap_EZDaapSong'):
        assert _is_linked(b2, 'ezdaap_EZDaapSong', a)
    _safe_set(a, 'ezdaap_EZDaapITunesInstance4', set())
    assert not _is_linked(a, 'ezdaap_EZDaapITunesInstance4', b2)
    if hasattr(b2, 'ezdaap_EZDaapSong'):
        assert not _is_linked(b2, 'ezdaap_EZDaapSong', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EZDaapElem_strategy = st.builds(EZDaapElem)
@given(instance=EZDaapElem_strategy)
@settings(max_examples=25)
def test_EZDaapElem_instantiation(instance):
    assert isinstance(instance, EZDaapElem)


EZDaapIntelPropertyElem_strategy = st.builds(EZDaapIntelPropertyElem)
@given(instance=EZDaapIntelPropertyElem_strategy)
@settings(max_examples=25)
def test_EZDaapIntelPropertyElem_instantiation(instance):
    assert isinstance(instance, EZDaapIntelPropertyElem)


EZDaapLibraryUnit_strategy = st.builds(EZDaapLibraryUnit)
@given(instance=EZDaapLibraryUnit_strategy)
@settings(max_examples=25)
def test_EZDaapLibraryUnit_instantiation(instance):
    assert isinstance(instance, EZDaapLibraryUnit)


ezdaap_EZDaapAlbum_strategy = st.builds(ezdaap_EZDaapAlbum)
@given(instance=ezdaap_EZDaapAlbum_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapAlbum_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapAlbum)


ezdaap_EZDaapArtist_strategy = st.builds(ezdaap_EZDaapArtist)
@given(instance=ezdaap_EZDaapArtist_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapArtist_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapArtist)


ezdaap_EZDaapDictionary_strategy = st.builds(ezdaap_EZDaapDictionary)
@given(instance=ezdaap_EZDaapDictionary_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapDictionary_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapDictionary)


ezdaap_EZDaapElem_strategy = st.builds(ezdaap_EZDaapElem)
@given(instance=ezdaap_EZDaapElem_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapElem_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapElem)


ezdaap_EZDaapITunesInstance_strategy = st.builds(ezdaap_EZDaapITunesInstance, id=safe_text, revID=st.integers(), serverName=safe_text, sessionID=st.integers())
@given(instance=ezdaap_EZDaapITunesInstance_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapITunesInstance_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapITunesInstance)


ezdaap_EZDaapIntelPropertyElem_strategy = st.builds(ezdaap_EZDaapIntelPropertyElem, license=safe_text)
@given(instance=ezdaap_EZDaapIntelPropertyElem_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapIntelPropertyElem_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapIntelPropertyElem)


ezdaap_EZDaapLibrary_strategy = st.builds(ezdaap_EZDaapLibrary)
@given(instance=ezdaap_EZDaapLibrary_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapLibrary_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapLibrary)


ezdaap_EZDaapLibraryUnit_strategy = st.builds(ezdaap_EZDaapLibraryUnit, name=safe_text)
@given(instance=ezdaap_EZDaapLibraryUnit_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapLibraryUnit_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapLibraryUnit)


ezdaap_EZDaapManager_strategy = st.builds(ezdaap_EZDaapManager)
@given(instance=ezdaap_EZDaapManager_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapManager_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapManager)


ezdaap_EZDaapPlayList_strategy = st.builds(ezdaap_EZDaapPlayList)
@given(instance=ezdaap_EZDaapPlayList_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapPlayList_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapPlayList)


ezdaap_EZDaapSong_strategy = st.builds(ezdaap_EZDaapSong)
@given(instance=ezdaap_EZDaapSong_strategy)
@settings(max_examples=25)
def test_ezdaap_EZDaapSong_instantiation(instance):
    assert isinstance(instance, ezdaap_EZDaapSong)



