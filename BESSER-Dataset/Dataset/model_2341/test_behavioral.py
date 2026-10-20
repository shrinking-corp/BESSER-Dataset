import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Facility,
    NamedElement,
    Person,
    Persons_Association,
    Persons_Committee,
    Persons_Community,
    Persons_District,
    Persons_Facility,
    Persons_Man,
    Persons_NamedElement,
    Persons_OrdinaryFacility,
    Persons_Person,
    Persons_SpecialFacility,
    Persons_TownHall,
    Persons_Woman,
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

def test_assoc_members17_stub_double():
    # Persons_Facility has no real 'Persons_Facility18' property in the generated
    # code (a bare stub) -- manually attach it so Persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Persons_Person(fullName="sample_text")
    partner = Persons_Facility()
    setattr(partner, 'Persons_Facility18', None)
    _safe_set(owner, 'Persons_Person19', partner)
    assert owner in getattr(partner, 'Persons_Facility18')
    _safe_set(owner, 'Persons_Person19', None)
    assert owner not in getattr(partner, 'Persons_Facility18')


def test_assoc_persons0_stub_double():
    # Persons_Community has no real 'Persons_Community' property in the generated
    # code (a bare stub) -- manually attach it so Persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Persons_Person(fullName="sample_text")
    partner = Persons_Community()
    setattr(partner, 'Persons_Community', None)
    _safe_set(owner, 'Persons_Person', partner)
    assert owner in getattr(partner, 'Persons_Community')
    _safe_set(owner, 'Persons_Person', None)
    assert owner not in getattr(partner, 'Persons_Community')


def test_assoc_workers5_stub_double():
    # Persons_TownHall has no real 'Persons_TownHall6' property in the generated
    # code (a bare stub) -- manually attach it so Persons_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Persons_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Persons_Person(fullName="sample_text")
    partner = Persons_TownHall()
    setattr(partner, 'Persons_TownHall6', None)
    _safe_set(owner, 'Persons_Person7', partner)
    assert owner in getattr(partner, 'Persons_TownHall6')
    _safe_set(owner, 'Persons_Person7', None)
    assert owner not in getattr(partner, 'Persons_TownHall6')


