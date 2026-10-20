from python_code import ChangeAppearance

def test_ChangeAppearance___init__():
    assert ChangeAppearance.__init__(ChangeAppearance(0, 0, 0, 0, '', '', '', 0, 0, False, '\x00', ''), 0, 0, 0, 0, '', '', '', 0, 0, True, '', '') == None


from python_code import ChangeOptions

def test_ChangeOptions___init__():
    assert ChangeOptions.__init__(ChangeOptions('', False, 0, '', '\x00', '', 0, '', 0, '', 0, 0, '', '', ''), '', False, 0, '', '', '\x00', 0, '', 0, '', 0, 0, '', '', '') == None


from python_code import FireworksDisplay

def test_FireworksDisplay___init__():
    assert FireworksDisplay.__init__(FireworksDisplay(0, 0, 0, 0, '', '', '\x00', '', '', 0, 0, 0, '', ''), 0, 0, 0, 0, '', '', '', '', '\x00', 0, 0, 0, '', '') == None


from python_code import SolitaireLayout

def test_SolitaireLayout___init__():
    assert SolitaireLayout.__init__(SolitaireLayout('', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''), '\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '') == None

