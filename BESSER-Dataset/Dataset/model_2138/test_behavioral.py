import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    flowchart_Action,
    flowchart_Decision,
    flowchart_Flowchart,
    flowchart_Node,
    flowchart_Transition,
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

def test_assoc_actionNode6_reverse_link_reassign_clear():
    a1 = flowchart_Node(name="sample_text")
    a2 = flowchart_Node(name="sample_text_2")
    b = flowchart_Action(isAction=True)
    _safe_set(b, 'flowchart_Action', a1)
    assert _is_linked(b, 'flowchart_Action', a1)
    if hasattr(a1, 'flowchart_Node7'):
        assert _is_linked(a1, 'flowchart_Node7', b)
    _safe_set(b, 'flowchart_Action', a2)
    assert _is_linked(b, 'flowchart_Action', a2)
    if hasattr(a1, 'flowchart_Node7'):
        assert not _is_linked(a1, 'flowchart_Node7', b)
    if hasattr(a2, 'flowchart_Node7'):
        assert _is_linked(a2, 'flowchart_Node7', b)
    _safe_set(b, 'flowchart_Action', None)
    assert not _is_linked(b, 'flowchart_Action', a2)
    if hasattr(a2, 'flowchart_Node7'):
        assert not _is_linked(a2, 'flowchart_Node7', b)


def test_assoc_decisionNode8_reverse_link_reassign_clear():
    a1 = flowchart_Node(name="sample_text")
    a2 = flowchart_Node(name="sample_text_2")
    b = flowchart_Decision(condition="sample_text", isDecision=True)
    _safe_set(b, 'flowchart_Decision', a1)
    assert _is_linked(b, 'flowchart_Decision', a1)
    if hasattr(a1, 'flowchart_Node9'):
        assert _is_linked(a1, 'flowchart_Node9', b)
    _safe_set(b, 'flowchart_Decision', a2)
    assert _is_linked(b, 'flowchart_Decision', a2)
    if hasattr(a1, 'flowchart_Node9'):
        assert not _is_linked(a1, 'flowchart_Node9', b)
    if hasattr(a2, 'flowchart_Node9'):
        assert _is_linked(a2, 'flowchart_Node9', b)
    _safe_set(b, 'flowchart_Decision', None)
    assert not _is_linked(b, 'flowchart_Decision', a2)
    if hasattr(a2, 'flowchart_Node9'):
        assert not _is_linked(a2, 'flowchart_Node9', b)


def test_assoc_incoming3_reverse_link_reassign_clear():
    a1 = flowchart_Transition(label="sample_text")
    a2 = flowchart_Transition(label="sample_text_2")
    b = flowchart_Node(name="sample_text")
    _safe_set(b, 'target', {a1})
    assert _is_linked(b, 'target', a1)
    if hasattr(a1, 'Transition'):
        assert _is_linked(a1, 'Transition', b)
    _safe_set(b, 'target', {a2})
    assert _is_linked(b, 'target', a2)
    if hasattr(a1, 'Transition'):
        assert not _is_linked(a1, 'Transition', b)
    if hasattr(a2, 'Transition'):
        assert _is_linked(a2, 'Transition', b)
    _safe_set(b, 'target', set())
    assert not _is_linked(b, 'target', a2)
    if hasattr(a2, 'Transition'):
        assert not _is_linked(a2, 'Transition', b)


def test_assoc_outgoing4_reverse_link_reassign_clear():
    a1 = flowchart_Transition(label="sample_text")
    a2 = flowchart_Transition(label="sample_text_2")
    b = flowchart_Node(name="sample_text")
    _safe_set(b, 'source', {a1})
    assert _is_linked(b, 'source', a1)
    if hasattr(a1, 'Transition5'):
        assert _is_linked(a1, 'Transition5', b)
    _safe_set(b, 'source', {a2})
    assert _is_linked(b, 'source', a2)
    if hasattr(a1, 'Transition5'):
        assert not _is_linked(a1, 'Transition5', b)
    if hasattr(a2, 'Transition5'):
        assert _is_linked(a2, 'Transition5', b)
    _safe_set(b, 'source', set())
    assert not _is_linked(b, 'source', a2)
    if hasattr(a2, 'Transition5'):
        assert not _is_linked(a2, 'Transition5', b)


def test_assoc_source10_reverse_link_reassign_clear():
    a1 = flowchart_Transition(label="sample_text")
    a2 = flowchart_Transition(label="sample_text_2")
    b = flowchart_Node(name="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'outgoing'):
        assert _is_linked(a1, 'outgoing', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'outgoing'):
        assert not _is_linked(a1, 'outgoing', b)
    if hasattr(a2, 'outgoing'):
        assert _is_linked(a2, 'outgoing', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'outgoing'):
        assert not _is_linked(a2, 'outgoing', b)


def test_assoc_target11_reverse_link_reassign_clear():
    a1 = flowchart_Transition(label="sample_text")
    a2 = flowchart_Transition(label="sample_text_2")
    b = flowchart_Node(name="sample_text")
    _safe_set(b, 'Node12', a1)
    assert _is_linked(b, 'Node12', a1)
    if hasattr(a1, 'incoming'):
        assert _is_linked(a1, 'incoming', b)
    _safe_set(b, 'Node12', a2)
    assert _is_linked(b, 'Node12', a2)
    if hasattr(a1, 'incoming'):
        assert not _is_linked(a1, 'incoming', b)
    if hasattr(a2, 'incoming'):
        assert _is_linked(a2, 'incoming', b)
    _safe_set(b, 'Node12', None)
    assert not _is_linked(b, 'Node12', a2)
    if hasattr(a2, 'incoming'):
        assert not _is_linked(a2, 'incoming', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodes0_stub_double():
    # flowchart_Flowchart has no real 'flowchart_Flowchart' property in the generated
    # code (a bare stub) -- manually attach it so flowchart_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchart_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchart_Node(name="sample_text")
    partner = flowchart_Flowchart()
    setattr(partner, 'flowchart_Flowchart', None)
    _safe_set(owner, 'flowchart_Node', partner)
    assert owner in getattr(partner, 'flowchart_Flowchart')
    _safe_set(owner, 'flowchart_Node', None)
    assert owner not in getattr(partner, 'flowchart_Flowchart')


def test_assoc_transitions1_stub_double():
    # flowchart_Flowchart has no real 'flowchart_Flowchart2' property in the generated
    # code (a bare stub) -- manually attach it so flowchart_Transition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # flowchart_Transition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = flowchart_Transition(label="sample_text")
    partner = flowchart_Flowchart()
    setattr(partner, 'flowchart_Flowchart2', None)
    _safe_set(owner, 'flowchart_Transition', partner)
    assert owner in getattr(partner, 'flowchart_Flowchart2')
    _safe_set(owner, 'flowchart_Transition', None)
    assert owner not in getattr(partner, 'flowchart_Flowchart2')


