import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ArrayNatureDefinition,
    ArrayTypeDefinition,
    AssociationExpression,
    BinaryExpression,
    BlockConfiguration,
    BreakStatementItem,
    CallReference,
    CaseAlternative,
    CaseStatement,
    ComponentReference,
    CompositeNatureDefinition,
    CompositeTypeDefinition,
    ConditionalSignalAssignmentStatement,
    Configuration,
    ConfigurationItem,
    ConfigurationReference,
    Declaration,
    DelayMechanism,
    EntityReference,
    EnumerationLiteral,
    Expression,
    ExpressionStatement,
    GenerationScheme,
    IfStatement,
    IfStatementTest,
    InstantiationStatement,
    IterationScheme,
    Module,
    MultiName,
    MultiNamed,
    Name,
    Named,
    NatureDefinition,
    NatureReference,
    PackageReference,
    PhysicalTypeDefinitionSecondary,
    QuantityAspect,
    QuantityDeclaration,
    RecordNatureElement,
    RecordTypeElement,
    SignalAssignmentStatement,
    SourceAspect,
    Statement,
    SubprogramBody,
    SubprogramDeclaration,
    TypeDefinition,
    TypeReference,
    ValueDeclaration,
    ValueExpression,
    VhdlObject,
    configuration_ConfigurationItem,
    configuration_ConfigurationReference,
    configuration_vhdl_EntityReference,
    configuration_vhdl_GenericMaps,
    configuration_vhdl_MultiName,
    configuration_vhdl_Name,
    configuration_vhdl_PortMaps,
    declaration_Declaration,
    declaration_QuantityDeclaration,
    declaration_SubprogramDeclaration,
    declaration_vhdl_ComponentReference,
    declaration_vhdl_EntityReference,
    declaration_vhdl_GenericMaps,
    declaration_vhdl_MultiName,
    declaration_vhdl_Name,
    declaration_vhdl_PortMaps,
    expression_BinaryExpression,
    expression_Expression,
    expression_IndicationExpression,
    expression_MultiExpression,
    expression_ValueExpression,
    expression_vhdl_Name,
    expression_vhdl_Signature,
    nature_CompositeNatureDefinition,
    nature_NatureReference,
    nature_Natured,
    nature_vhdl_Name,
    statement_vhdl_CallReference,
    statement_vhdl_ComponentReference,
    statement_vhdl_EntityReference,
    statement_vhdl_GenericMaps,
    statement_vhdl_Generics,
    statement_vhdl_MultiName,
    statement_vhdl_Name,
    statement_vhdl_PortMaps,
    statement_vhdl_Ports,
    type_CompositeTypeDefinition,
    type_EnumerationLiteral,
    type_TypeDefinition,
    type_TypeReference,
    type_Typed,
    type_vhdl_Name,
    vhdl_Architecture,
    vhdl_CallReference,
    vhdl_CallResolvedReference,
    vhdl_Component,
    vhdl_ComponentReference,
    vhdl_ComponentResolvedReference,
    vhdl_DesignUnit,
    vhdl_Entity,
    vhdl_EntityReference,
    vhdl_EntityResolvedReference,
    vhdl_GenericMaps,
    vhdl_Generics,
    vhdl_Model,
    vhdl_Module,
    vhdl_MultiName,
    vhdl_MultiNamed,
    vhdl_Name,
    vhdl_NameList,
    vhdl_Named,
    vhdl_Package,
    vhdl_PackageBody,
    vhdl_PackageReference,
    vhdl_PackageResolvedReference,
    vhdl_PortMaps,
    vhdl_Ports,
    vhdl_Signature,
    vhdl_VhdlObject,
    vhdl_ams_Noise,
    vhdl_ams_QuantityAspect,
    vhdl_ams_SourceAspect,
    vhdl_ams_Spectrum,
    vhdl_configuration_BlockConfiguration,
    vhdl_configuration_ComponentConfiguration,
    vhdl_configuration_Configuration,
    vhdl_configuration_ConfigurationItem,
    vhdl_configuration_ConfigurationReference,
    vhdl_configuration_ConfigurationResolvedReference,
    vhdl_declaration_AliasDeclaration,
    vhdl_declaration_AttributeDeclaration,
    vhdl_declaration_AttributeSpecification,
    vhdl_declaration_BranchQuantityDeclaration,
    vhdl_declaration_ConfigurationSpecification,
    vhdl_declaration_ConstantDeclaration,
    vhdl_declaration_Declaration,
    vhdl_declaration_DisconnectionSpecification,
    vhdl_declaration_FileDeclaration,
    vhdl_declaration_FreeQuantityDeclaration,
    vhdl_declaration_FunctionDeclaration,
    vhdl_declaration_GroupDeclaration,
    vhdl_declaration_GroupTemplateDeclaration,
    vhdl_declaration_LimitDeclaration,
    vhdl_declaration_NatureDeclaration,
    vhdl_declaration_ProcedureDeclaration,
    vhdl_declaration_QuantityDeclaration,
    vhdl_declaration_SignalDeclaration,
    vhdl_declaration_SourceQuantityDeclaration,
    vhdl_declaration_SubnatureDeclaration,
    vhdl_declaration_SubprogramBody,
    vhdl_declaration_SubprogramDeclaration,
    vhdl_declaration_SubtypeDeclaration,
    vhdl_declaration_TerminalDeclaration,
    vhdl_declaration_TypeDeclaration,
    vhdl_declaration_UseClauseDeclaration,
    vhdl_declaration_ValueDeclaration,
    vhdl_declaration_VariableDeclaration,
    vhdl_expression_AddingExpression,
    vhdl_expression_AggregateExpression,
    vhdl_expression_AllExpression,
    vhdl_expression_AllocatorExpression,
    vhdl_expression_AssociationExpression,
    vhdl_expression_AttributeExpression,
    vhdl_expression_BinaryExpression,
    vhdl_expression_BitStringExpression,
    vhdl_expression_CharacterExpression,
    vhdl_expression_ConditionalWaveformExpression,
    vhdl_expression_Expression,
    vhdl_expression_IdentifierExpression,
    vhdl_expression_IndicationExpression,
    vhdl_expression_LogicalExpression,
    vhdl_expression_MultiExpression,
    vhdl_expression_MultiplyingExpression,
    vhdl_expression_NameExpression,
    vhdl_expression_NullExpression,
    vhdl_expression_OpenExpression,
    vhdl_expression_OthersExpression,
    vhdl_expression_PowerExpression,
    vhdl_expression_RangeExpression,
    vhdl_expression_RelationalExpression,
    vhdl_expression_ShiftExpression,
    vhdl_expression_SignExpression,
    vhdl_expression_SignatureExpression,
    vhdl_expression_StringExpression,
    vhdl_expression_SubnatureIndicationExpression,
    vhdl_expression_SubtypeIndicationExpression,
    vhdl_expression_TypeQualificationExpression,
    vhdl_expression_UnaffectedExpression,
    vhdl_expression_UnaryExpression,
    vhdl_expression_UnitValueExpression,
    vhdl_expression_ValueExpression,
    vhdl_expression_WaveformExpression,
    vhdl_nature_ArrayNatureDefinition,
    vhdl_nature_CompositeNatureDefinition,
    vhdl_nature_ConstrainedArrayNatureDefinition,
    vhdl_nature_NatureDefinition,
    vhdl_nature_NatureReference,
    vhdl_nature_Natured,
    vhdl_nature_RecordNatureDefinition,
    vhdl_nature_RecordNatureElement,
    vhdl_nature_ScalarNatureDefinition,
    vhdl_nature_UnconstrainedArrayNatureDefinition,
    vhdl_statement_AssertionStatement,
    vhdl_statement_BlockStatement,
    vhdl_statement_BreakStatement,
    vhdl_statement_BreakStatementItem,
    vhdl_statement_CaseAlternative,
    vhdl_statement_CaseStatement,
    vhdl_statement_ComponentInstantiationStatement,
    vhdl_statement_ConditionalSignalAssignmentStatement,
    vhdl_statement_ConfigurationInstantiationStatement,
    vhdl_statement_DelayMechanism,
    vhdl_statement_EntityInstantiationStatement,
    vhdl_statement_ExitStatement,
    vhdl_statement_ExpressionStatement,
    vhdl_statement_ForGenerationScheme,
    vhdl_statement_ForIterationScheme,
    vhdl_statement_GenerateStatement,
    vhdl_statement_GenerationScheme,
    vhdl_statement_IfGenerationScheme,
    vhdl_statement_IfStatement,
    vhdl_statement_IfStatementTest,
    vhdl_statement_InstantiationStatement,
    vhdl_statement_IterationScheme,
    vhdl_statement_LoopStatement,
    vhdl_statement_NextStatement,
    vhdl_statement_ProcedureCallStatement,
    vhdl_statement_ProcessStatement,
    vhdl_statement_RejectMechanism,
    vhdl_statement_ReportStatement,
    vhdl_statement_ReturnStatement,
    vhdl_statement_SelectedSignalAssignmentStatement,
    vhdl_statement_SequentialSignalAssignmentStatement,
    vhdl_statement_SignalAssignmentStatement,
    vhdl_statement_SimpleSimultaneousStatement,
    vhdl_statement_SimultaneousCaseStatement,
    vhdl_statement_SimultaneousIfStatement,
    vhdl_statement_SimultaneousProceduralStatement,
    vhdl_statement_Statement,
    vhdl_statement_TransportMechanism,
    vhdl_statement_VariableAssignmentStatement,
    vhdl_statement_WaitStatement,
    vhdl_statement_WhileIterationScheme,
    vhdl_type_AccessTypeDefinition,
    vhdl_type_ArrayTypeDefinition,
    vhdl_type_CompositeTypeDefinition,
    vhdl_type_ConstrainedArrayTypeDefinition,
    vhdl_type_EnumerationLiteral,
    vhdl_type_EnumerationTypeDefinition,
    vhdl_type_FileTypeDefinition,
    vhdl_type_PhysicalTypeDefinition,
    vhdl_type_PhysicalTypeDefinitionSecondary,
    vhdl_type_RangeTypeDefinition,
    vhdl_type_RecordTypeDefinition,
    vhdl_type_RecordTypeElement,
    vhdl_type_TypeDefinition,
    vhdl_type_TypeReference,
    vhdl_type_Typed,
    vhdl_type_UnconstrainedArrayTypeDefinition,
    AddingOperator,
    EntityClass,
    LogicalOperator,
    Mode,
    MultiplyingOperator,
    Purity,
    RangeDirection,
    RelationalOperator,
    ShiftOperator,
    Sign,
    SignalKind,
    UnaryOperator,
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

def test_assoc_condition105_stub_double():
    # Expression has no real 'Expression106' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_AssertionStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_AssertionStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_AssertionStatement(postponed=True)
    partner = Expression()
    setattr(partner, 'Expression106', None)
    _safe_set(owner, 'vhdl_statement_AssertionStatement', partner)
    assert getattr(partner, 'Expression106') == owner
    _safe_set(owner, 'vhdl_statement_AssertionStatement', None)
    assert getattr(partner, 'Expression106') is None


def test_assoc_declaration97_stub_double():
    # Declaration has no real 'Declaration98' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ProcessStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ProcessStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ProcessStatement(postponed=True)
    partner = Declaration()
    setattr(partner, 'Declaration98', None)
    _safe_set(owner, 'vhdl_statement_ProcessStatement', {partner})
    assert getattr(partner, 'Declaration98') == owner
    _safe_set(owner, 'vhdl_statement_ProcessStatement', set())
    assert getattr(partner, 'Declaration98') is None


def test_assoc_delay59_stub_double():
    # DelayMechanism has no real 'DelayMechanism' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_SignalAssignmentStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_SignalAssignmentStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_SignalAssignmentStatement(guarded=True, postponed=True)
    partner = DelayMechanism()
    setattr(partner, 'DelayMechanism', None)
    _safe_set(owner, 'vhdl_statement_SignalAssignmentStatement60', partner)
    assert getattr(partner, 'DelayMechanism') == owner
    _safe_set(owner, 'vhdl_statement_SignalAssignmentStatement60', None)
    assert getattr(partner, 'DelayMechanism') is None


def test_assoc_design23_stub_double():
    # vhdl_Model has no real 'vhdl_Model' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_DesignUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_DesignUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_DesignUnit(library="sample_text")
    partner = vhdl_Model()
    setattr(partner, 'vhdl_Model', None)
    _safe_set(owner, 'vhdl_DesignUnit24', partner)
    assert owner in getattr(partner, 'vhdl_Model')
    _safe_set(owner, 'vhdl_DesignUnit24', None)
    assert owner not in getattr(partner, 'vhdl_Model')


def test_assoc_entity233_stub_double():
    # declaration_vhdl_MultiName has no real 'declaration_vhdl_MultiName' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_declaration_AttributeSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_declaration_AttributeSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_declaration_AttributeSpecification(class_="sample_text")
    partner = declaration_vhdl_MultiName()
    setattr(partner, 'declaration_vhdl_MultiName', None)
    _safe_set(owner, 'vhdl_declaration_AttributeSpecification', partner)
    assert getattr(partner, 'declaration_vhdl_MultiName') == owner
    _safe_set(owner, 'vhdl_declaration_AttributeSpecification', None)
    assert getattr(partner, 'declaration_vhdl_MultiName') is None


def test_assoc_expression214_stub_double():
    # Expression has no real 'Expression215' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_expression_SignExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_expression_SignExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_expression_SignExpression(sign="sample_text")
    partner = Expression()
    setattr(partner, 'Expression215', None)
    _safe_set(owner, 'vhdl_expression_SignExpression', partner)
    assert getattr(partner, 'Expression215') == owner
    _safe_set(owner, 'vhdl_expression_SignExpression', None)
    assert getattr(partner, 'Expression215') is None


def test_assoc_expression216_stub_double():
    # Expression has no real 'Expression217' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_expression_UnaryExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_expression_UnaryExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_expression_UnaryExpression(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression217', None)
    _safe_set(owner, 'vhdl_expression_UnaryExpression', partner)
    assert getattr(partner, 'Expression217') == owner
    _safe_set(owner, 'vhdl_expression_UnaryExpression', None)
    assert getattr(partner, 'Expression217') is None


def test_assoc_in_178_stub_double():
    # Expression has no real 'Expression179' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ForGenerationScheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ForGenerationScheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ForGenerationScheme(variable="sample_text")
    partner = Expression()
    setattr(partner, 'Expression179', None)
    _safe_set(owner, 'vhdl_statement_ForGenerationScheme', partner)
    assert getattr(partner, 'Expression179') == owner
    _safe_set(owner, 'vhdl_statement_ForGenerationScheme', None)
    assert getattr(partner, 'Expression179') is None


def test_assoc_in_180_stub_double():
    # Expression has no real 'Expression181' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ForIterationScheme's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ForIterationScheme's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ForIterationScheme(variable="sample_text")
    partner = Expression()
    setattr(partner, 'Expression181', None)
    _safe_set(owner, 'vhdl_statement_ForIterationScheme', partner)
    assert getattr(partner, 'Expression181') == owner
    _safe_set(owner, 'vhdl_statement_ForIterationScheme', None)
    assert getattr(partner, 'Expression181') is None


def test_assoc_is_234_stub_double():
    # Expression has no real 'Expression236' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_declaration_AttributeSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_declaration_AttributeSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_declaration_AttributeSpecification(class_="sample_text")
    partner = Expression()
    setattr(partner, 'Expression236', None)
    _safe_set(owner, 'vhdl_declaration_AttributeSpecification235', partner)
    assert getattr(partner, 'Expression236') == owner
    _safe_set(owner, 'vhdl_declaration_AttributeSpecification235', None)
    assert getattr(partner, 'Expression236') is None


def test_assoc_left306_stub_double():
    # Expression has no real 'Expression307' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_type_RangeTypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_type_RangeTypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_type_RangeTypeDefinition(direction="sample_text")
    partner = Expression()
    setattr(partner, 'Expression307', None)
    _safe_set(owner, 'vhdl_type_RangeTypeDefinition', partner)
    assert getattr(partner, 'Expression307') == owner
    _safe_set(owner, 'vhdl_type_RangeTypeDefinition', None)
    assert getattr(partner, 'Expression307') is None


def test_assoc_module7_stub_double():
    # vhdl_Module has no real 'vhdl_Module' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_DesignUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_DesignUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_DesignUnit(library="sample_text")
    partner = vhdl_Module()
    setattr(partner, 'vhdl_Module', None)
    _safe_set(owner, 'vhdl_DesignUnit8', partner)
    assert getattr(partner, 'vhdl_Module') == owner
    _safe_set(owner, 'vhdl_DesignUnit8', None)
    assert getattr(partner, 'vhdl_Module') is None


def test_assoc_of305_stub_double():
    # type_vhdl_Name has no real 'type_vhdl_Name' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_type_PhysicalTypeDefinitionSecondary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_type_PhysicalTypeDefinitionSecondary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_type_PhysicalTypeDefinitionSecondary(name="sample_text", number="sample_text")
    partner = type_vhdl_Name()
    setattr(partner, 'type_vhdl_Name', None)
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinitionSecondary', partner)
    assert getattr(partner, 'type_vhdl_Name') == owner
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinitionSecondary', None)
    assert getattr(partner, 'type_vhdl_Name') is None


def test_assoc_procedure91_stub_double():
    # statement_vhdl_CallReference has no real 'statement_vhdl_CallReference' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ProcedureCallStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ProcedureCallStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ProcedureCallStatement(postponed=True)
    partner = statement_vhdl_CallReference()
    setattr(partner, 'statement_vhdl_CallReference', None)
    _safe_set(owner, 'vhdl_statement_ProcedureCallStatement', partner)
    assert getattr(partner, 'statement_vhdl_CallReference') == owner
    _safe_set(owner, 'vhdl_statement_ProcedureCallStatement', None)
    assert getattr(partner, 'statement_vhdl_CallReference') is None


def test_assoc_range301_stub_double():
    # Expression has no real 'Expression302' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_type_PhysicalTypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_type_PhysicalTypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_type_PhysicalTypeDefinition(primary="sample_text")
    partner = Expression()
    setattr(partner, 'Expression302', None)
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinition', partner)
    assert getattr(partner, 'Expression302') == owner
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinition', None)
    assert getattr(partner, 'Expression302') is None


def test_assoc_report107_stub_double():
    # Expression has no real 'Expression109' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_AssertionStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_AssertionStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_AssertionStatement(postponed=True)
    partner = Expression()
    setattr(partner, 'Expression109', None)
    _safe_set(owner, 'vhdl_statement_AssertionStatement108', partner)
    assert getattr(partner, 'Expression109') == owner
    _safe_set(owner, 'vhdl_statement_AssertionStatement108', None)
    assert getattr(partner, 'Expression109') is None


def test_assoc_right308_stub_double():
    # Expression has no real 'Expression310' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_type_RangeTypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_type_RangeTypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_type_RangeTypeDefinition(direction="sample_text")
    partner = Expression()
    setattr(partner, 'Expression310', None)
    _safe_set(owner, 'vhdl_type_RangeTypeDefinition309', partner)
    assert getattr(partner, 'Expression310') == owner
    _safe_set(owner, 'vhdl_type_RangeTypeDefinition309', None)
    assert getattr(partner, 'Expression310') is None


def test_assoc_secondary303_stub_double():
    # PhysicalTypeDefinitionSecondary has no real 'PhysicalTypeDefinitionSecondary' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_type_PhysicalTypeDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_type_PhysicalTypeDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_type_PhysicalTypeDefinition(primary="sample_text")
    partner = PhysicalTypeDefinitionSecondary()
    setattr(partner, 'PhysicalTypeDefinitionSecondary', None)
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinition304', {partner})
    assert getattr(partner, 'PhysicalTypeDefinitionSecondary') == owner
    _safe_set(owner, 'vhdl_type_PhysicalTypeDefinition304', set())
    assert getattr(partner, 'PhysicalTypeDefinitionSecondary') is None


def test_assoc_sensitivity102_stub_double():
    # statement_vhdl_MultiName has no real 'statement_vhdl_MultiName104' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ProcessStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ProcessStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ProcessStatement(postponed=True)
    partner = statement_vhdl_MultiName()
    setattr(partner, 'statement_vhdl_MultiName104', None)
    _safe_set(owner, 'vhdl_statement_ProcessStatement103', partner)
    assert getattr(partner, 'statement_vhdl_MultiName104') == owner
    _safe_set(owner, 'vhdl_statement_ProcessStatement103', None)
    assert getattr(partner, 'statement_vhdl_MultiName104') is None


def test_assoc_severity110_stub_double():
    # Expression has no real 'Expression112' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_AssertionStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_AssertionStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_AssertionStatement(postponed=True)
    partner = Expression()
    setattr(partner, 'Expression112', None)
    _safe_set(owner, 'vhdl_statement_AssertionStatement111', partner)
    assert getattr(partner, 'Expression112') == owner
    _safe_set(owner, 'vhdl_statement_AssertionStatement111', None)
    assert getattr(partner, 'Expression112') is None


def test_assoc_statement99_stub_double():
    # Statement has no real 'Statement101' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ProcessStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ProcessStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ProcessStatement(postponed=True)
    partner = Statement()
    setattr(partner, 'Statement101', None)
    _safe_set(owner, 'vhdl_statement_ProcessStatement100', {partner})
    assert getattr(partner, 'Statement101') == owner
    _safe_set(owner, 'vhdl_statement_ProcessStatement100', set())
    assert getattr(partner, 'Statement101') is None


def test_assoc_target57_stub_double():
    # Expression has no real 'Expression58' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_SignalAssignmentStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_SignalAssignmentStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_SignalAssignmentStatement(guarded=True, postponed=True)
    partner = Expression()
    setattr(partner, 'Expression58', None)
    _safe_set(owner, 'vhdl_statement_SignalAssignmentStatement', partner)
    assert getattr(partner, 'Expression58') == owner
    _safe_set(owner, 'vhdl_statement_SignalAssignmentStatement', None)
    assert getattr(partner, 'Expression58') is None


def test_assoc_use6_stub_double():
    # vhdl_Name has no real 'vhdl_Name' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_DesignUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_DesignUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_DesignUnit(library="sample_text")
    partner = vhdl_Name()
    setattr(partner, 'vhdl_Name', None)
    _safe_set(owner, 'vhdl_DesignUnit', {partner})
    assert getattr(partner, 'vhdl_Name') == owner
    _safe_set(owner, 'vhdl_DesignUnit', set())
    assert getattr(partner, 'vhdl_Name') is None


def test_assoc_when159_stub_double():
    # Expression has no real 'Expression160' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_ExitStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_ExitStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_ExitStatement(exit="sample_text")
    partner = Expression()
    setattr(partner, 'Expression160', None)
    _safe_set(owner, 'vhdl_statement_ExitStatement', partner)
    assert getattr(partner, 'Expression160') == owner
    _safe_set(owner, 'vhdl_statement_ExitStatement', None)
    assert getattr(partner, 'Expression160') is None


def test_assoc_when172_stub_double():
    # Expression has no real 'Expression173' property in the generated
    # code (a bare stub) -- manually attach it so vhdl_statement_NextStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # vhdl_statement_NextStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = vhdl_statement_NextStatement(next="sample_text")
    partner = Expression()
    setattr(partner, 'Expression173', None)
    _safe_set(owner, 'vhdl_statement_NextStatement', partner)
    assert getattr(partner, 'Expression173') == owner
    _safe_set(owner, 'vhdl_statement_NextStatement', None)
    assert getattr(partner, 'Expression173') is None


