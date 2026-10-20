from python_code import administrateur
from python_code import reservation

def test_reservation___init__():
    assert reservation.__init__(reservation(0, administrateur6=administrateur()), 0, administrateur6=administrateur()) == None


from python_code import voiture

def test_voiture___init__():
    assert voiture.__init__(voiture('', 0), '', 0) == None

