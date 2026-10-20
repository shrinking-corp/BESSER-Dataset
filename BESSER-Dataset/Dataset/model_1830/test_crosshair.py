from python_code import jointPackage_SrcArticle

def test_jointPackage_SrcArticle___init__():
    assert jointPackage_SrcArticle.__init__(jointPackage_SrcArticle(''), '') == None


from python_code import jointPackage_SrcAuthor

def test_jointPackage_SrcAuthor___init__():
    assert jointPackage_SrcAuthor.__init__(jointPackage_SrcAuthor(''), '') == None


from python_code import jointPackage_SrcBibTeXEntry

def test_jointPackage_SrcBibTeXEntry___init__():
    assert jointPackage_SrcBibTeXEntry.__init__(jointPackage_SrcBibTeXEntry(''), '') == None


from python_code import jointPackage_SrcBook

def test_jointPackage_SrcBook___init__():
    assert jointPackage_SrcBook.__init__(jointPackage_SrcBook(''), '') == None


from python_code import jointPackage_SrcBibTeXFile
from python_code import jointPackage_SrcBookTitledEntry

def test_jointPackage_SrcBookTitledEntry___init__():
    assert jointPackage_SrcBookTitledEntry.__init__(jointPackage_SrcBookTitledEntry('', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()) == None


from python_code import jointPackage_SrcBibTeXFile
from python_code import jointPackage_SrcDatedEntry

def test_jointPackage_SrcDatedEntry___init__():
    assert jointPackage_SrcDatedEntry.__init__(jointPackage_SrcDatedEntry('', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()) == None


from python_code import jointPackage_SrcInBook

def test_jointPackage_SrcInBook___init__():
    assert jointPackage_SrcInBook.__init__(jointPackage_SrcInBook(0), 0) == None


from python_code import jointPackage_SrcThesisEntry

def test_jointPackage_SrcThesisEntry___init__():
    assert jointPackage_SrcThesisEntry.__init__(jointPackage_SrcThesisEntry(''), '') == None


from python_code import jointPackage_SrcBibTeXFile
from python_code import jointPackage_SrcTitledEntry

def test_jointPackage_SrcTitledEntry___init__():
    assert jointPackage_SrcTitledEntry.__init__(jointPackage_SrcTitledEntry('', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_SrcBibTeXFile()) == None


from python_code import jointPackage_SrcUnpublished

def test_jointPackage_SrcUnpublished___init__():
    assert jointPackage_SrcUnpublished.__init__(jointPackage_SrcUnpublished(''), '') == None


from python_code import TrgSection
from python_code import jointPackage_TrgPara

def test_jointPackage_TrgPara___init__():
    assert jointPackage_TrgPara.__init__(jointPackage_TrgPara('', paras=TrgSection()), '\x00', paras=TrgSection()) == None


from python_code import jointPackage_TrgTitledElement

def test_jointPackage_TrgTitledElement___init__():
    assert jointPackage_TrgTitledElement.__init__(jointPackage_TrgTitledElement(''), '') == None

