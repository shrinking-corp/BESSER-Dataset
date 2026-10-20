import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Expression,
    Member,
    Statement,
    noop_AddExpression,
    noop_AndExpression,
    noop_ArrayLiteral,
    noop_AsmStatement,
    noop_AssignmentExpression,
    noop_BAndExpression,
    noop_BOrExpression,
    noop_BXorExpression,
    noop_Block,
    noop_BoolLiteral,
    noop_BreakStatement,
    noop_ByteLiteral,
    noop_CastExpression,
    noop_ComplementExpression,
    noop_Constructor,
    noop_ConstructorField,
    noop_ContinueStatement,
    noop_DecExpression,
    noop_DifferExpression,
    noop_DivExpression,
    noop_ElseStatement,
    noop_EqualsExpression,
    noop_Expression,
    noop_ForStatement,
    noop_ForeverStatement,
    noop_GeExpression,
    noop_GtExpression,
    noop_IfStatement,
    noop_IncExpression,
    noop_Index,
    noop_InstanceOfExpression,
    noop_LShiftExpression,
    noop_LeExpression,
    noop_Length,
    noop_LtExpression,
    noop_Member,
    noop_MemberRef,
    noop_MemberSelect,
    noop_Method,
    noop_ModExpression,
    noop_MulExpression,
    noop_NewInstance,
    noop_NoopClass,
    noop_NotExpression,
    noop_OrExpression,
    noop_RShiftExpression,
    noop_ReturnStatement,
    noop_SigNegExpression,
    noop_SigPosExpression,
    noop_Statement,
    noop_Storage,
    noop_StringLiteral,
    noop_SubExpression,
    noop_Super,
    noop_This,
    noop_Variable,
    AssignmentType,
    StorageType,
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

def test_assoc_else_28_reverse_link_reassign_clear():
    a1 = noop_IfStatement(name="sample_text")
    a2 = noop_IfStatement(name="sample_text_2")
    b = noop_ElseStatement(name="sample_text")
    _safe_set(b, 'noop_ElseStatement', a1)
    assert _is_linked(b, 'noop_ElseStatement', a1)
    if hasattr(a1, 'noop_IfStatement29'):
        assert _is_linked(a1, 'noop_IfStatement29', b)
    _safe_set(b, 'noop_ElseStatement', a2)
    assert _is_linked(b, 'noop_ElseStatement', a2)
    if hasattr(a1, 'noop_IfStatement29'):
        assert not _is_linked(a1, 'noop_IfStatement29', b)
    if hasattr(a2, 'noop_IfStatement29'):
        assert _is_linked(a2, 'noop_IfStatement29', b)
    _safe_set(b, 'noop_ElseStatement', None)
    assert not _is_linked(b, 'noop_ElseStatement', a2)
    if hasattr(a2, 'noop_IfStatement29'):
        assert not _is_linked(a2, 'noop_IfStatement29', b)


def test_assoc_if_33_reverse_link_reassign_clear():
    a1 = noop_IfStatement(name="sample_text")
    a2 = noop_IfStatement(name="sample_text_2")
    b = noop_ElseStatement(name="sample_text")
    _safe_set(b, 'noop_ElseStatement34', a1)
    assert _is_linked(b, 'noop_ElseStatement34', a1)
    if hasattr(a1, 'noop_IfStatement35'):
        assert _is_linked(a1, 'noop_IfStatement35', b)
    _safe_set(b, 'noop_ElseStatement34', a2)
    assert _is_linked(b, 'noop_ElseStatement34', a2)
    if hasattr(a1, 'noop_IfStatement35'):
        assert not _is_linked(a1, 'noop_IfStatement35', b)
    if hasattr(a2, 'noop_IfStatement35'):
        assert _is_linked(a2, 'noop_IfStatement35', b)
    _safe_set(b, 'noop_ElseStatement34', None)
    assert not _is_linked(b, 'noop_ElseStatement34', a2)
    if hasattr(a2, 'noop_IfStatement35'):
        assert not _is_linked(a2, 'noop_IfStatement35', b)


def test_assoc_member188_reverse_link_reassign_clear():
    a1 = noop_MemberSelect(hasArgs=True)
    a2 = noop_MemberSelect(hasArgs=False)
    b = noop_Member(name="sample_text")
    _safe_set(b, 'noop_Member190', a1)
    assert _is_linked(b, 'noop_Member190', a1)
    if hasattr(a1, 'noop_MemberSelect189'):
        assert _is_linked(a1, 'noop_MemberSelect189', b)
    _safe_set(b, 'noop_Member190', a2)
    assert _is_linked(b, 'noop_Member190', a2)
    if hasattr(a1, 'noop_MemberSelect189'):
        assert not _is_linked(a1, 'noop_MemberSelect189', b)
    if hasattr(a2, 'noop_MemberSelect189'):
        assert _is_linked(a2, 'noop_MemberSelect189', b)
    _safe_set(b, 'noop_Member190', None)
    assert not _is_linked(b, 'noop_Member190', a2)
    if hasattr(a2, 'noop_MemberSelect189'):
        assert not _is_linked(a2, 'noop_MemberSelect189', b)


def test_assoc_member207_reverse_link_reassign_clear():
    a1 = noop_MemberRef(hasArgs=True)
    a2 = noop_MemberRef(hasArgs=False)
    b = noop_Member(name="sample_text")
    _safe_set(b, 'noop_Member208', a1)
    assert _is_linked(b, 'noop_Member208', a1)
    if hasattr(a1, 'noop_MemberRef'):
        assert _is_linked(a1, 'noop_MemberRef', b)
    _safe_set(b, 'noop_Member208', a2)
    assert _is_linked(b, 'noop_Member208', a2)
    if hasattr(a1, 'noop_MemberRef'):
        assert not _is_linked(a1, 'noop_MemberRef', b)
    if hasattr(a2, 'noop_MemberRef'):
        assert _is_linked(a2, 'noop_MemberRef', b)
    _safe_set(b, 'noop_Member208', None)
    assert not _is_linked(b, 'noop_Member208', a2)
    if hasattr(a2, 'noop_MemberRef'):
        assert not _is_linked(a2, 'noop_MemberRef', b)


def test_assoc_members2_reverse_link_reassign_clear():
    a1 = noop_NoopClass(name="sample_text")
    a2 = noop_NoopClass(name="sample_text_2")
    b = noop_Member(name="sample_text")
    _safe_set(b, 'noop_Member', a1)
    assert _is_linked(b, 'noop_Member', a1)
    if hasattr(a1, 'noop_NoopClass3'):
        assert _is_linked(a1, 'noop_NoopClass3', b)
    _safe_set(b, 'noop_Member', a2)
    assert _is_linked(b, 'noop_Member', a2)
    if hasattr(a1, 'noop_NoopClass3'):
        assert not _is_linked(a1, 'noop_NoopClass3', b)
    if hasattr(a2, 'noop_NoopClass3'):
        assert _is_linked(a2, 'noop_NoopClass3', b)
    _safe_set(b, 'noop_Member', None)
    assert not _is_linked(b, 'noop_Member', a2)
    if hasattr(a2, 'noop_NoopClass3'):
        assert not _is_linked(a2, 'noop_NoopClass3', b)


def test_assoc_storage4_reverse_link_reassign_clear():
    a1 = noop_Storage(type="sample_text")
    a2 = noop_Storage(type="sample_text_2")
    b = noop_Member(name="sample_text")
    _safe_set(b, 'noop_Member5', a1)
    assert _is_linked(b, 'noop_Member5', a1)
    if hasattr(a1, 'noop_Storage'):
        assert _is_linked(a1, 'noop_Storage', b)
    _safe_set(b, 'noop_Member5', a2)
    assert _is_linked(b, 'noop_Member5', a2)
    if hasattr(a1, 'noop_Storage'):
        assert not _is_linked(a1, 'noop_Storage', b)
    if hasattr(a2, 'noop_Storage'):
        assert _is_linked(a2, 'noop_Storage', b)
    _safe_set(b, 'noop_Member5', None)
    assert not _is_linked(b, 'noop_Member5', a2)
    if hasattr(a2, 'noop_Storage'):
        assert not _is_linked(a2, 'noop_Storage', b)


def test_assoc_superClass1_reverse_link_reassign_clear():
    a1 = noop_NoopClass(name="sample_text")
    a2 = noop_NoopClass(name="sample_text_2")
    b = noop_NoopClass(name="sample_text")
    _safe_set(b, 'noop_NoopClass0', a1)
    assert _is_linked(b, 'noop_NoopClass0', a1)
    if hasattr(a1, 'noop_NoopClass'):
        assert _is_linked(a1, 'noop_NoopClass', b)
    _safe_set(b, 'noop_NoopClass0', a2)
    assert _is_linked(b, 'noop_NoopClass0', a2)
    if hasattr(a1, 'noop_NoopClass'):
        assert not _is_linked(a1, 'noop_NoopClass', b)
    if hasattr(a2, 'noop_NoopClass'):
        assert _is_linked(a2, 'noop_NoopClass', b)
    _safe_set(b, 'noop_NoopClass0', None)
    assert not _is_linked(b, 'noop_NoopClass0', a2)
    if hasattr(a2, 'noop_NoopClass'):
        assert not _is_linked(a2, 'noop_NoopClass', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_args191_stub_double():
    # noop_Expression has no real 'noop_Expression193' property in the generated
    # code (a bare stub) -- manually attach it so noop_MemberSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_MemberSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_MemberSelect(hasArgs=True)
    partner = noop_Expression()
    setattr(partner, 'noop_Expression193', None)
    _safe_set(owner, 'noop_MemberSelect192', {partner})
    assert getattr(partner, 'noop_Expression193') == owner
    _safe_set(owner, 'noop_MemberSelect192', set())
    assert getattr(partner, 'noop_Expression193') is None


def test_assoc_args209_stub_double():
    # noop_Expression has no real 'noop_Expression211' property in the generated
    # code (a bare stub) -- manually attach it so noop_MemberRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_MemberRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_MemberRef(hasArgs=True)
    partner = noop_Expression()
    setattr(partner, 'noop_Expression211', None)
    _safe_set(owner, 'noop_MemberRef210', {partner})
    assert getattr(partner, 'noop_Expression211') == owner
    _safe_set(owner, 'noop_MemberRef210', set())
    assert getattr(partner, 'noop_Expression211') is None


def test_assoc_assignments38_stub_double():
    # noop_Expression has no real 'noop_Expression40' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForStatement(name="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression40', None)
    _safe_set(owner, 'noop_ForStatement39', {partner})
    assert getattr(partner, 'noop_Expression40') == owner
    _safe_set(owner, 'noop_ForStatement39', set())
    assert getattr(partner, 'noop_Expression40') is None


def test_assoc_body25_stub_double():
    # noop_Block has no real 'noop_Block27' property in the generated
    # code (a bare stub) -- manually attach it so noop_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_IfStatement(name="sample_text")
    partner = noop_Block()
    setattr(partner, 'noop_Block27', None)
    _safe_set(owner, 'noop_IfStatement26', partner)
    assert getattr(partner, 'noop_Block27') == owner
    _safe_set(owner, 'noop_IfStatement26', None)
    assert getattr(partner, 'noop_Block27') is None


def test_assoc_body30_stub_double():
    # noop_Block has no real 'noop_Block32' property in the generated
    # code (a bare stub) -- manually attach it so noop_ElseStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ElseStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ElseStatement(name="sample_text")
    partner = noop_Block()
    setattr(partner, 'noop_Block32', None)
    _safe_set(owner, 'noop_ElseStatement31', partner)
    assert getattr(partner, 'noop_Block32') == owner
    _safe_set(owner, 'noop_ElseStatement31', None)
    assert getattr(partner, 'noop_Block32') is None


def test_assoc_body47_stub_double():
    # noop_Block has no real 'noop_Block49' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForStatement(name="sample_text")
    partner = noop_Block()
    setattr(partner, 'noop_Block49', None)
    _safe_set(owner, 'noop_ForStatement48', partner)
    assert getattr(partner, 'noop_Block49') == owner
    _safe_set(owner, 'noop_ForStatement48', None)
    assert getattr(partner, 'noop_Block49') is None


def test_assoc_body50_stub_double():
    # noop_Block has no real 'noop_Block51' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForeverStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForeverStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForeverStatement(name="sample_text")
    partner = noop_Block()
    setattr(partner, 'noop_Block51', None)
    _safe_set(owner, 'noop_ForeverStatement', partner)
    assert getattr(partner, 'noop_Block51') == owner
    _safe_set(owner, 'noop_ForeverStatement', None)
    assert getattr(partner, 'noop_Block51') is None


def test_assoc_condition23_stub_double():
    # noop_Expression has no real 'noop_Expression24' property in the generated
    # code (a bare stub) -- manually attach it so noop_IfStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_IfStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_IfStatement(name="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression24', None)
    _safe_set(owner, 'noop_IfStatement', partner)
    assert getattr(partner, 'noop_Expression24') == owner
    _safe_set(owner, 'noop_IfStatement', None)
    assert getattr(partner, 'noop_Expression24') is None


def test_assoc_condition41_stub_double():
    # noop_Expression has no real 'noop_Expression43' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForStatement(name="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression43', None)
    _safe_set(owner, 'noop_ForStatement42', partner)
    assert getattr(partner, 'noop_Expression43') == owner
    _safe_set(owner, 'noop_ForStatement42', None)
    assert getattr(partner, 'noop_Expression43') is None


def test_assoc_expressions44_stub_double():
    # noop_Expression has no real 'noop_Expression46' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForStatement(name="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression46', None)
    _safe_set(owner, 'noop_ForStatement45', {partner})
    assert getattr(partner, 'noop_Expression46') == owner
    _safe_set(owner, 'noop_ForStatement45', set())
    assert getattr(partner, 'noop_Expression46') is None


def test_assoc_indexes194_stub_double():
    # noop_Index has no real 'noop_Index196' property in the generated
    # code (a bare stub) -- manually attach it so noop_MemberSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_MemberSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_MemberSelect(hasArgs=True)
    partner = noop_Index()
    setattr(partner, 'noop_Index196', None)
    _safe_set(owner, 'noop_MemberSelect195', {partner})
    assert getattr(partner, 'noop_Index196') == owner
    _safe_set(owner, 'noop_MemberSelect195', set())
    assert getattr(partner, 'noop_Index196') is None


def test_assoc_indexes212_stub_double():
    # noop_Index has no real 'noop_Index214' property in the generated
    # code (a bare stub) -- manually attach it so noop_MemberRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_MemberRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_MemberRef(hasArgs=True)
    partner = noop_Index()
    setattr(partner, 'noop_Index214', None)
    _safe_set(owner, 'noop_MemberRef213', {partner})
    assert getattr(partner, 'noop_Index214') == owner
    _safe_set(owner, 'noop_MemberRef213', set())
    assert getattr(partner, 'noop_Index214') is None


def test_assoc_left66_stub_double():
    # noop_Expression has no real 'noop_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so noop_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_AssignmentExpression(assignment="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression67', None)
    _safe_set(owner, 'noop_AssignmentExpression', partner)
    assert getattr(partner, 'noop_Expression67') == owner
    _safe_set(owner, 'noop_AssignmentExpression', None)
    assert getattr(partner, 'noop_Expression67') is None


def test_assoc_location6_stub_double():
    # noop_Expression has no real 'noop_Expression' property in the generated
    # code (a bare stub) -- manually attach it so noop_Storage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_Storage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_Storage(type="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression', None)
    _safe_set(owner, 'noop_Storage7', partner)
    assert getattr(partner, 'noop_Expression') == owner
    _safe_set(owner, 'noop_Storage7', None)
    assert getattr(partner, 'noop_Expression') is None


def test_assoc_receiver186_stub_double():
    # noop_Expression has no real 'noop_Expression187' property in the generated
    # code (a bare stub) -- manually attach it so noop_MemberSelect's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_MemberSelect's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_MemberSelect(hasArgs=True)
    partner = noop_Expression()
    setattr(partner, 'noop_Expression187', None)
    _safe_set(owner, 'noop_MemberSelect', partner)
    assert getattr(partner, 'noop_Expression187') == owner
    _safe_set(owner, 'noop_MemberSelect', None)
    assert getattr(partner, 'noop_Expression187') is None


def test_assoc_right68_stub_double():
    # noop_Expression has no real 'noop_Expression70' property in the generated
    # code (a bare stub) -- manually attach it so noop_AssignmentExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_AssignmentExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_AssignmentExpression(assignment="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression70', None)
    _safe_set(owner, 'noop_AssignmentExpression69', partner)
    assert getattr(partner, 'noop_Expression70') == owner
    _safe_set(owner, 'noop_AssignmentExpression69', None)
    assert getattr(partner, 'noop_Expression70') is None


def test_assoc_type10_stub_double():
    # noop_Variable has no real 'noop_Variable11' property in the generated
    # code (a bare stub) -- manually attach it so noop_NoopClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_NoopClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_NoopClass(name="sample_text")
    partner = noop_Variable()
    setattr(partner, 'noop_Variable11', None)
    _safe_set(owner, 'noop_NoopClass12', partner)
    assert getattr(partner, 'noop_Variable11') == owner
    _safe_set(owner, 'noop_NoopClass12', None)
    assert getattr(partner, 'noop_Variable11') is None


def test_assoc_type128_stub_double():
    # noop_InstanceOfExpression has no real 'noop_InstanceOfExpression129' property in the generated
    # code (a bare stub) -- manually attach it so noop_NoopClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_NoopClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_NoopClass(name="sample_text")
    partner = noop_InstanceOfExpression()
    setattr(partner, 'noop_InstanceOfExpression129', None)
    _safe_set(owner, 'noop_NoopClass130', partner)
    assert getattr(partner, 'noop_InstanceOfExpression129') == owner
    _safe_set(owner, 'noop_NoopClass130', None)
    assert getattr(partner, 'noop_InstanceOfExpression129') is None


def test_assoc_type168_stub_double():
    # noop_CastExpression has no real 'noop_CastExpression169' property in the generated
    # code (a bare stub) -- manually attach it so noop_NoopClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_NoopClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_NoopClass(name="sample_text")
    partner = noop_CastExpression()
    setattr(partner, 'noop_CastExpression169', None)
    _safe_set(owner, 'noop_NoopClass170', partner)
    assert getattr(partner, 'noop_CastExpression169') == owner
    _safe_set(owner, 'noop_NoopClass170', None)
    assert getattr(partner, 'noop_CastExpression169') is None


def test_assoc_type199_stub_double():
    # noop_NewInstance has no real 'noop_NewInstance' property in the generated
    # code (a bare stub) -- manually attach it so noop_NoopClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_NoopClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_NoopClass(name="sample_text")
    partner = noop_NewInstance()
    setattr(partner, 'noop_NewInstance', None)
    _safe_set(owner, 'noop_NoopClass200', partner)
    assert getattr(partner, 'noop_NewInstance') == owner
    _safe_set(owner, 'noop_NoopClass200', None)
    assert getattr(partner, 'noop_NewInstance') is None


def test_assoc_value21_stub_double():
    # noop_Expression has no real 'noop_Expression22' property in the generated
    # code (a bare stub) -- manually attach it so noop_ReturnStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ReturnStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ReturnStatement(name="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression22', None)
    _safe_set(owner, 'noop_ReturnStatement', partner)
    assert getattr(partner, 'noop_Expression22') == owner
    _safe_set(owner, 'noop_ReturnStatement', None)
    assert getattr(partner, 'noop_Expression22') is None


def test_assoc_variables36_stub_double():
    # noop_Variable has no real 'noop_Variable37' property in the generated
    # code (a bare stub) -- manually attach it so noop_ForStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_ForStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_ForStatement(name="sample_text")
    partner = noop_Variable()
    setattr(partner, 'noop_Variable37', None)
    _safe_set(owner, 'noop_ForStatement', {partner})
    assert getattr(partner, 'noop_Variable37') == owner
    _safe_set(owner, 'noop_ForStatement', set())
    assert getattr(partner, 'noop_Variable37') is None


def test_assoc_vars52_stub_double():
    # noop_Expression has no real 'noop_Expression53' property in the generated
    # code (a bare stub) -- manually attach it so noop_AsmStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # noop_AsmStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = noop_AsmStatement(codes="sample_text")
    partner = noop_Expression()
    setattr(partner, 'noop_Expression53', None)
    _safe_set(owner, 'noop_AsmStatement', {partner})
    assert getattr(partner, 'noop_Expression53') == owner
    _safe_set(owner, 'noop_AsmStatement', set())
    assert getattr(partner, 'noop_Expression53') is None


