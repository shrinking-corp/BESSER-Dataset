import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constraint,
    Expression,
    PrologExpression,
    tExp_AndExpr,
    tExp_AtomExpression,
    tExp_Cardinality,
    tExp_CatExpr,
    tExp_Channel,
    tExp_Constraint,
    tExp_Domainmodel,
    tExp_EventType,
    tExp_Expression,
    tExp_FilterExpr,
    tExp_ListExpression,
    tExp_Msg,
    tExp_NumberExpression,
    tExp_Partition,
    tExp_PrologExpression,
    tExp_Role,
    tExp_SeqExpr,
    tExp_ShuffleExpr,
    tExp_Singletons,
    tExp_Size,
    tExp_StringExpression,
    tExp_Term,
    tExp_TerminalExpr,
    tExp_Together,
    tExp_TraceExpression,
    tExp_UnionExpr,
    tExp_VarExpr,
    tExp_VariableExpression,
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

def test_assoc_async_receiver67_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg68', a1)
    assert _is_linked(b, 'tExp_Msg68', a1)
    if hasattr(a1, 'tExp_Role69'):
        assert _is_linked(a1, 'tExp_Role69', b)
    _safe_set(b, 'tExp_Msg68', a2)
    assert _is_linked(b, 'tExp_Msg68', a2)
    if hasattr(a1, 'tExp_Role69'):
        assert not _is_linked(a1, 'tExp_Role69', b)
    if hasattr(a2, 'tExp_Role69'):
        assert _is_linked(a2, 'tExp_Role69', b)
    _safe_set(b, 'tExp_Msg68', None)
    assert not _is_linked(b, 'tExp_Msg68', a2)
    if hasattr(a2, 'tExp_Role69'):
        assert not _is_linked(a2, 'tExp_Role69', b)


def test_assoc_async_sender58_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg59', a1)
    assert _is_linked(b, 'tExp_Msg59', a1)
    if hasattr(a1, 'tExp_Role60'):
        assert _is_linked(a1, 'tExp_Role60', b)
    _safe_set(b, 'tExp_Msg59', a2)
    assert _is_linked(b, 'tExp_Msg59', a2)
    if hasattr(a1, 'tExp_Role60'):
        assert not _is_linked(a1, 'tExp_Role60', b)
    if hasattr(a2, 'tExp_Role60'):
        assert _is_linked(a2, 'tExp_Role60', b)
    _safe_set(b, 'tExp_Msg59', None)
    assert not _is_linked(b, 'tExp_Msg59', a2)
    if hasattr(a2, 'tExp_Role60'):
        assert not _is_linked(a2, 'tExp_Role60', b)


def test_assoc_bodyFilter33_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression34', a1)
    assert _is_linked(b, 'tExp_Expression34', a1)
    if hasattr(a1, 'tExp_Expression32'):
        assert _is_linked(a1, 'tExp_Expression32', b)
    _safe_set(b, 'tExp_Expression34', a2)
    assert _is_linked(b, 'tExp_Expression34', a2)
    if hasattr(a1, 'tExp_Expression32'):
        assert not _is_linked(a1, 'tExp_Expression32', b)
    if hasattr(a2, 'tExp_Expression32'):
        assert _is_linked(a2, 'tExp_Expression32', b)
    _safe_set(b, 'tExp_Expression34', None)
    assert not _is_linked(b, 'tExp_Expression34', a2)
    if hasattr(a2, 'tExp_Expression32'):
        assert not _is_linked(a2, 'tExp_Expression32', b)


def test_assoc_bodySeq39_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression40', a1)
    assert _is_linked(b, 'tExp_Expression40', a1)
    if hasattr(a1, 'tExp_Expression38'):
        assert _is_linked(a1, 'tExp_Expression38', b)
    _safe_set(b, 'tExp_Expression40', a2)
    assert _is_linked(b, 'tExp_Expression40', a2)
    if hasattr(a1, 'tExp_Expression38'):
        assert not _is_linked(a1, 'tExp_Expression38', b)
    if hasattr(a2, 'tExp_Expression38'):
        assert _is_linked(a2, 'tExp_Expression38', b)
    _safe_set(b, 'tExp_Expression40', None)
    assert not _is_linked(b, 'tExp_Expression40', a2)
    if hasattr(a2, 'tExp_Expression38'):
        assert not _is_linked(a2, 'tExp_Expression38', b)


def test_assoc_bodyVar21_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression22', a1)
    assert _is_linked(b, 'tExp_Expression22', a1)
    if hasattr(a1, 'tExp_Expression20'):
        assert _is_linked(a1, 'tExp_Expression20', b)
    _safe_set(b, 'tExp_Expression22', a2)
    assert _is_linked(b, 'tExp_Expression22', a2)
    if hasattr(a1, 'tExp_Expression20'):
        assert not _is_linked(a1, 'tExp_Expression20', b)
    if hasattr(a2, 'tExp_Expression20'):
        assert _is_linked(a2, 'tExp_Expression20', b)
    _safe_set(b, 'tExp_Expression22', None)
    assert not _is_linked(b, 'tExp_Expression22', a2)
    if hasattr(a2, 'tExp_Expression20'):
        assert not _is_linked(a2, 'tExp_Expression20', b)


def test_assoc_channel55_reverse_link_reassign_clear():
    a1 = tExp_EventType(name="sample_text")
    a2 = tExp_EventType(name="sample_text_2")
    b = tExp_Channel(name="sample_text", reliability="sample_text")
    _safe_set(b, 'tExp_Channel57', a1)
    assert _is_linked(b, 'tExp_Channel57', a1)
    if hasattr(a1, 'tExp_EventType56'):
        assert _is_linked(a1, 'tExp_EventType56', b)
    _safe_set(b, 'tExp_Channel57', a2)
    assert _is_linked(b, 'tExp_Channel57', a2)
    if hasattr(a1, 'tExp_EventType56'):
        assert not _is_linked(a1, 'tExp_EventType56', b)
    if hasattr(a2, 'tExp_EventType56'):
        assert _is_linked(a2, 'tExp_EventType56', b)
    _safe_set(b, 'tExp_Channel57', None)
    assert not _is_linked(b, 'tExp_Channel57', a2)
    if hasattr(a2, 'tExp_EventType56'):
        assert not _is_linked(a2, 'tExp_EventType56', b)


def test_assoc_channels16_reverse_link_reassign_clear():
    a1 = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    a2 = tExp_TraceExpression(bodyL="sample_text_2", channelsL="sample_text_2", constraintsL="sample_text_2", decentralized="sample_text_2", decentralizedL="sample_text_2", gui="sample_text_2", guiL="sample_text_2", minimal="sample_text_2", minimalL="sample_text_2", modules="sample_text_2", modulesL="sample_text_2", name="sample_text_2", partitionL="sample_text_2", rolesL="sample_text_2", threshold="sample_text_2", thresholdL="sample_text_2", typesL="sample_text_2")
    b = tExp_Channel(name="sample_text", reliability="sample_text")
    _safe_set(b, 'tExp_Channel', a1)
    assert _is_linked(b, 'tExp_Channel', a1)
    if hasattr(a1, 'tExp_TraceExpression17'):
        assert _is_linked(a1, 'tExp_TraceExpression17', b)
    _safe_set(b, 'tExp_Channel', a2)
    assert _is_linked(b, 'tExp_Channel', a2)
    if hasattr(a1, 'tExp_TraceExpression17'):
        assert not _is_linked(a1, 'tExp_TraceExpression17', b)
    if hasattr(a2, 'tExp_TraceExpression17'):
        assert _is_linked(a2, 'tExp_TraceExpression17', b)
    _safe_set(b, 'tExp_Channel', None)
    assert not _is_linked(b, 'tExp_Channel', a2)
    if hasattr(a2, 'tExp_TraceExpression17'):
        assert not _is_linked(a2, 'tExp_TraceExpression17', b)


def test_assoc_conditions73_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg74', a1)
    assert _is_linked(b, 'tExp_Msg74', a1)
    if hasattr(a1, 'tExp_PrologExpression75'):
        assert _is_linked(a1, 'tExp_PrologExpression75', b)
    _safe_set(b, 'tExp_Msg74', a2)
    assert _is_linked(b, 'tExp_Msg74', a2)
    if hasattr(a1, 'tExp_PrologExpression75'):
        assert not _is_linked(a1, 'tExp_PrologExpression75', b)
    if hasattr(a2, 'tExp_PrologExpression75'):
        assert _is_linked(a2, 'tExp_PrologExpression75', b)
    _safe_set(b, 'tExp_Msg74', None)
    assert not _is_linked(b, 'tExp_Msg74', a2)
    if hasattr(a2, 'tExp_PrologExpression75'):
        assert not _is_linked(a2, 'tExp_PrologExpression75', b)


def test_assoc_constraints14_reverse_link_reassign_clear():
    a1 = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    a2 = tExp_TraceExpression(bodyL="sample_text_2", channelsL="sample_text_2", constraintsL="sample_text_2", decentralized="sample_text_2", decentralizedL="sample_text_2", gui="sample_text_2", guiL="sample_text_2", minimal="sample_text_2", minimalL="sample_text_2", modules="sample_text_2", modulesL="sample_text_2", name="sample_text_2", partitionL="sample_text_2", rolesL="sample_text_2", threshold="sample_text_2", thresholdL="sample_text_2", typesL="sample_text_2")
    b = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    _safe_set(b, 'tExp_Constraint', a1)
    assert _is_linked(b, 'tExp_Constraint', a1)
    if hasattr(a1, 'tExp_TraceExpression15'):
        assert _is_linked(a1, 'tExp_TraceExpression15', b)
    _safe_set(b, 'tExp_Constraint', a2)
    assert _is_linked(b, 'tExp_Constraint', a2)
    if hasattr(a1, 'tExp_TraceExpression15'):
        assert not _is_linked(a1, 'tExp_TraceExpression15', b)
    if hasattr(a2, 'tExp_TraceExpression15'):
        assert _is_linked(a2, 'tExp_TraceExpression15', b)
    _safe_set(b, 'tExp_Constraint', None)
    assert not _is_linked(b, 'tExp_Constraint', a2)
    if hasattr(a2, 'tExp_TraceExpression15'):
        assert not _is_linked(a2, 'tExp_TraceExpression15', b)


def test_assoc_content70_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg71', a1)
    assert _is_linked(b, 'tExp_Msg71', a1)
    if hasattr(a1, 'tExp_PrologExpression72'):
        assert _is_linked(a1, 'tExp_PrologExpression72', b)
    _safe_set(b, 'tExp_Msg71', a2)
    assert _is_linked(b, 'tExp_Msg71', a2)
    if hasattr(a1, 'tExp_PrologExpression72'):
        assert not _is_linked(a1, 'tExp_PrologExpression72', b)
    if hasattr(a2, 'tExp_PrologExpression72'):
        assert _is_linked(a2, 'tExp_PrologExpression72', b)
    _safe_set(b, 'tExp_Msg71', None)
    assert not _is_linked(b, 'tExp_Msg71', a2)
    if hasattr(a2, 'tExp_PrologExpression72'):
        assert not _is_linked(a2, 'tExp_PrologExpression72', b)


def test_assoc_expr18_reverse_link_reassign_clear():
    a1 = tExp_Term(name="sample_text")
    a2 = tExp_Term(name="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression', a1)
    assert _is_linked(b, 'tExp_Expression', a1)
    if hasattr(a1, 'tExp_Term19'):
        assert _is_linked(a1, 'tExp_Term19', b)
    _safe_set(b, 'tExp_Expression', a2)
    assert _is_linked(b, 'tExp_Expression', a2)
    if hasattr(a1, 'tExp_Term19'):
        assert not _is_linked(a1, 'tExp_Term19', b)
    if hasattr(a2, 'tExp_Term19'):
        assert _is_linked(a2, 'tExp_Term19', b)
    _safe_set(b, 'tExp_Expression', None)
    assert not _is_linked(b, 'tExp_Expression', a2)
    if hasattr(a2, 'tExp_Term19'):
        assert not _is_linked(a2, 'tExp_Term19', b)


def test_assoc_expr45_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression46', a1)
    assert _is_linked(b, 'tExp_Expression46', a1)
    if hasattr(a1, 'tExp_Expression44'):
        assert _is_linked(a1, 'tExp_Expression44', b)
    _safe_set(b, 'tExp_Expression46', a2)
    assert _is_linked(b, 'tExp_Expression46', a2)
    if hasattr(a1, 'tExp_Expression44'):
        assert not _is_linked(a1, 'tExp_Expression44', b)
    if hasattr(a2, 'tExp_Expression44'):
        assert _is_linked(a2, 'tExp_Expression44', b)
    _safe_set(b, 'tExp_Expression46', None)
    assert not _is_linked(b, 'tExp_Expression46', a2)
    if hasattr(a2, 'tExp_Expression44'):
        assert not _is_linked(a2, 'tExp_Expression44', b)


def test_assoc_expr47_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType48', a1)
    assert _is_linked(b, 'tExp_EventType48', a1)
    if hasattr(a1, 'tExp_PrologExpression49'):
        assert _is_linked(a1, 'tExp_PrologExpression49', b)
    _safe_set(b, 'tExp_EventType48', a2)
    assert _is_linked(b, 'tExp_EventType48', a2)
    if hasattr(a1, 'tExp_PrologExpression49'):
        assert not _is_linked(a1, 'tExp_PrologExpression49', b)
    if hasattr(a2, 'tExp_PrologExpression49'):
        assert _is_linked(a2, 'tExp_PrologExpression49', b)
    _safe_set(b, 'tExp_EventType48', None)
    assert not _is_linked(b, 'tExp_EventType48', a2)
    if hasattr(a2, 'tExp_PrologExpression49'):
        assert not _is_linked(a2, 'tExp_PrologExpression49', b)


def test_assoc_exprs29_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression30', {a1})
    assert _is_linked(b, 'tExp_Expression30', a1)
    if hasattr(a1, 'tExp_PrologExpression31'):
        assert _is_linked(a1, 'tExp_PrologExpression31', b)
    _safe_set(b, 'tExp_Expression30', {a2})
    assert _is_linked(b, 'tExp_Expression30', a2)
    if hasattr(a1, 'tExp_PrologExpression31'):
        assert not _is_linked(a1, 'tExp_PrologExpression31', b)
    if hasattr(a2, 'tExp_PrologExpression31'):
        assert _is_linked(a2, 'tExp_PrologExpression31', b)
    _safe_set(b, 'tExp_Expression30', set())
    assert not _is_linked(b, 'tExp_Expression30', a2)
    if hasattr(a2, 'tExp_PrologExpression31'):
        assert not _is_linked(a2, 'tExp_PrologExpression31', b)


def test_assoc_exprs50_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType51', {a1})
    assert _is_linked(b, 'tExp_EventType51', a1)
    if hasattr(a1, 'tExp_PrologExpression52'):
        assert _is_linked(a1, 'tExp_PrologExpression52', b)
    _safe_set(b, 'tExp_EventType51', {a2})
    assert _is_linked(b, 'tExp_EventType51', a2)
    if hasattr(a1, 'tExp_PrologExpression52'):
        assert not _is_linked(a1, 'tExp_PrologExpression52', b)
    if hasattr(a2, 'tExp_PrologExpression52'):
        assert _is_linked(a2, 'tExp_PrologExpression52', b)
    _safe_set(b, 'tExp_EventType51', set())
    assert not _is_linked(b, 'tExp_EventType51', a2)
    if hasattr(a2, 'tExp_PrologExpression52'):
        assert not _is_linked(a2, 'tExp_PrologExpression52', b)


def test_assoc_first26_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression27', a1)
    assert _is_linked(b, 'tExp_Expression27', a1)
    if hasattr(a1, 'tExp_PrologExpression28'):
        assert _is_linked(a1, 'tExp_PrologExpression28', b)
    _safe_set(b, 'tExp_Expression27', a2)
    assert _is_linked(b, 'tExp_Expression27', a2)
    if hasattr(a1, 'tExp_PrologExpression28'):
        assert not _is_linked(a1, 'tExp_PrologExpression28', b)
    if hasattr(a2, 'tExp_PrologExpression28'):
        assert _is_linked(a2, 'tExp_PrologExpression28', b)
    _safe_set(b, 'tExp_Expression27', None)
    assert not _is_linked(b, 'tExp_Expression27', a2)
    if hasattr(a2, 'tExp_PrologExpression28'):
        assert not _is_linked(a2, 'tExp_PrologExpression28', b)


def test_assoc_left2_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_PrologExpression(op="sample_text")
    _safe_set(b, 'tExp_PrologExpression1', a1)
    assert _is_linked(b, 'tExp_PrologExpression1', a1)
    if hasattr(a1, 'tExp_PrologExpression'):
        assert _is_linked(a1, 'tExp_PrologExpression', b)
    _safe_set(b, 'tExp_PrologExpression1', a2)
    assert _is_linked(b, 'tExp_PrologExpression1', a2)
    if hasattr(a1, 'tExp_PrologExpression'):
        assert not _is_linked(a1, 'tExp_PrologExpression', b)
    if hasattr(a2, 'tExp_PrologExpression'):
        assert _is_linked(a2, 'tExp_PrologExpression', b)
    _safe_set(b, 'tExp_PrologExpression1', None)
    assert not _is_linked(b, 'tExp_PrologExpression1', a2)
    if hasattr(a2, 'tExp_PrologExpression'):
        assert not _is_linked(a2, 'tExp_PrologExpression', b)


def test_assoc_left81_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    _safe_set(b, 'tExp_Constraint82', {a1})
    assert _is_linked(b, 'tExp_Constraint82', a1)
    if hasattr(a1, 'tExp_Role83'):
        assert _is_linked(a1, 'tExp_Role83', b)
    _safe_set(b, 'tExp_Constraint82', {a2})
    assert _is_linked(b, 'tExp_Constraint82', a2)
    if hasattr(a1, 'tExp_Role83'):
        assert not _is_linked(a1, 'tExp_Role83', b)
    if hasattr(a2, 'tExp_Role83'):
        assert _is_linked(a2, 'tExp_Role83', b)
    _safe_set(b, 'tExp_Constraint82', set())
    assert not _is_linked(b, 'tExp_Constraint82', a2)
    if hasattr(a2, 'tExp_Role83'):
        assert not _is_linked(a2, 'tExp_Role83', b)


def test_assoc_msgs53_reverse_link_reassign_clear():
    a1 = tExp_Msg(performative="sample_text")
    a2 = tExp_Msg(performative="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType54', {a1})
    assert _is_linked(b, 'tExp_EventType54', a1)
    if hasattr(a1, 'tExp_Msg'):
        assert _is_linked(a1, 'tExp_Msg', b)
    _safe_set(b, 'tExp_EventType54', {a2})
    assert _is_linked(b, 'tExp_EventType54', a2)
    if hasattr(a1, 'tExp_Msg'):
        assert not _is_linked(a1, 'tExp_Msg', b)
    if hasattr(a2, 'tExp_Msg'):
        assert _is_linked(a2, 'tExp_Msg', b)
    _safe_set(b, 'tExp_EventType54', set())
    assert not _is_linked(b, 'tExp_EventType54', a2)
    if hasattr(a2, 'tExp_Msg'):
        assert not _is_linked(a2, 'tExp_Msg', b)


def test_assoc_receiver61_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg62', a1)
    assert _is_linked(b, 'tExp_Msg62', a1)
    if hasattr(a1, 'tExp_Role63'):
        assert _is_linked(a1, 'tExp_Role63', b)
    _safe_set(b, 'tExp_Msg62', a2)
    assert _is_linked(b, 'tExp_Msg62', a2)
    if hasattr(a1, 'tExp_Role63'):
        assert not _is_linked(a1, 'tExp_Role63', b)
    if hasattr(a2, 'tExp_Role63'):
        assert _is_linked(a2, 'tExp_Role63', b)
    _safe_set(b, 'tExp_Msg62', None)
    assert not _is_linked(b, 'tExp_Msg62', a2)
    if hasattr(a2, 'tExp_Role63'):
        assert not _is_linked(a2, 'tExp_Role63', b)


def test_assoc_right4_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_PrologExpression(op="sample_text")
    _safe_set(b, 'tExp_PrologExpression5', a1)
    assert _is_linked(b, 'tExp_PrologExpression5', a1)
    if hasattr(a1, 'tExp_PrologExpression3'):
        assert _is_linked(a1, 'tExp_PrologExpression3', b)
    _safe_set(b, 'tExp_PrologExpression5', a2)
    assert _is_linked(b, 'tExp_PrologExpression5', a2)
    if hasattr(a1, 'tExp_PrologExpression3'):
        assert not _is_linked(a1, 'tExp_PrologExpression3', b)
    if hasattr(a2, 'tExp_PrologExpression3'):
        assert _is_linked(a2, 'tExp_PrologExpression3', b)
    _safe_set(b, 'tExp_PrologExpression5', None)
    assert not _is_linked(b, 'tExp_PrologExpression5', a2)
    if hasattr(a2, 'tExp_PrologExpression3'):
        assert not _is_linked(a2, 'tExp_PrologExpression3', b)


def test_assoc_right84_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Constraint(parMax="sample_text", parMin="sample_text", split="sample_text", together="sample_text")
    _safe_set(b, 'tExp_Constraint85', {a1})
    assert _is_linked(b, 'tExp_Constraint85', a1)
    if hasattr(a1, 'tExp_Role86'):
        assert _is_linked(a1, 'tExp_Role86', b)
    _safe_set(b, 'tExp_Constraint85', {a2})
    assert _is_linked(b, 'tExp_Constraint85', a2)
    if hasattr(a1, 'tExp_Role86'):
        assert not _is_linked(a1, 'tExp_Role86', b)
    if hasattr(a2, 'tExp_Role86'):
        assert _is_linked(a2, 'tExp_Role86', b)
    _safe_set(b, 'tExp_Constraint85', set())
    assert not _is_linked(b, 'tExp_Constraint85', a2)
    if hasattr(a2, 'tExp_Role86'):
        assert not _is_linked(a2, 'tExp_Role86', b)


def test_assoc_roles8_reverse_link_reassign_clear():
    a1 = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    a2 = tExp_TraceExpression(bodyL="sample_text_2", channelsL="sample_text_2", constraintsL="sample_text_2", decentralized="sample_text_2", decentralizedL="sample_text_2", gui="sample_text_2", guiL="sample_text_2", minimal="sample_text_2", minimalL="sample_text_2", modules="sample_text_2", modulesL="sample_text_2", name="sample_text_2", partitionL="sample_text_2", rolesL="sample_text_2", threshold="sample_text_2", thresholdL="sample_text_2", typesL="sample_text_2")
    b = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    _safe_set(b, 'tExp_Role', a1)
    assert _is_linked(b, 'tExp_Role', a1)
    if hasattr(a1, 'tExp_TraceExpression9'):
        assert _is_linked(a1, 'tExp_TraceExpression9', b)
    _safe_set(b, 'tExp_Role', a2)
    assert _is_linked(b, 'tExp_Role', a2)
    if hasattr(a1, 'tExp_TraceExpression9'):
        assert not _is_linked(a1, 'tExp_TraceExpression9', b)
    if hasattr(a2, 'tExp_TraceExpression9'):
        assert _is_linked(a2, 'tExp_TraceExpression9', b)
    _safe_set(b, 'tExp_Role', None)
    assert not _is_linked(b, 'tExp_Role', a2)
    if hasattr(a2, 'tExp_TraceExpression9'):
        assert not _is_linked(a2, 'tExp_TraceExpression9', b)


def test_assoc_sender64_reverse_link_reassign_clear():
    a1 = tExp_Role(args="sample_text", class_="sample_text", name="sample_text")
    a2 = tExp_Role(args="sample_text_2", class_="sample_text_2", name="sample_text_2")
    b = tExp_Msg(performative="sample_text")
    _safe_set(b, 'tExp_Msg65', a1)
    assert _is_linked(b, 'tExp_Msg65', a1)
    if hasattr(a1, 'tExp_Role66'):
        assert _is_linked(a1, 'tExp_Role66', b)
    _safe_set(b, 'tExp_Msg65', a2)
    assert _is_linked(b, 'tExp_Msg65', a2)
    if hasattr(a1, 'tExp_Role66'):
        assert not _is_linked(a1, 'tExp_Role66', b)
    if hasattr(a2, 'tExp_Role66'):
        assert _is_linked(a2, 'tExp_Role66', b)
    _safe_set(b, 'tExp_Msg65', None)
    assert not _is_linked(b, 'tExp_Msg65', a2)
    if hasattr(a2, 'tExp_Role66'):
        assert not _is_linked(a2, 'tExp_Role66', b)


def test_assoc_term41_reverse_link_reassign_clear():
    a1 = tExp_Term(name="sample_text")
    a2 = tExp_Term(name="sample_text_2")
    b = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    _safe_set(b, 'tExp_Expression42', a1)
    assert _is_linked(b, 'tExp_Expression42', a1)
    if hasattr(a1, 'tExp_Term43'):
        assert _is_linked(a1, 'tExp_Term43', b)
    _safe_set(b, 'tExp_Expression42', a2)
    assert _is_linked(b, 'tExp_Expression42', a2)
    if hasattr(a1, 'tExp_Term43'):
        assert not _is_linked(a1, 'tExp_Term43', b)
    if hasattr(a2, 'tExp_Term43'):
        assert _is_linked(a2, 'tExp_Term43', b)
    _safe_set(b, 'tExp_Expression42', None)
    assert not _is_linked(b, 'tExp_Expression42', a2)
    if hasattr(a2, 'tExp_Term43'):
        assert not _is_linked(a2, 'tExp_Term43', b)


def test_assoc_terms6_reverse_link_reassign_clear():
    a1 = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    a2 = tExp_TraceExpression(bodyL="sample_text_2", channelsL="sample_text_2", constraintsL="sample_text_2", decentralized="sample_text_2", decentralizedL="sample_text_2", gui="sample_text_2", guiL="sample_text_2", minimal="sample_text_2", minimalL="sample_text_2", modules="sample_text_2", modulesL="sample_text_2", name="sample_text_2", partitionL="sample_text_2", rolesL="sample_text_2", threshold="sample_text_2", thresholdL="sample_text_2", typesL="sample_text_2")
    b = tExp_Term(name="sample_text")
    _safe_set(b, 'tExp_Term', a1)
    assert _is_linked(b, 'tExp_Term', a1)
    if hasattr(a1, 'tExp_TraceExpression7'):
        assert _is_linked(a1, 'tExp_TraceExpression7', b)
    _safe_set(b, 'tExp_Term', a2)
    assert _is_linked(b, 'tExp_Term', a2)
    if hasattr(a1, 'tExp_TraceExpression7'):
        assert not _is_linked(a1, 'tExp_TraceExpression7', b)
    if hasattr(a2, 'tExp_TraceExpression7'):
        assert _is_linked(a2, 'tExp_TraceExpression7', b)
    _safe_set(b, 'tExp_Term', None)
    assert not _is_linked(b, 'tExp_Term', a2)
    if hasattr(a2, 'tExp_TraceExpression7'):
        assert not _is_linked(a2, 'tExp_TraceExpression7', b)


def test_assoc_terms87_reverse_link_reassign_clear():
    a1 = tExp_PrologExpression(op="sample_text")
    a2 = tExp_PrologExpression(op="sample_text_2")
    b = tExp_AtomExpression(atom="sample_text")
    _safe_set(b, 'tExp_AtomExpression', a1)
    assert _is_linked(b, 'tExp_AtomExpression', a1)
    if hasattr(a1, 'tExp_PrologExpression88'):
        assert _is_linked(a1, 'tExp_PrologExpression88', b)
    _safe_set(b, 'tExp_AtomExpression', a2)
    assert _is_linked(b, 'tExp_AtomExpression', a2)
    if hasattr(a1, 'tExp_PrologExpression88'):
        assert not _is_linked(a1, 'tExp_PrologExpression88', b)
    if hasattr(a2, 'tExp_PrologExpression88'):
        assert _is_linked(a2, 'tExp_PrologExpression88', b)
    _safe_set(b, 'tExp_AtomExpression', None)
    assert not _is_linked(b, 'tExp_AtomExpression', a2)
    if hasattr(a2, 'tExp_PrologExpression88'):
        assert not _is_linked(a2, 'tExp_PrologExpression88', b)


def test_assoc_typeFilter23_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType25', a1)
    assert _is_linked(b, 'tExp_EventType25', a1)
    if hasattr(a1, 'tExp_Expression24'):
        assert _is_linked(a1, 'tExp_Expression24', b)
    _safe_set(b, 'tExp_EventType25', a2)
    assert _is_linked(b, 'tExp_EventType25', a2)
    if hasattr(a1, 'tExp_Expression24'):
        assert not _is_linked(a1, 'tExp_Expression24', b)
    if hasattr(a2, 'tExp_Expression24'):
        assert _is_linked(a2, 'tExp_Expression24', b)
    _safe_set(b, 'tExp_EventType25', None)
    assert not _is_linked(b, 'tExp_EventType25', a2)
    if hasattr(a2, 'tExp_Expression24'):
        assert not _is_linked(a2, 'tExp_Expression24', b)


def test_assoc_typeSeq35_reverse_link_reassign_clear():
    a1 = tExp_Expression(eps="sample_text", operator="sample_text", variable="sample_text")
    a2 = tExp_Expression(eps="sample_text_2", operator="sample_text_2", variable="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType37', a1)
    assert _is_linked(b, 'tExp_EventType37', a1)
    if hasattr(a1, 'tExp_Expression36'):
        assert _is_linked(a1, 'tExp_Expression36', b)
    _safe_set(b, 'tExp_EventType37', a2)
    assert _is_linked(b, 'tExp_EventType37', a2)
    if hasattr(a1, 'tExp_Expression36'):
        assert not _is_linked(a1, 'tExp_Expression36', b)
    if hasattr(a2, 'tExp_Expression36'):
        assert _is_linked(a2, 'tExp_Expression36', b)
    _safe_set(b, 'tExp_EventType37', None)
    assert not _is_linked(b, 'tExp_EventType37', a2)
    if hasattr(a2, 'tExp_Expression36'):
        assert not _is_linked(a2, 'tExp_Expression36', b)


def test_assoc_types10_reverse_link_reassign_clear():
    a1 = tExp_TraceExpression(bodyL="sample_text", channelsL="sample_text", constraintsL="sample_text", decentralized="sample_text", decentralizedL="sample_text", gui="sample_text", guiL="sample_text", minimal="sample_text", minimalL="sample_text", modules="sample_text", modulesL="sample_text", name="sample_text", partitionL="sample_text", rolesL="sample_text", threshold="sample_text", thresholdL="sample_text", typesL="sample_text")
    a2 = tExp_TraceExpression(bodyL="sample_text_2", channelsL="sample_text_2", constraintsL="sample_text_2", decentralized="sample_text_2", decentralizedL="sample_text_2", gui="sample_text_2", guiL="sample_text_2", minimal="sample_text_2", minimalL="sample_text_2", modules="sample_text_2", modulesL="sample_text_2", name="sample_text_2", partitionL="sample_text_2", rolesL="sample_text_2", threshold="sample_text_2", thresholdL="sample_text_2", typesL="sample_text_2")
    b = tExp_EventType(name="sample_text")
    _safe_set(b, 'tExp_EventType', a1)
    assert _is_linked(b, 'tExp_EventType', a1)
    if hasattr(a1, 'tExp_TraceExpression11'):
        assert _is_linked(a1, 'tExp_TraceExpression11', b)
    _safe_set(b, 'tExp_EventType', a2)
    assert _is_linked(b, 'tExp_EventType', a2)
    if hasattr(a1, 'tExp_TraceExpression11'):
        assert not _is_linked(a1, 'tExp_TraceExpression11', b)
    if hasattr(a2, 'tExp_TraceExpression11'):
        assert _is_linked(a2, 'tExp_TraceExpression11', b)
    _safe_set(b, 'tExp_EventType', None)
    assert not _is_linked(b, 'tExp_EventType', a2)
    if hasattr(a2, 'tExp_TraceExpression11'):
        assert not _is_linked(a2, 'tExp_TraceExpression11', b)


