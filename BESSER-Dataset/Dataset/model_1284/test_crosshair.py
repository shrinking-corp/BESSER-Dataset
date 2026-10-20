from python_code import morel_AdditiveExp

def test_morel_AdditiveExp___init__():
    assert morel_AdditiveExp.__init__(morel_AdditiveExp('', morel_AdditiveExp=set()), '', morel_AdditiveExp=set()) == None


from python_code import morel_BooleanAndExp

def test_morel_BooleanAndExp___init__():
    assert morel_BooleanAndExp.__init__(morel_BooleanAndExp('', morel_BooleanAndExp=set()), '', morel_BooleanAndExp=set()) == None


from python_code import morel_BooleanImpliesExp
from python_code import morel_BooleanImpliesExpChild
from python_code import morel_ConditionExp
from python_code import morel_ForStatement
from python_code import morel_IfStatement

def test_morel_BooleanImpliesExp___init__():
    assert morel_BooleanImpliesExp.__init__(morel_BooleanImpliesExp('', morel_BooleanImpliesExp=morel_ConditionExp(), morel_BooleanImpliesExp82=morel_BooleanImpliesExpChild(), morel_BooleanImpliesExp84=morel_BooleanImpliesExpChild(), morel_BooleanImpliesExp107=morel_IfStatement(), morel_BooleanImpliesExp117=morel_ForStatement()), '', morel_BooleanImpliesExp=morel_ConditionExp(), morel_BooleanImpliesExp82=morel_BooleanImpliesExpChild(), morel_BooleanImpliesExp84=morel_BooleanImpliesExpChild(), morel_BooleanImpliesExp107=morel_IfStatement(), morel_BooleanImpliesExp117=morel_ForStatement()) == None


from python_code import morel_BooleanLiteralExp

def test_morel_BooleanLiteralExp___init__():
    assert morel_BooleanLiteralExp.__init__(morel_BooleanLiteralExp(True), False) == None


from python_code import morel_BooleanOrExp

def test_morel_BooleanOrExp___init__():
    assert morel_BooleanOrExp.__init__(morel_BooleanOrExp('', morel_BooleanOrExp=set()), '', morel_BooleanOrExp=set()) == None


from python_code import morel_CollectionLiteralExp

def test_morel_CollectionLiteralExp___init__():
    assert morel_CollectionLiteralExp.__init__(morel_CollectionLiteralExp('', morel_CollectionLiteralExp=set()), '', morel_CollectionLiteralExp=set()) == None


from python_code import morel_Executable

def test_morel_Executable___init__():
    assert morel_Executable.__init__(morel_Executable(False, '\x00', morel_Executable=set()), False, '', morel_Executable=set()) == None


from python_code import morel_FeaturePathExp

def test_morel_FeaturePathExp___init__():
    assert morel_FeaturePathExp.__init__(morel_FeaturePathExp(''), '') == None


from python_code import morel_IntegerLiteralExp

def test_morel_IntegerLiteralExp___init__():
    assert morel_IntegerLiteralExp.__init__(morel_IntegerLiteralExp(0), 0) == None


from python_code import morel_Expression
from python_code import morel_IteratorPathExp
from python_code import morel_Variable

def test_morel_IteratorPathExp___init__():
    assert morel_IteratorPathExp.__init__(morel_IteratorPathExp('', morel_IteratorPathExp=morel_Variable(), morel_IteratorPathExp62=morel_Variable(), morel_IteratorPathExp65=morel_Expression()), '', morel_IteratorPathExp=morel_Variable(), morel_IteratorPathExp62=morel_Variable(), morel_IteratorPathExp65=morel_Expression()) == None


from python_code import morel_MultiplicativeExp

def test_morel_MultiplicativeExp___init__():
    assert morel_MultiplicativeExp.__init__(morel_MultiplicativeExp('', morel_MultiplicativeExp=set()), '', morel_MultiplicativeExp=set()) == None


from python_code import morel_NamedElement

def test_morel_NamedElement___init__():
    assert morel_NamedElement.__init__(morel_NamedElement(''), '') == None


from python_code import morel_OperationPathExp

def test_morel_OperationPathExp___init__():
    assert morel_OperationPathExp.__init__(morel_OperationPathExp('\x00\x00', '', morel_OperationPathExp=set()), '', '', morel_OperationPathExp=set()) == None


from python_code import morel_PathConstraint
from python_code import morel_Variable

def test_morel_PathConstraint___init__():
    assert morel_PathConstraint.__init__(morel_PathConstraint(0, 0, morel_PathConstraint=morel_Variable(), morel_PathConstraint30=set(), morel_PathConstraint33=set()), 0, 0, morel_PathConstraint=morel_Variable(), morel_PathConstraint30=set(), morel_PathConstraint33=set()) == None


from python_code import morel_PredefinedBindExp
from python_code import morel_PredefinedVariableExp

def test_morel_PredefinedVariableExp___init__():
    assert morel_PredefinedVariableExp.__init__(morel_PredefinedVariableExp('', morel_PredefinedVariableExp=morel_PredefinedBindExp()), '', morel_PredefinedVariableExp=morel_PredefinedBindExp()) == None


from python_code import morel_RealLiteralExp

def test_morel_RealLiteralExp___init__():
    assert morel_RealLiteralExp.__init__(morel_RealLiteralExp(0.0), 0.0) == None


from python_code import morel_RelationalExp
from python_code import morel_RelationalExpChild

def test_morel_RelationalExp___init__():
    assert morel_RelationalExp.__init__(morel_RelationalExp('', morel_RelationalExp=morel_RelationalExpChild(), morel_RelationalExp90=morel_RelationalExpChild()), '', morel_RelationalExp=morel_RelationalExpChild(), morel_RelationalExp90=morel_RelationalExpChild()) == None


from python_code import morel_RuleGroup

def test_morel_RuleGroup___init__():
    assert morel_RuleGroup.__init__(morel_RuleGroup('', 0, '\x00', '', 0, '', morel_RuleGroup=set()), '', 0, '', '', 0, '', morel_RuleGroup=set()) == None


from python_code import morel_Section

def test_morel_Section___init__():
    assert morel_Section.__init__(morel_Section(''), '') == None


from python_code import morel_StringLiteralExp

def test_morel_StringLiteralExp___init__():
    assert morel_StringLiteralExp.__init__(morel_StringLiteralExp(''), '') == None


from python_code import morel_UnaryExp
from python_code import morel_UnaryExpChild

def test_morel_UnaryExp___init__():
    assert morel_UnaryExp.__init__(morel_UnaryExp('', morel_UnaryExp=morel_UnaryExpChild()), '', morel_UnaryExp=morel_UnaryExpChild()) == None


from python_code import morel_UndefinedLiteralExp

def test_morel_UndefinedLiteralExp___init__():
    assert morel_UndefinedLiteralExp.__init__(morel_UndefinedLiteralExp(''), '') == None


from python_code import morel_Unit

def test_morel_Unit___init__():
    assert morel_Unit.__init__(morel_Unit(morel_Unit41=set(), morel_Unit=set()), morel_Unit41=set(), morel_Unit=set()) == None

def test_morel_Unit_getTypedModel():
    assert morel_Unit.getTypedModel(morel_Unit(morel_Unit41=set(), morel_Unit=set()), 0) == None

