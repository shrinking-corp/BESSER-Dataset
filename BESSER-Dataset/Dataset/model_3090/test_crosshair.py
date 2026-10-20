from python_code import Class
from python_code import SimpleClass_Association

def test_SimpleClass_Association___init__():
    assert SimpleClass_Association.__init__(SimpleClass_Association('', SimpleClass_Association=Class(), SimpleClass_Association5=Class()), '', SimpleClass_Association=Class(), SimpleClass_Association5=Class()) == None


from python_code import Class
from python_code import Classifier
from python_code import SimpleClass_Attribute

def test_SimpleClass_Attribute___init__():
    assert SimpleClass_Attribute.__init__(SimpleClass_Attribute('\x00', '', SimpleClass_Attribute=Classifier(), attrs=Class()), '', '', SimpleClass_Attribute=Classifier(), attrs=Class()) == None


from python_code import Class
from python_code import Classifier
from python_code import SimpleClass_Attribute
from python_code import SimpleClass_Class

def test_SimpleClass_Class___init__():
    assert SimpleClass_Class.__init__(SimpleClass_Class('', SimpleClass_Class=Class(), class_=set(), Classifier=SimpleClass_Attribute('', '', SimpleClass_Attribute=Classifier(), attrs=Class())), '', SimpleClass_Class=Class(), class_=set(), Classifier=SimpleClass_Attribute('', '', SimpleClass_Attribute=Classifier(), attrs=Class())) == None


from python_code import SimpleClass_Classifier

def test_SimpleClass_Classifier___init__():
    assert SimpleClass_Classifier.__init__(SimpleClass_Classifier(''), '') == None

