from python_code import vmlogo_StackFrame
from python_code import vmlogo_Variable

def test_vmlogo_Variable___init__():
    assert vmlogo_Variable.__init__(vmlogo_Variable('\x00', 0.0, vmlogo_Variable=vmlogo_StackFrame()), '', 0.0, vmlogo_Variable=vmlogo_StackFrame()) == None

