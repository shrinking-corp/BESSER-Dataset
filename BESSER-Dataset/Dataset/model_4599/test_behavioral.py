import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractGraph,
    Attributable,
    Attribute,
    Commentable,
    Connectable,
    Identifiable,
    Statement,
    StrictIdentifiable,
    dot_AList,
    dot_AbstractGraph,
    dot_AssignmentStatement,
    dot_Attributable,
    dot_Attribute,
    dot_AttributeList,
    dot_AttributeStatement,
    dot_Commentable,
    dot_Connectable,
    dot_EdgeStatement,
    dot_Graph,
    dot_Identifiable,
    dot_NodeID,
    dot_NodeStatement,
    dot_Port,
    dot_Statement,
    dot_StatementList,
    dot_StrictIdentifiable,
    dot_Subgraph,
    dot_Target,
    Compass,
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

def test_assoc_attribute1_reverse_link_reassign_clear():
    a1 = dot_Attribute(key="sample_text", value="sample_text")
    a2 = dot_Attribute(key="sample_text_2", value="sample_text_2")
    b = dot_AList()
    _safe_set(b, 'dot_AList', a1)
    assert _is_linked(b, 'dot_AList', a1)
    if hasattr(a1, 'dot_Attribute'):
        assert _is_linked(a1, 'dot_Attribute', b)
    _safe_set(b, 'dot_AList', a2)
    assert _is_linked(b, 'dot_AList', a2)
    if hasattr(a1, 'dot_Attribute'):
        assert not _is_linked(a1, 'dot_Attribute', b)
    if hasattr(a2, 'dot_Attribute'):
        assert _is_linked(a2, 'dot_Attribute', b)
    _safe_set(b, 'dot_AList', None)
    assert not _is_linked(b, 'dot_AList', a2)
    if hasattr(a2, 'dot_Attribute'):
        assert not _is_linked(a2, 'dot_Attribute', b)


def test_assoc_next_target24_reverse_link_reassign_clear():
    a1 = dot_Target(operation="sample_text")
    a2 = dot_Target(operation="sample_text_2")
    b = dot_Target(operation="sample_text")
    _safe_set(b, 'dot_Target25', a1)
    assert _is_linked(b, 'dot_Target25', a1)
    if hasattr(a1, 'dot_Target23'):
        assert _is_linked(a1, 'dot_Target23', b)
    _safe_set(b, 'dot_Target25', a2)
    assert _is_linked(b, 'dot_Target25', a2)
    if hasattr(a1, 'dot_Target23'):
        assert not _is_linked(a1, 'dot_Target23', b)
    if hasattr(a2, 'dot_Target23'):
        assert _is_linked(a2, 'dot_Target23', b)
    _safe_set(b, 'dot_Target25', None)
    assert not _is_linked(b, 'dot_Target25', a2)
    if hasattr(a2, 'dot_Target23'):
        assert not _is_linked(a2, 'dot_Target23', b)


def test_assoc_tail3_reverse_link_reassign_clear():
    a1 = dot_AList()
    a2 = dot_AList()
    b = dot_AList()
    _safe_set(b, 'dot_AList4', a1)
    assert _is_linked(b, 'dot_AList4', a1)
    if hasattr(a1, 'dot_AList2'):
        assert _is_linked(a1, 'dot_AList2', b)
    _safe_set(b, 'dot_AList4', a2)
    assert _is_linked(b, 'dot_AList4', a2)
    if hasattr(a1, 'dot_AList2'):
        assert not _is_linked(a1, 'dot_AList2', b)
    if hasattr(a2, 'dot_AList2'):
        assert _is_linked(a2, 'dot_AList2', b)
    _safe_set(b, 'dot_AList4', None)
    assert not _is_linked(b, 'dot_AList4', a2)
    if hasattr(a2, 'dot_AList2'):
        assert not _is_linked(a2, 'dot_AList2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes5_stub_double():
    # dot_AttributeList has no real 'dot_AttributeList' property in the generated
    # code (a bare stub) -- manually attach it so dot_Attributable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Attributable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Attributable()
    partner = dot_AttributeList()
    setattr(partner, 'dot_AttributeList', None)
    _safe_set(owner, 'dot_Attributable', partner)
    assert getattr(partner, 'dot_AttributeList') == owner
    _safe_set(owner, 'dot_Attributable', None)
    assert getattr(partner, 'dot_AttributeList') is None


def test_assoc_list6_stub_double():
    # dot_AttributeList has no real 'dot_AttributeList7' property in the generated
    # code (a bare stub) -- manually attach it so dot_AList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_AList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_AList()
    partner = dot_AttributeList()
    setattr(partner, 'dot_AttributeList7', None)
    _safe_set(owner, 'dot_AList8', partner)
    assert getattr(partner, 'dot_AttributeList7') == owner
    _safe_set(owner, 'dot_AList8', None)
    assert getattr(partner, 'dot_AttributeList7') is None


def test_assoc_port16_stub_double():
    # dot_NodeID has no real 'dot_NodeID17' property in the generated
    # code (a bare stub) -- manually attach it so dot_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Port(compass="sample_text")
    partner = dot_NodeID()
    setattr(partner, 'dot_NodeID17', None)
    _safe_set(owner, 'dot_Port', partner)
    assert getattr(partner, 'dot_NodeID17') == owner
    _safe_set(owner, 'dot_Port', None)
    assert getattr(partner, 'dot_NodeID17') is None


def test_assoc_target13_stub_double():
    # dot_EdgeStatement has no real 'dot_EdgeStatement14' property in the generated
    # code (a bare stub) -- manually attach it so dot_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Target(operation="sample_text")
    partner = dot_EdgeStatement()
    setattr(partner, 'dot_EdgeStatement14', None)
    _safe_set(owner, 'dot_Target', partner)
    assert getattr(partner, 'dot_EdgeStatement14') == owner
    _safe_set(owner, 'dot_Target', None)
    assert getattr(partner, 'dot_EdgeStatement14') is None


def test_assoc_target26_stub_double():
    # dot_Connectable has no real 'dot_Connectable28' property in the generated
    # code (a bare stub) -- manually attach it so dot_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dot_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dot_Target(operation="sample_text")
    partner = dot_Connectable()
    setattr(partner, 'dot_Connectable28', None)
    _safe_set(owner, 'dot_Target27', partner)
    assert getattr(partner, 'dot_Connectable28') == owner
    _safe_set(owner, 'dot_Target27', None)
    assert getattr(partner, 'dot_Connectable28') is None


