from python_code import ddlDsl_AddTableConstraint

def test_ddlDsl_AddTableConstraint___init__():
    assert ddlDsl_AddTableConstraint.__init__(ddlDsl_AddTableConstraint(''), '') == None


from python_code import ddlDsl_Comment

def test_ddlDsl_Comment___init__():
    assert ddlDsl_Comment.__init__(ddlDsl_Comment(''), '') == None


from python_code import ddlDsl_Create

def test_ddlDsl_Create___init__():
    assert ddlDsl_Create.__init__(ddlDsl_Create(''), '') == None


from python_code import ddlDsl_CreateIndex
from python_code import ddlDsl_CreateTable

def test_ddlDsl_CreateIndex___init__():
    assert ddlDsl_CreateIndex.__init__(ddlDsl_CreateIndex('\x00\x00', False, ddlDsl_CreateIndex=ddlDsl_CreateTable(), ddlDsl_CreateIndex16=set()), '', True, ddlDsl_CreateIndex=ddlDsl_CreateTable(), ddlDsl_CreateIndex16=set()) == None


from python_code import ddlDsl_Drop

def test_ddlDsl_Drop___init__():
    assert ddlDsl_Drop.__init__(ddlDsl_Drop(''), '') == None


from python_code import ddlDsl_LargeObjectType

def test_ddlDsl_LargeObjectType___init__():
    assert ddlDsl_LargeObjectType.__init__(ddlDsl_LargeObjectType(0), 0) == None


from python_code import ddlDsl_Long

def test_ddlDsl_Long___init__():
    assert ddlDsl_Long.__init__(ddlDsl_Long(True), False) == None


from python_code import ddlDsl_NullableConstraint

def test_ddlDsl_NullableConstraint___init__():
    assert ddlDsl_NullableConstraint.__init__(ddlDsl_NullableConstraint(True), False) == None


from python_code import ddlDsl_Raw

def test_ddlDsl_Raw___init__():
    assert ddlDsl_Raw.__init__(ddlDsl_Raw(0), 0) == None


from python_code import ddlDsl_RowIdType

def test_ddlDsl_RowIdType___init__():
    assert ddlDsl_RowIdType.__init__(ddlDsl_RowIdType(0), 0) == None


from python_code import ddlDsl_SqlCharacter

def test_ddlDsl_SqlCharacter___init__():
    assert ddlDsl_SqlCharacter.__init__(ddlDsl_SqlCharacter(False, 0), False, 0) == None


from python_code import ddlDsl_SqlInterval

def test_ddlDsl_SqlInterval___init__():
    assert ddlDsl_SqlInterval.__init__(ddlDsl_SqlInterval(False, False, 0, 0), False, False, 0, 0) == None


from python_code import ddlDsl_SqlNumber

def test_ddlDsl_SqlNumber___init__():
    assert ddlDsl_SqlNumber.__init__(ddlDsl_SqlNumber(False, 0, 0), False, 0, 0) == None


from python_code import ddlDsl_SqlTimeStamp

def test_ddlDsl_SqlTimeStamp___init__():
    assert ddlDsl_SqlTimeStamp.__init__(ddlDsl_SqlTimeStamp(0), 0) == None


from python_code import ddlDsl_CreateTable
from python_code import ddlDsl_TableProperty

def test_ddlDsl_TableProperty___init__():
    assert ddlDsl_TableProperty.__init__(ddlDsl_TableProperty('', ddlDsl_TableProperty=ddlDsl_CreateTable()), '', ddlDsl_TableProperty=ddlDsl_CreateTable()) == None

