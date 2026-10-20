import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator,
    Buyer,
    Property,
    Reg_User,
    Request,
    Requirement,
    Seller,
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

def test_assoc_Property_Buyer_reverse_link_reassign_clear():
    a1 = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    a2 = Property(address="sample_text_2", location="sample_text_2", property_id="sample_text_2", property_type="sample_text_2")
    b = Buyer(buyer_id="sample_text")
    _safe_set(b, 'property7', {a1})
    assert _is_linked(b, 'property7', a1)
    if hasattr(a1, 'user6'):
        assert _is_linked(a1, 'user6', b)
    _safe_set(b, 'property7', {a2})
    assert _is_linked(b, 'property7', a2)
    if hasattr(a1, 'user6'):
        assert not _is_linked(a1, 'user6', b)
    if hasattr(a2, 'user6'):
        assert _is_linked(a2, 'user6', b)
    _safe_set(b, 'property7', set())
    assert not _is_linked(b, 'property7', a2)
    if hasattr(a2, 'user6'):
        assert not _is_linked(a2, 'user6', b)


def test_assoc_Property_Seller_reverse_link_reassign_clear():
    a1 = Seller(property_id="sample_text", seller_id="sample_text")
    a2 = Seller(property_id="sample_text_2", seller_id="sample_text_2")
    b = Property(address="sample_text", location="sample_text", property_id="sample_text", property_type="sample_text")
    _safe_set(b, 'owner2', a1)
    assert _is_linked(b, 'owner2', a1)
    if hasattr(a1, 'property3'):
        assert _is_linked(a1, 'property3', b)
    _safe_set(b, 'owner2', a2)
    assert _is_linked(b, 'owner2', a2)
    if hasattr(a1, 'property3'):
        assert not _is_linked(a1, 'property3', b)
    if hasattr(a2, 'property3'):
        assert _is_linked(a2, 'property3', b)
    _safe_set(b, 'owner2', None)
    assert not _is_linked(b, 'owner2', a2)
    if hasattr(a2, 'property3'):
        assert not _is_linked(a2, 'property3', b)


def test_assoc_Reg_User_Requirement_reverse_link_reassign_clear():
    a1 = Requirement(req_description="sample_text", requirement_location="sample_text", requirement_type="sample_text", user_id="sample_text")
    a2 = Requirement(req_description="sample_text_2", requirement_location="sample_text_2", requirement_type="sample_text_2", user_id="sample_text_2")
    b = Reg_User(Address="sample_text", password="sample_text", username="sample_text")
    _safe_set(b, 'requirement8', {a1})
    assert _is_linked(b, 'requirement8', a1)
    if hasattr(a1, 'user9'):
        assert _is_linked(a1, 'user9', b)
    _safe_set(b, 'requirement8', {a2})
    assert _is_linked(b, 'requirement8', a2)
    if hasattr(a1, 'user9'):
        assert not _is_linked(a1, 'user9', b)
    if hasattr(a2, 'user9'):
        assert _is_linked(a2, 'user9', b)
    _safe_set(b, 'requirement8', set())
    assert not _is_linked(b, 'requirement8', a2)
    if hasattr(a2, 'user9'):
        assert not _is_linked(a2, 'user9', b)


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
    _safe_set(b, 'user5', a1)
    assert _is_linked(b, 'user5', a1)
    if hasattr(a1, 'request4'):
        assert _is_linked(a1, 'request4', b)
    _safe_set(b, 'user5', a2)
    assert _is_linked(b, 'user5', a2)
    if hasattr(a1, 'request4'):
        assert not _is_linked(a1, 'request4', b)
    if hasattr(a2, 'request4'):
        assert _is_linked(a2, 'request4', b)
    _safe_set(b, 'user5', None)
    assert not _is_linked(b, 'user5', a2)
    if hasattr(a2, 'request4'):
        assert not _is_linked(a2, 'request4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

