from python_code import class_diagramm_Association
from python_code import class_diagramm_RefClass

def test_class_diagramm_Association___init__():
    assert class_diagramm_Association.__init__(class_diagramm_Association(0, 0, '', False, class_diagramm_Association=class_diagramm_RefClass(), class_diagramm_Association28=class_diagramm_RefClass()), 0, 0, '', True, class_diagramm_Association=class_diagramm_RefClass(), class_diagramm_Association28=class_diagramm_RefClass()) == None


from python_code import class_diagramm_Attribute
from python_code import class_diagramm_RefClass
from python_code import class_diagramm_RefDataType

def test_class_diagramm_Attribute___init__():
    assert class_diagramm_Attribute.__init__(class_diagramm_Attribute('', '\x00', class_diagramm_Attribute=class_diagramm_RefClass(), class_diagramm_Attribute12=class_diagramm_RefDataType()), '\x00\x00', '', class_diagramm_Attribute=class_diagramm_RefClass(), class_diagramm_Attribute12=class_diagramm_RefDataType()) == None


from python_code import class_diagramm_Class
from python_code import class_diagramm_RefClass

def test_class_diagramm_Class___init__():
    assert class_diagramm_Class.__init__(class_diagramm_Class('', '', class_diagramm_Class=class_diagramm_RefClass(), class_diagramm_Class22=set(), class_diagramm_Class24=set()), '', '', class_diagramm_Class=class_diagramm_RefClass(), class_diagramm_Class22=set(), class_diagramm_Class24=set()) == None


from python_code import class_diagramm_DataType

def test_class_diagramm_DataType___init__():
    assert class_diagramm_DataType.__init__(class_diagramm_DataType(''), '') == None


from python_code import class_diagramm_Method
from python_code import class_diagramm_RefClass
from python_code import class_diagramm_RefDataType

def test_class_diagramm_Method___init__():
    assert class_diagramm_Method.__init__(class_diagramm_Method('\x00\x00', '', class_diagramm_Method=class_diagramm_RefClass(), class_diagramm_Method6=set(), class_diagramm_Method8=class_diagramm_RefDataType()), '', '', class_diagramm_Method=class_diagramm_RefClass(), class_diagramm_Method6=set(), class_diagramm_Method8=class_diagramm_RefDataType()) == None


from python_code import class_diagramm_Package

def test_class_diagramm_Package___init__():
    assert class_diagramm_Package.__init__(class_diagramm_Package('', class_diagramm_Package=set(), class_diagramm_Package2=set()), '', class_diagramm_Package=set(), class_diagramm_Package2=set()) == None


from python_code import class_diagramm_Parameter
from python_code import class_diagramm_RefClass
from python_code import class_diagramm_RefDataType

def test_class_diagramm_Parameter___init__():
    assert class_diagramm_Parameter.__init__(class_diagramm_Parameter('', class_diagramm_Parameter17=class_diagramm_RefDataType(), class_diagramm_Parameter=class_diagramm_RefClass()), '', class_diagramm_Parameter17=class_diagramm_RefDataType(), class_diagramm_Parameter=class_diagramm_RefClass()) == None

