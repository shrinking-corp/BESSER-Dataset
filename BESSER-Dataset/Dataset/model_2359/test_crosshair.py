from python_code import SimpleRDBMS_RdbmsColumn
from python_code import SimpleRDBMS_RdbmsForeignKey
from python_code import SimpleRDBMS_RdbmsKey
from python_code import SimpleRDBMS_RdbmsTable

def test_SimpleRDBMS_RdbmsColumn___init__():
    assert SimpleRDBMS_RdbmsColumn.__init__(SimpleRDBMS_RdbmsColumn('', RdbmsColumn=SimpleRDBMS_RdbmsForeignKey(), RdbmsColumn12=SimpleRDBMS_RdbmsKey(), RdbmsColumn21=SimpleRDBMS_RdbmsTable(), rdbmsColumn=SimpleRDBMS_RdbmsTable(), rdbmsColumn2=set(), rdbmsColumn4=set()), '', RdbmsColumn=SimpleRDBMS_RdbmsForeignKey(), RdbmsColumn12=SimpleRDBMS_RdbmsKey(), RdbmsColumn21=SimpleRDBMS_RdbmsTable(), rdbmsColumn=SimpleRDBMS_RdbmsTable(), rdbmsColumn2=set(), rdbmsColumn4=set()) == None


from python_code import SimpleRDBMS_RdbmsModelElement

def test_SimpleRDBMS_RdbmsModelElement___init__():
    assert SimpleRDBMS_RdbmsModelElement.__init__(SimpleRDBMS_RdbmsModelElement('', '', '\x00\x00'), '', '', '') == None

