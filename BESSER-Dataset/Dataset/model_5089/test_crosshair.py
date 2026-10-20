from python_code import adl401_Binding
from python_code import adl401_Interface

def test_adl401_Interface___init__():
    assert adl401_Interface.__init__(adl401_Interface('\x00\x00', '', adl401_Interface3=adl401_Binding(), adl401_Interface6=adl401_Binding(), adl401_Interface=set()), '', '', adl401_Interface3=adl401_Binding(), adl401_Interface6=adl401_Binding(), adl401_Interface=set()) == None

