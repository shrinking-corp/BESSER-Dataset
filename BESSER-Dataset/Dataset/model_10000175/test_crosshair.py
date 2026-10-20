from python_code import Agent

def test_Agent___init__():
    assert Agent.__init__(Agent('', '', '', 0, 0, Agent_Kupac_06=set(), Agent_Aran_man_08=set()), '', '', '', 0, 0, Agent_Kupac_06=set(), Agent_Aran_man_08=set()) == None


from python_code import Osiguranje

def test_Osiguranje___init__():
    assert Osiguranje.__init__(Osiguranje('', '', '', 0, '', Osiguranje_Putnik_00=set()), '', '', '', 0, '', Osiguranje_Putnik_00=set()) == None


from python_code import Transakcija

def test_Transakcija___init__():
    assert Transakcija.__init__(Transakcija('', '', '', '', Transakcija_Kupac_04=set()), '', '', '', '', Transakcija_Kupac_04=set()) == None

