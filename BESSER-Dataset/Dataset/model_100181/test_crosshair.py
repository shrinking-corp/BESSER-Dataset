from python_code import simpleRdbms_Column
from python_code import simpleRdbms_ForeignKey
from python_code import simpleRdbms_Key
from python_code import simpleRdbms_Table

def test_simpleRdbms_Column___init__():
    assert simpleRdbms_Column.__init__(simpleRdbms_Column('', Column=simpleRdbms_Table(), column=simpleRdbms_Table(), column10=set(), Column21=simpleRdbms_ForeignKey(), column13=set(), Column16=simpleRdbms_Key()), '', Column=simpleRdbms_Table(), column=simpleRdbms_Table(), column10=set(), Column21=simpleRdbms_ForeignKey(), column13=set(), Column16=simpleRdbms_Key()) == None


from python_code import simpleRdbms_RModelElement

def test_simpleRdbms_RModelElement___init__():
    assert simpleRdbms_RModelElement.__init__(simpleRdbms_RModelElement('', '\x00'), '\x00\x00', '') == None

