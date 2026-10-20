from python_code import Persoon

def test_Persoon___init__():
    assert Persoon.__init__(Persoon('', '', '', '', ''), '', '', '', '', '') == None

