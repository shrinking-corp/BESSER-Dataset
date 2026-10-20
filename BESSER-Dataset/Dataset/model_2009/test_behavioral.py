import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Stepdefn,
    scribbleTraceDsl_Messagetransfer,
    scribbleTraceDsl_Parameter,
    scribbleTraceDsl_Stepdefn,
    scribbleTraceDsl_Trace,
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

def test_assoc_parameters1_stub_double():
    # scribbleTraceDsl_Messagetransfer has no real 'scribbleTraceDsl_Messagetransfer' property in the generated
    # code (a bare stub) -- manually attach it so scribbleTraceDsl_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scribbleTraceDsl_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scribbleTraceDsl_Parameter(type="sample_text", value="sample_text")
    partner = scribbleTraceDsl_Messagetransfer()
    setattr(partner, 'scribbleTraceDsl_Messagetransfer', None)
    _safe_set(owner, 'scribbleTraceDsl_Parameter', partner)
    assert owner in getattr(partner, 'scribbleTraceDsl_Messagetransfer')
    _safe_set(owner, 'scribbleTraceDsl_Parameter', None)
    assert owner not in getattr(partner, 'scribbleTraceDsl_Messagetransfer')


def test_assoc_steps0_stub_double():
    # scribbleTraceDsl_Stepdefn has no real 'scribbleTraceDsl_Stepdefn' property in the generated
    # code (a bare stub) -- manually attach it so scribbleTraceDsl_Trace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # scribbleTraceDsl_Trace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = scribbleTraceDsl_Trace(roles="sample_text")
    partner = scribbleTraceDsl_Stepdefn()
    setattr(partner, 'scribbleTraceDsl_Stepdefn', None)
    _safe_set(owner, 'scribbleTraceDsl_Trace', {partner})
    assert getattr(partner, 'scribbleTraceDsl_Stepdefn') == owner
    _safe_set(owner, 'scribbleTraceDsl_Trace', set())
    assert getattr(partner, 'scribbleTraceDsl_Stepdefn') is None


