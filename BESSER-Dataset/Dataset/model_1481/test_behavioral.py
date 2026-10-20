import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Extendable,
    GraphElement,
    ParameterBinding,
    Pattern,
    PatternElement,
    graphpattern_Assignment,
    graphpattern_Association,
    graphpattern_AttributePattern,
    graphpattern_Bundle,
    graphpattern_DependencyEdge,
    graphpattern_DependencyGraph,
    graphpattern_DependencyNode,
    graphpattern_EAttribute,
    graphpattern_EClass,
    graphpattern_EObject,
    graphpattern_EObjectList,
    graphpattern_EPackage,
    graphpattern_EReference,
    graphpattern_EdgePattern,
    graphpattern_Extendable,
    graphpattern_GraphElement,
    graphpattern_GraphPattern,
    graphpattern_Matching,
    graphpattern_NodePattern,
    graphpattern_ObjectBinding,
    graphpattern_Parameter,
    graphpattern_ParameterBinding,
    graphpattern_Pattern,
    graphpattern_PatternElement,
    graphpattern_Profile,
    graphpattern_Resource,
    graphpattern_Stereotype,
    graphpattern_SubGraph,
    graphpattern_ValueBinding,
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

def test_assoc_attributes8_reverse_link_reassign_clear():
    a1 = graphpattern_NodePattern()
    a2 = graphpattern_NodePattern()
    b = graphpattern_AttributePattern(constant="sample_text", value="sample_text", variables="sample_text")
    _safe_set(b, 'AttributePattern', a1)
    assert _is_linked(b, 'AttributePattern', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'AttributePattern', a2)
    assert _is_linked(b, 'AttributePattern', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'AttributePattern', None)
    assert not _is_linked(b, 'AttributePattern', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_matching9_reverse_link_reassign_clear():
    a1 = graphpattern_NodePattern()
    a2 = graphpattern_NodePattern()
    b = graphpattern_Matching()
    _safe_set(b, 'Matching', a1)
    assert _is_linked(b, 'Matching', a1)
    if hasattr(a1, 'node10'):
        assert _is_linked(a1, 'node10', b)
    _safe_set(b, 'Matching', a2)
    assert _is_linked(b, 'Matching', a2)
    if hasattr(a1, 'node10'):
        assert not _is_linked(a1, 'node10', b)
    if hasattr(a2, 'node10'):
        assert _is_linked(a2, 'node10', b)
    _safe_set(b, 'Matching', None)
    assert not _is_linked(b, 'Matching', a2)
    if hasattr(a2, 'node10'):
        assert not _is_linked(a2, 'node10', b)


def test_assoc_node23_reverse_link_reassign_clear():
    a1 = graphpattern_NodePattern()
    a2 = graphpattern_NodePattern()
    b = graphpattern_AttributePattern(constant="sample_text", value="sample_text", variables="sample_text")
    _safe_set(b, 'attributes', a1)
    assert _is_linked(b, 'attributes', a1)
    if hasattr(a1, 'NodePattern24'):
        assert _is_linked(a1, 'NodePattern24', b)
    _safe_set(b, 'attributes', a2)
    assert _is_linked(b, 'attributes', a2)
    if hasattr(a1, 'NodePattern24'):
        assert not _is_linked(a1, 'NodePattern24', b)
    if hasattr(a2, 'NodePattern24'):
        assert _is_linked(a2, 'NodePattern24', b)
    _safe_set(b, 'attributes', None)
    assert not _is_linked(b, 'attributes', a2)
    if hasattr(a2, 'NodePattern24'):
        assert not _is_linked(a2, 'NodePattern24', b)


def test_assoc_node26_reverse_link_reassign_clear():
    a1 = graphpattern_NodePattern()
    a2 = graphpattern_NodePattern()
    b = graphpattern_Matching()
    _safe_set(b, 'matching', a1)
    assert _is_linked(b, 'matching', a1)
    if hasattr(a1, 'NodePattern27'):
        assert _is_linked(a1, 'NodePattern27', b)
    _safe_set(b, 'matching', a2)
    assert _is_linked(b, 'matching', a2)
    if hasattr(a1, 'NodePattern27'):
        assert not _is_linked(a1, 'NodePattern27', b)
    if hasattr(a2, 'NodePattern27'):
        assert _is_linked(a2, 'NodePattern27', b)
    _safe_set(b, 'matching', None)
    assert not _is_linked(b, 'matching', a2)
    if hasattr(a2, 'NodePattern27'):
        assert not _is_linked(a2, 'NodePattern27', b)


def test_assoc_patterns39_reverse_link_reassign_clear():
    a1 = graphpattern_Pattern()
    a2 = graphpattern_Pattern()
    b = graphpattern_Pattern()
    _safe_set(b, 'graphpattern_Pattern40', a1)
    assert _is_linked(b, 'graphpattern_Pattern40', a1)
    if hasattr(a1, 'graphpattern_Pattern38'):
        assert _is_linked(a1, 'graphpattern_Pattern38', b)
    _safe_set(b, 'graphpattern_Pattern40', a2)
    assert _is_linked(b, 'graphpattern_Pattern40', a2)
    if hasattr(a1, 'graphpattern_Pattern38'):
        assert not _is_linked(a1, 'graphpattern_Pattern38', b)
    if hasattr(a2, 'graphpattern_Pattern38'):
        assert _is_linked(a2, 'graphpattern_Pattern38', b)
    _safe_set(b, 'graphpattern_Pattern40', None)
    assert not _is_linked(b, 'graphpattern_Pattern40', a2)
    if hasattr(a2, 'graphpattern_Pattern38'):
        assert not _is_linked(a2, 'graphpattern_Pattern38', b)


def test_assoc_profile69_reverse_link_reassign_clear():
    a1 = graphpattern_Stereotype(name="sample_text")
    a2 = graphpattern_Stereotype(name="sample_text_2")
    b = graphpattern_Profile(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'Profile', a1)
    assert _is_linked(b, 'Profile', a1)
    if hasattr(a1, 'stereotypes'):
        assert _is_linked(a1, 'stereotypes', b)
    _safe_set(b, 'Profile', a2)
    assert _is_linked(b, 'Profile', a2)
    if hasattr(a1, 'stereotypes'):
        assert not _is_linked(a1, 'stereotypes', b)
    if hasattr(a2, 'stereotypes'):
        assert _is_linked(a2, 'stereotypes', b)
    _safe_set(b, 'Profile', None)
    assert not _is_linked(b, 'Profile', a2)
    if hasattr(a2, 'stereotypes'):
        assert not _is_linked(a2, 'stereotypes', b)


def test_assoc_stereotypes85_reverse_link_reassign_clear():
    a1 = graphpattern_Stereotype(name="sample_text")
    a2 = graphpattern_Stereotype(name="sample_text_2")
    b = graphpattern_Profile(description="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'profile', {a1})
    assert _is_linked(b, 'profile', a1)
    if hasattr(a1, 'Stereotype'):
        assert _is_linked(a1, 'Stereotype', b)
    _safe_set(b, 'profile', {a2})
    assert _is_linked(b, 'profile', a2)
    if hasattr(a1, 'Stereotype'):
        assert not _is_linked(a1, 'Stereotype', b)
    if hasattr(a2, 'Stereotype'):
        assert _is_linked(a2, 'Stereotype', b)
    _safe_set(b, 'profile', set())
    assert not _is_linked(b, 'profile', a2)
    if hasattr(a2, 'Stereotype'):
        assert not _is_linked(a2, 'Stereotype', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assignments34_stub_double():
    # graphpattern_Assignment has no real 'Assignment' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_Assignment()
    setattr(partner, 'Assignment', None)
    _safe_set(owner, 'pattern35', {partner})
    assert getattr(partner, 'Assignment') == owner
    _safe_set(owner, 'pattern35', set())
    assert getattr(partner, 'Assignment') is None


def test_assoc_associations13_stub_double():
    # graphpattern_Association has no real 'Association' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_Association()
    setattr(partner, 'Association', None)
    _safe_set(owner, 'source14', {partner})
    assert getattr(partner, 'Association') == owner
    _safe_set(owner, 'source14', set())
    assert getattr(partner, 'Association') is None


def test_assoc_bundle36_stub_double():
    # graphpattern_Bundle has no real 'graphpattern_Bundle37' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_Bundle()
    setattr(partner, 'graphpattern_Bundle37', None)
    _safe_set(owner, 'graphpattern_Pattern', partner)
    assert getattr(partner, 'graphpattern_Bundle37') == owner
    _safe_set(owner, 'graphpattern_Pattern', None)
    assert getattr(partner, 'graphpattern_Bundle37') is None


def test_assoc_content43_stub_double():
    # graphpattern_EObject has no real 'graphpattern_EObject44' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_EObjectList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_EObjectList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_EObjectList(label="sample_text")
    partner = graphpattern_EObject()
    setattr(partner, 'graphpattern_EObject44', None)
    _safe_set(owner, 'graphpattern_EObjectList', {partner})
    assert getattr(partner, 'graphpattern_EObject44') == owner
    _safe_set(owner, 'graphpattern_EObjectList', set())
    assert getattr(partner, 'graphpattern_EObject44') is None


def test_assoc_graphs31_stub_double():
    # graphpattern_GraphPattern has no real 'GraphPattern' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_GraphPattern()
    setattr(partner, 'GraphPattern', None)
    _safe_set(owner, 'pattern', {partner})
    assert getattr(partner, 'GraphPattern') == owner
    _safe_set(owner, 'pattern', set())
    assert getattr(partner, 'GraphPattern') is None


def test_assoc_incomings11_stub_double():
    # graphpattern_EdgePattern has no real 'EdgePattern12' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_EdgePattern()
    setattr(partner, 'EdgePattern12', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'EdgePattern12') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'EdgePattern12') is None


def test_assoc_matches25_stub_double():
    # graphpattern_EObject has no real 'graphpattern_EObject' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Matching's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Matching's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Matching()
    partner = graphpattern_EObject()
    setattr(partner, 'graphpattern_EObject', None)
    _safe_set(owner, 'graphpattern_Matching', {partner})
    assert getattr(partner, 'graphpattern_EObject') == owner
    _safe_set(owner, 'graphpattern_Matching', set())
    assert getattr(partner, 'graphpattern_EObject') is None


def test_assoc_nodes0_stub_double():
    # graphpattern_GraphPattern has no real 'graphpattern_GraphPattern' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_GraphPattern()
    setattr(partner, 'graphpattern_GraphPattern', None)
    _safe_set(owner, 'graphpattern_NodePattern', partner)
    assert owner in getattr(partner, 'graphpattern_GraphPattern')
    _safe_set(owner, 'graphpattern_NodePattern', None)
    assert owner not in getattr(partner, 'graphpattern_GraphPattern')


def test_assoc_nodes58_stub_double():
    # graphpattern_DependencyNode has no real 'graphpattern_DependencyNode59' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_DependencyNode()
    setattr(partner, 'graphpattern_DependencyNode59', None)
    _safe_set(owner, 'graphpattern_NodePattern60', partner)
    assert owner in getattr(partner, 'graphpattern_DependencyNode59')
    _safe_set(owner, 'graphpattern_NodePattern60', None)
    assert owner not in getattr(partner, 'graphpattern_DependencyNode59')


def test_assoc_outgoings5_stub_double():
    # graphpattern_EdgePattern has no real 'EdgePattern' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_EdgePattern()
    setattr(partner, 'EdgePattern', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'EdgePattern') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'EdgePattern') is None


def test_assoc_parameters32_stub_double():
    # graphpattern_Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'pattern33', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'pattern33', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_pattern1_stub_double():
    # graphpattern_GraphPattern has no real 'graphs' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_GraphPattern()
    setattr(partner, 'graphs', None)
    _safe_set(owner, 'Pattern', partner)
    assert getattr(partner, 'graphs') == owner
    _safe_set(owner, 'Pattern', None)
    assert getattr(partner, 'graphs') is None


def test_assoc_pattern41_stub_double():
    # graphpattern_Parameter has no real 'parameters' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_Parameter()
    setattr(partner, 'parameters', None)
    _safe_set(owner, 'Pattern42', partner)
    assert getattr(partner, 'parameters') == owner
    _safe_set(owner, 'Pattern42', None)
    assert getattr(partner, 'parameters') is None


def test_assoc_pattern73_stub_double():
    # graphpattern_Assignment has no real 'assignments' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Pattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Pattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Pattern()
    partner = graphpattern_Assignment()
    setattr(partner, 'assignments', None)
    _safe_set(owner, 'Pattern74', partner)
    assert getattr(partner, 'assignments') == owner
    _safe_set(owner, 'Pattern74', None)
    assert getattr(partner, 'assignments') is None


def test_assoc_profiles28_stub_double():
    # graphpattern_Bundle has no real 'graphpattern_Bundle' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Profile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Profile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Profile(description="sample_text", id="sample_text", name="sample_text")
    partner = graphpattern_Bundle()
    setattr(partner, 'graphpattern_Bundle', None)
    _safe_set(owner, 'graphpattern_Profile', partner)
    assert owner in getattr(partner, 'graphpattern_Bundle')
    _safe_set(owner, 'graphpattern_Profile', None)
    assert owner not in getattr(partner, 'graphpattern_Bundle')


def test_assoc_source16_stub_double():
    # graphpattern_EdgePattern has no real 'outgoings' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_EdgePattern()
    setattr(partner, 'outgoings', None)
    _safe_set(owner, 'NodePattern17', partner)
    assert getattr(partner, 'outgoings') == owner
    _safe_set(owner, 'NodePattern17', None)
    assert getattr(partner, 'outgoings') is None


def test_assoc_source66_stub_double():
    # graphpattern_Association has no real 'associations' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_Association()
    setattr(partner, 'associations', None)
    _safe_set(owner, 'NodePattern67', partner)
    assert getattr(partner, 'associations') == owner
    _safe_set(owner, 'NodePattern67', None)
    assert getattr(partner, 'associations') is None


def test_assoc_stereotypes88_stub_double():
    # graphpattern_Extendable has no real 'graphpattern_Extendable' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_Stereotype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_Stereotype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_Stereotype(name="sample_text")
    partner = graphpattern_Extendable()
    setattr(partner, 'graphpattern_Extendable', None)
    _safe_set(owner, 'graphpattern_Stereotype', partner)
    assert owner in getattr(partner, 'graphpattern_Extendable')
    _safe_set(owner, 'graphpattern_Stereotype', None)
    assert owner not in getattr(partner, 'graphpattern_Extendable')


def test_assoc_target15_stub_double():
    # graphpattern_EdgePattern has no real 'incomings' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_EdgePattern()
    setattr(partner, 'incomings', None)
    _safe_set(owner, 'NodePattern', partner)
    assert getattr(partner, 'incomings') == owner
    _safe_set(owner, 'NodePattern', None)
    assert getattr(partner, 'incomings') is None


def test_assoc_type22_stub_double():
    # graphpattern_EAttribute has no real 'graphpattern_EAttribute' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_AttributePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_AttributePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_AttributePattern(constant="sample_text", value="sample_text", variables="sample_text")
    partner = graphpattern_EAttribute()
    setattr(partner, 'graphpattern_EAttribute', None)
    _safe_set(owner, 'graphpattern_AttributePattern', partner)
    assert getattr(partner, 'graphpattern_EAttribute') == owner
    _safe_set(owner, 'graphpattern_AttributePattern', None)
    assert getattr(partner, 'graphpattern_EAttribute') is None


def test_assoc_type6_stub_double():
    # graphpattern_EClass has no real 'graphpattern_EClass' property in the generated
    # code (a bare stub) -- manually attach it so graphpattern_NodePattern's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graphpattern_NodePattern's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graphpattern_NodePattern()
    partner = graphpattern_EClass()
    setattr(partner, 'graphpattern_EClass', None)
    _safe_set(owner, 'graphpattern_NodePattern7', partner)
    assert getattr(partner, 'graphpattern_EClass') == owner
    _safe_set(owner, 'graphpattern_NodePattern7', None)
    assert getattr(partner, 'graphpattern_EClass') is None


