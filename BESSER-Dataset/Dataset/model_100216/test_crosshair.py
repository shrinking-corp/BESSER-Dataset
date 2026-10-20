from python_code import html_A

def test_html_A___init__():
    assert html_A.__init__(html_A('', '', '\x00\x00'), '', '', '') == None


from python_code import html_APPLET

def test_html_APPLET___init__():
    assert html_APPLET.__init__(html_APPLET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import html_AREA

def test_html_AREA___init__():
    assert html_AREA.__init__(html_AREA('', '', '\x00\x00'), '', '', '') == None


from python_code import html_BODY
from python_code import html_BODYElement
from python_code import html_HTML

def test_html_BODY___init__():
    assert html_BODY.__init__(html_BODY('', '', '\x00', '', '', '', BODY=html_HTML(), BODY18=html_BODYElement(), body=set(), body15=html_HTML()), '', '', '', '', '', '', BODY=html_HTML(), BODY18=html_BODYElement(), body=set(), body15=html_HTML()) == None


from python_code import html_BR

def test_html_BR___init__():
    assert html_BR.__init__(html_BR(''), '') == None


from python_code import html_DIV

def test_html_DIV___init__():
    assert html_DIV.__init__(html_DIV(''), '') == None


from python_code import html_EMBED

def test_html_EMBED___init__():
    assert html_EMBED.__init__(html_EMBED('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import html_FONT

def test_html_FONT___init__():
    assert html_FONT.__init__(html_FONT('', '', '\x00\x00'), '', '', '') == None


from python_code import html_FORM

def test_html_FORM___init__():
    assert html_FORM.__init__(html_FORM('', '\x00'), '\x00\x00', '') == None


from python_code import html_FRAME

def test_html_FRAME___init__():
    assert html_FRAME.__init__(html_FRAME('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import html_FRAMESET

def test_html_FRAMESET___init__():
    assert html_FRAMESET.__init__(html_FRAMESET('', '', '', '', ''), '', '', '', '', '') == None


from python_code import html_IMG

def test_html_IMG___init__():
    assert html_IMG.__init__(html_IMG('', '', '\x00', '', '', '', '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '') == None


from python_code import html_INPUT

def test_html_INPUT___init__():
    assert html_INPUT.__init__(html_INPUT('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import html_LI

def test_html_LI___init__():
    assert html_LI.__init__(html_LI(''), '') == None


from python_code import html_LINK

def test_html_LINK___init__():
    assert html_LINK.__init__(html_LINK('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import html_ListElement

def test_html_ListElement___init__():
    assert html_ListElement.__init__(html_ListElement(''), '') == None


from python_code import html_OBJECT

def test_html_OBJECT___init__():
    assert html_OBJECT.__init__(html_OBJECT('', '', '', '', ''), '', '', '', '', '') == None


from python_code import html_OL

def test_html_OL___init__():
    assert html_OL.__init__(html_OL(''), '') == None


from python_code import html_OPTION

def test_html_OPTION___init__():
    assert html_OPTION.__init__(html_OPTION('', '\x00'), '\x00\x00', '') == None


from python_code import html_PARAM

def test_html_PARAM___init__():
    assert html_PARAM.__init__(html_PARAM('', '\x00'), '\x00\x00', '') == None


from python_code import html_SELECT

def test_html_SELECT___init__():
    assert html_SELECT.__init__(html_SELECT('', '', '\x00\x00'), '', '', '') == None


from python_code import html_SPAN

def test_html_SPAN___init__():
    assert html_SPAN.__init__(html_SPAN(''), '') == None


from python_code import html_TABLEElement

def test_html_TABLEElement___init__():
    assert html_TABLEElement.__init__(html_TABLEElement('', '\x00'), '\x00\x00', '') == None


from python_code import html_TEXTAREA

def test_html_TEXTAREA___init__():
    assert html_TEXTAREA.__init__(html_TEXTAREA('', '', '\x00\x00'), '', '', '') == None

