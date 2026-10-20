from python_code import rdbms_RdbmsElement

def test_rdbms_RdbmsElement___init__():
    assert rdbms_RdbmsElement.__init__(rdbms_RdbmsElement('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import rdbms_RdbmsForeignKey
from python_code import rdbms_RdbmsIdentifierField
from python_code import rdbms_RdbmsJunctionTable

def test_rdbms_RdbmsForeignKey___init__():
    assert rdbms_RdbmsForeignKey.__init__(rdbms_RdbmsForeignKey(False, '', False, False, False, foreignKeys=rdbms_RdbmsIdentifierField(), rdbms_RdbmsForeignKey=rdbms_RdbmsJunctionTable(), rdbms_RdbmsForeignKey19=rdbms_RdbmsJunctionTable(), RdbmsForeignKey=rdbms_RdbmsIdentifierField()), True, '', False, False, False, foreignKeys=rdbms_RdbmsIdentifierField(), rdbms_RdbmsForeignKey=rdbms_RdbmsJunctionTable(), rdbms_RdbmsForeignKey19=rdbms_RdbmsJunctionTable(), RdbmsForeignKey=rdbms_RdbmsIdentifierField()) == None


from python_code import rdbms_RdbmsIndex
from python_code import rdbms_RdbmsTable

def test_rdbms_RdbmsIndex___init__():
    assert rdbms_RdbmsIndex.__init__(rdbms_RdbmsIndex(True, RdbmsIndex=rdbms_RdbmsTable(), indexes=rdbms_RdbmsTable(), rdbms_RdbmsIndex=set()), False, RdbmsIndex=rdbms_RdbmsTable(), indexes=rdbms_RdbmsTable(), rdbms_RdbmsIndex=set()) == None


from python_code import rdbms_RdbmsLabelExpression

def test_rdbms_RdbmsLabelExpression___init__():
    assert rdbms_RdbmsLabelExpression.__init__(rdbms_RdbmsLabelExpression(''), '') == None


from python_code import rdbms_RdbmsModifyTableOperation
from python_code import rdbms_RdbmsTable

def test_rdbms_RdbmsModifyTableOperation___init__():
    assert rdbms_RdbmsModifyTableOperation.__init__(rdbms_RdbmsModifyTableOperation('', rdbms_RdbmsModifyTableOperation=set(), rdbms_RdbmsModifyTableOperation59=set(), rdbms_RdbmsModifyTableOperation61=set(), rdbms_RdbmsModifyTableOperation63=rdbms_RdbmsTable()), '', rdbms_RdbmsModifyTableOperation=set(), rdbms_RdbmsModifyTableOperation59=set(), rdbms_RdbmsModifyTableOperation61=set(), rdbms_RdbmsModifyTableOperation63=rdbms_RdbmsTable()) == None


from python_code import rdbms_RdbmsValueField

def test_rdbms_RdbmsValueField___init__():
    assert rdbms_RdbmsValueField.__init__(rdbms_RdbmsValueField(True), False) == None


from python_code import rdbms_RdbmsViewExpressionField

def test_rdbms_RdbmsViewExpressionField___init__():
    assert rdbms_RdbmsViewExpressionField.__init__(rdbms_RdbmsViewExpressionField('\x00', rdbms_RdbmsViewExpressionField=set()), '', rdbms_RdbmsViewExpressionField=set()) == None


from python_code import rdbms_RdbmsViewIdentifierField
from python_code import rdbms_RdbmsViewRecord
from python_code import rdbms_RdbmsViewRecordValue
from python_code import rdbms_RdbmsViewValueField

def test_rdbms_RdbmsViewRecordValue___init__():
    assert rdbms_RdbmsViewRecordValue.__init__(rdbms_RdbmsViewRecordValue('', rdbms_RdbmsViewRecordValue=rdbms_RdbmsViewRecord(), rdbms_RdbmsViewRecordValue96=rdbms_RdbmsViewIdentifierField(), rdbms_RdbmsViewRecordValue99=rdbms_RdbmsViewValueField()), '', rdbms_RdbmsViewRecordValue=rdbms_RdbmsViewRecord(), rdbms_RdbmsViewRecordValue96=rdbms_RdbmsViewIdentifierField(), rdbms_RdbmsViewRecordValue99=rdbms_RdbmsViewValueField()) == None

