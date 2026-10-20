from python_code import ddl_DataElement

def test_ddl_DataElement___init__():
    assert ddl_DataElement.__init__(ddl_DataElement(''), '') == None


from python_code import ddl_Schema

def test_ddl_Schema___init__():
    assert ddl_Schema.__init__(ddl_Schema(0, False, 0.0, ddl_Schema=set(), ddl_Schema2=set()), 0, False, 0.0, ddl_Schema=set(), ddl_Schema2=set()) == None

