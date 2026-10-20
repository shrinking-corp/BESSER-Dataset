from python_code import tTCTest_Class_Element
from python_code import tTCTest_Containment

def test_tTCTest_Class_Element___init__():
    assert tTCTest_Class_Element.__init__(tTCTest_Class_Element('', tTCTest_Class_Element=tTCTest_Containment()), '', tTCTest_Class_Element=tTCTest_Containment()) == None


from python_code import tTCTest_Condition
from python_code import tTCTest_Warning

def test_tTCTest_Warning___init__():
    assert tTCTest_Warning.__init__(tTCTest_Warning('', tTCTest_Warning=tTCTest_Condition()), '', tTCTest_Warning=tTCTest_Condition()) == None

