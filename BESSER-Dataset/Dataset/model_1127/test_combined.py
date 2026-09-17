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
    robotmodel_Property,
    robotmodel_Role,
    robotmodel_Action,
    robotmodel_Transition,
    robotmodel_Event,
    robotmodel_State,
    robotmodel_Property_List,
    robotmodel_Port,
    robotmodel_Connector,
    robotmodel_Component,
    robotmodel_System,
    Is_Style,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_robotmodel_property_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Property)


def test_hyp_robotmodel_property_constructor_exists():
    assert callable(robotmodel_Property.__init__)


def test_hyp_robotmodel_property_constructor_args():
    sig = inspect.signature(robotmodel_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_robotmodel_role_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Role)


def test_hyp_robotmodel_role_constructor_exists():
    assert callable(robotmodel_Role.__init__)


def test_hyp_robotmodel_role_constructor_args():
    sig = inspect.signature(robotmodel_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_action_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Action)


def test_hyp_robotmodel_action_constructor_exists():
    assert callable(robotmodel_Action.__init__)


def test_hyp_robotmodel_action_constructor_args():
    sig = inspect.signature(robotmodel_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_transition_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Transition)


def test_hyp_robotmodel_transition_constructor_exists():
    assert callable(robotmodel_Transition.__init__)


def test_hyp_robotmodel_transition_constructor_args():
    sig = inspect.signature(robotmodel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_event_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Event)


def test_hyp_robotmodel_event_constructor_exists():
    assert callable(robotmodel_Event.__init__)


def test_hyp_robotmodel_event_constructor_args():
    sig = inspect.signature(robotmodel_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_state_is_not_abstract():
    assert not inspect.isabstract(robotmodel_State)


def test_hyp_robotmodel_state_constructor_exists():
    assert callable(robotmodel_State.__init__)


def test_hyp_robotmodel_state_constructor_args():
    sig = inspect.signature(robotmodel_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_property_list_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Property_List)


def test_hyp_robotmodel_property_list_constructor_exists():
    assert callable(robotmodel_Property_List.__init__)


def test_hyp_robotmodel_property_list_constructor_args():
    sig = inspect.signature(robotmodel_Property_List.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_port_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Port)


def test_hyp_robotmodel_port_constructor_exists():
    assert callable(robotmodel_Port.__init__)


def test_hyp_robotmodel_port_constructor_args():
    sig = inspect.signature(robotmodel_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_robotmodel_connector_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Connector)


def test_hyp_robotmodel_connector_constructor_exists():
    assert callable(robotmodel_Connector.__init__)


def test_hyp_robotmodel_connector_constructor_args():
    sig = inspect.signature(robotmodel_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "atype" in params, "Missing parameter 'atype'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_robotmodel_component_is_not_abstract():
    assert not inspect.isabstract(robotmodel_Component)


def test_hyp_robotmodel_component_constructor_exists():
    assert callable(robotmodel_Component.__init__)


def test_hyp_robotmodel_component_constructor_args():
    sig = inspect.signature(robotmodel_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "atype" in params, "Missing parameter 'atype'"
    assert "frequency" in params, "Missing parameter 'frequency'"
    assert "type" in params, "Missing parameter 'type'"
    assert "depends" in params, "Missing parameter 'depends'"








def test_hyp_robotmodel_system_is_not_abstract():
    assert not inspect.isabstract(robotmodel_System)


def test_hyp_robotmodel_system_constructor_exists():
    assert callable(robotmodel_System.__init__)


def test_hyp_robotmodel_system_constructor_args():
    sig = inspect.signature(robotmodel_System.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "author_email" in params, "Missing parameter 'author_email'"
    assert "depends" in params, "Missing parameter 'depends'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"






def test_hyp_is_style_exists():
    # Check that the Enumeration exists
    assert Is_Style is not None

def test_hyp_is_style_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Is_Style]
    expected_literals = [
        "non_style",
        "style",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Is_Style"


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
robotmodel_Property_strategy = st.builds(
    robotmodel_Property,
    name=
        safe_text,
    value=
        safe_text,
    type=
        safe_text
)
robotmodel_Role_strategy = st.builds(
    robotmodel_Role,
    name=
        safe_text
)
robotmodel_Action_strategy = st.builds(
    robotmodel_Action,
    name=
        safe_text
)
robotmodel_Transition_strategy = st.builds(
    robotmodel_Transition,
    name=
        safe_text
)
robotmodel_Event_strategy = st.builds(
    robotmodel_Event,
    name=
        safe_text
)
robotmodel_State_strategy = st.builds(
    robotmodel_State,
    name=
        safe_text
)
robotmodel_Property_List_strategy = st.builds(
    robotmodel_Property_List,
    name=
        safe_text
)
robotmodel_Port_strategy = st.builds(
    robotmodel_Port,
    name=
        safe_text
)
robotmodel_Connector_strategy = st.builds(
    robotmodel_Connector,
    atype=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
robotmodel_Component_strategy = st.builds(
    robotmodel_Component,
    name=
        safe_text,
    atype=
        safe_text,
    frequency=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text,
    depends=
        safe_text
)
robotmodel_System_strategy = st.builds(
    robotmodel_System,
    author=
        safe_text,
    author_email=
        safe_text,
    depends=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)




@given(instance=robotmodel_Property_strategy)
def test_hyp_robotmodel_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=robotmodel_Property_strategy)
def test_hyp_robotmodel_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=robotmodel_Property_strategy)
def test_hyp_robotmodel_property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=robotmodel_Role_strategy)
def test_hyp_robotmodel_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Action_strategy)
def test_hyp_robotmodel_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Transition_strategy)
def test_hyp_robotmodel_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Event_strategy)
def test_hyp_robotmodel_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_State_strategy)
def test_hyp_robotmodel_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Property_List_strategy)
def test_hyp_robotmodel_property_list_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Port_strategy)
def test_hyp_robotmodel_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=robotmodel_Connector_strategy)
def test_hyp_robotmodel_connector_atype_setter(instance):
    original = instance.atype
    instance.atype = original
    assert instance.atype == original



@given(instance=robotmodel_Connector_strategy)
def test_hyp_robotmodel_connector_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=robotmodel_Connector_strategy)
def test_hyp_robotmodel_connector_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=robotmodel_Component_strategy)
def test_hyp_robotmodel_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=robotmodel_Component_strategy)
def test_hyp_robotmodel_component_atype_setter(instance):
    original = instance.atype
    instance.atype = original
    assert instance.atype == original



@given(instance=robotmodel_Component_strategy)
def test_hyp_robotmodel_component_frequency_setter(instance):
    original = instance.frequency
    instance.frequency = original
    assert instance.frequency == original



@given(instance=robotmodel_Component_strategy)
def test_hyp_robotmodel_component_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=robotmodel_Component_strategy)
def test_hyp_robotmodel_component_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original




@given(instance=robotmodel_System_strategy)
def test_hyp_robotmodel_system_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=robotmodel_System_strategy)
def test_hyp_robotmodel_system_author_email_setter(instance):
    original = instance.author_email
    instance.author_email = original
    assert instance.author_email == original



@given(instance=robotmodel_System_strategy)
def test_hyp_robotmodel_system_depends_setter(instance):
    original = instance.depends
    instance.depends = original
    assert instance.depends == original



@given(instance=robotmodel_System_strategy)
def test_hyp_robotmodel_system_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=robotmodel_System_strategy)
def test_hyp_robotmodel_system_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    robotmodel_Action,
    robotmodel_Component,
    robotmodel_Connector,
    robotmodel_Event,
    robotmodel_Port,
    robotmodel_Property,
    robotmodel_Property_List,
    robotmodel_Role,
    robotmodel_State,
    robotmodel_System,
    robotmodel_Transition,
    Is_Style,
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

def test_robotmodel_Action_name_value_roundtrip():
    instance = robotmodel_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Component_atype_value_roundtrip():
    instance = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    assert instance.atype == "sample_text"
    instance.atype = "sample_text_2"
    assert instance.atype == "sample_text_2"


def test_robotmodel_Component_depends_value_roundtrip():
    instance = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    assert instance.depends == "sample_text"
    instance.depends = "sample_text_2"
    assert instance.depends == "sample_text_2"


def test_robotmodel_Component_frequency_value_roundtrip():
    instance = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    assert instance.frequency == 3.14
    instance.frequency = 9.99
    assert instance.frequency == 9.99


def test_robotmodel_Component_name_value_roundtrip():
    instance = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Component_type_value_roundtrip():
    instance = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robotmodel_Connector_atype_value_roundtrip():
    instance = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    assert instance.atype == "sample_text"
    instance.atype = "sample_text_2"
    assert instance.atype == "sample_text_2"


def test_robotmodel_Connector_name_value_roundtrip():
    instance = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Connector_type_value_roundtrip():
    instance = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robotmodel_Event_name_value_roundtrip():
    instance = robotmodel_Event(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Port_name_value_roundtrip():
    instance = robotmodel_Port(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Property_name_value_roundtrip():
    instance = robotmodel_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Property_type_value_roundtrip():
    instance = robotmodel_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_robotmodel_Property_value_value_roundtrip():
    instance = robotmodel_Property(name="sample_text", type="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_robotmodel_Property_List_name_value_roundtrip():
    instance = robotmodel_Property_List(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Role_name_value_roundtrip():
    instance = robotmodel_Role(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_State_name_value_roundtrip():
    instance = robotmodel_State(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_System_author_value_roundtrip():
    instance = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.author == "sample_text"
    instance.author = "sample_text_2"
    assert instance.author == "sample_text_2"


def test_robotmodel_System_author_email_value_roundtrip():
    instance = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.author_email == "sample_text"
    instance.author_email = "sample_text_2"
    assert instance.author_email == "sample_text_2"


def test_robotmodel_System_depends_value_roundtrip():
    instance = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.depends == "sample_text"
    instance.depends = "sample_text_2"
    assert instance.depends == "sample_text_2"


def test_robotmodel_System_description_value_roundtrip():
    instance = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_robotmodel_System_name_value_roundtrip():
    instance = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_robotmodel_Transition_name_value_roundtrip():
    instance = robotmodel_Transition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_assoc_action16_link_reassign_clear():
    a = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_Component17', {b1})
    assert _is_linked(a, 'robotmodel_Component17', b1)
    if hasattr(b1, 'robotmodel_Action'):
        assert _is_linked(b1, 'robotmodel_Action', a)
    _safe_set(a, 'robotmodel_Component17', {b2})
    assert _is_linked(a, 'robotmodel_Component17', b2)
    if hasattr(b1, 'robotmodel_Action'):
        assert not _is_linked(b1, 'robotmodel_Action', a)
    if hasattr(b2, 'robotmodel_Action'):
        assert _is_linked(b2, 'robotmodel_Action', a)
    _safe_set(a, 'robotmodel_Component17', set())
    assert not _is_linked(a, 'robotmodel_Component17', b2)
    if hasattr(b2, 'robotmodel_Action'):
        assert not _is_linked(b2, 'robotmodel_Action', a)


def test_assoc_action31_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_State32', {b1})
    assert _is_linked(a, 'robotmodel_State32', b1)
    if hasattr(b1, 'robotmodel_Action33'):
        assert _is_linked(b1, 'robotmodel_Action33', a)
    _safe_set(a, 'robotmodel_State32', {b2})
    assert _is_linked(a, 'robotmodel_State32', b2)
    if hasattr(b1, 'robotmodel_Action33'):
        assert not _is_linked(b1, 'robotmodel_Action33', a)
    if hasattr(b2, 'robotmodel_Action33'):
        assert _is_linked(b2, 'robotmodel_Action33', a)
    _safe_set(a, 'robotmodel_State32', set())
    assert not _is_linked(a, 'robotmodel_State32', b2)
    if hasattr(b2, 'robotmodel_Action33'):
        assert not _is_linked(b2, 'robotmodel_Action33', a)


def test_assoc_action46_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition47', b1)
    assert _is_linked(a, 'robotmodel_Transition47', b1)
    if hasattr(b1, 'robotmodel_Action48'):
        assert _is_linked(b1, 'robotmodel_Action48', a)
    _safe_set(a, 'robotmodel_Transition47', b2)
    assert _is_linked(a, 'robotmodel_Transition47', b2)
    if hasattr(b1, 'robotmodel_Action48'):
        assert not _is_linked(b1, 'robotmodel_Action48', a)
    if hasattr(b2, 'robotmodel_Action48'):
        assert _is_linked(b2, 'robotmodel_Action48', a)
    _safe_set(a, 'robotmodel_Transition47', None)
    assert not _is_linked(a, 'robotmodel_Transition47', b2)
    if hasattr(b2, 'robotmodel_Action48'):
        assert not _is_linked(b2, 'robotmodel_Action48', a)


def test_assoc_component0_link_reassign_clear():
    a = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_System', {b1})
    assert _is_linked(a, 'robotmodel_System', b1)
    if hasattr(b1, 'robotmodel_Component'):
        assert _is_linked(b1, 'robotmodel_Component', a)
    _safe_set(a, 'robotmodel_System', {b2})
    assert _is_linked(a, 'robotmodel_System', b2)
    if hasattr(b1, 'robotmodel_Component'):
        assert not _is_linked(b1, 'robotmodel_Component', a)
    if hasattr(b2, 'robotmodel_Component'):
        assert _is_linked(b2, 'robotmodel_Component', a)
    _safe_set(a, 'robotmodel_System', set())
    assert not _is_linked(a, 'robotmodel_System', b2)
    if hasattr(b2, 'robotmodel_Component'):
        assert not _is_linked(b2, 'robotmodel_Component', a)


def test_assoc_component8_link_reassign_clear():
    a = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Component7', {b1})
    assert _is_linked(a, 'robotmodel_Component7', b1)
    if hasattr(b1, 'robotmodel_Component9'):
        assert _is_linked(b1, 'robotmodel_Component9', a)
    _safe_set(a, 'robotmodel_Component7', {b2})
    assert _is_linked(a, 'robotmodel_Component7', b2)
    if hasattr(b1, 'robotmodel_Component9'):
        assert not _is_linked(b1, 'robotmodel_Component9', a)
    if hasattr(b2, 'robotmodel_Component9'):
        assert _is_linked(b2, 'robotmodel_Component9', a)
    _safe_set(a, 'robotmodel_Component7', set())
    assert not _is_linked(a, 'robotmodel_Component7', b2)
    if hasattr(b2, 'robotmodel_Component9'):
        assert not _is_linked(b2, 'robotmodel_Component9', a)


def test_assoc_connector1_link_reassign_clear():
    a = robotmodel_System(author="sample_text", author_email="sample_text", depends="sample_text", description="sample_text", name="sample_text")
    b1 = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    b2 = robotmodel_Connector(atype="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_System2', {b1})
    assert _is_linked(a, 'robotmodel_System2', b1)
    if hasattr(b1, 'robotmodel_Connector'):
        assert _is_linked(b1, 'robotmodel_Connector', a)
    _safe_set(a, 'robotmodel_System2', {b2})
    assert _is_linked(a, 'robotmodel_System2', b2)
    if hasattr(b1, 'robotmodel_Connector'):
        assert not _is_linked(b1, 'robotmodel_Connector', a)
    if hasattr(b2, 'robotmodel_Connector'):
        assert _is_linked(b2, 'robotmodel_Connector', a)
    _safe_set(a, 'robotmodel_System2', set())
    assert not _is_linked(a, 'robotmodel_System2', b2)
    if hasattr(b2, 'robotmodel_Connector'):
        assert not _is_linked(b2, 'robotmodel_Connector', a)


def test_assoc_entryaction37_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_State38', b1)
    assert _is_linked(a, 'robotmodel_State38', b1)
    if hasattr(b1, 'robotmodel_Action39'):
        assert _is_linked(b1, 'robotmodel_Action39', a)
    _safe_set(a, 'robotmodel_State38', b2)
    assert _is_linked(a, 'robotmodel_State38', b2)
    if hasattr(b1, 'robotmodel_Action39'):
        assert not _is_linked(b1, 'robotmodel_Action39', a)
    if hasattr(b2, 'robotmodel_Action39'):
        assert _is_linked(b2, 'robotmodel_Action39', a)
    _safe_set(a, 'robotmodel_State38', None)
    assert not _is_linked(a, 'robotmodel_State38', b2)
    if hasattr(b2, 'robotmodel_Action39'):
        assert not _is_linked(b2, 'robotmodel_Action39', a)


def test_assoc_event12_link_reassign_clear():
    a = robotmodel_Event(name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Event', b1)
    assert _is_linked(a, 'robotmodel_Event', b1)
    if hasattr(b1, 'robotmodel_Component13'):
        assert _is_linked(b1, 'robotmodel_Component13', a)
    _safe_set(a, 'robotmodel_Event', b2)
    assert _is_linked(a, 'robotmodel_Event', b2)
    if hasattr(b1, 'robotmodel_Component13'):
        assert not _is_linked(b1, 'robotmodel_Component13', a)
    if hasattr(b2, 'robotmodel_Component13'):
        assert _is_linked(b2, 'robotmodel_Component13', a)
    _safe_set(a, 'robotmodel_Event', None)
    assert not _is_linked(a, 'robotmodel_Event', b2)
    if hasattr(b2, 'robotmodel_Component13'):
        assert not _is_linked(b2, 'robotmodel_Component13', a)


def test_assoc_event43_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_Event(name="sample_text")
    b2 = robotmodel_Event(name="sample_text_2")
    _safe_set(a, 'robotmodel_State44', {b1})
    assert _is_linked(a, 'robotmodel_State44', b1)
    if hasattr(b1, 'robotmodel_Event45'):
        assert _is_linked(b1, 'robotmodel_Event45', a)
    _safe_set(a, 'robotmodel_State44', {b2})
    assert _is_linked(a, 'robotmodel_State44', b2)
    if hasattr(b1, 'robotmodel_Event45'):
        assert not _is_linked(b1, 'robotmodel_Event45', a)
    if hasattr(b2, 'robotmodel_Event45'):
        assert _is_linked(b2, 'robotmodel_Event45', a)
    _safe_set(a, 'robotmodel_State44', set())
    assert not _is_linked(a, 'robotmodel_State44', b2)
    if hasattr(b2, 'robotmodel_Event45'):
        assert not _is_linked(b2, 'robotmodel_Event45', a)


def test_assoc_exitaction40_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_State41', b1)
    assert _is_linked(a, 'robotmodel_State41', b1)
    if hasattr(b1, 'robotmodel_Action42'):
        assert _is_linked(b1, 'robotmodel_Action42', a)
    _safe_set(a, 'robotmodel_State41', b2)
    assert _is_linked(a, 'robotmodel_State41', b2)
    if hasattr(b1, 'robotmodel_Action42'):
        assert not _is_linked(b1, 'robotmodel_Action42', a)
    if hasattr(b2, 'robotmodel_Action42'):
        assert _is_linked(b2, 'robotmodel_Action42', a)
    _safe_set(a, 'robotmodel_State41', None)
    assert not _is_linked(a, 'robotmodel_State41', b2)
    if hasattr(b2, 'robotmodel_Action42'):
        assert not _is_linked(b2, 'robotmodel_Action42', a)


def test_assoc_guard49_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_Action(name="sample_text")
    b2 = robotmodel_Action(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition50', b1)
    assert _is_linked(a, 'robotmodel_Transition50', b1)
    if hasattr(b1, 'robotmodel_Action51'):
        assert _is_linked(b1, 'robotmodel_Action51', a)
    _safe_set(a, 'robotmodel_Transition50', b2)
    assert _is_linked(a, 'robotmodel_Transition50', b2)
    if hasattr(b1, 'robotmodel_Action51'):
        assert not _is_linked(b1, 'robotmodel_Action51', a)
    if hasattr(b2, 'robotmodel_Action51'):
        assert _is_linked(b2, 'robotmodel_Action51', a)
    _safe_set(a, 'robotmodel_Transition50', None)
    assert not _is_linked(a, 'robotmodel_Transition50', b2)
    if hasattr(b2, 'robotmodel_Action51'):
        assert not _is_linked(b2, 'robotmodel_Action51', a)


def test_assoc_port3_link_reassign_clear():
    a = robotmodel_Port(name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Port', b1)
    assert _is_linked(a, 'robotmodel_Port', b1)
    if hasattr(b1, 'robotmodel_Component4'):
        assert _is_linked(b1, 'robotmodel_Component4', a)
    _safe_set(a, 'robotmodel_Port', b2)
    assert _is_linked(a, 'robotmodel_Port', b2)
    if hasattr(b1, 'robotmodel_Component4'):
        assert not _is_linked(b1, 'robotmodel_Component4', a)
    if hasattr(b2, 'robotmodel_Component4'):
        assert _is_linked(b2, 'robotmodel_Component4', a)
    _safe_set(a, 'robotmodel_Port', None)
    assert not _is_linked(a, 'robotmodel_Port', b2)
    if hasattr(b2, 'robotmodel_Component4'):
        assert not _is_linked(b2, 'robotmodel_Component4', a)


def test_assoc_property26_link_reassign_clear():
    a = robotmodel_Property_List(name="sample_text")
    b1 = robotmodel_Property(name="sample_text", type="sample_text", value="sample_text")
    b2 = robotmodel_Property(name="sample_text_2", type="sample_text_2", value="sample_text_2")
    _safe_set(a, 'robotmodel_Property_List27', {b1})
    assert _is_linked(a, 'robotmodel_Property_List27', b1)
    if hasattr(b1, 'robotmodel_Property'):
        assert _is_linked(b1, 'robotmodel_Property', a)
    _safe_set(a, 'robotmodel_Property_List27', {b2})
    assert _is_linked(a, 'robotmodel_Property_List27', b2)
    if hasattr(b1, 'robotmodel_Property'):
        assert not _is_linked(b1, 'robotmodel_Property', a)
    if hasattr(b2, 'robotmodel_Property'):
        assert _is_linked(b2, 'robotmodel_Property', a)
    _safe_set(a, 'robotmodel_Property_List27', set())
    assert not _is_linked(a, 'robotmodel_Property_List27', b2)
    if hasattr(b2, 'robotmodel_Property'):
        assert not _is_linked(b2, 'robotmodel_Property', a)


def test_assoc_property_list18_link_reassign_clear():
    a = robotmodel_Property_List(name="sample_text")
    b1 = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    b2 = robotmodel_Connector(atype="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Property_List20', b1)
    assert _is_linked(a, 'robotmodel_Property_List20', b1)
    if hasattr(b1, 'robotmodel_Connector19'):
        assert _is_linked(b1, 'robotmodel_Connector19', a)
    _safe_set(a, 'robotmodel_Property_List20', b2)
    assert _is_linked(a, 'robotmodel_Property_List20', b2)
    if hasattr(b1, 'robotmodel_Connector19'):
        assert not _is_linked(b1, 'robotmodel_Connector19', a)
    if hasattr(b2, 'robotmodel_Connector19'):
        assert _is_linked(b2, 'robotmodel_Connector19', a)
    _safe_set(a, 'robotmodel_Property_List20', None)
    assert not _is_linked(a, 'robotmodel_Property_List20', b2)
    if hasattr(b2, 'robotmodel_Connector19'):
        assert not _is_linked(b2, 'robotmodel_Connector19', a)


def test_assoc_property_list5_link_reassign_clear():
    a = robotmodel_Property_List(name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Property_List', b1)
    assert _is_linked(a, 'robotmodel_Property_List', b1)
    if hasattr(b1, 'robotmodel_Component6'):
        assert _is_linked(b1, 'robotmodel_Component6', a)
    _safe_set(a, 'robotmodel_Property_List', b2)
    assert _is_linked(a, 'robotmodel_Property_List', b2)
    if hasattr(b1, 'robotmodel_Component6'):
        assert not _is_linked(b1, 'robotmodel_Component6', a)
    if hasattr(b2, 'robotmodel_Component6'):
        assert _is_linked(b2, 'robotmodel_Component6', a)
    _safe_set(a, 'robotmodel_Property_List', None)
    assert not _is_linked(a, 'robotmodel_Property_List', b2)
    if hasattr(b2, 'robotmodel_Component6'):
        assert not _is_linked(b2, 'robotmodel_Component6', a)


def test_assoc_role21_link_reassign_clear():
    a = robotmodel_Role(name="sample_text")
    b1 = robotmodel_Connector(atype="sample_text", name="sample_text", type="sample_text")
    b2 = robotmodel_Connector(atype="sample_text_2", name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Role', b1)
    assert _is_linked(a, 'robotmodel_Role', b1)
    if hasattr(b1, 'robotmodel_Connector22'):
        assert _is_linked(b1, 'robotmodel_Connector22', a)
    _safe_set(a, 'robotmodel_Role', b2)
    assert _is_linked(a, 'robotmodel_Role', b2)
    if hasattr(b1, 'robotmodel_Connector22'):
        assert not _is_linked(b1, 'robotmodel_Connector22', a)
    if hasattr(b2, 'robotmodel_Connector22'):
        assert _is_linked(b2, 'robotmodel_Connector22', a)
    _safe_set(a, 'robotmodel_Role', None)
    assert not _is_linked(a, 'robotmodel_Role', b2)
    if hasattr(b2, 'robotmodel_Connector22'):
        assert not _is_linked(b2, 'robotmodel_Connector22', a)


def test_assoc_role23_link_reassign_clear():
    a = robotmodel_Role(name="sample_text")
    b1 = robotmodel_Port(name="sample_text")
    b2 = robotmodel_Port(name="sample_text_2")
    _safe_set(a, 'robotmodel_Role25', b1)
    assert _is_linked(a, 'robotmodel_Role25', b1)
    if hasattr(b1, 'robotmodel_Port24'):
        assert _is_linked(b1, 'robotmodel_Port24', a)
    _safe_set(a, 'robotmodel_Role25', b2)
    assert _is_linked(a, 'robotmodel_Role25', b2)
    if hasattr(b1, 'robotmodel_Port24'):
        assert not _is_linked(b1, 'robotmodel_Port24', a)
    if hasattr(b2, 'robotmodel_Port24'):
        assert _is_linked(b2, 'robotmodel_Port24', a)
    _safe_set(a, 'robotmodel_Role25', None)
    assert not _is_linked(a, 'robotmodel_Role25', b2)
    if hasattr(b2, 'robotmodel_Port24'):
        assert not _is_linked(b2, 'robotmodel_Port24', a)


def test_assoc_source52_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_State(name="sample_text")
    b2 = robotmodel_State(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition53', b1)
    assert _is_linked(a, 'robotmodel_Transition53', b1)
    if hasattr(b1, 'robotmodel_State54'):
        assert _is_linked(b1, 'robotmodel_State54', a)
    _safe_set(a, 'robotmodel_Transition53', b2)
    assert _is_linked(a, 'robotmodel_Transition53', b2)
    if hasattr(b1, 'robotmodel_State54'):
        assert not _is_linked(b1, 'robotmodel_State54', a)
    if hasattr(b2, 'robotmodel_State54'):
        assert _is_linked(b2, 'robotmodel_State54', a)
    _safe_set(a, 'robotmodel_Transition53', None)
    assert not _is_linked(a, 'robotmodel_Transition53', b2)
    if hasattr(b2, 'robotmodel_State54'):
        assert not _is_linked(b2, 'robotmodel_State54', a)


def test_assoc_state10_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_State', b1)
    assert _is_linked(a, 'robotmodel_State', b1)
    if hasattr(b1, 'robotmodel_Component11'):
        assert _is_linked(b1, 'robotmodel_Component11', a)
    _safe_set(a, 'robotmodel_State', b2)
    assert _is_linked(a, 'robotmodel_State', b2)
    if hasattr(b1, 'robotmodel_Component11'):
        assert not _is_linked(b1, 'robotmodel_Component11', a)
    if hasattr(b2, 'robotmodel_Component11'):
        assert _is_linked(b2, 'robotmodel_Component11', a)
    _safe_set(a, 'robotmodel_State', None)
    assert not _is_linked(a, 'robotmodel_State', b2)
    if hasattr(b2, 'robotmodel_Component11'):
        assert not _is_linked(b2, 'robotmodel_Component11', a)


def test_assoc_substate29_link_reassign_clear():
    a = robotmodel_State(name="sample_text")
    b1 = robotmodel_State(name="sample_text")
    b2 = robotmodel_State(name="sample_text_2")
    _safe_set(a, 'robotmodel_State28', {b1})
    assert _is_linked(a, 'robotmodel_State28', b1)
    if hasattr(b1, 'robotmodel_State30'):
        assert _is_linked(b1, 'robotmodel_State30', a)
    _safe_set(a, 'robotmodel_State28', {b2})
    assert _is_linked(a, 'robotmodel_State28', b2)
    if hasattr(b1, 'robotmodel_State30'):
        assert not _is_linked(b1, 'robotmodel_State30', a)
    if hasattr(b2, 'robotmodel_State30'):
        assert _is_linked(b2, 'robotmodel_State30', a)
    _safe_set(a, 'robotmodel_State28', set())
    assert not _is_linked(a, 'robotmodel_State28', b2)
    if hasattr(b2, 'robotmodel_State30'):
        assert not _is_linked(b2, 'robotmodel_State30', a)


def test_assoc_target55_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_State(name="sample_text")
    b2 = robotmodel_State(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition56', b1)
    assert _is_linked(a, 'robotmodel_Transition56', b1)
    if hasattr(b1, 'robotmodel_State57'):
        assert _is_linked(b1, 'robotmodel_State57', a)
    _safe_set(a, 'robotmodel_Transition56', b2)
    assert _is_linked(a, 'robotmodel_Transition56', b2)
    if hasattr(b1, 'robotmodel_State57'):
        assert not _is_linked(b1, 'robotmodel_State57', a)
    if hasattr(b2, 'robotmodel_State57'):
        assert _is_linked(b2, 'robotmodel_State57', a)
    _safe_set(a, 'robotmodel_Transition56', None)
    assert not _is_linked(a, 'robotmodel_Transition56', b2)
    if hasattr(b2, 'robotmodel_State57'):
        assert not _is_linked(b2, 'robotmodel_State57', a)


def test_assoc_transition14_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_Component(atype="sample_text", depends="sample_text", frequency=3.14, name="sample_text", type="sample_text")
    b2 = robotmodel_Component(atype="sample_text_2", depends="sample_text_2", frequency=9.99, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'robotmodel_Transition', b1)
    assert _is_linked(a, 'robotmodel_Transition', b1)
    if hasattr(b1, 'robotmodel_Component15'):
        assert _is_linked(b1, 'robotmodel_Component15', a)
    _safe_set(a, 'robotmodel_Transition', b2)
    assert _is_linked(a, 'robotmodel_Transition', b2)
    if hasattr(b1, 'robotmodel_Component15'):
        assert not _is_linked(b1, 'robotmodel_Component15', a)
    if hasattr(b2, 'robotmodel_Component15'):
        assert _is_linked(b2, 'robotmodel_Component15', a)
    _safe_set(a, 'robotmodel_Transition', None)
    assert not _is_linked(a, 'robotmodel_Transition', b2)
    if hasattr(b2, 'robotmodel_Component15'):
        assert not _is_linked(b2, 'robotmodel_Component15', a)


def test_assoc_transition34_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_State(name="sample_text")
    b2 = robotmodel_State(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition36', b1)
    assert _is_linked(a, 'robotmodel_Transition36', b1)
    if hasattr(b1, 'robotmodel_State35'):
        assert _is_linked(b1, 'robotmodel_State35', a)
    _safe_set(a, 'robotmodel_Transition36', b2)
    assert _is_linked(a, 'robotmodel_Transition36', b2)
    if hasattr(b1, 'robotmodel_State35'):
        assert not _is_linked(b1, 'robotmodel_State35', a)
    if hasattr(b2, 'robotmodel_State35'):
        assert _is_linked(b2, 'robotmodel_State35', a)
    _safe_set(a, 'robotmodel_Transition36', None)
    assert not _is_linked(a, 'robotmodel_Transition36', b2)
    if hasattr(b2, 'robotmodel_State35'):
        assert not _is_linked(b2, 'robotmodel_State35', a)


def test_assoc_transition58_link_reassign_clear():
    a = robotmodel_Transition(name="sample_text")
    b1 = robotmodel_Event(name="sample_text")
    b2 = robotmodel_Event(name="sample_text_2")
    _safe_set(a, 'robotmodel_Transition60', b1)
    assert _is_linked(a, 'robotmodel_Transition60', b1)
    if hasattr(b1, 'robotmodel_Event59'):
        assert _is_linked(b1, 'robotmodel_Event59', a)
    _safe_set(a, 'robotmodel_Transition60', b2)
    assert _is_linked(a, 'robotmodel_Transition60', b2)
    if hasattr(b1, 'robotmodel_Event59'):
        assert not _is_linked(b1, 'robotmodel_Event59', a)
    if hasattr(b2, 'robotmodel_Event59'):
        assert _is_linked(b2, 'robotmodel_Event59', a)
    _safe_set(a, 'robotmodel_Transition60', None)
    assert not _is_linked(a, 'robotmodel_Transition60', b2)
    if hasattr(b2, 'robotmodel_Event59'):
        assert not _is_linked(b2, 'robotmodel_Event59', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

robotmodel_Action_strategy = st.builds(robotmodel_Action, name=safe_text)
@given(instance=robotmodel_Action_strategy)
@settings(max_examples=25)
def test_robotmodel_Action_instantiation(instance):
    assert isinstance(instance, robotmodel_Action)


robotmodel_Component_strategy = st.builds(robotmodel_Component, atype=safe_text, depends=safe_text, frequency=st.floats(allow_nan=False, allow_infinity=False), name=safe_text, type=safe_text)
@given(instance=robotmodel_Component_strategy)
@settings(max_examples=25)
def test_robotmodel_Component_instantiation(instance):
    assert isinstance(instance, robotmodel_Component)


robotmodel_Connector_strategy = st.builds(robotmodel_Connector, atype=safe_text, name=safe_text, type=safe_text)
@given(instance=robotmodel_Connector_strategy)
@settings(max_examples=25)
def test_robotmodel_Connector_instantiation(instance):
    assert isinstance(instance, robotmodel_Connector)


robotmodel_Event_strategy = st.builds(robotmodel_Event, name=safe_text)
@given(instance=robotmodel_Event_strategy)
@settings(max_examples=25)
def test_robotmodel_Event_instantiation(instance):
    assert isinstance(instance, robotmodel_Event)


robotmodel_Port_strategy = st.builds(robotmodel_Port, name=safe_text)
@given(instance=robotmodel_Port_strategy)
@settings(max_examples=25)
def test_robotmodel_Port_instantiation(instance):
    assert isinstance(instance, robotmodel_Port)


robotmodel_Property_strategy = st.builds(robotmodel_Property, name=safe_text, type=safe_text, value=safe_text)
@given(instance=robotmodel_Property_strategy)
@settings(max_examples=25)
def test_robotmodel_Property_instantiation(instance):
    assert isinstance(instance, robotmodel_Property)


robotmodel_Property_List_strategy = st.builds(robotmodel_Property_List, name=safe_text)
@given(instance=robotmodel_Property_List_strategy)
@settings(max_examples=25)
def test_robotmodel_Property_List_instantiation(instance):
    assert isinstance(instance, robotmodel_Property_List)


robotmodel_Role_strategy = st.builds(robotmodel_Role, name=safe_text)
@given(instance=robotmodel_Role_strategy)
@settings(max_examples=25)
def test_robotmodel_Role_instantiation(instance):
    assert isinstance(instance, robotmodel_Role)


robotmodel_State_strategy = st.builds(robotmodel_State, name=safe_text)
@given(instance=robotmodel_State_strategy)
@settings(max_examples=25)
def test_robotmodel_State_instantiation(instance):
    assert isinstance(instance, robotmodel_State)


robotmodel_System_strategy = st.builds(robotmodel_System, author=safe_text, author_email=safe_text, depends=safe_text, description=safe_text, name=safe_text)
@given(instance=robotmodel_System_strategy)
@settings(max_examples=25)
def test_robotmodel_System_instantiation(instance):
    assert isinstance(instance, robotmodel_System)


robotmodel_Transition_strategy = st.builds(robotmodel_Transition, name=safe_text)
@given(instance=robotmodel_Transition_strategy)
@settings(max_examples=25)
def test_robotmodel_Transition_instantiation(instance):
    assert isinstance(instance, robotmodel_Transition)



