from python_code import hello122_NamedElement

def test_hello122_NamedElement___init__():
    assert hello122_NamedElement.__init__(hello122_NamedElement('\x00', hello122_NamedElement=set()), '', hello122_NamedElement=set()) == None


from python_code import hello122_Base
from python_code import hello122_Top

def test_hello122_Top___init__():
    assert hello122_Top.__init__(hello122_Top('\x00', hello122_Top=hello122_Base(), hello122_Top37=set()), '', hello122_Top=hello122_Base(), hello122_Top37=set()) == None

