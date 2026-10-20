from python_code import myDsl_Attribute

def test_myDsl_Attribute___init__():
    assert myDsl_Attribute.__init__(myDsl_Attribute(''), '') == None


from python_code import myDsl_Entity
from python_code import myDsl_Model
from python_code import myDsl_Reference

def test_myDsl_Entity___init__():
    assert myDsl_Entity.__init__(myDsl_Entity('\x00', myDsl_Entity=myDsl_Model(), myDsl_Entity2=set(), myDsl_Entity4=myDsl_Reference()), '', myDsl_Entity=myDsl_Model(), myDsl_Entity2=set(), myDsl_Entity4=myDsl_Reference()) == None

