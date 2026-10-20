from python_code import UML_Activity_mine_Action

def test_UML_Activity_mine_Action___init__():
    assert UML_Activity_mine_Action.__init__(UML_Activity_mine_Action('', '\x00'), '\x00\x00', '') == None


from python_code import UML_Activity_mine_Activity
from python_code import UML_Activity_mine_ActivityEdge
from python_code import UML_Activity_mine_ActivityNode
from python_code import UML_Activity_mine_ExpansionRegion

def test_UML_Activity_mine_ActivityEdge___init__():
    assert UML_Activity_mine_ActivityEdge.__init__(UML_Activity_mine_ActivityEdge(True, ActivityEdge=UML_Activity_mine_ActivityNode(), ActivityEdge8=UML_Activity_mine_ActivityNode(), UML_Activity_mine_ActivityEdge=UML_Activity_mine_Activity(), incoming=UML_Activity_mine_ActivityNode(), outgoing=UML_Activity_mine_ActivityNode(), UML_Activity_mine_ActivityEdge15=UML_Activity_mine_ExpansionRegion()), False, ActivityEdge=UML_Activity_mine_ActivityNode(), ActivityEdge8=UML_Activity_mine_ActivityNode(), UML_Activity_mine_ActivityEdge=UML_Activity_mine_Activity(), incoming=UML_Activity_mine_ActivityNode(), outgoing=UML_Activity_mine_ActivityNode(), UML_Activity_mine_ActivityEdge15=UML_Activity_mine_ExpansionRegion()) == None


from python_code import UML_Activity_mine_ActivityParameterNode

def test_UML_Activity_mine_ActivityParameterNode___init__():
    assert UML_Activity_mine_ActivityParameterNode.__init__(UML_Activity_mine_ActivityParameterNode(''), '') == None


from python_code import UML_Activity_mine_Element

def test_UML_Activity_mine_Element___init__():
    assert UML_Activity_mine_Element.__init__(UML_Activity_mine_Element('', '', '\x00\x00'), '', '', '') == None


from python_code import UML_Activity_mine_ObjectNode

def test_UML_Activity_mine_ObjectNode___init__():
    assert UML_Activity_mine_ObjectNode.__init__(UML_Activity_mine_ObjectNode('', '\x00'), '\x00\x00', '') == None

