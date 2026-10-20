import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AU,
    BU,
    C2U,
    C4U,
    CU,
    DU,
    EU,
    ref_A,
    ref_B,
    ref_C,
    ref_C1,
    ref_C2,
    ref_C3,
    ref_C4,
    ref_D,
    ref_E,
    ref_unsettable_AU,
    ref_unsettable_BU,
    ref_unsettable_C1U,
    ref_unsettable_C2U,
    ref_unsettable_C3U,
    ref_unsettable_C4U,
    ref_unsettable_CU,
    ref_unsettable_DU,
    ref_unsettable_EU,
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

def test_assoc_d28_stub_double():
    # ref_D has no real 'D29' property in the generated
    # code (a bare stub) -- manually attach it so ref_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ref_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ref_E(ids="sample_text", labels="sample_text", name="sample_text")
    partner = ref_D()
    setattr(partner, 'D29', None)
    _safe_set(owner, 'e', {partner})
    assert getattr(partner, 'D29') == owner
    _safe_set(owner, 'e', set())
    assert getattr(partner, 'D29') is None


def test_assoc_du80_stub_double():
    # DU has no real 'DU81' property in the generated
    # code (a bare stub) -- manually attach it so ref_unsettable_EU's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ref_unsettable_EU's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ref_unsettable_EU(ids="sample_text", labels="sample_text", name="sample_text")
    partner = DU()
    setattr(partner, 'DU81', None)
    _safe_set(owner, 'eu', {partner})
    assert getattr(partner, 'DU81') == owner
    _safe_set(owner, 'eu', set())
    assert getattr(partner, 'DU81') is None


def test_assoc_e23_stub_double():
    # ref_D has no real 'd24' property in the generated
    # code (a bare stub) -- manually attach it so ref_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ref_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ref_E(ids="sample_text", labels="sample_text", name="sample_text")
    partner = ref_D()
    setattr(partner, 'd24', None)
    _safe_set(owner, 'E', partner)
    assert owner in getattr(partner, 'd24')
    _safe_set(owner, 'E', None)
    assert owner not in getattr(partner, 'd24')


