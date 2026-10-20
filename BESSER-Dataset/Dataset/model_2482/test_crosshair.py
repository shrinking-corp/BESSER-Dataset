from python_code import fsm_FSM
from python_code import fsm_NoAnnotation

def test_fsm_NoAnnotation___init__():
    assert fsm_NoAnnotation.__init__(fsm_NoAnnotation('\x00\x00', '', fsm_NoAnnotation=set(), fsm_NoAnnotation2=fsm_FSM()), '', '', fsm_NoAnnotation=set(), fsm_NoAnnotation2=fsm_FSM()) == None

def test_fsm_NoAnnotation_j():
    assert fsm_NoAnnotation.j(fsm_NoAnnotation('', '\x00', fsm_NoAnnotation=set(), fsm_NoAnnotation2=fsm_FSM()), '', '') == None

def test_fsm_NoAnnotation_k():
    assert fsm_NoAnnotation.k(fsm_NoAnnotation('', '\x00', fsm_NoAnnotation=set(), fsm_NoAnnotation2=fsm_FSM()), '') == None

