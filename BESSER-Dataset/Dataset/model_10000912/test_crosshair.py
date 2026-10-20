from python_code import datatypes_Array
from python_code import datatypes_Value

def test_datatypes_Array___init__():
    assert datatypes_Array.__init__(datatypes_Array(datatypes_Value('')), datatypes_Value('')) == None


from python_code import datatypes_Bool

def test_datatypes_Bool___init__():
    assert datatypes_Bool.__init__(datatypes_Bool(True), False) == None


from python_code import datatypes_Documents
from python_code import datatypes_Json
from python_code import datatypes_Value

def test_datatypes_Documents___init__():
    assert datatypes_Documents.__init__(datatypes_Documents('\x00\x00', datatypes_Json(datatypes_Value('')), '', 0), '', datatypes_Json(datatypes_Value('')), '', 0) == None


from python_code import datatypes_Json
from python_code import datatypes_Value

def test_datatypes_Json___init__():
    assert datatypes_Json.__init__(datatypes_Json(datatypes_Value('')), datatypes_Value('')) == None


from python_code import datatypes_Number

def test_datatypes_Number___init__():
    assert datatypes_Number.__init__(datatypes_Number(0), 0) == None


from python_code import datatypes_Value

def test_datatypes_Value___init__():
    assert datatypes_Value.__init__(datatypes_Value(''), '') == None


from python_code import user_Provider

def test_user_Provider___init__():
    assert user_Provider.__init__(user_Provider('', '', '', '', ''), '', '', '', '', '') == None

