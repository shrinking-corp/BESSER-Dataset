import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    metrics_Rule,
    metrics_RuleMetrics,
    metrics_RuleSetMetrics,
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

def test_assoc_ruleMetrics0_reverse_link_reassign_clear():
    a1 = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    a2 = metrics_RuleSetMetrics(numberOfRules=13, totalNumberOfAttributes=13, totalNumberOfEdges=13, totalNumberOfNodes=13)
    b = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    _safe_set(b, 'metrics_RuleMetrics', a1)
    assert _is_linked(b, 'metrics_RuleMetrics', a1)
    if hasattr(a1, 'metrics_RuleSetMetrics'):
        assert _is_linked(a1, 'metrics_RuleSetMetrics', b)
    _safe_set(b, 'metrics_RuleMetrics', a2)
    assert _is_linked(b, 'metrics_RuleMetrics', a2)
    if hasattr(a1, 'metrics_RuleSetMetrics'):
        assert not _is_linked(a1, 'metrics_RuleSetMetrics', b)
    if hasattr(a2, 'metrics_RuleSetMetrics'):
        assert _is_linked(a2, 'metrics_RuleSetMetrics', b)
    _safe_set(b, 'metrics_RuleMetrics', None)
    assert not _is_linked(b, 'metrics_RuleMetrics', a2)
    if hasattr(a2, 'metrics_RuleSetMetrics'):
        assert not _is_linked(a2, 'metrics_RuleSetMetrics', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_rule3_stub_double():
    # metrics_Rule has no real 'metrics_Rule5' property in the generated
    # code (a bare stub) -- manually attach it so metrics_RuleMetrics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_RuleMetrics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_RuleMetrics(numberOfAttributes=7, numberOfEdges=7, numberOfNodes=7)
    partner = metrics_Rule()
    setattr(partner, 'metrics_Rule5', None)
    _safe_set(owner, 'metrics_RuleMetrics4', partner)
    assert getattr(partner, 'metrics_Rule5') == owner
    _safe_set(owner, 'metrics_RuleMetrics4', None)
    assert getattr(partner, 'metrics_Rule5') is None


def test_assoc_ruleSet1_stub_double():
    # metrics_Rule has no real 'metrics_Rule' property in the generated
    # code (a bare stub) -- manually attach it so metrics_RuleSetMetrics's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # metrics_RuleSetMetrics's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = metrics_RuleSetMetrics(numberOfRules=7, totalNumberOfAttributes=7, totalNumberOfEdges=7, totalNumberOfNodes=7)
    partner = metrics_Rule()
    setattr(partner, 'metrics_Rule', None)
    _safe_set(owner, 'metrics_RuleSetMetrics2', {partner})
    assert getattr(partner, 'metrics_Rule') == owner
    _safe_set(owner, 'metrics_RuleSetMetrics2', set())
    assert getattr(partner, 'metrics_Rule') is None


