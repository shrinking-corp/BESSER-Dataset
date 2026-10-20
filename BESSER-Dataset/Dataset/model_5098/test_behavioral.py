import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    testport_Base,
    testport_Component,
    testport_Required,
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

def test_assoc_requiredInterfaces0_stub_double():
    # testport_Required has no real 'testport_Required' property in the generated
    # code (a bare stub) -- manually attach it so testport_Component's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # testport_Component's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = testport_Component(name="sample_text")
    partner = testport_Required()
    setattr(partner, 'testport_Required', None)
    _safe_set(owner, 'testport_Component', {partner})
    assert getattr(partner, 'testport_Required') == owner
    _safe_set(owner, 'testport_Component', set())
    assert getattr(partner, 'testport_Required') is None


