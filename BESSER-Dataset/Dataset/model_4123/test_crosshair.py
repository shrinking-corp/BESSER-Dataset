from python_code import myDsl_COMPARATEUR
from python_code import myDsl_Condition

def test_myDsl_COMPARATEUR___init__():
    assert myDsl_COMPARATEUR.__init__(myDsl_COMPARATEUR('', myDsl_COMPARATEUR=myDsl_Condition()), '', myDsl_COMPARATEUR=myDsl_Condition()) == None


from python_code import myDsl_Nop

def test_myDsl_Nop___init__():
    assert myDsl_Nop.__init__(myDsl_Nop(''), '') == None


from python_code import myDsl_Expression
from python_code import myDsl_Not

def test_myDsl_Not___init__():
    assert myDsl_Not.__init__(myDsl_Not('', myDsl_Not=myDsl_Expression()), '', myDsl_Not=myDsl_Expression()) == None


from python_code import myDsl_AccSucc
from python_code import myDsl_OpAccSucc

def test_myDsl_OpAccSucc___init__():
    assert myDsl_OpAccSucc.__init__(myDsl_OpAccSucc('', myDsl_OpAccSucc=myDsl_AccSucc()), '', myDsl_OpAccSucc=myDsl_AccSucc()) == None


from python_code import myDsl_ABin
from python_code import myDsl_OpConstructeur

def test_myDsl_OpConstructeur___init__():
    assert myDsl_OpConstructeur.__init__(myDsl_OpConstructeur('', myDsl_OpConstructeur=myDsl_ABin()), '', myDsl_OpConstructeur=myDsl_ABin()) == None

