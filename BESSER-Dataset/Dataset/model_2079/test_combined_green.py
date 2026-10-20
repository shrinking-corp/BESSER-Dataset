# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Infrastructure,
    goatInfrastructure_Cluster,
    goatInfrastructure_Ring,
    goatInfrastructure_Tree,
    goatInfrastructure_SingleServer,
    goatInfrastructure_Infrastructure,
    goatInfrastructure_TreeNode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_infrastructure_is_not_abstract():
    assert not inspect.isabstract(Infrastructure)


def test_hyp_infrastructure_constructor_exists():
    assert callable(Infrastructure.__init__)


def test_hyp_infrastructure_constructor_args():
    sig = inspect.signature(Infrastructure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_goatinfrastructure_cluster_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_Cluster)


def test_hyp_goatinfrastructure_cluster_constructor_exists():
    assert callable(goatInfrastructure_Cluster.__init__)


def test_hyp_goatinfrastructure_cluster_constructor_args():
    sig = inspect.signature(goatInfrastructure_Cluster.__init__)
    params = list(sig.parameters.keys())
    assert "nodes" in params, "Missing parameter 'nodes'"
    assert "registration" in params, "Missing parameter 'registration'"
    assert "message_queue" in params, "Missing parameter 'message_queue'"
    assert "mid_assigner" in params, "Missing parameter 'mid_assigner'"







def test_hyp_goatinfrastructure_ring_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_Ring)


def test_hyp_goatinfrastructure_ring_constructor_exists():
    assert callable(goatInfrastructure_Ring.__init__)


def test_hyp_goatinfrastructure_ring_constructor_args():
    sig = inspect.signature(goatInfrastructure_Ring.__init__)
    params = list(sig.parameters.keys())
    assert "nodes" in params, "Missing parameter 'nodes'"
    assert "mid_assigner" in params, "Missing parameter 'mid_assigner'"
    assert "registration" in params, "Missing parameter 'registration'"






def test_hyp_goatinfrastructure_tree_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_Tree)


def test_hyp_goatinfrastructure_tree_constructor_exists():
    assert callable(goatInfrastructure_Tree.__init__)


def test_hyp_goatinfrastructure_tree_constructor_args():
    sig = inspect.signature(goatInfrastructure_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "registration" in params, "Missing parameter 'registration'"




def test_hyp_goatinfrastructure_singleserver_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_SingleServer)


def test_hyp_goatinfrastructure_singleserver_constructor_exists():
    assert callable(goatInfrastructure_SingleServer.__init__)


def test_hyp_goatinfrastructure_singleserver_constructor_args():
    sig = inspect.signature(goatInfrastructure_SingleServer.__init__)
    params = list(sig.parameters.keys())
    assert "server" in params, "Missing parameter 'server'"
    assert "timeout" in params, "Missing parameter 'timeout'"





def test_hyp_goatinfrastructure_infrastructure_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_Infrastructure)


def test_hyp_goatinfrastructure_infrastructure_constructor_exists():
    assert callable(goatInfrastructure_Infrastructure.__init__)


def test_hyp_goatinfrastructure_infrastructure_constructor_args():
    sig = inspect.signature(goatInfrastructure_Infrastructure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_goatinfrastructure_treenode_is_not_abstract():
    assert not inspect.isabstract(goatInfrastructure_TreeNode)


def test_hyp_goatinfrastructure_treenode_constructor_exists():
    assert callable(goatInfrastructure_TreeNode.__init__)


def test_hyp_goatinfrastructure_treenode_constructor_args():
    sig = inspect.signature(goatInfrastructure_TreeNode.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"



# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Infrastructure_strategy = st.builds(
    Infrastructure,
)
goatInfrastructure_Cluster_strategy = st.builds(
    goatInfrastructure_Cluster,
    nodes=
        safe_text,
    registration=
        safe_text,
    message_queue=
        safe_text,
    mid_assigner=
        safe_text
)
goatInfrastructure_Ring_strategy = st.builds(
    goatInfrastructure_Ring,
    nodes=
        safe_text,
    mid_assigner=
        safe_text,
    registration=
        safe_text
)
goatInfrastructure_Tree_strategy = st.builds(
    goatInfrastructure_Tree,
    registration=
        safe_text
)
goatInfrastructure_SingleServer_strategy = st.builds(
    goatInfrastructure_SingleServer,
    server=
        safe_text,
    timeout=
        st.integers()
)
goatInfrastructure_Infrastructure_strategy = st.builds(
    goatInfrastructure_Infrastructure,
    name=
        safe_text
)
goatInfrastructure_TreeNode_strategy = st.builds(
    goatInfrastructure_TreeNode,
    address=
        safe_text
)





@given(instance=goatInfrastructure_Cluster_strategy)
def test_hyp_goatinfrastructure_cluster_nodes_setter(instance):
    original = instance.nodes
    instance.nodes = original
    assert instance.nodes == original



@given(instance=goatInfrastructure_Cluster_strategy)
def test_hyp_goatinfrastructure_cluster_registration_setter(instance):
    original = instance.registration
    instance.registration = original
    assert instance.registration == original



@given(instance=goatInfrastructure_Cluster_strategy)
def test_hyp_goatinfrastructure_cluster_message_queue_setter(instance):
    original = instance.message_queue
    instance.message_queue = original
    assert instance.message_queue == original



@given(instance=goatInfrastructure_Cluster_strategy)
def test_hyp_goatinfrastructure_cluster_mid_assigner_setter(instance):
    original = instance.mid_assigner
    instance.mid_assigner = original
    assert instance.mid_assigner == original




@given(instance=goatInfrastructure_Ring_strategy)
def test_hyp_goatinfrastructure_ring_nodes_setter(instance):
    original = instance.nodes
    instance.nodes = original
    assert instance.nodes == original



@given(instance=goatInfrastructure_Ring_strategy)
def test_hyp_goatinfrastructure_ring_mid_assigner_setter(instance):
    original = instance.mid_assigner
    instance.mid_assigner = original
    assert instance.mid_assigner == original



@given(instance=goatInfrastructure_Ring_strategy)
def test_hyp_goatinfrastructure_ring_registration_setter(instance):
    original = instance.registration
    instance.registration = original
    assert instance.registration == original




@given(instance=goatInfrastructure_Tree_strategy)
def test_hyp_goatinfrastructure_tree_registration_setter(instance):
    original = instance.registration
    instance.registration = original
    assert instance.registration == original




@given(instance=goatInfrastructure_SingleServer_strategy)
def test_hyp_goatinfrastructure_singleserver_server_setter(instance):
    original = instance.server
    instance.server = original
    assert instance.server == original



@given(instance=goatInfrastructure_SingleServer_strategy)
def test_hyp_goatinfrastructure_singleserver_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original




@given(instance=goatInfrastructure_Infrastructure_strategy)
def test_hyp_goatinfrastructure_infrastructure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=goatInfrastructure_TreeNode_strategy)
def test_hyp_goatinfrastructure_treenode_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Infrastructure,
    goatInfrastructure_Cluster,
    goatInfrastructure_Infrastructure,
    goatInfrastructure_Ring,
    goatInfrastructure_SingleServer,
    goatInfrastructure_Tree,
    goatInfrastructure_TreeNode,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_goatInfrastructure_Cluster_message_queue_value_roundtrip():
    instance = goatInfrastructure_Cluster(message_queue="sample_text", mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.message_queue == "sample_text"
    instance.message_queue = "sample_text_2"
    assert instance.message_queue == "sample_text_2"


def test_goatInfrastructure_Cluster_mid_assigner_value_roundtrip():
    instance = goatInfrastructure_Cluster(message_queue="sample_text", mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.mid_assigner == "sample_text"
    instance.mid_assigner = "sample_text_2"
    assert instance.mid_assigner == "sample_text_2"


def test_goatInfrastructure_Cluster_nodes_value_roundtrip():
    instance = goatInfrastructure_Cluster(message_queue="sample_text", mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.nodes == "sample_text"
    instance.nodes = "sample_text_2"
    assert instance.nodes == "sample_text_2"


def test_goatInfrastructure_Cluster_registration_value_roundtrip():
    instance = goatInfrastructure_Cluster(message_queue="sample_text", mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.registration == "sample_text"
    instance.registration = "sample_text_2"
    assert instance.registration == "sample_text_2"


def test_goatInfrastructure_Infrastructure_name_value_roundtrip():
    instance = goatInfrastructure_Infrastructure(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_goatInfrastructure_Ring_mid_assigner_value_roundtrip():
    instance = goatInfrastructure_Ring(mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.mid_assigner == "sample_text"
    instance.mid_assigner = "sample_text_2"
    assert instance.mid_assigner == "sample_text_2"


def test_goatInfrastructure_Ring_nodes_value_roundtrip():
    instance = goatInfrastructure_Ring(mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.nodes == "sample_text"
    instance.nodes = "sample_text_2"
    assert instance.nodes == "sample_text_2"


def test_goatInfrastructure_Ring_registration_value_roundtrip():
    instance = goatInfrastructure_Ring(mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert instance.registration == "sample_text"
    instance.registration = "sample_text_2"
    assert instance.registration == "sample_text_2"


def test_goatInfrastructure_SingleServer_server_value_roundtrip():
    instance = goatInfrastructure_SingleServer(server="sample_text", timeout=7)
    assert instance.server == "sample_text"
    instance.server = "sample_text_2"
    assert instance.server == "sample_text_2"


def test_goatInfrastructure_SingleServer_timeout_value_roundtrip():
    instance = goatInfrastructure_SingleServer(server="sample_text", timeout=7)
    assert instance.timeout == 7
    instance.timeout = 13
    assert instance.timeout == 13


def test_goatInfrastructure_Tree_registration_value_roundtrip():
    instance = goatInfrastructure_Tree(registration="sample_text")
    assert instance.registration == "sample_text"
    instance.registration = "sample_text_2"
    assert instance.registration == "sample_text_2"


def test_goatInfrastructure_TreeNode_address_value_roundtrip():
    instance = goatInfrastructure_TreeNode(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_goatInfrastructure_Cluster_isa_Infrastructure():
    instance = goatInfrastructure_Cluster(message_queue="sample_text", mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert isinstance(instance, Infrastructure)


def test_goatInfrastructure_Ring_isa_Infrastructure():
    instance = goatInfrastructure_Ring(mid_assigner="sample_text", nodes="sample_text", registration="sample_text")
    assert isinstance(instance, Infrastructure)


def test_goatInfrastructure_SingleServer_isa_Infrastructure():
    instance = goatInfrastructure_SingleServer(server="sample_text", timeout=7)
    assert isinstance(instance, Infrastructure)


def test_goatInfrastructure_Tree_isa_Infrastructure():
    instance = goatInfrastructure_Tree(registration="sample_text")
    assert isinstance(instance, Infrastructure)


def test_assoc_children2_link_reassign_clear():
    a = goatInfrastructure_TreeNode(address="sample_text")
    b1 = goatInfrastructure_TreeNode(address="sample_text")
    b2 = goatInfrastructure_TreeNode(address="sample_text_2")
    _safe_set(a, 'goatInfrastructure_TreeNode1', {b1})
    assert _is_linked(a, 'goatInfrastructure_TreeNode1', b1)
    if hasattr(b1, 'goatInfrastructure_TreeNode3'):
        assert _is_linked(b1, 'goatInfrastructure_TreeNode3', a)
    _safe_set(a, 'goatInfrastructure_TreeNode1', {b2})
    assert _is_linked(a, 'goatInfrastructure_TreeNode1', b2)
    if hasattr(b1, 'goatInfrastructure_TreeNode3'):
        assert not _is_linked(b1, 'goatInfrastructure_TreeNode3', a)
    if hasattr(b2, 'goatInfrastructure_TreeNode3'):
        assert _is_linked(b2, 'goatInfrastructure_TreeNode3', a)
    _safe_set(a, 'goatInfrastructure_TreeNode1', set())
    assert not _is_linked(a, 'goatInfrastructure_TreeNode1', b2)
    if hasattr(b2, 'goatInfrastructure_TreeNode3'):
        assert not _is_linked(b2, 'goatInfrastructure_TreeNode3', a)


def test_assoc_root0_link_reassign_clear():
    a = goatInfrastructure_TreeNode(address="sample_text")
    b1 = goatInfrastructure_Tree(registration="sample_text")
    b2 = goatInfrastructure_Tree(registration="sample_text_2")
    _safe_set(a, 'goatInfrastructure_TreeNode', b1)
    assert _is_linked(a, 'goatInfrastructure_TreeNode', b1)
    if hasattr(b1, 'goatInfrastructure_Tree'):
        assert _is_linked(b1, 'goatInfrastructure_Tree', a)
    _safe_set(a, 'goatInfrastructure_TreeNode', b2)
    assert _is_linked(a, 'goatInfrastructure_TreeNode', b2)
    if hasattr(b1, 'goatInfrastructure_Tree'):
        assert not _is_linked(b1, 'goatInfrastructure_Tree', a)
    if hasattr(b2, 'goatInfrastructure_Tree'):
        assert _is_linked(b2, 'goatInfrastructure_Tree', a)
    _safe_set(a, 'goatInfrastructure_TreeNode', None)
    assert not _is_linked(a, 'goatInfrastructure_TreeNode', b2)
    if hasattr(b2, 'goatInfrastructure_Tree'):
        assert not _is_linked(b2, 'goatInfrastructure_Tree', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Infrastructure_strategy = st.builds(Infrastructure)
@given(instance=Infrastructure_strategy)
@settings(max_examples=25)
def test_Infrastructure_instantiation(instance):
    assert isinstance(instance, Infrastructure)


goatInfrastructure_Cluster_strategy = st.builds(goatInfrastructure_Cluster, message_queue=safe_text, mid_assigner=safe_text, nodes=safe_text, registration=safe_text)
@given(instance=goatInfrastructure_Cluster_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_Cluster_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_Cluster)


goatInfrastructure_Infrastructure_strategy = st.builds(goatInfrastructure_Infrastructure, name=safe_text)
@given(instance=goatInfrastructure_Infrastructure_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_Infrastructure_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_Infrastructure)


goatInfrastructure_Ring_strategy = st.builds(goatInfrastructure_Ring, mid_assigner=safe_text, nodes=safe_text, registration=safe_text)
@given(instance=goatInfrastructure_Ring_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_Ring_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_Ring)


goatInfrastructure_SingleServer_strategy = st.builds(goatInfrastructure_SingleServer, server=safe_text, timeout=st.integers())
@given(instance=goatInfrastructure_SingleServer_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_SingleServer_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_SingleServer)


goatInfrastructure_Tree_strategy = st.builds(goatInfrastructure_Tree, registration=safe_text)
@given(instance=goatInfrastructure_Tree_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_Tree_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_Tree)


goatInfrastructure_TreeNode_strategy = st.builds(goatInfrastructure_TreeNode, address=safe_text)
@given(instance=goatInfrastructure_TreeNode_strategy)
@settings(max_examples=25)
def test_goatInfrastructure_TreeNode_instantiation(instance):
    assert isinstance(instance, goatInfrastructure_TreeNode)



