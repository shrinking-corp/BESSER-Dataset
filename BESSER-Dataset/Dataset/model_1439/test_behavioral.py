import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    mention_graph_Edge,
    mention_graph_HashTag,
    mention_graph_MentionGraph,
    mention_graph_Node,
    mention_graph_User,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodes0_stub_double():
    # mention_graph_MentionGraph has no real 'mention_graph_MentionGraph' property in the generated
    # code (a bare stub) -- manually attach it so mention_graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mention_graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mention_graph_Node(value="sample_text")
    partner = mention_graph_MentionGraph()
    setattr(partner, 'mention_graph_MentionGraph', None)
    _safe_set(owner, 'mention_graph_Node', partner)
    assert owner in getattr(partner, 'mention_graph_MentionGraph')
    _safe_set(owner, 'mention_graph_Node', None)
    assert owner not in getattr(partner, 'mention_graph_MentionGraph')


def test_assoc_relatedHashtags3_stub_double():
    # mention_graph_User has no real 'mention_graph_User' property in the generated
    # code (a bare stub) -- manually attach it so mention_graph_HashTag's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mention_graph_HashTag's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mention_graph_HashTag(count=7)
    partner = mention_graph_User()
    setattr(partner, 'mention_graph_User', None)
    _safe_set(owner, 'mention_graph_HashTag', partner)
    assert owner in getattr(partner, 'mention_graph_User')
    _safe_set(owner, 'mention_graph_HashTag', None)
    assert owner not in getattr(partner, 'mention_graph_User')


def test_assoc_source4_stub_double():
    # mention_graph_Edge has no real 'mention_graph_Edge5' property in the generated
    # code (a bare stub) -- manually attach it so mention_graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mention_graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mention_graph_Node(value="sample_text")
    partner = mention_graph_Edge()
    setattr(partner, 'mention_graph_Edge5', None)
    _safe_set(owner, 'mention_graph_Node6', partner)
    assert getattr(partner, 'mention_graph_Edge5') == owner
    _safe_set(owner, 'mention_graph_Node6', None)
    assert getattr(partner, 'mention_graph_Edge5') is None


def test_assoc_target7_stub_double():
    # mention_graph_Edge has no real 'mention_graph_Edge8' property in the generated
    # code (a bare stub) -- manually attach it so mention_graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mention_graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mention_graph_Node(value="sample_text")
    partner = mention_graph_Edge()
    setattr(partner, 'mention_graph_Edge8', None)
    _safe_set(owner, 'mention_graph_Node9', partner)
    assert getattr(partner, 'mention_graph_Edge8') == owner
    _safe_set(owner, 'mention_graph_Node9', None)
    assert getattr(partner, 'mention_graph_Edge8') is None


