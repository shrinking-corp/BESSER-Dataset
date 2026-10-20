from python_code import Enumeration
from python_code import forms_entityModeling_Attribute

def test_forms_entityModeling_Attribute___init__():
    assert forms_entityModeling_Attribute.__init__(forms_entityModeling_Attribute('', False, '\x00\x00', forms_entityModeling_Attribute=Enumeration()), '', False, '', forms_entityModeling_Attribute=Enumeration()) == None


from python_code import forms_entityModeling_Condition

def test_forms_entityModeling_Condition___init__():
    assert forms_entityModeling_Condition.__init__(forms_entityModeling_Condition('', '\x00'), '\x00\x00', '') == None


from python_code import Attribute
from python_code import Entity
from python_code import forms_entityModeling_Entity

def test_forms_entityModeling_Entity___init__():
    assert forms_entityModeling_Entity.__init__(forms_entityModeling_Entity('', forms_entityModeling_Entity=Attribute(), forms_entityModeling_Entity10=set(), forms_entityModeling_Entity13=Entity(), forms_entityModeling_Entity16=set()), '', forms_entityModeling_Entity=Attribute(), forms_entityModeling_Entity10=set(), forms_entityModeling_Entity13=Entity(), forms_entityModeling_Entity16=set()) == None


from python_code import forms_entityModeling_Enumeration

def test_forms_entityModeling_Enumeration___init__():
    assert forms_entityModeling_Enumeration.__init__(forms_entityModeling_Enumeration('', forms_entityModeling_Enumeration=set()), '', forms_entityModeling_Enumeration=set()) == None


from python_code import Entity
from python_code import forms_entityModeling_Form

def test_forms_entityModeling_Form___init__():
    assert forms_entityModeling_Form.__init__(forms_entityModeling_Form('', '', '', forms_entityModeling_Form=Entity(), forms_entityModeling_Form28=set()), '', '', '', forms_entityModeling_Form=Entity(), forms_entityModeling_Form28=set()) == None


from python_code import forms_entityModeling_Literal

def test_forms_entityModeling_Literal___init__():
    assert forms_entityModeling_Literal.__init__(forms_entityModeling_Literal('', '\x00'), '\x00\x00', '') == None


from python_code import Entity
from python_code import Relationship
from python_code import forms_entityModeling_Relationship

def test_forms_entityModeling_Relationship___init__():
    assert forms_entityModeling_Relationship.__init__(forms_entityModeling_Relationship(0, 0, '\x00\x00', forms_entityModeling_Relationship=Entity(), forms_entityModeling_Relationship23=Relationship()), 0, 0, '', forms_entityModeling_Relationship=Entity(), forms_entityModeling_Relationship23=Relationship()) == None


from python_code import forms_entityModeling_Textfield

def test_forms_entityModeling_Textfield___init__():
    assert forms_entityModeling_Textfield.__init__(forms_entityModeling_Textfield(''), '') == None

