from python_code import FPath_FunctionCallExp

def test_FPath_FunctionCallExp___init__():
    assert FPath_FunctionCallExp.__init__(FPath_FunctionCallExp('', FPath_FunctionCallExp=set()), '', FPath_FunctionCallExp=set()) == None


from python_code import FPath_LocatedElement

def test_FPath_LocatedElement___init__():
    assert FPath_LocatedElement.__init__(FPath_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import FPath_NameTest

def test_FPath_NameTest___init__():
    assert FPath_NameTest.__init__(FPath_NameTest(''), '') == None


from python_code import FPath_NumberExp

def test_FPath_NumberExp___init__():
    assert FPath_NumberExp.__init__(FPath_NumberExp(''), '') == None


from python_code import FPath_OperatorExp

def test_FPath_OperatorExp___init__():
    assert FPath_OperatorExp.__init__(FPath_OperatorExp(''), '') == None


from python_code import FPath_PathExp
from python_code import FPath_Step
from python_code import FPath_Test

def test_FPath_Step___init__():
    assert FPath_Step.__init__(FPath_Step('', FPath_Step=FPath_PathExp(), FPath_Step13=FPath_Test(), FPath_Step15=set()), '', FPath_Step=FPath_PathExp(), FPath_Step13=FPath_Test(), FPath_Step15=set()) == None


from python_code import FPath_StringExp

def test_FPath_StringExp___init__():
    assert FPath_StringExp.__init__(FPath_StringExp(''), '') == None


from python_code import FPath_VariableExp

def test_FPath_VariableExp___init__():
    assert FPath_VariableExp.__init__(FPath_VariableExp(''), '') == None

