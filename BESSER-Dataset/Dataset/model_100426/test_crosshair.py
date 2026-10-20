from python_code import statemachine_Event

def test_statemachine_Event___init__():
    assert statemachine_Event.__init__(statemachine_Event(''), '') == None


from python_code import statemachine_Pseudostate

def test_statemachine_Pseudostate___init__():
    assert statemachine_Pseudostate.__init__(statemachine_Pseudostate(''), '') == None


from python_code import statemachine_Variable

def test_statemachine_Variable___init__():
    assert statemachine_Variable.__init__(statemachine_Variable(''), '') == None

