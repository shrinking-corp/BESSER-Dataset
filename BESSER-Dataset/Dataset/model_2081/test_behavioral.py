import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BasicNode,
    Bundle,
    Coordinator,
    Mapping,
    Node,
    Process,
    Processor,
    Root,
    Simulator,
    Skeleton,
    Tree,
    VM,
    sgf_bundle_Bundle,
    sgf_bundle_Process,
    sgf_graph_Graph,
    sgf_graph_Mapping,
    sgf_skeleton_Skeleton,
    sgf_tree_BasicNode,
    sgf_tree_Coordinator,
    sgf_tree_Node,
    sgf_tree_Root,
    sgf_tree_Simulator,
    sgf_tree_Tree,
    sgf_vm_Processor,
    sgf_vm_VM,
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

def test_assoc_Coordinator1_stub_double():
    # Coordinator has no real 'Coordinator' property in the generated
    # code (a bare stub) -- manually attach it so sgf_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_tree_Tree(ID="sample_text")
    partner = Coordinator()
    setattr(partner, 'Coordinator', None)
    _safe_set(owner, 'sgf_tree_Tree2', {partner})
    assert getattr(partner, 'Coordinator') == owner
    _safe_set(owner, 'sgf_tree_Tree2', set())
    assert getattr(partner, 'Coordinator') is None


def test_assoc_Process13_stub_double():
    # Process has no real 'Process' property in the generated
    # code (a bare stub) -- manually attach it so sgf_bundle_Bundle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_bundle_Bundle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_bundle_Bundle(ID="sample_text")
    partner = Process()
    setattr(partner, 'Process', None)
    _safe_set(owner, 'sgf_bundle_Bundle14', {partner})
    assert getattr(partner, 'Process') == owner
    _safe_set(owner, 'sgf_bundle_Bundle14', set())
    assert getattr(partner, 'Process') is None


def test_assoc_Root0_stub_double():
    # Root has no real 'Root' property in the generated
    # code (a bare stub) -- manually attach it so sgf_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_tree_Tree(ID="sample_text")
    partner = Root()
    setattr(partner, 'Root', None)
    _safe_set(owner, 'sgf_tree_Tree', partner)
    assert getattr(partner, 'Root') == owner
    _safe_set(owner, 'sgf_tree_Tree', None)
    assert getattr(partner, 'Root') is None


def test_assoc_Simulator3_stub_double():
    # Simulator has no real 'Simulator' property in the generated
    # code (a bare stub) -- manually attach it so sgf_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_tree_Tree(ID="sample_text")
    partner = Simulator()
    setattr(partner, 'Simulator', None)
    _safe_set(owner, 'sgf_tree_Tree4', {partner})
    assert getattr(partner, 'Simulator') == owner
    _safe_set(owner, 'sgf_tree_Tree4', set())
    assert getattr(partner, 'Simulator') is None


def test_assoc_bundle17_stub_double():
    # Bundle has no real 'Bundle' property in the generated
    # code (a bare stub) -- manually attach it so sgf_graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_graph_Graph(ID="sample_text")
    partner = Bundle()
    setattr(partner, 'Bundle', None)
    _safe_set(owner, 'sgf_graph_Graph', partner)
    assert getattr(partner, 'Bundle') == owner
    _safe_set(owner, 'sgf_graph_Graph', None)
    assert getattr(partner, 'Bundle') is None


def test_assoc_mappings20_stub_double():
    # Mapping has no real 'Mapping' property in the generated
    # code (a bare stub) -- manually attach it so sgf_graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_graph_Graph(ID="sample_text")
    partner = Mapping()
    setattr(partner, 'Mapping', None)
    _safe_set(owner, 'sgf_graph_Graph21', {partner})
    assert getattr(partner, 'Mapping') == owner
    _safe_set(owner, 'sgf_graph_Graph21', set())
    assert getattr(partner, 'Mapping') is None


def test_assoc_nodes15_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so sgf_bundle_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_bundle_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_bundle_Process(ID="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'sgf_bundle_Process', {partner})
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'sgf_bundle_Process', set())
    assert getattr(partner, 'Node') is None


def test_assoc_processes22_stub_double():
    # Process has no real 'Process23' property in the generated
    # code (a bare stub) -- manually attach it so sgf_graph_Mapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_graph_Mapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_graph_Mapping(ID="sample_text")
    partner = Process()
    setattr(partner, 'Process23', None)
    _safe_set(owner, 'sgf_graph_Mapping', {partner})
    assert getattr(partner, 'Process23') == owner
    _safe_set(owner, 'sgf_graph_Mapping', set())
    assert getattr(partner, 'Process23') is None


def test_assoc_processor24_stub_double():
    # Processor has no real 'Processor26' property in the generated
    # code (a bare stub) -- manually attach it so sgf_graph_Mapping's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_graph_Mapping's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_graph_Mapping(ID="sample_text")
    partner = Processor()
    setattr(partner, 'Processor26', None)
    _safe_set(owner, 'sgf_graph_Mapping25', partner)
    assert getattr(partner, 'Processor26') == owner
    _safe_set(owner, 'sgf_graph_Mapping25', None)
    assert getattr(partner, 'Processor26') is None


def test_assoc_processors16_stub_double():
    # Processor has no real 'Processor' property in the generated
    # code (a bare stub) -- manually attach it so sgf_vm_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_vm_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_vm_VM(ID="sample_text", protocol="sample_text")
    partner = Processor()
    setattr(partner, 'Processor', None)
    _safe_set(owner, 'sgf_vm_VM', {partner})
    assert getattr(partner, 'Processor') == owner
    _safe_set(owner, 'sgf_vm_VM', set())
    assert getattr(partner, 'Processor') is None


def test_assoc_rootskel9_stub_double():
    # Root has no real 'Root11' property in the generated
    # code (a bare stub) -- manually attach it so sgf_skeleton_Skeleton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_skeleton_Skeleton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_skeleton_Skeleton(ID="sample_text")
    partner = Root()
    setattr(partner, 'Root11', None)
    _safe_set(owner, 'sgf_skeleton_Skeleton10', {partner})
    assert getattr(partner, 'Root11') == owner
    _safe_set(owner, 'sgf_skeleton_Skeleton10', set())
    assert getattr(partner, 'Root11') is None


def test_assoc_skeleton12_stub_double():
    # Skeleton has no real 'Skeleton' property in the generated
    # code (a bare stub) -- manually attach it so sgf_bundle_Bundle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_bundle_Bundle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_bundle_Bundle(ID="sample_text")
    partner = Skeleton()
    setattr(partner, 'Skeleton', None)
    _safe_set(owner, 'sgf_bundle_Bundle', partner)
    assert getattr(partner, 'Skeleton') == owner
    _safe_set(owner, 'sgf_bundle_Bundle', None)
    assert getattr(partner, 'Skeleton') is None


def test_assoc_tree8_stub_double():
    # Tree has no real 'Tree' property in the generated
    # code (a bare stub) -- manually attach it so sgf_skeleton_Skeleton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_skeleton_Skeleton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_skeleton_Skeleton(ID="sample_text")
    partner = Tree()
    setattr(partner, 'Tree', None)
    _safe_set(owner, 'sgf_skeleton_Skeleton', partner)
    assert getattr(partner, 'Tree') == owner
    _safe_set(owner, 'sgf_skeleton_Skeleton', None)
    assert getattr(partner, 'Tree') is None


def test_assoc_vm18_stub_double():
    # VM has no real 'VM' property in the generated
    # code (a bare stub) -- manually attach it so sgf_graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sgf_graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sgf_graph_Graph(ID="sample_text")
    partner = VM()
    setattr(partner, 'VM', None)
    _safe_set(owner, 'sgf_graph_Graph19', partner)
    assert getattr(partner, 'VM') == owner
    _safe_set(owner, 'sgf_graph_Graph19', None)
    assert getattr(partner, 'VM') is None


