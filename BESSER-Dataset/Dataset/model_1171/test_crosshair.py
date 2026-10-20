from python_code import atlstatic_ATL_CalledRule

def test_atlstatic_ATL_CalledRule___init__():
    assert atlstatic_ATL_CalledRule.__init__(atlstatic_ATL_CalledRule('\x00\x00', '', atlstatic_ATL_CalledRule=set()), '', '', atlstatic_ATL_CalledRule=set()) == None


from python_code import atlstatic_ATL_LazyRule

def test_atlstatic_ATL_LazyRule___init__():
    assert atlstatic_ATL_LazyRule.__init__(atlstatic_ATL_LazyRule(''), '') == None


from python_code import Unit
from python_code import atlstatic_ATL_LibraryRef

def test_atlstatic_ATL_LibraryRef___init__():
    assert atlstatic_ATL_LibraryRef.__init__(atlstatic_ATL_LibraryRef('', libraries=Unit()), '', libraries=Unit()) == None


from python_code import atlstatic_ATL_LocatedElement

def test_atlstatic_ATL_LocatedElement___init__():
    assert atlstatic_ATL_LocatedElement.__init__(atlstatic_ATL_LocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import Unit
from python_code import atlstatic_ATL_LibraryRef
from python_code import atlstatic_ATL_Module

def test_atlstatic_ATL_Module___init__():
    assert atlstatic_ATL_Module.__init__(atlstatic_ATL_Module('', atlstatic_ATL_Module=set(), atlstatic_ATL_Module7=set(), atlstatic_ATL_Module10=set(), Unit=atlstatic_ATL_LibraryRef('', libraries=Unit())), '', atlstatic_ATL_Module=set(), atlstatic_ATL_Module7=set(), atlstatic_ATL_Module10=set(), Unit=atlstatic_ATL_LibraryRef('', libraries=Unit())) == None


from python_code import ActionBlock
from python_code import OutPattern
from python_code import Unit
from python_code import atlstatic_ATL_LibraryRef
from python_code import atlstatic_ATL_Module
from python_code import atlstatic_ATL_Rule

def test_atlstatic_ATL_Rule___init__():
    assert atlstatic_ATL_Rule.__init__(atlstatic_ATL_Rule('', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=atlstatic_ATL_Module('', atlstatic_ATL_Module=set(), atlstatic_ATL_Module7=set(), atlstatic_ATL_Module10=set(), Unit=atlstatic_ATL_LibraryRef('', libraries=Unit()))), '', rule=OutPattern(), rule17=ActionBlock(), rule19=set(), ModuleElement=atlstatic_ATL_Module('', atlstatic_ATL_Module=set(), atlstatic_ATL_Module7=set(), atlstatic_ATL_Module10=set(), Unit=atlstatic_ATL_LibraryRef('', libraries=Unit()))) == None


from python_code import InPattern
from python_code import RuleWithPattern
from python_code import atlstatic_ATL_ActionBlock
from python_code import atlstatic_ATL_OutPattern
from python_code import atlstatic_ATL_RuleVariableDeclaration
from python_code import atlstatic_ATL_RuleWithPattern

def test_atlstatic_ATL_RuleWithPattern___init__():
    assert atlstatic_ATL_RuleWithPattern.__init__(atlstatic_ATL_RuleWithPattern('', '', '', atlstatic_ATL_RuleWithPattern=InPattern(), superRule=set(), children=RuleWithPattern(), Rule60=atlstatic_ATL_RuleVariableDeclaration(), Rule=atlstatic_ATL_OutPattern(), Rule63=atlstatic_ATL_ActionBlock()), '', '', '', atlstatic_ATL_RuleWithPattern=InPattern(), superRule=set(), children=RuleWithPattern(), Rule60=atlstatic_ATL_RuleVariableDeclaration(), Rule=atlstatic_ATL_OutPattern(), Rule63=atlstatic_ATL_ActionBlock()) == None


from python_code import atlstatic_ATL_Unit

def test_atlstatic_ATL_Unit___init__():
    assert atlstatic_ATL_Unit.__init__(atlstatic_ATL_Unit('', unit=set()), '', unit=set()) == None


from python_code import atlstatic_OCL_BooleanExp

def test_atlstatic_OCL_BooleanExp___init__():
    assert atlstatic_OCL_BooleanExp.__init__(atlstatic_OCL_BooleanExp(''), '') == None


from python_code import atlstatic_OCL_IntegerExp

def test_atlstatic_OCL_IntegerExp___init__():
    assert atlstatic_OCL_IntegerExp.__init__(atlstatic_OCL_IntegerExp(''), '') == None


from python_code import atlstatic_OCL_Iterator
from python_code import atlstatic_OCL_IteratorExp
from python_code import atlstatic_OCL_OclExpression

def test_atlstatic_OCL_IteratorExp___init__():
    assert atlstatic_OCL_IteratorExp.__init__(atlstatic_OCL_IteratorExp('', LoopExp=atlstatic_OCL_OclExpression(), LoopExp149=atlstatic_OCL_Iterator()), '', LoopExp=atlstatic_OCL_OclExpression(), LoopExp149=atlstatic_OCL_Iterator()) == None


from python_code import atlstatic_OCL_NavigationOrAttributeCallExp
from python_code import atlstatic_OCL_OclExpression

def test_atlstatic_OCL_NavigationOrAttributeCallExp___init__():
    assert atlstatic_OCL_NavigationOrAttributeCallExp.__init__(atlstatic_OCL_NavigationOrAttributeCallExp('', PropertyCallExp=atlstatic_OCL_OclExpression()), '', PropertyCallExp=atlstatic_OCL_OclExpression()) == None


from python_code import OclModel
from python_code import atlstatic_OCL_OclModel

def test_atlstatic_OCL_OclModel___init__():
    assert atlstatic_OCL_OclModel.__init__(atlstatic_OCL_OclModel('', model=OclModel(), model205=set(), metamodel=set()), '', model=OclModel(), model205=set(), metamodel=set()) == None

