from python_code import rdbms_Column
from python_code import rdbms_ForeignKey
from python_code import rdbms_Key
from python_code import rdbms_Table

def test_rdbms_Column___init__():
    assert rdbms_Column.__init__(rdbms_Column('', column=set(), Column=rdbms_ForeignKey(), columns=rdbms_Table(), Column17=rdbms_Table(), Column13=rdbms_Key(), columns2=set()), '', column=set(), Column=rdbms_ForeignKey(), columns=rdbms_Table(), Column17=rdbms_Table(), Column13=rdbms_Key(), columns2=set()) == None


from python_code import rdbms_RModelElement

def test_rdbms_RModelElement___init__():
    assert rdbms_RModelElement.__init__(rdbms_RModelElement('', '\x00'), '\x00\x00', '') == None

