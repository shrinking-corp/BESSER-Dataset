from python_code import rdbmsMM_Column
from python_code import rdbmsMM_ForeignKey
from python_code import rdbmsMM_Key
from python_code import rdbmsMM_Table

def test_rdbmsMM_Column___init__():
    assert rdbmsMM_Column.__init__(rdbmsMM_Column('', Column=rdbmsMM_ForeignKey(), Column16=rdbmsMM_Key(), column=rdbmsMM_Table(), column2=set(), column4=set(), Column23=rdbmsMM_Table()), '', Column=rdbmsMM_ForeignKey(), Column16=rdbmsMM_Key(), column=rdbmsMM_Table(), column2=set(), column4=set(), Column23=rdbmsMM_Table()) == None


from python_code import rdbmsMM_RModelElement

def test_rdbmsMM_RModelElement___init__():
    assert rdbmsMM_RModelElement.__init__(rdbmsMM_RModelElement('', '\x00'), '\x00\x00', '') == None

