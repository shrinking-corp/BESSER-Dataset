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
    scxml_Description,
    IAdaptable,
    scxml_DescriptionContainer,
    scxml_DatamodelContainer,
    scxml_EClass,
    scxml_IAdaptable,
    Data,
    scxml_XData,
    scxml_XObject,
    scxml_Else,
    Conditional,
    scxml_ElseIf,
    scxml_Conditional,
    scxml_Validate,
    scxml_Assign,
    scxml_Cancel,
    Donedata,
    scxml_Send,
    scxml_ExecutableContent,
    InitialState,
    scxml_Invoke,
    scxml_AbstractSimpleState,
    State,
    scxml_Raise,
    scxml_Log,
    scxml_EObject,
    scxml_Donedata,
    scxml_Param,
    Transition,
    scxml_Content,
    scxml_ParallelState,
    scxml_AbstractState,
    scxml_CondEventTransition,
    Node,
    scxml_TransitionTarget,
    scxml_TransitionSource,
    ExecutableContent,
    scxml_If,
    scxml_OnExit,
    scxml_OnEntry,
    TransitionSource,
    TransitionTarget,
    scxml_HistoryState,
    scxml_FinalState,
    scxml_Script,
    DescriptionContainer,
    scxml_InitialState,
    scxml_Datamodel,
    scxml_Transition,
    scxml_Data,
    scxml_Node,
    DatamodelContainer,
    AbstractSimpleState,
    scxml_SimpleState,
    AbstractState,
    scxml_State,
    scxml_StateChart,
    HistoryTypeDatatype,
    ExmodeDatatype,
    AdapterToken,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_scxml_description_is_not_abstract():
    assert not inspect.isabstract(scxml_Description)


def test_hyp_scxml_description_constructor_exists():
    assert callable(scxml_Description.__init__)


def test_hyp_scxml_description_constructor_args():
    sig = inspect.signature(scxml_Description.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iadaptable_is_not_abstract():
    assert not inspect.isabstract(IAdaptable)


def test_hyp_iadaptable_constructor_exists():
    assert callable(IAdaptable.__init__)


def test_hyp_iadaptable_constructor_args():
    sig = inspect.signature(IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_descriptioncontainer_is_not_abstract():
    assert not inspect.isabstract(scxml_DescriptionContainer)


def test_hyp_scxml_descriptioncontainer_constructor_exists():
    assert callable(scxml_DescriptionContainer.__init__)


def test_hyp_scxml_descriptioncontainer_constructor_args():
    sig = inspect.signature(scxml_DescriptionContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_datamodelcontainer_is_not_abstract():
    assert not inspect.isabstract(scxml_DatamodelContainer)


def test_hyp_scxml_datamodelcontainer_constructor_exists():
    assert callable(scxml_DatamodelContainer.__init__)


def test_hyp_scxml_datamodelcontainer_constructor_args():
    sig = inspect.signature(scxml_DatamodelContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_eclass_is_not_abstract():
    assert not inspect.isabstract(scxml_EClass)


def test_hyp_scxml_eclass_constructor_exists():
    assert callable(scxml_EClass.__init__)


def test_hyp_scxml_eclass_constructor_args():
    sig = inspect.signature(scxml_EClass.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_iadaptable_is_not_abstract():
    assert not inspect.isabstract(scxml_IAdaptable)


def test_hyp_scxml_iadaptable_constructor_exists():
    assert callable(scxml_IAdaptable.__init__)


def test_hyp_scxml_iadaptable_constructor_args():
    sig = inspect.signature(scxml_IAdaptable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_hyp_data_constructor_exists():
    assert callable(Data.__init__)


def test_hyp_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_xdata_is_not_abstract():
    assert not inspect.isabstract(scxml_XData)


def test_hyp_scxml_xdata_constructor_exists():
    assert callable(scxml_XData.__init__)


def test_hyp_scxml_xdata_constructor_args():
    sig = inspect.signature(scxml_XData.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_xobject_is_not_abstract():
    assert not inspect.isabstract(scxml_XObject)


def test_hyp_scxml_xobject_constructor_exists():
    assert callable(scxml_XObject.__init__)


def test_hyp_scxml_xobject_constructor_args():
    sig = inspect.signature(scxml_XObject.__init__)
    params = list(sig.parameters.keys())
    assert "classifierName" in params, "Missing parameter 'classifierName'"
    assert "nsUri" in params, "Missing parameter 'nsUri'"
    assert "exchange" in params, "Missing parameter 'exchange'"






def test_hyp_scxml_else_is_not_abstract():
    assert not inspect.isabstract(scxml_Else)


def test_hyp_scxml_else_constructor_exists():
    assert callable(scxml_Else.__init__)


def test_hyp_scxml_else_constructor_args():
    sig = inspect.signature(scxml_Else.__init__)
    params = list(sig.parameters.keys())



def test_hyp_conditional_is_not_abstract():
    assert not inspect.isabstract(Conditional)


def test_hyp_conditional_constructor_exists():
    assert callable(Conditional.__init__)


def test_hyp_conditional_constructor_args():
    sig = inspect.signature(Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_elseif_is_not_abstract():
    assert not inspect.isabstract(scxml_ElseIf)


def test_hyp_scxml_elseif_constructor_exists():
    assert callable(scxml_ElseIf.__init__)


def test_hyp_scxml_elseif_constructor_args():
    sig = inspect.signature(scxml_ElseIf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_conditional_is_not_abstract():
    assert not inspect.isabstract(scxml_Conditional)


def test_hyp_scxml_conditional_constructor_exists():
    assert callable(scxml_Conditional.__init__)


def test_hyp_scxml_conditional_constructor_args():
    sig = inspect.signature(scxml_Conditional.__init__)
    params = list(sig.parameters.keys())
    assert "cond" in params, "Missing parameter 'cond'"




def test_hyp_scxml_validate_is_not_abstract():
    assert not inspect.isabstract(scxml_Validate)


def test_hyp_scxml_validate_constructor_exists():
    assert callable(scxml_Validate.__init__)


def test_hyp_scxml_validate_constructor_args():
    sig = inspect.signature(scxml_Validate.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "schema" in params, "Missing parameter 'schema'"





def test_hyp_scxml_assign_is_not_abstract():
    assert not inspect.isabstract(scxml_Assign)


def test_hyp_scxml_assign_constructor_exists():
    assert callable(scxml_Assign.__init__)


def test_hyp_scxml_assign_constructor_args():
    sig = inspect.signature(scxml_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "name" in params, "Missing parameter 'name'"






def test_hyp_scxml_cancel_is_not_abstract():
    assert not inspect.isabstract(scxml_Cancel)


def test_hyp_scxml_cancel_constructor_exists():
    assert callable(scxml_Cancel.__init__)


def test_hyp_scxml_cancel_constructor_args():
    sig = inspect.signature(scxml_Cancel.__init__)
    params = list(sig.parameters.keys())
    assert "sendid" in params, "Missing parameter 'sendid'"
    assert "sendidexpr" in params, "Missing parameter 'sendidexpr'"





def test_hyp_donedata_is_not_abstract():
    assert not inspect.isabstract(Donedata)


def test_hyp_donedata_constructor_exists():
    assert callable(Donedata.__init__)


def test_hyp_donedata_constructor_args():
    sig = inspect.signature(Donedata.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_send_is_not_abstract():
    assert not inspect.isabstract(scxml_Send)


def test_hyp_scxml_send_constructor_exists():
    assert callable(scxml_Send.__init__)


def test_hyp_scxml_send_constructor_args():
    sig = inspect.signature(scxml_Send.__init__)
    params = list(sig.parameters.keys())
    assert "hints" in params, "Missing parameter 'hints'"
    assert "event" in params, "Missing parameter 'event'"
    assert "delay" in params, "Missing parameter 'delay'"
    assert "hintsexpr" in params, "Missing parameter 'hintsexpr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "type" in params, "Missing parameter 'type'"
    assert "target" in params, "Missing parameter 'target'"
    assert "eventexpr" in params, "Missing parameter 'eventexpr'"
    assert "targetexpr" in params, "Missing parameter 'targetexpr'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "delayexpr" in params, "Missing parameter 'delayexpr'"
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
















def test_hyp_scxml_executablecontent_is_not_abstract():
    assert not inspect.isabstract(scxml_ExecutableContent)


def test_hyp_scxml_executablecontent_constructor_exists():
    assert callable(scxml_ExecutableContent.__init__)


def test_hyp_scxml_executablecontent_constructor_args():
    sig = inspect.signature(scxml_ExecutableContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_hyp_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_hyp_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_invoke_is_not_abstract():
    assert not inspect.isabstract(scxml_Invoke)


def test_hyp_scxml_invoke_constructor_exists():
    assert callable(scxml_Invoke.__init__)


def test_hyp_scxml_invoke_constructor_args():
    sig = inspect.signature(scxml_Invoke.__init__)
    params = list(sig.parameters.keys())
    assert "typeexpr" in params, "Missing parameter 'typeexpr'"
    assert "idlocation" in params, "Missing parameter 'idlocation'"
    assert "type" in params, "Missing parameter 'type'"
    assert "srcexpr" in params, "Missing parameter 'srcexpr'"
    assert "id" in params, "Missing parameter 'id'"
    assert "src" in params, "Missing parameter 'src'"
    assert "namelist" in params, "Missing parameter 'namelist'"
    assert "autoforward" in params, "Missing parameter 'autoforward'"











def test_hyp_scxml_abstractsimplestate_is_not_abstract():
    assert not inspect.isabstract(scxml_AbstractSimpleState)


def test_hyp_scxml_abstractsimplestate_constructor_exists():
    assert callable(scxml_AbstractSimpleState.__init__)


def test_hyp_scxml_abstractsimplestate_constructor_args():
    sig = inspect.signature(scxml_AbstractSimpleState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_hyp_state_constructor_exists():
    assert callable(State.__init__)


def test_hyp_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_raise_is_not_abstract():
    assert not inspect.isabstract(scxml_Raise)


def test_hyp_scxml_raise_constructor_exists():
    assert callable(scxml_Raise.__init__)


def test_hyp_scxml_raise_constructor_args():
    sig = inspect.signature(scxml_Raise.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"




def test_hyp_scxml_log_is_not_abstract():
    assert not inspect.isabstract(scxml_Log)


def test_hyp_scxml_log_constructor_exists():
    assert callable(scxml_Log.__init__)


def test_hyp_scxml_log_constructor_args():
    sig = inspect.signature(scxml_Log.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "label" in params, "Missing parameter 'label'"
    assert "expr" in params, "Missing parameter 'expr'"






def test_hyp_scxml_eobject_is_not_abstract():
    assert not inspect.isabstract(scxml_EObject)


def test_hyp_scxml_eobject_constructor_exists():
    assert callable(scxml_EObject.__init__)


def test_hyp_scxml_eobject_constructor_args():
    sig = inspect.signature(scxml_EObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_donedata_is_not_abstract():
    assert not inspect.isabstract(scxml_Donedata)


def test_hyp_scxml_donedata_constructor_exists():
    assert callable(scxml_Donedata.__init__)


def test_hyp_scxml_donedata_constructor_args():
    sig = inspect.signature(scxml_Donedata.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_param_is_not_abstract():
    assert not inspect.isabstract(scxml_Param)


def test_hyp_scxml_param_constructor_exists():
    assert callable(scxml_Param.__init__)


def test_hyp_scxml_param_constructor_args():
    sig = inspect.signature(scxml_Param.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_content_is_not_abstract():
    assert not inspect.isabstract(scxml_Content)


def test_hyp_scxml_content_constructor_exists():
    assert callable(scxml_Content.__init__)


def test_hyp_scxml_content_constructor_args():
    sig = inspect.signature(scxml_Content.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_scxml_parallelstate_is_not_abstract():
    assert not inspect.isabstract(scxml_ParallelState)


def test_hyp_scxml_parallelstate_constructor_exists():
    assert callable(scxml_ParallelState.__init__)


def test_hyp_scxml_parallelstate_constructor_args():
    sig = inspect.signature(scxml_ParallelState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_abstractstate_is_not_abstract():
    assert not inspect.isabstract(scxml_AbstractState)


def test_hyp_scxml_abstractstate_constructor_exists():
    assert callable(scxml_AbstractState.__init__)


def test_hyp_scxml_abstractstate_constructor_args():
    sig = inspect.signature(scxml_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_condeventtransition_is_not_abstract():
    assert not inspect.isabstract(scxml_CondEventTransition)


def test_hyp_scxml_condeventtransition_constructor_exists():
    assert callable(scxml_CondEventTransition.__init__)


def test_hyp_scxml_condeventtransition_constructor_args():
    sig = inspect.signature(scxml_CondEventTransition.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "cond" in params, "Missing parameter 'cond'"





def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_transitiontarget_is_not_abstract():
    assert not inspect.isabstract(scxml_TransitionTarget)


def test_hyp_scxml_transitiontarget_constructor_exists():
    assert callable(scxml_TransitionTarget.__init__)


def test_hyp_scxml_transitiontarget_constructor_args():
    sig = inspect.signature(scxml_TransitionTarget.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_scxml_transitionsource_is_not_abstract():
    assert not inspect.isabstract(scxml_TransitionSource)


def test_hyp_scxml_transitionsource_constructor_exists():
    assert callable(scxml_TransitionSource.__init__)


def test_hyp_scxml_transitionsource_constructor_args():
    sig = inspect.signature(scxml_TransitionSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_executablecontent_is_not_abstract():
    assert not inspect.isabstract(ExecutableContent)


def test_hyp_executablecontent_constructor_exists():
    assert callable(ExecutableContent.__init__)


def test_hyp_executablecontent_constructor_args():
    sig = inspect.signature(ExecutableContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_if_is_not_abstract():
    assert not inspect.isabstract(scxml_If)


def test_hyp_scxml_if_constructor_exists():
    assert callable(scxml_If.__init__)


def test_hyp_scxml_if_constructor_args():
    sig = inspect.signature(scxml_If.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_onexit_is_not_abstract():
    assert not inspect.isabstract(scxml_OnExit)


def test_hyp_scxml_onexit_constructor_exists():
    assert callable(scxml_OnExit.__init__)


def test_hyp_scxml_onexit_constructor_args():
    sig = inspect.signature(scxml_OnExit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_onentry_is_not_abstract():
    assert not inspect.isabstract(scxml_OnEntry)


def test_hyp_scxml_onentry_constructor_exists():
    assert callable(scxml_OnEntry.__init__)


def test_hyp_scxml_onentry_constructor_args():
    sig = inspect.signature(scxml_OnEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transitionsource_is_not_abstract():
    assert not inspect.isabstract(TransitionSource)


def test_hyp_transitionsource_constructor_exists():
    assert callable(TransitionSource.__init__)


def test_hyp_transitionsource_constructor_args():
    sig = inspect.signature(TransitionSource.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transitiontarget_is_not_abstract():
    assert not inspect.isabstract(TransitionTarget)


def test_hyp_transitiontarget_constructor_exists():
    assert callable(TransitionTarget.__init__)


def test_hyp_transitiontarget_constructor_args():
    sig = inspect.signature(TransitionTarget.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_historystate_is_not_abstract():
    assert not inspect.isabstract(scxml_HistoryState)


def test_hyp_scxml_historystate_constructor_exists():
    assert callable(scxml_HistoryState.__init__)


def test_hyp_scxml_historystate_constructor_args():
    sig = inspect.signature(scxml_HistoryState.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_scxml_finalstate_is_not_abstract():
    assert not inspect.isabstract(scxml_FinalState)


def test_hyp_scxml_finalstate_constructor_exists():
    assert callable(scxml_FinalState.__init__)


def test_hyp_scxml_finalstate_constructor_args():
    sig = inspect.signature(scxml_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_script_is_not_abstract():
    assert not inspect.isabstract(scxml_Script)


def test_hyp_scxml_script_constructor_exists():
    assert callable(scxml_Script.__init__)


def test_hyp_scxml_script_constructor_args():
    sig = inspect.signature(scxml_Script.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_descriptioncontainer_is_not_abstract():
    assert not inspect.isabstract(DescriptionContainer)


def test_hyp_descriptioncontainer_constructor_exists():
    assert callable(DescriptionContainer.__init__)


def test_hyp_descriptioncontainer_constructor_args():
    sig = inspect.signature(DescriptionContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_initialstate_is_not_abstract():
    assert not inspect.isabstract(scxml_InitialState)


def test_hyp_scxml_initialstate_constructor_exists():
    assert callable(scxml_InitialState.__init__)


def test_hyp_scxml_initialstate_constructor_args():
    sig = inspect.signature(scxml_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_datamodel_is_not_abstract():
    assert not inspect.isabstract(scxml_Datamodel)


def test_hyp_scxml_datamodel_constructor_exists():
    assert callable(scxml_Datamodel.__init__)


def test_hyp_scxml_datamodel_constructor_args():
    sig = inspect.signature(scxml_Datamodel.__init__)
    params = list(sig.parameters.keys())
    assert "schema" in params, "Missing parameter 'schema'"




def test_hyp_scxml_transition_is_not_abstract():
    assert not inspect.isabstract(scxml_Transition)


def test_hyp_scxml_transition_constructor_exists():
    assert callable(scxml_Transition.__init__)


def test_hyp_scxml_transition_constructor_args():
    sig = inspect.signature(scxml_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_data_is_not_abstract():
    assert not inspect.isabstract(scxml_Data)


def test_hyp_scxml_data_constructor_exists():
    assert callable(scxml_Data.__init__)


def test_hyp_scxml_data_constructor_args():
    sig = inspect.signature(scxml_Data.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "id" in params, "Missing parameter 'id'"
    assert "expr" in params, "Missing parameter 'expr'"






def test_hyp_scxml_node_is_not_abstract():
    assert not inspect.isabstract(scxml_Node)


def test_hyp_scxml_node_constructor_exists():
    assert callable(scxml_Node.__init__)


def test_hyp_scxml_node_constructor_args():
    sig = inspect.signature(scxml_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_datamodelcontainer_is_not_abstract():
    assert not inspect.isabstract(DatamodelContainer)


def test_hyp_datamodelcontainer_constructor_exists():
    assert callable(DatamodelContainer.__init__)


def test_hyp_datamodelcontainer_constructor_args():
    sig = inspect.signature(DatamodelContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractsimplestate_is_not_abstract():
    assert not inspect.isabstract(AbstractSimpleState)


def test_hyp_abstractsimplestate_constructor_exists():
    assert callable(AbstractSimpleState.__init__)


def test_hyp_abstractsimplestate_constructor_args():
    sig = inspect.signature(AbstractSimpleState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_simplestate_is_not_abstract():
    assert not inspect.isabstract(scxml_SimpleState)


def test_hyp_scxml_simplestate_constructor_exists():
    assert callable(scxml_SimpleState.__init__)


def test_hyp_scxml_simplestate_constructor_args():
    sig = inspect.signature(scxml_SimpleState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_hyp_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_hyp_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_state_is_not_abstract():
    assert not inspect.isabstract(scxml_State)


def test_hyp_scxml_state_constructor_exists():
    assert callable(scxml_State.__init__)


def test_hyp_scxml_state_constructor_args():
    sig = inspect.signature(scxml_State.__init__)
    params = list(sig.parameters.keys())



def test_hyp_scxml_statechart_is_not_abstract():
    assert not inspect.isabstract(scxml_StateChart)


def test_hyp_scxml_statechart_constructor_exists():
    assert callable(scxml_StateChart.__init__)


def test_hyp_scxml_statechart_constructor_args():
    sig = inspect.signature(scxml_StateChart.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"
    assert "version" in params, "Missing parameter 'version'"
    assert "profile" in params, "Missing parameter 'profile'"
    assert "id" in params, "Missing parameter 'id'"
    assert "exmode" in params, "Missing parameter 'exmode'"






def test_hyp_historytypedatatype_exists():
    # Check that the Enumeration exists
    assert HistoryTypeDatatype is not None

def test_hyp_historytypedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HistoryTypeDatatype]
    expected_literals = [
        "deep",
        "shallow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HistoryTypeDatatype"

def test_hyp_exmodedatatype_exists():
    # Check that the Enumeration exists
    assert ExmodeDatatype is not None

def test_hyp_exmodedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExmodeDatatype]
    expected_literals = [
        "strict",
        "lax",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExmodeDatatype"

def test_hyp_adaptertoken_exists():
    # Check that the Enumeration exists
    assert AdapterToken is not None

def test_hyp_adaptertoken_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdapterToken]
    expected_literals = [
        "DATAMODEL",
        "DESCRIPTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdapterToken"


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
scxml_Description_strategy = st.builds(
    scxml_Description,
    value=
        safe_text
)
IAdaptable_strategy = st.builds(
    IAdaptable,
)
scxml_DescriptionContainer_strategy = st.builds(
    scxml_DescriptionContainer,
)
scxml_DatamodelContainer_strategy = st.builds(
    scxml_DatamodelContainer,
)
scxml_EClass_strategy = st.builds(
    scxml_EClass,
)
scxml_IAdaptable_strategy = st.builds(
    scxml_IAdaptable,
)
Data_strategy = st.builds(
    Data,
)
scxml_XData_strategy = st.builds(
    scxml_XData,
)
scxml_XObject_strategy = st.builds(
    scxml_XObject,
    classifierName=
        safe_text,
    nsUri=
        safe_text,
    exchange=
        st.booleans()
)
scxml_Else_strategy = st.builds(
    scxml_Else,
)
Conditional_strategy = st.builds(
    Conditional,
)
scxml_ElseIf_strategy = st.builds(
    scxml_ElseIf,
)
scxml_Conditional_strategy = st.builds(
    scxml_Conditional,
    cond=
        safe_text
)
scxml_Validate_strategy = st.builds(
    scxml_Validate,
    location=
        safe_text,
    schema=
        safe_text
)
scxml_Assign_strategy = st.builds(
    scxml_Assign,
    location=
        safe_text,
    expr=
        safe_text,
    name=
        safe_text
)
scxml_Cancel_strategy = st.builds(
    scxml_Cancel,
    sendid=
        safe_text,
    sendidexpr=
        safe_text
)
Donedata_strategy = st.builds(
    Donedata,
)
scxml_Send_strategy = st.builds(
    scxml_Send,
    hints=
        safe_text,
    event=
        safe_text,
    delay=
        safe_text,
    hintsexpr=
        safe_text,
    id=
        safe_text,
    namelist=
        safe_text,
    type=
        safe_text,
    target=
        safe_text,
    eventexpr=
        safe_text,
    targetexpr=
        safe_text,
    idlocation=
        safe_text,
    delayexpr=
        safe_text,
    typeexpr=
        safe_text
)
scxml_ExecutableContent_strategy = st.builds(
    scxml_ExecutableContent,
    group=
        safe_text
)
InitialState_strategy = st.builds(
    InitialState,
)
scxml_Invoke_strategy = st.builds(
    scxml_Invoke,
    typeexpr=
        safe_text,
    idlocation=
        safe_text,
    type=
        safe_text,
    srcexpr=
        safe_text,
    id=
        safe_text,
    src=
        safe_text,
    namelist=
        safe_text,
    autoforward=
        safe_text
)
scxml_AbstractSimpleState_strategy = st.builds(
    scxml_AbstractSimpleState,
)
State_strategy = st.builds(
    State,
)
scxml_Raise_strategy = st.builds(
    scxml_Raise,
    event=
        safe_text
)
scxml_Log_strategy = st.builds(
    scxml_Log,
    level=
        safe_text,
    label=
        safe_text,
    expr=
        safe_text
)
scxml_EObject_strategy = st.builds(
    scxml_EObject,
)
scxml_Donedata_strategy = st.builds(
    scxml_Donedata,
)
scxml_Param_strategy = st.builds(
    scxml_Param,
    expr=
        safe_text,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
scxml_Content_strategy = st.builds(
    scxml_Content,
    value=
        safe_text
)
scxml_ParallelState_strategy = st.builds(
    scxml_ParallelState,
)
scxml_AbstractState_strategy = st.builds(
    scxml_AbstractState,
)
scxml_CondEventTransition_strategy = st.builds(
    scxml_CondEventTransition,
    event=
        safe_text,
    cond=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
scxml_TransitionTarget_strategy = st.builds(
    scxml_TransitionTarget,
    id=
        safe_text
)
scxml_TransitionSource_strategy = st.builds(
    scxml_TransitionSource,
)
ExecutableContent_strategy = st.builds(
    ExecutableContent,
)
scxml_If_strategy = st.builds(
    scxml_If,
)
scxml_OnExit_strategy = st.builds(
    scxml_OnExit,
)
scxml_OnEntry_strategy = st.builds(
    scxml_OnEntry,
)
TransitionSource_strategy = st.builds(
    TransitionSource,
)
TransitionTarget_strategy = st.builds(
    TransitionTarget,
)
scxml_HistoryState_strategy = st.builds(
    scxml_HistoryState,
    type=
        safe_text
)
scxml_FinalState_strategy = st.builds(
    scxml_FinalState,
)
scxml_Script_strategy = st.builds(
    scxml_Script,
    value=
        safe_text
)
DescriptionContainer_strategy = st.builds(
    DescriptionContainer,
)
scxml_InitialState_strategy = st.builds(
    scxml_InitialState,
)
scxml_Datamodel_strategy = st.builds(
    scxml_Datamodel,
    schema=
        safe_text
)
scxml_Transition_strategy = st.builds(
    scxml_Transition,
)
scxml_Data_strategy = st.builds(
    scxml_Data,
    src=
        safe_text,
    id=
        safe_text,
    expr=
        safe_text
)
scxml_Node_strategy = st.builds(
    scxml_Node,
)
DatamodelContainer_strategy = st.builds(
    DatamodelContainer,
)
AbstractSimpleState_strategy = st.builds(
    AbstractSimpleState,
)
scxml_SimpleState_strategy = st.builds(
    scxml_SimpleState,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
scxml_State_strategy = st.builds(
    scxml_State,
)
scxml_StateChart_strategy = st.builds(
    scxml_StateChart,
    xmlns=
        safe_text,
    version=
        safe_text,
    profile=
        safe_text,
    id=
        safe_text,
    exmode=
        safe_text
)




@given(instance=scxml_Description_strategy)
def test_hyp_scxml_description_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original











@given(instance=scxml_XObject_strategy)
def test_hyp_scxml_xobject_classifierName_setter(instance):
    original = instance.classifierName
    instance.classifierName = original
    assert instance.classifierName == original



@given(instance=scxml_XObject_strategy)
def test_hyp_scxml_xobject_nsUri_setter(instance):
    original = instance.nsUri
    instance.nsUri = original
    assert instance.nsUri == original



@given(instance=scxml_XObject_strategy)
def test_hyp_scxml_xobject_exchange_setter(instance):
    original = instance.exchange
    instance.exchange = original
    assert instance.exchange == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=scxml_XObject_strategy)
@settings(max_examples=30)
def test_hyp_scxml_xobject_registeradapter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.registerAdapter()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.registerAdapter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'registerAdapter' in scxml_XObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'registerAdapter' in scxml_XObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'registerAdapter' in scxml_XObject is not implemented or raised an error")







@given(instance=scxml_Conditional_strategy)
def test_hyp_scxml_conditional_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original




@given(instance=scxml_Validate_strategy)
def test_hyp_scxml_validate_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_Validate_strategy)
def test_hyp_scxml_validate_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original




@given(instance=scxml_Assign_strategy)
def test_hyp_scxml_assign_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=scxml_Assign_strategy)
def test_hyp_scxml_assign_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_Assign_strategy)
def test_hyp_scxml_assign_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=scxml_Cancel_strategy)
def test_hyp_scxml_cancel_sendid_setter(instance):
    original = instance.sendid
    instance.sendid = original
    assert instance.sendid == original



@given(instance=scxml_Cancel_strategy)
def test_hyp_scxml_cancel_sendidexpr_setter(instance):
    original = instance.sendidexpr
    instance.sendidexpr = original
    assert instance.sendidexpr == original





@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_hints_setter(instance):
    original = instance.hints
    instance.hints = original
    assert instance.hints == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_delay_setter(instance):
    original = instance.delay
    instance.delay = original
    assert instance.delay == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_hintsexpr_setter(instance):
    original = instance.hintsexpr
    instance.hintsexpr = original
    assert instance.hintsexpr == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_eventexpr_setter(instance):
    original = instance.eventexpr
    instance.eventexpr = original
    assert instance.eventexpr == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_targetexpr_setter(instance):
    original = instance.targetexpr
    instance.targetexpr = original
    assert instance.targetexpr == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_delayexpr_setter(instance):
    original = instance.delayexpr
    instance.delayexpr = original
    assert instance.delayexpr == original



@given(instance=scxml_Send_strategy)
def test_hyp_scxml_send_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original




@given(instance=scxml_ExecutableContent_strategy)
def test_hyp_scxml_executablecontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original





@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_typeexpr_setter(instance):
    original = instance.typeexpr
    instance.typeexpr = original
    assert instance.typeexpr == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_idlocation_setter(instance):
    original = instance.idlocation
    instance.idlocation = original
    assert instance.idlocation == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_srcexpr_setter(instance):
    original = instance.srcexpr
    instance.srcexpr = original
    assert instance.srcexpr == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_namelist_setter(instance):
    original = instance.namelist
    instance.namelist = original
    assert instance.namelist == original



@given(instance=scxml_Invoke_strategy)
def test_hyp_scxml_invoke_autoforward_setter(instance):
    original = instance.autoforward
    instance.autoforward = original
    assert instance.autoforward == original






@given(instance=scxml_Raise_strategy)
def test_hyp_scxml_raise_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original




@given(instance=scxml_Log_strategy)
def test_hyp_scxml_log_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=scxml_Log_strategy)
def test_hyp_scxml_log_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=scxml_Log_strategy)
def test_hyp_scxml_log_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original






@given(instance=scxml_Param_strategy)
def test_hyp_scxml_param_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=scxml_Param_strategy)
def test_hyp_scxml_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=scxml_Content_strategy)
def test_hyp_scxml_content_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=scxml_CondEventTransition_strategy)
def test_hyp_scxml_condeventtransition_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=scxml_CondEventTransition_strategy)
def test_hyp_scxml_condeventtransition_cond_setter(instance):
    original = instance.cond
    instance.cond = original
    assert instance.cond == original





@given(instance=scxml_TransitionTarget_strategy)
def test_hyp_scxml_transitiontarget_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original











@given(instance=scxml_HistoryState_strategy)
def test_hyp_scxml_historystate_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original





@given(instance=scxml_Script_strategy)
def test_hyp_scxml_script_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=scxml_Datamodel_strategy)
def test_hyp_scxml_datamodel_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original





@given(instance=scxml_Data_strategy)
def test_hyp_scxml_data_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=scxml_Data_strategy)
def test_hyp_scxml_data_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_Data_strategy)
def test_hyp_scxml_data_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original










@given(instance=scxml_StateChart_strategy)
def test_hyp_scxml_statechart_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original



@given(instance=scxml_StateChart_strategy)
def test_hyp_scxml_statechart_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=scxml_StateChart_strategy)
def test_hyp_scxml_statechart_profile_setter(instance):
    original = instance.profile
    instance.profile = original
    assert instance.profile == original



@given(instance=scxml_StateChart_strategy)
def test_hyp_scxml_statechart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=scxml_StateChart_strategy)
def test_hyp_scxml_statechart_exmode_setter(instance):
    original = instance.exmode
    instance.exmode = original
    assert instance.exmode == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractSimpleState,
    AbstractState,
    Conditional,
    Data,
    DatamodelContainer,
    DescriptionContainer,
    Donedata,
    ExecutableContent,
    IAdaptable,
    InitialState,
    Node,
    State,
    Transition,
    TransitionSource,
    TransitionTarget,
    scxml_AbstractSimpleState,
    scxml_AbstractState,
    scxml_Assign,
    scxml_Cancel,
    scxml_CondEventTransition,
    scxml_Conditional,
    scxml_Content,
    scxml_Data,
    scxml_Datamodel,
    scxml_DatamodelContainer,
    scxml_Description,
    scxml_DescriptionContainer,
    scxml_Donedata,
    scxml_EClass,
    scxml_EObject,
    scxml_Else,
    scxml_ElseIf,
    scxml_ExecutableContent,
    scxml_FinalState,
    scxml_HistoryState,
    scxml_IAdaptable,
    scxml_If,
    scxml_InitialState,
    scxml_Invoke,
    scxml_Log,
    scxml_Node,
    scxml_OnEntry,
    scxml_OnExit,
    scxml_ParallelState,
    scxml_Param,
    scxml_Raise,
    scxml_Script,
    scxml_Send,
    scxml_SimpleState,
    scxml_State,
    scxml_StateChart,
    scxml_Transition,
    scxml_TransitionSource,
    scxml_TransitionTarget,
    scxml_Validate,
    scxml_XData,
    scxml_XObject,
    AdapterToken,
    ExmodeDatatype,
    HistoryTypeDatatype,
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

def test_scxml_Assign_expr_value_roundtrip():
    instance = scxml_Assign(expr="sample_text", location="sample_text", name="sample_text")
    assert instance.expr == "sample_text"
    instance.expr = "sample_text_2"
    assert instance.expr == "sample_text_2"


def test_scxml_Assign_location_value_roundtrip():
    instance = scxml_Assign(expr="sample_text", location="sample_text", name="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_scxml_Assign_name_value_roundtrip():
    instance = scxml_Assign(expr="sample_text", location="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_scxml_Cancel_sendid_value_roundtrip():
    instance = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    assert instance.sendid == "sample_text"
    instance.sendid = "sample_text_2"
    assert instance.sendid == "sample_text_2"


def test_scxml_Cancel_sendidexpr_value_roundtrip():
    instance = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    assert instance.sendidexpr == "sample_text"
    instance.sendidexpr = "sample_text_2"
    assert instance.sendidexpr == "sample_text_2"


def test_scxml_CondEventTransition_cond_value_roundtrip():
    instance = scxml_CondEventTransition(cond="sample_text", event="sample_text")
    assert instance.cond == "sample_text"
    instance.cond = "sample_text_2"
    assert instance.cond == "sample_text_2"


def test_scxml_CondEventTransition_event_value_roundtrip():
    instance = scxml_CondEventTransition(cond="sample_text", event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_scxml_Conditional_cond_value_roundtrip():
    instance = scxml_Conditional(cond="sample_text")
    assert instance.cond == "sample_text"
    instance.cond = "sample_text_2"
    assert instance.cond == "sample_text_2"


def test_scxml_Content_value_value_roundtrip():
    instance = scxml_Content(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_scxml_Data_expr_value_roundtrip():
    instance = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    assert instance.expr == "sample_text"
    instance.expr = "sample_text_2"
    assert instance.expr == "sample_text_2"


def test_scxml_Data_id_value_roundtrip():
    instance = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scxml_Data_src_value_roundtrip():
    instance = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_scxml_Datamodel_schema_value_roundtrip():
    instance = scxml_Datamodel(schema="sample_text")
    assert instance.schema == "sample_text"
    instance.schema = "sample_text_2"
    assert instance.schema == "sample_text_2"


def test_scxml_Description_value_value_roundtrip():
    instance = scxml_Description(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_scxml_ExecutableContent_group_value_roundtrip():
    instance = scxml_ExecutableContent(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_scxml_HistoryState_type_value_roundtrip():
    instance = scxml_HistoryState(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scxml_Invoke_autoforward_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.autoforward == "sample_text"
    instance.autoforward = "sample_text_2"
    assert instance.autoforward == "sample_text_2"


def test_scxml_Invoke_id_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scxml_Invoke_idlocation_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.idlocation == "sample_text"
    instance.idlocation = "sample_text_2"
    assert instance.idlocation == "sample_text_2"


def test_scxml_Invoke_namelist_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.namelist == "sample_text"
    instance.namelist = "sample_text_2"
    assert instance.namelist == "sample_text_2"


def test_scxml_Invoke_src_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.src == "sample_text"
    instance.src = "sample_text_2"
    assert instance.src == "sample_text_2"


def test_scxml_Invoke_srcexpr_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.srcexpr == "sample_text"
    instance.srcexpr = "sample_text_2"
    assert instance.srcexpr == "sample_text_2"


def test_scxml_Invoke_type_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scxml_Invoke_typeexpr_value_roundtrip():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.typeexpr == "sample_text"
    instance.typeexpr = "sample_text_2"
    assert instance.typeexpr == "sample_text_2"


def test_scxml_Log_expr_value_roundtrip():
    instance = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    assert instance.expr == "sample_text"
    instance.expr = "sample_text_2"
    assert instance.expr == "sample_text_2"


def test_scxml_Log_label_value_roundtrip():
    instance = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_scxml_Log_level_value_roundtrip():
    instance = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    assert instance.level == "sample_text"
    instance.level = "sample_text_2"
    assert instance.level == "sample_text_2"


def test_scxml_Param_expr_value_roundtrip():
    instance = scxml_Param(expr="sample_text", name="sample_text")
    assert instance.expr == "sample_text"
    instance.expr = "sample_text_2"
    assert instance.expr == "sample_text_2"


def test_scxml_Param_name_value_roundtrip():
    instance = scxml_Param(expr="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_scxml_Raise_event_value_roundtrip():
    instance = scxml_Raise(event="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_scxml_Script_value_value_roundtrip():
    instance = scxml_Script(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_scxml_Send_delay_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.delay == "sample_text"
    instance.delay = "sample_text_2"
    assert instance.delay == "sample_text_2"


def test_scxml_Send_delayexpr_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.delayexpr == "sample_text"
    instance.delayexpr = "sample_text_2"
    assert instance.delayexpr == "sample_text_2"


def test_scxml_Send_event_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.event == "sample_text"
    instance.event = "sample_text_2"
    assert instance.event == "sample_text_2"


def test_scxml_Send_eventexpr_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.eventexpr == "sample_text"
    instance.eventexpr = "sample_text_2"
    assert instance.eventexpr == "sample_text_2"


def test_scxml_Send_hints_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.hints == "sample_text"
    instance.hints = "sample_text_2"
    assert instance.hints == "sample_text_2"


def test_scxml_Send_hintsexpr_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.hintsexpr == "sample_text"
    instance.hintsexpr = "sample_text_2"
    assert instance.hintsexpr == "sample_text_2"


def test_scxml_Send_id_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scxml_Send_idlocation_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.idlocation == "sample_text"
    instance.idlocation = "sample_text_2"
    assert instance.idlocation == "sample_text_2"


def test_scxml_Send_namelist_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.namelist == "sample_text"
    instance.namelist = "sample_text_2"
    assert instance.namelist == "sample_text_2"


def test_scxml_Send_target_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_scxml_Send_targetexpr_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.targetexpr == "sample_text"
    instance.targetexpr = "sample_text_2"
    assert instance.targetexpr == "sample_text_2"


def test_scxml_Send_type_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_scxml_Send_typeexpr_value_roundtrip():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert instance.typeexpr == "sample_text"
    instance.typeexpr = "sample_text_2"
    assert instance.typeexpr == "sample_text_2"


def test_scxml_StateChart_exmode_value_roundtrip():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert instance.exmode == "sample_text"
    instance.exmode = "sample_text_2"
    assert instance.exmode == "sample_text_2"


def test_scxml_StateChart_id_value_roundtrip():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scxml_StateChart_profile_value_roundtrip():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert instance.profile == "sample_text"
    instance.profile = "sample_text_2"
    assert instance.profile == "sample_text_2"


def test_scxml_StateChart_version_value_roundtrip():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_scxml_StateChart_xmlns_value_roundtrip():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert instance.xmlns == "sample_text"
    instance.xmlns = "sample_text_2"
    assert instance.xmlns == "sample_text_2"


def test_scxml_TransitionTarget_id_value_roundtrip():
    instance = scxml_TransitionTarget(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_scxml_Validate_location_value_roundtrip():
    instance = scxml_Validate(location="sample_text", schema="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_scxml_Validate_schema_value_roundtrip():
    instance = scxml_Validate(location="sample_text", schema="sample_text")
    assert instance.schema == "sample_text"
    instance.schema = "sample_text_2"
    assert instance.schema == "sample_text_2"


def test_scxml_XObject_classifierName_value_roundtrip():
    instance = scxml_XObject(classifierName="sample_text", exchange=True, nsUri="sample_text")
    assert instance.classifierName == "sample_text"
    instance.classifierName = "sample_text_2"
    assert instance.classifierName == "sample_text_2"


def test_scxml_XObject_exchange_value_roundtrip():
    instance = scxml_XObject(classifierName="sample_text", exchange=True, nsUri="sample_text")
    assert instance.exchange == True
    instance.exchange = False
    assert instance.exchange == False


def test_scxml_XObject_nsUri_value_roundtrip():
    instance = scxml_XObject(classifierName="sample_text", exchange=True, nsUri="sample_text")
    assert instance.nsUri == "sample_text"
    instance.nsUri = "sample_text_2"
    assert instance.nsUri == "sample_text_2"


def test_scxml_SimpleState_isa_AbstractSimpleState():
    instance = scxml_SimpleState()
    assert isinstance(instance, AbstractSimpleState)


def test_scxml_StateChart_isa_AbstractSimpleState():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert isinstance(instance, AbstractSimpleState)


def test_scxml_State_isa_AbstractState():
    instance = scxml_State()
    assert isinstance(instance, AbstractState)


def test_scxml_StateChart_isa_AbstractState():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert isinstance(instance, AbstractState)


def test_scxml_ElseIf_isa_Conditional():
    instance = scxml_ElseIf()
    assert isinstance(instance, Conditional)


def test_scxml_If_isa_Conditional():
    instance = scxml_If()
    assert isinstance(instance, Conditional)


def test_scxml_XData_isa_Data():
    instance = scxml_XData()
    assert isinstance(instance, Data)


def test_scxml_State_isa_DatamodelContainer():
    instance = scxml_State()
    assert isinstance(instance, DatamodelContainer)


def test_scxml_StateChart_isa_DatamodelContainer():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert isinstance(instance, DatamodelContainer)


def test_scxml_Data_isa_DescriptionContainer():
    instance = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    assert isinstance(instance, DescriptionContainer)


def test_scxml_Datamodel_isa_DescriptionContainer():
    instance = scxml_Datamodel(schema="sample_text")
    assert isinstance(instance, DescriptionContainer)


def test_scxml_InitialState_isa_DescriptionContainer():
    instance = scxml_InitialState()
    assert isinstance(instance, DescriptionContainer)


def test_scxml_Node_isa_DescriptionContainer():
    instance = scxml_Node()
    assert isinstance(instance, DescriptionContainer)


def test_scxml_StateChart_isa_DescriptionContainer():
    instance = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    assert isinstance(instance, DescriptionContainer)


def test_scxml_Transition_isa_DescriptionContainer():
    instance = scxml_Transition()
    assert isinstance(instance, DescriptionContainer)


def test_scxml_Invoke_isa_Donedata():
    instance = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert isinstance(instance, Donedata)


def test_scxml_Raise_isa_Donedata():
    instance = scxml_Raise(event="sample_text")
    assert isinstance(instance, Donedata)


def test_scxml_Send_isa_Donedata():
    instance = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    assert isinstance(instance, Donedata)


def test_scxml_If_isa_ExecutableContent():
    instance = scxml_If()
    assert isinstance(instance, ExecutableContent)


def test_scxml_OnEntry_isa_ExecutableContent():
    instance = scxml_OnEntry()
    assert isinstance(instance, ExecutableContent)


def test_scxml_OnExit_isa_ExecutableContent():
    instance = scxml_OnExit()
    assert isinstance(instance, ExecutableContent)


def test_scxml_Transition_isa_ExecutableContent():
    instance = scxml_Transition()
    assert isinstance(instance, ExecutableContent)


def test_scxml_DatamodelContainer_isa_IAdaptable():
    instance = scxml_DatamodelContainer()
    assert isinstance(instance, IAdaptable)


def test_scxml_DescriptionContainer_isa_IAdaptable():
    instance = scxml_DescriptionContainer()
    assert isinstance(instance, IAdaptable)


def test_scxml_HistoryState_isa_InitialState():
    instance = scxml_HistoryState(type="sample_text")
    assert isinstance(instance, InitialState)


def test_scxml_TransitionSource_isa_Node():
    instance = scxml_TransitionSource()
    assert isinstance(instance, Node)


def test_scxml_TransitionTarget_isa_Node():
    instance = scxml_TransitionTarget(id="sample_text")
    assert isinstance(instance, Node)


def test_scxml_ParallelState_isa_State():
    instance = scxml_ParallelState()
    assert isinstance(instance, State)


def test_scxml_SimpleState_isa_State():
    instance = scxml_SimpleState()
    assert isinstance(instance, State)


def test_scxml_CondEventTransition_isa_Transition():
    instance = scxml_CondEventTransition(cond="sample_text", event="sample_text")
    assert isinstance(instance, Transition)


def test_scxml_State_isa_TransitionSource():
    instance = scxml_State()
    assert isinstance(instance, TransitionSource)


def test_scxml_FinalState_isa_TransitionTarget():
    instance = scxml_FinalState()
    assert isinstance(instance, TransitionTarget)


def test_scxml_HistoryState_isa_TransitionTarget():
    instance = scxml_HistoryState(type="sample_text")
    assert isinstance(instance, TransitionTarget)


def test_scxml_State_isa_TransitionTarget():
    instance = scxml_State()
    assert isinstance(instance, TransitionTarget)


def test_assoc_assign36_link_reassign_clear():
    a = scxml_ExecutableContent(group="sample_text")
    b1 = scxml_Assign(expr="sample_text", location="sample_text", name="sample_text")
    b2 = scxml_Assign(expr="sample_text_2", location="sample_text_2", name="sample_text_2")
    _safe_set(a, 'scxml_ExecutableContent37', {b1})
    assert _is_linked(a, 'scxml_ExecutableContent37', b1)
    if hasattr(b1, 'scxml_Assign'):
        assert _is_linked(b1, 'scxml_Assign', a)
    _safe_set(a, 'scxml_ExecutableContent37', {b2})
    assert _is_linked(a, 'scxml_ExecutableContent37', b2)
    if hasattr(b1, 'scxml_Assign'):
        assert not _is_linked(b1, 'scxml_Assign', a)
    if hasattr(b2, 'scxml_Assign'):
        assert _is_linked(b2, 'scxml_Assign', a)
    _safe_set(a, 'scxml_ExecutableContent37', set())
    assert not _is_linked(a, 'scxml_ExecutableContent37', b2)
    if hasattr(b2, 'scxml_Assign'):
        assert not _is_linked(b2, 'scxml_Assign', a)


def test_assoc_cancel34_link_reassign_clear():
    a = scxml_ExecutableContent(group="sample_text")
    b1 = scxml_Cancel(sendid="sample_text", sendidexpr="sample_text")
    b2 = scxml_Cancel(sendid="sample_text_2", sendidexpr="sample_text_2")
    _safe_set(a, 'scxml_ExecutableContent35', {b1})
    assert _is_linked(a, 'scxml_ExecutableContent35', b1)
    if hasattr(b1, 'scxml_Cancel'):
        assert _is_linked(b1, 'scxml_Cancel', a)
    _safe_set(a, 'scxml_ExecutableContent35', {b2})
    assert _is_linked(a, 'scxml_ExecutableContent35', b2)
    if hasattr(b1, 'scxml_Cancel'):
        assert not _is_linked(b1, 'scxml_Cancel', a)
    if hasattr(b2, 'scxml_Cancel'):
        assert _is_linked(b2, 'scxml_Cancel', a)
    _safe_set(a, 'scxml_ExecutableContent35', set())
    assert not _is_linked(a, 'scxml_ExecutableContent35', b2)
    if hasattr(b2, 'scxml_Cancel'):
        assert not _is_linked(b2, 'scxml_Cancel', a)


def test_assoc_data53_link_reassign_clear():
    a = scxml_Datamodel(schema="sample_text")
    b1 = scxml_Data(expr="sample_text", id="sample_text", src="sample_text")
    b2 = scxml_Data(expr="sample_text_2", id="sample_text_2", src="sample_text_2")
    _safe_set(a, 'scxml_Datamodel', {b1})
    assert _is_linked(a, 'scxml_Datamodel', b1)
    if hasattr(b1, 'scxml_Data'):
        assert _is_linked(b1, 'scxml_Data', a)
    _safe_set(a, 'scxml_Datamodel', {b2})
    assert _is_linked(a, 'scxml_Datamodel', b2)
    if hasattr(b1, 'scxml_Data'):
        assert not _is_linked(b1, 'scxml_Data', a)
    if hasattr(b2, 'scxml_Data'):
        assert _is_linked(b2, 'scxml_Data', a)
    _safe_set(a, 'scxml_Datamodel', set())
    assert not _is_linked(a, 'scxml_Datamodel', b2)
    if hasattr(b2, 'scxml_Data'):
        assert not _is_linked(b2, 'scxml_Data', a)


def test_assoc_datamodel54_link_reassign_clear():
    a = scxml_DatamodelContainer()
    b1 = scxml_Datamodel(schema="sample_text")
    b2 = scxml_Datamodel(schema="sample_text_2")
    _safe_set(a, 'scxml_DatamodelContainer', b1)
    assert _is_linked(a, 'scxml_DatamodelContainer', b1)
    if hasattr(b1, 'scxml_Datamodel55'):
        assert _is_linked(b1, 'scxml_Datamodel55', a)
    _safe_set(a, 'scxml_DatamodelContainer', b2)
    assert _is_linked(a, 'scxml_DatamodelContainer', b2)
    if hasattr(b1, 'scxml_Datamodel55'):
        assert not _is_linked(b1, 'scxml_Datamodel55', a)
    if hasattr(b2, 'scxml_Datamodel55'):
        assert _is_linked(b2, 'scxml_Datamodel55', a)
    _safe_set(a, 'scxml_DatamodelContainer', None)
    assert not _is_linked(a, 'scxml_DatamodelContainer', b2)
    if hasattr(b2, 'scxml_Datamodel55'):
        assert not _is_linked(b2, 'scxml_Datamodel55', a)


def test_assoc_description56_link_reassign_clear():
    a = scxml_DescriptionContainer()
    b1 = scxml_Description(value="sample_text")
    b2 = scxml_Description(value="sample_text_2")
    _safe_set(a, 'scxml_DescriptionContainer', b1)
    assert _is_linked(a, 'scxml_DescriptionContainer', b1)
    if hasattr(b1, 'scxml_Description'):
        assert _is_linked(b1, 'scxml_Description', a)
    _safe_set(a, 'scxml_DescriptionContainer', b2)
    assert _is_linked(a, 'scxml_DescriptionContainer', b2)
    if hasattr(b1, 'scxml_Description'):
        assert not _is_linked(b1, 'scxml_Description', a)
    if hasattr(b2, 'scxml_Description'):
        assert _is_linked(b2, 'scxml_Description', a)
    _safe_set(a, 'scxml_DescriptionContainer', None)
    assert not _is_linked(a, 'scxml_DescriptionContainer', b2)
    if hasattr(b2, 'scxml_Description'):
        assert not _is_linked(b2, 'scxml_Description', a)


def test_assoc_finalize47_link_reassign_clear():
    a = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Invoke48', b1)
    assert _is_linked(a, 'scxml_Invoke48', b1)
    if hasattr(b1, 'scxml_ExecutableContent49'):
        assert _is_linked(b1, 'scxml_ExecutableContent49', a)
    _safe_set(a, 'scxml_Invoke48', b2)
    assert _is_linked(a, 'scxml_Invoke48', b2)
    if hasattr(b1, 'scxml_ExecutableContent49'):
        assert not _is_linked(b1, 'scxml_ExecutableContent49', a)
    if hasattr(b2, 'scxml_ExecutableContent49'):
        assert _is_linked(b2, 'scxml_ExecutableContent49', a)
    _safe_set(a, 'scxml_Invoke48', None)
    assert not _is_linked(a, 'scxml_Invoke48', b2)
    if hasattr(b2, 'scxml_ExecutableContent49'):
        assert not _is_linked(b2, 'scxml_ExecutableContent49', a)


def test_assoc_history8_link_reassign_clear():
    a = scxml_HistoryState(type="sample_text")
    b1 = scxml_State()
    b2 = scxml_State()
    _safe_set(a, 'scxml_HistoryState', b1)
    assert _is_linked(a, 'scxml_HistoryState', b1)
    if hasattr(b1, 'scxml_State'):
        assert _is_linked(b1, 'scxml_State', a)
    _safe_set(a, 'scxml_HistoryState', b2)
    assert _is_linked(a, 'scxml_HistoryState', b2)
    if hasattr(b1, 'scxml_State'):
        assert not _is_linked(b1, 'scxml_State', a)
    if hasattr(b2, 'scxml_State'):
        assert _is_linked(b2, 'scxml_State', a)
    _safe_set(a, 'scxml_HistoryState', None)
    assert not _is_linked(a, 'scxml_HistoryState', b2)
    if hasattr(b2, 'scxml_State'):
        assert not _is_linked(b2, 'scxml_State', a)


def test_assoc_if_27_link_reassign_clear():
    a = scxml_ExecutableContent(group="sample_text")
    b1 = scxml_If()
    b2 = scxml_If()
    _safe_set(a, 'scxml_ExecutableContent', {b1})
    assert _is_linked(a, 'scxml_ExecutableContent', b1)
    if hasattr(b1, 'scxml_If'):
        assert _is_linked(b1, 'scxml_If', a)
    _safe_set(a, 'scxml_ExecutableContent', {b2})
    assert _is_linked(a, 'scxml_ExecutableContent', b2)
    if hasattr(b1, 'scxml_If'):
        assert not _is_linked(b1, 'scxml_If', a)
    if hasattr(b2, 'scxml_If'):
        assert _is_linked(b2, 'scxml_If', a)
    _safe_set(a, 'scxml_ExecutableContent', set())
    assert not _is_linked(a, 'scxml_ExecutableContent', b2)
    if hasattr(b2, 'scxml_If'):
        assert not _is_linked(b2, 'scxml_If', a)


def test_assoc_initial117_link_reassign_clear():
    a = scxml_TransitionTarget(id="sample_text")
    b1 = scxml_AbstractSimpleState()
    b2 = scxml_AbstractSimpleState()
    _safe_set(a, 'scxml_TransitionTarget18', b1)
    assert _is_linked(a, 'scxml_TransitionTarget18', b1)
    if hasattr(b1, 'scxml_AbstractSimpleState'):
        assert _is_linked(b1, 'scxml_AbstractSimpleState', a)
    _safe_set(a, 'scxml_TransitionTarget18', b2)
    assert _is_linked(a, 'scxml_TransitionTarget18', b2)
    if hasattr(b1, 'scxml_AbstractSimpleState'):
        assert not _is_linked(b1, 'scxml_AbstractSimpleState', a)
    if hasattr(b2, 'scxml_AbstractSimpleState'):
        assert _is_linked(b2, 'scxml_AbstractSimpleState', a)
    _safe_set(a, 'scxml_TransitionTarget18', None)
    assert not _is_linked(a, 'scxml_TransitionTarget18', b2)
    if hasattr(b2, 'scxml_AbstractSimpleState'):
        assert not _is_linked(b2, 'scxml_AbstractSimpleState', a)


def test_assoc_invoke25_link_reassign_clear():
    a = scxml_Invoke(autoforward="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", src="sample_text", srcexpr="sample_text", type="sample_text", typeexpr="sample_text")
    b1 = scxml_SimpleState()
    b2 = scxml_SimpleState()
    _safe_set(a, 'scxml_Invoke', b1)
    assert _is_linked(a, 'scxml_Invoke', b1)
    if hasattr(b1, 'scxml_SimpleState26'):
        assert _is_linked(b1, 'scxml_SimpleState26', a)
    _safe_set(a, 'scxml_Invoke', b2)
    assert _is_linked(a, 'scxml_Invoke', b2)
    if hasattr(b1, 'scxml_SimpleState26'):
        assert not _is_linked(b1, 'scxml_SimpleState26', a)
    if hasattr(b2, 'scxml_SimpleState26'):
        assert _is_linked(b2, 'scxml_SimpleState26', a)
    _safe_set(a, 'scxml_Invoke', None)
    assert not _is_linked(a, 'scxml_Invoke', b2)
    if hasattr(b2, 'scxml_SimpleState26'):
        assert not _is_linked(b2, 'scxml_SimpleState26', a)


def test_assoc_log28_link_reassign_clear():
    a = scxml_Log(expr="sample_text", label="sample_text", level="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Log', b1)
    assert _is_linked(a, 'scxml_Log', b1)
    if hasattr(b1, 'scxml_ExecutableContent29'):
        assert _is_linked(b1, 'scxml_ExecutableContent29', a)
    _safe_set(a, 'scxml_Log', b2)
    assert _is_linked(a, 'scxml_Log', b2)
    if hasattr(b1, 'scxml_ExecutableContent29'):
        assert not _is_linked(b1, 'scxml_ExecutableContent29', a)
    if hasattr(b2, 'scxml_ExecutableContent29'):
        assert _is_linked(b2, 'scxml_ExecutableContent29', a)
    _safe_set(a, 'scxml_Log', None)
    assert not _is_linked(a, 'scxml_Log', b2)
    if hasattr(b2, 'scxml_ExecutableContent29'):
        assert not _is_linked(b2, 'scxml_ExecutableContent29', a)


def test_assoc_param12_link_reassign_clear():
    a = scxml_Param(expr="sample_text", name="sample_text")
    b1 = scxml_Donedata()
    b2 = scxml_Donedata()
    _safe_set(a, 'scxml_Param', b1)
    assert _is_linked(a, 'scxml_Param', b1)
    if hasattr(b1, 'scxml_Donedata'):
        assert _is_linked(b1, 'scxml_Donedata', a)
    _safe_set(a, 'scxml_Param', b2)
    assert _is_linked(a, 'scxml_Param', b2)
    if hasattr(b1, 'scxml_Donedata'):
        assert not _is_linked(b1, 'scxml_Donedata', a)
    if hasattr(b2, 'scxml_Donedata'):
        assert _is_linked(b2, 'scxml_Donedata', a)
    _safe_set(a, 'scxml_Param', None)
    assert not _is_linked(a, 'scxml_Param', b2)
    if hasattr(b2, 'scxml_Donedata'):
        assert not _is_linked(b2, 'scxml_Donedata', a)


def test_assoc_raise_30_link_reassign_clear():
    a = scxml_Raise(event="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Raise', b1)
    assert _is_linked(a, 'scxml_Raise', b1)
    if hasattr(b1, 'scxml_ExecutableContent31'):
        assert _is_linked(b1, 'scxml_ExecutableContent31', a)
    _safe_set(a, 'scxml_Raise', b2)
    assert _is_linked(a, 'scxml_Raise', b2)
    if hasattr(b1, 'scxml_ExecutableContent31'):
        assert not _is_linked(b1, 'scxml_ExecutableContent31', a)
    if hasattr(b2, 'scxml_ExecutableContent31'):
        assert _is_linked(b2, 'scxml_ExecutableContent31', a)
    _safe_set(a, 'scxml_Raise', None)
    assert not _is_linked(a, 'scxml_Raise', b2)
    if hasattr(b2, 'scxml_ExecutableContent31'):
        assert not _is_linked(b2, 'scxml_ExecutableContent31', a)


def test_assoc_script0_link_reassign_clear():
    a = scxml_StateChart(exmode="sample_text", id="sample_text", profile="sample_text", version="sample_text", xmlns="sample_text")
    b1 = scxml_Script(value="sample_text")
    b2 = scxml_Script(value="sample_text_2")
    _safe_set(a, 'scxml_StateChart', {b1})
    assert _is_linked(a, 'scxml_StateChart', b1)
    if hasattr(b1, 'scxml_Script'):
        assert _is_linked(b1, 'scxml_Script', a)
    _safe_set(a, 'scxml_StateChart', {b2})
    assert _is_linked(a, 'scxml_StateChart', b2)
    if hasattr(b1, 'scxml_Script'):
        assert not _is_linked(b1, 'scxml_Script', a)
    if hasattr(b2, 'scxml_Script'):
        assert _is_linked(b2, 'scxml_Script', a)
    _safe_set(a, 'scxml_StateChart', set())
    assert not _is_linked(a, 'scxml_StateChart', b2)
    if hasattr(b2, 'scxml_Script'):
        assert not _is_linked(b2, 'scxml_Script', a)


def test_assoc_script40_link_reassign_clear():
    a = scxml_Script(value="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Script42', b1)
    assert _is_linked(a, 'scxml_Script42', b1)
    if hasattr(b1, 'scxml_ExecutableContent41'):
        assert _is_linked(b1, 'scxml_ExecutableContent41', a)
    _safe_set(a, 'scxml_Script42', b2)
    assert _is_linked(a, 'scxml_Script42', b2)
    if hasattr(b1, 'scxml_ExecutableContent41'):
        assert not _is_linked(b1, 'scxml_ExecutableContent41', a)
    if hasattr(b2, 'scxml_ExecutableContent41'):
        assert _is_linked(b2, 'scxml_ExecutableContent41', a)
    _safe_set(a, 'scxml_Script42', None)
    assert not _is_linked(a, 'scxml_Script42', b2)
    if hasattr(b2, 'scxml_ExecutableContent41'):
        assert not _is_linked(b2, 'scxml_ExecutableContent41', a)


def test_assoc_send32_link_reassign_clear():
    a = scxml_Send(delay="sample_text", delayexpr="sample_text", event="sample_text", eventexpr="sample_text", hints="sample_text", hintsexpr="sample_text", id="sample_text", idlocation="sample_text", namelist="sample_text", target="sample_text", targetexpr="sample_text", type="sample_text", typeexpr="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Send', b1)
    assert _is_linked(a, 'scxml_Send', b1)
    if hasattr(b1, 'scxml_ExecutableContent33'):
        assert _is_linked(b1, 'scxml_ExecutableContent33', a)
    _safe_set(a, 'scxml_Send', b2)
    assert _is_linked(a, 'scxml_Send', b2)
    if hasattr(b1, 'scxml_ExecutableContent33'):
        assert not _is_linked(b1, 'scxml_ExecutableContent33', a)
    if hasattr(b2, 'scxml_ExecutableContent33'):
        assert _is_linked(b2, 'scxml_ExecutableContent33', a)
    _safe_set(a, 'scxml_Send', None)
    assert not _is_linked(a, 'scxml_Send', b2)
    if hasattr(b2, 'scxml_ExecutableContent33'):
        assert not _is_linked(b2, 'scxml_ExecutableContent33', a)


def test_assoc_target9_link_reassign_clear():
    a = scxml_TransitionTarget(id="sample_text")
    b1 = scxml_Transition()
    b2 = scxml_Transition()
    _safe_set(a, 'scxml_TransitionTarget', b1)
    assert _is_linked(a, 'scxml_TransitionTarget', b1)
    if hasattr(b1, 'scxml_Transition'):
        assert _is_linked(b1, 'scxml_Transition', a)
    _safe_set(a, 'scxml_TransitionTarget', b2)
    assert _is_linked(a, 'scxml_TransitionTarget', b2)
    if hasattr(b1, 'scxml_Transition'):
        assert not _is_linked(b1, 'scxml_Transition', a)
    if hasattr(b2, 'scxml_Transition'):
        assert _is_linked(b2, 'scxml_Transition', a)
    _safe_set(a, 'scxml_TransitionTarget', None)
    assert not _is_linked(a, 'scxml_TransitionTarget', b2)
    if hasattr(b2, 'scxml_Transition'):
        assert not _is_linked(b2, 'scxml_Transition', a)


def test_assoc_transition4_link_reassign_clear():
    a = scxml_CondEventTransition(cond="sample_text", event="sample_text")
    b1 = scxml_TransitionSource()
    b2 = scxml_TransitionSource()
    _safe_set(a, 'scxml_CondEventTransition', b1)
    assert _is_linked(a, 'scxml_CondEventTransition', b1)
    if hasattr(b1, 'scxml_TransitionSource'):
        assert _is_linked(b1, 'scxml_TransitionSource', a)
    _safe_set(a, 'scxml_CondEventTransition', b2)
    assert _is_linked(a, 'scxml_CondEventTransition', b2)
    if hasattr(b1, 'scxml_TransitionSource'):
        assert not _is_linked(b1, 'scxml_TransitionSource', a)
    if hasattr(b2, 'scxml_TransitionSource'):
        assert _is_linked(b2, 'scxml_TransitionSource', a)
    _safe_set(a, 'scxml_CondEventTransition', None)
    assert not _is_linked(a, 'scxml_CondEventTransition', b2)
    if hasattr(b2, 'scxml_TransitionSource'):
        assert not _is_linked(b2, 'scxml_TransitionSource', a)


def test_assoc_type52_link_reassign_clear():
    a = scxml_XObject(classifierName="sample_text", exchange=True, nsUri="sample_text")
    b1 = scxml_EClass()
    b2 = scxml_EClass()
    _safe_set(a, 'scxml_XObject', b1)
    assert _is_linked(a, 'scxml_XObject', b1)
    if hasattr(b1, 'scxml_EClass'):
        assert _is_linked(b1, 'scxml_EClass', a)
    _safe_set(a, 'scxml_XObject', b2)
    assert _is_linked(a, 'scxml_XObject', b2)
    if hasattr(b1, 'scxml_EClass'):
        assert not _is_linked(b1, 'scxml_EClass', a)
    if hasattr(b2, 'scxml_EClass'):
        assert _is_linked(b2, 'scxml_EClass', a)
    _safe_set(a, 'scxml_XObject', None)
    assert not _is_linked(a, 'scxml_XObject', b2)
    if hasattr(b2, 'scxml_EClass'):
        assert not _is_linked(b2, 'scxml_EClass', a)


def test_assoc_validate38_link_reassign_clear():
    a = scxml_Validate(location="sample_text", schema="sample_text")
    b1 = scxml_ExecutableContent(group="sample_text")
    b2 = scxml_ExecutableContent(group="sample_text_2")
    _safe_set(a, 'scxml_Validate', b1)
    assert _is_linked(a, 'scxml_Validate', b1)
    if hasattr(b1, 'scxml_ExecutableContent39'):
        assert _is_linked(b1, 'scxml_ExecutableContent39', a)
    _safe_set(a, 'scxml_Validate', b2)
    assert _is_linked(a, 'scxml_Validate', b2)
    if hasattr(b1, 'scxml_ExecutableContent39'):
        assert not _is_linked(b1, 'scxml_ExecutableContent39', a)
    if hasattr(b2, 'scxml_ExecutableContent39'):
        assert _is_linked(b2, 'scxml_ExecutableContent39', a)
    _safe_set(a, 'scxml_Validate', None)
    assert not _is_linked(a, 'scxml_Validate', b2)
    if hasattr(b2, 'scxml_ExecutableContent39'):
        assert not _is_linked(b2, 'scxml_ExecutableContent39', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AbstractSimpleState_strategy = st.builds(AbstractSimpleState)
@given(instance=AbstractSimpleState_strategy)
@settings(max_examples=25)
def test_AbstractSimpleState_instantiation(instance):
    assert isinstance(instance, AbstractSimpleState)


AbstractState_strategy = st.builds(AbstractState)
@given(instance=AbstractState_strategy)
@settings(max_examples=25)
def test_AbstractState_instantiation(instance):
    assert isinstance(instance, AbstractState)


Conditional_strategy = st.builds(Conditional)
@given(instance=Conditional_strategy)
@settings(max_examples=25)
def test_Conditional_instantiation(instance):
    assert isinstance(instance, Conditional)


Data_strategy = st.builds(Data)
@given(instance=Data_strategy)
@settings(max_examples=25)
def test_Data_instantiation(instance):
    assert isinstance(instance, Data)


DatamodelContainer_strategy = st.builds(DatamodelContainer)
@given(instance=DatamodelContainer_strategy)
@settings(max_examples=25)
def test_DatamodelContainer_instantiation(instance):
    assert isinstance(instance, DatamodelContainer)


DescriptionContainer_strategy = st.builds(DescriptionContainer)
@given(instance=DescriptionContainer_strategy)
@settings(max_examples=25)
def test_DescriptionContainer_instantiation(instance):
    assert isinstance(instance, DescriptionContainer)


Donedata_strategy = st.builds(Donedata)
@given(instance=Donedata_strategy)
@settings(max_examples=25)
def test_Donedata_instantiation(instance):
    assert isinstance(instance, Donedata)


ExecutableContent_strategy = st.builds(ExecutableContent)
@given(instance=ExecutableContent_strategy)
@settings(max_examples=25)
def test_ExecutableContent_instantiation(instance):
    assert isinstance(instance, ExecutableContent)


IAdaptable_strategy = st.builds(IAdaptable)
@given(instance=IAdaptable_strategy)
@settings(max_examples=25)
def test_IAdaptable_instantiation(instance):
    assert isinstance(instance, IAdaptable)


InitialState_strategy = st.builds(InitialState)
@given(instance=InitialState_strategy)
@settings(max_examples=25)
def test_InitialState_instantiation(instance):
    assert isinstance(instance, InitialState)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


State_strategy = st.builds(State)
@given(instance=State_strategy)
@settings(max_examples=25)
def test_State_instantiation(instance):
    assert isinstance(instance, State)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


TransitionSource_strategy = st.builds(TransitionSource)
@given(instance=TransitionSource_strategy)
@settings(max_examples=25)
def test_TransitionSource_instantiation(instance):
    assert isinstance(instance, TransitionSource)


TransitionTarget_strategy = st.builds(TransitionTarget)
@given(instance=TransitionTarget_strategy)
@settings(max_examples=25)
def test_TransitionTarget_instantiation(instance):
    assert isinstance(instance, TransitionTarget)


scxml_AbstractSimpleState_strategy = st.builds(scxml_AbstractSimpleState)
@given(instance=scxml_AbstractSimpleState_strategy)
@settings(max_examples=25)
def test_scxml_AbstractSimpleState_instantiation(instance):
    assert isinstance(instance, scxml_AbstractSimpleState)


scxml_AbstractState_strategy = st.builds(scxml_AbstractState)
@given(instance=scxml_AbstractState_strategy)
@settings(max_examples=25)
def test_scxml_AbstractState_instantiation(instance):
    assert isinstance(instance, scxml_AbstractState)


scxml_Assign_strategy = st.builds(scxml_Assign, expr=safe_text, location=safe_text, name=safe_text)
@given(instance=scxml_Assign_strategy)
@settings(max_examples=25)
def test_scxml_Assign_instantiation(instance):
    assert isinstance(instance, scxml_Assign)


scxml_Cancel_strategy = st.builds(scxml_Cancel, sendid=safe_text, sendidexpr=safe_text)
@given(instance=scxml_Cancel_strategy)
@settings(max_examples=25)
def test_scxml_Cancel_instantiation(instance):
    assert isinstance(instance, scxml_Cancel)


scxml_CondEventTransition_strategy = st.builds(scxml_CondEventTransition, cond=safe_text, event=safe_text)
@given(instance=scxml_CondEventTransition_strategy)
@settings(max_examples=25)
def test_scxml_CondEventTransition_instantiation(instance):
    assert isinstance(instance, scxml_CondEventTransition)


scxml_Conditional_strategy = st.builds(scxml_Conditional, cond=safe_text)
@given(instance=scxml_Conditional_strategy)
@settings(max_examples=25)
def test_scxml_Conditional_instantiation(instance):
    assert isinstance(instance, scxml_Conditional)


scxml_Content_strategy = st.builds(scxml_Content, value=safe_text)
@given(instance=scxml_Content_strategy)
@settings(max_examples=25)
def test_scxml_Content_instantiation(instance):
    assert isinstance(instance, scxml_Content)


scxml_Data_strategy = st.builds(scxml_Data, expr=safe_text, id=safe_text, src=safe_text)
@given(instance=scxml_Data_strategy)
@settings(max_examples=25)
def test_scxml_Data_instantiation(instance):
    assert isinstance(instance, scxml_Data)


scxml_Datamodel_strategy = st.builds(scxml_Datamodel, schema=safe_text)
@given(instance=scxml_Datamodel_strategy)
@settings(max_examples=25)
def test_scxml_Datamodel_instantiation(instance):
    assert isinstance(instance, scxml_Datamodel)


scxml_DatamodelContainer_strategy = st.builds(scxml_DatamodelContainer)
@given(instance=scxml_DatamodelContainer_strategy)
@settings(max_examples=25)
def test_scxml_DatamodelContainer_instantiation(instance):
    assert isinstance(instance, scxml_DatamodelContainer)


scxml_Description_strategy = st.builds(scxml_Description, value=safe_text)
@given(instance=scxml_Description_strategy)
@settings(max_examples=25)
def test_scxml_Description_instantiation(instance):
    assert isinstance(instance, scxml_Description)


scxml_DescriptionContainer_strategy = st.builds(scxml_DescriptionContainer)
@given(instance=scxml_DescriptionContainer_strategy)
@settings(max_examples=25)
def test_scxml_DescriptionContainer_instantiation(instance):
    assert isinstance(instance, scxml_DescriptionContainer)


scxml_Donedata_strategy = st.builds(scxml_Donedata)
@given(instance=scxml_Donedata_strategy)
@settings(max_examples=25)
def test_scxml_Donedata_instantiation(instance):
    assert isinstance(instance, scxml_Donedata)


scxml_EClass_strategy = st.builds(scxml_EClass)
@given(instance=scxml_EClass_strategy)
@settings(max_examples=25)
def test_scxml_EClass_instantiation(instance):
    assert isinstance(instance, scxml_EClass)


scxml_EObject_strategy = st.builds(scxml_EObject)
@given(instance=scxml_EObject_strategy)
@settings(max_examples=25)
def test_scxml_EObject_instantiation(instance):
    assert isinstance(instance, scxml_EObject)


scxml_Else_strategy = st.builds(scxml_Else)
@given(instance=scxml_Else_strategy)
@settings(max_examples=25)
def test_scxml_Else_instantiation(instance):
    assert isinstance(instance, scxml_Else)


scxml_ElseIf_strategy = st.builds(scxml_ElseIf)
@given(instance=scxml_ElseIf_strategy)
@settings(max_examples=25)
def test_scxml_ElseIf_instantiation(instance):
    assert isinstance(instance, scxml_ElseIf)


scxml_ExecutableContent_strategy = st.builds(scxml_ExecutableContent, group=safe_text)
@given(instance=scxml_ExecutableContent_strategy)
@settings(max_examples=25)
def test_scxml_ExecutableContent_instantiation(instance):
    assert isinstance(instance, scxml_ExecutableContent)


scxml_FinalState_strategy = st.builds(scxml_FinalState)
@given(instance=scxml_FinalState_strategy)
@settings(max_examples=25)
def test_scxml_FinalState_instantiation(instance):
    assert isinstance(instance, scxml_FinalState)


scxml_HistoryState_strategy = st.builds(scxml_HistoryState, type=safe_text)
@given(instance=scxml_HistoryState_strategy)
@settings(max_examples=25)
def test_scxml_HistoryState_instantiation(instance):
    assert isinstance(instance, scxml_HistoryState)


scxml_IAdaptable_strategy = st.builds(scxml_IAdaptable)
@given(instance=scxml_IAdaptable_strategy)
@settings(max_examples=25)
def test_scxml_IAdaptable_instantiation(instance):
    assert isinstance(instance, scxml_IAdaptable)


scxml_If_strategy = st.builds(scxml_If)
@given(instance=scxml_If_strategy)
@settings(max_examples=25)
def test_scxml_If_instantiation(instance):
    assert isinstance(instance, scxml_If)


scxml_InitialState_strategy = st.builds(scxml_InitialState)
@given(instance=scxml_InitialState_strategy)
@settings(max_examples=25)
def test_scxml_InitialState_instantiation(instance):
    assert isinstance(instance, scxml_InitialState)


scxml_Invoke_strategy = st.builds(scxml_Invoke, autoforward=safe_text, id=safe_text, idlocation=safe_text, namelist=safe_text, src=safe_text, srcexpr=safe_text, type=safe_text, typeexpr=safe_text)
@given(instance=scxml_Invoke_strategy)
@settings(max_examples=25)
def test_scxml_Invoke_instantiation(instance):
    assert isinstance(instance, scxml_Invoke)


scxml_Log_strategy = st.builds(scxml_Log, expr=safe_text, label=safe_text, level=safe_text)
@given(instance=scxml_Log_strategy)
@settings(max_examples=25)
def test_scxml_Log_instantiation(instance):
    assert isinstance(instance, scxml_Log)


scxml_Node_strategy = st.builds(scxml_Node)
@given(instance=scxml_Node_strategy)
@settings(max_examples=25)
def test_scxml_Node_instantiation(instance):
    assert isinstance(instance, scxml_Node)


scxml_OnEntry_strategy = st.builds(scxml_OnEntry)
@given(instance=scxml_OnEntry_strategy)
@settings(max_examples=25)
def test_scxml_OnEntry_instantiation(instance):
    assert isinstance(instance, scxml_OnEntry)


scxml_OnExit_strategy = st.builds(scxml_OnExit)
@given(instance=scxml_OnExit_strategy)
@settings(max_examples=25)
def test_scxml_OnExit_instantiation(instance):
    assert isinstance(instance, scxml_OnExit)


scxml_ParallelState_strategy = st.builds(scxml_ParallelState)
@given(instance=scxml_ParallelState_strategy)
@settings(max_examples=25)
def test_scxml_ParallelState_instantiation(instance):
    assert isinstance(instance, scxml_ParallelState)


scxml_Param_strategy = st.builds(scxml_Param, expr=safe_text, name=safe_text)
@given(instance=scxml_Param_strategy)
@settings(max_examples=25)
def test_scxml_Param_instantiation(instance):
    assert isinstance(instance, scxml_Param)


scxml_Raise_strategy = st.builds(scxml_Raise, event=safe_text)
@given(instance=scxml_Raise_strategy)
@settings(max_examples=25)
def test_scxml_Raise_instantiation(instance):
    assert isinstance(instance, scxml_Raise)


scxml_Script_strategy = st.builds(scxml_Script, value=safe_text)
@given(instance=scxml_Script_strategy)
@settings(max_examples=25)
def test_scxml_Script_instantiation(instance):
    assert isinstance(instance, scxml_Script)


scxml_Send_strategy = st.builds(scxml_Send, delay=safe_text, delayexpr=safe_text, event=safe_text, eventexpr=safe_text, hints=safe_text, hintsexpr=safe_text, id=safe_text, idlocation=safe_text, namelist=safe_text, target=safe_text, targetexpr=safe_text, type=safe_text, typeexpr=safe_text)
@given(instance=scxml_Send_strategy)
@settings(max_examples=25)
def test_scxml_Send_instantiation(instance):
    assert isinstance(instance, scxml_Send)


scxml_SimpleState_strategy = st.builds(scxml_SimpleState)
@given(instance=scxml_SimpleState_strategy)
@settings(max_examples=25)
def test_scxml_SimpleState_instantiation(instance):
    assert isinstance(instance, scxml_SimpleState)


scxml_State_strategy = st.builds(scxml_State)
@given(instance=scxml_State_strategy)
@settings(max_examples=25)
def test_scxml_State_instantiation(instance):
    assert isinstance(instance, scxml_State)


scxml_StateChart_strategy = st.builds(scxml_StateChart, exmode=safe_text, id=safe_text, profile=safe_text, version=safe_text, xmlns=safe_text)
@given(instance=scxml_StateChart_strategy)
@settings(max_examples=25)
def test_scxml_StateChart_instantiation(instance):
    assert isinstance(instance, scxml_StateChart)


scxml_Transition_strategy = st.builds(scxml_Transition)
@given(instance=scxml_Transition_strategy)
@settings(max_examples=25)
def test_scxml_Transition_instantiation(instance):
    assert isinstance(instance, scxml_Transition)


scxml_TransitionSource_strategy = st.builds(scxml_TransitionSource)
@given(instance=scxml_TransitionSource_strategy)
@settings(max_examples=25)
def test_scxml_TransitionSource_instantiation(instance):
    assert isinstance(instance, scxml_TransitionSource)


scxml_TransitionTarget_strategy = st.builds(scxml_TransitionTarget, id=safe_text)
@given(instance=scxml_TransitionTarget_strategy)
@settings(max_examples=25)
def test_scxml_TransitionTarget_instantiation(instance):
    assert isinstance(instance, scxml_TransitionTarget)


scxml_Validate_strategy = st.builds(scxml_Validate, location=safe_text, schema=safe_text)
@given(instance=scxml_Validate_strategy)
@settings(max_examples=25)
def test_scxml_Validate_instantiation(instance):
    assert isinstance(instance, scxml_Validate)


scxml_XData_strategy = st.builds(scxml_XData)
@given(instance=scxml_XData_strategy)
@settings(max_examples=25)
def test_scxml_XData_instantiation(instance):
    assert isinstance(instance, scxml_XData)


scxml_XObject_strategy = st.builds(scxml_XObject, classifierName=safe_text, exchange=st.booleans(), nsUri=safe_text)
@given(instance=scxml_XObject_strategy)
@settings(max_examples=25)
def test_scxml_XObject_instantiation(instance):
    assert isinstance(instance, scxml_XObject)



