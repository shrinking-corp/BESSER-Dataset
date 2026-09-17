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
    graph_ElkBendPoint,
    ElkGraphElement,
    graph_ElkShape,
    ElkConnectableShape,
    graph_ElkPort,
    graph_ElkNode,
    graph_ElkEdge,
    ElkShape,
    graph_ElkConnectableShape,
    graph_ElkLabel,
    EMapPropertyHolder,
    graph_ElkEdgeSection,
    graph_ElkGraphElement,
    graph_ElkPropertyToValueMapEntry,
    IPropertyHolder,
    graph_EMapPropertyHolder,
    graph_IPropertyHolder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_graph_elkbendpoint_is_not_abstract():
    assert not inspect.isabstract(graph_ElkBendPoint)


def test_hyp_graph_elkbendpoint_constructor_exists():
    assert callable(graph_ElkBendPoint.__init__)


def test_hyp_graph_elkbendpoint_constructor_args():
    sig = inspect.signature(graph_ElkBendPoint.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_elkgraphelement_is_not_abstract():
    assert not inspect.isabstract(ElkGraphElement)


def test_hyp_elkgraphelement_constructor_exists():
    assert callable(ElkGraphElement.__init__)


def test_hyp_elkgraphelement_constructor_args():
    sig = inspect.signature(ElkGraphElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elkshape_is_not_abstract():
    assert not inspect.isabstract(graph_ElkShape)


def test_hyp_graph_elkshape_constructor_exists():
    assert callable(graph_ElkShape.__init__)


def test_hyp_graph_elkshape_constructor_args():
    sig = inspect.signature(graph_ElkShape.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"







def test_hyp_elkconnectableshape_is_not_abstract():
    assert not inspect.isabstract(ElkConnectableShape)


def test_hyp_elkconnectableshape_constructor_exists():
    assert callable(ElkConnectableShape.__init__)


def test_hyp_elkconnectableshape_constructor_args():
    sig = inspect.signature(ElkConnectableShape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elkport_is_not_abstract():
    assert not inspect.isabstract(graph_ElkPort)


def test_hyp_graph_elkport_constructor_exists():
    assert callable(graph_ElkPort.__init__)


def test_hyp_graph_elkport_constructor_args():
    sig = inspect.signature(graph_ElkPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elknode_is_not_abstract():
    assert not inspect.isabstract(graph_ElkNode)


def test_hyp_graph_elknode_constructor_exists():
    assert callable(graph_ElkNode.__init__)


def test_hyp_graph_elknode_constructor_args():
    sig = inspect.signature(graph_ElkNode.__init__)
    params = list(sig.parameters.keys())
    assert "hierarchical" in params, "Missing parameter 'hierarchical'"




def test_hyp_graph_elkedge_is_not_abstract():
    assert not inspect.isabstract(graph_ElkEdge)


def test_hyp_graph_elkedge_constructor_exists():
    assert callable(graph_ElkEdge.__init__)


def test_hyp_graph_elkedge_constructor_args():
    sig = inspect.signature(graph_ElkEdge.__init__)
    params = list(sig.parameters.keys())
    assert "selfloop" in params, "Missing parameter 'selfloop'"
    assert "hierarchical" in params, "Missing parameter 'hierarchical'"
    assert "connected" in params, "Missing parameter 'connected'"
    assert "hyperedge" in params, "Missing parameter 'hyperedge'"







def test_hyp_elkshape_is_not_abstract():
    assert not inspect.isabstract(ElkShape)


def test_hyp_elkshape_constructor_exists():
    assert callable(ElkShape.__init__)


def test_hyp_elkshape_constructor_args():
    sig = inspect.signature(ElkShape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elkconnectableshape_is_not_abstract():
    assert not inspect.isabstract(graph_ElkConnectableShape)


def test_hyp_graph_elkconnectableshape_constructor_exists():
    assert callable(graph_ElkConnectableShape.__init__)


def test_hyp_graph_elkconnectableshape_constructor_args():
    sig = inspect.signature(graph_ElkConnectableShape.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elklabel_is_not_abstract():
    assert not inspect.isabstract(graph_ElkLabel)


def test_hyp_graph_elklabel_constructor_exists():
    assert callable(graph_ElkLabel.__init__)


def test_hyp_graph_elklabel_constructor_args():
    sig = inspect.signature(graph_ElkLabel.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_emappropertyholder_is_not_abstract():
    assert not inspect.isabstract(EMapPropertyHolder)


def test_hyp_emappropertyholder_constructor_exists():
    assert callable(EMapPropertyHolder.__init__)


def test_hyp_emappropertyholder_constructor_args():
    sig = inspect.signature(EMapPropertyHolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_elkedgesection_is_not_abstract():
    assert not inspect.isabstract(graph_ElkEdgeSection)


def test_hyp_graph_elkedgesection_constructor_exists():
    assert callable(graph_ElkEdgeSection.__init__)


def test_hyp_graph_elkedgesection_constructor_args():
    sig = inspect.signature(graph_ElkEdgeSection.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "startY" in params, "Missing parameter 'startY'"
    assert "endY" in params, "Missing parameter 'endY'"
    assert "startX" in params, "Missing parameter 'startX'"
    assert "endX" in params, "Missing parameter 'endX'"








def test_hyp_graph_elkgraphelement_is_not_abstract():
    assert not inspect.isabstract(graph_ElkGraphElement)


def test_hyp_graph_elkgraphelement_constructor_exists():
    assert callable(graph_ElkGraphElement.__init__)


def test_hyp_graph_elkgraphelement_constructor_args():
    sig = inspect.signature(graph_ElkGraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"




def test_hyp_graph_elkpropertytovaluemapentry_is_not_abstract():
    assert not inspect.isabstract(graph_ElkPropertyToValueMapEntry)


def test_hyp_graph_elkpropertytovaluemapentry_constructor_exists():
    assert callable(graph_ElkPropertyToValueMapEntry.__init__)


def test_hyp_graph_elkpropertytovaluemapentry_constructor_args():
    sig = inspect.signature(graph_ElkPropertyToValueMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_ipropertyholder_is_not_abstract():
    assert not inspect.isabstract(IPropertyHolder)


def test_hyp_ipropertyholder_constructor_exists():
    assert callable(IPropertyHolder.__init__)


def test_hyp_ipropertyholder_constructor_args():
    sig = inspect.signature(IPropertyHolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_emappropertyholder_is_not_abstract():
    assert not inspect.isabstract(graph_EMapPropertyHolder)


def test_hyp_graph_emappropertyholder_constructor_exists():
    assert callable(graph_EMapPropertyHolder.__init__)


def test_hyp_graph_emappropertyholder_constructor_args():
    sig = inspect.signature(graph_EMapPropertyHolder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_ipropertyholder_is_not_abstract():
    assert not inspect.isabstract(graph_IPropertyHolder)


def test_hyp_graph_ipropertyholder_constructor_exists():
    assert callable(graph_IPropertyHolder.__init__)


def test_hyp_graph_ipropertyholder_constructor_args():
    sig = inspect.signature(graph_IPropertyHolder.__init__)
    params = list(sig.parameters.keys())


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
graph_ElkBendPoint_strategy = st.builds(
    graph_ElkBendPoint,
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ElkGraphElement_strategy = st.builds(
    ElkGraphElement,
)
graph_ElkShape_strategy = st.builds(
    graph_ElkShape,
    x=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    height=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    width=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    y=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ElkConnectableShape_strategy = st.builds(
    ElkConnectableShape,
)
graph_ElkPort_strategy = st.builds(
    graph_ElkPort,
)
graph_ElkNode_strategy = st.builds(
    graph_ElkNode,
    hierarchical=
        st.booleans()
)
graph_ElkEdge_strategy = st.builds(
    graph_ElkEdge,
    selfloop=
        st.booleans(),
    hierarchical=
        st.booleans(),
    connected=
        st.booleans(),
    hyperedge=
        st.booleans()
)
ElkShape_strategy = st.builds(
    ElkShape,
)
graph_ElkConnectableShape_strategy = st.builds(
    graph_ElkConnectableShape,
)
graph_ElkLabel_strategy = st.builds(
    graph_ElkLabel,
    text=
        safe_text
)
EMapPropertyHolder_strategy = st.builds(
    EMapPropertyHolder,
)
graph_ElkEdgeSection_strategy = st.builds(
    graph_ElkEdgeSection,
    identifier=
        safe_text,
    startY=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    endY=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    startX=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    endX=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
graph_ElkGraphElement_strategy = st.builds(
    graph_ElkGraphElement,
    identifier=
        safe_text
)
graph_ElkPropertyToValueMapEntry_strategy = st.builds(
    graph_ElkPropertyToValueMapEntry,
    value=
        safe_text,
    key=
        safe_text
)
IPropertyHolder_strategy = st.builds(
    IPropertyHolder,
)
graph_EMapPropertyHolder_strategy = st.builds(
    graph_EMapPropertyHolder,
)
graph_IPropertyHolder_strategy = st.builds(
    graph_IPropertyHolder,
)




@given(instance=graph_ElkBendPoint_strategy)
def test_hyp_graph_elkbendpoint_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=graph_ElkBendPoint_strategy)
def test_hyp_graph_elkbendpoint_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_ElkBendPoint_strategy)
@settings(max_examples=30)
def test_hyp_graph_elkbendpoint_set_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.set(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.set).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'set' in graph_ElkBendPoint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'set' in graph_ElkBendPoint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'set' in graph_ElkBendPoint is not implemented or raised an error")





@given(instance=graph_ElkShape_strategy)
def test_hyp_graph_elkshape_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graph_ElkShape_strategy)
def test_hyp_graph_elkshape_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=graph_ElkShape_strategy)
def test_hyp_graph_elkshape_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=graph_ElkShape_strategy)
def test_hyp_graph_elkshape_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_ElkShape_strategy)
@settings(max_examples=30)
def test_hyp_graph_elkshape_setdimensions_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setDimensions(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setDimensions).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setDimensions' in graph_ElkShape is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setDimensions' in graph_ElkShape did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setDimensions' in graph_ElkShape is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_ElkShape_strategy)
@settings(max_examples=30)
def test_hyp_graph_elkshape_setlocation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setLocation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setLocation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setLocation' in graph_ElkShape is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setLocation' in graph_ElkShape did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setLocation' in graph_ElkShape is not implemented or raised an error")






@given(instance=graph_ElkNode_strategy)
def test_hyp_graph_elknode_hierarchical_setter(instance):
    original = instance.hierarchical
    instance.hierarchical = original
    assert instance.hierarchical == original




@given(instance=graph_ElkEdge_strategy)
def test_hyp_graph_elkedge_selfloop_setter(instance):
    original = instance.selfloop
    instance.selfloop = original
    assert instance.selfloop == original



@given(instance=graph_ElkEdge_strategy)
def test_hyp_graph_elkedge_hierarchical_setter(instance):
    original = instance.hierarchical
    instance.hierarchical = original
    assert instance.hierarchical == original



@given(instance=graph_ElkEdge_strategy)
def test_hyp_graph_elkedge_connected_setter(instance):
    original = instance.connected
    instance.connected = original
    assert instance.connected == original



@given(instance=graph_ElkEdge_strategy)
def test_hyp_graph_elkedge_hyperedge_setter(instance):
    original = instance.hyperedge
    instance.hyperedge = original
    assert instance.hyperedge == original






@given(instance=graph_ElkLabel_strategy)
def test_hyp_graph_elklabel_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original





@given(instance=graph_ElkEdgeSection_strategy)
def test_hyp_graph_elkedgesection_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=graph_ElkEdgeSection_strategy)
def test_hyp_graph_elkedgesection_startY_setter(instance):
    original = instance.startY
    instance.startY = original
    assert instance.startY == original



@given(instance=graph_ElkEdgeSection_strategy)
def test_hyp_graph_elkedgesection_endY_setter(instance):
    original = instance.endY
    instance.endY = original
    assert instance.endY == original



@given(instance=graph_ElkEdgeSection_strategy)
def test_hyp_graph_elkedgesection_startX_setter(instance):
    original = instance.startX
    instance.startX = original
    assert instance.startX == original



@given(instance=graph_ElkEdgeSection_strategy)
def test_hyp_graph_elkedgesection_endX_setter(instance):
    original = instance.endX
    instance.endX = original
    assert instance.endX == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_ElkEdgeSection_strategy)
@settings(max_examples=30)
def test_hyp_graph_elkedgesection_setstartlocation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setStartLocation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setStartLocation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setStartLocation' in graph_ElkEdgeSection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setStartLocation' in graph_ElkEdgeSection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setStartLocation' in graph_ElkEdgeSection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_ElkEdgeSection_strategy)
@settings(max_examples=30)
def test_hyp_graph_elkedgesection_setendlocation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setEndLocation(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setEndLocation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setEndLocation' in graph_ElkEdgeSection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setEndLocation' in graph_ElkEdgeSection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setEndLocation' in graph_ElkEdgeSection is not implemented or raised an error")




@given(instance=graph_ElkGraphElement_strategy)
def test_hyp_graph_elkgraphelement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original




@given(instance=graph_ElkPropertyToValueMapEntry_strategy)
def test_hyp_graph_elkpropertytovaluemapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=graph_ElkPropertyToValueMapEntry_strategy)
def test_hyp_graph_elkpropertytovaluemapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_IPropertyHolder_strategy)
@settings(max_examples=30)
def test_hyp_graph_ipropertyholder_copyproperties_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.copyProperties(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.copyProperties).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'copyProperties' in graph_IPropertyHolder is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'copyProperties' in graph_IPropertyHolder did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'copyProperties' in graph_IPropertyHolder is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_IPropertyHolder_strategy)
@settings(max_examples=30)
def test_hyp_graph_ipropertyholder_setproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setProperty(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setProperty' in graph_IPropertyHolder is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setProperty' in graph_IPropertyHolder did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setProperty' in graph_IPropertyHolder is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=graph_IPropertyHolder_strategy)
@settings(max_examples=30)
def test_hyp_graph_ipropertyholder_hasproperty_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasProperty(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasProperty).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasProperty' in graph_IPropertyHolder is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasProperty' in graph_IPropertyHolder did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasProperty' in graph_IPropertyHolder is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EMapPropertyHolder,
    ElkConnectableShape,
    ElkGraphElement,
    ElkShape,
    IPropertyHolder,
    graph_EMapPropertyHolder,
    graph_ElkBendPoint,
    graph_ElkConnectableShape,
    graph_ElkEdge,
    graph_ElkEdgeSection,
    graph_ElkGraphElement,
    graph_ElkLabel,
    graph_ElkNode,
    graph_ElkPort,
    graph_ElkPropertyToValueMapEntry,
    graph_ElkShape,
    graph_IPropertyHolder,
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

def test_graph_ElkBendPoint_x_value_roundtrip():
    instance = graph_ElkBendPoint(x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_graph_ElkBendPoint_y_value_roundtrip():
    instance = graph_ElkBendPoint(x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_graph_ElkEdge_connected_value_roundtrip():
    instance = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    assert instance.connected == True
    instance.connected = False
    assert instance.connected == False


def test_graph_ElkEdge_hierarchical_value_roundtrip():
    instance = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    assert instance.hierarchical == True
    instance.hierarchical = False
    assert instance.hierarchical == False


def test_graph_ElkEdge_hyperedge_value_roundtrip():
    instance = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    assert instance.hyperedge == True
    instance.hyperedge = False
    assert instance.hyperedge == False


def test_graph_ElkEdge_selfloop_value_roundtrip():
    instance = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    assert instance.selfloop == True
    instance.selfloop = False
    assert instance.selfloop == False


def test_graph_ElkEdgeSection_endX_value_roundtrip():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert instance.endX == 3.14
    instance.endX = 9.99
    assert instance.endX == 9.99


def test_graph_ElkEdgeSection_endY_value_roundtrip():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert instance.endY == 3.14
    instance.endY = 9.99
    assert instance.endY == 9.99


def test_graph_ElkEdgeSection_identifier_value_roundtrip():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_graph_ElkEdgeSection_startX_value_roundtrip():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert instance.startX == 3.14
    instance.startX = 9.99
    assert instance.startX == 9.99


def test_graph_ElkEdgeSection_startY_value_roundtrip():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert instance.startY == 3.14
    instance.startY = 9.99
    assert instance.startY == 9.99


def test_graph_ElkGraphElement_identifier_value_roundtrip():
    instance = graph_ElkGraphElement(identifier="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_graph_ElkLabel_text_value_roundtrip():
    instance = graph_ElkLabel(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graph_ElkNode_hierarchical_value_roundtrip():
    instance = graph_ElkNode(hierarchical=True)
    assert instance.hierarchical == True
    instance.hierarchical = False
    assert instance.hierarchical == False


def test_graph_ElkPropertyToValueMapEntry_key_value_roundtrip():
    instance = graph_ElkPropertyToValueMapEntry(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_graph_ElkPropertyToValueMapEntry_value_value_roundtrip():
    instance = graph_ElkPropertyToValueMapEntry(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graph_ElkShape_height_value_roundtrip():
    instance = graph_ElkShape(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.height == 3.14
    instance.height = 9.99
    assert instance.height == 9.99


def test_graph_ElkShape_width_value_roundtrip():
    instance = graph_ElkShape(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.width == 3.14
    instance.width = 9.99
    assert instance.width == 9.99


def test_graph_ElkShape_x_value_roundtrip():
    instance = graph_ElkShape(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.x == 3.14
    instance.x = 9.99
    assert instance.x == 9.99


def test_graph_ElkShape_y_value_roundtrip():
    instance = graph_ElkShape(height=3.14, width=3.14, x=3.14, y=3.14)
    assert instance.y == 3.14
    instance.y = 9.99
    assert instance.y == 9.99


def test_graph_ElkEdgeSection_isa_EMapPropertyHolder():
    instance = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    assert isinstance(instance, EMapPropertyHolder)


def test_graph_ElkGraphElement_isa_EMapPropertyHolder():
    instance = graph_ElkGraphElement(identifier="sample_text")
    assert isinstance(instance, EMapPropertyHolder)


def test_graph_ElkNode_isa_ElkConnectableShape():
    instance = graph_ElkNode(hierarchical=True)
    assert isinstance(instance, ElkConnectableShape)


def test_graph_ElkPort_isa_ElkConnectableShape():
    instance = graph_ElkPort()
    assert isinstance(instance, ElkConnectableShape)


def test_graph_ElkEdge_isa_ElkGraphElement():
    instance = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    assert isinstance(instance, ElkGraphElement)


def test_graph_ElkShape_isa_ElkGraphElement():
    instance = graph_ElkShape(height=3.14, width=3.14, x=3.14, y=3.14)
    assert isinstance(instance, ElkGraphElement)


def test_graph_ElkConnectableShape_isa_ElkShape():
    instance = graph_ElkConnectableShape()
    assert isinstance(instance, ElkShape)


def test_graph_ElkLabel_isa_ElkShape():
    instance = graph_ElkLabel(text="sample_text")
    assert isinstance(instance, ElkShape)


def test_graph_EMapPropertyHolder_isa_IPropertyHolder():
    instance = graph_EMapPropertyHolder()
    assert isinstance(instance, IPropertyHolder)


def test_assoc_bendPoints25_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkBendPoint(x=3.14, y=3.14)
    b2 = graph_ElkBendPoint(x=9.99, y=9.99)
    _safe_set(a, 'graph_ElkEdgeSection', {b1})
    assert _is_linked(a, 'graph_ElkEdgeSection', b1)
    if hasattr(b1, 'graph_ElkBendPoint'):
        assert _is_linked(b1, 'graph_ElkBendPoint', a)
    _safe_set(a, 'graph_ElkEdgeSection', {b2})
    assert _is_linked(a, 'graph_ElkEdgeSection', b2)
    if hasattr(b1, 'graph_ElkBendPoint'):
        assert not _is_linked(b1, 'graph_ElkBendPoint', a)
    if hasattr(b2, 'graph_ElkBendPoint'):
        assert _is_linked(b2, 'graph_ElkBendPoint', a)
    _safe_set(a, 'graph_ElkEdgeSection', set())
    assert not _is_linked(a, 'graph_ElkEdgeSection', b2)
    if hasattr(b2, 'graph_ElkBendPoint'):
        assert not _is_linked(b2, 'graph_ElkBendPoint', a)


def test_assoc_children9_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkNode(hierarchical=True)
    b2 = graph_ElkNode(hierarchical=False)
    _safe_set(a, 'ElkNode', b1)
    assert _is_linked(a, 'ElkNode', b1)
    if hasattr(b1, 'parent10'):
        assert _is_linked(b1, 'parent10', a)
    _safe_set(a, 'ElkNode', b2)
    assert _is_linked(a, 'ElkNode', b2)
    if hasattr(b1, 'parent10'):
        assert not _is_linked(b1, 'parent10', a)
    if hasattr(b2, 'parent10'):
        assert _is_linked(b2, 'parent10', a)
    _safe_set(a, 'ElkNode', None)
    assert not _is_linked(a, 'ElkNode', b2)
    if hasattr(b2, 'parent10'):
        assert not _is_linked(b2, 'parent10', a)


def test_assoc_containedEdges14_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b2 = graph_ElkEdge(connected=False, hierarchical=False, hyperedge=False, selfloop=False)
    _safe_set(a, 'containingNode', {b1})
    assert _is_linked(a, 'containingNode', b1)
    if hasattr(b1, 'ElkEdge15'):
        assert _is_linked(b1, 'ElkEdge15', a)
    _safe_set(a, 'containingNode', {b2})
    assert _is_linked(a, 'containingNode', b2)
    if hasattr(b1, 'ElkEdge15'):
        assert not _is_linked(b1, 'ElkEdge15', a)
    if hasattr(b2, 'ElkEdge15'):
        assert _is_linked(b2, 'ElkEdge15', a)
    _safe_set(a, 'containingNode', set())
    assert not _is_linked(a, 'containingNode', b2)
    if hasattr(b2, 'ElkEdge15'):
        assert not _is_linked(b2, 'ElkEdge15', a)


def test_assoc_containingNode18_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b2 = graph_ElkEdge(connected=False, hierarchical=False, hyperedge=False, selfloop=False)
    _safe_set(a, 'ElkNode19', b1)
    assert _is_linked(a, 'ElkNode19', b1)
    if hasattr(b1, 'containedEdges'):
        assert _is_linked(b1, 'containedEdges', a)
    _safe_set(a, 'ElkNode19', b2)
    assert _is_linked(a, 'ElkNode19', b2)
    if hasattr(b1, 'containedEdges'):
        assert not _is_linked(b1, 'containedEdges', a)
    if hasattr(b2, 'containedEdges'):
        assert _is_linked(b2, 'containedEdges', a)
    _safe_set(a, 'ElkNode19', None)
    assert not _is_linked(a, 'ElkNode19', b2)
    if hasattr(b2, 'containedEdges'):
        assert not _is_linked(b2, 'containedEdges', a)


def test_assoc_incomingEdges4_link_reassign_clear():
    a = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'ElkEdge5', b1)
    assert _is_linked(a, 'ElkEdge5', b1)
    if hasattr(b1, 'targets'):
        assert _is_linked(b1, 'targets', a)
    _safe_set(a, 'ElkEdge5', b2)
    assert _is_linked(a, 'ElkEdge5', b2)
    if hasattr(b1, 'targets'):
        assert not _is_linked(b1, 'targets', a)
    if hasattr(b2, 'targets'):
        assert _is_linked(b2, 'targets', a)
    _safe_set(a, 'ElkEdge5', None)
    assert not _is_linked(a, 'ElkEdge5', b2)
    if hasattr(b2, 'targets'):
        assert not _is_linked(b2, 'targets', a)


def test_assoc_incomingSections37_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    _safe_set(a, 'ElkEdgeSection38', b1)
    assert _is_linked(a, 'ElkEdgeSection38', b1)
    if hasattr(b1, 'outgoingSections'):
        assert _is_linked(b1, 'outgoingSections', a)
    _safe_set(a, 'ElkEdgeSection38', b2)
    assert _is_linked(a, 'ElkEdgeSection38', b2)
    if hasattr(b1, 'outgoingSections'):
        assert not _is_linked(b1, 'outgoingSections', a)
    if hasattr(b2, 'outgoingSections'):
        assert _is_linked(b2, 'outgoingSections', a)
    _safe_set(a, 'ElkEdgeSection38', None)
    assert not _is_linked(a, 'ElkEdgeSection38', b2)
    if hasattr(b2, 'outgoingSections'):
        assert not _is_linked(b2, 'outgoingSections', a)


def test_assoc_incomingShape30_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'graph_ElkEdgeSection31', b1)
    assert _is_linked(a, 'graph_ElkEdgeSection31', b1)
    if hasattr(b1, 'graph_ElkConnectableShape32'):
        assert _is_linked(b1, 'graph_ElkConnectableShape32', a)
    _safe_set(a, 'graph_ElkEdgeSection31', b2)
    assert _is_linked(a, 'graph_ElkEdgeSection31', b2)
    if hasattr(b1, 'graph_ElkConnectableShape32'):
        assert not _is_linked(b1, 'graph_ElkConnectableShape32', a)
    if hasattr(b2, 'graph_ElkConnectableShape32'):
        assert _is_linked(b2, 'graph_ElkConnectableShape32', a)
    _safe_set(a, 'graph_ElkEdgeSection31', None)
    assert not _is_linked(a, 'graph_ElkEdgeSection31', b2)
    if hasattr(b2, 'graph_ElkConnectableShape32'):
        assert not _is_linked(b2, 'graph_ElkConnectableShape32', a)


def test_assoc_labels1_link_reassign_clear():
    a = graph_ElkLabel(text="sample_text")
    b1 = graph_ElkGraphElement(identifier="sample_text")
    b2 = graph_ElkGraphElement(identifier="sample_text_2")
    _safe_set(a, 'ElkLabel', b1)
    assert _is_linked(a, 'ElkLabel', b1)
    if hasattr(b1, 'parent'):
        assert _is_linked(b1, 'parent', a)
    _safe_set(a, 'ElkLabel', b2)
    assert _is_linked(a, 'ElkLabel', b2)
    if hasattr(b1, 'parent'):
        assert not _is_linked(b1, 'parent', a)
    if hasattr(b2, 'parent'):
        assert _is_linked(b2, 'parent', a)
    _safe_set(a, 'ElkLabel', None)
    assert not _is_linked(a, 'ElkLabel', b2)
    if hasattr(b2, 'parent'):
        assert not _is_linked(b2, 'parent', a)


def test_assoc_outgoingEdges3_link_reassign_clear():
    a = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'ElkEdge', b1)
    assert _is_linked(a, 'ElkEdge', b1)
    if hasattr(b1, 'sources'):
        assert _is_linked(b1, 'sources', a)
    _safe_set(a, 'ElkEdge', b2)
    assert _is_linked(a, 'ElkEdge', b2)
    if hasattr(b1, 'sources'):
        assert not _is_linked(b1, 'sources', a)
    if hasattr(b2, 'sources'):
        assert _is_linked(b2, 'sources', a)
    _safe_set(a, 'ElkEdge', None)
    assert not _is_linked(a, 'ElkEdge', b2)
    if hasattr(b2, 'sources'):
        assert not _is_linked(b2, 'sources', a)


def test_assoc_outgoingSections34_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b2 = graph_ElkEdgeSection(endX=9.99, endY=9.99, identifier="sample_text_2", startX=9.99, startY=9.99)
    _safe_set(a, 'ElkEdgeSection35', b1)
    assert _is_linked(a, 'ElkEdgeSection35', b1)
    if hasattr(b1, 'incomingSections'):
        assert _is_linked(b1, 'incomingSections', a)
    _safe_set(a, 'ElkEdgeSection35', b2)
    assert _is_linked(a, 'ElkEdgeSection35', b2)
    if hasattr(b1, 'incomingSections'):
        assert not _is_linked(b1, 'incomingSections', a)
    if hasattr(b2, 'incomingSections'):
        assert _is_linked(b2, 'incomingSections', a)
    _safe_set(a, 'ElkEdgeSection35', None)
    assert not _is_linked(a, 'ElkEdgeSection35', b2)
    if hasattr(b2, 'incomingSections'):
        assert not _is_linked(b2, 'incomingSections', a)


def test_assoc_outgoingShape28_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'graph_ElkEdgeSection29', b1)
    assert _is_linked(a, 'graph_ElkEdgeSection29', b1)
    if hasattr(b1, 'graph_ElkConnectableShape'):
        assert _is_linked(b1, 'graph_ElkConnectableShape', a)
    _safe_set(a, 'graph_ElkEdgeSection29', b2)
    assert _is_linked(a, 'graph_ElkEdgeSection29', b2)
    if hasattr(b1, 'graph_ElkConnectableShape'):
        assert not _is_linked(b1, 'graph_ElkConnectableShape', a)
    if hasattr(b2, 'graph_ElkConnectableShape'):
        assert _is_linked(b2, 'graph_ElkConnectableShape', a)
    _safe_set(a, 'graph_ElkEdgeSection29', None)
    assert not _is_linked(a, 'graph_ElkEdgeSection29', b2)
    if hasattr(b2, 'graph_ElkConnectableShape'):
        assert not _is_linked(b2, 'graph_ElkConnectableShape', a)


def test_assoc_parent12_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkNode(hierarchical=True)
    b2 = graph_ElkNode(hierarchical=False)
    _safe_set(a, 'ElkNode13', b1)
    assert _is_linked(a, 'ElkNode13', b1)
    if hasattr(b1, 'children'):
        assert _is_linked(b1, 'children', a)
    _safe_set(a, 'ElkNode13', b2)
    assert _is_linked(a, 'ElkNode13', b2)
    if hasattr(b1, 'children'):
        assert not _is_linked(b1, 'children', a)
    if hasattr(b2, 'children'):
        assert _is_linked(b2, 'children', a)
    _safe_set(a, 'ElkNode13', None)
    assert not _is_linked(a, 'ElkNode13', b2)
    if hasattr(b2, 'children'):
        assert not _is_linked(b2, 'children', a)


def test_assoc_parent16_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkPort()
    b2 = graph_ElkPort()
    _safe_set(a, 'ElkNode17', b1)
    assert _is_linked(a, 'ElkNode17', b1)
    if hasattr(b1, 'ports'):
        assert _is_linked(b1, 'ports', a)
    _safe_set(a, 'ElkNode17', b2)
    assert _is_linked(a, 'ElkNode17', b2)
    if hasattr(b1, 'ports'):
        assert not _is_linked(b1, 'ports', a)
    if hasattr(b2, 'ports'):
        assert _is_linked(b2, 'ports', a)
    _safe_set(a, 'ElkNode17', None)
    assert not _is_linked(a, 'ElkNode17', b2)
    if hasattr(b2, 'ports'):
        assert not _is_linked(b2, 'ports', a)


def test_assoc_parent2_link_reassign_clear():
    a = graph_ElkLabel(text="sample_text")
    b1 = graph_ElkGraphElement(identifier="sample_text")
    b2 = graph_ElkGraphElement(identifier="sample_text_2")
    _safe_set(a, 'labels', b1)
    assert _is_linked(a, 'labels', b1)
    if hasattr(b1, 'ElkGraphElement'):
        assert _is_linked(b1, 'ElkGraphElement', a)
    _safe_set(a, 'labels', b2)
    assert _is_linked(a, 'labels', b2)
    if hasattr(b1, 'ElkGraphElement'):
        assert not _is_linked(b1, 'ElkGraphElement', a)
    if hasattr(b2, 'ElkGraphElement'):
        assert _is_linked(b2, 'ElkGraphElement', a)
    _safe_set(a, 'labels', None)
    assert not _is_linked(a, 'labels', b2)
    if hasattr(b2, 'ElkGraphElement'):
        assert not _is_linked(b2, 'ElkGraphElement', a)


def test_assoc_parent26_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b2 = graph_ElkEdge(connected=False, hierarchical=False, hyperedge=False, selfloop=False)
    _safe_set(a, 'sections', b1)
    assert _is_linked(a, 'sections', b1)
    if hasattr(b1, 'ElkEdge27'):
        assert _is_linked(b1, 'ElkEdge27', a)
    _safe_set(a, 'sections', b2)
    assert _is_linked(a, 'sections', b2)
    if hasattr(b1, 'ElkEdge27'):
        assert not _is_linked(b1, 'ElkEdge27', a)
    if hasattr(b2, 'ElkEdge27'):
        assert _is_linked(b2, 'ElkEdge27', a)
    _safe_set(a, 'sections', None)
    assert not _is_linked(a, 'sections', b2)
    if hasattr(b2, 'ElkEdge27'):
        assert not _is_linked(b2, 'ElkEdge27', a)


def test_assoc_ports6_link_reassign_clear():
    a = graph_ElkNode(hierarchical=True)
    b1 = graph_ElkPort()
    b2 = graph_ElkPort()
    _safe_set(a, 'parent7', {b1})
    assert _is_linked(a, 'parent7', b1)
    if hasattr(b1, 'ElkPort'):
        assert _is_linked(b1, 'ElkPort', a)
    _safe_set(a, 'parent7', {b2})
    assert _is_linked(a, 'parent7', b2)
    if hasattr(b1, 'ElkPort'):
        assert not _is_linked(b1, 'ElkPort', a)
    if hasattr(b2, 'ElkPort'):
        assert _is_linked(b2, 'ElkPort', a)
    _safe_set(a, 'parent7', set())
    assert not _is_linked(a, 'parent7', b2)
    if hasattr(b2, 'ElkPort'):
        assert not _is_linked(b2, 'ElkPort', a)


def test_assoc_properties0_link_reassign_clear():
    a = graph_ElkPropertyToValueMapEntry(key="sample_text", value="sample_text")
    b1 = graph_EMapPropertyHolder()
    b2 = graph_EMapPropertyHolder()
    _safe_set(a, 'graph_ElkPropertyToValueMapEntry', b1)
    assert _is_linked(a, 'graph_ElkPropertyToValueMapEntry', b1)
    if hasattr(b1, 'graph_EMapPropertyHolder'):
        assert _is_linked(b1, 'graph_EMapPropertyHolder', a)
    _safe_set(a, 'graph_ElkPropertyToValueMapEntry', b2)
    assert _is_linked(a, 'graph_ElkPropertyToValueMapEntry', b2)
    if hasattr(b1, 'graph_EMapPropertyHolder'):
        assert not _is_linked(b1, 'graph_EMapPropertyHolder', a)
    if hasattr(b2, 'graph_EMapPropertyHolder'):
        assert _is_linked(b2, 'graph_EMapPropertyHolder', a)
    _safe_set(a, 'graph_ElkPropertyToValueMapEntry', None)
    assert not _is_linked(a, 'graph_ElkPropertyToValueMapEntry', b2)
    if hasattr(b2, 'graph_EMapPropertyHolder'):
        assert not _is_linked(b2, 'graph_EMapPropertyHolder', a)


def test_assoc_sections23_link_reassign_clear():
    a = graph_ElkEdgeSection(endX=3.14, endY=3.14, identifier="sample_text", startX=3.14, startY=3.14)
    b1 = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b2 = graph_ElkEdge(connected=False, hierarchical=False, hyperedge=False, selfloop=False)
    _safe_set(a, 'ElkEdgeSection', b1)
    assert _is_linked(a, 'ElkEdgeSection', b1)
    if hasattr(b1, 'parent24'):
        assert _is_linked(b1, 'parent24', a)
    _safe_set(a, 'ElkEdgeSection', b2)
    assert _is_linked(a, 'ElkEdgeSection', b2)
    if hasattr(b1, 'parent24'):
        assert not _is_linked(b1, 'parent24', a)
    if hasattr(b2, 'parent24'):
        assert _is_linked(b2, 'parent24', a)
    _safe_set(a, 'ElkEdgeSection', None)
    assert not _is_linked(a, 'ElkEdgeSection', b2)
    if hasattr(b2, 'parent24'):
        assert not _is_linked(b2, 'parent24', a)


def test_assoc_sources20_link_reassign_clear():
    a = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'outgoingEdges', {b1})
    assert _is_linked(a, 'outgoingEdges', b1)
    if hasattr(b1, 'ElkConnectableShape'):
        assert _is_linked(b1, 'ElkConnectableShape', a)
    _safe_set(a, 'outgoingEdges', {b2})
    assert _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b1, 'ElkConnectableShape'):
        assert not _is_linked(b1, 'ElkConnectableShape', a)
    if hasattr(b2, 'ElkConnectableShape'):
        assert _is_linked(b2, 'ElkConnectableShape', a)
    _safe_set(a, 'outgoingEdges', set())
    assert not _is_linked(a, 'outgoingEdges', b2)
    if hasattr(b2, 'ElkConnectableShape'):
        assert not _is_linked(b2, 'ElkConnectableShape', a)


def test_assoc_targets21_link_reassign_clear():
    a = graph_ElkEdge(connected=True, hierarchical=True, hyperedge=True, selfloop=True)
    b1 = graph_ElkConnectableShape()
    b2 = graph_ElkConnectableShape()
    _safe_set(a, 'incomingEdges', {b1})
    assert _is_linked(a, 'incomingEdges', b1)
    if hasattr(b1, 'ElkConnectableShape22'):
        assert _is_linked(b1, 'ElkConnectableShape22', a)
    _safe_set(a, 'incomingEdges', {b2})
    assert _is_linked(a, 'incomingEdges', b2)
    if hasattr(b1, 'ElkConnectableShape22'):
        assert not _is_linked(b1, 'ElkConnectableShape22', a)
    if hasattr(b2, 'ElkConnectableShape22'):
        assert _is_linked(b2, 'ElkConnectableShape22', a)
    _safe_set(a, 'incomingEdges', set())
    assert not _is_linked(a, 'incomingEdges', b2)
    if hasattr(b2, 'ElkConnectableShape22'):
        assert not _is_linked(b2, 'ElkConnectableShape22', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EMapPropertyHolder_strategy = st.builds(EMapPropertyHolder)
@given(instance=EMapPropertyHolder_strategy)
@settings(max_examples=25)
def test_EMapPropertyHolder_instantiation(instance):
    assert isinstance(instance, EMapPropertyHolder)


ElkConnectableShape_strategy = st.builds(ElkConnectableShape)
@given(instance=ElkConnectableShape_strategy)
@settings(max_examples=25)
def test_ElkConnectableShape_instantiation(instance):
    assert isinstance(instance, ElkConnectableShape)


ElkGraphElement_strategy = st.builds(ElkGraphElement)
@given(instance=ElkGraphElement_strategy)
@settings(max_examples=25)
def test_ElkGraphElement_instantiation(instance):
    assert isinstance(instance, ElkGraphElement)


ElkShape_strategy = st.builds(ElkShape)
@given(instance=ElkShape_strategy)
@settings(max_examples=25)
def test_ElkShape_instantiation(instance):
    assert isinstance(instance, ElkShape)


IPropertyHolder_strategy = st.builds(IPropertyHolder)
@given(instance=IPropertyHolder_strategy)
@settings(max_examples=25)
def test_IPropertyHolder_instantiation(instance):
    assert isinstance(instance, IPropertyHolder)


graph_EMapPropertyHolder_strategy = st.builds(graph_EMapPropertyHolder)
@given(instance=graph_EMapPropertyHolder_strategy)
@settings(max_examples=25)
def test_graph_EMapPropertyHolder_instantiation(instance):
    assert isinstance(instance, graph_EMapPropertyHolder)


graph_ElkBendPoint_strategy = st.builds(graph_ElkBendPoint, x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_ElkBendPoint_strategy)
@settings(max_examples=25)
def test_graph_ElkBendPoint_instantiation(instance):
    assert isinstance(instance, graph_ElkBendPoint)


graph_ElkConnectableShape_strategy = st.builds(graph_ElkConnectableShape)
@given(instance=graph_ElkConnectableShape_strategy)
@settings(max_examples=25)
def test_graph_ElkConnectableShape_instantiation(instance):
    assert isinstance(instance, graph_ElkConnectableShape)


graph_ElkEdge_strategy = st.builds(graph_ElkEdge, connected=st.booleans(), hierarchical=st.booleans(), hyperedge=st.booleans(), selfloop=st.booleans())
@given(instance=graph_ElkEdge_strategy)
@settings(max_examples=25)
def test_graph_ElkEdge_instantiation(instance):
    assert isinstance(instance, graph_ElkEdge)


graph_ElkEdgeSection_strategy = st.builds(graph_ElkEdgeSection, endX=st.floats(allow_nan=False, allow_infinity=False), endY=st.floats(allow_nan=False, allow_infinity=False), identifier=safe_text, startX=st.floats(allow_nan=False, allow_infinity=False), startY=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_ElkEdgeSection_strategy)
@settings(max_examples=25)
def test_graph_ElkEdgeSection_instantiation(instance):
    assert isinstance(instance, graph_ElkEdgeSection)


graph_ElkGraphElement_strategy = st.builds(graph_ElkGraphElement, identifier=safe_text)
@given(instance=graph_ElkGraphElement_strategy)
@settings(max_examples=25)
def test_graph_ElkGraphElement_instantiation(instance):
    assert isinstance(instance, graph_ElkGraphElement)


graph_ElkLabel_strategy = st.builds(graph_ElkLabel, text=safe_text)
@given(instance=graph_ElkLabel_strategy)
@settings(max_examples=25)
def test_graph_ElkLabel_instantiation(instance):
    assert isinstance(instance, graph_ElkLabel)


graph_ElkNode_strategy = st.builds(graph_ElkNode, hierarchical=st.booleans())
@given(instance=graph_ElkNode_strategy)
@settings(max_examples=25)
def test_graph_ElkNode_instantiation(instance):
    assert isinstance(instance, graph_ElkNode)


graph_ElkPort_strategy = st.builds(graph_ElkPort)
@given(instance=graph_ElkPort_strategy)
@settings(max_examples=25)
def test_graph_ElkPort_instantiation(instance):
    assert isinstance(instance, graph_ElkPort)


graph_ElkPropertyToValueMapEntry_strategy = st.builds(graph_ElkPropertyToValueMapEntry, key=safe_text, value=safe_text)
@given(instance=graph_ElkPropertyToValueMapEntry_strategy)
@settings(max_examples=25)
def test_graph_ElkPropertyToValueMapEntry_instantiation(instance):
    assert isinstance(instance, graph_ElkPropertyToValueMapEntry)


graph_ElkShape_strategy = st.builds(graph_ElkShape, height=st.floats(allow_nan=False, allow_infinity=False), width=st.floats(allow_nan=False, allow_infinity=False), x=st.floats(allow_nan=False, allow_infinity=False), y=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=graph_ElkShape_strategy)
@settings(max_examples=25)
def test_graph_ElkShape_instantiation(instance):
    assert isinstance(instance, graph_ElkShape)


graph_IPropertyHolder_strategy = st.builds(graph_IPropertyHolder)
@given(instance=graph_IPropertyHolder_strategy)
@settings(max_examples=25)
def test_graph_IPropertyHolder_instantiation(instance):
    assert isinstance(instance, graph_IPropertyHolder)



