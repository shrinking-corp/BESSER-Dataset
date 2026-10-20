from python_code import TypeA_AA

def test_TypeA_AA___init__():
    assert TypeA_AA.__init__(TypeA_AA(''), '') == None


from python_code import TypeA_C

def test_TypeA_C___init__():
    assert TypeA_C.__init__(TypeA_C(''), '') == None


from python_code import AA
from python_code import TypeA_ListElement

def test_TypeA_ListElement___init__():
    assert TypeA_ListElement.__init__(TypeA_ListElement('', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set()), '', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set()) == None


from python_code import TypeA_ObjectR

def test_TypeA_ObjectR___init__():
    assert TypeA_ObjectR.__init__(TypeA_ObjectR(''), '') == None


from python_code import AA
from python_code import TypeA_ListElement
from python_code import TypeA_ObjectS

def test_TypeA_ObjectS___init__():
    assert TypeA_ObjectS.__init__(TypeA_ObjectS('', ObjectR=TypeA_ListElement('', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set())), '', ObjectR=TypeA_ListElement('', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set())) == None


from python_code import TypeA_ObjectX

def test_TypeA_ObjectX___init__():
    assert TypeA_ObjectX.__init__(TypeA_ObjectX(''), '') == None


from python_code import AA
from python_code import TypeA_ListElement
from python_code import TypeA_ObjectY

def test_TypeA_ObjectY___init__():
    assert TypeA_ObjectY.__init__(TypeA_ObjectY('', ObjectX=TypeA_ListElement('', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set())), '', ObjectX=TypeA_ListElement('', TypeA_ListElement=set(), TypeA_ListElement2=AA(), TypeA_ListElement5=set(), TypeA_ListElement7=set())) == None

