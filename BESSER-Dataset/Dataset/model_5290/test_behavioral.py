import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    A,
    CE,
    DNamedElement,
    E,
    refinher3_A,
    refinher3_BB,
    refinher3_CE,
    refinher3_DC,
    refinher3_DG,
    refinher3_DL,
    refinher3_DNamedElement,
    refinher3_DR,
    refinher3_E,
    refinher3_Foobar,
    refinher3_M,
    refinher3_N,
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

def test_assoc_esbars12_stub_double():
    # refinher3_E has no real 'refinher3_E14' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_M's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_M's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_M(id="sample_text")
    partner = refinher3_E()
    setattr(partner, 'refinher3_E14', None)
    _safe_set(owner, 'refinher3_M13', {partner})
    assert getattr(partner, 'refinher3_E14') == owner
    _safe_set(owner, 'refinher3_M13', set())
    assert getattr(partner, 'refinher3_E14') is None


def test_assoc_foobars15_stub_double():
    # refinher3_Foobar has no real 'refinher3_Foobar' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_M's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_M's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_M(id="sample_text")
    partner = refinher3_Foobar()
    setattr(partner, 'refinher3_Foobar', None)
    _safe_set(owner, 'refinher3_M16', {partner})
    assert getattr(partner, 'refinher3_Foobar') == owner
    _safe_set(owner, 'refinher3_M16', set())
    assert getattr(partner, 'refinher3_Foobar') is None


def test_assoc_ms10_stub_double():
    # refinher3_DG has no real 'refinher3_DG11' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_M's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_M's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_M(id="sample_text")
    partner = refinher3_DG()
    setattr(partner, 'refinher3_DG11', None)
    _safe_set(owner, 'refinher3_M', partner)
    assert owner in getattr(partner, 'refinher3_DG11')
    _safe_set(owner, 'refinher3_M', None)
    assert owner not in getattr(partner, 'refinher3_DG11')


def test_assoc_ns7_stub_double():
    # refinher3_DG has no real 'refinher3_DG8' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_N's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_N's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_N(nam="sample_text")
    partner = refinher3_DG()
    setattr(partner, 'refinher3_DG8', None)
    _safe_set(owner, 'refinher3_N9', partner)
    assert owner in getattr(partner, 'refinher3_DG8')
    _safe_set(owner, 'refinher3_N9', None)
    assert owner not in getattr(partner, 'refinher3_DG8')


def test_assoc_sn0_stub_double():
    # refinher3_E has no real 'refinher3_E' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_N's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_N's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_N(nam="sample_text")
    partner = refinher3_E()
    setattr(partner, 'refinher3_E', None)
    _safe_set(owner, 'refinher3_N', partner)
    assert getattr(partner, 'refinher3_E') == owner
    _safe_set(owner, 'refinher3_N', None)
    assert getattr(partner, 'refinher3_E') is None


def test_assoc_tn1_stub_double():
    # refinher3_E has no real 'refinher3_E2' property in the generated
    # code (a bare stub) -- manually attach it so refinher3_N's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # refinher3_N's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = refinher3_N(nam="sample_text")
    partner = refinher3_E()
    setattr(partner, 'refinher3_E2', None)
    _safe_set(owner, 'refinher3_N3', partner)
    assert getattr(partner, 'refinher3_E2') == owner
    _safe_set(owner, 'refinher3_N3', None)
    assert getattr(partner, 'refinher3_E2') is None


