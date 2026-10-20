from python_code import drn_CameraBottom

def test_drn_CameraBottom___init__():
    assert drn_CameraBottom.__init__(drn_CameraBottom(''), '') == None


from python_code import drn_CameraFront

def test_drn_CameraFront___init__():
    assert drn_CameraFront.__init__(drn_CameraFront(''), '') == None


from python_code import drn_DepXYZ_IMPL

def test_drn_DepXYZ_IMPL___init__():
    assert drn_DepXYZ_IMPL.__init__(drn_DepXYZ_IMPL(''), '') == None


from python_code import drn_Land

def test_drn_Land___init__():
    assert drn_Land.__init__(drn_Land(''), '') == None


from python_code import drn_Led_Impl

def test_drn_Led_Impl___init__():
    assert drn_Led_Impl.__init__(drn_Led_Impl(''), '') == None


from python_code import drn_Context
from python_code import drn_Limit

def test_drn_Limit___init__():
    assert drn_Limit.__init__(drn_Limit('', '\x00', drn_Limit=drn_Context()), '\x00\x00', '', drn_Limit=drn_Context()) == None


from python_code import drn_TakeOff

def test_drn_TakeOff___init__():
    assert drn_TakeOff.__init__(drn_TakeOff(''), '') == None

