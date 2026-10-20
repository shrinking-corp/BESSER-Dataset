from python_code import Alimento

def test_Alimento___init__():
    assert Alimento.__init__(Alimento('', '', '', True, compuesta_por1=set()), '', '', '', False, compuesta_por1=set()) == None


from python_code import RMS

def test_RMS___init__():
    assert RMS.__init__(RMS('', has2=set(), is_generated_by5=set()), '', has2=set(), is_generated_by5=set()) == None


from python_code import Vegetariano

def test_Vegetariano___init__():
    assert Vegetariano.__init__(Vegetariano(''), '') == None

