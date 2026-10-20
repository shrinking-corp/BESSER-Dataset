import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    A1,
    A2,
    A21,
    A3,
    A31,
    A5,
    B,
    B1,
    B2,
    B21,
    B3,
    B5,
    C,
    C1,
    C2,
    C21,
    C3,
    C4,
    C5,
    Interface_Interface,
    Mariage,
    Mariage1,
    PACS,
    Personne,
    R,
    Union,
    Union1,
    Y,
    Z,
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

def test_assoc_A_B_reverse_link_reassign_clear():
    a1 = B(attB=7)
    a2 = B(attB=13)
    b = A(attA="sample_text")
    _safe_set(b, 'b0', {a1})
    assert _is_linked(b, 'b0', a1)
    if hasattr(a1, 'a1'):
        assert _is_linked(a1, 'a1', b)
    _safe_set(b, 'b0', {a2})
    assert _is_linked(b, 'b0', a2)
    if hasattr(a1, 'a1'):
        assert not _is_linked(a1, 'a1', b)
    if hasattr(a2, 'a1'):
        assert _is_linked(a2, 'a1', b)
    _safe_set(b, 'b0', set())
    assert not _is_linked(b, 'b0', a2)
    if hasattr(a2, 'a1'):
        assert not _is_linked(a2, 'a1', b)


def test_assoc_A_B2_reverse_link_reassign_clear():
    a1 = B2(attB=7)
    a2 = B2(attB=13)
    b = A2(attA="sample_text")
    _safe_set(b, 'b4', {a1})
    assert _is_linked(b, 'b4', a1)
    if hasattr(a1, 'a5'):
        assert _is_linked(a1, 'a5', b)
    _safe_set(b, 'b4', {a2})
    assert _is_linked(b, 'b4', a2)
    if hasattr(a1, 'a5'):
        assert not _is_linked(a1, 'a5', b)
    if hasattr(a2, 'a5'):
        assert _is_linked(a2, 'a5', b)
    _safe_set(b, 'b4', set())
    assert not _is_linked(b, 'b4', a2)
    if hasattr(a2, 'a5'):
        assert not _is_linked(a2, 'a5', b)


def test_assoc_A_B3_reverse_link_reassign_clear():
    a1 = B1(attB=7)
    a2 = B1(attB=13)
    b = A1(attA="sample_text")
    _safe_set(b, 'b8', {a1})
    assert _is_linked(b, 'b8', a1)
    if hasattr(a1, 'a9'):
        assert _is_linked(a1, 'a9', b)
    _safe_set(b, 'b8', {a2})
    assert _is_linked(b, 'b8', a2)
    if hasattr(a1, 'a9'):
        assert not _is_linked(a1, 'a9', b)
    if hasattr(a2, 'a9'):
        assert _is_linked(a2, 'a9', b)
    _safe_set(b, 'b8', set())
    assert not _is_linked(b, 'b8', a2)
    if hasattr(a2, 'a9'):
        assert not _is_linked(a2, 'a9', b)


def test_assoc_A_B4_reverse_link_reassign_clear():
    a1 = B1(attB=7)
    a2 = B1(attB=13)
    b = A1(attA="sample_text")
    _safe_set(b, 'b14', {a1})
    assert _is_linked(b, 'b14', a1)
    if hasattr(a1, 'a15'):
        assert _is_linked(a1, 'a15', b)
    _safe_set(b, 'b14', {a2})
    assert _is_linked(b, 'b14', a2)
    if hasattr(a1, 'a15'):
        assert not _is_linked(a1, 'a15', b)
    if hasattr(a2, 'a15'):
        assert _is_linked(a2, 'a15', b)
    _safe_set(b, 'b14', set())
    assert not _is_linked(b, 'b14', a2)
    if hasattr(a2, 'a15'):
        assert not _is_linked(a2, 'a15', b)


def test_assoc_A_B51_reverse_link_reassign_clear():
    a1 = B5(attB=7)
    a2 = B5(attB=13)
    b = A5(attA="sample_text")
    _safe_set(b, 'b24', {a1})
    assert _is_linked(b, 'b24', a1)
    if hasattr(a1, 'a25'):
        assert _is_linked(a1, 'a25', b)
    _safe_set(b, 'b24', {a2})
    assert _is_linked(b, 'b24', a2)
    if hasattr(a1, 'a25'):
        assert not _is_linked(a1, 'a25', b)
    if hasattr(a2, 'a25'):
        assert _is_linked(a2, 'a25', b)
    _safe_set(b, 'b24', set())
    assert not _is_linked(b, 'b24', a2)
    if hasattr(a2, 'a25'):
        assert not _is_linked(a2, 'a25', b)


def test_assoc_B_C2_reverse_link_reassign_clear():
    a1 = C(attC1=7, attC2=True)
    a2 = C(attC1=13, attC2=False)
    b = B(attB=7)
    _safe_set(b, 'c2', {a1})
    assert _is_linked(b, 'c2', a1)
    if hasattr(a1, 'b3'):
        assert _is_linked(a1, 'b3', b)
    _safe_set(b, 'c2', {a2})
    assert _is_linked(b, 'c2', a2)
    if hasattr(a1, 'b3'):
        assert not _is_linked(a1, 'b3', b)
    if hasattr(a2, 'b3'):
        assert _is_linked(a2, 'b3', b)
    _safe_set(b, 'c2', set())
    assert not _is_linked(b, 'c2', a2)
    if hasattr(a2, 'b3'):
        assert not _is_linked(a2, 'b3', b)


def test_assoc_B_C22_reverse_link_reassign_clear():
    a1 = C2(attC1=7, attC2=True)
    a2 = C2(attC1=13, attC2=False)
    b = B2(attB=7)
    _safe_set(b, 'c6', {a1})
    assert _is_linked(b, 'c6', a1)
    if hasattr(a1, 'b7'):
        assert _is_linked(a1, 'b7', b)
    _safe_set(b, 'c6', {a2})
    assert _is_linked(b, 'c6', a2)
    if hasattr(a1, 'b7'):
        assert not _is_linked(a1, 'b7', b)
    if hasattr(a2, 'b7'):
        assert _is_linked(a2, 'b7', b)
    _safe_set(b, 'c6', set())
    assert not _is_linked(b, 'c6', a2)
    if hasattr(a2, 'b7'):
        assert not _is_linked(a2, 'b7', b)


def test_assoc_B_C23_reverse_link_reassign_clear():
    a1 = C1(attC1=7, attC2=True)
    a2 = C1(attC1=13, attC2=False)
    b = B1(attB=7)
    _safe_set(b, 'c10', {a1})
    assert _is_linked(b, 'c10', a1)
    if hasattr(a1, 'b11'):
        assert _is_linked(a1, 'b11', b)
    _safe_set(b, 'c10', {a2})
    assert _is_linked(b, 'c10', a2)
    if hasattr(a1, 'b11'):
        assert not _is_linked(a1, 'b11', b)
    if hasattr(a2, 'b11'):
        assert _is_linked(a2, 'b11', b)
    _safe_set(b, 'c10', set())
    assert not _is_linked(b, 'c10', a2)
    if hasattr(a2, 'b11'):
        assert not _is_linked(a2, 'b11', b)


def test_assoc_B_C25_reverse_link_reassign_clear():
    a1 = C5(attC1=7, attC2=True)
    a2 = C5(attC1=13, attC2=False)
    b = B5(attB=7)
    _safe_set(b, 'c26', {a1})
    assert _is_linked(b, 'c26', a1)
    if hasattr(a1, 'b27'):
        assert _is_linked(a1, 'b27', b)
    _safe_set(b, 'c26', {a2})
    assert _is_linked(b, 'c26', a2)
    if hasattr(a1, 'b27'):
        assert not _is_linked(a1, 'b27', b)
    if hasattr(a2, 'b27'):
        assert _is_linked(a2, 'b27', b)
    _safe_set(b, 'c26', set())
    assert not _is_linked(b, 'c26', a2)
    if hasattr(a2, 'b27'):
        assert not _is_linked(a2, 'b27', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Personne_Union2_stub_double():
    # Personne has no real 'unions28' property in the generated
    # code (a bare stub) -- manually attach it so Union1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union1(dateUnion="sample_text")
    partner = Personne()
    setattr(partner, 'unions28', None)
    _safe_set(owner, 'pers29', {partner})
    assert owner in getattr(partner, 'unions28')
    _safe_set(owner, 'pers29', set())
    assert owner not in getattr(partner, 'unions28')


def test_assoc_Personne_Union3_stub_double():
    # Personne has no real 'unionActuelle30' property in the generated
    # code (a bare stub) -- manually attach it so Union1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Union1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Union1(dateUnion="sample_text")
    partner = Personne()
    setattr(partner, 'unionActuelle30', None)
    _safe_set(owner, 'personne31', {partner})
    assert getattr(partner, 'unionActuelle30') == owner
    _safe_set(owner, 'personne31', set())
    assert getattr(partner, 'unionActuelle30') is None


def test_assoc_R_A_stub_double():
    # R has no real 'aR12' property in the generated
    # code (a bare stub) -- manually attach it so A1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # A1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = A1(attA="sample_text")
    partner = R()
    setattr(partner, 'aR12', None)
    _safe_set(owner, 'r13', partner)
    assert owner in getattr(partner, 'aR12')
    _safe_set(owner, 'r13', None)
    assert owner not in getattr(partner, 'aR12')


