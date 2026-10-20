from python_code import vhdl_DesignUnit
from python_code import vhdl_Model
from python_code import vhdl_Module

def test_vhdl_DesignUnit___init__():
    assert vhdl_DesignUnit.__init__(vhdl_DesignUnit('', vhdl_DesignUnit=set(), vhdl_DesignUnit8=vhdl_Module(), vhdl_DesignUnit24=vhdl_Model()), '', vhdl_DesignUnit=set(), vhdl_DesignUnit8=vhdl_Module(), vhdl_DesignUnit24=vhdl_Model()) == None


from python_code import vhdl_VhdlObject

def test_vhdl_VhdlObject___init__():
    assert vhdl_VhdlObject.__init__(vhdl_VhdlObject(''), '') == None


from python_code import vhdl_declaration_FunctionDeclaration

def test_vhdl_declaration_FunctionDeclaration___init__():
    assert vhdl_declaration_FunctionDeclaration.__init__(vhdl_declaration_FunctionDeclaration(''), '') == None


from python_code import vhdl_declaration_GroupTemplateDeclaration

def test_vhdl_declaration_GroupTemplateDeclaration___init__():
    assert vhdl_declaration_GroupTemplateDeclaration.__init__(vhdl_declaration_GroupTemplateDeclaration(''), '') == None


from python_code import vhdl_declaration_SignalDeclaration

def test_vhdl_declaration_SignalDeclaration___init__():
    assert vhdl_declaration_SignalDeclaration.__init__(vhdl_declaration_SignalDeclaration('', '\x00'), '\x00\x00', '') == None


from python_code import vhdl_declaration_VariableDeclaration

def test_vhdl_declaration_VariableDeclaration___init__():
    assert vhdl_declaration_VariableDeclaration.__init__(vhdl_declaration_VariableDeclaration(False, '\x00'), False, '\x00') == None


from python_code import vhdl_expression_AddingExpression

def test_vhdl_expression_AddingExpression___init__():
    assert vhdl_expression_AddingExpression.__init__(vhdl_expression_AddingExpression(''), '') == None


from python_code import vhdl_expression_LogicalExpression

def test_vhdl_expression_LogicalExpression___init__():
    assert vhdl_expression_LogicalExpression.__init__(vhdl_expression_LogicalExpression(''), '') == None


from python_code import vhdl_expression_MultiplyingExpression

def test_vhdl_expression_MultiplyingExpression___init__():
    assert vhdl_expression_MultiplyingExpression.__init__(vhdl_expression_MultiplyingExpression(''), '') == None


from python_code import vhdl_expression_RangeExpression

def test_vhdl_expression_RangeExpression___init__():
    assert vhdl_expression_RangeExpression.__init__(vhdl_expression_RangeExpression(''), '') == None


from python_code import vhdl_expression_RelationalExpression

def test_vhdl_expression_RelationalExpression___init__():
    assert vhdl_expression_RelationalExpression.__init__(vhdl_expression_RelationalExpression(''), '') == None


from python_code import vhdl_expression_ShiftExpression

def test_vhdl_expression_ShiftExpression___init__():
    assert vhdl_expression_ShiftExpression.__init__(vhdl_expression_ShiftExpression(''), '') == None


from python_code import vhdl_statement_Statement

def test_vhdl_statement_Statement___init__():
    assert vhdl_statement_Statement.__init__(vhdl_statement_Statement(''), '') == None


from python_code import type_vhdl_Name
from python_code import vhdl_type_PhysicalTypeDefinitionSecondary

def test_vhdl_type_PhysicalTypeDefinitionSecondary___init__():
    assert vhdl_type_PhysicalTypeDefinitionSecondary.__init__(vhdl_type_PhysicalTypeDefinitionSecondary('', '\x00', vhdl_type_PhysicalTypeDefinitionSecondary=type_vhdl_Name()), '\x00\x00', '', vhdl_type_PhysicalTypeDefinitionSecondary=type_vhdl_Name()) == None

