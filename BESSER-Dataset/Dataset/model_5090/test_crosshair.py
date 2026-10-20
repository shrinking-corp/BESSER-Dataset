from python_code import adl402_Binding
from python_code import adl402_Interface

def test_adl402_Interface___init__():
    assert adl402_Interface.__init__(adl402_Interface('\x00\x00', '', adl402_Interface3=adl402_Binding(), adl402_Interface6=adl402_Binding(), adl402_Interface=set()), '', '', adl402_Interface3=adl402_Binding(), adl402_Interface6=adl402_Binding(), adl402_Interface=set()) == None

