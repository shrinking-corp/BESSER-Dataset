from python_code import Submit_information
from python_code import Userguest

def test_Submit_information___init__():
    assert Submit_information.__init__(Submit_information('\x00\x00', '', '', '', userguest16=Userguest()), '', '', '', '', userguest16=Userguest()) == None

