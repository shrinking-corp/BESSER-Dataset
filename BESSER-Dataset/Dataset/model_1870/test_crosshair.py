from python_code import Wires_BasicData

def test_Wires_BasicData___init__():
    assert Wires_BasicData.__init__(Wires_BasicData(''), '') == None


from python_code import Wires_ConnectableElement
from python_code import Wires_DataFlow

def test_Wires_ConnectableElement___init__():
    assert Wires_ConnectableElement.__init__(Wires_ConnectableElement('', ConnectableElement=Wires_DataFlow(), ConnectableElement17=Wires_DataFlow(), target=set(), src=set()), '', ConnectableElement=Wires_DataFlow(), ConnectableElement17=Wires_DataFlow(), target=set(), src=set()) == None


from python_code import Wires_DecisionNode
from python_code import Wires_Transformation

def test_Wires_DecisionNode___init__():
    assert Wires_DecisionNode.__init__(Wires_DecisionNode('', Wires_DecisionNode=Wires_Transformation(), Wires_DecisionNode7=set(), Wires_DecisionNode10=set(), Wires_DecisionNode13=set()), '', Wires_DecisionNode=Wires_Transformation(), Wires_DecisionNode7=set(), Wires_DecisionNode10=set(), Wires_DecisionNode13=set()) == None


from python_code import Wires_DataType
from python_code import Wires_FormalParameter

def test_Wires_FormalParameter___init__():
    assert Wires_FormalParameter.__init__(Wires_FormalParameter('', Wires_FormalParameter=Wires_DataType()), '', Wires_FormalParameter=Wires_DataType()) == None


from python_code import Wires_Model

def test_Wires_Model___init__():
    assert Wires_Model.__init__(Wires_Model(''), '') == None


from python_code import Wires_ModelType

def test_Wires_ModelType___init__():
    assert Wires_ModelType.__init__(Wires_ModelType(''), '') == None


from python_code import Wires_Type
from python_code import Wires_TypedElement

def test_Wires_Type___init__():
    assert Wires_Type.__init__(Wires_Type('', Wires_Type=Wires_TypedElement()), '', Wires_Type=Wires_TypedElement()) == None

