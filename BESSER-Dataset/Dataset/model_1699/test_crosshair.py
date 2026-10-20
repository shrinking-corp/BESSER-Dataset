from python_code import yyg_Boul

def test_yyg_Boul___init__():
    assert yyg_Boul.__init__(yyg_Boul(''), '') == None


from python_code import yyg_Bouz

def test_yyg_Bouz___init__():
    assert yyg_Bouz.__init__(yyg_Bouz('', yyg_Bouz=set()), '', yyg_Bouz=set()) == None

