from python_code import Coach

def test_Coach___init__():
    assert Coach.__init__(Coach(0, 0, '', '', ''), 0, 0, '', '', '') == None


from python_code import Commutator
from python_code import TrainBuilder_Interface

def test_Commutator___init__():
    assert Commutator.__init__(Commutator(TrainBuilder_Interface(), '', trainBuilder8=TrainBuilder_Interface(), trainBuilder18=set()), TrainBuilder_Interface(), '', trainBuilder8=TrainBuilder_Interface(), trainBuilder18=set()) == None


from python_code import Engine

def test_Engine___init__():
    assert Engine.__init__(Engine('', '\x00'), '\x00\x00', '') == None


from python_code import InterCity
from python_code import TrainBuilder_Interface

def test_InterCity___init__():
    assert InterCity.__init__(InterCity(TrainBuilder_Interface(), '', trainBuilder6=TrainBuilder_Interface(), trainBuilder14=set()), TrainBuilder_Interface(), '', trainBuilder6=TrainBuilder_Interface(), trainBuilder14=set()) == None


from python_code import Sleeper
from python_code import TrainBuilder_Interface

def test_Sleeper___init__():
    assert Sleeper.__init__(Sleeper(TrainBuilder_Interface(), '', trainBuilder4=TrainBuilder_Interface(), trainBuilder16=set()), TrainBuilder_Interface(), '', trainBuilder4=TrainBuilder_Interface(), trainBuilder16=set()) == None


from python_code import Train

def test_Train___init__():
    assert Train.__init__(Train('', '\x00'), '\x00\x00', '') == None

