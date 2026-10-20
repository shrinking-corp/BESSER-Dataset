from python_code import Modele_Participants

def test_Modele_Participants___init__():
    assert Modele_Participants.__init__(Modele_Participants(0, '\x00', Joueur12=set()), 0, '', Joueur12=set()) == None

