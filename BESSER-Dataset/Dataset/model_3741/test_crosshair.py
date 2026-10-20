from python_code import genericsql_Check

def test_genericsql_Check___init__():
    assert genericsql_Check.__init__(genericsql_Check(''), '') == None


from python_code import genericsql_Constraint
from python_code import genericsql_Field
from python_code import genericsql_ForeignKey
from python_code import genericsql_PrimaryKey
from python_code import genericsql_Table

def test_genericsql_Field___init__():
    assert genericsql_Field.__init__(genericsql_Field(False, True, '', False, 0, '', '', fields=genericsql_Table(), Field=genericsql_Table(), genericsql_Field=genericsql_PrimaryKey(), genericsql_Field12=genericsql_ForeignKey(), genericsql_Field22=genericsql_Constraint()), False, False, '', False, 0, '', '', fields=genericsql_Table(), Field=genericsql_Table(), genericsql_Field=genericsql_PrimaryKey(), genericsql_Field12=genericsql_ForeignKey(), genericsql_Field22=genericsql_Constraint()) == None


from python_code import genericsql_NamedElement

def test_genericsql_NamedElement___init__():
    assert genericsql_NamedElement.__init__(genericsql_NamedElement('', '\x00'), '\x00\x00', '') == None

