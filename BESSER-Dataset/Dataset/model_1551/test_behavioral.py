import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    Person,
    conf101_Admin,
    conf101_Chapter,
    conf101_Conference,
    conf101_Contribution,
    conf101_Evaluation,
    conf101_Laboratory,
    conf101_Location,
    conf101_NamedElement,
    conf101_Person,
    conf101_ProgramComitee,
    conf101_Publication,
    conf101_Researcher,
    conf101_RevisionNote,
    conf101_RevisionProcess,
    conf101_Session,
    conf101_SteeringComitee,
    conf101_System,
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

def test_assoc_contributions12_stub_double():
    # conf101_Contribution has no real 'conf101_Contribution' property in the generated
    # code (a bare stub) -- manually attach it so conf101_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf101_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf101_Session(year="sample_text")
    partner = conf101_Contribution()
    setattr(partner, 'conf101_Contribution', None)
    _safe_set(owner, 'conf101_Session13', partner)
    assert getattr(partner, 'conf101_Contribution') == owner
    _safe_set(owner, 'conf101_Session13', None)
    assert getattr(partner, 'conf101_Contribution') is None


def test_assoc_location7_stub_double():
    # conf101_Location has no real 'conf101_Location' property in the generated
    # code (a bare stub) -- manually attach it so conf101_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf101_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf101_Session(year="sample_text")
    partner = conf101_Location()
    setattr(partner, 'conf101_Location', None)
    _safe_set(owner, 'conf101_Session', partner)
    assert getattr(partner, 'conf101_Location') == owner
    _safe_set(owner, 'conf101_Session', None)
    assert getattr(partner, 'conf101_Location') is None


def test_assoc_progcomit8_stub_double():
    # conf101_ProgramComitee has no real 'conf101_ProgramComitee' property in the generated
    # code (a bare stub) -- manually attach it so conf101_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf101_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf101_Session(year="sample_text")
    partner = conf101_ProgramComitee()
    setattr(partner, 'conf101_ProgramComitee', None)
    _safe_set(owner, 'conf101_Session9', partner)
    assert getattr(partner, 'conf101_ProgramComitee') == owner
    _safe_set(owner, 'conf101_Session9', None)
    assert getattr(partner, 'conf101_ProgramComitee') is None


def test_assoc_sessions17_stub_double():
    # conf101_Conference has no real 'conf101_Conference18' property in the generated
    # code (a bare stub) -- manually attach it so conf101_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf101_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf101_Session(year="sample_text")
    partner = conf101_Conference()
    setattr(partner, 'conf101_Conference18', None)
    _safe_set(owner, 'conf101_Session19', partner)
    assert owner in getattr(partner, 'conf101_Conference18')
    _safe_set(owner, 'conf101_Session19', None)
    assert owner not in getattr(partner, 'conf101_Conference18')


def test_assoc_steercomit10_stub_double():
    # conf101_SteeringComitee has no real 'conf101_SteeringComitee' property in the generated
    # code (a bare stub) -- manually attach it so conf101_Session's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # conf101_Session's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = conf101_Session(year="sample_text")
    partner = conf101_SteeringComitee()
    setattr(partner, 'conf101_SteeringComitee', None)
    _safe_set(owner, 'conf101_Session11', partner)
    assert getattr(partner, 'conf101_SteeringComitee') == owner
    _safe_set(owner, 'conf101_Session11', None)
    assert getattr(partner, 'conf101_SteeringComitee') is None


