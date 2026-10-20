from python_code import typeA_RootA

def test_typeA_RootA___init__():
    assert typeA_RootA.__init__(typeA_RootA('\x00', typeA_RootA=set()), '', typeA_RootA=set()) == None

