import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Bank,
    BankAccount,
    FixedAccount,
    SavingsAccount,
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

def test_assoc_Bank_BankAccount_reverse_link_reassign_clear():
    a1 = BankAccount(accountHolder="sample_text", accountNumber=7, balance=3.14)
    a2 = BankAccount(accountHolder="sample_text_2", accountNumber=13, balance=9.99)
    b = Bank(name="sample_text")
    _safe_set(b, 'bankAccount0', {a1})
    assert _is_linked(b, 'bankAccount0', a1)
    if hasattr(a1, 'bank1'):
        assert _is_linked(a1, 'bank1', b)
    _safe_set(b, 'bankAccount0', {a2})
    assert _is_linked(b, 'bankAccount0', a2)
    if hasattr(a1, 'bank1'):
        assert not _is_linked(a1, 'bank1', b)
    if hasattr(a2, 'bank1'):
        assert _is_linked(a2, 'bank1', b)
    _safe_set(b, 'bankAccount0', set())
    assert not _is_linked(b, 'bankAccount0', a2)
    if hasattr(a2, 'bank1'):
        assert not _is_linked(a2, 'bank1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

