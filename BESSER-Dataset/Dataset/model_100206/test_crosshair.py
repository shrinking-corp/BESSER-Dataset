from python_code import sqlview_EclExpression

def test_sqlview_EclExpression___init__():
    assert sqlview_EclExpression.__init__(sqlview_EclExpression(''), '') == None


from python_code import sqlview_Model

def test_sqlview_Model___init__():
    assert sqlview_Model.__init__(sqlview_Model('', sqlview_Model=set(), sqlview_Model2=set()), '', sqlview_Model=set(), sqlview_Model2=set()) == None


from python_code import sqlview_Join
from python_code import sqlview_Relation

def test_sqlview_Relation___init__():
    assert sqlview_Relation.__init__(sqlview_Relation('', sqlview_Relation=sqlview_Join()), '', sqlview_Relation=sqlview_Join()) == None


from python_code import sqlview_Expression
from python_code import sqlview_Select

def test_sqlview_Select___init__():
    assert sqlview_Select.__init__(sqlview_Select('', sqlview_Select12=set(), sqlview_Select=sqlview_Expression()), '', sqlview_Select12=set(), sqlview_Select=sqlview_Expression()) == None

