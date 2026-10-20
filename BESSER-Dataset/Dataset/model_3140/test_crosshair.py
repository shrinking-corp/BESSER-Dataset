from python_code import classes_Constant
from python_code import classes_ConstantRef
from python_code import classes_Value

def test_classes_Constant___init__():
    assert classes_Constant.__init__(classes_Constant('', classes_Constant=classes_Value(), classes_Constant28=classes_ConstantRef()), '', classes_Constant=classes_Value(), classes_Constant28=classes_ConstantRef()) == None


from python_code import classes_Description

def test_classes_Description___init__():
    assert classes_Description.__init__(classes_Description(''), '') == None


from python_code import classes_IntegerLiteral

def test_classes_IntegerLiteral___init__():
    assert classes_IntegerLiteral.__init__(classes_IntegerLiteral(0), 0) == None

