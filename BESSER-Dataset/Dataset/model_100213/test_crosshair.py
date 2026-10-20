from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_A
from python_code import HTML_BODY
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement

def test_HTML_A___init__():
    assert HTML_A.__init__(HTML_A('', '', '', BODYElement=HTML_BODY('\x00', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_HEAD()))), '', '', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_APPLET

def test_HTML_APPLET___init__():
    assert HTML_APPLET.__init__(HTML_APPLET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_AREA
from python_code import HTML_BODY
from python_code import HTML_HTMLElement

def test_HTML_AREA___init__():
    assert HTML_AREA.__init__(HTML_AREA('\x00', '', '', BODYElement=HTML_BODY('', '', '\x00', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', '', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement

def test_HTML_BODY___init__():
    assert HTML_BODY.__init__(HTML_BODY('', '', '\x00', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_HEAD())), '', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement())) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_BR
from python_code import HTML_HTMLElement

def test_HTML_BR___init__():
    assert HTML_BR.__init__(HTML_BR('\x00', BODYElement=HTML_BODY('', '', '', '', '\x00', '\x00', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()))), '', BODYElement=HTML_BODY('\x01', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_EMBED
from python_code import HTML_HTMLElement

def test_HTML_EMBED___init__():
    assert HTML_EMBED.__init__(HTML_EMBED('', '', '\x00', '', '', '', '', BODYElement=HTML_BODY('', '', '', '', '\x00', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', '', '', '', '', '', '', BODYElement=HTML_BODY('\x00', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_FONT
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement

def test_HTML_FONT___init__():
    assert HTML_FONT.__init__(HTML_FONT('', '', '', BODYElement=HTML_BODY('\x00', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_HEAD()))), '', '', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_FORM

def test_HTML_FORM___init__():
    assert HTML_FORM.__init__(HTML_FORM('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_FRAME

def test_HTML_FRAME___init__():
    assert HTML_FRAME.__init__(HTML_FRAME('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import HTML_FRAMESET

def test_HTML_FRAMESET___init__():
    assert HTML_FRAMESET.__init__(HTML_FRAMESET('', '', '', '', ''), '', '', '', '', '') == None


from python_code import HTMLElement
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement

def test_HTML_HTMLElement___init__():
    assert HTML_HTMLElement.__init__(HTML_HTMLElement('', parent=set(), children=HTML_HEAD()), '', parent=set(), children=HTMLElement()) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_BODYElement
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement
from python_code import HTML_IMG

def test_HTML_IMG___init__():
    assert HTML_IMG.__init__(HTML_IMG('', '', '', '', '', '', '', '', '', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_BODYElement()))), '', '', '', '', '', '', '', '', '', '', BODYElement=HTML_BODY('', '\x01', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTML_HEAD()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_INPUT

def test_HTML_INPUT___init__():
    assert HTML_INPUT.__init__(HTML_INPUT('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import HTML_LI

def test_HTML_LI___init__():
    assert HTML_LI.__init__(HTML_LI(''), '') == None


from python_code import HTML_HEAD
from python_code import HTML_LINK

def test_HTML_LINK___init__():
    assert HTML_LINK.__init__(HTML_LINK('\x00\x00', '', '', '', HEADElement=HTML_HEAD()), '', '', '', '', HEADElement=HTML_HEAD()) == None


from python_code import HTML_ListElement

def test_HTML_ListElement___init__():
    assert HTML_ListElement.__init__(HTML_ListElement(''), '') == None


from python_code import HTML_OBJECT

def test_HTML_OBJECT___init__():
    assert HTML_OBJECT.__init__(HTML_OBJECT('', '', '', '', ''), '', '', '', '', '') == None


from python_code import HTML_OL

def test_HTML_OL___init__():
    assert HTML_OL.__init__(HTML_OL(''), '') == None


from python_code import HTML_OPTION

def test_HTML_OPTION___init__():
    assert HTML_OPTION.__init__(HTML_OPTION('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_PARAM

def test_HTML_PARAM___init__():
    assert HTML_PARAM.__init__(HTML_PARAM('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_SELECT

def test_HTML_SELECT___init__():
    assert HTML_SELECT.__init__(HTML_SELECT('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_HTMLElement
from python_code import HTML_SPAN

def test_HTML_SPAN___init__():
    assert HTML_SPAN.__init__(HTML_SPAN('', BODYElement=HTML_BODY('\x01', '\x00', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', BODYElement=HTML_BODY('', '', '\x00', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_TABLE

def test_HTML_TABLE___init__():
    assert HTML_TABLE.__init__(HTML_TABLE('', '', '', '', table=set()), '', '', '', '', table=set()) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BODY
from python_code import HTML_HTMLElement
from python_code import HTML_TABLEElement

def test_HTML_TABLEElement___init__():
    assert HTML_TABLEElement.__init__(HTML_TABLEElement('', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', '', BODYElement=HTML_BODY('', '', '', '', '', '', body=set(), body13=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_TD
from python_code import TR

def test_HTML_TD___init__():
    assert HTML_TD.__init__(HTML_TD('', '', '', '', '', tds=TR()), '', '', '', '', '', tds=TR()) == None


from python_code import HTML_TEXTAREA

def test_HTML_TEXTAREA___init__():
    assert HTML_TEXTAREA.__init__(HTML_TEXTAREA('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML_TR
from python_code import TABLE

def test_HTML_TR___init__():
    assert HTML_TR.__init__(HTML_TR('\x00\x00', '', trs=TABLE(), tr=set()), '', '', trs=TABLE(), tr=set()) == None

