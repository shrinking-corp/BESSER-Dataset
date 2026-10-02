from python_code import bibTeX_AddressField
from python_code import bibTeX_Book

def test_bibTeX_AddressField___init__():
    assert bibTeX_AddressField.__init__(bibTeX_AddressField('', bibTeX_AddressField=bibTeX_Book()), '', bibTeX_AddressField=bibTeX_Book()) == None

from python_code import bibTeX_BibtexEntryTypes
from python_code import bibTeX_CiteKey

def test_bibTeX_CiteKey___init__():
    assert bibTeX_CiteKey.__init__(bibTeX_CiteKey('', bibTeX_CiteKey=bibTeX_BibtexEntryTypes()), '', bibTeX_CiteKey=bibTeX_BibtexEntryTypes()) == None

from python_code import bibTeX_Book
from python_code import bibTeX_EditionField

def test_bibTeX_EditionField___init__():
    assert bibTeX_EditionField.__init__(bibTeX_EditionField('', bibTeX_EditionField=bibTeX_Book()), '', bibTeX_EditionField=bibTeX_Book()) == None

from python_code import bibTeX_EditorField

def test_bibTeX_EditorField___init__():
    assert bibTeX_EditorField.__init__(bibTeX_EditorField(''), '') == None

from python_code import bibTeX_Authors
from python_code import bibTeX_Fullname

def test_bibTeX_Fullname___init__():
    assert bibTeX_Fullname.__init__(bibTeX_Fullname('', '\x00', bibTeX_Fullname=bibTeX_Authors()), '\x00\x00', '', bibTeX_Fullname=bibTeX_Authors()) == None

from python_code import bibTeX_Book
from python_code import bibTeX_IsbnField

def test_bibTeX_IsbnField___init__():
    assert bibTeX_IsbnField.__init__(bibTeX_IsbnField('', bibTeX_IsbnField=bibTeX_Book()), '', bibTeX_IsbnField=bibTeX_Book()) == None

from python_code import bibTeX_Article
from python_code import bibTeX_JournalField

def test_bibTeX_JournalField___init__():
    assert bibTeX_JournalField.__init__(bibTeX_JournalField('', bibTeX_JournalField=bibTeX_Article()), '', bibTeX_JournalField=bibTeX_Article()) == None

from python_code import bibTeX_BibtexEntryTypes
from python_code import bibTeX_MonthField

def test_bibTeX_MonthField___init__():
    assert bibTeX_MonthField.__init__(bibTeX_MonthField('', bibTeX_MonthField=bibTeX_BibtexEntryTypes()), '', bibTeX_MonthField=bibTeX_BibtexEntryTypes()) == None

from python_code import bibTeX_BibtexEntryTypes
from python_code import bibTeX_NoteField

def test_bibTeX_NoteField___init__():
    assert bibTeX_NoteField.__init__(bibTeX_NoteField('', bibTeX_NoteField=bibTeX_BibtexEntryTypes()), '', bibTeX_NoteField=bibTeX_BibtexEntryTypes()) == None

from python_code import bibTeX_Article
from python_code import bibTeX_NumberField

def test_bibTeX_NumberField___init__():
    assert bibTeX_NumberField.__init__(bibTeX_NumberField('', bibTeX_NumberField=bibTeX_Article()), '', bibTeX_NumberField=bibTeX_Article()) == None

from python_code import bibTeX_Article
from python_code import bibTeX_PagesField

def test_bibTeX_PagesField___init__():
    assert bibTeX_PagesField.__init__(bibTeX_PagesField('', bibTeX_PagesField=bibTeX_Article()), '', bibTeX_PagesField=bibTeX_Article()) == None

from python_code import bibTeX_Book
from python_code import bibTeX_PublisherField

def test_bibTeX_PublisherField___init__():
    assert bibTeX_PublisherField.__init__(bibTeX_PublisherField('', bibTeX_PublisherField=bibTeX_Book()), '', bibTeX_PublisherField=bibTeX_Book()) == None

from python_code import bibTeX_Book
from python_code import bibTeX_SeriesField

def test_bibTeX_SeriesField___init__():
    assert bibTeX_SeriesField.__init__(bibTeX_SeriesField('', bibTeX_SeriesField=bibTeX_Book()), '', bibTeX_SeriesField=bibTeX_Book()) == None

from python_code import bibTeX_BibtexEntryTypes
from python_code import bibTeX_TitleField

def test_bibTeX_TitleField___init__():
    assert bibTeX_TitleField.__init__(bibTeX_TitleField('', bibTeX_TitleField=bibTeX_BibtexEntryTypes()), '', bibTeX_TitleField=bibTeX_BibtexEntryTypes()) == None

from python_code import bibTeX_UnknownField
from python_code import bibTeX_UnknownType

def test_bibTeX_UnknownType___init__():
    assert bibTeX_UnknownType.__init__(bibTeX_UnknownType('', bibTeX_UnknownType=bibTeX_UnknownField()), '', bibTeX_UnknownType=bibTeX_UnknownField()) == None

from python_code import bibTeX_UnknownField
from python_code import bibTeX_UnknownValue

def test_bibTeX_UnknownValue___init__():
    assert bibTeX_UnknownValue.__init__(bibTeX_UnknownValue('', bibTeX_UnknownValue=bibTeX_UnknownField()), '', bibTeX_UnknownValue=bibTeX_UnknownField()) == None

from python_code import bibTeX_Article
from python_code import bibTeX_VolumeField

def test_bibTeX_VolumeField___init__():
    assert bibTeX_VolumeField.__init__(bibTeX_VolumeField('', bibTeX_VolumeField=bibTeX_Article()), '', bibTeX_VolumeField=bibTeX_Article()) == None

from python_code import bibTeX_BibtexEntryTypes
from python_code import bibTeX_YearField

def test_bibTeX_YearField___init__():
    assert bibTeX_YearField.__init__(bibTeX_YearField('', bibTeX_YearField=bibTeX_BibtexEntryTypes()), '', bibTeX_YearField=bibTeX_BibtexEntryTypes()) == None
