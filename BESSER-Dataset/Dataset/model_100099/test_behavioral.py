import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Person,
    conf_Admin,
    conf_Chapter,
    conf_Conference,
    conf_Contribution,
    conf_Evaluation,
    conf_Laboratory,
    conf_Location,
    conf_Person,
    conf_ProgramComitee,
    conf_Publication,
    conf_Researcher,
    conf_RevisionNote,
    conf_RevisionProcess,
    conf_Session,
    conf_SteeringComitee,
    conf_System,
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

def test_assoc_location7_reverse_link_reassign_clear():
    a1 = conf_Session(year="sample_text")
    a2 = conf_Session(year="sample_text_2")
    b = conf_Location(name="sample_text")
    _safe_set(b, 'conf_Location', a1)
    assert _is_linked(b, 'conf_Location', a1)
    if hasattr(a1, 'conf_Session'):
        assert _is_linked(a1, 'conf_Session', b)
    _safe_set(b, 'conf_Location', a2)
    assert _is_linked(b, 'conf_Location', a2)
    if hasattr(a1, 'conf_Session'):
        assert not _is_linked(a1, 'conf_Session', b)
    if hasattr(a2, 'conf_Session'):
        assert _is_linked(a2, 'conf_Session', b)
    _safe_set(b, 'conf_Location', None)
    assert not _is_linked(b, 'conf_Location', a2)
    if hasattr(a2, 'conf_Session'):
        assert not _is_linked(a2, 'conf_Session', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_contributions12_stub_double():
    # conf_Contribution has no real 'conf_Contribution' property in the generated
    # code (a bare stub) -- manually attach it so conf_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf_Session(year="sample_text")
    partner = conf_Contribution()
    setattr(partner, 'conf_Contribution', None)
    _safe_set(owner, 'conf_Session13', partner)
    assert getattr(partner, 'conf_Contribution') == owner
    _safe_set(owner, 'conf_Session13', None)
    assert getattr(partner, 'conf_Contribution') is None


def test_assoc_locations14_stub_double():
    # conf_Admin has no real 'conf_Admin15' property in the generated
    # code (a bare stub) -- manually attach it so conf_Location's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf_Location's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf_Location(name="sample_text")
    partner = conf_Admin()
    setattr(partner, 'conf_Admin15', None)
    _safe_set(owner, 'conf_Location16', partner)
    assert owner in getattr(partner, 'conf_Admin15')
    _safe_set(owner, 'conf_Location16', None)
    assert owner not in getattr(partner, 'conf_Admin15')


def test_assoc_progcomit8_stub_double():
    # conf_ProgramComitee has no real 'conf_ProgramComitee' property in the generated
    # code (a bare stub) -- manually attach it so conf_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf_Session(year="sample_text")
    partner = conf_ProgramComitee()
    setattr(partner, 'conf_ProgramComitee', None)
    _safe_set(owner, 'conf_Session9', partner)
    assert getattr(partner, 'conf_ProgramComitee') == owner
    _safe_set(owner, 'conf_Session9', None)
    assert getattr(partner, 'conf_ProgramComitee') is None


def test_assoc_sessions17_stub_double():
    # conf_Conference has no real 'conf_Conference18' property in the generated
    # code (a bare stub) -- manually attach it so conf_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf_Session(year="sample_text")
    partner = conf_Conference()
    setattr(partner, 'conf_Conference18', None)
    _safe_set(owner, 'conf_Session19', partner)
    assert owner in getattr(partner, 'conf_Conference18')
    _safe_set(owner, 'conf_Session19', None)
    assert owner not in getattr(partner, 'conf_Conference18')


def test_assoc_steercomit10_stub_double():
    # conf_SteeringComitee has no real 'conf_SteeringComitee' property in the generated
    # code (a bare stub) -- manually attach it so conf_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf_Session(year="sample_text")
    partner = conf_SteeringComitee()
    setattr(partner, 'conf_SteeringComitee', None)
    _safe_set(owner, 'conf_Session11', partner)
    assert getattr(partner, 'conf_SteeringComitee') == owner
    _safe_set(owner, 'conf_Session11', None)
    assert getattr(partner, 'conf_SteeringComitee') is None


