from python_code import Traces_EObject
from python_code import Traces_Trace

def test_Traces_Trace___init__():
    assert Traces_Trace.__init__(Traces_Trace('', Traces_Trace=Traces_EObject(), Traces_Trace2=Traces_EObject()), '', Traces_Trace=Traces_EObject(), Traces_Trace2=Traces_EObject()) == None

