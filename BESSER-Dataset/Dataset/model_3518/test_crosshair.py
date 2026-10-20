from python_code import test1_ConceptA

def test_test1_ConceptA___init__():
    assert test1_ConceptA.__init__(test1_ConceptA('', '\x00'), '\x00\x00', '') == None

