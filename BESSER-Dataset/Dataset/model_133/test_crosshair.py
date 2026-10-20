from python_code import ast_DocumentationLine
from python_code import ast_EJBase

def test_ast_DocumentationLine___init__():
    assert ast_DocumentationLine.__init__(ast_DocumentationLine('', ast_DocumentationLine=ast_EJBase()), '', ast_DocumentationLine=ast_EJBase()) == None


from python_code import ast_EJElement

def test_ast_EJElement___init__():
    assert ast_EJElement.__init__(ast_EJElement(0, 0, 0, 0, '', ''), 0, 0, 0, 0, '\x00', '') == None


from python_code import ast_BehaviorFeature
from python_code import ast_ClassifierStatement
from python_code import ast_EnumLiteral
from python_code import ast_Identifier
from python_code import ast_NamedElement

def test_ast_Identifier___init__():
    assert ast_Identifier.__init__(ast_Identifier('', '', '\x00\x00', ast_Identifier77=ast_ClassifierStatement(), ast_Identifier=ast_BehaviorFeature(), ast_Identifier32=ast_EnumLiteral(), ast_Identifier273=ast_NamedElement()), '', '', '', ast_Identifier77=ast_ClassifierStatement(), ast_Identifier=ast_BehaviorFeature(), ast_Identifier32=ast_EnumLiteral(), ast_Identifier273=ast_NamedElement()) == None


from python_code import ast_JumpStatement
from python_code import ast_Label
from python_code import ast_LabeledStatement

def test_ast_Label___init__():
    assert ast_Label.__init__(ast_Label('', ast_Label=ast_JumpStatement(), ast_Label160=ast_LabeledStatement()), '', ast_Label=ast_JumpStatement(), ast_Label160=ast_LabeledStatement()) == None


from python_code import ast_Literal

def test_ast_Literal___init__():
    assert ast_Literal.__init__(ast_Literal(''), '') == None


from python_code import ast_ClassStatement
from python_code import ast_ClassifierStatement
from python_code import ast_Feature
from python_code import ast_FieldStatement
from python_code import ast_ImplemenationClassifierStatement
from python_code import ast_ImportStatement
from python_code import ast_LocalVarStatement
from python_code import ast_MethodStatement
from python_code import ast_Modifier
from python_code import ast_Parameter

def test_ast_Modifier___init__():
    assert ast_Modifier.__init__(ast_Modifier('', ast_Modifier65=ast_MethodStatement(), ast_Modifier68=ast_MethodStatement(), ast_Modifier71=ast_MethodStatement(), ast_Modifier74=ast_MethodStatement(), ast_Modifier88=ast_ClassStatement(), ast_Modifier96=ast_ImplemenationClassifierStatement(), ast_Modifier99=ast_ImplemenationClassifierStatement(), ast_Modifier102=ast_ImplemenationClassifierStatement(), ast_Modifier106=ast_ImportStatement(), ast_Modifier109=ast_ImportStatement(), ast_Modifier=ast_Parameter(), ast_Modifier37=ast_Feature(), ast_Modifier40=ast_Feature(), ast_Modifier43=ast_Feature(), ast_Modifier80=ast_ClassifierStatement(), ast_Modifier45=ast_FieldStatement(), ast_Modifier48=ast_FieldStatement(), ast_Modifier163=ast_LocalVarStatement()), '', ast_Modifier65=ast_MethodStatement(), ast_Modifier68=ast_MethodStatement(), ast_Modifier71=ast_MethodStatement(), ast_Modifier74=ast_MethodStatement(), ast_Modifier88=ast_ClassStatement(), ast_Modifier96=ast_ImplemenationClassifierStatement(), ast_Modifier99=ast_ImplemenationClassifierStatement(), ast_Modifier102=ast_ImplemenationClassifierStatement(), ast_Modifier106=ast_ImportStatement(), ast_Modifier109=ast_ImportStatement(), ast_Modifier=ast_Parameter(), ast_Modifier37=ast_Feature(), ast_Modifier40=ast_Feature(), ast_Modifier43=ast_Feature(), ast_Modifier80=ast_ClassifierStatement(), ast_Modifier45=ast_FieldStatement(), ast_Modifier48=ast_FieldStatement(), ast_Modifier163=ast_LocalVarStatement()) == None


from python_code import ast_PrimitiveType

def test_ast_PrimitiveType___init__():
    assert ast_PrimitiveType.__init__(ast_PrimitiveType(''), '') == None


from python_code import ast_SuperReference

def test_ast_SuperReference___init__():
    assert ast_SuperReference.__init__(ast_SuperReference(''), '') == None


from python_code import ast_ThisReference

def test_ast_ThisReference___init__():
    assert ast_ThisReference.__init__(ast_ThisReference(''), '') == None

