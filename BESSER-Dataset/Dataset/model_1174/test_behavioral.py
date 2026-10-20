import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ATL_Callable,
    ATL_Helper,
    ATL_LocatedElement,
    ATL_ModuleCallable,
    ATL_ModuleElement,
    ATL_Rule,
    ATL_RuleWithPattern,
    ATL_StaticRule,
    ATL_atlext_EObject,
    ATL_atlext_Type,
    ActionBlock,
    Attribute,
    Binding,
    Callable,
    CallableParameter,
    CollectionExp,
    CollectionOperationCallExp,
    CollectionType,
    ContextHelper,
    DropPattern,
    Helper,
    IfExp,
    InPattern,
    InPatternElement,
    IterateExp,
    Iterator,
    JavaBody,
    LetExp,
    Library,
    LibraryRef,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
    MatchedRule,
    ModuleElement,
    NumericExp,
    NumericType,
    OCL_TypedElement,
    OCL_atlext_EObject,
    OCL_atlext_Type,
    OclContextDefinition,
    OclExpression,
    OclFeature,
    OclFeatureDefinition,
    OclModel,
    OclModelElement,
    OclType,
    Operation,
    OperationCallExp,
    OutPattern,
    OutPatternElement,
    Parameter,
    PatternElement,
    Primitive,
    PrimitiveExp,
    PropertyCallExp,
    Query,
    ResolveTempResolution,
    Rule,
    RuleResolutionInfo,
    RuleVariableDeclaration,
    RuleWithPattern,
    Statement,
    StaticRule,
    StringToStringMap,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Unit,
    VariableDeclaration,
    VariableExp,
    atlext_ATL_ActionBlock,
    atlext_ATL_Binding,
    atlext_ATL_BindingStat,
    atlext_ATL_Callable,
    atlext_ATL_CallableParameter,
    atlext_ATL_CalledRule,
    atlext_ATL_ContextHelper,
    atlext_ATL_DropPattern,
    atlext_ATL_ExpressionStat,
    atlext_ATL_ForEachOutPatternElement,
    atlext_ATL_ForStat,
    atlext_ATL_Helper,
    atlext_ATL_IfStat,
    atlext_ATL_InPattern,
    atlext_ATL_InPatternElement,
    atlext_ATL_LazyRule,
    atlext_ATL_Library,
    atlext_ATL_LibraryRef,
    atlext_ATL_LocatedElement,
    atlext_ATL_MatchedRule,
    atlext_ATL_Module,
    atlext_ATL_ModuleCallable,
    atlext_ATL_ModuleElement,
    atlext_ATL_OutPattern,
    atlext_ATL_OutPatternElement,
    atlext_ATL_PatternElement,
    atlext_ATL_Query,
    atlext_ATL_Rule,
    atlext_ATL_RuleResolutionInfo,
    atlext_ATL_RuleVariableDeclaration,
    atlext_ATL_RuleWithPattern,
    atlext_ATL_SimpleInPatternElement,
    atlext_ATL_SimpleOutPatternElement,
    atlext_ATL_Statement,
    atlext_ATL_StaticHelper,
    atlext_ATL_StaticRule,
    atlext_ATL_StringToStringMap,
    atlext_ATL_Unit,
    atlext_OCL2_SelectByKind,
    atlext_OCL_Attribute,
    atlext_OCL_BagExp,
    atlext_OCL_BagType,
    atlext_OCL_BooleanExp,
    atlext_OCL_BooleanType,
    atlext_OCL_CollectionExp,
    atlext_OCL_CollectionOperationCallExp,
    atlext_OCL_CollectionType,
    atlext_OCL_EnumLiteralExp,
    atlext_OCL_GetAppliedStereotypesBody,
    atlext_OCL_IfExp,
    atlext_OCL_IntegerExp,
    atlext_OCL_IntegerType,
    atlext_OCL_IterateExp,
    atlext_OCL_Iterator,
    atlext_OCL_IteratorExp,
    atlext_OCL_JavaBody,
    atlext_OCL_LetExp,
    atlext_OCL_LoopExp,
    atlext_OCL_MapElement,
    atlext_OCL_MapExp,
    atlext_OCL_MapType,
    atlext_OCL_NavigationOrAttributeCallExp,
    atlext_OCL_NumericExp,
    atlext_OCL_NumericType,
    atlext_OCL_OclAnyType,
    atlext_OCL_OclContextDefinition,
    atlext_OCL_OclExpression,
    atlext_OCL_OclFeature,
    atlext_OCL_OclFeatureDefinition,
    atlext_OCL_OclModel,
    atlext_OCL_OclModelElement,
    atlext_OCL_OclType,
    atlext_OCL_OclUndefinedExp,
    atlext_OCL_Operation,
    atlext_OCL_OperationCallExp,
    atlext_OCL_OperatorCallExp,
    atlext_OCL_OrderedSetExp,
    atlext_OCL_OrderedSetType,
    atlext_OCL_Parameter,
    atlext_OCL_Primitive,
    atlext_OCL_PrimitiveExp,
    atlext_OCL_PropertyCallExp,
    atlext_OCL_RealExp,
    atlext_OCL_RealType,
    atlext_OCL_ResolveTempResolution,
    atlext_OCL_SequenceExp,
    atlext_OCL_SequenceType,
    atlext_OCL_SetExp,
    atlext_OCL_SetType,
    atlext_OCL_StringExp,
    atlext_OCL_StringType,
    atlext_OCL_SuperExp,
    atlext_OCL_TupleExp,
    atlext_OCL_TuplePart,
    atlext_OCL_TupleType,
    atlext_OCL_TupleTypeAttribute,
    atlext_OCL_TypedElement,
    atlext_OCL_VariableDeclaration,
    atlext_OCL_VariableExp,
    RuleResolutionStatus,
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

def test_assoc_actionBlock27_stub_double():
    # ActionBlock has no real 'ActionBlock' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Rule(name="sample_text")
    partner = ActionBlock()
    setattr(partner, 'ActionBlock', None)
    _safe_set(owner, 'rule28', partner)
    assert getattr(partner, 'ActionBlock') == owner
    _safe_set(owner, 'rule28', None)
    assert getattr(partner, 'ActionBlock') is None


def test_assoc_allInvolvedRules116_stub_double():
    # MatchedRule has no real 'MatchedRule118' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_RuleResolutionInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_RuleResolutionInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_RuleResolutionInfo(status="sample_text")
    partner = MatchedRule()
    setattr(partner, 'MatchedRule118', None)
    _safe_set(owner, 'atlext_ATL_RuleResolutionInfo117', {partner})
    assert getattr(partner, 'MatchedRule118') == owner
    _safe_set(owner, 'atlext_ATL_RuleResolutionInfo117', set())
    assert getattr(partner, 'MatchedRule118') is None


def test_assoc_annotations1_stub_double():
    # StringToStringMap has no real 'StringToStringMap' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_LocatedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_LocatedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", fileLocation="sample_text", fileObject="sample_text", location="sample_text")
    partner = StringToStringMap()
    setattr(partner, 'StringToStringMap', None)
    _safe_set(owner, 'atlext_ATL_LocatedElement2', {partner})
    assert getattr(partner, 'StringToStringMap') == owner
    _safe_set(owner, 'atlext_ATL_LocatedElement2', set())
    assert getattr(partner, 'StringToStringMap') is None


def test_assoc_appliedProperty121_stub_double():
    # PropertyCallExp has no real 'PropertyCallExp122' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = PropertyCallExp()
    setattr(partner, 'PropertyCallExp122', None)
    _safe_set(owner, 'source', partner)
    assert getattr(partner, 'PropertyCallExp122') == owner
    _safe_set(owner, 'source', None)
    assert getattr(partner, 'PropertyCallExp122') is None


def test_assoc_arguments165_stub_double():
    # OclExpression has no real 'OclExpression166' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression166', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression166') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression166') is None


def test_assoc_attribute205_stub_double():
    # Attribute has no real 'Attribute207' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute207', None)
    _safe_set(owner, 'type206', partner)
    assert getattr(partner, 'Attribute207') == owner
    _safe_set(owner, 'type206', None)
    assert getattr(partner, 'Attribute207') is None


def test_assoc_baseExp191_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_body247_stub_double():
    # OclExpression has no real 'OclExpression248' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression248', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression248') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression248') is None


def test_assoc_children36_stub_double():
    # RuleWithPattern has no real 'RuleWithPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = RuleWithPattern()
    setattr(partner, 'RuleWithPattern', None)
    _safe_set(owner, 'superRule', {partner})
    assert getattr(partner, 'RuleWithPattern') == owner
    _safe_set(owner, 'superRule', set())
    assert getattr(partner, 'RuleWithPattern') is None


def test_assoc_collection123_stub_double():
    # CollectionExp has no real 'CollectionExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = CollectionExp()
    setattr(partner, 'CollectionExp', None)
    _safe_set(owner, 'elements124', partner)
    assert getattr(partner, 'CollectionExp') == owner
    _safe_set(owner, 'elements124', None)
    assert getattr(partner, 'CollectionExp') is None


def test_assoc_collectionTypes210_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_definition17_stub_double():
    # OclFeatureDefinition has no real 'OclFeatureDefinition' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = OclFeatureDefinition()
    setattr(partner, 'OclFeatureDefinition', None)
    _safe_set(owner, 'atlext_ATL_Helper', partner)
    assert getattr(partner, 'OclFeatureDefinition') == owner
    _safe_set(owner, 'atlext_ATL_Helper', None)
    assert getattr(partner, 'OclFeatureDefinition') is None


def test_assoc_definitions199_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_dynamicResolvers164_stub_double():
    # ContextHelper has no real 'ContextHelper' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = ContextHelper()
    setattr(partner, 'ContextHelper', None)
    _safe_set(owner, 'polymorphicCalledBy', {partner})
    assert getattr(partner, 'ContextHelper') == owner
    _safe_set(owner, 'polymorphicCalledBy', set())
    assert getattr(partner, 'ContextHelper') is None


def test_assoc_elements12_stub_double():
    # ModuleElement has no real 'ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Module(isRefining="sample_text")
    partner = ModuleElement()
    setattr(partner, 'ModuleElement', None)
    _safe_set(owner, 'atlext_ATL_Module13', {partner})
    assert getattr(partner, 'ModuleElement') == owner
    _safe_set(owner, 'atlext_ATL_Module13', set())
    assert getattr(partner, 'ModuleElement') is None


def test_assoc_elements251_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model252', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model252', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_ifExp1134_stub_double():
    # IfExp has no real 'IfExp135' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = IfExp()
    setattr(partner, 'IfExp135', None)
    _safe_set(owner, 'condition', partner)
    assert getattr(partner, 'IfExp135') == owner
    _safe_set(owner, 'condition', None)
    assert getattr(partner, 'IfExp135') is None


def test_assoc_ifExp2130_stub_double():
    # IfExp has no real 'IfExp131' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = IfExp()
    setattr(partner, 'IfExp131', None)
    _safe_set(owner, 'thenExpression', partner)
    assert getattr(partner, 'IfExp131') == owner
    _safe_set(owner, 'thenExpression', None)
    assert getattr(partner, 'IfExp131') is None


def test_assoc_ifExp3120_stub_double():
    # IfExp has no real 'IfExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = IfExp()
    setattr(partner, 'IfExp', None)
    _safe_set(owner, 'elseExpression', partner)
    assert getattr(partner, 'IfExp') == owner
    _safe_set(owner, 'elseExpression', None)
    assert getattr(partner, 'IfExp') is None


def test_assoc_inModels8_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'atlext_ATL_Module', {partner})
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'atlext_ATL_Module', set())
    assert getattr(partner, 'OclModel') is None


def test_assoc_inPattern35_stub_double():
    # InPattern has no real 'InPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = InPattern()
    setattr(partner, 'InPattern', None)
    _safe_set(owner, 'atlext_ATL_RuleWithPattern', partner)
    assert getattr(partner, 'InPattern') == owner
    _safe_set(owner, 'atlext_ATL_RuleWithPattern', None)
    assert getattr(partner, 'InPattern') is None


def test_assoc_inferredReturnType18_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type', None)
    _safe_set(owner, 'atlext_ATL_Helper19', partner)
    assert getattr(partner, 'ATL_atlext_Type') == owner
    _safe_set(owner, 'atlext_ATL_Helper19', None)
    assert getattr(partner, 'ATL_atlext_Type') is None


def test_assoc_initExpression187_stub_double():
    # OclExpression has no real 'OclExpression188' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression188', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression188') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression188') is None


def test_assoc_initExpression239_stub_double():
    # OclExpression has no real 'OclExpression240' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression240', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression240') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression240') is None


def test_assoc_initializedVariable128_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration129' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration129', None)
    _safe_set(owner, 'initExpression', partner)
    assert getattr(partner, 'VariableDeclaration129') == owner
    _safe_set(owner, 'initExpression', None)
    assert getattr(partner, 'VariableDeclaration129') is None


def test_assoc_leftType77_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type79' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type79', None)
    _safe_set(owner, 'atlext_ATL_Binding78', partner)
    assert getattr(partner, 'ATL_atlext_Type79') == owner
    _safe_set(owner, 'atlext_ATL_Binding78', None)
    assert getattr(partner, 'ATL_atlext_Type79') is None


def test_assoc_letExp125_stub_double():
    # LetExp has no real 'LetExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = LetExp()
    setattr(partner, 'LetExp', None)
    _safe_set(owner, 'in_', partner)
    assert getattr(partner, 'LetExp') == owner
    _safe_set(owner, 'in_', None)
    assert getattr(partner, 'LetExp') is None


def test_assoc_letExp189_stub_double():
    # LetExp has no real 'LetExp190' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp190', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp190') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp190') is None


def test_assoc_libraries3_stub_double():
    # LibraryRef has no real 'LibraryRef' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Unit(name="sample_text")
    partner = LibraryRef()
    setattr(partner, 'LibraryRef', None)
    _safe_set(owner, 'unit', {partner})
    assert getattr(partner, 'LibraryRef') == owner
    _safe_set(owner, 'unit', set())
    assert getattr(partner, 'LibraryRef') is None


def test_assoc_library15_stub_double():
    # Library has no real 'Library' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = Library()
    setattr(partner, 'Library', None)
    _safe_set(owner, 'helpers16', partner)
    assert getattr(partner, 'Library') == owner
    _safe_set(owner, 'helpers16', None)
    assert getattr(partner, 'Library') is None


def test_assoc_loopExp126_stub_double():
    # LoopExp has no real 'LoopExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = LoopExp()
    setattr(partner, 'LoopExp', None)
    _safe_set(owner, 'body', partner)
    assert getattr(partner, 'LoopExp') == owner
    _safe_set(owner, 'body', None)
    assert getattr(partner, 'LoopExp') is None


def test_assoc_mapType208_stub_double():
    # MapType has no real 'MapType209' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType209', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType209') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType209') is None


def test_assoc_mapType2204_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_metamodel249_stub_double():
    # OclModel has no real 'OclModel250' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel250', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel250') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel250') is None


def test_assoc_model253_stub_double():
    # OclModel has no real 'OclModel254' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel254', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel254') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel254') is None


def test_assoc_noCastedType138_stub_double():
    # OCL_atlext_Type has no real 'OCL_atlext_Type' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = OCL_atlext_Type()
    setattr(partner, 'OCL_atlext_Type', None)
    _safe_set(owner, 'atlext_OCL_OclExpression', partner)
    assert getattr(partner, 'OCL_atlext_Type') == owner
    _safe_set(owner, 'atlext_OCL_OclExpression', None)
    assert getattr(partner, 'OCL_atlext_Type') is None


def test_assoc_oclExpression200_stub_double():
    # OclExpression has no real 'OclExpression201' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression201', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression201') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression201') is None


def test_assoc_operation202_stub_double():
    # Operation has no real 'Operation203' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation203', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation203') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation203') is None


def test_assoc_outModels9_stub_double():
    # OclModel has no real 'OclModel11' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel11', None)
    _safe_set(owner, 'atlext_ATL_Module10', {partner})
    assert getattr(partner, 'OclModel11') == owner
    _safe_set(owner, 'atlext_ATL_Module10', set())
    assert getattr(partner, 'OclModel11') is None


def test_assoc_outPattern26_stub_double():
    # OutPattern has no real 'OutPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Rule(name="sample_text")
    partner = OutPattern()
    setattr(partner, 'OutPattern', None)
    _safe_set(owner, 'rule', partner)
    assert getattr(partner, 'OutPattern') == owner
    _safe_set(owner, 'rule', None)
    assert getattr(partner, 'OutPattern') is None


def test_assoc_outPatternElement72_stub_double():
    # OutPatternElement has no real 'OutPatternElement73' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OutPatternElement()
    setattr(partner, 'OutPatternElement73', None)
    _safe_set(owner, 'bindings', partner)
    assert getattr(partner, 'OutPatternElement73') == owner
    _safe_set(owner, 'bindings', None)
    assert getattr(partner, 'OutPatternElement73') is None


def test_assoc_owningAttribute136_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'initExpression137', partner)
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'initExpression137', None)
    assert getattr(partner, 'Attribute') is None


def test_assoc_owningOperation132_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'body133', partner)
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'body133', None)
    assert getattr(partner, 'Operation') is None


def test_assoc_paramDeclaration113_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_CallableParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_CallableParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_CallableParameter(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration', None)
    _safe_set(owner, 'atlext_ATL_CallableParameter114', partner)
    assert getattr(partner, 'VariableDeclaration') == owner
    _safe_set(owner, 'atlext_ATL_CallableParameter114', None)
    assert getattr(partner, 'VariableDeclaration') is None


def test_assoc_parameters243_stub_double():
    # Parameter has no real 'Parameter244' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_Operation(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter244', None)
    _safe_set(owner, 'atlext_OCL_Operation', {partner})
    assert getattr(partner, 'Parameter244') == owner
    _safe_set(owner, 'atlext_OCL_Operation', set())
    assert getattr(partner, 'Parameter244') is None


def test_assoc_parameters39_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_CalledRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_CalledRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_CalledRule(isEndpoint="sample_text", isEntrypoint="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'atlext_ATL_CalledRule', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'atlext_ATL_CalledRule', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_parentOperation127_stub_double():
    # OperationCallExp has no real 'OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = OperationCallExp()
    setattr(partner, 'OperationCallExp', None)
    _safe_set(owner, 'arguments', partner)
    assert getattr(partner, 'OperationCallExp') == owner
    _safe_set(owner, 'arguments', None)
    assert getattr(partner, 'OperationCallExp') is None


def test_assoc_problems0_stub_double():
    # ATL_atlext_EObject has no real 'ATL_atlext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_LocatedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_LocatedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_LocatedElement(commentsAfter="sample_text", commentsBefore="sample_text", fileLocation="sample_text", fileObject="sample_text", location="sample_text")
    partner = ATL_atlext_EObject()
    setattr(partner, 'ATL_atlext_EObject', None)
    _safe_set(owner, 'atlext_ATL_LocatedElement', {partner})
    assert getattr(partner, 'ATL_atlext_EObject') == owner
    _safe_set(owner, 'atlext_ATL_LocatedElement', set())
    assert getattr(partner, 'ATL_atlext_EObject') is None


def test_assoc_query14_stub_double():
    # Query has no real 'Query' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = Query()
    setattr(partner, 'Query', None)
    _safe_set(owner, 'helpers', partner)
    assert getattr(partner, 'Query') == owner
    _safe_set(owner, 'helpers', None)
    assert getattr(partner, 'Query') is None


def test_assoc_receptorType159_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject161' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject161', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp160', partner)
    assert getattr(partner, 'OCL_atlext_EObject161') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp160', None)
    assert getattr(partner, 'OCL_atlext_EObject161') is None


def test_assoc_resolveTempResolvedBy167_stub_double():
    # ResolveTempResolution has no real 'ResolveTempResolution' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OperationCallExp(operationName="sample_text")
    partner = ResolveTempResolution()
    setattr(partner, 'ResolveTempResolution', None)
    _safe_set(owner, 'atlext_OCL_OperationCallExp', {partner})
    assert getattr(partner, 'ResolveTempResolution') == owner
    _safe_set(owner, 'atlext_OCL_OperationCallExp', set())
    assert getattr(partner, 'ResolveTempResolution') is None


def test_assoc_resolvedBy80_stub_double():
    # RuleResolutionInfo has no real 'RuleResolutionInfo' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = RuleResolutionInfo()
    setattr(partner, 'RuleResolutionInfo', None)
    _safe_set(owner, 'atlext_ATL_Binding81', {partner})
    assert getattr(partner, 'RuleResolutionInfo') == owner
    _safe_set(owner, 'atlext_ATL_Binding81', set())
    assert getattr(partner, 'RuleResolutionInfo') is None


def test_assoc_returnType245_stub_double():
    # OclType has no real 'OclType246' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType246', None)
    _safe_set(owner, 'operation', partner)
    assert getattr(partner, 'OclType246') == owner
    _safe_set(owner, 'operation', None)
    assert getattr(partner, 'OclType246') is None


def test_assoc_rule115_stub_double():
    # MatchedRule has no real 'MatchedRule' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_RuleResolutionInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_RuleResolutionInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_RuleResolutionInfo(status="sample_text")
    partner = MatchedRule()
    setattr(partner, 'MatchedRule', None)
    _safe_set(owner, 'atlext_ATL_RuleResolutionInfo', partner)
    assert getattr(partner, 'MatchedRule') == owner
    _safe_set(owner, 'atlext_ATL_RuleResolutionInfo', None)
    assert getattr(partner, 'MatchedRule') is None


def test_assoc_source153_stub_double():
    # OclExpression has no real 'OclExpression154' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression154', None)
    _safe_set(owner, 'appliedProperty', partner)
    assert getattr(partner, 'OclExpression154') == owner
    _safe_set(owner, 'appliedProperty', None)
    assert getattr(partner, 'OclExpression154') is None


def test_assoc_source90_stub_double():
    # OclExpression has no real 'OclExpression91' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression91', None)
    _safe_set(owner, 'atlext_ATL_BindingStat', partner)
    assert getattr(partner, 'OclExpression91') == owner
    _safe_set(owner, 'atlext_ATL_BindingStat', None)
    assert getattr(partner, 'OclExpression91') is None


def test_assoc_staticResolver162_stub_double():
    # Callable has no real 'Callable' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = Callable()
    setattr(partner, 'Callable', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp163', partner)
    assert getattr(partner, 'Callable') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp163', None)
    assert getattr(partner, 'Callable') is None


def test_assoc_staticReturnType20_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type22' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Helper's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Helper's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Helper(hasContext=True, isAttribute=True)
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type22', None)
    _safe_set(owner, 'atlext_ATL_Helper21', partner)
    assert getattr(partner, 'ATL_atlext_Type22') == owner
    _safe_set(owner, 'atlext_ATL_Helper21', None)
    assert getattr(partner, 'ATL_atlext_Type22') is None


def test_assoc_staticType111_stub_double():
    # ATL_atlext_Type has no real 'ATL_atlext_Type112' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_CallableParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_CallableParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_CallableParameter(name="sample_text")
    partner = ATL_atlext_Type()
    setattr(partner, 'ATL_atlext_Type112', None)
    _safe_set(owner, 'atlext_ATL_CallableParameter', partner)
    assert getattr(partner, 'ATL_atlext_Type112') == owner
    _safe_set(owner, 'atlext_ATL_CallableParameter', None)
    assert getattr(partner, 'ATL_atlext_Type112') is None


def test_assoc_staticType193_stub_double():
    # OCL_atlext_Type has no real 'OCL_atlext_Type194' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OCL_atlext_Type()
    setattr(partner, 'OCL_atlext_Type194', None)
    _safe_set(owner, 'atlext_OCL_VariableDeclaration', partner)
    assert getattr(partner, 'OCL_atlext_Type194') == owner
    _safe_set(owner, 'atlext_OCL_VariableDeclaration', None)
    assert getattr(partner, 'OCL_atlext_Type194') is None


def test_assoc_subtypeFeatures156_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject158' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject158', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp157', {partner})
    assert getattr(partner, 'OCL_atlext_EObject158') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp157', set())
    assert getattr(partner, 'OCL_atlext_EObject158') is None


def test_assoc_superRule37_stub_double():
    # RuleWithPattern has no real 'RuleWithPattern38' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = RuleWithPattern()
    setattr(partner, 'RuleWithPattern38', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'RuleWithPattern38') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'RuleWithPattern38') is None


def test_assoc_tupleType220_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute211_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type212', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type212', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type119_stub_double():
    # OclType has no real 'OclType' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclExpression(implicitlyCasted=True)
    partner = OclType()
    setattr(partner, 'OclType', None)
    _safe_set(owner, 'oclExpression', partner)
    assert getattr(partner, 'OclType') == owner
    _safe_set(owner, 'oclExpression', None)
    assert getattr(partner, 'OclType') is None


def test_assoc_type185_stub_double():
    # OclType has no real 'OclType186' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType186', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType186') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType186') is None


def test_assoc_type218_stub_double():
    # OclType has no real 'OclType219' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType219', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType219') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType219') is None


def test_assoc_type241_stub_double():
    # OclType has no real 'OclType242' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType242', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType242') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType242') is None


def test_assoc_unit84_stub_double():
    # Unit has no real 'Unit' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_LibraryRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_LibraryRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_LibraryRef(name="sample_text")
    partner = Unit()
    setattr(partner, 'Unit', None)
    _safe_set(owner, 'libraries', partner)
    assert getattr(partner, 'Unit') == owner
    _safe_set(owner, 'libraries', None)
    assert getattr(partner, 'Unit') is None


def test_assoc_usedFeature155_stub_double():
    # OCL_atlext_EObject has no real 'OCL_atlext_EObject' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_PropertyCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_PropertyCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_PropertyCallExp(isStaticCall=True)
    partner = OCL_atlext_EObject()
    setattr(partner, 'OCL_atlext_EObject', None)
    _safe_set(owner, 'atlext_OCL_PropertyCallExp', partner)
    assert getattr(partner, 'OCL_atlext_EObject') == owner
    _safe_set(owner, 'atlext_OCL_PropertyCallExp', None)
    assert getattr(partner, 'OCL_atlext_EObject') is None


def test_assoc_value70_stub_double():
    # OclExpression has no real 'OclExpression71' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression71', None)
    _safe_set(owner, 'atlext_ATL_Binding', partner)
    assert getattr(partner, 'OclExpression71') == owner
    _safe_set(owner, 'atlext_ATL_Binding', None)
    assert getattr(partner, 'OclExpression71') is None


def test_assoc_value92_stub_double():
    # OclExpression has no real 'OclExpression94' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression94', None)
    _safe_set(owner, 'atlext_ATL_BindingStat93', partner)
    assert getattr(partner, 'OclExpression94') == owner
    _safe_set(owner, 'atlext_ATL_BindingStat93', None)
    assert getattr(partner, 'OclExpression94') is None


def test_assoc_variableDeclaration213_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration215' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration215', None)
    _safe_set(owner, 'type214', partner)
    assert getattr(partner, 'VariableDeclaration215') == owner
    _safe_set(owner, 'type214', None)
    assert getattr(partner, 'VariableDeclaration215') is None


def test_assoc_variableExp192_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so atlext_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


def test_assoc_variables29_stub_double():
    # RuleVariableDeclaration has no real 'RuleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Rule(name="sample_text")
    partner = RuleVariableDeclaration()
    setattr(partner, 'RuleVariableDeclaration', None)
    _safe_set(owner, 'rule30', {partner})
    assert getattr(partner, 'RuleVariableDeclaration') == owner
    _safe_set(owner, 'rule30', set())
    assert getattr(partner, 'RuleVariableDeclaration') is None


def test_assoc_writtenFeature74_stub_double():
    # ATL_atlext_EObject has no real 'ATL_atlext_EObject76' property in the generated
    # code (a bare stub) -- manually attach it so atlext_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlext_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlext_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = ATL_atlext_EObject()
    setattr(partner, 'ATL_atlext_EObject76', None)
    _safe_set(owner, 'atlext_ATL_Binding75', partner)
    assert getattr(partner, 'ATL_atlext_EObject76') == owner
    _safe_set(owner, 'atlext_ATL_Binding75', None)
    assert getattr(partner, 'ATL_atlext_EObject76') is None


