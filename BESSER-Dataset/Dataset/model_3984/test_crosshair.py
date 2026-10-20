from python_code import failureLogic_FMEA_FMEA

def test_failureLogic_FMEA_FMEA___init__():
    assert failureLogic_FMEA_FMEA.__init__(failureLogic_FMEA_FMEA('', failureLogic_FMEA_FMEA=set()), '', failureLogic_FMEA_FMEA=set()) == None


from python_code import FMEA_failureLogic_ProbDist
from python_code import failureLogic_FMEA_FMEA
from python_code import failureLogic_FMEA_FMEDAEntry

def test_failureLogic_FMEA_FMEDAEntry___init__():
    assert failureLogic_FMEA_FMEDAEntry.__init__(failureLogic_FMEA_FMEDAEntry(0.0, failureLogic_FMEA_FMEDAEntry=FMEA_failureLogic_ProbDist(), FMEAEntry=failureLogic_FMEA_FMEA('', failureLogic_FMEA_FMEA=set())), 0.0, failureLogic_FMEA_FMEDAEntry=FMEA_failureLogic_ProbDist(), FMEAEntry=failureLogic_FMEA_FMEA('', failureLogic_FMEA_FMEA=set())) == None


from python_code import FTA_failureLogic_Failure
from python_code import failureLogic_FTA_Cause

def test_failureLogic_FTA_Cause___init__():
    assert failureLogic_FTA_Cause.__init__(failureLogic_FTA_Cause('', failureLogic_FTA_Cause=FTA_failureLogic_Failure()), '', failureLogic_FTA_Cause=FTA_failureLogic_Failure()) == None


from python_code import Markov_failureLogic_Failure
from python_code import failureLogic_Markov_State

def test_failureLogic_Markov_State___init__():
    assert failureLogic_Markov_State.__init__(failureLogic_Markov_State(False, False, failureLogic_Markov_State=Markov_failureLogic_Failure()), False, False, failureLogic_Markov_State=Markov_failureLogic_Failure()) == None


from python_code import Markov_failureLogic_ProbDist
from python_code import failureLogic_Markov_Transition

def test_failureLogic_Markov_Transition___init__():
    assert failureLogic_Markov_Transition.__init__(failureLogic_Markov_Transition(0.0, failureLogic_Markov_Transition36=set(), failureLogic_Markov_Transition=Markov_failureLogic_ProbDist(), failureLogic_Markov_Transition33=set()), 0.0, failureLogic_Markov_Transition36=set(), failureLogic_Markov_Transition=Markov_failureLogic_ProbDist(), failureLogic_Markov_Transition33=set()) == None

