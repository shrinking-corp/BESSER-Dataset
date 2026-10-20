from python_code import driver_DocumentRoot

def test_driver_DocumentRoot___init__():
    assert driver_DocumentRoot.__init__(driver_DocumentRoot('', driver_DocumentRoot=set(), driver_DocumentRoot2=set(), driver_DocumentRoot5=set()), '', driver_DocumentRoot=set(), driver_DocumentRoot2=set(), driver_DocumentRoot5=set()) == None


from python_code import driver_DriverInfo
from python_code import driver_Info

def test_driver_Info___init__():
    assert driver_Info.__init__(driver_Info('', '\x00', driver_Info=driver_DriverInfo()), '\x00\x00', '', driver_Info=driver_DriverInfo()) == None

