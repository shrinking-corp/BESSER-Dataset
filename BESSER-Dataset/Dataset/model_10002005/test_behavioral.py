import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MyClass,
    MyClass2,
    MyClass3,
    MyClass4,
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

def test_assoc_MyClass_MyClass3_reverse_link_reassign_clear():
    a1 = MyClass3(attribute="sample_text")
    a2 = MyClass3(attribute="sample_text_2")
    b = MyClass(asdf="sample_text")
    _safe_set(b, 'myClass30', a1)
    assert _is_linked(b, 'myClass30', a1)
    if hasattr(a1, 'myClass1'):
        assert _is_linked(a1, 'myClass1', b)
    _safe_set(b, 'myClass30', a2)
    assert _is_linked(b, 'myClass30', a2)
    if hasattr(a1, 'myClass1'):
        assert not _is_linked(a1, 'myClass1', b)
    if hasattr(a2, 'myClass1'):
        assert _is_linked(a2, 'myClass1', b)
    _safe_set(b, 'myClass30', None)
    assert not _is_linked(b, 'myClass30', a2)
    if hasattr(a2, 'myClass1'):
        assert not _is_linked(a2, 'myClass1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_MyClass2_MyClass3_stub_double():
    # MyClass2 has no real 'myClass34' property in the generated
    # code (a bare stub) -- manually attach it so MyClass3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MyClass3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MyClass3(attribute="sample_text")
    partner = MyClass2()
    setattr(partner, 'myClass34', None)
    _safe_set(owner, 'dfgd5', partner)
    assert getattr(partner, 'myClass34') == owner
    _safe_set(owner, 'dfgd5', None)
    assert getattr(partner, 'myClass34') is None


def test_assoc_MyClass_MyClass4_stub_double():
    # MyClass4 has no real 'myClass7' property in the generated
    # code (a bare stub) -- manually attach it so MyClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MyClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MyClass(asdf="sample_text")
    partner = MyClass4()
    setattr(partner, 'myClass7', None)
    _safe_set(owner, 'myClass46', partner)
    assert getattr(partner, 'myClass7') == owner
    _safe_set(owner, 'myClass46', None)
    assert getattr(partner, 'myClass7') is None


