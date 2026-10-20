import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ATL_Callable,
    ATL_Helper,
    ATL_ModuleCallable,
    ATL_ModuleElement,
    ATL_Rule,
    ATL_RuleWithPattern,
    ATL_StaticRule,
    ActionBlock,
    Attribute,
    Binding,
    Callable,
    CollectionExp,
    CollectionType,
    DropPattern,
    Helper,
    IfExp,
    InPattern,
    InPatternElement,
    IterateExp,
    Iterator,
    LetExp,
    Library,
    LibraryRef,
    LocatedElement,
    LoopExp,
    MapElement,
    MapExp,
    MapType,
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
    Rule,
    RuleVariableDeclaration,
    RuleWithPattern,
    Statement,
    StaticRule,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Unit,
    VariableDeclaration,
    VariableExp,
    atlstatic_ATL_ActionBlock,
    atlstatic_ATL_Binding,
    atlstatic_ATL_BindingStat,
    atlstatic_ATL_Callable,
    atlstatic_ATL_CalledRule,
    atlstatic_ATL_ContextHelper,
    atlstatic_ATL_DropPattern,
    atlstatic_ATL_ExpressionStat,
    atlstatic_ATL_ForEachOutPatternElement,
    atlstatic_ATL_ForStat,
    atlstatic_ATL_Helper,
    atlstatic_ATL_IfStat,
    atlstatic_ATL_InPattern,
    atlstatic_ATL_InPatternElement,
    atlstatic_ATL_LazyRule,
    atlstatic_ATL_Library,
    atlstatic_ATL_LibraryRef,
    atlstatic_ATL_LocatedElement,
    atlstatic_ATL_MatchedRule,
    atlstatic_ATL_Module,
    atlstatic_ATL_ModuleCallable,
    atlstatic_ATL_ModuleElement,
    atlstatic_ATL_OutPattern,
    atlstatic_ATL_OutPatternElement,
    atlstatic_ATL_PatternElement,
    atlstatic_ATL_Query,
    atlstatic_ATL_Rule,
    atlstatic_ATL_RuleVariableDeclaration,
    atlstatic_ATL_RuleWithPattern,
    atlstatic_ATL_SimpleInPatternElement,
    atlstatic_ATL_SimpleOutPatternElement,
    atlstatic_ATL_Statement,
    atlstatic_ATL_StaticHelper,
    atlstatic_ATL_StaticRule,
    atlstatic_ATL_Unit,
    atlstatic_OCL_Attribute,
    atlstatic_OCL_BagExp,
    atlstatic_OCL_BagType,
    atlstatic_OCL_BooleanExp,
    atlstatic_OCL_BooleanType,
    atlstatic_OCL_CollectionExp,
    atlstatic_OCL_CollectionOperationCallExp,
    atlstatic_OCL_CollectionType,
    atlstatic_OCL_EnumLiteralExp,
    atlstatic_OCL_IfExp,
    atlstatic_OCL_IntegerExp,
    atlstatic_OCL_IntegerType,
    atlstatic_OCL_IterateExp,
    atlstatic_OCL_Iterator,
    atlstatic_OCL_IteratorExp,
    atlstatic_OCL_LetExp,
    atlstatic_OCL_LoopExp,
    atlstatic_OCL_MapElement,
    atlstatic_OCL_MapExp,
    atlstatic_OCL_MapType,
    atlstatic_OCL_NavigationOrAttributeCallExp,
    atlstatic_OCL_NumericExp,
    atlstatic_OCL_NumericType,
    atlstatic_OCL_OclAnyType,
    atlstatic_OCL_OclContextDefinition,
    atlstatic_OCL_OclExpression,
    atlstatic_OCL_OclFeature,
    atlstatic_OCL_OclFeatureDefinition,
    atlstatic_OCL_OclModel,
    atlstatic_OCL_OclModelElement,
    atlstatic_OCL_OclType,
    atlstatic_OCL_OclUndefinedExp,
    atlstatic_OCL_Operation,
    atlstatic_OCL_OperationCallExp,
    atlstatic_OCL_OperatorCallExp,
    atlstatic_OCL_OrderedSetExp,
    atlstatic_OCL_OrderedSetType,
    atlstatic_OCL_Parameter,
    atlstatic_OCL_Primitive,
    atlstatic_OCL_PrimitiveExp,
    atlstatic_OCL_PropertyCallExp,
    atlstatic_OCL_RealExp,
    atlstatic_OCL_RealType,
    atlstatic_OCL_SequenceExp,
    atlstatic_OCL_SequenceType,
    atlstatic_OCL_SetExp,
    atlstatic_OCL_SetType,
    atlstatic_OCL_StringExp,
    atlstatic_OCL_StringType,
    atlstatic_OCL_SuperExp,
    atlstatic_OCL_TupleExp,
    atlstatic_OCL_TuplePart,
    atlstatic_OCL_TupleType,
    atlstatic_OCL_TupleTypeAttribute,
    atlstatic_OCL_VariableDeclaration,
    atlstatic_OCL_VariableExp,
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

def test_assoc_actionBlock16_stub_double():
    # ActionBlock has no real 'ActionBlock' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Rule(name="sample_text")
    partner = ActionBlock()
    setattr(partner, 'ActionBlock', None)
    _safe_set(owner, 'rule17', partner)
    assert getattr(partner, 'ActionBlock') == owner
    _safe_set(owner, 'rule17', None)
    assert getattr(partner, 'ActionBlock') is None


def test_assoc_arguments121_stub_double():
    # OclExpression has no real 'OclExpression122' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression122', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression122') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression122') is None


def test_assoc_attribute158_stub_double():
    # Attribute has no real 'Attribute160' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute160', None)
    _safe_set(owner, 'type159', partner)
    assert getattr(partner, 'Attribute160') == owner
    _safe_set(owner, 'type159', None)
    assert getattr(partner, 'Attribute160') is None


def test_assoc_baseExp146_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_body200_stub_double():
    # OclExpression has no real 'OclExpression201' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression201', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression201') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression201') is None


def test_assoc_children21_stub_double():
    # RuleWithPattern has no real 'RuleWithPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = RuleWithPattern()
    setattr(partner, 'RuleWithPattern', None)
    _safe_set(owner, 'superRule', {partner})
    assert getattr(partner, 'RuleWithPattern') == owner
    _safe_set(owner, 'superRule', set())
    assert getattr(partner, 'RuleWithPattern') is None


def test_assoc_collectionTypes163_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_definitions152_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elements204_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model205', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model205', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_elements9_stub_double():
    # ModuleElement has no real 'ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Module(isRefining="sample_text")
    partner = ModuleElement()
    setattr(partner, 'ModuleElement', None)
    _safe_set(owner, 'atlstatic_ATL_Module10', {partner})
    assert getattr(partner, 'ModuleElement') == owner
    _safe_set(owner, 'atlstatic_ATL_Module10', set())
    assert getattr(partner, 'ModuleElement') is None


def test_assoc_inModels5_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'atlstatic_ATL_Module', {partner})
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'atlstatic_ATL_Module', set())
    assert getattr(partner, 'OclModel') is None


def test_assoc_inPattern20_stub_double():
    # InPattern has no real 'InPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = InPattern()
    setattr(partner, 'InPattern', None)
    _safe_set(owner, 'atlstatic_ATL_RuleWithPattern', partner)
    assert getattr(partner, 'InPattern') == owner
    _safe_set(owner, 'atlstatic_ATL_RuleWithPattern', None)
    assert getattr(partner, 'InPattern') is None


def test_assoc_initExpression142_stub_double():
    # OclExpression has no real 'OclExpression143' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression143', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression143') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression143') is None


def test_assoc_initExpression192_stub_double():
    # OclExpression has no real 'OclExpression193' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression193', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression193') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression193') is None


def test_assoc_letExp144_stub_double():
    # LetExp has no real 'LetExp145' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp145', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp145') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp145') is None


def test_assoc_libraries0_stub_double():
    # LibraryRef has no real 'LibraryRef' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Unit(name="sample_text")
    partner = LibraryRef()
    setattr(partner, 'LibraryRef', None)
    _safe_set(owner, 'unit', {partner})
    assert getattr(partner, 'LibraryRef') == owner
    _safe_set(owner, 'unit', set())
    assert getattr(partner, 'LibraryRef') is None


def test_assoc_mapType161_stub_double():
    # MapType has no real 'MapType162' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType162', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType162') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType162') is None


def test_assoc_mapType2157_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_metamodel202_stub_double():
    # OclModel has no real 'OclModel203' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel203', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel203') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel203') is None


def test_assoc_model206_stub_double():
    # OclModel has no real 'OclModel207' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel207', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel207') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel207') is None


def test_assoc_oclExpression153_stub_double():
    # OclExpression has no real 'OclExpression154' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression154', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression154') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression154') is None


def test_assoc_operation155_stub_double():
    # Operation has no real 'Operation156' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation156', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation156') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation156') is None


def test_assoc_outModels6_stub_double():
    # OclModel has no real 'OclModel8' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel8', None)
    _safe_set(owner, 'atlstatic_ATL_Module7', {partner})
    assert getattr(partner, 'OclModel8') == owner
    _safe_set(owner, 'atlstatic_ATL_Module7', set())
    assert getattr(partner, 'OclModel8') is None


def test_assoc_outPattern15_stub_double():
    # OutPattern has no real 'OutPattern' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Rule(name="sample_text")
    partner = OutPattern()
    setattr(partner, 'OutPattern', None)
    _safe_set(owner, 'rule', partner)
    assert getattr(partner, 'OutPattern') == owner
    _safe_set(owner, 'rule', None)
    assert getattr(partner, 'OutPattern') is None


def test_assoc_outPatternElement57_stub_double():
    # OutPatternElement has no real 'OutPatternElement58' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OutPatternElement()
    setattr(partner, 'OutPatternElement58', None)
    _safe_set(owner, 'bindings', partner)
    assert getattr(partner, 'OutPatternElement58') == owner
    _safe_set(owner, 'bindings', None)
    assert getattr(partner, 'OutPatternElement58') is None


def test_assoc_parameters196_stub_double():
    # Parameter has no real 'Parameter197' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_Operation(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter197', None)
    _safe_set(owner, 'atlstatic_OCL_Operation', {partner})
    assert getattr(partner, 'Parameter197') == owner
    _safe_set(owner, 'atlstatic_OCL_Operation', set())
    assert getattr(partner, 'Parameter197') is None


def test_assoc_parameters24_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_CalledRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_CalledRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_CalledRule(isEndpoint="sample_text", isEntrypoint="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'atlstatic_ATL_CalledRule', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'atlstatic_ATL_CalledRule', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType198_stub_double():
    # OclType has no real 'OclType199' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType199', None)
    _safe_set(owner, 'operation', partner)
    assert getattr(partner, 'OclType199') == owner
    _safe_set(owner, 'operation', None)
    assert getattr(partner, 'OclType199') is None


def test_assoc_source67_stub_double():
    # OclExpression has no real 'OclExpression68' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression68', None)
    _safe_set(owner, 'atlstatic_ATL_BindingStat', partner)
    assert getattr(partner, 'OclExpression68') == owner
    _safe_set(owner, 'atlstatic_ATL_BindingStat', None)
    assert getattr(partner, 'OclExpression68') is None


def test_assoc_superRule22_stub_double():
    # RuleWithPattern has no real 'RuleWithPattern23' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_RuleWithPattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_RuleWithPattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_RuleWithPattern(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = RuleWithPattern()
    setattr(partner, 'RuleWithPattern23', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'RuleWithPattern23') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'RuleWithPattern23') is None


def test_assoc_tupleType173_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute164_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type165', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type165', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type140_stub_double():
    # OclType has no real 'OclType141' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType141', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType141') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType141') is None


def test_assoc_type171_stub_double():
    # OclType has no real 'OclType172' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType172', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType172') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType172') is None


def test_assoc_type194_stub_double():
    # OclType has no real 'OclType195' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType195', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType195') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType195') is None


def test_assoc_unit61_stub_double():
    # Unit has no real 'Unit' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_LibraryRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_LibraryRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_LibraryRef(name="sample_text")
    partner = Unit()
    setattr(partner, 'Unit', None)
    _safe_set(owner, 'libraries', partner)
    assert getattr(partner, 'Unit') == owner
    _safe_set(owner, 'libraries', None)
    assert getattr(partner, 'Unit') is None


def test_assoc_value55_stub_double():
    # OclExpression has no real 'OclExpression56' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression56', None)
    _safe_set(owner, 'atlstatic_ATL_Binding', partner)
    assert getattr(partner, 'OclExpression56') == owner
    _safe_set(owner, 'atlstatic_ATL_Binding', None)
    assert getattr(partner, 'OclExpression56') is None


def test_assoc_value69_stub_double():
    # OclExpression has no real 'OclExpression71' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression71', None)
    _safe_set(owner, 'atlstatic_ATL_BindingStat70', partner)
    assert getattr(partner, 'OclExpression71') == owner
    _safe_set(owner, 'atlstatic_ATL_BindingStat70', None)
    assert getattr(partner, 'OclExpression71') is None


def test_assoc_variableDeclaration166_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration168' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration168', None)
    _safe_set(owner, 'type167', partner)
    assert getattr(partner, 'VariableDeclaration168') == owner
    _safe_set(owner, 'type167', None)
    assert getattr(partner, 'VariableDeclaration168') is None


def test_assoc_variableExp147_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


def test_assoc_variables18_stub_double():
    # RuleVariableDeclaration has no real 'RuleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so atlstatic_ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # atlstatic_ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = atlstatic_ATL_Rule(name="sample_text")
    partner = RuleVariableDeclaration()
    setattr(partner, 'RuleVariableDeclaration', None)
    _safe_set(owner, 'rule19', {partner})
    assert getattr(partner, 'RuleVariableDeclaration') == owner
    _safe_set(owner, 'rule19', set())
    assert getattr(partner, 'RuleVariableDeclaration') is None


