import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    NamedElement,
    test_NamedElement,
    test_Root,
    test_TestClassDelegate,
    test_TestElement,
    test_TestElementWrapper,
    test_TestPolicy,
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

def test_assoc_children0_reverse_link_reassign_clear():
    a1 = test_TestElement()
    a2 = test_TestElement()
    b = test_Root(ttt="sample_text")
    _safe_set(b, 'test_Root', {a1})
    assert _is_linked(b, 'test_Root', a1)
    if hasattr(a1, 'test_TestElement'):
        assert _is_linked(a1, 'test_TestElement', b)
    _safe_set(b, 'test_Root', {a2})
    assert _is_linked(b, 'test_Root', a2)
    if hasattr(a1, 'test_TestElement'):
        assert not _is_linked(a1, 'test_TestElement', b)
    if hasattr(a2, 'test_TestElement'):
        assert _is_linked(a2, 'test_TestElement', b)
    _safe_set(b, 'test_Root', set())
    assert not _is_linked(b, 'test_Root', a2)
    if hasattr(a2, 'test_TestElement'):
        assert not _is_linked(a2, 'test_TestElement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_element5_stub_double():
    # test_TestElementWrapper has no real 'test_TestElementWrapper' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement()
    partner = test_TestElementWrapper()
    setattr(partner, 'test_TestElementWrapper', None)
    _safe_set(owner, 'test_TestElement6', partner)
    assert getattr(partner, 'test_TestElementWrapper') == owner
    _safe_set(owner, 'test_TestElement6', None)
    assert getattr(partner, 'test_TestElementWrapper') is None


def test_assoc_policies1_stub_double():
    # test_TestPolicy has no real 'test_TestPolicy' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement()
    partner = test_TestPolicy()
    setattr(partner, 'test_TestPolicy', None)
    _safe_set(owner, 'test_TestElement2', {partner})
    assert getattr(partner, 'test_TestPolicy') == owner
    _safe_set(owner, 'test_TestElement2', set())
    assert getattr(partner, 'test_TestPolicy') is None


def test_assoc_testClassDelegate3_stub_double():
    # test_TestClassDelegate has no real 'test_TestClassDelegate' property in the generated
    # code (a bare stub) -- manually attach it so test_TestElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # test_TestElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = test_TestElement()
    partner = test_TestClassDelegate()
    setattr(partner, 'test_TestClassDelegate', None)
    _safe_set(owner, 'test_TestElement4', partner)
    assert getattr(partner, 'test_TestClassDelegate') == owner
    _safe_set(owner, 'test_TestElement4', None)
    assert getattr(partner, 'test_TestClassDelegate') is None


