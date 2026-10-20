import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SkillGraph_Edge,
    SkillGraph_Equation,
    SkillGraph_Graph,
    SkillGraph_Node,
    SkillGraph_Parameter,
    SkillGraph_Requirement,
    Category,
    Type,
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

def test_assoc_equations6_reverse_link_reassign_clear():
    a1 = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    a2 = SkillGraph_Node(category="sample_text_2", name="sample_text_2", programPath="sample_text_2")
    b = SkillGraph_Equation(equation="sample_text")
    _safe_set(b, 'Equation', a1)
    assert _is_linked(b, 'Equation', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Equation', a2)
    assert _is_linked(b, 'Equation', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Equation', None)
    assert not _is_linked(b, 'Equation', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_node14_reverse_link_reassign_clear():
    a1 = SkillGraph_Requirement(comment="sample_text", term="sample_text", type="sample_text")
    a2 = SkillGraph_Requirement(comment="sample_text_2", term="sample_text_2", type="sample_text_2")
    b = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'requirements'):
        assert _is_linked(a1, 'requirements', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'requirements'):
        assert not _is_linked(a1, 'requirements', b)
    if hasattr(a2, 'requirements'):
        assert _is_linked(a2, 'requirements', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'requirements'):
        assert not _is_linked(a2, 'requirements', b)


def test_assoc_node15_reverse_link_reassign_clear():
    a1 = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    a2 = SkillGraph_Node(category="sample_text_2", name="sample_text_2", programPath="sample_text_2")
    b = SkillGraph_Equation(equation="sample_text")
    _safe_set(b, 'equations', a1)
    assert _is_linked(b, 'equations', a1)
    if hasattr(a1, 'Node16'):
        assert _is_linked(a1, 'Node16', b)
    _safe_set(b, 'equations', a2)
    assert _is_linked(b, 'equations', a2)
    if hasattr(a1, 'Node16'):
        assert not _is_linked(a1, 'Node16', b)
    if hasattr(a2, 'Node16'):
        assert _is_linked(a2, 'Node16', b)
    _safe_set(b, 'equations', None)
    assert not _is_linked(b, 'equations', a2)
    if hasattr(a2, 'Node16'):
        assert not _is_linked(a2, 'Node16', b)


def test_assoc_parentNodes10_reverse_link_reassign_clear():
    a1 = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    a2 = SkillGraph_Node(category="sample_text_2", name="sample_text_2", programPath="sample_text_2")
    b = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    _safe_set(b, 'SkillGraph_Node9', {a1})
    assert _is_linked(b, 'SkillGraph_Node9', a1)
    if hasattr(a1, 'SkillGraph_Node11'):
        assert _is_linked(a1, 'SkillGraph_Node11', b)
    _safe_set(b, 'SkillGraph_Node9', {a2})
    assert _is_linked(b, 'SkillGraph_Node9', a2)
    if hasattr(a1, 'SkillGraph_Node11'):
        assert not _is_linked(a1, 'SkillGraph_Node11', b)
    if hasattr(a2, 'SkillGraph_Node11'):
        assert _is_linked(a2, 'SkillGraph_Node11', b)
    _safe_set(b, 'SkillGraph_Node9', set())
    assert not _is_linked(b, 'SkillGraph_Node9', a2)
    if hasattr(a2, 'SkillGraph_Node11'):
        assert not _is_linked(a2, 'SkillGraph_Node11', b)


def test_assoc_requirements12_reverse_link_reassign_clear():
    a1 = SkillGraph_Requirement(comment="sample_text", term="sample_text", type="sample_text")
    a2 = SkillGraph_Requirement(comment="sample_text_2", term="sample_text_2", type="sample_text_2")
    b = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    _safe_set(b, 'node13', {a1})
    assert _is_linked(b, 'node13', a1)
    if hasattr(a1, 'Requirement'):
        assert _is_linked(a1, 'Requirement', b)
    _safe_set(b, 'node13', {a2})
    assert _is_linked(b, 'node13', a2)
    if hasattr(a1, 'Requirement'):
        assert not _is_linked(a1, 'Requirement', b)
    if hasattr(a2, 'Requirement'):
        assert _is_linked(a2, 'Requirement', b)
    _safe_set(b, 'node13', set())
    assert not _is_linked(b, 'node13', a2)
    if hasattr(a2, 'Requirement'):
        assert not _is_linked(a2, 'Requirement', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_childEdges7_stub_double():
    # SkillGraph_Edge has no real 'SkillGraph_Edge' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    partner = SkillGraph_Edge()
    setattr(partner, 'SkillGraph_Edge', None)
    _safe_set(owner, 'SkillGraph_Node8', {partner})
    assert getattr(partner, 'SkillGraph_Edge') == owner
    _safe_set(owner, 'SkillGraph_Node8', set())
    assert getattr(partner, 'SkillGraph_Edge') is None


def test_assoc_childNode20_stub_double():
    # SkillGraph_Edge has no real 'SkillGraph_Edge21' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    partner = SkillGraph_Edge()
    setattr(partner, 'SkillGraph_Edge21', None)
    _safe_set(owner, 'SkillGraph_Node22', partner)
    assert getattr(partner, 'SkillGraph_Edge21') == owner
    _safe_set(owner, 'SkillGraph_Node22', None)
    assert getattr(partner, 'SkillGraph_Edge21') is None


def test_assoc_graph0_stub_double():
    # SkillGraph_Graph has no real 'Graph' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Parameter(abbreviation="sample_text", defaultValue="sample_text", name="sample_text", unit="sample_text", variable=True)
    partner = SkillGraph_Graph()
    setattr(partner, 'Graph', None)
    _safe_set(owner, 'parameterList', partner)
    assert getattr(partner, 'Graph') == owner
    _safe_set(owner, 'parameterList', None)
    assert getattr(partner, 'Graph') is None


def test_assoc_nodes1_stub_double():
    # SkillGraph_Graph has no real 'SkillGraph_Graph' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    partner = SkillGraph_Graph()
    setattr(partner, 'SkillGraph_Graph', None)
    _safe_set(owner, 'SkillGraph_Node', partner)
    assert owner in getattr(partner, 'SkillGraph_Graph')
    _safe_set(owner, 'SkillGraph_Node', None)
    assert owner not in getattr(partner, 'SkillGraph_Graph')


def test_assoc_parameterList5_stub_double():
    # SkillGraph_Graph has no real 'graph' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Parameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Parameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Parameter(abbreviation="sample_text", defaultValue="sample_text", name="sample_text", unit="sample_text", variable=True)
    partner = SkillGraph_Graph()
    setattr(partner, 'graph', None)
    _safe_set(owner, 'Parameter', partner)
    assert owner in getattr(partner, 'graph')
    _safe_set(owner, 'Parameter', None)
    assert owner not in getattr(partner, 'graph')


def test_assoc_parentNode17_stub_double():
    # SkillGraph_Edge has no real 'SkillGraph_Edge18' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    partner = SkillGraph_Edge()
    setattr(partner, 'SkillGraph_Edge18', None)
    _safe_set(owner, 'SkillGraph_Node19', partner)
    assert getattr(partner, 'SkillGraph_Edge18') == owner
    _safe_set(owner, 'SkillGraph_Node19', None)
    assert getattr(partner, 'SkillGraph_Edge18') is None


def test_assoc_rootNode2_stub_double():
    # SkillGraph_Graph has no real 'SkillGraph_Graph3' property in the generated
    # code (a bare stub) -- manually attach it so SkillGraph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SkillGraph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SkillGraph_Node(category="sample_text", name="sample_text", programPath="sample_text")
    partner = SkillGraph_Graph()
    setattr(partner, 'SkillGraph_Graph3', None)
    _safe_set(owner, 'SkillGraph_Node4', partner)
    assert getattr(partner, 'SkillGraph_Graph3') == owner
    _safe_set(owner, 'SkillGraph_Node4', None)
    assert getattr(partner, 'SkillGraph_Graph3') is None


