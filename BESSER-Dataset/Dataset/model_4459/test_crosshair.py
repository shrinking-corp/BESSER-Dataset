from python_code import farrusco_Action
from python_code import farrusco_ActionChild

def test_farrusco_Action___init__():
    assert farrusco_Action.__init__(farrusco_Action('', farrusco_Action=farrusco_ActionChild()), '', farrusco_Action=farrusco_ActionChild()) == None


from python_code import farrusco_ActionChild
from python_code import farrusco_Behavior
from python_code import farrusco_Child

def test_farrusco_Behavior___init__():
    assert farrusco_Behavior.__init__(farrusco_Behavior('', farrusco_Behavior20=farrusco_ActionChild(), farrusco_Behavior=farrusco_Child(), farrusco_Behavior11=farrusco_Child()), '', farrusco_Behavior20=farrusco_ActionChild(), farrusco_Behavior=farrusco_Child(), farrusco_Behavior11=farrusco_Child()) == None


from python_code import farrusco_IRdist

def test_farrusco_IRdist___init__():
    assert farrusco_IRdist.__init__(farrusco_IRdist(0, False), 0, False) == None


from python_code import farrusco_LED

def test_farrusco_LED___init__():
    assert farrusco_LED.__init__(farrusco_LED(True), False) == None


from python_code import farrusco_Motors

def test_farrusco_Motors___init__():
    assert farrusco_Motors.__init__(farrusco_Motors(0, 0), 0, 0) == None


from python_code import farrusco_Robot

def test_farrusco_Robot___init__():
    assert farrusco_Robot.__init__(farrusco_Robot('', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set(), farrusco_Robot6=set()), '', farrusco_Robot=set(), farrusco_Robot2=set(), farrusco_Robot4=set(), farrusco_Robot6=set()) == None


from python_code import farrusco_ServoRange

def test_farrusco_ServoRange___init__():
    assert farrusco_ServoRange.__init__(farrusco_ServoRange(0, 0, 0), 0, 0, 0) == None


from python_code import farrusco_StateOverride

def test_farrusco_StateOverride___init__():
    assert farrusco_StateOverride.__init__(farrusco_StateOverride(0, 0, 0), 0, 0, 0) == None


from python_code import farrusco_Wait

def test_farrusco_Wait___init__():
    assert farrusco_Wait.__init__(farrusco_Wait(0), 0) == None

