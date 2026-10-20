from python_code import ImperativeOCL_AssertExp
from python_code import LogExp

def test_ImperativeOCL_AssertExp___init__():
    assert ImperativeOCL_AssertExp.__init__(ImperativeOCL_AssertExp('', ImperativeOCL_AssertExp=LogExp()), '', ImperativeOCL_AssertExp=LogExp()) == None


from python_code import ImperativeOCL_AssignExp

def test_ImperativeOCL_AssignExp___init__():
    assert ImperativeOCL_AssignExp.__init__(ImperativeOCL_AssignExp(''), '') == None


from python_code import ImperativeOCL_VariableInitExp

def test_ImperativeOCL_VariableInitExp___init__():
    assert ImperativeOCL_VariableInitExp.__init__(ImperativeOCL_VariableInitExp(''), '') == None

