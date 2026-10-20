from python_code import Class
from python_code import Class_Attribute
from python_code import Classifier

def test_Class_Attribute___init__():
    assert Class_Attribute.__init__(Class_Attribute('', Class_Attribute=Classifier(), attr=Class()), '\x00', Class_Attribute=Classifier(), attr=Class()) == None


from python_code import Class
from python_code import Class_Attribute
from python_code import Class_Class
from python_code import Classifier

def test_Class_Class___init__():
    assert Class_Class.__init__(Class_Class('', Class_Class=set(), owner=set(), Classifier=Class_Attribute('', Class_Attribute=Classifier(), attr=Class())), '', Class_Class=set(), owner=set(), Classifier=Class_Attribute('', Class_Attribute=Classifier(), attr=Class())) == None


from python_code import Class_NamedElt

def test_Class_NamedElt___init__():
    assert Class_NamedElt.__init__(Class_NamedElt(''), '') == None

