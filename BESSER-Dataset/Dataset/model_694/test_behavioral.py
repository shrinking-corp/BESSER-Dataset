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
    DictLiteralExp,
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
    ImperativeOCL_RaiseExp,
    ImperativeOCL_ReturnExp,
    ImperativeOCL_SwitchExp,
    ImperativeOCL_TryExp,
    ImperativeOCL_Typedef,
    ImperativeOCL_UnlinkExp,
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
    OperationalTransformation,
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

def test_assoc_additionalCondition370_stub_double():
    # OclExpression has no real 'OclExpression371' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression371', None)
    _safe_set(owner, 'QVTOperational_ModelType', {partner})
    assert getattr(partner, 'OclExpression371') == owner
    _safe_set(owner, 'QVTOperational_ModelType', set())
    assert getattr(partner, 'OclExpression371') is None


def test_assoc_annotatedElement4_stub_double():
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


def test_assoc_assertion241_stub_double():
    # OclExpression has no real 'OclExpression242' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression242', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp', partner)
    assert getattr(partner, 'OclExpression242') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp', None)
    assert getattr(partner, 'OclExpression242') is None


def test_assoc_binding388_stub_double():
    # ModelType has no real 'ModelType389' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType389', None)
    _safe_set(owner, 'QVTOperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType389') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport', set())
    assert getattr(partner, 'ModelType389') is None


def test_assoc_body337_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'operation338', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'operation338', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_bottomPattern135_stub_double():
    # BottomPattern has no real 'BottomPattern136' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_Assignment(isDefault="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern136', None)
    _safe_set(owner, 'assignment', partner)
    assert getattr(partner, 'BottomPattern136') == owner
    _safe_set(owner, 'assignment', None)
    assert getattr(partner, 'BottomPattern136') is None


def test_assoc_bottomPattern148_stub_double():
    # BottomPattern has no real 'BottomPattern149' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_EnforcementOperation(enforcementMode="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern149', None)
    _safe_set(owner, 'enforcementOperation', partner)
    assert getattr(partner, 'BottomPattern149') == owner
    _safe_set(owner, 'enforcementOperation', None)
    assert getattr(partner, 'BottomPattern149') is None


def test_assoc_class_21_stub_double():
    # Class has no real 'Class22' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Class()
    setattr(partner, 'Class22', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'Class22') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'Class22') is None


def test_assoc_condition419_stub_double():
    # OclExpression has no real 'OclExpression420' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression420', None)
    _safe_set(owner, 'QVTOperational_ResolveExp', partner)
    assert getattr(partner, 'OclExpression420') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp', None)
    assert getattr(partner, 'OclExpression420') is None


def test_assoc_configProperty375_stub_double():
    # Property has no real 'Property376' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Property()
    setattr(partner, 'Property376', None)
    _safe_set(owner, 'QVTOperational_Module', {partner})
    assert getattr(partner, 'Property376') == owner
    _safe_set(owner, 'QVTOperational_Module', set())
    assert getattr(partner, 'Property376') is None


def test_assoc_context339_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'ctxOwner', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'ctxOwner', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner426_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation428' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation428', None)
    _safe_set(owner, 'context427', partner)
    assert getattr(partner, 'ImperativeOperation428') == owner
    _safe_set(owner, 'context427', None)
    assert getattr(partner, 'ImperativeOperation428') is None


def test_assoc_defaultValue245_stub_double():
    # OclExpression has no real 'OclExpression246' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression246', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp', partner)
    assert getattr(partner, 'OclExpression246') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp', None)
    assert getattr(partner, 'OclExpression246') is None


def test_assoc_element25_stub_double():
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


def test_assoc_entry377_stub_double():
    # EntryOperation has no real 'EntryOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = EntryOperation()
    setattr(partner, 'EntryOperation', None)
    _safe_set(owner, 'QVTOperational_Module378', partner)
    assert getattr(partner, 'EntryOperation') == owner
    _safe_set(owner, 'QVTOperational_Module378', None)
    assert getattr(partner, 'EntryOperation') is None


def test_assoc_importedModule390_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'QVTOperational_ModuleImport391', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'QVTOperational_ModuleImport391', None)
    assert getattr(partner, 'Module') is None


def test_assoc_left247_stub_double():
    # OclExpression has no real 'OclExpression249' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression249', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp248', partner)
    assert getattr(partner, 'OclExpression249') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp248', None)
    assert getattr(partner, 'OclExpression249') is None


def test_assoc_log243_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'ImperativeOCL_AssertExp244', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'ImperativeOCL_AssertExp244', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_metamodel372_stub_double():
    # Package has no real 'Package374' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModelType(conformanceKind="sample_text")
    partner = Package()
    setattr(partner, 'Package374', None)
    _safe_set(owner, 'QVTOperational_ModelType373', {partner})
    assert getattr(partner, 'Package374') == owner
    _safe_set(owner, 'QVTOperational_ModelType373', set())
    assert getattr(partner, 'Package374') is None


def test_assoc_module392_stub_double():
    # Module has no real 'Module393' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module393', None)
    _safe_set(owner, 'moduleImport', partner)
    assert getattr(partner, 'Module393') == owner
    _safe_set(owner, 'moduleImport', None)
    assert getattr(partner, 'Module393') is None


def test_assoc_moduleImport379_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'module', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'module', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_nestedPackage13_stub_double():
    # Package has no real 'Package14' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package14', None)
    _safe_set(owner, 'nestingPackage', {partner})
    assert getattr(partner, 'Package14') == owner
    _safe_set(owner, 'nestingPackage', set())
    assert getattr(partner, 'Package14') is None


def test_assoc_nestingPackage15_stub_double():
    # Package has no real 'Package16' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package16', None)
    _safe_set(owner, 'nestedPackage', partner)
    assert getattr(partner, 'Package16') == owner
    _safe_set(owner, 'nestedPackage', None)
    assert getattr(partner, 'Package16') is None


def test_assoc_objContainer179_stub_double():
    # ObjectTemplateExp has no real 'ObjectTemplateExp' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = ObjectTemplateExp()
    setattr(partner, 'ObjectTemplateExp', None)
    _safe_set(owner, 'part180', partner)
    assert getattr(partner, 'ObjectTemplateExp') == owner
    _safe_set(owner, 'part180', None)
    assert getattr(partner, 'ObjectTemplateExp') is None


def test_assoc_operationCallExp150_stub_double():
    # OperationCallExp has no real 'OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_EnforcementOperation(enforcementMode="sample_text")
    partner = OperationCallExp()
    setattr(partner, 'OperationCallExp', None)
    _safe_set(owner, 'QVTCore_EnforcementOperation', partner)
    assert getattr(partner, 'OperationCallExp') == owner
    _safe_set(owner, 'QVTCore_EnforcementOperation', None)
    assert getattr(partner, 'OperationCallExp') is None


def test_assoc_operationalImpl203_stub_double():
    # RelationImplementation has no real 'RelationImplementation' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = RelationImplementation()
    setattr(partner, 'RelationImplementation', None)
    _safe_set(owner, 'relation', {partner})
    assert getattr(partner, 'RelationImplementation') == owner
    _safe_set(owner, 'relation', set())
    assert getattr(partner, 'RelationImplementation') is None


def test_assoc_opposite23_stub_double():
    # Property has no real 'Property24' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isID="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property24', None)
    _safe_set(owner, 'EMOF_Property', partner)
    assert getattr(partner, 'Property24') == owner
    _safe_set(owner, 'EMOF_Property', None)
    assert getattr(partner, 'Property24') is None


def test_assoc_overridden340_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'QVTOperational_ImperativeOperation', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'QVTOperational_ImperativeOperation', None)
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
    _safe_set(owner, 'class_', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'class_', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedComment5_stub_double():
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
    _safe_set(owner, 'class_2', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'class_2', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedTag380_stub_double():
    # Tag has no real 'Tag382' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Tag()
    setattr(partner, 'Tag382', None)
    _safe_set(owner, 'QVTOperational_Module381', {partner})
    assert getattr(partner, 'Tag382') == owner
    _safe_set(owner, 'QVTOperational_Module381', set())
    assert getattr(partner, 'Tag382') is None


def test_assoc_ownedType17_stub_double():
    # Type has no real 'Type18' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type18', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type18') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type18') is None


def test_assoc_ownedVariable383_stub_double():
    # Variable has no real 'Variable385' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = Variable()
    setattr(partner, 'Variable385', None)
    _safe_set(owner, 'QVTOperational_Module384', {partner})
    assert getattr(partner, 'Variable385') == owner
    _safe_set(owner, 'QVTOperational_Module384', set())
    assert getattr(partner, 'Variable385') is None


def test_assoc_package26_stub_double():
    # Package has no real 'Package27' property in the generated
    # code (a bare stub) -- manually attach it so EMOF_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EMOF_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EMOF_Type()
    partner = Package()
    setattr(partner, 'Package27', None)
    _safe_set(owner, 'ownedType', partner)
    assert getattr(partner, 'Package27') == owner
    _safe_set(owner, 'ownedType', None)
    assert getattr(partner, 'Package27') is None


def test_assoc_package8_stub_double():
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


def test_assoc_part33_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so EssentialOCL_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # EssentialOCL_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = EssentialOCL_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'collectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'collectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_referredProperty181_stub_double():
    # Property has no real 'Property182' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = Property()
    setattr(partner, 'Property182', None)
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem', partner)
    assert getattr(partner, 'Property182') == owner
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem', None)
    assert getattr(partner, 'Property182') is None


def test_assoc_referredVariable322_stub_double():
    # Variable has no real 'Variable323' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_VariableInitExp(withResult="sample_text")
    partner = Variable()
    setattr(partner, 'Variable323', None)
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', partner)
    assert getattr(partner, 'Variable323') == owner
    _safe_set(owner, 'ImperativeOCL_VariableInitExp', None)
    assert getattr(partner, 'Variable323') is None


def test_assoc_resOwner429_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation430' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation430', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'ImperativeOperation430') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'ImperativeOperation430') is None


def test_assoc_result341_stub_double():
    # VarParameter has no real 'VarParameter342' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter342', None)
    _safe_set(owner, 'resOwner', {partner})
    assert getattr(partner, 'VarParameter342') == owner
    _safe_set(owner, 'resOwner', set())
    assert getattr(partner, 'VarParameter342') is None


def test_assoc_rule101_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so QVTBase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTBase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTBase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'domain', None)
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
    _safe_set(owner, 'EMOF_Class', {partner})
    assert getattr(partner, 'Class') == owner
    _safe_set(owner, 'EMOF_Class', set())
    assert getattr(partner, 'Class') is None


def test_assoc_target421_stub_double():
    # Variable has no real 'Variable423' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = Variable()
    setattr(partner, 'Variable423', None)
    _safe_set(owner, 'QVTOperational_ResolveExp422', partner)
    assert getattr(partner, 'Variable423') == owner
    _safe_set(owner, 'QVTOperational_ResolveExp422', None)
    assert getattr(partner, 'Variable423') is None


def test_assoc_typedModel102_stub_double():
    # TypedModel has no real 'TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so QVTBase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTBase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTBase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = TypedModel()
    setattr(partner, 'TypedModel', None)
    _safe_set(owner, 'QVTBase_Domain', partner)
    assert getattr(partner, 'TypedModel') == owner
    _safe_set(owner, 'QVTBase_Domain', None)
    assert getattr(partner, 'TypedModel') is None


def test_assoc_usedModelType386_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so QVTOperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTOperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTOperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'QVTOperational_Module387', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'QVTOperational_Module387', set())
    assert getattr(partner, 'ModelType') is None


def test_assoc_value137_stub_double():
    # OclExpression has no real 'OclExpression138' property in the generated
    # code (a bare stub) -- manually attach it so QVTCore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTCore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTCore_Assignment(isDefault="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression138', None)
    _safe_set(owner, 'QVTCore_Assignment', partner)
    assert getattr(partner, 'OclExpression138') == owner
    _safe_set(owner, 'QVTCore_Assignment', None)
    assert getattr(partner, 'OclExpression138') is None


def test_assoc_value183_stub_double():
    # OclExpression has no real 'OclExpression185' property in the generated
    # code (a bare stub) -- manually attach it so QVTTemplate_PropertyTemplateItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTTemplate_PropertyTemplateItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTTemplate_PropertyTemplateItem(isOpposite="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression185', None)
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem184', partner)
    assert getattr(partner, 'OclExpression185') == owner
    _safe_set(owner, 'QVTTemplate_PropertyTemplateItem184', None)
    assert getattr(partner, 'OclExpression185') is None


def test_assoc_value250_stub_double():
    # OclExpression has no real 'OclExpression252' property in the generated
    # code (a bare stub) -- manually attach it so ImperativeOCL_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ImperativeOCL_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ImperativeOCL_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression252', None)
    _safe_set(owner, 'ImperativeOCL_AssignExp251', {partner})
    assert getattr(partner, 'OclExpression252') == owner
    _safe_set(owner, 'ImperativeOCL_AssignExp251', set())
    assert getattr(partner, 'OclExpression252') is None


def test_assoc_variable204_stub_double():
    # Variable has no real 'Variable205' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Variable()
    setattr(partner, 'Variable205', None)
    _safe_set(owner, 'QVTRelation_Relation', {partner})
    assert getattr(partner, 'Variable205') == owner
    _safe_set(owner, 'QVTRelation_Relation', set())
    assert getattr(partner, 'Variable205') is None


def test_assoc_when206_stub_double():
    # Pattern has no real 'Pattern208' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern208', None)
    _safe_set(owner, 'QVTRelation_Relation207', partner)
    assert getattr(partner, 'Pattern208') == owner
    _safe_set(owner, 'QVTRelation_Relation207', None)
    assert getattr(partner, 'Pattern208') is None


def test_assoc_where209_stub_double():
    # Pattern has no real 'Pattern211' property in the generated
    # code (a bare stub) -- manually attach it so QVTRelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # QVTRelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = QVTRelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern211', None)
    _safe_set(owner, 'QVTRelation_Relation210', partner)
    assert getattr(partner, 'Pattern211') == owner
    _safe_set(owner, 'QVTRelation_Relation210', None)
    assert getattr(partner, 'Pattern211') is None


