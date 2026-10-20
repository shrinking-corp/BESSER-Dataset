from python_code import domain_Authentification

def test_domain_Authentification___init__():
    assert domain_Authentification.__init__(domain_Authentification('\x00\x00', '', personne1=set()), '', '', personne1=set()) == None

