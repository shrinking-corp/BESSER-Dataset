from python_code import arithmetics_AbstractDefinition
from python_code import arithmetics_FunctionCall

def test_arithmetics_AbstractDefinition___init__():
    assert arithmetics_AbstractDefinition.__init__(arithmetics_AbstractDefinition('', arithmetics_AbstractDefinition=arithmetics_FunctionCall()), '', arithmetics_AbstractDefinition=arithmetics_FunctionCall()) == None


from python_code import arithmetics_Import
from python_code import arithmetics_Module

def test_arithmetics_Module___init__():
    assert arithmetics_Module.__init__(arithmetics_Module('', arithmetics_Module=set(), arithmetics_Module2=set(), arithmetics_Module5=arithmetics_Import()), '', arithmetics_Module=set(), arithmetics_Module2=set(), arithmetics_Module5=arithmetics_Import()) == None


from python_code import arithmetics_NumberLiteral

def test_arithmetics_NumberLiteral___init__():
    assert arithmetics_NumberLiteral.__init__(arithmetics_NumberLiteral(''), '') == None

