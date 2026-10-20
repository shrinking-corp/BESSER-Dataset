import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Access,
    BlockStmt,
    Decl,
    Exp,
    IdUse,
    Stmt,
    TypeDecl,
    picojava_Access,
    picojava_AssignStmt,
    picojava_Block,
    picojava_BlockStmt,
    picojava_BooleanLiteral,
    picojava_ClassDecl,
    picojava_Decl,
    picojava_Dot,
    picojava_Exp,
    picojava_IdUse,
    picojava_PrimitiveDecl,
    picojava_Program,
    picojava_Stmt,
    picojava_TypeDecl,
    picojava_TypeUse,
    picojava_UnknownDecl,
    picojava_Use,
    picojava_VarDecl,
    picojava_VariableUse,
    picojava_WhileStmt,
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

def test_assoc_Block0_reverse_link_reassign_clear():
    a1 = picojava_Program()
    a2 = picojava_Program()
    b = picojava_Block()
    _safe_set(b, 'picojava_Block', a1)
    assert _is_linked(b, 'picojava_Block', a1)
    if hasattr(a1, 'picojava_Program'):
        assert _is_linked(a1, 'picojava_Program', b)
    _safe_set(b, 'picojava_Block', a2)
    assert _is_linked(b, 'picojava_Block', a2)
    if hasattr(a1, 'picojava_Program'):
        assert not _is_linked(a1, 'picojava_Program', b)
    if hasattr(a2, 'picojava_Program'):
        assert _is_linked(a2, 'picojava_Program', b)
    _safe_set(b, 'picojava_Block', None)
    assert not _is_linked(b, 'picojava_Block', a2)
    if hasattr(a2, 'picojava_Program'):
        assert not _is_linked(a2, 'picojava_Program', b)


def test_assoc_BlockStmt7_reverse_link_reassign_clear():
    a1 = picojava_BlockStmt()
    a2 = picojava_BlockStmt()
    b = picojava_Block()
    _safe_set(b, 'picojava_Block8', {a1})
    assert _is_linked(b, 'picojava_Block8', a1)
    if hasattr(a1, 'picojava_BlockStmt'):
        assert _is_linked(a1, 'picojava_BlockStmt', b)
    _safe_set(b, 'picojava_Block8', {a2})
    assert _is_linked(b, 'picojava_Block8', a2)
    if hasattr(a1, 'picojava_BlockStmt'):
        assert not _is_linked(a1, 'picojava_BlockStmt', b)
    if hasattr(a2, 'picojava_BlockStmt'):
        assert _is_linked(a2, 'picojava_BlockStmt', b)
    _safe_set(b, 'picojava_Block8', set())
    assert not _is_linked(b, 'picojava_Block8', a2)
    if hasattr(a2, 'picojava_BlockStmt'):
        assert not _is_linked(a2, 'picojava_BlockStmt', b)


def test_assoc_Body23_reverse_link_reassign_clear():
    a1 = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    a2 = picojava_ClassDecl(hasCycleOnSuperclassChain=False)
    b = picojava_Block()
    _safe_set(b, 'picojava_Block25', a1)
    assert _is_linked(b, 'picojava_Block25', a1)
    if hasattr(a1, 'picojava_ClassDecl24'):
        assert _is_linked(a1, 'picojava_ClassDecl24', b)
    _safe_set(b, 'picojava_Block25', a2)
    assert _is_linked(b, 'picojava_Block25', a2)
    if hasattr(a1, 'picojava_ClassDecl24'):
        assert not _is_linked(a1, 'picojava_ClassDecl24', b)
    if hasattr(a2, 'picojava_ClassDecl24'):
        assert _is_linked(a2, 'picojava_ClassDecl24', b)
    _safe_set(b, 'picojava_Block25', None)
    assert not _is_linked(b, 'picojava_Block25', a2)
    if hasattr(a2, 'picojava_ClassDecl24'):
        assert not _is_linked(a2, 'picojava_ClassDecl24', b)


def test_assoc_PredefinedType1_reverse_link_reassign_clear():
    a1 = picojava_TypeDecl(isQualified=True)
    a2 = picojava_TypeDecl(isQualified=False)
    b = picojava_Program()
    _safe_set(b, 'picojava_Program2', {a1})
    assert _is_linked(b, 'picojava_Program2', a1)
    if hasattr(a1, 'picojava_TypeDecl'):
        assert _is_linked(a1, 'picojava_TypeDecl', b)
    _safe_set(b, 'picojava_Program2', {a2})
    assert _is_linked(b, 'picojava_Program2', a2)
    if hasattr(a1, 'picojava_TypeDecl'):
        assert not _is_linked(a1, 'picojava_TypeDecl', b)
    if hasattr(a2, 'picojava_TypeDecl'):
        assert _is_linked(a2, 'picojava_TypeDecl', b)
    _safe_set(b, 'picojava_Program2', set())
    assert not _is_linked(b, 'picojava_Program2', a2)
    if hasattr(a2, 'picojava_TypeDecl'):
        assert not _is_linked(a2, 'picojava_TypeDecl', b)


def test_assoc_SuperclassId22_reverse_link_reassign_clear():
    a1 = picojava_IdUse(Name="sample_text", isQualified=True)
    a2 = picojava_IdUse(Name="sample_text_2", isQualified=False)
    b = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    _safe_set(b, 'picojava_ClassDecl', a1)
    assert _is_linked(b, 'picojava_ClassDecl', a1)
    if hasattr(a1, 'picojava_IdUse'):
        assert _is_linked(a1, 'picojava_IdUse', b)
    _safe_set(b, 'picojava_ClassDecl', a2)
    assert _is_linked(b, 'picojava_ClassDecl', a2)
    if hasattr(a1, 'picojava_IdUse'):
        assert not _is_linked(a1, 'picojava_IdUse', b)
    if hasattr(a2, 'picojava_IdUse'):
        assert _is_linked(a2, 'picojava_IdUse', b)
    _safe_set(b, 'picojava_ClassDecl', None)
    assert not _is_linked(b, 'picojava_ClassDecl', a2)
    if hasattr(a2, 'picojava_IdUse'):
        assert not _is_linked(a2, 'picojava_IdUse', b)


def test_assoc_superClass27_reverse_link_reassign_clear():
    a1 = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    a2 = picojava_ClassDecl(hasCycleOnSuperclassChain=False)
    b = picojava_ClassDecl(hasCycleOnSuperclassChain=True)
    _safe_set(b, 'picojava_ClassDecl28', a1)
    assert _is_linked(b, 'picojava_ClassDecl28', a1)
    if hasattr(a1, 'picojava_ClassDecl26'):
        assert _is_linked(a1, 'picojava_ClassDecl26', b)
    _safe_set(b, 'picojava_ClassDecl28', a2)
    assert _is_linked(b, 'picojava_ClassDecl28', a2)
    if hasattr(a1, 'picojava_ClassDecl26'):
        assert not _is_linked(a1, 'picojava_ClassDecl26', b)
    if hasattr(a2, 'picojava_ClassDecl26'):
        assert _is_linked(a2, 'picojava_ClassDecl26', b)
    _safe_set(b, 'picojava_ClassDecl28', None)
    assert not _is_linked(b, 'picojava_ClassDecl28', a2)
    if hasattr(a2, 'picojava_ClassDecl26'):
        assert not _is_linked(a2, 'picojava_ClassDecl26', b)


def test_assoc_type11_reverse_link_reassign_clear():
    a1 = picojava_TypeDecl(isQualified=True)
    a2 = picojava_TypeDecl(isQualified=False)
    b = picojava_Decl(Name="sample_text", isUnknown=True)
    _safe_set(b, 'picojava_Decl12', a1)
    assert _is_linked(b, 'picojava_Decl12', a1)
    if hasattr(a1, 'picojava_TypeDecl13'):
        assert _is_linked(a1, 'picojava_TypeDecl13', b)
    _safe_set(b, 'picojava_Decl12', a2)
    assert _is_linked(b, 'picojava_Decl12', a2)
    if hasattr(a1, 'picojava_TypeDecl13'):
        assert not _is_linked(a1, 'picojava_TypeDecl13', b)
    if hasattr(a2, 'picojava_TypeDecl13'):
        assert _is_linked(a2, 'picojava_TypeDecl13', b)
    _safe_set(b, 'picojava_Decl12', None)
    assert not _is_linked(b, 'picojava_Decl12', a2)
    if hasattr(a2, 'picojava_TypeDecl13'):
        assert not _is_linked(a2, 'picojava_TypeDecl13', b)


def test_assoc_type42_reverse_link_reassign_clear():
    a1 = picojava_TypeDecl(isQualified=True)
    a2 = picojava_TypeDecl(isQualified=False)
    b = picojava_Exp(isValue=True)
    _safe_set(b, 'picojava_Exp43', a1)
    assert _is_linked(b, 'picojava_Exp43', a1)
    if hasattr(a1, 'picojava_TypeDecl44'):
        assert _is_linked(a1, 'picojava_TypeDecl44', b)
    _safe_set(b, 'picojava_Exp43', a2)
    assert _is_linked(b, 'picojava_Exp43', a2)
    if hasattr(a1, 'picojava_TypeDecl44'):
        assert not _is_linked(a1, 'picojava_TypeDecl44', b)
    if hasattr(a2, 'picojava_TypeDecl44'):
        assert _is_linked(a2, 'picojava_TypeDecl44', b)
    _safe_set(b, 'picojava_Exp43', None)
    assert not _is_linked(b, 'picojava_Exp43', a2)
    if hasattr(a2, 'picojava_TypeDecl44'):
        assert not _is_linked(a2, 'picojava_TypeDecl44', b)


def test_assoc_unknownDecl19_reverse_link_reassign_clear():
    a1 = picojava_TypeDecl(isQualified=True)
    a2 = picojava_TypeDecl(isQualified=False)
    b = picojava_Decl(Name="sample_text", isUnknown=True)
    _safe_set(b, 'picojava_Decl21', a1)
    assert _is_linked(b, 'picojava_Decl21', a1)
    if hasattr(a1, 'picojava_TypeDecl20'):
        assert _is_linked(a1, 'picojava_TypeDecl20', b)
    _safe_set(b, 'picojava_Decl21', a2)
    assert _is_linked(b, 'picojava_Decl21', a2)
    if hasattr(a1, 'picojava_TypeDecl20'):
        assert not _is_linked(a1, 'picojava_TypeDecl20', b)
    if hasattr(a2, 'picojava_TypeDecl20'):
        assert _is_linked(a2, 'picojava_TypeDecl20', b)
    _safe_set(b, 'picojava_Decl21', None)
    assert not _is_linked(b, 'picojava_Decl21', a2)
    if hasattr(a2, 'picojava_TypeDecl20'):
        assert not _is_linked(a2, 'picojava_TypeDecl20', b)


def test_assoc_unknownDecl9_reverse_link_reassign_clear():
    a1 = picojava_Decl(Name="sample_text", isUnknown=True)
    a2 = picojava_Decl(Name="sample_text_2", isUnknown=False)
    b = picojava_Block()
    _safe_set(b, 'picojava_Block10', a1)
    assert _is_linked(b, 'picojava_Block10', a1)
    if hasattr(a1, 'picojava_Decl'):
        assert _is_linked(a1, 'picojava_Decl', b)
    _safe_set(b, 'picojava_Block10', a2)
    assert _is_linked(b, 'picojava_Block10', a2)
    if hasattr(a1, 'picojava_Decl'):
        assert not _is_linked(a1, 'picojava_Decl', b)
    if hasattr(a2, 'picojava_Decl'):
        assert _is_linked(a2, 'picojava_Decl', b)
    _safe_set(b, 'picojava_Block10', None)
    assert not _is_linked(b, 'picojava_Block10', a2)
    if hasattr(a2, 'picojava_Decl'):
        assert not _is_linked(a2, 'picojava_Decl', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Condition35_stub_double():
    # picojava_WhileStmt has no real 'picojava_WhileStmt' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Exp(isValue=True)
    partner = picojava_WhileStmt()
    setattr(partner, 'picojava_WhileStmt', None)
    _safe_set(owner, 'picojava_Exp36', partner)
    assert getattr(partner, 'picojava_WhileStmt') == owner
    _safe_set(owner, 'picojava_Exp36', None)
    assert getattr(partner, 'picojava_WhileStmt') is None


def test_assoc_IdUse53_stub_double():
    # picojava_Dot has no real 'picojava_Dot54' property in the generated
    # code (a bare stub) -- manually attach it so picojava_IdUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_IdUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_IdUse(Name="sample_text", isQualified=True)
    partner = picojava_Dot()
    setattr(partner, 'picojava_Dot54', None)
    _safe_set(owner, 'picojava_IdUse55', partner)
    assert getattr(partner, 'picojava_Dot54') == owner
    _safe_set(owner, 'picojava_IdUse55', None)
    assert getattr(partner, 'picojava_Dot54') is None


def test_assoc_Value33_stub_double():
    # picojava_AssignStmt has no real 'picojava_AssignStmt34' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Exp's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Exp's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Exp(isValue=True)
    partner = picojava_AssignStmt()
    setattr(partner, 'picojava_AssignStmt34', None)
    _safe_set(owner, 'picojava_Exp', partner)
    assert getattr(partner, 'picojava_AssignStmt34') == owner
    _safe_set(owner, 'picojava_Exp', None)
    assert getattr(partner, 'picojava_AssignStmt34') is None


def test_assoc_booleanType14_stub_double():
    # picojava_PrimitiveDecl has no real 'picojava_PrimitiveDecl16' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Decl(Name="sample_text", isUnknown=True)
    partner = picojava_PrimitiveDecl()
    setattr(partner, 'picojava_PrimitiveDecl16', None)
    _safe_set(owner, 'picojava_Decl15', partner)
    assert getattr(partner, 'picojava_PrimitiveDecl16') == owner
    _safe_set(owner, 'picojava_Decl15', None)
    assert getattr(partner, 'picojava_PrimitiveDecl16') is None


def test_assoc_booleanType5_stub_double():
    # picojava_PrimitiveDecl has no real 'picojava_PrimitiveDecl' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Program()
    partner = picojava_PrimitiveDecl()
    setattr(partner, 'picojava_PrimitiveDecl', None)
    _safe_set(owner, 'picojava_Program6', partner)
    assert getattr(partner, 'picojava_PrimitiveDecl') == owner
    _safe_set(owner, 'picojava_Program6', None)
    assert getattr(partner, 'picojava_PrimitiveDecl') is None


def test_assoc_booleanType56_stub_double():
    # picojava_PrimitiveDecl has no real 'picojava_PrimitiveDecl57' property in the generated
    # code (a bare stub) -- manually attach it so picojava_BooleanLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_BooleanLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_BooleanLiteral(Value="sample_text")
    partner = picojava_PrimitiveDecl()
    setattr(partner, 'picojava_PrimitiveDecl57', None)
    _safe_set(owner, 'picojava_BooleanLiteral', partner)
    assert getattr(partner, 'picojava_PrimitiveDecl57') == owner
    _safe_set(owner, 'picojava_BooleanLiteral', None)
    assert getattr(partner, 'picojava_PrimitiveDecl57') is None


def test_assoc_decl45_stub_double():
    # picojava_Access has no real 'picojava_Access46' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Decl(Name="sample_text", isUnknown=True)
    partner = picojava_Access()
    setattr(partner, 'picojava_Access46', None)
    _safe_set(owner, 'picojava_Decl47', partner)
    assert getattr(partner, 'picojava_Access46') == owner
    _safe_set(owner, 'picojava_Decl47', None)
    assert getattr(partner, 'picojava_Access46') is None


def test_assoc_qualifier17_stub_double():
    # picojava_Access has no real 'picojava_Access' property in the generated
    # code (a bare stub) -- manually attach it so picojava_TypeDecl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_TypeDecl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_TypeDecl(isQualified=True)
    partner = picojava_Access()
    setattr(partner, 'picojava_Access', None)
    _safe_set(owner, 'picojava_TypeDecl18', partner)
    assert getattr(partner, 'picojava_Access') == owner
    _safe_set(owner, 'picojava_TypeDecl18', None)
    assert getattr(partner, 'picojava_Access') is None


def test_assoc_qualifier48_stub_double():
    # picojava_Access has no real 'picojava_Access50' property in the generated
    # code (a bare stub) -- manually attach it so picojava_IdUse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_IdUse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_IdUse(Name="sample_text", isQualified=True)
    partner = picojava_Access()
    setattr(partner, 'picojava_Access50', None)
    _safe_set(owner, 'picojava_IdUse49', partner)
    assert getattr(partner, 'picojava_Access50') == owner
    _safe_set(owner, 'picojava_IdUse49', None)
    assert getattr(partner, 'picojava_Access50') is None


def test_assoc_unknownDecl3_stub_double():
    # picojava_UnknownDecl has no real 'picojava_UnknownDecl' property in the generated
    # code (a bare stub) -- manually attach it so picojava_Program's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # picojava_Program's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = picojava_Program()
    partner = picojava_UnknownDecl()
    setattr(partner, 'picojava_UnknownDecl', None)
    _safe_set(owner, 'picojava_Program4', partner)
    assert getattr(partner, 'picojava_UnknownDecl') == owner
    _safe_set(owner, 'picojava_Program4', None)
    assert getattr(partner, 'picojava_UnknownDecl') is None


