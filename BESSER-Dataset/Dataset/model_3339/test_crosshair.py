from python_code import JavaSimplified_Assignment
from python_code import JavaSimplified_Expression

def test_JavaSimplified_Assignment___init__():
    assert JavaSimplified_Assignment.__init__(JavaSimplified_Assignment('', JavaSimplified_Assignment2=JavaSimplified_Expression(), JavaSimplified_Assignment=JavaSimplified_Expression()), '', JavaSimplified_Assignment2=JavaSimplified_Expression(), JavaSimplified_Assignment=JavaSimplified_Expression()) == None


from python_code import JavaSimplified_Comment
from python_code import JavaSimplified_CommentStatement
from python_code import JavaSimplified_CommentedElement

def test_JavaSimplified_Comment___init__():
    assert JavaSimplified_Comment.__init__(JavaSimplified_Comment(True, JavaSimplified_Comment=JavaSimplified_CommentedElement(), JavaSimplified_Comment15=JavaSimplified_CommentStatement()), False, JavaSimplified_Comment=JavaSimplified_CommentedElement(), JavaSimplified_Comment15=JavaSimplified_CommentStatement()) == None


from python_code import JavaSimplified_Feature

def test_JavaSimplified_Feature___init__():
    assert JavaSimplified_Feature.__init__(JavaSimplified_Feature(''), '') == None


from python_code import JavaSimplified_Expression
from python_code import JavaSimplified_InfixExpression

def test_JavaSimplified_InfixExpression___init__():
    assert JavaSimplified_InfixExpression.__init__(JavaSimplified_InfixExpression('', JavaSimplified_InfixExpression=JavaSimplified_Expression(), JavaSimplified_InfixExpression34=JavaSimplified_Expression()), '', JavaSimplified_InfixExpression=JavaSimplified_Expression(), JavaSimplified_InfixExpression34=JavaSimplified_Expression()) == None


from python_code import JavaSimplified_Literal

def test_JavaSimplified_Literal___init__():
    assert JavaSimplified_Literal.__init__(JavaSimplified_Literal('', '\x00'), '\x00\x00', '') == None


from python_code import JavaSimplified_FieldAccess
from python_code import JavaSimplified_MethodCall
from python_code import JavaSimplified_MethodInvocation
from python_code import JavaSimplified_Name
from python_code import JavaSimplified_NamedElement

def test_JavaSimplified_Name___init__():
    assert JavaSimplified_Name.__init__(JavaSimplified_Name('', JavaSimplified_Name=JavaSimplified_FieldAccess(), JavaSimplified_Name60=JavaSimplified_MethodCall(), JavaSimplified_Name62=JavaSimplified_MethodInvocation(), JavaSimplified_Name67=JavaSimplified_NamedElement()), '', JavaSimplified_Name=JavaSimplified_FieldAccess(), JavaSimplified_Name60=JavaSimplified_MethodCall(), JavaSimplified_Name62=JavaSimplified_MethodInvocation(), JavaSimplified_Name67=JavaSimplified_NamedElement()) == None


from python_code import JavaSimplified_StringElement

def test_JavaSimplified_StringElement___init__():
    assert JavaSimplified_StringElement.__init__(JavaSimplified_StringElement(''), '') == None

