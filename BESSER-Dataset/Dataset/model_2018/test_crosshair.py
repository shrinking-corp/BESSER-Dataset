from python_code import execTraces_BoolLiteral

def test_execTraces_BoolLiteral___init__():
    assert execTraces_BoolLiteral.__init__(execTraces_BoolLiteral(''), '') == None


from python_code import execTraces_ExecTraces

def test_execTraces_ExecTraces___init__():
    assert execTraces_ExecTraces.__init__(execTraces_ExecTraces('', execTraces_ExecTraces=set(), execTraces_ExecTraces2=set()), '', execTraces_ExecTraces=set(), execTraces_ExecTraces2=set()) == None


from python_code import execTraces_IntLiteral

def test_execTraces_IntLiteral___init__():
    assert execTraces_IntLiteral.__init__(execTraces_IntLiteral(0), 0) == None


from python_code import execTraces_RealLiteral

def test_execTraces_RealLiteral___init__():
    assert execTraces_RealLiteral.__init__(execTraces_RealLiteral(0, 0), 0, 0) == None

