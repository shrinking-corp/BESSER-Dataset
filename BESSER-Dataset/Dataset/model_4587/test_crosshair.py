from python_code import ActivitiesProv_ConditionalNode

def test_ActivitiesProv_ConditionalNode___init__():
    assert ActivitiesProv_ConditionalNode.__init__(ActivitiesProv_ConditionalNode(True, False, ActivitiesProv_ConditionalNode=set(), ActivitiesProv_ConditionalNode104=set(), ActivitiesProv_ConditionalNode107=set()), False, True, ActivitiesProv_ConditionalNode=set(), ActivitiesProv_ConditionalNode104=set(), ActivitiesProv_ConditionalNode107=set()) == None


from python_code import ActivitiesProv_JoinNode

def test_ActivitiesProv_JoinNode___init__():
    assert ActivitiesProv_JoinNode.__init__(ActivitiesProv_JoinNode(True), False) == None


from python_code import ActivitiesProv_LoopNode

def test_ActivitiesProv_LoopNode___init__():
    assert ActivitiesProv_LoopNode.__init__(ActivitiesProv_LoopNode(False, ActivitiesProv_LoopNode=set(), ActivitiesProv_LoopNode97=set(), ActivitiesProv_LoopNode100=set()), True, ActivitiesProv_LoopNode=set(), ActivitiesProv_LoopNode97=set(), ActivitiesProv_LoopNode100=set()) == None


from python_code import ActivitiesProv_DecisionNode
from python_code import ActivitiesProv_ObjectFlow

def test_ActivitiesProv_ObjectFlow___init__():
    assert ActivitiesProv_ObjectFlow.__init__(ActivitiesProv_ObjectFlow(False, False, False, ActivitiesProv_ObjectFlow=ActivitiesProv_DecisionNode()), False, False, False, ActivitiesProv_ObjectFlow=ActivitiesProv_DecisionNode()) == None

