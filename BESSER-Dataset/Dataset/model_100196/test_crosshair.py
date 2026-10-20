from python_code import SQLDDL_Column
from python_code import SQLDDL_Table
from python_code import Type
from python_code import Value

def test_SQLDDL_Column___init__():
    assert SQLDDL_Column.__init__(SQLDDL_Column('', '', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()), '', '', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()) == None


from python_code import SQLDDL_Column
from python_code import SQLDDL_IntegerVal
from python_code import SQLDDL_Parameter
from python_code import SQLDDL_Table
from python_code import Type
from python_code import Value

def test_SQLDDL_IntegerVal___init__():
    assert SQLDDL_IntegerVal.__init__(SQLDDL_IntegerVal('', Value=SQLDDL_Column('', '\x00', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()), Value23=SQLDDL_Parameter()), '', Value=SQLDDL_Column('', '', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()), Value23=SQLDDL_Parameter()) == None


from python_code import SQLDDL_Key
from python_code import SQLDDL_Table

def test_SQLDDL_Key___init__():
    assert SQLDDL_Key.__init__(SQLDDL_Key('\x00\x00', '', keys=set(), TableElement=SQLDDL_Table()), '', '', keys=set(), TableElement=SQLDDL_Table()) == None


from python_code import SQLDDL_LocatedElement

def test_SQLDDL_LocatedElement___init__():
    assert SQLDDL_LocatedElement.__init__(SQLDDL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import SQLDDL_NamedElement

def test_SQLDDL_NamedElement___init__():
    assert SQLDDL_NamedElement.__init__(SQLDDL_NamedElement(''), '') == None


from python_code import SQLDDL_Column
from python_code import SQLDDL_Parameter
from python_code import SQLDDL_StringVal
from python_code import SQLDDL_Table
from python_code import Type
from python_code import Value

def test_SQLDDL_StringVal___init__():
    assert SQLDDL_StringVal.__init__(SQLDDL_StringVal('', Value=SQLDDL_Column('', '\x00', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()), Value23=SQLDDL_Parameter()), '', Value=SQLDDL_Column('', '', referencedColumns=set(), SQLDDL_Column=Type(), SQLDDL_Column12=Value(), columns=set(), TableElement=SQLDDL_Table()), Value23=SQLDDL_Parameter()) == None


from python_code import SQLDDL_Type

def test_SQLDDL_Type___init__():
    assert SQLDDL_Type.__init__(SQLDDL_Type('', '\x00'), '\x00\x00', '') == None

