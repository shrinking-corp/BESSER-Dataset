from python_code import myDsl_IdentifierListLinhaAction
from python_code import myDsl_identifier_list_linha

def test_myDsl_IdentifierListLinhaAction___init__():
    assert myDsl_IdentifierListLinhaAction.__init__(myDsl_IdentifierListLinhaAction('', myDsl_IdentifierListLinhaAction=myDsl_identifier_list_linha()), '', myDsl_IdentifierListLinhaAction=myDsl_identifier_list_linha()) == None


from python_code import myDsl_PlusPlus

def test_myDsl_PlusPlus___init__():
    assert myDsl_PlusPlus.__init__(myDsl_PlusPlus(''), '') == None


from python_code import myDsl_additive_expression_complement
from python_code import myDsl_additive_expression_linha
from python_code import myDsl_multiplicative_expression

def test_myDsl_additive_expression_complement___init__():
    assert myDsl_additive_expression_complement.__init__(myDsl_additive_expression_complement('', '\x00', myDsl_additive_expression_complement=myDsl_additive_expression_linha(), myDsl_additive_expression_complement274=myDsl_multiplicative_expression()), '\x00\x00', '', myDsl_additive_expression_complement=myDsl_additive_expression_linha(), myDsl_additive_expression_complement274=myDsl_multiplicative_expression()) == None


from python_code import myDsl_DesignatorListLinhaAction
from python_code import myDsl_conditional_expression
from python_code import myDsl_designator
from python_code import myDsl_designator_list

def test_myDsl_designator___init__():
    assert myDsl_designator.__init__(myDsl_designator('', myDsl_designator222=myDsl_conditional_expression(), myDsl_designator=myDsl_designator_list(), myDsl_designator540=myDsl_DesignatorListLinhaAction()), '', myDsl_designator222=myDsl_conditional_expression(), myDsl_designator=myDsl_designator_list(), myDsl_designator540=myDsl_DesignatorListLinhaAction()) == None


from python_code import myDsl_declarator
from python_code import myDsl_direct_declarator
from python_code import myDsl_direct_declarator_linha

def test_myDsl_direct_declarator___init__():
    assert myDsl_direct_declarator.__init__(myDsl_direct_declarator('', myDsl_direct_declarator=myDsl_declarator(), myDsl_direct_declarator111=myDsl_direct_declarator_linha(), myDsl_direct_declarator113=myDsl_declarator()), '', myDsl_direct_declarator=myDsl_declarator(), myDsl_direct_declarator111=myDsl_direct_declarator_linha(), myDsl_direct_declarator113=myDsl_declarator()) == None


from python_code import myDsl_enumeration_constant
from python_code import myDsl_enumerator

def test_myDsl_enumeration_constant___init__():
    assert myDsl_enumeration_constant.__init__(myDsl_enumeration_constant('', myDsl_enumeration_constant=myDsl_enumerator()), '', myDsl_enumeration_constant=myDsl_enumerator()) == None


from python_code import myDsl_equality_expression_complement
from python_code import myDsl_equality_expression_linha
from python_code import myDsl_relational_expression

def test_myDsl_equality_expression_complement___init__():
    assert myDsl_equality_expression_complement.__init__(myDsl_equality_expression_complement('', '', '', '', '', '', myDsl_equality_expression_complement=myDsl_equality_expression_linha(), myDsl_equality_expression_complement310=myDsl_relational_expression()), '', '', '', '', '\x00', '', myDsl_equality_expression_complement=myDsl_equality_expression_linha(), myDsl_equality_expression_complement310=myDsl_relational_expression()) == None


from python_code import myDsl_direct_declarator_complemento
from python_code import myDsl_identifier_list
from python_code import myDsl_identifier_list_linha

def test_myDsl_identifier_list___init__():
    assert myDsl_identifier_list.__init__(myDsl_identifier_list('', myDsl_identifier_list=myDsl_direct_declarator_complemento(), myDsl_identifier_list178=myDsl_identifier_list_linha()), '', myDsl_identifier_list=myDsl_direct_declarator_complemento(), myDsl_identifier_list178=myDsl_identifier_list_linha()) == None


from python_code import myDsl_expression
from python_code import myDsl_jump_statement
from python_code import myDsl_statement

def test_myDsl_jump_statement___init__():
    assert myDsl_jump_statement.__init__(myDsl_jump_statement('\x00\x00', '', '', '', myDsl_jump_statement325=myDsl_expression(), myDsl_jump_statement=myDsl_statement()), '', '', '', '', myDsl_jump_statement325=myDsl_expression(), myDsl_jump_statement=myDsl_statement()) == None


from python_code import myDsl_conditional_expression
from python_code import myDsl_labeled_statement
from python_code import myDsl_statement

def test_myDsl_labeled_statement___init__():
    assert myDsl_labeled_statement.__init__(myDsl_labeled_statement('', myDsl_labeled_statement352=myDsl_statement(), myDsl_labeled_statement=myDsl_statement(), myDsl_labeled_statement355=myDsl_conditional_expression()), '', myDsl_labeled_statement352=myDsl_statement(), myDsl_labeled_statement=myDsl_statement(), myDsl_labeled_statement355=myDsl_conditional_expression()) == None


from python_code import myDsl_cast_expression
from python_code import myDsl_multiplicative_expression_complement
from python_code import myDsl_multiplicative_expression_linha

def test_myDsl_multiplicative_expression_complement___init__():
    assert myDsl_multiplicative_expression_complement.__init__(myDsl_multiplicative_expression_complement('', '', '\x00\x00', myDsl_multiplicative_expression_complement=myDsl_multiplicative_expression_linha(), myDsl_multiplicative_expression_complement262=myDsl_cast_expression()), '', '', '', myDsl_multiplicative_expression_complement=myDsl_multiplicative_expression_linha(), myDsl_multiplicative_expression_complement262=myDsl_cast_expression()) == None


from python_code import myDsl_PostfixExpressionLinhaAction
from python_code import myDsl_argument_expression_list
from python_code import myDsl_expression
from python_code import myDsl_postfix_expression_complement

def test_myDsl_postfix_expression_complement___init__():
    assert myDsl_postfix_expression_complement.__init__(myDsl_postfix_expression_complement('', myDsl_postfix_expression_complement=myDsl_expression(), myDsl_postfix_expression_complement229=myDsl_argument_expression_list(), myDsl_postfix_expression_complement530=myDsl_PostfixExpressionLinhaAction()), '', myDsl_postfix_expression_complement=myDsl_expression(), myDsl_postfix_expression_complement229=myDsl_argument_expression_list(), myDsl_postfix_expression_complement530=myDsl_PostfixExpressionLinhaAction()) == None


from python_code import myDsl_relational_expression_complement
from python_code import myDsl_shift_expression

def test_myDsl_relational_expression_complement___init__():
    assert myDsl_relational_expression_complement.__init__(myDsl_relational_expression_complement('\x00\x00', '', '', '', myDsl_relational_expression_complement=myDsl_shift_expression()), '', '', '', '', myDsl_relational_expression_complement=myDsl_shift_expression()) == None


from python_code import myDsl_additive_expression
from python_code import myDsl_relational_expression_linha
from python_code import myDsl_shift_expression_complement
from python_code import myDsl_shift_expression_linha

def test_myDsl_shift_expression_complement___init__():
    assert myDsl_shift_expression_complement.__init__(myDsl_shift_expression_complement('', '\x00', myDsl_shift_expression_complement294=myDsl_relational_expression_linha(), myDsl_shift_expression_complement=myDsl_shift_expression_linha(), myDsl_shift_expression_complement286=myDsl_additive_expression()), '\x00\x00', '', myDsl_shift_expression_complement294=myDsl_relational_expression_linha(), myDsl_shift_expression_complement=myDsl_shift_expression_linha(), myDsl_shift_expression_complement286=myDsl_additive_expression()) == None


from python_code import myDsl_string_dsl

def test_myDsl_string_dsl___init__():
    assert myDsl_string_dsl.__init__(myDsl_string_dsl('', '\x00'), '\x00\x00', '') == None

