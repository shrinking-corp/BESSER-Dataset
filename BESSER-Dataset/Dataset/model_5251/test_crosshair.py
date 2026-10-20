from python_code import HTML
from python_code import HTMLElement
from python_code import Html_A
from python_code import Html_BODY
from python_code import Html_HEADElement
from python_code import Html_HTMLElement

def test_Html_A___init__():
    assert Html_A.__init__(Html_A('', '', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '\x00', '\x00', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '\x00', '', '', parent=set(), children=HTMLElement()))), '', '', BODYElement=Html_BODY('', '', '', '', '', '\x00', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '\x00', '', parent=set(), children=Html_HEADElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))) == None


from python_code import Html_APPLET

def test_Html_APPLET___init__():
    assert Html_APPLET.__init__(Html_APPLET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_BODYElement
from python_code import Html_HTMLElement

def test_Html_BODY___init__():
    assert Html_BODY.__init__(Html_BODY('', '', '', '', '', '\x00', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement())), '', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=Html_BODYElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement())) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_BR
from python_code import Html_HTMLElement

def test_Html_BR___init__():
    assert Html_BR.__init__(Html_BR('', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))), '', BODYElement=Html_BODY('', '', '', '', '\x00', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_DIV
from python_code import Html_HTMLElement

def test_Html_DIV___init__():
    assert Html_DIV.__init__(Html_DIV('', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))), '', BODYElement=Html_BODY('', '', '', '', '\x00', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_EMBED
from python_code import Html_HEAD
from python_code import Html_HEADElement
from python_code import Html_HTMLElement

def test_Html_EMBED___init__():
    assert Html_EMBED.__init__(Html_EMBED('', '', '', '', '', '', '', BODYElement=Html_BODY('', '\x00', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=Html_HEAD()))), '', '', '', '', '', '', '', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=Html_HEADElement()))) == None


from python_code import Html_FORM

def test_Html_FORM___init__():
    assert Html_FORM.__init__(Html_FORM('', '\x00'), '\x00\x00', '') == None


from python_code import Html_FRAME

def test_Html_FRAME___init__():
    assert Html_FRAME.__init__(Html_FRAME('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import Html_FRAMESET

def test_Html_FRAMESET___init__():
    assert Html_FRAMESET.__init__(Html_FRAMESET('', '', '', '', ''), '', '', '', '', '') == None


from python_code import HTMLElement
from python_code import Html_HEAD
from python_code import Html_HTMLElement

def test_Html_HTMLElement___init__():
    assert Html_HTMLElement.__init__(Html_HTMLElement('', '', '', '', parent=set(), children=Html_HEAD()), '', '', '', '', parent=set(), children=HTMLElement()) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_BODYElement
from python_code import Html_HTMLElement
from python_code import Html_IMG

def test_Html_IMG___init__():
    assert Html_IMG.__init__(Html_IMG('', '', '', '', '', '', '', '', '', '', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=Html_BODYElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))), '', '', '', '', '', '', '', '\x00', '', '', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))) == None


from python_code import Html_INPUT

def test_Html_INPUT___init__():
    assert Html_INPUT.__init__(Html_INPUT('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import Html_LI

def test_Html_LI___init__():
    assert Html_LI.__init__(Html_LI(''), '') == None


from python_code import Html_HEAD
from python_code import Html_LINK

def test_Html_LINK___init__():
    assert Html_LINK.__init__(Html_LINK('', '', '\x00\x00', HEADElement=Html_HEAD()), '', '', '', HEADElement=Html_HEAD()) == None


from python_code import Html_ListElement

def test_Html_ListElement___init__():
    assert Html_ListElement.__init__(Html_ListElement(''), '') == None


from python_code import Html_OBJECT

def test_Html_OBJECT___init__():
    assert Html_OBJECT.__init__(Html_OBJECT('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import Html_OL

def test_Html_OL___init__():
    assert Html_OL.__init__(Html_OL(''), '') == None


from python_code import Html_OPTION

def test_Html_OPTION___init__():
    assert Html_OPTION.__init__(Html_OPTION('', '\x00'), '\x00\x00', '') == None


from python_code import Html_PARAM

def test_Html_PARAM___init__():
    assert Html_PARAM.__init__(Html_PARAM('', '\x00'), '\x00\x00', '') == None


from python_code import Html_SELECT

def test_Html_SELECT___init__():
    assert Html_SELECT.__init__(Html_SELECT('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML
from python_code import HTMLElement
from python_code import Html_BODY
from python_code import Html_HTMLElement
from python_code import Html_SPAN

def test_Html_SPAN___init__():
    assert Html_SPAN.__init__(Html_SPAN('', BODYElement=Html_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))), '', BODYElement=Html_BODY('', '', '', '', '\x00', '', body=set(), body13=HTML(), HTMLElement=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()), HTMLElement5=Html_HTMLElement('', '', '', '', parent=set(), children=HTMLElement()))) == None


from python_code import Html_TABLE

def test_Html_TABLE___init__():
    assert Html_TABLE.__init__(Html_TABLE('', '', '', '', table=set()), '', '', '', '', table=set()) == None


from python_code import Html_TD
from python_code import TR

def test_Html_TD___init__():
    assert Html_TD.__init__(Html_TD('', '', '', '', '', tds=TR()), '', '', '', '', '', tds=TR()) == None


from python_code import Html_TEXTAREA

def test_Html_TEXTAREA___init__():
    assert Html_TEXTAREA.__init__(Html_TEXTAREA('', '', '\x00\x00'), '', '', '') == None


from python_code import Html_TR
from python_code import TABLE

def test_Html_TR___init__():
    assert Html_TR.__init__(Html_TR('\x00\x00', '', trs=TABLE(), tr=set()), '', '', trs=TABLE(), tr=set()) == None

