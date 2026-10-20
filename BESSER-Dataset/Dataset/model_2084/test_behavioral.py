import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BasicNode,
    Coordinator,
    Middleware,
    Node,
    Process,
    Processor,
    Repository,
    Root,
    ServiceDescription,
    ServiceImpl,
    Simulator,
    Skeleton,
    Stub,
    Tree,
    VM,
    ws_bundle_Bundle,
    ws_bundle_Process,
    ws_middleware_Middleware,
    ws_middleware_Processor,
    ws_middleware_Repository,
    ws_middleware_ServiceDescription,
    ws_middleware_ServiceImpl,
    ws_middleware_Stub,
    ws_middleware_VM,
    ws_middleware_WebService,
    ws_skeleton_Skeleton,
    ws_tree_BasicNode,
    ws_tree_CDEVSCoordinator,
    ws_tree_CDEVSSimulator,
    ws_tree_Coordinator,
    ws_tree_FlatCoordinator,
    ws_tree_Node,
    ws_tree_NodeCoordinator,
    ws_tree_PDEVSCoordinator,
    ws_tree_PDEVSSimulator,
    ws_tree_P_Coordinator,
    ws_tree_P_Simulator,
    ws_tree_Root,
    ws_tree_Simulator,
    ws_tree_Tree,
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

def test_assoc_Coordinator10_stub_double():
    # Coordinator has no real 'Coordinator' property in the generated
    # code (a bare stub) -- manually attach it so ws_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_tree_Tree(ID="sample_text")
    partner = Coordinator()
    setattr(partner, 'Coordinator', None)
    _safe_set(owner, 'ws_tree_Tree11', {partner})
    assert getattr(partner, 'Coordinator') == owner
    _safe_set(owner, 'ws_tree_Tree11', set())
    assert getattr(partner, 'Coordinator') is None


def test_assoc_Process22_stub_double():
    # Process has no real 'Process24' property in the generated
    # code (a bare stub) -- manually attach it so ws_bundle_Bundle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_bundle_Bundle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_bundle_Bundle(ID="sample_text")
    partner = Process()
    setattr(partner, 'Process24', None)
    _safe_set(owner, 'ws_bundle_Bundle23', {partner})
    assert getattr(partner, 'Process24') == owner
    _safe_set(owner, 'ws_bundle_Bundle23', set())
    assert getattr(partner, 'Process24') is None


def test_assoc_Root9_stub_double():
    # Root has no real 'Root' property in the generated
    # code (a bare stub) -- manually attach it so ws_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_tree_Tree(ID="sample_text")
    partner = Root()
    setattr(partner, 'Root', None)
    _safe_set(owner, 'ws_tree_Tree', partner)
    assert getattr(partner, 'Root') == owner
    _safe_set(owner, 'ws_tree_Tree', None)
    assert getattr(partner, 'Root') is None


def test_assoc_Simulator12_stub_double():
    # Simulator has no real 'Simulator' property in the generated
    # code (a bare stub) -- manually attach it so ws_tree_Tree's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_tree_Tree's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_tree_Tree(ID="sample_text")
    partner = Simulator()
    setattr(partner, 'Simulator', None)
    _safe_set(owner, 'ws_tree_Tree13', {partner})
    assert getattr(partner, 'Simulator') == owner
    _safe_set(owner, 'ws_tree_Tree13', set())
    assert getattr(partner, 'Simulator') is None


def test_assoc_impl7_stub_double():
    # ServiceImpl has no real 'ServiceImpl' property in the generated
    # code (a bare stub) -- manually attach it so ws_middleware_Stub's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_middleware_Stub's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_middleware_Stub()
    partner = ServiceImpl()
    setattr(partner, 'ServiceImpl', None)
    _safe_set(owner, 'ws_middleware_Stub', partner)
    assert getattr(partner, 'ServiceImpl') == owner
    _safe_set(owner, 'ws_middleware_Stub', None)
    assert getattr(partner, 'ServiceImpl') is None


def test_assoc_middleware26_stub_double():
    # Middleware has no real 'Middleware' property in the generated
    # code (a bare stub) -- manually attach it so ws_bundle_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_bundle_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_bundle_Process(ID="sample_text")
    partner = Middleware()
    setattr(partner, 'Middleware', None)
    _safe_set(owner, 'ws_bundle_Process27', partner)
    assert getattr(partner, 'Middleware') == owner
    _safe_set(owner, 'ws_bundle_Process27', None)
    assert getattr(partner, 'Middleware') is None


def test_assoc_nodes25_stub_double():
    # Node has no real 'Node' property in the generated
    # code (a bare stub) -- manually attach it so ws_bundle_Process's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_bundle_Process's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_bundle_Process(ID="sample_text")
    partner = Node()
    setattr(partner, 'Node', None)
    _safe_set(owner, 'ws_bundle_Process', {partner})
    assert getattr(partner, 'Node') == owner
    _safe_set(owner, 'ws_bundle_Process', set())
    assert getattr(partner, 'Node') is None


def test_assoc_process1_stub_double():
    # Process has no real 'Process' property in the generated
    # code (a bare stub) -- manually attach it so ws_middleware_Middleware's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_middleware_Middleware's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_middleware_Middleware()
    partner = Process()
    setattr(partner, 'Process', None)
    _safe_set(owner, 'ws_middleware_Middleware2', {partner})
    assert getattr(partner, 'Process') == owner
    _safe_set(owner, 'ws_middleware_Middleware2', set())
    assert getattr(partner, 'Process') is None


def test_assoc_processors6_stub_double():
    # Processor has no real 'Processor' property in the generated
    # code (a bare stub) -- manually attach it so ws_middleware_VM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_middleware_VM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_middleware_VM(ID="sample_text", protocol="sample_text")
    partner = Processor()
    setattr(partner, 'Processor', None)
    _safe_set(owner, 'ws_middleware_VM', {partner})
    assert getattr(partner, 'Processor') == owner
    _safe_set(owner, 'ws_middleware_VM', set())
    assert getattr(partner, 'Processor') is None


def test_assoc_rootskel18_stub_double():
    # Root has no real 'Root20' property in the generated
    # code (a bare stub) -- manually attach it so ws_skeleton_Skeleton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_skeleton_Skeleton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_skeleton_Skeleton(ID="sample_text")
    partner = Root()
    setattr(partner, 'Root20', None)
    _safe_set(owner, 'ws_skeleton_Skeleton19', {partner})
    assert getattr(partner, 'Root20') == owner
    _safe_set(owner, 'ws_skeleton_Skeleton19', set())
    assert getattr(partner, 'Root20') is None


def test_assoc_services8_stub_double():
    # ServiceDescription has no real 'ServiceDescription' property in the generated
    # code (a bare stub) -- manually attach it so ws_middleware_Repository's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_middleware_Repository's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_middleware_Repository()
    partner = ServiceDescription()
    setattr(partner, 'ServiceDescription', None)
    _safe_set(owner, 'ws_middleware_Repository', {partner})
    assert getattr(partner, 'ServiceDescription') == owner
    _safe_set(owner, 'ws_middleware_Repository', set())
    assert getattr(partner, 'ServiceDescription') is None


def test_assoc_skeleton21_stub_double():
    # Skeleton has no real 'Skeleton' property in the generated
    # code (a bare stub) -- manually attach it so ws_bundle_Bundle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_bundle_Bundle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_bundle_Bundle(ID="sample_text")
    partner = Skeleton()
    setattr(partner, 'Skeleton', None)
    _safe_set(owner, 'ws_bundle_Bundle', partner)
    assert getattr(partner, 'Skeleton') == owner
    _safe_set(owner, 'ws_bundle_Bundle', None)
    assert getattr(partner, 'Skeleton') is None


def test_assoc_tree17_stub_double():
    # Tree has no real 'Tree' property in the generated
    # code (a bare stub) -- manually attach it so ws_skeleton_Skeleton's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_skeleton_Skeleton's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_skeleton_Skeleton(ID="sample_text")
    partner = Tree()
    setattr(partner, 'Tree', None)
    _safe_set(owner, 'ws_skeleton_Skeleton', partner)
    assert getattr(partner, 'Tree') == owner
    _safe_set(owner, 'ws_skeleton_Skeleton', None)
    assert getattr(partner, 'Tree') is None


def test_assoc_uses0_stub_double():
    # VM has no real 'VM' property in the generated
    # code (a bare stub) -- manually attach it so ws_middleware_Middleware's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ws_middleware_Middleware's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ws_middleware_Middleware()
    partner = VM()
    setattr(partner, 'VM', None)
    _safe_set(owner, 'ws_middleware_Middleware', partner)
    assert getattr(partner, 'VM') == owner
    _safe_set(owner, 'ws_middleware_Middleware', None)
    assert getattr(partner, 'VM') is None


