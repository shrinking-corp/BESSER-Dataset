from python_code import BancniRacun

def test_BancniRacun___init__():
    assert BancniRacun.__init__(BancniRacun('\x00', 0.0, False), '', 0.0, False) == None


from python_code import BancniRacun1

def test_BancniRacun1___init__():
    assert BancniRacun1.__init__(BancniRacun1('\x00', 0.0, False), '', 0.0, False) == None


from python_code import Color
from python_code import Lik

def test_Lik___init__():
    assert Lik.__init__(Lik('', Color(), '\x00'), '\x00\x00', Color(), '') == None


from python_code import Color
from python_code import Lik1

def test_Lik1___init__():
    assert Lik1.__init__(Lik1('\x00\x00', Color(), '', '', ''), '', Color(), '', '', '') == None


from python_code import Color
from python_code import Lik2

def test_Lik2___init__():
    assert Lik2.__init__(Lik2('\x00\x00', '', '', '', Color()), '', '', '', '', Color()) == None


from python_code import Color
from python_code import Lik3

def test_Lik3___init__():
    assert Lik3.__init__(Lik3('', '\x00', Color()), '\x00\x00', '', Color()) == None


from python_code import LocalDate
from python_code import Oseba

def test_Oseba___init__():
    assert Oseba.__init__(Oseba('', '', '\x00\x00', LocalDate()), '', '', '', LocalDate()) == None


from python_code import Oseba1

def test_Oseba1___init__():
    assert Oseba1.__init__(Oseba1('', '', '\x00\x00'), '', '', '') == None


import datetime as _ch_datetime
from python_code import Oseba2

def test_Oseba2___init__():
    assert Oseba2.__init__(Oseba2('', '\x00', _ch_datetime.date(1, 1, 3)), '', '', _ch_datetime.date(1, 1, 1)) == None


from python_code import Pes

def test_Pes___init__():
    assert Pes.__init__(Pes('', '', '\x00\x00'), '', '', '') == None


from python_code import PravokotniLik

def test_PravokotniLik___init__():
    assert PravokotniLik.__init__(PravokotniLik('', '\x00'), '\x00\x00', '') == None


from python_code import Pravokotnik1

def test_Pravokotnik1___init__():
    assert Pravokotnik1.__init__(Pravokotnik1('', '\x00'), '\x00\x00', '') == None


from python_code import Pravokotnik3

def test_Pravokotnik3___init__():
    assert Pravokotnik3.__init__(Pravokotnik3('', '\x00'), '\x00\x00', '') == None


from python_code import PravokotnikA

def test_PravokotnikA___init__():
    assert PravokotnikA.__init__(PravokotnikA('', '\x00'), '\x00\x00', '') == None


from python_code import Razred

def test_Razred___init__():
    assert Razred.__init__(Razred(''), '') == None


from python_code import RazredA

def test_RazredA___init__():
    assert RazredA.__init__(RazredA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import RazredA1

def test_RazredA1___init__():
    assert RazredA1.__init__(RazredA1(''), '') == None


from python_code import RazredA2
from python_code import RazredB2

def test_RazredA2___init__():
    assert RazredA2.__init__(RazredA2(RazredB2(), razredB20=RazredB2(), razredB22=RazredB2()), RazredB2(), razredB20=RazredB2(), razredB22=RazredB2()) == None


from python_code import RazredC

def test_RazredC___init__():
    assert RazredC.__init__(RazredC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import RazredC1

def test_RazredC1___init__():
    assert RazredC1.__init__(RazredC1(''), '') == None


from python_code import LocalDate1
from python_code import Student

def test_Student___init__():
    assert Student.__init__(Student('', '\x00', LocalDate1()), '\x00\x00', '', LocalDate1()) == None


from python_code import Zaposlen

def test_Zaposlen___init__():
    assert Zaposlen.__init__(Zaposlen('\x00', 0.0), '', 0.0) == None

