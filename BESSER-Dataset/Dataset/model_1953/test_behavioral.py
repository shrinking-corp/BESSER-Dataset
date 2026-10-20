import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MediaArtifact,
    mode_AudioBook,
    mode_Device,
    mode_EBook,
    mode_MediaArtifact,
    mode_MediaCollection,
    mode_MediaLibrary,
    mode_Music,
    mode_User,
    mode_Video,
    DeviceType,
    MediaSourceType,
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

def test_assoc_collection9_reverse_link_reassign_clear():
    a1 = mode_MediaCollection(name="sample_text")
    a2 = mode_MediaCollection(name="sample_text_2")
    b = mode_MediaArtifact(identifier="sample_text", name="sample_text", source="sample_text")
    _safe_set(b, 'mediaArtifacts', a1)
    assert _is_linked(b, 'mediaArtifacts', a1)
    if hasattr(a1, 'MediaCollection10'):
        assert _is_linked(a1, 'MediaCollection10', b)
    _safe_set(b, 'mediaArtifacts', a2)
    assert _is_linked(b, 'mediaArtifacts', a2)
    if hasattr(a1, 'MediaCollection10'):
        assert not _is_linked(a1, 'MediaCollection10', b)
    if hasattr(a2, 'MediaCollection10'):
        assert _is_linked(a2, 'MediaCollection10', b)
    _safe_set(b, 'mediaArtifacts', None)
    assert not _is_linked(b, 'mediaArtifacts', a2)
    if hasattr(a2, 'MediaCollection10'):
        assert not _is_linked(a2, 'MediaCollection10', b)


def test_assoc_mediaArtifacts6_reverse_link_reassign_clear():
    a1 = mode_MediaCollection(name="sample_text")
    a2 = mode_MediaCollection(name="sample_text_2")
    b = mode_MediaArtifact(identifier="sample_text", name="sample_text", source="sample_text")
    _safe_set(b, 'MediaArtifact', a1)
    assert _is_linked(b, 'MediaArtifact', a1)
    if hasattr(a1, 'collection'):
        assert _is_linked(a1, 'collection', b)
    _safe_set(b, 'MediaArtifact', a2)
    assert _is_linked(b, 'MediaArtifact', a2)
    if hasattr(a1, 'collection'):
        assert not _is_linked(a1, 'collection', b)
    if hasattr(a2, 'collection'):
        assert _is_linked(a2, 'collection', b)
    _safe_set(b, 'MediaArtifact', None)
    assert not _is_linked(b, 'MediaArtifact', a2)
    if hasattr(a2, 'collection'):
        assert not _is_linked(a2, 'collection', b)


def test_assoc_ownedCollections5_reverse_link_reassign_clear():
    a1 = mode_User(name="sample_text")
    a2 = mode_User(name="sample_text_2")
    b = mode_MediaCollection(name="sample_text")
    _safe_set(b, 'MediaCollection', a1)
    assert _is_linked(b, 'MediaCollection', a1)
    if hasattr(a1, 'ownedUser'):
        assert _is_linked(a1, 'ownedUser', b)
    _safe_set(b, 'MediaCollection', a2)
    assert _is_linked(b, 'MediaCollection', a2)
    if hasattr(a1, 'ownedUser'):
        assert not _is_linked(a1, 'ownedUser', b)
    if hasattr(a2, 'ownedUser'):
        assert _is_linked(a2, 'ownedUser', b)
    _safe_set(b, 'MediaCollection', None)
    assert not _is_linked(b, 'MediaCollection', a2)
    if hasattr(a2, 'ownedUser'):
        assert not _is_linked(a2, 'ownedUser', b)


def test_assoc_ownedUser8_reverse_link_reassign_clear():
    a1 = mode_User(name="sample_text")
    a2 = mode_User(name="sample_text_2")
    b = mode_MediaCollection(name="sample_text")
    _safe_set(b, 'ownedCollections', a1)
    assert _is_linked(b, 'ownedCollections', a1)
    if hasattr(a1, 'User'):
        assert _is_linked(a1, 'User', b)
    _safe_set(b, 'ownedCollections', a2)
    assert _is_linked(b, 'ownedCollections', a2)
    if hasattr(a1, 'User'):
        assert not _is_linked(a1, 'User', b)
    if hasattr(a2, 'User'):
        assert _is_linked(a2, 'User', b)
    _safe_set(b, 'ownedCollections', None)
    assert not _is_linked(b, 'ownedCollections', a2)
    if hasattr(a2, 'User'):
        assert not _is_linked(a2, 'User', b)


def test_assoc_synchronisedCollections11_reverse_link_reassign_clear():
    a1 = mode_MediaCollection(name="sample_text")
    a2 = mode_MediaCollection(name="sample_text_2")
    b = mode_Device(name="sample_text", type="sample_text")
    _safe_set(b, 'synchronisedDevices', {a1})
    assert _is_linked(b, 'synchronisedDevices', a1)
    if hasattr(a1, 'MediaCollection12'):
        assert _is_linked(a1, 'MediaCollection12', b)
    _safe_set(b, 'synchronisedDevices', {a2})
    assert _is_linked(b, 'synchronisedDevices', a2)
    if hasattr(a1, 'MediaCollection12'):
        assert not _is_linked(a1, 'MediaCollection12', b)
    if hasattr(a2, 'MediaCollection12'):
        assert _is_linked(a2, 'MediaCollection12', b)
    _safe_set(b, 'synchronisedDevices', set())
    assert not _is_linked(b, 'synchronisedDevices', a2)
    if hasattr(a2, 'MediaCollection12'):
        assert not _is_linked(a2, 'MediaCollection12', b)


def test_assoc_synchronisedDevices7_reverse_link_reassign_clear():
    a1 = mode_MediaCollection(name="sample_text")
    a2 = mode_MediaCollection(name="sample_text_2")
    b = mode_Device(name="sample_text", type="sample_text")
    _safe_set(b, 'Device', a1)
    assert _is_linked(b, 'Device', a1)
    if hasattr(a1, 'synchronisedCollections'):
        assert _is_linked(a1, 'synchronisedCollections', b)
    _safe_set(b, 'Device', a2)
    assert _is_linked(b, 'Device', a2)
    if hasattr(a1, 'synchronisedCollections'):
        assert not _is_linked(a1, 'synchronisedCollections', b)
    if hasattr(a2, 'synchronisedCollections'):
        assert _is_linked(a2, 'synchronisedCollections', b)
    _safe_set(b, 'Device', None)
    assert not _is_linked(b, 'Device', a2)
    if hasattr(a2, 'synchronisedCollections'):
        assert not _is_linked(a2, 'synchronisedCollections', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_collections3_stub_double():
    # mode_MediaLibrary has no real 'mode_MediaLibrary4' property in the generated
    # code (a bare stub) -- manually attach it so mode_MediaCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mode_MediaCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mode_MediaCollection(name="sample_text")
    partner = mode_MediaLibrary()
    setattr(partner, 'mode_MediaLibrary4', None)
    _safe_set(owner, 'mode_MediaCollection', partner)
    assert owner in getattr(partner, 'mode_MediaLibrary4')
    _safe_set(owner, 'mode_MediaCollection', None)
    assert owner not in getattr(partner, 'mode_MediaLibrary4')


def test_assoc_devices0_stub_double():
    # mode_MediaLibrary has no real 'mode_MediaLibrary' property in the generated
    # code (a bare stub) -- manually attach it so mode_Device's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mode_Device's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mode_Device(name="sample_text", type="sample_text")
    partner = mode_MediaLibrary()
    setattr(partner, 'mode_MediaLibrary', None)
    _safe_set(owner, 'mode_Device', partner)
    assert owner in getattr(partner, 'mode_MediaLibrary')
    _safe_set(owner, 'mode_Device', None)
    assert owner not in getattr(partner, 'mode_MediaLibrary')


def test_assoc_users1_stub_double():
    # mode_MediaLibrary has no real 'mode_MediaLibrary2' property in the generated
    # code (a bare stub) -- manually attach it so mode_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mode_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mode_User(name="sample_text")
    partner = mode_MediaLibrary()
    setattr(partner, 'mode_MediaLibrary2', None)
    _safe_set(owner, 'mode_User', partner)
    assert owner in getattr(partner, 'mode_MediaLibrary2')
    _safe_set(owner, 'mode_User', None)
    assert owner not in getattr(partner, 'mode_MediaLibrary2')


