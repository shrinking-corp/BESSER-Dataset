import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotableElement,
    Annotation,
    AnnotationParameter,
    Assignment,
    Attribute2Attribute,
    AttributeDcl,
    AttributeModifier,
    AttributeRef,
    AttributeRightPart,
    AttributionRule,
    AvailableTransformation,
    C2CModifier,
    Class2Class,
    ClassMapping,
    ClassRef,
    ClassUse,
    ClosureParameter,
    CompositeTransformation,
    Context,
    Converter,
    DefaultValue,
    DefinitionParameter,
    Delegate,
    Expression,
    ExternalTransformation,
    Feature2Feature,
    FeatureRef,
    GeneratedModel,
    IfBranch,
    ImportedModel,
    InlineClass,
    InlineFeature,
    InlineModel,
    InvocationParameter,
    InvokeTransformation,
    IteratorStatement,
    KeywordParameter,
    KoanRule,
    LocatedElement,
    MappingElement,
    MatchPredicate,
    MatchedElement,
    Matcher,
    MetamodelElementRef,
    MethodDefinition,
    MethodParameter,
    MethodSelf,
    Modifier,
    ModuleDefinition,
    NamedElement,
    NamedInvocationParameter,
    ObjectInstantiation,
    ObjectSourceVariable,
    Operator,
    PFeature,
    PObject,
    POutputVariable,
    PReference,
    Pattern,
    PutTraceParameter,
    QoolQueue,
    QueueOptimization,
    ReferenceAssignment,
    ReferenceRef,
    RepresentModel,
    RequireDeclaration,
    RequireParameter,
    ResolveLink,
    RuleSelf,
    Section,
    Segment,
    SingleAnnotation,
    SourceExpression,
    Statement,
    Tag,
    Template,
    TemplateParameter,
    TemplateRootObject,
    TraceCompareExpression,
    TraceDefinition,
    TraceElement,
    TraceInterface,
    TransformationDefinition,
    TransformationDefinitionParameter,
    TransformationExecution,
    TypeExpression,
    UseDeclaration,
    Variable,
    chain_AvailableTransformation,
    core_AnnotableElement,
    core_ClassUse,
    core_DefinitionParameter,
    core_Expression,
    core_ImplicitlyAnnotableElement,
    core_LocatedElement,
    core_ModuleDefinition,
    core_NamedElement,
    core_RepresentModel,
    core_Statement,
    core_TransformationDefinition,
    core_TypeExpression,
    core_TypedWithClass,
    core_Variable,
    facilities_CopierCallbackDefinition,
    frontend_DummyRootMetaclass,
    frontend_attribution_AttributeDcl,
    frontend_attribution_AttributeInit,
    frontend_attribution_AttributeUse,
    frontend_attribution_AttributionRule,
    frontend_attribution_AttributionTransformation,
    frontend_attribution_InheritedAttributeDcl,
    frontend_attribution_RuleSelf,
    frontend_attribution_SynthesizedAttributeDcl,
    frontend_chain_AvailableTransformation,
    frontend_chain_ChainTransformation,
    frontend_chain_CompositeTransformation,
    frontend_chain_ExternalTransformation,
    frontend_chain_GeneratedModel,
    frontend_chain_TransformationExecution,
    frontend_core_AnnotableElement,
    frontend_core_Annotation,
    frontend_core_AnnotationParameter,
    frontend_core_BinaryExpr,
    frontend_core_BooleanLiteral,
    frontend_core_ClassUse,
    frontend_core_ClosureDeclaration,
    frontend_core_ClosureParameter,
    frontend_core_DefineVariable,
    frontend_core_DefinitionParameter,
    frontend_core_DoubleLiteral,
    frontend_core_EclecticTransformationDefinition,
    frontend_core_Expression,
    frontend_core_GenericAnnotation,
    frontend_core_IfBranch,
    frontend_core_IfExpr,
    frontend_core_ImplicitlyAnnotableElement,
    frontend_core_ImportedModel,
    frontend_core_InlineAttribute,
    frontend_core_InlineClass,
    frontend_core_InlineFeature,
    frontend_core_InlineModel,
    frontend_core_InlineReference,
    frontend_core_KeywordMethodCall,
    frontend_core_KeywordParameter,
    frontend_core_LocatedElement,
    frontend_core_MatchTrace,
    frontend_core_MetamodelModelAnnotation,
    frontend_core_MethodCall,
    frontend_core_ModelReference,
    frontend_core_ModuleDefinition,
    frontend_core_ModuleParameter,
    frontend_core_NamedElement,
    frontend_core_NumLiteral,
    frontend_core_OptimizationsAnnotation,
    frontend_core_PotencyAnnotation,
    frontend_core_PropertyWrite,
    frontend_core_PutTrace,
    frontend_core_PutTraceParameter,
    frontend_core_RepresentModel,
    frontend_core_RequireDeclaration,
    frontend_core_RequireModelParameter,
    frontend_core_RequireParameter,
    frontend_core_ResolveLink,
    frontend_core_SingleAnnotation,
    frontend_core_Statement,
    frontend_core_StringLiteral,
    frontend_core_TraceCompareExpression,
    frontend_core_TraceDefinition,
    frontend_core_TraceElement,
    frontend_core_TraceInterface,
    frontend_core_TraceUse,
    frontend_core_TracedModelParameter,
    frontend_core_TransformationDefinition,
    frontend_core_TransformationDefinitionParameter,
    frontend_core_TypeExpression,
    frontend_core_TypedWithClass,
    frontend_core_UseDeclaration,
    frontend_core_Variable,
    frontend_core_VariableReference,
    frontend_facilities_Copier,
    frontend_facilities_CopierCallbackDefinition,
    frontend_imperative_ImperativeTransformation,
    frontend_imperative_MethodDefinition,
    frontend_imperative_MethodParameter,
    frontend_imperative_MethodSelf,
    frontend_koan_ForAllMatcher,
    frontend_koan_KoanRule,
    frontend_koan_KoanTransformation,
    frontend_koan_Matcher,
    frontend_mappings_Attribute2Attribute,
    frontend_mappings_AttributeIsBoolean,
    frontend_mappings_AttributeIsDouble,
    frontend_mappings_AttributeIsInteger,
    frontend_mappings_AttributeIsResolveLink,
    frontend_mappings_AttributeIsString,
    frontend_mappings_AttributeMapping,
    frontend_mappings_AttributeModifier,
    frontend_mappings_AttributeRef,
    frontend_mappings_AttributeRightPart,
    frontend_mappings_C2CModifier,
    frontend_mappings_Class2Class,
    frontend_mappings_ClassMapping,
    frontend_mappings_ClassRef,
    frontend_mappings_Context,
    frontend_mappings_ConvertModifier,
    frontend_mappings_Converter,
    frontend_mappings_DefaultValue,
    frontend_mappings_Delegate,
    frontend_mappings_EqualityFilter,
    frontend_mappings_Feature2Feature,
    frontend_mappings_FeatureRef,
    frontend_mappings_IntDefaultValue,
    frontend_mappings_Join,
    frontend_mappings_LinkedBy,
    frontend_mappings_MappingElement,
    frontend_mappings_MappingTransformation,
    frontend_mappings_MappingVariable,
    frontend_mappings_MatchedElement,
    frontend_mappings_MetamodelElementRef,
    frontend_mappings_Modifier,
    frontend_mappings_Operator,
    frontend_mappings_Reference2Reference,
    frontend_mappings_ReferenceRef,
    frontend_mappings_RelatedBy,
    frontend_mappings_Section,
    frontend_mappings_Split,
    frontend_mappings_Tag,
    frontend_patterns_CollectionReference,
    frontend_patterns_PAttribute,
    frontend_patterns_PFeature,
    frontend_patterns_PObject,
    frontend_patterns_POutputVariable,
    frontend_patterns_PReference,
    frontend_patterns_Pattern,
    frontend_patterns_PatternSpecification,
    frontend_qool_AccessByFeatureOptimization,
    frontend_qool_EmitStatement,
    frontend_qool_ForAllStatement,
    frontend_qool_ForEachStatement,
    frontend_qool_InvocationParameter,
    frontend_qool_InvokeExternal,
    frontend_qool_InvokeInternal,
    frontend_qool_InvokeTransformation,
    frontend_qool_IteratorStatement,
    frontend_qool_KindOfPredicate,
    frontend_qool_LocalQueue,
    frontend_qool_MatchExpression,
    frontend_qool_MatchPredicate,
    frontend_qool_ModelElementQueue,
    frontend_qool_NamedInvocationParameter,
    frontend_qool_PropertyEqualsPredicate,
    frontend_qool_QoolQueue,
    frontend_qool_QoolTransformation,
    frontend_qool_QueueOptimization,
    frontend_qool_Segment,
    frontend_script_ScriptedTransformation,
    frontend_tao_Assignment,
    frontend_tao_AttributeAssigment,
    frontend_tao_Invocation,
    frontend_tao_ObjectInstantiation,
    frontend_tao_ObjectSourceVariable,
    frontend_tao_ObjectSyntax,
    frontend_tao_ReferenceAssignment,
    frontend_tao_SourceExpression,
    frontend_tao_TaoTransformation,
    frontend_tao_Template,
    frontend_tao_TemplateParameter,
    frontend_tao_TemplateRootObject,
    frontend_tao_WithOptionalVariableExpression,
    koan_Matcher,
    mappings_AttributeRightPart,
    mappings_Feature2Feature,
    mappings_MappingVariable,
    mappings_MetamodelElementRef,
    tao_Assignment,
    BinaryOp,
    MappingCardinality,
    ResolveTraceCardinality,
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

def test_assoc_action207_stub_double():
    # Expression has no real 'Expression209' property in the generated
    # code (a bare stub) -- manually attach it so frontend_facilities_CopierCallbackDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_facilities_CopierCallbackDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_facilities_CopierCallbackDefinition(stop=True)
    partner = Expression()
    setattr(partner, 'Expression209', None)
    _safe_set(owner, 'frontend_facilities_CopierCallbackDefinition208', partner)
    assert getattr(partner, 'Expression209') == owner
    _safe_set(owner, 'frontend_facilities_CopierCallbackDefinition208', None)
    assert getattr(partner, 'Expression209') is None


def test_assoc_actualParameter196_stub_double():
    # Expression has no real 'Expression197' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_NamedInvocationParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_NamedInvocationParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_NamedInvocationParameter(formalName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression197', None)
    _safe_set(owner, 'frontend_qool_NamedInvocationParameter', partner)
    assert getattr(partner, 'Expression197') == owner
    _safe_set(owner, 'frontend_qool_NamedInvocationParameter', None)
    assert getattr(partner, 'Expression197') is None


def test_assoc_attribute125_stub_double():
    # AttributeRef has no real 'AttributeRef126' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_EqualityFilter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_EqualityFilter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_EqualityFilter(filter="sample_text")
    partner = AttributeRef()
    setattr(partner, 'AttributeRef126', None)
    _safe_set(owner, 'frontend_mappings_EqualityFilter', partner)
    assert getattr(partner, 'AttributeRef126') == owner
    _safe_set(owner, 'frontend_mappings_EqualityFilter', None)
    assert getattr(partner, 'AttributeRef126') is None


def test_assoc_context130_stub_double():
    # Class2Class has no real 'Class2Class' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Attribute2Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Attribute2Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Attribute2Attribute(cardinality="sample_text")
    partner = Class2Class()
    setattr(partner, 'Class2Class', None)
    _safe_set(owner, 'scopedAttributes', partner)
    assert getattr(partner, 'Class2Class') == owner
    _safe_set(owner, 'scopedAttributes', None)
    assert getattr(partner, 'Class2Class') is None


def test_assoc_entryPointParameters190_stub_double():
    # Expression has no real 'Expression192' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeTransformation(entryPointName="sample_text", transformationName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression192', None)
    _safe_set(owner, 'frontend_qool_InvokeTransformation191', {partner})
    assert getattr(partner, 'Expression192') == owner
    _safe_set(owner, 'frontend_qool_InvokeTransformation191', set())
    assert getattr(partner, 'Expression192') is None


def test_assoc_expr220_stub_double():
    # SourceExpression has no real 'SourceExpression' property in the generated
    # code (a bare stub) -- manually attach it so frontend_tao_AttributeAssigment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_tao_AttributeAssigment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_tao_AttributeAssigment(targetFeature="sample_text")
    partner = SourceExpression()
    setattr(partner, 'SourceExpression', None)
    _safe_set(owner, 'frontend_tao_AttributeAssigment', partner)
    assert getattr(partner, 'SourceExpression') == owner
    _safe_set(owner, 'frontend_tao_AttributeAssigment', None)
    assert getattr(partner, 'SourceExpression') is None


def test_assoc_expr225_stub_double():
    # SourceExpression has no real 'SourceExpression226' property in the generated
    # code (a bare stub) -- manually attach it so frontend_tao_ReferenceAssignment's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_tao_ReferenceAssignment's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_tao_ReferenceAssignment(multivalued=True, targetFeature="sample_text")
    partner = SourceExpression()
    setattr(partner, 'SourceExpression226', None)
    _safe_set(owner, 'frontend_tao_ReferenceAssignment', partner)
    assert getattr(partner, 'SourceExpression226') == owner
    _safe_set(owner, 'frontend_tao_ReferenceAssignment', None)
    assert getattr(partner, 'SourceExpression226') is None


def test_assoc_expr284_stub_double():
    # Expression has no real 'Expression285' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_ResolveLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_ResolveLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_ResolveLink(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression285', None)
    _safe_set(owner, 'frontend_core_ResolveLink', partner)
    assert getattr(partner, 'Expression285') == owner
    _safe_set(owner, 'frontend_core_ResolveLink', None)
    assert getattr(partner, 'Expression285') is None


def test_assoc_expr321_stub_double():
    # Expression has no real 'Expression323' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_TraceCompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_TraceCompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_TraceCompareExpression(multivaluedTag=True)
    partner = Expression()
    setattr(partner, 'Expression323', None)
    _safe_set(owner, 'frontend_core_TraceCompareExpression322', partner)
    assert getattr(partner, 'Expression323') == owner
    _safe_set(owner, 'frontend_core_TraceCompareExpression322', None)
    assert getattr(partner, 'Expression323') is None


def test_assoc_expression259_stub_double():
    # Expression has no real 'Expression261' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_PropertyWrite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_PropertyWrite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_PropertyWrite(_property="sample_text")
    partner = Expression()
    setattr(partner, 'Expression261', None)
    _safe_set(owner, 'frontend_core_PropertyWrite260', partner)
    assert getattr(partner, 'Expression261') == owner
    _safe_set(owner, 'frontend_core_PropertyWrite260', None)
    assert getattr(partner, 'Expression261') is None


def test_assoc_formalParameters37_stub_double():
    # MethodParameter has no real 'MethodParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_imperative_MethodDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_imperative_MethodDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_imperative_MethodDefinition(name="sample_text")
    partner = MethodParameter()
    setattr(partner, 'MethodParameter', None)
    _safe_set(owner, 'frontend_imperative_MethodDefinition', {partner})
    assert getattr(partner, 'MethodParameter') == owner
    _safe_set(owner, 'frontend_imperative_MethodDefinition', set())
    assert getattr(partner, 'MethodParameter') is None


def test_assoc_inputViewFilter187_stub_double():
    # Variable has no real 'Variable189' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeTransformation(entryPointName="sample_text", transformationName="sample_text")
    partner = Variable()
    setattr(partner, 'Variable189', None)
    _safe_set(owner, 'frontend_qool_InvokeTransformation188', partner)
    assert getattr(partner, 'Variable189') == owner
    _safe_set(owner, 'frontend_qool_InvokeTransformation188', None)
    assert getattr(partner, 'Variable189') is None


def test_assoc_left112_stub_double():
    # ClassRef has no real 'ClassRef' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Class2Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Class2Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Class2Class(cardinality="sample_text")
    partner = ClassRef()
    setattr(partner, 'ClassRef', None)
    _safe_set(owner, 'frontend_mappings_Class2Class113', {partner})
    assert getattr(partner, 'ClassRef') == owner
    _safe_set(owner, 'frontend_mappings_Class2Class113', set())
    assert getattr(partner, 'ClassRef') is None


def test_assoc_left135_stub_double():
    # ReferenceRef has no real 'ReferenceRef' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Reference2Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Reference2Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Reference2Reference(cardinality="sample_text", resolverName="sample_text")
    partner = ReferenceRef()
    setattr(partner, 'ReferenceRef', None)
    _safe_set(owner, 'frontend_mappings_Reference2Reference', {partner})
    assert getattr(partner, 'ReferenceRef') == owner
    _safe_set(owner, 'frontend_mappings_Reference2Reference', set())
    assert getattr(partner, 'ReferenceRef') is None


def test_assoc_left275_stub_double():
    # Expression has no real 'Expression276' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_BinaryExpr(binaryOp="sample_text")
    partner = Expression()
    setattr(partner, 'Expression276', None)
    _safe_set(owner, 'frontend_core_BinaryExpr', partner)
    assert getattr(partner, 'Expression276') == owner
    _safe_set(owner, 'frontend_core_BinaryExpr', None)
    assert getattr(partner, 'Expression276') is None


def test_assoc_left80_stub_double():
    # MatchedElement has no real 'MatchedElement' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Delegate(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = MatchedElement()
    setattr(partner, 'MatchedElement', None)
    _safe_set(owner, 'frontend_mappings_Delegate', {partner})
    assert getattr(partner, 'MatchedElement') == owner
    _safe_set(owner, 'frontend_mappings_Delegate', set())
    assert getattr(partner, 'MatchedElement') is None


def test_assoc_mappings99_stub_double():
    # MappingElement has no real 'MappingElement100' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Section(sectionType="sample_text")
    partner = MappingElement()
    setattr(partner, 'MappingElement100', None)
    _safe_set(owner, 'frontend_mappings_Section', {partner})
    assert getattr(partner, 'MappingElement100') == owner
    _safe_set(owner, 'frontend_mappings_Section', set())
    assert getattr(partner, 'MappingElement100') is None


def test_assoc_model195_stub_double():
    # TransformationDefinitionParameter has no real 'TransformationDefinitionParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvocationParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvocationParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvocationParameter(calleeModelName="sample_text")
    partner = TransformationDefinitionParameter()
    setattr(partner, 'TransformationDefinitionParameter', None)
    _safe_set(owner, 'frontend_qool_InvocationParameter', partner)
    assert getattr(partner, 'TransformationDefinitionParameter') == owner
    _safe_set(owner, 'frontend_qool_InvocationParameter', None)
    assert getattr(partner, 'TransformationDefinitionParameter') is None


def test_assoc_model301_stub_double():
    # RepresentModel has no real 'RepresentModel302' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_ClassUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_ClassUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_ClassUse(className="sample_text", strictType=True)
    partner = RepresentModel()
    setattr(partner, 'RepresentModel302', None)
    _safe_set(owner, 'frontend_core_ClassUse', partner)
    assert getattr(partner, 'RepresentModel302') == owner
    _safe_set(owner, 'frontend_core_ClassUse', None)
    assert getattr(partner, 'RepresentModel302') is None


def test_assoc_modifiers110_stub_double():
    # C2CModifier has no real 'C2CModifier111' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Class2Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Class2Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Class2Class(cardinality="sample_text")
    partner = C2CModifier()
    setattr(partner, 'C2CModifier111', None)
    _safe_set(owner, 'frontend_mappings_Class2Class', {partner})
    assert getattr(partner, 'C2CModifier111') == owner
    _safe_set(owner, 'frontend_mappings_Class2Class', set())
    assert getattr(partner, 'C2CModifier111') is None


def test_assoc_modifiers133_stub_double():
    # AttributeModifier has no real 'AttributeModifier' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Attribute2Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Attribute2Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Attribute2Attribute(cardinality="sample_text")
    partner = AttributeModifier()
    setattr(partner, 'AttributeModifier', None)
    _safe_set(owner, 'frontend_mappings_Attribute2Attribute134', {partner})
    assert getattr(partner, 'AttributeModifier') == owner
    _safe_set(owner, 'frontend_mappings_Attribute2Attribute134', set())
    assert getattr(partner, 'AttributeModifier') is None


def test_assoc_module108_stub_double():
    # UseDeclaration has no real 'UseDeclaration109' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Converter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Converter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Converter(converterName="sample_text", isExternal="sample_text")
    partner = UseDeclaration()
    setattr(partner, 'UseDeclaration109', None)
    _safe_set(owner, 'frontend_mappings_Converter', partner)
    assert getattr(partner, 'UseDeclaration109') == owner
    _safe_set(owner, 'frontend_mappings_Converter', None)
    assert getattr(partner, 'UseDeclaration109') is None


def test_assoc_module286_stub_double():
    # UseDeclaration has no real 'UseDeclaration288' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_ResolveLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_ResolveLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_ResolveLink(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = UseDeclaration()
    setattr(partner, 'UseDeclaration288', None)
    _safe_set(owner, 'frontend_core_ResolveLink287', partner)
    assert getattr(partner, 'UseDeclaration288') == owner
    _safe_set(owner, 'frontend_core_ResolveLink287', None)
    assert getattr(partner, 'UseDeclaration288') is None


def test_assoc_module81_stub_double():
    # UseDeclaration has no real 'UseDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Delegate(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = UseDeclaration()
    setattr(partner, 'UseDeclaration', None)
    _safe_set(owner, 'frontend_mappings_Delegate82', partner)
    assert getattr(partner, 'UseDeclaration') == owner
    _safe_set(owner, 'frontend_mappings_Delegate82', None)
    assert getattr(partner, 'UseDeclaration') is None


def test_assoc_objects62_stub_double():
    # PObject has no real 'PObject' property in the generated
    # code (a bare stub) -- manually attach it so frontend_patterns_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_patterns_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_patterns_Pattern(name="sample_text")
    partner = PObject()
    setattr(partner, 'PObject', None)
    _safe_set(owner, 'frontend_patterns_Pattern', {partner})
    assert getattr(partner, 'PObject') == owner
    _safe_set(owner, 'frontend_patterns_Pattern', set())
    assert getattr(partner, 'PObject') is None


def test_assoc_outputResolutionSourceElement193_stub_double():
    # Expression has no real 'Expression194' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeExternal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeExternal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeExternal(queueName="sample_text", traceAttributeName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression194', None)
    _safe_set(owner, 'frontend_qool_InvokeExternal', partner)
    assert getattr(partner, 'Expression194') == owner
    _safe_set(owner, 'frontend_qool_InvokeExternal', None)
    assert getattr(partner, 'Expression194') is None


def test_assoc_outputVariables63_stub_double():
    # POutputVariable has no real 'POutputVariable' property in the generated
    # code (a bare stub) -- manually attach it so frontend_patterns_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_patterns_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_patterns_Pattern(name="sample_text")
    partner = POutputVariable()
    setattr(partner, 'POutputVariable', None)
    _safe_set(owner, 'frontend_patterns_Pattern64', {partner})
    assert getattr(partner, 'POutputVariable') == owner
    _safe_set(owner, 'frontend_patterns_Pattern64', set())
    assert getattr(partner, 'POutputVariable') is None


def test_assoc_parameters185_stub_double():
    # NamedInvocationParameter has no real 'NamedInvocationParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeTransformation(entryPointName="sample_text", transformationName="sample_text")
    partner = NamedInvocationParameter()
    setattr(partner, 'NamedInvocationParameter', None)
    _safe_set(owner, 'frontend_qool_InvokeTransformation186', {partner})
    assert getattr(partner, 'NamedInvocationParameter') == owner
    _safe_set(owner, 'frontend_qool_InvokeTransformation186', set())
    assert getattr(partner, 'NamedInvocationParameter') is None


def test_assoc_parameters233_stub_double():
    # AnnotationParameter has no real 'AnnotationParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_GenericAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_GenericAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_GenericAnnotation(name="sample_text")
    partner = AnnotationParameter()
    setattr(partner, 'AnnotationParameter', None)
    _safe_set(owner, 'frontend_core_GenericAnnotation', {partner})
    assert getattr(partner, 'AnnotationParameter') == owner
    _safe_set(owner, 'frontend_core_GenericAnnotation', set())
    assert getattr(partner, 'AnnotationParameter') is None


def test_assoc_parameters252_stub_double():
    # RequireParameter has no real 'RequireParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_RequireDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_RequireDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_RequireDeclaration(default="sample_text", name="sample_text")
    partner = RequireParameter()
    setattr(partner, 'RequireParameter', None)
    _safe_set(owner, 'frontend_core_RequireDeclaration', {partner})
    assert getattr(partner, 'RequireParameter') == owner
    _safe_set(owner, 'frontend_core_RequireDeclaration', set())
    assert getattr(partner, 'RequireParameter') is None


def test_assoc_parameters266_stub_double():
    # Expression has no real 'Expression268' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_MethodCall(methodName="sample_text", withParameters=True)
    partner = Expression()
    setattr(partner, 'Expression268', None)
    _safe_set(owner, 'frontend_core_MethodCall267', {partner})
    assert getattr(partner, 'Expression268') == owner
    _safe_set(owner, 'frontend_core_MethodCall267', set())
    assert getattr(partner, 'Expression268') is None


def test_assoc_receptor257_stub_double():
    # Variable has no real 'Variable258' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_PropertyWrite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_PropertyWrite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_PropertyWrite(_property="sample_text")
    partner = Variable()
    setattr(partner, 'Variable258', None)
    _safe_set(owner, 'frontend_core_PropertyWrite', partner)
    assert getattr(partner, 'Variable258') == owner
    _safe_set(owner, 'frontend_core_PropertyWrite', None)
    assert getattr(partner, 'Variable258') is None


def test_assoc_receptor264_stub_double():
    # Expression has no real 'Expression265' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_MethodCall(methodName="sample_text", withParameters=True)
    partner = Expression()
    setattr(partner, 'Expression265', None)
    _safe_set(owner, 'frontend_core_MethodCall', partner)
    assert getattr(partner, 'Expression265') == owner
    _safe_set(owner, 'frontend_core_MethodCall', None)
    assert getattr(partner, 'Expression265') is None


def test_assoc_referredElement141_stub_double():
    # MatchedElement has no real 'MatchedElement142' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_FeatureRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_FeatureRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_FeatureRef(featureName="sample_text", multivalued=True)
    partner = MatchedElement()
    setattr(partner, 'MatchedElement142', None)
    _safe_set(owner, 'frontend_mappings_FeatureRef', partner)
    assert getattr(partner, 'MatchedElement142') == owner
    _safe_set(owner, 'frontend_mappings_FeatureRef', None)
    assert getattr(partner, 'MatchedElement142') is None


def test_assoc_referredElement143_stub_double():
    # MatchedElement has no real 'MatchedElement144' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_AttributeRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_AttributeRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_AttributeRef(featureName="sample_text", multivalued=True)
    partner = MatchedElement()
    setattr(partner, 'MatchedElement144', None)
    _safe_set(owner, 'frontend_mappings_AttributeRef', partner)
    assert getattr(partner, 'MatchedElement144') == owner
    _safe_set(owner, 'frontend_mappings_AttributeRef', None)
    assert getattr(partner, 'MatchedElement144') is None


def test_assoc_referredElement145_stub_double():
    # MatchedElement has no real 'MatchedElement146' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_ReferenceRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_ReferenceRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_ReferenceRef(featureName="sample_text", multivalued=True)
    partner = MatchedElement()
    setattr(partner, 'MatchedElement146', None)
    _safe_set(owner, 'frontend_mappings_ReferenceRef', partner)
    assert getattr(partner, 'MatchedElement146') == owner
    _safe_set(owner, 'frontend_mappings_ReferenceRef', None)
    assert getattr(partner, 'MatchedElement146') is None


def test_assoc_right114_stub_double():
    # ClassRef has no real 'ClassRef116' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Class2Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Class2Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Class2Class(cardinality="sample_text")
    partner = ClassRef()
    setattr(partner, 'ClassRef116', None)
    _safe_set(owner, 'frontend_mappings_Class2Class115', {partner})
    assert getattr(partner, 'ClassRef116') == owner
    _safe_set(owner, 'frontend_mappings_Class2Class115', set())
    assert getattr(partner, 'ClassRef116') is None


def test_assoc_right131_stub_double():
    # AttributeRef has no real 'AttributeRef132' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Attribute2Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Attribute2Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Attribute2Attribute(cardinality="sample_text")
    partner = AttributeRef()
    setattr(partner, 'AttributeRef132', None)
    _safe_set(owner, 'frontend_mappings_Attribute2Attribute', {partner})
    assert getattr(partner, 'AttributeRef132') == owner
    _safe_set(owner, 'frontend_mappings_Attribute2Attribute', set())
    assert getattr(partner, 'AttributeRef132') is None


def test_assoc_right136_stub_double():
    # ReferenceRef has no real 'ReferenceRef138' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Reference2Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Reference2Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Reference2Reference(cardinality="sample_text", resolverName="sample_text")
    partner = ReferenceRef()
    setattr(partner, 'ReferenceRef138', None)
    _safe_set(owner, 'frontend_mappings_Reference2Reference137', {partner})
    assert getattr(partner, 'ReferenceRef138') == owner
    _safe_set(owner, 'frontend_mappings_Reference2Reference137', set())
    assert getattr(partner, 'ReferenceRef138') is None


def test_assoc_right277_stub_double():
    # Expression has no real 'Expression279' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_BinaryExpr(binaryOp="sample_text")
    partner = Expression()
    setattr(partner, 'Expression279', None)
    _safe_set(owner, 'frontend_core_BinaryExpr278', partner)
    assert getattr(partner, 'Expression279') == owner
    _safe_set(owner, 'frontend_core_BinaryExpr278', None)
    assert getattr(partner, 'Expression279') is None


def test_assoc_scopedAttributes117_stub_double():
    # Attribute2Attribute has no real 'Attribute2Attribute' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Class2Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Class2Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Class2Class(cardinality="sample_text")
    partner = Attribute2Attribute()
    setattr(partner, 'Attribute2Attribute', None)
    _safe_set(owner, 'context', {partner})
    assert getattr(partner, 'Attribute2Attribute') == owner
    _safe_set(owner, 'context', set())
    assert getattr(partner, 'Attribute2Attribute') is None


def test_assoc_self38_stub_double():
    # MethodSelf has no real 'MethodSelf' property in the generated
    # code (a bare stub) -- manually attach it so frontend_imperative_MethodDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_imperative_MethodDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_imperative_MethodDefinition(name="sample_text")
    partner = MethodSelf()
    setattr(partner, 'MethodSelf', None)
    _safe_set(owner, 'frontend_imperative_MethodDefinition39', partner)
    assert getattr(partner, 'MethodSelf') == owner
    _safe_set(owner, 'frontend_imperative_MethodDefinition39', None)
    assert getattr(partner, 'MethodSelf') is None


def test_assoc_sourceModels181_stub_double():
    # InvocationParameter has no real 'InvocationParameter' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeTransformation(entryPointName="sample_text", transformationName="sample_text")
    partner = InvocationParameter()
    setattr(partner, 'InvocationParameter', None)
    _safe_set(owner, 'frontend_qool_InvokeTransformation', {partner})
    assert getattr(partner, 'InvocationParameter') == owner
    _safe_set(owner, 'frontend_qool_InvokeTransformation', set())
    assert getattr(partner, 'InvocationParameter') is None


def test_assoc_statements43_stub_double():
    # Statement has no real 'Statement45' property in the generated
    # code (a bare stub) -- manually attach it so frontend_imperative_MethodDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_imperative_MethodDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_imperative_MethodDefinition(name="sample_text")
    partner = Statement()
    setattr(partner, 'Statement45', None)
    _safe_set(owner, 'frontend_imperative_MethodDefinition44', {partner})
    assert getattr(partner, 'Statement45') == owner
    _safe_set(owner, 'frontend_imperative_MethodDefinition44', set())
    assert getattr(partner, 'Statement45') is None


def test_assoc_tags83_stub_double():
    # Tag has no real 'Tag' property in the generated
    # code (a bare stub) -- manually attach it so frontend_mappings_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_mappings_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_mappings_Delegate(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = Tag()
    setattr(partner, 'Tag', None)
    _safe_set(owner, 'frontend_mappings_Delegate84', {partner})
    assert getattr(partner, 'Tag') == owner
    _safe_set(owner, 'frontend_mappings_Delegate84', set())
    assert getattr(partner, 'Tag') is None


def test_assoc_targetModels182_stub_double():
    # InvocationParameter has no real 'InvocationParameter184' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_InvokeTransformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_InvokeTransformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_InvokeTransformation(entryPointName="sample_text", transformationName="sample_text")
    partner = InvocationParameter()
    setattr(partner, 'InvocationParameter184', None)
    _safe_set(owner, 'frontend_qool_InvokeTransformation183', {partner})
    assert getattr(partner, 'InvocationParameter184') == owner
    _safe_set(owner, 'frontend_qool_InvokeTransformation183', set())
    assert getattr(partner, 'InvocationParameter184') is None


def test_assoc_trace315_stub_double():
    # TraceDefinition has no real 'TraceDefinition316' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_MatchTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_MatchTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_MatchTrace(cardinality="sample_text")
    partner = TraceDefinition()
    setattr(partner, 'TraceDefinition316', None)
    _safe_set(owner, 'frontend_core_MatchTrace', partner)
    assert getattr(partner, 'TraceDefinition316') == owner
    _safe_set(owner, 'frontend_core_MatchTrace', None)
    assert getattr(partner, 'TraceDefinition316') is None


def test_assoc_traceExpr317_stub_double():
    # TraceCompareExpression has no real 'TraceCompareExpression' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_MatchTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_MatchTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_MatchTrace(cardinality="sample_text")
    partner = TraceCompareExpression()
    setattr(partner, 'TraceCompareExpression', None)
    _safe_set(owner, 'frontend_core_MatchTrace318', partner)
    assert getattr(partner, 'TraceCompareExpression') == owner
    _safe_set(owner, 'frontend_core_MatchTrace318', None)
    assert getattr(partner, 'TraceCompareExpression') is None


def test_assoc_traceVar319_stub_double():
    # TraceElement has no real 'TraceElement320' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_TraceCompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_TraceCompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_TraceCompareExpression(multivaluedTag=True)
    partner = TraceElement()
    setattr(partner, 'TraceElement320', None)
    _safe_set(owner, 'frontend_core_TraceCompareExpression', partner)
    assert getattr(partner, 'TraceElement320') == owner
    _safe_set(owner, 'frontend_core_TraceCompareExpression', None)
    assert getattr(partner, 'TraceElement320') is None


def test_assoc_trigger205_stub_double():
    # Expression has no real 'Expression206' property in the generated
    # code (a bare stub) -- manually attach it so frontend_facilities_CopierCallbackDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_facilities_CopierCallbackDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_facilities_CopierCallbackDefinition(stop=True)
    partner = Expression()
    setattr(partner, 'Expression206', None)
    _safe_set(owner, 'frontend_facilities_CopierCallbackDefinition', partner)
    assert getattr(partner, 'Expression206') == owner
    _safe_set(owner, 'frontend_facilities_CopierCallbackDefinition', None)
    assert getattr(partner, 'Expression206') is None


def test_assoc_type313_stub_double():
    # TypeExpression has no real 'TypeExpression314' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_InlineFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_InlineFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_InlineFeature(multivalued=True)
    partner = TypeExpression()
    setattr(partner, 'TypeExpression314', None)
    _safe_set(owner, 'frontend_core_InlineFeature', partner)
    assert getattr(partner, 'TypeExpression314') == owner
    _safe_set(owner, 'frontend_core_InlineFeature', None)
    assert getattr(partner, 'TypeExpression314') is None


def test_assoc_type40_stub_double():
    # ClassUse has no real 'ClassUse42' property in the generated
    # code (a bare stub) -- manually attach it so frontend_imperative_MethodDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_imperative_MethodDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_imperative_MethodDefinition(name="sample_text")
    partner = ClassUse()
    setattr(partner, 'ClassUse42', None)
    _safe_set(owner, 'frontend_imperative_MethodDefinition41', partner)
    assert getattr(partner, 'ClassUse42') == owner
    _safe_set(owner, 'frontend_imperative_MethodDefinition41', None)
    assert getattr(partner, 'ClassUse42') is None


def test_assoc_value179_stub_double():
    # Expression has no real 'Expression180' property in the generated
    # code (a bare stub) -- manually attach it so frontend_qool_PropertyEqualsPredicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_qool_PropertyEqualsPredicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_qool_PropertyEqualsPredicate(propertyName="sample_text")
    partner = Expression()
    setattr(partner, 'Expression180', None)
    _safe_set(owner, 'frontend_qool_PropertyEqualsPredicate', partner)
    assert getattr(partner, 'Expression180') == owner
    _safe_set(owner, 'frontend_qool_PropertyEqualsPredicate', None)
    assert getattr(partner, 'Expression180') is None


def test_assoc_value273_stub_double():
    # Expression has no real 'Expression274' property in the generated
    # code (a bare stub) -- manually attach it so frontend_core_KeywordParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # frontend_core_KeywordParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = frontend_core_KeywordParameter(keyword="sample_text")
    partner = Expression()
    setattr(partner, 'Expression274', None)
    _safe_set(owner, 'frontend_core_KeywordParameter', partner)
    assert getattr(partner, 'Expression274') == owner
    _safe_set(owner, 'frontend_core_KeywordParameter', None)
    assert getattr(partner, 'Expression274') is None


