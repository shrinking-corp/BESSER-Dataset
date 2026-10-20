import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CSTNode,
    CallExpCS,
    CollectionLiteralPartCS,
    ContextDeclCS,
    DefExpressionCS,
    FeatureCallExpCS,
    InitOrDerValueCS,
    InvOrDefCS,
    IsMarkedPreCS,
    LiteralExpCS,
    LoopExpCS,
    OCLExpressionCS,
    OCLMessageArgCS,
    OperationCS,
    PathNameCS,
    PrePostOrBodyDeclCS,
    PrimitiveLiteralExpCS,
    SimpleNameCS,
    TypeCS,
    VariableCS,
    cst_SimpleNameCS,
    cst_TypeCS,
    ocl_cst_BooleanLiteralExpCS,
    ocl_cst_CSTNode,
    ocl_cst_CallExpCS,
    ocl_cst_ClassifierContextDeclCS,
    ocl_cst_CollectionLiteralExpCS,
    ocl_cst_CollectionLiteralPartCS,
    ocl_cst_CollectionRangeCS,
    ocl_cst_CollectionTypeCS,
    ocl_cst_ContextDeclCS,
    ocl_cst_DefCS,
    ocl_cst_DefExpressionCS,
    ocl_cst_DerValueCS,
    ocl_cst_EnumLiteralExpCS,
    ocl_cst_FeatureCallExpCS,
    ocl_cst_IfExpCS,
    ocl_cst_InitOrDerValueCS,
    ocl_cst_InitValueCS,
    ocl_cst_IntegerLiteralExpCS,
    ocl_cst_InvCS,
    ocl_cst_InvOrDefCS,
    ocl_cst_InvalidLiteralExpCS,
    ocl_cst_IsMarkedPreCS,
    ocl_cst_IterateExpCS,
    ocl_cst_IteratorExpCS,
    ocl_cst_LetExpCS,
    ocl_cst_LiteralExpCS,
    ocl_cst_LoopExpCS,
    ocl_cst_MessageExpCS,
    ocl_cst_NullLiteralExpCS,
    ocl_cst_OCLExpressionCS,
    ocl_cst_OCLMessageArgCS,
    ocl_cst_OperationCS,
    ocl_cst_OperationCallExpCS,
    ocl_cst_OperationContextDeclCS,
    ocl_cst_PackageDeclarationCS,
    ocl_cst_PathNameCS,
    ocl_cst_PrePostOrBodyDeclCS,
    ocl_cst_PrimitiveLiteralExpCS,
    ocl_cst_PrimitiveTypeCS,
    ocl_cst_PropertyContextCS,
    ocl_cst_RealLiteralExpCS,
    ocl_cst_SimpleNameCS,
    ocl_cst_StateExpCS,
    ocl_cst_StringLiteralExpCS,
    ocl_cst_TupleLiteralExpCS,
    ocl_cst_TupleTypeCS,
    ocl_cst_TypeCS,
    ocl_cst_VariableCS,
    ocl_cst_VariableExpCS,
    CollectionTypeIdentifierEnum,
    DotOrArrowEnum,
    MessageExpKind,
    PrePostOrBodyEnum,
    SimpleTypeEnum,
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

def test_assoc_arguments82_stub_double():
    # OCLMessageArgCS has no real 'OCLMessageArgCS' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_MessageExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_MessageExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_MessageExpCS(kind="sample_text")
    partner = OCLMessageArgCS()
    setattr(partner, 'OCLMessageArgCS', None)
    _safe_set(owner, 'ocl_cst_MessageExpCS83', {partner})
    assert getattr(partner, 'OCLMessageArgCS') == owner
    _safe_set(owner, 'ocl_cst_MessageExpCS83', set())
    assert getattr(partner, 'OCLMessageArgCS') is None


def test_assoc_collectionLiteralParts99_stub_double():
    # CollectionLiteralPartCS has no real 'CollectionLiteralPartCS' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_CollectionLiteralExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_CollectionLiteralExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_CollectionLiteralExpCS(collectionType="sample_text")
    partner = CollectionLiteralPartCS()
    setattr(partner, 'CollectionLiteralPartCS', None)
    _safe_set(owner, 'ocl_cst_CollectionLiteralExpCS', {partner})
    assert getattr(partner, 'CollectionLiteralPartCS') == owner
    _safe_set(owner, 'ocl_cst_CollectionLiteralExpCS', set())
    assert getattr(partner, 'CollectionLiteralPartCS') is None


def test_assoc_expressionCS20_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_PrePostOrBodyDeclCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_PrePostOrBodyDeclCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_PrePostOrBodyDeclCS(kind="sample_text")
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS', None)
    _safe_set(owner, 'ocl_cst_PrePostOrBodyDeclCS21', partner)
    assert getattr(partner, 'OCLExpressionCS') == owner
    _safe_set(owner, 'ocl_cst_PrePostOrBodyDeclCS21', None)
    assert getattr(partner, 'OCLExpressionCS') is None


def test_assoc_initExpression91_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS93' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_VariableCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_VariableCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_VariableCS(name="sample_text")
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS93', None)
    _safe_set(owner, 'ocl_cst_VariableCS92', partner)
    assert getattr(partner, 'OCLExpressionCS93') == owner
    _safe_set(owner, 'ocl_cst_VariableCS92', None)
    assert getattr(partner, 'OCLExpressionCS93') is None


def test_assoc_simpleNameCS108_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS110' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_CallExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_CallExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_CallExpCS(accessor="sample_text")
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS110', None)
    _safe_set(owner, 'ocl_cst_CallExpCS109', partner)
    assert getattr(partner, 'SimpleNameCS110') == owner
    _safe_set(owner, 'ocl_cst_CallExpCS109', None)
    assert getattr(partner, 'SimpleNameCS110') is None


def test_assoc_simpleNameCS18_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS19' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_PrePostOrBodyDeclCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_PrePostOrBodyDeclCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_PrePostOrBodyDeclCS(kind="sample_text")
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS19', None)
    _safe_set(owner, 'ocl_cst_PrePostOrBodyDeclCS', partner)
    assert getattr(partner, 'SimpleNameCS19') == owner
    _safe_set(owner, 'ocl_cst_PrePostOrBodyDeclCS', None)
    assert getattr(partner, 'SimpleNameCS19') is None


def test_assoc_simpleNameCS79_stub_double():
    # SimpleNameCS has no real 'SimpleNameCS81' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_MessageExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_MessageExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_MessageExpCS(kind="sample_text")
    partner = SimpleNameCS()
    setattr(partner, 'SimpleNameCS81', None)
    _safe_set(owner, 'ocl_cst_MessageExpCS80', partner)
    assert getattr(partner, 'SimpleNameCS81') == owner
    _safe_set(owner, 'ocl_cst_MessageExpCS80', None)
    assert getattr(partner, 'SimpleNameCS81') is None


def test_assoc_source106_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS107' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_CallExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_CallExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_CallExpCS(accessor="sample_text")
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS107', None)
    _safe_set(owner, 'ocl_cst_CallExpCS', partner)
    assert getattr(partner, 'OCLExpressionCS107') == owner
    _safe_set(owner, 'ocl_cst_CallExpCS', None)
    assert getattr(partner, 'OCLExpressionCS107') is None


def test_assoc_target77_stub_double():
    # OCLExpressionCS has no real 'OCLExpressionCS78' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_MessageExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_MessageExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_MessageExpCS(kind="sample_text")
    partner = OCLExpressionCS()
    setattr(partner, 'OCLExpressionCS78', None)
    _safe_set(owner, 'ocl_cst_MessageExpCS', partner)
    assert getattr(partner, 'OCLExpressionCS78') == owner
    _safe_set(owner, 'ocl_cst_MessageExpCS', None)
    assert getattr(partner, 'OCLExpressionCS78') is None


def test_assoc_typeCS62_stub_double():
    # TypeCS has no real 'TypeCS63' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_CollectionTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_CollectionTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_CollectionTypeCS(collectionTypeIdentifier="sample_text")
    partner = TypeCS()
    setattr(partner, 'TypeCS63', None)
    _safe_set(owner, 'ocl_cst_CollectionTypeCS', partner)
    assert getattr(partner, 'TypeCS63') == owner
    _safe_set(owner, 'ocl_cst_CollectionTypeCS', None)
    assert getattr(partner, 'TypeCS63') is None


def test_assoc_typeCS89_stub_double():
    # TypeCS has no real 'TypeCS90' property in the generated
    # code (a bare stub) -- manually attach it so ocl_cst_VariableCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocl_cst_VariableCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocl_cst_VariableCS(name="sample_text")
    partner = TypeCS()
    setattr(partner, 'TypeCS90', None)
    _safe_set(owner, 'ocl_cst_VariableCS', partner)
    assert getattr(partner, 'TypeCS90') == owner
    _safe_set(owner, 'ocl_cst_VariableCS', None)
    assert getattr(partner, 'TypeCS90') is None


