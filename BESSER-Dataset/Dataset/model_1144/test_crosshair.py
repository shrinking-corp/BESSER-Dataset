from python_code import SrcCompositeState
from python_code import SrcStateMachine
from python_code import jointPackage_HSM2FSM_SrcAbstractState

def test_jointPackage_HSM2FSM_SrcAbstractState___init__():
    assert jointPackage_HSM2FSM_SrcAbstractState.__init__(jointPackage_HSM2FSM_SrcAbstractState('', states=SrcStateMachine(), states17=SrcCompositeState()), '', states=SrcStateMachine(), states17=SrcCompositeState()) == None


from python_code import jointPackage_HSM2FSM_SrcStateMachine

def test_jointPackage_HSM2FSM_SrcStateMachine___init__():
    assert jointPackage_HSM2FSM_SrcStateMachine.__init__(jointPackage_HSM2FSM_SrcStateMachine('', stateMachine=set(), stateMachine6=set()), '', stateMachine=set(), stateMachine6=set()) == None


from python_code import SrcAbstractState
from python_code import SrcStateMachine
from python_code import jointPackage_HSM2FSM_SrcTransition

def test_jointPackage_HSM2FSM_SrcTransition___init__():
    assert jointPackage_HSM2FSM_SrcTransition.__init__(jointPackage_HSM2FSM_SrcTransition('\x00', transitions=SrcStateMachine(), jointPackage_HSM2FSM_SrcTransition=SrcAbstractState(), jointPackage_HSM2FSM_SrcTransition12=SrcAbstractState()), '', transitions=SrcStateMachine(), jointPackage_HSM2FSM_SrcTransition=SrcAbstractState(), jointPackage_HSM2FSM_SrcTransition12=SrcAbstractState()) == None


from python_code import TrgCompositeState
from python_code import TrgStateMachine
from python_code import jointPackage_HSM2FSM_TrgAbstractState

def test_jointPackage_HSM2FSM_TrgAbstractState___init__():
    assert jointPackage_HSM2FSM_TrgAbstractState.__init__(jointPackage_HSM2FSM_TrgAbstractState('', states34=TrgStateMachine(), states37=TrgCompositeState()), '', states34=TrgStateMachine(), states37=TrgCompositeState()) == None


from python_code import jointPackage_HSM2FSM_TrgStateMachine

def test_jointPackage_HSM2FSM_TrgStateMachine___init__():
    assert jointPackage_HSM2FSM_TrgStateMachine.__init__(jointPackage_HSM2FSM_TrgStateMachine('', stateMachine22=set(), stateMachine24=set()), '', stateMachine22=set(), stateMachine24=set()) == None


from python_code import TrgAbstractState
from python_code import TrgStateMachine
from python_code import jointPackage_HSM2FSM_TrgTransition

def test_jointPackage_HSM2FSM_TrgTransition___init__():
    assert jointPackage_HSM2FSM_TrgTransition.__init__(jointPackage_HSM2FSM_TrgTransition('\x00', transitions26=TrgStateMachine(), jointPackage_HSM2FSM_TrgTransition=TrgAbstractState(), jointPackage_HSM2FSM_TrgTransition31=TrgAbstractState()), '', transitions26=TrgStateMachine(), jointPackage_HSM2FSM_TrgTransition=TrgAbstractState(), jointPackage_HSM2FSM_TrgTransition31=TrgAbstractState()) == None

