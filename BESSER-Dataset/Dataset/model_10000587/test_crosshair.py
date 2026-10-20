from python_code import Patient

def test_Patient___init__():
    assert Patient.__init__(Patient(0, '', 0, '', 0, '', doctors1=set()), 0, '', 0, '', 0, '', doctors1=set()) == None

