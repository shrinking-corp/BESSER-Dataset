from python_code import SMTlib2extended_BitstringExpression

def test_SMTlib2extended_BitstringExpression___init__():
    assert SMTlib2extended_BitstringExpression.__init__(SMTlib2extended_BitstringExpression(''), '') == None


from python_code import SMTlib2extended_Bitvector

def test_SMTlib2extended_Bitvector___init__():
    assert SMTlib2extended_Bitvector.__init__(SMTlib2extended_Bitvector(0), 0) == None


from python_code import SMTlib2extended_CardExpression

def test_SMTlib2extended_CardExpression___init__():
    assert SMTlib2extended_CardExpression.__init__(SMTlib2extended_CardExpression(0, SMTlib2extended_CardExpression=set()), 0, SMTlib2extended_CardExpression=set()) == None


from python_code import SMTlib2extended_ConstBooleanExpression

def test_SMTlib2extended_ConstBooleanExpression___init__():
    assert SMTlib2extended_ConstBooleanExpression.__init__(SMTlib2extended_ConstBooleanExpression(True), False) == None


from python_code import SMTlib2extended_ConstIntegerExpression

def test_SMTlib2extended_ConstIntegerExpression___init__():
    assert SMTlib2extended_ConstIntegerExpression.__init__(SMTlib2extended_ConstIntegerExpression(0, 0), 0, 0) == None


from python_code import SMTlib2extended_ExtractIndexExpression

def test_SMTlib2extended_ExtractIndexExpression___init__():
    assert SMTlib2extended_ExtractIndexExpression.__init__(SMTlib2extended_ExtractIndexExpression(0, 0), 0, 0) == None


from python_code import SMTlib2extended_NamedElement

def test_SMTlib2extended_NamedElement___init__():
    assert SMTlib2extended_NamedElement.__init__(SMTlib2extended_NamedElement(''), '') == None

