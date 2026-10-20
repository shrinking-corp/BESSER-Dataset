from python_code import jointPackage_BibTeX2DocBook_SrcArticle

def test_jointPackage_BibTeX2DocBook_SrcArticle___init__():
    assert jointPackage_BibTeX2DocBook_SrcArticle.__init__(jointPackage_BibTeX2DocBook_SrcArticle(''), '') == None


from python_code import jointPackage_BibTeX2DocBook_SrcAuthor

def test_jointPackage_BibTeX2DocBook_SrcAuthor___init__():
    assert jointPackage_BibTeX2DocBook_SrcAuthor.__init__(jointPackage_BibTeX2DocBook_SrcAuthor(''), '') == None


from python_code import jointPackage_BibTeX2DocBook_SrcBibTeXEntry

def test_jointPackage_BibTeX2DocBook_SrcBibTeXEntry___init__():
    assert jointPackage_BibTeX2DocBook_SrcBibTeXEntry.__init__(jointPackage_BibTeX2DocBook_SrcBibTeXEntry(''), '') == None


from python_code import jointPackage_BibTeX2DocBook_SrcBook

def test_jointPackage_BibTeX2DocBook_SrcBook___init__():
    assert jointPackage_BibTeX2DocBook_SrcBook.__init__(jointPackage_BibTeX2DocBook_SrcBook(''), '') == None


from python_code import jointPackage_BibTeX2DocBook_SrcBibTeXFile
from python_code import jointPackage_BibTeX2DocBook_SrcBookTitledEntry

def test_jointPackage_BibTeX2DocBook_SrcBookTitledEntry___init__():
    assert jointPackage_BibTeX2DocBook_SrcBookTitledEntry.__init__(jointPackage_BibTeX2DocBook_SrcBookTitledEntry('', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()) == None


from python_code import jointPackage_BibTeX2DocBook_SrcBibTeXFile
from python_code import jointPackage_BibTeX2DocBook_SrcDatedEntry

def test_jointPackage_BibTeX2DocBook_SrcDatedEntry___init__():
    assert jointPackage_BibTeX2DocBook_SrcDatedEntry.__init__(jointPackage_BibTeX2DocBook_SrcDatedEntry('', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()) == None


from python_code import jointPackage_BibTeX2DocBook_SrcInBook

def test_jointPackage_BibTeX2DocBook_SrcInBook___init__():
    assert jointPackage_BibTeX2DocBook_SrcInBook.__init__(jointPackage_BibTeX2DocBook_SrcInBook(0), 0) == None


from python_code import jointPackage_BibTeX2DocBook_SrcThesisEntry

def test_jointPackage_BibTeX2DocBook_SrcThesisEntry___init__():
    assert jointPackage_BibTeX2DocBook_SrcThesisEntry.__init__(jointPackage_BibTeX2DocBook_SrcThesisEntry(''), '') == None


from python_code import jointPackage_BibTeX2DocBook_SrcBibTeXFile
from python_code import jointPackage_BibTeX2DocBook_SrcTitledEntry

def test_jointPackage_BibTeX2DocBook_SrcTitledEntry___init__():
    assert jointPackage_BibTeX2DocBook_SrcTitledEntry.__init__(jointPackage_BibTeX2DocBook_SrcTitledEntry('', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()), '', SrcBibTeXEntry=jointPackage_BibTeX2DocBook_SrcBibTeXFile()) == None


from python_code import jointPackage_BibTeX2DocBook_SrcUnpublished

def test_jointPackage_BibTeX2DocBook_SrcUnpublished___init__():
    assert jointPackage_BibTeX2DocBook_SrcUnpublished.__init__(jointPackage_BibTeX2DocBook_SrcUnpublished(''), '') == None


from python_code import TrgSection
from python_code import jointPackage_BibTeX2DocBook_TrgPara

def test_jointPackage_BibTeX2DocBook_TrgPara___init__():
    assert jointPackage_BibTeX2DocBook_TrgPara.__init__(jointPackage_BibTeX2DocBook_TrgPara('', paras=TrgSection()), '\x00', paras=TrgSection()) == None


from python_code import jointPackage_BibTeX2DocBook_TrgTitledElement

def test_jointPackage_BibTeX2DocBook_TrgTitledElement___init__():
    assert jointPackage_BibTeX2DocBook_TrgTitledElement.__init__(jointPackage_BibTeX2DocBook_TrgTitledElement(''), '') == None

