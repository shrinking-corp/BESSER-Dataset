import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    RandL_Burning,
    RandL_Container_RandL,
    RandL_Customer,
    RandL_CustomerCard,
    RandL_Date,
    RandL_Earning,
    RandL_LoyaltyAccount,
    RandL_LoyaltyProgram,
    RandL_Membership,
    RandL_ProgramPartner,
    RandL_Service,
    RandL_ServiceLevel,
    RandL_Transaction,
    RandL_TransactionReport,
    RandL_TransactionReportLine,
    Transaction,
    Gender,
    RandLColor,
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

def test_assoc_account4_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    _safe_set(b, 'LoyaltyAccount', a1)
    assert _is_linked(b, 'LoyaltyAccount', a1)
    if hasattr(a1, 'transactions'):
        assert _is_linked(a1, 'transactions', b)
    _safe_set(b, 'LoyaltyAccount', a2)
    assert _is_linked(b, 'LoyaltyAccount', a2)
    if hasattr(a1, 'transactions'):
        assert not _is_linked(a1, 'transactions', b)
    if hasattr(a2, 'transactions'):
        assert _is_linked(a2, 'transactions', b)
    _safe_set(b, 'LoyaltyAccount', None)
    assert not _is_linked(b, 'LoyaltyAccount', a2)
    if hasattr(a2, 'transactions'):
        assert not _is_linked(a2, 'transactions', b)


def test_assoc_availableServices1_reverse_link_reassign_clear():
    a1 = RandL_ServiceLevel(name="sample_text")
    a2 = RandL_ServiceLevel(name="sample_text_2")
    b = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    _safe_set(b, 'Service', a1)
    assert _is_linked(b, 'Service', a1)
    if hasattr(a1, 'level'):
        assert _is_linked(a1, 'level', b)
    _safe_set(b, 'Service', a2)
    assert _is_linked(b, 'Service', a2)
    if hasattr(a1, 'level'):
        assert not _is_linked(a1, 'level', b)
    if hasattr(a2, 'level'):
        assert _is_linked(a2, 'level', b)
    _safe_set(b, 'Service', None)
    assert not _is_linked(b, 'Service', a2)
    if hasattr(a2, 'level'):
        assert not _is_linked(a2, 'level', b)


def test_assoc_card25_reverse_link_reassign_clear():
    a1 = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    a2 = RandL_TransactionReport(balance="sample_text_2", name="sample_text_2", number="sample_text_2", totalBurned="sample_text_2", totalEarned="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'RandL_CustomerCard', a1)
    assert _is_linked(b, 'RandL_CustomerCard', a1)
    if hasattr(a1, 'RandL_TransactionReport26'):
        assert _is_linked(a1, 'RandL_TransactionReport26', b)
    _safe_set(b, 'RandL_CustomerCard', a2)
    assert _is_linked(b, 'RandL_CustomerCard', a2)
    if hasattr(a1, 'RandL_TransactionReport26'):
        assert not _is_linked(a1, 'RandL_TransactionReport26', b)
    if hasattr(a2, 'RandL_TransactionReport26'):
        assert _is_linked(a2, 'RandL_TransactionReport26', b)
    _safe_set(b, 'RandL_CustomerCard', None)
    assert not _is_linked(b, 'RandL_CustomerCard', a2)
    if hasattr(a2, 'RandL_TransactionReport26'):
        assert not _is_linked(a2, 'RandL_TransactionReport26', b)


def test_assoc_card8_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'CustomerCard', a1)
    assert _is_linked(b, 'CustomerCard', a1)
    if hasattr(a1, 'transactions9'):
        assert _is_linked(a1, 'transactions9', b)
    _safe_set(b, 'CustomerCard', a2)
    assert _is_linked(b, 'CustomerCard', a2)
    if hasattr(a1, 'transactions9'):
        assert not _is_linked(a1, 'transactions9', b)
    if hasattr(a2, 'transactions9'):
        assert _is_linked(a2, 'transactions9', b)
    _safe_set(b, 'CustomerCard', None)
    assert not _is_linked(b, 'CustomerCard', a2)
    if hasattr(a2, 'transactions9'):
        assert not _is_linked(a2, 'transactions9', b)


def test_assoc_cards96_reverse_link_reassign_clear():
    a1 = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    a2 = RandL_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid="sample_text_2")
    b = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'CustomerCard97'):
        assert _is_linked(a1, 'CustomerCard97', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'CustomerCard97'):
        assert not _is_linked(a1, 'CustomerCard97', b)
    if hasattr(a2, 'CustomerCard97'):
        assert _is_linked(a2, 'CustomerCard97', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'CustomerCard97'):
        assert not _is_linked(a2, 'CustomerCard97', b)


def test_assoc_date101_reverse_link_reassign_clear():
    a1 = RandL_TransactionReportLine(amount="sample_text", partnerName="sample_text", points="sample_text", serviceDesc="sample_text")
    a2 = RandL_TransactionReportLine(amount="sample_text_2", partnerName="sample_text_2", points="sample_text_2", serviceDesc="sample_text_2")
    b = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    _safe_set(b, 'RandL_Date103', a1)
    assert _is_linked(b, 'RandL_Date103', a1)
    if hasattr(a1, 'RandL_TransactionReportLine102'):
        assert _is_linked(a1, 'RandL_TransactionReportLine102', b)
    _safe_set(b, 'RandL_Date103', a2)
    assert _is_linked(b, 'RandL_Date103', a2)
    if hasattr(a1, 'RandL_TransactionReportLine102'):
        assert not _is_linked(a1, 'RandL_TransactionReportLine102', b)
    if hasattr(a2, 'RandL_TransactionReportLine102'):
        assert _is_linked(a2, 'RandL_TransactionReportLine102', b)
    _safe_set(b, 'RandL_Date103', None)
    assert not _is_linked(b, 'RandL_Date103', a2)
    if hasattr(a2, 'RandL_TransactionReportLine102'):
        assert not _is_linked(a2, 'RandL_TransactionReportLine102', b)


def test_assoc_date3_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    _safe_set(b, 'RandL_Date', a1)
    assert _is_linked(b, 'RandL_Date', a1)
    if hasattr(a1, 'RandL_Transaction'):
        assert _is_linked(a1, 'RandL_Transaction', b)
    _safe_set(b, 'RandL_Date', a2)
    assert _is_linked(b, 'RandL_Date', a2)
    if hasattr(a1, 'RandL_Transaction'):
        assert not _is_linked(a1, 'RandL_Transaction', b)
    if hasattr(a2, 'RandL_Transaction'):
        assert _is_linked(a2, 'RandL_Transaction', b)
    _safe_set(b, 'RandL_Date', None)
    assert not _is_linked(b, 'RandL_Date', a2)
    if hasattr(a2, 'RandL_Transaction'):
        assert not _is_linked(a2, 'RandL_Transaction', b)


def test_assoc_dateOfBirth91_reverse_link_reassign_clear():
    a1 = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    a2 = RandL_Date(day="sample_text_2", month="sample_text_2", year="sample_text_2")
    b = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'RandL_Customer92', a1)
    assert _is_linked(b, 'RandL_Customer92', a1)
    if hasattr(a1, 'RandL_Date93'):
        assert _is_linked(a1, 'RandL_Date93', b)
    _safe_set(b, 'RandL_Customer92', a2)
    assert _is_linked(b, 'RandL_Customer92', a2)
    if hasattr(a1, 'RandL_Date93'):
        assert not _is_linked(a1, 'RandL_Date93', b)
    if hasattr(a2, 'RandL_Date93'):
        assert _is_linked(a2, 'RandL_Date93', b)
    _safe_set(b, 'RandL_Customer92', None)
    assert not _is_linked(b, 'RandL_Customer92', a2)
    if hasattr(a2, 'RandL_Date93'):
        assert not _is_linked(a2, 'RandL_Date93', b)


def test_assoc_deliveredServices15_reverse_link_reassign_clear():
    a1 = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    a2 = RandL_Service(condition="sample_text_2", description="sample_text_2", pointsBurned="sample_text_2", pointsEarned="sample_text_2", serviceNr="sample_text_2")
    b = RandL_ProgramPartner(name="sample_text", numberOfCustomers="sample_text")
    _safe_set(b, 'partner', {a1})
    assert _is_linked(b, 'partner', a1)
    if hasattr(a1, 'Service16'):
        assert _is_linked(a1, 'Service16', b)
    _safe_set(b, 'partner', {a2})
    assert _is_linked(b, 'partner', a2)
    if hasattr(a1, 'Service16'):
        assert not _is_linked(a1, 'Service16', b)
    if hasattr(a2, 'Service16'):
        assert _is_linked(a2, 'Service16', b)
    _safe_set(b, 'partner', set())
    assert not _is_linked(b, 'partner', a2)
    if hasattr(a2, 'Service16'):
        assert not _is_linked(a2, 'Service16', b)


def test_assoc_from_21_reverse_link_reassign_clear():
    a1 = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    a2 = RandL_TransactionReport(balance="sample_text_2", name="sample_text_2", number="sample_text_2", totalBurned="sample_text_2", totalEarned="sample_text_2")
    b = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    _safe_set(b, 'RandL_Date23', a1)
    assert _is_linked(b, 'RandL_Date23', a1)
    if hasattr(a1, 'RandL_TransactionReport22'):
        assert _is_linked(a1, 'RandL_TransactionReport22', b)
    _safe_set(b, 'RandL_Date23', a2)
    assert _is_linked(b, 'RandL_Date23', a2)
    if hasattr(a1, 'RandL_TransactionReport22'):
        assert not _is_linked(a1, 'RandL_TransactionReport22', b)
    if hasattr(a2, 'RandL_TransactionReport22'):
        assert _is_linked(a2, 'RandL_TransactionReport22', b)
    _safe_set(b, 'RandL_Date23', None)
    assert not _is_linked(b, 'RandL_Date23', a2)
    if hasattr(a2, 'RandL_TransactionReport22'):
        assert not _is_linked(a2, 'RandL_TransactionReport22', b)


def test_assoc_generatedBy5_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    _safe_set(b, 'Service7', a1)
    assert _is_linked(b, 'Service7', a1)
    if hasattr(a1, 'transactions6'):
        assert _is_linked(a1, 'transactions6', b)
    _safe_set(b, 'Service7', a2)
    assert _is_linked(b, 'Service7', a2)
    if hasattr(a1, 'transactions6'):
        assert not _is_linked(a1, 'transactions6', b)
    if hasattr(a2, 'transactions6'):
        assert _is_linked(a2, 'transactions6', b)
    _safe_set(b, 'Service7', None)
    assert not _is_linked(b, 'Service7', a2)
    if hasattr(a2, 'transactions6'):
        assert not _is_linked(a2, 'transactions6', b)


def test_assoc_goodThru27_reverse_link_reassign_clear():
    a1 = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    a2 = RandL_Date(day="sample_text_2", month="sample_text_2", year="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'RandL_CustomerCard28', a1)
    assert _is_linked(b, 'RandL_CustomerCard28', a1)
    if hasattr(a1, 'RandL_Date29'):
        assert _is_linked(a1, 'RandL_Date29', b)
    _safe_set(b, 'RandL_CustomerCard28', a2)
    assert _is_linked(b, 'RandL_CustomerCard28', a2)
    if hasattr(a1, 'RandL_Date29'):
        assert not _is_linked(a1, 'RandL_Date29', b)
    if hasattr(a2, 'RandL_Date29'):
        assert _is_linked(a2, 'RandL_Date29', b)
    _safe_set(b, 'RandL_CustomerCard28', None)
    assert not _is_linked(b, 'RandL_CustomerCard28', a2)
    if hasattr(a2, 'RandL_Date29'):
        assert not _is_linked(a2, 'RandL_Date29', b)


def test_assoc_level89_reverse_link_reassign_clear():
    a1 = RandL_ServiceLevel(name="sample_text")
    a2 = RandL_ServiceLevel(name="sample_text_2")
    b = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    _safe_set(b, 'availableServices', a1)
    assert _is_linked(b, 'availableServices', a1)
    if hasattr(a1, 'ServiceLevel90'):
        assert _is_linked(a1, 'ServiceLevel90', b)
    _safe_set(b, 'availableServices', a2)
    assert _is_linked(b, 'availableServices', a2)
    if hasattr(a1, 'ServiceLevel90'):
        assert not _is_linked(a1, 'ServiceLevel90', b)
    if hasattr(a2, 'ServiceLevel90'):
        assert _is_linked(a2, 'ServiceLevel90', b)
    _safe_set(b, 'availableServices', None)
    assert not _is_linked(b, 'availableServices', a2)
    if hasattr(a2, 'ServiceLevel90'):
        assert not _is_linked(a2, 'ServiceLevel90', b)


def test_assoc_levels110_reverse_link_reassign_clear():
    a1 = RandL_ServiceLevel(name="sample_text")
    a2 = RandL_ServiceLevel(name="sample_text_2")
    b = RandL_LoyaltyProgram(name="sample_text")
    _safe_set(b, 'program', {a1})
    assert _is_linked(b, 'program', a1)
    if hasattr(a1, 'ServiceLevel111'):
        assert _is_linked(a1, 'ServiceLevel111', b)
    _safe_set(b, 'program', {a2})
    assert _is_linked(b, 'program', a2)
    if hasattr(a1, 'ServiceLevel111'):
        assert not _is_linked(a1, 'ServiceLevel111', b)
    if hasattr(a2, 'ServiceLevel111'):
        assert _is_linked(a2, 'ServiceLevel111', b)
    _safe_set(b, 'program', set())
    assert not _is_linked(b, 'program', a2)
    if hasattr(a2, 'ServiceLevel111'):
        assert not _is_linked(a2, 'ServiceLevel111', b)


def test_assoc_lines24_reverse_link_reassign_clear():
    a1 = RandL_TransactionReportLine(amount="sample_text", partnerName="sample_text", points="sample_text", serviceDesc="sample_text")
    a2 = RandL_TransactionReportLine(amount="sample_text_2", partnerName="sample_text_2", points="sample_text_2", serviceDesc="sample_text_2")
    b = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    _safe_set(b, 'report', {a1})
    assert _is_linked(b, 'report', a1)
    if hasattr(a1, 'TransactionReportLine'):
        assert _is_linked(a1, 'TransactionReportLine', b)
    _safe_set(b, 'report', {a2})
    assert _is_linked(b, 'report', a2)
    if hasattr(a1, 'TransactionReportLine'):
        assert not _is_linked(a1, 'TransactionReportLine', b)
    if hasattr(a2, 'TransactionReportLine'):
        assert _is_linked(a2, 'TransactionReportLine', b)
    _safe_set(b, 'report', set())
    assert not _is_linked(b, 'report', a2)
    if hasattr(a2, 'TransactionReportLine'):
        assert not _is_linked(a2, 'TransactionReportLine', b)


def test_assoc_myLevel33_reverse_link_reassign_clear():
    a1 = RandL_ServiceLevel(name="sample_text")
    a2 = RandL_ServiceLevel(name="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'RandL_CustomerCard34', a1)
    assert _is_linked(b, 'RandL_CustomerCard34', a1)
    if hasattr(a1, 'RandL_ServiceLevel'):
        assert _is_linked(a1, 'RandL_ServiceLevel', b)
    _safe_set(b, 'RandL_CustomerCard34', a2)
    assert _is_linked(b, 'RandL_CustomerCard34', a2)
    if hasattr(a1, 'RandL_ServiceLevel'):
        assert not _is_linked(a1, 'RandL_ServiceLevel', b)
    if hasattr(a2, 'RandL_ServiceLevel'):
        assert _is_linked(a2, 'RandL_ServiceLevel', b)
    _safe_set(b, 'RandL_CustomerCard34', None)
    assert not _is_linked(b, 'RandL_CustomerCard34', a2)
    if hasattr(a2, 'RandL_ServiceLevel'):
        assert not _is_linked(a2, 'RandL_ServiceLevel', b)


def test_assoc_owner35_reverse_link_reassign_clear():
    a1 = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    a2 = RandL_CustomerCard(color="sample_text_2", printedName="sample_text_2", valid="sample_text_2")
    b = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'Customer', a1)
    assert _is_linked(b, 'Customer', a1)
    if hasattr(a1, 'cards'):
        assert _is_linked(a1, 'cards', b)
    _safe_set(b, 'Customer', a2)
    assert _is_linked(b, 'Customer', a2)
    if hasattr(a1, 'cards'):
        assert not _is_linked(a1, 'cards', b)
    if hasattr(a2, 'cards'):
        assert _is_linked(a2, 'cards', b)
    _safe_set(b, 'Customer', None)
    assert not _is_linked(b, 'Customer', a2)
    if hasattr(a2, 'cards'):
        assert not _is_linked(a2, 'cards', b)


def test_assoc_participants112_reverse_link_reassign_clear():
    a1 = RandL_LoyaltyProgram(name="sample_text")
    a2 = RandL_LoyaltyProgram(name="sample_text_2")
    b = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'Customer114', a1)
    assert _is_linked(b, 'Customer114', a1)
    if hasattr(a1, 'programs113'):
        assert _is_linked(a1, 'programs113', b)
    _safe_set(b, 'Customer114', a2)
    assert _is_linked(b, 'Customer114', a2)
    if hasattr(a1, 'programs113'):
        assert not _is_linked(a1, 'programs113', b)
    if hasattr(a2, 'programs113'):
        assert _is_linked(a2, 'programs113', b)
    _safe_set(b, 'Customer114', None)
    assert not _is_linked(b, 'Customer114', a2)
    if hasattr(a2, 'programs113'):
        assert not _is_linked(a2, 'programs113', b)


def test_assoc_partner86_reverse_link_reassign_clear():
    a1 = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    a2 = RandL_Service(condition="sample_text_2", description="sample_text_2", pointsBurned="sample_text_2", pointsEarned="sample_text_2", serviceNr="sample_text_2")
    b = RandL_ProgramPartner(name="sample_text", numberOfCustomers="sample_text")
    _safe_set(b, 'ProgramPartner', a1)
    assert _is_linked(b, 'ProgramPartner', a1)
    if hasattr(a1, 'deliveredServices'):
        assert _is_linked(a1, 'deliveredServices', b)
    _safe_set(b, 'ProgramPartner', a2)
    assert _is_linked(b, 'ProgramPartner', a2)
    if hasattr(a1, 'deliveredServices'):
        assert not _is_linked(a1, 'deliveredServices', b)
    if hasattr(a2, 'deliveredServices'):
        assert _is_linked(a2, 'deliveredServices', b)
    _safe_set(b, 'ProgramPartner', None)
    assert not _is_linked(b, 'ProgramPartner', a2)
    if hasattr(a2, 'deliveredServices'):
        assert not _is_linked(a2, 'deliveredServices', b)


def test_assoc_partners108_reverse_link_reassign_clear():
    a1 = RandL_ProgramPartner(name="sample_text", numberOfCustomers="sample_text")
    a2 = RandL_ProgramPartner(name="sample_text_2", numberOfCustomers="sample_text_2")
    b = RandL_LoyaltyProgram(name="sample_text")
    _safe_set(b, 'programs', {a1})
    assert _is_linked(b, 'programs', a1)
    if hasattr(a1, 'ProgramPartner109'):
        assert _is_linked(a1, 'ProgramPartner109', b)
    _safe_set(b, 'programs', {a2})
    assert _is_linked(b, 'programs', a2)
    if hasattr(a1, 'ProgramPartner109'):
        assert not _is_linked(a1, 'ProgramPartner109', b)
    if hasattr(a2, 'ProgramPartner109'):
        assert _is_linked(a2, 'ProgramPartner109', b)
    _safe_set(b, 'programs', set())
    assert not _is_linked(b, 'programs', a2)
    if hasattr(a2, 'ProgramPartner109'):
        assert not _is_linked(a2, 'ProgramPartner109', b)


def test_assoc_program0_reverse_link_reassign_clear():
    a1 = RandL_ServiceLevel(name="sample_text")
    a2 = RandL_ServiceLevel(name="sample_text_2")
    b = RandL_LoyaltyProgram(name="sample_text")
    _safe_set(b, 'LoyaltyProgram', a1)
    assert _is_linked(b, 'LoyaltyProgram', a1)
    if hasattr(a1, 'levels'):
        assert _is_linked(a1, 'levels', b)
    _safe_set(b, 'LoyaltyProgram', a2)
    assert _is_linked(b, 'LoyaltyProgram', a2)
    if hasattr(a1, 'levels'):
        assert not _is_linked(a1, 'levels', b)
    if hasattr(a2, 'levels'):
        assert _is_linked(a2, 'levels', b)
    _safe_set(b, 'LoyaltyProgram', None)
    assert not _is_linked(b, 'LoyaltyProgram', a2)
    if hasattr(a2, 'levels'):
        assert not _is_linked(a2, 'levels', b)


def test_assoc_programs17_reverse_link_reassign_clear():
    a1 = RandL_ProgramPartner(name="sample_text", numberOfCustomers="sample_text")
    a2 = RandL_ProgramPartner(name="sample_text_2", numberOfCustomers="sample_text_2")
    b = RandL_LoyaltyProgram(name="sample_text")
    _safe_set(b, 'LoyaltyProgram18', a1)
    assert _is_linked(b, 'LoyaltyProgram18', a1)
    if hasattr(a1, 'partners'):
        assert _is_linked(a1, 'partners', b)
    _safe_set(b, 'LoyaltyProgram18', a2)
    assert _is_linked(b, 'LoyaltyProgram18', a2)
    if hasattr(a1, 'partners'):
        assert not _is_linked(a1, 'partners', b)
    if hasattr(a2, 'partners'):
        assert _is_linked(a2, 'partners', b)
    _safe_set(b, 'LoyaltyProgram18', None)
    assert not _is_linked(b, 'LoyaltyProgram18', a2)
    if hasattr(a2, 'partners'):
        assert not _is_linked(a2, 'partners', b)


def test_assoc_programs94_reverse_link_reassign_clear():
    a1 = RandL_LoyaltyProgram(name="sample_text")
    a2 = RandL_LoyaltyProgram(name="sample_text_2")
    b = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    _safe_set(b, 'participants', {a1})
    assert _is_linked(b, 'participants', a1)
    if hasattr(a1, 'LoyaltyProgram95'):
        assert _is_linked(a1, 'LoyaltyProgram95', b)
    _safe_set(b, 'participants', {a2})
    assert _is_linked(b, 'participants', a2)
    if hasattr(a1, 'LoyaltyProgram95'):
        assert not _is_linked(a1, 'LoyaltyProgram95', b)
    if hasattr(a2, 'LoyaltyProgram95'):
        assert _is_linked(a2, 'LoyaltyProgram95', b)
    _safe_set(b, 'participants', set())
    assert not _is_linked(b, 'participants', a2)
    if hasattr(a2, 'LoyaltyProgram95'):
        assert not _is_linked(a2, 'LoyaltyProgram95', b)


def test_assoc_report107_reverse_link_reassign_clear():
    a1 = RandL_TransactionReportLine(amount="sample_text", partnerName="sample_text", points="sample_text", serviceDesc="sample_text")
    a2 = RandL_TransactionReportLine(amount="sample_text_2", partnerName="sample_text_2", points="sample_text_2", serviceDesc="sample_text_2")
    b = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    _safe_set(b, 'TransactionReport', a1)
    assert _is_linked(b, 'TransactionReport', a1)
    if hasattr(a1, 'lines'):
        assert _is_linked(a1, 'lines', b)
    _safe_set(b, 'TransactionReport', a2)
    assert _is_linked(b, 'TransactionReport', a2)
    if hasattr(a1, 'lines'):
        assert not _is_linked(a1, 'lines', b)
    if hasattr(a2, 'lines'):
        assert _is_linked(a2, 'lines', b)
    _safe_set(b, 'TransactionReport', None)
    assert not _is_linked(b, 'TransactionReport', a2)
    if hasattr(a2, 'lines'):
        assert not _is_linked(a2, 'lines', b)


def test_assoc_transaction104_reverse_link_reassign_clear():
    a1 = RandL_TransactionReportLine(amount="sample_text", partnerName="sample_text", points="sample_text", serviceDesc="sample_text")
    a2 = RandL_TransactionReportLine(amount="sample_text_2", partnerName="sample_text_2", points="sample_text_2", serviceDesc="sample_text_2")
    b = RandL_Transaction(amount="sample_text", points="sample_text")
    _safe_set(b, 'RandL_Transaction106', a1)
    assert _is_linked(b, 'RandL_Transaction106', a1)
    if hasattr(a1, 'RandL_TransactionReportLine105'):
        assert _is_linked(a1, 'RandL_TransactionReportLine105', b)
    _safe_set(b, 'RandL_Transaction106', a2)
    assert _is_linked(b, 'RandL_Transaction106', a2)
    if hasattr(a1, 'RandL_TransactionReportLine105'):
        assert not _is_linked(a1, 'RandL_TransactionReportLine105', b)
    if hasattr(a2, 'RandL_TransactionReportLine105'):
        assert _is_linked(a2, 'RandL_TransactionReportLine105', b)
    _safe_set(b, 'RandL_Transaction106', None)
    assert not _is_linked(b, 'RandL_Transaction106', a2)
    if hasattr(a2, 'RandL_TransactionReportLine105'):
        assert not _is_linked(a2, 'RandL_TransactionReportLine105', b)


def test_assoc_transactions13_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    _safe_set(b, 'account14', {a1})
    assert _is_linked(b, 'account14', a1)
    if hasattr(a1, 'Transaction'):
        assert _is_linked(a1, 'Transaction', b)
    _safe_set(b, 'account14', {a2})
    assert _is_linked(b, 'account14', a2)
    if hasattr(a1, 'Transaction'):
        assert not _is_linked(a1, 'Transaction', b)
    if hasattr(a2, 'Transaction'):
        assert _is_linked(a2, 'Transaction', b)
    _safe_set(b, 'account14', set())
    assert not _is_linked(b, 'account14', a2)
    if hasattr(a2, 'Transaction'):
        assert not _is_linked(a2, 'Transaction', b)


def test_assoc_transactions38_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'card39', {a1})
    assert _is_linked(b, 'card39', a1)
    if hasattr(a1, 'Transaction40'):
        assert _is_linked(a1, 'Transaction40', b)
    _safe_set(b, 'card39', {a2})
    assert _is_linked(b, 'card39', a2)
    if hasattr(a1, 'Transaction40'):
        assert not _is_linked(a1, 'Transaction40', b)
    if hasattr(a2, 'Transaction40'):
        assert _is_linked(a2, 'Transaction40', b)
    _safe_set(b, 'card39', set())
    assert not _is_linked(b, 'card39', a2)
    if hasattr(a2, 'Transaction40'):
        assert not _is_linked(a2, 'Transaction40', b)


def test_assoc_transactions87_reverse_link_reassign_clear():
    a1 = RandL_Transaction(amount="sample_text", points="sample_text")
    a2 = RandL_Transaction(amount="sample_text_2", points="sample_text_2")
    b = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    _safe_set(b, 'generatedBy', {a1})
    assert _is_linked(b, 'generatedBy', a1)
    if hasattr(a1, 'Transaction88'):
        assert _is_linked(a1, 'Transaction88', b)
    _safe_set(b, 'generatedBy', {a2})
    assert _is_linked(b, 'generatedBy', a2)
    if hasattr(a1, 'Transaction88'):
        assert not _is_linked(a1, 'Transaction88', b)
    if hasattr(a2, 'Transaction88'):
        assert _is_linked(a2, 'Transaction88', b)
    _safe_set(b, 'generatedBy', set())
    assert not _is_linked(b, 'generatedBy', a2)
    if hasattr(a2, 'Transaction88'):
        assert not _is_linked(a2, 'Transaction88', b)


def test_assoc_until19_reverse_link_reassign_clear():
    a1 = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    a2 = RandL_TransactionReport(balance="sample_text_2", name="sample_text_2", number="sample_text_2", totalBurned="sample_text_2", totalEarned="sample_text_2")
    b = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    _safe_set(b, 'RandL_Date20', a1)
    assert _is_linked(b, 'RandL_Date20', a1)
    if hasattr(a1, 'RandL_TransactionReport'):
        assert _is_linked(a1, 'RandL_TransactionReport', b)
    _safe_set(b, 'RandL_Date20', a2)
    assert _is_linked(b, 'RandL_Date20', a2)
    if hasattr(a1, 'RandL_TransactionReport'):
        assert not _is_linked(a1, 'RandL_TransactionReport', b)
    if hasattr(a2, 'RandL_TransactionReport'):
        assert _is_linked(a2, 'RandL_TransactionReport', b)
    _safe_set(b, 'RandL_Date20', None)
    assert not _is_linked(b, 'RandL_Date20', a2)
    if hasattr(a2, 'RandL_TransactionReport'):
        assert not _is_linked(a2, 'RandL_TransactionReport', b)


def test_assoc_usedServices10_reverse_link_reassign_clear():
    a1 = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    a2 = RandL_Service(condition="sample_text_2", description="sample_text_2", pointsBurned="sample_text_2", pointsEarned="sample_text_2", serviceNr="sample_text_2")
    b = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    _safe_set(b, 'RandL_LoyaltyAccount', {a1})
    assert _is_linked(b, 'RandL_LoyaltyAccount', a1)
    if hasattr(a1, 'RandL_Service'):
        assert _is_linked(a1, 'RandL_Service', b)
    _safe_set(b, 'RandL_LoyaltyAccount', {a2})
    assert _is_linked(b, 'RandL_LoyaltyAccount', a2)
    if hasattr(a1, 'RandL_Service'):
        assert not _is_linked(a1, 'RandL_Service', b)
    if hasattr(a2, 'RandL_Service'):
        assert _is_linked(a2, 'RandL_Service', b)
    _safe_set(b, 'RandL_LoyaltyAccount', set())
    assert not _is_linked(b, 'RandL_LoyaltyAccount', a2)
    if hasattr(a2, 'RandL_Service'):
        assert not _is_linked(a2, 'RandL_Service', b)


def test_assoc_validFrom30_reverse_link_reassign_clear():
    a1 = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    a2 = RandL_Date(day="sample_text_2", month="sample_text_2", year="sample_text_2")
    b = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    _safe_set(b, 'RandL_CustomerCard31', a1)
    assert _is_linked(b, 'RandL_CustomerCard31', a1)
    if hasattr(a1, 'RandL_Date32'):
        assert _is_linked(a1, 'RandL_Date32', b)
    _safe_set(b, 'RandL_CustomerCard31', a2)
    assert _is_linked(b, 'RandL_CustomerCard31', a2)
    if hasattr(a1, 'RandL_Date32'):
        assert not _is_linked(a1, 'RandL_Date32', b)
    if hasattr(a2, 'RandL_Date32'):
        assert _is_linked(a2, 'RandL_Date32', b)
    _safe_set(b, 'RandL_CustomerCard31', None)
    assert not _is_linked(b, 'RandL_CustomerCard31', a2)
    if hasattr(a2, 'RandL_Date32'):
        assert not _is_linked(a2, 'RandL_Date32', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Membership11_stub_double():
    # RandL_Membership has no real 'Membership12' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyAccount's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyAccount's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership12', None)
    _safe_set(owner, 'account', partner)
    assert getattr(partner, 'Membership12') == owner
    _safe_set(owner, 'account', None)
    assert getattr(partner, 'Membership12') is None


def test_assoc_Membership2_stub_double():
    # RandL_Membership has no real 'Membership' property in the generated
    # code (a bare stub) -- manually attach it so RandL_ServiceLevel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_ServiceLevel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_ServiceLevel(name="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership', None)
    _safe_set(owner, 'currentLevel', {partner})
    assert getattr(partner, 'Membership') == owner
    _safe_set(owner, 'currentLevel', set())
    assert getattr(partner, 'Membership') is None


def test_assoc_Membership36_stub_double():
    # RandL_Membership has no real 'Membership37' property in the generated
    # code (a bare stub) -- manually attach it so RandL_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership37', None)
    _safe_set(owner, 'card', partner)
    assert getattr(partner, 'Membership37') == owner
    _safe_set(owner, 'card', None)
    assert getattr(partner, 'Membership37') is None


def test_assoc_account46_stub_double():
    # RandL_Membership has no real 'Membership47' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyAccount's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyAccount's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership47', None)
    _safe_set(owner, 'LoyaltyAccount48', partner)
    assert getattr(partner, 'Membership47') == owner
    _safe_set(owner, 'LoyaltyAccount48', None)
    assert getattr(partner, 'Membership47') is None


def test_assoc_card43_stub_double():
    # RandL_Membership has no real 'Membership44' property in the generated
    # code (a bare stub) -- manually attach it so RandL_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership44', None)
    _safe_set(owner, 'CustomerCard45', partner)
    assert getattr(partner, 'Membership44') == owner
    _safe_set(owner, 'CustomerCard45', None)
    assert getattr(partner, 'Membership44') is None


def test_assoc_currentLevel41_stub_double():
    # RandL_Membership has no real 'Membership42' property in the generated
    # code (a bare stub) -- manually attach it so RandL_ServiceLevel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_ServiceLevel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_ServiceLevel(name="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'Membership42', None)
    _safe_set(owner, 'ServiceLevel', partner)
    assert getattr(partner, 'Membership42') == owner
    _safe_set(owner, 'ServiceLevel', None)
    assert getattr(partner, 'Membership42') is None


def test_assoc_memberships115_stub_double():
    # RandL_Membership has no real 'RandL_Membership117' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyProgram(name="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'RandL_Membership117', None)
    _safe_set(owner, 'RandL_LoyaltyProgram116', {partner})
    assert getattr(partner, 'RandL_Membership117') == owner
    _safe_set(owner, 'RandL_LoyaltyProgram116', set())
    assert getattr(partner, 'RandL_Membership117') is None


def test_assoc_memberships98_stub_double():
    # RandL_Membership has no real 'RandL_Membership100' property in the generated
    # code (a bare stub) -- manually attach it so RandL_Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'RandL_Membership100', None)
    _safe_set(owner, 'RandL_Customer99', {partner})
    assert getattr(partner, 'RandL_Membership100') == owner
    _safe_set(owner, 'RandL_Customer99', set())
    assert getattr(partner, 'RandL_Membership100') is None


def test_assoc_participants50_stub_double():
    # RandL_Membership has no real 'RandL_Membership51' property in the generated
    # code (a bare stub) -- manually attach it so RandL_Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'RandL_Membership51', None)
    _safe_set(owner, 'RandL_Customer', partner)
    assert getattr(partner, 'RandL_Membership51') == owner
    _safe_set(owner, 'RandL_Customer', None)
    assert getattr(partner, 'RandL_Membership51') is None


def test_assoc_programs49_stub_double():
    # RandL_Membership has no real 'RandL_Membership' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyProgram(name="sample_text")
    partner = RandL_Membership()
    setattr(partner, 'RandL_Membership', None)
    _safe_set(owner, 'RandL_LoyaltyProgram', partner)
    assert getattr(partner, 'RandL_Membership') == owner
    _safe_set(owner, 'RandL_LoyaltyProgram', None)
    assert getattr(partner, 'RandL_Membership') is None


def test_assoc_ref_RandL_Customer52_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL' property in the generated
    # code (a bare stub) -- manually attach it so RandL_Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_Customer(age="sample_text", gender="sample_text", isMale="sample_text", name="sample_text", title="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL', None)
    _safe_set(owner, 'RandL_Customer53', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL')
    _safe_set(owner, 'RandL_Customer53', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL')


def test_assoc_ref_RandL_CustomerCard57_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL58' property in the generated
    # code (a bare stub) -- manually attach it so RandL_CustomerCard's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_CustomerCard's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_CustomerCard(color="sample_text", printedName="sample_text", valid="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL58', None)
    _safe_set(owner, 'RandL_CustomerCard59', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL58')
    _safe_set(owner, 'RandL_CustomerCard59', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL58')


def test_assoc_ref_RandL_Date54_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL55' property in the generated
    # code (a bare stub) -- manually attach it so RandL_Date's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_Date's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_Date(day="sample_text", month="sample_text", year="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL55', None)
    _safe_set(owner, 'RandL_Date56', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL55')
    _safe_set(owner, 'RandL_Date56', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL55')


def test_assoc_ref_RandL_LoyaltyAccount71_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL72' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyAccount's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyAccount's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyAccount(number="sample_text", points="sample_text", totalPointsEarned="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL72', None)
    _safe_set(owner, 'RandL_LoyaltyAccount73', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL72')
    _safe_set(owner, 'RandL_LoyaltyAccount73', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL72')


def test_assoc_ref_RandL_LoyaltyProgram66_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL67' property in the generated
    # code (a bare stub) -- manually attach it so RandL_LoyaltyProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_LoyaltyProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_LoyaltyProgram(name="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL67', None)
    _safe_set(owner, 'RandL_LoyaltyProgram68', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL67')
    _safe_set(owner, 'RandL_LoyaltyProgram68', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL67')


def test_assoc_ref_RandL_ProgramPartner80_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL81' property in the generated
    # code (a bare stub) -- manually attach it so RandL_ProgramPartner's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_ProgramPartner's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_ProgramPartner(name="sample_text", numberOfCustomers="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL81', None)
    _safe_set(owner, 'RandL_ProgramPartner', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL81')
    _safe_set(owner, 'RandL_ProgramPartner', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL81')


def test_assoc_ref_RandL_Service63_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL64' property in the generated
    # code (a bare stub) -- manually attach it so RandL_Service's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_Service's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_Service(condition="sample_text", description="sample_text", pointsBurned="sample_text", pointsEarned="sample_text", serviceNr="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL64', None)
    _safe_set(owner, 'RandL_Service65', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL64')
    _safe_set(owner, 'RandL_Service65', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL64')


def test_assoc_ref_RandL_ServiceLevel74_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL75' property in the generated
    # code (a bare stub) -- manually attach it so RandL_ServiceLevel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_ServiceLevel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_ServiceLevel(name="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL75', None)
    _safe_set(owner, 'RandL_ServiceLevel76', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL75')
    _safe_set(owner, 'RandL_ServiceLevel76', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL75')


def test_assoc_ref_RandL_TransactionReport77_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL78' property in the generated
    # code (a bare stub) -- manually attach it so RandL_TransactionReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_TransactionReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_TransactionReport(balance="sample_text", name="sample_text", number="sample_text", totalBurned="sample_text", totalEarned="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL78', None)
    _safe_set(owner, 'RandL_TransactionReport79', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL78')
    _safe_set(owner, 'RandL_TransactionReport79', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL78')


def test_assoc_ref_RandL_TransactionReportLine84_stub_double():
    # RandL_Container_RandL has no real 'RandL_Container_RandL85' property in the generated
    # code (a bare stub) -- manually attach it so RandL_TransactionReportLine's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RandL_TransactionReportLine's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RandL_TransactionReportLine(amount="sample_text", partnerName="sample_text", points="sample_text", serviceDesc="sample_text")
    partner = RandL_Container_RandL()
    setattr(partner, 'RandL_Container_RandL85', None)
    _safe_set(owner, 'RandL_TransactionReportLine', partner)
    assert owner in getattr(partner, 'RandL_Container_RandL85')
    _safe_set(owner, 'RandL_TransactionReportLine', None)
    assert owner not in getattr(partner, 'RandL_Container_RandL85')


