from python_code import MySQL_Column
from python_code import Table

def test_MySQL_Column___init__():
    assert MySQL_Column.__init__(MySQL_Column('', '', '', '', '', columns=Table()), '', '', '', '', '', columns=Table()) == None


from python_code import MySQL_IntegerColumn
from python_code import MySQL_Table

def test_MySQL_IntegerColumn___init__():
    assert MySQL_IntegerColumn.__init__(MySQL_IntegerColumn('', Column=MySQL_Table()), '', Column=MySQL_Table()) == None


from python_code import MySQL_NamedElement

def test_MySQL_NamedElement___init__():
    assert MySQL_NamedElement.__init__(MySQL_NamedElement(''), '') == None

