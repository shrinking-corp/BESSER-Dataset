from python_code import sql_common_Comment
from python_code import sql_literal_NationalCharacterStringLiteral

def test_sql_common_Comment___init__():
    assert sql_common_Comment.__init__(sql_common_Comment('\x00\x00', Separator=sql_literal_NationalCharacterStringLiteral('', sql_literal_NationalCharacterStringLiteral=set())), '', Separator=sql_literal_NationalCharacterStringLiteral('', sql_literal_NationalCharacterStringLiteral=set())) == None


from python_code import sql_common_SchemaQualifiedName

def test_sql_common_SchemaQualifiedName___init__():
    assert sql_common_SchemaQualifiedName.__init__(sql_common_SchemaQualifiedName('', '', '\x00\x00'), '', '', '') == None


from python_code import sql_datatype_ApproximateNumericType

def test_sql_datatype_ApproximateNumericType___init__():
    assert sql_datatype_ApproximateNumericType.__init__(sql_datatype_ApproximateNumericType('', '\x00'), '\x00\x00', '') == None


from python_code import LargeObjectLength
from python_code import sql_datatype_BinaryLargeObjectStringType

def test_sql_datatype_BinaryLargeObjectStringType___init__():
    assert sql_datatype_BinaryLargeObjectStringType.__init__(sql_datatype_BinaryLargeObjectStringType('', sql_datatype_BinaryLargeObjectStringType=LargeObjectLength()), '', sql_datatype_BinaryLargeObjectStringType=LargeObjectLength()) == None


from python_code import SchemaQualifiedName
from python_code import sql_datatype_CharacterStringType

def test_sql_datatype_CharacterStringType___init__():
    assert sql_datatype_CharacterStringType.__init__(sql_datatype_CharacterStringType('', '\x00', sql_datatype_CharacterStringType6=SchemaQualifiedName(), sql_datatype_CharacterStringType=SchemaQualifiedName()), '\x00\x00', '', sql_datatype_CharacterStringType6=SchemaQualifiedName(), sql_datatype_CharacterStringType=SchemaQualifiedName()) == None


from python_code import sql_datatype_ExactNumericType

def test_sql_datatype_ExactNumericType___init__():
    assert sql_datatype_ExactNumericType.__init__(sql_datatype_ExactNumericType('', '', '\x00\x00'), '', '', '') == None


from python_code import sql_datatype_LargeObjectLength

def test_sql_datatype_LargeObjectLength___init__():
    assert sql_datatype_LargeObjectLength.__init__(sql_datatype_LargeObjectLength('', '', '\x00\x00'), '', '', '') == None


from python_code import SchemaQualifiedName
from python_code import sql_datatype_NationalCharacterStringType

def test_sql_datatype_NationalCharacterStringType___init__():
    assert sql_datatype_NationalCharacterStringType.__init__(sql_datatype_NationalCharacterStringType('', '\x00', sql_datatype_NationalCharacterStringType=SchemaQualifiedName()), '\x00\x00', '', sql_datatype_NationalCharacterStringType=SchemaQualifiedName()) == None


from python_code import sql_datatype_TimeType

def test_sql_datatype_TimeType___init__():
    assert sql_datatype_TimeType.__init__(sql_datatype_TimeType('', '\x00'), '\x00\x00', '') == None


from python_code import sql_datatype_TimestampType

def test_sql_datatype_TimestampType___init__():
    assert sql_datatype_TimestampType.__init__(sql_datatype_TimestampType('', '\x00'), '\x00\x00', '') == None


from python_code import sql_function_DatetimeValueFunction

def test_sql_function_DatetimeValueFunction___init__():
    assert sql_function_DatetimeValueFunction.__init__(sql_function_DatetimeValueFunction('', '\x00'), '\x00\x00', '') == None


from python_code import sql_literal_ApproximateNumericLiteral

def test_sql_literal_ApproximateNumericLiteral___init__():
    assert sql_literal_ApproximateNumericLiteral.__init__(sql_literal_ApproximateNumericLiteral(0.0), 0.0) == None


from python_code import sql_literal_BooleanLiteral

def test_sql_literal_BooleanLiteral___init__():
    assert sql_literal_BooleanLiteral.__init__(sql_literal_BooleanLiteral(''), '') == None


from python_code import sql_literal_DateLiteral

def test_sql_literal_DateLiteral___init__():
    assert sql_literal_DateLiteral.__init__(sql_literal_DateLiteral(''), '') == None


from python_code import sql_literal_ExactNumericLiteral

def test_sql_literal_ExactNumericLiteral___init__():
    assert sql_literal_ExactNumericLiteral.__init__(sql_literal_ExactNumericLiteral(''), '') == None


from python_code import sql_literal_NationalCharacterStringLiteral

def test_sql_literal_NationalCharacterStringLiteral___init__():
    assert sql_literal_NationalCharacterStringLiteral.__init__(sql_literal_NationalCharacterStringLiteral('', sql_literal_NationalCharacterStringLiteral=set()), '', sql_literal_NationalCharacterStringLiteral=set()) == None


from python_code import sql_literal_TimeLiteral

def test_sql_literal_TimeLiteral___init__():
    assert sql_literal_TimeLiteral.__init__(sql_literal_TimeLiteral(''), '') == None


from python_code import sql_literal_TimestampLiteral

def test_sql_literal_TimestampLiteral___init__():
    assert sql_literal_TimestampLiteral.__init__(sql_literal_TimestampLiteral(''), '') == None


from python_code import ColumnConstraint
from python_code import DataType
from python_code import DefaultOption
from python_code import SchemaQualifiedName
from python_code import sql_schema_Column
from python_code import sql_schema_TableElementList

def test_sql_schema_Column___init__():
    assert sql_schema_Column.__init__(sql_schema_Column('\x00', owner21=ColumnConstraint(), sql_schema_Column23=SchemaQualifiedName(), sql_schema_Column=DataType(), owner19=DefaultOption(), TableElement=sql_schema_TableElementList()), '', owner21=ColumnConstraint(), sql_schema_Column23=SchemaQualifiedName(), sql_schema_Column=DataType(), owner19=DefaultOption(), TableElement=sql_schema_TableElementList()) == None


from python_code import SchemaQualifiedName
from python_code import TableContentsSource
from python_code import sql_schema_TableDefinition

def test_sql_schema_TableDefinition___init__():
    assert sql_schema_TableDefinition.__init__(sql_schema_TableDefinition('', '', sql_schema_TableDefinition=SchemaQualifiedName(), owner=TableContentsSource()), '\x00', '', sql_schema_TableDefinition=SchemaQualifiedName(), owner=TableContentsSource()) == None


from python_code import TableDefinition
from python_code import sql_schema_TableReference

def test_sql_schema_TableReference___init__():
    assert sql_schema_TableReference.__init__(sql_schema_TableReference('', '\x00', sql_schema_TableReference=TableDefinition()), '\x00\x00', '', sql_schema_TableReference=TableDefinition()) == None


from python_code import sql_schema_UniqueConstraint

def test_sql_schema_UniqueConstraint___init__():
    assert sql_schema_UniqueConstraint.__init__(sql_schema_UniqueConstraint(''), '') == None

