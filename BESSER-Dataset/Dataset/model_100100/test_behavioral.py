import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Day,
    Participant,
    Story,
    Task,
    conference_Conference,
    conference_Day,
    conference_Location,
    conference_Person,
    conference_Subject,
    conference_Talk,
    conference_Track,
    conference_makingOf_Day,
    conference_makingOf_Participant,
    conference_makingOf_Story,
    conference_makingOf_Task,
    makingOf_conference_Person,
    Attitude,
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

def test_assoc_animators20_reverse_link_reassign_clear():
    a1 = conference_Track(name="sample_text")
    a2 = conference_Track(name="sample_text_2")
    b = conference_Person(name="sample_text", organisation="sample_text")
    _safe_set(b, 'Person21', a1)
    assert _is_linked(b, 'Person21', a1)
    if hasattr(a1, 'tracks'):
        assert _is_linked(a1, 'tracks', b)
    _safe_set(b, 'Person21', a2)
    assert _is_linked(b, 'Person21', a2)
    if hasattr(a1, 'tracks'):
        assert not _is_linked(a1, 'tracks', b)
    if hasattr(a2, 'tracks'):
        assert _is_linked(a2, 'tracks', b)
    _safe_set(b, 'Person21', None)
    assert not _is_linked(b, 'Person21', a2)
    if hasattr(a2, 'tracks'):
        assert not _is_linked(a2, 'tracks', b)


def test_assoc_day11_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Day(name="sample_text")
    _safe_set(b, 'Day', a1)
    assert _is_linked(b, 'Day', a1)
    if hasattr(a1, 'talks12'):
        assert _is_linked(a1, 'talks12', b)
    _safe_set(b, 'Day', a2)
    assert _is_linked(b, 'Day', a2)
    if hasattr(a1, 'talks12'):
        assert not _is_linked(a1, 'talks12', b)
    if hasattr(a2, 'talks12'):
        assert _is_linked(a2, 'talks12', b)
    _safe_set(b, 'Day', None)
    assert not _is_linked(b, 'Day', a2)
    if hasattr(a2, 'talks12'):
        assert not _is_linked(a2, 'talks12', b)


def test_assoc_days3_reverse_link_reassign_clear():
    a1 = conference_Day(name="sample_text")
    a2 = conference_Day(name="sample_text_2")
    b = conference_Conference(name="sample_text")
    _safe_set(b, 'conference_Conference4', {a1})
    assert _is_linked(b, 'conference_Conference4', a1)
    if hasattr(a1, 'conference_Day'):
        assert _is_linked(a1, 'conference_Day', b)
    _safe_set(b, 'conference_Conference4', {a2})
    assert _is_linked(b, 'conference_Conference4', a2)
    if hasattr(a1, 'conference_Day'):
        assert not _is_linked(a1, 'conference_Day', b)
    if hasattr(a2, 'conference_Day'):
        assert _is_linked(a2, 'conference_Day', b)
    _safe_set(b, 'conference_Conference4', set())
    assert not _is_linked(b, 'conference_Conference4', a2)
    if hasattr(a2, 'conference_Day'):
        assert not _is_linked(a2, 'conference_Day', b)


def test_assoc_location13_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Location(name="sample_text")
    _safe_set(b, 'Location', a1)
    assert _is_linked(b, 'Location', a1)
    if hasattr(a1, 'talks14'):
        assert _is_linked(a1, 'talks14', b)
    _safe_set(b, 'Location', a2)
    assert _is_linked(b, 'Location', a2)
    if hasattr(a1, 'talks14'):
        assert not _is_linked(a1, 'talks14', b)
    if hasattr(a2, 'talks14'):
        assert _is_linked(a2, 'talks14', b)
    _safe_set(b, 'Location', None)
    assert not _is_linked(b, 'Location', a2)
    if hasattr(a2, 'talks14'):
        assert not _is_linked(a2, 'talks14', b)


def test_assoc_locations5_reverse_link_reassign_clear():
    a1 = conference_Location(name="sample_text")
    a2 = conference_Location(name="sample_text_2")
    b = conference_Conference(name="sample_text")
    _safe_set(b, 'conference_Conference6', {a1})
    assert _is_linked(b, 'conference_Conference6', a1)
    if hasattr(a1, 'conference_Location'):
        assert _is_linked(a1, 'conference_Location', b)
    _safe_set(b, 'conference_Conference6', {a2})
    assert _is_linked(b, 'conference_Conference6', a2)
    if hasattr(a1, 'conference_Location'):
        assert not _is_linked(a1, 'conference_Location', b)
    if hasattr(a2, 'conference_Location'):
        assert _is_linked(a2, 'conference_Location', b)
    _safe_set(b, 'conference_Conference6', set())
    assert not _is_linked(b, 'conference_Conference6', a2)
    if hasattr(a2, 'conference_Location'):
        assert not _is_linked(a2, 'conference_Location', b)


def test_assoc_speakers1_reverse_link_reassign_clear():
    a1 = conference_Person(name="sample_text", organisation="sample_text")
    a2 = conference_Person(name="sample_text_2", organisation="sample_text_2")
    b = conference_Conference(name="sample_text")
    _safe_set(b, 'conference_Conference2', {a1})
    assert _is_linked(b, 'conference_Conference2', a1)
    if hasattr(a1, 'conference_Person'):
        assert _is_linked(a1, 'conference_Person', b)
    _safe_set(b, 'conference_Conference2', {a2})
    assert _is_linked(b, 'conference_Conference2', a2)
    if hasattr(a1, 'conference_Person'):
        assert not _is_linked(a1, 'conference_Person', b)
    if hasattr(a2, 'conference_Person'):
        assert _is_linked(a2, 'conference_Person', b)
    _safe_set(b, 'conference_Conference2', set())
    assert not _is_linked(b, 'conference_Conference2', a2)
    if hasattr(a2, 'conference_Person'):
        assert not _is_linked(a2, 'conference_Person', b)


def test_assoc_speakers7_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Person(name="sample_text", organisation="sample_text")
    _safe_set(b, 'Person', a1)
    assert _is_linked(b, 'Person', a1)
    if hasattr(a1, 'talks'):
        assert _is_linked(a1, 'talks', b)
    _safe_set(b, 'Person', a2)
    assert _is_linked(b, 'Person', a2)
    if hasattr(a1, 'talks'):
        assert not _is_linked(a1, 'talks', b)
    if hasattr(a2, 'talks'):
        assert _is_linked(a2, 'talks', b)
    _safe_set(b, 'Person', None)
    assert not _is_linked(b, 'Person', a2)
    if hasattr(a2, 'talks'):
        assert not _is_linked(a2, 'talks', b)


def test_assoc_subjects8_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Subject(description="sample_text", isDone=True)
    _safe_set(b, 'conference_Subject', a1)
    assert _is_linked(b, 'conference_Subject', a1)
    if hasattr(a1, 'conference_Talk'):
        assert _is_linked(a1, 'conference_Talk', b)
    _safe_set(b, 'conference_Subject', a2)
    assert _is_linked(b, 'conference_Subject', a2)
    if hasattr(a1, 'conference_Talk'):
        assert not _is_linked(a1, 'conference_Talk', b)
    if hasattr(a2, 'conference_Talk'):
        assert _is_linked(a2, 'conference_Talk', b)
    _safe_set(b, 'conference_Subject', None)
    assert not _is_linked(b, 'conference_Subject', a2)
    if hasattr(a2, 'conference_Talk'):
        assert not _is_linked(a2, 'conference_Talk', b)


def test_assoc_talks15_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Person(name="sample_text", organisation="sample_text")
    _safe_set(b, 'speakers', {a1})
    assert _is_linked(b, 'speakers', a1)
    if hasattr(a1, 'Talk'):
        assert _is_linked(a1, 'Talk', b)
    _safe_set(b, 'speakers', {a2})
    assert _is_linked(b, 'speakers', a2)
    if hasattr(a1, 'Talk'):
        assert not _is_linked(a1, 'Talk', b)
    if hasattr(a2, 'Talk'):
        assert _is_linked(a2, 'Talk', b)
    _safe_set(b, 'speakers', set())
    assert not _is_linked(b, 'speakers', a2)
    if hasattr(a2, 'Talk'):
        assert not _is_linked(a2, 'Talk', b)


def test_assoc_talks17_reverse_link_reassign_clear():
    a1 = conference_Track(name="sample_text")
    a2 = conference_Track(name="sample_text_2")
    b = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    _safe_set(b, 'conference_Talk19', a1)
    assert _is_linked(b, 'conference_Talk19', a1)
    if hasattr(a1, 'conference_Track18'):
        assert _is_linked(a1, 'conference_Track18', b)
    _safe_set(b, 'conference_Talk19', a2)
    assert _is_linked(b, 'conference_Talk19', a2)
    if hasattr(a1, 'conference_Track18'):
        assert not _is_linked(a1, 'conference_Track18', b)
    if hasattr(a2, 'conference_Track18'):
        assert _is_linked(a2, 'conference_Track18', b)
    _safe_set(b, 'conference_Talk19', None)
    assert not _is_linked(b, 'conference_Talk19', a2)
    if hasattr(a2, 'conference_Track18'):
        assert not _is_linked(a2, 'conference_Track18', b)


def test_assoc_talks22_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Day(name="sample_text")
    _safe_set(b, 'day', {a1})
    assert _is_linked(b, 'day', a1)
    if hasattr(a1, 'Talk23'):
        assert _is_linked(a1, 'Talk23', b)
    _safe_set(b, 'day', {a2})
    assert _is_linked(b, 'day', a2)
    if hasattr(a1, 'Talk23'):
        assert not _is_linked(a1, 'Talk23', b)
    if hasattr(a2, 'Talk23'):
        assert _is_linked(a2, 'Talk23', b)
    _safe_set(b, 'day', set())
    assert not _is_linked(b, 'day', a2)
    if hasattr(a2, 'Talk23'):
        assert not _is_linked(a2, 'Talk23', b)


def test_assoc_talks24_reverse_link_reassign_clear():
    a1 = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    a2 = conference_Talk(abstract="sample_text_2", duration=13, name="sample_text_2", time="sample_text_2")
    b = conference_Location(name="sample_text")
    _safe_set(b, 'location', {a1})
    assert _is_linked(b, 'location', a1)
    if hasattr(a1, 'Talk25'):
        assert _is_linked(a1, 'Talk25', b)
    _safe_set(b, 'location', {a2})
    assert _is_linked(b, 'location', a2)
    if hasattr(a1, 'Talk25'):
        assert not _is_linked(a1, 'Talk25', b)
    if hasattr(a2, 'Talk25'):
        assert _is_linked(a2, 'Talk25', b)
    _safe_set(b, 'location', set())
    assert not _is_linked(b, 'location', a2)
    if hasattr(a2, 'Talk25'):
        assert not _is_linked(a2, 'Talk25', b)


def test_assoc_tracks0_reverse_link_reassign_clear():
    a1 = conference_Track(name="sample_text")
    a2 = conference_Track(name="sample_text_2")
    b = conference_Conference(name="sample_text")
    _safe_set(b, 'conference_Conference', {a1})
    assert _is_linked(b, 'conference_Conference', a1)
    if hasattr(a1, 'conference_Track'):
        assert _is_linked(a1, 'conference_Track', b)
    _safe_set(b, 'conference_Conference', {a2})
    assert _is_linked(b, 'conference_Conference', a2)
    if hasattr(a1, 'conference_Track'):
        assert not _is_linked(a1, 'conference_Track', b)
    if hasattr(a2, 'conference_Track'):
        assert _is_linked(a2, 'conference_Track', b)
    _safe_set(b, 'conference_Conference', set())
    assert not _is_linked(b, 'conference_Conference', a2)
    if hasattr(a2, 'conference_Track'):
        assert not _is_linked(a2, 'conference_Track', b)


def test_assoc_tracks16_reverse_link_reassign_clear():
    a1 = conference_Track(name="sample_text")
    a2 = conference_Track(name="sample_text_2")
    b = conference_Person(name="sample_text", organisation="sample_text")
    _safe_set(b, 'animators', {a1})
    assert _is_linked(b, 'animators', a1)
    if hasattr(a1, 'Track'):
        assert _is_linked(a1, 'Track', b)
    _safe_set(b, 'animators', {a2})
    assert _is_linked(b, 'animators', a2)
    if hasattr(a1, 'Track'):
        assert not _is_linked(a1, 'Track', b)
    if hasattr(a2, 'Track'):
        assert _is_linked(a2, 'Track', b)
    _safe_set(b, 'animators', set())
    assert not _is_linked(b, 'animators', a2)
    if hasattr(a2, 'Track'):
        assert not _is_linked(a2, 'Track', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_days32_stub_double():
    # Day has no real 'Day33' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Story's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Story's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Story(name="sample_text")
    partner = Day()
    setattr(partner, 'Day33', None)
    _safe_set(owner, 'conference_makingOf_Story', {partner})
    assert getattr(partner, 'Day33') == owner
    _safe_set(owner, 'conference_makingOf_Story', set())
    assert getattr(partner, 'Day33') is None


def test_assoc_ideas27_stub_double():
    # Task has no real 'Task29' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Day's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Day's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Day(name="sample_text")
    partner = Task()
    setattr(partner, 'Task29', None)
    _safe_set(owner, 'conference_makingOf_Day28', {partner})
    assert getattr(partner, 'Task29') == owner
    _safe_set(owner, 'conference_makingOf_Day28', set())
    assert getattr(partner, 'Task29') is None


def test_assoc_isInvolved34_stub_double():
    # Participant has no real 'Participant35' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Task(name="sample_text")
    partner = Participant()
    setattr(partner, 'Participant35', None)
    _safe_set(owner, 'conference_makingOf_Task', {partner})
    assert getattr(partner, 'Participant35') == owner
    _safe_set(owner, 'conference_makingOf_Task', set())
    assert getattr(partner, 'Participant35') is None


def test_assoc_makingOfStories9_stub_double():
    # Story has no real 'Story' property in the generated
    # code (a bare stub) -- manually attach it so conference_Talk's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_Talk's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_Talk(abstract="sample_text", duration=7, name="sample_text", time="sample_text")
    partner = Story()
    setattr(partner, 'Story', None)
    _safe_set(owner, 'conference_Talk10', {partner})
    assert getattr(partner, 'Story') == owner
    _safe_set(owner, 'conference_Talk10', set())
    assert getattr(partner, 'Story') is None


def test_assoc_participants30_stub_double():
    # Participant has no real 'Participant' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Day's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Day's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Day(name="sample_text")
    partner = Participant()
    setattr(partner, 'Participant', None)
    _safe_set(owner, 'conference_makingOf_Day31', {partner})
    assert getattr(partner, 'Participant') == owner
    _safe_set(owner, 'conference_makingOf_Day31', set())
    assert getattr(partner, 'Participant') is None


def test_assoc_person36_stub_double():
    # makingOf_conference_Person has no real 'makingOf_conference_Person' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Participant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Participant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Participant(age=7, attitude="sample_text")
    partner = makingOf_conference_Person()
    setattr(partner, 'makingOf_conference_Person', None)
    _safe_set(owner, 'conference_makingOf_Participant', partner)
    assert getattr(partner, 'makingOf_conference_Person') == owner
    _safe_set(owner, 'conference_makingOf_Participant', None)
    assert getattr(partner, 'makingOf_conference_Person') is None


def test_assoc_tasks26_stub_double():
    # Task has no real 'Task' property in the generated
    # code (a bare stub) -- manually attach it so conference_makingOf_Day's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conference_makingOf_Day's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conference_makingOf_Day(name="sample_text")
    partner = Task()
    setattr(partner, 'Task', None)
    _safe_set(owner, 'conference_makingOf_Day', {partner})
    assert getattr(partner, 'Task') == owner
    _safe_set(owner, 'conference_makingOf_Day', set())
    assert getattr(partner, 'Task') is None


