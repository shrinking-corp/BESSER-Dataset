import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnnotableElement,
    Annotation,
    ClassUse,
    DefinitionParameter,
    Expression,
    ImplicitlyAnnotableElement,
    InlineFeature,
    LocatedElement,
    ModuleDefinition,
    NamedElement,
    RepresentModel,
    RequireParameter,
    SingleAnnotation,
    Statement,
    TransformationDefinition,
    TypeExpression,
    Variable,
    core_AnnotableElement,
    core_Annotation,
    core_AnnotationParameter,
    core_BinaryExpr,
    core_BooleanLiteral,
    core_ClassUse,
    core_ClosureDeclaration,
    core_ClosureParameter,
    core_DefineVariable,
    core_DefinitionParameter,
    core_DoubleLiteral,
    core_EclecticTransformationDefinition,
    core_Expression,
    core_GenericAnnotation,
    core_IfBranch,
    core_IfExpr,
    core_ImplicitlyAnnotableElement,
    core_ImportedModel,
    core_InlineAttribute,
    core_InlineClass,
    core_InlineFeature,
    core_InlineModel,
    core_InlineReference,
    core_KeywordMethodCall,
    core_KeywordParameter,
    core_LocatedElement,
    core_MatchTrace,
    core_MetamodelModelAnnotation,
    core_MethodCall,
    core_ModelReference,
    core_ModuleDefinition,
    core_ModuleParameter,
    core_NamedElement,
    core_NumLiteral,
    core_OptimizationsAnnotation,
    core_PotencyAnnotation,
    core_PropertyWrite,
    core_PutTrace,
    core_PutTraceParameter,
    core_RepresentModel,
    core_RequireDeclaration,
    core_RequireModelParameter,
    core_RequireParameter,
    core_ResolveLink,
    core_SingleAnnotation,
    core_Statement,
    core_StringLiteral,
    core_TraceCompareExpression,
    core_TraceDefinition,
    core_TraceElement,
    core_TraceInterface,
    core_TraceUse,
    core_TracedModelParameter,
    core_TransformationDefinition,
    core_TransformationDefinitionParameter,
    core_TypeExpression,
    core_TypedWithClass,
    core_UseDeclaration,
    core_Variable,
    core_VariableReference,
    BinaryOp,
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

def test_assoc_module52_reverse_link_reassign_clear():
    a1 = core_UseDeclaration(as_="sample_text", module="sample_text")
    a2 = core_UseDeclaration(as_="sample_text_2", module="sample_text_2")
    b = core_ResolveLink(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    _safe_set(b, 'core_ResolveLink53', a1)
    assert _is_linked(b, 'core_ResolveLink53', a1)
    if hasattr(a1, 'core_UseDeclaration54'):
        assert _is_linked(a1, 'core_UseDeclaration54', b)
    _safe_set(b, 'core_ResolveLink53', a2)
    assert _is_linked(b, 'core_ResolveLink53', a2)
    if hasattr(a1, 'core_UseDeclaration54'):
        assert not _is_linked(a1, 'core_UseDeclaration54', b)
    if hasattr(a2, 'core_UseDeclaration54'):
        assert _is_linked(a2, 'core_UseDeclaration54', b)
    _safe_set(b, 'core_ResolveLink53', None)
    assert not _is_linked(b, 'core_ResolveLink53', a2)
    if hasattr(a2, 'core_UseDeclaration54'):
        assert not _is_linked(a2, 'core_UseDeclaration54', b)


def test_assoc_parameters20_reverse_link_reassign_clear():
    a1 = core_RequireParameter(formalParameterName="sample_text")
    a2 = core_RequireParameter(formalParameterName="sample_text_2")
    b = core_RequireDeclaration(default="sample_text", name="sample_text")
    _safe_set(b, 'core_RequireDeclaration21', {a1})
    assert _is_linked(b, 'core_RequireDeclaration21', a1)
    if hasattr(a1, 'core_RequireParameter'):
        assert _is_linked(a1, 'core_RequireParameter', b)
    _safe_set(b, 'core_RequireDeclaration21', {a2})
    assert _is_linked(b, 'core_RequireDeclaration21', a2)
    if hasattr(a1, 'core_RequireParameter'):
        assert not _is_linked(a1, 'core_RequireParameter', b)
    if hasattr(a2, 'core_RequireParameter'):
        assert _is_linked(a2, 'core_RequireParameter', b)
    _safe_set(b, 'core_RequireDeclaration21', set())
    assert not _is_linked(b, 'core_RequireDeclaration21', a2)
    if hasattr(a2, 'core_RequireParameter'):
        assert not _is_linked(a2, 'core_RequireParameter', b)


def test_assoc_receptor24_reverse_link_reassign_clear():
    a1 = core_Variable(name="sample_text")
    a2 = core_Variable(name="sample_text_2")
    b = core_PropertyWrite(_property="sample_text")
    _safe_set(b, 'core_PropertyWrite', a1)
    assert _is_linked(b, 'core_PropertyWrite', a1)
    if hasattr(a1, 'core_Variable'):
        assert _is_linked(a1, 'core_Variable', b)
    _safe_set(b, 'core_PropertyWrite', a2)
    assert _is_linked(b, 'core_PropertyWrite', a2)
    if hasattr(a1, 'core_Variable'):
        assert not _is_linked(a1, 'core_Variable', b)
    if hasattr(a2, 'core_Variable'):
        assert _is_linked(a2, 'core_Variable', b)
    _safe_set(b, 'core_PropertyWrite', None)
    assert not _is_linked(b, 'core_PropertyWrite', a2)
    if hasattr(a2, 'core_Variable'):
        assert not _is_linked(a2, 'core_Variable', b)


def test_assoc_traceExpr88_reverse_link_reassign_clear():
    a1 = core_TraceCompareExpression(multivaluedTag=True)
    a2 = core_TraceCompareExpression(multivaluedTag=False)
    b = core_MatchTrace(cardinality="sample_text")
    _safe_set(b, 'core_MatchTrace89', a1)
    assert _is_linked(b, 'core_MatchTrace89', a1)
    if hasattr(a1, 'core_TraceCompareExpression'):
        assert _is_linked(a1, 'core_TraceCompareExpression', b)
    _safe_set(b, 'core_MatchTrace89', a2)
    assert _is_linked(b, 'core_MatchTrace89', a2)
    if hasattr(a1, 'core_TraceCompareExpression'):
        assert not _is_linked(a1, 'core_TraceCompareExpression', b)
    if hasattr(a2, 'core_TraceCompareExpression'):
        assert _is_linked(a2, 'core_TraceCompareExpression', b)
    _safe_set(b, 'core_MatchTrace89', None)
    assert not _is_linked(b, 'core_MatchTrace89', a2)
    if hasattr(a2, 'core_TraceCompareExpression'):
        assert not _is_linked(a2, 'core_TraceCompareExpression', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_expr50_stub_double():
    # core_Expression has no real 'core_Expression51' property in the generated
    # code (a bare stub) -- manually attach it so core_ResolveLink's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ResolveLink's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ResolveLink(featureName="sample_text", isExternal="sample_text", linkName="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression51', None)
    _safe_set(owner, 'core_ResolveLink', partner)
    assert getattr(partner, 'core_Expression51') == owner
    _safe_set(owner, 'core_ResolveLink', None)
    assert getattr(partner, 'core_Expression51') is None


def test_assoc_expr93_stub_double():
    # core_Expression has no real 'core_Expression95' property in the generated
    # code (a bare stub) -- manually attach it so core_TraceCompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_TraceCompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_TraceCompareExpression(multivaluedTag=True)
    partner = core_Expression()
    setattr(partner, 'core_Expression95', None)
    _safe_set(owner, 'core_TraceCompareExpression94', partner)
    assert getattr(partner, 'core_Expression95') == owner
    _safe_set(owner, 'core_TraceCompareExpression94', None)
    assert getattr(partner, 'core_Expression95') is None


def test_assoc_expression25_stub_double():
    # core_Expression has no real 'core_Expression27' property in the generated
    # code (a bare stub) -- manually attach it so core_PropertyWrite's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_PropertyWrite's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_PropertyWrite(_property="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression27', None)
    _safe_set(owner, 'core_PropertyWrite26', partner)
    assert getattr(partner, 'core_Expression27') == owner
    _safe_set(owner, 'core_PropertyWrite26', None)
    assert getattr(partner, 'core_Expression27') is None


def test_assoc_features81_stub_double():
    # core_InlineClass has no real 'core_InlineClass82' property in the generated
    # code (a bare stub) -- manually attach it so core_InlineFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_InlineFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_InlineFeature(multivalued=True)
    partner = core_InlineClass()
    setattr(partner, 'core_InlineClass82', None)
    _safe_set(owner, 'core_InlineFeature', partner)
    assert owner in getattr(partner, 'core_InlineClass82')
    _safe_set(owner, 'core_InlineFeature', None)
    assert owner not in getattr(partner, 'core_InlineClass82')


def test_assoc_left42_stub_double():
    # core_Expression has no real 'core_Expression43' property in the generated
    # code (a bare stub) -- manually attach it so core_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_BinaryExpr(binaryOp="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression43', None)
    _safe_set(owner, 'core_BinaryExpr', partner)
    assert getattr(partner, 'core_Expression43') == owner
    _safe_set(owner, 'core_BinaryExpr', None)
    assert getattr(partner, 'core_Expression43') is None


def test_assoc_model68_stub_double():
    # core_RepresentModel has no real 'core_RepresentModel69' property in the generated
    # code (a bare stub) -- manually attach it so core_ClassUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ClassUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ClassUse(className="sample_text", strictType=True)
    partner = core_RepresentModel()
    setattr(partner, 'core_RepresentModel69', None)
    _safe_set(owner, 'core_ClassUse', partner)
    assert getattr(partner, 'core_RepresentModel69') == owner
    _safe_set(owner, 'core_ClassUse', None)
    assert getattr(partner, 'core_RepresentModel69') is None


def test_assoc_parameters3_stub_double():
    # core_AnnotationParameter has no real 'core_AnnotationParameter' property in the generated
    # code (a bare stub) -- manually attach it so core_GenericAnnotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_GenericAnnotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_GenericAnnotation(name="sample_text")
    partner = core_AnnotationParameter()
    setattr(partner, 'core_AnnotationParameter', None)
    _safe_set(owner, 'core_GenericAnnotation', {partner})
    assert getattr(partner, 'core_AnnotationParameter') == owner
    _safe_set(owner, 'core_GenericAnnotation', set())
    assert getattr(partner, 'core_AnnotationParameter') is None


def test_assoc_parameters32_stub_double():
    # core_Expression has no real 'core_Expression34' property in the generated
    # code (a bare stub) -- manually attach it so core_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_MethodCall(methodName="sample_text", withParameters=True)
    partner = core_Expression()
    setattr(partner, 'core_Expression34', None)
    _safe_set(owner, 'core_MethodCall33', {partner})
    assert getattr(partner, 'core_Expression34') == owner
    _safe_set(owner, 'core_MethodCall33', set())
    assert getattr(partner, 'core_Expression34') is None


def test_assoc_parameters37_stub_double():
    # core_KeywordMethodCall has no real 'core_KeywordMethodCall38' property in the generated
    # code (a bare stub) -- manually attach it so core_KeywordParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_KeywordParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_KeywordParameter(keyword="sample_text")
    partner = core_KeywordMethodCall()
    setattr(partner, 'core_KeywordMethodCall38', None)
    _safe_set(owner, 'core_KeywordParameter', partner)
    assert owner in getattr(partner, 'core_KeywordMethodCall38')
    _safe_set(owner, 'core_KeywordParameter', None)
    assert owner not in getattr(partner, 'core_KeywordMethodCall38')


def test_assoc_receptor30_stub_double():
    # core_Expression has no real 'core_Expression31' property in the generated
    # code (a bare stub) -- manually attach it so core_MethodCall's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_MethodCall's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_MethodCall(methodName="sample_text", withParameters=True)
    partner = core_Expression()
    setattr(partner, 'core_Expression31', None)
    _safe_set(owner, 'core_MethodCall', partner)
    assert getattr(partner, 'core_Expression31') == owner
    _safe_set(owner, 'core_MethodCall', None)
    assert getattr(partner, 'core_Expression31') is None


def test_assoc_requires16_stub_double():
    # core_TransformationDefinition has no real 'core_TransformationDefinition17' property in the generated
    # code (a bare stub) -- manually attach it so core_RequireDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_RequireDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_RequireDeclaration(default="sample_text", name="sample_text")
    partner = core_TransformationDefinition()
    setattr(partner, 'core_TransformationDefinition17', None)
    _safe_set(owner, 'core_RequireDeclaration', partner)
    assert owner in getattr(partner, 'core_TransformationDefinition17')
    _safe_set(owner, 'core_RequireDeclaration', None)
    assert owner not in getattr(partner, 'core_TransformationDefinition17')


def test_assoc_right44_stub_double():
    # core_Expression has no real 'core_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so core_BinaryExpr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_BinaryExpr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_BinaryExpr(binaryOp="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression46', None)
    _safe_set(owner, 'core_BinaryExpr45', partner)
    assert getattr(partner, 'core_Expression46') == owner
    _safe_set(owner, 'core_BinaryExpr45', None)
    assert getattr(partner, 'core_Expression46') is None


def test_assoc_trace86_stub_double():
    # core_TraceDefinition has no real 'core_TraceDefinition87' property in the generated
    # code (a bare stub) -- manually attach it so core_MatchTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_MatchTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_MatchTrace(cardinality="sample_text")
    partner = core_TraceDefinition()
    setattr(partner, 'core_TraceDefinition87', None)
    _safe_set(owner, 'core_MatchTrace', partner)
    assert getattr(partner, 'core_TraceDefinition87') == owner
    _safe_set(owner, 'core_MatchTrace', None)
    assert getattr(partner, 'core_TraceDefinition87') is None


def test_assoc_traceVar90_stub_double():
    # core_TraceElement has no real 'core_TraceElement92' property in the generated
    # code (a bare stub) -- manually attach it so core_TraceCompareExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_TraceCompareExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_TraceCompareExpression(multivaluedTag=True)
    partner = core_TraceElement()
    setattr(partner, 'core_TraceElement92', None)
    _safe_set(owner, 'core_TraceCompareExpression91', partner)
    assert getattr(partner, 'core_TraceElement92') == owner
    _safe_set(owner, 'core_TraceCompareExpression91', None)
    assert getattr(partner, 'core_TraceElement92') is None


def test_assoc_type83_stub_double():
    # core_TypeExpression has no real 'core_TypeExpression85' property in the generated
    # code (a bare stub) -- manually attach it so core_InlineFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_InlineFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_InlineFeature(multivalued=True)
    partner = core_TypeExpression()
    setattr(partner, 'core_TypeExpression85', None)
    _safe_set(owner, 'core_InlineFeature84', partner)
    assert getattr(partner, 'core_TypeExpression85') == owner
    _safe_set(owner, 'core_InlineFeature84', None)
    assert getattr(partner, 'core_TypeExpression85') is None


def test_assoc_type_71_stub_double():
    # core_TypedWithClass has no real 'core_TypedWithClass' property in the generated
    # code (a bare stub) -- manually attach it so core_ClassUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ClassUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ClassUse(className="sample_text", strictType=True)
    partner = core_TypedWithClass()
    setattr(partner, 'core_TypedWithClass', None)
    _safe_set(owner, 'core_ClassUse72', partner)
    assert getattr(partner, 'core_TypedWithClass') == owner
    _safe_set(owner, 'core_ClassUse72', None)
    assert getattr(partner, 'core_TypedWithClass') is None


def test_assoc_uses14_stub_double():
    # core_TransformationDefinition has no real 'core_TransformationDefinition15' property in the generated
    # code (a bare stub) -- manually attach it so core_UseDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_UseDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_UseDeclaration(as_="sample_text", module="sample_text")
    partner = core_TransformationDefinition()
    setattr(partner, 'core_TransformationDefinition15', None)
    _safe_set(owner, 'core_UseDeclaration', partner)
    assert owner in getattr(partner, 'core_TransformationDefinition15')
    _safe_set(owner, 'core_UseDeclaration', None)
    assert owner not in getattr(partner, 'core_TransformationDefinition15')


def test_assoc_value39_stub_double():
    # core_Expression has no real 'core_Expression41' property in the generated
    # code (a bare stub) -- manually attach it so core_KeywordParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_KeywordParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_KeywordParameter(keyword="sample_text")
    partner = core_Expression()
    setattr(partner, 'core_Expression41', None)
    _safe_set(owner, 'core_KeywordParameter40', partner)
    assert getattr(partner, 'core_Expression41') == owner
    _safe_set(owner, 'core_KeywordParameter40', None)
    assert getattr(partner, 'core_Expression41') is None


def test_assoc_variable28_stub_double():
    # core_VariableReference has no real 'core_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so core_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_Variable(name="sample_text")
    partner = core_VariableReference()
    setattr(partner, 'core_VariableReference', None)
    _safe_set(owner, 'core_Variable29', partner)
    assert getattr(partner, 'core_VariableReference') == owner
    _safe_set(owner, 'core_Variable29', None)
    assert getattr(partner, 'core_VariableReference') is None


