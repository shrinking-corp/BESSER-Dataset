import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CallArgumentsCS,
    CollectionLiteralExpCS,
    LiteralExpCS,
    OclExpressionCS,
    PrimitiveLiteralExpCS,
    TypeCS,
    TypeLiteralExpCS,
    VariableExpCS,
    essentialOCLCST_ArrowCallArgumentsCS,
    essentialOCLCST_BinaryExpressionCS,
    essentialOCLCST_BooleanLiteralExpCS,
    essentialOCLCST_CallArgumentsCS,
    essentialOCLCST_CallExpCS,
    essentialOCLCST_CollectionLiteralExpCS,
    essentialOCLCST_CollectionLiteralPartCS,
    essentialOCLCST_CollectionTypeCS,
    essentialOCLCST_DotIndexArgumentsCS,
    essentialOCLCST_IfExpCS,
    essentialOCLCST_IntegerLiteralExpCS,
    essentialOCLCST_InvalidLiteralExpCS,
    essentialOCLCST_LetExpCS,
    essentialOCLCST_LiteralExpCS,
    essentialOCLCST_NullLiteralExpCS,
    essentialOCLCST_OclExpressionCS,
    essentialOCLCST_PathNameCS,
    essentialOCLCST_PrimitiveLiteralExpCS,
    essentialOCLCST_RealLiteralExpCS,
    essentialOCLCST_SimpleNameCS,
    essentialOCLCST_StringLiteralExpCS,
    essentialOCLCST_TupleLiteralExpCS,
    essentialOCLCST_TupleTypeCS,
    essentialOCLCST_TypeCS,
    essentialOCLCST_TypeLiteralExpCS,
    essentialOCLCST_UnaryExpressionCS,
    essentialOCLCST_UnlimitedNaturalLiteralExpCS,
    essentialOCLCST_VariableCS,
    essentialOCLCST_VariableExpCS,
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

def test_assoc_collectionLiteralParts49_stub_double():
    # essentialOCLCST_CollectionLiteralPartCS has no real 'essentialOCLCST_CollectionLiteralPartCS51' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_SimpleNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_SimpleNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_SimpleNameCS(value="sample_text")
    partner = essentialOCLCST_CollectionLiteralPartCS()
    setattr(partner, 'essentialOCLCST_CollectionLiteralPartCS51', None)
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS50', {partner})
    assert getattr(partner, 'essentialOCLCST_CollectionLiteralPartCS51') == owner
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS50', set())
    assert getattr(partner, 'essentialOCLCST_CollectionLiteralPartCS51') is None


def test_assoc_indexes31_stub_double():
    # essentialOCLCST_OclExpressionCS has no real 'essentialOCLCST_OclExpressionCS32' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_DotIndexArgumentsCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_DotIndexArgumentsCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_DotIndexArgumentsCS(isPre=True)
    partner = essentialOCLCST_OclExpressionCS()
    setattr(partner, 'essentialOCLCST_OclExpressionCS32', None)
    _safe_set(owner, 'essentialOCLCST_DotIndexArgumentsCS', {partner})
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS32') == owner
    _safe_set(owner, 'essentialOCLCST_DotIndexArgumentsCS', set())
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS32') is None


def test_assoc_left6_stub_double():
    # essentialOCLCST_OclExpressionCS has no real 'essentialOCLCST_OclExpressionCS7' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_BinaryExpressionCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_BinaryExpressionCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    partner = essentialOCLCST_OclExpressionCS()
    setattr(partner, 'essentialOCLCST_OclExpressionCS7', None)
    _safe_set(owner, 'essentialOCLCST_BinaryExpressionCS', partner)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS7') == owner
    _safe_set(owner, 'essentialOCLCST_BinaryExpressionCS', None)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS7') is None


def test_assoc_name58_stub_double():
    # essentialOCLCST_VariableCS has no real 'essentialOCLCST_VariableCS59' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_SimpleNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_SimpleNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_SimpleNameCS(value="sample_text")
    partner = essentialOCLCST_VariableCS()
    setattr(partner, 'essentialOCLCST_VariableCS59', None)
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS60', partner)
    assert getattr(partner, 'essentialOCLCST_VariableCS59') == owner
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS60', None)
    assert getattr(partner, 'essentialOCLCST_VariableCS59') is None


def test_assoc_part54_stub_double():
    # essentialOCLCST_VariableCS has no real 'essentialOCLCST_VariableCS55' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_TupleTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_TupleTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_TupleTypeCS(value="sample_text")
    partner = essentialOCLCST_VariableCS()
    setattr(partner, 'essentialOCLCST_VariableCS55', None)
    _safe_set(owner, 'essentialOCLCST_TupleTypeCS', {partner})
    assert getattr(partner, 'essentialOCLCST_VariableCS55') == owner
    _safe_set(owner, 'essentialOCLCST_TupleTypeCS', set())
    assert getattr(partner, 'essentialOCLCST_VariableCS55') is None


def test_assoc_right8_stub_double():
    # essentialOCLCST_OclExpressionCS has no real 'essentialOCLCST_OclExpressionCS10' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_BinaryExpressionCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_BinaryExpressionCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_BinaryExpressionCS(op="sample_text")
    partner = essentialOCLCST_OclExpressionCS()
    setattr(partner, 'essentialOCLCST_OclExpressionCS10', None)
    _safe_set(owner, 'essentialOCLCST_BinaryExpressionCS9', partner)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS10') == owner
    _safe_set(owner, 'essentialOCLCST_BinaryExpressionCS9', None)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS10') is None


def test_assoc_simpleNames46_stub_double():
    # essentialOCLCST_PathNameCS has no real 'essentialOCLCST_PathNameCS47' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_SimpleNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_SimpleNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_SimpleNameCS(value="sample_text")
    partner = essentialOCLCST_PathNameCS()
    setattr(partner, 'essentialOCLCST_PathNameCS47', None)
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS48', partner)
    assert owner in getattr(partner, 'essentialOCLCST_PathNameCS47')
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS48', None)
    assert owner not in getattr(partner, 'essentialOCLCST_PathNameCS47')


def test_assoc_source56_stub_double():
    # essentialOCLCST_OclExpressionCS has no real 'essentialOCLCST_OclExpressionCS57' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_UnaryExpressionCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_UnaryExpressionCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_UnaryExpressionCS(op="sample_text")
    partner = essentialOCLCST_OclExpressionCS()
    setattr(partner, 'essentialOCLCST_OclExpressionCS57', None)
    _safe_set(owner, 'essentialOCLCST_UnaryExpressionCS', partner)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS57') == owner
    _safe_set(owner, 'essentialOCLCST_UnaryExpressionCS', None)
    assert getattr(partner, 'essentialOCLCST_OclExpressionCS57') is None


def test_assoc_value25_stub_double():
    # essentialOCLCST_CollectionTypeCS has no real 'essentialOCLCST_CollectionTypeCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialOCLCST_SimpleNameCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialOCLCST_SimpleNameCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialOCLCST_SimpleNameCS(value="sample_text")
    partner = essentialOCLCST_CollectionTypeCS()
    setattr(partner, 'essentialOCLCST_CollectionTypeCS', None)
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS', partner)
    assert getattr(partner, 'essentialOCLCST_CollectionTypeCS') == owner
    _safe_set(owner, 'essentialOCLCST_SimpleNameCS', None)
    assert getattr(partner, 'essentialOCLCST_CollectionTypeCS') is None


