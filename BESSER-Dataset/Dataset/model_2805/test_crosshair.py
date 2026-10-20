from python_code import attackimpact_Model

def test_attackimpact_Model___init__():
    assert attackimpact_Model.__init__(attackimpact_Model('\x00\x00', '', attackimpact_Model=set()), '', '', attackimpact_Model=set()) == None

