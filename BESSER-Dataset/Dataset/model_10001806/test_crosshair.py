from python_code import A
from python_code import R

def test_A___init__():
    assert A.__init__(A('', b2=set(), r5=R()), '', b2=set(), r5=R()) == None


from python_code import Client

def test_Client___init__():
    assert Client.__init__(Client('\x00\x00', '', groupe6=set()), '', '', groupe6=set()) == None


from python_code import E
from python_code import G

def test_E___init__():
    assert E.__init__(E('', g17=G()), '', g17=G()) == None


from python_code import F

def test_F___init__():
    assert F.__init__(F(''), '') == None


from python_code import Groupe
from python_code import Reservation

def test_Groupe___init__():
    assert Groupe.__init__(Groupe('', reservation8=Reservation(), client7=set()), '', reservation8=Reservation(), client7=set()) == None


from python_code import Y

def test_Y___init__():
    assert Y.__init__(Y(''), '') == None

