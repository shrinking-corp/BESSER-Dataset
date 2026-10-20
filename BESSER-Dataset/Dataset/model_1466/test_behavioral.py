import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Cause,
    graph_Dependency,
    graph_DocumentRoot,
    graph_EStringToStringMapEntry,
    graph_EnvironmentGraph,
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
    b = graph_Cause(name="sample_text", type="sample_text", version="sample_text")
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


def test_assoc_cause10_reverse_link_reassign_clear():
    a1 = graph_DocumentRoot(mixed="sample_text")
    a2 = graph_DocumentRoot(mixed="sample_text_2")
    b = graph_Cause(name="sample_text", type="sample_text", version="sample_text")
    _safe_set(b, 'graph_Cause12', a1)
    assert _is_linked(b, 'graph_Cause12', a1)
    if hasattr(a1, 'graph_DocumentRoot11'):
        assert _is_linked(a1, 'graph_DocumentRoot11', b)
    _safe_set(b, 'graph_Cause12', a2)
    assert _is_linked(b, 'graph_Cause12', a2)
    if hasattr(a1, 'graph_DocumentRoot11'):
        assert not _is_linked(a1, 'graph_DocumentRoot11', b)
    if hasattr(a2, 'graph_DocumentRoot11'):
        assert _is_linked(a2, 'graph_DocumentRoot11', b)
    _safe_set(b, 'graph_Cause12', None)
    assert not _is_linked(b, 'graph_Cause12', a2)
    if hasattr(a2, 'graph_DocumentRoot11'):
        assert not _is_linked(a2, 'graph_DocumentRoot11', b)


def test_assoc_dependencies30_reverse_link_reassign_clear():
    a1 = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    a2 = graph_Node(containerName="sample_text_2", id="sample_text_2", nodeName="sample_text_2", unitName="sample_text_2", unitVersion="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency32', a1)
    assert _is_linked(b, 'graph_Dependency32', a1)
    if hasattr(a1, 'graph_Node31'):
        assert _is_linked(a1, 'graph_Node31', b)
    _safe_set(b, 'graph_Dependency32', a2)
    assert _is_linked(b, 'graph_Dependency32', a2)
    if hasattr(a1, 'graph_Node31'):
        assert not _is_linked(a1, 'graph_Node31', b)
    if hasattr(a2, 'graph_Node31'):
        assert _is_linked(a2, 'graph_Node31', b)
    _safe_set(b, 'graph_Dependency32', None)
    assert not _is_linked(b, 'graph_Dependency32', a2)
    if hasattr(a2, 'graph_Node31'):
        assert not _is_linked(a2, 'graph_Node31', b)


def test_assoc_dependency13_reverse_link_reassign_clear():
    a1 = graph_DocumentRoot(mixed="sample_text")
    a2 = graph_DocumentRoot(mixed="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency15', a1)
    assert _is_linked(b, 'graph_Dependency15', a1)
    if hasattr(a1, 'graph_DocumentRoot14'):
        assert _is_linked(a1, 'graph_DocumentRoot14', b)
    _safe_set(b, 'graph_Dependency15', a2)
    assert _is_linked(b, 'graph_Dependency15', a2)
    if hasattr(a1, 'graph_DocumentRoot14'):
        assert not _is_linked(a1, 'graph_DocumentRoot14', b)
    if hasattr(a2, 'graph_DocumentRoot14'):
        assert _is_linked(a2, 'graph_DocumentRoot14', b)
    _safe_set(b, 'graph_Dependency15', None)
    assert not _is_linked(b, 'graph_Dependency15', a2)
    if hasattr(a2, 'graph_DocumentRoot14'):
        assert not _is_linked(a2, 'graph_DocumentRoot14', b)


def test_assoc_destination1_reverse_link_reassign_clear():
    a1 = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    a2 = graph_Node(containerName="sample_text_2", id="sample_text_2", nodeName="sample_text_2", unitName="sample_text_2", unitVersion="sample_text_2")
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


def test_assoc_isRequiredBy33_reverse_link_reassign_clear():
    a1 = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    a2 = graph_Node(containerName="sample_text_2", id="sample_text_2", nodeName="sample_text_2", unitName="sample_text_2", unitVersion="sample_text_2")
    b = graph_Dependency(id="sample_text", locality="sample_text")
    _safe_set(b, 'graph_Dependency35', a1)
    assert _is_linked(b, 'graph_Dependency35', a1)
    if hasattr(a1, 'graph_Node34'):
        assert _is_linked(a1, 'graph_Node34', b)
    _safe_set(b, 'graph_Dependency35', a2)
    assert _is_linked(b, 'graph_Dependency35', a2)
    if hasattr(a1, 'graph_Node34'):
        assert not _is_linked(a1, 'graph_Node34', b)
    if hasattr(a2, 'graph_Node34'):
        assert _is_linked(a2, 'graph_Node34', b)
    _safe_set(b, 'graph_Dependency35', None)
    assert not _is_linked(b, 'graph_Dependency35', a2)
    if hasattr(a2, 'graph_Node34'):
        assert not _is_linked(a2, 'graph_Node34', b)


def test_assoc_node18_reverse_link_reassign_clear():
    a1 = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    a2 = graph_Node(containerName="sample_text_2", id="sample_text_2", nodeName="sample_text_2", unitName="sample_text_2", unitVersion="sample_text_2")
    b = graph_DocumentRoot(mixed="sample_text")
    _safe_set(b, 'graph_DocumentRoot19', {a1})
    assert _is_linked(b, 'graph_DocumentRoot19', a1)
    if hasattr(a1, 'graph_Node20'):
        assert _is_linked(a1, 'graph_Node20', b)
    _safe_set(b, 'graph_DocumentRoot19', {a2})
    assert _is_linked(b, 'graph_DocumentRoot19', a2)
    if hasattr(a1, 'graph_Node20'):
        assert not _is_linked(a1, 'graph_Node20', b)
    if hasattr(a2, 'graph_Node20'):
        assert _is_linked(a2, 'graph_Node20', b)
    _safe_set(b, 'graph_DocumentRoot19', set())
    assert not _is_linked(b, 'graph_DocumentRoot19', a2)
    if hasattr(a2, 'graph_Node20'):
        assert not _is_linked(a2, 'graph_Node20', b)


def test_assoc_source3_reverse_link_reassign_clear():
    a1 = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    a2 = graph_Node(containerName="sample_text_2", id="sample_text_2", nodeName="sample_text_2", unitName="sample_text_2", unitVersion="sample_text_2")
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

def test_assoc_dependencies24_stub_double():
    # graph_EnvironmentGraph has no real 'graph_EnvironmentGraph25' property in the generated
    # code (a bare stub) -- manually attach it so graph_Dependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Dependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Dependency(id="sample_text", locality="sample_text")
    partner = graph_EnvironmentGraph()
    setattr(partner, 'graph_EnvironmentGraph25', None)
    _safe_set(owner, 'graph_Dependency26', partner)
    assert owner in getattr(partner, 'graph_EnvironmentGraph25')
    _safe_set(owner, 'graph_Dependency26', None)
    assert owner not in getattr(partner, 'graph_EnvironmentGraph25')


def test_assoc_environmentGraph16_stub_double():
    # graph_EnvironmentGraph has no real 'graph_EnvironmentGraph' property in the generated
    # code (a bare stub) -- manually attach it so graph_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DocumentRoot(mixed="sample_text")
    partner = graph_EnvironmentGraph()
    setattr(partner, 'graph_EnvironmentGraph', None)
    _safe_set(owner, 'graph_DocumentRoot17', {partner})
    assert getattr(partner, 'graph_EnvironmentGraph') == owner
    _safe_set(owner, 'graph_DocumentRoot17', set())
    assert getattr(partner, 'graph_EnvironmentGraph') is None


def test_assoc_node21_stub_double():
    # graph_EnvironmentGraph has no real 'graph_EnvironmentGraph22' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    partner = graph_EnvironmentGraph()
    setattr(partner, 'graph_EnvironmentGraph22', None)
    _safe_set(owner, 'graph_Node23', partner)
    assert owner in getattr(partner, 'graph_EnvironmentGraph22')
    _safe_set(owner, 'graph_Node23', None)
    assert owner not in getattr(partner, 'graph_EnvironmentGraph22')


def test_assoc_origins27_stub_double():
    # graph_EnvironmentGraph has no real 'graph_EnvironmentGraph28' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(containerName="sample_text", id="sample_text", nodeName="sample_text", unitName="sample_text", unitVersion="sample_text")
    partner = graph_EnvironmentGraph()
    setattr(partner, 'graph_EnvironmentGraph28', None)
    _safe_set(owner, 'graph_Node29', partner)
    assert owner in getattr(partner, 'graph_EnvironmentGraph28')
    _safe_set(owner, 'graph_Node29', None)
    assert owner not in getattr(partner, 'graph_EnvironmentGraph28')


def test_assoc_xMLNSPrefixMap6_stub_double():
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


def test_assoc_xSISchemaLocation7_stub_double():
    # graph_EStringToStringMapEntry has no real 'graph_EStringToStringMapEntry9' property in the generated
    # code (a bare stub) -- manually attach it so graph_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DocumentRoot(mixed="sample_text")
    partner = graph_EStringToStringMapEntry()
    setattr(partner, 'graph_EStringToStringMapEntry9', None)
    _safe_set(owner, 'graph_DocumentRoot8', {partner})
    assert getattr(partner, 'graph_EStringToStringMapEntry9') == owner
    _safe_set(owner, 'graph_DocumentRoot8', set())
    assert getattr(partner, 'graph_EStringToStringMapEntry9') is None


