from enum import Enum
from python_code import AccessLevel
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessLevel.PUBLIC, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessLevel.PUBLIC, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessLevel.PUBLIC, '', 0, '') == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessLevel.PUBLIC, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessLevel.PUBLIC, 'PUBLIC') == AccessLevel.PUBLIC

from python_code import aS3_BoolConstant

def test_aS3_BoolConstant___init__():
    assert aS3_BoolConstant.__init__(aS3_BoolConstant(''), '') == None

from python_code import aS3_Import
from python_code import aS3_Imports

def test_aS3_Import___init__():
    assert aS3_Import.__init__(aS3_Import('', aS3_Import=aS3_Imports()), '', aS3_Import=aS3_Imports()) == None

from python_code import aS3_NumberConstant

def test_aS3_NumberConstant___init__():
    assert aS3_NumberConstant.__init__(aS3_NumberConstant(''), '') == None

from python_code import aS3_Imports
from python_code import aS3_Model
from python_code import aS3_Package

def test_aS3_Package___init__():
    assert aS3_Package.__init__(aS3_Package('', aS3_Package=aS3_Model(), aS3_Package9=aS3_Imports(), aS3_Package12=set(), aS3_Package14=set(), aS3_Package17=set()), '', aS3_Package=aS3_Model(), aS3_Package9=aS3_Imports(), aS3_Package12=set(), aS3_Package14=set(), aS3_Package17=set()) == None

from python_code import aS3_StringConstant

def test_aS3_StringConstant___init__():
    assert aS3_StringConstant.__init__(aS3_StringConstant(''), '') == None

from python_code import aS3_Uses
from python_code import aS3_directive

def test_aS3_Uses___init__():
    assert aS3_Uses.__init__(aS3_Uses('', '\x00', aS3_Uses=aS3_directive()), '\x00\x00', '', aS3_Uses=aS3_directive()) == None

from python_code import aS3_EObject
from python_code import aS3_VariableDeclaration
from python_code import aS3_assignmentExpression
from python_code import aS3_forInit

def test_aS3_VariableDeclaration___init__():
    assert aS3_VariableDeclaration.__init__(aS3_VariableDeclaration('', '\x00', aS3_VariableDeclaration=aS3_EObject(), aS3_VariableDeclaration102=aS3_assignmentExpression(), aS3_VariableDeclaration325=aS3_forInit()), '\x00\x00', '', aS3_VariableDeclaration=aS3_EObject(), aS3_VariableDeclaration102=aS3_assignmentExpression(), aS3_VariableDeclaration325=aS3_forInit()) == None

from python_code import aS3_XmlConstant

def test_aS3_XmlConstant___init__():
    assert aS3_XmlConstant.__init__(aS3_XmlConstant(''), '') == None

from python_code import aS3_Expression
from python_code import aS3_annotationField
from python_code import aS3_annotationFields

def test_aS3_annotationField___init__():
    assert aS3_annotationField.__init__(aS3_annotationField('', aS3_annotationField=aS3_annotationFields(), aS3_annotationField27=aS3_Expression()), '', aS3_annotationField=aS3_annotationFields(), aS3_annotationField27=aS3_Expression()) == None

from python_code import aS3_conditionalExpression

def test_aS3_conditionalExpression___init__():
    assert aS3_conditionalExpression.__init__(aS3_conditionalExpression('', aS3_conditionalExpression=set()), '', aS3_conditionalExpression=set()) == None

from python_code import aS3_fullNewSubexpression

def test_aS3_fullNewSubexpression___init__():
    assert aS3_fullNewSubexpression.__init__(aS3_fullNewSubexpression('', aS3_fullNewSubexpression=set(), aS3_fullNewSubexpression241=set(), aS3_fullNewSubexpression244=set()), '', aS3_fullNewSubexpression=set(), aS3_fullNewSubexpression241=set(), aS3_fullNewSubexpression244=set()) == None

from python_code import aS3_functionCommon
from python_code import aS3_functionExpression
from python_code import aS3_primaryExpression

def test_aS3_functionExpression___init__():
    assert aS3_functionExpression.__init__(aS3_functionExpression('', aS3_functionExpression=aS3_functionCommon(), aS3_functionExpression218=aS3_primaryExpression()), '', aS3_functionExpression=aS3_functionCommon(), aS3_functionExpression218=aS3_primaryExpression()) == None

from python_code import aS3_logicalAndExpression

def test_aS3_logicalAndExpression___init__():
    assert aS3_logicalAndExpression.__init__(aS3_logicalAndExpression('', aS3_logicalAndExpression=set()), '', aS3_logicalAndExpression=set()) == None

from python_code import aS3_conditionalSubExpression
from python_code import aS3_logicalOrExpression

def test_aS3_logicalOrExpression___init__():
    assert aS3_logicalOrExpression.__init__(aS3_logicalOrExpression('', aS3_logicalOrExpression=aS3_conditionalSubExpression()), '', aS3_logicalOrExpression=aS3_conditionalSubExpression()) == None

from python_code import aS3_namespaceName

def test_aS3_namespaceName___init__():
    assert aS3_namespaceName.__init__(aS3_namespaceName(''), '') == None

from python_code import aS3_qualifier
from python_code import aS3_simpleQualifiedIdentifier

def test_aS3_qualifier___init__():
    assert aS3_qualifier.__init__(aS3_qualifier('', aS3_qualifier=aS3_simpleQualifiedIdentifier()), '', aS3_qualifier=aS3_simpleQualifiedIdentifier()) == None

from python_code import aS3_RegexpConstant
from python_code import aS3_regexpLiteral

def test_aS3_regexpLiteral___init__():
    assert aS3_regexpLiteral.__init__(aS3_regexpLiteral('', aS3_regexpLiteral=aS3_RegexpConstant()), '', aS3_regexpLiteral=aS3_RegexpConstant()) == None

from python_code import aS3_unaryExpression
from python_code import aS3_unaryExpressionNotPlusMinus

def test_aS3_unaryExpressionNotPlusMinus___init__():
    assert aS3_unaryExpressionNotPlusMinus.__init__(aS3_unaryExpressionNotPlusMinus('', '\x00', aS3_unaryExpressionNotPlusMinus=aS3_unaryExpression()), '\x00\x00', '', aS3_unaryExpressionNotPlusMinus=aS3_unaryExpression()) == None
