from python_code import OCL_BooleanExp

def test_OCL_BooleanExp___init__():
    assert OCL_BooleanExp.__init__(OCL_BooleanExp(''), '') == None

from python_code import OCL_IntegerExp

def test_OCL_IntegerExp___init__():
    assert OCL_IntegerExp.__init__(OCL_IntegerExp(''), '') == None

from python_code import OCL_Iterator
from python_code import OCL_IteratorExp
from python_code import OCL_OclExpression

def test_OCL_IteratorExp___init__():
    assert OCL_IteratorExp.__init__(OCL_IteratorExp('', LoopExp=OCL_OclExpression(), LoopExp71=OCL_Iterator()), '', LoopExp=OCL_OclExpression(), LoopExp71=OCL_Iterator()) == None

from python_code import OCL_NavigationOrAttributeCallExp
from python_code import OCL_OclExpression

def test_OCL_NavigationOrAttributeCallExp___init__():
    assert OCL_NavigationOrAttributeCallExp.__init__(OCL_NavigationOrAttributeCallExp('', PropertyCallExp=OCL_OclExpression()), '', PropertyCallExp=OCL_OclExpression()) == None

from python_code import OCL_OclModel
from python_code import OclModel

def test_OCL_OclModel___init__():
    assert OCL_OclModel.__init__(OCL_OclModel('', model=OclModel(), model127=set(), metamodel=set()), '', model=OclModel(), model127=set(), metamodel=set()) == None

from python_code import OCL_RealExp

def test_OCL_RealExp___init__():
    assert OCL_RealExp.__init__(OCL_RealExp(''), '') == None

from python_code import OCL_StringExp

def test_OCL_StringExp___init__():
    assert OCL_StringExp.__init__(OCL_StringExp(''), '') == None

from python_code import OCL_TupleTypeAttribute
from python_code import OclType
from python_code import TupleType

def test_OCL_TupleTypeAttribute___init__():
    assert OCL_TupleTypeAttribute.__init__(OCL_TupleTypeAttribute('', tupleTypeAttribute=OclType(), attributes=TupleType()), '', tupleTypeAttribute=OclType(), attributes=TupleType()) == None

from python_code import ocl_constraints_LocatedElement

def test_ocl_constraints_LocatedElement___init__():
    assert ocl_constraints_LocatedElement.__init__(ocl_constraints_LocatedElement('', '', '\x00\x00'), '', '', '') == None

from python_code import ocl_constraints_Metaclass

def test_ocl_constraints_Metaclass___init__():
    assert ocl_constraints_Metaclass.__init__(ocl_constraints_Metaclass(''), '') == None

from python_code import ocl_constraints_OclConstraintsModel

def test_ocl_constraints_OclConstraintsModel___init__():
    assert ocl_constraints_OclConstraintsModel.__init__(ocl_constraints_OclConstraintsModel('', '', model_=set(), ocl_constraints_OclConstraintsModel=set()), '', '', model_=set(), ocl_constraints_OclConstraintsModel=set()) == None
