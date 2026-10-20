from python_code import CWMRelationalData_Column
from python_code import ColumnSet
from python_code import NamedColumnSet
from python_code import SQLDataType

def test_CWMRelationalData_Column___init__():
    assert CWMRelationalData_Column.__init__(CWMRelationalData_Column('', '', '\x00', '\x00', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet()), '\x00', '', '', '', '', '\x00', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet()) == None


from python_code import CWMRelationalData_QueryExpression

def test_CWMRelationalData_QueryExpression___init__():
    assert CWMRelationalData_QueryExpression.__init__(CWMRelationalData_QueryExpression(''), '') == None


from python_code import CWMRelationalData_SQLDataType

def test_CWMRelationalData_SQLDataType___init__():
    assert CWMRelationalData_SQLDataType.__init__(CWMRelationalData_SQLDataType('', type=set()), '', type=set()) == None


from python_code import CWMRelationalData_Column
from python_code import CWMRelationalData_SQLDistinctType
from python_code import ColumnSet
from python_code import NamedColumnSet
from python_code import SQLDataType
from python_code import SQLSimpleType

def test_CWMRelationalData_SQLDistinctType___init__():
    assert CWMRelationalData_SQLDistinctType.__init__(CWMRelationalData_SQLDistinctType('\x00', '', '', sqlDistinctTypes=SQLSimpleType(), SQLDataType=CWMRelationalData_Column('\x00', '\x00', '', '', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())), '', '', '', sqlDistinctTypes=SQLSimpleType(), SQLDataType=CWMRelationalData_Column('', '', '', '', '', '\x00', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())) == None


from python_code import CWMRelationalData_Column
from python_code import CWMRelationalData_SQLSimpleType
from python_code import ColumnSet
from python_code import NamedColumnSet
from python_code import SQLDataType

def test_CWMRelationalData_SQLSimpleType___init__():
    assert CWMRelationalData_SQLSimpleType.__init__(CWMRelationalData_SQLSimpleType('', '\x01', '', '', '', '', sqlSimpleType=set(), SQLDataType=CWMRelationalData_Column('', '', '', '', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())), '', '', '', '', '', '', sqlSimpleType=set(), SQLDataType=CWMRelationalData_Column('', '', '', '', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())) == None


from python_code import CWMRelationalData_Column
from python_code import CWMRelationalData_Trigger
from python_code import CWMRelationalData_View
from python_code import ColumnSet
from python_code import NamedColumnSet
from python_code import QueryExpression
from python_code import SQLDataType

def test_CWMRelationalData_View___init__():
    assert CWMRelationalData_View.__init__(CWMRelationalData_View('', '', CWMRelationalData_View=QueryExpression(), NamedColumnSet17=CWMRelationalData_Trigger(), NamedColumnSet=CWMRelationalData_Column('', '', '', '', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())), '', '', CWMRelationalData_View=QueryExpression(), NamedColumnSet17=CWMRelationalData_Trigger(), NamedColumnSet=CWMRelationalData_Column('', '', '', '', '', '', constraintElements=set(), structuralFeatures=SQLDataType(), features=ColumnSet(), optionScopeColumn=NamedColumnSet())) == None

