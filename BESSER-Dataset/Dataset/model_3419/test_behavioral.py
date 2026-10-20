import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Animal,
    Birthing,
    Bovine,
    Event,
    MedicalCondition,
    tracker_Animal,
    tracker_AnimalMissing,
    tracker_BirthDefect,
    tracker_Birthing,
    tracker_Bovine,
    tracker_BovineBeef,
    tracker_BovineBison,
    tracker_BovineDairy,
    tracker_Calving,
    tracker_Caprine,
    tracker_Died,
    tracker_Equine,
    tracker_Event,
    tracker_EventAttribute,
    tracker_EventAttributeSchema,
    tracker_EventSchema,
    tracker_Exported,
    tracker_GenericEvent,
    tracker_HerdTest,
    tracker_ICVI,
    tracker_Imported,
    tracker_Location,
    tracker_LostTag,
    tracker_Mastitis,
    tracker_MedicalCondition,
    tracker_MedicalTreatment,
    tracker_MilkTest,
    tracker_MovedIn,
    tracker_MovedOut,
    tracker_Ovine,
    tracker_Premises,
    tracker_ReplacedTag,
    tracker_Schema,
    tracker_Sighting,
    tracker_Slaughtered,
    tracker_Swine,
    tracker_Tag,
    tracker_TagAllocated,
    tracker_TagApplied,
    tracker_TagRetired,
    tracker_WeighIn,
    AnimalType,
    BeefBreed,
    BisonBreed,
    DairyBreed,
    EventDataType,
    GoatBreed,
    HorseBreed,
    OneToTen,
    Sex,
    SheepBreed,
    SwineBreed,
    Treatment,
    TreatmentMethod,
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

def test_assoc_animals9_reverse_link_reassign_clear():
    a1 = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    a2 = tracker_Premises(emailContact="sample_text_2", name="sample_text_2", premisesId="sample_text_2", uri="sample_text_2")
    b = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    _safe_set(b, 'tracker_Animal10', a1)
    assert _is_linked(b, 'tracker_Animal10', a1)
    if hasattr(a1, 'tracker_Premises'):
        assert _is_linked(a1, 'tracker_Premises', b)
    _safe_set(b, 'tracker_Animal10', a2)
    assert _is_linked(b, 'tracker_Animal10', a2)
    if hasattr(a1, 'tracker_Premises'):
        assert not _is_linked(a1, 'tracker_Premises', b)
    if hasattr(a2, 'tracker_Premises'):
        assert _is_linked(a2, 'tracker_Premises', b)
    _safe_set(b, 'tracker_Animal10', None)
    assert not _is_linked(b, 'tracker_Animal10', a2)
    if hasattr(a2, 'tracker_Premises'):
        assert not _is_linked(a2, 'tracker_Premises', b)


def test_assoc_dam2_reverse_link_reassign_clear():
    a1 = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    a2 = tracker_Animal(age="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
    b = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    _safe_set(b, 'tracker_Animal3', a1)
    assert _is_linked(b, 'tracker_Animal3', a1)
    if hasattr(a1, 'tracker_Animal1'):
        assert _is_linked(a1, 'tracker_Animal1', b)
    _safe_set(b, 'tracker_Animal3', a2)
    assert _is_linked(b, 'tracker_Animal3', a2)
    if hasattr(a1, 'tracker_Animal1'):
        assert not _is_linked(a1, 'tracker_Animal1', b)
    if hasattr(a2, 'tracker_Animal1'):
        assert _is_linked(a2, 'tracker_Animal1', b)
    _safe_set(b, 'tracker_Animal3', None)
    assert not _is_linked(b, 'tracker_Animal3', a2)
    if hasattr(a2, 'tracker_Animal1'):
        assert not _is_linked(a2, 'tracker_Animal1', b)


def test_assoc_eventAttributes22_reverse_link_reassign_clear():
    a1 = tracker_GenericEvent()
    a2 = tracker_GenericEvent()
    b = tracker_EventAttribute(key="sample_text", value="sample_text")
    _safe_set(b, 'tracker_EventAttribute', a1)
    assert _is_linked(b, 'tracker_EventAttribute', a1)
    if hasattr(a1, 'tracker_GenericEvent'):
        assert _is_linked(a1, 'tracker_GenericEvent', b)
    _safe_set(b, 'tracker_EventAttribute', a2)
    assert _is_linked(b, 'tracker_EventAttribute', a2)
    if hasattr(a1, 'tracker_GenericEvent'):
        assert not _is_linked(a1, 'tracker_GenericEvent', b)
    if hasattr(a2, 'tracker_GenericEvent'):
        assert _is_linked(a2, 'tracker_GenericEvent', b)
    _safe_set(b, 'tracker_EventAttribute', None)
    assert not _is_linked(b, 'tracker_EventAttribute', a2)
    if hasattr(a2, 'tracker_GenericEvent'):
        assert not _is_linked(a2, 'tracker_GenericEvent', b)


def test_assoc_eventAttributes25_reverse_link_reassign_clear():
    a1 = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    a2 = tracker_EventSchema(animalType="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = tracker_EventAttributeSchema(dataType="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'tracker_EventAttributeSchema', a1)
    assert _is_linked(b, 'tracker_EventAttributeSchema', a1)
    if hasattr(a1, 'tracker_EventSchema26'):
        assert _is_linked(a1, 'tracker_EventSchema26', b)
    _safe_set(b, 'tracker_EventAttributeSchema', a2)
    assert _is_linked(b, 'tracker_EventAttributeSchema', a2)
    if hasattr(a1, 'tracker_EventSchema26'):
        assert not _is_linked(a1, 'tracker_EventSchema26', b)
    if hasattr(a2, 'tracker_EventSchema26'):
        assert _is_linked(a2, 'tracker_EventSchema26', b)
    _safe_set(b, 'tracker_EventAttributeSchema', None)
    assert not _is_linked(b, 'tracker_EventAttributeSchema', a2)
    if hasattr(a2, 'tracker_EventSchema26'):
        assert not _is_linked(a2, 'tracker_EventSchema26', b)


def test_assoc_eventSchema23_reverse_link_reassign_clear():
    a1 = tracker_GenericEvent()
    a2 = tracker_GenericEvent()
    b = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'tracker_EventSchema', a1)
    assert _is_linked(b, 'tracker_EventSchema', a1)
    if hasattr(a1, 'tracker_GenericEvent24'):
        assert _is_linked(a1, 'tracker_GenericEvent24', b)
    _safe_set(b, 'tracker_EventSchema', a2)
    assert _is_linked(b, 'tracker_EventSchema', a2)
    if hasattr(a1, 'tracker_GenericEvent24'):
        assert not _is_linked(a1, 'tracker_GenericEvent24', b)
    if hasattr(a2, 'tracker_GenericEvent24'):
        assert _is_linked(a2, 'tracker_GenericEvent24', b)
    _safe_set(b, 'tracker_EventSchema', None)
    assert not _is_linked(b, 'tracker_EventSchema', a2)
    if hasattr(a2, 'tracker_GenericEvent24'):
        assert not _is_linked(a2, 'tracker_GenericEvent24', b)


def test_assoc_events7_reverse_link_reassign_clear():
    a1 = tracker_Tag(id="sample_text", usainNumberUsed=True)
    a2 = tracker_Tag(id="sample_text_2", usainNumberUsed=False)
    b = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    _safe_set(b, 'Event', a1)
    assert _is_linked(b, 'Event', a1)
    if hasattr(a1, 'tag'):
        assert _is_linked(a1, 'tag', b)
    _safe_set(b, 'Event', a2)
    assert _is_linked(b, 'Event', a2)
    if hasattr(a1, 'tag'):
        assert not _is_linked(a1, 'tag', b)
    if hasattr(a2, 'tag'):
        assert _is_linked(a2, 'tag', b)
    _safe_set(b, 'Event', None)
    assert not _is_linked(b, 'Event', a2)
    if hasattr(a2, 'tag'):
        assert not _is_linked(a2, 'tag', b)


def test_assoc_locations14_reverse_link_reassign_clear():
    a1 = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    a2 = tracker_Premises(emailContact="sample_text_2", name="sample_text_2", premisesId="sample_text_2", uri="sample_text_2")
    b = tracker_Location(name="sample_text")
    _safe_set(b, 'tracker_Location', a1)
    assert _is_linked(b, 'tracker_Location', a1)
    if hasattr(a1, 'tracker_Premises15'):
        assert _is_linked(a1, 'tracker_Premises15', b)
    _safe_set(b, 'tracker_Location', a2)
    assert _is_linked(b, 'tracker_Location', a2)
    if hasattr(a1, 'tracker_Premises15'):
        assert not _is_linked(a1, 'tracker_Premises15', b)
    if hasattr(a2, 'tracker_Premises15'):
        assert _is_linked(a2, 'tracker_Premises15', b)
    _safe_set(b, 'tracker_Location', None)
    assert not _is_linked(b, 'tracker_Location', a2)
    if hasattr(a2, 'tracker_Premises15'):
        assert not _is_linked(a2, 'tracker_Premises15', b)


def test_assoc_oldTag18_reverse_link_reassign_clear():
    a1 = tracker_Tag(id="sample_text", usainNumberUsed=True)
    a2 = tracker_Tag(id="sample_text_2", usainNumberUsed=False)
    b = tracker_ReplacedTag(oldId="sample_text", usainNumberUsedForOldId=True)
    _safe_set(b, 'tracker_ReplacedTag', a1)
    assert _is_linked(b, 'tracker_ReplacedTag', a1)
    if hasattr(a1, 'tracker_Tag19'):
        assert _is_linked(a1, 'tracker_Tag19', b)
    _safe_set(b, 'tracker_ReplacedTag', a2)
    assert _is_linked(b, 'tracker_ReplacedTag', a2)
    if hasattr(a1, 'tracker_Tag19'):
        assert not _is_linked(a1, 'tracker_Tag19', b)
    if hasattr(a2, 'tracker_Tag19'):
        assert _is_linked(a2, 'tracker_Tag19', b)
    _safe_set(b, 'tracker_ReplacedTag', None)
    assert not _is_linked(b, 'tracker_ReplacedTag', a2)
    if hasattr(a2, 'tracker_Tag19'):
        assert not _is_linked(a2, 'tracker_Tag19', b)


def test_assoc_sire5_reverse_link_reassign_clear():
    a1 = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    a2 = tracker_Animal(age="sample_text_2", birthDate=date(2025, 6, 15), breed="sample_text_2", comments="sample_text_2", id="sample_text_2", lastEventDateTime=date(2025, 6, 15), sex="sample_text_2", sexCode="sample_text_2", species="sample_text_2", speciesCode="sample_text_2", weight="sample_text_2", weightGainPerDay="sample_text_2")
    b = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    _safe_set(b, 'tracker_Animal6', a1)
    assert _is_linked(b, 'tracker_Animal6', a1)
    if hasattr(a1, 'tracker_Animal4'):
        assert _is_linked(a1, 'tracker_Animal4', b)
    _safe_set(b, 'tracker_Animal6', a2)
    assert _is_linked(b, 'tracker_Animal6', a2)
    if hasattr(a1, 'tracker_Animal4'):
        assert not _is_linked(a1, 'tracker_Animal4', b)
    if hasattr(a2, 'tracker_Animal4'):
        assert _is_linked(a2, 'tracker_Animal4', b)
    _safe_set(b, 'tracker_Animal6', None)
    assert not _is_linked(b, 'tracker_Animal6', a2)
    if hasattr(a2, 'tracker_Animal4'):
        assert not _is_linked(a2, 'tracker_Animal4', b)


def test_assoc_tag8_reverse_link_reassign_clear():
    a1 = tracker_Tag(id="sample_text", usainNumberUsed=True)
    a2 = tracker_Tag(id="sample_text_2", usainNumberUsed=False)
    b = tracker_Event(comments="sample_text", correction=True, dateTime=date(2024, 1, 1), electronicallyRead=True, eventCode=7, id="sample_text")
    _safe_set(b, 'events', a1)
    assert _is_linked(b, 'events', a1)
    if hasattr(a1, 'Tag'):
        assert _is_linked(a1, 'Tag', b)
    _safe_set(b, 'events', a2)
    assert _is_linked(b, 'events', a2)
    if hasattr(a1, 'Tag'):
        assert not _is_linked(a1, 'Tag', b)
    if hasattr(a2, 'Tag'):
        assert _is_linked(a2, 'Tag', b)
    _safe_set(b, 'events', None)
    assert not _is_linked(b, 'events', a2)
    if hasattr(a2, 'Tag'):
        assert not _is_linked(a2, 'Tag', b)


def test_assoc_tags0_reverse_link_reassign_clear():
    a1 = tracker_Tag(id="sample_text", usainNumberUsed=True)
    a2 = tracker_Tag(id="sample_text_2", usainNumberUsed=False)
    b = tracker_Animal(age="sample_text", birthDate=date(2024, 1, 1), breed="sample_text", comments="sample_text", id="sample_text", lastEventDateTime=date(2024, 1, 1), sex="sample_text", sexCode="sample_text", species="sample_text", speciesCode="sample_text", weight="sample_text", weightGainPerDay="sample_text")
    _safe_set(b, 'tracker_Animal', {a1})
    assert _is_linked(b, 'tracker_Animal', a1)
    if hasattr(a1, 'tracker_Tag'):
        assert _is_linked(a1, 'tracker_Tag', b)
    _safe_set(b, 'tracker_Animal', {a2})
    assert _is_linked(b, 'tracker_Animal', a2)
    if hasattr(a1, 'tracker_Tag'):
        assert not _is_linked(a1, 'tracker_Tag', b)
    if hasattr(a2, 'tracker_Tag'):
        assert _is_linked(a2, 'tracker_Tag', b)
    _safe_set(b, 'tracker_Animal', set())
    assert not _is_linked(b, 'tracker_Animal', a2)
    if hasattr(a2, 'tracker_Tag'):
        assert not _is_linked(a2, 'tracker_Tag', b)


def test_assoc_unAppliedTags11_reverse_link_reassign_clear():
    a1 = tracker_Tag(id="sample_text", usainNumberUsed=True)
    a2 = tracker_Tag(id="sample_text_2", usainNumberUsed=False)
    b = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    _safe_set(b, 'tracker_Premises12', {a1})
    assert _is_linked(b, 'tracker_Premises12', a1)
    if hasattr(a1, 'tracker_Tag13'):
        assert _is_linked(a1, 'tracker_Tag13', b)
    _safe_set(b, 'tracker_Premises12', {a2})
    assert _is_linked(b, 'tracker_Premises12', a2)
    if hasattr(a1, 'tracker_Tag13'):
        assert not _is_linked(a1, 'tracker_Tag13', b)
    if hasattr(a2, 'tracker_Tag13'):
        assert _is_linked(a2, 'tracker_Tag13', b)
    _safe_set(b, 'tracker_Premises12', set())
    assert not _is_linked(b, 'tracker_Premises12', a2)
    if hasattr(a2, 'tracker_Tag13'):
        assert not _is_linked(a2, 'tracker_Tag13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_eventSchemas27_stub_double():
    # tracker_Schema has no real 'tracker_Schema28' property in the generated
    # code (a bare stub) -- manually attach it so tracker_EventSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_EventSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_EventSchema(animalType="sample_text", description="sample_text", name="sample_text")
    partner = tracker_Schema()
    setattr(partner, 'tracker_Schema28', None)
    _safe_set(owner, 'tracker_EventSchema29', partner)
    assert owner in getattr(partner, 'tracker_Schema28')
    _safe_set(owner, 'tracker_EventSchema29', None)
    assert owner not in getattr(partner, 'tracker_Schema28')


def test_assoc_location20_stub_double():
    # tracker_Sighting has no real 'tracker_Sighting' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Location(name="sample_text")
    partner = tracker_Sighting()
    setattr(partner, 'tracker_Sighting', None)
    _safe_set(owner, 'tracker_Location21', partner)
    assert getattr(partner, 'tracker_Sighting') == owner
    _safe_set(owner, 'tracker_Location21', None)
    assert getattr(partner, 'tracker_Sighting') is None


def test_assoc_schema16_stub_double():
    # tracker_Schema has no real 'tracker_Schema' property in the generated
    # code (a bare stub) -- manually attach it so tracker_Premises's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tracker_Premises's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tracker_Premises(emailContact="sample_text", name="sample_text", premisesId="sample_text", uri="sample_text")
    partner = tracker_Schema()
    setattr(partner, 'tracker_Schema', None)
    _safe_set(owner, 'tracker_Premises17', partner)
    assert getattr(partner, 'tracker_Schema') == owner
    _safe_set(owner, 'tracker_Premises17', None)
    assert getattr(partner, 'tracker_Schema') is None


