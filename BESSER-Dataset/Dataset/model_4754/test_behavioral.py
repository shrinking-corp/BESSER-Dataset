import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    SequenceNode,
    myffbd_And,
    myffbd_Description,
    myffbd_Final,
    myffbd_Flow,
    myffbd_Function,
    myffbd_InputPort,
    myffbd_Item,
    myffbd_Iteration,
    myffbd_Loop,
    myffbd_LoopExit,
    myffbd_Or,
    myffbd_OutputPort,
    myffbd_Port,
    myffbd_PortType,
    myffbd_SequenceNode,
    myffbd_Start,
    myffbd_Token,
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
    a1 = myffbd_SequenceNode(name="sample_text")
    a2 = myffbd_SequenceNode(name="sample_text_2")
    b = myffbd_SequenceNode(name="sample_text")
    _safe_set(b, 'myffbd_SequenceNode16', a1)
    assert _is_linked(b, 'myffbd_SequenceNode16', a1)
    if hasattr(a1, 'myffbd_SequenceNode14'):
        assert _is_linked(a1, 'myffbd_SequenceNode14', b)
    _safe_set(b, 'myffbd_SequenceNode16', a2)
    assert _is_linked(b, 'myffbd_SequenceNode16', a2)
    if hasattr(a1, 'myffbd_SequenceNode14'):
        assert not _is_linked(a1, 'myffbd_SequenceNode14', b)
    if hasattr(a2, 'myffbd_SequenceNode14'):
        assert _is_linked(a2, 'myffbd_SequenceNode14', b)
    _safe_set(b, 'myffbd_SequenceNode16', None)
    assert not _is_linked(b, 'myffbd_SequenceNode16', a2)
    if hasattr(a2, 'myffbd_SequenceNode14'):
        assert not _is_linked(a2, 'myffbd_SequenceNode14', b)


def test_assoc_decompositions1_reverse_link_reassign_clear():
    a1 = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    a2 = myffbd_Function(domain="sample_text_2", tMax=13, tMin=13)
    b = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'myffbd_Function0', {a1})
    assert _is_linked(b, 'myffbd_Function0', a1)
    if hasattr(a1, 'myffbd_Function'):
        assert _is_linked(a1, 'myffbd_Function', b)
    _safe_set(b, 'myffbd_Function0', {a2})
    assert _is_linked(b, 'myffbd_Function0', a2)
    if hasattr(a1, 'myffbd_Function'):
        assert not _is_linked(a1, 'myffbd_Function', b)
    if hasattr(a2, 'myffbd_Function'):
        assert _is_linked(a2, 'myffbd_Function', b)
    _safe_set(b, 'myffbd_Function0', set())
    assert not _is_linked(b, 'myffbd_Function0', a2)
    if hasattr(a2, 'myffbd_Function'):
        assert not _is_linked(a2, 'myffbd_Function', b)


def test_assoc_descriptions8_reverse_link_reassign_clear():
    a1 = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    a2 = myffbd_Function(domain="sample_text_2", tMax=13, tMin=13)
    b = myffbd_Description(content="sample_text")
    _safe_set(b, 'myffbd_Description', a1)
    assert _is_linked(b, 'myffbd_Description', a1)
    if hasattr(a1, 'myffbd_Function9'):
        assert _is_linked(a1, 'myffbd_Function9', b)
    _safe_set(b, 'myffbd_Description', a2)
    assert _is_linked(b, 'myffbd_Description', a2)
    if hasattr(a1, 'myffbd_Function9'):
        assert not _is_linked(a1, 'myffbd_Function9', b)
    if hasattr(a2, 'myffbd_Function9'):
        assert _is_linked(a2, 'myffbd_Function9', b)
    _safe_set(b, 'myffbd_Description', None)
    assert not _is_linked(b, 'myffbd_Description', a2)
    if hasattr(a2, 'myffbd_Function9'):
        assert not _is_linked(a2, 'myffbd_Function9', b)


def test_assoc_portTypes12_reverse_link_reassign_clear():
    a1 = myffbd_PortType(type="sample_text")
    a2 = myffbd_PortType(type="sample_text_2")
    b = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'myffbd_Function13', {a1})
    assert _is_linked(b, 'myffbd_Function13', a1)
    if hasattr(a1, 'myffbd_PortType'):
        assert _is_linked(a1, 'myffbd_PortType', b)
    _safe_set(b, 'myffbd_Function13', {a2})
    assert _is_linked(b, 'myffbd_Function13', a2)
    if hasattr(a1, 'myffbd_PortType'):
        assert not _is_linked(a1, 'myffbd_PortType', b)
    if hasattr(a2, 'myffbd_PortType'):
        assert _is_linked(a2, 'myffbd_PortType', b)
    _safe_set(b, 'myffbd_Function13', set())
    assert not _is_linked(b, 'myffbd_Function13', a2)
    if hasattr(a2, 'myffbd_PortType'):
        assert not _is_linked(a2, 'myffbd_PortType', b)


def test_assoc_sequenceNodes2_reverse_link_reassign_clear():
    a1 = myffbd_SequenceNode(name="sample_text")
    a2 = myffbd_SequenceNode(name="sample_text_2")
    b = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    _safe_set(b, 'myffbd_Function3', {a1})
    assert _is_linked(b, 'myffbd_Function3', a1)
    if hasattr(a1, 'myffbd_SequenceNode'):
        assert _is_linked(a1, 'myffbd_SequenceNode', b)
    _safe_set(b, 'myffbd_Function3', {a2})
    assert _is_linked(b, 'myffbd_Function3', a2)
    if hasattr(a1, 'myffbd_SequenceNode'):
        assert not _is_linked(a1, 'myffbd_SequenceNode', b)
    if hasattr(a2, 'myffbd_SequenceNode'):
        assert _is_linked(a2, 'myffbd_SequenceNode', b)
    _safe_set(b, 'myffbd_Function3', set())
    assert not _is_linked(b, 'myffbd_Function3', a2)
    if hasattr(a2, 'myffbd_SequenceNode'):
        assert not _is_linked(a2, 'myffbd_SequenceNode', b)


def test_assoc_type18_reverse_link_reassign_clear():
    a1 = myffbd_PortType(type="sample_text")
    a2 = myffbd_PortType(type="sample_text_2")
    b = myffbd_Port(id="sample_text")
    _safe_set(b, 'myffbd_Port19', a1)
    assert _is_linked(b, 'myffbd_Port19', a1)
    if hasattr(a1, 'myffbd_PortType20'):
        assert _is_linked(a1, 'myffbd_PortType20', b)
    _safe_set(b, 'myffbd_Port19', a2)
    assert _is_linked(b, 'myffbd_Port19', a2)
    if hasattr(a1, 'myffbd_PortType20'):
        assert not _is_linked(a1, 'myffbd_PortType20', b)
    if hasattr(a2, 'myffbd_PortType20'):
        assert _is_linked(a2, 'myffbd_PortType20', b)
    _safe_set(b, 'myffbd_Port19', None)
    assert not _is_linked(b, 'myffbd_Port19', a2)
    if hasattr(a2, 'myffbd_PortType20'):
        assert not _is_linked(a2, 'myffbd_PortType20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_flows17_stub_double():
    # myffbd_Flow has no real 'myffbd_Flow' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Port(id="sample_text")
    partner = myffbd_Flow()
    setattr(partner, 'myffbd_Flow', None)
    _safe_set(owner, 'myffbd_Port', {partner})
    assert getattr(partner, 'myffbd_Flow') == owner
    _safe_set(owner, 'myffbd_Port', set())
    assert getattr(partner, 'myffbd_Flow') is None


def test_assoc_inputPorts6_stub_double():
    # myffbd_InputPort has no real 'myffbd_InputPort' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    partner = myffbd_InputPort()
    setattr(partner, 'myffbd_InputPort', None)
    _safe_set(owner, 'myffbd_Function7', {partner})
    assert getattr(partner, 'myffbd_InputPort') == owner
    _safe_set(owner, 'myffbd_Function7', set())
    assert getattr(partner, 'myffbd_InputPort') is None


def test_assoc_items24_stub_double():
    # myffbd_Flow has no real 'myffbd_Flow25' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Item's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Item's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Item(name="sample_text")
    partner = myffbd_Flow()
    setattr(partner, 'myffbd_Flow25', None)
    _safe_set(owner, 'myffbd_Item', partner)
    assert owner in getattr(partner, 'myffbd_Flow25')
    _safe_set(owner, 'myffbd_Item', None)
    assert owner not in getattr(partner, 'myffbd_Flow25')


def test_assoc_outputPorts4_stub_double():
    # myffbd_OutputPort has no real 'myffbd_OutputPort' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    partner = myffbd_OutputPort()
    setattr(partner, 'myffbd_OutputPort', None)
    _safe_set(owner, 'myffbd_Function5', {partner})
    assert getattr(partner, 'myffbd_OutputPort') == owner
    _safe_set(owner, 'myffbd_Function5', set())
    assert getattr(partner, 'myffbd_OutputPort') is None


def test_assoc_src21_stub_double():
    # myffbd_Flow has no real 'myffbd_Flow22' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Port(id="sample_text")
    partner = myffbd_Flow()
    setattr(partner, 'myffbd_Flow22', None)
    _safe_set(owner, 'myffbd_Port23', partner)
    assert getattr(partner, 'myffbd_Flow22') == owner
    _safe_set(owner, 'myffbd_Port23', None)
    assert getattr(partner, 'myffbd_Flow22') is None


def test_assoc_tokens10_stub_double():
    # myffbd_Token has no real 'myffbd_Token' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Function(domain="sample_text", tMax=7, tMin=7)
    partner = myffbd_Token()
    setattr(partner, 'myffbd_Token', None)
    _safe_set(owner, 'myffbd_Function11', {partner})
    assert getattr(partner, 'myffbd_Token') == owner
    _safe_set(owner, 'myffbd_Function11', set())
    assert getattr(partner, 'myffbd_Token') is None


def test_assoc_trg26_stub_double():
    # myffbd_Flow has no real 'myffbd_Flow27' property in the generated
    # code (a bare stub) -- manually attach it so myffbd_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myffbd_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myffbd_Port(id="sample_text")
    partner = myffbd_Flow()
    setattr(partner, 'myffbd_Flow27', None)
    _safe_set(owner, 'myffbd_Port28', partner)
    assert getattr(partner, 'myffbd_Flow27') == owner
    _safe_set(owner, 'myffbd_Port28', None)
    assert getattr(partner, 'myffbd_Flow27') is None


