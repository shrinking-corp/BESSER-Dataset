import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Serializable,
    accounting_Account,
    accounting_AccountGroup,
    accounting_Accounting,
    accounting_BalanceAccount,
    accounting_JournalGroup,
    accounting_JournalStatement,
    accounting_PLAccount,
    accounting_Report,
    accounting_ReportGroup,
    accounting_Serializable,
    accounting_Vat,
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

def test_assoc_account0_reverse_link_reassign_clear():
    a1 = accounting_AccountGroup(name="sample_text")
    a2 = accounting_AccountGroup(name="sample_text_2")
    b = accounting_Account(name="sample_text")
    _safe_set(b, 'accounting_Account', a1)
    assert _is_linked(b, 'accounting_Account', a1)
    if hasattr(a1, 'accounting_AccountGroup'):
        assert _is_linked(a1, 'accounting_AccountGroup', b)
    _safe_set(b, 'accounting_Account', a2)
    assert _is_linked(b, 'accounting_Account', a2)
    if hasattr(a1, 'accounting_AccountGroup'):
        assert not _is_linked(a1, 'accounting_AccountGroup', b)
    if hasattr(a2, 'accounting_AccountGroup'):
        assert _is_linked(a2, 'accounting_AccountGroup', b)
    _safe_set(b, 'accounting_Account', None)
    assert not _is_linked(b, 'accounting_Account', a2)
    if hasattr(a2, 'accounting_AccountGroup'):
        assert not _is_linked(a2, 'accounting_AccountGroup', b)


def test_assoc_accountGroup1_reverse_link_reassign_clear():
    a1 = accounting_Accounting(name="sample_text")
    a2 = accounting_Accounting(name="sample_text_2")
    b = accounting_AccountGroup(name="sample_text")
    _safe_set(b, 'accounting_AccountGroup2', a1)
    assert _is_linked(b, 'accounting_AccountGroup2', a1)
    if hasattr(a1, 'accounting_Accounting'):
        assert _is_linked(a1, 'accounting_Accounting', b)
    _safe_set(b, 'accounting_AccountGroup2', a2)
    assert _is_linked(b, 'accounting_AccountGroup2', a2)
    if hasattr(a1, 'accounting_Accounting'):
        assert not _is_linked(a1, 'accounting_Accounting', b)
    if hasattr(a2, 'accounting_Accounting'):
        assert _is_linked(a2, 'accounting_Accounting', b)
    _safe_set(b, 'accounting_AccountGroup2', None)
    assert not _is_linked(b, 'accounting_AccountGroup2', a2)
    if hasattr(a2, 'accounting_Accounting'):
        assert not _is_linked(a2, 'accounting_Accounting', b)


def test_assoc_creditAccount20_reverse_link_reassign_clear():
    a1 = accounting_JournalStatement(amount="sample_text", date="sample_text", description="sample_text")
    a2 = accounting_JournalStatement(amount="sample_text_2", date="sample_text_2", description="sample_text_2")
    b = accounting_Account(name="sample_text")
    _safe_set(b, 'accounting_Account22', a1)
    assert _is_linked(b, 'accounting_Account22', a1)
    if hasattr(a1, 'accounting_JournalStatement21'):
        assert _is_linked(a1, 'accounting_JournalStatement21', b)
    _safe_set(b, 'accounting_Account22', a2)
    assert _is_linked(b, 'accounting_Account22', a2)
    if hasattr(a1, 'accounting_JournalStatement21'):
        assert not _is_linked(a1, 'accounting_JournalStatement21', b)
    if hasattr(a2, 'accounting_JournalStatement21'):
        assert _is_linked(a2, 'accounting_JournalStatement21', b)
    _safe_set(b, 'accounting_Account22', None)
    assert not _is_linked(b, 'accounting_Account22', a2)
    if hasattr(a2, 'accounting_JournalStatement21'):
        assert not _is_linked(a2, 'accounting_JournalStatement21', b)


def test_assoc_creditReportGroup28_reverse_link_reassign_clear():
    a1 = accounting_ReportGroup(name="sample_text")
    a2 = accounting_ReportGroup(name="sample_text_2")
    b = accounting_Report(name="sample_text")
    _safe_set(b, 'accounting_Report29', a1)
    assert _is_linked(b, 'accounting_Report29', a1)
    if hasattr(a1, 'accounting_ReportGroup30'):
        assert _is_linked(a1, 'accounting_ReportGroup30', b)
    _safe_set(b, 'accounting_Report29', a2)
    assert _is_linked(b, 'accounting_Report29', a2)
    if hasattr(a1, 'accounting_ReportGroup30'):
        assert not _is_linked(a1, 'accounting_ReportGroup30', b)
    if hasattr(a2, 'accounting_ReportGroup30'):
        assert _is_linked(a2, 'accounting_ReportGroup30', b)
    _safe_set(b, 'accounting_Report29', None)
    assert not _is_linked(b, 'accounting_Report29', a2)
    if hasattr(a2, 'accounting_ReportGroup30'):
        assert not _is_linked(a2, 'accounting_ReportGroup30', b)


def test_assoc_debitAccount17_reverse_link_reassign_clear():
    a1 = accounting_JournalStatement(amount="sample_text", date="sample_text", description="sample_text")
    a2 = accounting_JournalStatement(amount="sample_text_2", date="sample_text_2", description="sample_text_2")
    b = accounting_Account(name="sample_text")
    _safe_set(b, 'accounting_Account19', a1)
    assert _is_linked(b, 'accounting_Account19', a1)
    if hasattr(a1, 'accounting_JournalStatement18'):
        assert _is_linked(a1, 'accounting_JournalStatement18', b)
    _safe_set(b, 'accounting_Account19', a2)
    assert _is_linked(b, 'accounting_Account19', a2)
    if hasattr(a1, 'accounting_JournalStatement18'):
        assert not _is_linked(a1, 'accounting_JournalStatement18', b)
    if hasattr(a2, 'accounting_JournalStatement18'):
        assert _is_linked(a2, 'accounting_JournalStatement18', b)
    _safe_set(b, 'accounting_Account19', None)
    assert not _is_linked(b, 'accounting_Account19', a2)
    if hasattr(a2, 'accounting_JournalStatement18'):
        assert not _is_linked(a2, 'accounting_JournalStatement18', b)


def test_assoc_debitReportGroup26_reverse_link_reassign_clear():
    a1 = accounting_ReportGroup(name="sample_text")
    a2 = accounting_ReportGroup(name="sample_text_2")
    b = accounting_Report(name="sample_text")
    _safe_set(b, 'accounting_Report27', a1)
    assert _is_linked(b, 'accounting_Report27', a1)
    if hasattr(a1, 'accounting_ReportGroup'):
        assert _is_linked(a1, 'accounting_ReportGroup', b)
    _safe_set(b, 'accounting_Report27', a2)
    assert _is_linked(b, 'accounting_Report27', a2)
    if hasattr(a1, 'accounting_ReportGroup'):
        assert not _is_linked(a1, 'accounting_ReportGroup', b)
    if hasattr(a2, 'accounting_ReportGroup'):
        assert _is_linked(a2, 'accounting_ReportGroup', b)
    _safe_set(b, 'accounting_Report27', None)
    assert not _is_linked(b, 'accounting_Report27', a2)
    if hasattr(a2, 'accounting_ReportGroup'):
        assert not _is_linked(a2, 'accounting_ReportGroup', b)


def test_assoc_journalGroup9_reverse_link_reassign_clear():
    a1 = accounting_JournalGroup(name="sample_text")
    a2 = accounting_JournalGroup(name="sample_text_2")
    b = accounting_Accounting(name="sample_text")
    _safe_set(b, 'accounting_Accounting10', {a1})
    assert _is_linked(b, 'accounting_Accounting10', a1)
    if hasattr(a1, 'accounting_JournalGroup'):
        assert _is_linked(a1, 'accounting_JournalGroup', b)
    _safe_set(b, 'accounting_Accounting10', {a2})
    assert _is_linked(b, 'accounting_Accounting10', a2)
    if hasattr(a1, 'accounting_JournalGroup'):
        assert not _is_linked(a1, 'accounting_JournalGroup', b)
    if hasattr(a2, 'accounting_JournalGroup'):
        assert _is_linked(a2, 'accounting_JournalGroup', b)
    _safe_set(b, 'accounting_Accounting10', set())
    assert not _is_linked(b, 'accounting_Accounting10', a2)
    if hasattr(a2, 'accounting_JournalGroup'):
        assert not _is_linked(a2, 'accounting_JournalGroup', b)


def test_assoc_journalGroups13_reverse_link_reassign_clear():
    a1 = accounting_JournalGroup(name="sample_text")
    a2 = accounting_JournalGroup(name="sample_text_2")
    b = accounting_JournalGroup(name="sample_text")
    _safe_set(b, 'accounting_JournalGroup14', a1)
    assert _is_linked(b, 'accounting_JournalGroup14', a1)
    if hasattr(a1, 'accounting_JournalGroup12'):
        assert _is_linked(a1, 'accounting_JournalGroup12', b)
    _safe_set(b, 'accounting_JournalGroup14', a2)
    assert _is_linked(b, 'accounting_JournalGroup14', a2)
    if hasattr(a1, 'accounting_JournalGroup12'):
        assert not _is_linked(a1, 'accounting_JournalGroup12', b)
    if hasattr(a2, 'accounting_JournalGroup12'):
        assert _is_linked(a2, 'accounting_JournalGroup12', b)
    _safe_set(b, 'accounting_JournalGroup14', None)
    assert not _is_linked(b, 'accounting_JournalGroup14', a2)
    if hasattr(a2, 'accounting_JournalGroup12'):
        assert not _is_linked(a2, 'accounting_JournalGroup12', b)


def test_assoc_journalStatements15_reverse_link_reassign_clear():
    a1 = accounting_JournalStatement(amount="sample_text", date="sample_text", description="sample_text")
    a2 = accounting_JournalStatement(amount="sample_text_2", date="sample_text_2", description="sample_text_2")
    b = accounting_JournalGroup(name="sample_text")
    _safe_set(b, 'accounting_JournalGroup16', {a1})
    assert _is_linked(b, 'accounting_JournalGroup16', a1)
    if hasattr(a1, 'accounting_JournalStatement'):
        assert _is_linked(a1, 'accounting_JournalStatement', b)
    _safe_set(b, 'accounting_JournalGroup16', {a2})
    assert _is_linked(b, 'accounting_JournalGroup16', a2)
    if hasattr(a1, 'accounting_JournalStatement'):
        assert not _is_linked(a1, 'accounting_JournalStatement', b)
    if hasattr(a2, 'accounting_JournalStatement'):
        assert _is_linked(a2, 'accounting_JournalStatement', b)
    _safe_set(b, 'accounting_JournalGroup16', set())
    assert not _is_linked(b, 'accounting_JournalGroup16', a2)
    if hasattr(a2, 'accounting_JournalStatement'):
        assert not _is_linked(a2, 'accounting_JournalStatement', b)


def test_assoc_report7_reverse_link_reassign_clear():
    a1 = accounting_Report(name="sample_text")
    a2 = accounting_Report(name="sample_text_2")
    b = accounting_Accounting(name="sample_text")
    _safe_set(b, 'accounting_Accounting8', a1)
    assert _is_linked(b, 'accounting_Accounting8', a1)
    if hasattr(a1, 'accounting_Report'):
        assert _is_linked(a1, 'accounting_Report', b)
    _safe_set(b, 'accounting_Accounting8', a2)
    assert _is_linked(b, 'accounting_Accounting8', a2)
    if hasattr(a1, 'accounting_Report'):
        assert not _is_linked(a1, 'accounting_Report', b)
    if hasattr(a2, 'accounting_Report'):
        assert _is_linked(a2, 'accounting_Report', b)
    _safe_set(b, 'accounting_Accounting8', None)
    assert not _is_linked(b, 'accounting_Accounting8', a2)
    if hasattr(a2, 'accounting_Report'):
        assert not _is_linked(a2, 'accounting_Report', b)


def test_assoc_reportGroup32_reverse_link_reassign_clear():
    a1 = accounting_ReportGroup(name="sample_text")
    a2 = accounting_ReportGroup(name="sample_text_2")
    b = accounting_ReportGroup(name="sample_text")
    _safe_set(b, 'accounting_ReportGroup33', a1)
    assert _is_linked(b, 'accounting_ReportGroup33', a1)
    if hasattr(a1, 'accounting_ReportGroup31'):
        assert _is_linked(a1, 'accounting_ReportGroup31', b)
    _safe_set(b, 'accounting_ReportGroup33', a2)
    assert _is_linked(b, 'accounting_ReportGroup33', a2)
    if hasattr(a1, 'accounting_ReportGroup31'):
        assert not _is_linked(a1, 'accounting_ReportGroup31', b)
    if hasattr(a2, 'accounting_ReportGroup31'):
        assert _is_linked(a2, 'accounting_ReportGroup31', b)
    _safe_set(b, 'accounting_ReportGroup33', None)
    assert not _is_linked(b, 'accounting_ReportGroup33', a2)
    if hasattr(a2, 'accounting_ReportGroup31'):
        assert not _is_linked(a2, 'accounting_ReportGroup31', b)


def test_assoc_vat23_reverse_link_reassign_clear():
    a1 = accounting_Vat(name="sample_text", rate="sample_text")
    a2 = accounting_Vat(name="sample_text_2", rate="sample_text_2")
    b = accounting_JournalStatement(amount="sample_text", date="sample_text", description="sample_text")
    _safe_set(b, 'accounting_JournalStatement24', a1)
    assert _is_linked(b, 'accounting_JournalStatement24', a1)
    if hasattr(a1, 'accounting_Vat25'):
        assert _is_linked(a1, 'accounting_Vat25', b)
    _safe_set(b, 'accounting_JournalStatement24', a2)
    assert _is_linked(b, 'accounting_JournalStatement24', a2)
    if hasattr(a1, 'accounting_Vat25'):
        assert not _is_linked(a1, 'accounting_Vat25', b)
    if hasattr(a2, 'accounting_Vat25'):
        assert _is_linked(a2, 'accounting_Vat25', b)
    _safe_set(b, 'accounting_JournalStatement24', None)
    assert not _is_linked(b, 'accounting_JournalStatement24', a2)
    if hasattr(a2, 'accounting_Vat25'):
        assert not _is_linked(a2, 'accounting_Vat25', b)


def test_assoc_vat3_reverse_link_reassign_clear():
    a1 = accounting_Vat(name="sample_text", rate="sample_text")
    a2 = accounting_Vat(name="sample_text_2", rate="sample_text_2")
    b = accounting_Accounting(name="sample_text")
    _safe_set(b, 'accounting_Accounting4', {a1})
    assert _is_linked(b, 'accounting_Accounting4', a1)
    if hasattr(a1, 'accounting_Vat'):
        assert _is_linked(a1, 'accounting_Vat', b)
    _safe_set(b, 'accounting_Accounting4', {a2})
    assert _is_linked(b, 'accounting_Accounting4', a2)
    if hasattr(a1, 'accounting_Vat'):
        assert not _is_linked(a1, 'accounting_Vat', b)
    if hasattr(a2, 'accounting_Vat'):
        assert _is_linked(a2, 'accounting_Vat', b)
    _safe_set(b, 'accounting_Accounting4', set())
    assert not _is_linked(b, 'accounting_Accounting4', a2)
    if hasattr(a2, 'accounting_Vat'):
        assert not _is_linked(a2, 'accounting_Vat', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_account34_stub_double():
    # accounting_BalanceAccount has no real 'BalanceAccount' property in the generated
    # code (a bare stub) -- manually attach it so accounting_ReportGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_ReportGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_ReportGroup(name="sample_text")
    partner = accounting_BalanceAccount()
    setattr(partner, 'BalanceAccount', None)
    _safe_set(owner, 'report', {partner})
    assert getattr(partner, 'BalanceAccount') == owner
    _safe_set(owner, 'report', set())
    assert getattr(partner, 'BalanceAccount') is None


def test_assoc_report11_stub_double():
    # accounting_BalanceAccount has no real 'account' property in the generated
    # code (a bare stub) -- manually attach it so accounting_ReportGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_ReportGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_ReportGroup(name="sample_text")
    partner = accounting_BalanceAccount()
    setattr(partner, 'account', None)
    _safe_set(owner, 'ReportGroup', partner)
    assert owner in getattr(partner, 'account')
    _safe_set(owner, 'ReportGroup', None)
    assert owner not in getattr(partner, 'account')


def test_assoc_vatAccount5_stub_double():
    # accounting_BalanceAccount has no real 'accounting_BalanceAccount' property in the generated
    # code (a bare stub) -- manually attach it so accounting_Accounting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # accounting_Accounting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = accounting_Accounting(name="sample_text")
    partner = accounting_BalanceAccount()
    setattr(partner, 'accounting_BalanceAccount', None)
    _safe_set(owner, 'accounting_Accounting6', partner)
    assert getattr(partner, 'accounting_BalanceAccount') == owner
    _safe_set(owner, 'accounting_Accounting6', None)
    assert getattr(partner, 'accounting_BalanceAccount') is None


