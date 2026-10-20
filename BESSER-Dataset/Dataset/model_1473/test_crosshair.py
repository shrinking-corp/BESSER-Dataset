from python_code import GraphConstraint_Attribute
from python_code import GraphConstraint_EAttribute
from python_code import GraphConstraint_Node

def test_GraphConstraint_Attribute___init__():
    assert GraphConstraint_Attribute.__init__(GraphConstraint_Attribute('', '\x00', GraphConstraint_Attribute21=GraphConstraint_EAttribute(), GraphConstraint_Attribute=GraphConstraint_Node()), '\x00\x00', '', GraphConstraint_Attribute21=GraphConstraint_EAttribute(), GraphConstraint_Attribute=GraphConstraint_Node()) == None


from python_code import GraphConstraint_Formula
from python_code import GraphConstraint_NestedGraphCondition

def test_GraphConstraint_Formula___init__():
    assert GraphConstraint_Formula.__init__(GraphConstraint_Formula('', formula=set(), Formula=GraphConstraint_NestedGraphCondition()), '', formula=set(), Formula=GraphConstraint_NestedGraphCondition()) == None


from python_code import GraphConstraint_ElementMapping
from python_code import GraphConstraint_GraphElement

def test_GraphConstraint_GraphElement___init__():
    assert GraphConstraint_GraphElement.__init__(GraphConstraint_GraphElement('', GraphConstraint_GraphElement=GraphConstraint_ElementMapping(), GraphConstraint_GraphElement33=GraphConstraint_ElementMapping()), '', GraphConstraint_GraphElement=GraphConstraint_ElementMapping(), GraphConstraint_GraphElement33=GraphConstraint_ElementMapping()) == None


from python_code import GraphConstraint_EPackage
from python_code import GraphConstraint_Graph
from python_code import GraphConstraint_NestedGraphCondition
from python_code import GraphConstraint_NestedGraphConstraint

def test_GraphConstraint_NestedGraphConstraint___init__():
    assert GraphConstraint_NestedGraphConstraint.__init__(GraphConstraint_NestedGraphConstraint('', NestedGraphConstraint=GraphConstraint_NestedGraphCondition(), GraphConstraint_NestedGraphConstraint=GraphConstraint_EPackage(), gc=GraphConstraint_NestedGraphCondition(), GraphConstraint_NestedGraphConstraint6=GraphConstraint_Graph()), '', NestedGraphConstraint=GraphConstraint_NestedGraphCondition(), GraphConstraint_NestedGraphConstraint=GraphConstraint_EPackage(), gc=GraphConstraint_NestedGraphCondition(), GraphConstraint_NestedGraphConstraint6=GraphConstraint_Graph()) == None


from python_code import GraphConstraint_Graph
from python_code import GraphConstraint_Mapping
from python_code import GraphConstraint_NestedGraphCondition
from python_code import GraphConstraint_QuantifiedGraphCondition

def test_GraphConstraint_QuantifiedGraphCondition___init__():
    assert GraphConstraint_QuantifiedGraphCondition.__init__(GraphConstraint_QuantifiedGraphCondition('', GraphConstraint_QuantifiedGraphCondition37=GraphConstraint_Graph(), GraphConstraint_QuantifiedGraphCondition40=GraphConstraint_Mapping(), GraphConstraint_QuantifiedGraphCondition43=GraphConstraint_Mapping(), qgc=GraphConstraint_NestedGraphCondition(), QuantifiedGraphCondition=GraphConstraint_NestedGraphCondition(), GraphConstraint_QuantifiedGraphCondition=GraphConstraint_Graph()), '', GraphConstraint_QuantifiedGraphCondition37=GraphConstraint_Graph(), GraphConstraint_QuantifiedGraphCondition40=GraphConstraint_Mapping(), GraphConstraint_QuantifiedGraphCondition43=GraphConstraint_Mapping(), qgc=GraphConstraint_NestedGraphCondition(), QuantifiedGraphCondition=GraphConstraint_NestedGraphCondition(), GraphConstraint_QuantifiedGraphCondition=GraphConstraint_Graph()) == None


from python_code import GraphConstraint_EDataType
from python_code import GraphConstraint_NestedGraphCondition
from python_code import GraphConstraint_Variable

def test_GraphConstraint_Variable___init__():
    assert GraphConstraint_Variable.__init__(GraphConstraint_Variable('', GraphConstraint_Variable=GraphConstraint_EDataType(), GraphConstraint_Variable57=GraphConstraint_NestedGraphCondition()), '', GraphConstraint_Variable=GraphConstraint_EDataType(), GraphConstraint_Variable57=GraphConstraint_NestedGraphCondition()) == None

