from python_code import minuml2_ActivityPartition
from python_code import minuml2_ModelElement
from python_code import minuml2_ObjectFlow

def test_minuml2_ModelElement___init__():
    assert minuml2_ModelElement.__init__(minuml2_ModelElement('', minuml2_ModelElement=minuml2_ActivityPartition(), minuml2_ModelElement22=minuml2_ObjectFlow()), '', minuml2_ModelElement=minuml2_ActivityPartition(), minuml2_ModelElement22=minuml2_ObjectFlow()) == None


from python_code import minuml2_ActivityEdge
from python_code import minuml2_OpaqueExpression

def test_minuml2_OpaqueExpression___init__():
    assert minuml2_OpaqueExpression.__init__(minuml2_OpaqueExpression('', '\x00', minuml2_OpaqueExpression=minuml2_ActivityEdge()), '\x00\x00', '', minuml2_OpaqueExpression=minuml2_ActivityEdge()) == None

