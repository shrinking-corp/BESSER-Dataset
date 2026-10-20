from python_code import DiagonosticModel_Action

def test_DiagonosticModel_Action___init__():
    assert DiagonosticModel_Action.__init__(DiagonosticModel_Action('\x00', 0.0, ''), '', 0.0, '') == None


from python_code import DiagonosticModel_CheckAction

def test_DiagonosticModel_CheckAction___init__():
    assert DiagonosticModel_CheckAction.__init__(DiagonosticModel_CheckAction(''), '') == None


from python_code import DiagonosticModel_ForLoop

def test_DiagonosticModel_ForLoop___init__():
    assert DiagonosticModel_ForLoop.__init__(DiagonosticModel_ForLoop('', 0, 0), '\x00', 0, 0) == None


from python_code import DiagonosticModel_OneOf

def test_DiagonosticModel_OneOf___init__():
    assert DiagonosticModel_OneOf.__init__(DiagonosticModel_OneOf(''), '') == None


from python_code import DiagonosticModel_Range

def test_DiagonosticModel_Range___init__():
    assert DiagonosticModel_Range.__init__(DiagonosticModel_Range(0, 0), 0, 0) == None


from python_code import DiagonosticModel_TestSpecification

def test_DiagonosticModel_TestSpecification___init__():
    assert DiagonosticModel_TestSpecification.__init__(DiagonosticModel_TestSpecification('', '', '', '', '', '', DiagonosticModel_TestSpecification=set(), DiagonosticModel_TestSpecification4=set(), DiagonosticModel_TestSpecification6=set(), DiagonosticModel_TestSpecification2=set()), '\x00', '', '', '', '', '', DiagonosticModel_TestSpecification=set(), DiagonosticModel_TestSpecification4=set(), DiagonosticModel_TestSpecification6=set(), DiagonosticModel_TestSpecification2=set()) == None

def test_DiagonosticModel_TestSpecification_getSignals():
    assert DiagonosticModel_TestSpecification.getSignals(DiagonosticModel_TestSpecification('', '', '', '', '', '', DiagonosticModel_TestSpecification=set(), DiagonosticModel_TestSpecification4=set(), DiagonosticModel_TestSpecification6=set(), DiagonosticModel_TestSpecification2=set())) == None


from python_code import DiagonosticModel_Var

def test_DiagonosticModel_Var___init__():
    assert DiagonosticModel_Var.__init__(DiagonosticModel_Var(''), '') == None


from python_code import DiagonosticModel_WhileLoop

def test_DiagonosticModel_WhileLoop___init__():
    assert DiagonosticModel_WhileLoop.__init__(DiagonosticModel_WhileLoop('', '', '\x00\x00'), '', '', '') == None

