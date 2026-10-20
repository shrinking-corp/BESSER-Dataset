from python_code import StatemachineMetamodel_State
from python_code import StatemachineMetamodel_Statemachine
from python_code import StatemachineMetamodel_Transition

def test_StatemachineMetamodel_State___init__():
    assert StatemachineMetamodel_State.__init__(StatemachineMetamodel_State('', StatemachineMetamodel_State2=StatemachineMetamodel_Transition(), StatemachineMetamodel_State=StatemachineMetamodel_Statemachine(), StatemachineMetamodel_State4=set()), '', StatemachineMetamodel_State2=StatemachineMetamodel_Transition(), StatemachineMetamodel_State=StatemachineMetamodel_Statemachine(), StatemachineMetamodel_State4=set()) == None

