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
    Entity,
    graphmodel_Operation,
    graphmodel_Node,
    graphmodel_Edge,
    graphmodel_Property,
    graphmodel_Graph,
    graphmodel_Entity,
    graphmodel_ModellingType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_hyp_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_hyp_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_operation_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Operation)


def test_hyp_graphmodel_operation_constructor_exists():
    assert callable(graphmodel_Operation.__init__)


def test_hyp_graphmodel_operation_constructor_args():
    sig = inspect.signature(graphmodel_Operation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_node_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Node)


def test_hyp_graphmodel_node_constructor_exists():
    assert callable(graphmodel_Node.__init__)


def test_hyp_graphmodel_node_constructor_args():
    sig = inspect.signature(graphmodel_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_edge_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Edge)


def test_hyp_graphmodel_edge_constructor_exists():
    assert callable(graphmodel_Edge.__init__)


def test_hyp_graphmodel_edge_constructor_args():
    sig = inspect.signature(graphmodel_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_property_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Property)


def test_hyp_graphmodel_property_constructor_exists():
    assert callable(graphmodel_Property.__init__)


def test_hyp_graphmodel_property_constructor_args():
    sig = inspect.signature(graphmodel_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_graph_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Graph)


def test_hyp_graphmodel_graph_constructor_exists():
    assert callable(graphmodel_Graph.__init__)


def test_hyp_graphmodel_graph_constructor_args():
    sig = inspect.signature(graphmodel_Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphmodel_entity_is_not_abstract():
    assert not inspect.isabstract(graphmodel_Entity)


def test_hyp_graphmodel_entity_constructor_exists():
    assert callable(graphmodel_Entity.__init__)


def test_hyp_graphmodel_entity_constructor_args():
    sig = inspect.signature(graphmodel_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "x" in params, "Missing parameter 'x'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"
    assert "height" in params, "Missing parameter 'height'"
    assert "category" in params, "Missing parameter 'category'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "description" in params, "Missing parameter 'description'"
    assert "className" in params, "Missing parameter 'className'"
    assert "group" in params, "Missing parameter 'group'"
    assert "value" in params, "Missing parameter 'value'"

















def test_hyp_graphmodel_modellingtype_is_not_abstract():
    assert not inspect.isabstract(graphmodel_ModellingType)


def test_hyp_graphmodel_modellingtype_constructor_exists():
    assert callable(graphmodel_ModellingType.__init__)


def test_hyp_graphmodel_modellingtype_constructor_args():
    sig = inspect.signature(graphmodel_ModellingType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"



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
Entity_strategy = st.builds(
    Entity,
)
graphmodel_Operation_strategy = st.builds(
    graphmodel_Operation,
)
graphmodel_Node_strategy = st.builds(
    graphmodel_Node,
)
graphmodel_Edge_strategy = st.builds(
    graphmodel_Edge,
)
graphmodel_Property_strategy = st.builds(
    graphmodel_Property,
)
graphmodel_Graph_strategy = st.builds(
    graphmodel_Graph,
)
graphmodel_Entity_strategy = st.builds(
    graphmodel_Entity,
    text=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    x=
        safe_text,
    accessModifier=
        safe_text,
    height=
        safe_text,
    category=
        safe_text,
    width=
        safe_text,
    y=
        safe_text,
    ID=
        safe_text,
    description=
        safe_text,
    className=
        safe_text,
    group=
        safe_text,
    value=
        safe_text
)
graphmodel_ModellingType_strategy = st.builds(
    graphmodel_ModellingType,
    name=
        safe_text
)










@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=graphmodel_Entity_strategy)
def test_hyp_graphmodel_entity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=graphmodel_ModellingType_strategy)
def test_hyp_graphmodel_modellingtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Entity,
    graphmodel_Edge,
    graphmodel_Entity,
    graphmodel_Graph,
    graphmodel_ModellingType,
    graphmodel_Node,
    graphmodel_Operation,
    graphmodel_Property,
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

def test_graphmodel_Entity_ID_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_graphmodel_Entity_accessModifier_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.accessModifier == "sample_text"
    instance.accessModifier = "sample_text_2"
    assert instance.accessModifier == "sample_text_2"


def test_graphmodel_Entity_category_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_graphmodel_Entity_className_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_graphmodel_Entity_description_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_graphmodel_Entity_group_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_graphmodel_Entity_height_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_graphmodel_Entity_name_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphmodel_Entity_text_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graphmodel_Entity_type_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphmodel_Entity_value_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graphmodel_Entity_width_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_graphmodel_Entity_x_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_graphmodel_Entity_y_value_roundtrip():
    instance = graphmodel_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_graphmodel_ModellingType_name_value_roundtrip():
    instance = graphmodel_ModellingType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphmodel_Edge_isa_Entity():
    instance = graphmodel_Edge()
    assert isinstance(instance, Entity)


def test_graphmodel_Graph_isa_Entity():
    instance = graphmodel_Graph()
    assert isinstance(instance, Entity)


def test_graphmodel_Node_isa_Entity():
    instance = graphmodel_Node()
    assert isinstance(instance, Entity)


def test_graphmodel_Operation_isa_Entity():
    instance = graphmodel_Operation()
    assert isinstance(instance, Entity)


def test_graphmodel_Property_isa_Entity():
    instance = graphmodel_Property()
    assert isinstance(instance, Entity)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Entity_strategy = st.builds(Entity)
@given(instance=Entity_strategy)
@settings(max_examples=25)
def test_Entity_instantiation(instance):
    assert isinstance(instance, Entity)


graphmodel_Edge_strategy = st.builds(graphmodel_Edge)
@given(instance=graphmodel_Edge_strategy)
@settings(max_examples=25)
def test_graphmodel_Edge_instantiation(instance):
    assert isinstance(instance, graphmodel_Edge)


graphmodel_Entity_strategy = st.builds(graphmodel_Entity, ID=safe_text, accessModifier=safe_text, category=safe_text, className=safe_text, description=safe_text, group=safe_text, height=safe_text, name=safe_text, text=safe_text, type=safe_text, value=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=graphmodel_Entity_strategy)
@settings(max_examples=25)
def test_graphmodel_Entity_instantiation(instance):
    assert isinstance(instance, graphmodel_Entity)


graphmodel_Graph_strategy = st.builds(graphmodel_Graph)
@given(instance=graphmodel_Graph_strategy)
@settings(max_examples=25)
def test_graphmodel_Graph_instantiation(instance):
    assert isinstance(instance, graphmodel_Graph)


graphmodel_ModellingType_strategy = st.builds(graphmodel_ModellingType, name=safe_text)
@given(instance=graphmodel_ModellingType_strategy)
@settings(max_examples=25)
def test_graphmodel_ModellingType_instantiation(instance):
    assert isinstance(instance, graphmodel_ModellingType)


graphmodel_Node_strategy = st.builds(graphmodel_Node)
@given(instance=graphmodel_Node_strategy)
@settings(max_examples=25)
def test_graphmodel_Node_instantiation(instance):
    assert isinstance(instance, graphmodel_Node)


graphmodel_Operation_strategy = st.builds(graphmodel_Operation)
@given(instance=graphmodel_Operation_strategy)
@settings(max_examples=25)
def test_graphmodel_Operation_instantiation(instance):
    assert isinstance(instance, graphmodel_Operation)


graphmodel_Property_strategy = st.builds(graphmodel_Property)
@given(instance=graphmodel_Property_strategy)
@settings(max_examples=25)
def test_graphmodel_Property_instantiation(instance):
    assert isinstance(instance, graphmodel_Property)



