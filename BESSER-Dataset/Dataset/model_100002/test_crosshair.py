from python_code import BIBTEXML_Article

def test_BIBTEXML_Article___init__():
    assert BIBTEXML_Article.__init__(BIBTEXML_Article('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import BIBTEXML_Author

def test_BIBTEXML_Author___init__():
    assert BIBTEXML_Author.__init__(BIBTEXML_Author(''), '') == None


from python_code import BIBTEXML_Book

def test_BIBTEXML_Book___init__():
    assert BIBTEXML_Book.__init__(BIBTEXML_Book('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_BookTitledEntry

def test_BIBTEXML_BookTitledEntry___init__():
    assert BIBTEXML_BookTitledEntry.__init__(BIBTEXML_BookTitledEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_Booklet

def test_BIBTEXML_Booklet___init__():
    assert BIBTEXML_Booklet.__init__(BIBTEXML_Booklet('', '', '', BIBTEXML_Booklet=set()), '', '', '', BIBTEXML_Booklet=set()) == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_DatedEntry

def test_BIBTEXML_DatedEntry___init__():
    assert BIBTEXML_DatedEntry.__init__(BIBTEXML_DatedEntry('', '\x00', Entry=BIBTEXML_BibtexFile()), '\x00\x00', '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_EditoredEntry

def test_BIBTEXML_EditoredEntry___init__():
    assert BIBTEXML_EditoredEntry.__init__(BIBTEXML_EditoredEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_Entry

def test_BIBTEXML_Entry___init__():
    assert BIBTEXML_Entry.__init__(BIBTEXML_Entry('', '\x00'), '\x00\x00', '') == None


from python_code import BIBTEXML_InBook

def test_BIBTEXML_InBook___init__():
    assert BIBTEXML_InBook.__init__(BIBTEXML_InBook('', '\x00'), '\x00\x00', '') == None


from python_code import BIBTEXML_InCollection

def test_BIBTEXML_InCollection___init__():
    assert BIBTEXML_InCollection.__init__(BIBTEXML_InCollection('', '\x00'), '\x00\x00', '') == None


from python_code import BIBTEXML_InProceedings

def test_BIBTEXML_InProceedings___init__():
    assert BIBTEXML_InProceedings.__init__(BIBTEXML_InProceedings(''), '') == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_InstitutionEntry

def test_BIBTEXML_InstitutionEntry___init__():
    assert BIBTEXML_InstitutionEntry.__init__(BIBTEXML_InstitutionEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_JournalEntry

def test_BIBTEXML_JournalEntry___init__():
    assert BIBTEXML_JournalEntry.__init__(BIBTEXML_JournalEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_Manual

def test_BIBTEXML_Manual___init__():
    assert BIBTEXML_Manual.__init__(BIBTEXML_Manual('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_Misc

def test_BIBTEXML_Misc___init__():
    assert BIBTEXML_Misc.__init__(BIBTEXML_Misc('', '', '', '', '', BIBTEXML_Misc=set(), Entry=BIBTEXML_BibtexFile()), '', '', '', '\x00', '', BIBTEXML_Misc=set(), Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_NotedEntry

def test_BIBTEXML_NotedEntry___init__():
    assert BIBTEXML_NotedEntry.__init__(BIBTEXML_NotedEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_Proceedings

def test_BIBTEXML_Proceedings___init__():
    assert BIBTEXML_Proceedings.__init__(BIBTEXML_Proceedings('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_PublisheredEntry

def test_BIBTEXML_PublisheredEntry___init__():
    assert BIBTEXML_PublisheredEntry.__init__(BIBTEXML_PublisheredEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_SchoolEntry

def test_BIBTEXML_SchoolEntry___init__():
    assert BIBTEXML_SchoolEntry.__init__(BIBTEXML_SchoolEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None


from python_code import BIBTEXML_TechReport

def test_BIBTEXML_TechReport___init__():
    assert BIBTEXML_TechReport.__init__(BIBTEXML_TechReport('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import BIBTEXML_ThesisEntry

def test_BIBTEXML_ThesisEntry___init__():
    assert BIBTEXML_ThesisEntry.__init__(BIBTEXML_ThesisEntry('', '', '\x00\x00'), '', '', '') == None


from python_code import BIBTEXML_BibtexFile
from python_code import BIBTEXML_TitledEntry

def test_BIBTEXML_TitledEntry___init__():
    assert BIBTEXML_TitledEntry.__init__(BIBTEXML_TitledEntry('', Entry=BIBTEXML_BibtexFile()), '', Entry=BIBTEXML_BibtexFile()) == None

