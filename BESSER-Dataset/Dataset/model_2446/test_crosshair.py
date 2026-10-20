from python_code import ioautomaton_Object
from python_code import ioautomaton_OutMessage

def test_ioautomaton_Object___init__():
    assert ioautomaton_Object.__init__(ioautomaton_Object('', ioautomaton_Object=ioautomaton_OutMessage()), '', ioautomaton_Object=ioautomaton_OutMessage()) == None


from python_code import ioautomaton_Operation
from python_code import ioautomaton_OutMessage
from python_code import ioautomaton_Transition

def test_ioautomaton_Operation___init__():
    assert ioautomaton_Operation.__init__(ioautomaton_Operation('', ioautomaton_Operation=ioautomaton_Transition(), ioautomaton_Operation27=ioautomaton_OutMessage()), '', ioautomaton_Operation=ioautomaton_Transition(), ioautomaton_Operation27=ioautomaton_OutMessage()) == None


from python_code import ioautomaton_OutMessage
from python_code import ioautomaton_Return
from python_code import ioautomaton_Transition

def test_ioautomaton_Return___init__():
    assert ioautomaton_Return.__init__(ioautomaton_Return('', ioautomaton_Return22=ioautomaton_OutMessage(), ioautomaton_Return=ioautomaton_Transition()), '', ioautomaton_Return22=ioautomaton_OutMessage(), ioautomaton_Return=ioautomaton_Transition()) == None

