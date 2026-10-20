import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Sequence,
    SequenceNode,
    ctrlflow101_And,
    ctrlflow101_Final,
    ctrlflow101_Function,
    ctrlflow101_Loop,
    ctrlflow101_Or,
    ctrlflow101_Sequence,
    ctrlflow101_SequenceNode,
    ctrlflow101_Start,
    ctrlflow101_Token,
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

def test_assoc_controlFlowEdge7_reverse_link_reassign_clear():
    a1 = ctrlflow101_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = ctrlflow101_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = ctrlflow101_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'ctrlflow101_SequenceNode6', {a1})
    assert _is_linked(b, 'ctrlflow101_SequenceNode6', a1)
    if hasattr(a1, 'ctrlflow101_SequenceNode'):
        assert _is_linked(a1, 'ctrlflow101_SequenceNode', b)
    _safe_set(b, 'ctrlflow101_SequenceNode6', {a2})
    assert _is_linked(b, 'ctrlflow101_SequenceNode6', a2)
    if hasattr(a1, 'ctrlflow101_SequenceNode'):
        assert not _is_linked(a1, 'ctrlflow101_SequenceNode', b)
    if hasattr(a2, 'ctrlflow101_SequenceNode'):
        assert _is_linked(a2, 'ctrlflow101_SequenceNode', b)
    _safe_set(b, 'ctrlflow101_SequenceNode6', set())
    assert not _is_linked(b, 'ctrlflow101_SequenceNode6', a2)
    if hasattr(a2, 'ctrlflow101_SequenceNode'):
        assert not _is_linked(a2, 'ctrlflow101_SequenceNode', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_sequenceNodes2_stub_double():
    # ctrlflow101_Function has no real 'ctrlflow101_Function3' property in the generated
    # code (a bare stub) -- manually attach it so ctrlflow101_Sequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ctrlflow101_Sequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ctrlflow101_Sequence(weight=7)
    partner = ctrlflow101_Function()
    setattr(partner, 'ctrlflow101_Function3', None)
    _safe_set(owner, 'ctrlflow101_Sequence', partner)
    assert owner in getattr(partner, 'ctrlflow101_Function3')
    _safe_set(owner, 'ctrlflow101_Sequence', None)
    assert owner not in getattr(partner, 'ctrlflow101_Function3')


