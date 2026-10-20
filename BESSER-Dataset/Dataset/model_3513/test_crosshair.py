from python_code import testoperationbody_ChildA

def test_testoperationbody_ChildA___init__():
    assert testoperationbody_ChildA.__init__(testoperationbody_ChildA(''), '') == None


from python_code import testoperationbody_ConceptA
from python_code import testoperationbody_Main

def test_testoperationbody_Main___init__():
    assert testoperationbody_Main.__init__(testoperationbody_Main(False, 0, testoperationbody_Main=set(), testoperationbody_Main2=testoperationbody_ConceptA(), testoperationbody_Main5=set()), False, 0, testoperationbody_Main=set(), testoperationbody_Main2=testoperationbody_ConceptA(), testoperationbody_Main5=set()) == None

