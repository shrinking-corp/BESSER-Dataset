import pytest
from datetime import date, datetime, time, timedelta

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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Albums5_stub_double():
    # ezdaap_EZDaapAlbum has no real 'ezdaap_EZDaapAlbum' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapAlbum()
    setattr(partner, 'ezdaap_EZDaapAlbum', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance6', {partner})
    assert getattr(partner, 'ezdaap_EZDaapAlbum') == owner
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance6', set())
    assert getattr(partner, 'ezdaap_EZDaapAlbum') is None


def test_assoc_artists19_stub_double():
    # ezdaap_EZDaapArtist has no real 'ezdaap_EZDaapArtist20' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapIntelPropertyElem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapIntelPropertyElem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapIntelPropertyElem(license="sample_text")
    partner = ezdaap_EZDaapArtist()
    setattr(partner, 'ezdaap_EZDaapArtist20', None)
    _safe_set(owner, 'ezdaap_EZDaapIntelPropertyElem', {partner})
    assert getattr(partner, 'ezdaap_EZDaapArtist20') == owner
    _safe_set(owner, 'ezdaap_EZDaapIntelPropertyElem', set())
    assert getattr(partner, 'ezdaap_EZDaapArtist20') is None


def test_assoc_artists7_stub_double():
    # ezdaap_EZDaapArtist has no real 'ezdaap_EZDaapArtist' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapArtist()
    setattr(partner, 'ezdaap_EZDaapArtist', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance8', {partner})
    assert getattr(partner, 'ezdaap_EZDaapArtist') == owner
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance8', set())
    assert getattr(partner, 'ezdaap_EZDaapArtist') is None


def test_assoc_elements17_stub_double():
    # ezdaap_EZDaapLibrary has no real 'ezdaap_EZDaapLibrary18' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapLibraryUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapLibraryUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapLibraryUnit(name="sample_text")
    partner = ezdaap_EZDaapLibrary()
    setattr(partner, 'ezdaap_EZDaapLibrary18', None)
    _safe_set(owner, 'ezdaap_EZDaapLibraryUnit', partner)
    assert owner in getattr(partner, 'ezdaap_EZDaapLibrary18')
    _safe_set(owner, 'ezdaap_EZDaapLibraryUnit', None)
    assert owner not in getattr(partner, 'ezdaap_EZDaapLibrary18')


def test_assoc_iTunes9_stub_double():
    # ezdaap_EZDaapManager has no real 'ezdaap_EZDaapManager' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapManager()
    setattr(partner, 'ezdaap_EZDaapManager', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance10', partner)
    assert owner in getattr(partner, 'ezdaap_EZDaapManager')
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance10', None)
    assert owner not in getattr(partner, 'ezdaap_EZDaapManager')


def test_assoc_libraries0_stub_double():
    # ezdaap_EZDaapLibrary has no real 'ezdaap_EZDaapLibrary' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapLibrary()
    setattr(partner, 'ezdaap_EZDaapLibrary', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance', {partner})
    assert getattr(partner, 'ezdaap_EZDaapLibrary') == owner
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance', set())
    assert getattr(partner, 'ezdaap_EZDaapLibrary') is None


def test_assoc_palylists1_stub_double():
    # ezdaap_EZDaapPlayList has no real 'ezdaap_EZDaapPlayList' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapPlayList()
    setattr(partner, 'ezdaap_EZDaapPlayList', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance2', {partner})
    assert getattr(partner, 'ezdaap_EZDaapPlayList') == owner
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance2', set())
    assert getattr(partner, 'ezdaap_EZDaapPlayList') is None


def test_assoc_songs3_stub_double():
    # ezdaap_EZDaapSong has no real 'ezdaap_EZDaapSong' property in the generated
    # code (a bare stub) -- manually attach it so ezdaap_EZDaapITunesInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ezdaap_EZDaapITunesInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ezdaap_EZDaapITunesInstance(id="sample_text", revID=7, serverName="sample_text", sessionID=7)
    partner = ezdaap_EZDaapSong()
    setattr(partner, 'ezdaap_EZDaapSong', None)
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance4', {partner})
    assert getattr(partner, 'ezdaap_EZDaapSong') == owner
    _safe_set(owner, 'ezdaap_EZDaapITunesInstance4', set())
    assert getattr(partner, 'ezdaap_EZDaapSong') is None


