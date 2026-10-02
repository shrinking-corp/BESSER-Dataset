from python_code import SimpleRDBMS_Column
from python_code import SimpleRDBMS_ForeignKey
from python_code import SimpleRDBMS_Key
from python_code import SimpleRDBMS_Table

def test_SimpleRDBMS_Column___init__():
    assert SimpleRDBMS_Column.__init__(SimpleRDBMS_Column('', Column=SimpleRDBMS_Table(), column=SimpleRDBMS_Table(), column8=set(), column11=set(), Column19=SimpleRDBMS_ForeignKey(), Column14=SimpleRDBMS_Key()), '', Column=SimpleRDBMS_Table(), column=SimpleRDBMS_Table(), column8=set(), column11=set(), Column19=SimpleRDBMS_ForeignKey(), Column14=SimpleRDBMS_Key()) == None

from python_code import SimpleRDBMS_RModelElement

def test_SimpleRDBMS_RModelElement___init__():
    assert SimpleRDBMS_RModelElement.__init__(SimpleRDBMS_RModelElement('', '\x00'), '\x00\x00', '') == None
