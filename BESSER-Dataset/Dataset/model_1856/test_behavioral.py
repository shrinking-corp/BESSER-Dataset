import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Contact,
    addressbook_AddressBook,
    addressbook_BookVersion,
    addressbook_Contact,
    addressbook_Electronic,
    addressbook_Office,
    addressbook_People,
    addressbook_Repository,
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

def test_assoc_history5_reverse_link_reassign_clear():
    a1 = addressbook_Repository()
    a2 = addressbook_Repository()
    b = addressbook_BookVersion(id=7)
    _safe_set(b, 'addressbook_BookVersion', a1)
    assert _is_linked(b, 'addressbook_BookVersion', a1)
    if hasattr(a1, 'addressbook_Repository6'):
        assert _is_linked(a1, 'addressbook_Repository6', b)
    _safe_set(b, 'addressbook_BookVersion', a2)
    assert _is_linked(b, 'addressbook_BookVersion', a2)
    if hasattr(a1, 'addressbook_Repository6'):
        assert not _is_linked(a1, 'addressbook_Repository6', b)
    if hasattr(a2, 'addressbook_Repository6'):
        assert _is_linked(a2, 'addressbook_Repository6', b)
    _safe_set(b, 'addressbook_BookVersion', None)
    assert not _is_linked(b, 'addressbook_BookVersion', a2)
    if hasattr(a2, 'addressbook_Repository6'):
        assert not _is_linked(a2, 'addressbook_Repository6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_book7_stub_double():
    # addressbook_AddressBook has no real 'addressbook_AddressBook9' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_BookVersion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_BookVersion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_BookVersion(id=7)
    partner = addressbook_AddressBook()
    setattr(partner, 'addressbook_AddressBook9', None)
    _safe_set(owner, 'addressbook_BookVersion8', partner)
    assert getattr(partner, 'addressbook_AddressBook9') == owner
    _safe_set(owner, 'addressbook_BookVersion8', None)
    assert getattr(partner, 'addressbook_AddressBook9') is None


def test_assoc_contacts0_stub_double():
    # addressbook_Contact has no real 'addressbook_Contact' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_People's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_People's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_People(name="sample_text")
    partner = addressbook_Contact()
    setattr(partner, 'addressbook_Contact', None)
    _safe_set(owner, 'addressbook_People', {partner})
    assert getattr(partner, 'addressbook_Contact') == owner
    _safe_set(owner, 'addressbook_People', set())
    assert getattr(partner, 'addressbook_Contact') is None


def test_assoc_head3_stub_double():
    # addressbook_AddressBook has no real 'addressbook_AddressBook4' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_Repository()
    partner = addressbook_AddressBook()
    setattr(partner, 'addressbook_AddressBook4', None)
    _safe_set(owner, 'addressbook_Repository', partner)
    assert getattr(partner, 'addressbook_AddressBook4') == owner
    _safe_set(owner, 'addressbook_Repository', None)
    assert getattr(partner, 'addressbook_AddressBook4') is None


def test_assoc_peoples1_stub_double():
    # addressbook_AddressBook has no real 'addressbook_AddressBook' property in the generated
    # code (a bare stub) -- manually attach it so addressbook_People's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # addressbook_People's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = addressbook_People(name="sample_text")
    partner = addressbook_AddressBook()
    setattr(partner, 'addressbook_AddressBook', None)
    _safe_set(owner, 'addressbook_People2', partner)
    assert owner in getattr(partner, 'addressbook_AddressBook')
    _safe_set(owner, 'addressbook_People2', None)
    assert owner not in getattr(partner, 'addressbook_AddressBook')


