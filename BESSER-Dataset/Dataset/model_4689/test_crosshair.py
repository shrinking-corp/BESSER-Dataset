from python_code import simpleal_ArithLit

def test_simpleal_ArithLit___init__():
    assert simpleal_ArithLit.__init__(simpleal_ArithLit(0), 0) == None


from python_code import simpleal_Arith
from python_code import simpleal_Assign

def test_simpleal_Assign___init__():
    assert simpleal_Assign.__init__(simpleal_Assign('', simpleal_Assign=simpleal_Arith()), '', simpleal_Assign=simpleal_Arith()) == None


from python_code import simpleal_Print

def test_simpleal_Print___init__():
    assert simpleal_Print.__init__(simpleal_Print(''), '') == None


from python_code import simpleal_VarRef

def test_simpleal_VarRef___init__():
    assert simpleal_VarRef.__init__(simpleal_VarRef(''), '') == None

