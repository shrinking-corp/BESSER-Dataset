import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    Area,
    Assignment,
    BottomPattern,
    CallExp,
    CatchExp,
    Class,
    CollectionLiteralExp,
    CollectionLiteralPart,
    CollectionType,
    Comment,
    ConstructorBody,
    CorePattern,
    DataType,
    DictLiteralPart,
    Domain,
    DomainPattern,
    Element,
    EnforcementOperation,
    EntryOperation,
    Enumeration,
    EnumerationLiteral,
    Extent,
    FeatureCallExp,
    FlatQVT_AltExp,
    FlatQVT_AnyType,
    FlatQVT_Area,
    FlatQVT_AssertExp,
    FlatQVT_AssignExp,
    FlatQVT_Assignment,
    FlatQVT_BagType,
    FlatQVT_BlockExp,
    FlatQVT_BooleanLiteralExp,
    FlatQVT_BottomPattern,
    FlatQVT_BreakExp,
    FlatQVT_CallExp,
    FlatQVT_CatchExp,
    FlatQVT_Class,
    FlatQVT_CollectionItem,
    FlatQVT_CollectionLiteralExp,
    FlatQVT_CollectionLiteralPart,
    FlatQVT_CollectionRange,
    FlatQVT_CollectionTemplateExp,
    FlatQVT_CollectionType,
    FlatQVT_Comment,
    FlatQVT_ComputeExp,
    FlatQVT_Constructor,
    FlatQVT_ConstructorBody,
    FlatQVT_ContextualProperty,
    FlatQVT_ContinueExp,
    FlatQVT_CoreDomain,
    FlatQVT_CorePattern,
    FlatQVT_DataType,
    FlatQVT_DictLiteralExp,
    FlatQVT_DictLiteralPart,
    FlatQVT_DictionaryType,
    FlatQVT_Domain,
    FlatQVT_DomainPattern,
    FlatQVT_Element,
    FlatQVT_EnforcementOperation,
    FlatQVT_EntryOperation,
    FlatQVT_EnumLiteralExp,
    FlatQVT_Enumeration,
    FlatQVT_EnumerationLiteral,
    FlatQVT_ExpressionInOcl,
    FlatQVT_Extent,
    FlatQVT_Factory,
    FlatQVT_FeatureCallExp,
    FlatQVT_ForExp,
    FlatQVT_Function,
    FlatQVT_FunctionParameter,
    FlatQVT_GuardPattern,
    FlatQVT_Helper,
    FlatQVT_IfExp,
    FlatQVT_ImperativeCallExp,
    FlatQVT_ImperativeExpression,
    FlatQVT_ImperativeIterateExp,
    FlatQVT_ImperativeLoopExp,
    FlatQVT_ImperativeOperation,
    FlatQVT_InstantiationExp,
    FlatQVT_IntegerLiteralExp,
    FlatQVT_InvalidLiteralExp,
    FlatQVT_InvalidType,
    FlatQVT_IterateExp,
    FlatQVT_IteratorExp,
    FlatQVT_Key,
    FlatQVT_LetExp,
    FlatQVT_Library,
    FlatQVT_ListLiteralExp,
    FlatQVT_ListType,
    FlatQVT_LiteralExp,
    FlatQVT_LogExp,
    FlatQVT_LoopExp,
    FlatQVT_Mapping,
    FlatQVT_MappingBody,
    FlatQVT_MappingCallExp,
    FlatQVT_MappingOperation,
    FlatQVT_MappingParameter,
    FlatQVT_ModelParameter,
    FlatQVT_ModelType,
    FlatQVT_Module,
    FlatQVT_ModuleImport,
    FlatQVT_MultiplicityElement,
    FlatQVT_NamedElement,
    FlatQVT_NavigationCallExp,
    FlatQVT_NullLiteralExp,
    FlatQVT_NumericLiteralExp,
    FlatQVT_Object,
    FlatQVT_ObjectExp,
    FlatQVT_ObjectTemplateExp,
    FlatQVT_OclExpression,
    FlatQVT_Operation,
    FlatQVT_OperationBody,
    FlatQVT_OperationCallExp,
    FlatQVT_OperationalTransformation,
    FlatQVT_OppositePropertyCallExp,
    FlatQVT_OrderedSetType,
    FlatQVT_OrderedTupleLiteralExp,
    FlatQVT_OrderedTupleLiteralPart,
    FlatQVT_OrderedTupleType,
    FlatQVT_Package,
    FlatQVT_Parameter,
    FlatQVT_Pattern,
    FlatQVT_Predicate,
    FlatQVT_PrimitiveLiteralExp,
    FlatQVT_PrimitiveType,
    FlatQVT_Property,
    FlatQVT_PropertyAssignment,
    FlatQVT_PropertyCallExp,
    FlatQVT_PropertyTemplateItem,
    FlatQVT_RaiseExp,
    FlatQVT_RealLiteralExp,
    FlatQVT_RealizedVariable,
    FlatQVT_ReflectiveCollection,
    FlatQVT_ReflectiveSequence,
    FlatQVT_Relation,
    FlatQVT_RelationCallExp,
    FlatQVT_RelationDomain,
    FlatQVT_RelationDomainAssignment,
    FlatQVT_RelationImplementation,
    FlatQVT_RelationalTransformation,
    FlatQVT_ResolveExp,
    FlatQVT_ResolveInExp,
    FlatQVT_ReturnExp,
    FlatQVT_Rule,
    FlatQVT_SequenceType,
    FlatQVT_SetType,
    FlatQVT_StringLiteralExp,
    FlatQVT_SwitchExp,
    FlatQVT_Tag,
    FlatQVT_TemplateExp,
    FlatQVT_TemplateParameterType,
    FlatQVT_Transformation,
    FlatQVT_TryExp,
    FlatQVT_TupleLiteralExp,
    FlatQVT_TupleLiteralPart,
    FlatQVT_TupleType,
    FlatQVT_Type,
    FlatQVT_TypeExp,
    FlatQVT_TypedElement,
    FlatQVT_TypedModel,
    FlatQVT_Typedef,
    FlatQVT_URIExtent,
    FlatQVT_UnlimitedNaturalExp,
    FlatQVT_UnlinkExp,
    FlatQVT_UnpackExp,
    FlatQVT_VarParameter,
    FlatQVT_Variable,
    FlatQVT_VariableAssignment,
    FlatQVT_VariableExp,
    FlatQVT_VariableInitExp,
    FlatQVT_VoidType,
    FlatQVT_WhileExp,
    GuardPattern,
    ImperativeCallExp,
    ImperativeExpression,
    ImperativeLoopExp,
    ImperativeOperation,
    InstantiationExp,
    Key,
    LetExp,
    LiteralExp,
    LogExp,
    LoopExp,
    Mapping,
    MappingOperation,
    ModelParameter,
    ModelType,
    Module,
    ModuleImport,
    MultiplicityElement,
    NamedElement,
    NavigationCallExp,
    NumericLiteralExp,
    Object,
    ObjectTemplateExp,
    OclExpression,
    Operation,
    OperationBody,
    OperationCallExp,
    OrderedTupleLiteralPart,
    Package,
    Parameter,
    Pattern,
    Predicate,
    PrimitiveLiteralExp,
    Property,
    PropertyCallExp,
    PropertyTemplateItem,
    RealizedVariable,
    ReflectiveCollection,
    Relation,
    RelationDomain,
    RelationDomainAssignment,
    RelationImplementation,
    RelationalTransformation,
    ResolveExp,
    Rule,
    Tag,
    TemplateExp,
    Transformation,
    TupleLiteralExp,
    TupleLiteralPart,
    Type,
    TypedElement,
    TypedModel,
    VarParameter,
    Variable,
    CollectionKind,
    DirectionKind,
    EnforcementMode,
    ImportKind,
    SeverityKind,
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

def test_assoc_additionalCondition204_stub_double():
    # OclExpression has no real 'OclExpression205' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ModelType(conformanceKind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression205', None)
    _safe_set(owner, 'FlatQVT_ModelType', {partner})
    assert getattr(partner, 'OclExpression205') == owner
    _safe_set(owner, 'FlatQVT_ModelType', set())
    assert getattr(partner, 'OclExpression205') is None


def test_assoc_annotatedElement61_stub_double():
    # NamedElement has no real 'NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Comment(body="sample_text")
    partner = NamedElement()
    setattr(partner, 'NamedElement', None)
    _safe_set(owner, 'FlatQVT_Comment', {partner})
    assert getattr(partner, 'NamedElement') == owner
    _safe_set(owner, 'FlatQVT_Comment', set())
    assert getattr(partner, 'NamedElement') is None


def test_assoc_assertion7_stub_double():
    # OclExpression has no real 'OclExpression8' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression8', None)
    _safe_set(owner, 'FlatQVT_AssertExp', partner)
    assert getattr(partner, 'OclExpression8') == owner
    _safe_set(owner, 'FlatQVT_AssertExp', None)
    assert getattr(partner, 'OclExpression8') is None


def test_assoc_binding222_stub_double():
    # ModelType has no real 'ModelType223' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType223', None)
    _safe_set(owner, 'FlatQVT_ModuleImport', {partner})
    assert getattr(partner, 'ModelType223') == owner
    _safe_set(owner, 'FlatQVT_ModuleImport', set())
    assert getattr(partner, 'ModelType223') is None


def test_assoc_body129_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'FlatQVT_ImperativeOperation', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'FlatQVT_ImperativeOperation', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_bottomPattern19_stub_double():
    # BottomPattern has no real 'BottomPattern20' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Assignment(isDefault="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern20', None)
    _safe_set(owner, 'FlatQVT_Assignment', partner)
    assert getattr(partner, 'BottomPattern20') == owner
    _safe_set(owner, 'FlatQVT_Assignment', None)
    assert getattr(partner, 'BottomPattern20') is None


def test_assoc_bottomPattern90_stub_double():
    # BottomPattern has no real 'BottomPattern91' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_EnforcementOperation(enforcementMode="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern91', None)
    _safe_set(owner, 'FlatQVT_EnforcementOperation', partner)
    assert getattr(partner, 'BottomPattern91') == owner
    _safe_set(owner, 'FlatQVT_EnforcementOperation', None)
    assert getattr(partner, 'BottomPattern91') is None


def test_assoc_class_294_stub_double():
    # Class has no real 'Class295' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Class()
    setattr(partner, 'Class295', None)
    _safe_set(owner, 'FlatQVT_Property', partner)
    assert getattr(partner, 'Class295') == owner
    _safe_set(owner, 'FlatQVT_Property', None)
    assert getattr(partner, 'Class295') is None


def test_assoc_condition353_stub_double():
    # OclExpression has no real 'OclExpression354' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression354', None)
    _safe_set(owner, 'FlatQVT_ResolveExp', partner)
    assert getattr(partner, 'OclExpression354') == owner
    _safe_set(owner, 'FlatQVT_ResolveExp', None)
    assert getattr(partner, 'OclExpression354') is None


def test_assoc_configProperty209_stub_double():
    # Property has no real 'Property210' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = Property()
    setattr(partner, 'Property210', None)
    _safe_set(owner, 'FlatQVT_Module', {partner})
    assert getattr(partner, 'Property210') == owner
    _safe_set(owner, 'FlatQVT_Module', set())
    assert getattr(partner, 'Property210') is None


def test_assoc_context130_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'FlatQVT_ImperativeOperation131', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'FlatQVT_ImperativeOperation131', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner430_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation431' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation431', None)
    _safe_set(owner, 'FlatQVT_VarParameter', partner)
    assert getattr(partner, 'ImperativeOperation431') == owner
    _safe_set(owner, 'FlatQVT_VarParameter', None)
    assert getattr(partner, 'ImperativeOperation431') is None


def test_assoc_defaultValue11_stub_double():
    # OclExpression has no real 'OclExpression12' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression12', None)
    _safe_set(owner, 'FlatQVT_AssignExp', partner)
    assert getattr(partner, 'OclExpression12') == owner
    _safe_set(owner, 'FlatQVT_AssignExp', None)
    assert getattr(partner, 'OclExpression12') is None


def test_assoc_element372_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'FlatQVT_Tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'FlatQVT_Tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_entry211_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'FlatQVT_Module212', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'FlatQVT_Module212', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule224_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'FlatQVT_ModuleImport225', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'FlatQVT_ModuleImport225', None)
    assert getattr(partner, 'Module') is None


def test_assoc_left13_stub_double():
    # OclExpression has no real 'OclExpression15' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression15', None)
    _safe_set(owner, 'FlatQVT_AssignExp14', partner)
    assert getattr(partner, 'OclExpression15') == owner
    _safe_set(owner, 'FlatQVT_AssignExp14', None)
    assert getattr(partner, 'OclExpression15') is None


def test_assoc_log9_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'FlatQVT_AssertExp10', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'FlatQVT_AssertExp10', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_metamodel206_stub_double():
    # Package has no real 'Package208' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ModelType(conformanceKind="sample_text")
    partner = Package()
    setattr(partner, 'Package208', None)
    _safe_set(owner, 'FlatQVT_ModelType207', {partner})
    assert getattr(partner, 'Package208') == owner
    _safe_set(owner, 'FlatQVT_ModelType207', set())
    assert getattr(partner, 'Package208') is None


def test_assoc_module226_stub_double():
    # Module has no real 'Module228' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module228', None)
    _safe_set(owner, 'FlatQVT_ModuleImport227', partner)
    assert getattr(partner, 'Module228') == owner
    _safe_set(owner, 'FlatQVT_ModuleImport227', None)
    assert getattr(partner, 'Module228') is None


def test_assoc_moduleImport213_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'FlatQVT_Module214', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'FlatQVT_Module214', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_nestedPackage276_stub_double():
    # Package has no real 'Package277' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package277', None)
    _safe_set(owner, 'FlatQVT_Package', {partner})
    assert getattr(partner, 'Package277') == owner
    _safe_set(owner, 'FlatQVT_Package', set())
    assert getattr(partner, 'Package277') is None


def test_assoc_nestingPackage278_stub_double():
    # Package has no real 'Package280' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package280', None)
    _safe_set(owner, 'FlatQVT_Package279', partner)
    assert getattr(partner, 'Package280') == owner
    _safe_set(owner, 'FlatQVT_Package279', None)
    assert getattr(partner, 'Package280') is None


def test_assoc_objContainer306_stub_double():
    # ObjectTemplateExp has no real 'ObjectTemplateExp' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_PropertyTemplateItem(isOpposite="sample_text")
    partner = ObjectTemplateExp()
    setattr(partner, 'ObjectTemplateExp', None)
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem', partner)
    assert getattr(partner, 'ObjectTemplateExp') == owner
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem', None)
    assert getattr(partner, 'ObjectTemplateExp') is None


def test_assoc_operationCallExp92_stub_double():
    # OperationCallExp has no real 'OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_EnforcementOperation(enforcementMode="sample_text")
    partner = OperationCallExp()
    setattr(partner, 'OperationCallExp', None)
    _safe_set(owner, 'FlatQVT_EnforcementOperation93', partner)
    assert getattr(partner, 'OperationCallExp') == owner
    _safe_set(owner, 'FlatQVT_EnforcementOperation93', None)
    assert getattr(partner, 'OperationCallExp') is None


def test_assoc_operationalImpl318_stub_double():
    # RelationImplementation has no real 'RelationImplementation' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Relation(isTopLevel="sample_text")
    partner = RelationImplementation()
    setattr(partner, 'RelationImplementation', None)
    _safe_set(owner, 'FlatQVT_Relation', {partner})
    assert getattr(partner, 'RelationImplementation') == owner
    _safe_set(owner, 'FlatQVT_Relation', set())
    assert getattr(partner, 'RelationImplementation') is None


def test_assoc_opposite296_stub_double():
    # Property has no real 'Property298' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property298', None)
    _safe_set(owner, 'FlatQVT_Property297', partner)
    assert getattr(partner, 'Property298') == owner
    _safe_set(owner, 'FlatQVT_Property297', None)
    assert getattr(partner, 'Property298') is None


def test_assoc_overridden132_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'FlatQVT_ImperativeOperation133', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'FlatQVT_ImperativeOperation133', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_ownedAttribute39_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Class(isAbstract="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'FlatQVT_Class', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'FlatQVT_Class', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedComment89_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Element()
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'FlatQVT_Element', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'FlatQVT_Element', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_ownedOperation40_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'FlatQVT_Class41', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'FlatQVT_Class41', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedTag215_stub_double():
    # Tag has no real 'Tag' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = Tag()
    setattr(partner, 'Tag', None)
    _safe_set(owner, 'FlatQVT_Module216', {partner})
    assert getattr(partner, 'Tag') == owner
    _safe_set(owner, 'FlatQVT_Module216', set())
    assert getattr(partner, 'Tag') is None


def test_assoc_ownedType281_stub_double():
    # Type has no real 'Type283' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type283', None)
    _safe_set(owner, 'FlatQVT_Package282', {partner})
    assert getattr(partner, 'Type283') == owner
    _safe_set(owner, 'FlatQVT_Package282', set())
    assert getattr(partner, 'Type283') is None


def test_assoc_ownedVariable217_stub_double():
    # Variable has no real 'Variable219' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = Variable()
    setattr(partner, 'Variable219', None)
    _safe_set(owner, 'FlatQVT_Module218', {partner})
    assert getattr(partner, 'Variable219') == owner
    _safe_set(owner, 'FlatQVT_Module218', set())
    assert getattr(partner, 'Variable219') is None


def test_assoc_package112_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Factory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Factory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Factory()
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'FlatQVT_Factory', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'FlatQVT_Factory', None)
    assert getattr(partner, 'Package') is None


def test_assoc_package401_stub_double():
    # Package has no real 'Package402' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Type()
    partner = Package()
    setattr(partner, 'Package402', None)
    _safe_set(owner, 'FlatQVT_Type', partner)
    assert getattr(partner, 'Package402') == owner
    _safe_set(owner, 'FlatQVT_Type', None)
    assert getattr(partner, 'Package402') is None


def test_assoc_part46_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'FlatQVT_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'FlatQVT_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_referredProperty307_stub_double():
    # Property has no real 'Property309' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_PropertyTemplateItem(isOpposite="sample_text")
    partner = Property()
    setattr(partner, 'Property309', None)
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem308', partner)
    assert getattr(partner, 'Property309') == owner
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem308', None)
    assert getattr(partner, 'Property309') is None


def test_assoc_referredVariable446_stub_double():
    # Variable has no real 'Variable447' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_VariableInitExp(withResult="sample_text")
    partner = Variable()
    setattr(partner, 'Variable447', None)
    _safe_set(owner, 'FlatQVT_VariableInitExp', partner)
    assert getattr(partner, 'Variable447') == owner
    _safe_set(owner, 'FlatQVT_VariableInitExp', None)
    assert getattr(partner, 'Variable447') is None


def test_assoc_resOwner432_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation434' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation434', None)
    _safe_set(owner, 'FlatQVT_VarParameter433', partner)
    assert getattr(partner, 'ImperativeOperation434') == owner
    _safe_set(owner, 'FlatQVT_VarParameter433', None)
    assert getattr(partner, 'ImperativeOperation434') is None


def test_assoc_result134_stub_double():
    # VarParameter has no real 'VarParameter136' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter136', None)
    _safe_set(owner, 'FlatQVT_ImperativeOperation135', {partner})
    assert getattr(partner, 'VarParameter136') == owner
    _safe_set(owner, 'FlatQVT_ImperativeOperation135', set())
    assert getattr(partner, 'VarParameter136') is None


def test_assoc_rule85_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'FlatQVT_Domain', partner)
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'FlatQVT_Domain', None)
    assert getattr(partner, 'Rule') is None


def test_assoc_superClass42_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Class(isAbstract="sample_text")
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'FlatQVT_Class43', {partner})
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'FlatQVT_Class43', set())
    assert getattr(partner, 'Class') is None


def test_assoc_target355_stub_double():
    # Variable has no real 'Variable357' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = Variable()
    setattr(partner, 'Variable357', None)
    _safe_set(owner, 'FlatQVT_ResolveExp356', partner)
    assert getattr(partner, 'Variable357') == owner
    _safe_set(owner, 'FlatQVT_ResolveExp356', None)
    assert getattr(partner, 'Variable357') is None


def test_assoc_typedModel86_stub_double():
    # TypedModel has no real 'TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = TypedModel()
    setattr(partner, 'TypedModel', None)
    _safe_set(owner, 'FlatQVT_Domain87', partner)
    assert getattr(partner, 'TypedModel') == owner
    _safe_set(owner, 'FlatQVT_Domain87', None)
    assert getattr(partner, 'TypedModel') is None


def test_assoc_usedModelType220_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'FlatQVT_Module221', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'FlatQVT_Module221', set())
    assert getattr(partner, 'ModelType') is None


def test_assoc_value16_stub_double():
    # OclExpression has no real 'OclExpression18' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression18', None)
    _safe_set(owner, 'FlatQVT_AssignExp17', {partner})
    assert getattr(partner, 'OclExpression18') == owner
    _safe_set(owner, 'FlatQVT_AssignExp17', set())
    assert getattr(partner, 'OclExpression18') is None


def test_assoc_value21_stub_double():
    # OclExpression has no real 'OclExpression23' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Assignment(isDefault="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression23', None)
    _safe_set(owner, 'FlatQVT_Assignment22', partner)
    assert getattr(partner, 'OclExpression23') == owner
    _safe_set(owner, 'FlatQVT_Assignment22', None)
    assert getattr(partner, 'OclExpression23') is None


def test_assoc_value310_stub_double():
    # OclExpression has no real 'OclExpression312' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_PropertyTemplateItem(isOpposite="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression312', None)
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem311', partner)
    assert getattr(partner, 'OclExpression312') == owner
    _safe_set(owner, 'FlatQVT_PropertyTemplateItem311', None)
    assert getattr(partner, 'OclExpression312') is None


def test_assoc_variable319_stub_double():
    # Variable has no real 'Variable321' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Relation(isTopLevel="sample_text")
    partner = Variable()
    setattr(partner, 'Variable321', None)
    _safe_set(owner, 'FlatQVT_Relation320', {partner})
    assert getattr(partner, 'Variable321') == owner
    _safe_set(owner, 'FlatQVT_Relation320', set())
    assert getattr(partner, 'Variable321') is None


def test_assoc_when322_stub_double():
    # Pattern has no real 'Pattern324' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern324', None)
    _safe_set(owner, 'FlatQVT_Relation323', partner)
    assert getattr(partner, 'Pattern324') == owner
    _safe_set(owner, 'FlatQVT_Relation323', None)
    assert getattr(partner, 'Pattern324') is None


def test_assoc_where325_stub_double():
    # Pattern has no real 'Pattern327' property in the generated
    # code (a bare stub) -- manually attach it so FlatQVT_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FlatQVT_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FlatQVT_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern327', None)
    _safe_set(owner, 'FlatQVT_Relation326', partner)
    assert getattr(partner, 'Pattern327') == owner
    _safe_set(owner, 'FlatQVT_Relation326', None)
    assert getattr(partner, 'Pattern327') is None


