from python_code import top_ATL_ActionBlock
from python_code import top_ATL_CalledRule
from python_code import top_ATL_OutPattern
from python_code import top_ATL_RuleVariableDeclaration

def test_top_ATL_CalledRule___init__():
    assert top_ATL_CalledRule.__init__(top_ATL_CalledRule('\x00\x00', '', top_ATL_CalledRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()), '', '', top_ATL_CalledRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()) == None


from python_code import InPattern
from python_code import MatchedRule
from python_code import top_ATL_ActionBlock
from python_code import top_ATL_InPattern
from python_code import top_ATL_LazyMatchedRule
from python_code import top_ATL_MatchedRule
from python_code import top_ATL_OutPattern
from python_code import top_ATL_RuleVariableDeclaration

def test_top_ATL_LazyMatchedRule___init__():
    assert top_ATL_LazyMatchedRule.__init__(top_ATL_LazyMatchedRule('', MatchedRule29=top_ATL_InPattern(), MatchedRule24=top_ATL_MatchedRule('\x00', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()), MatchedRule=top_ATL_MatchedRule('', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern())), '', MatchedRule29=top_ATL_InPattern(), MatchedRule24=top_ATL_MatchedRule('', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()), MatchedRule=top_ATL_MatchedRule('', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern())) == None


from python_code import Unit
from python_code import top_ATL_LibraryRef

def test_top_ATL_LibraryRef___init__():
    assert top_ATL_LibraryRef.__init__(top_ATL_LibraryRef('', libraries=Unit()), '', libraries=Unit()) == None


from python_code import top_ATL_LocatedElement

def test_top_ATL_LocatedElement___init__():
    assert top_ATL_LocatedElement.__init__(top_ATL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import InPattern
from python_code import MatchedRule
from python_code import top_ATL_ActionBlock
from python_code import top_ATL_MatchedRule
from python_code import top_ATL_OutPattern
from python_code import top_ATL_RuleVariableDeclaration

def test_top_ATL_MatchedRule___init__():
    assert top_ATL_MatchedRule.__init__(top_ATL_MatchedRule('', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()), '', '', '', children=MatchedRule(), rule21=InPattern(), superRule=set(), Rule68=top_ATL_ActionBlock(), Rule65=top_ATL_RuleVariableDeclaration(), Rule=top_ATL_OutPattern()) == None


from python_code import Unit
from python_code import top_ATL_LibraryRef
from python_code import top_ATL_Module

def test_top_ATL_Module___init__():
    assert top_ATL_Module.__init__(top_ATL_Module('\x00', top_ATL_Module7=set(), module=set(), top_ATL_Module=set(), Unit=top_ATL_LibraryRef('', libraries=Unit())), '', top_ATL_Module7=set(), module=set(), top_ATL_Module=set(), Unit=top_ATL_LibraryRef('', libraries=Unit())) == None


from python_code import ActionBlock
from python_code import OutPattern
from python_code import Unit
from python_code import top_ATL_LibraryRef
from python_code import top_ATL_Module
from python_code import top_ATL_Rule

def test_top_ATL_Rule___init__():
    assert top_ATL_Rule.__init__(top_ATL_Rule('', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=top_ATL_Module('', top_ATL_Module7=set(), module=set(), top_ATL_Module=set(), Unit=top_ATL_LibraryRef('', libraries=Unit()))), '', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=top_ATL_Module('', top_ATL_Module7=set(), module=set(), top_ATL_Module=set(), Unit=top_ATL_LibraryRef('', libraries=Unit()))) == None


from python_code import top_ATL_Unit

def test_top_ATL_Unit___init__():
    assert top_ATL_Unit.__init__(top_ATL_Unit('', unit=set()), '', unit=set()) == None


from python_code import top_OCL_BooleanExp

def test_top_OCL_BooleanExp___init__():
    assert top_OCL_BooleanExp.__init__(top_OCL_BooleanExp(''), '') == None


from python_code import top_OCL_IntegerExp

def test_top_OCL_IntegerExp___init__():
    assert top_OCL_IntegerExp.__init__(top_OCL_IntegerExp(''), '') == None


from python_code import top_OCL_Iterator
from python_code import top_OCL_IteratorExp
from python_code import top_OCL_OclExpression

def test_top_OCL_IteratorExp___init__():
    assert top_OCL_IteratorExp.__init__(top_OCL_IteratorExp('', LoopExp154=top_OCL_Iterator(), LoopExp=top_OCL_OclExpression()), '', LoopExp154=top_OCL_Iterator(), LoopExp=top_OCL_OclExpression()) == None


from python_code import top_OCL_NavigationOrAttributeCallExp
from python_code import top_OCL_OclExpression

def test_top_OCL_NavigationOrAttributeCallExp___init__():
    assert top_OCL_NavigationOrAttributeCallExp.__init__(top_OCL_NavigationOrAttributeCallExp('', PropertyCallExp=top_OCL_OclExpression()), '', PropertyCallExp=top_OCL_OclExpression()) == None


from python_code import OclModel
from python_code import top_OCL_OclModel

def test_top_OCL_OclModel___init__():
    assert top_OCL_OclModel.__init__(top_OCL_OclModel('', model=OclModel(), model213=set(), metamodel=set()), '', model=OclModel(), model213=set(), metamodel=set()) == None


from python_code import top_OCL_OclExpression
from python_code import top_OCL_OperationCallExp

def test_top_OCL_OperationCallExp___init__():
    assert top_OCL_OperationCallExp.__init__(top_OCL_OperationCallExp('', parentOperation=set(), PropertyCallExp=top_OCL_OclExpression()), '', parentOperation=set(), PropertyCallExp=top_OCL_OclExpression()) == None


from python_code import top_OCL_RealExp

def test_top_OCL_RealExp___init__():
    assert top_OCL_RealExp.__init__(top_OCL_RealExp(''), '') == None


from python_code import top_OCL_StringExp

def test_top_OCL_StringExp___init__():
    assert top_OCL_StringExp.__init__(top_OCL_StringExp(''), '') == None


from python_code import OclType
from python_code import TupleType
from python_code import top_OCL_TupleTypeAttribute

def test_top_OCL_TupleTypeAttribute___init__():
    assert top_OCL_TupleTypeAttribute.__init__(top_OCL_TupleTypeAttribute('', tupleTypeAttribute=OclType(), attributes=TupleType()), '', tupleTypeAttribute=OclType(), attributes=TupleType()) == None

