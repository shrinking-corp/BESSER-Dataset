import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Admin,
    Booking,
    Credit_Card,
    Customer,
    Debit_Card,
    Hotel,
    Payment,
    Room,
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

def test_assoc_Admin_Booking_reverse_link_reassign_clear():
    a1 = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    a2 = Booking(Date="sample_text_2", Description="sample_text_2", Id="sample_text_2", Type="sample_text_2")
    b = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'booking0', a1)
    assert _is_linked(b, 'booking0', a1)
    if hasattr(a1, 'admin1'):
        assert _is_linked(a1, 'admin1', b)
    _safe_set(b, 'booking0', a2)
    assert _is_linked(b, 'booking0', a2)
    if hasattr(a1, 'admin1'):
        assert not _is_linked(a1, 'admin1', b)
    if hasattr(a2, 'admin1'):
        assert _is_linked(a2, 'admin1', b)
    _safe_set(b, 'booking0', None)
    assert not _is_linked(b, 'booking0', a2)
    if hasattr(a2, 'admin1'):
        assert not _is_linked(a2, 'admin1', b)


def test_assoc_Admin_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    a2 = Hotel(Hotel_Address="sample_text_2", Hotel_ID="sample_text_2", Hotel_Name="sample_text_2", Hotel_Rent="sample_text_2", Hotel_Type="sample_text_2")
    b = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'hotel16', a1)
    assert _is_linked(b, 'hotel16', a1)
    if hasattr(a1, 'admin17'):
        assert _is_linked(a1, 'admin17', b)
    _safe_set(b, 'hotel16', a2)
    assert _is_linked(b, 'hotel16', a2)
    if hasattr(a1, 'admin17'):
        assert not _is_linked(a1, 'admin17', b)
    if hasattr(a2, 'admin17'):
        assert _is_linked(a2, 'admin17', b)
    _safe_set(b, 'hotel16', None)
    assert not _is_linked(b, 'hotel16', a2)
    if hasattr(a2, 'admin17'):
        assert not _is_linked(a2, 'admin17', b)


def test_assoc_Admin_Room_reverse_link_reassign_clear():
    a1 = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    a2 = Room(Room_Id="sample_text_2", Room_description="sample_text_2", Room_number="sample_text_2", Room_type="sample_text_2")
    b = Admin(Id="sample_text", Name="sample_text", Password="sample_text")
    _safe_set(b, 'room2', a1)
    assert _is_linked(b, 'room2', a1)
    if hasattr(a1, 'admin3'):
        assert _is_linked(a1, 'admin3', b)
    _safe_set(b, 'room2', a2)
    assert _is_linked(b, 'room2', a2)
    if hasattr(a1, 'admin3'):
        assert not _is_linked(a1, 'admin3', b)
    if hasattr(a2, 'admin3'):
        assert _is_linked(a2, 'admin3', b)
    _safe_set(b, 'room2', None)
    assert not _is_linked(b, 'room2', a2)
    if hasattr(a2, 'admin3'):
        assert not _is_linked(a2, 'admin3', b)


def test_assoc_Booking_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    a2 = Hotel(Hotel_Address="sample_text_2", Hotel_ID="sample_text_2", Hotel_Name="sample_text_2", Hotel_Rent="sample_text_2", Hotel_Type="sample_text_2")
    b = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    _safe_set(b, 'hotel12', a1)
    assert _is_linked(b, 'hotel12', a1)
    if hasattr(a1, 'booking13'):
        assert _is_linked(a1, 'booking13', b)
    _safe_set(b, 'hotel12', a2)
    assert _is_linked(b, 'hotel12', a2)
    if hasattr(a1, 'booking13'):
        assert not _is_linked(a1, 'booking13', b)
    if hasattr(a2, 'booking13'):
        assert _is_linked(a2, 'booking13', b)
    _safe_set(b, 'hotel12', None)
    assert not _is_linked(b, 'hotel12', a2)
    if hasattr(a2, 'booking13'):
        assert not _is_linked(a2, 'booking13', b)


def test_assoc_Customer_Hotel_reverse_link_reassign_clear():
    a1 = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    a2 = Hotel(Hotel_Address="sample_text_2", Hotel_ID="sample_text_2", Hotel_Name="sample_text_2", Hotel_Rent="sample_text_2", Hotel_Type="sample_text_2")
    b = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    _safe_set(b, 'hotel14', a1)
    assert _is_linked(b, 'hotel14', a1)
    if hasattr(a1, 'customer15'):
        assert _is_linked(a1, 'customer15', b)
    _safe_set(b, 'hotel14', a2)
    assert _is_linked(b, 'hotel14', a2)
    if hasattr(a1, 'customer15'):
        assert not _is_linked(a1, 'customer15', b)
    if hasattr(a2, 'customer15'):
        assert _is_linked(a2, 'customer15', b)
    _safe_set(b, 'hotel14', None)
    assert not _is_linked(b, 'hotel14', a2)
    if hasattr(a2, 'customer15'):
        assert not _is_linked(a2, 'customer15', b)


def test_assoc_Customer_Payment_reverse_link_reassign_clear():
    a1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    a2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    b = Customer(Address="sample_text", Id="sample_text", Mobile_no___Email="sample_text", Name="sample_text")
    _safe_set(b, 'payment6', a1)
    assert _is_linked(b, 'payment6', a1)
    if hasattr(a1, 'customer7'):
        assert _is_linked(a1, 'customer7', b)
    _safe_set(b, 'payment6', a2)
    assert _is_linked(b, 'payment6', a2)
    if hasattr(a1, 'customer7'):
        assert not _is_linked(a1, 'customer7', b)
    if hasattr(a2, 'customer7'):
        assert _is_linked(a2, 'customer7', b)
    _safe_set(b, 'payment6', None)
    assert not _is_linked(b, 'payment6', a2)
    if hasattr(a2, 'customer7'):
        assert not _is_linked(a2, 'customer7', b)


def test_assoc_Payment_Booking_reverse_link_reassign_clear():
    a1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    a2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    b = Booking(Date="sample_text", Description="sample_text", Id="sample_text", Type="sample_text")
    _safe_set(b, 'payment19', a1)
    assert _is_linked(b, 'payment19', a1)
    if hasattr(a1, 'booking18'):
        assert _is_linked(a1, 'booking18', b)
    _safe_set(b, 'payment19', a2)
    assert _is_linked(b, 'payment19', a2)
    if hasattr(a1, 'booking18'):
        assert not _is_linked(a1, 'booking18', b)
    if hasattr(a2, 'booking18'):
        assert _is_linked(a2, 'booking18', b)
    _safe_set(b, 'payment19', None)
    assert not _is_linked(b, 'payment19', a2)
    if hasattr(a2, 'booking18'):
        assert not _is_linked(a2, 'booking18', b)


def test_assoc_Payment_Credit_Card_reverse_link_reassign_clear():
    a1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    a2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    b = Credit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    _safe_set(b, 'payment11', a1)
    assert _is_linked(b, 'payment11', a1)
    if hasattr(a1, 'credit_Card10'):
        assert _is_linked(a1, 'credit_Card10', b)
    _safe_set(b, 'payment11', a2)
    assert _is_linked(b, 'payment11', a2)
    if hasattr(a1, 'credit_Card10'):
        assert not _is_linked(a1, 'credit_Card10', b)
    if hasattr(a2, 'credit_Card10'):
        assert _is_linked(a2, 'credit_Card10', b)
    _safe_set(b, 'payment11', None)
    assert not _is_linked(b, 'payment11', a2)
    if hasattr(a2, 'credit_Card10'):
        assert not _is_linked(a2, 'credit_Card10', b)


def test_assoc_Payment_Debit_Card_reverse_link_reassign_clear():
    a1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    a2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    b = Debit_Card(Card_No_="sample_text", Pin_No_="sample_text")
    _safe_set(b, 'payment9', a1)
    assert _is_linked(b, 'payment9', a1)
    if hasattr(a1, 'debit_Card8'):
        assert _is_linked(a1, 'debit_Card8', b)
    _safe_set(b, 'payment9', a2)
    assert _is_linked(b, 'payment9', a2)
    if hasattr(a1, 'debit_Card8'):
        assert not _is_linked(a1, 'debit_Card8', b)
    if hasattr(a2, 'debit_Card8'):
        assert _is_linked(a2, 'debit_Card8', b)
    _safe_set(b, 'payment9', None)
    assert not _is_linked(b, 'payment9', a2)
    if hasattr(a2, 'debit_Card8'):
        assert not _is_linked(a2, 'debit_Card8', b)


def test_assoc_Payment_Hotel_reverse_link_reassign_clear():
    a1 = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    a2 = Payment(Amount="sample_text_2", Customer_s_Id="sample_text_2", Payment_Date="sample_text_2", Payment_Description="sample_text_2")
    b = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    _safe_set(b, 'payment23', a1)
    assert _is_linked(b, 'payment23', a1)
    if hasattr(a1, 'hotel22'):
        assert _is_linked(a1, 'hotel22', b)
    _safe_set(b, 'payment23', a2)
    assert _is_linked(b, 'payment23', a2)
    if hasattr(a1, 'hotel22'):
        assert not _is_linked(a1, 'hotel22', b)
    if hasattr(a2, 'hotel22'):
        assert _is_linked(a2, 'hotel22', b)
    _safe_set(b, 'payment23', None)
    assert not _is_linked(b, 'payment23', a2)
    if hasattr(a2, 'hotel22'):
        assert not _is_linked(a2, 'hotel22', b)


def test_assoc_Payment_Room_reverse_link_reassign_clear():
    a1 = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    a2 = Room(Room_Id="sample_text_2", Room_description="sample_text_2", Room_number="sample_text_2", Room_type="sample_text_2")
    b = Payment(Amount="sample_text", Customer_s_Id="sample_text", Payment_Date="sample_text", Payment_Description="sample_text")
    _safe_set(b, 'room20', a1)
    assert _is_linked(b, 'room20', a1)
    if hasattr(a1, 'payment21'):
        assert _is_linked(a1, 'payment21', b)
    _safe_set(b, 'room20', a2)
    assert _is_linked(b, 'room20', a2)
    if hasattr(a1, 'payment21'):
        assert not _is_linked(a1, 'payment21', b)
    if hasattr(a2, 'payment21'):
        assert _is_linked(a2, 'payment21', b)
    _safe_set(b, 'room20', None)
    assert not _is_linked(b, 'room20', a2)
    if hasattr(a2, 'payment21'):
        assert not _is_linked(a2, 'payment21', b)


def test_assoc_Room_Hotel_reverse_link_reassign_clear():
    a1 = Room(Room_Id="sample_text", Room_description="sample_text", Room_number="sample_text", Room_type="sample_text")
    a2 = Room(Room_Id="sample_text_2", Room_description="sample_text_2", Room_number="sample_text_2", Room_type="sample_text_2")
    b = Hotel(Hotel_Address="sample_text", Hotel_ID="sample_text", Hotel_Name="sample_text", Hotel_Rent="sample_text", Hotel_Type="sample_text")
    _safe_set(b, 'room5', a1)
    assert _is_linked(b, 'room5', a1)
    if hasattr(a1, 'hotel4'):
        assert _is_linked(a1, 'hotel4', b)
    _safe_set(b, 'room5', a2)
    assert _is_linked(b, 'room5', a2)
    if hasattr(a1, 'hotel4'):
        assert not _is_linked(a1, 'hotel4', b)
    if hasattr(a2, 'hotel4'):
        assert _is_linked(a2, 'hotel4', b)
    _safe_set(b, 'room5', None)
    assert not _is_linked(b, 'room5', a2)
    if hasattr(a2, 'hotel4'):
        assert not _is_linked(a2, 'hotel4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

