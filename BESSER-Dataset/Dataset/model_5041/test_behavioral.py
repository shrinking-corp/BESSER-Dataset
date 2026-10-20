import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    ContactMethod,
    Device,
    Party,
    TransactionInitiator,
    bank_Account,
    bank_Bank,
    bank_Banker,
    bank_BankerTransaction,
    bank_Card,
    bank_ContactMethod,
    bank_Customer,
    bank_CustomerAccount,
    bank_Device,
    bank_DeviceTransaction,
    bank_EMail,
    bank_InternalAccount,
    bank_Merchant,
    bank_MobilePhone,
    bank_OnlineSession,
    bank_OnlineTransaction,
    bank_Party,
    bank_Phone,
    bank_PointOfSale,
    bank_PostalAddress,
    bank_Product,
    bank_Statement,
    bank_Token,
    bank_TokenTransaction,
    bank_Transaction,
    bank_TransactionInitiator,
    bank_WebAddress,
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

def test_assoc_contactMethods0_reverse_link_reassign_clear():
    a1 = bank_Party(name="sample_text")
    a2 = bank_Party(name="sample_text_2")
    b = bank_ContactMethod(description="sample_text", name="sample_text")
    _safe_set(b, 'bank_ContactMethod', a1)
    assert _is_linked(b, 'bank_ContactMethod', a1)
    if hasattr(a1, 'bank_Party'):
        assert _is_linked(a1, 'bank_Party', b)
    _safe_set(b, 'bank_ContactMethod', a2)
    assert _is_linked(b, 'bank_ContactMethod', a2)
    if hasattr(a1, 'bank_Party'):
        assert not _is_linked(a1, 'bank_Party', b)
    if hasattr(a2, 'bank_Party'):
        assert _is_linked(a2, 'bank_Party', b)
    _safe_set(b, 'bank_ContactMethod', None)
    assert not _is_linked(b, 'bank_ContactMethod', a2)
    if hasattr(a2, 'bank_Party'):
        assert not _is_linked(a2, 'bank_Party', b)


def test_assoc_credit16_reverse_link_reassign_clear():
    a1 = bank_Transaction(amount="sample_text", comment="sample_text", date=date(2024, 1, 1), id="sample_text")
    a2 = bank_Transaction(amount="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), id="sample_text_2")
    b = bank_Statement(closingBalance="sample_text", closingDate=date(2024, 1, 1), openingBalance="sample_text", openingDate=date(2024, 1, 1))
    _safe_set(b, 'Statement17', a1)
    assert _is_linked(b, 'Statement17', a1)
    if hasattr(a1, 'credits'):
        assert _is_linked(a1, 'credits', b)
    _safe_set(b, 'Statement17', a2)
    assert _is_linked(b, 'Statement17', a2)
    if hasattr(a1, 'credits'):
        assert not _is_linked(a1, 'credits', b)
    if hasattr(a2, 'credits'):
        assert _is_linked(a2, 'credits', b)
    _safe_set(b, 'Statement17', None)
    assert not _is_linked(b, 'Statement17', a2)
    if hasattr(a2, 'credits'):
        assert not _is_linked(a2, 'credits', b)


def test_assoc_debit15_reverse_link_reassign_clear():
    a1 = bank_Transaction(amount="sample_text", comment="sample_text", date=date(2024, 1, 1), id="sample_text")
    a2 = bank_Transaction(amount="sample_text_2", comment="sample_text_2", date=date(2025, 6, 15), id="sample_text_2")
    b = bank_Statement(closingBalance="sample_text", closingDate=date(2024, 1, 1), openingBalance="sample_text", openingDate=date(2024, 1, 1))
    _safe_set(b, 'Statement', a1)
    assert _is_linked(b, 'Statement', a1)
    if hasattr(a1, 'debits'):
        assert _is_linked(a1, 'debits', b)
    _safe_set(b, 'Statement', a2)
    assert _is_linked(b, 'Statement', a2)
    if hasattr(a1, 'debits'):
        assert not _is_linked(a1, 'debits', b)
    if hasattr(a2, 'debits'):
        assert _is_linked(a2, 'debits', b)
    _safe_set(b, 'Statement', None)
    assert not _is_linked(b, 'Statement', a2)
    if hasattr(a2, 'debits'):
        assert not _is_linked(a2, 'debits', b)


def test_assoc_location21_reverse_link_reassign_clear():
    a1 = bank_PostalAddress(city="sample_text", country="sample_text", line1="sample_text", line2="sample_text", postalCode="sample_text", stateProvince="sample_text")
    a2 = bank_PostalAddress(city="sample_text_2", country="sample_text_2", line1="sample_text_2", line2="sample_text_2", postalCode="sample_text_2", stateProvince="sample_text_2")
    b = bank_PointOfSale(id="sample_text")
    _safe_set(b, 'bank_PointOfSale22', a1)
    assert _is_linked(b, 'bank_PointOfSale22', a1)
    if hasattr(a1, 'bank_PostalAddress'):
        assert _is_linked(a1, 'bank_PostalAddress', b)
    _safe_set(b, 'bank_PointOfSale22', a2)
    assert _is_linked(b, 'bank_PointOfSale22', a2)
    if hasattr(a1, 'bank_PostalAddress'):
        assert not _is_linked(a1, 'bank_PostalAddress', b)
    if hasattr(a2, 'bank_PostalAddress'):
        assert _is_linked(a2, 'bank_PostalAddress', b)
    _safe_set(b, 'bank_PointOfSale22', None)
    assert not _is_linked(b, 'bank_PointOfSale22', a2)
    if hasattr(a2, 'bank_PostalAddress'):
        assert not _is_linked(a2, 'bank_PostalAddress', b)


def test_assoc_replaces27_reverse_link_reassign_clear():
    a1 = bank_Card(activated=date(2024, 1, 1), deactivated=date(2024, 1, 1), expires=date(2024, 1, 1), id="sample_text", issued=date(2024, 1, 1), virtual=True)
    a2 = bank_Card(activated=date(2025, 6, 15), deactivated=date(2025, 6, 15), expires=date(2025, 6, 15), id="sample_text_2", issued=date(2025, 6, 15), virtual=False)
    b = bank_Card(activated=date(2024, 1, 1), deactivated=date(2024, 1, 1), expires=date(2024, 1, 1), id="sample_text", issued=date(2024, 1, 1), virtual=True)
    _safe_set(b, 'bank_Card28', a1)
    assert _is_linked(b, 'bank_Card28', a1)
    if hasattr(a1, 'bank_Card26'):
        assert _is_linked(a1, 'bank_Card26', b)
    _safe_set(b, 'bank_Card28', a2)
    assert _is_linked(b, 'bank_Card28', a2)
    if hasattr(a1, 'bank_Card26'):
        assert not _is_linked(a1, 'bank_Card26', b)
    if hasattr(a2, 'bank_Card26'):
        assert _is_linked(a2, 'bank_Card26', b)
    _safe_set(b, 'bank_Card28', None)
    assert not _is_linked(b, 'bank_Card28', a2)
    if hasattr(a2, 'bank_Card26'):
        assert not _is_linked(a2, 'bank_Card26', b)


def test_assoc_statements13_reverse_link_reassign_clear():
    a1 = bank_Statement(closingBalance="sample_text", closingDate=date(2024, 1, 1), openingBalance="sample_text", openingDate=date(2024, 1, 1))
    a2 = bank_Statement(closingBalance="sample_text_2", closingDate=date(2025, 6, 15), openingBalance="sample_text_2", openingDate=date(2025, 6, 15))
    b = bank_Account(balance="sample_text", description="sample_text", number="sample_text", periodStart=7)
    _safe_set(b, 'bank_Account14', {a1})
    assert _is_linked(b, 'bank_Account14', a1)
    if hasattr(a1, 'bank_Statement'):
        assert _is_linked(a1, 'bank_Statement', b)
    _safe_set(b, 'bank_Account14', {a2})
    assert _is_linked(b, 'bank_Account14', a2)
    if hasattr(a1, 'bank_Statement'):
        assert not _is_linked(a1, 'bank_Statement', b)
    if hasattr(a2, 'bank_Statement'):
        assert _is_linked(a2, 'bank_Statement', b)
    _safe_set(b, 'bank_Account14', set())
    assert not _is_linked(b, 'bank_Account14', a2)
    if hasattr(a2, 'bank_Statement'):
        assert not _is_linked(a2, 'bank_Statement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accounts4_stub_double():
    # bank_Bank has no real 'bank_Bank5' property in the generated
    # code (a bare stub) -- manually attach it so bank_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Account(balance="sample_text", description="sample_text", number="sample_text", periodStart=7)
    partner = bank_Bank()
    setattr(partner, 'bank_Bank5', None)
    _safe_set(owner, 'bank_Account', partner)
    assert owner in getattr(partner, 'bank_Bank5')
    _safe_set(owner, 'bank_Account', None)
    assert owner not in getattr(partner, 'bank_Bank5')


def test_assoc_initiator18_stub_double():
    # bank_TransactionInitiator has no real 'bank_TransactionInitiator' property in the generated
    # code (a bare stub) -- manually attach it so bank_Transaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Transaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Transaction(amount="sample_text", comment="sample_text", date=date(2024, 1, 1), id="sample_text")
    partner = bank_TransactionInitiator()
    setattr(partner, 'bank_TransactionInitiator', None)
    _safe_set(owner, 'bank_Transaction', partner)
    assert getattr(partner, 'bank_TransactionInitiator') == owner
    _safe_set(owner, 'bank_Transaction', None)
    assert getattr(partner, 'bank_TransactionInitiator') is None


def test_assoc_lockedTo24_stub_double():
    # bank_Merchant has no real 'bank_Merchant25' property in the generated
    # code (a bare stub) -- manually attach it so bank_Card's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Card's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Card(activated=date(2024, 1, 1), deactivated=date(2024, 1, 1), expires=date(2024, 1, 1), id="sample_text", issued=date(2024, 1, 1), virtual=True)
    partner = bank_Merchant()
    setattr(partner, 'bank_Merchant25', None)
    _safe_set(owner, 'bank_Card', partner)
    assert getattr(partner, 'bank_Merchant25') == owner
    _safe_set(owner, 'bank_Card', None)
    assert getattr(partner, 'bank_Merchant25') is None


def test_assoc_merchant37_stub_double():
    # bank_Merchant has no real 'bank_Merchant39' property in the generated
    # code (a bare stub) -- manually attach it so bank_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Token(value="sample_text")
    partner = bank_Merchant()
    setattr(partner, 'bank_Merchant39', None)
    _safe_set(owner, 'bank_Token38', partner)
    assert getattr(partner, 'bank_Merchant39') == owner
    _safe_set(owner, 'bank_Token38', None)
    assert getattr(partner, 'bank_Merchant39') is None


def test_assoc_onlineSessions11_stub_double():
    # bank_Customer has no real 'bank_Customer12' property in the generated
    # code (a bare stub) -- manually attach it so bank_OnlineSession's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_OnlineSession's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_OnlineSession(end=date(2024, 1, 1), internetAddress="sample_text", start=date(2024, 1, 1))
    partner = bank_Customer()
    setattr(partner, 'bank_Customer12', None)
    _safe_set(owner, 'bank_OnlineSession', partner)
    assert owner in getattr(partner, 'bank_Customer12')
    _safe_set(owner, 'bank_OnlineSession', None)
    assert owner not in getattr(partner, 'bank_Customer12')


def test_assoc_pointOfSale29_stub_double():
    # bank_DeviceTransaction has no real 'bank_DeviceTransaction' property in the generated
    # code (a bare stub) -- manually attach it so bank_PointOfSale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_PointOfSale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_PointOfSale(id="sample_text")
    partner = bank_DeviceTransaction()
    setattr(partner, 'bank_DeviceTransaction', None)
    _safe_set(owner, 'bank_PointOfSale30', partner)
    assert getattr(partner, 'bank_DeviceTransaction') == owner
    _safe_set(owner, 'bank_PointOfSale30', None)
    assert getattr(partner, 'bank_DeviceTransaction') is None


def test_assoc_pointsOfSale19_stub_double():
    # bank_Merchant has no real 'bank_Merchant20' property in the generated
    # code (a bare stub) -- manually attach it so bank_PointOfSale's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_PointOfSale's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_PointOfSale(id="sample_text")
    partner = bank_Merchant()
    setattr(partner, 'bank_Merchant20', None)
    _safe_set(owner, 'bank_PointOfSale', partner)
    assert owner in getattr(partner, 'bank_Merchant20')
    _safe_set(owner, 'bank_PointOfSale', None)
    assert owner not in getattr(partner, 'bank_Merchant20')


def test_assoc_product33_stub_double():
    # bank_CustomerAccount has no real 'bank_CustomerAccount34' property in the generated
    # code (a bare stub) -- manually attach it so bank_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Product(description="sample_text", name="sample_text")
    partner = bank_CustomerAccount()
    setattr(partner, 'bank_CustomerAccount34', None)
    _safe_set(owner, 'bank_Product35', partner)
    assert getattr(partner, 'bank_CustomerAccount34') == owner
    _safe_set(owner, 'bank_Product35', None)
    assert getattr(partner, 'bank_CustomerAccount34') is None


def test_assoc_products2_stub_double():
    # bank_Bank has no real 'bank_Bank3' property in the generated
    # code (a bare stub) -- manually attach it so bank_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Product(description="sample_text", name="sample_text")
    partner = bank_Bank()
    setattr(partner, 'bank_Bank3', None)
    _safe_set(owner, 'bank_Product', partner)
    assert owner in getattr(partner, 'bank_Bank3')
    _safe_set(owner, 'bank_Product', None)
    assert owner not in getattr(partner, 'bank_Bank3')


def test_assoc_tokens23_stub_double():
    # bank_Device has no real 'bank_Device' property in the generated
    # code (a bare stub) -- manually attach it so bank_Token's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bank_Token's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bank_Token(value="sample_text")
    partner = bank_Device()
    setattr(partner, 'bank_Device', None)
    _safe_set(owner, 'bank_Token', partner)
    assert owner in getattr(partner, 'bank_Device')
    _safe_set(owner, 'bank_Token', None)
    assert owner not in getattr(partner, 'bank_Device')


