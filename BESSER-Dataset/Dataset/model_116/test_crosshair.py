from enum import Enum
from python_code import Visibility
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Visibility.PUBLIC, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Visibility.PUBLIC, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Visibility.PUBLIC, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Visibility.PUBLIC, 0)

def test_Enum___new___2():
    assert Enum.__new__(Visibility.PUBLIC, 'PUBLIC') == Visibility.PUBLIC

from python_code import dsl_BreakStatement
from python_code import dsl_Statement

def test_dsl_BreakStatement___init__():
    assert dsl_BreakStatement.__init__(dsl_BreakStatement('', dsl_BreakStatement=dsl_Statement()), '', dsl_BreakStatement=dsl_Statement()) == None

from python_code import dsl_ContinueStatement
from python_code import dsl_Statement

def test_dsl_ContinueStatement___init__():
    assert dsl_ContinueStatement.__init__(dsl_ContinueStatement('', dsl_ContinueStatement=dsl_Statement()), '', dsl_ContinueStatement=dsl_Statement()) == None

from python_code import dsl_Arguments
from python_code import dsl_ClassOrInterfaceBody
from python_code import dsl_EnumBody
from python_code import dsl_EnumConstant

def test_dsl_EnumConstant___init__():
    assert dsl_EnumConstant.__init__(dsl_EnumConstant('', dsl_EnumConstant=dsl_EnumBody(), dsl_EnumConstant46=dsl_Arguments(), dsl_EnumConstant48=dsl_ClassOrInterfaceBody()), '', dsl_EnumConstant=dsl_EnumBody(), dsl_EnumConstant46=dsl_Arguments(), dsl_EnumConstant48=dsl_ClassOrInterfaceBody()) == None

from python_code import dsl_Block
from python_code import dsl_ClassOrInterfaceBodyDeclaration
from python_code import dsl_Initializer

def test_dsl_Initializer___init__():
    assert dsl_Initializer.__init__(dsl_Initializer(True, dsl_Initializer=dsl_ClassOrInterfaceBodyDeclaration(), dsl_Initializer124=dsl_Block()), False, dsl_Initializer=dsl_ClassOrInterfaceBodyDeclaration(), dsl_Initializer124=dsl_Block()) == None

from python_code import dsl_LabeledStatement
from python_code import dsl_Statement

def test_dsl_LabeledStatement___init__():
    assert dsl_LabeledStatement.__init__(dsl_LabeledStatement('', dsl_LabeledStatement=dsl_Statement(), dsl_LabeledStatement344=dsl_Statement()), '', dsl_LabeledStatement=dsl_Statement(), dsl_LabeledStatement344=dsl_Statement()) == None

from python_code import dsl_MemberValue
from python_code import dsl_MemberValuePair
from python_code import dsl_MemberValuePairs

def test_dsl_MemberValuePair___init__():
    assert dsl_MemberValuePair.__init__(dsl_MemberValuePair('', dsl_MemberValuePair=dsl_MemberValuePairs(), dsl_MemberValuePair455=dsl_MemberValue()), '', dsl_MemberValuePair=dsl_MemberValuePairs(), dsl_MemberValuePair455=dsl_MemberValue()) == None

from python_code import dsl_TypeBound
from python_code import dsl_TypeParameter
from python_code import dsl_TypeParameters

def test_dsl_TypeParameter___init__():
    assert dsl_TypeParameter.__init__(dsl_TypeParameter('', dsl_TypeParameter=dsl_TypeParameters(), dsl_TypeParameter53=dsl_TypeBound()), '', dsl_TypeParameter=dsl_TypeParameters(), dsl_TypeParameter53=dsl_TypeBound()) == None
