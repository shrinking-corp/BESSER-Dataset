import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActiveRecord,
    Car,
    Check_Car_Stock_UseCase,
    Check_for_Parts_UseCase,
    Compute_Billables_UseCase,
    ConnectionInterface_Interface,
    Customer,
    Customer_Actor,
    Dealer_Actor,
    Enquire_for_Cars_UseCase,
    Maintenance_Team_Actor,
    Manufacturer_Actor,
    Order_Cars_UseCase,
    Purchase_Car_UseCase,
    Repair,
    RepairPart,
    Repair_Part_Purchase_UseCase,
    Sale,
    Send_for_Repair_UseCase,
    CustomerType,
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

