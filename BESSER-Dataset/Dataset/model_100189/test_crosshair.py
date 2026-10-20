from python_code import sql_ExpOperand
from python_code import sql_Operand

def test_sql_ExpOperand___init__():
    assert sql_ExpOperand.__init__(sql_ExpOperand('', sql_ExpOperand=sql_Operand()), '', sql_ExpOperand=sql_Operand()) == None


from python_code import sql_JRParameter
from python_code import sql_Prms

def test_sql_JRParameter___init__():
    assert sql_JRParameter.__init__(sql_JRParameter('', sql_JRParameter=sql_Prms()), '', sql_JRParameter=sql_Prms()) == None


from python_code import sql_ColumnFull
from python_code import sql_OrOrderByColumn
from python_code import sql_OrderByColumnFull

def test_sql_OrderByColumnFull___init__():
    assert sql_OrderByColumnFull.__init__(sql_OrderByColumnFull(0, '\x00', sql_OrderByColumnFull=sql_OrOrderByColumn(), sql_OrderByColumnFull48=sql_ColumnFull()), 0, '\x00', sql_OrderByColumnFull=sql_OrOrderByColumn(), sql_OrderByColumnFull48=sql_ColumnFull()) == None


from python_code import sql_Operand
from python_code import sql_POperand

def test_sql_POperand___init__():
    assert sql_POperand.__init__(sql_POperand('', sql_POperand=sql_Operand()), '', sql_POperand=sql_Operand()) == None


import datetime as _ch_datetime
from python_code import sql_OpList
from python_code import sql_Operand
from python_code import sql_ScalarOperand

def test_sql_ScalarOperand___init__():
    assert sql_ScalarOperand.__init__(sql_ScalarOperand('', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 3), _ch_datetime.date(1, 1, 1), 0, '', sql_ScalarOperand=sql_Operand(), sql_ScalarOperand167=sql_OpList()), '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0, '', sql_ScalarOperand=sql_Operand(), sql_ScalarOperand167=sql_OpList()) == None

