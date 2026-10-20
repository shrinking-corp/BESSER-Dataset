from python_code import miniJava_BoolConstant

def test_miniJava_BoolConstant___init__():
    assert miniJava_BoolConstant.__init__(miniJava_BoolConstant(''), '') == None


from python_code import miniJava_IntConstant

def test_miniJava_IntConstant___init__():
    assert miniJava_IntConstant.__init__(miniJava_IntConstant(0), 0) == None


from python_code import miniJava_Block
from python_code import miniJava_Method
from python_code import miniJava_MethodCall

def test_miniJava_Method___init__():
    assert miniJava_Method.__init__(miniJava_Method(False, False, miniJava_Method=set(), miniJava_Method11=miniJava_Block(), miniJava_Method131=miniJava_MethodCall()), False, False, miniJava_Method=set(), miniJava_Method11=miniJava_Block(), miniJava_Method131=miniJava_MethodCall()) == None


from python_code import miniJava_NamedElement

def test_miniJava_NamedElement___init__():
    assert miniJava_NamedElement.__init__(miniJava_NamedElement(''), '') == None


from python_code import miniJava_Program

def test_miniJava_Program___init__():
    assert miniJava_Program.__init__(miniJava_Program('', miniJava_Program=set(), miniJava_Program2=set()), '', miniJava_Program=set(), miniJava_Program2=set()) == None


from python_code import miniJava_StringConstant

def test_miniJava_StringConstant___init__():
    assert miniJava_StringConstant.__init__(miniJava_StringConstant(''), '') == None

