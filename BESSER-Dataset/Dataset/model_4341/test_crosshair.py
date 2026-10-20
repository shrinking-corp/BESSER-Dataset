from python_code import edu_ASTNode

def test_edu_ASTNode___init__():
    assert edu_ASTNode.__init__(edu_ASTNode()) == None

def test_edu_ASTNode_accept():
    assert edu_ASTNode.accept(edu_ASTNode(), '') == None


from python_code import edu_Addition

def test_edu_Addition___init__():
    assert edu_Addition.__init__(edu_Addition()) == None

def test_edu_Addition_accept():
    assert edu_Addition.accept(edu_Addition(), '') == None


from python_code import edu_Assertion

def test_edu_Assertion___init__():
    assert edu_Assertion.__init__(edu_Assertion()) == None

def test_edu_Assertion_accept():
    assert edu_Assertion.accept(edu_Assertion(), '') == None


from python_code import edu_Assumption

def test_edu_Assumption___init__():
    assert edu_Assumption.__init__(edu_Assumption()) == None

def test_edu_Assumption_accept():
    assert edu_Assumption.accept(edu_Assumption(), '') == None


from python_code import edu_BooleanLiteral

def test_edu_BooleanLiteral___init__():
    assert edu_BooleanLiteral.__init__(edu_BooleanLiteral(True), False) == None

def test_edu_BooleanLiteral_getValue():
    assert edu_BooleanLiteral.getValue(edu_BooleanLiteral(False)) == None

def test_edu_BooleanLiteral_accept():
    assert edu_BooleanLiteral.accept(edu_BooleanLiteral(False), 0) == None


from python_code import edu_BooleanType

def test_edu_BooleanType___init__():
    assert edu_BooleanType.__init__(edu_BooleanType()) == None

def test_edu_BooleanType_accept():
    assert edu_BooleanType.accept(edu_BooleanType(), '') == None


from python_code import edu_Conjunction

def test_edu_Conjunction___init__():
    assert edu_Conjunction.__init__(edu_Conjunction()) == None

def test_edu_Conjunction_accept():
    assert edu_Conjunction.accept(edu_Conjunction(), '') == None


from python_code import edu_Disjunction

def test_edu_Disjunction___init__():
    assert edu_Disjunction.__init__(edu_Disjunction()) == None

def test_edu_Disjunction_accept():
    assert edu_Disjunction.accept(edu_Disjunction(), '') == None


from python_code import edu_Division

def test_edu_Division___init__():
    assert edu_Division.__init__(edu_Division()) == None

def test_edu_Division_accept():
    assert edu_Division.accept(edu_Division(), '') == None


from python_code import edu_Equal

def test_edu_Equal___init__():
    assert edu_Equal.__init__(edu_Equal()) == None

def test_edu_Equal_accept():
    assert edu_Equal.accept(edu_Equal(), '') == None


from python_code import edu_Equivalence

def test_edu_Equivalence___init__():
    assert edu_Equivalence.__init__(edu_Equivalence()) == None

def test_edu_Equivalence_accept():
    assert edu_Equivalence.accept(edu_Equivalence(), '') == None


from python_code import edu_ExistsQuantifier

def test_edu_ExistsQuantifier___init__():
    assert edu_ExistsQuantifier.__init__(edu_ExistsQuantifier()) == None

def test_edu_ExistsQuantifier_accept():
    assert edu_ExistsQuantifier.accept(edu_ExistsQuantifier(), '') == None


from python_code import edu_ForAllQuantifier

def test_edu_ForAllQuantifier___init__():
    assert edu_ForAllQuantifier.__init__(edu_ForAllQuantifier()) == None

def test_edu_ForAllQuantifier_accept():
    assert edu_ForAllQuantifier.accept(edu_ForAllQuantifier(), '') == None


from python_code import edu_FunctionAnnotation

def test_edu_FunctionAnnotation___init__():
    assert edu_FunctionAnnotation.__init__(edu_FunctionAnnotation()) == None

def test_edu_FunctionAnnotation_accept():
    assert edu_FunctionAnnotation.accept(edu_FunctionAnnotation(), '') == None


from python_code import edu_Greater

def test_edu_Greater___init__():
    assert edu_Greater.__init__(edu_Greater()) == None

def test_edu_Greater_accept():
    assert edu_Greater.accept(edu_Greater(), '') == None


from python_code import edu_GreaterOrEqual

def test_edu_GreaterOrEqual___init__():
    assert edu_GreaterOrEqual.__init__(edu_GreaterOrEqual()) == None

def test_edu_GreaterOrEqual_accept():
    assert edu_GreaterOrEqual.accept(edu_GreaterOrEqual(), '') == None


from python_code import edu_GuardAssertion

def test_edu_GuardAssertion___init__():
    assert edu_GuardAssertion.__init__(edu_GuardAssertion()) == None

def test_edu_GuardAssertion_accept():
    assert edu_GuardAssertion.accept(edu_GuardAssertion(), '') == None


from python_code import edu_Implication

def test_edu_Implication___init__():
    assert edu_Implication.__init__(edu_Implication()) == None

def test_edu_Implication_accept():
    assert edu_Implication.accept(edu_Implication(), '') == None


from python_code import edu_IntegerLiteral

def test_edu_IntegerLiteral___init__():
    assert edu_IntegerLiteral.__init__(edu_IntegerLiteral(''), '') == None

def test_edu_IntegerLiteral_accept():
    assert edu_IntegerLiteral.accept(edu_IntegerLiteral(''), 0) == None


from python_code import edu_IntegerType

def test_edu_IntegerType___init__():
    assert edu_IntegerType.__init__(edu_IntegerType()) == None

def test_edu_IntegerType_accept():
    assert edu_IntegerType.accept(edu_IntegerType(), '') == None


from python_code import edu_Less

def test_edu_Less___init__():
    assert edu_Less.__init__(edu_Less()) == None

def test_edu_Less_accept():
    assert edu_Less.accept(edu_Less(), '') == None


from python_code import edu_LessOrEqual

def test_edu_LessOrEqual___init__():
    assert edu_LessOrEqual.__init__(edu_LessOrEqual()) == None

def test_edu_LessOrEqual_accept():
    assert edu_LessOrEqual.accept(edu_LessOrEqual(), '') == None


from python_code import edu_Literal

def test_edu_Literal___init__():
    assert edu_Literal.__init__(edu_Literal()) == None

def test_edu_Literal_accept():
    assert edu_Literal.accept(edu_Literal(), '') == None


from python_code import edu_Minus

def test_edu_Minus___init__():
    assert edu_Minus.__init__(edu_Minus()) == None

def test_edu_Minus_accept():
    assert edu_Minus.accept(edu_Minus(), '') == None


from python_code import edu_Modulus

def test_edu_Modulus___init__():
    assert edu_Modulus.__init__(edu_Modulus()) == None

def test_edu_Modulus_accept():
    assert edu_Modulus.accept(edu_Modulus(), '') == None


from python_code import edu_Multiplication

def test_edu_Multiplication___init__():
    assert edu_Multiplication.__init__(edu_Multiplication()) == None

def test_edu_Multiplication_accept():
    assert edu_Multiplication.accept(edu_Multiplication(), '') == None


from python_code import edu_Negation

def test_edu_Negation___init__():
    assert edu_Negation.__init__(edu_Negation()) == None

def test_edu_Negation_accept():
    assert edu_Negation.accept(edu_Negation(), '') == None


from python_code import edu_Plus

def test_edu_Plus___init__():
    assert edu_Plus.__init__(edu_Plus()) == None

def test_edu_Plus_accept():
    assert edu_Plus.accept(edu_Plus(), '') == None


from python_code import edu_Sign

def test_edu_Sign___init__():
    assert edu_Sign.__init__(edu_Sign()) == None

def test_edu_Sign_accept():
    assert edu_Sign.accept(edu_Sign(), '') == None


from python_code import edu_Subtraction

def test_edu_Subtraction___init__():
    assert edu_Subtraction.__init__(edu_Subtraction()) == None

def test_edu_Subtraction_accept():
    assert edu_Subtraction.accept(edu_Subtraction(), '') == None


from python_code import edu_Unequal

def test_edu_Unequal___init__():
    assert edu_Unequal.__init__(edu_Unequal()) == None

def test_edu_Unequal_accept():
    assert edu_Unequal.accept(edu_Unequal(), '') == None


from python_code import edu_visitor_IASTNodeVisitor

def test_edu_visitor_IASTNodeVisitor___init__():
    assert edu_visitor_IASTNodeVisitor.__init__(edu_visitor_IASTNodeVisitor()) == None

def test_edu_visitor_IASTNodeVisitor_visit():
    assert edu_visitor_IASTNodeVisitor.visit(edu_visitor_IASTNodeVisitor(), '') == None

