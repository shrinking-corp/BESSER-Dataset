from python_code import CartItems

def test_CartItems___init__():
    assert CartItems.__init__(CartItems('', '\x00'), '\x00\x00', '') == None


from python_code import Categories

def test_Categories___init__():
    assert Categories.__init__(Categories(''), '') == None


from python_code import CompanyAddItem

def test_CompanyAddItem___init__():
    assert CompanyAddItem.__init__(CompanyAddItem('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import CompanyAddRider

def test_CompanyAddRider___init__():
    assert CompanyAddRider.__init__(CompanyAddRider('', '', '', '', '', '', 0), '', '\x00', '', '', '', '', 0) == None


from python_code import CompanyAssignRider

def test_CompanyAssignRider___init__():
    assert CompanyAssignRider.__init__(CompanyAssignRider('', '', '\x00\x00'), '', '', '') == None


from python_code import CompanyOrderHistory

def test_CompanyOrderHistory___init__():
    assert CompanyOrderHistory.__init__(CompanyOrderHistory('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import CompanyTrackOrder

def test_CompanyTrackOrder___init__():
    assert CompanyTrackOrder.__init__(CompanyTrackOrder('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ConfirmOrder

def test_ConfirmOrder___init__():
    assert ConfirmOrder.__init__(ConfirmOrder('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Login

def test_Login___init__():
    assert Login.__init__(Login('', '\x00'), '\x00\x00', '') == None


from python_code import Order

def test_Order___init__():
    assert Order.__init__(Order('', '', '', '', ''), '', '', '', '', '') == None


from python_code import OrderHistory

def test_OrderHistory___init__():
    assert OrderHistory.__init__(OrderHistory('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import PlaceOrder

def test_PlaceOrder___init__():
    assert PlaceOrder.__init__(PlaceOrder('', '\x00'), '\x00\x00', '') == None


from python_code import ReviewOrder

def test_ReviewOrder___init__():
    assert ReviewOrder.__init__(ReviewOrder('', '', '\x00\x00'), '', '', '') == None


from python_code import RiderStatusUpdate

def test_RiderStatusUpdate___init__():
    assert RiderStatusUpdate.__init__(RiderStatusUpdate('', '', '\x00\x00'), '', '', '') == None


from python_code import Store

def test_Store___init__():
    assert Store.__init__(Store(''), '') == None


from python_code import TrackOrder

def test_TrackOrder___init__():
    assert TrackOrder.__init__(TrackOrder('', '\x00'), '\x00\x00', '') == None


from python_code import UserRegisteration

def test_UserRegisteration___init__():
    assert UserRegisteration.__init__(UserRegisteration('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None

