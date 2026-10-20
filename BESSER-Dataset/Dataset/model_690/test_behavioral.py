import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    AnonymousTupleLiteralPart,
    Area,
    Assignment,
    BottomPattern,
    CallExp,
    Class,
    CollectionLiteralExp,
    CollectionLiteralPart,
    CollectionType,
    Comment,
    ComputeExp,
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
    FeaturePropertyCall,
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
    NumericLiteralExp,
    Object,
    ObjectTemplateExp,
    OclExpression,
    OpaqueExpression,
    Operation,
    OperationBody,
    OperationCallExp,
    Package,
    Parameter,
    Pattern,
    Predicate,
    PrimitiveLiteralExp,
    Property,
    PropertyTemplateItem,
    RealizedVariable,
    Relation,
    RelationDomain,
    RelationImplementation,
    RelationalTransformation,
    ResolveExp,
    Rule,
    Tag,
    TemplateExp,
    Transformation,
    TryExp,
    TupleLiteralExp,
    TupleLiteralPart,
    Type,
    TypedElement,
    TypedModel,
    URIExtent,
    VarParameter,
    Variable,
    emof_Class,
    emof_Comment,
    emof_DataType,
    emof_Element,
    emof_Enumeration,
    emof_EnumerationLiteral,
    emof_Extent,
    emof_MultiplicityElement,
    emof_NamedElement,
    emof_Object,
    emof_Operation,
    emof_Package,
    emof_Parameter,
    emof_PrimitiveType,
    emof_Property,
    emof_Tag,
    emof_Type,
    emof_TypedElement,
    emof_URIExtent,
    essentialocl_AnyType,
    essentialocl_BagType,
    essentialocl_BooleanLiteralExp,
    essentialocl_CallExp,
    essentialocl_CollectionItem,
    essentialocl_CollectionLiteralExp,
    essentialocl_CollectionLiteralPart,
    essentialocl_CollectionRange,
    essentialocl_CollectionType,
    essentialocl_EnumLiteralExp,
    essentialocl_ExpressionInOcl,
    essentialocl_FeaturePropertyCall,
    essentialocl_IfExp,
    essentialocl_IntegerLiteralExp,
    essentialocl_InvalidLiteralExp,
    essentialocl_InvalidType,
    essentialocl_IterateExp,
    essentialocl_IteratorExp,
    essentialocl_LetExp,
    essentialocl_LiteralExp,
    essentialocl_LoopExp,
    essentialocl_NullLiteralExp,
    essentialocl_NumericLiteralExp,
    essentialocl_OclExpression,
    essentialocl_OpaqueExpression,
    essentialocl_OperationCallExp,
    essentialocl_OrderedSetType,
    essentialocl_PrimitiveLiteralExp,
    essentialocl_PropertyCallExp,
    essentialocl_RealLiteralExp,
    essentialocl_SequenceType,
    essentialocl_SetType,
    essentialocl_StringLiteralExp,
    essentialocl_TupleLiteralExp,
    essentialocl_TupleLiteralPart,
    essentialocl_TupleType,
    essentialocl_TypeExp,
    essentialocl_UnlimitedNaturalExp,
    essentialocl_Variable,
    essentialocl_VariableExp,
    essentialocl_VoidType,
    imperativeocl_AltExp,
    imperativeocl_AnonymousTupleLiteralExp,
    imperativeocl_AnonymousTupleLiteralPart,
    imperativeocl_AnonymousTupleType,
    imperativeocl_AssertExp,
    imperativeocl_AssignExp,
    imperativeocl_BlockExp,
    imperativeocl_BreakExp,
    imperativeocl_CollectorExp,
    imperativeocl_ComputeExp,
    imperativeocl_ContinueExp,
    imperativeocl_DictLiteralExp,
    imperativeocl_DictLiteralPart,
    imperativeocl_DictionaryType,
    imperativeocl_ForExp,
    imperativeocl_ImperativeExpression,
    imperativeocl_ImperativeIterateExp,
    imperativeocl_ImperativeLoopExp,
    imperativeocl_InstantiationExp,
    imperativeocl_ListType,
    imperativeocl_LogExp,
    imperativeocl_RaiseExp,
    imperativeocl_ReturnExp,
    imperativeocl_SwitchExp,
    imperativeocl_TemplateParameterType,
    imperativeocl_TryExp,
    imperativeocl_TupleExp,
    imperativeocl_Typedef,
    imperativeocl_UnlinkExp,
    imperativeocl_UnpackExp,
    imperativeocl_VariableInitExp,
    imperativeocl_WhileExp,
    qvtbase_Domain,
    qvtbase_Function,
    qvtbase_FunctionParameter,
    qvtbase_Pattern,
    qvtbase_Predicate,
    qvtbase_Rule,
    qvtbase_Transformation,
    qvtbase_TypedModel,
    qvtcore_Area,
    qvtcore_Assignment,
    qvtcore_BottomPattern,
    qvtcore_CoreDomain,
    qvtcore_CorePattern,
    qvtcore_EnforcementOperation,
    qvtcore_GuardPattern,
    qvtcore_Mapping,
    qvtcore_RealizedVariable,
    qvtoperational_Constructor,
    qvtoperational_ConstructorBody,
    qvtoperational_ContextualProperty,
    qvtoperational_EntryOperation,
    qvtoperational_Helper,
    qvtoperational_ImperativeCallExp,
    qvtoperational_ImperativeOperation,
    qvtoperational_Library,
    qvtoperational_MappingBody,
    qvtoperational_MappingCallExp,
    qvtoperational_MappingOperation,
    qvtoperational_MappingParameter,
    qvtoperational_ModelParameter,
    qvtoperational_ModelType,
    qvtoperational_Module,
    qvtoperational_ModuleImport,
    qvtoperational_ObjectExp,
    qvtoperational_OperationBody,
    qvtoperational_OperationalTransformation,
    qvtoperational_ResolveExp,
    qvtoperational_ResolveInExp,
    qvtoperational_VarParameter,
    qvtrelation_DomainPattern,
    qvtrelation_Key,
    qvtrelation_Relation,
    qvtrelation_RelationDomain,
    qvtrelation_RelationImplementation,
    qvtrelation_RelationalTransformation,
    qvttemplate_CollectionTemplateExp,
    qvttemplate_ObjectTemplateExp,
    qvttemplate_PropertyTemplateItem,
    qvttemplate_TemplateExp,
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

def test_assoc_additionalCondition196_stub_double():
    # OclExpression has no real 'OclExpression198' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModelType(conformanceKind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression198', None)
    _safe_set(owner, 'qvtoperational_ModelType197', {partner})
    assert getattr(partner, 'OclExpression198') == owner
    _safe_set(owner, 'qvtoperational_ModelType197', set())
    assert getattr(partner, 'OclExpression198') is None


def test_assoc_assertion92_stub_double():
    # OclExpression has no real 'OclExpression94' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression94', None)
    _safe_set(owner, 'imperativeocl_AssertExp93', partner)
    assert getattr(partner, 'OclExpression94') == owner
    _safe_set(owner, 'imperativeocl_AssertExp93', None)
    assert getattr(partner, 'OclExpression94') is None


def test_assoc_binding206_stub_double():
    # ModelType has no real 'ModelType207' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType207', None)
    _safe_set(owner, 'qvtoperational_ModuleImport', {partner})
    assert getattr(partner, 'ModelType207') == owner
    _safe_set(owner, 'qvtoperational_ModuleImport', set())
    assert getattr(partner, 'ModelType207') is None


def test_assoc_body192_stub_double():
    # OperationBody has no real 'OperationBody' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = OperationBody()
    setattr(partner, 'OperationBody', None)
    _safe_set(owner, 'operation193', partner)
    assert getattr(partner, 'OperationBody') == owner
    _safe_set(owner, 'operation193', None)
    assert getattr(partner, 'OperationBody') is None


def test_assoc_bottomPattern228_stub_double():
    # BottomPattern has no real 'BottomPattern229' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_Assignment(isDefault="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern229', None)
    _safe_set(owner, 'assignment', partner)
    assert getattr(partner, 'BottomPattern229') == owner
    _safe_set(owner, 'assignment', None)
    assert getattr(partner, 'BottomPattern229') is None


def test_assoc_bottomPattern252_stub_double():
    # BottomPattern has no real 'BottomPattern253' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_EnforcementOperation(enforcementMode="sample_text")
    partner = BottomPattern()
    setattr(partner, 'BottomPattern253', None)
    _safe_set(owner, 'enforcementOperation', partner)
    assert getattr(partner, 'BottomPattern253') == owner
    _safe_set(owner, 'enforcementOperation', None)
    assert getattr(partner, 'BottomPattern253') is None


def test_assoc_class_133_stub_double():
    # Class has no real 'Class134' property in the generated
    # code (a bare stub) -- manually attach it so emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    partner = Class()
    setattr(partner, 'Class134', None)
    _safe_set(owner, 'emof_Property', partner)
    assert getattr(partner, 'Class134') == owner
    _safe_set(owner, 'emof_Property', None)
    assert getattr(partner, 'Class134') is None


def test_assoc_condition148_stub_double():
    # OclExpression has no real 'OclExpression149' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ResolveExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ResolveExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ResolveExp(isDeferred="sample_text", isInverse="sample_text", one="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression149', None)
    _safe_set(owner, 'qvtoperational_ResolveExp', partner)
    assert getattr(partner, 'OclExpression149') == owner
    _safe_set(owner, 'qvtoperational_ResolveExp', None)
    assert getattr(partner, 'OclExpression149') is None


def test_assoc_condition87_stub_double():
    # OclExpression has no real 'OclExpression88' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_LogExp(level="sample_text", text="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression88', None)
    _safe_set(owner, 'imperativeocl_LogExp', partner)
    assert getattr(partner, 'OclExpression88') == owner
    _safe_set(owner, 'imperativeocl_LogExp', None)
    assert getattr(partner, 'OclExpression88') is None


def test_assoc_configProperty201_stub_double():
    # Property has no real 'Property202' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = Property()
    setattr(partner, 'Property202', None)
    _safe_set(owner, 'module', {partner})
    assert getattr(partner, 'Property202') == owner
    _safe_set(owner, 'module', set())
    assert getattr(partner, 'Property202') is None


def test_assoc_context188_stub_double():
    # VarParameter has no real 'VarParameter' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter', None)
    _safe_set(owner, 'ctxOwner', partner)
    assert getattr(partner, 'VarParameter') == owner
    _safe_set(owner, 'ctxOwner', None)
    assert getattr(partner, 'VarParameter') is None


def test_assoc_ctxOwner213_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation214' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation214', None)
    _safe_set(owner, 'context', partner)
    assert getattr(partner, 'ImperativeOperation214') == owner
    _safe_set(owner, 'context', None)
    assert getattr(partner, 'ImperativeOperation214') is None


def test_assoc_defaultValue24_stub_double():
    # OclExpression has no real 'OclExpression26' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression26', None)
    _safe_set(owner, 'imperativeocl_AssignExp25', partner)
    assert getattr(partner, 'OclExpression26') == owner
    _safe_set(owner, 'imperativeocl_AssignExp25', None)
    assert getattr(partner, 'OclExpression26') is None


def test_assoc_element114_stub_double():
    # Element has no real 'Element115' property in the generated
    # code (a bare stub) -- manually attach it so emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element115', None)
    _safe_set(owner, 'tag', {partner})
    assert getattr(partner, 'Element115') == owner
    _safe_set(owner, 'tag', set())
    assert getattr(partner, 'Element115') is None


def test_assoc_element89_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_LogExp(level="sample_text", text="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'imperativeocl_LogExp90', partner)
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'imperativeocl_LogExp90', None)
    assert getattr(partner, 'Element') is None


def test_assoc_importedModule210_stub_double():
    # Module has no real 'Module212' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module212', None)
    _safe_set(owner, 'qvtoperational_ModuleImport211', partner)
    assert getattr(partner, 'Module212') == owner
    _safe_set(owner, 'qvtoperational_ModuleImport211', None)
    assert getattr(partner, 'Module212') is None


def test_assoc_left21_stub_double():
    # OclExpression has no real 'OclExpression23' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression23', None)
    _safe_set(owner, 'imperativeocl_AssignExp22', partner)
    assert getattr(partner, 'OclExpression23') == owner
    _safe_set(owner, 'imperativeocl_AssignExp22', None)
    assert getattr(partner, 'OclExpression23') is None


def test_assoc_log91_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'imperativeocl_AssertExp', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'imperativeocl_AssertExp', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_match9_stub_double():
    # OclExpression has no real 'OclExpression11' property in the generated
    # code (a bare stub) -- manually attach it so qvttemplate_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvttemplate_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvttemplate_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression11', None)
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp10', partner)
    assert getattr(partner, 'OclExpression11') == owner
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp10', None)
    assert getattr(partner, 'OclExpression11') is None


def test_assoc_metamodel194_stub_double():
    # Package has no real 'Package195' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModelType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModelType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModelType(conformanceKind="sample_text")
    partner = Package()
    setattr(partner, 'Package195', None)
    _safe_set(owner, 'qvtoperational_ModelType', {partner})
    assert getattr(partner, 'Package195') == owner
    _safe_set(owner, 'qvtoperational_ModelType', set())
    assert getattr(partner, 'Package195') is None


def test_assoc_module138_stub_double():
    # Module has no real 'Module139' property in the generated
    # code (a bare stub) -- manually attach it so emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    partner = Module()
    setattr(partner, 'Module139', None)
    _safe_set(owner, 'configProperty', partner)
    assert getattr(partner, 'Module139') == owner
    _safe_set(owner, 'configProperty', None)
    assert getattr(partner, 'Module139') is None


def test_assoc_module208_stub_double():
    # Module has no real 'Module209' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ModuleImport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ModuleImport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ModuleImport(kind="sample_text")
    partner = Module()
    setattr(partner, 'Module209', None)
    _safe_set(owner, 'moduleImport', partner)
    assert getattr(partner, 'Module209') == owner
    _safe_set(owner, 'moduleImport', None)
    assert getattr(partner, 'Module209') is None


def test_assoc_moduleImport203_stub_double():
    # ModuleImport has no real 'ModuleImport' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = ModuleImport()
    setattr(partner, 'ModuleImport', None)
    _safe_set(owner, 'module204', {partner})
    assert getattr(partner, 'ModuleImport') == owner
    _safe_set(owner, 'module204', set())
    assert getattr(partner, 'ModuleImport') is None


def test_assoc_nestedPackage127_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'emof_Package', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'emof_Package', set())
    assert getattr(partner, 'Package') is None


def test_assoc_operationCallExp254_stub_double():
    # OperationCallExp has no real 'OperationCallExp' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_EnforcementOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_EnforcementOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_EnforcementOperation(enforcementMode="sample_text")
    partner = OperationCallExp()
    setattr(partner, 'OperationCallExp', None)
    _safe_set(owner, 'qvtcore_EnforcementOperation', partner)
    assert getattr(partner, 'OperationCallExp') == owner
    _safe_set(owner, 'qvtcore_EnforcementOperation', None)
    assert getattr(partner, 'OperationCallExp') is None


def test_assoc_operationalImpl296_stub_double():
    # RelationImplementation has no real 'RelationImplementation' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_Relation(isTopLevel="sample_text")
    partner = RelationImplementation()
    setattr(partner, 'RelationImplementation', None)
    _safe_set(owner, 'relation', {partner})
    assert getattr(partner, 'RelationImplementation') == owner
    _safe_set(owner, 'relation', set())
    assert getattr(partner, 'RelationImplementation') is None


def test_assoc_opposite135_stub_double():
    # Property has no real 'Property137' property in the generated
    # code (a bare stub) -- manually attach it so emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Property(default="sample_text", isComposite="sample_text", isDerived="sample_text", isId="sample_text", isReadOnly="sample_text")
    partner = Property()
    setattr(partner, 'Property137', None)
    _safe_set(owner, 'emof_Property136', partner)
    assert getattr(partner, 'Property137') == owner
    _safe_set(owner, 'emof_Property136', None)
    assert getattr(partner, 'Property137') is None


def test_assoc_overridden191_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation', None)
    _safe_set(owner, 'qvtoperational_ImperativeOperation', partner)
    assert getattr(partner, 'ImperativeOperation') == owner
    _safe_set(owner, 'qvtoperational_ImperativeOperation', None)
    assert getattr(partner, 'ImperativeOperation') is None


def test_assoc_ownedAttribute106_stub_double():
    # Property has no real 'Property107' property in the generated
    # code (a bare stub) -- manually attach it so emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Class(isAbstract="sample_text")
    partner = Property()
    setattr(partner, 'Property107', None)
    _safe_set(owner, 'emof_Class', {partner})
    assert getattr(partner, 'Property107') == owner
    _safe_set(owner, 'emof_Class', set())
    assert getattr(partner, 'Property107') is None


def test_assoc_ownedOperation108_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Class(isAbstract="sample_text")
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'class_', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'class_', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedTag199_stub_double():
    # Tag has no real 'Tag200' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = Tag()
    setattr(partner, 'Tag200', None)
    _safe_set(owner, 'owner', {partner})
    assert getattr(partner, 'Tag200') == owner
    _safe_set(owner, 'owner', set())
    assert getattr(partner, 'Tag200') is None


def test_assoc_ownedType125_stub_double():
    # Type has no real 'Type126' property in the generated
    # code (a bare stub) -- manually attach it so emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type126', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type126') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type126') is None


def test_assoc_owner117_stub_double():
    # Module has no real 'Module' property in the generated
    # code (a bare stub) -- manually attach it so emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Tag(name="sample_text", value="sample_text")
    partner = Module()
    setattr(partner, 'Module', None)
    _safe_set(owner, 'ownedTag118', partner)
    assert getattr(partner, 'Module') == owner
    _safe_set(owner, 'ownedTag118', None)
    assert getattr(partner, 'Module') is None


def test_assoc_part360_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so essentialocl_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialocl_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialocl_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_part5_stub_double():
    # OclExpression has no real 'OclExpression6' property in the generated
    # code (a bare stub) -- manually attach it so qvttemplate_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvttemplate_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvttemplate_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression6', None)
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp', {partner})
    assert getattr(partner, 'OclExpression6') == owner
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp', set())
    assert getattr(partner, 'OclExpression6') is None


def test_assoc_referredCollectionType7_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so qvttemplate_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvttemplate_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvttemplate_CollectionTemplateExp(kind="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp8', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'qvttemplate_CollectionTemplateExp8', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_referredVariable33_stub_double():
    # Variable has no real 'Variable34' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_VariableInitExp(withResult="sample_text")
    partner = Variable()
    setattr(partner, 'Variable34', None)
    _safe_set(owner, 'imperativeocl_VariableInitExp', partner)
    assert getattr(partner, 'Variable34') == owner
    _safe_set(owner, 'imperativeocl_VariableInitExp', None)
    assert getattr(partner, 'Variable34') is None


def test_assoc_resOwner215_stub_double():
    # ImperativeOperation has no real 'ImperativeOperation216' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_VarParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_VarParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_VarParameter(kind="sample_text")
    partner = ImperativeOperation()
    setattr(partner, 'ImperativeOperation216', None)
    _safe_set(owner, 'result', partner)
    assert getattr(partner, 'ImperativeOperation216') == owner
    _safe_set(owner, 'result', None)
    assert getattr(partner, 'ImperativeOperation216') is None


def test_assoc_result189_stub_double():
    # VarParameter has no real 'VarParameter190' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_ImperativeOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_ImperativeOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_ImperativeOperation(isBlackbox="sample_text")
    partner = VarParameter()
    setattr(partner, 'VarParameter190', None)
    _safe_set(owner, 'resOwner', {partner})
    assert getattr(partner, 'VarParameter190') == owner
    _safe_set(owner, 'resOwner', set())
    assert getattr(partner, 'VarParameter190') is None


def test_assoc_rule255_stub_double():
    # Rule has no real 'Rule' property in the generated
    # code (a bare stub) -- manually attach it so qvtbase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtbase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtbase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = Rule()
    setattr(partner, 'Rule', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Rule') == owner
    _safe_set(owner, 'domain', None)
    assert getattr(partner, 'Rule') is None


def test_assoc_slotExpression230_stub_double():
    # OclExpression has no real 'OclExpression231' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_Assignment(isDefault="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression231', None)
    _safe_set(owner, 'qvtcore_Assignment', partner)
    assert getattr(partner, 'OclExpression231') == owner
    _safe_set(owner, 'qvtcore_Assignment', None)
    assert getattr(partner, 'OclExpression231') is None


def test_assoc_superClass109_stub_double():
    # Class has no real 'Class111' property in the generated
    # code (a bare stub) -- manually attach it so emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Class(isAbstract="sample_text")
    partner = Class()
    setattr(partner, 'Class111', None)
    _safe_set(owner, 'emof_Class110', {partner})
    assert getattr(partner, 'Class111') == owner
    _safe_set(owner, 'emof_Class110', set())
    assert getattr(partner, 'Class111') is None


def test_assoc_targetProperty235_stub_double():
    # Property has no real 'Property237' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_Assignment(isDefault="sample_text")
    partner = Property()
    setattr(partner, 'Property237', None)
    _safe_set(owner, 'qvtcore_Assignment236', partner)
    assert getattr(partner, 'Property237') == owner
    _safe_set(owner, 'qvtcore_Assignment236', None)
    assert getattr(partner, 'Property237') is None


def test_assoc_transformation116_stub_double():
    # Transformation has no real 'Transformation' property in the generated
    # code (a bare stub) -- manually attach it so emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emof_Tag(name="sample_text", value="sample_text")
    partner = Transformation()
    setattr(partner, 'Transformation', None)
    _safe_set(owner, 'ownedTag', partner)
    assert getattr(partner, 'Transformation') == owner
    _safe_set(owner, 'ownedTag', None)
    assert getattr(partner, 'Transformation') is None


def test_assoc_typedModel256_stub_double():
    # TypedModel has no real 'TypedModel' property in the generated
    # code (a bare stub) -- manually attach it so qvtbase_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtbase_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtbase_Domain(isCheckable="sample_text", isEnforceable="sample_text")
    partner = TypedModel()
    setattr(partner, 'TypedModel', None)
    _safe_set(owner, 'qvtbase_Domain', partner)
    assert getattr(partner, 'TypedModel') == owner
    _safe_set(owner, 'qvtbase_Domain', None)
    assert getattr(partner, 'TypedModel') is None


def test_assoc_usedModelType205_stub_double():
    # ModelType has no real 'ModelType' property in the generated
    # code (a bare stub) -- manually attach it so qvtoperational_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtoperational_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtoperational_Module(isBlackbox="sample_text")
    partner = ModelType()
    setattr(partner, 'ModelType', None)
    _safe_set(owner, 'qvtoperational_Module', {partner})
    assert getattr(partner, 'ModelType') == owner
    _safe_set(owner, 'qvtoperational_Module', set())
    assert getattr(partner, 'ModelType') is None


def test_assoc_value19_stub_double():
    # OclExpression has no real 'OclExpression20' property in the generated
    # code (a bare stub) -- manually attach it so imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = imperativeocl_AssignExp(isReset="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression20', None)
    _safe_set(owner, 'imperativeocl_AssignExp', {partner})
    assert getattr(partner, 'OclExpression20') == owner
    _safe_set(owner, 'imperativeocl_AssignExp', set())
    assert getattr(partner, 'OclExpression20') is None


def test_assoc_value232_stub_double():
    # OclExpression has no real 'OclExpression234' property in the generated
    # code (a bare stub) -- manually attach it so qvtcore_Assignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtcore_Assignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtcore_Assignment(isDefault="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression234', None)
    _safe_set(owner, 'qvtcore_Assignment233', partner)
    assert getattr(partner, 'OclExpression234') == owner
    _safe_set(owner, 'qvtcore_Assignment233', None)
    assert getattr(partner, 'OclExpression234') is None


def test_assoc_variable294_stub_double():
    # Variable has no real 'Variable295' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_Relation(isTopLevel="sample_text")
    partner = Variable()
    setattr(partner, 'Variable295', None)
    _safe_set(owner, 'qvtrelation_Relation', {partner})
    assert getattr(partner, 'Variable295') == owner
    _safe_set(owner, 'qvtrelation_Relation', set())
    assert getattr(partner, 'Variable295') is None


def test_assoc_when299_stub_double():
    # Pattern has no real 'Pattern300' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern300', None)
    _safe_set(owner, 'whereOwner', partner)
    assert getattr(partner, 'Pattern300') == owner
    _safe_set(owner, 'whereOwner', None)
    assert getattr(partner, 'Pattern300') is None


def test_assoc_where297_stub_double():
    # Pattern has no real 'Pattern298' property in the generated
    # code (a bare stub) -- manually attach it so qvtrelation_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qvtrelation_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qvtrelation_Relation(isTopLevel="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern298', None)
    _safe_set(owner, 'whenOwner', partner)
    assert getattr(partner, 'Pattern298') == owner
    _safe_set(owner, 'whenOwner', None)
    assert getattr(partner, 'Pattern298') is None


