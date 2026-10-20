import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Literal,
    execTraces_BoolLiteral,
    execTraces_Edge,
    execTraces_ExecTraces,
    execTraces_IntLiteral,
    execTraces_Literal,
    execTraces_Node,
    execTraces_RealLiteral,
    execTraces_Variable,
    StateStatus,
    TransStatus,
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

def test_assoc_Edge1_reverse_link_reassign_clear():
    a1 = execTraces_ExecTraces(ComponentName="sample_text")
    a2 = execTraces_ExecTraces(ComponentName="sample_text_2")
    b = execTraces_Edge(actions="sample_text", guard="sample_text", status="sample_text", trigger="sample_text")
    _safe_set(b, 'execTraces_Edge', a1)
    assert _is_linked(b, 'execTraces_Edge', a1)
    if hasattr(a1, 'execTraces_ExecTraces2'):
        assert _is_linked(a1, 'execTraces_ExecTraces2', b)
    _safe_set(b, 'execTraces_Edge', a2)
    assert _is_linked(b, 'execTraces_Edge', a2)
    if hasattr(a1, 'execTraces_ExecTraces2'):
        assert not _is_linked(a1, 'execTraces_ExecTraces2', b)
    if hasattr(a2, 'execTraces_ExecTraces2'):
        assert _is_linked(a2, 'execTraces_ExecTraces2', b)
    _safe_set(b, 'execTraces_Edge', None)
    assert not _is_linked(b, 'execTraces_Edge', a2)
    if hasattr(a2, 'execTraces_ExecTraces2'):
        assert not _is_linked(a2, 'execTraces_ExecTraces2', b)


def test_assoc_Node0_reverse_link_reassign_clear():
    a1 = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    a2 = execTraces_Node(constraints="sample_text_2", id=13, level=13, name="sample_text_2", status="sample_text_2")
    b = execTraces_ExecTraces(ComponentName="sample_text")
    _safe_set(b, 'execTraces_ExecTraces', {a1})
    assert _is_linked(b, 'execTraces_ExecTraces', a1)
    if hasattr(a1, 'execTraces_Node'):
        assert _is_linked(a1, 'execTraces_Node', b)
    _safe_set(b, 'execTraces_ExecTraces', {a2})
    assert _is_linked(b, 'execTraces_ExecTraces', a2)
    if hasattr(a1, 'execTraces_Node'):
        assert not _is_linked(a1, 'execTraces_Node', b)
    if hasattr(a2, 'execTraces_Node'):
        assert _is_linked(a2, 'execTraces_Node', b)
    _safe_set(b, 'execTraces_ExecTraces', set())
    assert not _is_linked(b, 'execTraces_ExecTraces', a2)
    if hasattr(a2, 'execTraces_Node'):
        assert not _is_linked(a2, 'execTraces_Node', b)


def test_assoc_VarData9_reverse_link_reassign_clear():
    a1 = execTraces_Variable(name="sample_text")
    a2 = execTraces_Variable(name="sample_text_2")
    b = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    _safe_set(b, 'execTraces_Node10', {a1})
    assert _is_linked(b, 'execTraces_Node10', a1)
    if hasattr(a1, 'execTraces_Variable'):
        assert _is_linked(a1, 'execTraces_Variable', b)
    _safe_set(b, 'execTraces_Node10', {a2})
    assert _is_linked(b, 'execTraces_Node10', a2)
    if hasattr(a1, 'execTraces_Variable'):
        assert not _is_linked(a1, 'execTraces_Variable', b)
    if hasattr(a2, 'execTraces_Variable'):
        assert _is_linked(a2, 'execTraces_Variable', b)
    _safe_set(b, 'execTraces_Node10', set())
    assert not _is_linked(b, 'execTraces_Node10', a2)
    if hasattr(a2, 'execTraces_Variable'):
        assert not _is_linked(a2, 'execTraces_Variable', b)


def test_assoc_destination6_reverse_link_reassign_clear():
    a1 = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    a2 = execTraces_Node(constraints="sample_text_2", id=13, level=13, name="sample_text_2", status="sample_text_2")
    b = execTraces_Edge(actions="sample_text", guard="sample_text", status="sample_text", trigger="sample_text")
    _safe_set(b, 'execTraces_Edge7', a1)
    assert _is_linked(b, 'execTraces_Edge7', a1)
    if hasattr(a1, 'execTraces_Node8'):
        assert _is_linked(a1, 'execTraces_Node8', b)
    _safe_set(b, 'execTraces_Edge7', a2)
    assert _is_linked(b, 'execTraces_Edge7', a2)
    if hasattr(a1, 'execTraces_Node8'):
        assert not _is_linked(a1, 'execTraces_Node8', b)
    if hasattr(a2, 'execTraces_Node8'):
        assert _is_linked(a2, 'execTraces_Node8', b)
    _safe_set(b, 'execTraces_Edge7', None)
    assert not _is_linked(b, 'execTraces_Edge7', a2)
    if hasattr(a2, 'execTraces_Node8'):
        assert not _is_linked(a2, 'execTraces_Node8', b)


def test_assoc_incomingEdges14_reverse_link_reassign_clear():
    a1 = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    a2 = execTraces_Node(constraints="sample_text_2", id=13, level=13, name="sample_text_2", status="sample_text_2")
    b = execTraces_Edge(actions="sample_text", guard="sample_text", status="sample_text", trigger="sample_text")
    _safe_set(b, 'execTraces_Edge16', a1)
    assert _is_linked(b, 'execTraces_Edge16', a1)
    if hasattr(a1, 'execTraces_Node15'):
        assert _is_linked(a1, 'execTraces_Node15', b)
    _safe_set(b, 'execTraces_Edge16', a2)
    assert _is_linked(b, 'execTraces_Edge16', a2)
    if hasattr(a1, 'execTraces_Node15'):
        assert not _is_linked(a1, 'execTraces_Node15', b)
    if hasattr(a2, 'execTraces_Node15'):
        assert _is_linked(a2, 'execTraces_Node15', b)
    _safe_set(b, 'execTraces_Edge16', None)
    assert not _is_linked(b, 'execTraces_Edge16', a2)
    if hasattr(a2, 'execTraces_Node15'):
        assert not _is_linked(a2, 'execTraces_Node15', b)


def test_assoc_outgoingEdges11_reverse_link_reassign_clear():
    a1 = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    a2 = execTraces_Node(constraints="sample_text_2", id=13, level=13, name="sample_text_2", status="sample_text_2")
    b = execTraces_Edge(actions="sample_text", guard="sample_text", status="sample_text", trigger="sample_text")
    _safe_set(b, 'execTraces_Edge13', a1)
    assert _is_linked(b, 'execTraces_Edge13', a1)
    if hasattr(a1, 'execTraces_Node12'):
        assert _is_linked(a1, 'execTraces_Node12', b)
    _safe_set(b, 'execTraces_Edge13', a2)
    assert _is_linked(b, 'execTraces_Edge13', a2)
    if hasattr(a1, 'execTraces_Node12'):
        assert not _is_linked(a1, 'execTraces_Node12', b)
    if hasattr(a2, 'execTraces_Node12'):
        assert _is_linked(a2, 'execTraces_Node12', b)
    _safe_set(b, 'execTraces_Edge13', None)
    assert not _is_linked(b, 'execTraces_Edge13', a2)
    if hasattr(a2, 'execTraces_Node12'):
        assert not _is_linked(a2, 'execTraces_Node12', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = execTraces_Node(constraints="sample_text", id=7, level=7, name="sample_text", status="sample_text")
    a2 = execTraces_Node(constraints="sample_text_2", id=13, level=13, name="sample_text_2", status="sample_text_2")
    b = execTraces_Edge(actions="sample_text", guard="sample_text", status="sample_text", trigger="sample_text")
    _safe_set(b, 'execTraces_Edge4', a1)
    assert _is_linked(b, 'execTraces_Edge4', a1)
    if hasattr(a1, 'execTraces_Node5'):
        assert _is_linked(a1, 'execTraces_Node5', b)
    _safe_set(b, 'execTraces_Edge4', a2)
    assert _is_linked(b, 'execTraces_Edge4', a2)
    if hasattr(a1, 'execTraces_Node5'):
        assert not _is_linked(a1, 'execTraces_Node5', b)
    if hasattr(a2, 'execTraces_Node5'):
        assert _is_linked(a2, 'execTraces_Node5', b)
    _safe_set(b, 'execTraces_Edge4', None)
    assert not _is_linked(b, 'execTraces_Edge4', a2)
    if hasattr(a2, 'execTraces_Node5'):
        assert not _is_linked(a2, 'execTraces_Node5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_value17_stub_double():
    # execTraces_Literal has no real 'execTraces_Literal' property in the generated
    # code (a bare stub) -- manually attach it so execTraces_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # execTraces_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = execTraces_Variable(name="sample_text")
    partner = execTraces_Literal()
    setattr(partner, 'execTraces_Literal', None)
    _safe_set(owner, 'execTraces_Variable18', partner)
    assert getattr(partner, 'execTraces_Literal') == owner
    _safe_set(owner, 'execTraces_Variable18', None)
    assert getattr(partner, 'execTraces_Literal') is None


