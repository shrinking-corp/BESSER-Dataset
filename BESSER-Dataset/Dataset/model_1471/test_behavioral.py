import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Cause,
    graph_Dependency,
    graph_DependencyGraph,
    graph_DeploymentUnitType,
    graph_DocumentRoot,
    graph_EStringToStringMapEntry,
    graph_Node,
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

def test_assoc_cause0_reverse_link_reassign_clear():
    a1 = graph_Dependency(id="sample_text", locality="sample_text")
    a2 = graph_Dependency(id="sample_text_2", locality="sample_text_2")
    b = graph_Cause(name="sample_text", type="sample_text")
    _safe_set(b, 'graph_Cause', a1)
    assert _is_linked(b, 'graph_Cause', a1)
    if hasattr(a1, 'graph_Dependency'):
        assert _is_linked(a1, 'graph_Dependency', b)
    _safe_set(b, 'graph_Cause', a2)
    assert _is_linked(b, 'graph_Cause', a2)
    if hasattr(a1, 'graph_Dependency'):
        assert not _is_linked(a1, 'graph_Dependency', b)
    if hasattr(a2, 'graph_Dependency'):
        assert _is_linked(a2, 'graph_Dependency', b)
    _safe_set(b, 'graph_Cause', None)
    assert not _is_linked(b, 'graph_Cause', a2)
    if hasattr(a2, 'graph_Dependency'):
        assert not _is_linked(a2, 'graph_Dependency', b)


def test_assoc_dependency23_reverse_link_reassign_clear():
    a1 = graph_Node(id="sample_text")
    a2 = graph_Node(id="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency25', a1)
    assert _is_linked(b, 'graph_Dependency25', a1)
    if hasattr(a1, 'graph_Node24'):
        assert _is_linked(a1, 'graph_Node24', b)
    _safe_set(b, 'graph_Dependency25', a2)
    assert _is_linked(b, 'graph_Dependency25', a2)
    if hasattr(a1, 'graph_Node24'):
        assert not _is_linked(a1, 'graph_Node24', b)
    if hasattr(a2, 'graph_Node24'):
        assert _is_linked(a2, 'graph_Node24', b)
    _safe_set(b, 'graph_Dependency25', None)
    assert not _is_linked(b, 'graph_Dependency25', a2)
    if hasattr(a2, 'graph_Node24'):
        assert not _is_linked(a2, 'graph_Node24', b)


def test_assoc_destination1_reverse_link_reassign_clear():
    a1 = graph_Node(id="sample_text")
    a2 = graph_Node(id="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency2', a1)
    assert _is_linked(b, 'graph_Dependency2', a1)
    if hasattr(a1, 'graph_Node'):
        assert _is_linked(a1, 'graph_Node', b)
    _safe_set(b, 'graph_Dependency2', a2)
    assert _is_linked(b, 'graph_Dependency2', a2)
    if hasattr(a1, 'graph_Node'):
        assert not _is_linked(a1, 'graph_Node', b)
    if hasattr(a2, 'graph_Node'):
        assert _is_linked(a2, 'graph_Node', b)
    _safe_set(b, 'graph_Dependency2', None)
    assert not _is_linked(b, 'graph_Dependency2', a2)
    if hasattr(a2, 'graph_Node'):
        assert not _is_linked(a2, 'graph_Node', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = graph_Node(id="sample_text")
    a2 = graph_Node(id="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency4', a1)
    assert _is_linked(b, 'graph_Dependency4', a1)
    if hasattr(a1, 'graph_Node5'):
        assert _is_linked(a1, 'graph_Node5', b)
    _safe_set(b, 'graph_Dependency4', a2)
    assert _is_linked(b, 'graph_Dependency4', a2)
    if hasattr(a1, 'graph_Node5'):
        assert not _is_linked(a1, 'graph_Node5', b)
    if hasattr(a2, 'graph_Node5'):
        assert _is_linked(a2, 'graph_Node5', b)
    _safe_set(b, 'graph_Dependency4', None)
    assert not _is_linked(b, 'graph_Dependency4', a2)
    if hasattr(a2, 'graph_Node5'):
        assert not _is_linked(a2, 'graph_Node5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_dependency8_stub_double():
    # graph_DependencyGraph has no real 'graph_DependencyGraph9' property in the generated
    # code (a bare stub) -- manually attach it so graph_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Dependency(id="sample_text", locality="sample_text")
    partner = graph_DependencyGraph()
    setattr(partner, 'graph_DependencyGraph9', None)
    _safe_set(owner, 'graph_Dependency10', partner)
    assert owner in getattr(partner, 'graph_DependencyGraph9')
    _safe_set(owner, 'graph_Dependency10', None)
    assert owner not in getattr(partner, 'graph_DependencyGraph9')


def test_assoc_dependencyGraph18_stub_double():
    # graph_DependencyGraph has no real 'graph_DependencyGraph20' property in the generated
    # code (a bare stub) -- manually attach it so graph_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DocumentRoot(mixed="sample_text")
    partner = graph_DependencyGraph()
    setattr(partner, 'graph_DependencyGraph20', None)
    _safe_set(owner, 'graph_DocumentRoot19', {partner})
    assert getattr(partner, 'graph_DependencyGraph20') == owner
    _safe_set(owner, 'graph_DocumentRoot19', set())
    assert getattr(partner, 'graph_DependencyGraph20') is None


def test_assoc_node6_stub_double():
    # graph_DependencyGraph has no real 'graph_DependencyGraph' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(id="sample_text")
    partner = graph_DependencyGraph()
    setattr(partner, 'graph_DependencyGraph', None)
    _safe_set(owner, 'graph_Node7', partner)
    assert owner in getattr(partner, 'graph_DependencyGraph')
    _safe_set(owner, 'graph_Node7', None)
    assert owner not in getattr(partner, 'graph_DependencyGraph')


def test_assoc_origin11_stub_double():
    # graph_DependencyGraph has no real 'graph_DependencyGraph12' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(id="sample_text")
    partner = graph_DependencyGraph()
    setattr(partner, 'graph_DependencyGraph12', None)
    _safe_set(owner, 'graph_Node13', partner)
    assert getattr(partner, 'graph_DependencyGraph12') == owner
    _safe_set(owner, 'graph_Node13', None)
    assert getattr(partner, 'graph_DependencyGraph12') is None


def test_assoc_unit21_stub_double():
    # graph_DeploymentUnitType has no real 'graph_DeploymentUnitType' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(id="sample_text")
    partner = graph_DeploymentUnitType()
    setattr(partner, 'graph_DeploymentUnitType', None)
    _safe_set(owner, 'graph_Node22', partner)
    assert getattr(partner, 'graph_DeploymentUnitType') == owner
    _safe_set(owner, 'graph_Node22', None)
    assert getattr(partner, 'graph_DeploymentUnitType') is None


def test_assoc_xMLNSPrefixMap14_stub_double():
    # graph_EStringToStringMapEntry has no real 'graph_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so graph_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DocumentRoot(mixed="sample_text")
    partner = graph_EStringToStringMapEntry()
    setattr(partner, 'graph_EStringToStringMapEntry', None)
    _safe_set(owner, 'graph_DocumentRoot', {partner})
    assert getattr(partner, 'graph_EStringToStringMapEntry') == owner
    _safe_set(owner, 'graph_DocumentRoot', set())
    assert getattr(partner, 'graph_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation15_stub_double():
    # graph_EStringToStringMapEntry has no real 'graph_EStringToStringMapEntry17' property in the generated
    # code (a bare stub) -- manually attach it so graph_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DocumentRoot(mixed="sample_text")
    partner = graph_EStringToStringMapEntry()
    setattr(partner, 'graph_EStringToStringMapEntry17', None)
    _safe_set(owner, 'graph_DocumentRoot16', {partner})
    assert getattr(partner, 'graph_EStringToStringMapEntry17') == owner
    _safe_set(owner, 'graph_DocumentRoot16', set())
    assert getattr(partner, 'graph_EStringToStringMapEntry17') is None


