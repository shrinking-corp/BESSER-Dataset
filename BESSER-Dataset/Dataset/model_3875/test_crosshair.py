from python_code import fl_ApplyExp
from python_code import fl_Exp
from python_code import fl_Function
from python_code import fl_Program

def test_fl_Function___init__():
    assert fl_Function.__init__(fl_Function('\x00', fl_Function16=fl_ApplyExp(), fl_Function=fl_Program(), fl_Function2=set(), fl_Function4=fl_Exp()), '', fl_Function16=fl_ApplyExp(), fl_Function=fl_Program(), fl_Function2=set(), fl_Function4=fl_Exp()) == None


from python_code import fl_LiteralExp

def test_fl_LiteralExp___init__():
    assert fl_LiteralExp.__init__(fl_LiteralExp(0), 0) == None

