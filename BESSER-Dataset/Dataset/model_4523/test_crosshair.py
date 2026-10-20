from python_code import vmlogo_CallStack
from python_code import vmlogo_StackFrame

def test_vmlogo_StackFrame___init__():
    assert vmlogo_StackFrame.__init__(vmlogo_StackFrame('', vmlogo_StackFrame=vmlogo_CallStack()), '', vmlogo_StackFrame=vmlogo_CallStack()) == None

