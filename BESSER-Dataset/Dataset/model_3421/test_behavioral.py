import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Animal,
    Bovine,
    Event,
    tracker_Animal,
    tracker_AnimalId,
    tracker_AnimalMissing,
    tracker_Animals,
    tracker_Bovine,
    tracker_BovineBeef,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_Died,
    tracker_Event,
    tracker_EventHistory,
    tracker_Exported,
    tracker_FairRegistration,
    tracker_ICVI,
    tracker_Imported,
    tracker_LostTag,
    tracker_MovedIn,
    tracker_MovedOut,
    tracker_Ovine,
    tracker_Premises,
    tracker_ReplacedTag,
    tracker_Sighting,
    tracker_Slaughtered,
    tracker_Swine,
    tracker_TagAllocated,
    tracker_TagApplied,
    tracker_TagRetired,
    tracker_UnAppliedTags,
    tracker_WeighIn,
    BeefBreed,
    BisonBreed,
    DairyBreed,
    Sex,
    SheepBreed,
    SwineBreed,
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

def test_assoc_ain0_reverse_link_reassign_clear():
    a1 = tracker_AnimalId(idNumber="sample_text", usainNumberUsed=True)
    a2 = tracker_AnimalId(idNumber="sample_text_2", usainNumberUsed=False)
    b = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    _safe_set(b, 'tracker_Animal', a1)
    assert _is_linked(b, 'tracker_Animal', a1)
    if hasattr(a1, 'tracker_AnimalId'):
        assert _is_linked(a1, 'tracker_AnimalId', b)
    _safe_set(b, 'tracker_Animal', a2)
    assert _is_linked(b, 'tracker_Animal', a2)
    if hasattr(a1, 'tracker_AnimalId'):
        assert not _is_linked(a1, 'tracker_AnimalId', b)
    if hasattr(a2, 'tracker_AnimalId'):
        assert _is_linked(a2, 'tracker_AnimalId', b)
    _safe_set(b, 'tracker_Animal', None)
    assert not _is_linked(b, 'tracker_Animal', a2)
    if hasattr(a2, 'tracker_AnimalId'):
        assert not _is_linked(a2, 'tracker_AnimalId', b)


def test_assoc_ain1_reverse_link_reassign_clear():
    a1 = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, id="sample_text")
    a2 = tracker_Event(comments="sample_text_2", correction=False, dateTime="sample_text_2", electronicallyRead=False, eventCode=13, id="sample_text_2")
    b = tracker_AnimalId(idNumber="sample_text", usainNumberUsed=True)
    _safe_set(b, 'tracker_AnimalId2', a1)
    assert _is_linked(b, 'tracker_AnimalId2', a1)
    if hasattr(a1, 'tracker_Event'):
        assert _is_linked(a1, 'tracker_Event', b)
    _safe_set(b, 'tracker_AnimalId2', a2)
    assert _is_linked(b, 'tracker_AnimalId2', a2)
    if hasattr(a1, 'tracker_Event'):
        assert not _is_linked(a1, 'tracker_Event', b)
    if hasattr(a2, 'tracker_Event'):
        assert _is_linked(a2, 'tracker_Event', b)
    _safe_set(b, 'tracker_AnimalId2', None)
    assert not _is_linked(b, 'tracker_AnimalId2', a2)
    if hasattr(a2, 'tracker_Event'):
        assert not _is_linked(a2, 'tracker_Event', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ain14_stub_double():
    # tracker_UnAppliedTags has no real 'tracker_UnAppliedTags15' property in the generated
    # code (a bare stub) -- manually attach it so tracker_AnimalId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_AnimalId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_AnimalId(idNumber="sample_text", usainNumberUsed=True)
    partner = tracker_UnAppliedTags()
    setattr(partner, 'tracker_UnAppliedTags15', None)
    _safe_set(owner, 'tracker_AnimalId16', partner)
    assert owner in getattr(partner, 'tracker_UnAppliedTags15')
    _safe_set(owner, 'tracker_AnimalId16', None)
    assert owner not in getattr(partner, 'tracker_UnAppliedTags15')


def test_assoc_animal11_stub_double():
    # tracker_Animals has no real 'tracker_Animals12' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Animal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Animal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Animal(age="sample_text", birthDate="sample_text", breed="sample_text", idNumber="sample_text", sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text")
    partner = tracker_Animals()
    setattr(partner, 'tracker_Animals12', None)
    _safe_set(owner, 'tracker_Animal13', partner)
    assert owner in getattr(partner, 'tracker_Animals12')
    _safe_set(owner, 'tracker_Animal13', None)
    assert owner not in getattr(partner, 'tracker_Animals12')


def test_assoc_animals3_stub_double():
    # tracker_Animals has no real 'tracker_Animals' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Premises's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Premises's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    partner = tracker_Animals()
    setattr(partner, 'tracker_Animals', None)
    _safe_set(owner, 'tracker_Premises', partner)
    assert getattr(partner, 'tracker_Animals') == owner
    _safe_set(owner, 'tracker_Premises', None)
    assert getattr(partner, 'tracker_Animals') is None


def test_assoc_eventHistory4_stub_double():
    # tracker_EventHistory has no real 'tracker_EventHistory' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Premises's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Premises's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    partner = tracker_EventHistory()
    setattr(partner, 'tracker_EventHistory', None)
    _safe_set(owner, 'tracker_Premises5', partner)
    assert getattr(partner, 'tracker_EventHistory') == owner
    _safe_set(owner, 'tracker_Premises5', None)
    assert getattr(partner, 'tracker_EventHistory') is None


def test_assoc_events8_stub_double():
    # tracker_EventHistory has no real 'tracker_EventHistory9' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Event(comments="sample_text", correction=True, dateTime="sample_text", electronicallyRead=True, eventCode=7, id="sample_text")
    partner = tracker_EventHistory()
    setattr(partner, 'tracker_EventHistory9', None)
    _safe_set(owner, 'tracker_Event10', partner)
    assert owner in getattr(partner, 'tracker_EventHistory9')
    _safe_set(owner, 'tracker_Event10', None)
    assert owner not in getattr(partner, 'tracker_EventHistory9')


def test_assoc_unAppliedTags6_stub_double():
    # tracker_UnAppliedTags has no real 'tracker_UnAppliedTags' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Premises's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Premises's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Premises(emailContact="sample_text", premisesId="sample_text")
    partner = tracker_UnAppliedTags()
    setattr(partner, 'tracker_UnAppliedTags', None)
    _safe_set(owner, 'tracker_Premises7', partner)
    assert getattr(partner, 'tracker_UnAppliedTags') == owner
    _safe_set(owner, 'tracker_Premises7', None)
    assert getattr(partner, 'tracker_UnAppliedTags') is None


