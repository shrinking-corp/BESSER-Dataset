from python_code import Bishop

def test_Bishop___init__():
    assert Bishop.__init__(Bishop(''), '') == None


from python_code import Chess

def test_Chess___init__():
    assert Chess.__init__(Chess(''), '') == None


from python_code import King

def test_King___init__():
    assert King.__init__(King(''), '') == None


from python_code import Knight

def test_Knight___init__():
    assert Knight.__init__(Knight(''), '') == None


from python_code import ParkingLot

def test_ParkingLot___init__():
    assert ParkingLot.__init__(ParkingLot('', 0, '', 0, 0, level0=set()), '', 0, '', 0, 0, level0=set()) == None


from python_code import Pawn

def test_Pawn___init__():
    assert Pawn.__init__(Pawn(''), '') == None


from python_code import Queen

def test_Queen___init__():
    assert Queen.__init__(Queen(''), '') == None


from python_code import Rook

def test_Rook___init__():
    assert Rook.__init__(Rook(''), '') == None

