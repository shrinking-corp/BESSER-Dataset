from python_code import table_Column
from python_code import table_Table

def test_table_Column___init__():
    assert table_Column.__init__(table_Column('', table_Column=table_Table(), table_Column3=table_Table()), '', table_Column=table_Table(), table_Column3=table_Table()) == None


from python_code import table_NamedElement

def test_table_NamedElement___init__():
    assert table_NamedElement.__init__(table_NamedElement(''), '') == None

