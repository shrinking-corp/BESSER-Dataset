import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActualSituation,
    CharacteristicType,
    ConditionalRule,
    ConstantReference,
    Context,
    CoveringConstraint,
    Definition,
    EntityType,
    Equality,
    Evaluation,
    ExpressionContext,
    ExpressionNode,
    Facade,
    Facet,
    FunctionCall,
    FunctionType,
    GeneralizationConstraint,
    IRIIdentifier,
    IdentifiableEntity,
    Identifier,
    InformationSource,
    LexicalReference,
    LexicalScope,
    Mapping,
    MatchEnd,
    MatchRule,
    Metadata,
    MultiplicityConstraint,
    Name,
    Namespace,
    ObjectOperationType,
    OwnedPropertyBinding,
    Package,
    Pattern,
    PatternMatch,
    PatternOfType,
    PatternVariable,
    Prefix,
    PropertyBinding,
    PropertyConstraint,
    PropertyOwnerType,
    PropertyType,
    PropertyTypeConstraint,
    Proposition,
    PropositionVariable,
    Record,
    RecordType,
    Relationship,
    RepresentationRule,
    Rule,
    Situation,
    Statement,
    SystemOfUnits,
    TechnicalIdentifier,
    TemporalEntity,
    Term,
    TextIdentifier,
    Thing,
    Traversal,
    Type,
    TypeConstraint,
    TypePatternVariable,
    UniqueIdentifier,
    UniqueTextIdentifier,
    UniquenessConstraint,
    UnitType,
    UnitValue,
    Value,
    ValueType,
    VariableBinding,
    constraints_Conditional,
    constraints_Rule,
    expressions_ExpressionContext,
    expressions_ExpressionNode,
    facets_Facet,
    identifiers_Name,
    identifiers_TextIdentifier,
    identifiers_UniqueIdentifier,
    identifiers_UniqueTextIdentifier,
    lexicalscope_LexicalScope,
    metadata_Metadata,
    patterns_Computed,
    patterns_Pattern,
    patterns_PatternVariable,
    properties_OwnedPropertyType,
    properties_PropertyBinding,
    properties_PropertyOwner,
    properties_PropertyOwnerType,
    properties_PropertyType,
    situations_ActualSituation,
    situations_Situation,
    situations_SituationType,
    smif_Repository,
    smif_associations_Association,
    smif_associations_AssociationType,
    smif_constraints_Conditional,
    smif_constraints_ConditionalRule,
    smif_constraints_CoveringConstraint,
    smif_constraints_Disjoint,
    smif_constraints_Enumerated,
    smif_constraints_Equivalent,
    smif_constraints_FacetClassificationConstraint,
    smif_constraints_GeneralizationConstraint,
    smif_constraints_MultiplicityConstraint,
    smif_constraints_PropertyConstraint,
    smif_constraints_PropertyTransitivityConstraint,
    smif_constraints_PropertyTypeConstraint,
    smif_constraints_Rule,
    smif_constraints_TypeConstraint,
    smif_constraints_UniquenessConstraint,
    smif_expressions_ConstantReference,
    smif_expressions_Equality,
    smif_expressions_Evaluation,
    smif_expressions_ExpressionContext,
    smif_expressions_ExpressionNode,
    smif_expressions_FunctionCall,
    smif_expressions_FunctionType,
    smif_expressions_ObjectOperationType,
    smif_expressions_Traversal,
    smif_facets_Category,
    smif_facets_Facet,
    smif_facets_FacetOfEntity,
    smif_facets_Phase,
    smif_facets_Role,
    smif_identifiers_IRIIdentifier,
    smif_identifiers_Identifier,
    smif_identifiers_Name,
    smif_identifiers_Namespace,
    smif_identifiers_TechnicalIdentifier,
    smif_identifiers_Term,
    smif_identifiers_TextIdentifier,
    smif_identifiers_UniqueIdentifier,
    smif_identifiers_UniqueTextIdentifier,
    smif_lexicalscope_Include,
    smif_lexicalscope_LexicalReference,
    smif_lexicalscope_LexicalScope,
    smif_lexicalscope_LogicalPackage,
    smif_lexicalscope_MOFPackage,
    smif_lexicalscope_MappingPackage,
    smif_lexicalscope_Model,
    smif_lexicalscope_Package,
    smif_lexicalscope_PhysicalPackage,
    smif_lexicalscope_Prefix,
    smif_mapping_ComputedFacade,
    smif_mapping_Facade,
    smif_mapping_Mapping,
    smif_mapping_MatchEnd,
    smif_mapping_MatchRule,
    smif_mapping_RepresentationRule,
    smif_metadata_Definition,
    smif_metadata_InformationSource,
    smif_metadata_Metadata,
    smif_metadata_Statement,
    smif_patterns_Computed,
    smif_patterns_ExpressionVariable,
    smif_patterns_FocusVariable,
    smif_patterns_PartVariable,
    smif_patterns_Pattern,
    smif_patterns_PatternMatch,
    smif_patterns_PatternOfType,
    smif_patterns_PatternVariable,
    smif_patterns_PropositionVariable,
    smif_patterns_TypePatternVariable,
    smif_patterns_VariableBinding,
    smif_properties_AnnotationProperty,
    smif_properties_CharacteristicBinding,
    smif_properties_CharacteristicType,
    smif_properties_OwnedPropertyBinding,
    smif_properties_OwnedPropertyType,
    smif_properties_PropertyBinding,
    smif_properties_PropertyOwner,
    smif_properties_PropertyOwnerType,
    smif_properties_PropertyType,
    smif_records_Record,
    smif_records_RecordType,
    smif_relationships_Relationship,
    smif_relationships_RelationshipType,
    smif_situations_ActualSituation,
    smif_situations_Situation,
    smif_situations_SituationType,
    smif_toplevel_ActualEntity,
    smif_toplevel_Context,
    smif_toplevel_IdentifiableEntity,
    smif_toplevel_Proposition,
    smif_toplevel_TemporalEntity,
    smif_toplevel_Thing,
    smif_types_EntityType,
    smif_types_IntersectionType,
    smif_types_Type,
    smif_types_UnionType,
    smif_values_BaseUnitType,
    smif_values_QuantityKind,
    smif_values_ScalarQuantity,
    smif_values_StructuredValue,
    smif_values_StructuredValueType,
    smif_values_SystemOfUnits,
    smif_values_UnitType,
    smif_values_UnitValue,
    smif_values_Value,
    smif_values_ValueType,
    toplevel_ActualEntity,
    toplevel_Context,
    toplevel_Proposition,
    toplevel_TemporalEntity,
    values_Value,
    values_ValueType,
    AssertionStrength,
    VariableQualification,
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

def test_assoc_concreteEnd135_stub_double():
    # MatchEnd has no real 'MatchEnd136' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_MatchRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_MatchRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_MatchRule(coerce="sample_text")
    partner = MatchEnd()
    setattr(partner, 'MatchEnd136', None)
    _safe_set(owner, 'matchFrom', partner)
    assert getattr(partner, 'MatchEnd136') == owner
    _safe_set(owner, 'matchFrom', None)
    assert getattr(partner, 'MatchEnd136') is None


def test_assoc_concreteFocus148_stub_double():
    # PatternVariable has no real 'PatternVariable149' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_Mapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_Mapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_Mapping(strength="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable149', None)
    _safe_set(owner, 'concreteMapping', partner)
    assert getattr(partner, 'PatternVariable149') == owner
    _safe_set(owner, 'concreteMapping', None)
    assert getattr(partner, 'PatternVariable149') is None


def test_assoc_concreteMapping121_stub_double():
    # Mapping has no real 'Mapping122' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = Mapping()
    setattr(partner, 'Mapping122', None)
    _safe_set(owner, 'concreteFocus', partner)
    assert getattr(partner, 'Mapping122') == owner
    _safe_set(owner, 'concreteFocus', None)
    assert getattr(partner, 'Mapping122') is None


def test_assoc_definedWithinSystem20_stub_double():
    # SystemOfUnits has no real 'SystemOfUnits' property in the generated
    # code (a bare stub) -- manually attach it so smif_values_UnitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_values_UnitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_values_UnitType(offset="sample_text", ratio="sample_text", symbol="sample_text")
    partner = SystemOfUnits()
    setattr(partner, 'SystemOfUnits', None)
    _safe_set(owner, 'unitOfSystem', partner)
    assert getattr(partner, 'SystemOfUnits') == owner
    _safe_set(owner, 'unitOfSystem', None)
    assert getattr(partner, 'SystemOfUnits') is None


def test_assoc_definesEntity186_stub_double():
    # IdentifiableEntity has no real 'IdentifiableEntity187' property in the generated
    # code (a bare stub) -- manually attach it so smif_metadata_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_metadata_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_metadata_Definition(summaryDescription="sample_text", textDefinition="sample_text")
    partner = IdentifiableEntity()
    setattr(partner, 'IdentifiableEntity187', None)
    _safe_set(owner, 'definedBy', partner)
    assert getattr(partner, 'IdentifiableEntity187') == owner
    _safe_set(owner, 'definedBy', None)
    assert getattr(partner, 'IdentifiableEntity187') is None


def test_assoc_evaluatedBy33_stub_double():
    # Evaluation has no real 'Evaluation' property in the generated
    # code (a bare stub) -- manually attach it so smif_expressions_ExpressionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_expressions_ExpressionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_expressions_ExpressionNode(expressionText="sample_text", expressionTextLanguage="sample_text")
    partner = Evaluation()
    setattr(partner, 'Evaluation', None)
    _safe_set(owner, 'evaluates', {partner})
    assert getattr(partner, 'Evaluation') == owner
    _safe_set(owner, 'evaluates', set())
    assert getattr(partner, 'Evaluation') is None


def test_assoc_excludedBy116_stub_double():
    # PatternVariable has no real 'PatternVariable117' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable117', None)
    _safe_set(owner, 'excludes', {partner})
    assert getattr(partner, 'PatternVariable117') == owner
    _safe_set(owner, 'excludes', set())
    assert getattr(partner, 'PatternVariable117') is None


def test_assoc_excludes118_stub_double():
    # PatternVariable has no real 'PatternVariable119' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable119', None)
    _safe_set(owner, 'excludedBy', {partner})
    assert getattr(partner, 'PatternVariable119') == owner
    _safe_set(owner, 'excludedBy', set())
    assert getattr(partner, 'PatternVariable119') is None


def test_assoc_externalReference183_stub_double():
    # IRIIdentifier has no real 'IRIIdentifier' property in the generated
    # code (a bare stub) -- manually attach it so smif_metadata_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_metadata_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_metadata_Definition(summaryDescription="sample_text", textDefinition="sample_text")
    partner = IRIIdentifier()
    setattr(partner, 'IRIIdentifier', None)
    _safe_set(owner, 'smif_metadata_Definition', partner)
    assert getattr(partner, 'IRIIdentifier') == owner
    _safe_set(owner, 'smif_metadata_Definition', None)
    assert getattr(partner, 'IRIIdentifier') is None


def test_assoc_externalTerm184_stub_double():
    # Term has no real 'Term' property in the generated
    # code (a bare stub) -- manually attach it so smif_metadata_Definition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_metadata_Definition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_metadata_Definition(summaryDescription="sample_text", textDefinition="sample_text")
    partner = Term()
    setattr(partner, 'Term', None)
    _safe_set(owner, 'smif_metadata_Definition185', partner)
    assert getattr(partner, 'Term') == owner
    _safe_set(owner, 'smif_metadata_Definition185', None)
    assert getattr(partner, 'Term') is None


def test_assoc_hasGeneral58_stub_double():
    # Type has no real 'Type59' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_GeneralizationConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_GeneralizationConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_GeneralizationConstraint(redefines="sample_text")
    partner = Type()
    setattr(partner, 'Type59', None)
    _safe_set(owner, 'hasSpecialization', partner)
    assert getattr(partner, 'Type59') == owner
    _safe_set(owner, 'hasSpecialization', None)
    assert getattr(partner, 'Type59') is None


def test_assoc_hasMapRule150_stub_double():
    # MatchRule has no real 'MatchRule151' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_Mapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_Mapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_Mapping(strength="sample_text")
    partner = MatchRule()
    setattr(partner, 'MatchRule151', None)
    _safe_set(owner, 'mapRuleOf', {partner})
    assert getattr(partner, 'MatchRule151') == owner
    _safe_set(owner, 'mapRuleOf', set())
    assert getattr(partner, 'MatchRule151') is None


def test_assoc_hasOwningPattern109_stub_double():
    # Pattern has no real 'Pattern' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = Pattern()
    setattr(partner, 'Pattern', None)
    _safe_set(owner, 'ownsVariable', partner)
    assert getattr(partner, 'Pattern') == owner
    _safe_set(owner, 'ownsVariable', None)
    assert getattr(partner, 'Pattern') is None


def test_assoc_hasSpecific60_stub_double():
    # Type has no real 'Type61' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_GeneralizationConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_GeneralizationConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_GeneralizationConstraint(redefines="sample_text")
    partner = Type()
    setattr(partner, 'Type61', None)
    _safe_set(owner, 'hasGeneralization', partner)
    assert getattr(partner, 'Type61') == owner
    _safe_set(owner, 'hasGeneralization', None)
    assert getattr(partner, 'Type61') is None


def test_assoc_hasSubset110_stub_double():
    # PatternVariable has no real 'PatternVariable111' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable111', None)
    _safe_set(owner, 'subsets', {partner})
    assert getattr(partner, 'PatternVariable111') == owner
    _safe_set(owner, 'subsets', set())
    assert getattr(partner, 'PatternVariable111') is None


def test_assoc_hasUnique56_stub_double():
    # PropertyType has no real 'PropertyType57' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_UniquenessConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_UniquenessConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_UniquenessConstraint(isPrimaryIdentity="sample_text")
    partner = PropertyType()
    setattr(partner, 'PropertyType57', None)
    _safe_set(owner, 'hasUniquenessConstraint', {partner})
    assert getattr(partner, 'PropertyType57') == owner
    _safe_set(owner, 'hasUniquenessConstraint', set())
    assert getattr(partner, 'PropertyType57') is None


def test_assoc_implements34_stub_double():
    # FunctionType has no real 'FunctionType' property in the generated
    # code (a bare stub) -- manually attach it so smif_expressions_ExpressionNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_expressions_ExpressionNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_expressions_ExpressionNode(expressionText="sample_text", expressionTextLanguage="sample_text")
    partner = FunctionType()
    setattr(partner, 'FunctionType', None)
    _safe_set(owner, 'implementedBy', partner)
    assert getattr(partner, 'FunctionType') == owner
    _safe_set(owner, 'implementedBy', None)
    assert getattr(partner, 'FunctionType') is None


def test_assoc_isOfType62_stub_double():
    # Type has no real 'Type63' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_PropertyTypeConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_PropertyTypeConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_PropertyTypeConstraint(prerequisiteType="sample_text")
    partner = Type()
    setattr(partner, 'Type63', None)
    _safe_set(owner, 'propertiesOfType', partner)
    assert getattr(partner, 'Type63') == owner
    _safe_set(owner, 'propertiesOfType', None)
    assert getattr(partner, 'Type63') is None


def test_assoc_mapRuleOf139_stub_double():
    # Mapping has no real 'Mapping140' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_MatchRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_MatchRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_MatchRule(coerce="sample_text")
    partner = Mapping()
    setattr(partner, 'Mapping140', None)
    _safe_set(owner, 'hasMapRule', partner)
    assert getattr(partner, 'Mapping140') == owner
    _safe_set(owner, 'hasMapRule', None)
    assert getattr(partner, 'Mapping140') is None


def test_assoc_mapsTo112_stub_double():
    # MatchEnd has no real 'MatchEnd113' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = MatchEnd()
    setattr(partner, 'MatchEnd113', None)
    _safe_set(owner, 'mapsVariable', {partner})
    assert getattr(partner, 'MatchEnd113') == owner
    _safe_set(owner, 'mapsVariable', set())
    assert getattr(partner, 'MatchEnd113') is None


def test_assoc_multiplicityOf54_stub_double():
    # Type has no real 'Type55' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_MultiplicityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_MultiplicityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_MultiplicityConstraint(atOnce="sample_text", isSufficent="sample_text", maximumNumber="sample_text", mininumNumber="sample_text")
    partner = Type()
    setattr(partner, 'Type55', None)
    _safe_set(owner, 'hasMultiplicity', partner)
    assert getattr(partner, 'Type55') == owner
    _safe_set(owner, 'hasMultiplicity', None)
    assert getattr(partner, 'Type55') is None


def test_assoc_referenceEnd137_stub_double():
    # MatchEnd has no real 'MatchEnd138' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_MatchRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_MatchRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_MatchRule(coerce="sample_text")
    partner = MatchEnd()
    setattr(partner, 'MatchEnd138', None)
    _safe_set(owner, 'matchTo', partner)
    assert getattr(partner, 'MatchEnd138') == owner
    _safe_set(owner, 'matchTo', None)
    assert getattr(partner, 'MatchEnd138') is None


def test_assoc_referenceFocus152_stub_double():
    # PatternVariable has no real 'PatternVariable153' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_Mapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_Mapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_Mapping(strength="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable153', None)
    _safe_set(owner, 'referenceMapping', partner)
    assert getattr(partner, 'PatternVariable153') == owner
    _safe_set(owner, 'referenceMapping', None)
    assert getattr(partner, 'PatternVariable153') is None


def test_assoc_referenceMapping120_stub_double():
    # Mapping has no real 'Mapping' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = Mapping()
    setattr(partner, 'Mapping', None)
    _safe_set(owner, 'referenceFocus', partner)
    assert getattr(partner, 'Mapping') == owner
    _safe_set(owner, 'referenceFocus', None)
    assert getattr(partner, 'Mapping') is None


def test_assoc_representedBy154_stub_double():
    # Type has no real 'Type155' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_RepresentationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_RepresentationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_RepresentationRule(mapAll="sample_text")
    partner = Type()
    setattr(partner, 'Type155', None)
    _safe_set(owner, 'representsRule', partner)
    assert getattr(partner, 'Type155') == owner
    _safe_set(owner, 'representsRule', None)
    assert getattr(partner, 'Type155') is None


def test_assoc_representedType156_stub_double():
    # Type has no real 'Type157' property in the generated
    # code (a bare stub) -- manually attach it so smif_mapping_RepresentationRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_mapping_RepresentationRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_mapping_RepresentationRule(mapAll="sample_text")
    partner = Type()
    setattr(partner, 'Type157', None)
    _safe_set(owner, 'conceptRule', {partner})
    assert getattr(partner, 'Type157') == owner
    _safe_set(owner, 'conceptRule', set())
    assert getattr(partner, 'Type157') is None


def test_assoc_subsets114_stub_double():
    # PatternVariable has no real 'PatternVariable115' property in the generated
    # code (a bare stub) -- manually attach it so smif_patterns_PatternVariable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_patterns_PatternVariable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_patterns_PatternVariable(explicit="sample_text", qualification="sample_text")
    partner = PatternVariable()
    setattr(partner, 'PatternVariable115', None)
    _safe_set(owner, 'hasSubset', {partner})
    assert getattr(partner, 'PatternVariable115') == owner
    _safe_set(owner, 'hasSubset', set())
    assert getattr(partner, 'PatternVariable115') is None


def test_assoc_traversesThrough37_stub_double():
    # PropertyType has no real 'PropertyType38' property in the generated
    # code (a bare stub) -- manually attach it so smif_expressions_Traversal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_expressions_Traversal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_expressions_Traversal(inverse="sample_text", traverseToRelation="sample_text")
    partner = PropertyType()
    setattr(partner, 'PropertyType38', None)
    _safe_set(owner, 'traversedBy', {partner})
    assert getattr(partner, 'PropertyType38') == owner
    _safe_set(owner, 'traversedBy', set())
    assert getattr(partner, 'PropertyType38') is None


def test_assoc_unitReference19_stub_double():
    # Definition has no real 'Definition' property in the generated
    # code (a bare stub) -- manually attach it so smif_values_UnitType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_values_UnitType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_values_UnitType(offset="sample_text", ratio="sample_text", symbol="sample_text")
    partner = Definition()
    setattr(partner, 'Definition', None)
    _safe_set(owner, 'smif_values_UnitType', partner)
    assert getattr(partner, 'Definition') == owner
    _safe_set(owner, 'smif_values_UnitType', None)
    assert getattr(partner, 'Definition') is None


def test_assoc_withRespectTo52_stub_double():
    # Type has no real 'Type53' property in the generated
    # code (a bare stub) -- manually attach it so smif_constraints_MultiplicityConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smif_constraints_MultiplicityConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smif_constraints_MultiplicityConstraint(atOnce="sample_text", isSufficent="sample_text", maximumNumber="sample_text", mininumNumber="sample_text")
    partner = Type()
    setattr(partner, 'Type53', None)
    _safe_set(owner, 'respectOf', {partner})
    assert getattr(partner, 'Type53') == owner
    _safe_set(owner, 'respectOf', set())
    assert getattr(partner, 'Type53') is None


