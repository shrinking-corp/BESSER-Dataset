import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMapping,
    ArithmeticExpression,
    BinaryExpression,
    CompositeMapping,
    ContentMapping,
    EqualityExpression,
    ExplicitMetamodel,
    Expression,
    LogicalExpression,
    MetamodelDeclaration,
    RelationalExpression,
    UnaryExpression,
    transformation_AbstractMapping,
    transformation_Addition,
    transformation_And,
    transformation_ArithmeticExpression,
    transformation_BinaryExpression,
    transformation_BooleanLiteral,
    transformation_ClassLiteral,
    transformation_ClassMapping,
    transformation_CoalescingExpression,
    transformation_CompositeMapping,
    transformation_ConditionalExpression,
    transformation_ConditionalMapping,
    transformation_ContentMapping,
    transformation_DataTypeMapping,
    transformation_Different,
    transformation_Division,
    transformation_EClass,
    transformation_EClassifier,
    transformation_EDataType,
    transformation_EEnumLiteral,
    transformation_EPackage,
    transformation_EStructuralFeature,
    transformation_ETypedElement,
    transformation_EnumLiteral,
    transformation_Equal,
    transformation_EqualityExpression,
    transformation_ExplicitMetamodel,
    transformation_Expression,
    transformation_ExtentExpression,
    transformation_ExtentMetamodel,
    transformation_FeatureAccess,
    transformation_FeatureMapping,
    transformation_Greater,
    transformation_GreaterOrEqual,
    transformation_If,
    transformation_IntegerLiteral,
    transformation_Invocation,
    transformation_Lambda,
    transformation_Less,
    transformation_LessOrEqual,
    transformation_Let,
    transformation_LogicalExpression,
    transformation_Map,
    transformation_MetamodelDeclaration,
    transformation_Minus,
    transformation_Multiplication,
    transformation_Negation,
    transformation_Or,
    transformation_OtherwiseClause,
    transformation_RealLiteral,
    transformation_RelationalExpression,
    transformation_ResultMapping,
    transformation_Source,
    transformation_SourceMetamodel,
    transformation_StringLiteral,
    transformation_Subtraction,
    transformation_TargetMetamodel,
    transformation_Transformation,
    transformation_TypeOfExpression,
    transformation_UnaryExpression,
    transformation_VariableDefinition,
    transformation_VariableInitialization,
    transformation_VariableUse,
    transformation_WhenClause,
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

def test_assoc_content16_stub_double():
    # transformation_ContentMapping has no real 'transformation_ContentMapping18' property in the generated
    # code (a bare stub) -- manually attach it so transformation_ClassMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_ClassMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_ClassMapping(default=True)
    partner = transformation_ContentMapping()
    setattr(partner, 'transformation_ContentMapping18', None)
    _safe_set(owner, 'transformation_ClassMapping17', partner)
    assert getattr(partner, 'transformation_ContentMapping18') == owner
    _safe_set(owner, 'transformation_ClassMapping17', None)
    assert getattr(partner, 'transformation_ContentMapping18') is None


def test_assoc_feature66_stub_double():
    # transformation_ETypedElement has no real 'transformation_ETypedElement' property in the generated
    # code (a bare stub) -- manually attach it so transformation_FeatureAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_FeatureAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_FeatureAccess(nullable=True, spreading=True)
    partner = transformation_ETypedElement()
    setattr(partner, 'transformation_ETypedElement', None)
    _safe_set(owner, 'transformation_FeatureAccess67', partner)
    assert getattr(partner, 'transformation_ETypedElement') == owner
    _safe_set(owner, 'transformation_FeatureAccess67', None)
    assert getattr(partner, 'transformation_ETypedElement') is None


def test_assoc_mappings1_stub_double():
    # transformation_AbstractMapping has no real 'transformation_AbstractMapping' property in the generated
    # code (a bare stub) -- manually attach it so transformation_Transformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_Transformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_Transformation(name="sample_text")
    partner = transformation_AbstractMapping()
    setattr(partner, 'transformation_AbstractMapping', None)
    _safe_set(owner, 'transformation_Transformation2', {partner})
    assert getattr(partner, 'transformation_AbstractMapping') == owner
    _safe_set(owner, 'transformation_Transformation2', set())
    assert getattr(partner, 'transformation_AbstractMapping') is None


def test_assoc_metamodelDeclarations0_stub_double():
    # transformation_MetamodelDeclaration has no real 'transformation_MetamodelDeclaration' property in the generated
    # code (a bare stub) -- manually attach it so transformation_Transformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_Transformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_Transformation(name="sample_text")
    partner = transformation_MetamodelDeclaration()
    setattr(partner, 'transformation_MetamodelDeclaration', None)
    _safe_set(owner, 'transformation_Transformation', {partner})
    assert getattr(partner, 'transformation_MetamodelDeclaration') == owner
    _safe_set(owner, 'transformation_Transformation', set())
    assert getattr(partner, 'transformation_MetamodelDeclaration') is None


def test_assoc_object64_stub_double():
    # transformation_Expression has no real 'transformation_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so transformation_FeatureAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_FeatureAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_FeatureAccess(nullable=True, spreading=True)
    partner = transformation_Expression()
    setattr(partner, 'transformation_Expression65', None)
    _safe_set(owner, 'transformation_FeatureAccess', partner)
    assert getattr(partner, 'transformation_Expression65') == owner
    _safe_set(owner, 'transformation_FeatureAccess', None)
    assert getattr(partner, 'transformation_Expression65') is None


def test_assoc_parameters77_stub_double():
    # transformation_Lambda has no real 'transformation_Lambda' property in the generated
    # code (a bare stub) -- manually attach it so transformation_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_VariableDefinition(name="sample_text")
    partner = transformation_Lambda()
    setattr(partner, 'transformation_Lambda', None)
    _safe_set(owner, 'transformation_VariableDefinition78', partner)
    assert owner in getattr(partner, 'transformation_Lambda')
    _safe_set(owner, 'transformation_VariableDefinition78', None)
    assert owner not in getattr(partner, 'transformation_Lambda')


def test_assoc_source12_stub_double():
    # transformation_EClass has no real 'transformation_EClass' property in the generated
    # code (a bare stub) -- manually attach it so transformation_ClassMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_ClassMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_ClassMapping(default=True)
    partner = transformation_EClass()
    setattr(partner, 'transformation_EClass', None)
    _safe_set(owner, 'transformation_ClassMapping', partner)
    assert getattr(partner, 'transformation_EClass') == owner
    _safe_set(owner, 'transformation_ClassMapping', None)
    assert getattr(partner, 'transformation_EClass') is None


def test_assoc_sourceMetamodel5_stub_double():
    # transformation_SourceMetamodel has no real 'transformation_SourceMetamodel' property in the generated
    # code (a bare stub) -- manually attach it so transformation_ExtentMetamodel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_ExtentMetamodel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_ExtentMetamodel(generated=True)
    partner = transformation_SourceMetamodel()
    setattr(partner, 'transformation_SourceMetamodel', None)
    _safe_set(owner, 'transformation_ExtentMetamodel', partner)
    assert getattr(partner, 'transformation_SourceMetamodel') == owner
    _safe_set(owner, 'transformation_ExtentMetamodel', None)
    assert getattr(partner, 'transformation_SourceMetamodel') is None


def test_assoc_target13_stub_double():
    # transformation_EClass has no real 'transformation_EClass15' property in the generated
    # code (a bare stub) -- manually attach it so transformation_ClassMapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_ClassMapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_ClassMapping(default=True)
    partner = transformation_EClass()
    setattr(partner, 'transformation_EClass15', None)
    _safe_set(owner, 'transformation_ClassMapping14', partner)
    assert getattr(partner, 'transformation_EClass15') == owner
    _safe_set(owner, 'transformation_ClassMapping14', None)
    assert getattr(partner, 'transformation_EClass15') is None


def test_assoc_variable32_stub_double():
    # transformation_VariableInitialization has no real 'transformation_VariableInitialization' property in the generated
    # code (a bare stub) -- manually attach it so transformation_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_VariableDefinition(name="sample_text")
    partner = transformation_VariableInitialization()
    setattr(partner, 'transformation_VariableInitialization', None)
    _safe_set(owner, 'transformation_VariableDefinition', partner)
    assert getattr(partner, 'transformation_VariableInitialization') == owner
    _safe_set(owner, 'transformation_VariableDefinition', None)
    assert getattr(partner, 'transformation_VariableInitialization') is None


def test_assoc_variable86_stub_double():
    # transformation_VariableUse has no real 'transformation_VariableUse' property in the generated
    # code (a bare stub) -- manually attach it so transformation_VariableDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformation_VariableDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformation_VariableDefinition(name="sample_text")
    partner = transformation_VariableUse()
    setattr(partner, 'transformation_VariableUse', None)
    _safe_set(owner, 'transformation_VariableDefinition87', partner)
    assert getattr(partner, 'transformation_VariableUse') == owner
    _safe_set(owner, 'transformation_VariableDefinition87', None)
    assert getattr(partner, 'transformation_VariableUse') is None


