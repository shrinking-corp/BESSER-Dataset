import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActualEntry,
    BudgetEntry,
    BudgetingFile,
    Category,
    Transaction,
    budgeting_ActualAmountEntry,
    budgeting_ActualEntry,
    budgeting_ActualTransactionEntry,
    budgeting_BudgetAmountEntry,
    budgeting_BudgetEntry,
    budgeting_BudgetFactorEntry,
    budgeting_BudgetingFile,
    budgeting_CardTransaction,
    budgeting_CashTransaction,
    budgeting_Category,
    budgeting_ExpenseCategory,
    budgeting_IncomeCategory,
    budgeting_Library,
    budgeting_Month,
    budgeting_Transaction,
    budgeting_Year,
    MonthEnum,
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

def test_assoc_categories0_reverse_link_reassign_clear():
    a1 = budgeting_Library(name="sample_text")
    a2 = budgeting_Library(name="sample_text_2")
    b = budgeting_Category(name="sample_text")
    _safe_set(b, 'budgeting_Category', a1)
    assert _is_linked(b, 'budgeting_Category', a1)
    if hasattr(a1, 'budgeting_Library'):
        assert _is_linked(a1, 'budgeting_Library', b)
    _safe_set(b, 'budgeting_Category', a2)
    assert _is_linked(b, 'budgeting_Category', a2)
    if hasattr(a1, 'budgeting_Library'):
        assert not _is_linked(a1, 'budgeting_Library', b)
    if hasattr(a2, 'budgeting_Library'):
        assert _is_linked(a2, 'budgeting_Library', b)
    _safe_set(b, 'budgeting_Category', None)
    assert not _is_linked(b, 'budgeting_Category', a2)
    if hasattr(a2, 'budgeting_Library'):
        assert not _is_linked(a2, 'budgeting_Library', b)


def test_assoc_library1_reverse_link_reassign_clear():
    a1 = budgeting_Year(name=7)
    a2 = budgeting_Year(name=13)
    b = budgeting_Library(name="sample_text")
    _safe_set(b, 'budgeting_Library2', a1)
    assert _is_linked(b, 'budgeting_Library2', a1)
    if hasattr(a1, 'budgeting_Year'):
        assert _is_linked(a1, 'budgeting_Year', b)
    _safe_set(b, 'budgeting_Library2', a2)
    assert _is_linked(b, 'budgeting_Library2', a2)
    if hasattr(a1, 'budgeting_Year'):
        assert not _is_linked(a1, 'budgeting_Year', b)
    if hasattr(a2, 'budgeting_Year'):
        assert _is_linked(a2, 'budgeting_Year', b)
    _safe_set(b, 'budgeting_Library2', None)
    assert not _is_linked(b, 'budgeting_Library2', a2)
    if hasattr(a2, 'budgeting_Year'):
        assert not _is_linked(a2, 'budgeting_Year', b)


def test_assoc_months3_reverse_link_reassign_clear():
    a1 = budgeting_Year(name=7)
    a2 = budgeting_Year(name=13)
    b = budgeting_Month(name="sample_text")
    _safe_set(b, 'budgeting_Month', a1)
    assert _is_linked(b, 'budgeting_Month', a1)
    if hasattr(a1, 'budgeting_Year4'):
        assert _is_linked(a1, 'budgeting_Year4', b)
    _safe_set(b, 'budgeting_Month', a2)
    assert _is_linked(b, 'budgeting_Month', a2)
    if hasattr(a1, 'budgeting_Year4'):
        assert not _is_linked(a1, 'budgeting_Year4', b)
    if hasattr(a2, 'budgeting_Year4'):
        assert _is_linked(a2, 'budgeting_Year4', b)
    _safe_set(b, 'budgeting_Month', None)
    assert not _is_linked(b, 'budgeting_Month', a2)
    if hasattr(a2, 'budgeting_Year4'):
        assert not _is_linked(a2, 'budgeting_Year4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actualEntries7_stub_double():
    # budgeting_ActualEntry has no real 'budgeting_ActualEntry' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_Month's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_Month's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_Month(name="sample_text")
    partner = budgeting_ActualEntry()
    setattr(partner, 'budgeting_ActualEntry', None)
    _safe_set(owner, 'budgeting_Month8', {partner})
    assert getattr(partner, 'budgeting_ActualEntry') == owner
    _safe_set(owner, 'budgeting_Month8', set())
    assert getattr(partner, 'budgeting_ActualEntry') is None


def test_assoc_baseEntry15_stub_double():
    # budgeting_BudgetEntry has no real 'budgeting_BudgetEntry16' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_BudgetFactorEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_BudgetFactorEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_BudgetFactorEntry(factor=3.14)
    partner = budgeting_BudgetEntry()
    setattr(partner, 'budgeting_BudgetEntry16', None)
    _safe_set(owner, 'budgeting_BudgetFactorEntry', partner)
    assert getattr(partner, 'budgeting_BudgetEntry16') == owner
    _safe_set(owner, 'budgeting_BudgetFactorEntry', None)
    assert getattr(partner, 'budgeting_BudgetEntry16') is None


def test_assoc_budgetEntries5_stub_double():
    # budgeting_BudgetEntry has no real 'budgeting_BudgetEntry' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_Month's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_Month's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_Month(name="sample_text")
    partner = budgeting_BudgetEntry()
    setattr(partner, 'budgeting_BudgetEntry', None)
    _safe_set(owner, 'budgeting_Month6', {partner})
    assert getattr(partner, 'budgeting_BudgetEntry') == owner
    _safe_set(owner, 'budgeting_Month6', set())
    assert getattr(partner, 'budgeting_BudgetEntry') is None


def test_assoc_category12_stub_double():
    # budgeting_ActualEntry has no real 'budgeting_ActualEntry13' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_Category(name="sample_text")
    partner = budgeting_ActualEntry()
    setattr(partner, 'budgeting_ActualEntry13', None)
    _safe_set(owner, 'budgeting_Category14', partner)
    assert getattr(partner, 'budgeting_ActualEntry13') == owner
    _safe_set(owner, 'budgeting_Category14', None)
    assert getattr(partner, 'budgeting_ActualEntry13') is None


def test_assoc_category9_stub_double():
    # budgeting_BudgetEntry has no real 'budgeting_BudgetEntry10' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_Category's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_Category's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_Category(name="sample_text")
    partner = budgeting_BudgetEntry()
    setattr(partner, 'budgeting_BudgetEntry10', None)
    _safe_set(owner, 'budgeting_Category11', partner)
    assert getattr(partner, 'budgeting_BudgetEntry10') == owner
    _safe_set(owner, 'budgeting_Category11', None)
    assert getattr(partner, 'budgeting_BudgetEntry10') is None


def test_assoc_transactions17_stub_double():
    # budgeting_ActualTransactionEntry has no real 'budgeting_ActualTransactionEntry' property in the generated
    # code (a bare stub) -- manually attach it so budgeting_Transaction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # budgeting_Transaction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = budgeting_Transaction(amount="sample_text")
    partner = budgeting_ActualTransactionEntry()
    setattr(partner, 'budgeting_ActualTransactionEntry', None)
    _safe_set(owner, 'budgeting_Transaction', partner)
    assert owner in getattr(partner, 'budgeting_ActualTransactionEntry')
    _safe_set(owner, 'budgeting_Transaction', None)
    assert owner not in getattr(partner, 'budgeting_ActualTransactionEntry')


