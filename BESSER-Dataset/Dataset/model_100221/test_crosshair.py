from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_A
from python_code import HTML_BBODY
from python_code import HTML_BODYElement
from python_code import HTML_HTMLElement

def test_HTML_A___init__():
    assert HTML_A.__init__(HTML_A('', '', '', BODYElement=HTML_BBODY('\x00', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_BODYElement()))), '', '', '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement

def test_HTML_BBODY___init__():
    assert HTML_BBODY.__init__(HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_HEAD())), '', '', '', '\x00', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement())) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_BR
from python_code import HTML_HTMLElement

def test_HTML_BR___init__():
    assert HTML_BR.__init__(HTML_BR('\x00', BODYElement=HTML_BBODY('', '', '', '', '\x00', '\x00', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()))), '', BODYElement=HTML_BBODY('\x01', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_DIV
from python_code import HTML_HEADElement
from python_code import HTML_HTMLElement

def test_HTML_DIV___init__():
    assert HTML_DIV.__init__(HTML_DIV('\x00', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTML_HEADElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTMLElement
from python_code import HTML_BODYElement
from python_code import HTML_HTMLElement

def test_HTML_HTMLElement___init__():
    assert HTML_HTMLElement.__init__(HTML_HTMLElement('', parent=set(), children=HTMLElement()), '', parent=set(), children=HTML_BODYElement()) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_HEAD
from python_code import HTML_HTMLElement
from python_code import HTML_IMG

def test_HTML_IMG___init__():
    assert HTML_IMG.__init__(HTML_IMG('', '', '', '', '', '', '', '', '', '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTML_HEAD()))), '', '', '', '', '', '', '', '', '', '', BODYElement=HTML_BBODY('', '', '', '', '', '\x00', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


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


from python_code import HTML_OL

def test_HTML_OL___init__():
    assert HTML_OL.__init__(HTML_OL(''), '') == None


from python_code import HTML_OPTION

def test_HTML_OPTION___init__():
    assert HTML_OPTION.__init__(HTML_OPTION('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_SELECT

def test_HTML_SELECT___init__():
    assert HTML_SELECT.__init__(HTML_SELECT('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_BODYElement
from python_code import HTML_HTMLElement
from python_code import HTML_SPAN

def test_HTML_SPAN___init__():
    assert HTML_SPAN.__init__(HTML_SPAN('', BODYElement=HTML_BBODY('', '', '', '', '\x00', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTML_BODYElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_TABLE

def test_HTML_TABLE___init__():
    assert HTML_TABLE.__init__(HTML_TABLE('', '', '', '', table=set()), '', '', '', '', table=set()) == None


from python_code import HTML
from python_code import HTMLElement
from python_code import HTML_BBODY
from python_code import HTML_HTMLElement
from python_code import HTML_TABLEElement

def test_HTML_TABLEElement___init__():
    assert HTML_TABLEElement.__init__(HTML_TABLEElement('', '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('\x00', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))), '', '', BODYElement=HTML_BBODY('', '', '', '', '', '', body=set(), bbody=HTML(), HTMLElement=HTML_HTMLElement('', parent=set(), children=HTMLElement()), HTMLElement5=HTML_HTMLElement('', parent=set(), children=HTMLElement()))) == None


from python_code import HTML_TD
from python_code import TR

def test_HTML_TD___init__():
    assert HTML_TD.__init__(HTML_TD('', '', '', '', '', tds=TR()), '', '', '', '', '', tds=TR()) == None


from python_code import HTML_TR
from python_code import TABLE

def test_HTML_TR___init__():
    assert HTML_TR.__init__(HTML_TR('\x00\x00', '', trs=TABLE(), tr=set()), '', '', trs=TABLE(), tr=set()) == None

