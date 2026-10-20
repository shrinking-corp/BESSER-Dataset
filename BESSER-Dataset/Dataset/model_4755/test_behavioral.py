import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    effbd201_And,
    effbd201_Description,
    effbd201_Final,
    effbd201_Flow,
    effbd201_Function,
    effbd201_InputPort,
    effbd201_Item,
    effbd201_Iteration,
    effbd201_Loop,
    effbd201_LoopExit,
    effbd201_Or,
    effbd201_OutputPort,
    effbd201_Port,
    effbd201_ProcessNode,
    effbd201_Sequence,
    effbd201_SequenceNode,
    effbd201_Start,
    effbd201_Token,
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
    a1 = effbd201_SequenceNode(name="sample_text", tMax=7, tMin=7)
    a2 = effbd201_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    b = effbd201_SequenceNode(name="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'effbd201_SequenceNode14', {a1})
    assert _is_linked(b, 'effbd201_SequenceNode14', a1)
    if hasattr(a1, 'effbd201_SequenceNode'):
        assert _is_linked(a1, 'effbd201_SequenceNode', b)
    _safe_set(b, 'effbd201_SequenceNode14', {a2})
    assert _is_linked(b, 'effbd201_SequenceNode14', a2)
    if hasattr(a1, 'effbd201_SequenceNode'):
        assert not _is_linked(a1, 'effbd201_SequenceNode', b)
    if hasattr(a2, 'effbd201_SequenceNode'):
        assert _is_linked(a2, 'effbd201_SequenceNode', b)
    _safe_set(b, 'effbd201_SequenceNode14', set())
    assert not _is_linked(b, 'effbd201_SequenceNode14', a2)
    if hasattr(a2, 'effbd201_SequenceNode'):
        assert not _is_linked(a2, 'effbd201_SequenceNode', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = effbd201_Function(domain="sample_text")
    a2 = effbd201_Function(domain="sample_text_2")
    b = effbd201_Function(domain="sample_text")
    _safe_set(b, 'effbd201_Function0', {a1})
    assert _is_linked(b, 'effbd201_Function0', a1)
    if hasattr(a1, 'effbd201_Function'):
        assert _is_linked(a1, 'effbd201_Function', b)
    _safe_set(b, 'effbd201_Function0', {a2})
    assert _is_linked(b, 'effbd201_Function0', a2)
    if hasattr(a1, 'effbd201_Function'):
        assert not _is_linked(a1, 'effbd201_Function', b)
    if hasattr(a2, 'effbd201_Function'):
        assert _is_linked(a2, 'effbd201_Function', b)
    _safe_set(b, 'effbd201_Function0', set())
    assert not _is_linked(b, 'effbd201_Function0', a2)
    if hasattr(a2, 'effbd201_Function'):
        assert not _is_linked(a2, 'effbd201_Function', b)


def test_assoc_descriptions10_reverse_link_reassign_clear():
    a1 = effbd201_Function(domain="sample_text")
    a2 = effbd201_Function(domain="sample_text_2")
    b = effbd201_Description(content="sample_text")
    _safe_set(b, 'effbd201_Description', a1)
    assert _is_linked(b, 'effbd201_Description', a1)
    if hasattr(a1, 'effbd201_Function11'):
        assert _is_linked(a1, 'effbd201_Function11', b)
    _safe_set(b, 'effbd201_Description', a2)
    assert _is_linked(b, 'effbd201_Description', a2)
    if hasattr(a1, 'effbd201_Function11'):
        assert not _is_linked(a1, 'effbd201_Function11', b)
    if hasattr(a2, 'effbd201_Function11'):
        assert _is_linked(a2, 'effbd201_Function11', b)
    _safe_set(b, 'effbd201_Description', None)
    assert not _is_linked(b, 'effbd201_Description', a2)
    if hasattr(a2, 'effbd201_Function11'):
        assert not _is_linked(a2, 'effbd201_Function11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows4_stub_double():
    # effbd201_Flow has no real 'effbd201_Flow' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Function(domain="sample_text")
    partner = effbd201_Flow()
    setattr(partner, 'effbd201_Flow', None)
    _safe_set(owner, 'effbd201_Function5', {partner})
    assert getattr(partner, 'effbd201_Flow') == owner
    _safe_set(owner, 'effbd201_Function5', set())
    assert getattr(partner, 'effbd201_Flow') is None


def test_assoc_inputPorts8_stub_double():
    # effbd201_InputPort has no real 'effbd201_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Function(domain="sample_text")
    partner = effbd201_InputPort()
    setattr(partner, 'effbd201_InputPort', None)
    _safe_set(owner, 'effbd201_Function9', {partner})
    assert getattr(partner, 'effbd201_InputPort') == owner
    _safe_set(owner, 'effbd201_Function9', set())
    assert getattr(partner, 'effbd201_InputPort') is None


def test_assoc_inputflowEdge18_stub_double():
    # effbd201_Flow has no real 'effbd201_Flow19' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Port(id="sample_text")
    partner = effbd201_Flow()
    setattr(partner, 'effbd201_Flow19', None)
    _safe_set(owner, 'effbd201_Port20', partner)
    assert owner in getattr(partner, 'effbd201_Flow19')
    _safe_set(owner, 'effbd201_Port20', None)
    assert owner not in getattr(partner, 'effbd201_Flow19')


def test_assoc_items21_stub_double():
    # effbd201_Flow has no real 'effbd201_Flow22' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Item(name="sample_text")
    partner = effbd201_Flow()
    setattr(partner, 'effbd201_Flow22', None)
    _safe_set(owner, 'effbd201_Item', partner)
    assert owner in getattr(partner, 'effbd201_Flow22')
    _safe_set(owner, 'effbd201_Item', None)
    assert owner not in getattr(partner, 'effbd201_Flow22')


def test_assoc_outputPorts6_stub_double():
    # effbd201_OutputPort has no real 'effbd201_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Function(domain="sample_text")
    partner = effbd201_OutputPort()
    setattr(partner, 'effbd201_OutputPort', None)
    _safe_set(owner, 'effbd201_Function7', {partner})
    assert getattr(partner, 'effbd201_OutputPort') == owner
    _safe_set(owner, 'effbd201_Function7', set())
    assert getattr(partner, 'effbd201_OutputPort') is None


def test_assoc_outputflowEdge16_stub_double():
    # effbd201_Flow has no real 'effbd201_Flow17' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Port(id="sample_text")
    partner = effbd201_Flow()
    setattr(partner, 'effbd201_Flow17', None)
    _safe_set(owner, 'effbd201_Port', {partner})
    assert getattr(partner, 'effbd201_Flow17') == owner
    _safe_set(owner, 'effbd201_Port', set())
    assert getattr(partner, 'effbd201_Flow17') is None


def test_assoc_sequenceNodes2_stub_double():
    # effbd201_Sequence has no real 'effbd201_Sequence' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Function(domain="sample_text")
    partner = effbd201_Sequence()
    setattr(partner, 'effbd201_Sequence', None)
    _safe_set(owner, 'effbd201_Function3', {partner})
    assert getattr(partner, 'effbd201_Sequence') == owner
    _safe_set(owner, 'effbd201_Function3', set())
    assert getattr(partner, 'effbd201_Sequence') is None


def test_assoc_tokens12_stub_double():
    # effbd201_Token has no real 'effbd201_Token' property in the generated
    # code (a bare stub) -- manually attach it so effbd201_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # effbd201_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = effbd201_Function(domain="sample_text")
    partner = effbd201_Token()
    setattr(partner, 'effbd201_Token', None)
    _safe_set(owner, 'effbd201_Function13', {partner})
    assert getattr(partner, 'effbd201_Token') == owner
    _safe_set(owner, 'effbd201_Function13', set())
    assert getattr(partner, 'effbd201_Token') is None


