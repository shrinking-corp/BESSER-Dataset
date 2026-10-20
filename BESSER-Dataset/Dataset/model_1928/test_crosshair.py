from python_code import BibTeX_Article

def test_BibTeX_Article___init__():
    assert BibTeX_Article.__init__(BibTeX_Article(''), '') == None


from python_code import BibTeX_Author

def test_BibTeX_Author___init__():
    assert BibTeX_Author.__init__(BibTeX_Author(''), '') == None


from python_code import BibTeX_BibTeXEntry

def test_BibTeX_BibTeXEntry___init__():
    assert BibTeX_BibTeXEntry.__init__(BibTeX_BibTeXEntry(''), '') == None


from python_code import BibTeX_Book

def test_BibTeX_Book___init__():
    assert BibTeX_Book.__init__(BibTeX_Book(''), '') == None


from python_code import BibTeX_BibTeXFile
from python_code import BibTeX_BookTitledEntry

def test_BibTeX_BookTitledEntry___init__():
    assert BibTeX_BookTitledEntry.__init__(BibTeX_BookTitledEntry('', BibTeXEntry=BibTeX_BibTeXFile()), '', BibTeXEntry=BibTeX_BibTeXFile()) == None


from python_code import BibTeX_BibTeXFile
from python_code import BibTeX_DatedEntry

def test_BibTeX_DatedEntry___init__():
    assert BibTeX_DatedEntry.__init__(BibTeX_DatedEntry('', BibTeXEntry=BibTeX_BibTeXFile()), '', BibTeXEntry=BibTeX_BibTeXFile()) == None


from python_code import BibTeX_InBook

def test_BibTeX_InBook___init__():
    assert BibTeX_InBook.__init__(BibTeX_InBook(0), 0) == None


from python_code import BibTeX_ThesisEntry

def test_BibTeX_ThesisEntry___init__():
    assert BibTeX_ThesisEntry.__init__(BibTeX_ThesisEntry(''), '') == None


from python_code import BibTeX_BibTeXFile
from python_code import BibTeX_TitledEntry

def test_BibTeX_TitledEntry___init__():
    assert BibTeX_TitledEntry.__init__(BibTeX_TitledEntry('', BibTeXEntry=BibTeX_BibTeXFile()), '', BibTeXEntry=BibTeX_BibTeXFile()) == None


from python_code import BibTeX_Unpublished

def test_BibTeX_Unpublished___init__():
    assert BibTeX_Unpublished.__init__(BibTeX_Unpublished(''), '') == None

