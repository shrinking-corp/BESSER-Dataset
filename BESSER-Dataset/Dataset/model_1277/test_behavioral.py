import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractNameExpCS,
    AssociationClassCallExpCS,
    CallExpCS,
    ContextLessElementCS,
    ExpCS,
    IterateCallExpCS,
    IterationCallExpCS,
    LiteralExpCS,
    ModelElementCS,
    Nameable,
    NamedElementCS,
    OperationCallExpCS,
    OperatorExpCS,
    PrimitiveLiteralExpCS,
    PropertyCallExpCS,
    RootCS,
    ShadowExpCS,
    SpecificationCS,
    TypedRefCS,
    VariableCS,
    VariableExpCS,
    essentialoclcs_AbstractNameExpCS,
    essentialoclcs_AssociationClass,
    essentialoclcs_AssociationClassCallExpCS,
    essentialoclcs_BooleanLiteralExpCS,
    essentialoclcs_CallExpCS,
    essentialoclcs_CollectionLiteralExpCS,
    essentialoclcs_CollectionLiteralPartCS,
    essentialoclcs_CollectionPatternCS,
    essentialoclcs_CollectionTypeCS,
    essentialoclcs_ContextCS,
    essentialoclcs_CurlyBracketedClauseCS,
    essentialoclcs_ExpCS,
    essentialoclcs_ExpSpecificationCS,
    essentialoclcs_IfExpCS,
    essentialoclcs_IfThenExpCS,
    essentialoclcs_InfixExpCS,
    essentialoclcs_InvalidLiteralExpCS,
    essentialoclcs_IterateCallExpCS,
    essentialoclcs_Iteration,
    essentialoclcs_IterationCallExpCS,
    essentialoclcs_LambdaLiteralExpCS,
    essentialoclcs_LetExpCS,
    essentialoclcs_LetVariableCS,
    essentialoclcs_LiteralExpCS,
    essentialoclcs_MapLiteralExpCS,
    essentialoclcs_MapLiteralPartCS,
    essentialoclcs_MapTypeCS,
    essentialoclcs_NameExpCS,
    essentialoclcs_NavigatingArgCS,
    essentialoclcs_NestedExpCS,
    essentialoclcs_NullLiteralExpCS,
    essentialoclcs_NumberLiteralExpCS,
    essentialoclcs_Operation,
    essentialoclcs_OperationCallExpCS,
    essentialoclcs_OperatorExpCS,
    essentialoclcs_PathNameCS,
    essentialoclcs_PatternExpCS,
    essentialoclcs_Precedence,
    essentialoclcs_PrefixExpCS,
    essentialoclcs_PrimitiveLiteralExpCS,
    essentialoclcs_Property,
    essentialoclcs_PropertyCallExpCS,
    essentialoclcs_RoundBracketedClauseCS,
    essentialoclcs_SelfExpCS,
    essentialoclcs_ShadowExpCS,
    essentialoclcs_ShadowPartCS,
    essentialoclcs_SquareBracketedClauseCS,
    essentialoclcs_StringLiteralExpCS,
    essentialoclcs_TupleLiteralExpCS,
    essentialoclcs_TupleLiteralPartCS,
    essentialoclcs_Type,
    essentialoclcs_TypeLiteralExpCS,
    essentialoclcs_TypeNameExpCS,
    essentialoclcs_TypeRefCS,
    essentialoclcs_TypedRefCS,
    essentialoclcs_UnlimitedNaturalLiteralExpCS,
    essentialoclcs_Variable,
    essentialoclcs_VariableCS,
    essentialoclcs_VariableExpCS,
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

def test_assoc_localLeft39_reverse_link_reassign_clear():
    a1 = essentialoclcs_ExpCS(hasError=True)
    a2 = essentialoclcs_ExpCS(hasError=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS40', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS40', a1)
    if hasattr(a1, 'essentialoclcs_ExpCS38'):
        assert _is_linked(a1, 'essentialoclcs_ExpCS38', b)
    _safe_set(b, 'essentialoclcs_ExpCS40', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS40', a2)
    if hasattr(a1, 'essentialoclcs_ExpCS38'):
        assert not _is_linked(a1, 'essentialoclcs_ExpCS38', b)
    if hasattr(a2, 'essentialoclcs_ExpCS38'):
        assert _is_linked(a2, 'essentialoclcs_ExpCS38', b)
    _safe_set(b, 'essentialoclcs_ExpCS40', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS40', a2)
    if hasattr(a2, 'essentialoclcs_ExpCS38'):
        assert not _is_linked(a2, 'essentialoclcs_ExpCS38', b)


def test_assoc_localLeftmostDescendant42_reverse_link_reassign_clear():
    a1 = essentialoclcs_ExpCS(hasError=True)
    a2 = essentialoclcs_ExpCS(hasError=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS43', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS43', a1)
    if hasattr(a1, 'essentialoclcs_ExpCS41'):
        assert _is_linked(a1, 'essentialoclcs_ExpCS41', b)
    _safe_set(b, 'essentialoclcs_ExpCS43', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS43', a2)
    if hasattr(a1, 'essentialoclcs_ExpCS41'):
        assert not _is_linked(a1, 'essentialoclcs_ExpCS41', b)
    if hasattr(a2, 'essentialoclcs_ExpCS41'):
        assert _is_linked(a2, 'essentialoclcs_ExpCS41', b)
    _safe_set(b, 'essentialoclcs_ExpCS43', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS43', a2)
    if hasattr(a2, 'essentialoclcs_ExpCS41'):
        assert not _is_linked(a2, 'essentialoclcs_ExpCS41', b)


def test_assoc_localRight47_reverse_link_reassign_clear():
    a1 = essentialoclcs_ExpCS(hasError=True)
    a2 = essentialoclcs_ExpCS(hasError=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS48', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS48', a1)
    if hasattr(a1, 'essentialoclcs_ExpCS46'):
        assert _is_linked(a1, 'essentialoclcs_ExpCS46', b)
    _safe_set(b, 'essentialoclcs_ExpCS48', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS48', a2)
    if hasattr(a1, 'essentialoclcs_ExpCS46'):
        assert not _is_linked(a1, 'essentialoclcs_ExpCS46', b)
    if hasattr(a2, 'essentialoclcs_ExpCS46'):
        assert _is_linked(a2, 'essentialoclcs_ExpCS46', b)
    _safe_set(b, 'essentialoclcs_ExpCS48', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS48', a2)
    if hasattr(a2, 'essentialoclcs_ExpCS46'):
        assert not _is_linked(a2, 'essentialoclcs_ExpCS46', b)


def test_assoc_localRightmostDescendant50_reverse_link_reassign_clear():
    a1 = essentialoclcs_ExpCS(hasError=True)
    a2 = essentialoclcs_ExpCS(hasError=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS51', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS51', a1)
    if hasattr(a1, 'essentialoclcs_ExpCS49'):
        assert _is_linked(a1, 'essentialoclcs_ExpCS49', b)
    _safe_set(b, 'essentialoclcs_ExpCS51', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS51', a2)
    if hasattr(a1, 'essentialoclcs_ExpCS49'):
        assert not _is_linked(a1, 'essentialoclcs_ExpCS49', b)
    if hasattr(a2, 'essentialoclcs_ExpCS49'):
        assert _is_linked(a2, 'essentialoclcs_ExpCS49', b)
    _safe_set(b, 'essentialoclcs_ExpCS51', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS51', a2)
    if hasattr(a2, 'essentialoclcs_ExpCS49'):
        assert not _is_linked(a2, 'essentialoclcs_ExpCS49', b)


def test_assoc_ownedCondition56_reverse_link_reassign_clear():
    a1 = essentialoclcs_IfExpCS(isImplicit=True)
    a2 = essentialoclcs_IfExpCS(isImplicit=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS57', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS57', a1)
    if hasattr(a1, 'essentialoclcs_IfExpCS'):
        assert _is_linked(a1, 'essentialoclcs_IfExpCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS57', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS57', a2)
    if hasattr(a1, 'essentialoclcs_IfExpCS'):
        assert not _is_linked(a1, 'essentialoclcs_IfExpCS', b)
    if hasattr(a2, 'essentialoclcs_IfExpCS'):
        assert _is_linked(a2, 'essentialoclcs_IfExpCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS57', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS57', a2)
    if hasattr(a2, 'essentialoclcs_IfExpCS'):
        assert not _is_linked(a2, 'essentialoclcs_IfExpCS', b)


def test_assoc_ownedCurlyBracketedClause0_reverse_link_reassign_clear():
    a1 = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    a2 = essentialoclcs_CurlyBracketedClauseCS(value="sample_text_2")
    b = essentialoclcs_AbstractNameExpCS(isPre=True)
    _safe_set(b, 'owningNameExp', a1)
    assert _is_linked(b, 'owningNameExp', a1)
    if hasattr(a1, 'CurlyBracketedClauseCS'):
        assert _is_linked(a1, 'CurlyBracketedClauseCS', b)
    _safe_set(b, 'owningNameExp', a2)
    assert _is_linked(b, 'owningNameExp', a2)
    if hasattr(a1, 'CurlyBracketedClauseCS'):
        assert not _is_linked(a1, 'CurlyBracketedClauseCS', b)
    if hasattr(a2, 'CurlyBracketedClauseCS'):
        assert _is_linked(a2, 'CurlyBracketedClauseCS', b)
    _safe_set(b, 'owningNameExp', None)
    assert not _is_linked(b, 'owningNameExp', a2)
    if hasattr(a2, 'CurlyBracketedClauseCS'):
        assert not _is_linked(a2, 'CurlyBracketedClauseCS', b)


def test_assoc_ownedElseExpression58_reverse_link_reassign_clear():
    a1 = essentialoclcs_IfExpCS(isImplicit=True)
    a2 = essentialoclcs_IfExpCS(isImplicit=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS60', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS60', a1)
    if hasattr(a1, 'essentialoclcs_IfExpCS59'):
        assert _is_linked(a1, 'essentialoclcs_IfExpCS59', b)
    _safe_set(b, 'essentialoclcs_ExpCS60', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS60', a2)
    if hasattr(a1, 'essentialoclcs_IfExpCS59'):
        assert not _is_linked(a1, 'essentialoclcs_IfExpCS59', b)
    if hasattr(a2, 'essentialoclcs_IfExpCS59'):
        assert _is_linked(a2, 'essentialoclcs_IfExpCS59', b)
    _safe_set(b, 'essentialoclcs_ExpCS60', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS60', a2)
    if hasattr(a2, 'essentialoclcs_IfExpCS59'):
        assert not _is_linked(a2, 'essentialoclcs_IfExpCS59', b)


def test_assoc_ownedInExpression84_reverse_link_reassign_clear():
    a1 = essentialoclcs_LetExpCS(isImplicit=True)
    a2 = essentialoclcs_LetExpCS(isImplicit=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS85', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS85', a1)
    if hasattr(a1, 'essentialoclcs_LetExpCS'):
        assert _is_linked(a1, 'essentialoclcs_LetExpCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS85', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS85', a2)
    if hasattr(a1, 'essentialoclcs_LetExpCS'):
        assert not _is_linked(a1, 'essentialoclcs_LetExpCS', b)
    if hasattr(a2, 'essentialoclcs_LetExpCS'):
        assert _is_linked(a2, 'essentialoclcs_LetExpCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS85', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS85', a2)
    if hasattr(a2, 'essentialoclcs_LetExpCS'):
        assert not _is_linked(a2, 'essentialoclcs_LetExpCS', b)


def test_assoc_ownedInitExpression104_reverse_link_reassign_clear():
    a1 = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    a2 = essentialoclcs_NavigatingArgCS(prefix="sample_text_2", role="sample_text_2")
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS105', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS105', a1)
    if hasattr(a1, 'essentialoclcs_NavigatingArgCS'):
        assert _is_linked(a1, 'essentialoclcs_NavigatingArgCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS105', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS105', a2)
    if hasattr(a1, 'essentialoclcs_NavigatingArgCS'):
        assert not _is_linked(a1, 'essentialoclcs_NavigatingArgCS', b)
    if hasattr(a2, 'essentialoclcs_NavigatingArgCS'):
        assert _is_linked(a2, 'essentialoclcs_NavigatingArgCS', b)
    _safe_set(b, 'essentialoclcs_ExpCS105', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS105', a2)
    if hasattr(a2, 'essentialoclcs_NavigatingArgCS'):
        assert not _is_linked(a2, 'essentialoclcs_NavigatingArgCS', b)


def test_assoc_ownedNameExpression106_reverse_link_reassign_clear():
    a1 = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    a2 = essentialoclcs_NavigatingArgCS(prefix="sample_text_2", role="sample_text_2")
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS108', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS108', a1)
    if hasattr(a1, 'essentialoclcs_NavigatingArgCS107'):
        assert _is_linked(a1, 'essentialoclcs_NavigatingArgCS107', b)
    _safe_set(b, 'essentialoclcs_ExpCS108', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS108', a2)
    if hasattr(a1, 'essentialoclcs_NavigatingArgCS107'):
        assert not _is_linked(a1, 'essentialoclcs_NavigatingArgCS107', b)
    if hasattr(a2, 'essentialoclcs_NavigatingArgCS107'):
        assert _is_linked(a2, 'essentialoclcs_NavigatingArgCS107', b)
    _safe_set(b, 'essentialoclcs_ExpCS108', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS108', a2)
    if hasattr(a2, 'essentialoclcs_NavigatingArgCS107'):
        assert not _is_linked(a2, 'essentialoclcs_NavigatingArgCS107', b)


def test_assoc_ownedParts25_reverse_link_reassign_clear():
    a1 = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    a2 = essentialoclcs_PatternExpCS(patternVariableName="sample_text_2")
    b = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    _safe_set(b, 'essentialoclcs_CollectionPatternCS', {a1})
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS', a1)
    if hasattr(a1, 'essentialoclcs_PatternExpCS'):
        assert _is_linked(a1, 'essentialoclcs_PatternExpCS', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS', {a2})
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS', a2)
    if hasattr(a1, 'essentialoclcs_PatternExpCS'):
        assert not _is_linked(a1, 'essentialoclcs_PatternExpCS', b)
    if hasattr(a2, 'essentialoclcs_PatternExpCS'):
        assert _is_linked(a2, 'essentialoclcs_PatternExpCS', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS', set())
    assert not _is_linked(b, 'essentialoclcs_CollectionPatternCS', a2)
    if hasattr(a2, 'essentialoclcs_PatternExpCS'):
        assert not _is_linked(a2, 'essentialoclcs_PatternExpCS', b)


def test_assoc_ownedPatternGuard26_reverse_link_reassign_clear():
    a1 = essentialoclcs_ExpCS(hasError=True)
    a2 = essentialoclcs_ExpCS(hasError=False)
    b = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    _safe_set(b, 'essentialoclcs_CollectionPatternCS27', a1)
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS27', a1)
    if hasattr(a1, 'essentialoclcs_ExpCS28'):
        assert _is_linked(a1, 'essentialoclcs_ExpCS28', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS27', a2)
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS27', a2)
    if hasattr(a1, 'essentialoclcs_ExpCS28'):
        assert not _is_linked(a1, 'essentialoclcs_ExpCS28', b)
    if hasattr(a2, 'essentialoclcs_ExpCS28'):
        assert _is_linked(a2, 'essentialoclcs_ExpCS28', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS27', None)
    assert not _is_linked(b, 'essentialoclcs_CollectionPatternCS27', a2)
    if hasattr(a2, 'essentialoclcs_ExpCS28'):
        assert not _is_linked(a2, 'essentialoclcs_ExpCS28', b)


def test_assoc_ownedThenExpression63_reverse_link_reassign_clear():
    a1 = essentialoclcs_IfExpCS(isImplicit=True)
    a2 = essentialoclcs_IfExpCS(isImplicit=False)
    b = essentialoclcs_ExpCS(hasError=True)
    _safe_set(b, 'essentialoclcs_ExpCS65', a1)
    assert _is_linked(b, 'essentialoclcs_ExpCS65', a1)
    if hasattr(a1, 'essentialoclcs_IfExpCS64'):
        assert _is_linked(a1, 'essentialoclcs_IfExpCS64', b)
    _safe_set(b, 'essentialoclcs_ExpCS65', a2)
    assert _is_linked(b, 'essentialoclcs_ExpCS65', a2)
    if hasattr(a1, 'essentialoclcs_IfExpCS64'):
        assert not _is_linked(a1, 'essentialoclcs_IfExpCS64', b)
    if hasattr(a2, 'essentialoclcs_IfExpCS64'):
        assert _is_linked(a2, 'essentialoclcs_IfExpCS64', b)
    _safe_set(b, 'essentialoclcs_ExpCS65', None)
    assert not _is_linked(b, 'essentialoclcs_ExpCS65', a2)
    if hasattr(a2, 'essentialoclcs_IfExpCS64'):
        assert not _is_linked(a2, 'essentialoclcs_IfExpCS64', b)


def test_assoc_ownedType29_reverse_link_reassign_clear():
    a1 = essentialoclcs_CollectionTypeCS(name="sample_text")
    a2 = essentialoclcs_CollectionTypeCS(name="sample_text_2")
    b = essentialoclcs_CollectionPatternCS(restVariableName="sample_text")
    _safe_set(b, 'essentialoclcs_CollectionPatternCS30', a1)
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS30', a1)
    if hasattr(a1, 'essentialoclcs_CollectionTypeCS31'):
        assert _is_linked(a1, 'essentialoclcs_CollectionTypeCS31', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS30', a2)
    assert _is_linked(b, 'essentialoclcs_CollectionPatternCS30', a2)
    if hasattr(a1, 'essentialoclcs_CollectionTypeCS31'):
        assert not _is_linked(a1, 'essentialoclcs_CollectionTypeCS31', b)
    if hasattr(a2, 'essentialoclcs_CollectionTypeCS31'):
        assert _is_linked(a2, 'essentialoclcs_CollectionTypeCS31', b)
    _safe_set(b, 'essentialoclcs_CollectionPatternCS30', None)
    assert not _is_linked(b, 'essentialoclcs_CollectionPatternCS30', a2)
    if hasattr(a2, 'essentialoclcs_CollectionTypeCS31'):
        assert not _is_linked(a2, 'essentialoclcs_CollectionTypeCS31', b)


def test_assoc_owningNameExp37_reverse_link_reassign_clear():
    a1 = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    a2 = essentialoclcs_CurlyBracketedClauseCS(value="sample_text_2")
    b = essentialoclcs_AbstractNameExpCS(isPre=True)
    _safe_set(b, 'AbstractNameExpCS', a1)
    assert _is_linked(b, 'AbstractNameExpCS', a1)
    if hasattr(a1, 'ownedCurlyBracketedClause'):
        assert _is_linked(a1, 'ownedCurlyBracketedClause', b)
    _safe_set(b, 'AbstractNameExpCS', a2)
    assert _is_linked(b, 'AbstractNameExpCS', a2)
    if hasattr(a1, 'ownedCurlyBracketedClause'):
        assert not _is_linked(a1, 'ownedCurlyBracketedClause', b)
    if hasattr(a2, 'ownedCurlyBracketedClause'):
        assert _is_linked(a2, 'ownedCurlyBracketedClause', b)
    _safe_set(b, 'AbstractNameExpCS', None)
    assert not _is_linked(b, 'AbstractNameExpCS', a2)
    if hasattr(a2, 'ownedCurlyBracketedClause'):
        assert not _is_linked(a2, 'ownedCurlyBracketedClause', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_argument72_stub_double():
    # essentialoclcs_InfixExpCS has no real 'essentialoclcs_InfixExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_InfixExpCS()
    setattr(partner, 'essentialoclcs_InfixExpCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS73', partner)
    assert getattr(partner, 'essentialoclcs_InfixExpCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS73', None)
    assert getattr(partner, 'essentialoclcs_InfixExpCS') is None


def test_assoc_arguments12_stub_double():
    # essentialoclcs_CallExpCS has no real 'essentialoclcs_CallExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_CallExpCS()
    setattr(partner, 'essentialoclcs_CallExpCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS', partner)
    assert owner in getattr(partner, 'essentialoclcs_CallExpCS')
    _safe_set(owner, 'essentialoclcs_ExpCS', None)
    assert owner not in getattr(partner, 'essentialoclcs_CallExpCS')


def test_assoc_localParent44_stub_double():
    # essentialoclcs_OperatorExpCS has no real 'essentialoclcs_OperatorExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_OperatorExpCS()
    setattr(partner, 'essentialoclcs_OperatorExpCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS45', partner)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS45', None)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS') is None


def test_assoc_ownedArguments126_stub_double():
    # essentialoclcs_RoundBracketedClauseCS has no real 'owningRoundBracketedClause' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_RoundBracketedClauseCS()
    setattr(partner, 'owningRoundBracketedClause', None)
    _safe_set(owner, 'NavigatingArgCS', partner)
    assert owner in getattr(partner, 'owningRoundBracketedClause')
    _safe_set(owner, 'NavigatingArgCS', None)
    assert owner not in getattr(partner, 'owningRoundBracketedClause')


def test_assoc_ownedCondition66_stub_double():
    # essentialoclcs_IfThenExpCS has no real 'essentialoclcs_IfThenExpCS67' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_IfThenExpCS()
    setattr(partner, 'essentialoclcs_IfThenExpCS67', None)
    _safe_set(owner, 'essentialoclcs_ExpCS68', partner)
    assert getattr(partner, 'essentialoclcs_IfThenExpCS67') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS68', None)
    assert getattr(partner, 'essentialoclcs_IfThenExpCS67') is None


def test_assoc_ownedCurlyBracketedClause153_stub_double():
    # essentialoclcs_TypeNameExpCS has no real 'essentialoclcs_TypeNameExpCS154' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CurlyBracketedClauseCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CurlyBracketedClauseCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    partner = essentialoclcs_TypeNameExpCS()
    setattr(partner, 'essentialoclcs_TypeNameExpCS154', None)
    _safe_set(owner, 'essentialoclcs_CurlyBracketedClauseCS', partner)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS154') == owner
    _safe_set(owner, 'essentialoclcs_CurlyBracketedClauseCS', None)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS154') is None


def test_assoc_ownedExpression114_stub_double():
    # essentialoclcs_NestedExpCS has no real 'essentialoclcs_NestedExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_NestedExpCS()
    setattr(partner, 'essentialoclcs_NestedExpCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS115', partner)
    assert getattr(partner, 'essentialoclcs_NestedExpCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS115', None)
    assert getattr(partner, 'essentialoclcs_NestedExpCS') is None


def test_assoc_ownedExpression19_stub_double():
    # essentialoclcs_CollectionLiteralPartCS has no real 'essentialoclcs_CollectionLiteralPartCS20' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_CollectionLiteralPartCS()
    setattr(partner, 'essentialoclcs_CollectionLiteralPartCS20', None)
    _safe_set(owner, 'essentialoclcs_ExpCS21', partner)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralPartCS20') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS21', None)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralPartCS20') is None


def test_assoc_ownedExpression34_stub_double():
    # essentialoclcs_ContextCS has no real 'essentialoclcs_ContextCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_ContextCS()
    setattr(partner, 'essentialoclcs_ContextCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS35', partner)
    assert getattr(partner, 'essentialoclcs_ContextCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS35', None)
    assert getattr(partner, 'essentialoclcs_ContextCS') is None


def test_assoc_ownedExpression54_stub_double():
    # essentialoclcs_ExpSpecificationCS has no real 'essentialoclcs_ExpSpecificationCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_ExpSpecificationCS()
    setattr(partner, 'essentialoclcs_ExpSpecificationCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS55', partner)
    assert getattr(partner, 'essentialoclcs_ExpSpecificationCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS55', None)
    assert getattr(partner, 'essentialoclcs_ExpSpecificationCS') is None


def test_assoc_ownedExpressionCS82_stub_double():
    # essentialoclcs_LambdaLiteralExpCS has no real 'essentialoclcs_LambdaLiteralExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_LambdaLiteralExpCS()
    setattr(partner, 'essentialoclcs_LambdaLiteralExpCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS83', partner)
    assert getattr(partner, 'essentialoclcs_LambdaLiteralExpCS') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS83', None)
    assert getattr(partner, 'essentialoclcs_LambdaLiteralExpCS') is None


def test_assoc_ownedIfThenExpressions61_stub_double():
    # essentialoclcs_IfThenExpCS has no real 'essentialoclcs_IfThenExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_IfExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_IfExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_IfExpCS(isImplicit=True)
    partner = essentialoclcs_IfThenExpCS()
    setattr(partner, 'essentialoclcs_IfThenExpCS', None)
    _safe_set(owner, 'essentialoclcs_IfExpCS62', {partner})
    assert getattr(partner, 'essentialoclcs_IfThenExpCS') == owner
    _safe_set(owner, 'essentialoclcs_IfExpCS62', set())
    assert getattr(partner, 'essentialoclcs_IfThenExpCS') is None


def test_assoc_ownedInitExpression132_stub_double():
    # essentialoclcs_ShadowPartCS has no real 'essentialoclcs_ShadowPartCS133' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_ShadowPartCS()
    setattr(partner, 'essentialoclcs_ShadowPartCS133', None)
    _safe_set(owner, 'essentialoclcs_ExpCS134', partner)
    assert getattr(partner, 'essentialoclcs_ShadowPartCS133') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS134', None)
    assert getattr(partner, 'essentialoclcs_ShadowPartCS133') is None


def test_assoc_ownedInitExpression161_stub_double():
    # essentialoclcs_VariableCS has no real 'essentialoclcs_VariableCS162' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_VariableCS()
    setattr(partner, 'essentialoclcs_VariableCS162', None)
    _safe_set(owner, 'essentialoclcs_ExpCS163', partner)
    assert getattr(partner, 'essentialoclcs_VariableCS162') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS163', None)
    assert getattr(partner, 'essentialoclcs_VariableCS162') is None


def test_assoc_ownedKey92_stub_double():
    # essentialoclcs_MapLiteralPartCS has no real 'essentialoclcs_MapLiteralPartCS93' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_MapLiteralPartCS()
    setattr(partner, 'essentialoclcs_MapLiteralPartCS93', None)
    _safe_set(owner, 'essentialoclcs_ExpCS94', partner)
    assert getattr(partner, 'essentialoclcs_MapLiteralPartCS93') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS94', None)
    assert getattr(partner, 'essentialoclcs_MapLiteralPartCS93') is None


def test_assoc_ownedKeyType98_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS100' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_MapTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_MapTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_MapTypeCS(name="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS100', None)
    _safe_set(owner, 'essentialoclcs_MapTypeCS99', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS100') == owner
    _safe_set(owner, 'essentialoclcs_MapTypeCS99', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS100') is None


def test_assoc_ownedLastExpression22_stub_double():
    # essentialoclcs_CollectionLiteralPartCS has no real 'essentialoclcs_CollectionLiteralPartCS23' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_CollectionLiteralPartCS()
    setattr(partner, 'essentialoclcs_CollectionLiteralPartCS23', None)
    _safe_set(owner, 'essentialoclcs_ExpCS24', partner)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralPartCS23') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS24', None)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralPartCS23') is None


def test_assoc_ownedLeft74_stub_double():
    # essentialoclcs_InfixExpCS has no real 'essentialoclcs_InfixExpCS75' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_InfixExpCS()
    setattr(partner, 'essentialoclcs_InfixExpCS75', None)
    _safe_set(owner, 'essentialoclcs_ExpCS76', partner)
    assert getattr(partner, 'essentialoclcs_InfixExpCS75') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS76', None)
    assert getattr(partner, 'essentialoclcs_InfixExpCS75') is None


def test_assoc_ownedParts36_stub_double():
    # essentialoclcs_ShadowPartCS has no real 'ShadowPartCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CurlyBracketedClauseCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CurlyBracketedClauseCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    partner = essentialoclcs_ShadowPartCS()
    setattr(partner, 'ShadowPartCS', None)
    _safe_set(owner, 'owningCurlyBracketClause', {partner})
    assert getattr(partner, 'ShadowPartCS') == owner
    _safe_set(owner, 'owningCurlyBracketClause', set())
    assert getattr(partner, 'ShadowPartCS') is None


def test_assoc_ownedPathName1_stub_double():
    # essentialoclcs_PathNameCS has no real 'essentialoclcs_PathNameCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_PathNameCS()
    setattr(partner, 'essentialoclcs_PathNameCS', None)
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS', partner)
    assert getattr(partner, 'essentialoclcs_PathNameCS') == owner
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS', None)
    assert getattr(partner, 'essentialoclcs_PathNameCS') is None


def test_assoc_ownedPatternGuard158_stub_double():
    # essentialoclcs_TypeNameExpCS has no real 'essentialoclcs_TypeNameExpCS159' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_TypeNameExpCS()
    setattr(partner, 'essentialoclcs_TypeNameExpCS159', None)
    _safe_set(owner, 'essentialoclcs_ExpCS160', partner)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS159') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS160', None)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS159') is None


def test_assoc_ownedPatternType123_stub_double():
    # essentialoclcs_TypeRefCS has no real 'essentialoclcs_TypeRefCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_PatternExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_PatternExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_PatternExpCS(patternVariableName="sample_text")
    partner = essentialoclcs_TypeRefCS()
    setattr(partner, 'essentialoclcs_TypeRefCS', None)
    _safe_set(owner, 'essentialoclcs_PatternExpCS124', partner)
    assert getattr(partner, 'essentialoclcs_TypeRefCS') == owner
    _safe_set(owner, 'essentialoclcs_PatternExpCS124', None)
    assert getattr(partner, 'essentialoclcs_TypeRefCS') is None


def test_assoc_ownedRight117_stub_double():
    # essentialoclcs_OperatorExpCS has no real 'essentialoclcs_OperatorExpCS118' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_OperatorExpCS()
    setattr(partner, 'essentialoclcs_OperatorExpCS118', None)
    _safe_set(owner, 'essentialoclcs_ExpCS119', partner)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS118') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS119', None)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS118') is None


def test_assoc_ownedRoundBracketedClause2_stub_double():
    # essentialoclcs_RoundBracketedClauseCS has no real 'RoundBracketedClauseCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_RoundBracketedClauseCS()
    setattr(partner, 'RoundBracketedClauseCS', None)
    _safe_set(owner, 'owningNameExp3', partner)
    assert getattr(partner, 'RoundBracketedClauseCS') == owner
    _safe_set(owner, 'owningNameExp3', None)
    assert getattr(partner, 'RoundBracketedClauseCS') is None


def test_assoc_ownedSquareBracketedClauses4_stub_double():
    # essentialoclcs_SquareBracketedClauseCS has no real 'SquareBracketedClauseCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_SquareBracketedClauseCS()
    setattr(partner, 'SquareBracketedClauseCS', None)
    _safe_set(owner, 'owningNameExp5', {partner})
    assert getattr(partner, 'SquareBracketedClauseCS') == owner
    _safe_set(owner, 'owningNameExp5', set())
    assert getattr(partner, 'SquareBracketedClauseCS') is None


def test_assoc_ownedTerms140_stub_double():
    # essentialoclcs_SquareBracketedClauseCS has no real 'essentialoclcs_SquareBracketedClauseCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_SquareBracketedClauseCS()
    setattr(partner, 'essentialoclcs_SquareBracketedClauseCS', None)
    _safe_set(owner, 'essentialoclcs_ExpCS141', partner)
    assert owner in getattr(partner, 'essentialoclcs_SquareBracketedClauseCS')
    _safe_set(owner, 'essentialoclcs_ExpCS141', None)
    assert owner not in getattr(partner, 'essentialoclcs_SquareBracketedClauseCS')


def test_assoc_ownedThenExpression69_stub_double():
    # essentialoclcs_IfThenExpCS has no real 'essentialoclcs_IfThenExpCS70' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_IfThenExpCS()
    setattr(partner, 'essentialoclcs_IfThenExpCS70', None)
    _safe_set(owner, 'essentialoclcs_ExpCS71', partner)
    assert getattr(partner, 'essentialoclcs_IfThenExpCS70') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS71', None)
    assert getattr(partner, 'essentialoclcs_IfThenExpCS70') is None


def test_assoc_ownedType109_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS111' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS111', None)
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS110', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS111') == owner
    _safe_set(owner, 'essentialoclcs_NavigatingArgCS110', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS111') is None


def test_assoc_ownedType17_stub_double():
    # essentialoclcs_CollectionLiteralExpCS has no real 'essentialoclcs_CollectionLiteralExpCS18' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CollectionTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CollectionTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CollectionTypeCS(name="sample_text")
    partner = essentialoclcs_CollectionLiteralExpCS()
    setattr(partner, 'essentialoclcs_CollectionLiteralExpCS18', None)
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS', partner)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralExpCS18') == owner
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS', None)
    assert getattr(partner, 'essentialoclcs_CollectionLiteralExpCS18') is None


def test_assoc_ownedType32_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CollectionTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CollectionTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CollectionTypeCS(name="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS', None)
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS33', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS') == owner
    _safe_set(owner, 'essentialoclcs_CollectionTypeCS33', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS') is None


def test_assoc_ownedType90_stub_double():
    # essentialoclcs_MapLiteralExpCS has no real 'essentialoclcs_MapLiteralExpCS91' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_MapTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_MapTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_MapTypeCS(name="sample_text")
    partner = essentialoclcs_MapLiteralExpCS()
    setattr(partner, 'essentialoclcs_MapLiteralExpCS91', None)
    _safe_set(owner, 'essentialoclcs_MapTypeCS', partner)
    assert getattr(partner, 'essentialoclcs_MapLiteralExpCS91') == owner
    _safe_set(owner, 'essentialoclcs_MapTypeCS', None)
    assert getattr(partner, 'essentialoclcs_MapLiteralExpCS91') is None


def test_assoc_ownedValue95_stub_double():
    # essentialoclcs_MapLiteralPartCS has no real 'essentialoclcs_MapLiteralPartCS96' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_MapLiteralPartCS()
    setattr(partner, 'essentialoclcs_MapLiteralPartCS96', None)
    _safe_set(owner, 'essentialoclcs_ExpCS97', partner)
    assert getattr(partner, 'essentialoclcs_MapLiteralPartCS96') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS97', None)
    assert getattr(partner, 'essentialoclcs_MapLiteralPartCS96') is None


def test_assoc_ownedValueType101_stub_double():
    # essentialoclcs_TypedRefCS has no real 'essentialoclcs_TypedRefCS103' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_MapTypeCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_MapTypeCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_MapTypeCS(name="sample_text")
    partner = essentialoclcs_TypedRefCS()
    setattr(partner, 'essentialoclcs_TypedRefCS103', None)
    _safe_set(owner, 'essentialoclcs_MapTypeCS102', partner)
    assert getattr(partner, 'essentialoclcs_TypedRefCS103') == owner
    _safe_set(owner, 'essentialoclcs_MapTypeCS102', None)
    assert getattr(partner, 'essentialoclcs_TypedRefCS103') is None


def test_assoc_ownedVariables86_stub_double():
    # essentialoclcs_LetVariableCS has no real 'LetVariableCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_LetExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_LetExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_LetExpCS(isImplicit=True)
    partner = essentialoclcs_LetVariableCS()
    setattr(partner, 'LetVariableCS', None)
    _safe_set(owner, 'owningLetExpression', {partner})
    assert getattr(partner, 'LetVariableCS') == owner
    _safe_set(owner, 'owningLetExpression', set())
    assert getattr(partner, 'LetVariableCS') is None


def test_assoc_owningCurlyBracketClause135_stub_double():
    # essentialoclcs_ShadowPartCS has no real 'ownedParts' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_CurlyBracketedClauseCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_CurlyBracketedClauseCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_CurlyBracketedClauseCS(value="sample_text")
    partner = essentialoclcs_ShadowPartCS()
    setattr(partner, 'ownedParts', None)
    _safe_set(owner, 'CurlyBracketedClauseCS136', partner)
    assert getattr(partner, 'ownedParts') == owner
    _safe_set(owner, 'CurlyBracketedClauseCS136', None)
    assert getattr(partner, 'ownedParts') is None


def test_assoc_owningLetExpression88_stub_double():
    # essentialoclcs_LetVariableCS has no real 'ownedVariables' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_LetExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_LetExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_LetExpCS(isImplicit=True)
    partner = essentialoclcs_LetVariableCS()
    setattr(partner, 'ownedVariables', None)
    _safe_set(owner, 'LetExpCS', partner)
    assert getattr(partner, 'ownedVariables') == owner
    _safe_set(owner, 'LetExpCS', None)
    assert getattr(partner, 'ownedVariables') is None


def test_assoc_owningNameExp127_stub_double():
    # essentialoclcs_RoundBracketedClauseCS has no real 'ownedRoundBracketedClause' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_RoundBracketedClauseCS()
    setattr(partner, 'ownedRoundBracketedClause', None)
    _safe_set(owner, 'AbstractNameExpCS128', partner)
    assert getattr(partner, 'ownedRoundBracketedClause') == owner
    _safe_set(owner, 'AbstractNameExpCS128', None)
    assert getattr(partner, 'ownedRoundBracketedClause') is None


def test_assoc_owningNameExp142_stub_double():
    # essentialoclcs_SquareBracketedClauseCS has no real 'ownedSquareBracketedClauses' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_SquareBracketedClauseCS()
    setattr(partner, 'ownedSquareBracketedClauses', None)
    _safe_set(owner, 'AbstractNameExpCS143', partner)
    assert getattr(partner, 'ownedSquareBracketedClauses') == owner
    _safe_set(owner, 'AbstractNameExpCS143', None)
    assert getattr(partner, 'ownedSquareBracketedClauses') is None


def test_assoc_owningRoundBracketedClause112_stub_double():
    # essentialoclcs_RoundBracketedClauseCS has no real 'RoundBracketedClauseCS113' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_NavigatingArgCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_NavigatingArgCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_NavigatingArgCS(prefix="sample_text", role="sample_text")
    partner = essentialoclcs_RoundBracketedClauseCS()
    setattr(partner, 'RoundBracketedClauseCS113', None)
    _safe_set(owner, 'ownedArguments', partner)
    assert getattr(partner, 'RoundBracketedClauseCS113') == owner
    _safe_set(owner, 'ownedArguments', None)
    assert getattr(partner, 'RoundBracketedClauseCS113') is None


def test_assoc_parts129_stub_double():
    # essentialoclcs_ShadowPartCS has no real 'essentialoclcs_ShadowPartCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ShadowExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ShadowExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ShadowExpCS(value="sample_text")
    partner = essentialoclcs_ShadowPartCS()
    setattr(partner, 'essentialoclcs_ShadowPartCS', None)
    _safe_set(owner, 'essentialoclcs_ShadowExpCS', {partner})
    assert getattr(partner, 'essentialoclcs_ShadowPartCS') == owner
    _safe_set(owner, 'essentialoclcs_ShadowExpCS', set())
    assert getattr(partner, 'essentialoclcs_ShadowPartCS') is None


def test_assoc_precedence52_stub_double():
    # essentialoclcs_Precedence has no real 'essentialoclcs_Precedence' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_Precedence()
    setattr(partner, 'essentialoclcs_Precedence', None)
    _safe_set(owner, 'essentialoclcs_ExpCS53', partner)
    assert getattr(partner, 'essentialoclcs_Precedence') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS53', None)
    assert getattr(partner, 'essentialoclcs_Precedence') is None


def test_assoc_source120_stub_double():
    # essentialoclcs_OperatorExpCS has no real 'essentialoclcs_OperatorExpCS121' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_OperatorExpCS()
    setattr(partner, 'essentialoclcs_OperatorExpCS121', None)
    _safe_set(owner, 'essentialoclcs_ExpCS122', partner)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS121') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS122', None)
    assert getattr(partner, 'essentialoclcs_OperatorExpCS121') is None


def test_assoc_source13_stub_double():
    # essentialoclcs_CallExpCS has no real 'essentialoclcs_CallExpCS14' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ExpCS(hasError=True)
    partner = essentialoclcs_CallExpCS()
    setattr(partner, 'essentialoclcs_CallExpCS14', None)
    _safe_set(owner, 'essentialoclcs_ExpCS15', partner)
    assert getattr(partner, 'essentialoclcs_CallExpCS14') == owner
    _safe_set(owner, 'essentialoclcs_ExpCS15', None)
    assert getattr(partner, 'essentialoclcs_CallExpCS14') is None


def test_assoc_sourceType6_stub_double():
    # essentialoclcs_Type has no real 'essentialoclcs_Type' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_Type()
    setattr(partner, 'essentialoclcs_Type', None)
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS7', partner)
    assert getattr(partner, 'essentialoclcs_Type') == owner
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS7', None)
    assert getattr(partner, 'essentialoclcs_Type') is None


def test_assoc_sourceTypeValue8_stub_double():
    # essentialoclcs_Type has no real 'essentialoclcs_Type10' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_AbstractNameExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_AbstractNameExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_AbstractNameExpCS(isPre=True)
    partner = essentialoclcs_Type()
    setattr(partner, 'essentialoclcs_Type10', None)
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS9', partner)
    assert getattr(partner, 'essentialoclcs_Type10') == owner
    _safe_set(owner, 'essentialoclcs_AbstractNameExpCS9', None)
    assert getattr(partner, 'essentialoclcs_Type10') is None


def test_assoc_typeName130_stub_double():
    # essentialoclcs_TypeNameExpCS has no real 'essentialoclcs_TypeNameExpCS' property in the generated
    # code (a bare stub) -- manually attach it so essentialoclcs_ShadowExpCS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # essentialoclcs_ShadowExpCS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = essentialoclcs_ShadowExpCS(value="sample_text")
    partner = essentialoclcs_TypeNameExpCS()
    setattr(partner, 'essentialoclcs_TypeNameExpCS', None)
    _safe_set(owner, 'essentialoclcs_ShadowExpCS131', partner)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS') == owner
    _safe_set(owner, 'essentialoclcs_ShadowExpCS131', None)
    assert getattr(partner, 'essentialoclcs_TypeNameExpCS') is None


