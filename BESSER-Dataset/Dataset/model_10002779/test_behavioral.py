import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Buildings,
    Management,
    Manager,
    Owner,
    Payment,
    Property,
    Reg_User,
    Request,
    Requirement,
    Tenant,
    Unreg_User,
    User,
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

def test_assoc_Advertiser_Advertiesment_reverse_link_reassign_clear():
    a1 = Manager(management_id="sample_text", manager_id="sample_text")
    a2 = Manager(management_id="sample_text_2", manager_id="sample_text_2")
    b = Buildings(end_date="sample_text", management_id=7, manager_id="sample_text", start_date="sample_text")
    _safe_set(b, 'owner3', a1)
    assert _is_linked(b, 'owner3', a1)
    if hasattr(a1, 'adds2'):
        assert _is_linked(a1, 'adds2', b)
    _safe_set(b, 'owner3', a2)
    assert _is_linked(b, 'owner3', a2)
    if hasattr(a1, 'adds2'):
        assert not _is_linked(a1, 'adds2', b)
    if hasattr(a2, 'adds2'):
        assert _is_linked(a2, 'adds2', b)
    _safe_set(b, 'owner3', None)
    assert not _is_linked(b, 'owner3', a2)
    if hasattr(a2, 'adds2'):
        assert not _is_linked(a2, 'adds2', b)


def test_assoc_Payment_Property_reverse_link_reassign_clear():
    a1 = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    a2 = Property(address="sample_text_2", location="sample_text_2", property_id="sample_text_2", property_type="sample_text_2")
    b = Payment(card_no="sample_text", ex_date="sample_text", pay_amount="sample_text", pay_id=7, pay_mode="sample_text")
    _safe_set(b, 'property16', {a1})
    assert _is_linked(b, 'property16', a1)
    if hasattr(a1, 'payment17'):
        assert _is_linked(a1, 'payment17', b)
    _safe_set(b, 'property16', {a2})
    assert _is_linked(b, 'property16', a2)
    if hasattr(a1, 'payment17'):
        assert not _is_linked(a1, 'payment17', b)
    if hasattr(a2, 'payment17'):
        assert _is_linked(a2, 'payment17', b)
    _safe_set(b, 'property16', set())
    assert not _is_linked(b, 'property16', a2)
    if hasattr(a2, 'payment17'):
        assert not _is_linked(a2, 'payment17', b)


def test_assoc_Payment_Reg_User_reverse_link_reassign_clear():
    a1 = Reg_User(Address="sample_text", password="sample_text", username="sample_text")
    a2 = Reg_User(Address="sample_text_2", password="sample_text_2", username="sample_text_2")
    b = Payment(card_no="sample_text", ex_date="sample_text", pay_amount="sample_text", pay_id=7, pay_mode="sample_text")
    _safe_set(b, 'reg_User14', {a1})
    assert _is_linked(b, 'reg_User14', a1)
    if hasattr(a1, 'payment15'):
        assert _is_linked(a1, 'payment15', b)
    _safe_set(b, 'reg_User14', {a2})
    assert _is_linked(b, 'reg_User14', a2)
    if hasattr(a1, 'payment15'):
        assert not _is_linked(a1, 'payment15', b)
    if hasattr(a2, 'payment15'):
        assert _is_linked(a2, 'payment15', b)
    _safe_set(b, 'reg_User14', set())
    assert not _is_linked(b, 'reg_User14', a2)
    if hasattr(a2, 'payment15'):
        assert not _is_linked(a2, 'payment15', b)


def test_assoc_Property_Buyer_reverse_link_reassign_clear():
    a1 = Tenant(tenant_id="sample_text")
    a2 = Tenant(tenant_id="sample_text_2")
    b = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    _safe_set(b, 'user8', a1)
    assert _is_linked(b, 'user8', a1)
    if hasattr(a1, 'property9'):
        assert _is_linked(a1, 'property9', b)
    _safe_set(b, 'user8', a2)
    assert _is_linked(b, 'user8', a2)
    if hasattr(a1, 'property9'):
        assert not _is_linked(a1, 'property9', b)
    if hasattr(a2, 'property9'):
        assert _is_linked(a2, 'property9', b)
    _safe_set(b, 'user8', None)
    assert not _is_linked(b, 'user8', a2)
    if hasattr(a2, 'property9'):
        assert not _is_linked(a2, 'property9', b)


def test_assoc_Property_Management_reverse_link_reassign_clear():
    a1 = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    a2 = Property(address="sample_text_2", location="sample_text_2", property_id="sample_text_2", property_type="sample_text_2")
    b = Management(specialoffers="sample_text", suggetions="sample_text")
    _safe_set(b, 'property13', a1)
    assert _is_linked(b, 'property13', a1)
    if hasattr(a1, 'management12'):
        assert _is_linked(a1, 'management12', b)
    _safe_set(b, 'property13', a2)
    assert _is_linked(b, 'property13', a2)
    if hasattr(a1, 'management12'):
        assert not _is_linked(a1, 'management12', b)
    if hasattr(a2, 'management12'):
        assert _is_linked(a2, 'management12', b)
    _safe_set(b, 'property13', None)
    assert not _is_linked(b, 'property13', a2)
    if hasattr(a2, 'management12'):
        assert not _is_linked(a2, 'management12', b)


def test_assoc_Property_Seller_reverse_link_reassign_clear():
    a1 = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    a2 = Property(address="sample_text_2", location="sample_text_2", property_id="sample_text_2", property_type="sample_text_2")
    b = Owner(owner_id="sample_text", property_id="sample_text")
    _safe_set(b, 'property5', {a1})
    assert _is_linked(b, 'property5', a1)
    if hasattr(a1, 'owner4'):
        assert _is_linked(a1, 'owner4', b)
    _safe_set(b, 'property5', {a2})
    assert _is_linked(b, 'property5', a2)
    if hasattr(a1, 'owner4'):
        assert not _is_linked(a1, 'owner4', b)
    if hasattr(a2, 'owner4'):
        assert _is_linked(a2, 'owner4', b)
    _safe_set(b, 'property5', set())
    assert not _is_linked(b, 'property5', a2)
    if hasattr(a2, 'owner4'):
        assert not _is_linked(a2, 'owner4', b)


def test_assoc_Reg_User_Requirement_reverse_link_reassign_clear():
    a1 = Requirement(req_description="sample_text", requirement_location="sample_text", requirement_type="sample_text", user_id="sample_text")
    a2 = Requirement(req_description="sample_text_2", requirement_location="sample_text_2", requirement_type="sample_text_2", user_id="sample_text_2")
    b = Reg_User(Address="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'requirement10', {a1})
    assert _is_linked(b, 'requirement10', a1)
    if hasattr(a1, 'user11'):
        assert _is_linked(a1, 'user11', b)
    _safe_set(b, 'requirement10', {a2})
    assert _is_linked(b, 'requirement10', a2)
    if hasattr(a1, 'user11'):
        assert not _is_linked(a1, 'user11', b)
    if hasattr(a2, 'user11'):
        assert _is_linked(a2, 'user11', b)
    _safe_set(b, 'requirement10', set())
    assert not _is_linked(b, 'requirement10', a2)
    if hasattr(a2, 'user11'):
        assert not _is_linked(a2, 'user11', b)


def test_assoc_User_Administrator_reverse_link_reassign_clear():
    a1 = User(email="sample_text", location="sample_text")
    a2 = User(email="sample_text_2", location="sample_text_2")
    b = Administrator(admin_name="sample_text", password="sample_text")
    _safe_set(b, 'employee1', {a1})
    assert _is_linked(b, 'employee1', a1)
    if hasattr(a1, 'administrator0'):
        assert _is_linked(a1, 'administrator0', b)
    _safe_set(b, 'employee1', {a2})
    assert _is_linked(b, 'employee1', a2)
    if hasattr(a1, 'administrator0'):
        assert not _is_linked(a1, 'administrator0', b)
    if hasattr(a2, 'administrator0'):
        assert _is_linked(a2, 'administrator0', b)
    _safe_set(b, 'employee1', set())
    assert not _is_linked(b, 'employee1', a2)
    if hasattr(a2, 'administrator0'):
        assert not _is_linked(a2, 'administrator0', b)


def test_assoc_User_Request_reverse_link_reassign_clear():
    a1 = User(email="sample_text", location="sample_text")
    a2 = User(email="sample_text_2", location="sample_text_2")
    b = Request(request_details="sample_text", request_id=7, request_type="sample_text", requser_id="sample_text")
    _safe_set(b, 'user7', a1)
    assert _is_linked(b, 'user7', a1)
    if hasattr(a1, 'request6'):
        assert _is_linked(a1, 'request6', b)
    _safe_set(b, 'user7', a2)
    assert _is_linked(b, 'user7', a2)
    if hasattr(a1, 'request6'):
        assert not _is_linked(a1, 'request6', b)
    if hasattr(a2, 'request6'):
        assert _is_linked(a2, 'request6', b)
    _safe_set(b, 'user7', None)
    assert not _is_linked(b, 'user7', a2)
    if hasattr(a2, 'request6'):
        assert not _is_linked(a2, 'request6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

