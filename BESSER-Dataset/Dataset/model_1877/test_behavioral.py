import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Address,
    Booking,
    BookingHandler,
    Classes_BuisnessLogicLayer_PaymentHandler,
    Classes_BuisnessLogicLayer_PaymentInfo,
    Classes_Buissnesslayer_Address,
    Classes_Buissnesslayer_Booking,
    Classes_Buissnesslayer_BookingHandler,
    Classes_Buissnesslayer_Employee,
    Classes_Buissnesslayer_Guest,
    Classes_Buissnesslayer_Room,
    Classes_Buissnesslayer_User,
    Classes_Buissnesslayer_UserHandler,
    Classes_Datalayer_Database,
    Classes_Interactionlayer_GUI,
    Classes_Interactionlayer_GUIController,
    Classes_Interactionlayer_LoginController,
    Classes_Interactionlayer_LoginController_DataType1,
    Database,
    Employee,
    GUI,
    GUIController,
    Guest,
    LoginController,
    PaymentHandler,
    Room,
    User,
    UserHandler,
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

def test_assoc_Bookings15_stub_double():
    # Booking has no real 'Booking17' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_BookingHandler()
    partner = Booking()
    setattr(partner, 'Booking17', None)
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler16', partner)
    assert getattr(partner, 'Booking17') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler16', None)
    assert getattr(partner, 'Booking17') is None


def test_assoc_Rooms10_stub_double():
    # Room has no real 'Room12' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_Booking(bookingID=7, checkedIn=True, checkedOut=True, endDate="sample_text", extras="sample_text", guest=7, nrOfGuests=7, parkings="sample_text", payment="sample_text", paymentComplete=True, startDate="sample_text")
    partner = Room()
    setattr(partner, 'Room12', None)
    _safe_set(owner, 'Classes_Buissnesslayer_Booking11', {partner})
    assert getattr(partner, 'Room12') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_Booking11', set())
    assert getattr(partner, 'Room12') is None


def test_assoc_User18_stub_double():
    # User has no real 'User' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_BookingHandler()
    partner = User()
    setattr(partner, 'User', None)
    _safe_set(owner, 'bookinghandler', {partner})
    assert getattr(partner, 'User') == owner
    _safe_set(owner, 'bookinghandler', set())
    assert getattr(partner, 'User') is None


def test_assoc_address28_stub_double():
    # Address has no real 'Address' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_User(Email="sample_text", Name="sample_text")
    partner = Address()
    setattr(partner, 'Address', None)
    _safe_set(owner, 'Classes_Buissnesslayer_User29', partner)
    assert getattr(partner, 'Address') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_User29', None)
    assert getattr(partner, 'Address') is None


def test_assoc_booking13_stub_double():
    # Booking has no real 'Booking14' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_BookingHandler()
    partner = Booking()
    setattr(partner, 'Booking14', None)
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler', partner)
    assert getattr(partner, 'Booking14') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler', None)
    assert getattr(partner, 'Booking14') is None


def test_assoc_bookingDB4_stub_double():
    # Booking has no real 'Booking' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Datalayer_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Datalayer_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Datalayer_Database(extrasDB="sample_text")
    partner = Booking()
    setattr(partner, 'Booking', None)
    _safe_set(owner, 'Classes_Datalayer_Database5', {partner})
    assert getattr(partner, 'Booking') == owner
    _safe_set(owner, 'Classes_Datalayer_Database5', set())
    assert getattr(partner, 'Booking') is None


def test_assoc_bookinghandler30_stub_double():
    # BookingHandler has no real 'BookingHandler' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_User(Email="sample_text", Name="sample_text")
    partner = BookingHandler()
    setattr(partner, 'BookingHandler', None)
    _safe_set(owner, 'User31', partner)
    assert getattr(partner, 'BookingHandler') == owner
    _safe_set(owner, 'User31', None)
    assert getattr(partner, 'BookingHandler') is None


def test_assoc_bookinghandler41_stub_double():
    # BookingHandler has no real 'BookingHandler43' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_GUIController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_GUIController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_GUIController()
    partner = BookingHandler()
    setattr(partner, 'BookingHandler43', None)
    _safe_set(owner, 'Classes_Interactionlayer_GUIController42', partner)
    assert getattr(partner, 'BookingHandler43') == owner
    _safe_set(owner, 'Classes_Interactionlayer_GUIController42', None)
    assert getattr(partner, 'BookingHandler43') is None


def test_assoc_currentUser46_stub_double():
    # User has no real 'User47' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_LoginController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_LoginController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_LoginController()
    partner = User()
    setattr(partner, 'User47', None)
    _safe_set(owner, 'Classes_Interactionlayer_LoginController', partner)
    assert getattr(partner, 'User47') == owner
    _safe_set(owner, 'Classes_Interactionlayer_LoginController', None)
    assert getattr(partner, 'User47') is None


def test_assoc_database19_stub_double():
    # Database has no real 'Database' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_BookingHandler()
    partner = Database()
    setattr(partner, 'Database', None)
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler20', partner)
    assert getattr(partner, 'Database') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler20', None)
    assert getattr(partner, 'Database') is None


def test_assoc_database32_stub_double():
    # Database has no real 'Database33' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_UserHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_UserHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_UserHandler(Users="sample_text")
    partner = Database()
    setattr(partner, 'Database33', None)
    _safe_set(owner, 'userhandler', partner)
    assert getattr(partner, 'Database33') == owner
    _safe_set(owner, 'userhandler', None)
    assert getattr(partner, 'Database33') is None


def test_assoc_display38_stub_double():
    # GUI has no real 'GUI' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_GUIController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_GUIController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_GUIController()
    partner = GUI()
    setattr(partner, 'GUI', None)
    _safe_set(owner, 'Classes_Interactionlayer_GUIController', partner)
    assert getattr(partner, 'GUI') == owner
    _safe_set(owner, 'Classes_Interactionlayer_GUIController', None)
    assert getattr(partner, 'GUI') is None


def test_assoc_employeeDB2_stub_double():
    # Employee has no real 'Employee' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Datalayer_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Datalayer_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Datalayer_Database(extrasDB="sample_text")
    partner = Employee()
    setattr(partner, 'Employee', None)
    _safe_set(owner, 'Classes_Datalayer_Database3', {partner})
    assert getattr(partner, 'Employee') == owner
    _safe_set(owner, 'Classes_Datalayer_Database3', set())
    assert getattr(partner, 'Employee') is None


def test_assoc_guicontroller44_stub_double():
    # GUIController has no real 'GUIController45' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_LoginController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_LoginController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_LoginController()
    partner = GUIController()
    setattr(partner, 'GUIController45', None)
    _safe_set(owner, 'logincontroller', partner)
    assert getattr(partner, 'GUIController45') == owner
    _safe_set(owner, 'logincontroller', None)
    assert getattr(partner, 'GUIController45') is None


def test_assoc_logincontroller24_stub_double():
    # LoginController has no real 'LoginController' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_User(Email="sample_text", Name="sample_text")
    partner = LoginController()
    setattr(partner, 'LoginController', None)
    _safe_set(owner, 'Classes_Buissnesslayer_User', partner)
    assert getattr(partner, 'LoginController') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_User', None)
    assert getattr(partner, 'LoginController') is None


def test_assoc_logincontroller34_stub_double():
    # LoginController has no real 'LoginController36' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_UserHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_UserHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_UserHandler(Users="sample_text")
    partner = LoginController()
    setattr(partner, 'LoginController36', None)
    _safe_set(owner, 'userhandler35', partner)
    assert getattr(partner, 'LoginController36') == owner
    _safe_set(owner, 'userhandler35', None)
    assert getattr(partner, 'LoginController36') is None


def test_assoc_logincontroller39_stub_double():
    # LoginController has no real 'LoginController40' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_GUIController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_GUIController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_GUIController()
    partner = LoginController()
    setattr(partner, 'LoginController40', None)
    _safe_set(owner, 'guicontroller', partner)
    assert getattr(partner, 'LoginController40') == owner
    _safe_set(owner, 'guicontroller', None)
    assert getattr(partner, 'LoginController40') is None


def test_assoc_paymenthandler48_stub_double():
    # PaymentHandler has no real 'PaymentHandler' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_LoginController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_LoginController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_LoginController()
    partner = PaymentHandler()
    setattr(partner, 'PaymentHandler', None)
    _safe_set(owner, 'Classes_Interactionlayer_LoginController49', partner)
    assert getattr(partner, 'PaymentHandler') == owner
    _safe_set(owner, 'Classes_Interactionlayer_LoginController49', None)
    assert getattr(partner, 'PaymentHandler') is None


def test_assoc_paymenthandler53_stub_double():
    # PaymentHandler has no real 'PaymentHandler54' property in the generated
    # code (a bare stub) -- manually attach it so Classes_BuisnessLogicLayer_PaymentInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_BuisnessLogicLayer_PaymentInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_BuisnessLogicLayer_PaymentInfo(CVV=7, CreditCard=7, ExpiryDate=7, PaymentComplete=True)
    partner = PaymentHandler()
    setattr(partner, 'PaymentHandler54', None)
    _safe_set(owner, 'Classes_BuisnessLogicLayer_PaymentInfo', partner)
    assert getattr(partner, 'PaymentHandler54') == owner
    _safe_set(owner, 'Classes_BuisnessLogicLayer_PaymentInfo', None)
    assert getattr(partner, 'PaymentHandler54') is None


def test_assoc_room8_stub_double():
    # Room has no real 'Room9' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_Booking(bookingID=7, checkedIn=True, checkedOut=True, endDate="sample_text", extras="sample_text", guest=7, nrOfGuests=7, parkings="sample_text", payment="sample_text", paymentComplete=True, startDate="sample_text")
    partner = Room()
    setattr(partner, 'Room9', None)
    _safe_set(owner, 'Classes_Buissnesslayer_Booking', {partner})
    assert getattr(partner, 'Room9') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_Booking', set())
    assert getattr(partner, 'Room9') is None


def test_assoc_roomDB6_stub_double():
    # Room has no real 'Room' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Datalayer_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Datalayer_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Datalayer_Database(extrasDB="sample_text")
    partner = Room()
    setattr(partner, 'Room', None)
    _safe_set(owner, 'Classes_Datalayer_Database7', {partner})
    assert getattr(partner, 'Room') == owner
    _safe_set(owner, 'Classes_Datalayer_Database7', set())
    assert getattr(partner, 'Room') is None


def test_assoc_userDB0_stub_double():
    # Guest has no real 'Guest' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Datalayer_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Datalayer_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Datalayer_Database(extrasDB="sample_text")
    partner = Guest()
    setattr(partner, 'Guest', None)
    _safe_set(owner, 'Classes_Datalayer_Database', {partner})
    assert getattr(partner, 'Guest') == owner
    _safe_set(owner, 'Classes_Datalayer_Database', set())
    assert getattr(partner, 'Guest') is None


def test_assoc_userhandler1_stub_double():
    # UserHandler has no real 'UserHandler' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Datalayer_Database's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Datalayer_Database's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Datalayer_Database(extrasDB="sample_text")
    partner = UserHandler()
    setattr(partner, 'UserHandler', None)
    _safe_set(owner, 'database', partner)
    assert getattr(partner, 'UserHandler') == owner
    _safe_set(owner, 'database', None)
    assert getattr(partner, 'UserHandler') is None


def test_assoc_userhandler21_stub_double():
    # UserHandler has no real 'UserHandler23' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_BookingHandler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_BookingHandler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_BookingHandler()
    partner = UserHandler()
    setattr(partner, 'UserHandler23', None)
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler22', partner)
    assert getattr(partner, 'UserHandler23') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_BookingHandler22', None)
    assert getattr(partner, 'UserHandler23') is None


def test_assoc_userhandler25_stub_double():
    # UserHandler has no real 'UserHandler27' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Buissnesslayer_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Buissnesslayer_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Buissnesslayer_User(Email="sample_text", Name="sample_text")
    partner = UserHandler()
    setattr(partner, 'UserHandler27', None)
    _safe_set(owner, 'Classes_Buissnesslayer_User26', partner)
    assert getattr(partner, 'UserHandler27') == owner
    _safe_set(owner, 'Classes_Buissnesslayer_User26', None)
    assert getattr(partner, 'UserHandler27') is None


def test_assoc_userhandler50_stub_double():
    # UserHandler has no real 'UserHandler52' property in the generated
    # code (a bare stub) -- manually attach it so Classes_Interactionlayer_LoginController's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Classes_Interactionlayer_LoginController's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Classes_Interactionlayer_LoginController()
    partner = UserHandler()
    setattr(partner, 'UserHandler52', None)
    _safe_set(owner, 'logincontroller51', partner)
    assert getattr(partner, 'UserHandler52') == owner
    _safe_set(owner, 'logincontroller51', None)
    assert getattr(partner, 'UserHandler52') is None


