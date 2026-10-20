from python_code import base_BooleanLiteral

def test_base_BooleanLiteral___init__():
    assert base_BooleanLiteral.__init__(base_BooleanLiteral(True), False) == None


from python_code import base_EnumAnnotationAttribute

def test_base_EnumAnnotationAttribute___init__():
    assert base_EnumAnnotationAttribute.__init__(base_EnumAnnotationAttribute(''), '') == None


from python_code import base_Import

def test_base_Import___init__():
    assert base_Import.__init__(base_Import('', '\x00'), '\x00\x00', '') == None


from python_code import base_IntLiteral

def test_base_IntLiteral___init__():
    assert base_IntLiteral.__init__(base_IntLiteral(''), '') == None


from python_code import base_Annotation
from python_code import base_KeyValue
from python_code import base_Literal

def test_base_KeyValue___init__():
    assert base_KeyValue.__init__(base_KeyValue('', base_KeyValue=base_Annotation(), base_KeyValue4=base_Literal()), '', base_KeyValue=base_Annotation(), base_KeyValue4=base_Literal()) == None


from python_code import base_RealLiteral

def test_base_RealLiteral___init__():
    assert base_RealLiteral.__init__(base_RealLiteral(0.0), 0.0) == None


from python_code import base_SimpleAnnotationAttribute

def test_base_SimpleAnnotationAttribute___init__():
    assert base_SimpleAnnotationAttribute.__init__(base_SimpleAnnotationAttribute(''), '') == None


from python_code import base_StringLiteral

def test_base_StringLiteral___init__():
    assert base_StringLiteral.__init__(base_StringLiteral(''), '') == None

