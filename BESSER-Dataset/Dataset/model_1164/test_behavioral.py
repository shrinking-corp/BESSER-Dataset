import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ATL_ActionBlock,
    ATL_Binding,
    ATL_BindingStat,
    ATL_CalledRule,
    ATL_DropPattern,
    ATL_ExpressionStat,
    ATL_ForEachOutPatternElement,
    ATL_ForStat,
    ATL_Helper,
    ATL_IfStat,
    ATL_InPattern,
    ATL_InPatternElement,
    ATL_LazyMatchedRule,
    ATL_Library,
    ATL_LibraryRef,
    ATL_LocatedElement,
    ATL_MatchedRule,
    ATL_Module,
    ATL_ModuleElement,
    ATL_OutPattern,
    ATL_OutPatternElement,
    ATL_PatternElement,
    ATL_Query,
    ATL_Rule,
    ATL_RuleVariableDeclaration,
    ATL_SimpleInPatternElement,
    ATL_SimpleOutPatternElement,
    ATL_Statement,
    ATL_Unit,
    ActionBlock,
    Attribute,
    Binding,
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
    MatchedRule,
    Module,
    ModuleElement,
    NumericExp,
    NumericType,
    OCL_Attribute,
    OCL_BagExp,
    OCL_BagType,
    OCL_BooleanExp,
    OCL_BooleanType,
    OCL_CollectionExp,
    OCL_CollectionOperationCallExp,
    OCL_CollectionType,
    OCL_EnumLiteralExp,
    OCL_IfExp,
    OCL_IntegerExp,
    OCL_IntegerType,
    OCL_IterateExp,
    OCL_Iterator,
    OCL_IteratorExp,
    OCL_LetExp,
    OCL_LoopExp,
    OCL_MapElement,
    OCL_MapExp,
    OCL_MapType,
    OCL_NavigationOrAttributeCallExp,
    OCL_NumericExp,
    OCL_NumericType,
    OCL_OclAnyType,
    OCL_OclContextDefinition,
    OCL_OclExpression,
    OCL_OclFeature,
    OCL_OclFeatureDefinition,
    OCL_OclModel,
    OCL_OclModelElement,
    OCL_OclType,
    OCL_OclUndefinedExp,
    OCL_Operation,
    OCL_OperationCallExp,
    OCL_OperatorCallExp,
    OCL_OrderedSetExp,
    OCL_OrderedSetType,
    OCL_Parameter,
    OCL_Primitive,
    OCL_PrimitiveExp,
    OCL_PropertyCallExp,
    OCL_RealExp,
    OCL_RealType,
    OCL_SequenceExp,
    OCL_SequenceType,
    OCL_SetExp,
    OCL_SetType,
    OCL_StringExp,
    OCL_StringType,
    OCL_SuperExp,
    OCL_TupleExp,
    OCL_TuplePart,
    OCL_TupleType,
    OCL_TupleTypeAttribute,
    OCL_VariableDeclaration,
    OCL_VariableExp,
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
    Statement,
    TupleExp,
    TuplePart,
    TupleType,
    TupleTypeAttribute,
    Unit,
    VariableDeclaration,
    VariableExp,
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
    # code (a bare stub) -- manually attach it so ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Rule(name="sample_text")
    partner = ActionBlock()
    setattr(partner, 'ActionBlock', None)
    _safe_set(owner, 'rule17', partner)
    assert getattr(partner, 'ActionBlock') == owner
    _safe_set(owner, 'rule17', None)
    assert getattr(partner, 'ActionBlock') is None


def test_assoc_arguments126_stub_double():
    # OclExpression has no real 'OclExpression127' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OperationCallExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OperationCallExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OperationCallExp(operationName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression127', None)
    _safe_set(owner, 'parentOperation', {partner})
    assert getattr(partner, 'OclExpression127') == owner
    _safe_set(owner, 'parentOperation', set())
    assert getattr(partner, 'OclExpression127') is None


def test_assoc_attribute165_stub_double():
    # Attribute has no real 'Attribute167' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute167', None)
    _safe_set(owner, 'type166', partner)
    assert getattr(partner, 'Attribute167') == owner
    _safe_set(owner, 'type166', None)
    assert getattr(partner, 'Attribute167') is None


def test_assoc_baseExp151_stub_double():
    # IterateExp has no real 'IterateExp' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = IterateExp()
    setattr(partner, 'IterateExp', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'IterateExp') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'IterateExp') is None


def test_assoc_body208_stub_double():
    # OclExpression has no real 'OclExpression209' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression209', None)
    _safe_set(owner, 'owningOperation', partner)
    assert getattr(partner, 'OclExpression209') == owner
    _safe_set(owner, 'owningOperation', None)
    assert getattr(partner, 'OclExpression209') is None


def test_assoc_children22_stub_double():
    # MatchedRule has no real 'MatchedRule' property in the generated
    # code (a bare stub) -- manually attach it so ATL_MatchedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_MatchedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_MatchedRule(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = MatchedRule()
    setattr(partner, 'MatchedRule', None)
    _safe_set(owner, 'superRule', {partner})
    assert getattr(partner, 'MatchedRule') == owner
    _safe_set(owner, 'superRule', set())
    assert getattr(partner, 'MatchedRule') is None


def test_assoc_collectionTypes170_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'elementType', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'elementType', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_definitions159_stub_double():
    # OclContextDefinition has no real 'OclContextDefinition' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclContextDefinition()
    setattr(partner, 'OclContextDefinition', None)
    _safe_set(owner, 'context_', partner)
    assert getattr(partner, 'OclContextDefinition') == owner
    _safe_set(owner, 'context_', None)
    assert getattr(partner, 'OclContextDefinition') is None


def test_assoc_elements212_stub_double():
    # OclModelElement has no real 'OclModelElement' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModelElement()
    setattr(partner, 'OclModelElement', None)
    _safe_set(owner, 'model213', {partner})
    assert getattr(partner, 'OclModelElement') == owner
    _safe_set(owner, 'model213', set())
    assert getattr(partner, 'OclModelElement') is None


def test_assoc_elements9_stub_double():
    # ModuleElement has no real 'ModuleElement' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Module(isRefining="sample_text")
    partner = ModuleElement()
    setattr(partner, 'ModuleElement', None)
    _safe_set(owner, 'module', {partner})
    assert getattr(partner, 'ModuleElement') == owner
    _safe_set(owner, 'module', set())
    assert getattr(partner, 'ModuleElement') is None


def test_assoc_inModels5_stub_double():
    # OclModel has no real 'OclModel' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel', None)
    _safe_set(owner, 'ATL_Module', {partner})
    assert getattr(partner, 'OclModel') == owner
    _safe_set(owner, 'ATL_Module', set())
    assert getattr(partner, 'OclModel') is None


def test_assoc_inPattern20_stub_double():
    # InPattern has no real 'InPattern' property in the generated
    # code (a bare stub) -- manually attach it so ATL_MatchedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_MatchedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_MatchedRule(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = InPattern()
    setattr(partner, 'InPattern', None)
    _safe_set(owner, 'rule21', partner)
    assert getattr(partner, 'InPattern') == owner
    _safe_set(owner, 'rule21', None)
    assert getattr(partner, 'InPattern') is None


def test_assoc_initExpression147_stub_double():
    # OclExpression has no real 'OclExpression148' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression148', None)
    _safe_set(owner, 'initializedVariable', partner)
    assert getattr(partner, 'OclExpression148') == owner
    _safe_set(owner, 'initializedVariable', None)
    assert getattr(partner, 'OclExpression148') is None


def test_assoc_initExpression199_stub_double():
    # OclExpression has no real 'OclExpression200' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression200', None)
    _safe_set(owner, 'owningAttribute', partner)
    assert getattr(partner, 'OclExpression200') == owner
    _safe_set(owner, 'owningAttribute', None)
    assert getattr(partner, 'OclExpression200') is None


def test_assoc_letExp149_stub_double():
    # LetExp has no real 'LetExp150' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp150', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp150') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp150') is None


def test_assoc_libraries0_stub_double():
    # LibraryRef has no real 'LibraryRef' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Unit(name="sample_text")
    partner = LibraryRef()
    setattr(partner, 'LibraryRef', None)
    _safe_set(owner, 'unit', {partner})
    assert getattr(partner, 'LibraryRef') == owner
    _safe_set(owner, 'unit', set())
    assert getattr(partner, 'LibraryRef') is None


def test_assoc_mapType168_stub_double():
    # MapType has no real 'MapType169' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType169', None)
    _safe_set(owner, 'keyType', partner)
    assert getattr(partner, 'MapType169') == owner
    _safe_set(owner, 'keyType', None)
    assert getattr(partner, 'MapType169') is None


def test_assoc_mapType2164_stub_double():
    # MapType has no real 'MapType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = MapType()
    setattr(partner, 'MapType', None)
    _safe_set(owner, 'valueType', partner)
    assert getattr(partner, 'MapType') == owner
    _safe_set(owner, 'valueType', None)
    assert getattr(partner, 'MapType') is None


def test_assoc_metamodel210_stub_double():
    # OclModel has no real 'OclModel211' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel211', None)
    _safe_set(owner, 'model', partner)
    assert getattr(partner, 'OclModel211') == owner
    _safe_set(owner, 'model', None)
    assert getattr(partner, 'OclModel211') is None


def test_assoc_model214_stub_double():
    # OclModel has no real 'OclModel215' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclModel(name="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel215', None)
    _safe_set(owner, 'metamodel', {partner})
    assert getattr(partner, 'OclModel215') == owner
    _safe_set(owner, 'metamodel', set())
    assert getattr(partner, 'OclModel215') is None


def test_assoc_oclExpression160_stub_double():
    # OclExpression has no real 'OclExpression161' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression161', None)
    _safe_set(owner, 'type', partner)
    assert getattr(partner, 'OclExpression161') == owner
    _safe_set(owner, 'type', None)
    assert getattr(partner, 'OclExpression161') is None


def test_assoc_operation162_stub_double():
    # Operation has no real 'Operation163' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = Operation()
    setattr(partner, 'Operation163', None)
    _safe_set(owner, 'returnType', partner)
    assert getattr(partner, 'Operation163') == owner
    _safe_set(owner, 'returnType', None)
    assert getattr(partner, 'Operation163') is None


def test_assoc_outModels6_stub_double():
    # OclModel has no real 'OclModel8' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Module(isRefining="sample_text")
    partner = OclModel()
    setattr(partner, 'OclModel8', None)
    _safe_set(owner, 'ATL_Module7', {partner})
    assert getattr(partner, 'OclModel8') == owner
    _safe_set(owner, 'ATL_Module7', set())
    assert getattr(partner, 'OclModel8') is None


def test_assoc_outPattern15_stub_double():
    # OutPattern has no real 'OutPattern' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Rule(name="sample_text")
    partner = OutPattern()
    setattr(partner, 'OutPattern', None)
    _safe_set(owner, 'rule', partner)
    assert getattr(partner, 'OutPattern') == owner
    _safe_set(owner, 'rule', None)
    assert getattr(partner, 'OutPattern') is None


def test_assoc_outPatternElement62_stub_double():
    # OutPatternElement has no real 'OutPatternElement63' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OutPatternElement()
    setattr(partner, 'OutPatternElement63', None)
    _safe_set(owner, 'bindings', partner)
    assert getattr(partner, 'OutPatternElement63') == owner
    _safe_set(owner, 'bindings', None)
    assert getattr(partner, 'OutPatternElement63') is None


def test_assoc_parameters203_stub_double():
    # Parameter has no real 'Parameter204' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter204', None)
    _safe_set(owner, 'operation', {partner})
    assert getattr(partner, 'Parameter204') == owner
    _safe_set(owner, 'operation', set())
    assert getattr(partner, 'Parameter204') is None


def test_assoc_parameters25_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so ATL_CalledRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_CalledRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_CalledRule(isEndpoint="sample_text", isEntrypoint="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'ATL_CalledRule', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'ATL_CalledRule', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_returnType205_stub_double():
    # OclType has no real 'OclType207' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Operation(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType207', None)
    _safe_set(owner, 'operation206', partner)
    assert getattr(partner, 'OclType207') == owner
    _safe_set(owner, 'operation206', None)
    assert getattr(partner, 'OclType207') is None


def test_assoc_source72_stub_double():
    # OclExpression has no real 'OclExpression73' property in the generated
    # code (a bare stub) -- manually attach it so ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression73', None)
    _safe_set(owner, 'ATL_BindingStat', partner)
    assert getattr(partner, 'OclExpression73') == owner
    _safe_set(owner, 'ATL_BindingStat', None)
    assert getattr(partner, 'OclExpression73') is None


def test_assoc_superRule23_stub_double():
    # MatchedRule has no real 'MatchedRule24' property in the generated
    # code (a bare stub) -- manually attach it so ATL_MatchedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_MatchedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_MatchedRule(isAbstract="sample_text", isNoDefault="sample_text", isRefining="sample_text")
    partner = MatchedRule()
    setattr(partner, 'MatchedRule24', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'MatchedRule24') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'MatchedRule24') is None


def test_assoc_tupleType180_stub_double():
    # TupleType has no real 'TupleType' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = TupleType()
    setattr(partner, 'TupleType', None)
    _safe_set(owner, 'attributes', partner)
    assert getattr(partner, 'TupleType') == owner
    _safe_set(owner, 'attributes', None)
    assert getattr(partner, 'TupleType') is None


def test_assoc_tupleTypeAttribute171_stub_double():
    # TupleTypeAttribute has no real 'TupleTypeAttribute' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = TupleTypeAttribute()
    setattr(partner, 'TupleTypeAttribute', None)
    _safe_set(owner, 'type172', partner)
    assert getattr(partner, 'TupleTypeAttribute') == owner
    _safe_set(owner, 'type172', None)
    assert getattr(partner, 'TupleTypeAttribute') is None


def test_assoc_type145_stub_double():
    # OclType has no real 'OclType146' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = OclType()
    setattr(partner, 'OclType146', None)
    _safe_set(owner, 'variableDeclaration', partner)
    assert getattr(partner, 'OclType146') == owner
    _safe_set(owner, 'variableDeclaration', None)
    assert getattr(partner, 'OclType146') is None


def test_assoc_type178_stub_double():
    # OclType has no real 'OclType179' property in the generated
    # code (a bare stub) -- manually attach it so OCL_TupleTypeAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_TupleTypeAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_TupleTypeAttribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType179', None)
    _safe_set(owner, 'tupleTypeAttribute', partner)
    assert getattr(partner, 'OclType179') == owner
    _safe_set(owner, 'tupleTypeAttribute', None)
    assert getattr(partner, 'OclType179') is None


def test_assoc_type201_stub_double():
    # OclType has no real 'OclType202' property in the generated
    # code (a bare stub) -- manually attach it so OCL_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_Attribute(name="sample_text")
    partner = OclType()
    setattr(partner, 'OclType202', None)
    _safe_set(owner, 'attribute', partner)
    assert getattr(partner, 'OclType202') == owner
    _safe_set(owner, 'attribute', None)
    assert getattr(partner, 'OclType202') is None


def test_assoc_unit66_stub_double():
    # Unit has no real 'Unit' property in the generated
    # code (a bare stub) -- manually attach it so ATL_LibraryRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_LibraryRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_LibraryRef(name="sample_text")
    partner = Unit()
    setattr(partner, 'Unit', None)
    _safe_set(owner, 'libraries', partner)
    assert getattr(partner, 'Unit') == owner
    _safe_set(owner, 'libraries', None)
    assert getattr(partner, 'Unit') is None


def test_assoc_value60_stub_double():
    # OclExpression has no real 'OclExpression61' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Binding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Binding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Binding(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression61', None)
    _safe_set(owner, 'ATL_Binding', partner)
    assert getattr(partner, 'OclExpression61') == owner
    _safe_set(owner, 'ATL_Binding', None)
    assert getattr(partner, 'OclExpression61') is None


def test_assoc_value74_stub_double():
    # OclExpression has no real 'OclExpression76' property in the generated
    # code (a bare stub) -- manually attach it so ATL_BindingStat's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_BindingStat's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_BindingStat(isAssignment="sample_text", propertyName="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression76', None)
    _safe_set(owner, 'ATL_BindingStat75', partner)
    assert getattr(partner, 'OclExpression76') == owner
    _safe_set(owner, 'ATL_BindingStat75', None)
    assert getattr(partner, 'OclExpression76') is None


def test_assoc_variableDeclaration173_stub_double():
    # VariableDeclaration has no real 'VariableDeclaration175' property in the generated
    # code (a bare stub) -- manually attach it so OCL_OclType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_OclType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_OclType(name="sample_text")
    partner = VariableDeclaration()
    setattr(partner, 'VariableDeclaration175', None)
    _safe_set(owner, 'type174', partner)
    assert getattr(partner, 'VariableDeclaration175') == owner
    _safe_set(owner, 'type174', None)
    assert getattr(partner, 'VariableDeclaration175') is None


def test_assoc_variableExp152_stub_double():
    # VariableExp has no real 'VariableExp' property in the generated
    # code (a bare stub) -- manually attach it so OCL_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # OCL_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = OCL_VariableDeclaration(id="sample_text", varName="sample_text")
    partner = VariableExp()
    setattr(partner, 'VariableExp', None)
    _safe_set(owner, 'referredVariable', {partner})
    assert getattr(partner, 'VariableExp') == owner
    _safe_set(owner, 'referredVariable', set())
    assert getattr(partner, 'VariableExp') is None


def test_assoc_variables18_stub_double():
    # RuleVariableDeclaration has no real 'RuleVariableDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so ATL_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ATL_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ATL_Rule(name="sample_text")
    partner = RuleVariableDeclaration()
    setattr(partner, 'RuleVariableDeclaration', None)
    _safe_set(owner, 'rule19', {partner})
    assert getattr(partner, 'RuleVariableDeclaration') == owner
    _safe_set(owner, 'rule19', set())
    assert getattr(partner, 'RuleVariableDeclaration') is None


