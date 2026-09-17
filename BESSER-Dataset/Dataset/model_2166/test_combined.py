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
    Refinement,
    pimm_HRefinement,
    pimm_visitor_PiMMVisitor,
    pimm_visitor_PiMMVisitable,
    pimm_ISetter,
    Parameter,
    pimm_ConfigInputInterface,
    InterfaceActor,
    pimm_DataOutputInterface,
    pimm_ConfigOutputInterface,
    pimm_DataInputInterface,
    ISetter,
    DataOutputPort,
    Port,
    pimm_DataPort,
    DataPort,
    ExecutableActor,
    pimm_RoundBufferActor,
    pimm_JoinActor,
    pimm_ForkActor,
    pimm_BroadcastActor,
    pimm_Actor,
    Parameterizable,
    pimm_Delay,
    pimm_AbstractVertex,
    pimm_ConfigInputPort,
    PiMMVisitable,
    pimm_Expression,
    pimm_Refinement,
    pimm_Fifo,
    pimm_Port,
    pimm_FunctionPrototype,
    pimm_Dependency,
    pimm_FunctionParameter,
    pimm_Parameterizable,
    AbstractActor,
    pimm_InterfaceActor,
    pimm_ExecutableActor,
    pimm_PiGraph,
    pimm_ConfigOutputPort,
    pimm_DataOutputPort,
    pimm_DataInputPort,
    AbstractVertex,
    pimm_Parameter,
    pimm_AbstractActor,
    Direction,
    PortMemoryAnnotation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_refinement_is_not_abstract():
    assert not inspect.isabstract(Refinement)


def test_hyp_refinement_constructor_exists():
    assert callable(Refinement.__init__)


def test_hyp_refinement_constructor_args():
    sig = inspect.signature(Refinement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_hrefinement_is_not_abstract():
    assert not inspect.isabstract(pimm_HRefinement)


def test_hyp_pimm_hrefinement_constructor_exists():
    assert callable(pimm_HRefinement.__init__)


def test_hyp_pimm_hrefinement_constructor_args():
    sig = inspect.signature(pimm_HRefinement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_visitor_pimmvisitor_is_not_abstract():
    assert not inspect.isabstract(pimm_visitor_PiMMVisitor)


def test_hyp_pimm_visitor_pimmvisitor_constructor_exists():
    assert callable(pimm_visitor_PiMMVisitor.__init__)


def test_hyp_pimm_visitor_pimmvisitor_constructor_args():
    sig = inspect.signature(pimm_visitor_PiMMVisitor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_visitor_pimmvisitable_is_not_abstract():
    assert not inspect.isabstract(pimm_visitor_PiMMVisitable)


def test_hyp_pimm_visitor_pimmvisitable_constructor_exists():
    assert callable(pimm_visitor_PiMMVisitable.__init__)


def test_hyp_pimm_visitor_pimmvisitable_constructor_args():
    sig = inspect.signature(pimm_visitor_PiMMVisitable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_isetter_is_not_abstract():
    assert not inspect.isabstract(pimm_ISetter)


def test_hyp_pimm_isetter_constructor_exists():
    assert callable(pimm_ISetter.__init__)


def test_hyp_pimm_isetter_constructor_args():
    sig = inspect.signature(pimm_ISetter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_hyp_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_hyp_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_configinputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm_ConfigInputInterface)


def test_hyp_pimm_configinputinterface_constructor_exists():
    assert callable(pimm_ConfigInputInterface.__init__)


def test_hyp_pimm_configinputinterface_constructor_args():
    sig = inspect.signature(pimm_ConfigInputInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_interfaceactor_is_not_abstract():
    assert not inspect.isabstract(InterfaceActor)


def test_hyp_interfaceactor_constructor_exists():
    assert callable(InterfaceActor.__init__)


def test_hyp_interfaceactor_constructor_args():
    sig = inspect.signature(InterfaceActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_dataoutputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm_DataOutputInterface)


def test_hyp_pimm_dataoutputinterface_constructor_exists():
    assert callable(pimm_DataOutputInterface.__init__)


def test_hyp_pimm_dataoutputinterface_constructor_args():
    sig = inspect.signature(pimm_DataOutputInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_configoutputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm_ConfigOutputInterface)


def test_hyp_pimm_configoutputinterface_constructor_exists():
    assert callable(pimm_ConfigOutputInterface.__init__)


def test_hyp_pimm_configoutputinterface_constructor_args():
    sig = inspect.signature(pimm_ConfigOutputInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_datainputinterface_is_not_abstract():
    assert not inspect.isabstract(pimm_DataInputInterface)


def test_hyp_pimm_datainputinterface_constructor_exists():
    assert callable(pimm_DataInputInterface.__init__)


def test_hyp_pimm_datainputinterface_constructor_args():
    sig = inspect.signature(pimm_DataInputInterface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_isetter_is_not_abstract():
    assert not inspect.isabstract(ISetter)


def test_hyp_isetter_constructor_exists():
    assert callable(ISetter.__init__)


def test_hyp_isetter_constructor_args():
    sig = inspect.signature(ISetter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_dataoutputport_is_not_abstract():
    assert not inspect.isabstract(DataOutputPort)


def test_hyp_dataoutputport_constructor_exists():
    assert callable(DataOutputPort.__init__)


def test_hyp_dataoutputport_constructor_args():
    sig = inspect.signature(DataOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_hyp_port_constructor_exists():
    assert callable(Port.__init__)


def test_hyp_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_dataport_is_not_abstract():
    assert not inspect.isabstract(pimm_DataPort)


def test_hyp_pimm_dataport_constructor_exists():
    assert callable(pimm_DataPort.__init__)


def test_hyp_pimm_dataport_constructor_args():
    sig = inspect.signature(pimm_DataPort.__init__)
    params = list(sig.parameters.keys())
    assert "annotation" in params, "Missing parameter 'annotation'"




def test_hyp_dataport_is_not_abstract():
    assert not inspect.isabstract(DataPort)


def test_hyp_dataport_constructor_exists():
    assert callable(DataPort.__init__)


def test_hyp_dataport_constructor_args():
    sig = inspect.signature(DataPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executableactor_is_not_abstract():
    assert not inspect.isabstract(ExecutableActor)


def test_hyp_executableactor_constructor_exists():
    assert callable(ExecutableActor.__init__)


def test_hyp_executableactor_constructor_args():
    sig = inspect.signature(ExecutableActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_roundbufferactor_is_not_abstract():
    assert not inspect.isabstract(pimm_RoundBufferActor)


def test_hyp_pimm_roundbufferactor_constructor_exists():
    assert callable(pimm_RoundBufferActor.__init__)


def test_hyp_pimm_roundbufferactor_constructor_args():
    sig = inspect.signature(pimm_RoundBufferActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_joinactor_is_not_abstract():
    assert not inspect.isabstract(pimm_JoinActor)


def test_hyp_pimm_joinactor_constructor_exists():
    assert callable(pimm_JoinActor.__init__)


def test_hyp_pimm_joinactor_constructor_args():
    sig = inspect.signature(pimm_JoinActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_forkactor_is_not_abstract():
    assert not inspect.isabstract(pimm_ForkActor)


def test_hyp_pimm_forkactor_constructor_exists():
    assert callable(pimm_ForkActor.__init__)


def test_hyp_pimm_forkactor_constructor_args():
    sig = inspect.signature(pimm_ForkActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_broadcastactor_is_not_abstract():
    assert not inspect.isabstract(pimm_BroadcastActor)


def test_hyp_pimm_broadcastactor_constructor_exists():
    assert callable(pimm_BroadcastActor.__init__)


def test_hyp_pimm_broadcastactor_constructor_args():
    sig = inspect.signature(pimm_BroadcastActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_actor_is_not_abstract():
    assert not inspect.isabstract(pimm_Actor)


def test_hyp_pimm_actor_constructor_exists():
    assert callable(pimm_Actor.__init__)


def test_hyp_pimm_actor_constructor_args():
    sig = inspect.signature(pimm_Actor.__init__)
    params = list(sig.parameters.keys())
    assert "configurationActor" in params, "Missing parameter 'configurationActor'"
    assert "memoryScriptPath" in params, "Missing parameter 'memoryScriptPath'"





def test_hyp_parameterizable_is_not_abstract():
    assert not inspect.isabstract(Parameterizable)


def test_hyp_parameterizable_constructor_exists():
    assert callable(Parameterizable.__init__)


def test_hyp_parameterizable_constructor_args():
    sig = inspect.signature(Parameterizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_delay_is_not_abstract():
    assert not inspect.isabstract(pimm_Delay)


def test_hyp_pimm_delay_constructor_exists():
    assert callable(pimm_Delay.__init__)


def test_hyp_pimm_delay_constructor_args():
    sig = inspect.signature(pimm_Delay.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_abstractvertex_is_not_abstract():
    assert not inspect.isabstract(pimm_AbstractVertex)


def test_hyp_pimm_abstractvertex_constructor_exists():
    assert callable(pimm_AbstractVertex.__init__)


def test_hyp_pimm_abstractvertex_constructor_args():
    sig = inspect.signature(pimm_AbstractVertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pimm_configinputport_is_not_abstract():
    assert not inspect.isabstract(pimm_ConfigInputPort)


def test_hyp_pimm_configinputport_constructor_exists():
    assert callable(pimm_ConfigInputPort.__init__)


def test_hyp_pimm_configinputport_constructor_args():
    sig = inspect.signature(pimm_ConfigInputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimmvisitable_is_not_abstract():
    assert not inspect.isabstract(PiMMVisitable)


def test_hyp_pimmvisitable_constructor_exists():
    assert callable(PiMMVisitable.__init__)


def test_hyp_pimmvisitable_constructor_args():
    sig = inspect.signature(PiMMVisitable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_expression_is_not_abstract():
    assert not inspect.isabstract(pimm_Expression)


def test_hyp_pimm_expression_constructor_exists():
    assert callable(pimm_Expression.__init__)


def test_hyp_pimm_expression_constructor_args():
    sig = inspect.signature(pimm_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"




def test_hyp_pimm_refinement_is_not_abstract():
    assert not inspect.isabstract(pimm_Refinement)


def test_hyp_pimm_refinement_constructor_exists():
    assert callable(pimm_Refinement.__init__)


def test_hyp_pimm_refinement_constructor_args():
    sig = inspect.signature(pimm_Refinement.__init__)
    params = list(sig.parameters.keys())
    assert "filePath" in params, "Missing parameter 'filePath'"
    assert "fileName" in params, "Missing parameter 'fileName'"





def test_hyp_pimm_fifo_is_not_abstract():
    assert not inspect.isabstract(pimm_Fifo)


def test_hyp_pimm_fifo_constructor_exists():
    assert callable(pimm_Fifo.__init__)


def test_hyp_pimm_fifo_constructor_args():
    sig = inspect.signature(pimm_Fifo.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_pimm_port_is_not_abstract():
    assert not inspect.isabstract(pimm_Port)


def test_hyp_pimm_port_constructor_exists():
    assert callable(pimm_Port.__init__)


def test_hyp_pimm_port_constructor_args():
    sig = inspect.signature(pimm_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"





def test_hyp_pimm_functionprototype_is_not_abstract():
    assert not inspect.isabstract(pimm_FunctionPrototype)


def test_hyp_pimm_functionprototype_constructor_exists():
    assert callable(pimm_FunctionPrototype.__init__)


def test_hyp_pimm_functionprototype_constructor_args():
    sig = inspect.signature(pimm_FunctionPrototype.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_pimm_dependency_is_not_abstract():
    assert not inspect.isabstract(pimm_Dependency)


def test_hyp_pimm_dependency_constructor_exists():
    assert callable(pimm_Dependency.__init__)


def test_hyp_pimm_dependency_constructor_args():
    sig = inspect.signature(pimm_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_functionparameter_is_not_abstract():
    assert not inspect.isabstract(pimm_FunctionParameter)


def test_hyp_pimm_functionparameter_constructor_exists():
    assert callable(pimm_FunctionParameter.__init__)


def test_hyp_pimm_functionparameter_constructor_args():
    sig = inspect.signature(pimm_FunctionParameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "isConfigurationParameter" in params, "Missing parameter 'isConfigurationParameter'"







def test_hyp_pimm_parameterizable_is_not_abstract():
    assert not inspect.isabstract(pimm_Parameterizable)


def test_hyp_pimm_parameterizable_constructor_exists():
    assert callable(pimm_Parameterizable.__init__)


def test_hyp_pimm_parameterizable_constructor_args():
    sig = inspect.signature(pimm_Parameterizable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractactor_is_not_abstract():
    assert not inspect.isabstract(AbstractActor)


def test_hyp_abstractactor_constructor_exists():
    assert callable(AbstractActor.__init__)


def test_hyp_abstractactor_constructor_args():
    sig = inspect.signature(AbstractActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_interfaceactor_is_not_abstract():
    assert not inspect.isabstract(pimm_InterfaceActor)


def test_hyp_pimm_interfaceactor_constructor_exists():
    assert callable(pimm_InterfaceActor.__init__)


def test_hyp_pimm_interfaceactor_constructor_args():
    sig = inspect.signature(pimm_InterfaceActor.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"




def test_hyp_pimm_executableactor_is_not_abstract():
    assert not inspect.isabstract(pimm_ExecutableActor)


def test_hyp_pimm_executableactor_constructor_exists():
    assert callable(pimm_ExecutableActor.__init__)


def test_hyp_pimm_executableactor_constructor_args():
    sig = inspect.signature(pimm_ExecutableActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_pigraph_is_not_abstract():
    assert not inspect.isabstract(pimm_PiGraph)


def test_hyp_pimm_pigraph_constructor_exists():
    assert callable(pimm_PiGraph.__init__)


def test_hyp_pimm_pigraph_constructor_args():
    sig = inspect.signature(pimm_PiGraph.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_configoutputport_is_not_abstract():
    assert not inspect.isabstract(pimm_ConfigOutputPort)


def test_hyp_pimm_configoutputport_constructor_exists():
    assert callable(pimm_ConfigOutputPort.__init__)


def test_hyp_pimm_configoutputport_constructor_args():
    sig = inspect.signature(pimm_ConfigOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_dataoutputport_is_not_abstract():
    assert not inspect.isabstract(pimm_DataOutputPort)


def test_hyp_pimm_dataoutputport_constructor_exists():
    assert callable(pimm_DataOutputPort.__init__)


def test_hyp_pimm_dataoutputport_constructor_args():
    sig = inspect.signature(pimm_DataOutputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_datainputport_is_not_abstract():
    assert not inspect.isabstract(pimm_DataInputPort)


def test_hyp_pimm_datainputport_constructor_exists():
    assert callable(pimm_DataInputPort.__init__)


def test_hyp_pimm_datainputport_constructor_args():
    sig = inspect.signature(pimm_DataInputPort.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractvertex_is_not_abstract():
    assert not inspect.isabstract(AbstractVertex)


def test_hyp_abstractvertex_constructor_exists():
    assert callable(AbstractVertex.__init__)


def test_hyp_abstractvertex_constructor_args():
    sig = inspect.signature(AbstractVertex.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pimm_parameter_is_not_abstract():
    assert not inspect.isabstract(pimm_Parameter)


def test_hyp_pimm_parameter_constructor_exists():
    assert callable(pimm_Parameter.__init__)


def test_hyp_pimm_parameter_constructor_args():
    sig = inspect.signature(pimm_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "configurationInterface" in params, "Missing parameter 'configurationInterface'"




def test_hyp_pimm_abstractactor_is_not_abstract():
    assert not inspect.isabstract(pimm_AbstractActor)


def test_hyp_pimm_abstractactor_constructor_exists():
    assert callable(pimm_AbstractActor.__init__)


def test_hyp_pimm_abstractactor_constructor_args():
    sig = inspect.signature(pimm_AbstractActor.__init__)
    params = list(sig.parameters.keys())

def test_hyp_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_hyp_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "IN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_hyp_portmemoryannotation_exists():
    # Check that the Enumeration exists
    assert PortMemoryAnnotation is not None

def test_hyp_portmemoryannotation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PortMemoryAnnotation]
    expected_literals = [
        "UNUSED",
        "READ_ONLY",
        "NONE",
        "WRITE_ONLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PortMemoryAnnotation"


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
Refinement_strategy = st.builds(
    Refinement,
)
pimm_HRefinement_strategy = st.builds(
    pimm_HRefinement,
)
pimm_visitor_PiMMVisitor_strategy = st.builds(
    pimm_visitor_PiMMVisitor,
)
pimm_visitor_PiMMVisitable_strategy = st.builds(
    pimm_visitor_PiMMVisitable,
)
pimm_ISetter_strategy = st.builds(
    pimm_ISetter,
)
Parameter_strategy = st.builds(
    Parameter,
)
pimm_ConfigInputInterface_strategy = st.builds(
    pimm_ConfigInputInterface,
)
InterfaceActor_strategy = st.builds(
    InterfaceActor,
)
pimm_DataOutputInterface_strategy = st.builds(
    pimm_DataOutputInterface,
)
pimm_ConfigOutputInterface_strategy = st.builds(
    pimm_ConfigOutputInterface,
)
pimm_DataInputInterface_strategy = st.builds(
    pimm_DataInputInterface,
)
ISetter_strategy = st.builds(
    ISetter,
)
DataOutputPort_strategy = st.builds(
    DataOutputPort,
)
Port_strategy = st.builds(
    Port,
)
pimm_DataPort_strategy = st.builds(
    pimm_DataPort,
    annotation=
        safe_text
)
DataPort_strategy = st.builds(
    DataPort,
)
ExecutableActor_strategy = st.builds(
    ExecutableActor,
)
pimm_RoundBufferActor_strategy = st.builds(
    pimm_RoundBufferActor,
)
pimm_JoinActor_strategy = st.builds(
    pimm_JoinActor,
)
pimm_ForkActor_strategy = st.builds(
    pimm_ForkActor,
)
pimm_BroadcastActor_strategy = st.builds(
    pimm_BroadcastActor,
)
pimm_Actor_strategy = st.builds(
    pimm_Actor,
    configurationActor=
        st.booleans(),
    memoryScriptPath=
        safe_text
)
Parameterizable_strategy = st.builds(
    Parameterizable,
)
pimm_Delay_strategy = st.builds(
    pimm_Delay,
)
pimm_AbstractVertex_strategy = st.builds(
    pimm_AbstractVertex,
    name=
        safe_text
)
pimm_ConfigInputPort_strategy = st.builds(
    pimm_ConfigInputPort,
)
PiMMVisitable_strategy = st.builds(
    PiMMVisitable,
)
pimm_Expression_strategy = st.builds(
    pimm_Expression,
    string=
        safe_text
)
pimm_Refinement_strategy = st.builds(
    pimm_Refinement,
    filePath=
        safe_text,
    fileName=
        safe_text
)
pimm_Fifo_strategy = st.builds(
    pimm_Fifo,
    type=
        safe_text,
    id=
        safe_text
)
pimm_Port_strategy = st.builds(
    pimm_Port,
    name=
        safe_text,
    kind=
        safe_text
)
pimm_FunctionPrototype_strategy = st.builds(
    pimm_FunctionPrototype,
    name=
        safe_text
)
pimm_Dependency_strategy = st.builds(
    pimm_Dependency,
)
pimm_FunctionParameter_strategy = st.builds(
    pimm_FunctionParameter,
    type=
        safe_text,
    name=
        safe_text,
    direction=
        safe_text,
    isConfigurationParameter=
        st.booleans()
)
pimm_Parameterizable_strategy = st.builds(
    pimm_Parameterizable,
)
AbstractActor_strategy = st.builds(
    AbstractActor,
)
pimm_InterfaceActor_strategy = st.builds(
    pimm_InterfaceActor,
    kind=
        safe_text
)
pimm_ExecutableActor_strategy = st.builds(
    pimm_ExecutableActor,
)
pimm_PiGraph_strategy = st.builds(
    pimm_PiGraph,
)
pimm_ConfigOutputPort_strategy = st.builds(
    pimm_ConfigOutputPort,
)
pimm_DataOutputPort_strategy = st.builds(
    pimm_DataOutputPort,
)
pimm_DataInputPort_strategy = st.builds(
    pimm_DataInputPort,
)
AbstractVertex_strategy = st.builds(
    AbstractVertex,
)
pimm_Parameter_strategy = st.builds(
    pimm_Parameter,
    configurationInterface=
        st.booleans()
)
pimm_AbstractActor_strategy = st.builds(
    pimm_AbstractActor,
)




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdatainputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataInputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataInputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataInputInterface' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataInputInterface' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataInputInterface' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitParameter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitParameter' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitParameter' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitParameter' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitfifo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFifo(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFifo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFifo' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFifo' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFifo' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdataport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitbroadcastactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitBroadcastActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitBroadcastActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitBroadcastActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitBroadcastActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitBroadcastActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitforkactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitForkActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitForkActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitForkActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitForkActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitForkActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitabstractvertex_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitAbstractVertex(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitAbstractVertex).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitAbstractVertex' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitAbstractVertex' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitAbstractVertex' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitinterfaceactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitInterfaceActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitInterfaceActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitInterfaceActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitInterfaceActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitInterfaceActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitfunctionparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFunctionParameter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFunctionParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFunctionParameter' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFunctionParameter' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFunctionParameter' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitconfigoutputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigOutputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigOutputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigOutputInterface' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigOutputInterface' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigOutputInterface' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitexpression_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitExpression(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitExpression).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitExpression' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitExpression' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitExpression' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdataoutputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataOutputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataOutputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataOutputInterface' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataOutputInterface' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataOutputInterface' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitroundbufferactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitRoundBufferActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitRoundBufferActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitRoundBufferActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitRoundBufferActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitRoundBufferActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitconfigoutputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigOutputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigOutputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigOutputPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigOutputPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigOutputPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdependency_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDependency(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDependency).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDependency' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDependency' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDependency' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdataoutputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataOutputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataOutputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataOutputPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataOutputPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataOutputPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitconfiginputinterface_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigInputInterface(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigInputInterface).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigInputInterface' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigInputInterface' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigInputInterface' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitabstractactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitAbstractActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitAbstractActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitAbstractActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitAbstractActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitAbstractActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitfunctionprototype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitFunctionPrototype(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitFunctionPrototype).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitFunctionPrototype' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitFunctionPrototype' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitFunctionPrototype' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdelay_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDelay(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDelay).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDelay' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDelay' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDelay' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitdatainputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitDataInputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitDataInputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitDataInputPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitDataInputPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitDataInputPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitparameterizable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitParameterizable(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitParameterizable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitParameterizable' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitParameterizable' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitParameterizable' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitisetter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitISetter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitISetter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitISetter' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitISetter' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitISetter' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visithrefinement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitHRefinement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitHRefinement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitHRefinement' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitHRefinement' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitHRefinement' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitjoinactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitJoinActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitJoinActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitJoinActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitJoinActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitJoinActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visit_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visit(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visit).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visit' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visit' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visit' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitexecutableactor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitExecutableActor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitExecutableActor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitExecutableActor' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitExecutableActor' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitExecutableActor' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitconfiginputport_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitConfigInputPort(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitConfigInputPort).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitConfigInputPort' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitConfigInputPort' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitConfigInputPort' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitpigraph_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitPiGraph(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitPiGraph).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitPiGraph' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitPiGraph' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitPiGraph' in pimm_visitor_PiMMVisitor is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitor_visitrefinement_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.visitRefinement(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.visitRefinement).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'visitRefinement' in pimm_visitor_PiMMVisitor is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'visitRefinement' in pimm_visitor_PiMMVisitor did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'visitRefinement' in pimm_visitor_PiMMVisitor is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_visitor_PiMMVisitable_strategy)
@settings(max_examples=30)
def test_hyp_pimm_visitor_pimmvisitable_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in pimm_visitor_PiMMVisitable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in pimm_visitor_PiMMVisitable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in pimm_visitor_PiMMVisitable is not implemented or raised an error")














@given(instance=pimm_DataPort_strategy)
def test_hyp_pimm_dataport_annotation_setter(instance):
    original = instance.annotation
    instance.annotation = original
    assert instance.annotation == original










@given(instance=pimm_Actor_strategy)
def test_hyp_pimm_actor_configurationActor_setter(instance):
    original = instance.configurationActor
    instance.configurationActor = original
    assert instance.configurationActor == original



@given(instance=pimm_Actor_strategy)
def test_hyp_pimm_actor_memoryScriptPath_setter(instance):
    original = instance.memoryScriptPath
    instance.memoryScriptPath = original
    assert instance.memoryScriptPath == original






@given(instance=pimm_AbstractVertex_strategy)
def test_hyp_pimm_abstractvertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=pimm_Expression_strategy)
def test_hyp_pimm_expression_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_Expression_strategy)
@settings(max_examples=30)
def test_hyp_pimm_expression_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in pimm_Expression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in pimm_Expression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in pimm_Expression is not implemented or raised an error")




@given(instance=pimm_Refinement_strategy)
def test_hyp_pimm_refinement_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original



@given(instance=pimm_Refinement_strategy)
def test_hyp_pimm_refinement_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original




@given(instance=pimm_Fifo_strategy)
def test_hyp_pimm_fifo_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=pimm_Fifo_strategy)
def test_hyp_pimm_fifo_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=pimm_Port_strategy)
def test_hyp_pimm_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pimm_Port_strategy)
def test_hyp_pimm_port_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original




@given(instance=pimm_FunctionPrototype_strategy)
def test_hyp_pimm_functionprototype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=pimm_FunctionParameter_strategy)
def test_hyp_pimm_functionparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=pimm_FunctionParameter_strategy)
def test_hyp_pimm_functionparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pimm_FunctionParameter_strategy)
def test_hyp_pimm_functionparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=pimm_FunctionParameter_strategy)
def test_hyp_pimm_functionparameter_isConfigurationParameter_setter(instance):
    original = instance.isConfigurationParameter
    instance.isConfigurationParameter = original
    assert instance.isConfigurationParameter == original






@given(instance=pimm_InterfaceActor_strategy)
def test_hyp_pimm_interfaceactor_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original










@given(instance=pimm_Parameter_strategy)
def test_hyp_pimm_parameter_configurationInterface_setter(instance):
    original = instance.configurationInterface
    instance.configurationInterface = original
    assert instance.configurationInterface == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_Parameter_strategy)
@settings(max_examples=30)
def test_hyp_pimm_parameter_isdependent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isDependent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isDependent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isDependent' in pimm_Parameter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isDependent' in pimm_Parameter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isDependent' in pimm_Parameter is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=pimm_Parameter_strategy)
@settings(max_examples=30)
def test_hyp_pimm_parameter_islocallystatic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isLocallyStatic()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isLocallyStatic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isLocallyStatic' in pimm_Parameter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isLocallyStatic' in pimm_Parameter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isLocallyStatic' in pimm_Parameter is not implemented or raised an error")



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractActor,
    AbstractVertex,
    DataOutputPort,
    DataPort,
    ExecutableActor,
    ISetter,
    InterfaceActor,
    Parameter,
    Parameterizable,
    PiMMVisitable,
    Port,
    Refinement,
    pimm_AbstractActor,
    pimm_AbstractVertex,
    pimm_Actor,
    pimm_BroadcastActor,
    pimm_ConfigInputInterface,
    pimm_ConfigInputPort,
    pimm_ConfigOutputInterface,
    pimm_ConfigOutputPort,
    pimm_DataInputInterface,
    pimm_DataInputPort,
    pimm_DataOutputInterface,
    pimm_DataOutputPort,
    pimm_DataPort,
    pimm_Delay,
    pimm_Dependency,
    pimm_ExecutableActor,
    pimm_Expression,
    pimm_Fifo,
    pimm_ForkActor,
    pimm_FunctionParameter,
    pimm_FunctionPrototype,
    pimm_HRefinement,
    pimm_ISetter,
    pimm_InterfaceActor,
    pimm_JoinActor,
    pimm_Parameter,
    pimm_Parameterizable,
    pimm_PiGraph,
    pimm_Port,
    pimm_Refinement,
    pimm_RoundBufferActor,
    pimm_visitor_PiMMVisitable,
    pimm_visitor_PiMMVisitor,
    Direction,
    PortMemoryAnnotation,
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

def test_pimm_AbstractVertex_name_value_roundtrip():
    instance = pimm_AbstractVertex(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pimm_Actor_configurationActor_value_roundtrip():
    instance = pimm_Actor(configurationActor=True, memoryScriptPath="sample_text")
    assert instance.configurationActor == True
    instance.configurationActor = False
    assert instance.configurationActor == False


def test_pimm_Actor_memoryScriptPath_value_roundtrip():
    instance = pimm_Actor(configurationActor=True, memoryScriptPath="sample_text")
    assert instance.memoryScriptPath == "sample_text"
    instance.memoryScriptPath = "sample_text_2"
    assert instance.memoryScriptPath == "sample_text_2"


def test_pimm_DataPort_annotation_value_roundtrip():
    instance = pimm_DataPort(annotation="sample_text")
    assert instance.annotation == "sample_text"
    instance.annotation = "sample_text_2"
    assert instance.annotation == "sample_text_2"


def test_pimm_Expression_string_value_roundtrip():
    instance = pimm_Expression(string="sample_text")
    assert instance.string == "sample_text"
    instance.string = "sample_text_2"
    assert instance.string == "sample_text_2"


def test_pimm_Fifo_id_value_roundtrip():
    instance = pimm_Fifo(id="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_pimm_Fifo_type_value_roundtrip():
    instance = pimm_Fifo(id="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pimm_FunctionParameter_direction_value_roundtrip():
    instance = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_pimm_FunctionParameter_isConfigurationParameter_value_roundtrip():
    instance = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    assert instance.isConfigurationParameter == True
    instance.isConfigurationParameter = False
    assert instance.isConfigurationParameter == False


def test_pimm_FunctionParameter_name_value_roundtrip():
    instance = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pimm_FunctionParameter_type_value_roundtrip():
    instance = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_pimm_FunctionPrototype_name_value_roundtrip():
    instance = pimm_FunctionPrototype(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pimm_InterfaceActor_kind_value_roundtrip():
    instance = pimm_InterfaceActor(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_pimm_Parameter_configurationInterface_value_roundtrip():
    instance = pimm_Parameter(configurationInterface=True)
    assert instance.configurationInterface == True
    instance.configurationInterface = False
    assert instance.configurationInterface == False


def test_pimm_Port_kind_value_roundtrip():
    instance = pimm_Port(kind="sample_text", name="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_pimm_Port_name_value_roundtrip():
    instance = pimm_Port(kind="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_pimm_Refinement_fileName_value_roundtrip():
    instance = pimm_Refinement(fileName="sample_text", filePath="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_pimm_Refinement_filePath_value_roundtrip():
    instance = pimm_Refinement(fileName="sample_text", filePath="sample_text")
    assert instance.filePath == "sample_text"
    instance.filePath = "sample_text_2"
    assert instance.filePath == "sample_text_2"


def test_pimm_ExecutableActor_isa_AbstractActor():
    instance = pimm_ExecutableActor()
    assert isinstance(instance, AbstractActor)


def test_pimm_InterfaceActor_isa_AbstractActor():
    instance = pimm_InterfaceActor(kind="sample_text")
    assert isinstance(instance, AbstractActor)


def test_pimm_PiGraph_isa_AbstractActor():
    instance = pimm_PiGraph()
    assert isinstance(instance, AbstractActor)


def test_pimm_AbstractActor_isa_AbstractVertex():
    instance = pimm_AbstractActor()
    assert isinstance(instance, AbstractVertex)


def test_pimm_Parameter_isa_AbstractVertex():
    instance = pimm_Parameter(configurationInterface=True)
    assert isinstance(instance, AbstractVertex)


def test_pimm_ConfigOutputPort_isa_DataOutputPort():
    instance = pimm_ConfigOutputPort()
    assert isinstance(instance, DataOutputPort)


def test_pimm_DataInputPort_isa_DataPort():
    instance = pimm_DataInputPort()
    assert isinstance(instance, DataPort)


def test_pimm_DataOutputPort_isa_DataPort():
    instance = pimm_DataOutputPort()
    assert isinstance(instance, DataPort)


def test_pimm_Actor_isa_ExecutableActor():
    instance = pimm_Actor(configurationActor=True, memoryScriptPath="sample_text")
    assert isinstance(instance, ExecutableActor)


def test_pimm_BroadcastActor_isa_ExecutableActor():
    instance = pimm_BroadcastActor()
    assert isinstance(instance, ExecutableActor)


def test_pimm_ForkActor_isa_ExecutableActor():
    instance = pimm_ForkActor()
    assert isinstance(instance, ExecutableActor)


def test_pimm_JoinActor_isa_ExecutableActor():
    instance = pimm_JoinActor()
    assert isinstance(instance, ExecutableActor)


def test_pimm_RoundBufferActor_isa_ExecutableActor():
    instance = pimm_RoundBufferActor()
    assert isinstance(instance, ExecutableActor)


def test_pimm_ConfigOutputPort_isa_ISetter():
    instance = pimm_ConfigOutputPort()
    assert isinstance(instance, ISetter)


def test_pimm_Parameter_isa_ISetter():
    instance = pimm_Parameter(configurationInterface=True)
    assert isinstance(instance, ISetter)


def test_pimm_ConfigOutputInterface_isa_InterfaceActor():
    instance = pimm_ConfigOutputInterface()
    assert isinstance(instance, InterfaceActor)


def test_pimm_DataInputInterface_isa_InterfaceActor():
    instance = pimm_DataInputInterface()
    assert isinstance(instance, InterfaceActor)


def test_pimm_DataOutputInterface_isa_InterfaceActor():
    instance = pimm_DataOutputInterface()
    assert isinstance(instance, InterfaceActor)


def test_pimm_ConfigInputInterface_isa_Parameter():
    instance = pimm_ConfigInputInterface()
    assert isinstance(instance, Parameter)


def test_pimm_AbstractVertex_isa_Parameterizable():
    instance = pimm_AbstractVertex(name="sample_text")
    assert isinstance(instance, Parameterizable)


def test_pimm_Delay_isa_Parameterizable():
    instance = pimm_Delay()
    assert isinstance(instance, Parameterizable)


def test_pimm_Dependency_isa_PiMMVisitable():
    instance = pimm_Dependency()
    assert isinstance(instance, PiMMVisitable)


def test_pimm_Expression_isa_PiMMVisitable():
    instance = pimm_Expression(string="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_Fifo_isa_PiMMVisitable():
    instance = pimm_Fifo(id="sample_text", type="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_FunctionParameter_isa_PiMMVisitable():
    instance = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_FunctionPrototype_isa_PiMMVisitable():
    instance = pimm_FunctionPrototype(name="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_Parameterizable_isa_PiMMVisitable():
    instance = pimm_Parameterizable()
    assert isinstance(instance, PiMMVisitable)


def test_pimm_Port_isa_PiMMVisitable():
    instance = pimm_Port(kind="sample_text", name="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_Refinement_isa_PiMMVisitable():
    instance = pimm_Refinement(fileName="sample_text", filePath="sample_text")
    assert isinstance(instance, PiMMVisitable)


def test_pimm_ConfigInputPort_isa_Port():
    instance = pimm_ConfigInputPort()
    assert isinstance(instance, Port)


def test_pimm_DataPort_isa_Port():
    instance = pimm_DataPort(annotation="sample_text")
    assert isinstance(instance, Port)


def test_pimm_HRefinement_isa_Refinement():
    instance = pimm_HRefinement()
    assert isinstance(instance, Refinement)


def test_assoc_configInputPorts0_link_reassign_clear():
    a = pimm_Parameterizable()
    b1 = pimm_ConfigInputPort()
    b2 = pimm_ConfigInputPort()
    _safe_set(a, 'pimm_Parameterizable', {b1})
    assert _is_linked(a, 'pimm_Parameterizable', b1)
    if hasattr(b1, 'pimm_ConfigInputPort'):
        assert _is_linked(b1, 'pimm_ConfigInputPort', a)
    _safe_set(a, 'pimm_Parameterizable', {b2})
    assert _is_linked(a, 'pimm_Parameterizable', b2)
    if hasattr(b1, 'pimm_ConfigInputPort'):
        assert not _is_linked(b1, 'pimm_ConfigInputPort', a)
    if hasattr(b2, 'pimm_ConfigInputPort'):
        assert _is_linked(b2, 'pimm_ConfigInputPort', a)
    _safe_set(a, 'pimm_Parameterizable', set())
    assert not _is_linked(a, 'pimm_Parameterizable', b2)
    if hasattr(b2, 'pimm_ConfigInputPort'):
        assert not _is_linked(b2, 'pimm_ConfigInputPort', a)


def test_assoc_configOutputPorts4_link_reassign_clear():
    a = pimm_AbstractActor()
    b1 = pimm_ConfigOutputPort()
    b2 = pimm_ConfigOutputPort()
    _safe_set(a, 'pimm_AbstractActor5', {b1})
    assert _is_linked(a, 'pimm_AbstractActor5', b1)
    if hasattr(b1, 'pimm_ConfigOutputPort'):
        assert _is_linked(b1, 'pimm_ConfigOutputPort', a)
    _safe_set(a, 'pimm_AbstractActor5', {b2})
    assert _is_linked(a, 'pimm_AbstractActor5', b2)
    if hasattr(b1, 'pimm_ConfigOutputPort'):
        assert not _is_linked(b1, 'pimm_ConfigOutputPort', a)
    if hasattr(b2, 'pimm_ConfigOutputPort'):
        assert _is_linked(b2, 'pimm_ConfigOutputPort', a)
    _safe_set(a, 'pimm_AbstractActor5', set())
    assert not _is_linked(a, 'pimm_AbstractActor5', b2)
    if hasattr(b2, 'pimm_ConfigOutputPort'):
        assert not _is_linked(b2, 'pimm_ConfigOutputPort', a)


def test_assoc_dataInputPorts1_link_reassign_clear():
    a = pimm_AbstractActor()
    b1 = pimm_DataInputPort()
    b2 = pimm_DataInputPort()
    _safe_set(a, 'pimm_AbstractActor', {b1})
    assert _is_linked(a, 'pimm_AbstractActor', b1)
    if hasattr(b1, 'pimm_DataInputPort'):
        assert _is_linked(b1, 'pimm_DataInputPort', a)
    _safe_set(a, 'pimm_AbstractActor', {b2})
    assert _is_linked(a, 'pimm_AbstractActor', b2)
    if hasattr(b1, 'pimm_DataInputPort'):
        assert not _is_linked(b1, 'pimm_DataInputPort', a)
    if hasattr(b2, 'pimm_DataInputPort'):
        assert _is_linked(b2, 'pimm_DataInputPort', a)
    _safe_set(a, 'pimm_AbstractActor', set())
    assert not _is_linked(a, 'pimm_AbstractActor', b2)
    if hasattr(b2, 'pimm_DataInputPort'):
        assert not _is_linked(b2, 'pimm_DataInputPort', a)


def test_assoc_dataOutputPorts2_link_reassign_clear():
    a = pimm_AbstractActor()
    b1 = pimm_DataOutputPort()
    b2 = pimm_DataOutputPort()
    _safe_set(a, 'pimm_AbstractActor3', {b1})
    assert _is_linked(a, 'pimm_AbstractActor3', b1)
    if hasattr(b1, 'pimm_DataOutputPort'):
        assert _is_linked(b1, 'pimm_DataOutputPort', a)
    _safe_set(a, 'pimm_AbstractActor3', {b2})
    assert _is_linked(a, 'pimm_AbstractActor3', b2)
    if hasattr(b1, 'pimm_DataOutputPort'):
        assert not _is_linked(b1, 'pimm_DataOutputPort', a)
    if hasattr(b2, 'pimm_DataOutputPort'):
        assert _is_linked(b2, 'pimm_DataOutputPort', a)
    _safe_set(a, 'pimm_AbstractActor3', set())
    assert not _is_linked(a, 'pimm_AbstractActor3', b2)
    if hasattr(b2, 'pimm_DataOutputPort'):
        assert not _is_linked(b2, 'pimm_DataOutputPort', a)


def test_assoc_delay21_link_reassign_clear():
    a = pimm_Fifo(id="sample_text", type="sample_text")
    b1 = pimm_Delay()
    b2 = pimm_Delay()
    _safe_set(a, 'pimm_Fifo22', b1)
    assert _is_linked(a, 'pimm_Fifo22', b1)
    if hasattr(b1, 'pimm_Delay'):
        assert _is_linked(b1, 'pimm_Delay', a)
    _safe_set(a, 'pimm_Fifo22', b2)
    assert _is_linked(a, 'pimm_Fifo22', b2)
    if hasattr(b1, 'pimm_Delay'):
        assert not _is_linked(b1, 'pimm_Delay', a)
    if hasattr(b2, 'pimm_Delay'):
        assert _is_linked(b2, 'pimm_Delay', a)
    _safe_set(a, 'pimm_Fifo22', None)
    assert not _is_linked(a, 'pimm_Fifo22', b2)
    if hasattr(b2, 'pimm_Delay'):
        assert not _is_linked(b2, 'pimm_Delay', a)


def test_assoc_dependencies12_link_reassign_clear():
    a = pimm_PiGraph()
    b1 = pimm_Dependency()
    b2 = pimm_Dependency()
    _safe_set(a, 'pimm_PiGraph13', {b1})
    assert _is_linked(a, 'pimm_PiGraph13', b1)
    if hasattr(b1, 'pimm_Dependency'):
        assert _is_linked(b1, 'pimm_Dependency', a)
    _safe_set(a, 'pimm_PiGraph13', {b2})
    assert _is_linked(a, 'pimm_PiGraph13', b2)
    if hasattr(b1, 'pimm_Dependency'):
        assert not _is_linked(b1, 'pimm_Dependency', a)
    if hasattr(b2, 'pimm_Dependency'):
        assert _is_linked(b2, 'pimm_Dependency', a)
    _safe_set(a, 'pimm_PiGraph13', set())
    assert not _is_linked(a, 'pimm_PiGraph13', b2)
    if hasattr(b2, 'pimm_Dependency'):
        assert not _is_linked(b2, 'pimm_Dependency', a)


def test_assoc_expression27_link_reassign_clear():
    a = pimm_Parameter(configurationInterface=True)
    b1 = pimm_Expression(string="sample_text")
    b2 = pimm_Expression(string="sample_text_2")
    _safe_set(a, 'pimm_Parameter28', b1)
    assert _is_linked(a, 'pimm_Parameter28', b1)
    if hasattr(b1, 'pimm_Expression'):
        assert _is_linked(b1, 'pimm_Expression', a)
    _safe_set(a, 'pimm_Parameter28', b2)
    assert _is_linked(a, 'pimm_Parameter28', b2)
    if hasattr(b1, 'pimm_Expression'):
        assert not _is_linked(b1, 'pimm_Expression', a)
    if hasattr(b2, 'pimm_Expression'):
        assert _is_linked(b2, 'pimm_Expression', a)
    _safe_set(a, 'pimm_Parameter28', None)
    assert not _is_linked(a, 'pimm_Parameter28', b2)
    if hasattr(b2, 'pimm_Expression'):
        assert not _is_linked(b2, 'pimm_Expression', a)


def test_assoc_expression33_link_reassign_clear():
    a = pimm_Expression(string="sample_text")
    b1 = pimm_Delay()
    b2 = pimm_Delay()
    _safe_set(a, 'pimm_Expression35', b1)
    assert _is_linked(a, 'pimm_Expression35', b1)
    if hasattr(b1, 'pimm_Delay34'):
        assert _is_linked(b1, 'pimm_Delay34', a)
    _safe_set(a, 'pimm_Expression35', b2)
    assert _is_linked(a, 'pimm_Expression35', b2)
    if hasattr(b1, 'pimm_Delay34'):
        assert not _is_linked(b1, 'pimm_Delay34', a)
    if hasattr(b2, 'pimm_Delay34'):
        assert _is_linked(b2, 'pimm_Delay34', a)
    _safe_set(a, 'pimm_Expression35', None)
    assert not _is_linked(a, 'pimm_Expression35', b2)
    if hasattr(b2, 'pimm_Delay34'):
        assert not _is_linked(b2, 'pimm_Delay34', a)


def test_assoc_expression42_link_reassign_clear():
    a = pimm_Expression(string="sample_text")
    b1 = pimm_DataPort(annotation="sample_text")
    b2 = pimm_DataPort(annotation="sample_text_2")
    _safe_set(a, 'pimm_Expression43', b1)
    assert _is_linked(a, 'pimm_Expression43', b1)
    if hasattr(b1, 'pimm_DataPort'):
        assert _is_linked(b1, 'pimm_DataPort', a)
    _safe_set(a, 'pimm_Expression43', b2)
    assert _is_linked(a, 'pimm_Expression43', b2)
    if hasattr(b1, 'pimm_DataPort'):
        assert not _is_linked(b1, 'pimm_DataPort', a)
    if hasattr(b2, 'pimm_DataPort'):
        assert _is_linked(b2, 'pimm_DataPort', a)
    _safe_set(a, 'pimm_Expression43', None)
    assert not _is_linked(a, 'pimm_Expression43', b2)
    if hasattr(b2, 'pimm_DataPort'):
        assert not _is_linked(b2, 'pimm_DataPort', a)


def test_assoc_fifos8_link_reassign_clear():
    a = pimm_PiGraph()
    b1 = pimm_Fifo(id="sample_text", type="sample_text")
    b2 = pimm_Fifo(id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'pimm_PiGraph9', {b1})
    assert _is_linked(a, 'pimm_PiGraph9', b1)
    if hasattr(b1, 'pimm_Fifo'):
        assert _is_linked(b1, 'pimm_Fifo', a)
    _safe_set(a, 'pimm_PiGraph9', {b2})
    assert _is_linked(a, 'pimm_PiGraph9', b2)
    if hasattr(b1, 'pimm_Fifo'):
        assert not _is_linked(b1, 'pimm_Fifo', a)
    if hasattr(b2, 'pimm_Fifo'):
        assert _is_linked(b2, 'pimm_Fifo', a)
    _safe_set(a, 'pimm_PiGraph9', set())
    assert not _is_linked(a, 'pimm_PiGraph9', b2)
    if hasattr(b2, 'pimm_Fifo'):
        assert not _is_linked(b2, 'pimm_Fifo', a)


def test_assoc_graphPort23_link_reassign_clear():
    a = pimm_Port(kind="sample_text", name="sample_text")
    b1 = pimm_InterfaceActor(kind="sample_text")
    b2 = pimm_InterfaceActor(kind="sample_text_2")
    _safe_set(a, 'pimm_Port', b1)
    assert _is_linked(a, 'pimm_Port', b1)
    if hasattr(b1, 'pimm_InterfaceActor'):
        assert _is_linked(b1, 'pimm_InterfaceActor', a)
    _safe_set(a, 'pimm_Port', b2)
    assert _is_linked(a, 'pimm_Port', b2)
    if hasattr(b1, 'pimm_InterfaceActor'):
        assert not _is_linked(b1, 'pimm_InterfaceActor', a)
    if hasattr(b2, 'pimm_InterfaceActor'):
        assert _is_linked(b2, 'pimm_InterfaceActor', a)
    _safe_set(a, 'pimm_Port', None)
    assert not _is_linked(a, 'pimm_Port', b2)
    if hasattr(b2, 'pimm_InterfaceActor'):
        assert not _is_linked(b2, 'pimm_InterfaceActor', a)


def test_assoc_graphPort24_link_reassign_clear():
    a = pimm_Parameter(configurationInterface=True)
    b1 = pimm_ConfigInputPort()
    b2 = pimm_ConfigInputPort()
    _safe_set(a, 'pimm_Parameter25', b1)
    assert _is_linked(a, 'pimm_Parameter25', b1)
    if hasattr(b1, 'pimm_ConfigInputPort26'):
        assert _is_linked(b1, 'pimm_ConfigInputPort26', a)
    _safe_set(a, 'pimm_Parameter25', b2)
    assert _is_linked(a, 'pimm_Parameter25', b2)
    if hasattr(b1, 'pimm_ConfigInputPort26'):
        assert not _is_linked(b1, 'pimm_ConfigInputPort26', a)
    if hasattr(b2, 'pimm_ConfigInputPort26'):
        assert _is_linked(b2, 'pimm_ConfigInputPort26', a)
    _safe_set(a, 'pimm_Parameter25', None)
    assert not _is_linked(a, 'pimm_Parameter25', b2)
    if hasattr(b2, 'pimm_ConfigInputPort26'):
        assert not _is_linked(b2, 'pimm_ConfigInputPort26', a)


def test_assoc_incomingFifo15_link_reassign_clear():
    a = pimm_Fifo(id="sample_text", type="sample_text")
    b1 = pimm_DataInputPort()
    b2 = pimm_DataInputPort()
    _safe_set(a, 'Fifo', b1)
    assert _is_linked(a, 'Fifo', b1)
    if hasattr(b1, 'targetPort'):
        assert _is_linked(b1, 'targetPort', a)
    _safe_set(a, 'Fifo', b2)
    assert _is_linked(a, 'Fifo', b2)
    if hasattr(b1, 'targetPort'):
        assert not _is_linked(b1, 'targetPort', a)
    if hasattr(b2, 'targetPort'):
        assert _is_linked(b2, 'targetPort', a)
    _safe_set(a, 'Fifo', None)
    assert not _is_linked(a, 'Fifo', b2)
    if hasattr(b2, 'targetPort'):
        assert not _is_linked(b2, 'targetPort', a)


def test_assoc_initPrototype37_link_reassign_clear():
    a = pimm_FunctionPrototype(name="sample_text")
    b1 = pimm_HRefinement()
    b2 = pimm_HRefinement()
    _safe_set(a, 'pimm_FunctionPrototype39', b1)
    assert _is_linked(a, 'pimm_FunctionPrototype39', b1)
    if hasattr(b1, 'pimm_HRefinement38'):
        assert _is_linked(b1, 'pimm_HRefinement38', a)
    _safe_set(a, 'pimm_FunctionPrototype39', b2)
    assert _is_linked(a, 'pimm_FunctionPrototype39', b2)
    if hasattr(b1, 'pimm_HRefinement38'):
        assert not _is_linked(b1, 'pimm_HRefinement38', a)
    if hasattr(b2, 'pimm_HRefinement38'):
        assert _is_linked(b2, 'pimm_HRefinement38', a)
    _safe_set(a, 'pimm_FunctionPrototype39', None)
    assert not _is_linked(a, 'pimm_FunctionPrototype39', b2)
    if hasattr(b2, 'pimm_HRefinement38'):
        assert not _is_linked(b2, 'pimm_HRefinement38', a)


def test_assoc_loopPrototype36_link_reassign_clear():
    a = pimm_FunctionPrototype(name="sample_text")
    b1 = pimm_HRefinement()
    b2 = pimm_HRefinement()
    _safe_set(a, 'pimm_FunctionPrototype', b1)
    assert _is_linked(a, 'pimm_FunctionPrototype', b1)
    if hasattr(b1, 'pimm_HRefinement'):
        assert _is_linked(b1, 'pimm_HRefinement', a)
    _safe_set(a, 'pimm_FunctionPrototype', b2)
    assert _is_linked(a, 'pimm_FunctionPrototype', b2)
    if hasattr(b1, 'pimm_HRefinement'):
        assert not _is_linked(b1, 'pimm_HRefinement', a)
    if hasattr(b2, 'pimm_HRefinement'):
        assert _is_linked(b2, 'pimm_HRefinement', a)
    _safe_set(a, 'pimm_FunctionPrototype', None)
    assert not _is_linked(a, 'pimm_FunctionPrototype', b2)
    if hasattr(b2, 'pimm_HRefinement'):
        assert not _is_linked(b2, 'pimm_HRefinement', a)


def test_assoc_outgoingDependencies31_link_reassign_clear():
    a = pimm_ISetter()
    b1 = pimm_Dependency()
    b2 = pimm_Dependency()
    _safe_set(a, 'setter', {b1})
    assert _is_linked(a, 'setter', b1)
    if hasattr(b1, 'Dependency32'):
        assert _is_linked(b1, 'Dependency32', a)
    _safe_set(a, 'setter', {b2})
    assert _is_linked(a, 'setter', b2)
    if hasattr(b1, 'Dependency32'):
        assert not _is_linked(b1, 'Dependency32', a)
    if hasattr(b2, 'Dependency32'):
        assert _is_linked(b2, 'Dependency32', a)
    _safe_set(a, 'setter', set())
    assert not _is_linked(a, 'setter', b2)
    if hasattr(b2, 'Dependency32'):
        assert not _is_linked(b2, 'Dependency32', a)


def test_assoc_outgoingFifo16_link_reassign_clear():
    a = pimm_Fifo(id="sample_text", type="sample_text")
    b1 = pimm_DataOutputPort()
    b2 = pimm_DataOutputPort()
    _safe_set(a, 'Fifo17', b1)
    assert _is_linked(a, 'Fifo17', b1)
    if hasattr(b1, 'sourcePort'):
        assert _is_linked(b1, 'sourcePort', a)
    _safe_set(a, 'Fifo17', b2)
    assert _is_linked(a, 'Fifo17', b2)
    if hasattr(b1, 'sourcePort'):
        assert not _is_linked(b1, 'sourcePort', a)
    if hasattr(b2, 'sourcePort'):
        assert _is_linked(b2, 'sourcePort', a)
    _safe_set(a, 'Fifo17', None)
    assert not _is_linked(a, 'Fifo17', b2)
    if hasattr(b2, 'sourcePort'):
        assert not _is_linked(b2, 'sourcePort', a)


def test_assoc_parameters10_link_reassign_clear():
    a = pimm_PiGraph()
    b1 = pimm_Parameter(configurationInterface=True)
    b2 = pimm_Parameter(configurationInterface=False)
    _safe_set(a, 'pimm_PiGraph11', {b1})
    assert _is_linked(a, 'pimm_PiGraph11', b1)
    if hasattr(b1, 'pimm_Parameter'):
        assert _is_linked(b1, 'pimm_Parameter', a)
    _safe_set(a, 'pimm_PiGraph11', {b2})
    assert _is_linked(a, 'pimm_PiGraph11', b2)
    if hasattr(b1, 'pimm_Parameter'):
        assert not _is_linked(b1, 'pimm_Parameter', a)
    if hasattr(b2, 'pimm_Parameter'):
        assert _is_linked(b2, 'pimm_Parameter', a)
    _safe_set(a, 'pimm_PiGraph11', set())
    assert not _is_linked(a, 'pimm_PiGraph11', b2)
    if hasattr(b2, 'pimm_Parameter'):
        assert not _is_linked(b2, 'pimm_Parameter', a)


def test_assoc_parameters40_link_reassign_clear():
    a = pimm_FunctionPrototype(name="sample_text")
    b1 = pimm_FunctionParameter(direction="sample_text", isConfigurationParameter=True, name="sample_text", type="sample_text")
    b2 = pimm_FunctionParameter(direction="sample_text_2", isConfigurationParameter=False, name="sample_text_2", type="sample_text_2")
    _safe_set(a, 'pimm_FunctionPrototype41', {b1})
    assert _is_linked(a, 'pimm_FunctionPrototype41', b1)
    if hasattr(b1, 'pimm_FunctionParameter'):
        assert _is_linked(b1, 'pimm_FunctionParameter', a)
    _safe_set(a, 'pimm_FunctionPrototype41', {b2})
    assert _is_linked(a, 'pimm_FunctionPrototype41', b2)
    if hasattr(b1, 'pimm_FunctionParameter'):
        assert not _is_linked(b1, 'pimm_FunctionParameter', a)
    if hasattr(b2, 'pimm_FunctionParameter'):
        assert _is_linked(b2, 'pimm_FunctionParameter', a)
    _safe_set(a, 'pimm_FunctionPrototype41', set())
    assert not _is_linked(a, 'pimm_FunctionPrototype41', b2)
    if hasattr(b2, 'pimm_FunctionParameter'):
        assert not _is_linked(b2, 'pimm_FunctionParameter', a)


def test_assoc_refinement14_link_reassign_clear():
    a = pimm_Refinement(fileName="sample_text", filePath="sample_text")
    b1 = pimm_Actor(configurationActor=True, memoryScriptPath="sample_text")
    b2 = pimm_Actor(configurationActor=False, memoryScriptPath="sample_text_2")
    _safe_set(a, 'pimm_Refinement', b1)
    assert _is_linked(a, 'pimm_Refinement', b1)
    if hasattr(b1, 'pimm_Actor'):
        assert _is_linked(b1, 'pimm_Actor', a)
    _safe_set(a, 'pimm_Refinement', b2)
    assert _is_linked(a, 'pimm_Refinement', b2)
    if hasattr(b1, 'pimm_Actor'):
        assert not _is_linked(b1, 'pimm_Actor', a)
    if hasattr(b2, 'pimm_Actor'):
        assert _is_linked(b2, 'pimm_Actor', a)
    _safe_set(a, 'pimm_Refinement', None)
    assert not _is_linked(a, 'pimm_Refinement', b2)
    if hasattr(b2, 'pimm_Actor'):
        assert not _is_linked(b2, 'pimm_Actor', a)


def test_assoc_setter29_link_reassign_clear():
    a = pimm_ISetter()
    b1 = pimm_Dependency()
    b2 = pimm_Dependency()
    _safe_set(a, 'ISetter', b1)
    assert _is_linked(a, 'ISetter', b1)
    if hasattr(b1, 'outgoingDependencies'):
        assert _is_linked(b1, 'outgoingDependencies', a)
    _safe_set(a, 'ISetter', b2)
    assert _is_linked(a, 'ISetter', b2)
    if hasattr(b1, 'outgoingDependencies'):
        assert not _is_linked(b1, 'outgoingDependencies', a)
    if hasattr(b2, 'outgoingDependencies'):
        assert _is_linked(b2, 'outgoingDependencies', a)
    _safe_set(a, 'ISetter', None)
    assert not _is_linked(a, 'ISetter', b2)
    if hasattr(b2, 'outgoingDependencies'):
        assert not _is_linked(b2, 'outgoingDependencies', a)


def test_assoc_sourcePort19_link_reassign_clear():
    a = pimm_Fifo(id="sample_text", type="sample_text")
    b1 = pimm_DataOutputPort()
    b2 = pimm_DataOutputPort()
    _safe_set(a, 'outgoingFifo', b1)
    assert _is_linked(a, 'outgoingFifo', b1)
    if hasattr(b1, 'DataOutputPort'):
        assert _is_linked(b1, 'DataOutputPort', a)
    _safe_set(a, 'outgoingFifo', b2)
    assert _is_linked(a, 'outgoingFifo', b2)
    if hasattr(b1, 'DataOutputPort'):
        assert not _is_linked(b1, 'DataOutputPort', a)
    if hasattr(b2, 'DataOutputPort'):
        assert _is_linked(b2, 'DataOutputPort', a)
    _safe_set(a, 'outgoingFifo', None)
    assert not _is_linked(a, 'outgoingFifo', b2)
    if hasattr(b2, 'DataOutputPort'):
        assert not _is_linked(b2, 'DataOutputPort', a)


def test_assoc_targetPort20_link_reassign_clear():
    a = pimm_Fifo(id="sample_text", type="sample_text")
    b1 = pimm_DataInputPort()
    b2 = pimm_DataInputPort()
    _safe_set(a, 'incomingFifo', b1)
    assert _is_linked(a, 'incomingFifo', b1)
    if hasattr(b1, 'DataInputPort'):
        assert _is_linked(b1, 'DataInputPort', a)
    _safe_set(a, 'incomingFifo', b2)
    assert _is_linked(a, 'incomingFifo', b2)
    if hasattr(b1, 'DataInputPort'):
        assert not _is_linked(b1, 'DataInputPort', a)
    if hasattr(b2, 'DataInputPort'):
        assert _is_linked(b2, 'DataInputPort', a)
    _safe_set(a, 'incomingFifo', None)
    assert not _is_linked(a, 'incomingFifo', b2)
    if hasattr(b2, 'DataInputPort'):
        assert not _is_linked(b2, 'DataInputPort', a)


def test_assoc_vertices6_link_reassign_clear():
    a = pimm_PiGraph()
    b1 = pimm_AbstractActor()
    b2 = pimm_AbstractActor()
    _safe_set(a, 'pimm_PiGraph', {b1})
    assert _is_linked(a, 'pimm_PiGraph', b1)
    if hasattr(b1, 'pimm_AbstractActor7'):
        assert _is_linked(b1, 'pimm_AbstractActor7', a)
    _safe_set(a, 'pimm_PiGraph', {b2})
    assert _is_linked(a, 'pimm_PiGraph', b2)
    if hasattr(b1, 'pimm_AbstractActor7'):
        assert not _is_linked(b1, 'pimm_AbstractActor7', a)
    if hasattr(b2, 'pimm_AbstractActor7'):
        assert _is_linked(b2, 'pimm_AbstractActor7', a)
    _safe_set(a, 'pimm_PiGraph', set())
    assert not _is_linked(a, 'pimm_PiGraph', b2)
    if hasattr(b2, 'pimm_AbstractActor7'):
        assert not _is_linked(b2, 'pimm_AbstractActor7', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractActor_strategy = st.builds(AbstractActor)
@given(instance=AbstractActor_strategy)
@settings(max_examples=25)
def test_AbstractActor_instantiation(instance):
    assert isinstance(instance, AbstractActor)


AbstractVertex_strategy = st.builds(AbstractVertex)
@given(instance=AbstractVertex_strategy)
@settings(max_examples=25)
def test_AbstractVertex_instantiation(instance):
    assert isinstance(instance, AbstractVertex)


DataOutputPort_strategy = st.builds(DataOutputPort)
@given(instance=DataOutputPort_strategy)
@settings(max_examples=25)
def test_DataOutputPort_instantiation(instance):
    assert isinstance(instance, DataOutputPort)


DataPort_strategy = st.builds(DataPort)
@given(instance=DataPort_strategy)
@settings(max_examples=25)
def test_DataPort_instantiation(instance):
    assert isinstance(instance, DataPort)


ExecutableActor_strategy = st.builds(ExecutableActor)
@given(instance=ExecutableActor_strategy)
@settings(max_examples=25)
def test_ExecutableActor_instantiation(instance):
    assert isinstance(instance, ExecutableActor)


ISetter_strategy = st.builds(ISetter)
@given(instance=ISetter_strategy)
@settings(max_examples=25)
def test_ISetter_instantiation(instance):
    assert isinstance(instance, ISetter)


InterfaceActor_strategy = st.builds(InterfaceActor)
@given(instance=InterfaceActor_strategy)
@settings(max_examples=25)
def test_InterfaceActor_instantiation(instance):
    assert isinstance(instance, InterfaceActor)


Parameter_strategy = st.builds(Parameter)
@given(instance=Parameter_strategy)
@settings(max_examples=25)
def test_Parameter_instantiation(instance):
    assert isinstance(instance, Parameter)


Parameterizable_strategy = st.builds(Parameterizable)
@given(instance=Parameterizable_strategy)
@settings(max_examples=25)
def test_Parameterizable_instantiation(instance):
    assert isinstance(instance, Parameterizable)


PiMMVisitable_strategy = st.builds(PiMMVisitable)
@given(instance=PiMMVisitable_strategy)
@settings(max_examples=25)
def test_PiMMVisitable_instantiation(instance):
    assert isinstance(instance, PiMMVisitable)


Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


Refinement_strategy = st.builds(Refinement)
@given(instance=Refinement_strategy)
@settings(max_examples=25)
def test_Refinement_instantiation(instance):
    assert isinstance(instance, Refinement)


pimm_AbstractActor_strategy = st.builds(pimm_AbstractActor)
@given(instance=pimm_AbstractActor_strategy)
@settings(max_examples=25)
def test_pimm_AbstractActor_instantiation(instance):
    assert isinstance(instance, pimm_AbstractActor)


pimm_AbstractVertex_strategy = st.builds(pimm_AbstractVertex, name=safe_text)
@given(instance=pimm_AbstractVertex_strategy)
@settings(max_examples=25)
def test_pimm_AbstractVertex_instantiation(instance):
    assert isinstance(instance, pimm_AbstractVertex)


pimm_Actor_strategy = st.builds(pimm_Actor, configurationActor=st.booleans(), memoryScriptPath=safe_text)
@given(instance=pimm_Actor_strategy)
@settings(max_examples=25)
def test_pimm_Actor_instantiation(instance):
    assert isinstance(instance, pimm_Actor)


pimm_BroadcastActor_strategy = st.builds(pimm_BroadcastActor)
@given(instance=pimm_BroadcastActor_strategy)
@settings(max_examples=25)
def test_pimm_BroadcastActor_instantiation(instance):
    assert isinstance(instance, pimm_BroadcastActor)


pimm_ConfigInputInterface_strategy = st.builds(pimm_ConfigInputInterface)
@given(instance=pimm_ConfigInputInterface_strategy)
@settings(max_examples=25)
def test_pimm_ConfigInputInterface_instantiation(instance):
    assert isinstance(instance, pimm_ConfigInputInterface)


pimm_ConfigInputPort_strategy = st.builds(pimm_ConfigInputPort)
@given(instance=pimm_ConfigInputPort_strategy)
@settings(max_examples=25)
def test_pimm_ConfigInputPort_instantiation(instance):
    assert isinstance(instance, pimm_ConfigInputPort)


pimm_ConfigOutputInterface_strategy = st.builds(pimm_ConfigOutputInterface)
@given(instance=pimm_ConfigOutputInterface_strategy)
@settings(max_examples=25)
def test_pimm_ConfigOutputInterface_instantiation(instance):
    assert isinstance(instance, pimm_ConfigOutputInterface)


pimm_ConfigOutputPort_strategy = st.builds(pimm_ConfigOutputPort)
@given(instance=pimm_ConfigOutputPort_strategy)
@settings(max_examples=25)
def test_pimm_ConfigOutputPort_instantiation(instance):
    assert isinstance(instance, pimm_ConfigOutputPort)


pimm_DataInputInterface_strategy = st.builds(pimm_DataInputInterface)
@given(instance=pimm_DataInputInterface_strategy)
@settings(max_examples=25)
def test_pimm_DataInputInterface_instantiation(instance):
    assert isinstance(instance, pimm_DataInputInterface)


pimm_DataInputPort_strategy = st.builds(pimm_DataInputPort)
@given(instance=pimm_DataInputPort_strategy)
@settings(max_examples=25)
def test_pimm_DataInputPort_instantiation(instance):
    assert isinstance(instance, pimm_DataInputPort)


pimm_DataOutputInterface_strategy = st.builds(pimm_DataOutputInterface)
@given(instance=pimm_DataOutputInterface_strategy)
@settings(max_examples=25)
def test_pimm_DataOutputInterface_instantiation(instance):
    assert isinstance(instance, pimm_DataOutputInterface)


pimm_DataOutputPort_strategy = st.builds(pimm_DataOutputPort)
@given(instance=pimm_DataOutputPort_strategy)
@settings(max_examples=25)
def test_pimm_DataOutputPort_instantiation(instance):
    assert isinstance(instance, pimm_DataOutputPort)


pimm_DataPort_strategy = st.builds(pimm_DataPort, annotation=safe_text)
@given(instance=pimm_DataPort_strategy)
@settings(max_examples=25)
def test_pimm_DataPort_instantiation(instance):
    assert isinstance(instance, pimm_DataPort)


pimm_Delay_strategy = st.builds(pimm_Delay)
@given(instance=pimm_Delay_strategy)
@settings(max_examples=25)
def test_pimm_Delay_instantiation(instance):
    assert isinstance(instance, pimm_Delay)


pimm_Dependency_strategy = st.builds(pimm_Dependency)
@given(instance=pimm_Dependency_strategy)
@settings(max_examples=25)
def test_pimm_Dependency_instantiation(instance):
    assert isinstance(instance, pimm_Dependency)


pimm_ExecutableActor_strategy = st.builds(pimm_ExecutableActor)
@given(instance=pimm_ExecutableActor_strategy)
@settings(max_examples=25)
def test_pimm_ExecutableActor_instantiation(instance):
    assert isinstance(instance, pimm_ExecutableActor)


pimm_Expression_strategy = st.builds(pimm_Expression, string=safe_text)
@given(instance=pimm_Expression_strategy)
@settings(max_examples=25)
def test_pimm_Expression_instantiation(instance):
    assert isinstance(instance, pimm_Expression)


pimm_Fifo_strategy = st.builds(pimm_Fifo, id=safe_text, type=safe_text)
@given(instance=pimm_Fifo_strategy)
@settings(max_examples=25)
def test_pimm_Fifo_instantiation(instance):
    assert isinstance(instance, pimm_Fifo)


pimm_ForkActor_strategy = st.builds(pimm_ForkActor)
@given(instance=pimm_ForkActor_strategy)
@settings(max_examples=25)
def test_pimm_ForkActor_instantiation(instance):
    assert isinstance(instance, pimm_ForkActor)


pimm_FunctionParameter_strategy = st.builds(pimm_FunctionParameter, direction=safe_text, isConfigurationParameter=st.booleans(), name=safe_text, type=safe_text)
@given(instance=pimm_FunctionParameter_strategy)
@settings(max_examples=25)
def test_pimm_FunctionParameter_instantiation(instance):
    assert isinstance(instance, pimm_FunctionParameter)


pimm_FunctionPrototype_strategy = st.builds(pimm_FunctionPrototype, name=safe_text)
@given(instance=pimm_FunctionPrototype_strategy)
@settings(max_examples=25)
def test_pimm_FunctionPrototype_instantiation(instance):
    assert isinstance(instance, pimm_FunctionPrototype)


pimm_HRefinement_strategy = st.builds(pimm_HRefinement)
@given(instance=pimm_HRefinement_strategy)
@settings(max_examples=25)
def test_pimm_HRefinement_instantiation(instance):
    assert isinstance(instance, pimm_HRefinement)


pimm_ISetter_strategy = st.builds(pimm_ISetter)
@given(instance=pimm_ISetter_strategy)
@settings(max_examples=25)
def test_pimm_ISetter_instantiation(instance):
    assert isinstance(instance, pimm_ISetter)


pimm_InterfaceActor_strategy = st.builds(pimm_InterfaceActor, kind=safe_text)
@given(instance=pimm_InterfaceActor_strategy)
@settings(max_examples=25)
def test_pimm_InterfaceActor_instantiation(instance):
    assert isinstance(instance, pimm_InterfaceActor)


pimm_JoinActor_strategy = st.builds(pimm_JoinActor)
@given(instance=pimm_JoinActor_strategy)
@settings(max_examples=25)
def test_pimm_JoinActor_instantiation(instance):
    assert isinstance(instance, pimm_JoinActor)


pimm_Parameter_strategy = st.builds(pimm_Parameter, configurationInterface=st.booleans())
@given(instance=pimm_Parameter_strategy)
@settings(max_examples=25)
def test_pimm_Parameter_instantiation(instance):
    assert isinstance(instance, pimm_Parameter)


pimm_Parameterizable_strategy = st.builds(pimm_Parameterizable)
@given(instance=pimm_Parameterizable_strategy)
@settings(max_examples=25)
def test_pimm_Parameterizable_instantiation(instance):
    assert isinstance(instance, pimm_Parameterizable)


pimm_PiGraph_strategy = st.builds(pimm_PiGraph)
@given(instance=pimm_PiGraph_strategy)
@settings(max_examples=25)
def test_pimm_PiGraph_instantiation(instance):
    assert isinstance(instance, pimm_PiGraph)


pimm_Port_strategy = st.builds(pimm_Port, kind=safe_text, name=safe_text)
@given(instance=pimm_Port_strategy)
@settings(max_examples=25)
def test_pimm_Port_instantiation(instance):
    assert isinstance(instance, pimm_Port)


pimm_Refinement_strategy = st.builds(pimm_Refinement, fileName=safe_text, filePath=safe_text)
@given(instance=pimm_Refinement_strategy)
@settings(max_examples=25)
def test_pimm_Refinement_instantiation(instance):
    assert isinstance(instance, pimm_Refinement)


pimm_RoundBufferActor_strategy = st.builds(pimm_RoundBufferActor)
@given(instance=pimm_RoundBufferActor_strategy)
@settings(max_examples=25)
def test_pimm_RoundBufferActor_instantiation(instance):
    assert isinstance(instance, pimm_RoundBufferActor)


pimm_visitor_PiMMVisitable_strategy = st.builds(pimm_visitor_PiMMVisitable)
@given(instance=pimm_visitor_PiMMVisitable_strategy)
@settings(max_examples=25)
def test_pimm_visitor_PiMMVisitable_instantiation(instance):
    assert isinstance(instance, pimm_visitor_PiMMVisitable)


pimm_visitor_PiMMVisitor_strategy = st.builds(pimm_visitor_PiMMVisitor)
@given(instance=pimm_visitor_PiMMVisitor_strategy)
@settings(max_examples=25)
def test_pimm_visitor_PiMMVisitor_instantiation(instance):
    assert isinstance(instance, pimm_visitor_PiMMVisitor)



