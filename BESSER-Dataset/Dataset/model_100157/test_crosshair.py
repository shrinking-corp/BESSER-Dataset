from python_code import query_BooleanArrayExpression

def test_query_BooleanArrayExpression___init__():
    assert query_BooleanArrayExpression.__init__(query_BooleanArrayExpression(''), '') == None


from python_code import query_BooleanExpression

def test_query_BooleanExpression___init__():
    assert query_BooleanExpression.__init__(query_BooleanExpression(''), '') == None


import datetime as _ch_datetime
from python_code import query_DateArrayExpression

def test_query_DateArrayExpression___init__():
    assert query_DateArrayExpression.__init__(query_DateArrayExpression(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


import datetime as _ch_datetime
from python_code import query_DateExpression

def test_query_DateExpression___init__():
    assert query_DateExpression.__init__(query_DateExpression(_ch_datetime.date(1, 1, 2)), _ch_datetime.date(1, 1, 1)) == None


from python_code import query_DoubleArrayExpression

def test_query_DoubleArrayExpression___init__():
    assert query_DoubleArrayExpression.__init__(query_DoubleArrayExpression(0.0), 0.0) == None


from python_code import query_DoubleExpression

def test_query_DoubleExpression___init__():
    assert query_DoubleExpression.__init__(query_DoubleExpression(0.0), 0.0) == None


from python_code import query_ExpressionWhereEntry

def test_query_ExpressionWhereEntry___init__():
    assert query_ExpressionWhereEntry.__init__(query_ExpressionWhereEntry(''), '') == None


from python_code import query_LongArrayExpression

def test_query_LongArrayExpression___init__():
    assert query_LongArrayExpression.__init__(query_LongArrayExpression(''), '') == None


from python_code import query_LongExpression

def test_query_LongExpression___init__():
    assert query_LongExpression.__init__(query_LongExpression(''), '') == None


from python_code import query_ArrayExpression
from python_code import query_MultiExpressionWhereEntry

def test_query_MultiExpressionWhereEntry___init__():
    assert query_MultiExpressionWhereEntry.__init__(query_MultiExpressionWhereEntry('', query_MultiExpressionWhereEntry=query_ArrayExpression()), '', query_MultiExpressionWhereEntry=query_ArrayExpression()) == None


from python_code import query_NullArrayExpression

def test_query_NullArrayExpression___init__():
    assert query_NullArrayExpression.__init__(query_NullArrayExpression(''), '') == None


from python_code import query_NullExpression

def test_query_NullExpression___init__():
    assert query_NullExpression.__init__(query_NullExpression(''), '') == None


from python_code import query_ReplacableValue

def test_query_ReplacableValue___init__():
    assert query_ReplacableValue.__init__(query_ReplacableValue(''), '') == None


from python_code import query_Expression
from python_code import query_SingleExpressionWhereEntry

def test_query_SingleExpressionWhereEntry___init__():
    assert query_SingleExpressionWhereEntry.__init__(query_SingleExpressionWhereEntry('', query_SingleExpressionWhereEntry=query_Expression()), '', query_SingleExpressionWhereEntry=query_Expression()) == None


from python_code import query_StringArrayExpression

def test_query_StringArrayExpression___init__():
    assert query_StringArrayExpression.__init__(query_StringArrayExpression(''), '') == None


from python_code import query_StringExpression

def test_query_StringExpression___init__():
    assert query_StringExpression.__init__(query_StringExpression(''), '') == None

