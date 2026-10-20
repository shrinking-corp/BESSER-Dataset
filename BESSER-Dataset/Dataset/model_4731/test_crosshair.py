from python_code import prolog_Additive
from python_code import prolog_Term

def test_prolog_Additive___init__():
    assert prolog_Additive.__init__(prolog_Additive('', prolog_Additive=prolog_Term(), prolog_Additive22=prolog_Term()), '', prolog_Additive=prolog_Term(), prolog_Additive22=prolog_Term()) == None


from python_code import prolog_AnonymousVariable

def test_prolog_AnonymousVariable___init__():
    assert prolog_AnonymousVariable.__init__(prolog_AnonymousVariable(''), '') == None


from python_code import prolog_Multiplicative
from python_code import prolog_Term

def test_prolog_Multiplicative___init__():
    assert prolog_Multiplicative.__init__(prolog_Multiplicative('', prolog_Multiplicative=prolog_Term(), prolog_Multiplicative27=prolog_Term()), '', prolog_Multiplicative=prolog_Term(), prolog_Multiplicative27=prolog_Term()) == None


from python_code import prolog_Negation
from python_code import prolog_Term

def test_prolog_Negation___init__():
    assert prolog_Negation.__init__(prolog_Negation('', prolog_Negation=prolog_Term()), '', prolog_Negation=prolog_Term()) == None


from python_code import prolog_Numeral

def test_prolog_Numeral___init__():
    assert prolog_Numeral.__init__(prolog_Numeral(0.0), 0.0) == None


from python_code import prolog_Clause
from python_code import prolog_Predicate

def test_prolog_Predicate___init__():
    assert prolog_Predicate.__init__(prolog_Predicate('', prolog_Predicate9=set(), prolog_Predicate=prolog_Clause()), '', prolog_Predicate9=set(), prolog_Predicate=prolog_Clause()) == None


from python_code import prolog_String

def test_prolog_String___init__():
    assert prolog_String.__init__(prolog_String(''), '') == None


from python_code import prolog_Variable
from python_code import prolog_VariableReference

def test_prolog_Variable___init__():
    assert prolog_Variable.__init__(prolog_Variable('', prolog_Variable=prolog_VariableReference()), '', prolog_Variable=prolog_VariableReference()) == None

