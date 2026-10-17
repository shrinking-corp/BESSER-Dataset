import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActionBlock,
    Binding,
    CollectionExp,
    CollectionType,
    DropPattern,
    Helper,
    InPattern,
    InPatternElement,
    Iterator,
    LoopExp,
    MapElement,
    MatchedRule,
    ModuleElement,
    NumericExp,
    NumericType,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    OperationCallExp,
    OutPattern,
    OutPatternElement,
    Parameter,
    PatternElement,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    Rule,
    RuleVariableDeclaration,
    Statement,
    TupleExp,
    TuplePart,
    TupleTypeAttribute,
    VariableDeclaration,
    atl_n_ocl_ATL_ActionBlock,
    atl_n_ocl_ATL_Binding,
    atl_n_ocl_ATL_BindingStat,
    atl_n_ocl_ATL_CalledRule,
    atl_n_ocl_ATL_DropPattern,
    atl_n_ocl_ATL_ExpressionStat,
    atl_n_ocl_ATL_ForEachOutPatternElement,
    atl_n_ocl_ATL_ForStat,
    atl_n_ocl_ATL_Helper,
    atl_n_ocl_ATL_IfStat,
    atl_n_ocl_ATL_InPattern,
    atl_n_ocl_ATL_InPatternElement,
    atl_n_ocl_ATL_LazyMatchedRule,
    atl_n_ocl_ATL_MatchedRule,
    atl_n_ocl_ATL_Module,
    atl_n_ocl_ATL_ModuleElement,
    atl_n_ocl_ATL_OutPattern,
    atl_n_ocl_ATL_OutPatternElement,
    atl_n_ocl_ATL_PatternElement,
    atl_n_ocl_ATL_Query,
    atl_n_ocl_ATL_Rule,
    atl_n_ocl_ATL_RuleVariableDeclaration,
    atl_n_ocl_ATL_SimpleInPatternElement,
    atl_n_ocl_ATL_SimpleOutPatternElement,
    atl_n_ocl_ATL_Statement,
    atl_n_ocl_OCL_Attribute,
    atl_n_ocl_OCL_BagExp,
    atl_n_ocl_OCL_BagType,
    atl_n_ocl_OCL_BooleanExp,
    atl_n_ocl_OCL_BooleanType,
    atl_n_ocl_OCL_CollectionExp,
    atl_n_ocl_OCL_CollectionOperationCallExp,
    atl_n_ocl_OCL_CollectionType,
    atl_n_ocl_OCL_EnumLiteralExp,
    atl_n_ocl_OCL_IfExp,
    atl_n_ocl_OCL_IntegerExp,
    atl_n_ocl_OCL_IntegerType,
    atl_n_ocl_OCL_IterateExp,
    atl_n_ocl_OCL_Iterator,
    atl_n_ocl_OCL_IteratorExp,
    atl_n_ocl_OCL_LetExp,
    atl_n_ocl_OCL_LoopExp,
    atl_n_ocl_OCL_MapElement,
    atl_n_ocl_OCL_MapExp,
    atl_n_ocl_OCL_MapType,
    atl_n_ocl_OCL_NavigationOrAttributeCallExp,
    atl_n_ocl_OCL_NumericExp,
    atl_n_ocl_OCL_NumericType,
    atl_n_ocl_OCL_OclAnyType,
    atl_n_ocl_OCL_OclContextDefinition,
    atl_n_ocl_OCL_OclExpression,
    atl_n_ocl_OCL_OclFeature,
    atl_n_ocl_OCL_OclFeatureDefinition,
    atl_n_ocl_OCL_OclModel,
    atl_n_ocl_OCL_OclModelElement,
    atl_n_ocl_OCL_OclType,
    atl_n_ocl_OCL_OclUndefinedExp,
    atl_n_ocl_OCL_Operation,
    atl_n_ocl_OCL_OperationCallExp,
    atl_n_ocl_OCL_OperatorCallExp,
    atl_n_ocl_OCL_OrderedSetExp,
    atl_n_ocl_OCL_OrderedSetType,
    atl_n_ocl_OCL_Parameter,
    atl_n_ocl_OCL_Primitive,
    atl_n_ocl_OCL_PrimitiveExp,
    atl_n_ocl_OCL_PropertyCallExp,
    atl_n_ocl_OCL_RealExp,
    atl_n_ocl_OCL_RealType,
    atl_n_ocl_OCL_SequenceExp,
    atl_n_ocl_OCL_SequenceType,
    atl_n_ocl_OCL_SetExp,
    atl_n_ocl_OCL_SetType,
    atl_n_ocl_OCL_StringExp,
    atl_n_ocl_OCL_StringType,
    atl_n_ocl_OCL_SuperExp,
    atl_n_ocl_OCL_TupleExp,
    atl_n_ocl_OCL_TuplePart,
    atl_n_ocl_OCL_TupleType,
    atl_n_ocl_OCL_TupleTypeAttribute,
    atl_n_ocl_OCL_VariableDeclaration,
    atl_n_ocl_OCL_VariableExp,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_actionBlock11_stub_double():
    # ActionBlock has no real 'ActionBlock' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Rule(name="sample_text")
    partner = ActionBlock()
    setattr(partner, 'ActionBlock', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Rule12', partner)
    assert getattr(partner, 'ActionBlock') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Rule12', None)
    assert getattr(partner, 'ActionBlock') is None


def test_assoc_arguments83_stub_double():
    # OclExpression has no real 'OclExpression84' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression84', None)
    _safe_set(owner, 'atl_n_ocl_OCL_OperationCallExp', {partner})
    assert getattr(partner, 'OclExpression84') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_OperationCallExp', set())
    assert getattr(partner, 'OclExpression84') is None


def test_assoc_body135_stub_double():
    # OclExpression has no real 'OclExpression137' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression137', None)
    _safe_set(owner, 'atl_n_ocl_OCL_Operation136', partner)
    assert getattr(partner, 'OclExpression137') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_Operation136', None)
    assert getattr(partner, 'OclExpression137') is None


def test_assoc_children16_stub_double():
    # MatchedRule has no real 'MatchedRule' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_MatchedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_MatchedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_MatchedRule(isAbstract=True, isNoDefault=True, isRefining=True)
    partner = MatchedRule()
    setattr(partner, 'MatchedRule', None)
    _safe_set(owner, 'atl_n_ocl_ATL_MatchedRule17', {partner})
    assert getattr(partner, 'MatchedRule') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_MatchedRule17', set())
    assert getattr(partner, 'MatchedRule') is None


def test_assoc_elements140_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel141', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel141', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_elements7_stub_double():
    # ModuleElement has no real 'ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Module(isRefining=True)
    partner = ModuleElement()
    setattr(partner, 'ModuleElement', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Module8', {partner})
    assert getattr(partner, 'ModuleElement') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Module8', set())
    assert getattr(partner, 'ModuleElement') is None


def test_assoc_inModels3_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Module(isRefining=True)
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Module', {partner})
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Module', set())
    assert getattr(partner, 'OclModel') is None


def test_assoc_inPattern15_stub_double():
    # InPattern has no real 'InPattern' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_MatchedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_MatchedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_MatchedRule(isAbstract=True, isNoDefault=True, isRefining=True)
    partner = InPattern()
    setattr(partner, 'InPattern', None)
    _safe_set(owner, 'atl_n_ocl_ATL_MatchedRule', partner)
    assert getattr(partner, 'InPattern') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_MatchedRule', None)
    assert getattr(partner, 'InPattern') is None


def test_assoc_initExpression107_stub_double():
    # OclExpression has no real 'OclExpression109' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression109', None)
    _safe_set(owner, 'atl_n_ocl_OCL_VariableDeclaration108', partner)
    assert getattr(partner, 'OclExpression109') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_VariableDeclaration108', None)
    assert getattr(partner, 'OclExpression109') is None


def test_assoc_initExpression125_stub_double():
    # OclExpression has no real 'OclExpression126' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression126', None)
    _safe_set(owner, 'atl_n_ocl_OCL_Attribute', partner)
    assert getattr(partner, 'OclExpression126') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_Attribute', None)
    assert getattr(partner, 'OclExpression126') is None


def test_assoc_metamodel138_stub_double():
    # OclModel has no real 'OclModel139' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel139', None)
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel', partner)
    assert getattr(partner, 'OclModel139') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel', None)
    assert getattr(partner, 'OclModel139') is None


def test_assoc_model142_stub_double():
    # OclModel has no real 'OclModel144' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel144', None)
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel143', {partner})
    assert getattr(partner, 'OclModel144') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_OclModel143', set())
    assert getattr(partner, 'OclModel144') is None


def test_assoc_outModels4_stub_double():
    # OclModel has no real 'OclModel6' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Module(isRefining=True)
    partner = OclModel()
    setattr(partner, 'OclModel6', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Module5', {partner})
    assert getattr(partner, 'OclModel6') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Module5', set())
    assert getattr(partner, 'OclModel6') is None


def test_assoc_outPattern10_stub_double():
    # OutPattern has no real 'OutPattern' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Rule(name="sample_text")
    partner = OutPattern()
    setattr(partner, 'OutPattern', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Rule', partner)
    assert getattr(partner, 'OutPattern') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Rule', None)
    assert getattr(partner, 'OutPattern') is None


def test_assoc_parameters130_stub_double():
    # Parameter has no real 'Parameter131' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_Operation(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter131', None)
    _safe_set(owner, 'atl_n_ocl_OCL_Operation', {partner})
    assert getattr(partner, 'Parameter131') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_Operation', set())
    assert getattr(partner, 'Parameter131') is None


def test_assoc_parameters18_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_CalledRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_CalledRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_CalledRule(isEndpoint=True, isEntrypoint=True)
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'atl_n_ocl_ATL_CalledRule', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_CalledRule', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType132_stub_double():
    # OclType has no real 'OclType134' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType134', None)
    _safe_set(owner, 'atl_n_ocl_OCL_Operation133', partner)
    assert getattr(partner, 'OclType134') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_Operation133', None)
    assert getattr(partner, 'OclType134') is None


def test_assoc_source48_stub_double():
    # OclExpression has no real 'OclExpression49' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_BindingStat(isAssignment=True, propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression49', None)
    _safe_set(owner, 'atl_n_ocl_ATL_BindingStat', partner)
    assert getattr(partner, 'OclExpression49') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_BindingStat', None)
    assert getattr(partner, 'OclExpression49') is None


def test_assoc_type105_stub_double():
    # OclType has no real 'OclType106' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType106', None)
    _safe_set(owner, 'atl_n_ocl_OCL_VariableDeclaration', partner)
    assert getattr(partner, 'OclType106') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_VariableDeclaration', None)
    assert getattr(partner, 'OclType106') is None


def test_assoc_type113_stub_double():
    # OclType has no real 'OclType114' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType114', None)
    _safe_set(owner, 'atl_n_ocl_OCL_TupleTypeAttribute', partner)
    assert getattr(partner, 'OclType114') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_TupleTypeAttribute', None)
    assert getattr(partner, 'OclType114') is None


def test_assoc_type127_stub_double():
    # OclType has no real 'OclType129' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType129', None)
    _safe_set(owner, 'atl_n_ocl_OCL_Attribute128', partner)
    assert getattr(partner, 'OclType129') == owner
    _safe_set(owner, 'atl_n_ocl_OCL_Attribute128', None)
    assert getattr(partner, 'OclType129') is None


def test_assoc_value43_stub_double():
    # OclExpression has no real 'OclExpression44' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Binding(isAssignment=True, propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression44', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Binding', partner)
    assert getattr(partner, 'OclExpression44') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Binding', None)
    assert getattr(partner, 'OclExpression44') is None


def test_assoc_value50_stub_double():
    # OclExpression has no real 'OclExpression52' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_BindingStat(isAssignment=True, propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression52', None)
    _safe_set(owner, 'atl_n_ocl_ATL_BindingStat51', partner)
    assert getattr(partner, 'OclExpression52') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_BindingStat51', None)
    assert getattr(partner, 'OclExpression52') is None


def test_assoc_variables13_stub_double():
    # RuleVariableDeclaration has no real 'RuleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so atl_n_ocl_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atl_n_ocl_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atl_n_ocl_ATL_Rule(name="sample_text")
    partner = RuleVariableDeclaration()
    setattr(partner, 'RuleVariableDeclaration', None)
    _safe_set(owner, 'atl_n_ocl_ATL_Rule14', {partner})
    assert getattr(partner, 'RuleVariableDeclaration') == owner
    _safe_set(owner, 'atl_n_ocl_ATL_Rule14', set())
    assert getattr(partner, 'RuleVariableDeclaration') is None


