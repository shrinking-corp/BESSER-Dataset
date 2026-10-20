from python_code import activity_AbstractActivity

def test_activity_AbstractActivity___init__():
    assert activity_AbstractActivity.__init__(activity_AbstractActivity(False, False), False, False) == None


from python_code import activity_AcceptEventAction

def test_activity_AcceptEventAction___init__():
    assert activity_AcceptEventAction.__init__(activity_AcceptEventAction(True), False) == None


from python_code import activity_ActivityEdge
from python_code import activity_ActivityNode
from python_code import activity_ValueSpecification

def test_activity_ActivityEdge___init__():
    assert activity_ActivityEdge.__init__(activity_ActivityEdge('', activity_ActivityEdge17=activity_ActivityNode(), activity_ActivityEdge=activity_ValueSpecification(), activity_ActivityEdge2=activity_ValueSpecification(), activity_ActivityEdge5=activity_ActivityNode(), activity_ActivityEdge7=activity_ActivityNode(), activity_ActivityEdge10=activity_ValueSpecification(), activity_ActivityEdge13=activity_ValueSpecification(), activity_ActivityEdge20=activity_ActivityNode()), '', activity_ActivityEdge17=activity_ActivityNode(), activity_ActivityEdge=activity_ValueSpecification(), activity_ActivityEdge2=activity_ValueSpecification(), activity_ActivityEdge5=activity_ActivityNode(), activity_ActivityEdge7=activity_ActivityNode(), activity_ActivityEdge10=activity_ValueSpecification(), activity_ActivityEdge13=activity_ValueSpecification(), activity_ActivityEdge20=activity_ActivityNode()) == None


from python_code import activity_ActivityPartition

def test_activity_ActivityPartition___init__():
    assert activity_ActivityPartition.__init__(activity_ActivityPartition(False, False), False, False) == None


from python_code import activity_ObjectFlow

def test_activity_ObjectFlow___init__():
    assert activity_ObjectFlow.__init__(activity_ObjectFlow(False, False), False, False) == None


from python_code import activity_AbstractBehavior
from python_code import activity_ObjectNode
from python_code import activity_ValueSpecification

def test_activity_ObjectNode___init__():
    assert activity_ObjectNode.__init__(activity_ObjectNode(False, '', '', activity_ObjectNode=activity_ValueSpecification(), activity_ObjectNode27=set(), activity_ObjectNode29=activity_AbstractBehavior()), False, '', '', activity_ObjectNode=activity_ValueSpecification(), activity_ObjectNode27=set(), activity_ObjectNode29=activity_AbstractBehavior()) == None


from python_code import activity_Pin

def test_activity_Pin___init__():
    assert activity_Pin.__init__(activity_Pin(True), False) == None

