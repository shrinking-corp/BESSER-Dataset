from enum import Enum
from python_code import CollectionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(CollectionKind.set, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(CollectionKind.set, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(CollectionKind.set, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(CollectionKind.set, 0)

def test_Enum___new___2():
    assert Enum.__new__(CollectionKind.set, 'set') == CollectionKind.set

from python_code import ocl_expressions_BooleanLiteralExp

def test_ocl_expressions_BooleanLiteralExp___init__():
    assert ocl_expressions_BooleanLiteralExp.__init__(ocl_expressions_BooleanLiteralExp(''), '') == None

from python_code import ocl_expressions_CollectionLiteralExp

def test_ocl_expressions_CollectionLiteralExp___init__():
    assert ocl_expressions_CollectionLiteralExp.__init__(ocl_expressions_CollectionLiteralExp('', ocl_expressions_CollectionLiteralExp=set()), '', ocl_expressions_CollectionLiteralExp=set()) == None

from python_code import ocl_expressions_FeatureCallExp

def test_ocl_expressions_FeatureCallExp___init__():
    assert ocl_expressions_FeatureCallExp.__init__(ocl_expressions_FeatureCallExp(True), False) == None

from python_code import ocl_expressions_IntegerLiteralExp

def test_ocl_expressions_IntegerLiteralExp___init__():
    assert ocl_expressions_IntegerLiteralExp.__init__(ocl_expressions_IntegerLiteralExp(''), '') == None

from python_code import ocl_expressions_RealLiteralExp

def test_ocl_expressions_RealLiteralExp___init__():
    assert ocl_expressions_RealLiteralExp.__init__(ocl_expressions_RealLiteralExp(''), '') == None

from python_code import ocl_expressions_StringLiteralExp

def test_ocl_expressions_StringLiteralExp___init__():
    assert ocl_expressions_StringLiteralExp.__init__(ocl_expressions_StringLiteralExp(''), '') == None

from python_code import OCLExpression
from python_code import ocl_query_Query

def test_ocl_query_Query___init__():
    assert ocl_query_Query.__init__(ocl_query_Query('', ocl_query_Query=OCLExpression()), '', ocl_query_Query=OCLExpression()) == None

def test_ocl_query_Query_evaluate():
    assert ocl_query_Query.evaluate(ocl_query_Query('', ocl_query_Query=OCLExpression()), '') == None

def test_ocl_query_Query_queryText():
    assert ocl_query_Query.queryText(ocl_query_Query('', ocl_query_Query=OCLExpression())) == None

def test_ocl_query_Query_resultType():
    assert ocl_query_Query.resultType(ocl_query_Query('', ocl_query_Query=OCLExpression())) == None

def test_ocl_query_Query_select():
    assert ocl_query_Query.select(ocl_query_Query('', ocl_query_Query=OCLExpression()), '') == None

def test_ocl_query_Query_reject():
    assert ocl_query_Query.reject(ocl_query_Query('', ocl_query_Query=OCLExpression()), '') == None

def test_ocl_query_Query_check():
    assert ocl_query_Query.check(ocl_query_Query('', ocl_query_Query=OCLExpression()), '') == None

from python_code import ocl_types_CollectionType
from python_code import types_ocl_EClassifier

def test_ocl_types_CollectionType___init__():
    assert ocl_types_CollectionType.__init__(ocl_types_CollectionType('', ocl_types_CollectionType=types_ocl_EClassifier()), '', ocl_types_CollectionType=types_ocl_EClassifier()) == None

from python_code import OCLExpression
from python_code import ocl_uml_Constraint

def test_ocl_uml_Constraint___init__():
    assert ocl_uml_Constraint.__init__(ocl_uml_Constraint('', '', ocl_uml_Constraint=OCLExpression(), ocl_uml_Constraint71=set()), '', '', ocl_uml_Constraint=OCLExpression(), ocl_uml_Constraint71=set()) == None

from python_code import ocl_utilities_ASTNode

def test_ocl_utilities_ASTNode___init__():
    assert ocl_utilities_ASTNode.__init__(ocl_utilities_ASTNode(0, 0), 0, 0) == None

from python_code import ocl_utilities_CallingASTNode

def test_ocl_utilities_CallingASTNode___init__():
    assert ocl_utilities_CallingASTNode.__init__(ocl_utilities_CallingASTNode(0, 0), 0, 0) == None

from python_code import ocl_utilities_PredefinedType

def test_ocl_utilities_PredefinedType___init__():
    assert ocl_utilities_PredefinedType.__init__(ocl_utilities_PredefinedType()) == None

def test_ocl_utilities_PredefinedType_getOperationCodeFor():
    assert ocl_utilities_PredefinedType.getOperationCodeFor(ocl_utilities_PredefinedType(), '') == None

def test_ocl_utilities_PredefinedType_getCommonSupertype():
    assert ocl_utilities_PredefinedType.getCommonSupertype(ocl_utilities_PredefinedType(), '') == None

def test_ocl_utilities_PredefinedType_getOperations():
    assert ocl_utilities_PredefinedType.getOperations(ocl_utilities_PredefinedType()) == None

def test_ocl_utilities_PredefinedType_getResultTypeFor():
    assert ocl_utilities_PredefinedType.getResultTypeFor(ocl_utilities_PredefinedType(), '', '', '') == None

def test_ocl_utilities_PredefinedType_getRelationshipTo():
    assert ocl_utilities_PredefinedType.getRelationshipTo(ocl_utilities_PredefinedType(), '') == None

def test_ocl_utilities_PredefinedType_getOperationNameFor():
    assert ocl_utilities_PredefinedType.getOperationNameFor(ocl_utilities_PredefinedType(), '') == None

from python_code import ocl_utilities_TypedASTNode

def test_ocl_utilities_TypedASTNode___init__():
    assert ocl_utilities_TypedASTNode.__init__(ocl_utilities_TypedASTNode(0, 0), 0, 0) == None

from python_code import ocl_utilities_Visitable

def test_ocl_utilities_Visitable___init__():
    assert ocl_utilities_Visitable.__init__(ocl_utilities_Visitable()) == None

def test_ocl_utilities_Visitable_accept():
    assert ocl_utilities_Visitable.accept(ocl_utilities_Visitable(), '') == None
