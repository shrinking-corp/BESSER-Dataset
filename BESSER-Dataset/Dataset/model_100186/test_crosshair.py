from python_code import sql_ColumnFull
from python_code import sql_ColumnOperand
from python_code import sql_Operand

def test_sql_ColumnOperand___init__():
    assert sql_ColumnOperand.__init__(sql_ColumnOperand('', sql_ColumnOperand=sql_Operand(), sql_ColumnOperand233=sql_ColumnFull()), '', sql_ColumnOperand=sql_Operand(), sql_ColumnOperand233=sql_ColumnFull()) == None


from python_code import sql_ExpOperand
from python_code import sql_Operand

def test_sql_ExpOperand___init__():
    assert sql_ExpOperand.__init__(sql_ExpOperand('', sql_ExpOperand=sql_Operand()), '', sql_ExpOperand=sql_Operand()) == None


from python_code import sql_FunctionExtract
from python_code import sql_Operand
from python_code import sql_Operands

def test_sql_FunctionExtract___init__():
    assert sql_FunctionExtract.__init__(sql_FunctionExtract('', sql_FunctionExtract=sql_Operand(), sql_FunctionExtract198=sql_Operands()), '', sql_FunctionExtract=sql_Operand(), sql_FunctionExtract198=sql_Operands()) == None


from python_code import sql_JRParameter
from python_code import sql_Prms

def test_sql_JRParameter___init__():
    assert sql_JRParameter.__init__(sql_JRParameter('', sql_JRParameter=sql_Prms()), '', sql_JRParameter=sql_Prms()) == None


from python_code import sql_ColumnFull
from python_code import sql_OrOrderByColumn
from python_code import sql_OrderByColumnFull

def test_sql_OrderByColumnFull___init__():
    assert sql_OrderByColumnFull.__init__(sql_OrderByColumnFull(0, '\x00', sql_OrderByColumnFull86=sql_ColumnFull(), sql_OrderByColumnFull=sql_OrOrderByColumn()), 0, '\x00', sql_OrderByColumnFull86=sql_ColumnFull(), sql_OrderByColumnFull=sql_OrOrderByColumn()) == None


from python_code import sql_PivotFunctions
from python_code import sql_PivotTable

def test_sql_PivotFunctions___init__():
    assert sql_PivotFunctions.__init__(sql_PivotFunctions('', sql_PivotFunctions=sql_PivotTable()), '', sql_PivotFunctions=sql_PivotTable()) == None


from python_code import sql_PivotInClause
from python_code import sql_PivotTable
from python_code import sql_SubQueryOperand
from python_code import sql_UnpivotInClauseArgs

def test_sql_PivotInClause___init__():
    assert sql_PivotInClause.__init__(sql_PivotInClause('', sql_PivotInClause=sql_PivotTable(), sql_PivotInClause70=sql_UnpivotInClauseArgs(), sql_PivotInClause67=sql_SubQueryOperand()), '', sql_PivotInClause=sql_PivotTable(), sql_PivotInClause70=sql_UnpivotInClauseArgs(), sql_PivotInClause67=sql_SubQueryOperand()) == None


import datetime as _ch_datetime
from python_code import sql_OpList
from python_code import sql_Operand
from python_code import sql_ScalarOperand

def test_sql_ScalarOperand___init__():
    assert sql_ScalarOperand.__init__(sql_ScalarOperand(0, '', '\x00\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), sql_ScalarOperand=sql_Operand(), sql_ScalarOperand263=sql_OpList()), 0, '', '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), sql_ScalarOperand=sql_Operand(), sql_ScalarOperand263=sql_OpList()) == None


from python_code import sql_UnipivotInClause
from python_code import sql_UnpivotInClauseArgs

def test_sql_UnipivotInClause___init__():
    assert sql_UnipivotInClause.__init__(sql_UnipivotInClause('', sql_UnipivotInClause=sql_UnpivotInClauseArgs()), '', sql_UnipivotInClause=sql_UnpivotInClauseArgs()) == None

