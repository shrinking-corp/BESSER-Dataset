from python_code import lua_Expression
from python_code import lua_Expression_AccessMember

def test_lua_Expression_AccessMember___init__():
    assert lua_Expression_AccessMember.__init__(lua_Expression_AccessMember('', lua_Expression_AccessMember=lua_Expression()), '', lua_Expression_AccessMember=lua_Expression()) == None


from python_code import lua_Expression
from python_code import lua_Expression_CallMemberFunction
from python_code import lua_Functioncall_Arguments

def test_lua_Expression_CallMemberFunction___init__():
    assert lua_Expression_CallMemberFunction.__init__(lua_Expression_CallMemberFunction('', lua_Expression_CallMemberFunction=lua_Expression(), lua_Expression_CallMemberFunction165=lua_Functioncall_Arguments()), '', lua_Expression_CallMemberFunction=lua_Expression(), lua_Expression_CallMemberFunction165=lua_Functioncall_Arguments()) == None


from python_code import lua_Expression_Number

def test_lua_Expression_Number___init__():
    assert lua_Expression_Number.__init__(lua_Expression_Number(0.0), 0.0) == None


from python_code import lua_Expression_String

def test_lua_Expression_String___init__():
    assert lua_Expression_String.__init__(lua_Expression_String(''), '') == None


from python_code import lua_Expression_VariableName

def test_lua_Expression_VariableName___init__():
    assert lua_Expression_VariableName.__init__(lua_Expression_VariableName(''), '') == None


from python_code import lua_Field_AddEntryToTable

def test_lua_Field_AddEntryToTable___init__():
    assert lua_Field_AddEntryToTable.__init__(lua_Field_AddEntryToTable(''), '') == None


from python_code import lua_Expression
from python_code import lua_Functioncall_Arguments
from python_code import lua_Statement_CallMemberFunction

def test_lua_Statement_CallMemberFunction___init__():
    assert lua_Statement_CallMemberFunction.__init__(lua_Statement_CallMemberFunction('', lua_Statement_CallMemberFunction=lua_Expression(), lua_Statement_CallMemberFunction74=lua_Functioncall_Arguments()), '', lua_Statement_CallMemberFunction=lua_Expression(), lua_Statement_CallMemberFunction74=lua_Functioncall_Arguments()) == None


from python_code import lua_Block
from python_code import lua_Statement_For_Generic

def test_lua_Statement_For_Generic___init__():
    assert lua_Statement_For_Generic.__init__(lua_Statement_For_Generic('', lua_Statement_For_Generic44=lua_Block(), lua_Statement_For_Generic=set()), '', lua_Statement_For_Generic44=lua_Block(), lua_Statement_For_Generic=set()) == None


from python_code import lua_Block
from python_code import lua_Expression
from python_code import lua_Statement_For_Numeric

def test_lua_Statement_For_Numeric___init__():
    assert lua_Statement_For_Numeric.__init__(lua_Statement_For_Numeric('', lua_Statement_For_Numeric=lua_Expression(), lua_Statement_For_Numeric33=lua_Expression(), lua_Statement_For_Numeric36=lua_Expression(), lua_Statement_For_Numeric39=lua_Block()), '', lua_Statement_For_Numeric=lua_Expression(), lua_Statement_For_Numeric33=lua_Expression(), lua_Statement_For_Numeric36=lua_Expression(), lua_Statement_For_Numeric39=lua_Block()) == None


from python_code import lua_Statement_Local_Variable_Declaration

def test_lua_Statement_Local_Variable_Declaration___init__():
    assert lua_Statement_Local_Variable_Declaration.__init__(lua_Statement_Local_Variable_Declaration('', lua_Statement_Local_Variable_Declaration=set()), '', lua_Statement_Local_Variable_Declaration=set()) == None

