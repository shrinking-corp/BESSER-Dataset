from python_code import sql_ColumnNames
from python_code import sql_abc

def test_sql_ColumnNames___init__():
    assert sql_ColumnNames.__init__(sql_ColumnNames('', sql_ColumnNames=sql_abc()), '', sql_ColumnNames=sql_abc()) == None


from python_code import sql_ColumnFull
from python_code import sql_ColumnOperand
from python_code import sql_Operand

def test_sql_ColumnOperand___init__():
    assert sql_ColumnOperand.__init__(sql_ColumnOperand('', sql_ColumnOperand=sql_Operand(), sql_ColumnOperand253=sql_ColumnFull()), '', sql_ColumnOperand=sql_Operand(), sql_ColumnOperand253=sql_ColumnFull()) == None


from python_code import sql_ExpOperand
from python_code import sql_Operand

def test_sql_ExpOperand___init__():
    assert sql_ExpOperand.__init__(sql_ExpOperand('', sql_ExpOperand=sql_Operand()), '', sql_ExpOperand=sql_Operand()) == None


from python_code import sql_FunctionExtract
from python_code import sql_Operand
from python_code import sql_Operands

def test_sql_FunctionExtract___init__():
    assert sql_FunctionExtract.__init__(sql_FunctionExtract('', sql_FunctionExtract218=sql_Operands(), sql_FunctionExtract=sql_Operand()), '', sql_FunctionExtract218=sql_Operands(), sql_FunctionExtract=sql_Operand()) == None


from python_code import sql_IntegerValue

def test_sql_IntegerValue___init__():
    assert sql_IntegerValue.__init__(sql_IntegerValue(''), '') == None


from python_code import sql_JRParameter
from python_code import sql_Prms

def test_sql_JRParameter___init__():
    assert sql_JRParameter.__init__(sql_JRParameter('', sql_JRParameter=sql_Prms()), '', sql_JRParameter=sql_Prms()) == None


from python_code import sql_ColumnFull
from python_code import sql_OrOrderByColumn
from python_code import sql_OrderByColumnFull

def test_sql_OrderByColumnFull___init__():
    assert sql_OrderByColumnFull.__init__(sql_OrderByColumnFull('', '\x00', sql_OrderByColumnFull=sql_OrOrderByColumn(), sql_OrderByColumnFull106=sql_ColumnFull()), '\x00\x00', '', sql_OrderByColumnFull=sql_OrOrderByColumn(), sql_OrderByColumnFull106=sql_ColumnFull()) == None


from python_code import sql_PivotFunctions
from python_code import sql_PivotTable

def test_sql_PivotFunctions___init__():
    assert sql_PivotFunctions.__init__(sql_PivotFunctions('', sql_PivotFunctions=sql_PivotTable()), '', sql_PivotFunctions=sql_PivotTable()) == None


from python_code import sql_PivotInClause
from python_code import sql_PivotTable
from python_code import sql_SubQueryOperand
from python_code import sql_UnpivotInClauseArgs

def test_sql_PivotInClause___init__():
    assert sql_PivotInClause.__init__(sql_PivotInClause('', sql_PivotInClause=sql_PivotTable(), sql_PivotInClause87=sql_SubQueryOperand(), sql_PivotInClause90=sql_UnpivotInClauseArgs()), '', sql_PivotInClause=sql_PivotTable(), sql_PivotInClause87=sql_SubQueryOperand(), sql_PivotInClause90=sql_UnpivotInClauseArgs()) == None


from python_code import sql_RowValue
from python_code import sql_RowValues

def test_sql_RowValue___init__():
    assert sql_RowValue.__init__(sql_RowValue('', sql_RowValue=sql_RowValues()), '', sql_RowValue=sql_RowValues()) == None


from python_code import sql_OpList
from python_code import sql_Operand
from python_code import sql_ScalarOperand

def test_sql_ScalarOperand___init__():
    assert sql_ScalarOperand.__init__(sql_ScalarOperand('', '', '', '', '', '', '', sql_ScalarOperand=sql_Operand(), sql_ScalarOperand284=sql_OpList()), '', '\x00', '', '', '', '', '', sql_ScalarOperand=sql_Operand(), sql_ScalarOperand284=sql_OpList()) == None


from python_code import sql_UnipivotInClause
from python_code import sql_UnpivotInClauseArgs

def test_sql_UnipivotInClause___init__():
    assert sql_UnipivotInClause.__init__(sql_UnipivotInClause('', sql_UnipivotInClause=sql_UnpivotInClauseArgs()), '', sql_UnipivotInClause=sql_UnpivotInClauseArgs()) == None

