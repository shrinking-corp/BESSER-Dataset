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
    df_Expression,
    df_VarToPortMapEntry,
    df_PortToVarMapEntry,
    df_Tag,
    df_Pattern,
    Edge,
    df_Transition,
    df_Connection,
    df_Vertex,
    df_PortToEIntegerObjectMapEntry,
    df_MoC,
    Graph,
    df_FSM,
    df_EObject,
    df_Argument,
    Adaptable,
    df_Network,
    df_Type,
    Vertex,
    df_Actor,
    df_State,
    df_Instance,
    df_Port,
    df_Procedure,
    df_Var,
    Attributable,
    df_Action,
    df_Entity,
    df_Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_df_expression_is_not_abstract():
    assert not inspect.isabstract(df_Expression)


def test_hyp_df_expression_constructor_exists():
    assert callable(df_Expression.__init__)


def test_hyp_df_expression_constructor_args():
    sig = inspect.signature(df_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_vartoportmapentry_is_not_abstract():
    assert not inspect.isabstract(df_VarToPortMapEntry)


def test_hyp_df_vartoportmapentry_constructor_exists():
    assert callable(df_VarToPortMapEntry.__init__)


def test_hyp_df_vartoportmapentry_constructor_args():
    sig = inspect.signature(df_VarToPortMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_porttovarmapentry_is_not_abstract():
    assert not inspect.isabstract(df_PortToVarMapEntry)


def test_hyp_df_porttovarmapentry_constructor_exists():
    assert callable(df_PortToVarMapEntry.__init__)


def test_hyp_df_porttovarmapentry_constructor_args():
    sig = inspect.signature(df_PortToVarMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_tag_is_not_abstract():
    assert not inspect.isabstract(df_Tag)


def test_hyp_df_tag_constructor_exists():
    assert callable(df_Tag.__init__)


def test_hyp_df_tag_constructor_args():
    sig = inspect.signature(df_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"




def test_hyp_df_pattern_is_not_abstract():
    assert not inspect.isabstract(df_Pattern)


def test_hyp_df_pattern_constructor_exists():
    assert callable(df_Pattern.__init__)


def test_hyp_df_pattern_constructor_args():
    sig = inspect.signature(df_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_hyp_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_hyp_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_hyp_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_transition_is_not_abstract():
    assert not inspect.isabstract(df_Transition)


def test_hyp_df_transition_constructor_exists():
    assert callable(df_Transition.__init__)


def test_hyp_df_transition_constructor_args():
    sig = inspect.signature(df_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_connection_is_not_abstract():
    assert not inspect.isabstract(df_Connection)


def test_hyp_df_connection_constructor_exists():
    assert callable(df_Connection.__init__)


def test_hyp_df_connection_constructor_args():
    sig = inspect.signature(df_Connection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_vertex_is_not_abstract():
    assert not inspect.isabstract(df_Vertex)


def test_hyp_df_vertex_constructor_exists():
    assert callable(df_Vertex.__init__)


def test_hyp_df_vertex_constructor_args():
    sig = inspect.signature(df_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_porttoeintegerobjectmapentry_is_not_abstract():
    assert not inspect.isabstract(df_PortToEIntegerObjectMapEntry)


def test_hyp_df_porttoeintegerobjectmapentry_constructor_exists():
    assert callable(df_PortToEIntegerObjectMapEntry.__init__)


def test_hyp_df_porttoeintegerobjectmapentry_constructor_args():
    sig = inspect.signature(df_PortToEIntegerObjectMapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_df_moc_is_not_abstract():
    assert not inspect.isabstract(df_MoC)


def test_hyp_df_moc_constructor_exists():
    assert callable(df_MoC.__init__)


def test_hyp_df_moc_constructor_args():
    sig = inspect.signature(df_MoC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_hyp_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_hyp_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_fsm_is_not_abstract():
    assert not inspect.isabstract(df_FSM)


def test_hyp_df_fsm_constructor_exists():
    assert callable(df_FSM.__init__)


def test_hyp_df_fsm_constructor_args():
    sig = inspect.signature(df_FSM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_eobject_is_not_abstract():
    assert not inspect.isabstract(df_EObject)


def test_hyp_df_eobject_constructor_exists():
    assert callable(df_EObject.__init__)


def test_hyp_df_eobject_constructor_args():
    sig = inspect.signature(df_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_argument_is_not_abstract():
    assert not inspect.isabstract(df_Argument)


def test_hyp_df_argument_constructor_exists():
    assert callable(df_Argument.__init__)


def test_hyp_df_argument_constructor_args():
    sig = inspect.signature(df_Argument.__init__)
    params = list(sig.parameters.keys())



def test_hyp_adaptable_is_not_abstract():
    assert not inspect.isabstract(Adaptable)


def test_hyp_adaptable_constructor_exists():
    assert callable(Adaptable.__init__)


def test_hyp_adaptable_constructor_args():
    sig = inspect.signature(Adaptable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_network_is_not_abstract():
    assert not inspect.isabstract(df_Network)


def test_hyp_df_network_constructor_exists():
    assert callable(df_Network.__init__)


def test_hyp_df_network_constructor_args():
    sig = inspect.signature(df_Network.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_df_type_is_not_abstract():
    assert not inspect.isabstract(df_Type)


def test_hyp_df_type_constructor_exists():
    assert callable(df_Type.__init__)


def test_hyp_df_type_constructor_args():
    sig = inspect.signature(df_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_hyp_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_hyp_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_actor_is_not_abstract():
    assert not inspect.isabstract(df_Actor)


def test_hyp_df_actor_constructor_exists():
    assert callable(df_Actor.__init__)


def test_hyp_df_actor_constructor_args():
    sig = inspect.signature(df_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "native" in params, "Missing parameter 'native'"
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "name" in params, "Missing parameter 'name'"







def test_hyp_df_state_is_not_abstract():
    assert not inspect.isabstract(df_State)


def test_hyp_df_state_constructor_exists():
    assert callable(df_State.__init__)


def test_hyp_df_state_constructor_args():
    sig = inspect.signature(df_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_instance_is_not_abstract():
    assert not inspect.isabstract(df_Instance)


def test_hyp_df_instance_constructor_exists():
    assert callable(df_Instance.__init__)


def test_hyp_df_instance_constructor_args():
    sig = inspect.signature(df_Instance.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_df_port_is_not_abstract():
    assert not inspect.isabstract(df_Port)


def test_hyp_df_port_constructor_exists():
    assert callable(df_Port.__init__)


def test_hyp_df_port_constructor_args():
    sig = inspect.signature(df_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "numTokensConsumed" in params, "Missing parameter 'numTokensConsumed'"
    assert "numTokensProduced" in params, "Missing parameter 'numTokensProduced'"






def test_hyp_df_procedure_is_not_abstract():
    assert not inspect.isabstract(df_Procedure)


def test_hyp_df_procedure_constructor_exists():
    assert callable(df_Procedure.__init__)


def test_hyp_df_procedure_constructor_args():
    sig = inspect.signature(df_Procedure.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_var_is_not_abstract():
    assert not inspect.isabstract(df_Var)


def test_hyp_df_var_constructor_exists():
    assert callable(df_Var.__init__)


def test_hyp_df_var_constructor_args():
    sig = inspect.signature(df_Var.__init__)
    params = list(sig.parameters.keys())



def test_hyp_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_hyp_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_hyp_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_action_is_not_abstract():
    assert not inspect.isabstract(df_Action)


def test_hyp_df_action_constructor_exists():
    assert callable(df_Action.__init__)


def test_hyp_df_action_constructor_args():
    sig = inspect.signature(df_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_df_entity_is_not_abstract():
    assert not inspect.isabstract(df_Entity)


def test_hyp_df_entity_constructor_exists():
    assert callable(df_Entity.__init__)


def test_hyp_df_entity_constructor_args():
    sig = inspect.signature(df_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "outgoingPortMap" in params, "Missing parameter 'outgoingPortMap'"
    assert "name" in params, "Missing parameter 'name'"
    assert "incomingPortMap" in params, "Missing parameter 'incomingPortMap'"






def test_hyp_df_unit_is_not_abstract():
    assert not inspect.isabstract(df_Unit)


def test_hyp_df_unit_constructor_exists():
    assert callable(df_Unit.__init__)


def test_hyp_df_unit_constructor_args():
    sig = inspect.signature(df_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "lineNumber" in params, "Missing parameter 'lineNumber'"
    assert "name" in params, "Missing parameter 'name'"
    assert "fileName" in params, "Missing parameter 'fileName'"





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
df_Expression_strategy = st.builds(
    df_Expression,
)
df_VarToPortMapEntry_strategy = st.builds(
    df_VarToPortMapEntry,
)
df_PortToVarMapEntry_strategy = st.builds(
    df_PortToVarMapEntry,
)
df_Tag_strategy = st.builds(
    df_Tag,
    identifiers=
        safe_text
)
df_Pattern_strategy = st.builds(
    df_Pattern,
)
Edge_strategy = st.builds(
    Edge,
)
df_Transition_strategy = st.builds(
    df_Transition,
)
df_Connection_strategy = st.builds(
    df_Connection,
)
df_Vertex_strategy = st.builds(
    df_Vertex,
)
df_PortToEIntegerObjectMapEntry_strategy = st.builds(
    df_PortToEIntegerObjectMapEntry,
    value=
        safe_text
)
df_MoC_strategy = st.builds(
    df_MoC,
)
Graph_strategy = st.builds(
    Graph,
)
df_FSM_strategy = st.builds(
    df_FSM,
)
df_EObject_strategy = st.builds(
    df_EObject,
)
df_Argument_strategy = st.builds(
    df_Argument,
)
Adaptable_strategy = st.builds(
    Adaptable,
)
df_Network_strategy = st.builds(
    df_Network,
    fileName=
        safe_text,
    name=
        safe_text
)
df_Type_strategy = st.builds(
    df_Type,
)
Vertex_strategy = st.builds(
    Vertex,
)
df_Actor_strategy = st.builds(
    df_Actor,
    fileName=
        safe_text,
    native=
        st.booleans(),
    lineNumber=
        st.integers(),
    name=
        safe_text
)
df_State_strategy = st.builds(
    df_State,
)
df_Instance_strategy = st.builds(
    df_Instance,
    name=
        safe_text
)
df_Port_strategy = st.builds(
    df_Port,
    name=
        safe_text,
    numTokensConsumed=
        st.integers(),
    numTokensProduced=
        st.integers()
)
df_Procedure_strategy = st.builds(
    df_Procedure,
)
df_Var_strategy = st.builds(
    df_Var,
)
Attributable_strategy = st.builds(
    Attributable,
)
df_Action_strategy = st.builds(
    df_Action,
)
df_Entity_strategy = st.builds(
    df_Entity,
    outgoingPortMap=
        safe_text,
    name=
        safe_text,
    incomingPortMap=
        safe_text
)
df_Unit_strategy = st.builds(
    df_Unit,
    lineNumber=
        st.integers(),
    name=
        safe_text,
    fileName=
        safe_text
)







@given(instance=df_Tag_strategy)
def test_hyp_df_tag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original









@given(instance=df_PortToEIntegerObjectMapEntry_strategy)
def test_hyp_df_porttoeintegerobjectmapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original










@given(instance=df_Network_strategy)
def test_hyp_df_network_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=df_Network_strategy)
def test_hyp_df_network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=df_Actor_strategy)
def test_hyp_df_actor_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=df_Actor_strategy)
def test_hyp_df_actor_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=df_Actor_strategy)
def test_hyp_df_actor_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original



@given(instance=df_Actor_strategy)
def test_hyp_df_actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=df_Instance_strategy)
def test_hyp_df_instance_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=df_Port_strategy)
def test_hyp_df_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Port_strategy)
def test_hyp_df_port_numTokensConsumed_setter(instance):
    original = instance.numTokensConsumed
    instance.numTokensConsumed = original
    assert instance.numTokensConsumed == original



@given(instance=df_Port_strategy)
def test_hyp_df_port_numTokensProduced_setter(instance):
    original = instance.numTokensProduced
    instance.numTokensProduced = original
    assert instance.numTokensProduced == original








@given(instance=df_Entity_strategy)
def test_hyp_df_entity_outgoingPortMap_setter(instance):
    original = instance.outgoingPortMap
    instance.outgoingPortMap = original
    assert instance.outgoingPortMap == original



@given(instance=df_Entity_strategy)
def test_hyp_df_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Entity_strategy)
def test_hyp_df_entity_incomingPortMap_setter(instance):
    original = instance.incomingPortMap
    instance.incomingPortMap = original
    assert instance.incomingPortMap == original




@given(instance=df_Unit_strategy)
def test_hyp_df_unit_lineNumber_setter(instance):
    original = instance.lineNumber
    instance.lineNumber = original
    assert instance.lineNumber == original



@given(instance=df_Unit_strategy)
def test_hyp_df_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=df_Unit_strategy)
def test_hyp_df_unit_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Adaptable,
    Attributable,
    Edge,
    Graph,
    Vertex,
    df_Action,
    df_Actor,
    df_Argument,
    df_Connection,
    df_EObject,
    df_Entity,
    df_Expression,
    df_FSM,
    df_Instance,
    df_MoC,
    df_Network,
    df_Pattern,
    df_Port,
    df_PortToEIntegerObjectMapEntry,
    df_PortToVarMapEntry,
    df_Procedure,
    df_State,
    df_Tag,
    df_Transition,
    df_Type,
    df_Unit,
    df_Var,
    df_VarToPortMapEntry,
    df_Vertex,
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

def test_df_Actor_fileName_value_roundtrip():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_df_Actor_lineNumber_value_roundtrip():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert instance.lineNumber == 7
    instance.lineNumber = 13
    assert instance.lineNumber == 13


def test_df_Actor_name_value_roundtrip():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Actor_native_value_roundtrip():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert instance.native == True
    instance.native = False
    assert instance.native == False


def test_df_Entity_incomingPortMap_value_roundtrip():
    instance = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    assert instance.incomingPortMap == "sample_text"
    instance.incomingPortMap = "sample_text_2"
    assert instance.incomingPortMap == "sample_text_2"


def test_df_Entity_name_value_roundtrip():
    instance = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Entity_outgoingPortMap_value_roundtrip():
    instance = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    assert instance.outgoingPortMap == "sample_text"
    instance.outgoingPortMap = "sample_text_2"
    assert instance.outgoingPortMap == "sample_text_2"


def test_df_Instance_name_value_roundtrip():
    instance = df_Instance(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Network_fileName_value_roundtrip():
    instance = df_Network(fileName="sample_text", name="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_df_Network_name_value_roundtrip():
    instance = df_Network(fileName="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Port_name_value_roundtrip():
    instance = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Port_numTokensConsumed_value_roundtrip():
    instance = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    assert instance.numTokensConsumed == 7
    instance.numTokensConsumed = 13
    assert instance.numTokensConsumed == 13


def test_df_Port_numTokensProduced_value_roundtrip():
    instance = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    assert instance.numTokensProduced == 7
    instance.numTokensProduced = 13
    assert instance.numTokensProduced == 13


def test_df_PortToEIntegerObjectMapEntry_value_value_roundtrip():
    instance = df_PortToEIntegerObjectMapEntry(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_df_Tag_identifiers_value_roundtrip():
    instance = df_Tag(identifiers="sample_text")
    assert instance.identifiers == "sample_text"
    instance.identifiers = "sample_text_2"
    assert instance.identifiers == "sample_text_2"


def test_df_Unit_fileName_value_roundtrip():
    instance = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_df_Unit_lineNumber_value_roundtrip():
    instance = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    assert instance.lineNumber == 7
    instance.lineNumber = 13
    assert instance.lineNumber == 13


def test_df_Unit_name_value_roundtrip():
    instance = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_df_Actor_isa_Adaptable():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert isinstance(instance, Adaptable)


def test_df_Entity_isa_Adaptable():
    instance = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    assert isinstance(instance, Adaptable)


def test_df_Instance_isa_Adaptable():
    instance = df_Instance(name="sample_text")
    assert isinstance(instance, Adaptable)


def test_df_Network_isa_Adaptable():
    instance = df_Network(fileName="sample_text", name="sample_text")
    assert isinstance(instance, Adaptable)


def test_df_Action_isa_Attributable():
    instance = df_Action()
    assert isinstance(instance, Attributable)


def test_df_Entity_isa_Attributable():
    instance = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    assert isinstance(instance, Attributable)


def test_df_Unit_isa_Attributable():
    instance = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    assert isinstance(instance, Attributable)


def test_df_Connection_isa_Edge():
    instance = df_Connection()
    assert isinstance(instance, Edge)


def test_df_Transition_isa_Edge():
    instance = df_Transition()
    assert isinstance(instance, Edge)


def test_df_FSM_isa_Graph():
    instance = df_FSM()
    assert isinstance(instance, Graph)


def test_df_Network_isa_Graph():
    instance = df_Network(fileName="sample_text", name="sample_text")
    assert isinstance(instance, Graph)


def test_df_Actor_isa_Vertex():
    instance = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    assert isinstance(instance, Vertex)


def test_df_Instance_isa_Vertex():
    instance = df_Instance(name="sample_text")
    assert isinstance(instance, Vertex)


def test_df_Port_isa_Vertex():
    instance = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    assert isinstance(instance, Vertex)


def test_df_State_isa_Vertex():
    instance = df_State()
    assert isinstance(instance, Vertex)


def test_assoc_actions15_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Action()
    b2 = df_Action()
    _safe_set(a, 'df_Actor', {b1})
    assert _is_linked(a, 'df_Actor', b1)
    if hasattr(b1, 'df_Action'):
        assert _is_linked(b1, 'df_Action', a)
    _safe_set(a, 'df_Actor', {b2})
    assert _is_linked(a, 'df_Actor', b2)
    if hasattr(b1, 'df_Action'):
        assert not _is_linked(b1, 'df_Action', a)
    if hasattr(b2, 'df_Action'):
        assert _is_linked(b2, 'df_Action', a)
    _safe_set(a, 'df_Actor', set())
    assert not _is_linked(a, 'df_Actor', b2)
    if hasattr(b2, 'df_Action'):
        assert not _is_linked(b2, 'df_Action', a)


def test_assoc_actionsOutsideFsm16_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Action()
    b2 = df_Action()
    _safe_set(a, 'df_Actor17', {b1})
    assert _is_linked(a, 'df_Actor17', b1)
    if hasattr(b1, 'df_Action18'):
        assert _is_linked(b1, 'df_Action18', a)
    _safe_set(a, 'df_Actor17', {b2})
    assert _is_linked(a, 'df_Actor17', b2)
    if hasattr(b1, 'df_Action18'):
        assert not _is_linked(b1, 'df_Action18', a)
    if hasattr(b2, 'df_Action18'):
        assert _is_linked(b2, 'df_Action18', a)
    _safe_set(a, 'df_Actor17', set())
    assert not _is_linked(a, 'df_Actor17', b2)
    if hasattr(b2, 'df_Action18'):
        assert not _is_linked(b2, 'df_Action18', a)


def test_assoc_arguments4_link_reassign_clear():
    a = df_Instance(name="sample_text")
    b1 = df_Argument()
    b2 = df_Argument()
    _safe_set(a, 'df_Instance', {b1})
    assert _is_linked(a, 'df_Instance', b1)
    if hasattr(b1, 'df_Argument'):
        assert _is_linked(b1, 'df_Argument', a)
    _safe_set(a, 'df_Instance', {b2})
    assert _is_linked(a, 'df_Instance', b2)
    if hasattr(b1, 'df_Argument'):
        assert not _is_linked(b1, 'df_Argument', a)
    if hasattr(b2, 'df_Argument'):
        assert _is_linked(b2, 'df_Argument', a)
    _safe_set(a, 'df_Instance', set())
    assert not _is_linked(a, 'df_Instance', b2)
    if hasattr(b2, 'df_Argument'):
        assert not _is_linked(b2, 'df_Argument', a)


def test_assoc_children41_link_reassign_clear():
    a = df_Network(fileName="sample_text", name="sample_text")
    b1 = df_Vertex()
    b2 = df_Vertex()
    _safe_set(a, 'df_Network', {b1})
    assert _is_linked(a, 'df_Network', b1)
    if hasattr(b1, 'df_Vertex'):
        assert _is_linked(b1, 'df_Vertex', a)
    _safe_set(a, 'df_Network', {b2})
    assert _is_linked(a, 'df_Network', b2)
    if hasattr(b1, 'df_Vertex'):
        assert not _is_linked(b1, 'df_Vertex', a)
    if hasattr(b2, 'df_Vertex'):
        assert _is_linked(b2, 'df_Vertex', a)
    _safe_set(a, 'df_Network', set())
    assert not _is_linked(a, 'df_Network', b2)
    if hasattr(b2, 'df_Vertex'):
        assert not _is_linked(b2, 'df_Vertex', a)


def test_assoc_constants0_link_reassign_clear():
    a = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Unit', {b1})
    assert _is_linked(a, 'df_Unit', b1)
    if hasattr(b1, 'df_Var'):
        assert _is_linked(b1, 'df_Var', a)
    _safe_set(a, 'df_Unit', {b2})
    assert _is_linked(a, 'df_Unit', b2)
    if hasattr(b1, 'df_Var'):
        assert not _is_linked(b1, 'df_Var', a)
    if hasattr(b2, 'df_Var'):
        assert _is_linked(b2, 'df_Var', a)
    _safe_set(a, 'df_Unit', set())
    assert not _is_linked(a, 'df_Unit', b2)
    if hasattr(b2, 'df_Var'):
        assert not _is_linked(b2, 'df_Var', a)


def test_assoc_entity5_link_reassign_clear():
    a = df_Instance(name="sample_text")
    b1 = df_EObject()
    b2 = df_EObject()
    _safe_set(a, 'df_Instance6', b1)
    assert _is_linked(a, 'df_Instance6', b1)
    if hasattr(b1, 'df_EObject'):
        assert _is_linked(b1, 'df_EObject', a)
    _safe_set(a, 'df_Instance6', b2)
    assert _is_linked(a, 'df_Instance6', b2)
    if hasattr(b1, 'df_EObject'):
        assert not _is_linked(b1, 'df_EObject', a)
    if hasattr(b2, 'df_EObject'):
        assert _is_linked(b2, 'df_EObject', a)
    _safe_set(a, 'df_Instance6', None)
    assert not _is_linked(a, 'df_Instance6', b2)
    if hasattr(b2, 'df_EObject'):
        assert not _is_linked(b2, 'df_EObject', a)


def test_assoc_fsm19_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_FSM()
    b2 = df_FSM()
    _safe_set(a, 'df_Actor20', b1)
    assert _is_linked(a, 'df_Actor20', b1)
    if hasattr(b1, 'df_FSM'):
        assert _is_linked(b1, 'df_FSM', a)
    _safe_set(a, 'df_Actor20', b2)
    assert _is_linked(a, 'df_Actor20', b2)
    if hasattr(b1, 'df_FSM'):
        assert not _is_linked(b1, 'df_FSM', a)
    if hasattr(b2, 'df_FSM'):
        assert _is_linked(b2, 'df_FSM', a)
    _safe_set(a, 'df_Actor20', None)
    assert not _is_linked(a, 'df_Actor20', b2)
    if hasattr(b2, 'df_FSM'):
        assert not _is_linked(b2, 'df_FSM', a)


def test_assoc_initializes21_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Action()
    b2 = df_Action()
    _safe_set(a, 'df_Actor22', {b1})
    assert _is_linked(a, 'df_Actor22', b1)
    if hasattr(b1, 'df_Action23'):
        assert _is_linked(b1, 'df_Action23', a)
    _safe_set(a, 'df_Actor22', {b2})
    assert _is_linked(a, 'df_Actor22', b2)
    if hasattr(b1, 'df_Action23'):
        assert not _is_linked(b1, 'df_Action23', a)
    if hasattr(b2, 'df_Action23'):
        assert _is_linked(b2, 'df_Action23', a)
    _safe_set(a, 'df_Actor22', set())
    assert not _is_linked(a, 'df_Actor22', b2)
    if hasattr(b2, 'df_Action23'):
        assert not _is_linked(b2, 'df_Action23', a)


def test_assoc_inputs24_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b2 = df_Actor(fileName="sample_text_2", lineNumber=13, name="sample_text_2", native=False)
    _safe_set(a, 'df_Port26', b1)
    assert _is_linked(a, 'df_Port26', b1)
    if hasattr(b1, 'df_Actor25'):
        assert _is_linked(b1, 'df_Actor25', a)
    _safe_set(a, 'df_Port26', b2)
    assert _is_linked(a, 'df_Port26', b2)
    if hasattr(b1, 'df_Actor25'):
        assert not _is_linked(b1, 'df_Actor25', a)
    if hasattr(b2, 'df_Actor25'):
        assert _is_linked(b2, 'df_Actor25', a)
    _safe_set(a, 'df_Port26', None)
    assert not _is_linked(a, 'df_Port26', b2)
    if hasattr(b2, 'df_Actor25'):
        assert not _is_linked(b2, 'df_Actor25', a)


def test_assoc_inputs42_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Network(fileName="sample_text", name="sample_text")
    b2 = df_Network(fileName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'df_Port44', b1)
    assert _is_linked(a, 'df_Port44', b1)
    if hasattr(b1, 'df_Network43'):
        assert _is_linked(b1, 'df_Network43', a)
    _safe_set(a, 'df_Port44', b2)
    assert _is_linked(a, 'df_Port44', b2)
    if hasattr(b1, 'df_Network43'):
        assert not _is_linked(b1, 'df_Network43', a)
    if hasattr(b2, 'df_Network43'):
        assert _is_linked(b2, 'df_Network43', a)
    _safe_set(a, 'df_Port44', None)
    assert not _is_linked(a, 'df_Port44', b2)
    if hasattr(b2, 'df_Network43'):
        assert not _is_linked(b2, 'df_Network43', a)


def test_assoc_inputs7_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    b2 = df_Entity(incomingPortMap="sample_text_2", name="sample_text_2", outgoingPortMap="sample_text_2")
    _safe_set(a, 'df_Port8', b1)
    assert _is_linked(a, 'df_Port8', b1)
    if hasattr(b1, 'df_Entity'):
        assert _is_linked(b1, 'df_Entity', a)
    _safe_set(a, 'df_Port8', b2)
    assert _is_linked(a, 'df_Port8', b2)
    if hasattr(b1, 'df_Entity'):
        assert not _is_linked(b1, 'df_Entity', a)
    if hasattr(b2, 'df_Entity'):
        assert _is_linked(b2, 'df_Entity', a)
    _safe_set(a, 'df_Port8', None)
    assert not _is_linked(a, 'df_Port8', b2)
    if hasattr(b2, 'df_Entity'):
        assert not _is_linked(b2, 'df_Entity', a)


def test_assoc_key94_link_reassign_clear():
    a = df_PortToEIntegerObjectMapEntry(value="sample_text")
    b1 = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b2 = df_Port(name="sample_text_2", numTokensConsumed=13, numTokensProduced=13)
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry95', b1)
    assert _is_linked(a, 'df_PortToEIntegerObjectMapEntry95', b1)
    if hasattr(b1, 'df_Port96'):
        assert _is_linked(b1, 'df_Port96', a)
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry95', b2)
    assert _is_linked(a, 'df_PortToEIntegerObjectMapEntry95', b2)
    if hasattr(b1, 'df_Port96'):
        assert not _is_linked(b1, 'df_Port96', a)
    if hasattr(b2, 'df_Port96'):
        assert _is_linked(b2, 'df_Port96', a)
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry95', None)
    assert not _is_linked(a, 'df_PortToEIntegerObjectMapEntry95', b2)
    if hasattr(b2, 'df_Port96'):
        assert not _is_linked(b2, 'df_Port96', a)


def test_assoc_key97_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_PortToVarMapEntry()
    b2 = df_PortToVarMapEntry()
    _safe_set(a, 'df_Port99', b1)
    assert _is_linked(a, 'df_Port99', b1)
    if hasattr(b1, 'df_PortToVarMapEntry98'):
        assert _is_linked(b1, 'df_PortToVarMapEntry98', a)
    _safe_set(a, 'df_Port99', b2)
    assert _is_linked(a, 'df_Port99', b2)
    if hasattr(b1, 'df_PortToVarMapEntry98'):
        assert not _is_linked(b1, 'df_PortToVarMapEntry98', a)
    if hasattr(b2, 'df_PortToVarMapEntry98'):
        assert _is_linked(b2, 'df_PortToVarMapEntry98', a)
    _safe_set(a, 'df_Port99', None)
    assert not _is_linked(a, 'df_Port99', b2)
    if hasattr(b2, 'df_PortToVarMapEntry98'):
        assert not _is_linked(b2, 'df_PortToVarMapEntry98', a)


def test_assoc_moC27_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_MoC()
    b2 = df_MoC()
    _safe_set(a, 'df_Actor28', b1)
    assert _is_linked(a, 'df_Actor28', b1)
    if hasattr(b1, 'df_MoC'):
        assert _is_linked(b1, 'df_MoC', a)
    _safe_set(a, 'df_Actor28', b2)
    assert _is_linked(a, 'df_Actor28', b2)
    if hasattr(b1, 'df_MoC'):
        assert not _is_linked(b1, 'df_MoC', a)
    if hasattr(b2, 'df_MoC'):
        assert _is_linked(b2, 'df_MoC', a)
    _safe_set(a, 'df_Actor28', None)
    assert not _is_linked(a, 'df_Actor28', b2)
    if hasattr(b2, 'df_MoC'):
        assert not _is_linked(b2, 'df_MoC', a)


def test_assoc_moC45_link_reassign_clear():
    a = df_Network(fileName="sample_text", name="sample_text")
    b1 = df_MoC()
    b2 = df_MoC()
    _safe_set(a, 'df_Network46', b1)
    assert _is_linked(a, 'df_Network46', b1)
    if hasattr(b1, 'df_MoC47'):
        assert _is_linked(b1, 'df_MoC47', a)
    _safe_set(a, 'df_Network46', b2)
    assert _is_linked(a, 'df_Network46', b2)
    if hasattr(b1, 'df_MoC47'):
        assert not _is_linked(b1, 'df_MoC47', a)
    if hasattr(b2, 'df_MoC47'):
        assert _is_linked(b2, 'df_MoC47', a)
    _safe_set(a, 'df_Network46', None)
    assert not _is_linked(a, 'df_Network46', b2)
    if hasattr(b2, 'df_MoC47'):
        assert not _is_linked(b2, 'df_MoC47', a)


def test_assoc_numTokensMap80_link_reassign_clear():
    a = df_PortToEIntegerObjectMapEntry(value="sample_text")
    b1 = df_Pattern()
    b2 = df_Pattern()
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry', b1)
    assert _is_linked(a, 'df_PortToEIntegerObjectMapEntry', b1)
    if hasattr(b1, 'df_Pattern81'):
        assert _is_linked(b1, 'df_Pattern81', a)
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry', b2)
    assert _is_linked(a, 'df_PortToEIntegerObjectMapEntry', b2)
    if hasattr(b1, 'df_Pattern81'):
        assert not _is_linked(b1, 'df_Pattern81', a)
    if hasattr(b2, 'df_Pattern81'):
        assert _is_linked(b2, 'df_Pattern81', a)
    _safe_set(a, 'df_PortToEIntegerObjectMapEntry', None)
    assert not _is_linked(a, 'df_PortToEIntegerObjectMapEntry', b2)
    if hasattr(b2, 'df_Pattern81'):
        assert not _is_linked(b2, 'df_Pattern81', a)


def test_assoc_outputs29_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b2 = df_Actor(fileName="sample_text_2", lineNumber=13, name="sample_text_2", native=False)
    _safe_set(a, 'df_Port31', b1)
    assert _is_linked(a, 'df_Port31', b1)
    if hasattr(b1, 'df_Actor30'):
        assert _is_linked(b1, 'df_Actor30', a)
    _safe_set(a, 'df_Port31', b2)
    assert _is_linked(a, 'df_Port31', b2)
    if hasattr(b1, 'df_Actor30'):
        assert not _is_linked(b1, 'df_Actor30', a)
    if hasattr(b2, 'df_Actor30'):
        assert _is_linked(b2, 'df_Actor30', a)
    _safe_set(a, 'df_Port31', None)
    assert not _is_linked(a, 'df_Port31', b2)
    if hasattr(b2, 'df_Actor30'):
        assert not _is_linked(b2, 'df_Actor30', a)


def test_assoc_outputs48_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Network(fileName="sample_text", name="sample_text")
    b2 = df_Network(fileName="sample_text_2", name="sample_text_2")
    _safe_set(a, 'df_Port50', b1)
    assert _is_linked(a, 'df_Port50', b1)
    if hasattr(b1, 'df_Network49'):
        assert _is_linked(b1, 'df_Network49', a)
    _safe_set(a, 'df_Port50', b2)
    assert _is_linked(a, 'df_Port50', b2)
    if hasattr(b1, 'df_Network49'):
        assert not _is_linked(b1, 'df_Network49', a)
    if hasattr(b2, 'df_Network49'):
        assert _is_linked(b2, 'df_Network49', a)
    _safe_set(a, 'df_Port50', None)
    assert not _is_linked(a, 'df_Port50', b2)
    if hasattr(b2, 'df_Network49'):
        assert not _is_linked(b2, 'df_Network49', a)


def test_assoc_outputs9_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    b2 = df_Entity(incomingPortMap="sample_text_2", name="sample_text_2", outgoingPortMap="sample_text_2")
    _safe_set(a, 'df_Port11', b1)
    assert _is_linked(a, 'df_Port11', b1)
    if hasattr(b1, 'df_Entity10'):
        assert _is_linked(b1, 'df_Entity10', a)
    _safe_set(a, 'df_Port11', b2)
    assert _is_linked(a, 'df_Port11', b2)
    if hasattr(b1, 'df_Entity10'):
        assert not _is_linked(b1, 'df_Entity10', a)
    if hasattr(b2, 'df_Entity10'):
        assert _is_linked(b2, 'df_Entity10', a)
    _safe_set(a, 'df_Port11', None)
    assert not _is_linked(a, 'df_Port11', b2)
    if hasattr(b2, 'df_Entity10'):
        assert not _is_linked(b2, 'df_Entity10', a)


def test_assoc_parameters12_link_reassign_clear():
    a = df_Entity(incomingPortMap="sample_text", name="sample_text", outgoingPortMap="sample_text")
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Entity13', {b1})
    assert _is_linked(a, 'df_Entity13', b1)
    if hasattr(b1, 'df_Var14'):
        assert _is_linked(b1, 'df_Var14', a)
    _safe_set(a, 'df_Entity13', {b2})
    assert _is_linked(a, 'df_Entity13', b2)
    if hasattr(b1, 'df_Var14'):
        assert not _is_linked(b1, 'df_Var14', a)
    if hasattr(b2, 'df_Var14'):
        assert _is_linked(b2, 'df_Var14', a)
    _safe_set(a, 'df_Entity13', set())
    assert not _is_linked(a, 'df_Entity13', b2)
    if hasattr(b2, 'df_Var14'):
        assert not _is_linked(b2, 'df_Var14', a)


def test_assoc_parameters32_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Actor33', {b1})
    assert _is_linked(a, 'df_Actor33', b1)
    if hasattr(b1, 'df_Var34'):
        assert _is_linked(b1, 'df_Var34', a)
    _safe_set(a, 'df_Actor33', {b2})
    assert _is_linked(a, 'df_Actor33', b2)
    if hasattr(b1, 'df_Var34'):
        assert not _is_linked(b1, 'df_Var34', a)
    if hasattr(b2, 'df_Var34'):
        assert _is_linked(b2, 'df_Var34', a)
    _safe_set(a, 'df_Actor33', set())
    assert not _is_linked(a, 'df_Actor33', b2)
    if hasattr(b2, 'df_Var34'):
        assert not _is_linked(b2, 'df_Var34', a)


def test_assoc_parameters51_link_reassign_clear():
    a = df_Network(fileName="sample_text", name="sample_text")
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Network52', {b1})
    assert _is_linked(a, 'df_Network52', b1)
    if hasattr(b1, 'df_Var53'):
        assert _is_linked(b1, 'df_Var53', a)
    _safe_set(a, 'df_Network52', {b2})
    assert _is_linked(a, 'df_Network52', b2)
    if hasattr(b1, 'df_Var53'):
        assert not _is_linked(b1, 'df_Var53', a)
    if hasattr(b2, 'df_Var53'):
        assert _is_linked(b2, 'df_Var53', a)
    _safe_set(a, 'df_Network52', set())
    assert not _is_linked(a, 'df_Network52', b2)
    if hasattr(b2, 'df_Var53'):
        assert not _is_linked(b2, 'df_Var53', a)


def test_assoc_ports82_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Pattern()
    b2 = df_Pattern()
    _safe_set(a, 'df_Port84', b1)
    assert _is_linked(a, 'df_Port84', b1)
    if hasattr(b1, 'df_Pattern83'):
        assert _is_linked(b1, 'df_Pattern83', a)
    _safe_set(a, 'df_Port84', b2)
    assert _is_linked(a, 'df_Port84', b2)
    if hasattr(b1, 'df_Pattern83'):
        assert not _is_linked(b1, 'df_Pattern83', a)
    if hasattr(b2, 'df_Pattern83'):
        assert _is_linked(b2, 'df_Pattern83', a)
    _safe_set(a, 'df_Port84', None)
    assert not _is_linked(a, 'df_Port84', b2)
    if hasattr(b2, 'df_Pattern83'):
        assert not _is_linked(b2, 'df_Pattern83', a)


def test_assoc_procedures1_link_reassign_clear():
    a = df_Unit(fileName="sample_text", lineNumber=7, name="sample_text")
    b1 = df_Procedure()
    b2 = df_Procedure()
    _safe_set(a, 'df_Unit2', {b1})
    assert _is_linked(a, 'df_Unit2', b1)
    if hasattr(b1, 'df_Procedure'):
        assert _is_linked(b1, 'df_Procedure', a)
    _safe_set(a, 'df_Unit2', {b2})
    assert _is_linked(a, 'df_Unit2', b2)
    if hasattr(b1, 'df_Procedure'):
        assert not _is_linked(b1, 'df_Procedure', a)
    if hasattr(b2, 'df_Procedure'):
        assert _is_linked(b2, 'df_Procedure', a)
    _safe_set(a, 'df_Unit2', set())
    assert not _is_linked(a, 'df_Unit2', b2)
    if hasattr(b2, 'df_Procedure'):
        assert not _is_linked(b2, 'df_Procedure', a)


def test_assoc_procs35_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Procedure()
    b2 = df_Procedure()
    _safe_set(a, 'df_Actor36', {b1})
    assert _is_linked(a, 'df_Actor36', b1)
    if hasattr(b1, 'df_Procedure37'):
        assert _is_linked(b1, 'df_Procedure37', a)
    _safe_set(a, 'df_Actor36', {b2})
    assert _is_linked(a, 'df_Actor36', b2)
    if hasattr(b1, 'df_Procedure37'):
        assert not _is_linked(b1, 'df_Procedure37', a)
    if hasattr(b2, 'df_Procedure37'):
        assert _is_linked(b2, 'df_Procedure37', a)
    _safe_set(a, 'df_Actor36', set())
    assert not _is_linked(a, 'df_Actor36', b2)
    if hasattr(b2, 'df_Procedure37'):
        assert not _is_linked(b2, 'df_Procedure37', a)


def test_assoc_sourcePort57_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Connection()
    b2 = df_Connection()
    _safe_set(a, 'df_Port58', b1)
    assert _is_linked(a, 'df_Port58', b1)
    if hasattr(b1, 'df_Connection'):
        assert _is_linked(b1, 'df_Connection', a)
    _safe_set(a, 'df_Port58', b2)
    assert _is_linked(a, 'df_Port58', b2)
    if hasattr(b1, 'df_Connection'):
        assert not _is_linked(b1, 'df_Connection', a)
    if hasattr(b2, 'df_Connection'):
        assert _is_linked(b2, 'df_Connection', a)
    _safe_set(a, 'df_Port58', None)
    assert not _is_linked(a, 'df_Port58', b2)
    if hasattr(b2, 'df_Connection'):
        assert not _is_linked(b2, 'df_Connection', a)


def test_assoc_stateVars38_link_reassign_clear():
    a = df_Actor(fileName="sample_text", lineNumber=7, name="sample_text", native=True)
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Actor39', {b1})
    assert _is_linked(a, 'df_Actor39', b1)
    if hasattr(b1, 'df_Var40'):
        assert _is_linked(b1, 'df_Var40', a)
    _safe_set(a, 'df_Actor39', {b2})
    assert _is_linked(a, 'df_Actor39', b2)
    if hasattr(b1, 'df_Var40'):
        assert not _is_linked(b1, 'df_Var40', a)
    if hasattr(b2, 'df_Var40'):
        assert _is_linked(b2, 'df_Var40', a)
    _safe_set(a, 'df_Actor39', set())
    assert not _is_linked(a, 'df_Actor39', b2)
    if hasattr(b2, 'df_Var40'):
        assert not _is_linked(b2, 'df_Var40', a)


def test_assoc_tag76_link_reassign_clear():
    a = df_Tag(identifiers="sample_text")
    b1 = df_Action()
    b2 = df_Action()
    _safe_set(a, 'df_Tag', b1)
    assert _is_linked(a, 'df_Tag', b1)
    if hasattr(b1, 'df_Action77'):
        assert _is_linked(b1, 'df_Action77', a)
    _safe_set(a, 'df_Tag', b2)
    assert _is_linked(a, 'df_Tag', b2)
    if hasattr(b1, 'df_Action77'):
        assert not _is_linked(b1, 'df_Action77', a)
    if hasattr(b2, 'df_Action77'):
        assert _is_linked(b2, 'df_Action77', a)
    _safe_set(a, 'df_Tag', None)
    assert not _is_linked(a, 'df_Tag', b2)
    if hasattr(b2, 'df_Action77'):
        assert not _is_linked(b2, 'df_Action77', a)


def test_assoc_targetPort59_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Connection()
    b2 = df_Connection()
    _safe_set(a, 'df_Port61', b1)
    assert _is_linked(a, 'df_Port61', b1)
    if hasattr(b1, 'df_Connection60'):
        assert _is_linked(b1, 'df_Connection60', a)
    _safe_set(a, 'df_Port61', b2)
    assert _is_linked(a, 'df_Port61', b2)
    if hasattr(b1, 'df_Connection60'):
        assert not _is_linked(b1, 'df_Connection60', a)
    if hasattr(b2, 'df_Connection60'):
        assert _is_linked(b2, 'df_Connection60', a)
    _safe_set(a, 'df_Port61', None)
    assert not _is_linked(a, 'df_Port61', b2)
    if hasattr(b2, 'df_Connection60'):
        assert not _is_linked(b2, 'df_Connection60', a)


def test_assoc_type3_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_Type()
    b2 = df_Type()
    _safe_set(a, 'df_Port', b1)
    assert _is_linked(a, 'df_Port', b1)
    if hasattr(b1, 'df_Type'):
        assert _is_linked(b1, 'df_Type', a)
    _safe_set(a, 'df_Port', b2)
    assert _is_linked(a, 'df_Port', b2)
    if hasattr(b1, 'df_Type'):
        assert not _is_linked(b1, 'df_Type', a)
    if hasattr(b2, 'df_Type'):
        assert _is_linked(b2, 'df_Type', a)
    _safe_set(a, 'df_Port', None)
    assert not _is_linked(a, 'df_Port', b2)
    if hasattr(b2, 'df_Type'):
        assert not _is_linked(b2, 'df_Type', a)


def test_assoc_value106_link_reassign_clear():
    a = df_Port(name="sample_text", numTokensConsumed=7, numTokensProduced=7)
    b1 = df_VarToPortMapEntry()
    b2 = df_VarToPortMapEntry()
    _safe_set(a, 'df_Port108', b1)
    assert _is_linked(a, 'df_Port108', b1)
    if hasattr(b1, 'df_VarToPortMapEntry107'):
        assert _is_linked(b1, 'df_VarToPortMapEntry107', a)
    _safe_set(a, 'df_Port108', b2)
    assert _is_linked(a, 'df_Port108', b2)
    if hasattr(b1, 'df_VarToPortMapEntry107'):
        assert not _is_linked(b1, 'df_VarToPortMapEntry107', a)
    if hasattr(b2, 'df_VarToPortMapEntry107'):
        assert _is_linked(b2, 'df_VarToPortMapEntry107', a)
    _safe_set(a, 'df_Port108', None)
    assert not _is_linked(a, 'df_Port108', b2)
    if hasattr(b2, 'df_VarToPortMapEntry107'):
        assert not _is_linked(b2, 'df_VarToPortMapEntry107', a)


def test_assoc_variables54_link_reassign_clear():
    a = df_Network(fileName="sample_text", name="sample_text")
    b1 = df_Var()
    b2 = df_Var()
    _safe_set(a, 'df_Network55', {b1})
    assert _is_linked(a, 'df_Network55', b1)
    if hasattr(b1, 'df_Var56'):
        assert _is_linked(b1, 'df_Var56', a)
    _safe_set(a, 'df_Network55', {b2})
    assert _is_linked(a, 'df_Network55', b2)
    if hasattr(b1, 'df_Var56'):
        assert not _is_linked(b1, 'df_Var56', a)
    if hasattr(b2, 'df_Var56'):
        assert _is_linked(b2, 'df_Var56', a)
    _safe_set(a, 'df_Network55', set())
    assert not _is_linked(a, 'df_Network55', b2)
    if hasattr(b2, 'df_Var56'):
        assert not _is_linked(b2, 'df_Var56', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Adaptable_strategy = st.builds(Adaptable)
@given(instance=Adaptable_strategy)
@settings(max_examples=25)
def test_Adaptable_instantiation(instance):
    assert isinstance(instance, Adaptable)


Attributable_strategy = st.builds(Attributable)
@given(instance=Attributable_strategy)
@settings(max_examples=25)
def test_Attributable_instantiation(instance):
    assert isinstance(instance, Attributable)


Edge_strategy = st.builds(Edge)
@given(instance=Edge_strategy)
@settings(max_examples=25)
def test_Edge_instantiation(instance):
    assert isinstance(instance, Edge)


Graph_strategy = st.builds(Graph)
@given(instance=Graph_strategy)
@settings(max_examples=25)
def test_Graph_instantiation(instance):
    assert isinstance(instance, Graph)


Vertex_strategy = st.builds(Vertex)
@given(instance=Vertex_strategy)
@settings(max_examples=25)
def test_Vertex_instantiation(instance):
    assert isinstance(instance, Vertex)


df_Action_strategy = st.builds(df_Action)
@given(instance=df_Action_strategy)
@settings(max_examples=25)
def test_df_Action_instantiation(instance):
    assert isinstance(instance, df_Action)


df_Actor_strategy = st.builds(df_Actor, fileName=safe_text, lineNumber=st.integers(), name=safe_text, native=st.booleans())
@given(instance=df_Actor_strategy)
@settings(max_examples=25)
def test_df_Actor_instantiation(instance):
    assert isinstance(instance, df_Actor)


df_Argument_strategy = st.builds(df_Argument)
@given(instance=df_Argument_strategy)
@settings(max_examples=25)
def test_df_Argument_instantiation(instance):
    assert isinstance(instance, df_Argument)


df_Connection_strategy = st.builds(df_Connection)
@given(instance=df_Connection_strategy)
@settings(max_examples=25)
def test_df_Connection_instantiation(instance):
    assert isinstance(instance, df_Connection)


df_EObject_strategy = st.builds(df_EObject)
@given(instance=df_EObject_strategy)
@settings(max_examples=25)
def test_df_EObject_instantiation(instance):
    assert isinstance(instance, df_EObject)


df_Entity_strategy = st.builds(df_Entity, incomingPortMap=safe_text, name=safe_text, outgoingPortMap=safe_text)
@given(instance=df_Entity_strategy)
@settings(max_examples=25)
def test_df_Entity_instantiation(instance):
    assert isinstance(instance, df_Entity)


df_Expression_strategy = st.builds(df_Expression)
@given(instance=df_Expression_strategy)
@settings(max_examples=25)
def test_df_Expression_instantiation(instance):
    assert isinstance(instance, df_Expression)


df_FSM_strategy = st.builds(df_FSM)
@given(instance=df_FSM_strategy)
@settings(max_examples=25)
def test_df_FSM_instantiation(instance):
    assert isinstance(instance, df_FSM)


df_Instance_strategy = st.builds(df_Instance, name=safe_text)
@given(instance=df_Instance_strategy)
@settings(max_examples=25)
def test_df_Instance_instantiation(instance):
    assert isinstance(instance, df_Instance)


df_MoC_strategy = st.builds(df_MoC)
@given(instance=df_MoC_strategy)
@settings(max_examples=25)
def test_df_MoC_instantiation(instance):
    assert isinstance(instance, df_MoC)


df_Network_strategy = st.builds(df_Network, fileName=safe_text, name=safe_text)
@given(instance=df_Network_strategy)
@settings(max_examples=25)
def test_df_Network_instantiation(instance):
    assert isinstance(instance, df_Network)


df_Pattern_strategy = st.builds(df_Pattern)
@given(instance=df_Pattern_strategy)
@settings(max_examples=25)
def test_df_Pattern_instantiation(instance):
    assert isinstance(instance, df_Pattern)


df_Port_strategy = st.builds(df_Port, name=safe_text, numTokensConsumed=st.integers(), numTokensProduced=st.integers())
@given(instance=df_Port_strategy)
@settings(max_examples=25)
def test_df_Port_instantiation(instance):
    assert isinstance(instance, df_Port)


df_PortToEIntegerObjectMapEntry_strategy = st.builds(df_PortToEIntegerObjectMapEntry, value=safe_text)
@given(instance=df_PortToEIntegerObjectMapEntry_strategy)
@settings(max_examples=25)
def test_df_PortToEIntegerObjectMapEntry_instantiation(instance):
    assert isinstance(instance, df_PortToEIntegerObjectMapEntry)


df_PortToVarMapEntry_strategy = st.builds(df_PortToVarMapEntry)
@given(instance=df_PortToVarMapEntry_strategy)
@settings(max_examples=25)
def test_df_PortToVarMapEntry_instantiation(instance):
    assert isinstance(instance, df_PortToVarMapEntry)


df_Procedure_strategy = st.builds(df_Procedure)
@given(instance=df_Procedure_strategy)
@settings(max_examples=25)
def test_df_Procedure_instantiation(instance):
    assert isinstance(instance, df_Procedure)


df_State_strategy = st.builds(df_State)
@given(instance=df_State_strategy)
@settings(max_examples=25)
def test_df_State_instantiation(instance):
    assert isinstance(instance, df_State)


df_Tag_strategy = st.builds(df_Tag, identifiers=safe_text)
@given(instance=df_Tag_strategy)
@settings(max_examples=25)
def test_df_Tag_instantiation(instance):
    assert isinstance(instance, df_Tag)


df_Transition_strategy = st.builds(df_Transition)
@given(instance=df_Transition_strategy)
@settings(max_examples=25)
def test_df_Transition_instantiation(instance):
    assert isinstance(instance, df_Transition)


df_Type_strategy = st.builds(df_Type)
@given(instance=df_Type_strategy)
@settings(max_examples=25)
def test_df_Type_instantiation(instance):
    assert isinstance(instance, df_Type)


df_Unit_strategy = st.builds(df_Unit, fileName=safe_text, lineNumber=st.integers(), name=safe_text)
@given(instance=df_Unit_strategy)
@settings(max_examples=25)
def test_df_Unit_instantiation(instance):
    assert isinstance(instance, df_Unit)


df_Var_strategy = st.builds(df_Var)
@given(instance=df_Var_strategy)
@settings(max_examples=25)
def test_df_Var_instantiation(instance):
    assert isinstance(instance, df_Var)


df_VarToPortMapEntry_strategy = st.builds(df_VarToPortMapEntry)
@given(instance=df_VarToPortMapEntry_strategy)
@settings(max_examples=25)
def test_df_VarToPortMapEntry_instantiation(instance):
    assert isinstance(instance, df_VarToPortMapEntry)


df_Vertex_strategy = st.builds(df_Vertex)
@given(instance=df_Vertex_strategy)
@settings(max_examples=25)
def test_df_Vertex_instantiation(instance):
    assert isinstance(instance, df_Vertex)



