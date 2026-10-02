from python_code import superimposed_BooleanExp

def test_superimposed_BooleanExp___init__():
    assert superimposed_BooleanExp.__init__(superimposed_BooleanExp(''), '') == None

from python_code import superimposed_IntegerExp

def test_superimposed_IntegerExp___init__():
    assert superimposed_IntegerExp.__init__(superimposed_IntegerExp(''), '') == None

from python_code import superimposed_Iterator
from python_code import superimposed_IteratorExp

def test_superimposed_IteratorExp___init__():
    assert superimposed_IteratorExp.__init__(superimposed_IteratorExp('', superimposed_IteratorExp=superimposed_Iterator()), '', superimposed_IteratorExp=superimposed_Iterator()) == None

from python_code import superimposed_NavigationCallExp

def test_superimposed_NavigationCallExp___init__():
    assert superimposed_NavigationCallExp.__init__(superimposed_NavigationCallExp(''), '') == None

from python_code import superimposed_OperationCallExp

def test_superimposed_OperationCallExp___init__():
    assert superimposed_OperationCallExp.__init__(superimposed_OperationCallExp('', superimposed_OperationCallExp=set()), '', superimposed_OperationCallExp=set()) == None

from python_code import superimposed_OperatorCallExp

def test_superimposed_OperatorCallExp___init__():
    assert superimposed_OperatorCallExp.__init__(superimposed_OperatorCallExp(''), '') == None

from python_code import superimposed_RealExp

def test_superimposed_RealExp___init__():
    assert superimposed_RealExp.__init__(superimposed_RealExp(''), '') == None

from python_code import superimposed_StringExp

def test_superimposed_StringExp___init__():
    assert superimposed_StringExp.__init__(superimposed_StringExp(''), '') == None

from python_code import superimposed_LetExp
from python_code import superimposed_OclExpression
from python_code import superimposed_OclType
from python_code import superimposed_VariableDeclaration
from python_code import superimposed_VariableExp

def test_superimposed_VariableDeclaration___init__():
    assert superimposed_VariableDeclaration.__init__(superimposed_VariableDeclaration('', superimposed_VariableDeclaration=superimposed_OclExpression(), superimposed_VariableDeclaration2=superimposed_OclType(), superimposed_VariableDeclaration4=superimposed_VariableExp(), superimposed_VariableDeclaration6=superimposed_LetExp()), '', superimposed_VariableDeclaration=superimposed_OclExpression(), superimposed_VariableDeclaration2=superimposed_OclType(), superimposed_VariableDeclaration4=superimposed_VariableExp(), superimposed_VariableDeclaration6=superimposed_LetExp()) == None
