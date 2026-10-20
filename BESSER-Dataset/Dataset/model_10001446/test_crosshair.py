from python_code import Covoiturage_Authentification

def test_Covoiturage_Authentification___init__():
    assert Covoiturage_Authentification.__init__(Covoiturage_Authentification('', '', personne1=set()), '', '', personne1=set()) == None

