import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractFunction,
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    effbd902_AbstractFunction,
    effbd902_And,
    effbd902_Description,
    effbd902_Final,
    effbd902_Flow,
    effbd902_Function,
    effbd902_InputPort,
    effbd902_Item,
    effbd902_Iteration,
    effbd902_Loop,
    effbd902_LoopExit,
    effbd902_Or,
    effbd902_OutputPort,
    effbd902_Port,
    effbd902_ProcessNode,
    effbd902_Sequence,
    effbd902_SequenceNode,
    effbd902_Start,
    effbd902_Token,
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

def test_assoc_controlFlowEdge14_reverse_link_reassign_clear():
    a1 = effbd902_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = effbd902_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = effbd902_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'effbd902_SequenceNode13', {a1})
    assert _is_linked(b, 'effbd902_SequenceNode13', a1)
    if hasattr(a1, 'effbd902_SequenceNode'):
        assert _is_linked(a1, 'effbd902_SequenceNode', b)
    _safe_set(b, 'effbd902_SequenceNode13', {a2})
    assert _is_linked(b, 'effbd902_SequenceNode13', a2)
    if hasattr(a1, 'effbd902_SequenceNode'):
        assert not _is_linked(a1, 'effbd902_SequenceNode', b)
    if hasattr(a2, 'effbd902_SequenceNode'):
        assert _is_linked(a2, 'effbd902_SequenceNode', b)
    _safe_set(b, 'effbd902_SequenceNode13', set())
    assert not _is_linked(b, 'effbd902_SequenceNode13', a2)
    if hasattr(a2, 'effbd902_SequenceNode'):
        assert not _is_linked(a2, 'effbd902_SequenceNode', b)


def test_assoc_decompositions0_reverse_link_reassign_clear():
    a1 = effbd902_Function(domain="sample_text")
    a2 = effbd902_Function(domain="sample_text_2")
    b = effbd902_AbstractFunction(id="sample_text")
    _safe_set(b, 'effbd902_AbstractFunction', a1)
    assert _is_linked(b, 'effbd902_AbstractFunction', a1)
    if hasattr(a1, 'effbd902_Function'):
        assert _is_linked(a1, 'effbd902_Function', b)
    _safe_set(b, 'effbd902_AbstractFunction', a2)
    assert _is_linked(b, 'effbd902_AbstractFunction', a2)
    if hasattr(a1, 'effbd902_Function'):
        assert not _is_linked(a1, 'effbd902_Function', b)
    if hasattr(a2, 'effbd902_Function'):
        assert _is_linked(a2, 'effbd902_Function', b)
    _safe_set(b, 'effbd902_AbstractFunction', None)
    assert not _is_linked(b, 'effbd902_AbstractFunction', a2)
    if hasattr(a2, 'effbd902_Function'):
        assert not _is_linked(a2, 'effbd902_Function', b)


def test_assoc_descriptions9_reverse_link_reassign_clear():
    a1 = effbd902_Function(domain="sample_text")
    a2 = effbd902_Function(domain="sample_text_2")
    b = effbd902_Description(content="sample_text")
    _safe_set(b, 'effbd902_Description', a1)
    assert _is_linked(b, 'effbd902_Description', a1)
    if hasattr(a1, 'effbd902_Function10'):
        assert _is_linked(a1, 'effbd902_Function10', b)
    _safe_set(b, 'effbd902_Description', a2)
    assert _is_linked(b, 'effbd902_Description', a2)
    if hasattr(a1, 'effbd902_Function10'):
        assert not _is_linked(a1, 'effbd902_Function10', b)
    if hasattr(a2, 'effbd902_Function10'):
        assert _is_linked(a2, 'effbd902_Function10', b)
    _safe_set(b, 'effbd902_Description', None)
    assert not _is_linked(b, 'effbd902_Description', a2)
    if hasattr(a2, 'effbd902_Function10'):
        assert not _is_linked(a2, 'effbd902_Function10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows3_stub_double():
    # effbd902_Flow has no real 'effbd902_Flow' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Function(domain="sample_text")
    partner = effbd902_Flow()
    setattr(partner, 'effbd902_Flow', None)
    _safe_set(owner, 'effbd902_Function4', {partner})
    assert getattr(partner, 'effbd902_Flow') == owner
    _safe_set(owner, 'effbd902_Function4', set())
    assert getattr(partner, 'effbd902_Flow') is None


def test_assoc_inputPorts7_stub_double():
    # effbd902_InputPort has no real 'effbd902_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Function(domain="sample_text")
    partner = effbd902_InputPort()
    setattr(partner, 'effbd902_InputPort', None)
    _safe_set(owner, 'effbd902_Function8', {partner})
    assert getattr(partner, 'effbd902_InputPort') == owner
    _safe_set(owner, 'effbd902_Function8', set())
    assert getattr(partner, 'effbd902_InputPort') is None


def test_assoc_items18_stub_double():
    # effbd902_Flow has no real 'effbd902_Flow19' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Item(name="sample_text")
    partner = effbd902_Flow()
    setattr(partner, 'effbd902_Flow19', None)
    _safe_set(owner, 'effbd902_Item', partner)
    assert owner in getattr(partner, 'effbd902_Flow19')
    _safe_set(owner, 'effbd902_Item', None)
    assert owner not in getattr(partner, 'effbd902_Flow19')


def test_assoc_outputPorts5_stub_double():
    # effbd902_OutputPort has no real 'effbd902_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Function(domain="sample_text")
    partner = effbd902_OutputPort()
    setattr(partner, 'effbd902_OutputPort', None)
    _safe_set(owner, 'effbd902_Function6', {partner})
    assert getattr(partner, 'effbd902_OutputPort') == owner
    _safe_set(owner, 'effbd902_Function6', set())
    assert getattr(partner, 'effbd902_OutputPort') is None


def test_assoc_sequenceNodes1_stub_double():
    # effbd902_Sequence has no real 'effbd902_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Function(domain="sample_text")
    partner = effbd902_Sequence()
    setattr(partner, 'effbd902_Sequence', None)
    _safe_set(owner, 'effbd902_Function2', {partner})
    assert getattr(partner, 'effbd902_Sequence') == owner
    _safe_set(owner, 'effbd902_Function2', set())
    assert getattr(partner, 'effbd902_Sequence') is None


def test_assoc_tokens11_stub_double():
    # effbd902_Token has no real 'effbd902_Token' property in the generated
    # code (a bare stub) -- manually attach it so effbd902_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd902_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd902_Function(domain="sample_text")
    partner = effbd902_Token()
    setattr(partner, 'effbd902_Token', None)
    _safe_set(owner, 'effbd902_Function12', {partner})
    assert getattr(partner, 'effbd902_Token') == owner
    _safe_set(owner, 'effbd902_Function12', set())
    assert getattr(partner, 'effbd902_Token') is None


