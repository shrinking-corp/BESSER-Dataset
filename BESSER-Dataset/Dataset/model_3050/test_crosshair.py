from python_code import myDot_Attribute

def test_myDot_Attribute___init__():
    assert myDot_Attribute.__init__(myDot_Attribute(''), '') == None


from python_code import myDot_Entity
from python_code import myDot_EntityRef
from python_code import myDot_Model
from python_code import myDot_Reference

def test_myDot_Entity___init__():
    assert myDot_Entity.__init__(myDot_Entity('\x00', myDot_Entity=myDot_Model(), myDot_Entity4=set(), myDot_Entity6=myDot_Reference(), myDot_Entity15=myDot_EntityRef()), '', myDot_Entity=myDot_Model(), myDot_Entity4=set(), myDot_Entity6=myDot_Reference(), myDot_Entity15=myDot_EntityRef()) == None

