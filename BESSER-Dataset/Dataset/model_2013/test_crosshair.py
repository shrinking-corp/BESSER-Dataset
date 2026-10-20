from python_code import Level
from python_code import Trace_Call

def test_Trace_Call___init__():
    assert Trace_Call.__init__(Trace_Call('', '', '', '', calls=Level(), Trace_Call=set()), '', '', '', '', calls=Level(), Trace_Call=set()) == None


from python_code import Trace_Index

def test_Trace_Index___init__():
    assert Trace_Index.__init__(Trace_Index(''), '') == None


from python_code import Trace_Trace

def test_Trace_Trace___init__():
    assert Trace_Trace.__init__(Trace_Trace('', trace=set()), '', trace=set()) == None

