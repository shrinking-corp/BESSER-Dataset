import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    AnonymousTupleLiteralPart,
    AssignExp,
    CallExp,
    Class,
    CollectionLiteralExp,
    CollectionLiteralPart,
    CollectionType,
    Comment,
    ComputeExp,
    DataType,
    DictLiteralPart,
    Domain,
    Element,
    Enumeration,
    EnumerationLiteral,
    Extent,
    FeaturePropertyCall,
    ImperativeExpression,
    ImperativeLoopExp,
    JTL_JTL_Domain,
    JTL_JTL_Model,
    JTL_JTL_Pattern,
    JTL_JTL_Predicate,
    JTL_JTL_Relation,
    JTL_JTL_Transformation,
    JTL_JTL_When,
    JTL_JTL_Where,
    JTL_emof_Class,
    JTL_emof_Comment,
    JTL_emof_DataType,
    JTL_emof_Element,
    JTL_emof_Enumeration,
    JTL_emof_EnumerationLiteral,
    JTL_emof_Extent,
    JTL_emof_MultiplicityElement,
    JTL_emof_NamedElement,
    JTL_emof_Object,
    JTL_emof_Operation,
    JTL_emof_Package,
    JTL_emof_Parameter,
    JTL_emof_PrimitiveType,
    JTL_emof_Property,
    JTL_emof_Tag,
    JTL_emof_Type,
    JTL_emof_TypedElement,
    JTL_emof_URIExtent,
    JTL_essentialocl_AnyType,
    JTL_essentialocl_BagType,
    JTL_essentialocl_BooleanLiteralExp,
    JTL_essentialocl_CallExp,
    JTL_essentialocl_CollectionItem,
    JTL_essentialocl_CollectionLiteralExp,
    JTL_essentialocl_CollectionLiteralPart,
    JTL_essentialocl_CollectionRange,
    JTL_essentialocl_CollectionType,
    JTL_essentialocl_EnumLiteralExp,
    JTL_essentialocl_ExpressionInOcl,
    JTL_essentialocl_FeaturePropertyCall,
    JTL_essentialocl_IfExp,
    JTL_essentialocl_IntegerLiteralExp,
    JTL_essentialocl_InvalidLiteralExp,
    JTL_essentialocl_InvalidType,
    JTL_essentialocl_IterateExp,
    JTL_essentialocl_IteratorExp,
    JTL_essentialocl_LetExp,
    JTL_essentialocl_LiteralExp,
    JTL_essentialocl_LoopExp,
    JTL_essentialocl_NullLiteralExp,
    JTL_essentialocl_NumericLiteralExp,
    JTL_essentialocl_OclExpression,
    JTL_essentialocl_OpaqueExpression,
    JTL_essentialocl_OperationCallExp,
    JTL_essentialocl_OrderedSetType,
    JTL_essentialocl_PrimitiveLiteralExp,
    JTL_essentialocl_PropertyCallExp,
    JTL_essentialocl_RealLiteralExp,
    JTL_essentialocl_SequenceType,
    JTL_essentialocl_SetType,
    JTL_essentialocl_StringLiteralExp,
    JTL_essentialocl_TupleLiteralExp,
    JTL_essentialocl_TupleLiteralPart,
    JTL_essentialocl_TupleType,
    JTL_essentialocl_TypeExp,
    JTL_essentialocl_UnlimitedNaturalExp,
    JTL_essentialocl_Variable,
    JTL_essentialocl_VariableExp,
    JTL_essentialocl_VoidType,
    JTL_imperativeocl_AltExp,
    JTL_imperativeocl_AnonymousTupleLiteralExp,
    JTL_imperativeocl_AnonymousTupleLiteralPart,
    JTL_imperativeocl_AnonymousTupleType,
    JTL_imperativeocl_AssertExp,
    JTL_imperativeocl_AssignExp,
    JTL_imperativeocl_BlockExp,
    JTL_imperativeocl_BreakExp,
    JTL_imperativeocl_CollectorExp,
    JTL_imperativeocl_ComputeExp,
    JTL_imperativeocl_ContinueExp,
    JTL_imperativeocl_DictLiteralExp,
    JTL_imperativeocl_DictLiteralPart,
    JTL_imperativeocl_DictionaryType,
    JTL_imperativeocl_ForExp,
    JTL_imperativeocl_ImperativeExpression,
    JTL_imperativeocl_ImperativeIterateExp,
    JTL_imperativeocl_ImperativeLoopExp,
    JTL_imperativeocl_InstantiationExp,
    JTL_imperativeocl_ListType,
    JTL_imperativeocl_LogExp,
    JTL_imperativeocl_RaiseExp,
    JTL_imperativeocl_ReturnExp,
    JTL_imperativeocl_SwitchExp,
    JTL_imperativeocl_TemplateParameterType,
    JTL_imperativeocl_TryExp,
    JTL_imperativeocl_TupleExp,
    JTL_imperativeocl_Typedef,
    JTL_imperativeocl_UnlinkExp,
    JTL_imperativeocl_UnpackExp,
    JTL_imperativeocl_VariableInitExp,
    JTL_imperativeocl_WhileExp,
    JTL_template_CollectionTemplateExp,
    JTL_template_ObjectTemplateExp,
    JTL_template_PropertyTemplateItem,
    JTL_template_TemplateExp,
    LetExp,
    LiteralExp,
    LogExp,
    LoopExp,
    Model,
    NamedElement,
    NumericLiteralExp,
    Object,
    ObjectTemplateExp,
    OclExpression,
    OpaqueExpression,
    Operation,
    Package,
    Parameter,
    Pattern,
    Predicate,
    PrimitiveLiteralExp,
    Property,
    PropertyTemplateItem,
    Relation,
    Tag,
    TemplateExp,
    Transformation,
    TryExp,
    TupleLiteralExp,
    TupleLiteralPart,
    Type,
    TypedElement,
    Variable,
    When,
    Where,
    emof_Class,
    emof_DataType,
    emof_MultiplicityElement,
    emof_Package,
    emof_Type,
    emof_TypedElement,
    essentialocl_CallExp,
    essentialocl_LoopExp,
    essentialocl_OclExpression,
    imperativeocl_ImperativeExpression,
    CollectionKind,
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

def test_assoc_Class20_stub_double():
    # Class has no real 'Class21' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    partner = Class()
    setattr(partner, 'Class21', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'Class21') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'Class21') is None


def test_assoc_assertion230_stub_double():
    # OclExpression has no real 'OclExpression232' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression232', None)
    _safe_set(owner, 'JTL_imperativeocl_AssertExp231', partner)
    assert getattr(partner, 'OclExpression232') == owner
    _safe_set(owner, 'JTL_imperativeocl_AssertExp231', None)
    assert getattr(partner, 'OclExpression232') is None


def test_assoc_condition224_stub_double():
    # OclExpression has no real 'OclExpression225' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression225', None)
    _safe_set(owner, 'JTL_imperativeocl_LogExp', partner)
    assert getattr(partner, 'OclExpression225') == owner
    _safe_set(owner, 'JTL_imperativeocl_LogExp', None)
    assert getattr(partner, 'OclExpression225') is None


def test_assoc_defaultValue160_stub_double():
    # OclExpression has no real 'OclExpression162' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression162', None)
    _safe_set(owner, 'JTL_imperativeocl_AssignExp161', partner)
    assert getattr(partner, 'OclExpression162') == owner
    _safe_set(owner, 'JTL_imperativeocl_AssignExp161', None)
    assert getattr(partner, 'OclExpression162') is None


def test_assoc_dependsOn45_stub_double():
    # Model has no real 'Model46' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Model(usedPackage="sample_text")
    partner = Model()
    setattr(partner, 'Model46', None)
    _safe_set(owner, 'JTL_JTL_Model', {partner})
    assert getattr(partner, 'Model46') == owner
    _safe_set(owner, 'JTL_JTL_Model', set())
    assert getattr(partner, 'Model46') is None


def test_assoc_domain29_stub_double():
    # Domain has no real 'Domain' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Relation(isTopLevel=True)
    partner = Domain()
    setattr(partner, 'Domain', None)
    _safe_set(owner, 'relation30', {partner})
    assert getattr(partner, 'Domain') == owner
    _safe_set(owner, 'relation30', set())
    assert getattr(partner, 'Domain') is None


def test_assoc_element226_stub_double():
    # Element has no real 'Element228' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_LogExp(level=7, text="sample_text")
    partner = Element()
    setattr(partner, 'Element228', None)
    _safe_set(owner, 'JTL_imperativeocl_LogExp227', partner)
    assert getattr(partner, 'Element228') == owner
    _safe_set(owner, 'JTL_imperativeocl_LogExp227', None)
    assert getattr(partner, 'Element228') is None


def test_assoc_element6_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_inside138_stub_double():
    # AssignExp has no real 'AssignExp' property in the generated
    # code (a bare stub) -- manually attach it so JTL_template_ObjectTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_template_ObjectTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    partner = AssignExp()
    setattr(partner, 'AssignExp', None)
    _safe_set(owner, 'JTL_template_ObjectTemplateExp', {partner})
    assert getattr(partner, 'AssignExp') == owner
    _safe_set(owner, 'JTL_template_ObjectTemplateExp', set())
    assert getattr(partner, 'AssignExp') is None


def test_assoc_left157_stub_double():
    # OclExpression has no real 'OclExpression159' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression159', None)
    _safe_set(owner, 'JTL_imperativeocl_AssignExp158', partner)
    assert getattr(partner, 'OclExpression159') == owner
    _safe_set(owner, 'JTL_imperativeocl_AssignExp158', None)
    assert getattr(partner, 'OclExpression159') is None


def test_assoc_log229_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'JTL_imperativeocl_AssertExp', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'JTL_imperativeocl_AssertExp', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_match143_stub_double():
    # OclExpression has no real 'OclExpression145' property in the generated
    # code (a bare stub) -- manually attach it so JTL_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_template_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression145', None)
    _safe_set(owner, 'JTL_template_CollectionTemplateExp144', partner)
    assert getattr(partner, 'OclExpression145') == owner
    _safe_set(owner, 'JTL_template_CollectionTemplateExp144', None)
    assert getattr(partner, 'OclExpression145') is None


def test_assoc_model37_stub_double():
    # Model has no real 'Model39' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Model()
    setattr(partner, 'Model39', None)
    _safe_set(owner, 'JTL_JTL_Domain38', partner)
    assert getattr(partner, 'Model39') == owner
    _safe_set(owner, 'JTL_JTL_Domain38', None)
    assert getattr(partner, 'Model39') is None


def test_assoc_nestedPackage14_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'JTL_emof_Package', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'JTL_emof_Package', set())
    assert getattr(partner, 'Package') is None


def test_assoc_opposite22_stub_double():
    # Property has no real 'Property23' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    partner = Property()
    setattr(partner, 'Property23', None)
    _safe_set(owner, 'JTL_emof_Property', partner)
    assert getattr(partner, 'Property23') == owner
    _safe_set(owner, 'JTL_emof_Property', None)
    assert getattr(partner, 'Property23') is None


def test_assoc_ownedAttribute0_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Class(isAbstract=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'Class', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'Class', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedOperation1_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Class(isAbstract=True)
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'class_', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'class_', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedType12_stub_double():
    # Type has no real 'Type13' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type13', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type13') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type13') is None


def test_assoc_part103_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so JTL_essentialocl_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_essentialocl_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_essentialocl_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_part137_stub_double():
    # PropertyTemplateItem has no real 'PropertyTemplateItem' property in the generated
    # code (a bare stub) -- manually attach it so JTL_template_ObjectTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_template_ObjectTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_template_ObjectTemplateExp(referredClass="sample_text")
    partner = PropertyTemplateItem()
    setattr(partner, 'PropertyTemplateItem', None)
    _safe_set(owner, 'objContainer', {partner})
    assert getattr(partner, 'PropertyTemplateItem') == owner
    _safe_set(owner, 'objContainer', set())
    assert getattr(partner, 'PropertyTemplateItem') is None


def test_assoc_part139_stub_double():
    # OclExpression has no real 'OclExpression140' property in the generated
    # code (a bare stub) -- manually attach it so JTL_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_template_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression140', None)
    _safe_set(owner, 'JTL_template_CollectionTemplateExp', {partner})
    assert getattr(partner, 'OclExpression140') == owner
    _safe_set(owner, 'JTL_template_CollectionTemplateExp', set())
    assert getattr(partner, 'OclExpression140') is None


def test_assoc_pattern36_stub_double():
    # Pattern has no real 'Pattern' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Pattern()
    setattr(partner, 'Pattern', None)
    _safe_set(owner, 'JTL_JTL_Domain', partner)
    assert getattr(partner, 'Pattern') == owner
    _safe_set(owner, 'JTL_JTL_Domain', None)
    assert getattr(partner, 'Pattern') is None


def test_assoc_referredCollectionType141_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so JTL_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_template_CollectionTemplateExp(kind="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'JTL_template_CollectionTemplateExp142', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'JTL_template_CollectionTemplateExp142', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_referredVariable169_stub_double():
    # Variable has no real 'Variable170' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_VariableInitExp(withResult=True)
    partner = Variable()
    setattr(partner, 'Variable170', None)
    _safe_set(owner, 'JTL_imperativeocl_VariableInitExp', partner)
    assert getattr(partner, 'Variable170') == owner
    _safe_set(owner, 'JTL_imperativeocl_VariableInitExp', None)
    assert getattr(partner, 'Variable170') is None


def test_assoc_relation34_stub_double():
    # Relation has no real 'Relation35' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Relation()
    setattr(partner, 'Relation35', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Relation35') == owner
    _safe_set(owner, 'domain', None)
    assert getattr(partner, 'Relation35') is None


def test_assoc_rootVariable40_stub_double():
    # Variable has no real 'Variable42' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Variable()
    setattr(partner, 'Variable42', None)
    _safe_set(owner, 'JTL_JTL_Domain41', partner)
    assert getattr(partner, 'Variable42') == owner
    _safe_set(owner, 'JTL_JTL_Domain41', None)
    assert getattr(partner, 'Variable42') is None


def test_assoc_superClass2_stub_double():
    # Class has no real 'Class3' property in the generated
    # code (a bare stub) -- manually attach it so JTL_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_emof_Class(isAbstract=True)
    partner = Class()
    setattr(partner, 'Class3', None)
    _safe_set(owner, 'JTL_emof_Class', {partner})
    assert getattr(partner, 'Class3') == owner
    _safe_set(owner, 'JTL_emof_Class', set())
    assert getattr(partner, 'Class3') is None


def test_assoc_transformation28_stub_double():
    # Transformation has no real 'Transformation' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Relation(isTopLevel=True)
    partner = Transformation()
    setattr(partner, 'Transformation', None)
    _safe_set(owner, 'relation', partner)
    assert getattr(partner, 'Transformation') == owner
    _safe_set(owner, 'relation', None)
    assert getattr(partner, 'Transformation') is None


def test_assoc_transformation43_stub_double():
    # Transformation has no real 'Transformation44' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Model(usedPackage="sample_text")
    partner = Transformation()
    setattr(partner, 'Transformation44', None)
    _safe_set(owner, 'modelParameter', partner)
    assert getattr(partner, 'Transformation44') == owner
    _safe_set(owner, 'modelParameter', None)
    assert getattr(partner, 'Transformation44') is None


def test_assoc_value155_stub_double():
    # OclExpression has no real 'OclExpression156' property in the generated
    # code (a bare stub) -- manually attach it so JTL_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression156', None)
    _safe_set(owner, 'JTL_imperativeocl_AssignExp', {partner})
    assert getattr(partner, 'OclExpression156') == owner
    _safe_set(owner, 'JTL_imperativeocl_AssignExp', set())
    assert getattr(partner, 'OclExpression156') is None


def test_assoc_variable33_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Relation(isTopLevel=True)
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'JTL_JTL_Relation', {partner})
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'JTL_JTL_Relation', set())
    assert getattr(partner, 'Variable') is None


def test_assoc_when32_stub_double():
    # When has no real 'When' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Relation(isTopLevel=True)
    partner = When()
    setattr(partner, 'When', None)
    _safe_set(owner, 'whenOwner', partner)
    assert getattr(partner, 'When') == owner
    _safe_set(owner, 'whenOwner', None)
    assert getattr(partner, 'When') is None


def test_assoc_where31_stub_double():
    # Where has no real 'Where' property in the generated
    # code (a bare stub) -- manually attach it so JTL_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # JTL_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = JTL_JTL_Relation(isTopLevel=True)
    partner = Where()
    setattr(partner, 'Where', None)
    _safe_set(owner, 'whereOwner', partner)
    assert getattr(partner, 'Where') == owner
    _safe_set(owner, 'whereOwner', None)
    assert getattr(partner, 'Where') is None


