from python_code import wikiML_External

def test_wikiML_External___init__():
    assert wikiML_External.__init__(wikiML_External(''), '') == None


from python_code import wikiML_AbstractUnformattedInlineContent
from python_code import wikiML_AnyTextSequence
from python_code import wikiML_Image

def test_wikiML_Image___init__():
    assert wikiML_Image.__init__(wikiML_Image('', '', '\x00\x00', wikiML_Image=wikiML_AbstractUnformattedInlineContent(), wikiML_Image21=wikiML_AnyTextSequence()), '', '', '', wikiML_Image=wikiML_AbstractUnformattedInlineContent(), wikiML_Image21=wikiML_AnyTextSequence()) == None


from python_code import wikiML_OrderedList
from python_code import wikiML_Paragraph
from python_code import wikiML_UnorderedList

def test_wikiML_Paragraph___init__():
    assert wikiML_Paragraph.__init__(wikiML_Paragraph('', wikiML_Paragraph=wikiML_OrderedList(), wikiML_Paragraph12=wikiML_UnorderedList()), '', wikiML_Paragraph=wikiML_OrderedList(), wikiML_Paragraph12=wikiML_UnorderedList()) == None


from python_code import wikiML_Template

def test_wikiML_Template___init__():
    assert wikiML_Template.__init__(wikiML_Template(''), '') == None


from python_code import wikiML_AnyTextSequence
from python_code import wikiML_UnorderListItem
from python_code import wikiML_UnorderedList

def test_wikiML_UnorderListItem___init__():
    assert wikiML_UnorderListItem.__init__(wikiML_UnorderListItem('', wikiML_UnorderListItem=wikiML_UnorderedList(), wikiML_UnorderListItem14=wikiML_AnyTextSequence()), '', wikiML_UnorderListItem=wikiML_UnorderedList(), wikiML_UnorderListItem14=wikiML_AnyTextSequence()) == None


from python_code import wikiML_Internal
from python_code import wikiML_WikiPage

def test_wikiML_WikiPage___init__():
    assert wikiML_WikiPage.__init__(wikiML_WikiPage('', wikiML_WikiPage=set(), wikiML_WikiPage36=wikiML_Internal()), '', wikiML_WikiPage=set(), wikiML_WikiPage36=wikiML_Internal()) == None

