from enum import Enum
from python_code import IteratorKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(IteratorKind.Parameter, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(IteratorKind.Parameter, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(IteratorKind.Parameter, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(IteratorKind.Iterator, 0)

def test_Enum___new___2():
    assert Enum.__new__(IteratorKind.Iterator, 'Iterator') == IteratorKind.Iterator

from python_code import basecs_AnnotationElementCS
from python_code import basecs_DetailCS

def test_basecs_DetailCS___init__():
    assert basecs_DetailCS.__init__(basecs_DetailCS('', basecs_DetailCS=basecs_AnnotationElementCS()), '', basecs_DetailCS=basecs_AnnotationElementCS()) == None

from python_code import basecs_DocumentationCS

def test_basecs_DocumentationCS___init__():
    assert basecs_DocumentationCS.__init__(basecs_DocumentationCS(''), '') == None

from python_code import basecs_EnumerationCS

def test_basecs_EnumerationCS___init__():
    assert basecs_EnumerationCS.__init__(basecs_EnumerationCS(basecs_EnumerationCS=set()), basecs_EnumerationCS=set()) == None

def test_basecs_EnumerationCS_ast():
    assert basecs_EnumerationCS.ast(basecs_EnumerationCS(basecs_EnumerationCS=set())) == None

from python_code import basecs_LambdaTypeCS
from python_code import basecs_TypedRefCS

def test_basecs_LambdaTypeCS___init__():
    assert basecs_LambdaTypeCS.__init__(basecs_LambdaTypeCS('', basecs_LambdaTypeCS=basecs_TypedRefCS(), basecs_LambdaTypeCS28=set(), basecs_LambdaTypeCS31=basecs_TypedRefCS()), '', basecs_LambdaTypeCS=basecs_TypedRefCS(), basecs_LambdaTypeCS28=set(), basecs_LambdaTypeCS31=basecs_TypedRefCS()) == None

from python_code import basecs_AnnotationCS
from python_code import basecs_ModelElementCS

def test_basecs_ModelElementCS___init__():
    assert basecs_ModelElementCS.__init__(basecs_ModelElementCS('\x00\x00', '', basecs_ModelElementCS=basecs_AnnotationCS(), basecs_ModelElementCS36=set()), '', '', basecs_ModelElementCS=basecs_AnnotationCS(), basecs_ModelElementCS36=set()) == None

from python_code import basecs_MultiplicityBoundsCS

def test_basecs_MultiplicityBoundsCS___init__():
    assert basecs_MultiplicityBoundsCS.__init__(basecs_MultiplicityBoundsCS(0, '\x00'), 0, '\x00') == None

from python_code import basecs_MultiplicityCS
from python_code import basecs_TypedRefCS

def test_basecs_MultiplicityCS___init__():
    assert basecs_MultiplicityCS.__init__(basecs_MultiplicityCS(basecs_MultiplicityCS=basecs_TypedRefCS()), basecs_MultiplicityCS=basecs_TypedRefCS()) == None

def test_basecs_MultiplicityCS_getUpper():
    assert basecs_MultiplicityCS.getUpper(basecs_MultiplicityCS(basecs_MultiplicityCS=basecs_TypedRefCS())) == None

def test_basecs_MultiplicityCS_getLower():
    assert basecs_MultiplicityCS.getLower(basecs_MultiplicityCS(basecs_MultiplicityCS=basecs_TypedRefCS())) == None

from python_code import basecs_MultiplicityStringCS

def test_basecs_MultiplicityStringCS___init__():
    assert basecs_MultiplicityStringCS.__init__(basecs_MultiplicityStringCS(''), '') == None

from python_code import basecs_NamedElementCS

def test_basecs_NamedElementCS___init__():
    assert basecs_NamedElementCS.__init__(basecs_NamedElementCS(''), '') == None

from python_code import basecs_PathElementWithURICS

def test_basecs_PathElementWithURICS___init__():
    assert basecs_PathElementWithURICS.__init__(basecs_PathElementWithURICS(''), '') == None

from python_code import basecs_PrimitiveTypeRefCS

def test_basecs_PrimitiveTypeRefCS___init__():
    assert basecs_PrimitiveTypeRefCS.__init__(basecs_PrimitiveTypeRefCS(''), '') == None

from python_code import basecs_TupleTypeCS

def test_basecs_TupleTypeCS___init__():
    assert basecs_TupleTypeCS.__init__(basecs_TupleTypeCS('', basecs_TupleTypeCS=set()), '', basecs_TupleTypeCS=set()) == None

from python_code import basecs_TypedElementCS
from python_code import basecs_TypedRefCS

def test_basecs_TypedElementCS___init__():
    assert basecs_TypedElementCS.__init__(basecs_TypedElementCS(False, '\x00', basecs_TypedElementCS=basecs_TypedRefCS()), False, '\x00', basecs_TypedElementCS=basecs_TypedRefCS()) == None
