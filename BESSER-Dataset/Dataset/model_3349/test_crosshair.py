from python_code import smallJava_SJBoolConstant

def test_smallJava_SJBoolConstant___init__():
    assert smallJava_SJBoolConstant.__init__(smallJava_SJBoolConstant(''), '') == None


from python_code import smallJava_SJIntConstant

def test_smallJava_SJIntConstant___init__():
    assert smallJava_SJIntConstant.__init__(smallJava_SJIntConstant(0), 0) == None


from python_code import smallJava_SJProgram

def test_smallJava_SJProgram___init__():
    assert smallJava_SJProgram.__init__(smallJava_SJProgram('', smallJava_SJProgram=set(), smallJava_SJProgram2=set()), '', smallJava_SJProgram=set(), smallJava_SJProgram2=set()) == None


from python_code import smallJava_SJStringConstant

def test_smallJava_SJStringConstant___init__():
    assert smallJava_SJStringConstant.__init__(smallJava_SJStringConstant(''), '') == None

