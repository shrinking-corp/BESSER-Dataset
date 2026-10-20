from python_code import Borrowed

def test_Borrowed___init__():
    assert Borrowed.__init__(Borrowed('', '', books1=set(), member2=set()), '', '', books1=set(), member2=set()) == None


from python_code import Quado_Branco

def test_Quado_Branco___init__():
    assert Quado_Branco.__init__(Quado_Branco(0, '', '', '', '', '', '\x00', 0, books8=set(), fine10=set(), member15=set()), 0, '', '', '', '', '', '', 0, books8=set(), fine10=set(), member15=set()) == None


from python_code import Reserved

def test_Reserved___init__():
    assert Reserved.__init__(Reserved('', books5=set(), member6=set()), '', books5=set(), member6=set()) == None

