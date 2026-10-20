from python_code import SQLDML_IntegerValueExp

def test_SQLDML_IntegerValueExp___init__():
    assert SQLDML_IntegerValueExp.__init__(SQLDML_IntegerValueExp(''), '') == None


from python_code import SQLDML_LocatedElement

def test_SQLDML_LocatedElement___init__():
    assert SQLDML_LocatedElement.__init__(SQLDML_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import SQLDML_NamedElement

def test_SQLDML_NamedElement___init__():
    assert SQLDML_NamedElement.__init__(SQLDML_NamedElement(''), '') == None


from python_code import SQLDML_OperationExp

def test_SQLDML_OperationExp___init__():
    assert SQLDML_OperationExp.__init__(SQLDML_OperationExp(''), '') == None


from python_code import SQLDML_StringValueExp

def test_SQLDML_StringValueExp___init__():
    assert SQLDML_StringValueExp.__init__(SQLDML_StringValueExp(''), '') == None


from python_code import SQLDML_Table

def test_SQLDML_Table___init__():
    assert SQLDML_Table.__init__(SQLDML_Table(''), '') == None


from python_code import QueryStmt
from python_code import SQLDML_SQLRoot
from python_code import SQLDML_ViewStatement

def test_SQLDML_ViewStatement___init__():
    assert SQLDML_ViewStatement.__init__(SQLDML_ViewStatement('\x00', SQLDML_ViewStatement3=QueryStmt(), SQLDML_ViewStatement=set(), Statement=SQLDML_SQLRoot()), '', SQLDML_ViewStatement3=QueryStmt(), SQLDML_ViewStatement=set(), Statement=SQLDML_SQLRoot()) == None

