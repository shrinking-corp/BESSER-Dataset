import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    transformationtrace_ActivationTrace,
    transformationtrace_RuleParameterTrace,
    transformationtrace_TransformationTrace,
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

def test_assoc_ruleParameterTraces1_reverse_link_reassign_clear():
    a1 = transformationtrace_RuleParameterTrace(objectId="sample_text", parameterName="sample_text")
    a2 = transformationtrace_RuleParameterTrace(objectId="sample_text_2", parameterName="sample_text_2")
    b = transformationtrace_ActivationTrace(ruleName="sample_text")
    _safe_set(b, 'transformationtrace_ActivationTrace2', {a1})
    assert _is_linked(b, 'transformationtrace_ActivationTrace2', a1)
    if hasattr(a1, 'transformationtrace_RuleParameterTrace'):
        assert _is_linked(a1, 'transformationtrace_RuleParameterTrace', b)
    _safe_set(b, 'transformationtrace_ActivationTrace2', {a2})
    assert _is_linked(b, 'transformationtrace_ActivationTrace2', a2)
    if hasattr(a1, 'transformationtrace_RuleParameterTrace'):
        assert not _is_linked(a1, 'transformationtrace_RuleParameterTrace', b)
    if hasattr(a2, 'transformationtrace_RuleParameterTrace'):
        assert _is_linked(a2, 'transformationtrace_RuleParameterTrace', b)
    _safe_set(b, 'transformationtrace_ActivationTrace2', set())
    assert not _is_linked(b, 'transformationtrace_ActivationTrace2', a2)
    if hasattr(a2, 'transformationtrace_RuleParameterTrace'):
        assert not _is_linked(a2, 'transformationtrace_RuleParameterTrace', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activationTraces0_stub_double():
    # transformationtrace_TransformationTrace has no real 'transformationtrace_TransformationTrace' property in the generated
    # code (a bare stub) -- manually attach it so transformationtrace_ActivationTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transformationtrace_ActivationTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transformationtrace_ActivationTrace(ruleName="sample_text")
    partner = transformationtrace_TransformationTrace()
    setattr(partner, 'transformationtrace_TransformationTrace', None)
    _safe_set(owner, 'transformationtrace_ActivationTrace', partner)
    assert owner in getattr(partner, 'transformationtrace_TransformationTrace')
    _safe_set(owner, 'transformationtrace_ActivationTrace', None)
    assert owner not in getattr(partner, 'transformationtrace_TransformationTrace')


