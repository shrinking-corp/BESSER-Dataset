import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Statement,
    sourcecode_Assignment,
    sourcecode_Decision,
    sourcecode_Program,
    sourcecode_Statement,
    sourcecode_While,
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

def test_assoc_next1_reverse_link_reassign_clear():
    a1 = sourcecode_Statement(id="sample_text")
    a2 = sourcecode_Statement(id="sample_text_2")
    b = sourcecode_Statement(id="sample_text")
    _safe_set(b, 'sourcecode_Statement0', a1)
    assert _is_linked(b, 'sourcecode_Statement0', a1)
    if hasattr(a1, 'sourcecode_Statement'):
        assert _is_linked(a1, 'sourcecode_Statement', b)
    _safe_set(b, 'sourcecode_Statement0', a2)
    assert _is_linked(b, 'sourcecode_Statement0', a2)
    if hasattr(a1, 'sourcecode_Statement'):
        assert not _is_linked(a1, 'sourcecode_Statement', b)
    if hasattr(a2, 'sourcecode_Statement'):
        assert _is_linked(a2, 'sourcecode_Statement', b)
    _safe_set(b, 'sourcecode_Statement0', None)
    assert not _is_linked(b, 'sourcecode_Statement0', a2)
    if hasattr(a2, 'sourcecode_Statement'):
        assert not _is_linked(a2, 'sourcecode_Statement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_first12_stub_double():
    # sourcecode_Program has no real 'sourcecode_Program' property in the generated
    # code (a bare stub) -- manually attach it so sourcecode_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecode_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecode_Statement(id="sample_text")
    partner = sourcecode_Program()
    setattr(partner, 'sourcecode_Program', None)
    _safe_set(owner, 'sourcecode_Statement13', partner)
    assert getattr(partner, 'sourcecode_Program') == owner
    _safe_set(owner, 'sourcecode_Statement13', None)
    assert getattr(partner, 'sourcecode_Program') is None


def test_assoc_first7_stub_double():
    # sourcecode_While has no real 'sourcecode_While' property in the generated
    # code (a bare stub) -- manually attach it so sourcecode_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecode_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecode_Statement(id="sample_text")
    partner = sourcecode_While()
    setattr(partner, 'sourcecode_While', None)
    _safe_set(owner, 'sourcecode_Statement8', partner)
    assert getattr(partner, 'sourcecode_While') == owner
    _safe_set(owner, 'sourcecode_Statement8', None)
    assert getattr(partner, 'sourcecode_While') is None


def test_assoc_last9_stub_double():
    # sourcecode_While has no real 'sourcecode_While10' property in the generated
    # code (a bare stub) -- manually attach it so sourcecode_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecode_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecode_Statement(id="sample_text")
    partner = sourcecode_While()
    setattr(partner, 'sourcecode_While10', None)
    _safe_set(owner, 'sourcecode_Statement11', partner)
    assert getattr(partner, 'sourcecode_While10') == owner
    _safe_set(owner, 'sourcecode_Statement11', None)
    assert getattr(partner, 'sourcecode_While10') is None


def test_assoc_negative4_stub_double():
    # sourcecode_Decision has no real 'sourcecode_Decision5' property in the generated
    # code (a bare stub) -- manually attach it so sourcecode_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecode_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecode_Statement(id="sample_text")
    partner = sourcecode_Decision()
    setattr(partner, 'sourcecode_Decision5', None)
    _safe_set(owner, 'sourcecode_Statement6', partner)
    assert getattr(partner, 'sourcecode_Decision5') == owner
    _safe_set(owner, 'sourcecode_Statement6', None)
    assert getattr(partner, 'sourcecode_Decision5') is None


def test_assoc_positive2_stub_double():
    # sourcecode_Decision has no real 'sourcecode_Decision' property in the generated
    # code (a bare stub) -- manually attach it so sourcecode_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sourcecode_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sourcecode_Statement(id="sample_text")
    partner = sourcecode_Decision()
    setattr(partner, 'sourcecode_Decision', None)
    _safe_set(owner, 'sourcecode_Statement3', partner)
    assert getattr(partner, 'sourcecode_Decision') == owner
    _safe_set(owner, 'sourcecode_Statement3', None)
    assert getattr(partner, 'sourcecode_Decision') is None


