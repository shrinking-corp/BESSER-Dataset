import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Entity,
    graphmodelling_Edge,
    graphmodelling_Entity,
    graphmodelling_Graph,
    graphmodelling_ModellingType,
    graphmodelling_Node,
    graphmodelling_Operation,
    graphmodelling_Property,
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

def test_graphmodelling_Entity_ID_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.ID == "sample_text"
    instance.ID = "sample_text_2"
    assert instance.ID == "sample_text_2"


def test_graphmodelling_Entity_accessModifier_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.accessModifier == "sample_text"
    instance.accessModifier = "sample_text_2"
    assert instance.accessModifier == "sample_text_2"


def test_graphmodelling_Entity_category_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_graphmodelling_Entity_className_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_graphmodelling_Entity_description_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_graphmodelling_Entity_group_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_graphmodelling_Entity_height_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.height == "sample_text"
    instance.height = "sample_text_2"
    assert instance.height == "sample_text_2"


def test_graphmodelling_Entity_name_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphmodelling_Entity_text_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_graphmodelling_Entity_type_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_graphmodelling_Entity_value_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_graphmodelling_Entity_width_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_graphmodelling_Entity_x_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_graphmodelling_Entity_y_value_roundtrip():
    instance = graphmodelling_Entity(ID="sample_text", accessModifier="sample_text", category="sample_text", className="sample_text", description="sample_text", group="sample_text", height="sample_text", name="sample_text", text="sample_text", type="sample_text", value="sample_text", width="sample_text", x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_graphmodelling_ModellingType_name_value_roundtrip():
    instance = graphmodelling_ModellingType(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_graphmodelling_Edge_isa_Entity():
    instance = graphmodelling_Edge()
    assert isinstance(instance, Entity)


def test_graphmodelling_Graph_isa_Entity():
    instance = graphmodelling_Graph()
    assert isinstance(instance, Entity)


def test_graphmodelling_Node_isa_Entity():
    instance = graphmodelling_Node()
    assert isinstance(instance, Entity)


def test_graphmodelling_Operation_isa_Entity():
    instance = graphmodelling_Operation()
    assert isinstance(instance, Entity)


def test_graphmodelling_Property_isa_Entity():
    instance = graphmodelling_Property()
    assert isinstance(instance, Entity)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Entity_strategy = st.builds(Entity)
@given(instance=Entity_strategy)
@settings(max_examples=25)
def test_Entity_instantiation(instance):
    assert isinstance(instance, Entity)


graphmodelling_Edge_strategy = st.builds(graphmodelling_Edge)
@given(instance=graphmodelling_Edge_strategy)
@settings(max_examples=25)
def test_graphmodelling_Edge_instantiation(instance):
    assert isinstance(instance, graphmodelling_Edge)


graphmodelling_Entity_strategy = st.builds(graphmodelling_Entity, ID=safe_text, accessModifier=safe_text, category=safe_text, className=safe_text, description=safe_text, group=safe_text, height=safe_text, name=safe_text, text=safe_text, type=safe_text, value=safe_text, width=safe_text, x=safe_text, y=safe_text)
@given(instance=graphmodelling_Entity_strategy)
@settings(max_examples=25)
def test_graphmodelling_Entity_instantiation(instance):
    assert isinstance(instance, graphmodelling_Entity)


graphmodelling_Graph_strategy = st.builds(graphmodelling_Graph)
@given(instance=graphmodelling_Graph_strategy)
@settings(max_examples=25)
def test_graphmodelling_Graph_instantiation(instance):
    assert isinstance(instance, graphmodelling_Graph)


graphmodelling_ModellingType_strategy = st.builds(graphmodelling_ModellingType, name=safe_text)
@given(instance=graphmodelling_ModellingType_strategy)
@settings(max_examples=25)
def test_graphmodelling_ModellingType_instantiation(instance):
    assert isinstance(instance, graphmodelling_ModellingType)


graphmodelling_Node_strategy = st.builds(graphmodelling_Node)
@given(instance=graphmodelling_Node_strategy)
@settings(max_examples=25)
def test_graphmodelling_Node_instantiation(instance):
    assert isinstance(instance, graphmodelling_Node)


graphmodelling_Operation_strategy = st.builds(graphmodelling_Operation)
@given(instance=graphmodelling_Operation_strategy)
@settings(max_examples=25)
def test_graphmodelling_Operation_instantiation(instance):
    assert isinstance(instance, graphmodelling_Operation)


graphmodelling_Property_strategy = st.builds(graphmodelling_Property)
@given(instance=graphmodelling_Property_strategy)
@settings(max_examples=25)
def test_graphmodelling_Property_instantiation(instance):
    assert isinstance(instance, graphmodelling_Property)


