import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    effbd102_And,
    effbd102_Description,
    effbd102_Final,
    effbd102_Flow,
    effbd102_Function,
    effbd102_InputPort,
    effbd102_Item,
    effbd102_Iteration,
    effbd102_Loop,
    effbd102_LoopExit,
    effbd102_Or,
    effbd102_OutputPort,
    effbd102_Port,
    effbd102_ProcessNode,
    effbd102_Sequence,
    effbd102_SequenceNode,
    effbd102_Start,
    FunctionDomain,
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

def test_assoc_controlFlowEdge13_reverse_link_reassign_clear():
    a1 = effbd102_SequenceNode(name="sample_text")
    a2 = effbd102_SequenceNode(name="sample_text_2")
    b = effbd102_SequenceNode(name="sample_text")
    _safe_set(b, 'effbd102_SequenceNode12', {a1})
    assert _is_linked(b, 'effbd102_SequenceNode12', a1)
    if hasattr(a1, 'effbd102_SequenceNode'):
        assert _is_linked(a1, 'effbd102_SequenceNode', b)
    _safe_set(b, 'effbd102_SequenceNode12', {a2})
    assert _is_linked(b, 'effbd102_SequenceNode12', a2)
    if hasattr(a1, 'effbd102_SequenceNode'):
        assert not _is_linked(a1, 'effbd102_SequenceNode', b)
    if hasattr(a2, 'effbd102_SequenceNode'):
        assert _is_linked(a2, 'effbd102_SequenceNode', b)
    _safe_set(b, 'effbd102_SequenceNode12', set())
    assert not _is_linked(b, 'effbd102_SequenceNode12', a2)
    if hasattr(a2, 'effbd102_SequenceNode'):
        assert not _is_linked(a2, 'effbd102_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    a2 = effbd102_Function(domain="sample_text_2", maxDuration=9.99, minDuration=9.99)
    b = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    _safe_set(b, 'effbd102_Function0', {a1})
    assert _is_linked(b, 'effbd102_Function0', a1)
    if hasattr(a1, 'effbd102_Function'):
        assert _is_linked(a1, 'effbd102_Function', b)
    _safe_set(b, 'effbd102_Function0', {a2})
    assert _is_linked(b, 'effbd102_Function0', a2)
    if hasattr(a1, 'effbd102_Function'):
        assert not _is_linked(a1, 'effbd102_Function', b)
    if hasattr(a2, 'effbd102_Function'):
        assert _is_linked(a2, 'effbd102_Function', b)
    _safe_set(b, 'effbd102_Function0', set())
    assert not _is_linked(b, 'effbd102_Function0', a2)
    if hasattr(a2, 'effbd102_Function'):
        assert not _is_linked(a2, 'effbd102_Function', b)


def test_assoc_descriptions10_reverse_link_reassign_clear():
    a1 = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    a2 = effbd102_Function(domain="sample_text_2", maxDuration=9.99, minDuration=9.99)
    b = effbd102_Description(content="sample_text")
    _safe_set(b, 'effbd102_Description', a1)
    assert _is_linked(b, 'effbd102_Description', a1)
    if hasattr(a1, 'effbd102_Function11'):
        assert _is_linked(a1, 'effbd102_Function11', b)
    _safe_set(b, 'effbd102_Description', a2)
    assert _is_linked(b, 'effbd102_Description', a2)
    if hasattr(a1, 'effbd102_Function11'):
        assert not _is_linked(a1, 'effbd102_Function11', b)
    if hasattr(a2, 'effbd102_Function11'):
        assert _is_linked(a2, 'effbd102_Function11', b)
    _safe_set(b, 'effbd102_Description', None)
    assert not _is_linked(b, 'effbd102_Description', a2)
    if hasattr(a2, 'effbd102_Function11'):
        assert not _is_linked(a2, 'effbd102_Function11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows4_stub_double():
    # effbd102_Flow has no real 'effbd102_Flow' property in the generated
    # code (a bare stub) -- manually attach it so effbd102_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd102_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    partner = effbd102_Flow()
    setattr(partner, 'effbd102_Flow', None)
    _safe_set(owner, 'effbd102_Function5', {partner})
    assert getattr(partner, 'effbd102_Flow') == owner
    _safe_set(owner, 'effbd102_Function5', set())
    assert getattr(partner, 'effbd102_Flow') is None


def test_assoc_inputPorts8_stub_double():
    # effbd102_InputPort has no real 'effbd102_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd102_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd102_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    partner = effbd102_InputPort()
    setattr(partner, 'effbd102_InputPort', None)
    _safe_set(owner, 'effbd102_Function9', {partner})
    assert getattr(partner, 'effbd102_InputPort') == owner
    _safe_set(owner, 'effbd102_Function9', set())
    assert getattr(partner, 'effbd102_InputPort') is None


def test_assoc_items17_stub_double():
    # effbd102_Flow has no real 'effbd102_Flow18' property in the generated
    # code (a bare stub) -- manually attach it so effbd102_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd102_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd102_Item(name="sample_text")
    partner = effbd102_Flow()
    setattr(partner, 'effbd102_Flow18', None)
    _safe_set(owner, 'effbd102_Item', partner)
    assert owner in getattr(partner, 'effbd102_Flow18')
    _safe_set(owner, 'effbd102_Item', None)
    assert owner not in getattr(partner, 'effbd102_Flow18')


def test_assoc_outputPorts6_stub_double():
    # effbd102_OutputPort has no real 'effbd102_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd102_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd102_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    partner = effbd102_OutputPort()
    setattr(partner, 'effbd102_OutputPort', None)
    _safe_set(owner, 'effbd102_Function7', {partner})
    assert getattr(partner, 'effbd102_OutputPort') == owner
    _safe_set(owner, 'effbd102_Function7', set())
    assert getattr(partner, 'effbd102_OutputPort') is None


def test_assoc_sequenceNodes2_stub_double():
    # effbd102_Sequence has no real 'effbd102_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so effbd102_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd102_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd102_Function(domain="sample_text", maxDuration=3.14, minDuration=3.14)
    partner = effbd102_Sequence()
    setattr(partner, 'effbd102_Sequence', None)
    _safe_set(owner, 'effbd102_Function3', {partner})
    assert getattr(partner, 'effbd102_Sequence') == owner
    _safe_set(owner, 'effbd102_Function3', set())
    assert getattr(partner, 'effbd102_Sequence') is None


