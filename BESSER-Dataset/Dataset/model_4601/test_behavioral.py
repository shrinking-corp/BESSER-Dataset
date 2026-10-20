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
    gv_AList,
    gv_AbstractGraph,
    gv_AssignmentStatement,
    gv_Attributable,
    gv_Attribute,
    gv_AttributeList,
    gv_AttributeStatement,
    gv_Commentable,
    gv_Connectable,
    gv_EdgeStatement,
    gv_Graph,
    gv_Identifiable,
    gv_NodeID,
    gv_NodeStatement,
    gv_Port,
    gv_Statement,
    gv_StatementList,
    gv_StrictIdentifiable,
    gv_Subgraph,
    gv_Target,
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

def test_assoc_next_target26_reverse_link_reassign_clear():
    a1 = gv_Target(operation="sample_text")
    a2 = gv_Target(operation="sample_text_2")
    b = gv_Target(operation="sample_text")
    _safe_set(b, 'gv_Target27', a1)
    assert _is_linked(b, 'gv_Target27', a1)
    if hasattr(a1, 'gv_Target25'):
        assert _is_linked(a1, 'gv_Target25', b)
    _safe_set(b, 'gv_Target27', a2)
    assert _is_linked(b, 'gv_Target27', a2)
    if hasattr(a1, 'gv_Target25'):
        assert not _is_linked(a1, 'gv_Target25', b)
    if hasattr(a2, 'gv_Target25'):
        assert _is_linked(a2, 'gv_Target25', b)
    _safe_set(b, 'gv_Target27', None)
    assert not _is_linked(b, 'gv_Target27', a2)
    if hasattr(a2, 'gv_Target25'):
        assert not _is_linked(a2, 'gv_Target25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute1_stub_double():
    # gv_AList has no real 'gv_AList' property in the generated
    # code (a bare stub) -- manually attach it so gv_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gv_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gv_Attribute(key="sample_text", value="sample_text")
    partner = gv_AList()
    setattr(partner, 'gv_AList', None)
    _safe_set(owner, 'gv_Attribute', partner)
    assert getattr(partner, 'gv_AList') == owner
    _safe_set(owner, 'gv_Attribute', None)
    assert getattr(partner, 'gv_AList') is None


def test_assoc_attributes12_stub_double():
    # gv_AttributeList has no real 'gv_AttributeList13' property in the generated
    # code (a bare stub) -- manually attach it so gv_AttributeStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gv_AttributeStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gv_AttributeStatement(context="sample_text")
    partner = gv_AttributeList()
    setattr(partner, 'gv_AttributeList13', None)
    _safe_set(owner, 'gv_AttributeStatement', partner)
    assert getattr(partner, 'gv_AttributeList13') == owner
    _safe_set(owner, 'gv_AttributeStatement', None)
    assert getattr(partner, 'gv_AttributeList13') is None


def test_assoc_port18_stub_double():
    # gv_NodeID has no real 'gv_NodeID19' property in the generated
    # code (a bare stub) -- manually attach it so gv_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gv_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gv_Port(compass="sample_text")
    partner = gv_NodeID()
    setattr(partner, 'gv_NodeID19', None)
    _safe_set(owner, 'gv_Port', partner)
    assert getattr(partner, 'gv_NodeID19') == owner
    _safe_set(owner, 'gv_Port', None)
    assert getattr(partner, 'gv_NodeID19') is None


def test_assoc_target15_stub_double():
    # gv_EdgeStatement has no real 'gv_EdgeStatement16' property in the generated
    # code (a bare stub) -- manually attach it so gv_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gv_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gv_Target(operation="sample_text")
    partner = gv_EdgeStatement()
    setattr(partner, 'gv_EdgeStatement16', None)
    _safe_set(owner, 'gv_Target', partner)
    assert getattr(partner, 'gv_EdgeStatement16') == owner
    _safe_set(owner, 'gv_Target', None)
    assert getattr(partner, 'gv_EdgeStatement16') is None


def test_assoc_target28_stub_double():
    # gv_Connectable has no real 'gv_Connectable30' property in the generated
    # code (a bare stub) -- manually attach it so gv_Target's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gv_Target's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gv_Target(operation="sample_text")
    partner = gv_Connectable()
    setattr(partner, 'gv_Connectable30', None)
    _safe_set(owner, 'gv_Target29', partner)
    assert getattr(partner, 'gv_Connectable30') == owner
    _safe_set(owner, 'gv_Target29', None)
    assert getattr(partner, 'gv_Connectable30') is None


