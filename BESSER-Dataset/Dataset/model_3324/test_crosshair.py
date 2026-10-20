from python_code import Java_Annotation

def test_Java_Annotation___init__():
    assert Java_Annotation.__init__(Java_Annotation('', '\x00'), '\x00\x00', '') == None


from python_code import Java_Assignment
from python_code import Java_Method

def test_Java_Assignment___init__():
    assert Java_Assignment.__init__(Java_Assignment('', '', '\x00\x00', Statement=Java_Method()), '', '', '', Statement=Java_Method()) == None


from python_code import Class
from python_code import Java_Class
from python_code import Java_Package

def test_Java_Class___init__():
    assert Java_Class.__init__(Java_Class(False, False, Java_Class4=Class(), owner6=set(), Java_Class8=set(), Java_Class=set(), ObjectType=Java_Package('', owner=set())), False, False, Java_Class4=Class(), owner6=set(), Java_Class8=set(), Java_Class=set(), ObjectType=Java_Package('', owner=set())) == None


from python_code import Class
from python_code import Java_Field
from python_code import Type

def test_Java_Field___init__():
    assert Java_Field.__init__(Java_Field('', False, False, True, False, Java_Field=Type(), field=Class()), '', True, False, False, False, Java_Field=Type(), field=Class()) == None


from python_code import Java_Method
from python_code import Java_MethodCall

def test_Java_MethodCall___init__():
    assert Java_MethodCall.__init__(Java_MethodCall('', '\x00', Statement=Java_Method()), '\x00\x00', '', Statement=Java_Method()) == None


from python_code import Java_MethodSignature
from python_code import Type

def test_Java_MethodSignature___init__():
    assert Java_MethodSignature.__init__(Java_MethodSignature('', False, False, False, False, Java_MethodSignature=Type(), Java_MethodSignature15=set()), '', False, False, False, True, Java_MethodSignature=Type(), Java_MethodSignature15=set()) == None


from python_code import Java_Package

def test_Java_Package___init__():
    assert Java_Package.__init__(Java_Package('', owner=set()), '', owner=set()) == None


from python_code import Java_Parameter
from python_code import Type

def test_Java_Parameter___init__():
    assert Java_Parameter.__init__(Java_Parameter('', '', Java_Parameter=Type()), '', '', Java_Parameter=Type()) == None


from python_code import Java_Method
from python_code import Java_Return

def test_Java_Return___init__():
    assert Java_Return.__init__(Java_Return('', '\x00', Statement=Java_Method()), '\x00\x00', '', Statement=Java_Method()) == None


from python_code import Java_Type

def test_Java_Type___init__():
    assert Java_Type.__init__(Java_Type(''), '') == None


from python_code import Java_Method
from python_code import Java_VariableDeclaration
from python_code import Type

def test_Java_VariableDeclaration___init__():
    assert Java_VariableDeclaration.__init__(Java_VariableDeclaration('', Java_VariableDeclaration=Type(), Statement=Java_Method()), '', Java_VariableDeclaration=Type(), Statement=Java_Method()) == None

