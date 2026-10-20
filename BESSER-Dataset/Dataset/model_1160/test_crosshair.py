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
    assert OCL_IteratorExp.__init__(OCL_IteratorExp('', LoopExp=OCL_OclExpression(), LoopExp87=OCL_Iterator()), '', LoopExp=OCL_OclExpression(), LoopExp87=OCL_Iterator()) == None


from python_code import OCL_NavigationOrAttributeCallExp
from python_code import OCL_OclExpression

def test_OCL_NavigationOrAttributeCallExp___init__():
    assert OCL_NavigationOrAttributeCallExp.__init__(OCL_NavigationOrAttributeCallExp('', PropertyCallExp=OCL_OclExpression()), '', PropertyCallExp=OCL_OclExpression()) == None


from python_code import OCL_OclModel
from python_code import OclModel

def test_OCL_OclModel___init__():
    assert OCL_OclModel.__init__(OCL_OclModel('', model=OclModel(), model143=set(), metamodel=set()), '', model=OclModel(), model143=set(), metamodel=set()) == None


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


from python_code import ConceptMetaclass
from python_code import ConcreteMetaclass
from python_code import genericity_dsl_BaseFeatureBinding
from python_code import genericity_dsl_BindingModel

def test_genericity_dsl_BaseFeatureBinding___init__():
    assert genericity_dsl_BaseFeatureBinding.__init__(genericity_dsl_BaseFeatureBinding('', genericity_dsl_BaseFeatureBinding=ConceptMetaclass(), genericity_dsl_BaseFeatureBinding13=ConcreteMetaclass(), ConceptBinding=genericity_dsl_BindingModel('\x00', '', model_=set(), model_2=set(), genericity_dsl_BindingModel=set())), '', genericity_dsl_BaseFeatureBinding=ConceptMetaclass(), genericity_dsl_BaseFeatureBinding13=ConcreteMetaclass(), ConceptBinding=genericity_dsl_BindingModel('', '', model_=set(), model_2=set(), genericity_dsl_BindingModel=set())) == None


from python_code import genericity_dsl_BindingModel

def test_genericity_dsl_BindingModel___init__():
    assert genericity_dsl_BindingModel.__init__(genericity_dsl_BindingModel('', '', model_=set(), model_2=set(), genericity_dsl_BindingModel=set()), '', '', model_=set(), model_2=set(), genericity_dsl_BindingModel=set()) == None


from python_code import BindingModel
from python_code import genericity_dsl_ConceptBinding

def test_genericity_dsl_ConceptBinding___init__():
    assert genericity_dsl_ConceptBinding.__init__(genericity_dsl_ConceptBinding('', bindings=BindingModel()), '', bindings=BindingModel()) == None


from python_code import genericity_dsl_LocatedElement

def test_genericity_dsl_LocatedElement___init__():
    assert genericity_dsl_LocatedElement.__init__(genericity_dsl_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import genericity_dsl_Metaclass

def test_genericity_dsl_Metaclass___init__():
    assert genericity_dsl_Metaclass.__init__(genericity_dsl_Metaclass(''), '') == None


from python_code import genericity_dsl_RenamingFeatureBinding

def test_genericity_dsl_RenamingFeatureBinding___init__():
    assert genericity_dsl_RenamingFeatureBinding.__init__(genericity_dsl_RenamingFeatureBinding(''), '') == None

