from python_code import entitymm_Model

def test_entitymm_Model___init__():
    assert entitymm_Model.__init__(entitymm_Model('\x00', entitymm_Model=set()), '', entitymm_Model=set()) == None

