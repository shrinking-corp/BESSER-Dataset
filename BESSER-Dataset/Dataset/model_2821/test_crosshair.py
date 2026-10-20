from python_code import sofiagraphics_Text

def test_sofiagraphics_Text___init__():
    assert sofiagraphics_Text.__init__(sofiagraphics_Text('\x00\x00', '', '', ''), '', '', '', '') == None

