from python_code import dom_BooleanExpression
from python_code import dom_FeatureCallExpression
from python_code import dom_PropertyCallExpression
from python_code import dom_VariableDeclarationExpression

def test_dom_BooleanExpression___init__():
    assert dom_BooleanExpression.__init__(dom_BooleanExpression(True, dom_BooleanExpression=dom_FeatureCallExpression(), dom_BooleanExpression49=dom_VariableDeclarationExpression(), dom_BooleanExpression44=dom_PropertyCallExpression()), False, dom_BooleanExpression=dom_FeatureCallExpression(), dom_BooleanExpression49=dom_VariableDeclarationExpression(), dom_BooleanExpression44=dom_PropertyCallExpression()) == None


from python_code import dom_IntegerExpression

def test_dom_IntegerExpression___init__():
    assert dom_IntegerExpression.__init__(dom_IntegerExpression(0), 0) == None


from python_code import dom_Annotation
from python_code import dom_EnumerationLiteralExpression
from python_code import dom_FOLMethodCallExpression
from python_code import dom_FormalParameterExpression
from python_code import dom_MethodCallExpression
from python_code import dom_ModelDeclarationParameter
from python_code import dom_ModelDeclarationStatement
from python_code import dom_ModelElementTypeExpression
from python_code import dom_NameExpression
from python_code import dom_OperationDefinition
from python_code import dom_Program
from python_code import dom_PropertyCallExpression
from python_code import dom_TransactionStatement
from python_code import dom_VariableDeclarationExpression

def test_dom_NameExpression___init__():
    assert dom_NameExpression.__init__(dom_NameExpression('', dom_NameExpression=dom_Program(), dom_NameExpression28=dom_EnumerationLiteralExpression(), dom_NameExpression37=dom_MethodCallExpression(), dom_NameExpression22=dom_EnumerationLiteralExpression(), dom_NameExpression25=dom_EnumerationLiteralExpression(), dom_NameExpression46=dom_VariableDeclarationExpression(), dom_NameExpression66=dom_OperationDefinition(), dom_NameExpression41=dom_PropertyCallExpression(), dom_NameExpression109=dom_ModelDeclarationStatement(), dom_NameExpression112=dom_ModelDeclarationStatement(), dom_NameExpression115=dom_ModelDeclarationStatement(), dom_NameExpression137=dom_Annotation(), dom_NameExpression125=dom_FOLMethodCallExpression(), dom_NameExpression159=dom_ModelDeclarationParameter(), dom_NameExpression169=dom_TransactionStatement(), dom_NameExpression172=dom_FormalParameterExpression(), dom_NameExpression184=dom_ModelElementTypeExpression(), dom_NameExpression187=dom_ModelElementTypeExpression()), '', dom_NameExpression=dom_Program(), dom_NameExpression28=dom_EnumerationLiteralExpression(), dom_NameExpression37=dom_MethodCallExpression(), dom_NameExpression22=dom_EnumerationLiteralExpression(), dom_NameExpression25=dom_EnumerationLiteralExpression(), dom_NameExpression46=dom_VariableDeclarationExpression(), dom_NameExpression66=dom_OperationDefinition(), dom_NameExpression41=dom_PropertyCallExpression(), dom_NameExpression109=dom_ModelDeclarationStatement(), dom_NameExpression112=dom_ModelDeclarationStatement(), dom_NameExpression115=dom_ModelDeclarationStatement(), dom_NameExpression137=dom_Annotation(), dom_NameExpression125=dom_FOLMethodCallExpression(), dom_NameExpression159=dom_ModelDeclarationParameter(), dom_NameExpression169=dom_TransactionStatement(), dom_NameExpression172=dom_FormalParameterExpression(), dom_NameExpression184=dom_ModelElementTypeExpression(), dom_NameExpression187=dom_ModelElementTypeExpression()) == None


from python_code import dom_RealExpression

def test_dom_RealExpression___init__():
    assert dom_RealExpression.__init__(dom_RealExpression(0.0), 0.0) == None


from python_code import dom_Import
from python_code import dom_ModelDeclarationParameter
from python_code import dom_NativeType
from python_code import dom_SimpleAnnotation
from python_code import dom_StringExpression

def test_dom_StringExpression___init__():
    assert dom_StringExpression.__init__(dom_StringExpression('', dom_StringExpression=dom_Import(), dom_StringExpression150=dom_NativeType(), dom_StringExpression162=dom_ModelDeclarationParameter(), dom_StringExpression141=dom_SimpleAnnotation()), '', dom_StringExpression=dom_Import(), dom_StringExpression150=dom_NativeType(), dom_StringExpression162=dom_ModelDeclarationParameter(), dom_StringExpression141=dom_SimpleAnnotation()) == None

