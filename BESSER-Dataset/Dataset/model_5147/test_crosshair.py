from python_code import g_C

def test_g_C___init__():
    assert g_C.__init__(g_C(''), '') == None

from python_code import g_X

def test_g_X___init__():
    assert g_X.__init__(g_X(g_X=set()), g_X=set()) == None

def test_g_X_foo():
    assert g_X.foo(g_X(g_X=set())) == None
