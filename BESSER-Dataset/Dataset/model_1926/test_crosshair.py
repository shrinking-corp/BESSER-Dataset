from python_code import bibTeX_Article

def test_bibTeX_Article___init__():
    assert bibTeX_Article.__init__(bibTeX_Article(''), '') == None


from python_code import bibTeX_Author
from python_code import bibTeX_AuthoredEntry

def test_bibTeX_Author___init__():
    assert bibTeX_Author.__init__(bibTeX_Author('', bibTeX_Author=bibTeX_AuthoredEntry()), '', bibTeX_Author=bibTeX_AuthoredEntry()) == None


from python_code import bibTeX_BibTeXEntry
from python_code import bibTeX_BibTeXFile

def test_bibTeX_BibTeXEntry___init__():
    assert bibTeX_BibTeXEntry.__init__(bibTeX_BibTeXEntry('', bibTeX_BibTeXEntry=bibTeX_BibTeXFile()), '', bibTeX_BibTeXEntry=bibTeX_BibTeXFile()) == None


from python_code import bibTeX_Book

def test_bibTeX_Book___init__():
    assert bibTeX_Book.__init__(bibTeX_Book(''), '') == None


from python_code import bibTeX_BookTitledEntry

def test_bibTeX_BookTitledEntry___init__():
    assert bibTeX_BookTitledEntry.__init__(bibTeX_BookTitledEntry(''), '') == None


from python_code import bibTeX_DatedEntry

def test_bibTeX_DatedEntry___init__():
    assert bibTeX_DatedEntry.__init__(bibTeX_DatedEntry(''), '') == None


from python_code import bibTeX_InBook

def test_bibTeX_InBook___init__():
    assert bibTeX_InBook.__init__(bibTeX_InBook(''), '') == None


from python_code import bibTeX_ThesisEntry

def test_bibTeX_ThesisEntry___init__():
    assert bibTeX_ThesisEntry.__init__(bibTeX_ThesisEntry(''), '') == None


from python_code import bibTeX_TitledEntry

def test_bibTeX_TitledEntry___init__():
    assert bibTeX_TitledEntry.__init__(bibTeX_TitledEntry(''), '') == None


from python_code import bibTeX_Unpublished

def test_bibTeX_Unpublished___init__():
    assert bibTeX_Unpublished.__init__(bibTeX_Unpublished(''), '') == None

