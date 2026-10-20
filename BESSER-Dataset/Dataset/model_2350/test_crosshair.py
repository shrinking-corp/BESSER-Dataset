from python_code import simplerdbms_Column
from python_code import simplerdbms_ForeignKey
from python_code import simplerdbms_Key
from python_code import simplerdbms_Table

def test_simplerdbms_Column___init__():
    assert simplerdbms_Column.__init__(simplerdbms_Column('', Column14=simplerdbms_Key(), Column18=simplerdbms_Table(), column=simplerdbms_Table(), column2=set(), column4=set(), Column=simplerdbms_ForeignKey()), '', Column14=simplerdbms_Key(), Column18=simplerdbms_Table(), column=simplerdbms_Table(), column2=set(), column4=set(), Column=simplerdbms_ForeignKey()) == None


from python_code import simplerdbms_RModelElement

def test_simplerdbms_RModelElement___init__():
    assert simplerdbms_RModelElement.__init__(simplerdbms_RModelElement('', '\x00'), '\x00\x00', '') == None

