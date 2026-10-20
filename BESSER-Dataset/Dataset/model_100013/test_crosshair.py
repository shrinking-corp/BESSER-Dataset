from python_code import bibtex_Article

def test_bibtex_Article___init__():
    assert bibtex_Article.__init__(bibtex_Article(''), '') == None


from python_code import bibtex_Author
from python_code import bibtex_AuthoredEntry

def test_bibtex_Author___init__():
    assert bibtex_Author.__init__(bibtex_Author('', bibtex_Author=bibtex_AuthoredEntry()), '', bibtex_Author=bibtex_AuthoredEntry()) == None


from python_code import bibtex_BibTeXEntry
from python_code import bibtex_BibTeXFile

def test_bibtex_BibTeXEntry___init__():
    assert bibtex_BibTeXEntry.__init__(bibtex_BibTeXEntry('', bibtex_BibTeXEntry=bibtex_BibTeXFile()), '', bibtex_BibTeXEntry=bibtex_BibTeXFile()) == None


from python_code import bibtex_Book

def test_bibtex_Book___init__():
    assert bibtex_Book.__init__(bibtex_Book(''), '') == None


from python_code import bibtex_BookTitledEntry

def test_bibtex_BookTitledEntry___init__():
    assert bibtex_BookTitledEntry.__init__(bibtex_BookTitledEntry(''), '') == None


from python_code import bibtex_DatedEntry

def test_bibtex_DatedEntry___init__():
    assert bibtex_DatedEntry.__init__(bibtex_DatedEntry(''), '') == None


from python_code import bibtex_InBook

def test_bibtex_InBook___init__():
    assert bibtex_InBook.__init__(bibtex_InBook(0), 0) == None


from python_code import bibtex_ThesisEntry

def test_bibtex_ThesisEntry___init__():
    assert bibtex_ThesisEntry.__init__(bibtex_ThesisEntry(''), '') == None


from python_code import bibtex_TitledEntry

def test_bibtex_TitledEntry___init__():
    assert bibtex_TitledEntry.__init__(bibtex_TitledEntry(''), '') == None


from python_code import bibtex_Unpublished

def test_bibtex_Unpublished___init__():
    assert bibtex_Unpublished.__init__(bibtex_Unpublished(''), '') == None

