from python_code import essentialocl_expressions_BooleanLiteralExp

def test_essentialocl_expressions_BooleanLiteralExp___init__():
    assert essentialocl_expressions_BooleanLiteralExp.__init__(essentialocl_expressions_BooleanLiteralExp(''), '') == None


from python_code import essentialocl_expressions_CollectionLiteralExp
from python_code import expressions_essentialocl_Type

def test_essentialocl_expressions_CollectionLiteralExp___init__():
    assert essentialocl_expressions_CollectionLiteralExp.__init__(essentialocl_expressions_CollectionLiteralExp('', essentialocl_expressions_CollectionLiteralExp=set(), essentialocl_expressions_CollectionLiteralExp89=expressions_essentialocl_Type()), '', essentialocl_expressions_CollectionLiteralExp=set(), essentialocl_expressions_CollectionLiteralExp89=expressions_essentialocl_Type()) == None


from python_code import essentialocl_expressions_IntegerLiteralExp

def test_essentialocl_expressions_IntegerLiteralExp___init__():
    assert essentialocl_expressions_IntegerLiteralExp.__init__(essentialocl_expressions_IntegerLiteralExp(''), '') == None


from python_code import OclLibrary
from python_code import essentialocl_expressions_OclExpression

def test_essentialocl_expressions_OclExpression___init__():
    assert essentialocl_expressions_OclExpression.__init__(essentialocl_expressions_OclExpression(essentialocl_expressions_OclExpression=OclLibrary()), essentialocl_expressions_OclExpression=OclLibrary()) == None

def test_essentialocl_expressions_OclExpression_withAsSet():
    assert essentialocl_expressions_OclExpression.withAsSet(essentialocl_expressions_OclExpression(essentialocl_expressions_OclExpression=OclLibrary())) == None

def test_essentialocl_expressions_OclExpression_withAtPre():
    assert essentialocl_expressions_OclExpression.withAtPre(essentialocl_expressions_OclExpression(essentialocl_expressions_OclExpression=OclLibrary())) == None


from python_code import essentialocl_expressions_RealLiteralExp

def test_essentialocl_expressions_RealLiteralExp___init__():
    assert essentialocl_expressions_RealLiteralExp.__init__(essentialocl_expressions_RealLiteralExp(''), '') == None


from python_code import essentialocl_expressions_StringLiteralExp

def test_essentialocl_expressions_StringLiteralExp___init__():
    assert essentialocl_expressions_StringLiteralExp.__init__(essentialocl_expressions_StringLiteralExp(''), '') == None


from python_code import essentialocl_expressions_UnlimitedNaturalExp

def test_essentialocl_expressions_UnlimitedNaturalExp___init__():
    assert essentialocl_expressions_UnlimitedNaturalExp.__init__(essentialocl_expressions_UnlimitedNaturalExp(''), '') == None


from python_code import OclExpression
from python_code import essentialocl_expressions_Variable
from python_code import expressions_essentialocl_Parameter

def test_essentialocl_expressions_Variable___init__():
    assert essentialocl_expressions_Variable.__init__(essentialocl_expressions_Variable(essentialocl_expressions_Variable43=OclExpression(), essentialocl_expressions_Variable=expressions_essentialocl_Parameter()), essentialocl_expressions_Variable43=OclExpression(), essentialocl_expressions_Variable=expressions_essentialocl_Parameter()) == None

def test_essentialocl_expressions_Variable_asParameter():
    assert essentialocl_expressions_Variable.asParameter(essentialocl_expressions_Variable(essentialocl_expressions_Variable43=OclExpression(), essentialocl_expressions_Variable=expressions_essentialocl_Parameter())) == None

def test_essentialocl_expressions_Variable_asProperty():
    assert essentialocl_expressions_Variable.asProperty(essentialocl_expressions_Variable(essentialocl_expressions_Variable43=OclExpression(), essentialocl_expressions_Variable=expressions_essentialocl_Parameter())) == None


from python_code import OclLibrary
from python_code import essentialocl_types_CollectionType
from python_code import types_essentialocl_Type

def test_essentialocl_types_CollectionType___init__():
    assert essentialocl_types_CollectionType.__init__(essentialocl_types_CollectionType('', essentialocl_types_CollectionType=types_essentialocl_Type(), essentialocl_types_CollectionType3=OclLibrary()), '', essentialocl_types_CollectionType=types_essentialocl_Type(), essentialocl_types_CollectionType3=OclLibrary()) == None

