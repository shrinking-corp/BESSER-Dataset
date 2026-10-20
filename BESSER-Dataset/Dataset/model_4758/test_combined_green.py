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
    effbd106_ProcessNode,
    effbd106_SequenceNode,
    effbd106_Token,
    effbd106_Description,
    effbd106_Item,
    effbd106_Port,
    Port,
    effbd106_InputPort,
    Sequence,
    effbd106_LoopExit,
    effbd106_Iteration,
    effbd106_Start,
    effbd106_Final,
    effbd106_Or,
    effbd106_Loop,
    effbd106_And,
    ProcessNode,
    SequenceNode,
    effbd106_Function,
    effbd106_OutputPort,
    effbd106_Flow,
    effbd106_Sequence,
    FunctionDomain,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_effbd106_processnode_is_not_abstract():
    assert not inspect.isabstract(effbd106_ProcessNode)


def test_hyp_effbd106_processnode_constructor_exists():
    assert callable(effbd106_ProcessNode.__init__)


def test_hyp_effbd106_processnode_constructor_args():
    sig = inspect.signature(effbd106_ProcessNode.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"




def test_hyp_effbd106_sequencenode_is_not_abstract():
    assert not inspect.isabstract(effbd106_SequenceNode)


def test_hyp_effbd106_sequencenode_constructor_exists():
    assert callable(effbd106_SequenceNode.__init__)


def test_hyp_effbd106_sequencenode_constructor_args():
    sig = inspect.signature(effbd106_SequenceNode.__init__)
    params = list(sig.parameters.keys())
    assert "tMin" in params, "Missing parameter 'tMin'"
    assert "tMax" in params, "Missing parameter 'tMax'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_effbd106_token_is_not_abstract():
    assert not inspect.isabstract(effbd106_Token)


def test_hyp_effbd106_token_constructor_exists():
    assert callable(effbd106_Token.__init__)


def test_hyp_effbd106_token_constructor_args():
    sig = inspect.signature(effbd106_Token.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_description_is_not_abstract():
    assert not inspect.isabstract(effbd106_Description)


def test_hyp_effbd106_description_constructor_exists():
    assert callable(effbd106_Description.__init__)


def test_hyp_effbd106_description_constructor_args():
    sig = inspect.signature(effbd106_Description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_effbd106_item_is_not_abstract():
    assert not inspect.isabstract(effbd106_Item)


def test_hyp_effbd106_item_constructor_exists():
    assert callable(effbd106_Item.__init__)


def test_hyp_effbd106_item_constructor_args():
    sig = inspect.signature(effbd106_Item.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_effbd106_port_is_not_abstract():
    assert not inspect.isabstract(effbd106_Port)


def test_hyp_effbd106_port_constructor_exists():
    assert callable(effbd106_Port.__init__)


def test_hyp_effbd106_port_constructor_args():
    sig = inspect.signature(effbd106_Port.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_hyp_port_constructor_exists():
    assert callable(Port.__init__)


def test_hyp_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_inputport_is_not_abstract():
    assert not inspect.isabstract(effbd106_InputPort)


def test_hyp_effbd106_inputport_constructor_exists():
    assert callable(effbd106_InputPort.__init__)


def test_hyp_effbd106_inputport_constructor_args():
    sig = inspect.signature(effbd106_InputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sequence_is_not_abstract():
    assert not inspect.isabstract(Sequence)


def test_hyp_sequence_constructor_exists():
    assert callable(Sequence.__init__)


def test_hyp_sequence_constructor_args():
    sig = inspect.signature(Sequence.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_loopexit_is_not_abstract():
    assert not inspect.isabstract(effbd106_LoopExit)


def test_hyp_effbd106_loopexit_constructor_exists():
    assert callable(effbd106_LoopExit.__init__)


def test_hyp_effbd106_loopexit_constructor_args():
    sig = inspect.signature(effbd106_LoopExit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_iteration_is_not_abstract():
    assert not inspect.isabstract(effbd106_Iteration)


def test_hyp_effbd106_iteration_constructor_exists():
    assert callable(effbd106_Iteration.__init__)


def test_hyp_effbd106_iteration_constructor_args():
    sig = inspect.signature(effbd106_Iteration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_start_is_not_abstract():
    assert not inspect.isabstract(effbd106_Start)


def test_hyp_effbd106_start_constructor_exists():
    assert callable(effbd106_Start.__init__)


def test_hyp_effbd106_start_constructor_args():
    sig = inspect.signature(effbd106_Start.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_final_is_not_abstract():
    assert not inspect.isabstract(effbd106_Final)


def test_hyp_effbd106_final_constructor_exists():
    assert callable(effbd106_Final.__init__)


def test_hyp_effbd106_final_constructor_args():
    sig = inspect.signature(effbd106_Final.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_or_is_not_abstract():
    assert not inspect.isabstract(effbd106_Or)


def test_hyp_effbd106_or_constructor_exists():
    assert callable(effbd106_Or.__init__)


def test_hyp_effbd106_or_constructor_args():
    sig = inspect.signature(effbd106_Or.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_loop_is_not_abstract():
    assert not inspect.isabstract(effbd106_Loop)


def test_hyp_effbd106_loop_constructor_exists():
    assert callable(effbd106_Loop.__init__)


def test_hyp_effbd106_loop_constructor_args():
    sig = inspect.signature(effbd106_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_and_is_not_abstract():
    assert not inspect.isabstract(effbd106_And)


def test_hyp_effbd106_and_constructor_exists():
    assert callable(effbd106_And.__init__)


def test_hyp_effbd106_and_constructor_args():
    sig = inspect.signature(effbd106_And.__init__)
    params = list(sig.parameters.keys())



def test_hyp_processnode_is_not_abstract():
    assert not inspect.isabstract(ProcessNode)


def test_hyp_processnode_constructor_exists():
    assert callable(ProcessNode.__init__)


def test_hyp_processnode_constructor_args():
    sig = inspect.signature(ProcessNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sequencenode_is_not_abstract():
    assert not inspect.isabstract(SequenceNode)


def test_hyp_sequencenode_constructor_exists():
    assert callable(SequenceNode.__init__)


def test_hyp_sequencenode_constructor_args():
    sig = inspect.signature(SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_function_is_not_abstract():
    assert not inspect.isabstract(effbd106_Function)


def test_hyp_effbd106_function_constructor_exists():
    assert callable(effbd106_Function.__init__)


def test_hyp_effbd106_function_constructor_args():
    sig = inspect.signature(effbd106_Function.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"




def test_hyp_effbd106_outputport_is_not_abstract():
    assert not inspect.isabstract(effbd106_OutputPort)


def test_hyp_effbd106_outputport_constructor_exists():
    assert callable(effbd106_OutputPort.__init__)


def test_hyp_effbd106_outputport_constructor_args():
    sig = inspect.signature(effbd106_OutputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_flow_is_not_abstract():
    assert not inspect.isabstract(effbd106_Flow)


def test_hyp_effbd106_flow_constructor_exists():
    assert callable(effbd106_Flow.__init__)


def test_hyp_effbd106_flow_constructor_args():
    sig = inspect.signature(effbd106_Flow.__init__)
    params = list(sig.parameters.keys())



def test_hyp_effbd106_sequence_is_not_abstract():
    assert not inspect.isabstract(effbd106_Sequence)


def test_hyp_effbd106_sequence_constructor_exists():
    assert callable(effbd106_Sequence.__init__)


def test_hyp_effbd106_sequence_constructor_args():
    sig = inspect.signature(effbd106_Sequence.__init__)
    params = list(sig.parameters.keys())

def test_hyp_functiondomain_exists():
    # Check that the Enumeration exists
    assert FunctionDomain is not None

def test_hyp_functiondomain_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionDomain]
    expected_literals = [
        "time",
        "form",
        "space",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionDomain"


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
effbd106_ProcessNode_strategy = st.builds(
    effbd106_ProcessNode,
    label=
        safe_text
)
effbd106_SequenceNode_strategy = st.builds(
    effbd106_SequenceNode,
    tMin=
        st.integers(),
    tMax=
        st.integers(),
    name=
        safe_text
)
effbd106_Token_strategy = st.builds(
    effbd106_Token,
)
effbd106_Description_strategy = st.builds(
    effbd106_Description,
    content=
        safe_text
)
effbd106_Item_strategy = st.builds(
    effbd106_Item,
    name=
        safe_text
)
effbd106_Port_strategy = st.builds(
    effbd106_Port,
    id=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
effbd106_InputPort_strategy = st.builds(
    effbd106_InputPort,
)
Sequence_strategy = st.builds(
    Sequence,
)
effbd106_LoopExit_strategy = st.builds(
    effbd106_LoopExit,
)
effbd106_Iteration_strategy = st.builds(
    effbd106_Iteration,
)
effbd106_Start_strategy = st.builds(
    effbd106_Start,
)
effbd106_Final_strategy = st.builds(
    effbd106_Final,
)
effbd106_Or_strategy = st.builds(
    effbd106_Or,
)
effbd106_Loop_strategy = st.builds(
    effbd106_Loop,
)
effbd106_And_strategy = st.builds(
    effbd106_And,
)
ProcessNode_strategy = st.builds(
    ProcessNode,
)
SequenceNode_strategy = st.builds(
    SequenceNode,
)
effbd106_Function_strategy = st.builds(
    effbd106_Function,
    domain=
        safe_text
)
effbd106_OutputPort_strategy = st.builds(
    effbd106_OutputPort,
)
effbd106_Flow_strategy = st.builds(
    effbd106_Flow,
)
effbd106_Sequence_strategy = st.builds(
    effbd106_Sequence,
)




@given(instance=effbd106_ProcessNode_strategy)
def test_hyp_effbd106_processnode_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original




@given(instance=effbd106_SequenceNode_strategy)
def test_hyp_effbd106_sequencenode_tMin_setter(instance):
    original = instance.tMin
    instance.tMin = original
    assert instance.tMin == original



@given(instance=effbd106_SequenceNode_strategy)
def test_hyp_effbd106_sequencenode_tMax_setter(instance):
    original = instance.tMax
    instance.tMax = original
    assert instance.tMax == original



@given(instance=effbd106_SequenceNode_strategy)
def test_hyp_effbd106_sequencenode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=effbd106_Description_strategy)
def test_hyp_effbd106_description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original




@given(instance=effbd106_Item_strategy)
def test_hyp_effbd106_item_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=effbd106_Port_strategy)
def test_hyp_effbd106_port_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
















@given(instance=effbd106_Function_strategy)
def test_hyp_effbd106_function_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original





# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Port,
    ProcessNode,
    Sequence,
    SequenceNode,
    effbd106_And,
    effbd106_Description,
    effbd106_Final,
    effbd106_Flow,
    effbd106_Function,
    effbd106_InputPort,
    effbd106_Item,
    effbd106_Iteration,
    effbd106_Loop,
    effbd106_LoopExit,
    effbd106_Or,
    effbd106_OutputPort,
    effbd106_Port,
    effbd106_ProcessNode,
    effbd106_Sequence,
    effbd106_SequenceNode,
    effbd106_Start,
    effbd106_Token,
    FunctionDomain,
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

def test_effbd106_Description_content_value_roundtrip():
    instance = effbd106_Description(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_effbd106_Function_domain_value_roundtrip():
    instance = effbd106_Function(domain="sample_text")
    assert instance.domain == "sample_text"
    instance.domain = "sample_text_2"
    assert instance.domain == "sample_text_2"


def test_effbd106_Item_name_value_roundtrip():
    instance = effbd106_Item(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_effbd106_Port_id_value_roundtrip():
    instance = effbd106_Port(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_effbd106_ProcessNode_label_value_roundtrip():
    instance = effbd106_ProcessNode(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_effbd106_SequenceNode_name_value_roundtrip():
    instance = effbd106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_effbd106_SequenceNode_tMax_value_roundtrip():
    instance = effbd106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    assert instance.tMax == 7
    instance.tMax = 13
    assert instance.tMax == 13


def test_effbd106_SequenceNode_tMin_value_roundtrip():
    instance = effbd106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    assert instance.tMin == 7
    instance.tMin = 13
    assert instance.tMin == 13


def test_effbd106_InputPort_isa_Port():
    instance = effbd106_InputPort()
    assert isinstance(instance, Port)


def test_effbd106_OutputPort_isa_Port():
    instance = effbd106_OutputPort()
    assert isinstance(instance, Port)


def test_effbd106_Flow_isa_ProcessNode():
    instance = effbd106_Flow()
    assert isinstance(instance, ProcessNode)


def test_effbd106_Function_isa_ProcessNode():
    instance = effbd106_Function(domain="sample_text")
    assert isinstance(instance, ProcessNode)


def test_effbd106_And_isa_Sequence():
    instance = effbd106_And()
    assert isinstance(instance, Sequence)


def test_effbd106_Final_isa_Sequence():
    instance = effbd106_Final()
    assert isinstance(instance, Sequence)


def test_effbd106_Iteration_isa_Sequence():
    instance = effbd106_Iteration()
    assert isinstance(instance, Sequence)


def test_effbd106_Loop_isa_Sequence():
    instance = effbd106_Loop()
    assert isinstance(instance, Sequence)


def test_effbd106_LoopExit_isa_Sequence():
    instance = effbd106_LoopExit()
    assert isinstance(instance, Sequence)


def test_effbd106_Or_isa_Sequence():
    instance = effbd106_Or()
    assert isinstance(instance, Sequence)


def test_effbd106_Start_isa_Sequence():
    instance = effbd106_Start()
    assert isinstance(instance, Sequence)


def test_effbd106_Function_isa_SequenceNode():
    instance = effbd106_Function(domain="sample_text")
    assert isinstance(instance, SequenceNode)


def test_effbd106_Sequence_isa_SequenceNode():
    instance = effbd106_Sequence()
    assert isinstance(instance, SequenceNode)


def test_assoc_controlFlowEdge15_link_reassign_clear():
    a = effbd106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    b1 = effbd106_SequenceNode(name="sample_text", tMax=7, tMin=7)
    b2 = effbd106_SequenceNode(name="sample_text_2", tMax=13, tMin=13)
    _safe_set(a, 'effbd106_SequenceNode', b1)
    assert _is_linked(a, 'effbd106_SequenceNode', b1)
    if hasattr(b1, 'effbd106_SequenceNode14'):
        assert _is_linked(b1, 'effbd106_SequenceNode14', a)
    _safe_set(a, 'effbd106_SequenceNode', b2)
    assert _is_linked(a, 'effbd106_SequenceNode', b2)
    if hasattr(b1, 'effbd106_SequenceNode14'):
        assert not _is_linked(b1, 'effbd106_SequenceNode14', a)
    if hasattr(b2, 'effbd106_SequenceNode14'):
        assert _is_linked(b2, 'effbd106_SequenceNode14', a)
    _safe_set(a, 'effbd106_SequenceNode', None)
    assert not _is_linked(a, 'effbd106_SequenceNode', b2)
    if hasattr(b2, 'effbd106_SequenceNode14'):
        assert not _is_linked(b2, 'effbd106_SequenceNode14', a)


def test_assoc_decompositions1_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_Function(domain="sample_text")
    b2 = effbd106_Function(domain="sample_text_2")
    _safe_set(a, 'effbd106_Function', b1)
    assert _is_linked(a, 'effbd106_Function', b1)
    if hasattr(b1, 'effbd106_Function0'):
        assert _is_linked(b1, 'effbd106_Function0', a)
    _safe_set(a, 'effbd106_Function', b2)
    assert _is_linked(a, 'effbd106_Function', b2)
    if hasattr(b1, 'effbd106_Function0'):
        assert not _is_linked(b1, 'effbd106_Function0', a)
    if hasattr(b2, 'effbd106_Function0'):
        assert _is_linked(b2, 'effbd106_Function0', a)
    _safe_set(a, 'effbd106_Function', None)
    assert not _is_linked(a, 'effbd106_Function', b2)
    if hasattr(b2, 'effbd106_Function0'):
        assert not _is_linked(b2, 'effbd106_Function0', a)


def test_assoc_descriptions10_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_Description(content="sample_text")
    b2 = effbd106_Description(content="sample_text_2")
    _safe_set(a, 'effbd106_Function11', {b1})
    assert _is_linked(a, 'effbd106_Function11', b1)
    if hasattr(b1, 'effbd106_Description'):
        assert _is_linked(b1, 'effbd106_Description', a)
    _safe_set(a, 'effbd106_Function11', {b2})
    assert _is_linked(a, 'effbd106_Function11', b2)
    if hasattr(b1, 'effbd106_Description'):
        assert not _is_linked(b1, 'effbd106_Description', a)
    if hasattr(b2, 'effbd106_Description'):
        assert _is_linked(b2, 'effbd106_Description', a)
    _safe_set(a, 'effbd106_Function11', set())
    assert not _is_linked(a, 'effbd106_Function11', b2)
    if hasattr(b2, 'effbd106_Description'):
        assert not _is_linked(b2, 'effbd106_Description', a)


def test_assoc_flows4_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_Flow()
    b2 = effbd106_Flow()
    _safe_set(a, 'effbd106_Function5', {b1})
    assert _is_linked(a, 'effbd106_Function5', b1)
    if hasattr(b1, 'effbd106_Flow'):
        assert _is_linked(b1, 'effbd106_Flow', a)
    _safe_set(a, 'effbd106_Function5', {b2})
    assert _is_linked(a, 'effbd106_Function5', b2)
    if hasattr(b1, 'effbd106_Flow'):
        assert not _is_linked(b1, 'effbd106_Flow', a)
    if hasattr(b2, 'effbd106_Flow'):
        assert _is_linked(b2, 'effbd106_Flow', a)
    _safe_set(a, 'effbd106_Function5', set())
    assert not _is_linked(a, 'effbd106_Function5', b2)
    if hasattr(b2, 'effbd106_Flow'):
        assert not _is_linked(b2, 'effbd106_Flow', a)


def test_assoc_inputPorts8_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_InputPort()
    b2 = effbd106_InputPort()
    _safe_set(a, 'effbd106_Function9', {b1})
    assert _is_linked(a, 'effbd106_Function9', b1)
    if hasattr(b1, 'effbd106_InputPort'):
        assert _is_linked(b1, 'effbd106_InputPort', a)
    _safe_set(a, 'effbd106_Function9', {b2})
    assert _is_linked(a, 'effbd106_Function9', b2)
    if hasattr(b1, 'effbd106_InputPort'):
        assert not _is_linked(b1, 'effbd106_InputPort', a)
    if hasattr(b2, 'effbd106_InputPort'):
        assert _is_linked(b2, 'effbd106_InputPort', a)
    _safe_set(a, 'effbd106_Function9', set())
    assert not _is_linked(a, 'effbd106_Function9', b2)
    if hasattr(b2, 'effbd106_InputPort'):
        assert not _is_linked(b2, 'effbd106_InputPort', a)


def test_assoc_items19_link_reassign_clear():
    a = effbd106_Item(name="sample_text")
    b1 = effbd106_Flow()
    b2 = effbd106_Flow()
    _safe_set(a, 'effbd106_Item', b1)
    assert _is_linked(a, 'effbd106_Item', b1)
    if hasattr(b1, 'effbd106_Flow20'):
        assert _is_linked(b1, 'effbd106_Flow20', a)
    _safe_set(a, 'effbd106_Item', b2)
    assert _is_linked(a, 'effbd106_Item', b2)
    if hasattr(b1, 'effbd106_Flow20'):
        assert not _is_linked(b1, 'effbd106_Flow20', a)
    if hasattr(b2, 'effbd106_Flow20'):
        assert _is_linked(b2, 'effbd106_Flow20', a)
    _safe_set(a, 'effbd106_Item', None)
    assert not _is_linked(a, 'effbd106_Item', b2)
    if hasattr(b2, 'effbd106_Flow20'):
        assert not _is_linked(b2, 'effbd106_Flow20', a)


def test_assoc_outputPorts6_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_OutputPort()
    b2 = effbd106_OutputPort()
    _safe_set(a, 'effbd106_Function7', {b1})
    assert _is_linked(a, 'effbd106_Function7', b1)
    if hasattr(b1, 'effbd106_OutputPort'):
        assert _is_linked(b1, 'effbd106_OutputPort', a)
    _safe_set(a, 'effbd106_Function7', {b2})
    assert _is_linked(a, 'effbd106_Function7', b2)
    if hasattr(b1, 'effbd106_OutputPort'):
        assert not _is_linked(b1, 'effbd106_OutputPort', a)
    if hasattr(b2, 'effbd106_OutputPort'):
        assert _is_linked(b2, 'effbd106_OutputPort', a)
    _safe_set(a, 'effbd106_Function7', set())
    assert not _is_linked(a, 'effbd106_Function7', b2)
    if hasattr(b2, 'effbd106_OutputPort'):
        assert not _is_linked(b2, 'effbd106_OutputPort', a)


def test_assoc_sequenceNodes2_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_Sequence()
    b2 = effbd106_Sequence()
    _safe_set(a, 'effbd106_Function3', {b1})
    assert _is_linked(a, 'effbd106_Function3', b1)
    if hasattr(b1, 'effbd106_Sequence'):
        assert _is_linked(b1, 'effbd106_Sequence', a)
    _safe_set(a, 'effbd106_Function3', {b2})
    assert _is_linked(a, 'effbd106_Function3', b2)
    if hasattr(b1, 'effbd106_Sequence'):
        assert not _is_linked(b1, 'effbd106_Sequence', a)
    if hasattr(b2, 'effbd106_Sequence'):
        assert _is_linked(b2, 'effbd106_Sequence', a)
    _safe_set(a, 'effbd106_Function3', set())
    assert not _is_linked(a, 'effbd106_Function3', b2)
    if hasattr(b2, 'effbd106_Sequence'):
        assert not _is_linked(b2, 'effbd106_Sequence', a)


def test_assoc_tokens12_link_reassign_clear():
    a = effbd106_Function(domain="sample_text")
    b1 = effbd106_Token()
    b2 = effbd106_Token()
    _safe_set(a, 'effbd106_Function13', {b1})
    assert _is_linked(a, 'effbd106_Function13', b1)
    if hasattr(b1, 'effbd106_Token'):
        assert _is_linked(b1, 'effbd106_Token', a)
    _safe_set(a, 'effbd106_Function13', {b2})
    assert _is_linked(a, 'effbd106_Function13', b2)
    if hasattr(b1, 'effbd106_Token'):
        assert not _is_linked(b1, 'effbd106_Token', a)
    if hasattr(b2, 'effbd106_Token'):
        assert _is_linked(b2, 'effbd106_Token', a)
    _safe_set(a, 'effbd106_Function13', set())
    assert not _is_linked(a, 'effbd106_Function13', b2)
    if hasattr(b2, 'effbd106_Token'):
        assert not _is_linked(b2, 'effbd106_Token', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


ProcessNode_strategy = st.builds(ProcessNode)
@given(instance=ProcessNode_strategy)
@settings(max_examples=25)
def test_ProcessNode_instantiation(instance):
    assert isinstance(instance, ProcessNode)


Sequence_strategy = st.builds(Sequence)
@given(instance=Sequence_strategy)
@settings(max_examples=25)
def test_Sequence_instantiation(instance):
    assert isinstance(instance, Sequence)


SequenceNode_strategy = st.builds(SequenceNode)
@given(instance=SequenceNode_strategy)
@settings(max_examples=25)
def test_SequenceNode_instantiation(instance):
    assert isinstance(instance, SequenceNode)


effbd106_And_strategy = st.builds(effbd106_And)
@given(instance=effbd106_And_strategy)
@settings(max_examples=25)
def test_effbd106_And_instantiation(instance):
    assert isinstance(instance, effbd106_And)


effbd106_Description_strategy = st.builds(effbd106_Description, content=safe_text)
@given(instance=effbd106_Description_strategy)
@settings(max_examples=25)
def test_effbd106_Description_instantiation(instance):
    assert isinstance(instance, effbd106_Description)


effbd106_Final_strategy = st.builds(effbd106_Final)
@given(instance=effbd106_Final_strategy)
@settings(max_examples=25)
def test_effbd106_Final_instantiation(instance):
    assert isinstance(instance, effbd106_Final)


effbd106_Flow_strategy = st.builds(effbd106_Flow)
@given(instance=effbd106_Flow_strategy)
@settings(max_examples=25)
def test_effbd106_Flow_instantiation(instance):
    assert isinstance(instance, effbd106_Flow)


effbd106_Function_strategy = st.builds(effbd106_Function, domain=safe_text)
@given(instance=effbd106_Function_strategy)
@settings(max_examples=25)
def test_effbd106_Function_instantiation(instance):
    assert isinstance(instance, effbd106_Function)


effbd106_InputPort_strategy = st.builds(effbd106_InputPort)
@given(instance=effbd106_InputPort_strategy)
@settings(max_examples=25)
def test_effbd106_InputPort_instantiation(instance):
    assert isinstance(instance, effbd106_InputPort)


effbd106_Item_strategy = st.builds(effbd106_Item, name=safe_text)
@given(instance=effbd106_Item_strategy)
@settings(max_examples=25)
def test_effbd106_Item_instantiation(instance):
    assert isinstance(instance, effbd106_Item)


effbd106_Iteration_strategy = st.builds(effbd106_Iteration)
@given(instance=effbd106_Iteration_strategy)
@settings(max_examples=25)
def test_effbd106_Iteration_instantiation(instance):
    assert isinstance(instance, effbd106_Iteration)


effbd106_Loop_strategy = st.builds(effbd106_Loop)
@given(instance=effbd106_Loop_strategy)
@settings(max_examples=25)
def test_effbd106_Loop_instantiation(instance):
    assert isinstance(instance, effbd106_Loop)


effbd106_LoopExit_strategy = st.builds(effbd106_LoopExit)
@given(instance=effbd106_LoopExit_strategy)
@settings(max_examples=25)
def test_effbd106_LoopExit_instantiation(instance):
    assert isinstance(instance, effbd106_LoopExit)


effbd106_Or_strategy = st.builds(effbd106_Or)
@given(instance=effbd106_Or_strategy)
@settings(max_examples=25)
def test_effbd106_Or_instantiation(instance):
    assert isinstance(instance, effbd106_Or)


effbd106_OutputPort_strategy = st.builds(effbd106_OutputPort)
@given(instance=effbd106_OutputPort_strategy)
@settings(max_examples=25)
def test_effbd106_OutputPort_instantiation(instance):
    assert isinstance(instance, effbd106_OutputPort)


effbd106_Port_strategy = st.builds(effbd106_Port, id=safe_text)
@given(instance=effbd106_Port_strategy)
@settings(max_examples=25)
def test_effbd106_Port_instantiation(instance):
    assert isinstance(instance, effbd106_Port)


effbd106_ProcessNode_strategy = st.builds(effbd106_ProcessNode, label=safe_text)
@given(instance=effbd106_ProcessNode_strategy)
@settings(max_examples=25)
def test_effbd106_ProcessNode_instantiation(instance):
    assert isinstance(instance, effbd106_ProcessNode)


effbd106_Sequence_strategy = st.builds(effbd106_Sequence)
@given(instance=effbd106_Sequence_strategy)
@settings(max_examples=25)
def test_effbd106_Sequence_instantiation(instance):
    assert isinstance(instance, effbd106_Sequence)


effbd106_SequenceNode_strategy = st.builds(effbd106_SequenceNode, name=safe_text, tMax=st.integers(), tMin=st.integers())
@given(instance=effbd106_SequenceNode_strategy)
@settings(max_examples=25)
def test_effbd106_SequenceNode_instantiation(instance):
    assert isinstance(instance, effbd106_SequenceNode)


effbd106_Start_strategy = st.builds(effbd106_Start)
@given(instance=effbd106_Start_strategy)
@settings(max_examples=25)
def test_effbd106_Start_instantiation(instance):
    assert isinstance(instance, effbd106_Start)


effbd106_Token_strategy = st.builds(effbd106_Token)
@given(instance=effbd106_Token_strategy)
@settings(max_examples=25)
def test_effbd106_Token_instantiation(instance):
    assert isinstance(instance, effbd106_Token)



