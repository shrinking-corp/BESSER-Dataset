from python_code import adlrecur_Component

def test_adlrecur_Component___init__():
    assert adlrecur_Component.__init__(adlrecur_Component('', adlrecur_Component=set(), adlrecur_Component2=set()), '', adlrecur_Component=set(), adlrecur_Component2=set()) == None


from python_code import adlrecur_Binding
from python_code import adlrecur_Interface

def test_adlrecur_Interface___init__():
    assert adlrecur_Interface.__init__(adlrecur_Interface('\x00\x00', '', adlrecur_Interface6=adlrecur_Binding(), adlrecur_Interface9=adlrecur_Binding(), adlrecur_Interface=set()), '', '', adlrecur_Interface6=adlrecur_Binding(), adlrecur_Interface9=adlrecur_Binding(), adlrecur_Interface=set()) == None

