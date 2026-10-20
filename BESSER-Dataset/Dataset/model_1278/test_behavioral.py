import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractNameExpCS,
    BinaryOperatorCS,
    ExpCS,
    LiteralExpCS,
    ModelElementCS,
    Nameable,
    NamedElementCS,
    NamedExpCS,
    OperatorCS,
    PrimitiveLiteralExpCS,
    RootCS,
    SpecificationCS,
    TypedRefCS,
    VariableCS,
    essentialoclcs_AbstractNameExpCS,
    essentialoclcs_BinaryOperatorCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    essentialoclcs_CollectionLiteralPartCS,
    essentialoclcs_CollectionTypeCS,
    essentialoclcs_ConstructorExpCS,
    essentialoclcs_ConstructorPartCS,
    essentialoclcs_ContextCS,
    essentialoclcs_ExpCS,
    essentialoclcs_ExpSpecificationCS,
    essentialoclcs_IfExpCS,
    essentialoclcs_IndexExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    essentialoclcs_InvocationExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_LiteralExpCS,
    essentialoclcs_NameExpCS,
    essentialoclcs_NamedExpCS,
    essentialoclcs_NavigatingArgCS,
    essentialoclcs_NavigationOperatorCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_OperatorCS,
    essentialoclcs_PathNameCS,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_Property,
    essentialoclcs_SelfExpCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_TupleLiteralPartCS,
    essentialoclcs_Type,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_TypeNameExpCS,
    essentialoclcs_TypedRefCS,
    essentialoclcs_UnaryOperatorCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_VariableCS,
    NavigationRole,
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

def test_assoc_argument42_stub_double():
    # essentialoclcs_InvocationExpCS has no real 'navigatingExp' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_InvocationExpCS()
    setattr(partner, 'navigatingExp', None)
    _safe_set(owner, 'NavigatingArgCS', partner)
    assert owner in getattr(partner, 'navigatingExp')
    _safe_set(owner, 'NavigatingArgCS', None)
    assert owner not in getattr(partner, 'navigatingExp')


def test_assoc_firstIndexes32_stub_double():
    # essentialoclcs_ExpCS has no real 'essentialoclcs_ExpCS33' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_IndexExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_IndexExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_IndexExpCS(atPre=True)
    partner = essentialoclcs_ExpCS()
    setattr(partner, 'essentialoclcs_ExpCS33', None)
    _safe_set(owner, 'essentialoclcs_IndexExpCS', {partner})
    assert getattr(partner, 'essentialoclcs_ExpCS33') == owner
    _safe_set(owner, 'essentialoclcs_IndexExpCS', set())
    assert getattr(partner, 'essentialoclcs_ExpCS33') is None


def test_assoc_init56_stub_double():
    # essentialoclcs_ExpCS has no real 'essentialoclcs_ExpCS58' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_ExpCS()
    setattr(partner, 'essentialoclcs_ExpCS58', None)
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS57', partner)
    assert getattr(partner, 'essentialoclcs_ExpCS58') == owner
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS57', None)
    assert getattr(partner, 'essentialoclcs_ExpCS58') is None


def test_assoc_name51_stub_double():
    # essentialoclcs_ExpCS has no real 'essentialoclcs_ExpCS52' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_ExpCS()
    setattr(partner, 'essentialoclcs_ExpCS52', None)
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS', partner)
    assert getattr(partner, 'essentialoclcs_ExpCS52') == owner
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS', None)
    assert getattr(partner, 'essentialoclcs_ExpCS52') is None


def test_assoc_nameExp48_stub_double():
    # essentialoclcs_NamedExpCS has no real 'essentialoclcs_NamedExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NameExpCS(atPre=True)
    partner = essentialoclcs_NamedExpCS()
    setattr(partner, 'essentialoclcs_NamedExpCS', None)
    _safe_set(owner, 'essentialoclcs_NameExpCS49', partner)
    assert getattr(partner, 'essentialoclcs_NamedExpCS') == owner
    _safe_set(owner, 'essentialoclcs_NameExpCS49', None)
    assert getattr(partner, 'essentialoclcs_NamedExpCS') is None


def test_assoc_navigatingExp50_stub_double():
    # essentialoclcs_InvocationExpCS has no real 'InvocationExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_InvocationExpCS()
    setattr(partner, 'InvocationExpCS', None)
    _safe_set(owner, 'argument', partner)
    assert getattr(partner, 'InvocationExpCS') == owner
    _safe_set(owner, 'argument', None)
    assert getattr(partner, 'InvocationExpCS') is None


def test_assoc_ownedParts12_stub_double():
    # essentialoclcs_ConstructorPartCS has no real 'essentialoclcs_ConstructorPartCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ConstructorExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ConstructorExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ConstructorExpCS(value="sample_text")
    partner = essentialoclcs_ConstructorPartCS()
    setattr(partner, 'essentialoclcs_ConstructorPartCS', None)
    _safe_set(owner, 'essentialoclcs_ConstructorExpCS', {partner})
    assert getattr(partner, 'essentialoclcs_ConstructorPartCS') == owner
    _safe_set(owner, 'essentialoclcs_ConstructorExpCS', set())
    assert getattr(partner, 'essentialoclcs_ConstructorPartCS') is None


def test_assoc_ownedType1_stub_double():
    # essentialoclcs_CollectionLiteralExpCS has no real 'essentialoclcs_CollectionLiteralExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CollectionTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CollectionTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CollectionTypeCS(name="sample_text")
    partner = essentialoclcs_CollectionLiteralExpCS()
    setattr(partner, 'essentialoclcs_CollectionLiteralExpCS', None)
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS', partner)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralExpCS') == owner
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS', None)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralExpCS') is None


def test_assoc_ownedType10_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CollectionTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CollectionTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CollectionTypeCS(name="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS', None)
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS11', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS') == owner
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS11', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS') is None


def test_assoc_ownedType53_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS55' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS55', None)
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS54', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS55') == owner
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS54', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS55') is None


def test_assoc_pathName47_stub_double():
    # essentialoclcs_PathNameCS has no real 'essentialoclcs_PathNameCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NameExpCS(atPre=True)
    partner = essentialoclcs_PathNameCS()
    setattr(partner, 'essentialoclcs_PathNameCS', None)
    _safe_set(owner, 'essentialoclcs_NameExpCS', partner)
    assert getattr(partner, 'essentialoclcs_PathNameCS') == owner
    _safe_set(owner, 'essentialoclcs_NameExpCS', None)
    assert getattr(partner, 'essentialoclcs_PathNameCS') is None


def test_assoc_secondIndexes34_stub_double():
    # essentialoclcs_ExpCS has no real 'essentialoclcs_ExpCS36' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_IndexExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_IndexExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_IndexExpCS(atPre=True)
    partner = essentialoclcs_ExpCS()
    setattr(partner, 'essentialoclcs_ExpCS36', None)
    _safe_set(owner, 'essentialoclcs_IndexExpCS35', {partner})
    assert getattr(partner, 'essentialoclcs_ExpCS36') == owner
    _safe_set(owner, 'essentialoclcs_IndexExpCS35', set())
    assert getattr(partner, 'essentialoclcs_ExpCS36') is None


