from python_code import yyh_Boul

def test_yyh_Boul___init__():
    assert yyh_Boul.__init__(yyh_Boul(''), '') == None


from python_code import yyh_Bouz

def test_yyh_Bouz___init__():
    assert yyh_Bouz.__init__(yyh_Bouz('', yyh_Bouz=set()), '', yyh_Bouz=set()) == None

