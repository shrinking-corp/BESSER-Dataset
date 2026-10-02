from python_code import Bibtex_BibtexEntry

def test_Bibtex_BibtexEntry___init__():
    assert Bibtex_BibtexEntry.__init__(Bibtex_BibtexEntry('', '', '\x00', '', '', '', '', '', Bibtex_BibtexEntry=set()), '', '', '', '', '\x00', '', '', '', Bibtex_BibtexEntry=set()) == None

def test_Bibtex_BibtexEntry_toString():
    assert Bibtex_BibtexEntry.toString(Bibtex_BibtexEntry('', '', '', '', '', '', '', '', Bibtex_BibtexEntry=set())) == None
