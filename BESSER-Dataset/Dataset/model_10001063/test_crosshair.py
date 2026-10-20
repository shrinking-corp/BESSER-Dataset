from python_code import Admin

def test_Admin___init__():
    assert Admin.__init__(Admin('', '\x00'), '\x00\x00', '') == None


from python_code import Guestuser
from python_code import Submit_information

def test_Submit_information___init__():
    assert Submit_information.__init__(Submit_information('\x00\x00', '', '', '', userguest16=Guestuser()), '', '', '', '', userguest16=Guestuser()) == None

