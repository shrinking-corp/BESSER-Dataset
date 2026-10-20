from python_code import HSM_MgaObject

def test_HSM_MgaObject___init__():
    assert HSM_MgaObject.__init__(HSM_MgaObject('', '\x00'), '\x00\x00', '') == None


from python_code import HSM_RootFolder

def test_HSM_RootFolder___init__():
    assert HSM_RootFolder.__init__(HSM_RootFolder('', HSM_RootFolder=set(), rootFolder=set()), '', HSM_RootFolder=set(), rootFolder=set()) == None


from python_code import AssociationDataStateBase
from python_code import HSM_StateBase

def test_HSM_StateBase___init__():
    assert HSM_StateBase.__init__(HSM_StateBase('', '', dstTransition=set(), srcTransition=set(), stateBase=set(), stateBase5=AssociationDataStateBase()), '', '', dstTransition=set(), srcTransition=set(), stateBase=set(), stateBase5=AssociationDataStateBase()) == None


from python_code import AssociationDataStateBase
from python_code import HSM_StateDataRelation
from python_code import OrState

def test_HSM_StateDataRelation___init__():
    assert HSM_StateDataRelation.__init__(HSM_StateDataRelation('', '\x00', stateDataRelation=OrState(), stateDataRelation47=AssociationDataStateBase()), '\x00\x00', '', stateDataRelation=OrState(), stateDataRelation47=AssociationDataStateBase()) == None


from python_code import HSM_StateDateRelation

def test_HSM_StateDateRelation___init__():
    assert HSM_StateDateRelation.__init__(HSM_StateDateRelation('', '\x00'), '\x00\x00', '') == None


from python_code import AssociationStateState
from python_code import HSM_Transition
from python_code import OrState

def test_HSM_Transition___init__():
    assert HSM_Transition.__init__(HSM_Transition('\x00\x00', '', '', '', transition=OrState(), transition14=AssociationStateState()), '', '', '', '', transition=OrState(), transition14=AssociationStateState()) == None

