from python_code import Class
from python_code import Class_Attribute
from python_code import Classifier

def test_Class_Attribute___init__():
    assert Class_Attribute.__init__(Class_Attribute(False, Class_Attribute=Classifier(), attr=Class()), False, Class_Attribute=Classifier(), attr=Class()) == None


from python_code import Class
from python_code import Class_Attribute
from python_code import Class_Class
from python_code import Classifier

def test_Class_Class___init__():
    assert Class_Class.__init__(Class_Class(False, owner=set(), Class_Class=set(), Classifier=Class_Attribute(False, Class_Attribute=Classifier(), attr=Class())), True, owner=set(), Class_Class=set(), Classifier=Class_Attribute(False, Class_Attribute=Classifier(), attr=Class())) == None


from python_code import Class_NamedElt

def test_Class_NamedElt___init__():
    assert Class_NamedElt.__init__(Class_NamedElt(''), '') == None

