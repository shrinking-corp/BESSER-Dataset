from python_code import go_ExpressionLinha
from python_code import go_binary_op

def test_go_binary_op___init__():
    assert go_binary_op.__init__(go_binary_op('', '', '\x00\x00', go_binary_op=go_ExpressionLinha()), '', '', '', go_binary_op=go_ExpressionLinha()) == None


from python_code import go_FieldName
from python_code import go_FunctionName
from python_code import go_IdentifierList
from python_code import go_Label
from python_code import go_MethodName
from python_code import go_PackageName
from python_code import go_QualifiedIdent
from python_code import go_Selector
from python_code import go_TypeName
from python_code import go_TypeNameLinha
from python_code import go_TypeSpec
from python_code import go_TypeSwitchGuard
from python_code import go_identifier

def test_go_identifier___init__():
    assert go_identifier.__init__(go_identifier('', '\x00', go_identifier=go_TypeName(), go_identifier17=go_TypeNameLinha(), go_identifier161=go_TypeSpec(), go_identifier153=go_IdentifierList(), go_identifier101=go_MethodName(), go_identifier273=go_FieldName(), go_identifier312=go_Selector(), go_identifier191=go_FunctionName(), go_identifier225=go_QualifiedIdent(), go_identifier407=go_Label(), go_identifier555=go_PackageName(), go_identifier461=go_TypeSwitchGuard()), '\x00\x00', '', go_identifier=go_TypeName(), go_identifier17=go_TypeNameLinha(), go_identifier161=go_TypeSpec(), go_identifier153=go_IdentifierList(), go_identifier101=go_MethodName(), go_identifier273=go_FieldName(), go_identifier312=go_Selector(), go_identifier191=go_FunctionName(), go_identifier225=go_QualifiedIdent(), go_identifier407=go_Label(), go_identifier555=go_PackageName(), go_identifier461=go_TypeSwitchGuard()) == None

