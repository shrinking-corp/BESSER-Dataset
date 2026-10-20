from python_code import unql_Connection
from python_code import unql_Program

def test_unql_Connection___init__():
    assert unql_Connection.__init__(unql_Connection('\x00\x00', '', '', '', unql_Connection=unql_Program()), '', '', '', '', unql_Connection=unql_Program()) == None


from python_code import unql_Definition
from python_code import unql_Program

def test_unql_Definition___init__():
    assert unql_Definition.__init__(unql_Definition('', '\x00', unql_Definition=unql_Program()), '\x00\x00', '', unql_Definition=unql_Program()) == None


from python_code import unql_Program
from python_code import unql_Select

def test_unql_Select___init__():
    assert unql_Select.__init__(unql_Select('', '', '\x00\x00', unql_Select=unql_Program()), '', '', '', unql_Select=unql_Program()) == None

