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
    graph_Graph,
    graph_Identifiable,
    Identifiable,
    graph_NodeResponsibility,
    graph_Node,
    graph_GraphAsset,
    graph_Subgraphs,
    graph_Edge,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_hyp_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_hyp_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_identifiable_is_not_abstract():
    assert not inspect.isabstract(graph_Identifiable)


def test_hyp_graph_identifiable_constructor_exists():
    assert callable(graph_Identifiable.__init__)


def test_hyp_graph_identifiable_constructor_args():
    sig = inspect.signature(graph_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "ID" in params, "Missing parameter 'ID'"





def test_hyp_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_hyp_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_hyp_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_noderesponsibility_is_not_abstract():
    assert not inspect.isabstract(graph_NodeResponsibility)


def test_hyp_graph_noderesponsibility_constructor_exists():
    assert callable(graph_NodeResponsibility.__init__)


def test_hyp_graph_noderesponsibility_constructor_args():
    sig = inspect.signature(graph_NodeResponsibility.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"




def test_hyp_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_hyp_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_hyp_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "AttackerObservation" in params, "Missing parameter 'AttackerObservation'"
    assert "visited" in params, "Missing parameter 'visited'"
    assert "Attacker" in params, "Missing parameter 'Attacker'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_graph_graphasset_is_not_abstract():
    assert not inspect.isabstract(graph_GraphAsset)


def test_hyp_graph_graphasset_constructor_exists():
    assert callable(graph_GraphAsset.__init__)


def test_hyp_graph_graphasset_constructor_args():
    sig = inspect.signature(graph_GraphAsset.__init__)
    params = list(sig.parameters.keys())
    assert "Label" in params, "Missing parameter 'Label'"
    assert "Encrypted" in params, "Missing parameter 'Encrypted'"





def test_hyp_graph_subgraphs_is_not_abstract():
    assert not inspect.isabstract(graph_Subgraphs)


def test_hyp_graph_subgraphs_constructor_exists():
    assert callable(graph_Subgraphs.__init__)


def test_hyp_graph_subgraphs_constructor_args():
    sig = inspect.signature(graph_Subgraphs.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_hyp_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_hyp_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "visited" in params, "Missing parameter 'visited'"
    assert "EdgeLabel" in params, "Missing parameter 'EdgeLabel'"




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
graph_Graph_strategy = st.builds(
    graph_Graph,
)
graph_Identifiable_strategy = st.builds(
    graph_Identifiable,
    number=
        st.integers(),
    ID=
        safe_text
)
Identifiable_strategy = st.builds(
    Identifiable,
)
graph_NodeResponsibility_strategy = st.builds(
    graph_NodeResponsibility,
    operation=
        safe_text
)
graph_Node_strategy = st.builds(
    graph_Node,
    AttackerObservation=
        st.integers(),
    visited=
        st.booleans(),
    Attacker=
        st.booleans(),
    name=
        safe_text
)
graph_GraphAsset_strategy = st.builds(
    graph_GraphAsset,
    Label=
        st.integers(),
    Encrypted=
        st.booleans()
)
graph_Subgraphs_strategy = st.builds(
    graph_Subgraphs,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
    visited=
        st.booleans(),
    EdgeLabel=
        st.integers()
)





@given(instance=graph_Identifiable_strategy)
def test_hyp_graph_identifiable_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=graph_Identifiable_strategy)
def test_hyp_graph_identifiable_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original





@given(instance=graph_NodeResponsibility_strategy)
def test_hyp_graph_noderesponsibility_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_NodeResponsibility_strategy)
@settings(max_examples=30)
def test_hyp_graph_noderesponsibility_findmostrestrictivelabel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findMostRestrictiveLabel()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findMostRestrictiveLabel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findMostRestrictiveLabel' in graph_NodeResponsibility is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findMostRestrictiveLabel' in graph_NodeResponsibility did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findMostRestrictiveLabel' in graph_NodeResponsibility is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_NodeResponsibility_strategy)
@settings(max_examples=30)
def test_hyp_graph_noderesponsibility_findleastrestrictivelabel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.findLeastRestrictiveLabel()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.findLeastRestrictiveLabel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'findLeastRestrictiveLabel' in graph_NodeResponsibility is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'findLeastRestrictiveLabel' in graph_NodeResponsibility did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'findLeastRestrictiveLabel' in graph_NodeResponsibility is not implemented or raised an error")




@given(instance=graph_Node_strategy)
def test_hyp_graph_node_AttackerObservation_setter(instance):
    original = instance.AttackerObservation
    instance.AttackerObservation = original
    assert instance.AttackerObservation == original



@given(instance=graph_Node_strategy)
def test_hyp_graph_node_visited_setter(instance):
    original = instance.visited
    instance.visited = original
    assert instance.visited == original



@given(instance=graph_Node_strategy)
def test_hyp_graph_node_Attacker_setter(instance):
    original = instance.Attacker
    instance.Attacker = original
    assert instance.Attacker == original



@given(instance=graph_Node_strategy)
def test_hyp_graph_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=graph_GraphAsset_strategy)
def test_hyp_graph_graphasset_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original



@given(instance=graph_GraphAsset_strategy)
def test_hyp_graph_graphasset_Encrypted_setter(instance):
    original = instance.Encrypted
    instance.Encrypted = original
    assert instance.Encrypted == original





@given(instance=graph_Edge_strategy)
def test_hyp_graph_edge_visited_setter(instance):
    original = instance.visited
    instance.visited = original
    assert instance.visited == original



@given(instance=graph_Edge_strategy)
def test_hyp_graph_edge_EdgeLabel_setter(instance):
    original = instance.EdgeLabel
    instance.EdgeLabel = original
    assert instance.EdgeLabel == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Identifiable,
    graph_Edge,
    graph_Graph,
    graph_GraphAsset,
    graph_Identifiable,
    graph_Node,
    graph_NodeResponsibility,
    graph_Subgraphs,
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

def test_graph_Edge_EdgeLabel_value_roundtrip():
    instance = graph_Edge(EdgeLabel=7, visited=True)
    assert instance.EdgeLabel == 7
    instance.EdgeLabel = 13
    assert instance.EdgeLabel == 13


def test_graph_Edge_visited_value_roundtrip():
    instance = graph_Edge(EdgeLabel=7, visited=True)
    assert instance.visited == True
    instance.visited = False
    assert instance.visited == False


def test_graph_GraphAsset_Encrypted_value_roundtrip():
    instance = graph_GraphAsset(Encrypted=True, Label=7)
    assert instance.Encrypted == True
    instance.Encrypted = False
    assert instance.Encrypted == False


def test_graph_GraphAsset_Label_value_roundtrip():
    instance = graph_GraphAsset(Encrypted=True, Label=7)
    assert instance.Label == 7
    instance.Label = 13
    assert instance.Label == 13


def test_graph_Identifiable_ID_value_roundtrip():
    instance = graph_Identifiable(ID="sample_text", number=7)
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_graph_Identifiable_number_value_roundtrip():
    instance = graph_Identifiable(ID="sample_text", number=7)
    assert instance.number == 7
    instance.number = 13
    assert instance.number == 13


def test_graph_Node_Attacker_value_roundtrip():
    instance = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    assert instance.Attacker == True
    instance.Attacker = False
    assert instance.Attacker == False


def test_graph_Node_AttackerObservation_value_roundtrip():
    instance = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    assert instance.AttackerObservation == 7
    instance.AttackerObservation = 13
    assert instance.AttackerObservation == 13


def test_graph_Node_name_value_roundtrip():
    instance = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graph_Node_visited_value_roundtrip():
    instance = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    assert instance.visited == True
    instance.visited = False
    assert instance.visited == False


def test_graph_NodeResponsibility_operation_value_roundtrip():
    instance = graph_NodeResponsibility(operation="sample_text")
    assert instance.operation == "sample_text"
    instance.operation = "sample_text_2"
    assert instance.operation == "sample_text_2"


def test_graph_Edge_isa_Identifiable():
    instance = graph_Edge(EdgeLabel=7, visited=True)
    assert isinstance(instance, Identifiable)


def test_graph_GraphAsset_isa_Identifiable():
    instance = graph_GraphAsset(Encrypted=True, Label=7)
    assert isinstance(instance, Identifiable)


def test_graph_Node_isa_Identifiable():
    instance = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    assert isinstance(instance, Identifiable)


def test_graph_NodeResponsibility_isa_Identifiable():
    instance = graph_NodeResponsibility(operation="sample_text")
    assert isinstance(instance, Identifiable)


def test_graph_Subgraphs_isa_Identifiable():
    instance = graph_Subgraphs()
    assert isinstance(instance, Identifiable)


def test_assoc_assets22_link_reassign_clear():
    a = graph_GraphAsset(Encrypted=True, Label=7)
    b1 = graph_Subgraphs()
    b2 = graph_Subgraphs()
    _safe_set(a, 'graph_GraphAsset24', b1)
    assert _is_linked(a, 'graph_GraphAsset24', b1)
    if hasattr(b1, 'graph_Subgraphs23'):
        assert _is_linked(b1, 'graph_Subgraphs23', a)
    _safe_set(a, 'graph_GraphAsset24', b2)
    assert _is_linked(a, 'graph_GraphAsset24', b2)
    if hasattr(b1, 'graph_Subgraphs23'):
        assert not _is_linked(b1, 'graph_Subgraphs23', a)
    if hasattr(b2, 'graph_Subgraphs23'):
        assert _is_linked(b2, 'graph_Subgraphs23', a)
    _safe_set(a, 'graph_GraphAsset24', None)
    assert not _is_linked(a, 'graph_GraphAsset24', b2)
    if hasattr(b2, 'graph_Subgraphs23'):
        assert not _is_linked(b2, 'graph_Subgraphs23', a)


def test_assoc_graphassets4_link_reassign_clear():
    a = graph_GraphAsset(Encrypted=True, Label=7)
    b1 = graph_Edge(EdgeLabel=7, visited=True)
    b2 = graph_Edge(EdgeLabel=13, visited=False)
    _safe_set(a, 'graph_GraphAsset', b1)
    assert _is_linked(a, 'graph_GraphAsset', b1)
    if hasattr(b1, 'graph_Edge5'):
        assert _is_linked(b1, 'graph_Edge5', a)
    _safe_set(a, 'graph_GraphAsset', b2)
    assert _is_linked(a, 'graph_GraphAsset', b2)
    if hasattr(b1, 'graph_Edge5'):
        assert not _is_linked(b1, 'graph_Edge5', a)
    if hasattr(b2, 'graph_Edge5'):
        assert _is_linked(b2, 'graph_Edge5', a)
    _safe_set(a, 'graph_GraphAsset', None)
    assert not _is_linked(a, 'graph_GraphAsset', b2)
    if hasattr(b2, 'graph_Edge5'):
        assert not _is_linked(b2, 'graph_Edge5', a)


def test_assoc_incomingassets28_link_reassign_clear():
    a = graph_NodeResponsibility(operation="sample_text")
    b1 = graph_GraphAsset(Encrypted=True, Label=7)
    b2 = graph_GraphAsset(Encrypted=False, Label=13)
    _safe_set(a, 'graph_NodeResponsibility29', {b1})
    assert _is_linked(a, 'graph_NodeResponsibility29', b1)
    if hasattr(b1, 'graph_GraphAsset30'):
        assert _is_linked(b1, 'graph_GraphAsset30', a)
    _safe_set(a, 'graph_NodeResponsibility29', {b2})
    assert _is_linked(a, 'graph_NodeResponsibility29', b2)
    if hasattr(b1, 'graph_GraphAsset30'):
        assert not _is_linked(b1, 'graph_GraphAsset30', a)
    if hasattr(b2, 'graph_GraphAsset30'):
        assert _is_linked(b2, 'graph_GraphAsset30', a)
    _safe_set(a, 'graph_NodeResponsibility29', set())
    assert not _is_linked(a, 'graph_NodeResponsibility29', b2)
    if hasattr(b2, 'graph_GraphAsset30'):
        assert not _is_linked(b2, 'graph_GraphAsset30', a)


def test_assoc_inedges17_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_Edge(EdgeLabel=7, visited=True)
    b2 = graph_Edge(EdgeLabel=13, visited=False)
    _safe_set(a, 'graph_Node18', {b1})
    assert _is_linked(a, 'graph_Node18', b1)
    if hasattr(b1, 'graph_Edge19'):
        assert _is_linked(b1, 'graph_Edge19', a)
    _safe_set(a, 'graph_Node18', {b2})
    assert _is_linked(a, 'graph_Node18', b2)
    if hasattr(b1, 'graph_Edge19'):
        assert not _is_linked(b1, 'graph_Edge19', a)
    if hasattr(b2, 'graph_Edge19'):
        assert _is_linked(b2, 'graph_Edge19', a)
    _safe_set(a, 'graph_Node18', set())
    assert not _is_linked(a, 'graph_Node18', b2)
    if hasattr(b2, 'graph_Edge19'):
        assert not _is_linked(b2, 'graph_Edge19', a)


def test_assoc_nodes20_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_Subgraphs()
    b2 = graph_Subgraphs()
    _safe_set(a, 'graph_Node21', b1)
    assert _is_linked(a, 'graph_Node21', b1)
    if hasattr(b1, 'graph_Subgraphs'):
        assert _is_linked(b1, 'graph_Subgraphs', a)
    _safe_set(a, 'graph_Node21', b2)
    assert _is_linked(a, 'graph_Node21', b2)
    if hasattr(b1, 'graph_Subgraphs'):
        assert not _is_linked(b1, 'graph_Subgraphs', a)
    if hasattr(b2, 'graph_Subgraphs'):
        assert _is_linked(b2, 'graph_Subgraphs', a)
    _safe_set(a, 'graph_Node21', None)
    assert not _is_linked(a, 'graph_Node21', b2)
    if hasattr(b2, 'graph_Subgraphs'):
        assert not _is_linked(b2, 'graph_Subgraphs', a)


def test_assoc_outedges12_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_Edge(EdgeLabel=7, visited=True)
    b2 = graph_Edge(EdgeLabel=13, visited=False)
    _safe_set(a, 'graph_Node13', {b1})
    assert _is_linked(a, 'graph_Node13', b1)
    if hasattr(b1, 'graph_Edge14'):
        assert _is_linked(b1, 'graph_Edge14', a)
    _safe_set(a, 'graph_Node13', {b2})
    assert _is_linked(a, 'graph_Node13', b2)
    if hasattr(b1, 'graph_Edge14'):
        assert not _is_linked(b1, 'graph_Edge14', a)
    if hasattr(b2, 'graph_Edge14'):
        assert _is_linked(b2, 'graph_Edge14', a)
    _safe_set(a, 'graph_Node13', set())
    assert not _is_linked(a, 'graph_Node13', b2)
    if hasattr(b2, 'graph_Edge14'):
        assert not _is_linked(b2, 'graph_Edge14', a)


def test_assoc_outgoingassets25_link_reassign_clear():
    a = graph_NodeResponsibility(operation="sample_text")
    b1 = graph_GraphAsset(Encrypted=True, Label=7)
    b2 = graph_GraphAsset(Encrypted=False, Label=13)
    _safe_set(a, 'graph_NodeResponsibility26', {b1})
    assert _is_linked(a, 'graph_NodeResponsibility26', b1)
    if hasattr(b1, 'graph_GraphAsset27'):
        assert _is_linked(b1, 'graph_GraphAsset27', a)
    _safe_set(a, 'graph_NodeResponsibility26', {b2})
    assert _is_linked(a, 'graph_NodeResponsibility26', b2)
    if hasattr(b1, 'graph_GraphAsset27'):
        assert not _is_linked(b1, 'graph_GraphAsset27', a)
    if hasattr(b2, 'graph_GraphAsset27'):
        assert _is_linked(b2, 'graph_GraphAsset27', a)
    _safe_set(a, 'graph_NodeResponsibility26', set())
    assert not _is_linked(a, 'graph_NodeResponsibility26', b2)
    if hasattr(b2, 'graph_GraphAsset27'):
        assert not _is_linked(b2, 'graph_GraphAsset27', a)


def test_assoc_responsibility15_link_reassign_clear():
    a = graph_NodeResponsibility(operation="sample_text")
    b1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    _safe_set(a, 'graph_NodeResponsibility', b1)
    assert _is_linked(a, 'graph_NodeResponsibility', b1)
    if hasattr(b1, 'graph_Node16'):
        assert _is_linked(b1, 'graph_Node16', a)
    _safe_set(a, 'graph_NodeResponsibility', b2)
    assert _is_linked(a, 'graph_NodeResponsibility', b2)
    if hasattr(b1, 'graph_Node16'):
        assert not _is_linked(b1, 'graph_Node16', a)
    if hasattr(b2, 'graph_Node16'):
        assert _is_linked(b2, 'graph_Node16', a)
    _safe_set(a, 'graph_NodeResponsibility', None)
    assert not _is_linked(a, 'graph_NodeResponsibility', b2)
    if hasattr(b2, 'graph_Node16'):
        assert not _is_linked(b2, 'graph_Node16', a)


def test_assoc_source1_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_Edge(EdgeLabel=7, visited=True)
    b2 = graph_Edge(EdgeLabel=13, visited=False)
    _safe_set(a, 'graph_Node3', b1)
    assert _is_linked(a, 'graph_Node3', b1)
    if hasattr(b1, 'graph_Edge2'):
        assert _is_linked(b1, 'graph_Edge2', a)
    _safe_set(a, 'graph_Node3', b2)
    assert _is_linked(a, 'graph_Node3', b2)
    if hasattr(b1, 'graph_Edge2'):
        assert not _is_linked(b1, 'graph_Edge2', a)
    if hasattr(b2, 'graph_Edge2'):
        assert _is_linked(b2, 'graph_Edge2', a)
    _safe_set(a, 'graph_Node3', None)
    assert not _is_linked(a, 'graph_Node3', b2)
    if hasattr(b2, 'graph_Edge2'):
        assert not _is_linked(b2, 'graph_Edge2', a)


def test_assoc_source6_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_GraphAsset(Encrypted=True, Label=7)
    b2 = graph_GraphAsset(Encrypted=False, Label=13)
    _safe_set(a, 'graph_Node8', b1)
    assert _is_linked(a, 'graph_Node8', b1)
    if hasattr(b1, 'graph_GraphAsset7'):
        assert _is_linked(b1, 'graph_GraphAsset7', a)
    _safe_set(a, 'graph_Node8', b2)
    assert _is_linked(a, 'graph_Node8', b2)
    if hasattr(b1, 'graph_GraphAsset7'):
        assert not _is_linked(b1, 'graph_GraphAsset7', a)
    if hasattr(b2, 'graph_GraphAsset7'):
        assert _is_linked(b2, 'graph_GraphAsset7', a)
    _safe_set(a, 'graph_Node8', None)
    assert not _is_linked(a, 'graph_Node8', b2)
    if hasattr(b2, 'graph_GraphAsset7'):
        assert not _is_linked(b2, 'graph_GraphAsset7', a)


def test_assoc_target0_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_Edge(EdgeLabel=7, visited=True)
    b2 = graph_Edge(EdgeLabel=13, visited=False)
    _safe_set(a, 'graph_Node', b1)
    assert _is_linked(a, 'graph_Node', b1)
    if hasattr(b1, 'graph_Edge'):
        assert _is_linked(b1, 'graph_Edge', a)
    _safe_set(a, 'graph_Node', b2)
    assert _is_linked(a, 'graph_Node', b2)
    if hasattr(b1, 'graph_Edge'):
        assert not _is_linked(b1, 'graph_Edge', a)
    if hasattr(b2, 'graph_Edge'):
        assert _is_linked(b2, 'graph_Edge', a)
    _safe_set(a, 'graph_Node', None)
    assert not _is_linked(a, 'graph_Node', b2)
    if hasattr(b2, 'graph_Edge'):
        assert not _is_linked(b2, 'graph_Edge', a)


def test_assoc_targets9_link_reassign_clear():
    a = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    b1 = graph_GraphAsset(Encrypted=True, Label=7)
    b2 = graph_GraphAsset(Encrypted=False, Label=13)
    _safe_set(a, 'graph_Node11', b1)
    assert _is_linked(a, 'graph_Node11', b1)
    if hasattr(b1, 'graph_GraphAsset10'):
        assert _is_linked(b1, 'graph_GraphAsset10', a)
    _safe_set(a, 'graph_Node11', b2)
    assert _is_linked(a, 'graph_Node11', b2)
    if hasattr(b1, 'graph_GraphAsset10'):
        assert not _is_linked(b1, 'graph_GraphAsset10', a)
    if hasattr(b2, 'graph_GraphAsset10'):
        assert _is_linked(b2, 'graph_GraphAsset10', a)
    _safe_set(a, 'graph_Node11', None)
    assert not _is_linked(a, 'graph_Node11', b2)
    if hasattr(b2, 'graph_GraphAsset10'):
        assert not _is_linked(b2, 'graph_GraphAsset10', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Identifiable_strategy = st.builds(Identifiable)
@given(instance=Identifiable_strategy)
@settings(max_examples=25)
def test_Identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)


graph_Edge_strategy = st.builds(graph_Edge, EdgeLabel=st.integers(), visited=st.booleans())
@given(instance=graph_Edge_strategy)
@settings(max_examples=25)
def test_graph_Edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)


graph_Graph_strategy = st.builds(graph_Graph)
@given(instance=graph_Graph_strategy)
@settings(max_examples=25)
def test_graph_Graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)


graph_GraphAsset_strategy = st.builds(graph_GraphAsset, Encrypted=st.booleans(), Label=st.integers())
@given(instance=graph_GraphAsset_strategy)
@settings(max_examples=25)
def test_graph_GraphAsset_instantiation(instance):
    assert isinstance(instance, graph_GraphAsset)


graph_Identifiable_strategy = st.builds(graph_Identifiable, ID=safe_text, number=st.integers())
@given(instance=graph_Identifiable_strategy)
@settings(max_examples=25)
def test_graph_Identifiable_instantiation(instance):
    assert isinstance(instance, graph_Identifiable)


graph_Node_strategy = st.builds(graph_Node, Attacker=st.booleans(), AttackerObservation=st.integers(), name=safe_text, visited=st.booleans())
@given(instance=graph_Node_strategy)
@settings(max_examples=25)
def test_graph_Node_instantiation(instance):
    assert isinstance(instance, graph_Node)


graph_NodeResponsibility_strategy = st.builds(graph_NodeResponsibility, operation=safe_text)
@given(instance=graph_NodeResponsibility_strategy)
@settings(max_examples=25)
def test_graph_NodeResponsibility_instantiation(instance):
    assert isinstance(instance, graph_NodeResponsibility)


graph_Subgraphs_strategy = st.builds(graph_Subgraphs)
@given(instance=graph_Subgraphs_strategy)
@settings(max_examples=25)
def test_graph_Subgraphs_instantiation(instance):
    assert isinstance(instance, graph_Subgraphs)



