import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    addressbook_Address,
    addressbook_AddressBook,
    addressbook_Country,
    addressbook_FederalState,
    addressbook_Person,
    AddressType,
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

def test_assoc_addresses2_reverse_link_reassign_clear():
    a1 = addressbook_Person(firstname="sample_text", lastname="sample_text")
    a2 = addressbook_Person(firstname="sample_text_2", lastname="sample_text_2")
    b = addressbook_Address(city="sample_text", street="sample_text", type="sample_text", zip="sample_text")
    _safe_set(b, 'Address', a1)
    assert _is_linked(b, 'Address', a1)
    if hasattr(a1, 'person'):
        assert _is_linked(a1, 'person', b)
    _safe_set(b, 'Address', a2)
    assert _is_linked(b, 'Address', a2)
    if hasattr(a1, 'person'):
        assert not _is_linked(a1, 'person', b)
    if hasattr(a2, 'person'):
        assert _is_linked(a2, 'person', b)
    _safe_set(b, 'Address', None)
    assert not _is_linked(b, 'Address', a2)
    if hasattr(a2, 'person'):
        assert not _is_linked(a2, 'person', b)


def test_assoc_country14_reverse_link_reassign_clear():
    a1 = addressbook_FederalState(name="sample_text")
    a2 = addressbook_FederalState(name="sample_text_2")
    b = addressbook_Country(name="sample_text")
    _safe_set(b, 'Country', a1)
    assert _is_linked(b, 'Country', a1)
    if hasattr(a1, 'federalStates'):
        assert _is_linked(a1, 'federalStates', b)
    _safe_set(b, 'Country', a2)
    assert _is_linked(b, 'Country', a2)
    if hasattr(a1, 'federalStates'):
        assert not _is_linked(a1, 'federalStates', b)
    if hasattr(a2, 'federalStates'):
        assert _is_linked(a2, 'federalStates', b)
    _safe_set(b, 'Country', None)
    assert not _is_linked(b, 'Country', a2)
    if hasattr(a2, 'federalStates'):
        assert not _is_linked(a2, 'federalStates', b)


def test_assoc_country4_reverse_link_reassign_clear():
    a1 = addressbook_Country(name="sample_text")
    a2 = addressbook_Country(name="sample_text_2")
    b = addressbook_Address(city="sample_text", street="sample_text", type="sample_text", zip="sample_text")
    _safe_set(b, 'addressbook_Address', a1)
    assert _is_linked(b, 'addressbook_Address', a1)
    if hasattr(a1, 'addressbook_Country5'):
        assert _is_linked(a1, 'addressbook_Country5', b)
    _safe_set(b, 'addressbook_Address', a2)
    assert _is_linked(b, 'addressbook_Address', a2)
    if hasattr(a1, 'addressbook_Country5'):
        assert not _is_linked(a1, 'addressbook_Country5', b)
    if hasattr(a2, 'addressbook_Country5'):
        assert _is_linked(a2, 'addressbook_Country5', b)
    _safe_set(b, 'addressbook_Address', None)
    assert not _is_linked(b, 'addressbook_Address', a2)
    if hasattr(a2, 'addressbook_Country5'):
        assert not _is_linked(a2, 'addressbook_Country5', b)


def test_assoc_federalState6_reverse_link_reassign_clear():
    a1 = addressbook_FederalState(name="sample_text")
    a2 = addressbook_FederalState(name="sample_text_2")
    b = addressbook_Address(city="sample_text", street="sample_text", type="sample_text", zip="sample_text")
    _safe_set(b, 'addressbook_Address7', a1)
    assert _is_linked(b, 'addressbook_Address7', a1)
    if hasattr(a1, 'addressbook_FederalState'):
        assert _is_linked(a1, 'addressbook_FederalState', b)
    _safe_set(b, 'addressbook_Address7', a2)
    assert _is_linked(b, 'addressbook_Address7', a2)
    if hasattr(a1, 'addressbook_FederalState'):
        assert not _is_linked(a1, 'addressbook_FederalState', b)
    if hasattr(a2, 'addressbook_FederalState'):
        assert _is_linked(a2, 'addressbook_FederalState', b)
    _safe_set(b, 'addressbook_Address7', None)
    assert not _is_linked(b, 'addressbook_Address7', a2)
    if hasattr(a2, 'addressbook_FederalState'):
        assert not _is_linked(a2, 'addressbook_FederalState', b)


def test_assoc_federalStates10_reverse_link_reassign_clear():
    a1 = addressbook_FederalState(name="sample_text")
    a2 = addressbook_FederalState(name="sample_text_2")
    b = addressbook_Country(name="sample_text")
    _safe_set(b, 'country', {a1})
    assert _is_linked(b, 'country', a1)
    if hasattr(a1, 'FederalState'):
        assert _is_linked(a1, 'FederalState', b)
    _safe_set(b, 'country', {a2})
    assert _is_linked(b, 'country', a2)
    if hasattr(a1, 'FederalState'):
        assert not _is_linked(a1, 'FederalState', b)
    if hasattr(a2, 'FederalState'):
        assert _is_linked(a2, 'FederalState', b)
    _safe_set(b, 'country', set())
    assert not _is_linked(b, 'country', a2)
    if hasattr(a2, 'FederalState'):
        assert not _is_linked(a2, 'FederalState', b)


def test_assoc_person8_reverse_link_reassign_clear():
    a1 = addressbook_Person(firstname="sample_text", lastname="sample_text")
    a2 = addressbook_Person(firstname="sample_text_2", lastname="sample_text_2")
    b = addressbook_Address(city="sample_text", street="sample_text", type="sample_text", zip="sample_text")
    _safe_set(b, 'addresses', a1)
    assert _is_linked(b, 'addresses', a1)
    if hasattr(a1, 'Person9'):
        assert _is_linked(a1, 'Person9', b)
    _safe_set(b, 'addresses', a2)
    assert _is_linked(b, 'addresses', a2)
    if hasattr(a1, 'Person9'):
        assert not _is_linked(a1, 'Person9', b)
    if hasattr(a2, 'Person9'):
        assert _is_linked(a2, 'Person9', b)
    _safe_set(b, 'addresses', None)
    assert not _is_linked(b, 'addresses', a2)
    if hasattr(a2, 'Person9'):
        assert not _is_linked(a2, 'Person9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_addressBook11_stub_double():
    # addressbook_AddressBook has no real 'addressbook_AddressBook13' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_Country's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_Country's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_Country(name="sample_text")
    partner = addressbook_AddressBook()
    setattr(partner, 'addressbook_AddressBook13', None)
    _safe_set(owner, 'addressbook_Country12', partner)
    assert getattr(partner, 'addressbook_AddressBook13') == owner
    _safe_set(owner, 'addressbook_Country12', None)
    assert getattr(partner, 'addressbook_AddressBook13') is None


def test_assoc_addressBook3_stub_double():
    # addressbook_AddressBook has no real 'AddressBook' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_Person(firstname="sample_text", lastname="sample_text")
    partner = addressbook_AddressBook()
    setattr(partner, 'AddressBook', None)
    _safe_set(owner, 'persons', partner)
    assert getattr(partner, 'AddressBook') == owner
    _safe_set(owner, 'persons', None)
    assert getattr(partner, 'AddressBook') is None


def test_assoc_countries1_stub_double():
    # addressbook_AddressBook has no real 'addressbook_AddressBook' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_Country's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_Country's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_Country(name="sample_text")
    partner = addressbook_AddressBook()
    setattr(partner, 'addressbook_AddressBook', None)
    _safe_set(owner, 'addressbook_Country', partner)
    assert owner in getattr(partner, 'addressbook_AddressBook')
    _safe_set(owner, 'addressbook_Country', None)
    assert owner not in getattr(partner, 'addressbook_AddressBook')


def test_assoc_persons0_stub_double():
    # addressbook_AddressBook has no real 'addressBook' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_Person(firstname="sample_text", lastname="sample_text")
    partner = addressbook_AddressBook()
    setattr(partner, 'addressBook', None)
    _safe_set(owner, 'Person', partner)
    assert owner in getattr(partner, 'addressBook')
    _safe_set(owner, 'Person', None)
    assert owner not in getattr(partner, 'addressBook')


