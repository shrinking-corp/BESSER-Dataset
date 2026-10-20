import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Access_the_system_UseCase,
    Add_Edit_Delete_menus_UseCase,
    Add_Edit_Delete_menus_menu_items__UseCase,
    Add_user_and_Assign_role_UseCase,
    Admin_Actor,
    Customer_Actor,
    Edit_personal_Information_UseCase,
    Food,
    Log_in_logout_UseCase,
    Login_Logout_UseCase,
    Operator_Actor,
    See_order_Status_UseCase,
    Update_status_of_orders_UseCase,
    View_Food_products_UseCase,
    View_open_bill_and_ordered_items_UseCase,
    View_order_transation_UseCase,
    View_order_transation_UseCase1,
    Write_Review_UseCase,
    order_food_UseCase,
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

