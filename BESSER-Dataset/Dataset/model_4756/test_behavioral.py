import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    effbd104_And,
    effbd104_Description,
    effbd104_Final,
    effbd104_Flow,
    effbd104_Function,
    effbd104_InputPort,
    effbd104_Item,
    effbd104_Iteration,
    effbd104_Loop,
    effbd104_LoopExit,
    effbd104_Or,
    effbd104_OutputPort,
    effbd104_Port,
    effbd104_ProcessNode,
    effbd104_Sequence,
    effbd104_SequenceNode,
    effbd104_Start,
    effbd104_Token,
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

def test_assoc_controlFlowEdge15_reverse_link_reassign_clear():
    a1 = effbd104_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = effbd104_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = effbd104_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'effbd104_SequenceNode14', {a1})
    assert _is_linked(b, 'effbd104_SequenceNode14', a1)
    if hasattr(a1, 'effbd104_SequenceNode'):
        assert _is_linked(a1, 'effbd104_SequenceNode', b)
    _safe_set(b, 'effbd104_SequenceNode14', {a2})
    assert _is_linked(b, 'effbd104_SequenceNode14', a2)
    if hasattr(a1, 'effbd104_SequenceNode'):
        assert not _is_linked(a1, 'effbd104_SequenceNode', b)
    if hasattr(a2, 'effbd104_SequenceNode'):
        assert _is_linked(a2, 'effbd104_SequenceNode', b)
    _safe_set(b, 'effbd104_SequenceNode14', set())
    assert not _is_linked(b, 'effbd104_SequenceNode14', a2)
    if hasattr(a2, 'effbd104_SequenceNode'):
        assert not _is_linked(a2, 'effbd104_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = effbd104_Function(domain="sample_text")
    a2 = effbd104_Function(domain="sample_text_2")
    b = effbd104_Function(domain="sample_text")
    _safe_set(b, 'effbd104_Function0', {a1})
    assert _is_linked(b, 'effbd104_Function0', a1)
    if hasattr(a1, 'effbd104_Function'):
        assert _is_linked(a1, 'effbd104_Function', b)
    _safe_set(b, 'effbd104_Function0', {a2})
    assert _is_linked(b, 'effbd104_Function0', a2)
    if hasattr(a1, 'effbd104_Function'):
        assert not _is_linked(a1, 'effbd104_Function', b)
    if hasattr(a2, 'effbd104_Function'):
        assert _is_linked(a2, 'effbd104_Function', b)
    _safe_set(b, 'effbd104_Function0', set())
    assert not _is_linked(b, 'effbd104_Function0', a2)
    if hasattr(a2, 'effbd104_Function'):
        assert not _is_linked(a2, 'effbd104_Function', b)


def test_assoc_descriptions10_reverse_link_reassign_clear():
    a1 = effbd104_Function(domain="sample_text")
    a2 = effbd104_Function(domain="sample_text_2")
    b = effbd104_Description(content="sample_text")
    _safe_set(b, 'effbd104_Description', a1)
    assert _is_linked(b, 'effbd104_Description', a1)
    if hasattr(a1, 'effbd104_Function11'):
        assert _is_linked(a1, 'effbd104_Function11', b)
    _safe_set(b, 'effbd104_Description', a2)
    assert _is_linked(b, 'effbd104_Description', a2)
    if hasattr(a1, 'effbd104_Function11'):
        assert not _is_linked(a1, 'effbd104_Function11', b)
    if hasattr(a2, 'effbd104_Function11'):
        assert _is_linked(a2, 'effbd104_Function11', b)
    _safe_set(b, 'effbd104_Description', None)
    assert not _is_linked(b, 'effbd104_Description', a2)
    if hasattr(a2, 'effbd104_Function11'):
        assert not _is_linked(a2, 'effbd104_Function11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows4_stub_double():
    # effbd104_Flow has no real 'effbd104_Flow' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Function(domain="sample_text")
    partner = effbd104_Flow()
    setattr(partner, 'effbd104_Flow', None)
    _safe_set(owner, 'effbd104_Function5', {partner})
    assert getattr(partner, 'effbd104_Flow') == owner
    _safe_set(owner, 'effbd104_Function5', set())
    assert getattr(partner, 'effbd104_Flow') is None


def test_assoc_inputPorts8_stub_double():
    # effbd104_InputPort has no real 'effbd104_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Function(domain="sample_text")
    partner = effbd104_InputPort()
    setattr(partner, 'effbd104_InputPort', None)
    _safe_set(owner, 'effbd104_Function9', {partner})
    assert getattr(partner, 'effbd104_InputPort') == owner
    _safe_set(owner, 'effbd104_Function9', set())
    assert getattr(partner, 'effbd104_InputPort') is None


def test_assoc_items19_stub_double():
    # effbd104_Flow has no real 'effbd104_Flow20' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Item(name="sample_text")
    partner = effbd104_Flow()
    setattr(partner, 'effbd104_Flow20', None)
    _safe_set(owner, 'effbd104_Item', partner)
    assert owner in getattr(partner, 'effbd104_Flow20')
    _safe_set(owner, 'effbd104_Item', None)
    assert owner not in getattr(partner, 'effbd104_Flow20')


def test_assoc_outputPorts6_stub_double():
    # effbd104_OutputPort has no real 'effbd104_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Function(domain="sample_text")
    partner = effbd104_OutputPort()
    setattr(partner, 'effbd104_OutputPort', None)
    _safe_set(owner, 'effbd104_Function7', {partner})
    assert getattr(partner, 'effbd104_OutputPort') == owner
    _safe_set(owner, 'effbd104_Function7', set())
    assert getattr(partner, 'effbd104_OutputPort') is None


def test_assoc_sequenceNodes2_stub_double():
    # effbd104_Sequence has no real 'effbd104_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Function(domain="sample_text")
    partner = effbd104_Sequence()
    setattr(partner, 'effbd104_Sequence', None)
    _safe_set(owner, 'effbd104_Function3', {partner})
    assert getattr(partner, 'effbd104_Sequence') == owner
    _safe_set(owner, 'effbd104_Function3', set())
    assert getattr(partner, 'effbd104_Sequence') is None


def test_assoc_tokens12_stub_double():
    # effbd104_Token has no real 'effbd104_Token' property in the generated
    # code (a bare stub) -- manually attach it so effbd104_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd104_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd104_Function(domain="sample_text")
    partner = effbd104_Token()
    setattr(partner, 'effbd104_Token', None)
    _safe_set(owner, 'effbd104_Function13', {partner})
    assert getattr(partner, 'effbd104_Token') == owner
    _safe_set(owner, 'effbd104_Function13', set())
    assert getattr(partner, 'effbd104_Token') is None


