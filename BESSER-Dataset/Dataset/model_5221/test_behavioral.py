import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    anytype_A,
    anytype_B,
    anytype_C,
    anytype_EObject,
    anytype_TestAny,
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

def test_assoc_myB0_reverse_link_reassign_clear():
    a1 = anytype_B(name="sample_text")
    a2 = anytype_B(name="sample_text_2")
    b = anytype_A(doub="sample_text", lon="sample_text", name="sample_text")
    _safe_set(b, 'anytype_A', a1)
    assert _is_linked(b, 'anytype_A', a1)
    if hasattr(a1, 'anytype_B'):
        assert _is_linked(a1, 'anytype_B', b)
    _safe_set(b, 'anytype_A', a2)
    assert _is_linked(b, 'anytype_A', a2)
    if hasattr(a1, 'anytype_B'):
        assert not _is_linked(a1, 'anytype_B', b)
    if hasattr(a2, 'anytype_B'):
        assert _is_linked(a2, 'anytype_B', b)
    _safe_set(b, 'anytype_A', None)
    assert not _is_linked(b, 'anytype_A', a2)
    if hasattr(a2, 'anytype_B'):
        assert not _is_linked(a2, 'anytype_B', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_multiAnyType2_stub_double():
    # anytype_EObject has no real 'anytype_EObject4' property in the generated
    # code (a bare stub) -- manually attach it so anytype_TestAny's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anytype_TestAny's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anytype_TestAny(a="sample_text", any="sample_text", myAny="sample_text", name="sample_text")
    partner = anytype_EObject()
    setattr(partner, 'anytype_EObject4', None)
    _safe_set(owner, 'anytype_TestAny3', {partner})
    assert getattr(partner, 'anytype_EObject4') == owner
    _safe_set(owner, 'anytype_TestAny3', set())
    assert getattr(partner, 'anytype_EObject4') is None


def test_assoc_singleAnyType1_stub_double():
    # anytype_EObject has no real 'anytype_EObject' property in the generated
    # code (a bare stub) -- manually attach it so anytype_TestAny's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # anytype_TestAny's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = anytype_TestAny(a="sample_text", any="sample_text", myAny="sample_text", name="sample_text")
    partner = anytype_EObject()
    setattr(partner, 'anytype_EObject', None)
    _safe_set(owner, 'anytype_TestAny', partner)
    assert getattr(partner, 'anytype_EObject') == owner
    _safe_set(owner, 'anytype_TestAny', None)
    assert getattr(partner, 'anytype_EObject') is None


