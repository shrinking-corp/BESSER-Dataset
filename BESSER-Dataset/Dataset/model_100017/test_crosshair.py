from python_code import bibtex_ArticleEntry
from python_code import bibtex_AuthorField
from python_code import bibtex_EidField
from python_code import bibtex_JournalField
from python_code import bibtex_MonthField
from python_code import bibtex_NoteField
from python_code import bibtex_NumberField
from python_code import bibtex_PageField
from python_code import bibtex_PartField
from python_code import bibtex_TitleField
from python_code import bibtex_VolumeField
from python_code import bibtex_YearField

def test_bibtex_ArticleEntry___init__():
    assert bibtex_ArticleEntry.__init__(bibtex_ArticleEntry(bibtex_ArticleEntry73=bibtex_PartField(), bibtex_ArticleEntry75=bibtex_EidField(), bibtex_ArticleEntry53=bibtex_YearField(), bibtex_ArticleEntry56=bibtex_JournalField(), bibtex_ArticleEntry=bibtex_AuthorField(), bibtex_ArticleEntry50=bibtex_TitleField(), bibtex_ArticleEntry58=bibtex_PageField(), bibtex_ArticleEntry61=bibtex_VolumeField(), bibtex_ArticleEntry64=bibtex_NumberField(), bibtex_ArticleEntry67=bibtex_MonthField(), bibtex_ArticleEntry70=bibtex_NoteField()), bibtex_ArticleEntry73=bibtex_PartField(), bibtex_ArticleEntry75=bibtex_EidField(), bibtex_ArticleEntry53=bibtex_YearField(), bibtex_ArticleEntry56=bibtex_JournalField(), bibtex_ArticleEntry=bibtex_AuthorField(), bibtex_ArticleEntry50=bibtex_TitleField(), bibtex_ArticleEntry58=bibtex_PageField(), bibtex_ArticleEntry61=bibtex_VolumeField(), bibtex_ArticleEntry64=bibtex_NumberField(), bibtex_ArticleEntry67=bibtex_MonthField(), bibtex_ArticleEntry70=bibtex_NoteField()) == None

def test_bibtex_ArticleEntry_getFields():
    assert bibtex_ArticleEntry.getFields(bibtex_ArticleEntry(bibtex_ArticleEntry73=bibtex_PartField(), bibtex_ArticleEntry75=bibtex_EidField(), bibtex_ArticleEntry53=bibtex_YearField(), bibtex_ArticleEntry56=bibtex_JournalField(), bibtex_ArticleEntry=bibtex_AuthorField(), bibtex_ArticleEntry50=bibtex_TitleField(), bibtex_ArticleEntry58=bibtex_PageField(), bibtex_ArticleEntry61=bibtex_VolumeField(), bibtex_ArticleEntry64=bibtex_NumberField(), bibtex_ArticleEntry67=bibtex_MonthField(), bibtex_ArticleEntry70=bibtex_NoteField())) == None


from python_code import bibtex_AbstractField
from python_code import bibtex_Bibliography
from python_code import bibtex_BibtexKeyField
from python_code import bibtex_Entry
from python_code import bibtex_KeywordField
from python_code import bibtex_ReviewField
from python_code import bibtex_UrlField

def test_bibtex_Entry___init__():
    assert bibtex_Entry.__init__(bibtex_Entry(bibtex_Entry77=bibtex_Bibliography(), bibtex_Entry=bibtex_BibtexKeyField(), bibtex_Entry9=bibtex_AbstractField(), bibtex_Entry11=bibtex_UrlField(), bibtex_Entry13=bibtex_KeywordField(), bibtex_Entry16=bibtex_ReviewField()), bibtex_Entry77=bibtex_Bibliography(), bibtex_Entry=bibtex_BibtexKeyField(), bibtex_Entry9=bibtex_AbstractField(), bibtex_Entry11=bibtex_UrlField(), bibtex_Entry13=bibtex_KeywordField(), bibtex_Entry16=bibtex_ReviewField()) == None

def test_bibtex_Entry_getFields():
    assert bibtex_Entry.getFields(bibtex_Entry(bibtex_Entry77=bibtex_Bibliography(), bibtex_Entry=bibtex_BibtexKeyField(), bibtex_Entry9=bibtex_AbstractField(), bibtex_Entry11=bibtex_UrlField(), bibtex_Entry13=bibtex_KeywordField(), bibtex_Entry16=bibtex_ReviewField())) == None

def test_bibtex_Entry_getGeneralFields():
    assert bibtex_Entry.getGeneralFields(bibtex_Entry(bibtex_Entry77=bibtex_Bibliography(), bibtex_Entry=bibtex_BibtexKeyField(), bibtex_Entry9=bibtex_AbstractField(), bibtex_Entry11=bibtex_UrlField(), bibtex_Entry13=bibtex_KeywordField(), bibtex_Entry16=bibtex_ReviewField())) == None


from python_code import bibtex_AddressField
from python_code import bibtex_AuthorField
from python_code import bibtex_BookTitleField
from python_code import bibtex_EditorField
from python_code import bibtex_InProceedingsEntry
from python_code import bibtex_MonthField
from python_code import bibtex_NoteField
from python_code import bibtex_NumberField
from python_code import bibtex_OrganizationField
from python_code import bibtex_PageField
from python_code import bibtex_PublisherField
from python_code import bibtex_SeriesField
from python_code import bibtex_TitleField
from python_code import bibtex_VolumeField
from python_code import bibtex_YearField

def test_bibtex_InProceedingsEntry___init__():
    assert bibtex_InProceedingsEntry.__init__(bibtex_InProceedingsEntry(bibtex_InProceedingsEntry22=bibtex_BookTitleField(), bibtex_InProceedingsEntry24=bibtex_YearField(), bibtex_InProceedingsEntry26=bibtex_EditorField(), bibtex_InProceedingsEntry=bibtex_AuthorField(), bibtex_InProceedingsEntry20=bibtex_TitleField(), bibtex_InProceedingsEntry29=bibtex_PageField(), bibtex_InProceedingsEntry32=bibtex_VolumeField(), bibtex_InProceedingsEntry34=bibtex_NumberField(), bibtex_InProceedingsEntry36=bibtex_SeriesField(), bibtex_InProceedingsEntry38=bibtex_AddressField(), bibtex_InProceedingsEntry40=bibtex_MonthField(), bibtex_InProceedingsEntry42=bibtex_OrganizationField(), bibtex_InProceedingsEntry44=bibtex_NoteField(), bibtex_InProceedingsEntry46=bibtex_PublisherField()), bibtex_InProceedingsEntry22=bibtex_BookTitleField(), bibtex_InProceedingsEntry24=bibtex_YearField(), bibtex_InProceedingsEntry26=bibtex_EditorField(), bibtex_InProceedingsEntry=bibtex_AuthorField(), bibtex_InProceedingsEntry20=bibtex_TitleField(), bibtex_InProceedingsEntry29=bibtex_PageField(), bibtex_InProceedingsEntry32=bibtex_VolumeField(), bibtex_InProceedingsEntry34=bibtex_NumberField(), bibtex_InProceedingsEntry36=bibtex_SeriesField(), bibtex_InProceedingsEntry38=bibtex_AddressField(), bibtex_InProceedingsEntry40=bibtex_MonthField(), bibtex_InProceedingsEntry42=bibtex_OrganizationField(), bibtex_InProceedingsEntry44=bibtex_NoteField(), bibtex_InProceedingsEntry46=bibtex_PublisherField()) == None

def test_bibtex_InProceedingsEntry_getFields():
    assert bibtex_InProceedingsEntry.getFields(bibtex_InProceedingsEntry(bibtex_InProceedingsEntry22=bibtex_BookTitleField(), bibtex_InProceedingsEntry24=bibtex_YearField(), bibtex_InProceedingsEntry26=bibtex_EditorField(), bibtex_InProceedingsEntry=bibtex_AuthorField(), bibtex_InProceedingsEntry20=bibtex_TitleField(), bibtex_InProceedingsEntry29=bibtex_PageField(), bibtex_InProceedingsEntry32=bibtex_VolumeField(), bibtex_InProceedingsEntry34=bibtex_NumberField(), bibtex_InProceedingsEntry36=bibtex_SeriesField(), bibtex_InProceedingsEntry38=bibtex_AddressField(), bibtex_InProceedingsEntry40=bibtex_MonthField(), bibtex_InProceedingsEntry42=bibtex_OrganizationField(), bibtex_InProceedingsEntry44=bibtex_NoteField(), bibtex_InProceedingsEntry46=bibtex_PublisherField())) == None


from python_code import bibtex_IntValue

def test_bibtex_IntValue___init__():
    assert bibtex_IntValue.__init__(bibtex_IntValue(0), 0) == None


from python_code import bibtex_Person

def test_bibtex_Person___init__():
    assert bibtex_Person.__init__(bibtex_Person('', '', '\x00\x00'), '', '', '') == None


from python_code import bibtex_StringValue

def test_bibtex_StringValue___init__():
    assert bibtex_StringValue.__init__(bibtex_StringValue(''), '') == None


from python_code import bibtex_YearValue

def test_bibtex_YearValue___init__():
    assert bibtex_YearValue.__init__(bibtex_YearValue(0), 0) == None

