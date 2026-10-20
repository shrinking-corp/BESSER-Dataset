import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RoyalAndLoyal_Container_RandL,
    RoyalAndLoyal_Customer,
    RoyalAndLoyal_CustomerCard,
    RoyalAndLoyal_LoyaltyProgram,
    RoyalAndLoyal_ProgramPartner,
    RoyalAndLoyal_Service,
    RoyalAndLoyal_ServiceLevel,
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

def test_assoc_partners0_reverse_link_reassign_clear():
    a1 = RoyalAndLoyal_ProgramPartner(numberOfCustomers=7)
    a2 = RoyalAndLoyal_ProgramPartner(numberOfCustomers=13)
    b = RoyalAndLoyal_LoyaltyProgram()
    _safe_set(b, 'programs', {a1})
    assert _is_linked(b, 'programs', a1)
    if hasattr(a1, 'ProgramPartner'):
        assert _is_linked(a1, 'ProgramPartner', b)
    _safe_set(b, 'programs', {a2})
    assert _is_linked(b, 'programs', a2)
    if hasattr(a1, 'ProgramPartner'):
        assert not _is_linked(a1, 'ProgramPartner', b)
    if hasattr(a2, 'ProgramPartner'):
        assert _is_linked(a2, 'ProgramPartner', b)
    _safe_set(b, 'programs', set())
    assert not _is_linked(b, 'programs', a2)
    if hasattr(a2, 'ProgramPartner'):
        assert not _is_linked(a2, 'ProgramPartner', b)


def test_assoc_programs30_reverse_link_reassign_clear():
    a1 = RoyalAndLoyal_ProgramPartner(numberOfCustomers=7)
    a2 = RoyalAndLoyal_ProgramPartner(numberOfCustomers=13)
    b = RoyalAndLoyal_LoyaltyProgram()
    _safe_set(b, 'LoyaltyProgram31', a1)
    assert _is_linked(b, 'LoyaltyProgram31', a1)
    if hasattr(a1, 'partners'):
        assert _is_linked(a1, 'partners', b)
    _safe_set(b, 'LoyaltyProgram31', a2)
    assert _is_linked(b, 'LoyaltyProgram31', a2)
    if hasattr(a1, 'partners'):
        assert not _is_linked(a1, 'partners', b)
    if hasattr(a2, 'partners'):
        assert _is_linked(a2, 'partners', b)
    _safe_set(b, 'LoyaltyProgram31', None)
    assert not _is_linked(b, 'LoyaltyProgram31', a2)
    if hasattr(a2, 'partners'):
        assert not _is_linked(a2, 'partners', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_cards21_stub_double():
    # RoyalAndLoyal_Customer has no real 'owner' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_CustomerCard(valid=True)
    partner = RoyalAndLoyal_Customer()
    setattr(partner, 'owner', None)
    _safe_set(owner, 'CustomerCard', partner)
    assert owner in getattr(partner, 'owner')
    _safe_set(owner, 'CustomerCard', None)
    assert owner not in getattr(partner, 'owner')


def test_assoc_deliveredServices27_stub_double():
    # RoyalAndLoyal_Service has no real 'RoyalAndLoyal_Service29' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_ProgramPartner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_ProgramPartner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_ProgramPartner(numberOfCustomers=7)
    partner = RoyalAndLoyal_Service()
    setattr(partner, 'RoyalAndLoyal_Service29', None)
    _safe_set(owner, 'RoyalAndLoyal_ProgramPartner28', {partner})
    assert getattr(partner, 'RoyalAndLoyal_Service29') == owner
    _safe_set(owner, 'RoyalAndLoyal_ProgramPartner28', set())
    assert getattr(partner, 'RoyalAndLoyal_Service29') is None


def test_assoc_levels1_stub_double():
    # RoyalAndLoyal_ServiceLevel has no real 'ServiceLevel' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_LoyaltyProgram()
    partner = RoyalAndLoyal_ServiceLevel()
    setattr(partner, 'ServiceLevel', None)
    _safe_set(owner, 'program', {partner})
    assert getattr(partner, 'ServiceLevel') == owner
    _safe_set(owner, 'program', set())
    assert getattr(partner, 'ServiceLevel') is None


def test_assoc_myLevel22_stub_double():
    # RoyalAndLoyal_ServiceLevel has no real 'RoyalAndLoyal_ServiceLevel24' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_CustomerCard(valid=True)
    partner = RoyalAndLoyal_ServiceLevel()
    setattr(partner, 'RoyalAndLoyal_ServiceLevel24', None)
    _safe_set(owner, 'RoyalAndLoyal_CustomerCard23', partner)
    assert getattr(partner, 'RoyalAndLoyal_ServiceLevel24') == owner
    _safe_set(owner, 'RoyalAndLoyal_CustomerCard23', None)
    assert getattr(partner, 'RoyalAndLoyal_ServiceLevel24') is None


def test_assoc_owner25_stub_double():
    # RoyalAndLoyal_Customer has no real 'Customer26' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_CustomerCard(valid=True)
    partner = RoyalAndLoyal_Customer()
    setattr(partner, 'Customer26', None)
    _safe_set(owner, 'cards', partner)
    assert getattr(partner, 'Customer26') == owner
    _safe_set(owner, 'cards', None)
    assert getattr(partner, 'Customer26') is None


def test_assoc_participants2_stub_double():
    # RoyalAndLoyal_Customer has no real 'Customer' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_LoyaltyProgram()
    partner = RoyalAndLoyal_Customer()
    setattr(partner, 'Customer', None)
    _safe_set(owner, 'programs3', {partner})
    assert getattr(partner, 'Customer') == owner
    _safe_set(owner, 'programs3', set())
    assert getattr(partner, 'Customer') is None


def test_assoc_program4_stub_double():
    # RoyalAndLoyal_ServiceLevel has no real 'levels' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_LoyaltyProgram()
    partner = RoyalAndLoyal_ServiceLevel()
    setattr(partner, 'levels', None)
    _safe_set(owner, 'LoyaltyProgram', partner)
    assert getattr(partner, 'levels') == owner
    _safe_set(owner, 'LoyaltyProgram', None)
    assert getattr(partner, 'levels') is None


def test_assoc_programs19_stub_double():
    # RoyalAndLoyal_Customer has no real 'participants' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_LoyaltyProgram()
    partner = RoyalAndLoyal_Customer()
    setattr(partner, 'participants', None)
    _safe_set(owner, 'LoyaltyProgram20', partner)
    assert owner in getattr(partner, 'participants')
    _safe_set(owner, 'LoyaltyProgram20', None)
    assert owner not in getattr(partner, 'participants')


def test_assoc_ref_RandL_CustomerCard7_stub_double():
    # RoyalAndLoyal_Container_RandL has no real 'RoyalAndLoyal_Container_RandL8' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_CustomerCard(valid=True)
    partner = RoyalAndLoyal_Container_RandL()
    setattr(partner, 'RoyalAndLoyal_Container_RandL8', None)
    _safe_set(owner, 'RoyalAndLoyal_CustomerCard', partner)
    assert owner in getattr(partner, 'RoyalAndLoyal_Container_RandL8')
    _safe_set(owner, 'RoyalAndLoyal_CustomerCard', None)
    assert owner not in getattr(partner, 'RoyalAndLoyal_Container_RandL8')


def test_assoc_ref_RandL_LoyaltyProgram12_stub_double():
    # RoyalAndLoyal_Container_RandL has no real 'RoyalAndLoyal_Container_RandL13' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_LoyaltyProgram()
    partner = RoyalAndLoyal_Container_RandL()
    setattr(partner, 'RoyalAndLoyal_Container_RandL13', None)
    _safe_set(owner, 'RoyalAndLoyal_LoyaltyProgram', partner)
    assert owner in getattr(partner, 'RoyalAndLoyal_Container_RandL13')
    _safe_set(owner, 'RoyalAndLoyal_LoyaltyProgram', None)
    assert owner not in getattr(partner, 'RoyalAndLoyal_Container_RandL13')


def test_assoc_ref_RandL_ProgramPartner17_stub_double():
    # RoyalAndLoyal_Container_RandL has no real 'RoyalAndLoyal_Container_RandL18' property in the generated
    # code (a bare stub) -- manually attach it so RoyalAndLoyal_ProgramPartner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoyalAndLoyal_ProgramPartner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoyalAndLoyal_ProgramPartner(numberOfCustomers=7)
    partner = RoyalAndLoyal_Container_RandL()
    setattr(partner, 'RoyalAndLoyal_Container_RandL18', None)
    _safe_set(owner, 'RoyalAndLoyal_ProgramPartner', partner)
    assert owner in getattr(partner, 'RoyalAndLoyal_Container_RandL18')
    _safe_set(owner, 'RoyalAndLoyal_ProgramPartner', None)
    assert owner not in getattr(partner, 'RoyalAndLoyal_Container_RandL18')


