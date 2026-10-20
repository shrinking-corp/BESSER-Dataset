from python_code import SimpleRDBMS_Column
from python_code import Table

def test_SimpleRDBMS_Column___init__():
    assert SimpleRDBMS_Column.__init__(SimpleRDBMS_Column('', column=Table(), column10=set(), column13=set()), '', column=Table(), column10=set(), column13=set()) == None


from python_code import SimpleRDBMS_RModelElement

def test_SimpleRDBMS_RModelElement___init__():
    assert SimpleRDBMS_RModelElement.__init__(SimpleRDBMS_RModelElement('', '\x00'), '\x00\x00', '') == None

