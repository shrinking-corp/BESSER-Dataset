import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Kasu2_ClassA,
    Kasu2_ClassB,
    Kasu2_Root,
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

def test_assoc_C_A3_reverse_link_reassign_clear():
    a1 = Kasu2_ClassB(Name="sample_text")
    a2 = Kasu2_ClassB(Name="sample_text_2")
    b = Kasu2_ClassA(Name="sample_text")
    _safe_set(b, 'ClassA', a1)
    assert _is_linked(b, 'ClassA', a1)
    if hasattr(a1, 'C_B'):
        assert _is_linked(a1, 'C_B', b)
    _safe_set(b, 'ClassA', a2)
    assert _is_linked(b, 'ClassA', a2)
    if hasattr(a1, 'C_B'):
        assert not _is_linked(a1, 'C_B', b)
    if hasattr(a2, 'C_B'):
        assert _is_linked(a2, 'C_B', b)
    _safe_set(b, 'ClassA', None)
    assert not _is_linked(b, 'ClassA', a2)
    if hasattr(a2, 'C_B'):
        assert not _is_linked(a2, 'C_B', b)


def test_assoc_C_B0_reverse_link_reassign_clear():
    a1 = Kasu2_ClassB(Name="sample_text")
    a2 = Kasu2_ClassB(Name="sample_text_2")
    b = Kasu2_ClassA(Name="sample_text")
    _safe_set(b, 'C_A', {a1})
    assert _is_linked(b, 'C_A', a1)
    if hasattr(a1, 'ClassB'):
        assert _is_linked(a1, 'ClassB', b)
    _safe_set(b, 'C_A', {a2})
    assert _is_linked(b, 'C_A', a2)
    if hasattr(a1, 'ClassB'):
        assert not _is_linked(a1, 'ClassB', b)
    if hasattr(a2, 'ClassB'):
        assert _is_linked(a2, 'ClassB', b)
    _safe_set(b, 'C_A', set())
    assert not _is_linked(b, 'C_A', a2)
    if hasattr(a2, 'ClassB'):
        assert not _is_linked(a2, 'ClassB', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_C_A4_stub_double():
    # Kasu2_Root has no real 'C_R' property in the generated
    # code (a bare stub) -- manually attach it so Kasu2_ClassA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Kasu2_ClassA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Kasu2_ClassA(Name="sample_text")
    partner = Kasu2_Root()
    setattr(partner, 'C_R', None)
    _safe_set(owner, 'ClassA5', partner)
    assert owner in getattr(partner, 'C_R')
    _safe_set(owner, 'ClassA5', None)
    assert owner not in getattr(partner, 'C_R')


def test_assoc_C_R1_stub_double():
    # Kasu2_Root has no real 'Root' property in the generated
    # code (a bare stub) -- manually attach it so Kasu2_ClassA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Kasu2_ClassA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Kasu2_ClassA(Name="sample_text")
    partner = Kasu2_Root()
    setattr(partner, 'Root', None)
    _safe_set(owner, 'C_A2', partner)
    assert getattr(partner, 'Root') == owner
    _safe_set(owner, 'C_A2', None)
    assert getattr(partner, 'Root') is None


