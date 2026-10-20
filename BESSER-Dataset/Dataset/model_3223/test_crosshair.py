from python_code import ansic_IdentifierListLinhaAction
from python_code import ansic_identifier_list_linha

def test_ansic_IdentifierListLinhaAction___init__():
    assert ansic_IdentifierListLinhaAction.__init__(ansic_IdentifierListLinhaAction('', ansic_IdentifierListLinhaAction=ansic_identifier_list_linha()), '', ansic_IdentifierListLinhaAction=ansic_identifier_list_linha()) == None


from python_code import ansic_PlusPlus

def test_ansic_PlusPlus___init__():
    assert ansic_PlusPlus.__init__(ansic_PlusPlus(''), '') == None


from python_code import ansic_DesignatorListLinhaAction
from python_code import ansic_conditional_expression
from python_code import ansic_designator
from python_code import ansic_designator_list

def test_ansic_designator___init__():
    assert ansic_designator.__init__(ansic_designator('', ansic_designator222=ansic_conditional_expression(), ansic_designator=ansic_designator_list(), ansic_designator540=ansic_DesignatorListLinhaAction()), '', ansic_designator222=ansic_conditional_expression(), ansic_designator=ansic_designator_list(), ansic_designator540=ansic_DesignatorListLinhaAction()) == None


from python_code import ansic_declarator
from python_code import ansic_direct_declarator
from python_code import ansic_direct_declarator_linha

def test_ansic_direct_declarator___init__():
    assert ansic_direct_declarator.__init__(ansic_direct_declarator('', ansic_direct_declarator=ansic_declarator(), ansic_direct_declarator111=ansic_direct_declarator_linha(), ansic_direct_declarator113=ansic_declarator()), '', ansic_direct_declarator=ansic_declarator(), ansic_direct_declarator111=ansic_direct_declarator_linha(), ansic_direct_declarator113=ansic_declarator()) == None


from python_code import ansic_enumeration_constant
from python_code import ansic_enumerator

def test_ansic_enumeration_constant___init__():
    assert ansic_enumeration_constant.__init__(ansic_enumeration_constant('', ansic_enumeration_constant=ansic_enumerator()), '', ansic_enumeration_constant=ansic_enumerator()) == None


from python_code import ansic_direct_declarator_complemento
from python_code import ansic_identifier_list
from python_code import ansic_identifier_list_linha

def test_ansic_identifier_list___init__():
    assert ansic_identifier_list.__init__(ansic_identifier_list('', ansic_identifier_list178=ansic_identifier_list_linha(), ansic_identifier_list=ansic_direct_declarator_complemento()), '', ansic_identifier_list178=ansic_identifier_list_linha(), ansic_identifier_list=ansic_direct_declarator_complemento()) == None


from python_code import ansic_expression
from python_code import ansic_jump_statement
from python_code import ansic_statement

def test_ansic_jump_statement___init__():
    assert ansic_jump_statement.__init__(ansic_jump_statement('\x00\x00', '', '', '', ansic_jump_statement325=ansic_expression(), ansic_jump_statement=ansic_statement()), '', '', '', '', ansic_jump_statement325=ansic_expression(), ansic_jump_statement=ansic_statement()) == None


from python_code import ansic_conditional_expression
from python_code import ansic_labeled_statement
from python_code import ansic_statement

def test_ansic_labeled_statement___init__():
    assert ansic_labeled_statement.__init__(ansic_labeled_statement('', ansic_labeled_statement=ansic_statement(), ansic_labeled_statement352=ansic_statement(), ansic_labeled_statement355=ansic_conditional_expression()), '', ansic_labeled_statement=ansic_statement(), ansic_labeled_statement352=ansic_statement(), ansic_labeled_statement355=ansic_conditional_expression()) == None


from python_code import ansic_PostfixExpressionLinhaAction
from python_code import ansic_argument_expression_list
from python_code import ansic_expression
from python_code import ansic_postfix_expression_complement

def test_ansic_postfix_expression_complement___init__():
    assert ansic_postfix_expression_complement.__init__(ansic_postfix_expression_complement('', ansic_postfix_expression_complement=ansic_expression(), ansic_postfix_expression_complement229=ansic_argument_expression_list(), ansic_postfix_expression_complement530=ansic_PostfixExpressionLinhaAction()), '', ansic_postfix_expression_complement=ansic_expression(), ansic_postfix_expression_complement229=ansic_argument_expression_list(), ansic_postfix_expression_complement530=ansic_PostfixExpressionLinhaAction()) == None


from python_code import ansic_string_ufcg

def test_ansic_string_ufcg___init__():
    assert ansic_string_ufcg.__init__(ansic_string_ufcg('', '\x00'), '\x00\x00', '') == None

