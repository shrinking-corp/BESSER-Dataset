from python_code import VariableDeclaration
from python_code import atlext_ATL_CallableParameter
from python_code import atlext_OCL_Iterator

def test_atlext_ATL_CallableParameter___init__():
    assert atlext_ATL_CallableParameter.__init__(atlext_ATL_CallableParameter('', atlext_ATL_CallableParameter=VariableDeclaration()), '', atlext_ATL_CallableParameter=atlext_OCL_Iterator()) == None

from python_code import atlext_ATL_CalledRule

def test_atlext_ATL_CalledRule___init__():
    assert atlext_ATL_CalledRule.__init__(atlext_ATL_CalledRule('\x00\x00', '', atlext_ATL_CalledRule=set()), '', '', atlext_ATL_CalledRule=set()) == None

from python_code import Library
from python_code import OclFeatureDefinition
from python_code import Query
from python_code import atlext_ATL_Helper

def test_atlext_ATL_Helper___init__():
    assert atlext_ATL_Helper.__init__(atlext_ATL_Helper(False, '\x00', helpers=Query(), helpers14=Library(), atlext_ATL_Helper=OclFeatureDefinition()), False, '\x00', helpers=Query(), helpers14=Library(), atlext_ATL_Helper=OclFeatureDefinition()) == None

from python_code import atlext_ATL_LazyRule

def test_atlext_ATL_LazyRule___init__():
    assert atlext_ATL_LazyRule.__init__(atlext_ATL_LazyRule(''), '') == None

from python_code import Unit
from python_code import atlext_ATL_LibraryRef

def test_atlext_ATL_LibraryRef___init__():
    assert atlext_ATL_LibraryRef.__init__(atlext_ATL_LibraryRef('', libraries=Unit()), '', libraries=Unit()) == None

from python_code import atlext_ATL_LocatedElement

def test_atlext_ATL_LocatedElement___init__():
    assert atlext_ATL_LocatedElement.__init__(atlext_ATL_LocatedElement('', '', '', '', '', atlext_ATL_LocatedElement=set()), '', '', '', '\x00', '', atlext_ATL_LocatedElement=set()) == None

from python_code import Unit
from python_code import atlext_ATL_LibraryRef
from python_code import atlext_ATL_Module

def test_atlext_ATL_Module___init__():
    assert atlext_ATL_Module.__init__(atlext_ATL_Module('\x00', atlext_ATL_Module=set(), atlext_ATL_Module8=set(), atlext_ATL_Module11=set(), Unit=atlext_ATL_LibraryRef('', libraries=Unit())), '', atlext_ATL_Module=set(), atlext_ATL_Module8=set(), atlext_ATL_Module11=set(), Unit=atlext_ATL_LibraryRef('', libraries=Unit())) == None

from python_code import ActionBlock
from python_code import OutPattern
from python_code import Unit
from python_code import atlext_ATL_LibraryRef
from python_code import atlext_ATL_Module
from python_code import atlext_ATL_Rule

def test_atlext_ATL_Rule___init__():
    assert atlext_ATL_Rule.__init__(atlext_ATL_Rule('', rule=OutPattern(), rule19=ActionBlock(), rule21=set(), ModuleElement=atlext_ATL_Module('', atlext_ATL_Module=set(), atlext_ATL_Module8=set(), atlext_ATL_Module11=set(), Unit=atlext_ATL_LibraryRef('', libraries=Unit()))), '', rule=OutPattern(), rule19=ActionBlock(), rule21=set(), ModuleElement=atlext_ATL_Module('', atlext_ATL_Module=set(), atlext_ATL_Module8=set(), atlext_ATL_Module11=set(), Unit=atlext_ATL_LibraryRef('', libraries=Unit()))) == None

from python_code import InPattern
from python_code import RuleWithPattern
from python_code import atlext_ATL_ActionBlock
from python_code import atlext_ATL_OutPattern
from python_code import atlext_ATL_RuleVariableDeclaration
from python_code import atlext_ATL_RuleWithPattern

def test_atlext_ATL_RuleWithPattern___init__():
    assert atlext_ATL_RuleWithPattern.__init__(atlext_ATL_RuleWithPattern('', '', '', atlext_ATL_RuleWithPattern=InPattern(), superRule=set(), children=RuleWithPattern(), Rule68=atlext_ATL_RuleVariableDeclaration(), Rule71=atlext_ATL_ActionBlock(), Rule=atlext_ATL_OutPattern()), '', '', '', atlext_ATL_RuleWithPattern=InPattern(), superRule=set(), children=RuleWithPattern(), Rule68=atlext_ATL_RuleVariableDeclaration(), Rule71=atlext_ATL_ActionBlock(), Rule=atlext_ATL_OutPattern()) == None

from python_code import atlext_ATL_StringToStringMap

def test_atlext_ATL_StringToStringMap___init__():
    assert atlext_ATL_StringToStringMap.__init__(atlext_ATL_StringToStringMap('', '\x00'), '\x00\x00', '') == None

from python_code import atlext_ATL_Unit

def test_atlext_ATL_Unit___init__():
    assert atlext_ATL_Unit.__init__(atlext_ATL_Unit('', unit=set()), '', unit=set()) == None

from python_code import atlext_OCL_BooleanExp

def test_atlext_OCL_BooleanExp___init__():
    assert atlext_OCL_BooleanExp.__init__(atlext_OCL_BooleanExp(''), '') == None

from python_code import atlext_OCL_IntegerExp

def test_atlext_OCL_IntegerExp___init__():
    assert atlext_OCL_IntegerExp.__init__(atlext_OCL_IntegerExp(''), '') == None

from python_code import Attribute
from python_code import CollectionExp
from python_code import IfExp
from python_code import LetExp
from python_code import LoopExp
from python_code import OclType
from python_code import Operation
from python_code import OperationCallExp
from python_code import PropertyCallExp
from python_code import VariableDeclaration
from python_code import atlext_OCL_Iterator
from python_code import atlext_OCL_IteratorExp
from python_code import atlext_OCL_OclExpression

def test_atlext_OCL_IteratorExp___init__():
    assert atlext_OCL_IteratorExp.__init__(atlext_OCL_IteratorExp('', LoopExp=atlext_OCL_OclExpression('', body115=Operation(), condition=IfExp(), initExpression119=Attribute(), oclExpression=OclType(), elseExpression=IfExp(), source=PropertyCallExp(), elements106=CollectionExp(), in_=LetExp(), body=LoopExp(), arguments=OperationCallExp(), initExpression=VariableDeclaration(), thenExpression=IfExp()), LoopExp167=atlext_OCL_Iterator()), '', LoopExp=atlext_OCL_OclExpression('', body115=Operation(), condition=IfExp(), initExpression119=Attribute(), oclExpression=OclType(), elseExpression=IfExp(), source=PropertyCallExp(), elements106=CollectionExp(), in_=LetExp(), body=LoopExp(), arguments=OperationCallExp(), initExpression=VariableDeclaration(), thenExpression=IfExp()), LoopExp167=atlext_OCL_Iterator()) == None

from python_code import Attribute
from python_code import CollectionExp
from python_code import IfExp
from python_code import LetExp
from python_code import LoopExp
from python_code import OclType
from python_code import Operation
from python_code import OperationCallExp
from python_code import PropertyCallExp
from python_code import VariableDeclaration
from python_code import atlext_OCL_OclExpression

def test_atlext_OCL_OclExpression___init__():
    assert atlext_OCL_OclExpression.__init__(atlext_OCL_OclExpression('', body115=Operation(), condition=IfExp(), initExpression119=Attribute(), oclExpression=OclType(), elseExpression=IfExp(), source=PropertyCallExp(), elements106=CollectionExp(), in_=LetExp(), body=LoopExp(), arguments=OperationCallExp(), initExpression=VariableDeclaration(), thenExpression=IfExp()), '', body115=Operation(), condition=IfExp(), initExpression119=Attribute(), oclExpression=OclType(), elseExpression=IfExp(), source=PropertyCallExp(), elements106=CollectionExp(), in_=LetExp(), body=LoopExp(), arguments=OperationCallExp(), initExpression=VariableDeclaration(), thenExpression=IfExp()) == None

from python_code import OclModel
from python_code import atlext_OCL_OclModel

def test_atlext_OCL_OclModel___init__():
    assert atlext_OCL_OclModel.__init__(atlext_OCL_OclModel('', model=OclModel(), model223=set(), metamodel=set()), '', model=OclModel(), model223=set(), metamodel=set()) == None
