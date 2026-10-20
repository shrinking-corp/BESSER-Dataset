from python_code import metamodel_ActionWheel
from python_code import metamodel_Group

def test_metamodel_ActionWheel___init__():
    assert metamodel_ActionWheel.__init__(metamodel_ActionWheel(0, metamodel_ActionWheel=metamodel_Group()), 0, metamodel_ActionWheel=metamodel_Group()) == None


from python_code import metamodel_BoolVal

def test_metamodel_BoolVal___init__():
    assert metamodel_BoolVal.__init__(metamodel_BoolVal(True), False) == None


from python_code import metamodel_DifferentialWheel
from python_code import metamodel_Group

def test_metamodel_DifferentialWheel___init__():
    assert metamodel_DifferentialWheel.__init__(metamodel_DifferentialWheel(False, 0, metamodel_DifferentialWheel=metamodel_Group()), False, 0, metamodel_DifferentialWheel=metamodel_Group()) == None


from python_code import metamodel_FloatVal

def test_metamodel_FloatVal___init__():
    assert metamodel_FloatVal.__init__(metamodel_FloatVal(0.0), 0.0) == None


from python_code import metamodel_IntVal

def test_metamodel_IntVal___init__():
    assert metamodel_IntVal.__init__(metamodel_IntVal(0), 0) == None

