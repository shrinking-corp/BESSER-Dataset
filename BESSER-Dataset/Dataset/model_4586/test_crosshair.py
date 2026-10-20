from python_code import Activities_BasicActivities_Parameter

def test_Activities_BasicActivities_Parameter___init__():
    assert Activities_BasicActivities_Parameter.__init__(Activities_BasicActivities_Parameter(False, False, '', parameter=set()), False, False, '', parameter=set()) == None


from python_code import Activities_BasicActivities_Pin
from python_code import Activities_ExtraStructuredActivities_ExceptionHandler

def test_Activities_BasicActivities_Pin___init__():
    assert Activities_BasicActivities_Pin.__init__(Activities_BasicActivities_Pin(True, ObjectNode=Activities_ExtraStructuredActivities_ExceptionHandler()), False, ObjectNode=Activities_ExtraStructuredActivities_ExceptionHandler()) == None


from python_code import Activities_IntermediateActivities_JoinNode
from python_code import ValueSpecification

def test_Activities_IntermediateActivities_JoinNode___init__():
    assert Activities_IntermediateActivities_JoinNode.__init__(Activities_IntermediateActivities_JoinNode(True, Activities_IntermediateActivities_JoinNode=ValueSpecification()), False, Activities_IntermediateActivities_JoinNode=ValueSpecification()) == None

