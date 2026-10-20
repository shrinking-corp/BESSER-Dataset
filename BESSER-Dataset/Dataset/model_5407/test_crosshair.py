from python_code import faultTree_Event

def test_faultTree_Event___init__():
    assert faultTree_Event.__init__(faultTree_Event('', '\x00'), '\x00\x00', '') == None


from python_code import faultTree_ProbabalisticEvent

def test_faultTree_ProbabalisticEvent___init__():
    assert faultTree_ProbabalisticEvent.__init__(faultTree_ProbabalisticEvent(0.0), 0.0) == None

