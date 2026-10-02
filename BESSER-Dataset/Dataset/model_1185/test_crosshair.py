from python_code import OclExpression
from python_code import atl_n_ocl_ATL_Binding

def test_atl_n_ocl_ATL_Binding___init__():
    assert atl_n_ocl_ATL_Binding.__init__(atl_n_ocl_ATL_Binding('', False, atl_n_ocl_ATL_Binding=OclExpression()), '', True, atl_n_ocl_ATL_Binding=OclExpression()) == None

from python_code import OclExpression
from python_code import atl_n_ocl_ATL_ActionBlock
from python_code import atl_n_ocl_ATL_BindingStat
from python_code import atl_n_ocl_ATL_ForStat
from python_code import atl_n_ocl_ATL_IfStat

def test_atl_n_ocl_ATL_BindingStat___init__():
    assert atl_n_ocl_ATL_BindingStat.__init__(atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), '', True, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()) == None

from python_code import atl_n_ocl_ATL_CalledRule

def test_atl_n_ocl_ATL_CalledRule___init__():
    assert atl_n_ocl_ATL_CalledRule.__init__(atl_n_ocl_ATL_CalledRule(False, False, atl_n_ocl_ATL_CalledRule=set()), False, False, atl_n_ocl_ATL_CalledRule=set()) == None

from python_code import InPattern
from python_code import atl_n_ocl_ATL_LazyMatchedRule
from python_code import atl_n_ocl_ATL_MatchedRule

def test_atl_n_ocl_ATL_LazyMatchedRule___init__():
    assert atl_n_ocl_ATL_LazyMatchedRule.__init__(atl_n_ocl_ATL_LazyMatchedRule(False, MatchedRule=atl_n_ocl_ATL_MatchedRule(False, False, False, atl_n_ocl_ATL_MatchedRule=InPattern(), atl_n_ocl_ATL_MatchedRule17=set())), False, MatchedRule=atl_n_ocl_ATL_MatchedRule(False, True, False, atl_n_ocl_ATL_MatchedRule=InPattern(), atl_n_ocl_ATL_MatchedRule17=set())) == None

from python_code import InPattern
from python_code import atl_n_ocl_ATL_MatchedRule

def test_atl_n_ocl_ATL_MatchedRule___init__():
    assert atl_n_ocl_ATL_MatchedRule.__init__(atl_n_ocl_ATL_MatchedRule(False, False, False, atl_n_ocl_ATL_MatchedRule=InPattern(), atl_n_ocl_ATL_MatchedRule17=set()), False, False, True, atl_n_ocl_ATL_MatchedRule=InPattern(), atl_n_ocl_ATL_MatchedRule17=set()) == None

from python_code import atl_n_ocl_ATL_Module

def test_atl_n_ocl_ATL_Module___init__():
    assert atl_n_ocl_ATL_Module.__init__(atl_n_ocl_ATL_Module(False, atl_n_ocl_ATL_Module=set(), atl_n_ocl_ATL_Module5=set(), atl_n_ocl_ATL_Module8=set()), True, atl_n_ocl_ATL_Module=set(), atl_n_ocl_ATL_Module5=set(), atl_n_ocl_ATL_Module8=set()) == None

from python_code import ActionBlock
from python_code import OutPattern
from python_code import atl_n_ocl_ATL_Module
from python_code import atl_n_ocl_ATL_Rule

def test_atl_n_ocl_ATL_Rule___init__():
    assert atl_n_ocl_ATL_Rule.__init__(atl_n_ocl_ATL_Rule('', atl_n_ocl_ATL_Rule14=set(), atl_n_ocl_ATL_Rule=OutPattern(), atl_n_ocl_ATL_Rule12=ActionBlock(), ModuleElement=atl_n_ocl_ATL_Module(False, atl_n_ocl_ATL_Module=set(), atl_n_ocl_ATL_Module5=set(), atl_n_ocl_ATL_Module8=set())), '', atl_n_ocl_ATL_Rule14=set(), atl_n_ocl_ATL_Rule=OutPattern(), atl_n_ocl_ATL_Rule12=ActionBlock(), ModuleElement=atl_n_ocl_ATL_Module(False, atl_n_ocl_ATL_Module=set(), atl_n_ocl_ATL_Module5=set(), atl_n_ocl_ATL_Module8=set())) == None

from python_code import OclExpression
from python_code import OclType
from python_code import atl_n_ocl_OCL_Attribute
from python_code import atl_n_ocl_OCL_OclFeatureDefinition

def test_atl_n_ocl_OCL_Attribute___init__():
    assert atl_n_ocl_OCL_Attribute.__init__(atl_n_ocl_OCL_Attribute('', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=OclType(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), '', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=OclType(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()) == None

from python_code import atl_n_ocl_OCL_BooleanExp

def test_atl_n_ocl_OCL_BooleanExp___init__():
    assert atl_n_ocl_OCL_BooleanExp.__init__(atl_n_ocl_OCL_BooleanExp(True), False) == None

from python_code import OclExpression
from python_code import OclType
from python_code import atl_n_ocl_ATL_ActionBlock
from python_code import atl_n_ocl_ATL_Binding
from python_code import atl_n_ocl_ATL_BindingStat
from python_code import atl_n_ocl_ATL_ExpressionStat
from python_code import atl_n_ocl_ATL_ForEachOutPatternElement
from python_code import atl_n_ocl_ATL_ForStat
from python_code import atl_n_ocl_ATL_IfStat
from python_code import atl_n_ocl_ATL_InPattern
from python_code import atl_n_ocl_ATL_Query
from python_code import atl_n_ocl_ATL_SimpleOutPatternElement
from python_code import atl_n_ocl_OCL_Attribute
from python_code import atl_n_ocl_OCL_CollectionExp
from python_code import atl_n_ocl_OCL_EnumLiteralExp
from python_code import atl_n_ocl_OCL_IfExp
from python_code import atl_n_ocl_OCL_LetExp
from python_code import atl_n_ocl_OCL_LoopExp
from python_code import atl_n_ocl_OCL_MapElement
from python_code import atl_n_ocl_OCL_MapType
from python_code import atl_n_ocl_OCL_OclFeatureDefinition
from python_code import atl_n_ocl_OCL_Operation
from python_code import atl_n_ocl_OCL_OperationCallExp
from python_code import atl_n_ocl_OCL_Primitive
from python_code import atl_n_ocl_OCL_PropertyCallExp
from python_code import atl_n_ocl_OCL_VariableDeclaration

def test_atl_n_ocl_OCL_EnumLiteralExp___init__():
    assert atl_n_ocl_OCL_EnumLiteralExp.__init__(atl_n_ocl_OCL_EnumLiteralExp('', OclExpression126=atl_n_ocl_OCL_Attribute('', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=atl_n_ocl_OCL_Primitive(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression44=atl_n_ocl_ATL_Binding('', False, atl_n_ocl_ATL_Binding=OclExpression()), OclExpression38=atl_n_ocl_ATL_SimpleOutPatternElement(), OclExpression77=atl_n_ocl_OCL_MapElement(), OclExpression82=atl_n_ocl_OCL_PropertyCallExp(), OclExpression54=atl_n_ocl_ATL_IfStat(), OclExpression137=atl_n_ocl_OCL_Operation('', atl_n_ocl_OCL_Operation={<python_code.Parameter object at 0x0000016AD22A5A10>}, atl_n_ocl_OCL_Operation133=OclType(), atl_n_ocl_OCL_Operation136=OclExpression(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression=atl_n_ocl_ATL_Query(), OclExpression96=atl_n_ocl_OCL_LetExp(), OclExpression86=atl_n_ocl_OCL_LoopExp(), OclExpression47=atl_n_ocl_ATL_ExpressionStat(), OclExpression22=atl_n_ocl_ATL_InPattern(), OclExpression52=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=atl_n_ocl_OCL_LetExp(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression72=atl_n_ocl_OCL_CollectionExp(), OclExpression49=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression80=atl_n_ocl_OCL_MapElement(), OclExpression101=atl_n_ocl_OCL_IfExp(), OclExpression40=atl_n_ocl_ATL_ForEachOutPatternElement(), OclExpression98=atl_n_ocl_OCL_IfExp(), OclExpression65=atl_n_ocl_ATL_ForStat(), OclExpression84=atl_n_ocl_OCL_OperationCallExp('', atl_n_ocl_OCL_OperationCallExp=set()), OclExpression109=atl_n_ocl_OCL_VariableDeclaration('', '', atl_n_ocl_OCL_VariableDeclaration=atl_n_ocl_OCL_MapType(), atl_n_ocl_OCL_VariableDeclaration108=OclExpression()), OclExpression104=atl_n_ocl_OCL_IfExp()), '\x00', OclExpression126=atl_n_ocl_OCL_Attribute('', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=OclType(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression44=atl_n_ocl_ATL_Binding('\x00\x00', False, atl_n_ocl_ATL_Binding=atl_n_ocl_OCL_IfExp()), OclExpression38=atl_n_ocl_ATL_SimpleOutPatternElement(), OclExpression77=atl_n_ocl_OCL_MapElement(), OclExpression82=atl_n_ocl_OCL_PropertyCallExp(), OclExpression54=atl_n_ocl_ATL_IfStat(), OclExpression137=atl_n_ocl_OCL_Operation('', atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation133=OclType(), atl_n_ocl_OCL_Operation136=OclExpression(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression=atl_n_ocl_ATL_Query(), OclExpression96=atl_n_ocl_OCL_LetExp(), OclExpression86=atl_n_ocl_OCL_LoopExp(), OclExpression47=atl_n_ocl_ATL_ExpressionStat(), OclExpression22=atl_n_ocl_ATL_InPattern(), OclExpression52=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression72=atl_n_ocl_OCL_CollectionExp(), OclExpression49=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression80=atl_n_ocl_OCL_MapElement(), OclExpression101=atl_n_ocl_OCL_IfExp(), OclExpression40=atl_n_ocl_ATL_ForEachOutPatternElement(), OclExpression98=atl_n_ocl_OCL_IfExp(), OclExpression65=atl_n_ocl_ATL_ForStat(), OclExpression84=atl_n_ocl_OCL_OperationCallExp('\x00', atl_n_ocl_OCL_OperationCallExp={<python_code.OclExpression object at 0x0000016AD22B4110>}), OclExpression109=atl_n_ocl_OCL_VariableDeclaration('', '', atl_n_ocl_OCL_VariableDeclaration=OclType(), atl_n_ocl_OCL_VariableDeclaration108=OclExpression()), OclExpression104=atl_n_ocl_OCL_IfExp()) == None

from python_code import atl_n_ocl_OCL_IntegerExp

def test_atl_n_ocl_OCL_IntegerExp___init__():
    assert atl_n_ocl_OCL_IntegerExp.__init__(atl_n_ocl_OCL_IntegerExp(0), 0) == None

from python_code import atl_n_ocl_OCL_IteratorExp

def test_atl_n_ocl_OCL_IteratorExp___init__():
    assert atl_n_ocl_OCL_IteratorExp.__init__(atl_n_ocl_OCL_IteratorExp(''), '') == None

from python_code import atl_n_ocl_OCL_NavigationOrAttributeCallExp

def test_atl_n_ocl_OCL_NavigationOrAttributeCallExp___init__():
    assert atl_n_ocl_OCL_NavigationOrAttributeCallExp.__init__(atl_n_ocl_OCL_NavigationOrAttributeCallExp(''), '') == None

from python_code import OclModel
from python_code import atl_n_ocl_OCL_OclModel

def test_atl_n_ocl_OCL_OclModel___init__():
    assert atl_n_ocl_OCL_OclModel.__init__(atl_n_ocl_OCL_OclModel('', atl_n_ocl_OCL_OclModel=OclModel(), atl_n_ocl_OCL_OclModel141=set(), atl_n_ocl_OCL_OclModel143=set()), '', atl_n_ocl_OCL_OclModel=OclModel(), atl_n_ocl_OCL_OclModel141=set(), atl_n_ocl_OCL_OclModel143=set()) == None

from python_code import OclExpression
from python_code import OclType
from python_code import atl_n_ocl_ATL_ActionBlock
from python_code import atl_n_ocl_ATL_Binding
from python_code import atl_n_ocl_ATL_BindingStat
from python_code import atl_n_ocl_ATL_ExpressionStat
from python_code import atl_n_ocl_ATL_ForEachOutPatternElement
from python_code import atl_n_ocl_ATL_ForStat
from python_code import atl_n_ocl_ATL_IfStat
from python_code import atl_n_ocl_ATL_InPattern
from python_code import atl_n_ocl_ATL_Query
from python_code import atl_n_ocl_ATL_SimpleOutPatternElement
from python_code import atl_n_ocl_OCL_Attribute
from python_code import atl_n_ocl_OCL_CollectionExp
from python_code import atl_n_ocl_OCL_IfExp
from python_code import atl_n_ocl_OCL_LetExp
from python_code import atl_n_ocl_OCL_LoopExp
from python_code import atl_n_ocl_OCL_MapElement
from python_code import atl_n_ocl_OCL_OclFeatureDefinition
from python_code import atl_n_ocl_OCL_OclModelElement
from python_code import atl_n_ocl_OCL_OclType
from python_code import atl_n_ocl_OCL_Operation
from python_code import atl_n_ocl_OCL_OperationCallExp
from python_code import atl_n_ocl_OCL_Primitive
from python_code import atl_n_ocl_OCL_PrimitiveExp
from python_code import atl_n_ocl_OCL_PropertyCallExp
from python_code import atl_n_ocl_OCL_TupleExp
from python_code import atl_n_ocl_OCL_VariableDeclaration

def test_atl_n_ocl_OCL_OclType___init__():
    assert atl_n_ocl_OCL_OclType.__init__(atl_n_ocl_OCL_OclType('', OclExpression126=atl_n_ocl_OCL_Attribute('', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=atl_n_ocl_OCL_OclModelElement(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression44=atl_n_ocl_ATL_Binding('', False, atl_n_ocl_ATL_Binding=OclExpression()), OclExpression38=atl_n_ocl_ATL_SimpleOutPatternElement(), OclExpression77=atl_n_ocl_OCL_MapElement(), OclExpression82=atl_n_ocl_OCL_PropertyCallExp(), OclExpression54=atl_n_ocl_ATL_IfStat(), OclExpression137=atl_n_ocl_OCL_Operation('', atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation133=OclType(), atl_n_ocl_OCL_Operation136=OclExpression(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression=atl_n_ocl_ATL_Query(), OclExpression96=atl_n_ocl_OCL_LetExp(), OclExpression86=atl_n_ocl_OCL_LoopExp(), OclExpression47=atl_n_ocl_ATL_ExpressionStat(), OclExpression22=atl_n_ocl_ATL_InPattern(), OclExpression52=atl_n_ocl_ATL_BindingStat('', True, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression72=atl_n_ocl_OCL_CollectionExp(), OclExpression49=atl_n_ocl_ATL_BindingStat('', True, atl_n_ocl_ATL_BindingStat=atl_n_ocl_OCL_IfExp(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression80=atl_n_ocl_OCL_MapElement(), OclExpression101=atl_n_ocl_OCL_IfExp(), OclExpression40=atl_n_ocl_ATL_ForEachOutPatternElement(), OclExpression98=atl_n_ocl_OCL_IfExp(), OclExpression65=atl_n_ocl_ATL_ForStat(), OclExpression84=atl_n_ocl_OCL_OperationCallExp('', atl_n_ocl_OCL_OperationCallExp=set()), OclExpression109=atl_n_ocl_OCL_VariableDeclaration('', '', atl_n_ocl_OCL_VariableDeclaration=OclType(), atl_n_ocl_OCL_VariableDeclaration108=OclExpression()), OclExpression104=atl_n_ocl_OCL_IfExp()), '', OclExpression126=atl_n_ocl_OCL_Attribute('', atl_n_ocl_OCL_Attribute=OclExpression(), atl_n_ocl_OCL_Attribute128=OclType(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression44=atl_n_ocl_ATL_Binding('', False, atl_n_ocl_ATL_Binding=OclExpression()), OclExpression38=atl_n_ocl_ATL_SimpleOutPatternElement(), OclExpression77=atl_n_ocl_OCL_MapElement(), OclExpression82=atl_n_ocl_OCL_PropertyCallExp(), OclExpression54=atl_n_ocl_ATL_IfStat(), OclExpression137=atl_n_ocl_OCL_Operation('', atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation133=atl_n_ocl_OCL_Primitive(), atl_n_ocl_OCL_Operation136=atl_n_ocl_OCL_TupleExp(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), OclExpression=atl_n_ocl_ATL_Query(), OclExpression96=atl_n_ocl_OCL_LetExp(), OclExpression86=atl_n_ocl_OCL_LoopExp(), OclExpression47=atl_n_ocl_ATL_ExpressionStat(), OclExpression22=atl_n_ocl_ATL_InPattern(), OclExpression52=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression72=atl_n_ocl_OCL_CollectionExp(), OclExpression49=atl_n_ocl_ATL_BindingStat('', False, atl_n_ocl_ATL_BindingStat=OclExpression(), atl_n_ocl_ATL_BindingStat51=OclExpression(), Statement60=atl_n_ocl_ATL_IfStat(), Statement57=atl_n_ocl_ATL_IfStat(), Statement=atl_n_ocl_ATL_ActionBlock(), Statement68=atl_n_ocl_ATL_ForStat()), OclExpression80=atl_n_ocl_OCL_MapElement(), OclExpression101=atl_n_ocl_OCL_IfExp(), OclExpression40=atl_n_ocl_ATL_ForEachOutPatternElement(), OclExpression98=atl_n_ocl_OCL_IfExp(), OclExpression65=atl_n_ocl_ATL_ForStat(), OclExpression84=atl_n_ocl_OCL_OperationCallExp('', atl_n_ocl_OCL_OperationCallExp=set()), OclExpression109=atl_n_ocl_OCL_VariableDeclaration('', '', atl_n_ocl_OCL_VariableDeclaration=OclType(), atl_n_ocl_OCL_VariableDeclaration108=atl_n_ocl_OCL_PrimitiveExp()), OclExpression104=atl_n_ocl_OCL_IfExp()) == None

from python_code import OclExpression
from python_code import OclType
from python_code import atl_n_ocl_OCL_OclFeatureDefinition
from python_code import atl_n_ocl_OCL_Operation

def test_atl_n_ocl_OCL_Operation___init__():
    assert atl_n_ocl_OCL_Operation.__init__(atl_n_ocl_OCL_Operation('', atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation133=OclType(), atl_n_ocl_OCL_Operation136=OclExpression(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()), '', atl_n_ocl_OCL_Operation=set(), atl_n_ocl_OCL_Operation133=OclType(), atl_n_ocl_OCL_Operation136=OclExpression(), OclFeature=atl_n_ocl_OCL_OclFeatureDefinition()) == None

from python_code import atl_n_ocl_OCL_OperationCallExp

def test_atl_n_ocl_OCL_OperationCallExp___init__():
    assert atl_n_ocl_OCL_OperationCallExp.__init__(atl_n_ocl_OCL_OperationCallExp('', atl_n_ocl_OCL_OperationCallExp=set()), '', atl_n_ocl_OCL_OperationCallExp=set()) == None

from python_code import atl_n_ocl_OCL_RealExp

def test_atl_n_ocl_OCL_RealExp___init__():
    assert atl_n_ocl_OCL_RealExp.__init__(atl_n_ocl_OCL_RealExp(0.0), 0.0) == None

from python_code import atl_n_ocl_OCL_StringExp

def test_atl_n_ocl_OCL_StringExp___init__():
    assert atl_n_ocl_OCL_StringExp.__init__(atl_n_ocl_OCL_StringExp(''), '') == None

from python_code import OclType
from python_code import atl_n_ocl_OCL_TupleTypeAttribute

def test_atl_n_ocl_OCL_TupleTypeAttribute___init__():
    assert atl_n_ocl_OCL_TupleTypeAttribute.__init__(atl_n_ocl_OCL_TupleTypeAttribute('', atl_n_ocl_OCL_TupleTypeAttribute=OclType()), '', atl_n_ocl_OCL_TupleTypeAttribute=OclType()) == None

from python_code import OclExpression
from python_code import OclType
from python_code import atl_n_ocl_OCL_VariableDeclaration

def test_atl_n_ocl_OCL_VariableDeclaration___init__():
    assert atl_n_ocl_OCL_VariableDeclaration.__init__(atl_n_ocl_OCL_VariableDeclaration('', '', atl_n_ocl_OCL_VariableDeclaration=OclType(), atl_n_ocl_OCL_VariableDeclaration108=OclExpression()), '', '', atl_n_ocl_OCL_VariableDeclaration=OclType(), atl_n_ocl_OCL_VariableDeclaration108=OclExpression()) == None
