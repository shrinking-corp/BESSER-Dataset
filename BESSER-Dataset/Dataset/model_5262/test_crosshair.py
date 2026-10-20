from python_code import defaultname_A

def test_defaultname_A___init__():
    assert defaultname_A.__init__(defaultname_A('', '', '\x00\x00'), '', '', '') == None


from python_code import defaultname_APPLET

def test_defaultname_APPLET___init__():
    assert defaultname_APPLET.__init__(defaultname_APPLET('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import defaultname_AREA

def test_defaultname_AREA___init__():
    assert defaultname_AREA.__init__(defaultname_AREA('', '', '\x00\x00'), '', '', '') == None


from python_code import defaultname_BODY
from python_code import defaultname_BODYElement
from python_code import defaultname_HTML

def test_defaultname_BODY___init__():
    assert defaultname_BODY.__init__(defaultname_BODY('', '', '\x00', '', '', '', BODY=defaultname_HTML(), body=set(), BODY18=defaultname_BODYElement(), body15=defaultname_HTML()), '', '', '', '', '', '', BODY=defaultname_HTML(), body=set(), BODY18=defaultname_BODYElement(), body15=defaultname_HTML()) == None


from python_code import defaultname_BR

def test_defaultname_BR___init__():
    assert defaultname_BR.__init__(defaultname_BR(''), '') == None


from python_code import defaultname_DIV

def test_defaultname_DIV___init__():
    assert defaultname_DIV.__init__(defaultname_DIV(''), '') == None


from python_code import defaultname_EMBED

def test_defaultname_EMBED___init__():
    assert defaultname_EMBED.__init__(defaultname_EMBED('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import defaultname_FONT

def test_defaultname_FONT___init__():
    assert defaultname_FONT.__init__(defaultname_FONT('', '', '\x00\x00'), '', '', '') == None


from python_code import defaultname_FORM

def test_defaultname_FORM___init__():
    assert defaultname_FORM.__init__(defaultname_FORM('', '\x00'), '\x00\x00', '') == None


from python_code import defaultname_FRAME

def test_defaultname_FRAME___init__():
    assert defaultname_FRAME.__init__(defaultname_FRAME('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import defaultname_FRAMESET

def test_defaultname_FRAMESET___init__():
    assert defaultname_FRAMESET.__init__(defaultname_FRAMESET('', '', '', '', ''), '', '', '', '', '') == None


from python_code import defaultname_IMG

def test_defaultname_IMG___init__():
    assert defaultname_IMG.__init__(defaultname_IMG('', '', '\x00', '', '', '', '', '', '', ''), '', '', '\x00', '', '', '', '', '', '', '') == None


from python_code import defaultname_INPUT

def test_defaultname_INPUT___init__():
    assert defaultname_INPUT.__init__(defaultname_INPUT('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import defaultname_LI

def test_defaultname_LI___init__():
    assert defaultname_LI.__init__(defaultname_LI(''), '') == None


from python_code import defaultname_LINK

def test_defaultname_LINK___init__():
    assert defaultname_LINK.__init__(defaultname_LINK('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import defaultname_ListElement

def test_defaultname_ListElement___init__():
    assert defaultname_ListElement.__init__(defaultname_ListElement(''), '') == None


from python_code import defaultname_OBJECT

def test_defaultname_OBJECT___init__():
    assert defaultname_OBJECT.__init__(defaultname_OBJECT('', '', '', '', ''), '', '', '', '', '') == None


from python_code import defaultname_OL

def test_defaultname_OL___init__():
    assert defaultname_OL.__init__(defaultname_OL(''), '') == None


from python_code import defaultname_OPTION

def test_defaultname_OPTION___init__():
    assert defaultname_OPTION.__init__(defaultname_OPTION('', '\x00'), '\x00\x00', '') == None


from python_code import defaultname_PARAM

def test_defaultname_PARAM___init__():
    assert defaultname_PARAM.__init__(defaultname_PARAM('', '\x00'), '\x00\x00', '') == None


from python_code import defaultname_SELECT

def test_defaultname_SELECT___init__():
    assert defaultname_SELECT.__init__(defaultname_SELECT('', '', '\x00\x00'), '', '', '') == None


from python_code import defaultname_SPAN

def test_defaultname_SPAN___init__():
    assert defaultname_SPAN.__init__(defaultname_SPAN(''), '') == None


from python_code import defaultname_TABLEElement

def test_defaultname_TABLEElement___init__():
    assert defaultname_TABLEElement.__init__(defaultname_TABLEElement('', '\x00'), '\x00\x00', '') == None


from python_code import defaultname_TEXTAREA

def test_defaultname_TEXTAREA___init__():
    assert defaultname_TEXTAREA.__init__(defaultname_TEXTAREA('', '', '\x00\x00'), '', '', '') == None

