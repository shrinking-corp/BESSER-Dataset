from python_code import ir_AbstractFunction
from python_code import ir_EFType

def test_ir_AbstractFunction___init__():
    assert ir_AbstractFunction.__init__(ir_AbstractFunction('', ir_AbstractFunction=ir_EFType()), '', ir_AbstractFunction=ir_EFType()) == None


from python_code import ir_Constraint
from python_code import ir_Specification

def test_ir_Constraint___init__():
    assert ir_Constraint.__init__(ir_Constraint('', ir_Constraint=ir_Specification()), '', ir_Constraint=ir_Specification()) == None


from python_code import ir_EFEnum
from python_code import ir_EFEnumLiteral

def test_ir_EFEnumLiteral___init__():
    assert ir_EFEnumLiteral.__init__(ir_EFEnumLiteral('', ir_EFEnumLiteral=ir_EFEnum()), '', ir_EFEnumLiteral=ir_EFEnum()) == None


from python_code import ir_EFPrimitiveType
from python_code import ir_Specification

def test_ir_EFPrimitiveType___init__():
    assert ir_EFPrimitiveType.__init__(ir_EFPrimitiveType('', ir_EFPrimitiveType=ir_Specification()), '', ir_EFPrimitiveType=ir_Specification()) == None


from python_code import ir_TypeRef
from python_code import ir_VariableDeclaration

def test_ir_VariableDeclaration___init__():
    assert ir_VariableDeclaration.__init__(ir_VariableDeclaration('', ir_VariableDeclaration=ir_TypeRef()), '', ir_VariableDeclaration=ir_TypeRef()) == None


from python_code import ir_ocl_BooleanLiteralExp

def test_ir_ocl_BooleanLiteralExp___init__():
    assert ir_ocl_BooleanLiteralExp.__init__(ir_ocl_BooleanLiteralExp(True), False) == None


from python_code import ir_ocl_CollectionCallExp

def test_ir_ocl_CollectionCallExp___init__():
    assert ir_ocl_CollectionCallExp.__init__(ir_ocl_CollectionCallExp(''), '') == None


from python_code import ir_ocl_IntegerLiteralExp

def test_ir_ocl_IntegerLiteralExp___init__():
    assert ir_ocl_IntegerLiteralExp.__init__(ir_ocl_IntegerLiteralExp(''), '') == None


from python_code import ir_ocl_IteratorExp

def test_ir_ocl_IteratorExp___init__():
    assert ir_ocl_IteratorExp.__init__(ir_ocl_IteratorExp(''), '') == None


from python_code import ir_ocl_OperationCallExp
from python_code import ocl_ir_OperationFeatureRef

def test_ir_ocl_OperationCallExp___init__():
    assert ir_ocl_OperationCallExp.__init__(ir_ocl_OperationCallExp('', ir_ocl_OperationCallExp=ocl_ir_OperationFeatureRef()), '', ir_ocl_OperationCallExp=ocl_ir_OperationFeatureRef()) == None


from python_code import OclExpression
from python_code import ir_ocl_IfExp
from python_code import ir_ocl_OperatorCallExp

def test_ir_ocl_OperatorCallExp___init__():
    assert ir_ocl_OperatorCallExp.__init__(ir_ocl_OperatorCallExp('', ir_ocl_OperatorCallExp=OclExpression()), '', ir_ocl_OperatorCallExp=ir_ocl_IfExp()) == None


from python_code import ir_ocl_PropertyCallExp
from python_code import ocl_ir_PropertyFeatureRef

def test_ir_ocl_PropertyCallExp___init__():
    assert ir_ocl_PropertyCallExp.__init__(ir_ocl_PropertyCallExp('', ir_ocl_PropertyCallExp=ocl_ir_PropertyFeatureRef()), '', ir_ocl_PropertyCallExp=ocl_ir_PropertyFeatureRef()) == None


from python_code import ir_ocl_RealLiteralExp

def test_ir_ocl_RealLiteralExp___init__():
    assert ir_ocl_RealLiteralExp.__init__(ir_ocl_RealLiteralExp(''), '') == None


from python_code import ir_ocl_StringLiteralExp

def test_ir_ocl_StringLiteralExp___init__():
    assert ir_ocl_StringLiteralExp.__init__(ir_ocl_StringLiteralExp(''), '') == None


from python_code import OclExpression
from python_code import ir_ocl_IfExp
from python_code import ir_ocl_TuplePart

def test_ir_ocl_TuplePart___init__():
    assert ir_ocl_TuplePart.__init__(ir_ocl_TuplePart('', ir_ocl_TuplePart=ir_ocl_IfExp()), '', ir_ocl_TuplePart=OclExpression()) == None


from python_code import OclExpression
from python_code import ir_ocl_AbstractOperationCallExp
from python_code import ir_ocl_CallExp
from python_code import ir_ocl_CollectionLiteralExp
from python_code import ir_ocl_IfExp
from python_code import ir_ocl_IterateExp
from python_code import ir_ocl_LetExp
from python_code import ir_ocl_LoopExp
from python_code import ir_ocl_OclDerivedProperty
from python_code import ir_ocl_OclInvariant
from python_code import ir_ocl_OclOperation
from python_code import ir_ocl_OperatorCallExp
from python_code import ir_ocl_TuplePart
from python_code import ir_ocl_UnsupportedExp
from python_code import ir_ocl_VarExp

def test_ir_ocl_UnsupportedExp___init__():
    assert ir_ocl_UnsupportedExp.__init__(ir_ocl_UnsupportedExp('', '', OclExpression=ir_ocl_OclInvariant(), OclExpression60=ir_ocl_CallExp(), OclExpression78=ir_ocl_IfExp(), OclExpression62=ir_ocl_AbstractOperationCallExp(), OclExpression68=ir_ocl_LoopExp(), OclExpression98=ir_ocl_TuplePart('', ir_ocl_TuplePart=ir_ocl_IfExp()), OclExpression55=ir_ocl_OclDerivedProperty(), OclExpression89=ir_ocl_LetExp(), OclExpression81=ir_ocl_IfExp(), OclExpression57=ir_ocl_OclOperation(), OclExpression86=ir_ocl_LetExp(), OclExpression103=ir_ocl_CollectionLiteralExp(), OclExpression75=ir_ocl_IfExp(), OclExpression91=ir_ocl_OperatorCallExp('', ir_ocl_OperatorCallExp=OclExpression()), OclExpression73=ir_ocl_IterateExp()), '', '', OclExpression=ir_ocl_OclInvariant(), OclExpression60=ir_ocl_CallExp(), OclExpression78=ir_ocl_IfExp(), OclExpression62=ir_ocl_AbstractOperationCallExp(), OclExpression68=ir_ocl_LoopExp(), OclExpression98=ir_ocl_TuplePart('', ir_ocl_TuplePart=ir_ocl_VarExp()), OclExpression55=ir_ocl_OclDerivedProperty(), OclExpression89=ir_ocl_LetExp(), OclExpression81=ir_ocl_IfExp(), OclExpression57=ir_ocl_OclOperation(), OclExpression86=ir_ocl_LetExp(), OclExpression103=ir_ocl_CollectionLiteralExp(), OclExpression75=ir_ocl_IfExp(), OclExpression91=ir_ocl_OperatorCallExp('', ir_ocl_OperatorCallExp=OclExpression()), OclExpression73=ir_ocl_IterateExp()) == None

