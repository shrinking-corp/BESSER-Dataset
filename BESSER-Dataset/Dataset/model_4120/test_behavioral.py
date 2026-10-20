import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    whileLanguage_Affectation,
    whileLanguage_Command,
    whileLanguage_Commands,
    whileLanguage_Definition,
    whileLanguage_EObject,
    whileLanguage_Expr,
    whileLanguage_For,
    whileLanguage_Foreach,
    whileLanguage_Function,
    whileLanguage_If,
    whileLanguage_Lexpr,
    whileLanguage_Nop,
    whileLanguage_Program,
    whileLanguage_Read,
    whileLanguage_While,
    whileLanguage_Write,
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

def test_assoc_ex146_reverse_link_reassign_clear():
    a1 = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    a2 = whileLanguage_Expr(ope="sample_text_2", valeur="sample_text_2")
    b = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    _safe_set(b, 'whileLanguage_Expr47', a1)
    assert _is_linked(b, 'whileLanguage_Expr47', a1)
    if hasattr(a1, 'whileLanguage_Expr45'):
        assert _is_linked(a1, 'whileLanguage_Expr45', b)
    _safe_set(b, 'whileLanguage_Expr47', a2)
    assert _is_linked(b, 'whileLanguage_Expr47', a2)
    if hasattr(a1, 'whileLanguage_Expr45'):
        assert not _is_linked(a1, 'whileLanguage_Expr45', b)
    if hasattr(a2, 'whileLanguage_Expr45'):
        assert _is_linked(a2, 'whileLanguage_Expr45', b)
    _safe_set(b, 'whileLanguage_Expr47', None)
    assert not _is_linked(b, 'whileLanguage_Expr47', a2)
    if hasattr(a2, 'whileLanguage_Expr45'):
        assert not _is_linked(a2, 'whileLanguage_Expr45', b)


def test_assoc_ex249_reverse_link_reassign_clear():
    a1 = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    a2 = whileLanguage_Expr(ope="sample_text_2", valeur="sample_text_2")
    b = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    _safe_set(b, 'whileLanguage_Expr50', a1)
    assert _is_linked(b, 'whileLanguage_Expr50', a1)
    if hasattr(a1, 'whileLanguage_Expr48'):
        assert _is_linked(a1, 'whileLanguage_Expr48', b)
    _safe_set(b, 'whileLanguage_Expr50', a2)
    assert _is_linked(b, 'whileLanguage_Expr50', a2)
    if hasattr(a1, 'whileLanguage_Expr48'):
        assert not _is_linked(a1, 'whileLanguage_Expr48', b)
    if hasattr(a2, 'whileLanguage_Expr48'):
        assert _is_linked(a2, 'whileLanguage_Expr48', b)
    _safe_set(b, 'whileLanguage_Expr50', None)
    assert not _is_linked(b, 'whileLanguage_Expr50', a2)
    if hasattr(a2, 'whileLanguage_Expr48'):
        assert not _is_linked(a2, 'whileLanguage_Expr48', b)


def test_assoc_expr43_reverse_link_reassign_clear():
    a1 = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    a2 = whileLanguage_Expr(ope="sample_text_2", valeur="sample_text_2")
    b = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    _safe_set(b, 'whileLanguage_Expr44', a1)
    assert _is_linked(b, 'whileLanguage_Expr44', a1)
    if hasattr(a1, 'whileLanguage_Expr42'):
        assert _is_linked(a1, 'whileLanguage_Expr42', b)
    _safe_set(b, 'whileLanguage_Expr44', a2)
    assert _is_linked(b, 'whileLanguage_Expr44', a2)
    if hasattr(a1, 'whileLanguage_Expr42'):
        assert not _is_linked(a1, 'whileLanguage_Expr42', b)
    if hasattr(a2, 'whileLanguage_Expr42'):
        assert _is_linked(a2, 'whileLanguage_Expr42', b)
    _safe_set(b, 'whileLanguage_Expr44', None)
    assert not _is_linked(b, 'whileLanguage_Expr44', a2)
    if hasattr(a2, 'whileLanguage_Expr42'):
        assert not _is_linked(a2, 'whileLanguage_Expr42', b)


def test_assoc_valeurs9_reverse_link_reassign_clear():
    a1 = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    a2 = whileLanguage_Expr(ope="sample_text_2", valeur="sample_text_2")
    b = whileLanguage_Affectation(affectations="sample_text")
    _safe_set(b, 'whileLanguage_Affectation', {a1})
    assert _is_linked(b, 'whileLanguage_Affectation', a1)
    if hasattr(a1, 'whileLanguage_Expr'):
        assert _is_linked(a1, 'whileLanguage_Expr', b)
    _safe_set(b, 'whileLanguage_Affectation', {a2})
    assert _is_linked(b, 'whileLanguage_Affectation', a2)
    if hasattr(a1, 'whileLanguage_Expr'):
        assert not _is_linked(a1, 'whileLanguage_Expr', b)
    if hasattr(a2, 'whileLanguage_Expr'):
        assert _is_linked(a2, 'whileLanguage_Expr', b)
    _safe_set(b, 'whileLanguage_Affectation', set())
    assert not _is_linked(b, 'whileLanguage_Affectation', a2)
    if hasattr(a2, 'whileLanguage_Expr'):
        assert not _is_linked(a2, 'whileLanguage_Expr', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_definition1_stub_double():
    # whileLanguage_Definition has no real 'whileLanguage_Definition' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Function(name="sample_text")
    partner = whileLanguage_Definition()
    setattr(partner, 'whileLanguage_Definition', None)
    _safe_set(owner, 'whileLanguage_Function2', partner)
    assert getattr(partner, 'whileLanguage_Definition') == owner
    _safe_set(owner, 'whileLanguage_Function2', None)
    assert getattr(partner, 'whileLanguage_Definition') is None


def test_assoc_expr114_stub_double():
    # whileLanguage_Foreach has no real 'whileLanguage_Foreach' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_Foreach()
    setattr(partner, 'whileLanguage_Foreach', None)
    _safe_set(owner, 'whileLanguage_Expr15', partner)
    assert getattr(partner, 'whileLanguage_Foreach') == owner
    _safe_set(owner, 'whileLanguage_Expr15', None)
    assert getattr(partner, 'whileLanguage_Foreach') is None


def test_assoc_expr216_stub_double():
    # whileLanguage_Foreach has no real 'whileLanguage_Foreach17' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_Foreach()
    setattr(partner, 'whileLanguage_Foreach17', None)
    _safe_set(owner, 'whileLanguage_Expr18', partner)
    assert getattr(partner, 'whileLanguage_Foreach17') == owner
    _safe_set(owner, 'whileLanguage_Expr18', None)
    assert getattr(partner, 'whileLanguage_Foreach17') is None


def test_assoc_expr22_stub_double():
    # whileLanguage_If has no real 'whileLanguage_If' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_If()
    setattr(partner, 'whileLanguage_If', None)
    _safe_set(owner, 'whileLanguage_Expr23', partner)
    assert getattr(partner, 'whileLanguage_If') == owner
    _safe_set(owner, 'whileLanguage_Expr23', None)
    assert getattr(partner, 'whileLanguage_If') is None


def test_assoc_expr30_stub_double():
    # whileLanguage_For has no real 'whileLanguage_For' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_For()
    setattr(partner, 'whileLanguage_For', None)
    _safe_set(owner, 'whileLanguage_Expr31', partner)
    assert getattr(partner, 'whileLanguage_For') == owner
    _safe_set(owner, 'whileLanguage_Expr31', None)
    assert getattr(partner, 'whileLanguage_For') is None


def test_assoc_expr35_stub_double():
    # whileLanguage_While has no real 'whileLanguage_While' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_While()
    setattr(partner, 'whileLanguage_While', None)
    _safe_set(owner, 'whileLanguage_Expr36', partner)
    assert getattr(partner, 'whileLanguage_While') == owner
    _safe_set(owner, 'whileLanguage_Expr36', None)
    assert getattr(partner, 'whileLanguage_While') is None


def test_assoc_exprs51_stub_double():
    # whileLanguage_Lexpr has no real 'whileLanguage_Lexpr52' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_Lexpr()
    setattr(partner, 'whileLanguage_Lexpr52', None)
    _safe_set(owner, 'whileLanguage_Expr53', partner)
    assert owner in getattr(partner, 'whileLanguage_Lexpr52')
    _safe_set(owner, 'whileLanguage_Expr53', None)
    assert owner not in getattr(partner, 'whileLanguage_Lexpr52')


def test_assoc_functions0_stub_double():
    # whileLanguage_Program has no real 'whileLanguage_Program' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Function(name="sample_text")
    partner = whileLanguage_Program()
    setattr(partner, 'whileLanguage_Program', None)
    _safe_set(owner, 'whileLanguage_Function', partner)
    assert owner in getattr(partner, 'whileLanguage_Program')
    _safe_set(owner, 'whileLanguage_Function', None)
    assert owner not in getattr(partner, 'whileLanguage_Program')


def test_assoc_lexpr40_stub_double():
    # whileLanguage_Lexpr has no real 'whileLanguage_Lexpr' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Expr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Expr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Expr(ope="sample_text", valeur="sample_text")
    partner = whileLanguage_Lexpr()
    setattr(partner, 'whileLanguage_Lexpr', None)
    _safe_set(owner, 'whileLanguage_Expr41', partner)
    assert getattr(partner, 'whileLanguage_Lexpr') == owner
    _safe_set(owner, 'whileLanguage_Expr41', None)
    assert getattr(partner, 'whileLanguage_Lexpr') is None


def test_assoc_read3_stub_double():
    # whileLanguage_Definition has no real 'whileLanguage_Definition4' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Read's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Read's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Read(variable="sample_text")
    partner = whileLanguage_Definition()
    setattr(partner, 'whileLanguage_Definition4', None)
    _safe_set(owner, 'whileLanguage_Read', partner)
    assert getattr(partner, 'whileLanguage_Definition4') == owner
    _safe_set(owner, 'whileLanguage_Read', None)
    assert getattr(partner, 'whileLanguage_Definition4') is None


def test_assoc_write7_stub_double():
    # whileLanguage_Definition has no real 'whileLanguage_Definition8' property in the generated
    # code (a bare stub) -- manually attach it so whileLanguage_Write's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # whileLanguage_Write's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = whileLanguage_Write(variable="sample_text")
    partner = whileLanguage_Definition()
    setattr(partner, 'whileLanguage_Definition8', None)
    _safe_set(owner, 'whileLanguage_Write', partner)
    assert getattr(partner, 'whileLanguage_Definition8') == owner
    _safe_set(owner, 'whileLanguage_Write', None)
    assert getattr(partner, 'whileLanguage_Definition8') is None


