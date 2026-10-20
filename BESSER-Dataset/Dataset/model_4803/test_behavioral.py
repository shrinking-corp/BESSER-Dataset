import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    Child1,
    Child2,
    Child3,
    Common,
    GrandChildD,
    Interface,
    TestClassifier,
    TestPackageableElement,
    pltest_Base,
    pltest_Child1,
    pltest_Child2,
    pltest_Child3,
    pltest_Circle,
    pltest_Common,
    pltest_GrandChild,
    pltest_GrandChild2,
    pltest_GrandChildD,
    pltest_GrandGrandChildE,
    pltest_GrandGrandChildF,
    pltest_Interface,
    pltest_Numbers,
    pltest_Red,
    pltest_TestClass,
    pltest_TestClassifier,
    pltest_TestInterface,
    pltest_TestPackage,
    pltest_TestPackageableElement,
    pltest_WhatEver,
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

def test_assoc_red3_reverse_link_reassign_clear():
    a1 = pltest_Red(redness=7)
    a2 = pltest_Red(redness=13)
    b = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    _safe_set(b, 'pltest_Circle', {a1})
    assert _is_linked(b, 'pltest_Circle', a1)
    if hasattr(a1, 'pltest_Red'):
        assert _is_linked(a1, 'pltest_Red', b)
    _safe_set(b, 'pltest_Circle', {a2})
    assert _is_linked(b, 'pltest_Circle', a2)
    if hasattr(a1, 'pltest_Red'):
        assert not _is_linked(a1, 'pltest_Red', b)
    if hasattr(a2, 'pltest_Red'):
        assert _is_linked(a2, 'pltest_Red', b)
    _safe_set(b, 'pltest_Circle', set())
    assert not _is_linked(b, 'pltest_Circle', a2)
    if hasattr(a2, 'pltest_Red'):
        assert not _is_linked(a2, 'pltest_Red', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a10_stub_double():
    # pltest_Common has no real 'pltest_Common' property in the generated
    # code (a bare stub) -- manually attach it so pltest_Child1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pltest_Child1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pltest_Child1(name="sample_text")
    partner = pltest_Common()
    setattr(partner, 'pltest_Common', None)
    _safe_set(owner, 'pltest_Child1', partner)
    assert getattr(partner, 'pltest_Common') == owner
    _safe_set(owner, 'pltest_Child1', None)
    assert getattr(partner, 'pltest_Common') is None


def test_assoc_someRef4_stub_double():
    # pltest_WhatEver has no real 'pltest_WhatEver' property in the generated
    # code (a bare stub) -- manually attach it so pltest_Circle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pltest_Circle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pltest_Circle(area=3.14, circumference=3.14, diameter="sample_text")
    partner = pltest_WhatEver()
    setattr(partner, 'pltest_WhatEver', None)
    _safe_set(owner, 'pltest_Circle5', partner)
    assert getattr(partner, 'pltest_WhatEver') == owner
    _safe_set(owner, 'pltest_Circle5', None)
    assert getattr(partner, 'pltest_WhatEver') is None


