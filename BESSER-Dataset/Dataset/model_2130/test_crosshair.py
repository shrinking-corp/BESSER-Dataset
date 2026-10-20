from python_code import uitf_AssertInState

def test_uitf_AssertInState___init__():
    assert uitf_AssertInState.__init__(uitf_AssertInState(''), '') == None


from python_code import uitf_TriggeredTransition

def test_uitf_TriggeredTransition___init__():
    assert uitf_TriggeredTransition.__init__(uitf_TriggeredTransition('', '\x00'), '\x00\x00', '') == None

