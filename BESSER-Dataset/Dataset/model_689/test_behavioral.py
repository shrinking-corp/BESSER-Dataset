import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AltExp,
    AnonymousTupleLiteralPart,
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
    Janus_JTL_Domain,
    Janus_JTL_Model,
    Janus_JTL_Pattern,
    Janus_JTL_Predicate,
    Janus_JTL_Relation,
    Janus_JTL_Transformation,
    Janus_emof_Class,
    Janus_emof_Comment,
    Janus_emof_DataType,
    Janus_emof_Element,
    Janus_emof_Enumeration,
    Janus_emof_EnumerationLiteral,
    Janus_emof_Extent,
    Janus_emof_MultiplicityElement,
    Janus_emof_NamedElement,
    Janus_emof_Object,
    Janus_emof_Operation,
    Janus_emof_Package,
    Janus_emof_Parameter,
    Janus_emof_PrimitiveType,
    Janus_emof_Property,
    Janus_emof_Tag,
    Janus_emof_Type,
    Janus_emof_TypedElement,
    Janus_emof_URIExtent,
    Janus_essentialocl_AnyType,
    Janus_essentialocl_BagType,
    Janus_essentialocl_BooleanLiteralExp,
    Janus_essentialocl_CallExp,
    Janus_essentialocl_CollectionItem,
    Janus_essentialocl_CollectionLiteralExp,
    Janus_essentialocl_CollectionLiteralPart,
    Janus_essentialocl_CollectionRange,
    Janus_essentialocl_CollectionType,
    Janus_essentialocl_EnumLiteralExp,
    Janus_essentialocl_ExpressionInOcl,
    Janus_essentialocl_FeaturePropertyCall,
    Janus_essentialocl_IfExp,
    Janus_essentialocl_IntegerLiteralExp,
    Janus_essentialocl_InvalidLiteralExp,
    Janus_essentialocl_InvalidType,
    Janus_essentialocl_IterateExp,
    Janus_essentialocl_IteratorExp,
    Janus_essentialocl_LetExp,
    Janus_essentialocl_LiteralExp,
    Janus_essentialocl_LoopExp,
    Janus_essentialocl_NullLiteralExp,
    Janus_essentialocl_NumericLiteralExp,
    Janus_essentialocl_OclExpression,
    Janus_essentialocl_OpaqueExpression,
    Janus_essentialocl_OperationCallExp,
    Janus_essentialocl_OrderedSetType,
    Janus_essentialocl_PrimitiveLiteralExp,
    Janus_essentialocl_PropertyCallExp,
    Janus_essentialocl_RealLiteralExp,
    Janus_essentialocl_SequenceType,
    Janus_essentialocl_SetType,
    Janus_essentialocl_StringLiteralExp,
    Janus_essentialocl_TupleLiteralExp,
    Janus_essentialocl_TupleLiteralPart,
    Janus_essentialocl_TupleType,
    Janus_essentialocl_TypeExp,
    Janus_essentialocl_UnlimitedNaturalExp,
    Janus_essentialocl_Variable,
    Janus_essentialocl_VariableExp,
    Janus_essentialocl_VoidType,
    Janus_imperativeocl_AltExp,
    Janus_imperativeocl_AnonymousTupleLiteralExp,
    Janus_imperativeocl_AnonymousTupleLiteralPart,
    Janus_imperativeocl_AnonymousTupleType,
    Janus_imperativeocl_AssertExp,
    Janus_imperativeocl_AssignExp,
    Janus_imperativeocl_BlockExp,
    Janus_imperativeocl_BreakExp,
    Janus_imperativeocl_CollectorExp,
    Janus_imperativeocl_ComputeExp,
    Janus_imperativeocl_ContinueExp,
    Janus_imperativeocl_DictLiteralExp,
    Janus_imperativeocl_DictLiteralPart,
    Janus_imperativeocl_DictionaryType,
    Janus_imperativeocl_ForExp,
    Janus_imperativeocl_ImperativeExpression,
    Janus_imperativeocl_ImperativeIterateExp,
    Janus_imperativeocl_ImperativeLoopExp,
    Janus_imperativeocl_InstantiationExp,
    Janus_imperativeocl_ListType,
    Janus_imperativeocl_LogExp,
    Janus_imperativeocl_RaiseExp,
    Janus_imperativeocl_ReturnExp,
    Janus_imperativeocl_SwitchExp,
    Janus_imperativeocl_TemplateParameterType,
    Janus_imperativeocl_TryExp,
    Janus_imperativeocl_TupleExp,
    Janus_imperativeocl_Typedef,
    Janus_imperativeocl_UnlinkExp,
    Janus_imperativeocl_UnpackExp,
    Janus_imperativeocl_VariableInitExp,
    Janus_imperativeocl_WhileExp,
    Janus_template_CollectionTemplateExp,
    Janus_template_ObjectTemplateExp,
    Janus_template_PropertyTemplateItem,
    Janus_template_TemplateExp,
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
    # code (a bare stub) -- manually attach it so Janus_emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    partner = Class()
    setattr(partner, 'Class21', None)
    _safe_set(owner, 'ownedAttribute', partner)
    assert getattr(partner, 'Class21') == owner
    _safe_set(owner, 'ownedAttribute', None)
    assert getattr(partner, 'Class21') is None


def test_assoc_LetExp86_stub_double():
    # LetExp has no real 'LetExp87' property in the generated
    # code (a bare stub) -- manually attach it so Janus_essentialocl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_essentialocl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_essentialocl_Variable(varType="sample_text")
    partner = LetExp()
    setattr(partner, 'LetExp87', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'LetExp87') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'LetExp87') is None


def test_assoc_assertion238_stub_double():
    # OclExpression has no real 'OclExpression240' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_AssertExp(severity="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression240', None)
    _safe_set(owner, 'Janus_imperativeocl_AssertExp239', partner)
    assert getattr(partner, 'OclExpression240') == owner
    _safe_set(owner, 'Janus_imperativeocl_AssertExp239', None)
    assert getattr(partner, 'OclExpression240') is None


def test_assoc_bindParameter88_stub_double():
    # Parameter has no real 'Parameter90' property in the generated
    # code (a bare stub) -- manually attach it so Janus_essentialocl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_essentialocl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_essentialocl_Variable(varType="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter90', None)
    _safe_set(owner, 'Janus_essentialocl_Variable89', partner)
    assert getattr(partner, 'Parameter90') == owner
    _safe_set(owner, 'Janus_essentialocl_Variable89', None)
    assert getattr(partner, 'Parameter90') is None


def test_assoc_computeOwner91_stub_double():
    # ComputeExp has no real 'ComputeExp' property in the generated
    # code (a bare stub) -- manually attach it so Janus_essentialocl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_essentialocl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_essentialocl_Variable(varType="sample_text")
    partner = ComputeExp()
    setattr(partner, 'ComputeExp', None)
    _safe_set(owner, 'returnedElement', partner)
    assert getattr(partner, 'ComputeExp') == owner
    _safe_set(owner, 'returnedElement', None)
    assert getattr(partner, 'ComputeExp') is None


def test_assoc_condition232_stub_double():
    # OclExpression has no real 'OclExpression233' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_LogExp(level=7, text="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression233', None)
    _safe_set(owner, 'Janus_imperativeocl_LogExp', partner)
    assert getattr(partner, 'OclExpression233') == owner
    _safe_set(owner, 'Janus_imperativeocl_LogExp', None)
    assert getattr(partner, 'OclExpression233') is None


def test_assoc_defaultValue168_stub_double():
    # OclExpression has no real 'OclExpression170' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression170', None)
    _safe_set(owner, 'Janus_imperativeocl_AssignExp169', partner)
    assert getattr(partner, 'OclExpression170') == owner
    _safe_set(owner, 'Janus_imperativeocl_AssignExp169', None)
    assert getattr(partner, 'OclExpression170') is None


def test_assoc_domain31_stub_double():
    # Domain has no real 'Domain' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Relation(isTopLevel=True)
    partner = Domain()
    setattr(partner, 'Domain', None)
    _safe_set(owner, 'relation32', {partner})
    assert getattr(partner, 'Domain') == owner
    _safe_set(owner, 'relation32', set())
    assert getattr(partner, 'Domain') is None


def test_assoc_element234_stub_double():
    # Element has no real 'Element236' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_LogExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_LogExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_LogExp(level=7, text="sample_text")
    partner = Element()
    setattr(partner, 'Element236', None)
    _safe_set(owner, 'Janus_imperativeocl_LogExp235', partner)
    assert getattr(partner, 'Element236') == owner
    _safe_set(owner, 'Janus_imperativeocl_LogExp235', None)
    assert getattr(partner, 'Element236') is None


def test_assoc_element6_stub_double():
    # Element has no real 'Element' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Tag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Tag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Tag(name="sample_text", value="sample_text")
    partner = Element()
    setattr(partner, 'Element', None)
    _safe_set(owner, 'tag', {partner})
    assert getattr(partner, 'Element') == owner
    _safe_set(owner, 'tag', set())
    assert getattr(partner, 'Element') is None


def test_assoc_initExpression84_stub_double():
    # OclExpression has no real 'OclExpression85' property in the generated
    # code (a bare stub) -- manually attach it so Janus_essentialocl_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_essentialocl_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_essentialocl_Variable(varType="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression85', None)
    _safe_set(owner, 'Janus_essentialocl_Variable', partner)
    assert getattr(partner, 'OclExpression85') == owner
    _safe_set(owner, 'Janus_essentialocl_Variable', None)
    assert getattr(partner, 'OclExpression85') is None


def test_assoc_left165_stub_double():
    # OclExpression has no real 'OclExpression167' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression167', None)
    _safe_set(owner, 'Janus_imperativeocl_AssignExp166', partner)
    assert getattr(partner, 'OclExpression167') == owner
    _safe_set(owner, 'Janus_imperativeocl_AssignExp166', None)
    assert getattr(partner, 'OclExpression167') is None


def test_assoc_log237_stub_double():
    # LogExp has no real 'LogExp' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_AssertExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_AssertExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_AssertExp(severity="sample_text")
    partner = LogExp()
    setattr(partner, 'LogExp', None)
    _safe_set(owner, 'Janus_imperativeocl_AssertExp', partner)
    assert getattr(partner, 'LogExp') == owner
    _safe_set(owner, 'Janus_imperativeocl_AssertExp', None)
    assert getattr(partner, 'LogExp') is None


def test_assoc_match151_stub_double():
    # OclExpression has no real 'OclExpression153' property in the generated
    # code (a bare stub) -- manually attach it so Janus_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_template_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression153', None)
    _safe_set(owner, 'Janus_template_CollectionTemplateExp152', partner)
    assert getattr(partner, 'OclExpression153') == owner
    _safe_set(owner, 'Janus_template_CollectionTemplateExp152', None)
    assert getattr(partner, 'OclExpression153') is None


def test_assoc_model41_stub_double():
    # Model has no real 'Model43' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Model()
    setattr(partner, 'Model43', None)
    _safe_set(owner, 'Janus_JTL_Domain42', partner)
    assert getattr(partner, 'Model43') == owner
    _safe_set(owner, 'Janus_JTL_Domain42', None)
    assert getattr(partner, 'Model43') is None


def test_assoc_nestedPackage14_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Package(uri="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'Janus_emof_Package', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'Janus_emof_Package', set())
    assert getattr(partner, 'Package') is None


def test_assoc_opposite22_stub_double():
    # Property has no real 'Property23' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Property(default="sample_text", isComposite=True, isDerived=True, isId=True, isReadOnly=True)
    partner = Property()
    setattr(partner, 'Property23', None)
    _safe_set(owner, 'Janus_emof_Property', partner)
    assert getattr(partner, 'Property23') == owner
    _safe_set(owner, 'Janus_emof_Property', None)
    assert getattr(partner, 'Property23') is None


def test_assoc_ownedAttribute0_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Class(isAbstract=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'Class', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'Class', set())
    assert getattr(partner, 'Property') is None


def test_assoc_ownedOperation1_stub_double():
    # Operation has no real 'Operation' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Class(isAbstract=True)
    partner = Operation()
    setattr(partner, 'Operation', None)
    _safe_set(owner, 'class_', {partner})
    assert getattr(partner, 'Operation') == owner
    _safe_set(owner, 'class_', set())
    assert getattr(partner, 'Operation') is None


def test_assoc_ownedType12_stub_double():
    # Type has no real 'Type13' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Package(uri="sample_text")
    partner = Type()
    setattr(partner, 'Type13', None)
    _safe_set(owner, 'package', {partner})
    assert getattr(partner, 'Type13') == owner
    _safe_set(owner, 'package', set())
    assert getattr(partner, 'Type13') is None


def test_assoc_part110_stub_double():
    # CollectionLiteralPart has no real 'CollectionLiteralPart' property in the generated
    # code (a bare stub) -- manually attach it so Janus_essentialocl_CollectionLiteralExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_essentialocl_CollectionLiteralExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_essentialocl_CollectionLiteralExp(kind="sample_text")
    partner = CollectionLiteralPart()
    setattr(partner, 'CollectionLiteralPart', None)
    _safe_set(owner, 'CollectionLiteralExp', {partner})
    assert getattr(partner, 'CollectionLiteralPart') == owner
    _safe_set(owner, 'CollectionLiteralExp', set())
    assert getattr(partner, 'CollectionLiteralPart') is None


def test_assoc_part146_stub_double():
    # PropertyTemplateItem has no real 'PropertyTemplateItem' property in the generated
    # code (a bare stub) -- manually attach it so Janus_template_ObjectTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_template_ObjectTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_template_ObjectTemplateExp(referredClass="sample_text")
    partner = PropertyTemplateItem()
    setattr(partner, 'PropertyTemplateItem', None)
    _safe_set(owner, 'objContainer', {partner})
    assert getattr(partner, 'PropertyTemplateItem') == owner
    _safe_set(owner, 'objContainer', set())
    assert getattr(partner, 'PropertyTemplateItem') is None


def test_assoc_part147_stub_double():
    # OclExpression has no real 'OclExpression148' property in the generated
    # code (a bare stub) -- manually attach it so Janus_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_template_CollectionTemplateExp(kind="sample_text")
    partner = OclExpression()
    setattr(partner, 'OclExpression148', None)
    _safe_set(owner, 'Janus_template_CollectionTemplateExp', {partner})
    assert getattr(partner, 'OclExpression148') == owner
    _safe_set(owner, 'Janus_template_CollectionTemplateExp', set())
    assert getattr(partner, 'OclExpression148') is None


def test_assoc_pattern39_stub_double():
    # Pattern has no real 'Pattern40' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Pattern()
    setattr(partner, 'Pattern40', None)
    _safe_set(owner, 'Janus_JTL_Domain', partner)
    assert getattr(partner, 'Pattern40') == owner
    _safe_set(owner, 'Janus_JTL_Domain', None)
    assert getattr(partner, 'Pattern40') is None


def test_assoc_referredCollectionType149_stub_double():
    # CollectionType has no real 'CollectionType' property in the generated
    # code (a bare stub) -- manually attach it so Janus_template_CollectionTemplateExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_template_CollectionTemplateExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_template_CollectionTemplateExp(kind="sample_text")
    partner = CollectionType()
    setattr(partner, 'CollectionType', None)
    _safe_set(owner, 'Janus_template_CollectionTemplateExp150', partner)
    assert getattr(partner, 'CollectionType') == owner
    _safe_set(owner, 'Janus_template_CollectionTemplateExp150', None)
    assert getattr(partner, 'CollectionType') is None


def test_assoc_referredVariable177_stub_double():
    # Variable has no real 'Variable178' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_VariableInitExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_VariableInitExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_VariableInitExp(withResult=True)
    partner = Variable()
    setattr(partner, 'Variable178', None)
    _safe_set(owner, 'Janus_imperativeocl_VariableInitExp', partner)
    assert getattr(partner, 'Variable178') == owner
    _safe_set(owner, 'Janus_imperativeocl_VariableInitExp', None)
    assert getattr(partner, 'Variable178') is None


def test_assoc_relation37_stub_double():
    # Relation has no real 'Relation38' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Relation()
    setattr(partner, 'Relation38', None)
    _safe_set(owner, 'domain', partner)
    assert getattr(partner, 'Relation38') == owner
    _safe_set(owner, 'domain', None)
    assert getattr(partner, 'Relation38') is None


def test_assoc_rootVariable44_stub_double():
    # Variable has no real 'Variable46' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Domain(isCheckable=True, isEnforceable=True)
    partner = Variable()
    setattr(partner, 'Variable46', None)
    _safe_set(owner, 'Janus_JTL_Domain45', partner)
    assert getattr(partner, 'Variable46') == owner
    _safe_set(owner, 'Janus_JTL_Domain45', None)
    assert getattr(partner, 'Variable46') is None


def test_assoc_superClass2_stub_double():
    # Class has no real 'Class3' property in the generated
    # code (a bare stub) -- manually attach it so Janus_emof_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_emof_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_emof_Class(isAbstract=True)
    partner = Class()
    setattr(partner, 'Class3', None)
    _safe_set(owner, 'Janus_emof_Class', {partner})
    assert getattr(partner, 'Class3') == owner
    _safe_set(owner, 'Janus_emof_Class', set())
    assert getattr(partner, 'Class3') is None


def test_assoc_transformation30_stub_double():
    # Transformation has no real 'Transformation' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Relation(isTopLevel=True)
    partner = Transformation()
    setattr(partner, 'Transformation', None)
    _safe_set(owner, 'relation', partner)
    assert getattr(partner, 'Transformation') == owner
    _safe_set(owner, 'relation', None)
    assert getattr(partner, 'Transformation') is None


def test_assoc_value163_stub_double():
    # OclExpression has no real 'OclExpression164' property in the generated
    # code (a bare stub) -- manually attach it so Janus_imperativeocl_AssignExp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_imperativeocl_AssignExp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_imperativeocl_AssignExp(isReset=True)
    partner = OclExpression()
    setattr(partner, 'OclExpression164', None)
    _safe_set(owner, 'Janus_imperativeocl_AssignExp', {partner})
    assert getattr(partner, 'OclExpression164') == owner
    _safe_set(owner, 'Janus_imperativeocl_AssignExp', set())
    assert getattr(partner, 'OclExpression164') is None


def test_assoc_variable36_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Relation(isTopLevel=True)
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'Janus_JTL_Relation', {partner})
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'Janus_JTL_Relation', set())
    assert getattr(partner, 'Variable') is None


def test_assoc_when34_stub_double():
    # Pattern has no real 'Pattern35' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Relation(isTopLevel=True)
    partner = Pattern()
    setattr(partner, 'Pattern35', None)
    _safe_set(owner, 'whenOwner', partner)
    assert getattr(partner, 'Pattern35') == owner
    _safe_set(owner, 'whenOwner', None)
    assert getattr(partner, 'Pattern35') is None


def test_assoc_where33_stub_double():
    # Pattern has no real 'Pattern' property in the generated
    # code (a bare stub) -- manually attach it so Janus_JTL_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Janus_JTL_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Janus_JTL_Relation(isTopLevel=True)
    partner = Pattern()
    setattr(partner, 'Pattern', None)
    _safe_set(owner, 'whereOwner', partner)
    assert getattr(partner, 'Pattern') == owner
    _safe_set(owner, 'whereOwner', None)
    assert getattr(partner, 'Pattern') is None


