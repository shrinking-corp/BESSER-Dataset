from python_code import HTML_A

def test_HTML_A___init__():
    assert HTML_A.__init__(HTML_A('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML_APPLET

def test_HTML_APPLET___init__():
    assert HTML_APPLET.__init__(HTML_APPLET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import HTML_AREA

def test_HTML_AREA___init__():
    assert HTML_AREA.__init__(HTML_AREA('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML_BODY
from python_code import HTML_BODYElement
from python_code import HTML_HTML

def test_HTML_BODY___init__():
    assert HTML_BODY.__init__(HTML_BODY('', '', '\x00', '', '', '', BODY=HTML_HTML(), body=set(), body15=HTML_HTML(), BODY18=HTML_BODYElement()), '', '', '', '', '', '', BODY=HTML_HTML(), body=set(), body15=HTML_HTML(), BODY18=HTML_BODYElement()) == None


from python_code import HTML_BR

def test_HTML_BR___init__():
    assert HTML_BR.__init__(HTML_BR(''), '') == None


from python_code import HTML_DIV

def test_HTML_DIV___init__():
    assert HTML_DIV.__init__(HTML_DIV(''), '') == None


from python_code import HTML_EMBED

def test_HTML_EMBED___init__():
    assert HTML_EMBED.__init__(HTML_EMBED('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import HTML_FONT

def test_HTML_FONT___init__():
    assert HTML_FONT.__init__(HTML_FONT('', '', '\x00\x00'), '', '', '') == None


from python_code import HTML_FORM

def test_HTML_FORM___init__():
    assert HTML_FORM.__init__(HTML_FORM('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_FRAME

def test_HTML_FRAME___init__():
    assert HTML_FRAME.__init__(HTML_FRAME('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import HTML_FRAMESET

def test_HTML_FRAMESET___init__():
    assert HTML_FRAMESET.__init__(HTML_FRAMESET('', '', '', '', ''), '', '', '', '', '') == None


from python_code import HTML_IMG

def test_HTML_IMG___init__():
    assert HTML_IMG.__init__(HTML_IMG('', '', '\x00', '', '', '', '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '') == None


from python_code import HTML_INPUT

def test_HTML_INPUT___init__():
    assert HTML_INPUT.__init__(HTML_INPUT('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import HTML_LI

def test_HTML_LI___init__():
    assert HTML_LI.__init__(HTML_LI(''), '') == None


from python_code import HTML_LINK

def test_HTML_LINK___init__():
    assert HTML_LINK.__init__(HTML_LINK('\x00\x00', '', '', ''), '', '', '', '') == None


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


from python_code import HTML_SPAN

def test_HTML_SPAN___init__():
    assert HTML_SPAN.__init__(HTML_SPAN(''), '') == None


from python_code import HTML_TABLEElement

def test_HTML_TABLEElement___init__():
    assert HTML_TABLEElement.__init__(HTML_TABLEElement('', '\x00'), '\x00\x00', '') == None


from python_code import HTML_TEXTAREA

def test_HTML_TEXTAREA___init__():
    assert HTML_TEXTAREA.__init__(HTML_TEXTAREA('', '', '\x00\x00'), '', '', '') == None

