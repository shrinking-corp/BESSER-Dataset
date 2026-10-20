from python_code import ATL_ActionBlock
from python_code import ATL_CalledRule
from python_code import ATL_OutPattern
from python_code import ATL_RuleVariableDeclaration

def test_ATL_CalledRule___init__():
    assert ATL_CalledRule.__init__(ATL_CalledRule('\x00\x00', '', ATL_CalledRule=set(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), '', '', ATL_CalledRule=set(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()) == None


from python_code import ATL_ActionBlock
from python_code import ATL_InPattern
from python_code import ATL_LazyMatchedRule
from python_code import ATL_MatchedRule
from python_code import ATL_OutPattern
from python_code import ATL_RuleVariableDeclaration
from python_code import InPattern
from python_code import MatchedRule

def test_ATL_LazyMatchedRule___init__():
    assert ATL_LazyMatchedRule.__init__(ATL_LazyMatchedRule('', MatchedRule24=ATL_MatchedRule('', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), MatchedRule=ATL_MatchedRule('', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), MatchedRule29=ATL_InPattern()), '', MatchedRule24=ATL_MatchedRule('', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), MatchedRule=ATL_MatchedRule('', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), MatchedRule29=ATL_InPattern()) == None


from python_code import ATL_LibraryRef
from python_code import Unit

def test_ATL_LibraryRef___init__():
    assert ATL_LibraryRef.__init__(ATL_LibraryRef('', libraries=Unit()), '', libraries=Unit()) == None


from python_code import ATL_LocatedElement

def test_ATL_LocatedElement___init__():
    assert ATL_LocatedElement.__init__(ATL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import ATL_ActionBlock
from python_code import ATL_MatchedRule
from python_code import ATL_OutPattern
from python_code import ATL_RuleVariableDeclaration
from python_code import InPattern
from python_code import MatchedRule

def test_ATL_MatchedRule___init__():
    assert ATL_MatchedRule.__init__(ATL_MatchedRule('', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()), '', '', '', rule21=InPattern(), superRule=set(), children=MatchedRule(), Rule65=ATL_RuleVariableDeclaration(), Rule=ATL_OutPattern(), Rule68=ATL_ActionBlock()) == None


from python_code import ATL_LibraryRef
from python_code import ATL_Module
from python_code import Unit

def test_ATL_Module___init__():
    assert ATL_Module.__init__(ATL_Module('', ATL_Module=set(), ATL_Module7=set(), module=set(), Unit=ATL_LibraryRef('', libraries=Unit())), '', ATL_Module=set(), ATL_Module7=set(), module=set(), Unit=ATL_LibraryRef('', libraries=Unit())) == None


from python_code import ATL_LibraryRef
from python_code import ATL_Module
from python_code import ATL_Rule
from python_code import ActionBlock
from python_code import OutPattern
from python_code import Unit

def test_ATL_Rule___init__():
    assert ATL_Rule.__init__(ATL_Rule('', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=ATL_Module('', ATL_Module=set(), ATL_Module7=set(), module=set(), Unit=ATL_LibraryRef('', libraries=Unit()))), '', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=ATL_Module('', ATL_Module=set(), ATL_Module7=set(), module=set(), Unit=ATL_LibraryRef('', libraries=Unit()))) == None


from python_code import ATL_Unit

def test_ATL_Unit___init__():
    assert ATL_Unit.__init__(ATL_Unit('', unit=set()), '', unit=set()) == None


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
    assert OCL_IteratorExp.__init__(OCL_IteratorExp('', LoopExp=OCL_OclExpression(), LoopExp154=OCL_Iterator()), '', LoopExp=OCL_OclExpression(), LoopExp154=OCL_Iterator()) == None


from python_code import OCL_NavigationOrAttributeCallExp
from python_code import OCL_OclExpression

def test_OCL_NavigationOrAttributeCallExp___init__():
    assert OCL_NavigationOrAttributeCallExp.__init__(OCL_NavigationOrAttributeCallExp('', PropertyCallExp=OCL_OclExpression()), '', PropertyCallExp=OCL_OclExpression()) == None


from python_code import OCL_OclModel
from python_code import OclModel

def test_OCL_OclModel___init__():
    assert OCL_OclModel.__init__(OCL_OclModel('', metamodel=set(), model=OclModel(), model213=set()), '', metamodel=set(), model=OclModel(), model213=set()) == None


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

