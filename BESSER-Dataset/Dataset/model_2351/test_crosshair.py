from python_code import simplerdbms_Column
from python_code import simplerdbms_ForeignKey
from python_code import simplerdbms_Key
from python_code import simplerdbms_Table

def test_simplerdbms_Column___init__():
    assert simplerdbms_Column.__init__(simplerdbms_Column('', simplerdbms_Column=simplerdbms_Table(), column=set(), column3=set(), Column=simplerdbms_ForeignKey(), Column13=simplerdbms_Key(), simplerdbms_Column18=simplerdbms_Table()), '', simplerdbms_Column=simplerdbms_Table(), column=set(), column3=set(), Column=simplerdbms_ForeignKey(), Column13=simplerdbms_Key(), simplerdbms_Column18=simplerdbms_Table()) == None


from python_code import simplerdbms_RModelElement

def test_simplerdbms_RModelElement___init__():
    assert simplerdbms_RModelElement.__init__(simplerdbms_RModelElement('', '\x00'), '\x00\x00', '') == None

