from python_code import adl101_Binding
from python_code import adl101_Interface

def test_adl101_Interface___init__():
    assert adl101_Interface.__init__(adl101_Interface('\x00\x00', '', adl101_Interface=set(), adl101_Interface3=adl101_Binding(), adl101_Interface6=adl101_Binding()), '', '', adl101_Interface=set(), adl101_Interface3=adl101_Binding(), adl101_Interface6=adl101_Binding()) == None

