from python_code import classmodel_Attribute
from python_code import classmodel_Reference

def test_classmodel_Attribute___init__():
    assert classmodel_Attribute.__init__(classmodel_Attribute(False, '\x00', classmodel_Attribute=classmodel_Reference()), False, '\x00', classmodel_Attribute=classmodel_Reference()) == None


from python_code import classmodel_Import
from python_code import classmodel_Model

def test_classmodel_Import___init__():
    assert classmodel_Import.__init__(classmodel_Import('', classmodel_Import=classmodel_Model()), '', classmodel_Import=classmodel_Model()) == None


from python_code import classmodel_Operation
from python_code import classmodel_Reference

def test_classmodel_Operation___init__():
    assert classmodel_Operation.__init__(classmodel_Operation(False, '\x00', classmodel_Operation=set(), classmodel_Operation41=classmodel_Reference()), False, '', classmodel_Operation=set(), classmodel_Operation41=classmodel_Reference()) == None


from python_code import classmodel_Package

def test_classmodel_Package___init__():
    assert classmodel_Package.__init__(classmodel_Package('', classmodel_Package=set()), '', classmodel_Package=set()) == None

