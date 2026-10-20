from python_code import Publication_Publication

def test_Publication_Publication___init__():
    assert Publication_Publication.__init__(Publication_Publication('', '', '\x00\x00'), '', '', '') == None

