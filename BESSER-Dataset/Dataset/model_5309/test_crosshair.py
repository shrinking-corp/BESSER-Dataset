from python_code import TypeB_AnotherElement

def test_TypeB_AnotherElement___init__():
    assert TypeB_AnotherElement.__init__(TypeB_AnotherElement('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import TypeB_Element

def test_TypeB_Element___init__():
    assert TypeB_Element.__init__(TypeB_Element('', '', '\x00\x00'), '', '', '') == None


from python_code import TypeB_ElementR

def test_TypeB_ElementR___init__():
    assert TypeB_ElementR.__init__(TypeB_ElementR(''), '') == None


from python_code import Element
from python_code import TypeB_ElementS
from python_code import TypeB_ListElement

def test_TypeB_ElementS___init__():
    assert TypeB_ElementS.__init__(TypeB_ElementS('', ElementR=TypeB_ListElement('', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set())), '', ElementR=TypeB_ListElement('', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set())) == None


from python_code import TypeB_ElementX

def test_TypeB_ElementX___init__():
    assert TypeB_ElementX.__init__(TypeB_ElementX(''), '') == None


from python_code import Element
from python_code import TypeB_ElementY
from python_code import TypeB_ListElement

def test_TypeB_ElementY___init__():
    assert TypeB_ElementY.__init__(TypeB_ElementY('', ElementX=TypeB_ListElement('', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set())), '', ElementX=TypeB_ListElement('', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set())) == None


from python_code import Element
from python_code import TypeB_ListElement

def test_TypeB_ListElement___init__():
    assert TypeB_ListElement.__init__(TypeB_ListElement('', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set()), '', TypeB_ListElement=set(), TypeB_ListElement2=Element(), TypeB_ListElement5=set(), TypeB_ListElement7=set()) == None

