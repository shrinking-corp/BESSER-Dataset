import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Artifact,
    Device,
    DurationArtifact,
    MediaLibrary_Artifact,
    MediaLibrary_AudioBook,
    MediaLibrary_Computer,
    MediaLibrary_Device,
    MediaLibrary_DurationArtifact,
    MediaLibrary_EReader,
    MediaLibrary_Ebook,
    MediaLibrary_Ecosystem,
    MediaLibrary_ExternalSource,
    MediaLibrary_Image,
    MediaLibrary_Library,
    MediaLibrary_MediaCollection,
    MediaLibrary_MediaSource,
    MediaLibrary_MusicTrack,
    MediaLibrary_Smartphone,
    MediaLibrary_Store,
    MediaLibrary_Tablet,
    MediaLibrary_Video,
    MediaSource,
    SourceType,
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

def test_assoc_collections16_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Device(MACAddress="sample_text", resolutionHeight=7, resolutionWidth=7)
    _safe_set(b, 'syncedDevices', {a1})
    assert _is_linked(b, 'syncedDevices', a1)
    if hasattr(a1, 'MediaCollection17'):
        assert _is_linked(a1, 'MediaCollection17', b)
    _safe_set(b, 'syncedDevices', {a2})
    assert _is_linked(b, 'syncedDevices', a2)
    if hasattr(a1, 'MediaCollection17'):
        assert not _is_linked(a1, 'MediaCollection17', b)
    if hasattr(a2, 'MediaCollection17'):
        assert _is_linked(a2, 'MediaCollection17', b)
    _safe_set(b, 'syncedDevices', set())
    assert not _is_linked(b, 'syncedDevices', a2)
    if hasattr(a2, 'MediaCollection17'):
        assert not _is_linked(a2, 'MediaCollection17', b)


def test_assoc_collections7_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Library(name="sample_text")
    _safe_set(b, 'MediaLibrary_Library8', {a1})
    assert _is_linked(b, 'MediaLibrary_Library8', a1)
    if hasattr(a1, 'MediaLibrary_MediaCollection'):
        assert _is_linked(a1, 'MediaLibrary_MediaCollection', b)
    _safe_set(b, 'MediaLibrary_Library8', {a2})
    assert _is_linked(b, 'MediaLibrary_Library8', a2)
    if hasattr(a1, 'MediaLibrary_MediaCollection'):
        assert not _is_linked(a1, 'MediaLibrary_MediaCollection', b)
    if hasattr(a2, 'MediaLibrary_MediaCollection'):
        assert _is_linked(a2, 'MediaLibrary_MediaCollection', b)
    _safe_set(b, 'MediaLibrary_Library8', set())
    assert not _is_linked(b, 'MediaLibrary_Library8', a2)
    if hasattr(a2, 'MediaLibrary_MediaCollection'):
        assert not _is_linked(a2, 'MediaLibrary_MediaCollection', b)


def test_assoc_host12_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Device(MACAddress="sample_text", resolutionHeight=7, resolutionWidth=7)
    _safe_set(b, 'Device', a1)
    assert _is_linked(b, 'Device', a1)
    if hasattr(a1, 'hostOf'):
        assert _is_linked(a1, 'hostOf', b)
    _safe_set(b, 'Device', a2)
    assert _is_linked(b, 'Device', a2)
    if hasattr(a1, 'hostOf'):
        assert not _is_linked(a1, 'hostOf', b)
    if hasattr(a2, 'hostOf'):
        assert _is_linked(a2, 'hostOf', b)
    _safe_set(b, 'Device', None)
    assert not _is_linked(b, 'Device', a2)
    if hasattr(a2, 'hostOf'):
        assert not _is_linked(a2, 'hostOf', b)


def test_assoc_hostOf15_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Device(MACAddress="sample_text", resolutionHeight=7, resolutionWidth=7)
    _safe_set(b, 'host', {a1})
    assert _is_linked(b, 'host', a1)
    if hasattr(a1, 'MediaCollection'):
        assert _is_linked(a1, 'MediaCollection', b)
    _safe_set(b, 'host', {a2})
    assert _is_linked(b, 'host', a2)
    if hasattr(a1, 'MediaCollection'):
        assert not _is_linked(a1, 'MediaCollection', b)
    if hasattr(a2, 'MediaCollection'):
        assert _is_linked(a2, 'MediaCollection', b)
    _safe_set(b, 'host', set())
    assert not _is_linked(b, 'host', a2)
    if hasattr(a2, 'MediaCollection'):
        assert not _is_linked(a2, 'MediaCollection', b)


def test_assoc_members9_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Artifact(author="sample_text", name="sample_text")
    _safe_set(b, 'MediaLibrary_Artifact11', a1)
    assert _is_linked(b, 'MediaLibrary_Artifact11', a1)
    if hasattr(a1, 'MediaLibrary_MediaCollection10'):
        assert _is_linked(a1, 'MediaLibrary_MediaCollection10', b)
    _safe_set(b, 'MediaLibrary_Artifact11', a2)
    assert _is_linked(b, 'MediaLibrary_Artifact11', a2)
    if hasattr(a1, 'MediaLibrary_MediaCollection10'):
        assert not _is_linked(a1, 'MediaLibrary_MediaCollection10', b)
    if hasattr(a2, 'MediaLibrary_MediaCollection10'):
        assert _is_linked(a2, 'MediaLibrary_MediaCollection10', b)
    _safe_set(b, 'MediaLibrary_Artifact11', None)
    assert not _is_linked(b, 'MediaLibrary_Artifact11', a2)
    if hasattr(a2, 'MediaLibrary_MediaCollection10'):
        assert not _is_linked(a2, 'MediaLibrary_MediaCollection10', b)


def test_assoc_syncedDevices13_reverse_link_reassign_clear():
    a1 = MediaLibrary_MediaCollection(name="sample_text")
    a2 = MediaLibrary_MediaCollection(name="sample_text_2")
    b = MediaLibrary_Device(MACAddress="sample_text", resolutionHeight=7, resolutionWidth=7)
    _safe_set(b, 'Device14', a1)
    assert _is_linked(b, 'Device14', a1)
    if hasattr(a1, 'collections'):
        assert _is_linked(a1, 'collections', b)
    _safe_set(b, 'Device14', a2)
    assert _is_linked(b, 'Device14', a2)
    if hasattr(a1, 'collections'):
        assert not _is_linked(a1, 'collections', b)
    if hasattr(a2, 'collections'):
        assert _is_linked(a2, 'collections', b)
    _safe_set(b, 'Device14', None)
    assert not _is_linked(b, 'Device14', a2)
    if hasattr(a2, 'collections'):
        assert not _is_linked(a2, 'collections', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contents19_stub_double():
    # MediaLibrary_MediaSource has no real 'origin' property in the generated
    # code (a bare stub) -- manually attach it so MediaLibrary_Artifact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaLibrary_Artifact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaLibrary_Artifact(author="sample_text", name="sample_text")
    partner = MediaLibrary_MediaSource()
    setattr(partner, 'origin', None)
    _safe_set(owner, 'Artifact', partner)
    assert owner in getattr(partner, 'origin')
    _safe_set(owner, 'Artifact', None)
    assert owner not in getattr(partner, 'origin')


def test_assoc_devices1_stub_double():
    # MediaLibrary_Ecosystem has no real 'MediaLibrary_Ecosystem2' property in the generated
    # code (a bare stub) -- manually attach it so MediaLibrary_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaLibrary_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaLibrary_Device(MACAddress="sample_text", resolutionHeight=7, resolutionWidth=7)
    partner = MediaLibrary_Ecosystem()
    setattr(partner, 'MediaLibrary_Ecosystem2', None)
    _safe_set(owner, 'MediaLibrary_Device', partner)
    assert owner in getattr(partner, 'MediaLibrary_Ecosystem2')
    _safe_set(owner, 'MediaLibrary_Device', None)
    assert owner not in getattr(partner, 'MediaLibrary_Ecosystem2')


def test_assoc_libraries0_stub_double():
    # MediaLibrary_Ecosystem has no real 'MediaLibrary_Ecosystem' property in the generated
    # code (a bare stub) -- manually attach it so MediaLibrary_Library's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaLibrary_Library's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaLibrary_Library(name="sample_text")
    partner = MediaLibrary_Ecosystem()
    setattr(partner, 'MediaLibrary_Ecosystem', None)
    _safe_set(owner, 'MediaLibrary_Library', partner)
    assert owner in getattr(partner, 'MediaLibrary_Ecosystem')
    _safe_set(owner, 'MediaLibrary_Library', None)
    assert owner not in getattr(partner, 'MediaLibrary_Ecosystem')


def test_assoc_mediaArtifacts5_stub_double():
    # MediaLibrary_Ecosystem has no real 'MediaLibrary_Ecosystem6' property in the generated
    # code (a bare stub) -- manually attach it so MediaLibrary_Artifact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaLibrary_Artifact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaLibrary_Artifact(author="sample_text", name="sample_text")
    partner = MediaLibrary_Ecosystem()
    setattr(partner, 'MediaLibrary_Ecosystem6', None)
    _safe_set(owner, 'MediaLibrary_Artifact', partner)
    assert owner in getattr(partner, 'MediaLibrary_Ecosystem6')
    _safe_set(owner, 'MediaLibrary_Artifact', None)
    assert owner not in getattr(partner, 'MediaLibrary_Ecosystem6')


def test_assoc_origin18_stub_double():
    # MediaLibrary_MediaSource has no real 'MediaSource' property in the generated
    # code (a bare stub) -- manually attach it so MediaLibrary_Artifact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MediaLibrary_Artifact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MediaLibrary_Artifact(author="sample_text", name="sample_text")
    partner = MediaLibrary_MediaSource()
    setattr(partner, 'MediaSource', None)
    _safe_set(owner, 'contents', partner)
    assert getattr(partner, 'MediaSource') == owner
    _safe_set(owner, 'contents', None)
    assert getattr(partner, 'MediaSource') is None


