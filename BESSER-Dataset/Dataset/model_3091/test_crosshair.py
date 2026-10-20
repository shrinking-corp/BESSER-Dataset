from python_code import Class
from python_code import SimpleClass_Association

def test_SimpleClass_Association___init__():
    assert SimpleClass_Association.__init__(SimpleClass_Association('', SimpleClass_Association=Class(), SimpleClass_Association6=Class()), '', SimpleClass_Association=Class(), SimpleClass_Association6=Class()) == None


from python_code import Class
from python_code import Classifier
from python_code import SimpleClass_Attribute

def test_SimpleClass_Attribute___init__():
    assert SimpleClass_Attribute.__init__(SimpleClass_Attribute('', '', SimpleClass_Attribute=Classifier(), SimpleClass_Attribute10=Class()), '\x00', '', SimpleClass_Attribute=Classifier(), SimpleClass_Attribute10=Class()) == None


from python_code import Class
from python_code import Classifier
from python_code import SimpleClass_Attribute
from python_code import SimpleClass_Class

def test_SimpleClass_Class___init__():
    assert SimpleClass_Class.__init__(SimpleClass_Class('', SimpleClass_Class=Class(), SimpleClass_Class2=set(), Classifier=SimpleClass_Attribute('', '', SimpleClass_Attribute=Classifier(), SimpleClass_Attribute10=Class())), '', SimpleClass_Class=Class(), SimpleClass_Class2=set(), Classifier=SimpleClass_Attribute('', '', SimpleClass_Attribute=Classifier(), SimpleClass_Attribute10=Class())) == None


from python_code import SimpleClass_Classifier

def test_SimpleClass_Classifier___init__():
    assert SimpleClass_Classifier.__init__(SimpleClass_Classifier(''), '') == None

