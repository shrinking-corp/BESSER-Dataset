from python_code import fl_Apply

def test_fl_Apply___init__():
    assert fl_Apply.__init__(fl_Apply('', fl_Apply=set()), '', fl_Apply=set()) == None


from python_code import fl_Argument

def test_fl_Argument___init__():
    assert fl_Argument.__init__(fl_Argument(''), '') == None


from python_code import fl_Binary
from python_code import fl_Expr

def test_fl_Binary___init__():
    assert fl_Binary.__init__(fl_Binary('', fl_Binary=fl_Expr(), fl_Binary4=fl_Expr()), '', fl_Binary=fl_Expr(), fl_Binary4=fl_Expr()) == None


from python_code import fl_DocumentRoot

def test_fl_DocumentRoot___init__():
    assert fl_DocumentRoot.__init__(fl_DocumentRoot('\x00', fl_DocumentRoot=set(), fl_DocumentRoot8=set(), fl_DocumentRoot11=set(), fl_DocumentRoot14=set()), '', fl_DocumentRoot=set(), fl_DocumentRoot8=set(), fl_DocumentRoot11=set(), fl_DocumentRoot14=set()) == None


from python_code import fl_Expr
from python_code import fl_Function
from python_code import fl_ProgramType

def test_fl_Function___init__():
    assert fl_Function.__init__(fl_Function('', '\x00', fl_Function=fl_Expr(), fl_Function27=fl_ProgramType()), '\x00\x00', '', fl_Function=fl_Expr(), fl_Function27=fl_ProgramType()) == None


from python_code import fl_Literal

def test_fl_Literal___init__():
    assert fl_Literal.__init__(fl_Literal(''), '') == None

