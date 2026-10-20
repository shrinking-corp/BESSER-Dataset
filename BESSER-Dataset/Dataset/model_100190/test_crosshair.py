from python_code import sql_column_Column

def test_sql_column_Column___init__():
    assert sql_column_Column.__init__(sql_column_Column(''), '') == None


from python_code import column_ColumnOperation
from python_code import expression_Expression
from python_code import parameter_SelectParameter
from python_code import sql_column_SingleColumnExpression

def test_sql_column_SingleColumnExpression___init__():
    assert sql_column_SingleColumnExpression.__init__(sql_column_SingleColumnExpression('', sql_column_SingleColumnExpression=expression_Expression(), sql_column_SingleColumnExpression20=column_ColumnOperation(), sql_column_SingleColumnExpression22=parameter_SelectParameter()), '', sql_column_SingleColumnExpression=expression_Expression(), sql_column_SingleColumnExpression20=column_ColumnOperation(), sql_column_SingleColumnExpression22=parameter_SelectParameter()) == None


from python_code import sql_from_Table

def test_sql_from_Table___init__():
    assert sql_from_Table.__init__(sql_from_Table(''), '') == None


from python_code import SelectExpression
from python_code import from_Table
from python_code import sql_from_TableExpression

def test_sql_from_TableExpression___init__():
    assert sql_from_TableExpression.__init__(sql_from_TableExpression('', sql_from_TableExpression27=from_Table(), sql_from_TableExpression=SelectExpression()), '', sql_from_TableExpression27=from_Table(), sql_from_TableExpression=SelectExpression()) == None


from python_code import sql_limit_LimitExpression

def test_sql_limit_LimitExpression___init__():
    assert sql_limit_LimitExpression.__init__(sql_limit_LimitExpression('', '\x00'), '\x00\x00', '') == None


from python_code import sql_orderBy_OrderByAliasExpression

def test_sql_orderBy_OrderByAliasExpression___init__():
    assert sql_orderBy_OrderByAliasExpression.__init__(sql_orderBy_OrderByAliasExpression(''), '') == None


from python_code import sql_term_SimpleTerm

def test_sql_term_SimpleTerm___init__():
    assert sql_term_SimpleTerm.__init__(sql_term_SimpleTerm(''), '') == None


from python_code import sql_value_FunctionValue

def test_sql_value_FunctionValue___init__():
    assert sql_value_FunctionValue.__init__(sql_value_FunctionValue('', sql_value_FunctionValue=set()), '', sql_value_FunctionValue=set()) == None

