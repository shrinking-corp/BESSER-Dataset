from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', r3=R(), b4=set()), '', r3=R(), b4=set()) == None


from python_code import Personne

def test_Personne___init__():
    assert Personne.__init__(Personne(0, '', '', sport6=set(), lieu9=set()), 0, '', '', sport6=set(), lieu9=set()) == None


from python_code import Sport

def test_Sport___init__():
    assert Sport.__init__(Sport(0, '', personne7=set(), lieu10=set()), 0, '', personne7=set(), lieu10=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

