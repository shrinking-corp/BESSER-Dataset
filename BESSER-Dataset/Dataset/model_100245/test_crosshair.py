from python_code import BooleanValue
from python_code import Data

def test_BooleanValue___init__():
    assert BooleanValue.__init__(BooleanValue(True, ValueType=Data()), False, ValueType=Data()) == None


from python_code import ColOrRowElement

def test_ColOrRowElement___init__():
    assert ColOrRowElement.__init__(ColOrRowElement(0, False, 0), 0, False, 0) == None


from python_code import Column
from python_code import Table

def test_Column___init__():
    assert Column.__init__(Column(0, False, 0, Column=Table()), 0, False, 0, Column=Table()) == None


from python_code import Data
from python_code import NumberValue

def test_NumberValue___init__():
    assert NumberValue.__init__(NumberValue(0.0, ValueType=Data()), 0.0, ValueType=Data()) == None


from python_code import Data
from python_code import StringValue

def test_StringValue___init__():
    assert StringValue.__init__(StringValue('', ValueType=Data()), '', ValueType=Data()) == None


from python_code import TableElement

def test_TableElement___init__():
    assert TableElement.__init__(TableElement(0), 0) == None


from python_code import Table
from python_code import Workbook
from python_code import Worksheet

def test_Worksheet___init__():
    assert Worksheet.__init__(Worksheet('', Worksheet=Workbook(), Worksheet2=Table()), '', Worksheet=Workbook(), Worksheet2=Table()) == None

