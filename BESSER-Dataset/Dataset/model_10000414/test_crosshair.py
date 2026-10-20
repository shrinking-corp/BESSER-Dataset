from python_code import Administrateur

def test_Administrateur___init__():
    assert Administrateur.__init__(Administrateur(0, False, personne13=set()), 0, False, personne13=set()) == None


from python_code import BankAccount

def test_BankAccount___init__():
    assert BankAccount.__init__(BankAccount('\x00', 0.0), '', 0.0) == None


from python_code import CCP

def test_CCP___init__():
    assert CCP.__init__(CCP(0, '', '', formation19=set()), 0, '', '', formation19=set()) == None


from python_code import ClassA

def test_ClassA___init__():
    assert ClassA.__init__(ClassA(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import ClassC

def test_ClassC___init__():
    assert ClassC.__init__(ClassC(0.0, 0, '', ''), 0.0, 0, '', '') == None


from python_code import Direction

def test_Direction___init__():
    assert Direction.__init__(Direction(0, False, personne11=set()), 0, False, personne11=set()) == None


from python_code import Etudiant

def test_Etudiant___init__():
    assert Etudiant.__init__(Etudiant(0, 0.0, '', '', False, personne7=set(), session22=set()), 0, 0.0, '', '', False, personne7=set(), session22=set()) == None


from python_code import Formateur

def test_Formateur___init__():
    assert Formateur.__init__(Formateur(0, False, personne9=set(), session15=set()), 0, True, personne9=set(), session15=set()) == None

