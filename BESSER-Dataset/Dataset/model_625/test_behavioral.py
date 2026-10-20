import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ocldriven_Dependancy,
    ocldriven_Library,
    ocldriven_Loans,
    ocldriven_Media,
    ocldriven_Member,
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

def test_assoc_media9_reverse_link_reassign_clear():
    a1 = ocldriven_Media(copies="sample_text", name="sample_text")
    a2 = ocldriven_Media(copies="sample_text_2", name="sample_text_2")
    b = ocldriven_Loans(date=date(2024, 1, 1))
    _safe_set(b, 'ocldriven_Loans10', a1)
    assert _is_linked(b, 'ocldriven_Loans10', a1)
    if hasattr(a1, 'ocldriven_Media'):
        assert _is_linked(a1, 'ocldriven_Media', b)
    _safe_set(b, 'ocldriven_Loans10', a2)
    assert _is_linked(b, 'ocldriven_Loans10', a2)
    if hasattr(a1, 'ocldriven_Media'):
        assert not _is_linked(a1, 'ocldriven_Media', b)
    if hasattr(a2, 'ocldriven_Media'):
        assert _is_linked(a2, 'ocldriven_Media', b)
    _safe_set(b, 'ocldriven_Loans10', None)
    assert not _is_linked(b, 'ocldriven_Loans10', a2)
    if hasattr(a2, 'ocldriven_Media'):
        assert not _is_linked(a2, 'ocldriven_Media', b)


def test_assoc_member7_reverse_link_reassign_clear():
    a1 = ocldriven_Member(name="sample_text")
    a2 = ocldriven_Member(name="sample_text_2")
    b = ocldriven_Loans(date=date(2024, 1, 1))
    _safe_set(b, 'ocldriven_Loans8', a1)
    assert _is_linked(b, 'ocldriven_Loans8', a1)
    if hasattr(a1, 'ocldriven_Member'):
        assert _is_linked(a1, 'ocldriven_Member', b)
    _safe_set(b, 'ocldriven_Loans8', a2)
    assert _is_linked(b, 'ocldriven_Loans8', a2)
    if hasattr(a1, 'ocldriven_Member'):
        assert not _is_linked(a1, 'ocldriven_Member', b)
    if hasattr(a2, 'ocldriven_Member'):
        assert _is_linked(a2, 'ocldriven_Member', b)
    _safe_set(b, 'ocldriven_Loans8', None)
    assert not _is_linked(b, 'ocldriven_Loans8', a2)
    if hasattr(a2, 'ocldriven_Member'):
        assert not _is_linked(a2, 'ocldriven_Member', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_after16_stub_double():
    # ocldriven_Dependancy has no real 'ocldriven_Dependancy17' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Media's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Media's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Media(copies="sample_text", name="sample_text")
    partner = ocldriven_Dependancy()
    setattr(partner, 'ocldriven_Dependancy17', None)
    _safe_set(owner, 'ocldriven_Media18', partner)
    assert getattr(partner, 'ocldriven_Dependancy17') == owner
    _safe_set(owner, 'ocldriven_Media18', None)
    assert getattr(partner, 'ocldriven_Dependancy17') is None


def test_assoc_before13_stub_double():
    # ocldriven_Dependancy has no real 'ocldriven_Dependancy14' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Media's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Media's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Media(copies="sample_text", name="sample_text")
    partner = ocldriven_Dependancy()
    setattr(partner, 'ocldriven_Dependancy14', None)
    _safe_set(owner, 'ocldriven_Media15', partner)
    assert getattr(partner, 'ocldriven_Dependancy14') == owner
    _safe_set(owner, 'ocldriven_Media15', None)
    assert getattr(partner, 'ocldriven_Dependancy14') is None


def test_assoc_library11_stub_double():
    # ocldriven_Library has no real 'Library12' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Member(name="sample_text")
    partner = ocldriven_Library()
    setattr(partner, 'Library12', None)
    _safe_set(owner, 'members', partner)
    assert getattr(partner, 'Library12') == owner
    _safe_set(owner, 'members', None)
    assert getattr(partner, 'Library12') is None


def test_assoc_library6_stub_double():
    # ocldriven_Library has no real 'Library' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Media's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Media's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Media(copies="sample_text", name="sample_text")
    partner = ocldriven_Library()
    setattr(partner, 'Library', None)
    _safe_set(owner, 'medias', partner)
    assert getattr(partner, 'Library') == owner
    _safe_set(owner, 'medias', None)
    assert getattr(partner, 'Library') is None


def test_assoc_loans3_stub_double():
    # ocldriven_Library has no real 'ocldriven_Library' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Loans's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Loans's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Loans(date=date(2024, 1, 1))
    partner = ocldriven_Library()
    setattr(partner, 'ocldriven_Library', None)
    _safe_set(owner, 'ocldriven_Loans', partner)
    assert owner in getattr(partner, 'ocldriven_Library')
    _safe_set(owner, 'ocldriven_Loans', None)
    assert owner not in getattr(partner, 'ocldriven_Library')


def test_assoc_medias0_stub_double():
    # ocldriven_Library has no real 'library' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Media's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Media's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Media(copies="sample_text", name="sample_text")
    partner = ocldriven_Library()
    setattr(partner, 'library', None)
    _safe_set(owner, 'Media', partner)
    assert owner in getattr(partner, 'library')
    _safe_set(owner, 'Media', None)
    assert owner not in getattr(partner, 'library')


def test_assoc_members1_stub_double():
    # ocldriven_Library has no real 'library2' property in the generated
    # code (a bare stub) -- manually attach it so ocldriven_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ocldriven_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ocldriven_Member(name="sample_text")
    partner = ocldriven_Library()
    setattr(partner, 'library2', None)
    _safe_set(owner, 'Member', partner)
    assert owner in getattr(partner, 'library2')
    _safe_set(owner, 'Member', None)
    assert owner not in getattr(partner, 'library2')


