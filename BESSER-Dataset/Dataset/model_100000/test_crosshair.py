from python_code import BIBTEX_Entry

def test_BIBTEX_Entry___init__():
    assert BIBTEX_Entry.__init__(BIBTEX_Entry('', BIBTEX_Entry=set()), '', BIBTEX_Entry=set()) == None


from python_code import BIBTEX_Field

def test_BIBTEX_Field___init__():
    assert BIBTEX_Field.__init__(BIBTEX_Field(''), '') == None


from python_code import BIBTEX_LocatedElement

def test_BIBTEX_LocatedElement___init__():
    assert BIBTEX_LocatedElement.__init__(BIBTEX_LocatedElement('', '', '\x00\x00'), '', '', '') == None

