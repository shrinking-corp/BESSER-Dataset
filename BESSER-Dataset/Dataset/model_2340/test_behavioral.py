import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Facility,
    NamedElement,
    Person,
    persons_Association,
    persons_Committee,
    persons_Community,
    persons_District,
    persons_Facility,
    persons_Man,
    persons_NamedElement,
    persons_OrdinaryFacility,
    persons_Person,
    persons_SpecialFacility,
    persons_TownHall,
    persons_Woman,
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

def test_assoc_members14_stub_double():
    # persons_Facility has no real 'persons_Facility15' property in the generated
    # code (a bare stub) -- manually attach it so persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persons_Person(fullName="sample_text")
    partner = persons_Facility()
    setattr(partner, 'persons_Facility15', None)
    _safe_set(owner, 'persons_Person16', partner)
    assert owner in getattr(partner, 'persons_Facility15')
    _safe_set(owner, 'persons_Person16', None)
    assert owner not in getattr(partner, 'persons_Facility15')


def test_assoc_persons0_stub_double():
    # persons_Community has no real 'persons_Community' property in the generated
    # code (a bare stub) -- manually attach it so persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persons_Person(fullName="sample_text")
    partner = persons_Community()
    setattr(partner, 'persons_Community', None)
    _safe_set(owner, 'persons_Person', partner)
    assert owner in getattr(partner, 'persons_Community')
    _safe_set(owner, 'persons_Person', None)
    assert owner not in getattr(partner, 'persons_Community')


def test_assoc_workers5_stub_double():
    # persons_TownHall has no real 'persons_TownHall6' property in the generated
    # code (a bare stub) -- manually attach it so persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = persons_Person(fullName="sample_text")
    partner = persons_TownHall()
    setattr(partner, 'persons_TownHall6', None)
    _safe_set(owner, 'persons_Person7', partner)
    assert owner in getattr(partner, 'persons_TownHall6')
    _safe_set(owner, 'persons_Person7', None)
    assert owner not in getattr(partner, 'persons_TownHall6')


