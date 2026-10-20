from python_code import C_Abstractions_NamedElement

def test_C_Abstractions_NamedElement___init__():
    assert C_Abstractions_NamedElement.__init__(C_Abstractions_NamedElement(''), '') == None


from python_code import C_CompilationDirectiveDeclarations_Define

def test_C_CompilationDirectiveDeclarations_Define___init__():
    assert C_CompilationDirectiveDeclarations_Define.__init__(C_CompilationDirectiveDeclarations_Define(''), '') == None


from python_code import C_Declarations_ArrayDeclaration
from python_code import C_Main_Block
from python_code import Expressions_Construction
from python_code import Types_Type

def test_C_Declarations_ArrayDeclaration___init__():
    assert C_Declarations_ArrayDeclaration.__init__(C_Declarations_ArrayDeclaration('', C_Declarations_ArrayDeclaration=Expressions_Construction(), C_Declarations_ArrayDeclaration35=Types_Type(), Abstractions_BlockedElement=C_Main_Block()), '\x00', C_Declarations_ArrayDeclaration=Expressions_Construction(), C_Declarations_ArrayDeclaration35=Types_Type(), Abstractions_BlockedElement=C_Main_Block()) == None


from python_code import C_Declarations_Declaration

def test_C_Declarations_Declaration___init__():
    assert C_Declarations_Declaration.__init__(C_Declarations_Declaration(''), '') == None


from python_code import C_Declarations_PrototypeFunctionDeclaration
from python_code import Types_Type

def test_C_Declarations_PrototypeFunctionDeclaration___init__():
    assert C_Declarations_PrototypeFunctionDeclaration.__init__(C_Declarations_PrototypeFunctionDeclaration('', '', C_Declarations_PrototypeFunctionDeclaration=set(), C_Declarations_PrototypeFunctionDeclaration30=Types_Type()), '', '', C_Declarations_PrototypeFunctionDeclaration=set(), C_Declarations_PrototypeFunctionDeclaration30=Types_Type()) == None


from python_code import C_Declarations_VariableDeclaration

def test_C_Declarations_VariableDeclaration___init__():
    assert C_Declarations_VariableDeclaration.__init__(C_Declarations_VariableDeclaration('', '\x00'), '\x00\x00', '') == None


from python_code import C_Expressions_Access
from python_code import C_Expressions_BinaryArithmeticExpression

def test_C_Expressions_BinaryArithmeticExpression___init__():
    assert C_Expressions_BinaryArithmeticExpression.__init__(C_Expressions_BinaryArithmeticExpression('', C_Expressions_BinaryArithmeticExpression=C_Expressions_Access()), '', C_Expressions_BinaryArithmeticExpression=C_Expressions_Access()) == None


from python_code import C_Expressions_CharLiteral

def test_C_Expressions_CharLiteral___init__():
    assert C_Expressions_CharLiteral.__init__(C_Expressions_CharLiteral(''), '') == None


from python_code import C_Expressions_ComposedConditionalExpression

def test_C_Expressions_ComposedConditionalExpression___init__():
    assert C_Expressions_ComposedConditionalExpression.__init__(C_Expressions_ComposedConditionalExpression('', C_Expressions_ComposedConditionalExpression=set()), '', C_Expressions_ComposedConditionalExpression=set()) == None


from python_code import C_Expressions_ConditionalExpression

def test_C_Expressions_ConditionalExpression___init__():
    assert C_Expressions_ConditionalExpression.__init__(C_Expressions_ConditionalExpression(''), '') == None


from python_code import C_Expressions_Access
from python_code import C_Expressions_DisplacementLogicExpression

def test_C_Expressions_DisplacementLogicExpression___init__():
    assert C_Expressions_DisplacementLogicExpression.__init__(C_Expressions_DisplacementLogicExpression('', C_Expressions_DisplacementLogicExpression=C_Expressions_Access()), '', C_Expressions_DisplacementLogicExpression=C_Expressions_Access()) == None


from python_code import C_Expressions_DoubleLiteral

def test_C_Expressions_DoubleLiteral___init__():
    assert C_Expressions_DoubleLiteral.__init__(C_Expressions_DoubleLiteral(0.0), 0.0) == None


from python_code import C_Expressions_FloatLiteral

def test_C_Expressions_FloatLiteral___init__():
    assert C_Expressions_FloatLiteral.__init__(C_Expressions_FloatLiteral(0.0), 0.0) == None


from python_code import C_Expressions_IntLiteral

def test_C_Expressions_IntLiteral___init__():
    assert C_Expressions_IntLiteral.__init__(C_Expressions_IntLiteral(''), '') == None


from python_code import C_Expressions_ShortLiteral

def test_C_Expressions_ShortLiteral___init__():
    assert C_Expressions_ShortLiteral.__init__(C_Expressions_ShortLiteral(0), 0) == None


from python_code import C_Expressions_SimpleLogicExpression

def test_C_Expressions_SimpleLogicExpression___init__():
    assert C_Expressions_SimpleLogicExpression.__init__(C_Expressions_SimpleLogicExpression(''), '') == None


from python_code import C_Expressions_StringLiteral

def test_C_Expressions_StringLiteral___init__():
    assert C_Expressions_StringLiteral.__init__(C_Expressions_StringLiteral(''), '') == None


from python_code import C_Expressions_UnaryArithmeticExpression

def test_C_Expressions_UnaryArithmeticExpression___init__():
    assert C_Expressions_UnaryArithmeticExpression.__init__(C_Expressions_UnaryArithmeticExpression(''), '') == None


from python_code import C_Main_Function
from python_code import Main_Block
from python_code import Types_Type

def test_C_Main_Function___init__():
    assert C_Main_Function.__init__(C_Main_Function('', '', C_Main_Function7=Main_Block(), C_Main_Function10=set(), C_Main_Function=Types_Type()), '', '', C_Main_Function7=Main_Block(), C_Main_Function10=set(), C_Main_Function=Types_Type()) == None


from python_code import C_Main_Program

def test_C_Main_Program___init__():
    assert C_Main_Program.__init__(C_Main_Program('', C_Main_Program=set()), '', C_Main_Program=set()) == None

