from python_code import StateMachine_ActionExpression

def test_StateMachine_ActionExpression___init__():
    assert StateMachine_ActionExpression.__init__(StateMachine_ActionExpression(''), '') == None


from python_code import StateMachine_ChangeSignalAllowedSpeed
from python_code import StateMachine_Signal

def test_StateMachine_ChangeSignalAllowedSpeed___init__():
    assert StateMachine_ChangeSignalAllowedSpeed.__init__(StateMachine_ChangeSignalAllowedSpeed('', StateMachine_ChangeSignalAllowedSpeed=StateMachine_Signal()), '', StateMachine_ChangeSignalAllowedSpeed=StateMachine_Signal()) == None


from python_code import StateMachine_ChangeTrainHeadingSpeed
from python_code import StateMachine_Train

def test_StateMachine_ChangeTrainHeadingSpeed___init__():
    assert StateMachine_ChangeTrainHeadingSpeed.__init__(StateMachine_ChangeTrainHeadingSpeed('', StateMachine_ChangeTrainHeadingSpeed=StateMachine_Train()), '', StateMachine_ChangeTrainHeadingSpeed=StateMachine_Train()) == None


from python_code import StateMachine_ChangeTurnoutDirection
from python_code import StateMachine_Turnout

def test_StateMachine_ChangeTurnoutDirection___init__():
    assert StateMachine_ChangeTurnoutDirection.__init__(StateMachine_ChangeTurnoutDirection('', StateMachine_ChangeTurnoutDirection=StateMachine_Turnout()), '', StateMachine_ChangeTurnoutDirection=StateMachine_Turnout()) == None


from python_code import StateMachine_GuardExpression

def test_StateMachine_GuardExpression___init__():
    assert StateMachine_GuardExpression.__init__(StateMachine_GuardExpression(''), '') == None


from python_code import StateMachine_NamedElement

def test_StateMachine_NamedElement___init__():
    assert StateMachine_NamedElement.__init__(StateMachine_NamedElement(''), '') == None


from python_code import StateMachine_Signal
from python_code import StateMachine_SignalAllowedSpeedChanged

def test_StateMachine_SignalAllowedSpeedChanged___init__():
    assert StateMachine_SignalAllowedSpeedChanged.__init__(StateMachine_SignalAllowedSpeedChanged('', StateMachine_SignalAllowedSpeedChanged=StateMachine_Signal()), '', StateMachine_SignalAllowedSpeedChanged=StateMachine_Signal()) == None


from python_code import StateMachine_Signal
from python_code import StateMachine_SignalCurrentAllowedSpeed

def test_StateMachine_SignalCurrentAllowedSpeed___init__():
    assert StateMachine_SignalCurrentAllowedSpeed.__init__(StateMachine_SignalCurrentAllowedSpeed('', StateMachine_SignalCurrentAllowedSpeed=StateMachine_Signal()), '', StateMachine_SignalCurrentAllowedSpeed=StateMachine_Signal()) == None


from python_code import StateMachine_Train
from python_code import StateMachine_TrainCurrentHeadingSpeed

def test_StateMachine_TrainCurrentHeadingSpeed___init__():
    assert StateMachine_TrainCurrentHeadingSpeed.__init__(StateMachine_TrainCurrentHeadingSpeed('', StateMachine_TrainCurrentHeadingSpeed=StateMachine_Train()), '', StateMachine_TrainCurrentHeadingSpeed=StateMachine_Train()) == None


from python_code import StateMachine_Train
from python_code import StateMachine_TrainHeadingSpeedChanged

def test_StateMachine_TrainHeadingSpeedChanged___init__():
    assert StateMachine_TrainHeadingSpeedChanged.__init__(StateMachine_TrainHeadingSpeedChanged('', StateMachine_TrainHeadingSpeedChanged=StateMachine_Train()), '', StateMachine_TrainHeadingSpeedChanged=StateMachine_Train()) == None


from python_code import StateMachine_TriggerExpression

def test_StateMachine_TriggerExpression___init__():
    assert StateMachine_TriggerExpression.__init__(StateMachine_TriggerExpression(''), '') == None


from python_code import StateMachine_Turnout
from python_code import StateMachine_TurnoutCurrentDirection

def test_StateMachine_TurnoutCurrentDirection___init__():
    assert StateMachine_TurnoutCurrentDirection.__init__(StateMachine_TurnoutCurrentDirection('', StateMachine_TurnoutCurrentDirection=StateMachine_Turnout()), '', StateMachine_TurnoutCurrentDirection=StateMachine_Turnout()) == None


from python_code import StateMachine_Turnout
from python_code import StateMachine_TurnoutDirectionChanged

def test_StateMachine_TurnoutDirectionChanged___init__():
    assert StateMachine_TurnoutDirectionChanged.__init__(StateMachine_TurnoutDirectionChanged('', StateMachine_TurnoutDirectionChanged=StateMachine_Turnout()), '', StateMachine_TurnoutDirectionChanged=StateMachine_Turnout()) == None

