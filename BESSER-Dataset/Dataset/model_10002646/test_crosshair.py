from python_code import Staff
from python_code import StaffUI

def test_Staff___init__():
    assert Staff.__init__(Staff('', '', '\x00\x00', reservationManagementSystem2=StaffUI()), '', '', '', reservationManagementSystem2=StaffUI()) == None

