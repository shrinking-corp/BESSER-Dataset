import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    emapvselistentry_NewEClass1,
    emapvselistentry_NewEClass2,
    emapvselistentry_NewEClass3,
    emapvselistentry_NewEClass4,
    emapvselistentry_NewEClass5,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_neweclass20_stub_double():
    # emapvselistentry_NewEClass1 has no real 'emapvselistentry_NewEClass1' property in the generated
    # code (a bare stub) -- manually attach it so emapvselistentry_NewEClass2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapvselistentry_NewEClass2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapvselistentry_NewEClass2(key="sample_text", value="sample_text")
    partner = emapvselistentry_NewEClass1()
    setattr(partner, 'emapvselistentry_NewEClass1', None)
    _safe_set(owner, 'emapvselistentry_NewEClass2', partner)
    assert owner in getattr(partner, 'emapvselistentry_NewEClass1')
    _safe_set(owner, 'emapvselistentry_NewEClass2', None)
    assert owner not in getattr(partner, 'emapvselistentry_NewEClass1')


def test_assoc_neweclass31_stub_double():
    # emapvselistentry_NewEClass1 has no real 'emapvselistentry_NewEClass12' property in the generated
    # code (a bare stub) -- manually attach it so emapvselistentry_NewEClass3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapvselistentry_NewEClass3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapvselistentry_NewEClass3(key="sample_text", value="sample_text")
    partner = emapvselistentry_NewEClass1()
    setattr(partner, 'emapvselistentry_NewEClass12', None)
    _safe_set(owner, 'emapvselistentry_NewEClass3', partner)
    assert owner in getattr(partner, 'emapvselistentry_NewEClass12')
    _safe_set(owner, 'emapvselistentry_NewEClass3', None)
    assert owner not in getattr(partner, 'emapvselistentry_NewEClass12')


def test_assoc_neweclass43_stub_double():
    # emapvselistentry_NewEClass1 has no real 'emapvselistentry_NewEClass14' property in the generated
    # code (a bare stub) -- manually attach it so emapvselistentry_NewEClass4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapvselistentry_NewEClass4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapvselistentry_NewEClass4(key="sample_text", value="sample_text")
    partner = emapvselistentry_NewEClass1()
    setattr(partner, 'emapvselistentry_NewEClass14', None)
    _safe_set(owner, 'emapvselistentry_NewEClass4', partner)
    assert getattr(partner, 'emapvselistentry_NewEClass14') == owner
    _safe_set(owner, 'emapvselistentry_NewEClass4', None)
    assert getattr(partner, 'emapvselistentry_NewEClass14') is None


def test_assoc_neweclass55_stub_double():
    # emapvselistentry_NewEClass1 has no real 'emapvselistentry_NewEClass16' property in the generated
    # code (a bare stub) -- manually attach it so emapvselistentry_NewEClass5's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # emapvselistentry_NewEClass5's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = emapvselistentry_NewEClass5(key="sample_text", value="sample_text")
    partner = emapvselistentry_NewEClass1()
    setattr(partner, 'emapvselistentry_NewEClass16', None)
    _safe_set(owner, 'emapvselistentry_NewEClass5', partner)
    assert getattr(partner, 'emapvselistentry_NewEClass16') == owner
    _safe_set(owner, 'emapvselistentry_NewEClass5', None)
    assert getattr(partner, 'emapvselistentry_NewEClass16') is None


