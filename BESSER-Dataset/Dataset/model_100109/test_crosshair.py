from python_code import cassandra_AsciiType

def test_cassandra_AsciiType___init__():
    assert cassandra_AsciiType.__init__(cassandra_AsciiType(''), '') == None


from python_code import cassandra_BooleanType

def test_cassandra_BooleanType___init__():
    assert cassandra_BooleanType.__init__(cassandra_BooleanType(True), False) == None


from python_code import cassandra_BytesType

def test_cassandra_BytesType___init__():
    assert cassandra_BytesType.__init__(cassandra_BytesType(''), '') == None


from python_code import cassandra_CounterColumnType

def test_cassandra_CounterColumnType___init__():
    assert cassandra_CounterColumnType.__init__(cassandra_CounterColumnType(''), '') == None


from python_code import cassandra_DateType

def test_cassandra_DateType___init__():
    assert cassandra_DateType.__init__(cassandra_DateType(''), '') == None


from python_code import cassandra_DecimalType

def test_cassandra_DecimalType___init__():
    assert cassandra_DecimalType.__init__(cassandra_DecimalType(''), '') == None


from python_code import cassandra_DoubleType

def test_cassandra_DoubleType___init__():
    assert cassandra_DoubleType.__init__(cassandra_DoubleType(0.0), 0.0) == None


from python_code import cassandra_FloatType

def test_cassandra_FloatType___init__():
    assert cassandra_FloatType.__init__(cassandra_FloatType(0.0), 0.0) == None


from python_code import cassandra_IntegerType

def test_cassandra_IntegerType___init__():
    assert cassandra_IntegerType.__init__(cassandra_IntegerType(0), 0) == None


from python_code import cassandra_UTF8Type

def test_cassandra_UTF8Type___init__():
    assert cassandra_UTF8Type.__init__(cassandra_UTF8Type(''), '') == None


from python_code import cassandra_UUIDType

def test_cassandra_UUIDType___init__():
    assert cassandra_UUIDType.__init__(cassandra_UUIDType(''), '') == None

