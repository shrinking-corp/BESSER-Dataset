from python_code import A

def test_A___init__():
    assert A.__init__(A('', b6=set()), '', b6=set()) == None


from python_code import A1

def test_A1___init__():
    assert A1.__init__(A1(''), '') == None


from python_code import B1

def test_B1___init__():
    assert B1.__init__(B1(0), 0) == None


from python_code import C1

def test_C1___init__():
    assert C1.__init__(C1(False, 0), False, 0) == None


from python_code import CHAUFFEUR

def test_CHAUFFEUR___init__():
    assert CHAUFFEUR.__init__(CHAUFFEUR('', '', pERMIS0=set(), rESERVATION4=set()), '', '', pERMIS0=set(), rESERVATION4=set()) == None


from python_code import PERSONNEL

def test_PERSONNEL___init__():
    assert PERSONNEL.__init__(PERSONNEL('', '', False, rESERVATION2=set()), '', '', True, rESERVATION2=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

