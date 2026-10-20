from python_code import model_Block
from python_code import model_Command
from python_code import model_OzobotProgram
from python_code import model_Transition

def test_model_Command___init__():
    assert model_Command.__init__(model_Command('', model_Command=model_OzobotProgram(), model_Command5=model_OzobotProgram(), source=model_Transition(), target=model_Transition(), model_Command15=model_Block(), Command=model_Transition(), Command20=model_Transition()), '', model_Command=model_OzobotProgram(), model_Command5=model_OzobotProgram(), source=model_Transition(), target=model_Transition(), model_Command15=model_Block(), Command=model_Transition(), Command20=model_Transition()) == None


from python_code import model_Light

def test_model_Light___init__():
    assert model_Light.__init__(model_Light(''), '') == None


from python_code import model_Move

def test_model_Move___init__():
    assert model_Move.__init__(model_Move(0, '\x00'), 0, '\x00') == None


from python_code import model_NamedElement

def test_model_NamedElement___init__():
    assert model_NamedElement.__init__(model_NamedElement(''), '') == None


from python_code import model_Ozobot

def test_model_Ozobot___init__():
    assert model_Ozobot.__init__(model_Ozobot(0.0, 0.0, 0.0, model_Ozobot=set()), 0.0, 0.0, 0.0, model_Ozobot=set()) == None


from python_code import model_Block
from python_code import model_Repeat

def test_model_Repeat___init__():
    assert model_Repeat.__init__(model_Repeat(0, model_Repeat=model_Block()), 0, model_Repeat=model_Block()) == None


from python_code import model_Rotate

def test_model_Rotate___init__():
    assert model_Rotate.__init__(model_Rotate('', '', 0.0), '', '', 0.0) == None


from python_code import model_Wait

def test_model_Wait___init__():
    assert model_Wait.__init__(model_Wait(0), 0) == None

