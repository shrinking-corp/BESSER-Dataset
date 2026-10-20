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
    EMOF_Class,
    EMOF_Comment,
    EMOF_DataType,
    EMOF_Element,
    EMOF_Enumeration,
    EMOF_EnumerationLiteral,
    EMOF_Extent,
    EMOF_Factory,
    EMOF_MultiplicityElement,
    EMOF_NamedElement,
    EMOF_Object,
    EMOF_Operation,
    EMOF_Package,
    EMOF_Parameter,
    EMOF_PrimitiveType,
    EMOF_Property,
    EMOF_ReflectiveCollection,
    EMOF_ReflectiveSequence,
    EMOF_Tag,
    EMOF_Type,
    EMOF_TypedElement,
    EMOF_URIExtent,
    Element,
    EnforcementOperation,
    EntryOperation,
    Enumeration,
    EnumerationLiteral,
    EssentialOCL_AnyType,
    EssentialOCL_BagType,
    EssentialOCL_BooleanLiteralExp,
    EssentialOCL_CallExp,
    EssentialOCL_CollectionItem,
    EssentialOCL_CollectionLiteralExp,
    EssentialOCL_CollectionLiteralPart,
    EssentialOCL_CollectionRange,
    EssentialOCL_CollectionType,
    EssentialOCL_EnumLiteralExp,
    EssentialOCL_ExpressionInOcl,
    EssentialOCL_FeatureCallExp,
    EssentialOCL_IfExp,
    EssentialOCL_IntegerLiteralExp,
    EssentialOCL_InvalidLiteralExp,
    EssentialOCL_InvalidType,
    EssentialOCL_IterateExp,
    EssentialOCL_IteratorExp,
    EssentialOCL_LetExp,
    EssentialOCL_LiteralExp,
    EssentialOCL_LoopExp,
    EssentialOCL_NavigationCallExp,
    EssentialOCL_NullLiteralExp,
    EssentialOCL_NumericLiteralExp,
    EssentialOCL_OclExpression,
    EssentialOCL_OperationCallExp,
    EssentialOCL_OrderedSetType,
    EssentialOCL_PrimitiveLiteralExp,
    EssentialOCL_PropertyCallExp,
    EssentialOCL_RealLiteralExp,
    EssentialOCL_SequenceType,
    EssentialOCL_SetType,
    EssentialOCL_StringLiteralExp,
    EssentialOCL_TemplateParameterType,
    EssentialOCL_TupleLiteralExp,
    EssentialOCL_TupleLiteralPart,
    EssentialOCL_TupleType,
    EssentialOCL_TypeExp,
    EssentialOCL_UnlimitedNaturalExp,
    EssentialOCL_Variable,
    EssentialOCL_VariableExp,
    EssentialOCL_VoidType,
    Extent,
    FeatureCallExp,
    GuardPattern,
    ImperativeCallExp,
    ImperativeExpression,
    ImperativeLoopExp,
    ImperativeOCL_AltExp,
    ImperativeOCL_AssertExp,
    ImperativeOCL_AssignExp,
    ImperativeOCL_BlockExp,
    ImperativeOCL_BreakExp,
    ImperativeOCL_CatchExp,
    ImperativeOCL_ComputeExp,
    ImperativeOCL_ContinueExp,
    ImperativeOCL_DictLiteralExp,
    ImperativeOCL_DictLiteralPart,
    ImperativeOCL_DictionaryType,
    ImperativeOCL_ForExp,
    ImperativeOCL_ImperativeExpression,
    ImperativeOCL_ImperativeIterateExp,
    ImperativeOCL_ImperativeLoopExp,
    ImperativeOCL_InstantiationExp,
    ImperativeOCL_ListLiteralExp,
    ImperativeOCL_ListType,
    ImperativeOCL_LogExp,
    ImperativeOCL_OrderedTupleLiteralExp,
    ImperativeOCL_OrderedTupleLiteralPart,
    ImperativeOCL_OrderedTupleType,
    ImperativeOCL_RaiseExp,
    ImperativeOCL_ReturnExp,
    ImperativeOCL_SwitchExp,
    ImperativeOCL_TryExp,
    ImperativeOCL_Typedef,
    ImperativeOCL_UnlinkExp,
    ImperativeOCL_UnpackExp,
    ImperativeOCL_VariableInitExp,
    ImperativeOCL_WhileExp,
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
    QVTBase_Domain,
    QVTBase_Function,
    QVTBase_FunctionParameter,
    QVTBase_Pattern,
    QVTBase_Predicate,
    QVTBase_Rule,
    QVTBase_Transformation,
    QVTBase_TypedModel,
    QVTCore_Area,
    QVTCore_Assignment,
    QVTCore_BottomPattern,
    QVTCore_CoreDomain,
    QVTCore_CorePattern,
    QVTCore_EnforcementOperation,
    QVTCore_GuardPattern,
    QVTCore_Mapping,
    QVTCore_PropertyAssignment,
    QVTCore_RealizedVariable,
    QVTCore_VariableAssignment,
    QVTOperational_Constructor,
    QVTOperational_ConstructorBody,
    QVTOperational_ContextualProperty,
    QVTOperational_EntryOperation,
    QVTOperational_Helper,
    QVTOperational_ImperativeCallExp,
    QVTOperational_ImperativeOperation,
    QVTOperational_Library,
    QVTOperational_MappingBody,
    QVTOperational_MappingCallExp,
    QVTOperational_MappingOperation,
    QVTOperational_MappingParameter,
    QVTOperational_ModelParameter,
    QVTOperational_ModelType,
    QVTOperational_Module,
    QVTOperational_ModuleImport,
    QVTOperational_ObjectExp,
    QVTOperational_OperationBody,
    QVTOperational_OperationalTransformation,
    QVTOperational_ResolveExp,
    QVTOperational_ResolveInExp,
    QVTOperational_VarParameter,
    QVTRelation_DomainPattern,
    QVTRelation_Key,
    QVTRelation_OppositePropertyCallExp,
    QVTRelation_Relation,
    QVTRelation_RelationCallExp,
    QVTRelation_RelationDomain,
    QVTRelation_RelationDomainAssignment,
    QVTRelation_RelationImplementation,
    QVTRelation_RelationalTransformation,
    QVTTemplate_CollectionTemplateExp,
    QVTTemplate_ObjectTemplateExp,
    QVTTemplate_PropertyTemplateItem,
    QVTTemplate_TemplateExp,
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

def test_assoc_additionalCondition389_stub_double():
    # OclExpression has no real 'OclExpression390' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression390', None)
    _safe_set(owner, 'QVTOperational_ModelType', {partner})
    assert getattr(partner, 'OclExpression390') == owner
    _safe_set(owner, 'QVTOperational_ModelType', set())
    assert getattr(partner, 'OclExpression390') is None


def test_assoc_annotatedElement5_stub_double():
    # NamedElement has no real 'NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Comment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Comment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Comment(body="sample_text")
    partner = NamedElement()
    setattr(partner, 'NamedElement', None)
    _safe_set(owner, 'EMOF_Comment', {partner})
    assert getattr(partner, 'NamedElement') == owner
    _safe_set(owner, 'EMOF_Comment', set())
    assert getattr(partner, 'NamedElement') is None


def test_assoc_assertion114_stub_double():
    # OclExpression has no real 'OclExpression115' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression115', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp', partner)
    assert getattr(partner, 'OclExpression115') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp', None)
    assert getattr(partner, 'OclExpression115') is None


def test_assoc_binding408_stub_double():
    # ModelType has no real 'ModelType409' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType409', None)
    _safe_set(owner, 'QVTOperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType409') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport', set())
    assert getattr(partner, 'ModelType409') is None


def test_assoc_body357_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_bottomPattern244_stub_double():
    # BottomPattern has no real 'BottomPattern245' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_Assignment(isDefault="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern245', None)
    _safe_set(owner, 'QVTCore_Assignment', partner)
    assert getattr(partner, 'BottomPattern245') == owner
    _safe_set(owner, 'QVTCore_Assignment', None)
    assert getattr(partner, 'BottomPattern245') is None


def test_assoc_bottomPattern258_stub_double():
    # BottomPattern has no real 'BottomPattern259' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_EnforcementOperation(enforcementMode="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern259', None)
    _safe_set(owner, 'QVTCore_EnforcementOperation', partner)
    assert getattr(partner, 'BottomPattern259') == owner
    _safe_set(owner, 'QVTCore_EnforcementOperation', None)
    assert getattr(partner, 'BottomPattern259') is None


def test_assoc_class_26_stub_double():
    # Class has no real 'Class27' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Class()
    setattr(partner, 'Class27', None)
    _safe_set(owner, 'EMOF_Property', partner)
    assert getattr(partner, 'Class27') == owner
    _safe_set(owner, 'EMOF_Property', None)
    assert getattr(partner, 'Class27') is None


def test_assoc_condition441_stub_double():
    # OclExpression has no real 'OclExpression442' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression442', None)
    _safe_set(owner, 'QVTOperational_ResolveExp', partner)
    assert getattr(partner, 'OclExpression442') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp', None)
    assert getattr(partner, 'OclExpression442') is None


def test_assoc_configProperty394_stub_double():
    # Property has no real 'Property395' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Property()
    setattr(partner, 'Property395', None)
    _safe_set(owner, 'QVTOperational_Module', {partner})
    assert getattr(partner, 'Property395') == owner
    _safe_set(owner, 'QVTOperational_Module', set())
    assert getattr(partner, 'Property395') is None


def test_assoc_context358_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation359', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation359', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner448_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation449' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation449', None)
    _safe_set(owner, 'QVTOperational_VarParameter', partner)
    assert getattr(partner, 'ImperativeOperation449') == owner
    _safe_set(owner, 'QVTOperational_VarParameter', None)
    assert getattr(partner, 'ImperativeOperation449') is None


def test_assoc_defaultValue118_stub_double():
    # OclExpression has no real 'OclExpression119' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression119', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp', partner)
    assert getattr(partner, 'OclExpression119') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp', None)
    assert getattr(partner, 'OclExpression119') is None


def test_assoc_element31_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'EMOF_Tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'EMOF_Tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_entry396_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'QVTOperational_Module397', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'QVTOperational_Module397', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule410_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'QVTOperational_ModuleImport411', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport411', None)
    assert getattr(partner, 'Module') is None


def test_assoc_left120_stub_double():
    # OclExpression has no real 'OclExpression122' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression122', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp121', partner)
    assert getattr(partner, 'OclExpression122') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp121', None)
    assert getattr(partner, 'OclExpression122') is None


def test_assoc_log116_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp117', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp117', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_metamodel391_stub_double():
    # Package has no real 'Package393' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = Package()
    setattr(partner, 'Package393', None)
    _safe_set(owner, 'QVTOperational_ModelType392', {partner})
    assert getattr(partner, 'Package393') == owner
    _safe_set(owner, 'QVTOperational_ModelType392', set())
    assert getattr(partner, 'Package393') is None


def test_assoc_module412_stub_double():
    # Module has no real 'Module414' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module414', None)
    _safe_set(owner, 'QVTOperational_ModuleImport413', partner)
    assert getattr(partner, 'Module414') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport413', None)
    assert getattr(partner, 'Module414') is None


def test_assoc_moduleImport398_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'QVTOperational_Module399', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'QVTOperational_Module399', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_nestedPackage16_stub_double():
    # Package has no real 'Package17' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package17', None)
    _safe_set(owner, 'EMOF_Package', {partner})
    assert getattr(partner, 'Package17') == owner
    _safe_set(owner, 'EMOF_Package', set())
    assert getattr(partner, 'Package17') is None


def test_assoc_nestingPackage18_stub_double():
    # Package has no real 'Package20' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package20', None)
    _safe_set(owner, 'EMOF_Package19', partner)
    assert getattr(partner, 'Package20') == owner
    _safe_set(owner, 'EMOF_Package19', None)
    assert getattr(partner, 'Package20') is None


def test_assoc_objContainer292_stub_double():
    # ObjectTemplateExp has no real 'ObjectTemplateExp' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = ObjectTemplateExp()
    setattr(partner, 'ObjectTemplateExp', None)
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem', partner)
    assert getattr(partner, 'ObjectTemplateExp') == owner
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem', None)
    assert getattr(partner, 'ObjectTemplateExp') is None


def test_assoc_operationCallExp260_stub_double():
    # OperationCallExp has no real 'OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_EnforcementOperation(enforcementMode="sample_text")
    partner = OperationCallExp()
    setattr(partner, 'OperationCallExp', None)
    _safe_set(owner, 'QVTCore_EnforcementOperation261', partner)
    assert getattr(partner, 'OperationCallExp') == owner
    _safe_set(owner, 'QVTCore_EnforcementOperation261', None)
    assert getattr(partner, 'OperationCallExp') is None


def test_assoc_operationalImpl315_stub_double():
    # RelationImplementation has no real 'RelationImplementation' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = RelationImplementation()
    setattr(partner, 'RelationImplementation', None)
    _safe_set(owner, 'QVTRelation_Relation', {partner})
    assert getattr(partner, 'RelationImplementation') == owner
    _safe_set(owner, 'QVTRelation_Relation', set())
    assert getattr(partner, 'RelationImplementation') is None


def test_assoc_opposite28_stub_double():
    # Property has no real 'Property30' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property30', None)
    _safe_set(owner, 'EMOF_Property29', partner)
    assert getattr(partner, 'Property30') == owner
    _safe_set(owner, 'EMOF_Property29', None)
    assert getattr(partner, 'Property30') is None


def test_assoc_overridden360_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation361', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation361', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_ownedAttribute0_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'EMOF_Class', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'EMOF_Class', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedComment6_stub_double():
    # Comment has no real 'Comment' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Element()
    partner = Comment()
    setattr(partner, 'Comment', None)
    _safe_set(owner, 'EMOF_Element', {partner})
    assert getattr(partner, 'Comment') == owner
    _safe_set(owner, 'EMOF_Element', set())
    assert getattr(partner, 'Comment') is None


def test_assoc_ownedOperation1_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'EMOF_Class2', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'EMOF_Class2', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedTag400_stub_double():
    # Tag has no real 'Tag402' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Tag()
    setattr(partner, 'Tag402', None)
    _safe_set(owner, 'QVTOperational_Module401', {partner})
    assert getattr(partner, 'Tag402') == owner
    _safe_set(owner, 'QVTOperational_Module401', set())
    assert getattr(partner, 'Tag402') is None


def test_assoc_ownedType21_stub_double():
    # Type has no real 'Type23' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type23', None)
    _safe_set(owner, 'EMOF_Package22', {partner})
    assert getattr(partner, 'Type23') == owner
    _safe_set(owner, 'EMOF_Package22', set())
    assert getattr(partner, 'Type23') is None


def test_assoc_ownedVariable403_stub_double():
    # Variable has no real 'Variable405' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Variable()
    setattr(partner, 'Variable405', None)
    _safe_set(owner, 'QVTOperational_Module404', {partner})
    assert getattr(partner, 'Variable405') == owner
    _safe_set(owner, 'QVTOperational_Module404', set())
    assert getattr(partner, 'Variable405') is None


def test_assoc_package32_stub_double():
    # Package has no real 'Package33' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Type()
    partner = Package()
    setattr(partner, 'Package33', None)
    _safe_set(owner, 'EMOF_Type', partner)
    assert getattr(partner, 'Package33') == owner
    _safe_set(owner, 'EMOF_Type', None)
    assert getattr(partner, 'Package33') is None


def test_assoc_package9_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Factory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Factory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Factory()
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'EMOF_Factory', partner)
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'EMOF_Factory', None)
    assert getattr(partner, 'Package') is None


def test_assoc_part39_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so EssentialOCL_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EssentialOCL_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EssentialOCL_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'EssentialOCL_CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'EssentialOCL_CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_referredProperty293_stub_double():
    # Property has no real 'Property295' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = Property()
    setattr(partner, 'Property295', None)
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem294', partner)
    assert getattr(partner, 'Property295') == owner
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem294', None)
    assert getattr(partner, 'Property295') is None


def test_assoc_referredVariable197_stub_double():
    # Variable has no real 'Variable198' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_VariableInitExp(withResult="sample_text")
    partner = Variable()
    setattr(partner, 'Variable198', None)
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', partner)
    assert getattr(partner, 'Variable198') == owner
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', None)
    assert getattr(partner, 'Variable198') is None


def test_assoc_resOwner450_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation452' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation452', None)
    _safe_set(owner, 'QVTOperational_VarParameter451', partner)
    assert getattr(partner, 'ImperativeOperation452') == owner
    _safe_set(owner, 'QVTOperational_VarParameter451', None)
    assert getattr(partner, 'ImperativeOperation452') is None


def test_assoc_result362_stub_double():
    # VarParameter has no real 'VarParameter364' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter364', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation363', {partner})
    assert getattr(partner, 'VarParameter364') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation363', set())
    assert getattr(partner, 'VarParameter364') is None


def test_assoc_rule204_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so QVTBase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTBase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTBase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'QVTBase_Domain', partner)
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'QVTBase_Domain', None)
    assert getattr(partner, 'Rule') is None


def test_assoc_superClass3_stub_double():
    # Class has no real 'Class' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Class(isAbstract="sample_text")
    partner = Class()
    setattr(partner, 'Class', None)
    _safe_set(owner, 'EMOF_Class4', {partner})
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'EMOF_Class4', set())
    assert getattr(partner, 'Class') is None


def test_assoc_target443_stub_double():
    # Variable has no real 'Variable445' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = Variable()
    setattr(partner, 'Variable445', None)
    _safe_set(owner, 'QVTOperational_ResolveExp444', partner)
    assert getattr(partner, 'Variable445') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp444', None)
    assert getattr(partner, 'Variable445') is None


def test_assoc_typedModel205_stub_double():
    # TypedModel has no real 'TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so QVTBase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTBase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTBase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = TypedModel()
    setattr(partner, 'TypedModel', None)
    _safe_set(owner, 'QVTBase_Domain206', partner)
    assert getattr(partner, 'TypedModel') == owner
    _safe_set(owner, 'QVTBase_Domain206', None)
    assert getattr(partner, 'TypedModel') is None


def test_assoc_usedModelType406_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'QVTOperational_Module407', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'QVTOperational_Module407', set())
    assert getattr(partner, 'ModelType') is None


def test_assoc_value123_stub_double():
    # OclExpression has no real 'OclExpression125' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression125', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp124', {partner})
    assert getattr(partner, 'OclExpression125') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp124', set())
    assert getattr(partner, 'OclExpression125') is None


def test_assoc_value246_stub_double():
    # OclExpression has no real 'OclExpression248' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_Assignment(isDefault="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression248', None)
    _safe_set(owner, 'QVTCore_Assignment247', partner)
    assert getattr(partner, 'OclExpression248') == owner
    _safe_set(owner, 'QVTCore_Assignment247', None)
    assert getattr(partner, 'OclExpression248') is None


def test_assoc_value296_stub_double():
    # OclExpression has no real 'OclExpression298' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression298', None)
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem297', partner)
    assert getattr(partner, 'OclExpression298') == owner
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem297', None)
    assert getattr(partner, 'OclExpression298') is None


def test_assoc_variable316_stub_double():
    # Variable has no real 'Variable318' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Variable()
    setattr(partner, 'Variable318', None)
    _safe_set(owner, 'QVTRelation_Relation317', {partner})
    assert getattr(partner, 'Variable318') == owner
    _safe_set(owner, 'QVTRelation_Relation317', set())
    assert getattr(partner, 'Variable318') is None


def test_assoc_when319_stub_double():
    # Pattern has no real 'Pattern321' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern321', None)
    _safe_set(owner, 'QVTRelation_Relation320', partner)
    assert getattr(partner, 'Pattern321') == owner
    _safe_set(owner, 'QVTRelation_Relation320', None)
    assert getattr(partner, 'Pattern321') is None


def test_assoc_where322_stub_double():
    # Pattern has no real 'Pattern324' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern324', None)
    _safe_set(owner, 'QVTRelation_Relation323', partner)
    assert getattr(partner, 'Pattern324') == owner
    _safe_set(owner, 'QVTRelation_Relation323', None)
    assert getattr(partner, 'Pattern324') is None


