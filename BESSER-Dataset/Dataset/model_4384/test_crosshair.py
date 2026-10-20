from python_code import gseq_And
from python_code import gseq_BooleanExpression
from python_code import gseq_If
from python_code import gseq_Not
from python_code import gseq_While

def test_gseq_BooleanExpression___init__():
    assert gseq_BooleanExpression.__init__(gseq_BooleanExpression(gseq_BooleanExpression24=gseq_And(), gseq_BooleanExpression27=gseq_And(), gseq_BooleanExpression=gseq_If(), gseq_BooleanExpression22=gseq_Not(), gseq_BooleanExpression41=gseq_While()), gseq_BooleanExpression24=gseq_And(), gseq_BooleanExpression27=gseq_And(), gseq_BooleanExpression=gseq_If(), gseq_BooleanExpression22=gseq_Not(), gseq_BooleanExpression41=gseq_While()) == None

def test_gseq_BooleanExpression_bvalue():
    assert gseq_BooleanExpression.bvalue(gseq_BooleanExpression(gseq_BooleanExpression24=gseq_And(), gseq_BooleanExpression27=gseq_And(), gseq_BooleanExpression=gseq_If(), gseq_BooleanExpression22=gseq_Not(), gseq_BooleanExpression41=gseq_While())) == None

def test_gseq_BooleanExpression_pretty():
    assert gseq_BooleanExpression.pretty(gseq_BooleanExpression(gseq_BooleanExpression24=gseq_And(), gseq_BooleanExpression27=gseq_And(), gseq_BooleanExpression=gseq_If(), gseq_BooleanExpression22=gseq_Not(), gseq_BooleanExpression41=gseq_While())) == None


from python_code import gseq_Const

def test_gseq_Const___init__():
    assert gseq_Const.__init__(gseq_Const(''), '') == None


from python_code import gseq_Var

def test_gseq_Var___init__():
    assert gseq_Var.__init__(gseq_Var(''), '') == None

