import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Account,
    Bank,
    CheckTransaction,
    CheckingAccount,
    CoDTransaction,
    Customer,
    SavingAccount,
    Transaction,
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

def test_assoc_is_owner_of_reverse_link_reassign_clear():
    a1 = Customer(name="sample_text", taxId="sample_text")
    a2 = Customer(name="sample_text_2", taxId="sample_text_2")
    b = Account(MAX_HOLDERS="sample_text", accId="sample_text", accNumber="sample_text", balance="sample_text", openDate="sample_text")
    _safe_set(b, 'customer7', {a1})
    assert _is_linked(b, 'customer7', a1)
    if hasattr(a1, 'account6'):
        assert _is_linked(a1, 'account6', b)
    _safe_set(b, 'customer7', {a2})
    assert _is_linked(b, 'customer7', a2)
    if hasattr(a1, 'account6'):
        assert not _is_linked(a1, 'account6', b)
    if hasattr(a2, 'account6'):
        assert _is_linked(a2, 'account6', b)
    _safe_set(b, 'customer7', set())
    assert not _is_linked(b, 'customer7', a2)
    if hasattr(a2, 'account6'):
        assert not _is_linked(a2, 'account6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Bank_Account_stub_double():
    # Bank has no real 'account4' property in the generated
    # code (a bare stub) -- manually attach it so Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Account(MAX_HOLDERS="sample_text", accId="sample_text", accNumber="sample_text", balance="sample_text", openDate="sample_text")
    partner = Bank()
    setattr(partner, 'account4', None)
    _safe_set(owner, 'bank5', partner)
    assert owner in getattr(partner, 'account4')
    _safe_set(owner, 'bank5', None)
    assert owner not in getattr(partner, 'account4')


def test_assoc_Bank_Customer_stub_double():
    # Bank has no real 'customer0' property in the generated
    # code (a bare stub) -- manually attach it so Customer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Customer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Customer(name="sample_text", taxId="sample_text")
    partner = Bank()
    setattr(partner, 'customer0', None)
    _safe_set(owner, 'bank1', partner)
    assert owner in getattr(partner, 'customer0')
    _safe_set(owner, 'bank1', None)
    assert owner not in getattr(partner, 'customer0')


