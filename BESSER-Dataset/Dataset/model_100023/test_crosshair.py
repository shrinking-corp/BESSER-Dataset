from python_code import BibText_Article
from python_code import BibText_Author

def test_BibText_Author___init__():
    assert BibText_Author.__init__(BibText_Author('', Author=BibText_Article(), author=set()), '', Author=BibText_Article(), author=set()) == None


from python_code import BibText_BibTextEntry
from python_code import BibText_BibTextFile

def test_BibText_BibTextEntry___init__():
    assert BibText_BibTextEntry.__init__(BibText_BibTextEntry('\x00', BibText_BibTextEntry2=set(), BibText_BibTextEntry=BibText_BibTextFile()), '', BibText_BibTextEntry2=set(), BibText_BibTextEntry=BibText_BibTextFile()) == None


from python_code import BibText_LocatedElement

def test_BibText_LocatedElement___init__():
    assert BibText_LocatedElement.__init__(BibText_LocatedElement(''), '') == None

