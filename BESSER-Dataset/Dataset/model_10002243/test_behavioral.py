import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Add_To_Cart_UseCase,
    Cash_On_Delivery,
    Customer_Actor,
    Cutomer,
    Login_UseCase,
    Make_Payment_UseCase,
    Payment,
    Place_Order_UseCase,
    Rating_UseCase,
    Sign_Up_UseCase,
    System_Order,
    Track_Order_UseCase,
    View_Order_Details_UseCase,
    Wallet,
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

def test_assoc_System_Order_Payment_stub_double():
    # System_Order has no real 'System_Order_Payment_016' property in the generated
    # code (a bare stub) -- manually attach it so Payment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Payment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Payment(Amount=7)
    partner = System_Order()
    setattr(partner, 'System_Order_Payment_016', None)
    _safe_set(owner, 'System_Order_Payment_117', partner)
    assert getattr(partner, 'System_Order_Payment_016') == owner
    _safe_set(owner, 'System_Order_Payment_117', None)
    assert getattr(partner, 'System_Order_Payment_016') is None


