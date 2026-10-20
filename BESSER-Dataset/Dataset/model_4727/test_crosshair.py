from python_code import mprologTermReference_Functor
from python_code import mprologTermReference_FunctorReference
from python_code import mprologTermReference_Head
from python_code import mprologTermReference_Term

def test_mprologTermReference_Functor___init__():
    assert mprologTermReference_Functor.__init__(mprologTermReference_Functor('', mprologTermReference_Functor=mprologTermReference_Head(), mprologTermReference_Functor28=mprologTermReference_FunctorReference(), mprologTermReference_Functor13=mprologTermReference_Term()), '', mprologTermReference_Functor=mprologTermReference_Head(), mprologTermReference_Functor28=mprologTermReference_FunctorReference(), mprologTermReference_Functor13=mprologTermReference_Term()) == None


from python_code import mprologTermReference_Model

def test_mprologTermReference_Model___init__():
    assert mprologTermReference_Model.__init__(mprologTermReference_Model('', mprologTermReference_Model=set()), '', mprologTermReference_Model=set()) == None


from python_code import mprologTermReference_InfixExpression
from python_code import mprologTermReference_Operator

def test_mprologTermReference_Operator___init__():
    assert mprologTermReference_Operator.__init__(mprologTermReference_Operator('', mprologTermReference_Operator=mprologTermReference_InfixExpression()), '', mprologTermReference_Operator=mprologTermReference_InfixExpression()) == None


from python_code import mprologTermReference_QuotedAtom

def test_mprologTermReference_QuotedAtom___init__():
    assert mprologTermReference_QuotedAtom.__init__(mprologTermReference_QuotedAtom(''), '') == None


from python_code import mprologTermReference_Variable
from python_code import mprologTermReference_VariableReference

def test_mprologTermReference_Variable___init__():
    assert mprologTermReference_Variable.__init__(mprologTermReference_Variable('', mprologTermReference_Variable=mprologTermReference_VariableReference()), '', mprologTermReference_Variable=mprologTermReference_VariableReference()) == None

