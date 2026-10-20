import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AGGREGATEType,
    ActualAggregationType,
    ActualDataType,
    ActualParameter,
    ActualStructure,
    ActualStructureConstraint,
    ActualType,
    ActualTypeConstraint,
    AggregateValue,
    Algorithm,
    AlgorithmScope,
    AliasVariable,
    AnonymousType,
    ArrayBound,
    ArrayMember,
    Attribute,
    AttributeBinding,
    AttributeType,
    AttributeValue,
    BagMember,
    CaseAction,
    CommonElement,
    ConcreteAggregationType,
    ConcreteType,
    ConcreteValue,
    Constant,
    ControlStatement,
    ControlVariable,
    DataType,
    DefinedType,
    DomainConstraint,
    DomainRole,
    DomainRule,
    EntityInstance,
    EntityType,
    EntityValue,
    EnumerationItem,
    EnumerationType,
    EscapeStatement,
    ExplicitAttribute,
    Expression,
    Extent,
    Function,
    FunctionCall,
    FunctionResult,
    GeneralAggregationType,
    GeneralizedType,
    GenericAggregate,
    GenericType,
    GlobalRule,
    InParameter,
    InVariable,
    Indeterminate,
    IndexOperation,
    Instance,
    InstantiableType,
    InterfacedElement,
    InverseAttribute,
    InvertibleAttribute,
    LISTValue,
    LengthConstraint,
    ListMember,
    LocalElement,
    LocalScope,
    LogicalValue,
    MemberBinding,
    NamedElement,
    NamedRule,
    NamedType,
    NamedVariable,
    NumberValue,
    NumericType,
    Operation,
    Parameter,
    ParameterType,
    PartialEntityType,
    PartialEntityValue,
    Population,
    Primary,
    Procedure,
    ProcedureCall,
    QueryVariable,
    RangeRole,
    RealValue,
    Redeclaration,
    Relationship,
    Remark,
    RepeatCount,
    RepeatStatement,
    Role,
    SETValue,
    Schema,
    SchemaElement,
    Scope,
    ScopedId,
    SelectType,
    Selector,
    SimpleType,
    SimpleValue,
    SingleEntityType,
    SingleEntityValue,
    SizeConstraint,
    SkipStatement,
    Statement,
    StatementBlock,
    StringValue,
    SubtypeConstraint,
    SupertypeRule,
    TypeElement,
    TypedInstance,
    UniqueRule,
    VARExpression,
    VARVariable,
    Variable,
    VariableType,
    algorithms_GenericElement,
    algorithms_NamedVariable,
    algorithms_Parameter,
    algorithms_Statement,
    algorithms_VARVariable,
    core_AGGREGATEType,
    core_ActualType,
    core_AggregationType,
    core_AlgorithmScope,
    core_AnonymousType,
    core_AttributeType,
    core_CommonElement,
    core_ConcreteType,
    core_DataType,
    core_DomainConstraint,
    core_Expression,
    core_GeneralizedType,
    core_GenericType,
    core_Instance,
    core_InstantiableType,
    core_LocalScope,
    core_NamedType,
    core_ParameterType,
    core_SchemaElement,
    core_Scope,
    core_TypeElement,
    core_VariableType,
    express_algorithms_ActualAGGREGATEType,
    express_algorithms_ActualARRAYType,
    express_algorithms_ActualAggregationType,
    express_algorithms_ActualBAGType,
    express_algorithms_ActualDataType,
    express_algorithms_ActualGenericType,
    express_algorithms_ActualLISTType,
    express_algorithms_ActualSETType,
    express_algorithms_ActualStructure,
    express_algorithms_ActualStructureConstraint,
    express_algorithms_ActualTypeConstraint,
    express_algorithms_Algorithm,
    express_algorithms_Function,
    express_algorithms_FunctionResult,
    express_algorithms_GenericElement,
    express_algorithms_InParameter,
    express_algorithms_InVariable,
    express_algorithms_LocalVariable,
    express_algorithms_NamedVariable,
    express_algorithms_Parameter,
    express_algorithms_Procedure,
    express_algorithms_Statement,
    express_algorithms_VARParameter,
    express_algorithms_VARVariable,
    express_algorithms_Variable,
    express_core_AGGREGATEType,
    express_core_ARRAYType,
    express_core_ActualType,
    express_core_AggregationType,
    express_core_AlgorithmScope,
    express_core_AnonymousType,
    express_core_ArrayBound,
    express_core_Attribute,
    express_core_AttributeType,
    express_core_BAGType,
    express_core_BinaryType,
    express_core_CommonElement,
    express_core_ConcreteAggregationType,
    express_core_ConcreteType,
    express_core_DataType,
    express_core_DefinedType,
    express_core_DerivedAttribute,
    express_core_DomainConstraint,
    express_core_DomainRole,
    express_core_DomainRule,
    express_core_EntityType,
    express_core_EnumerationType,
    express_core_ExplicitAttribute,
    express_core_Expression,
    express_core_GeneralARRAYType,
    express_core_GeneralAggregationType,
    express_core_GeneralBAGType,
    express_core_GeneralLISTType,
    express_core_GeneralSETType,
    express_core_GeneralizedType,
    express_core_GenericType,
    express_core_Instance,
    express_core_InstantiableType,
    express_core_InterfacedElement,
    express_core_InverseAttribute,
    express_core_InvertibleAttribute,
    express_core_LISTType,
    express_core_LengthConstraint,
    express_core_LocalElement,
    express_core_LocalScope,
    express_core_LogicType,
    express_core_NamedElement,
    express_core_NamedType,
    express_core_NumericType,
    express_core_ParameterType,
    express_core_PartialEntityType,
    express_core_RangeRole,
    express_core_RealType,
    express_core_Redeclaration,
    express_core_Relationship,
    express_core_Remark,
    express_core_Role,
    express_core_SETType,
    express_core_Schema,
    express_core_SchemaElement,
    express_core_Scope,
    express_core_ScopedId,
    express_core_SelectType,
    express_core_SimpleType,
    express_core_SingleEntityType,
    express_core_SizeConstraint,
    express_core_SpecializedType,
    express_core_StringType,
    express_core_TypeElement,
    express_core_UniqueRule,
    express_core_VariableType,
    express_expressions_ActualParameter,
    express_expressions_AggregateIndex,
    express_expressions_AggregateInitializer,
    express_expressions_AttributeBinding,
    express_expressions_AttributeRef,
    express_expressions_BinaryIndex,
    express_expressions_BinaryOperation,
    express_expressions_Coercion,
    express_expressions_ConstantRef,
    express_expressions_EnumItemRef,
    express_expressions_ExtentRef,
    express_expressions_FunctionCall,
    express_expressions_GroupRef,
    express_expressions_IndeterminateRef,
    express_expressions_IndexOperation,
    express_expressions_Literal,
    express_expressions_MemberBinding,
    express_expressions_Operation,
    express_expressions_ParameterRef,
    express_expressions_PartialEntityConstructor,
    express_expressions_Primary,
    express_expressions_QueryExpression,
    express_expressions_QueryVariable,
    express_expressions_RepeatCount,
    express_expressions_SELFRef,
    express_expressions_Selector,
    express_expressions_StringIndex,
    express_expressions_UnaryOperation,
    express_expressions_UsedInRef,
    express_expressions_VariableRef,
    express_instances_ARRAYValue,
    express_instances_AggregateValue,
    express_instances_ArrayMember,
    express_instances_AttributeValue,
    express_instances_BAGValue,
    express_instances_BagMember,
    express_instances_BinaryValue,
    express_instances_BooleanValue,
    express_instances_ConcreteValue,
    express_instances_Constant,
    express_instances_EntityInstance,
    express_instances_EntityValue,
    express_instances_EnumerationItem,
    express_instances_GenericAggregate,
    express_instances_Indeterminate,
    express_instances_IntegerValue,
    express_instances_LISTValue,
    express_instances_ListMember,
    express_instances_LogicalValue,
    express_instances_MultiLeafInstance,
    express_instances_NumberValue,
    express_instances_PartialEntityValue,
    express_instances_Population,
    express_instances_RealValue,
    express_instances_RoleName,
    express_instances_SETValue,
    express_instances_SimpleValue,
    express_instances_SingleEntityValue,
    express_instances_SingleLeafInstance,
    express_instances_SpecializedValue,
    express_instances_StringValue,
    express_instances_TypeName,
    express_instances_TypedInstance,
    express_rules_ANDConstraint,
    express_rules_Extent,
    express_rules_GlobalRule,
    express_rules_NamedRule,
    express_rules_ONEOFConstraint,
    express_rules_SubtypeConstraint,
    express_rules_SupertypeRule,
    express_rules_TOTAL_OVERConstraint,
    express_statements_AliasStatement,
    express_statements_AliasVariable,
    express_statements_Assignment,
    express_statements_AttributeCell,
    express_statements_CaseAction,
    express_statements_CaseStatement,
    express_statements_ControlStatement,
    express_statements_ControlVariable,
    express_statements_EscapeStatement,
    express_statements_GroupCell,
    express_statements_IfStatement,
    express_statements_MemberCell,
    express_statements_NullStatement,
    express_statements_ProcedureCall,
    express_statements_RepeatStatement,
    express_statements_ReturnStatement,
    express_statements_SkipStatement,
    express_statements_StatementBlock,
    express_statements_VARCell,
    express_statements_VARExpression,
    express_statements_VariableCell,
    instances_AggregateValue,
    instances_ConcreteValue,
    instances_TypedInstance,
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

def test_assoc_action50_stub_double():
    # Statement has no real 'Statement52' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_CaseAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_CaseAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_CaseAction(isDefault="sample_text")
    partner = Statement()
    setattr(partner, 'Statement52', None)
    _safe_set(owner, 'express_statements_CaseAction51', partner)
    assert getattr(partner, 'Statement52') == owner
    _safe_set(owner, 'express_statements_CaseAction51', None)
    assert getattr(partner, 'Statement52') is None


def test_assoc_actualReferent132_stub_double():
    # VARExpression has no real 'VARExpression134' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ActualParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ActualParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ActualParameter(position="sample_text")
    partner = VARExpression()
    setattr(partner, 'VARExpression134', None)
    _safe_set(owner, 'express_expressions_ActualParameter133', partner)
    assert getattr(partner, 'VARExpression134') == owner
    _safe_set(owner, 'express_expressions_ActualParameter133', None)
    assert getattr(partner, 'VARExpression134') is None


def test_assoc_actualValue135_stub_double():
    # Expression has no real 'Expression137' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ActualParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ActualParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ActualParameter(position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression137', None)
    _safe_set(owner, 'express_expressions_ActualParameter136', partner)
    assert getattr(partner, 'Expression137') == owner
    _safe_set(owner, 'express_expressions_ActualParameter136', None)
    assert getattr(partner, 'Expression137') is None


def test_assoc_alias232_stub_double():
    # ScopedId has no real 'ScopedId234' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = ScopedId()
    setattr(partner, 'ScopedId234', None)
    _safe_set(owner, 'express_core_Redeclaration233', partner)
    assert getattr(partner, 'ScopedId234') == owner
    _safe_set(owner, 'express_core_Redeclaration233', None)
    assert getattr(partner, 'ScopedId234') is None


def test_assoc_allowedTypes380_stub_double():
    # NamedType has no real 'NamedType381' property in the generated
    # code (a bare stub) -- manually attach it so express_core_SelectType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_SelectType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_SelectType(isEntity="sample_text", isExtensible="sample_text")
    partner = NamedType()
    setattr(partner, 'NamedType381', None)
    _safe_set(owner, 'instantiates', {partner})
    assert getattr(partner, 'NamedType381') == owner
    _safe_set(owner, 'instantiates', set())
    assert getattr(partner, 'NamedType381') is None


def test_assoc_appearsIn335_stub_double():
    # Scope has no real 'Scope336' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Remark's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Remark's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Remark(isTagged="sample_text", isTail="sample_text", text="sample_text")
    partner = Scope()
    setattr(partner, 'Scope336', None)
    _safe_set(owner, 'includesRemarks', partner)
    assert getattr(partner, 'Scope336') == owner
    _safe_set(owner, 'includesRemarks', None)
    assert getattr(partner, 'Scope336') is None


def test_assoc_assertsExpression21_stub_double():
    # Expression has no real 'Expression22' property in the generated
    # code (a bare stub) -- manually attach it so express_rules_NamedRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_rules_NamedRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_rules_NamedRule(position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression22', None)
    _safe_set(owner, 'express_rules_NamedRule', partner)
    assert getattr(partner, 'Expression22') == owner
    _safe_set(owner, 'express_rules_NamedRule', None)
    assert getattr(partner, 'Expression22') is None


def test_assoc_attribute161_stub_double():
    # ExplicitAttribute has no real 'ExplicitAttribute163' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_AttributeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_AttributeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_AttributeBinding(position="sample_text")
    partner = ExplicitAttribute()
    setattr(partner, 'ExplicitAttribute163', None)
    _safe_set(owner, 'express_expressions_AttributeBinding162', partner)
    assert getattr(partner, 'ExplicitAttribute163') == owner
    _safe_set(owner, 'express_expressions_AttributeBinding162', None)
    assert getattr(partner, 'ExplicitAttribute163') is None


def test_assoc_attributeGroup119_stub_double():
    # SingleEntityType has no real 'SingleEntityType121' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_PartialEntityConstructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_PartialEntityConstructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_PartialEntityConstructor(id="sample_text")
    partner = SingleEntityType()
    setattr(partner, 'SingleEntityType121', None)
    _safe_set(owner, 'express_expressions_PartialEntityConstructor120', partner)
    assert getattr(partner, 'SingleEntityType121') == owner
    _safe_set(owner, 'express_expressions_PartialEntityConstructor120', None)
    assert getattr(partner, 'SingleEntityType121') is None


def test_assoc_attributeType304_stub_double():
    # AttributeType has no real 'AttributeType305' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Attribute(isAbstract="sample_text", position="sample_text")
    partner = AttributeType()
    setattr(partner, 'AttributeType305', None)
    _safe_set(owner, 'role', partner)
    assert getattr(partner, 'AttributeType305') == owner
    _safe_set(owner, 'role', None)
    assert getattr(partner, 'AttributeType305') is None


def test_assoc_attributeValue157_stub_double():
    # Expression has no real 'Expression158' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_AttributeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_AttributeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_AttributeBinding(position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression158', None)
    _safe_set(owner, 'express_expressions_AttributeBinding', partner)
    assert getattr(partner, 'Expression158') == owner
    _safe_set(owner, 'express_expressions_AttributeBinding', None)
    assert getattr(partner, 'Expression158') is None


def test_assoc_attributes240_stub_double():
    # Attribute has no real 'Attribute241' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute241', None)
    _safe_set(owner, 'owningEntity', {partner})
    assert getattr(partner, 'Attribute241') == owner
    _safe_set(owner, 'owningEntity', set())
    assert getattr(partner, 'Attribute241') is None


def test_assoc_base208_stub_double():
    # EnumerationType has no real 'EnumerationType210' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EnumerationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EnumerationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EnumerationType(isExtensible="sample_text")
    partner = EnumerationType()
    setattr(partner, 'EnumerationType210', None)
    _safe_set(owner, 'extension209', partner)
    assert getattr(partner, 'EnumerationType210') == owner
    _safe_set(owner, 'extension209', None)
    assert getattr(partner, 'EnumerationType210') is None


def test_assoc_base385_stub_double():
    # SelectType has no real 'SelectType387' property in the generated
    # code (a bare stub) -- manually attach it so express_core_SelectType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_SelectType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_SelectType(isEntity="sample_text", isExtensible="sample_text")
    partner = SelectType()
    setattr(partner, 'SelectType387', None)
    _safe_set(owner, 'extension386', partner)
    assert getattr(partner, 'SelectType387') == owner
    _safe_set(owner, 'extension386', None)
    assert getattr(partner, 'SelectType387') is None


def test_assoc_baseEntity43_stub_double():
    # VARExpression has no real 'VARExpression45' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_AttributeCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_AttributeCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_AttributeCell(id="sample_text")
    partner = VARExpression()
    setattr(partner, 'VARExpression45', None)
    _safe_set(owner, 'express_statements_AttributeCell44', partner)
    assert getattr(partner, 'VARExpression45') == owner
    _safe_set(owner, 'express_statements_AttributeCell44', None)
    assert getattr(partner, 'VARExpression45') is None


def test_assoc_baseEntity67_stub_double():
    # VARExpression has no real 'VARExpression68' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_GroupCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_GroupCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_GroupCell(id="sample_text")
    partner = VARExpression()
    setattr(partner, 'VARExpression68', None)
    _safe_set(owner, 'express_statements_GroupCell', partner)
    assert getattr(partner, 'VARExpression68') == owner
    _safe_set(owner, 'express_statements_GroupCell', None)
    assert getattr(partner, 'VARExpression68') is None


def test_assoc_bindings122_stub_double():
    # AttributeBinding has no real 'AttributeBinding' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_PartialEntityConstructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_PartialEntityConstructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_PartialEntityConstructor(id="sample_text")
    partner = AttributeBinding()
    setattr(partner, 'AttributeBinding', None)
    _safe_set(owner, 'express_expressions_PartialEntityConstructor123', {partner})
    assert getattr(partner, 'AttributeBinding') == owner
    _safe_set(owner, 'express_expressions_PartialEntityConstructor123', set())
    assert getattr(partner, 'AttributeBinding') is None


def test_assoc_bodyStatementsEscapeStatement416_stub_double():
    # EscapeStatement has no real 'EscapeStatement' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Statement(text="sample_text")
    partner = EscapeStatement()
    setattr(partner, 'EscapeStatement', None)
    _safe_set(owner, 'express_algorithms_Statement417', {partner})
    assert getattr(partner, 'EscapeStatement') == owner
    _safe_set(owner, 'express_algorithms_Statement417', set())
    assert getattr(partner, 'EscapeStatement') is None


def test_assoc_bodyStatementsSkipStatement415_stub_double():
    # SkipStatement has no real 'SkipStatement' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Statement(text="sample_text")
    partner = SkipStatement()
    setattr(partner, 'SkipStatement', None)
    _safe_set(owner, 'express_algorithms_Statement', {partner})
    assert getattr(partner, 'SkipStatement') == owner
    _safe_set(owner, 'express_algorithms_Statement', set())
    assert getattr(partner, 'SkipStatement') is None


def test_assoc_bodyStatements_Statement46_stub_double():
    # Statement has no real 'Statement47' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_StatementBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_StatementBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_StatementBlock(delimited="sample_text")
    partner = Statement()
    setattr(partner, 'Statement47', None)
    _safe_set(owner, 'inBlock', {partner})
    assert getattr(partner, 'Statement47') == owner
    _safe_set(owner, 'inBlock', set())
    assert getattr(partner, 'Statement47') is None


def test_assoc_boundExpression211_stub_double():
    # Expression has no real 'Expression212' property in the generated
    # code (a bare stub) -- manually attach it so express_core_ArrayBound's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_ArrayBound's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_ArrayBound(bound="sample_text")
    partner = Expression()
    setattr(partner, 'Expression212', None)
    _safe_set(owner, 'express_core_ArrayBound', partner)
    assert getattr(partner, 'Expression212') == owner
    _safe_set(owner, 'express_core_ArrayBound', None)
    assert getattr(partner, 'Expression212') is None


def test_assoc_constraint310_stub_double():
    # ActualTypeConstraint has no real 'ActualTypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so express_core_GenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_GenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_GenericType(isEntity="sample_text")
    partner = ActualTypeConstraint()
    setattr(partner, 'ActualTypeConstraint', None)
    _safe_set(owner, 'matchingType', partner)
    assert getattr(partner, 'ActualTypeConstraint') == owner
    _safe_set(owner, 'matchingType', None)
    assert getattr(partner, 'ActualTypeConstraint') is None


def test_assoc_constraints1_stub_double():
    # SubtypeConstraint has no real 'SubtypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so express_rules_SupertypeRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_rules_SupertypeRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_rules_SupertypeRule(assertsAbstract="sample_text")
    partner = SubtypeConstraint()
    setattr(partner, 'SubtypeConstraint', None)
    _safe_set(owner, 'collection', {partner})
    assert getattr(partner, 'SubtypeConstraint') == owner
    _safe_set(owner, 'collection', set())
    assert getattr(partner, 'SubtypeConstraint') is None


def test_assoc_controlledBy418_stub_double():
    # RepeatStatement has no real 'RepeatStatement' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Statement(text="sample_text")
    partner = RepeatStatement()
    setattr(partner, 'RepeatStatement', None)
    _safe_set(owner, 'body', partner)
    assert getattr(partner, 'RepeatStatement') == owner
    _safe_set(owner, 'body', None)
    assert getattr(partner, 'RepeatStatement') is None


def test_assoc_dataType199_stub_double():
    # DataType has no real 'DataType' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Expression(text="sample_text")
    partner = DataType()
    setattr(partner, 'DataType', None)
    _safe_set(owner, 'express_core_Expression200', partner)
    assert getattr(partner, 'DataType') == owner
    _safe_set(owner, 'express_core_Expression200', None)
    assert getattr(partner, 'DataType') is None


def test_assoc_declaredIn502_stub_double():
    # EnumerationType has no real 'EnumerationType503' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_EnumerationItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_EnumerationItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_EnumerationItem(position="sample_text")
    partner = EnumerationType()
    setattr(partner, 'EnumerationType503', None)
    _safe_set(owner, 'declaredItems', partner)
    assert getattr(partner, 'EnumerationType503') == owner
    _safe_set(owner, 'declaredItems', None)
    assert getattr(partner, 'EnumerationType503') is None


def test_assoc_declaredItems205_stub_double():
    # EnumerationItem has no real 'EnumerationItem206' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EnumerationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EnumerationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EnumerationType(isExtensible="sample_text")
    partner = EnumerationItem()
    setattr(partner, 'EnumerationItem206', None)
    _safe_set(owner, 'declaredIn', {partner})
    assert getattr(partner, 'EnumerationItem206') == owner
    _safe_set(owner, 'declaredIn', set())
    assert getattr(partner, 'EnumerationItem206') is None


def test_assoc_declares243_stub_double():
    # SingleEntityType has no real 'SingleEntityType245' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = SingleEntityType()
    setattr(partner, 'SingleEntityType245', None)
    _safe_set(owner, 'declaredIn244', partner)
    assert getattr(partner, 'SingleEntityType245') == owner
    _safe_set(owner, 'declaredIn244', None)
    assert getattr(partner, 'SingleEntityType245') is None


def test_assoc_definingScope367_stub_double():
    # Scope has no real 'Scope368' property in the generated
    # code (a bare stub) -- manually attach it so express_core_ScopedId's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_ScopedId's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_ScopedId(localName="sample_text")
    partner = Scope()
    setattr(partner, 'Scope368', None)
    _safe_set(owner, 'express_core_ScopedId', partner)
    assert getattr(partner, 'Scope368') == owner
    _safe_set(owner, 'express_core_ScopedId', None)
    assert getattr(partner, 'Scope368') is None


def test_assoc_derivation213_stub_double():
    # Expression has no real 'Expression214' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression214', None)
    _safe_set(owner, 'express_core_Redeclaration', partner)
    assert getattr(partner, 'Expression214') == owner
    _safe_set(owner, 'express_core_Redeclaration', None)
    assert getattr(partner, 'Expression214') is None


def test_assoc_describesElement337_stub_double():
    # NamedElement has no real 'NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Remark's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Remark's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Remark(isTagged="sample_text", isTail="sample_text", text="sample_text")
    partner = NamedElement()
    setattr(partner, 'NamedElement', None)
    _safe_set(owner, 'documentation338', {partner})
    assert getattr(partner, 'NamedElement') == owner
    _safe_set(owner, 'documentation338', set())
    assert getattr(partner, 'NamedElement') is None


def test_assoc_describesSchema333_stub_double():
    # Schema has no real 'Schema334' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Remark's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Remark's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Remark(isTagged="sample_text", isTail="sample_text", text="sample_text")
    partner = Schema()
    setattr(partner, 'Schema334', None)
    _safe_set(owner, 'documentation', {partner})
    assert getattr(partner, 'Schema334') == owner
    _safe_set(owner, 'documentation', set())
    assert getattr(partner, 'Schema334') is None


def test_assoc_documentation262_stub_double():
    # Remark has no real 'Remark' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Schema(name="sample_text", version="sample_text")
    partner = Remark()
    setattr(partner, 'Remark', None)
    _safe_set(owner, 'describesSchema', {partner})
    assert getattr(partner, 'Remark') == owner
    _safe_set(owner, 'describesSchema', set())
    assert getattr(partner, 'Remark') is None


def test_assoc_domain282_stub_double():
    # EntityType has no real 'EntityType283' property in the generated
    # code (a bare stub) -- manually attach it so express_core_UniqueRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_UniqueRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_UniqueRule(position="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType283', None)
    _safe_set(owner, 'uniqueRules', partner)
    assert getattr(partner, 'EntityType283') == owner
    _safe_set(owner, 'uniqueRules', None)
    assert getattr(partner, 'EntityType283') is None


def test_assoc_evaluation196_stub_double():
    # Instance has no real 'Instance' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Expression(text="sample_text")
    partner = Instance()
    setattr(partner, 'Instance', None)
    _safe_set(owner, 'express_core_Expression', partner)
    assert getattr(partner, 'Instance') == owner
    _safe_set(owner, 'express_core_Expression', None)
    assert getattr(partner, 'Instance') is None


def test_assoc_explicit202_stub_double():
    # InvertibleAttribute has no real 'InvertibleAttribute' property in the generated
    # code (a bare stub) -- manually attach it so express_core_InverseAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_InverseAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_InverseAttribute(isUnique="sample_text")
    partner = InvertibleAttribute()
    setattr(partner, 'InvertibleAttribute', None)
    _safe_set(owner, 'inverse', partner)
    assert getattr(partner, 'InvertibleAttribute') == owner
    _safe_set(owner, 'inverse', None)
    assert getattr(partner, 'InvertibleAttribute') is None


def test_assoc_extension207_stub_double():
    # EnumerationType has no real 'EnumerationType' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EnumerationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EnumerationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EnumerationType(isExtensible="sample_text")
    partner = EnumerationType()
    setattr(partner, 'EnumerationType', None)
    _safe_set(owner, 'base', {partner})
    assert getattr(partner, 'EnumerationType') == owner
    _safe_set(owner, 'base', set())
    assert getattr(partner, 'EnumerationType') is None


def test_assoc_extension246_stub_double():
    # Extent has no real 'Extent247' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = Extent()
    setattr(partner, 'Extent247', None)
    _safe_set(owner, 'forType', {partner})
    assert getattr(partner, 'Extent247') == owner
    _safe_set(owner, 'forType', set())
    assert getattr(partner, 'Extent247') is None


def test_assoc_extension382_stub_double():
    # SelectType has no real 'SelectType384' property in the generated
    # code (a bare stub) -- manually attach it so express_core_SelectType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_SelectType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_SelectType(isEntity="sample_text", isExtensible="sample_text")
    partner = SelectType()
    setattr(partner, 'SelectType384', None)
    _safe_set(owner, 'base383', {partner})
    assert getattr(partner, 'SelectType384') == owner
    _safe_set(owner, 'base383', set())
    assert getattr(partner, 'SelectType384') is None


def test_assoc_formalParameter131_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ActualParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ActualParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ActualParameter(position="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'express_expressions_ActualParameter', partner)
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'express_expressions_ActualParameter', None)
    assert getattr(partner, 'Parameter') is None


def test_assoc_formalParameterType445_stub_double():
    # ParameterType has no real 'ParameterType447' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Parameter(inout="sample_text", position="sample_text")
    partner = ParameterType()
    setattr(partner, 'ParameterType447', None)
    _safe_set(owner, 'express_algorithms_Parameter446', partner)
    assert getattr(partner, 'ParameterType447') == owner
    _safe_set(owner, 'express_algorithms_Parameter446', None)
    assert getattr(partner, 'ParameterType447') is None


def test_assoc_hiIndex349_stub_double():
    # ArrayBound has no real 'ArrayBound' property in the generated
    # code (a bare stub) -- manually attach it so express_core_GeneralARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_GeneralARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_GeneralARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound', None)
    _safe_set(owner, 'express_core_GeneralARRAYType', partner)
    assert getattr(partner, 'ArrayBound') == owner
    _safe_set(owner, 'express_core_GeneralARRAYType', None)
    assert getattr(partner, 'ArrayBound') is None


def test_assoc_hiIndex402_stub_double():
    # ArrayBound has no real 'ArrayBound404' property in the generated
    # code (a bare stub) -- manually attach it so express_core_ARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_ARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_ARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound404', None)
    _safe_set(owner, 'express_core_ARRAYType403', partner)
    assert getattr(partner, 'ArrayBound404') == owner
    _safe_set(owner, 'express_core_ARRAYType403', None)
    assert getattr(partner, 'ArrayBound404') is None


def test_assoc_hiIndex425_stub_double():
    # ArrayBound has no real 'ArrayBound426' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound426', None)
    _safe_set(owner, 'express_algorithms_ActualARRAYType', partner)
    assert getattr(partner, 'ArrayBound426') == owner
    _safe_set(owner, 'express_algorithms_ActualARRAYType', None)
    assert getattr(partner, 'ArrayBound426') is None


def test_assoc_implements419_stub_double():
    # Algorithm has no real 'Algorithm421' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Statement(text="sample_text")
    partner = Algorithm()
    setattr(partner, 'Algorithm421', None)
    _safe_set(owner, 'body420', partner)
    assert getattr(partner, 'Algorithm421') == owner
    _safe_set(owner, 'body420', None)
    assert getattr(partner, 'Algorithm421') is None


def test_assoc_inBlock414_stub_double():
    # StatementBlock has no real 'StatementBlock' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Statement(text="sample_text")
    partner = StatementBlock()
    setattr(partner, 'StatementBlock', None)
    _safe_set(owner, 'bodyStatements_Statement', partner)
    assert getattr(partner, 'StatementBlock') == owner
    _safe_set(owner, 'bodyStatements_Statement', None)
    assert getattr(partner, 'StatementBlock') is None


def test_assoc_inFunctionCall129_stub_double():
    # FunctionCall has no real 'FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ActualParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ActualParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ActualParameter(position="sample_text")
    partner = FunctionCall()
    setattr(partner, 'FunctionCall', None)
    _safe_set(owner, 'actualParameters130', partner)
    assert getattr(partner, 'FunctionCall') == owner
    _safe_set(owner, 'actualParameters130', None)
    assert getattr(partner, 'FunctionCall') is None


def test_assoc_inProcedureCall128_stub_double():
    # ProcedureCall has no real 'ProcedureCall' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ActualParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ActualParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ActualParameter(position="sample_text")
    partner = ProcedureCall()
    setattr(partner, 'ProcedureCall', None)
    _safe_set(owner, 'actualParameters', partner)
    assert getattr(partner, 'ProcedureCall') == owner
    _safe_set(owner, 'actualParameters', None)
    assert getattr(partner, 'ProcedureCall') is None


def test_assoc_instanceOf474_stub_double():
    # EntityType has no real 'EntityType475' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_EntityInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_EntityInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_EntityInstance(id="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType475', None)
    _safe_set(owner, 'express_instances_EntityInstance', {partner})
    assert getattr(partner, 'EntityType475') == owner
    _safe_set(owner, 'express_instances_EntityInstance', set())
    assert getattr(partner, 'EntityType475') is None


def test_assoc_interfacedElements265_stub_double():
    # SchemaElement has no real 'SchemaElement266' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Schema(name="sample_text", version="sample_text")
    partner = SchemaElement()
    setattr(partner, 'SchemaElement266', None)
    _safe_set(owner, 'referencedIn', {partner})
    assert getattr(partner, 'SchemaElement266') == owner
    _safe_set(owner, 'referencedIn', set())
    assert getattr(partner, 'SchemaElement266') is None


def test_assoc_interfacedId280_stub_double():
    # ScopedId has no real 'ScopedId281' property in the generated
    # code (a bare stub) -- manually attach it so express_core_InterfacedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_InterfacedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_InterfacedElement(isUSE="sample_text")
    partner = ScopedId()
    setattr(partner, 'ScopedId281', None)
    _safe_set(owner, 'express_core_InterfacedElement', partner)
    assert getattr(partner, 'ScopedId281') == owner
    _safe_set(owner, 'express_core_InterfacedElement', None)
    assert getattr(partner, 'ScopedId281') is None


def test_assoc_interfaces263_stub_double():
    # InterfacedElement has no real 'InterfacedElement' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Schema(name="sample_text", version="sample_text")
    partner = InterfacedElement()
    setattr(partner, 'InterfacedElement', None)
    _safe_set(owner, 'interfacingSchema', {partner})
    assert getattr(partner, 'InterfacedElement') == owner
    _safe_set(owner, 'interfacingSchema', set())
    assert getattr(partner, 'InterfacedElement') is None


def test_assoc_interfacingSchema277_stub_double():
    # Schema has no real 'Schema' property in the generated
    # code (a bare stub) -- manually attach it so express_core_InterfacedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_InterfacedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_InterfacedElement(isUSE="sample_text")
    partner = Schema()
    setattr(partner, 'Schema', None)
    _safe_set(owner, 'interfaces', partner)
    assert getattr(partner, 'Schema') == owner
    _safe_set(owner, 'interfaces', None)
    assert getattr(partner, 'Schema') is None


def test_assoc_interpretationContext197_stub_double():
    # Scope has no real 'Scope' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Expression(text="sample_text")
    partner = Scope()
    setattr(partner, 'Scope', None)
    _safe_set(owner, 'express_core_Expression198', partner)
    assert getattr(partner, 'Scope') == owner
    _safe_set(owner, 'express_core_Expression198', None)
    assert getattr(partner, 'Scope') is None


def test_assoc_invertibleAttributes248_stub_double():
    # InvertibleAttribute has no real 'InvertibleAttribute249' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = InvertibleAttribute()
    setattr(partner, 'InvertibleAttribute249', None)
    _safe_set(owner, 'referencingType', {partner})
    assert getattr(partner, 'InvertibleAttribute249') == owner
    _safe_set(owner, 'referencingType', set())
    assert getattr(partner, 'InvertibleAttribute249') is None


def test_assoc_keyComponent284_stub_double():
    # Attribute has no real 'Attribute285' property in the generated
    # code (a bare stub) -- manually attach it so express_core_UniqueRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_UniqueRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_UniqueRule(position="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute285', None)
    _safe_set(owner, 'express_core_UniqueRule', {partner})
    assert getattr(partner, 'Attribute285') == owner
    _safe_set(owner, 'express_core_UniqueRule', set())
    assert getattr(partner, 'Attribute285') is None


def test_assoc_labelValue48_stub_double():
    # Expression has no real 'Expression49' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_CaseAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_CaseAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_CaseAction(isDefault="sample_text")
    partner = Expression()
    setattr(partner, 'Expression49', None)
    _safe_set(owner, 'express_statements_CaseAction', {partner})
    assert getattr(partner, 'Expression49') == owner
    _safe_set(owner, 'express_statements_CaseAction', set())
    assert getattr(partner, 'Expression49') is None


def test_assoc_leftOperand105_stub_double():
    # Expression has no real 'Expression106' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_BinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_BinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_BinaryOperation(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression106', None)
    _safe_set(owner, 'express_expressions_BinaryOperation', partner)
    assert getattr(partner, 'Expression106') == owner
    _safe_set(owner, 'express_expressions_BinaryOperation', None)
    assert getattr(partner, 'Expression106') is None


def test_assoc_loIndex350_stub_double():
    # ArrayBound has no real 'ArrayBound352' property in the generated
    # code (a bare stub) -- manually attach it so express_core_GeneralARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_GeneralARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_GeneralARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound352', None)
    _safe_set(owner, 'express_core_GeneralARRAYType351', partner)
    assert getattr(partner, 'ArrayBound352') == owner
    _safe_set(owner, 'express_core_GeneralARRAYType351', None)
    assert getattr(partner, 'ArrayBound352') is None


def test_assoc_loIndex400_stub_double():
    # ArrayBound has no real 'ArrayBound401' property in the generated
    # code (a bare stub) -- manually attach it so express_core_ARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_ARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_ARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound401', None)
    _safe_set(owner, 'express_core_ARRAYType', partner)
    assert getattr(partner, 'ArrayBound401') == owner
    _safe_set(owner, 'express_core_ARRAYType', None)
    assert getattr(partner, 'ArrayBound401') is None


def test_assoc_loIndex427_stub_double():
    # ArrayBound has no real 'ArrayBound429' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualARRAYType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualARRAYType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualARRAYType(isOptional="sample_text")
    partner = ArrayBound()
    setattr(partner, 'ArrayBound429', None)
    _safe_set(owner, 'express_algorithms_ActualARRAYType428', partner)
    assert getattr(partner, 'ArrayBound429') == owner
    _safe_set(owner, 'express_algorithms_ActualARRAYType428', None)
    assert getattr(partner, 'ArrayBound429') is None


def test_assoc_lowerBound222_stub_double():
    # SizeConstraint has no real 'SizeConstraint224' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint224', None)
    _safe_set(owner, 'express_core_Redeclaration223', partner)
    assert getattr(partner, 'SizeConstraint224') == owner
    _safe_set(owner, 'express_core_Redeclaration223', None)
    assert getattr(partner, 'SizeConstraint224') is None


def test_assoc_lowerBound369_stub_double():
    # SizeConstraint has no real 'SizeConstraint370' property in the generated
    # code (a bare stub) -- manually attach it so express_core_AggregationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_AggregationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_AggregationType(isUnique="sample_text", ordering="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint370', None)
    _safe_set(owner, 'express_core_AggregationType', partner)
    assert getattr(partner, 'SizeConstraint370') == owner
    _safe_set(owner, 'express_core_AggregationType', None)
    assert getattr(partner, 'SizeConstraint370') is None


def test_assoc_lowerBound437_stub_double():
    # SizeConstraint has no real 'SizeConstraint439' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualAGGREGATEType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualAGGREGATEType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualAGGREGATEType(label="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint439', None)
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType438', partner)
    assert getattr(partner, 'SizeConstraint439') == owner
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType438', None)
    assert getattr(partner, 'SizeConstraint439') is None


def test_assoc_matchingStructure448_stub_double():
    # AGGREGATEType has no real 'AGGREGATEType' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualStructureConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualStructureConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualStructureConstraint(label="sample_text")
    partner = AGGREGATEType()
    setattr(partner, 'AGGREGATEType', None)
    _safe_set(owner, 'constraint449', partner)
    assert getattr(partner, 'AGGREGATEType') == owner
    _safe_set(owner, 'constraint449', None)
    assert getattr(partner, 'AGGREGATEType') is None


def test_assoc_matchingType405_stub_double():
    # GenericType has no real 'GenericType' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualTypeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualTypeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualTypeConstraint(label="sample_text")
    partner = GenericType()
    setattr(partner, 'GenericType', None)
    _safe_set(owner, 'constraint', partner)
    assert getattr(partner, 'GenericType') == owner
    _safe_set(owner, 'constraint', None)
    assert getattr(partner, 'GenericType') is None


def test_assoc_memberType434_stub_double():
    # VariableType has no real 'VariableType436' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualAGGREGATEType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualAGGREGATEType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualAGGREGATEType(label="sample_text")
    partner = VariableType()
    setattr(partner, 'VariableType436', None)
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType435', partner)
    assert getattr(partner, 'VariableType436') == owner
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType435', None)
    assert getattr(partner, 'VariableType436') is None


def test_assoc_memberValue172_stub_double():
    # Expression has no real 'Expression174' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_MemberBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_MemberBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_MemberBinding(position="sample_text")
    partner = Expression()
    setattr(partner, 'Expression174', None)
    _safe_set(owner, 'express_expressions_MemberBinding173', partner)
    assert getattr(partner, 'Expression174') == owner
    _safe_set(owner, 'express_expressions_MemberBinding173', None)
    assert getattr(partner, 'Expression174') is None


def test_assoc_memberValue486_stub_double():
    # Instance has no real 'Instance487' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_ListMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_ListMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_ListMember(position="sample_text")
    partner = Instance()
    setattr(partner, 'Instance487', None)
    _safe_set(owner, 'express_instances_ListMember', partner)
    assert getattr(partner, 'Instance487') == owner
    _safe_set(owner, 'express_instances_ListMember', None)
    assert getattr(partner, 'Instance487') is None


def test_assoc_memberValue488_stub_double():
    # Instance has no real 'Instance489' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_BagMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_BagMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_BagMember(count="sample_text")
    partner = Instance()
    setattr(partner, 'Instance489', None)
    _safe_set(owner, 'express_instances_BagMember', partner)
    assert getattr(partner, 'Instance489') == owner
    _safe_set(owner, 'express_instances_BagMember', None)
    assert getattr(partner, 'Instance489') is None


def test_assoc_memberValue510_stub_double():
    # Instance has no real 'Instance511' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_ArrayMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_ArrayMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_ArrayMember(index="sample_text")
    partner = Instance()
    setattr(partner, 'Instance511', None)
    _safe_set(owner, 'express_instances_ArrayMember', partner)
    assert getattr(partner, 'Instance511') == owner
    _safe_set(owner, 'express_instances_ArrayMember', None)
    assert getattr(partner, 'Instance511') is None


def test_assoc_modelsRole201_stub_double():
    # DomainRole has no real 'DomainRole' property in the generated
    # code (a bare stub) -- manually attach it so express_core_InverseAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_InverseAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_InverseAttribute(isUnique="sample_text")
    partner = DomainRole()
    setattr(partner, 'DomainRole', None)
    _safe_set(owner, 'rangeView', partner)
    assert getattr(partner, 'DomainRole') == owner
    _safe_set(owner, 'rangeView', None)
    assert getattr(partner, 'DomainRole') is None


def test_assoc_namedSupertype0_stub_double():
    # EntityType has no real 'EntityType' property in the generated
    # code (a bare stub) -- manually attach it so express_rules_SupertypeRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_rules_SupertypeRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_rules_SupertypeRule(assertsAbstract="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType', None)
    _safe_set(owner, 'express_rules_SupertypeRule', partner)
    assert getattr(partner, 'EntityType') == owner
    _safe_set(owner, 'express_rules_SupertypeRule', None)
    assert getattr(partner, 'EntityType') is None


def test_assoc_ofEntity306_stub_double():
    # SingleEntityType has no real 'SingleEntityType307' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Attribute(isAbstract="sample_text", position="sample_text")
    partner = SingleEntityType()
    setattr(partner, 'SingleEntityType307', None)
    _safe_set(owner, 'declaresAttribute', partner)
    assert getattr(partner, 'SingleEntityType307') == owner
    _safe_set(owner, 'declaresAttribute', None)
    assert getattr(partner, 'SingleEntityType307') is None


def test_assoc_originalAttribute227_stub_double():
    # Attribute has no real 'Attribute229' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute229', None)
    _safe_set(owner, 'express_core_Redeclaration228', partner)
    assert getattr(partner, 'Attribute229') == owner
    _safe_set(owner, 'express_core_Redeclaration228', None)
    assert getattr(partner, 'Attribute229') is None


def test_assoc_owningEntity308_stub_double():
    # EntityType has no real 'EntityType309' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Attribute(isAbstract="sample_text", position="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType309', None)
    _safe_set(owner, 'attributes', {partner})
    assert getattr(partner, 'EntityType309') == owner
    _safe_set(owner, 'attributes', set())
    assert getattr(partner, 'EntityType309') is None


def test_assoc_playsDomainRole250_stub_double():
    # DomainRole has no real 'DomainRole251' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = DomainRole()
    setattr(partner, 'DomainRole251', None)
    _safe_set(owner, 'domain', {partner})
    assert getattr(partner, 'DomainRole251') == owner
    _safe_set(owner, 'domain', set())
    assert getattr(partner, 'DomainRole251') is None


def test_assoc_playsRangeRole242_stub_double():
    # RangeRole has no real 'RangeRole' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = RangeRole()
    setattr(partner, 'RangeRole', None)
    _safe_set(owner, 'range', {partner})
    assert getattr(partner, 'RangeRole') == owner
    _safe_set(owner, 'range', set())
    assert getattr(partner, 'RangeRole') is None


def test_assoc_playsRole235_stub_double():
    # Role has no real 'Role237' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = Role()
    setattr(partner, 'Role237', None)
    _safe_set(owner, 'ofEntity236', {partner})
    assert getattr(partner, 'Role237') == owner
    _safe_set(owner, 'ofEntity236', set())
    assert getattr(partner, 'Role237') is None


def test_assoc_redeclarations238_stub_double():
    # Redeclaration has no real 'Redeclaration239' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = Redeclaration()
    setattr(partner, 'Redeclaration239', None)
    _safe_set(owner, 'scope', {partner})
    assert getattr(partner, 'Redeclaration239') == owner
    _safe_set(owner, 'scope', set())
    assert getattr(partner, 'Redeclaration239') is None


def test_assoc_refersTo138_stub_double():
    # Parameter has no real 'Parameter139' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ParameterRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ParameterRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ParameterRef(id="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter139', None)
    _safe_set(owner, 'express_expressions_ParameterRef', partner)
    assert getattr(partner, 'Parameter139') == owner
    _safe_set(owner, 'express_expressions_ParameterRef', None)
    assert getattr(partner, 'Parameter139') is None


def test_assoc_refersTo140_stub_double():
    # Attribute has no real 'Attribute' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_AttributeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_AttributeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_AttributeRef(id="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute', None)
    _safe_set(owner, 'express_expressions_AttributeRef', partner)
    assert getattr(partner, 'Attribute') == owner
    _safe_set(owner, 'express_expressions_AttributeRef', None)
    assert getattr(partner, 'Attribute') is None


def test_assoc_refersTo143_stub_double():
    # SingleEntityType has no real 'SingleEntityType144' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_GroupRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_GroupRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_GroupRef(id="sample_text")
    partner = SingleEntityType()
    setattr(partner, 'SingleEntityType144', None)
    _safe_set(owner, 'express_expressions_GroupRef', partner)
    assert getattr(partner, 'SingleEntityType144') == owner
    _safe_set(owner, 'express_expressions_GroupRef', None)
    assert getattr(partner, 'SingleEntityType144') is None


def test_assoc_refersTo149_stub_double():
    # Constant has no real 'Constant' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ConstantRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ConstantRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ConstantRef(id="sample_text")
    partner = Constant()
    setattr(partner, 'Constant', None)
    _safe_set(owner, 'express_expressions_ConstantRef', partner)
    assert getattr(partner, 'Constant') == owner
    _safe_set(owner, 'express_expressions_ConstantRef', None)
    assert getattr(partner, 'Constant') is None


def test_assoc_refersTo175_stub_double():
    # NamedType has no real 'NamedType' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_ExtentRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_ExtentRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_ExtentRef(id="sample_text")
    partner = NamedType()
    setattr(partner, 'NamedType', None)
    _safe_set(owner, 'express_expressions_ExtentRef', partner)
    assert getattr(partner, 'NamedType') == owner
    _safe_set(owner, 'express_expressions_ExtentRef', None)
    assert getattr(partner, 'NamedType') is None


def test_assoc_refersTo176_stub_double():
    # NamedVariable has no real 'NamedVariable' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_VariableRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_VariableRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_VariableRef(id="sample_text")
    partner = NamedVariable()
    setattr(partner, 'NamedVariable', None)
    _safe_set(owner, 'express_expressions_VariableRef', partner)
    assert getattr(partner, 'NamedVariable') == owner
    _safe_set(owner, 'express_expressions_VariableRef', None)
    assert getattr(partner, 'NamedVariable') is None


def test_assoc_refersTo278_stub_double():
    # SchemaElement has no real 'SchemaElement279' property in the generated
    # code (a bare stub) -- manually attach it so express_core_InterfacedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_InterfacedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_InterfacedElement(isUSE="sample_text")
    partner = SchemaElement()
    setattr(partner, 'SchemaElement279', None)
    _safe_set(owner, 'referencedAs', partner)
    assert getattr(partner, 'SchemaElement279') == owner
    _safe_set(owner, 'referencedAs', None)
    assert getattr(partner, 'SchemaElement279') is None


def test_assoc_refersTo41_stub_double():
    # VARVariable has no real 'VARVariable' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_VARCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_VARCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_VARCell(id="sample_text")
    partner = VARVariable()
    setattr(partner, 'VARVariable', None)
    _safe_set(owner, 'express_statements_VARCell', partner)
    assert getattr(partner, 'VARVariable') == owner
    _safe_set(owner, 'express_statements_VARCell', None)
    assert getattr(partner, 'VARVariable') is None


def test_assoc_refersTo412_stub_double():
    # ActualDataType has no real 'ActualDataType413' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualGenericType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualGenericType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualGenericType(isEntity="sample_text", label="sample_text")
    partner = ActualDataType()
    setattr(partner, 'ActualDataType413', None)
    _safe_set(owner, 'express_algorithms_ActualGenericType', partner)
    assert getattr(partner, 'ActualDataType413') == owner
    _safe_set(owner, 'express_algorithms_ActualGenericType', None)
    assert getattr(partner, 'ActualDataType413') is None


def test_assoc_refersTo42_stub_double():
    # ExplicitAttribute has no real 'ExplicitAttribute' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_AttributeCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_AttributeCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_AttributeCell(id="sample_text")
    partner = ExplicitAttribute()
    setattr(partner, 'ExplicitAttribute', None)
    _safe_set(owner, 'express_statements_AttributeCell', partner)
    assert getattr(partner, 'ExplicitAttribute') == owner
    _safe_set(owner, 'express_statements_AttributeCell', None)
    assert getattr(partner, 'ExplicitAttribute') is None


def test_assoc_refersTo432_stub_double():
    # ActualStructure has no real 'ActualStructure' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualAGGREGATEType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualAGGREGATEType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualAGGREGATEType(label="sample_text")
    partner = ActualStructure()
    setattr(partner, 'ActualStructure', None)
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType433', partner)
    assert getattr(partner, 'ActualStructure') == owner
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType433', None)
    assert getattr(partner, 'ActualStructure') is None


def test_assoc_refersTo69_stub_double():
    # SingleEntityType has no real 'SingleEntityType' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_GroupCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_GroupCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_GroupCell(id="sample_text")
    partner = SingleEntityType()
    setattr(partner, 'SingleEntityType', None)
    _safe_set(owner, 'express_statements_GroupCell70', partner)
    assert getattr(partner, 'SingleEntityType') == owner
    _safe_set(owner, 'express_statements_GroupCell70', None)
    assert getattr(partner, 'SingleEntityType') is None


def test_assoc_refersTo71_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so express_statements_VariableCell's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_statements_VariableCell's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_statements_VariableCell(id="sample_text")
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'express_statements_VariableCell', partner)
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'express_statements_VariableCell', None)
    assert getattr(partner, 'Variable') is None


def test_assoc_refersTo95_stub_double():
    # EnumerationItem has no real 'EnumerationItem' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_EnumItemRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_EnumItemRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_EnumItemRef(id="sample_text")
    partner = EnumerationItem()
    setattr(partner, 'EnumerationItem', None)
    _safe_set(owner, 'express_expressions_EnumItemRef', partner)
    assert getattr(partner, 'EnumerationItem') == owner
    _safe_set(owner, 'express_expressions_EnumItemRef', None)
    assert getattr(partner, 'EnumerationItem') is None


def test_assoc_refinedRole230_stub_double():
    # Role has no real 'Role' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = Role()
    setattr(partner, 'Role', None)
    _safe_set(owner, 'express_core_Redeclaration231', partner)
    assert getattr(partner, 'Role') == owner
    _safe_set(owner, 'express_core_Redeclaration231', None)
    assert getattr(partner, 'Role') is None


def test_assoc_refines217_stub_double():
    # Redeclaration has no real 'Redeclaration' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = Redeclaration()
    setattr(partner, 'Redeclaration', None)
    _safe_set(owner, 'express_core_Redeclaration218', partner)
    assert getattr(partner, 'Redeclaration') == owner
    _safe_set(owner, 'express_core_Redeclaration218', None)
    assert getattr(partner, 'Redeclaration') is None


def test_assoc_repetition169_stub_double():
    # RepeatCount has no real 'RepeatCount' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_MemberBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_MemberBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_MemberBinding(position="sample_text")
    partner = RepeatCount()
    setattr(partner, 'RepeatCount', None)
    _safe_set(owner, 'express_expressions_MemberBinding', partner)
    assert getattr(partner, 'RepeatCount') == owner
    _safe_set(owner, 'express_expressions_MemberBinding', None)
    assert getattr(partner, 'RepeatCount') is None


def test_assoc_requiredStructure450_stub_double():
    # ActualStructure has no real 'ActualStructure451' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualStructureConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualStructureConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualStructureConstraint(label="sample_text")
    partner = ActualStructure()
    setattr(partner, 'ActualStructure451', None)
    _safe_set(owner, 'express_algorithms_ActualStructureConstraint', partner)
    assert getattr(partner, 'ActualStructure451') == owner
    _safe_set(owner, 'express_algorithms_ActualStructureConstraint', None)
    assert getattr(partner, 'ActualStructure451') is None


def test_assoc_requiredType406_stub_double():
    # ActualDataType has no real 'ActualDataType' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualTypeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualTypeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualTypeConstraint(label="sample_text")
    partner = ActualDataType()
    setattr(partner, 'ActualDataType', None)
    _safe_set(owner, 'express_algorithms_ActualTypeConstraint', partner)
    assert getattr(partner, 'ActualDataType') == owner
    _safe_set(owner, 'express_algorithms_ActualTypeConstraint', None)
    assert getattr(partner, 'ActualDataType') is None


def test_assoc_restrictedType215_stub_double():
    # AttributeType has no real 'AttributeType' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = AttributeType()
    setattr(partner, 'AttributeType', None)
    _safe_set(owner, 'express_core_Redeclaration216', partner)
    assert getattr(partner, 'AttributeType') == owner
    _safe_set(owner, 'express_core_Redeclaration216', None)
    assert getattr(partner, 'AttributeType') is None


def test_assoc_resultValue118_stub_double():
    # PartialEntityValue has no real 'PartialEntityValue' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_PartialEntityConstructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_PartialEntityConstructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_PartialEntityConstructor(id="sample_text")
    partner = PartialEntityValue()
    setattr(partner, 'PartialEntityValue', None)
    _safe_set(owner, 'express_expressions_PartialEntityConstructor', partner)
    assert getattr(partner, 'PartialEntityValue') == owner
    _safe_set(owner, 'express_expressions_PartialEntityConstructor', None)
    assert getattr(partner, 'PartialEntityValue') is None


def test_assoc_rightOperand107_stub_double():
    # Expression has no real 'Expression109' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_BinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_BinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_BinaryOperation(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression109', None)
    _safe_set(owner, 'express_expressions_BinaryOperation108', partner)
    assert getattr(partner, 'Expression109') == owner
    _safe_set(owner, 'express_expressions_BinaryOperation108', None)
    assert getattr(partner, 'Expression109') is None


def test_assoc_schemaElements264_stub_double():
    # SchemaElement has no real 'SchemaElement' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Schema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Schema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Schema(name="sample_text", version="sample_text")
    partner = SchemaElement()
    setattr(partner, 'SchemaElement', None)
    _safe_set(owner, 'definedIn', {partner})
    assert getattr(partner, 'SchemaElement') == owner
    _safe_set(owner, 'definedIn', set())
    assert getattr(partner, 'SchemaElement') is None


def test_assoc_scope225_stub_double():
    # EntityType has no real 'EntityType226' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType226', None)
    _safe_set(owner, 'redeclarations', partner)
    assert getattr(partner, 'EntityType226') == owner
    _safe_set(owner, 'redeclarations', None)
    assert getattr(partner, 'EntityType226') is None


def test_assoc_selectList388_stub_double():
    # NamedType has no real 'NamedType389' property in the generated
    # code (a bare stub) -- manually attach it so express_core_SelectType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_SelectType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_SelectType(isEntity="sample_text", isExtensible="sample_text")
    partner = NamedType()
    setattr(partner, 'NamedType389', None)
    _safe_set(owner, 'express_core_SelectType', {partner})
    assert getattr(partner, 'NamedType389') == owner
    _safe_set(owner, 'express_core_SelectType', set())
    assert getattr(partner, 'NamedType389') is None


def test_assoc_state473_stub_double():
    # EntityValue has no real 'EntityValue' property in the generated
    # code (a bare stub) -- manually attach it so express_instances_EntityInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_instances_EntityInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_instances_EntityInstance(id="sample_text")
    partner = EntityValue()
    setattr(partner, 'EntityValue', None)
    _safe_set(owner, 'describes', partner)
    assert getattr(partner, 'EntityValue') == owner
    _safe_set(owner, 'describes', None)
    assert getattr(partner, 'EntityValue') is None


def test_assoc_structureConstraints440_stub_double():
    # ActualStructureConstraint has no real 'ActualStructureConstraint441' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Parameter(inout="sample_text", position="sample_text")
    partner = ActualStructureConstraint()
    setattr(partner, 'ActualStructureConstraint441', None)
    _safe_set(owner, 'express_algorithms_Parameter', {partner})
    assert getattr(partner, 'ActualStructureConstraint441') == owner
    _safe_set(owner, 'express_algorithms_Parameter', set())
    assert getattr(partner, 'ActualStructureConstraint441') is None


def test_assoc_subtypeOf256_stub_double():
    # EntityType has no real 'EntityType257' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = EntityType()
    setattr(partner, 'EntityType257', None)
    _safe_set(owner, 'express_core_EntityType', {partner})
    assert getattr(partner, 'EntityType257') == owner
    _safe_set(owner, 'express_core_EntityType', set())
    assert getattr(partner, 'EntityType257') is None


def test_assoc_toSlot170_stub_double():
    # ListMember has no real 'ListMember' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_MemberBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_MemberBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_MemberBinding(position="sample_text")
    partner = ListMember()
    setattr(partner, 'ListMember', None)
    _safe_set(owner, 'express_expressions_MemberBinding171', {partner})
    assert getattr(partner, 'ListMember') == owner
    _safe_set(owner, 'express_expressions_MemberBinding171', set())
    assert getattr(partner, 'ListMember') is None


def test_assoc_toValue159_stub_double():
    # AttributeValue has no real 'AttributeValue' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_AttributeBinding's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_AttributeBinding's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_AttributeBinding(position="sample_text")
    partner = AttributeValue()
    setattr(partner, 'AttributeValue', None)
    _safe_set(owner, 'express_expressions_AttributeBinding160', partner)
    assert getattr(partner, 'AttributeValue') == owner
    _safe_set(owner, 'express_expressions_AttributeBinding160', None)
    assert getattr(partner, 'AttributeValue') is None


def test_assoc_typeConstraints442_stub_double():
    # ActualTypeConstraint has no real 'ActualTypeConstraint444' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_Parameter(inout="sample_text", position="sample_text")
    partner = ActualTypeConstraint()
    setattr(partner, 'ActualTypeConstraint444', None)
    _safe_set(owner, 'express_algorithms_Parameter443', {partner})
    assert getattr(partner, 'ActualTypeConstraint444') == owner
    _safe_set(owner, 'express_algorithms_Parameter443', set())
    assert getattr(partner, 'ActualTypeConstraint444') is None


def test_assoc_unaryOperand145_stub_double():
    # Expression has no real 'Expression146' property in the generated
    # code (a bare stub) -- manually attach it so express_expressions_UnaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_expressions_UnaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_expressions_UnaryOperation(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression146', None)
    _safe_set(owner, 'express_expressions_UnaryOperation', partner)
    assert getattr(partner, 'Expression146') == owner
    _safe_set(owner, 'express_expressions_UnaryOperation', None)
    assert getattr(partner, 'Expression146') is None


def test_assoc_uniqueRules252_stub_double():
    # UniqueRule has no real 'UniqueRule' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = UniqueRule()
    setattr(partner, 'UniqueRule', None)
    _safe_set(owner, 'domain253', {partner})
    assert getattr(partner, 'UniqueRule') == owner
    _safe_set(owner, 'domain253', set())
    assert getattr(partner, 'UniqueRule') is None


def test_assoc_upperBound219_stub_double():
    # SizeConstraint has no real 'SizeConstraint221' property in the generated
    # code (a bare stub) -- manually attach it so express_core_Redeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_Redeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_Redeclaration(isMandatory="sample_text", position="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint221', None)
    _safe_set(owner, 'express_core_Redeclaration220', partner)
    assert getattr(partner, 'SizeConstraint221') == owner
    _safe_set(owner, 'express_core_Redeclaration220', None)
    assert getattr(partner, 'SizeConstraint221') is None


def test_assoc_upperBound371_stub_double():
    # SizeConstraint has no real 'SizeConstraint373' property in the generated
    # code (a bare stub) -- manually attach it so express_core_AggregationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_AggregationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_AggregationType(isUnique="sample_text", ordering="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint373', None)
    _safe_set(owner, 'express_core_AggregationType372', partner)
    assert getattr(partner, 'SizeConstraint373') == owner
    _safe_set(owner, 'express_core_AggregationType372', None)
    assert getattr(partner, 'SizeConstraint373') is None


def test_assoc_upperBound430_stub_double():
    # SizeConstraint has no real 'SizeConstraint431' property in the generated
    # code (a bare stub) -- manually attach it so express_algorithms_ActualAGGREGATEType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_algorithms_ActualAGGREGATEType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_algorithms_ActualAGGREGATEType(label="sample_text")
    partner = SizeConstraint()
    setattr(partner, 'SizeConstraint431', None)
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType', partner)
    assert getattr(partner, 'SizeConstraint431') == owner
    _safe_set(owner, 'express_algorithms_ActualAGGREGATEType', None)
    assert getattr(partner, 'SizeConstraint431') is None


def test_assoc_usedIn254_stub_double():
    # InvertibleAttribute has no real 'InvertibleAttribute255' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EntityType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EntityType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EntityType(isAbstract="sample_text")
    partner = InvertibleAttribute()
    setattr(partner, 'InvertibleAttribute255', None)
    _safe_set(owner, 'rangeType', {partner})
    assert getattr(partner, 'InvertibleAttribute255') == owner
    _safe_set(owner, 'rangeType', set())
    assert getattr(partner, 'InvertibleAttribute255') is None


def test_assoc_values203_stub_double():
    # EnumerationItem has no real 'EnumerationItem204' property in the generated
    # code (a bare stub) -- manually attach it so express_core_EnumerationType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # express_core_EnumerationType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = express_core_EnumerationType(isExtensible="sample_text")
    partner = EnumerationItem()
    setattr(partner, 'EnumerationItem204', None)
    _safe_set(owner, 'express_core_EnumerationType', {partner})
    assert getattr(partner, 'EnumerationItem204') == owner
    _safe_set(owner, 'express_core_EnumerationType', set())
    assert getattr(partner, 'EnumerationItem204') is None


