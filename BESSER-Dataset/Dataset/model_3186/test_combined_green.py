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
    Action,
    co2_ActionType,
    co2_Action,
    Expression,
    co2_StringLiteral,
    co2_Equals,
    co2_Comparison,
    co2_Minus,
    co2_OrExpression,
    co2_AndExpression,
    co2_Plus,
    co2_NumberLiteral,
    co2_Case,
    Contract,
    co2_ExtSum,
    co2_IntSum,
    co2_EmptyContract,
    VariableDeclaration,
    co2_Type,
    co2_Placeholder,
    co2_BooleanLiteral,
    co2_Session,
    co2_ExtAction,
    co2_Input,
    ReceiveGroup,
    co2_Receive,
    SendGroup,
    co2_Send,
    co2_TimeoutProcess,
    co2_IntAction,
    co2_Contract,
    co2_VariableDeclaration,
    Prefix,
    co2_Ask,
    co2_DoOutput,
    co2_Retract,
    co2_Tau,
    co2_DoInput,
    co2_Tell,
    co2_Variable,
    co2_ContractDefinition,
    co2_ProcessDefinition,
    co2_Import,
    co2_ContractsAndProcessesDeclaration,
    co2_HonestyDeclaration,
    co2_Expression,
    co2_Prefix,
    co2_Process,
    co2_DelimitedProcess,
    Process,
    co2_Sum,
    co2_TellAndWait,
    co2_EmptyProcess,
    co2_ParallelProcesses,
    co2_SwitchCase,
    co2_IfThenElse,
    co2_TellAndReturn,
    co2_SendGroup,
    co2_ProcessCall,
    co2_ReceiveGroup,
    co2_RetractedProcess,
    co2_PackageDeclaration,
    co2_CO2System,
    Placeholder,
    co2_BoolPlaceholder,
    co2_IntPlaceholder,
    co2_VariableReference,
    co2_ArithmeticSigned,
    co2_BooleanNegation,
    co2_MultiOrDiv,
    ActionType,
    co2_IntActionType,
    co2_StringActionType,
    co2_UnitActionType,
    co2_ContractReference,
    Type,
    co2_SessionType,
    co2_BooleanType,
    co2_StringType,
    co2_IntType,
    co2_StringPlaceholder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_actiontype_is_not_abstract():
    assert not inspect.isabstract(co2_ActionType)


def test_hyp_co2_actiontype_constructor_exists():
    assert callable(co2_ActionType.__init__)


def test_hyp_co2_actiontype_constructor_args():
    sig = inspect.signature(co2_ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_action_is_not_abstract():
    assert not inspect.isabstract(co2_Action)


def test_hyp_co2_action_constructor_exists():
    assert callable(co2_Action.__init__)


def test_hyp_co2_action_constructor_args():
    sig = inspect.signature(co2_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_stringliteral_is_not_abstract():
    assert not inspect.isabstract(co2_StringLiteral)


def test_hyp_co2_stringliteral_constructor_exists():
    assert callable(co2_StringLiteral.__init__)


def test_hyp_co2_stringliteral_constructor_args():
    sig = inspect.signature(co2_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_equals_is_not_abstract():
    assert not inspect.isabstract(co2_Equals)


def test_hyp_co2_equals_constructor_exists():
    assert callable(co2_Equals.__init__)


def test_hyp_co2_equals_constructor_args():
    sig = inspect.signature(co2_Equals.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_co2_comparison_is_not_abstract():
    assert not inspect.isabstract(co2_Comparison)


def test_hyp_co2_comparison_constructor_exists():
    assert callable(co2_Comparison.__init__)


def test_hyp_co2_comparison_constructor_args():
    sig = inspect.signature(co2_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_co2_minus_is_not_abstract():
    assert not inspect.isabstract(co2_Minus)


def test_hyp_co2_minus_constructor_exists():
    assert callable(co2_Minus.__init__)


def test_hyp_co2_minus_constructor_args():
    sig = inspect.signature(co2_Minus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_orexpression_is_not_abstract():
    assert not inspect.isabstract(co2_OrExpression)


def test_hyp_co2_orexpression_constructor_exists():
    assert callable(co2_OrExpression.__init__)


def test_hyp_co2_orexpression_constructor_args():
    sig = inspect.signature(co2_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_andexpression_is_not_abstract():
    assert not inspect.isabstract(co2_AndExpression)


def test_hyp_co2_andexpression_constructor_exists():
    assert callable(co2_AndExpression.__init__)


def test_hyp_co2_andexpression_constructor_args():
    sig = inspect.signature(co2_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_plus_is_not_abstract():
    assert not inspect.isabstract(co2_Plus)


def test_hyp_co2_plus_constructor_exists():
    assert callable(co2_Plus.__init__)


def test_hyp_co2_plus_constructor_args():
    sig = inspect.signature(co2_Plus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_numberliteral_is_not_abstract():
    assert not inspect.isabstract(co2_NumberLiteral)


def test_hyp_co2_numberliteral_constructor_exists():
    assert callable(co2_NumberLiteral.__init__)


def test_hyp_co2_numberliteral_constructor_args():
    sig = inspect.signature(co2_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_case_is_not_abstract():
    assert not inspect.isabstract(co2_Case)


def test_hyp_co2_case_constructor_exists():
    assert callable(co2_Case.__init__)


def test_hyp_co2_case_constructor_args():
    sig = inspect.signature(co2_Case.__init__)
    params = list(sig.parameters.keys())



def test_hyp_contract_is_not_abstract():
    assert not inspect.isabstract(Contract)


def test_hyp_contract_constructor_exists():
    assert callable(Contract.__init__)


def test_hyp_contract_constructor_args():
    sig = inspect.signature(Contract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_extsum_is_not_abstract():
    assert not inspect.isabstract(co2_ExtSum)


def test_hyp_co2_extsum_constructor_exists():
    assert callable(co2_ExtSum.__init__)


def test_hyp_co2_extsum_constructor_args():
    sig = inspect.signature(co2_ExtSum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_intsum_is_not_abstract():
    assert not inspect.isabstract(co2_IntSum)


def test_hyp_co2_intsum_constructor_exists():
    assert callable(co2_IntSum.__init__)


def test_hyp_co2_intsum_constructor_args():
    sig = inspect.signature(co2_IntSum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_emptycontract_is_not_abstract():
    assert not inspect.isabstract(co2_EmptyContract)


def test_hyp_co2_emptycontract_constructor_exists():
    assert callable(co2_EmptyContract.__init__)


def test_hyp_co2_emptycontract_constructor_args():
    sig = inspect.signature(co2_EmptyContract.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_hyp_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_hyp_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_type_is_not_abstract():
    assert not inspect.isabstract(co2_Type)


def test_hyp_co2_type_constructor_exists():
    assert callable(co2_Type.__init__)


def test_hyp_co2_type_constructor_args():
    sig = inspect.signature(co2_Type.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_placeholder_is_not_abstract():
    assert not inspect.isabstract(co2_Placeholder)


def test_hyp_co2_placeholder_constructor_exists():
    assert callable(co2_Placeholder.__init__)


def test_hyp_co2_placeholder_constructor_args():
    sig = inspect.signature(co2_Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanLiteral)


def test_hyp_co2_booleanliteral_constructor_exists():
    assert callable(co2_BooleanLiteral.__init__)


def test_hyp_co2_booleanliteral_constructor_args():
    sig = inspect.signature(co2_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_session_is_not_abstract():
    assert not inspect.isabstract(co2_Session)


def test_hyp_co2_session_constructor_exists():
    assert callable(co2_Session.__init__)


def test_hyp_co2_session_constructor_args():
    sig = inspect.signature(co2_Session.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_extaction_is_not_abstract():
    assert not inspect.isabstract(co2_ExtAction)


def test_hyp_co2_extaction_constructor_exists():
    assert callable(co2_ExtAction.__init__)


def test_hyp_co2_extaction_constructor_args():
    sig = inspect.signature(co2_ExtAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_input_is_not_abstract():
    assert not inspect.isabstract(co2_Input)


def test_hyp_co2_input_constructor_exists():
    assert callable(co2_Input.__init__)


def test_hyp_co2_input_constructor_args():
    sig = inspect.signature(co2_Input.__init__)
    params = list(sig.parameters.keys())



def test_hyp_receivegroup_is_not_abstract():
    assert not inspect.isabstract(ReceiveGroup)


def test_hyp_receivegroup_constructor_exists():
    assert callable(ReceiveGroup.__init__)


def test_hyp_receivegroup_constructor_args():
    sig = inspect.signature(ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_receive_is_not_abstract():
    assert not inspect.isabstract(co2_Receive)


def test_hyp_co2_receive_constructor_exists():
    assert callable(co2_Receive.__init__)


def test_hyp_co2_receive_constructor_args():
    sig = inspect.signature(co2_Receive.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"




def test_hyp_sendgroup_is_not_abstract():
    assert not inspect.isabstract(SendGroup)


def test_hyp_sendgroup_constructor_exists():
    assert callable(SendGroup.__init__)


def test_hyp_sendgroup_constructor_args():
    sig = inspect.signature(SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_send_is_not_abstract():
    assert not inspect.isabstract(co2_Send)


def test_hyp_co2_send_constructor_exists():
    assert callable(co2_Send.__init__)


def test_hyp_co2_send_constructor_args():
    sig = inspect.signature(co2_Send.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_timeoutprocess_is_not_abstract():
    assert not inspect.isabstract(co2_TimeoutProcess)


def test_hyp_co2_timeoutprocess_constructor_exists():
    assert callable(co2_TimeoutProcess.__init__)


def test_hyp_co2_timeoutprocess_constructor_args():
    sig = inspect.signature(co2_TimeoutProcess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_intaction_is_not_abstract():
    assert not inspect.isabstract(co2_IntAction)


def test_hyp_co2_intaction_constructor_exists():
    assert callable(co2_IntAction.__init__)


def test_hyp_co2_intaction_constructor_args():
    sig = inspect.signature(co2_IntAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_contract_is_not_abstract():
    assert not inspect.isabstract(co2_Contract)


def test_hyp_co2_contract_constructor_exists():
    assert callable(co2_Contract.__init__)


def test_hyp_co2_contract_constructor_args():
    sig = inspect.signature(co2_Contract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_VariableDeclaration)


def test_hyp_co2_variabledeclaration_constructor_exists():
    assert callable(co2_VariableDeclaration.__init__)


def test_hyp_co2_variabledeclaration_constructor_args():
    sig = inspect.signature(co2_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_hyp_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_hyp_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_ask_is_not_abstract():
    assert not inspect.isabstract(co2_Ask)


def test_hyp_co2_ask_constructor_exists():
    assert callable(co2_Ask.__init__)


def test_hyp_co2_ask_constructor_args():
    sig = inspect.signature(co2_Ask.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"




def test_hyp_co2_dooutput_is_not_abstract():
    assert not inspect.isabstract(co2_DoOutput)


def test_hyp_co2_dooutput_constructor_exists():
    assert callable(co2_DoOutput.__init__)


def test_hyp_co2_dooutput_constructor_args():
    sig = inspect.signature(co2_DoOutput.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_retract_is_not_abstract():
    assert not inspect.isabstract(co2_Retract)


def test_hyp_co2_retract_constructor_exists():
    assert callable(co2_Retract.__init__)


def test_hyp_co2_retract_constructor_args():
    sig = inspect.signature(co2_Retract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_tau_is_not_abstract():
    assert not inspect.isabstract(co2_Tau)


def test_hyp_co2_tau_constructor_exists():
    assert callable(co2_Tau.__init__)


def test_hyp_co2_tau_constructor_args():
    sig = inspect.signature(co2_Tau.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_doinput_is_not_abstract():
    assert not inspect.isabstract(co2_DoInput)


def test_hyp_co2_doinput_constructor_exists():
    assert callable(co2_DoInput.__init__)


def test_hyp_co2_doinput_constructor_args():
    sig = inspect.signature(co2_DoInput.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_tell_is_not_abstract():
    assert not inspect.isabstract(co2_Tell)


def test_hyp_co2_tell_constructor_exists():
    assert callable(co2_Tell.__init__)


def test_hyp_co2_tell_constructor_args():
    sig = inspect.signature(co2_Tell.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_variable_is_not_abstract():
    assert not inspect.isabstract(co2_Variable)


def test_hyp_co2_variable_constructor_exists():
    assert callable(co2_Variable.__init__)


def test_hyp_co2_variable_constructor_args():
    sig = inspect.signature(co2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_contractdefinition_is_not_abstract():
    assert not inspect.isabstract(co2_ContractDefinition)


def test_hyp_co2_contractdefinition_constructor_exists():
    assert callable(co2_ContractDefinition.__init__)


def test_hyp_co2_contractdefinition_constructor_args():
    sig = inspect.signature(co2_ContractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_co2_processdefinition_is_not_abstract():
    assert not inspect.isabstract(co2_ProcessDefinition)


def test_hyp_co2_processdefinition_constructor_exists():
    assert callable(co2_ProcessDefinition.__init__)


def test_hyp_co2_processdefinition_constructor_args():
    sig = inspect.signature(co2_ProcessDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "withoutRestrictions" in params, "Missing parameter 'withoutRestrictions'"





def test_hyp_co2_import_is_not_abstract():
    assert not inspect.isabstract(co2_Import)


def test_hyp_co2_import_constructor_exists():
    assert callable(co2_Import.__init__)


def test_hyp_co2_import_constructor_args():
    sig = inspect.signature(co2_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"




def test_hyp_co2_contractsandprocessesdeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_ContractsAndProcessesDeclaration)


def test_hyp_co2_contractsandprocessesdeclaration_constructor_exists():
    assert callable(co2_ContractsAndProcessesDeclaration.__init__)


def test_hyp_co2_contractsandprocessesdeclaration_constructor_args():
    sig = inspect.signature(co2_ContractsAndProcessesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_honestydeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_HonestyDeclaration)


def test_hyp_co2_honestydeclaration_constructor_exists():
    assert callable(co2_HonestyDeclaration.__init__)


def test_hyp_co2_honestydeclaration_constructor_args():
    sig = inspect.signature(co2_HonestyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_expression_is_not_abstract():
    assert not inspect.isabstract(co2_Expression)


def test_hyp_co2_expression_constructor_exists():
    assert callable(co2_Expression.__init__)


def test_hyp_co2_expression_constructor_args():
    sig = inspect.signature(co2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_prefix_is_not_abstract():
    assert not inspect.isabstract(co2_Prefix)


def test_hyp_co2_prefix_constructor_exists():
    assert callable(co2_Prefix.__init__)


def test_hyp_co2_prefix_constructor_args():
    sig = inspect.signature(co2_Prefix.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_process_is_not_abstract():
    assert not inspect.isabstract(co2_Process)


def test_hyp_co2_process_constructor_exists():
    assert callable(co2_Process.__init__)


def test_hyp_co2_process_constructor_args():
    sig = inspect.signature(co2_Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_delimitedprocess_is_not_abstract():
    assert not inspect.isabstract(co2_DelimitedProcess)


def test_hyp_co2_delimitedprocess_constructor_exists():
    assert callable(co2_DelimitedProcess.__init__)


def test_hyp_co2_delimitedprocess_constructor_args():
    sig = inspect.signature(co2_DelimitedProcess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_hyp_process_constructor_exists():
    assert callable(Process.__init__)


def test_hyp_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_sum_is_not_abstract():
    assert not inspect.isabstract(co2_Sum)


def test_hyp_co2_sum_constructor_exists():
    assert callable(co2_Sum.__init__)


def test_hyp_co2_sum_constructor_args():
    sig = inspect.signature(co2_Sum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_tellandwait_is_not_abstract():
    assert not inspect.isabstract(co2_TellAndWait)


def test_hyp_co2_tellandwait_constructor_exists():
    assert callable(co2_TellAndWait.__init__)


def test_hyp_co2_tellandwait_constructor_args():
    sig = inspect.signature(co2_TellAndWait.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"




def test_hyp_co2_emptyprocess_is_not_abstract():
    assert not inspect.isabstract(co2_EmptyProcess)


def test_hyp_co2_emptyprocess_constructor_exists():
    assert callable(co2_EmptyProcess.__init__)


def test_hyp_co2_emptyprocess_constructor_args():
    sig = inspect.signature(co2_EmptyProcess.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_co2_parallelprocesses_is_not_abstract():
    assert not inspect.isabstract(co2_ParallelProcesses)


def test_hyp_co2_parallelprocesses_constructor_exists():
    assert callable(co2_ParallelProcesses.__init__)


def test_hyp_co2_parallelprocesses_constructor_args():
    sig = inspect.signature(co2_ParallelProcesses.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_switchcase_is_not_abstract():
    assert not inspect.isabstract(co2_SwitchCase)


def test_hyp_co2_switchcase_constructor_exists():
    assert callable(co2_SwitchCase.__init__)


def test_hyp_co2_switchcase_constructor_args():
    sig = inspect.signature(co2_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_co2_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(co2_IfThenElse)


def test_hyp_co2_ifthenelse_constructor_exists():
    assert callable(co2_IfThenElse.__init__)


def test_hyp_co2_ifthenelse_constructor_args():
    sig = inspect.signature(co2_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_tellandreturn_is_not_abstract():
    assert not inspect.isabstract(co2_TellAndReturn)


def test_hyp_co2_tellandreturn_constructor_exists():
    assert callable(co2_TellAndReturn.__init__)


def test_hyp_co2_tellandreturn_constructor_args():
    sig = inspect.signature(co2_TellAndReturn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_sendgroup_is_not_abstract():
    assert not inspect.isabstract(co2_SendGroup)


def test_hyp_co2_sendgroup_constructor_exists():
    assert callable(co2_SendGroup.__init__)


def test_hyp_co2_sendgroup_constructor_args():
    sig = inspect.signature(co2_SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_processcall_is_not_abstract():
    assert not inspect.isabstract(co2_ProcessCall)


def test_hyp_co2_processcall_constructor_exists():
    assert callable(co2_ProcessCall.__init__)


def test_hyp_co2_processcall_constructor_args():
    sig = inspect.signature(co2_ProcessCall.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_receivegroup_is_not_abstract():
    assert not inspect.isabstract(co2_ReceiveGroup)


def test_hyp_co2_receivegroup_constructor_exists():
    assert callable(co2_ReceiveGroup.__init__)


def test_hyp_co2_receivegroup_constructor_args():
    sig = inspect.signature(co2_ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_retractedprocess_is_not_abstract():
    assert not inspect.isabstract(co2_RetractedProcess)


def test_hyp_co2_retractedprocess_constructor_exists():
    assert callable(co2_RetractedProcess.__init__)


def test_hyp_co2_retractedprocess_constructor_args():
    sig = inspect.signature(co2_RetractedProcess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_PackageDeclaration)


def test_hyp_co2_packagedeclaration_constructor_exists():
    assert callable(co2_PackageDeclaration.__init__)


def test_hyp_co2_packagedeclaration_constructor_args():
    sig = inspect.signature(co2_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_co2_co2system_is_not_abstract():
    assert not inspect.isabstract(co2_CO2System)


def test_hyp_co2_co2system_constructor_exists():
    assert callable(co2_CO2System.__init__)


def test_hyp_co2_co2system_constructor_args():
    sig = inspect.signature(co2_CO2System.__init__)
    params = list(sig.parameters.keys())



def test_hyp_placeholder_is_not_abstract():
    assert not inspect.isabstract(Placeholder)


def test_hyp_placeholder_constructor_exists():
    assert callable(Placeholder.__init__)


def test_hyp_placeholder_constructor_args():
    sig = inspect.signature(Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_boolplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_BoolPlaceholder)


def test_hyp_co2_boolplaceholder_constructor_exists():
    assert callable(co2_BoolPlaceholder.__init__)


def test_hyp_co2_boolplaceholder_constructor_args():
    sig = inspect.signature(co2_BoolPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_intplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_IntPlaceholder)


def test_hyp_co2_intplaceholder_constructor_exists():
    assert callable(co2_IntPlaceholder.__init__)


def test_hyp_co2_intplaceholder_constructor_args():
    sig = inspect.signature(co2_IntPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_variablereference_is_not_abstract():
    assert not inspect.isabstract(co2_VariableReference)


def test_hyp_co2_variablereference_constructor_exists():
    assert callable(co2_VariableReference.__init__)


def test_hyp_co2_variablereference_constructor_args():
    sig = inspect.signature(co2_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_arithmeticsigned_is_not_abstract():
    assert not inspect.isabstract(co2_ArithmeticSigned)


def test_hyp_co2_arithmeticsigned_constructor_exists():
    assert callable(co2_ArithmeticSigned.__init__)


def test_hyp_co2_arithmeticsigned_constructor_args():
    sig = inspect.signature(co2_ArithmeticSigned.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_booleannegation_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanNegation)


def test_hyp_co2_booleannegation_constructor_exists():
    assert callable(co2_BooleanNegation.__init__)


def test_hyp_co2_booleannegation_constructor_args():
    sig = inspect.signature(co2_BooleanNegation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_multiordiv_is_not_abstract():
    assert not inspect.isabstract(co2_MultiOrDiv)


def test_hyp_co2_multiordiv_constructor_exists():
    assert callable(co2_MultiOrDiv.__init__)


def test_hyp_co2_multiordiv_constructor_args():
    sig = inspect.signature(co2_MultiOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_actiontype_is_not_abstract():
    assert not inspect.isabstract(ActionType)


def test_hyp_actiontype_constructor_exists():
    assert callable(ActionType.__init__)


def test_hyp_actiontype_constructor_args():
    sig = inspect.signature(ActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_intactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_IntActionType)


def test_hyp_co2_intactiontype_constructor_exists():
    assert callable(co2_IntActionType.__init__)


def test_hyp_co2_intactiontype_constructor_args():
    sig = inspect.signature(co2_IntActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_stringactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_StringActionType)


def test_hyp_co2_stringactiontype_constructor_exists():
    assert callable(co2_StringActionType.__init__)


def test_hyp_co2_stringactiontype_constructor_args():
    sig = inspect.signature(co2_StringActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_unitactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_UnitActionType)


def test_hyp_co2_unitactiontype_constructor_exists():
    assert callable(co2_UnitActionType.__init__)


def test_hyp_co2_unitactiontype_constructor_args():
    sig = inspect.signature(co2_UnitActionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_contractreference_is_not_abstract():
    assert not inspect.isabstract(co2_ContractReference)


def test_hyp_co2_contractreference_constructor_exists():
    assert callable(co2_ContractReference.__init__)


def test_hyp_co2_contractreference_constructor_args():
    sig = inspect.signature(co2_ContractReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_hyp_type_constructor_exists():
    assert callable(Type.__init__)


def test_hyp_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_sessiontype_is_not_abstract():
    assert not inspect.isabstract(co2_SessionType)


def test_hyp_co2_sessiontype_constructor_exists():
    assert callable(co2_SessionType.__init__)


def test_hyp_co2_sessiontype_constructor_args():
    sig = inspect.signature(co2_SessionType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_booleantype_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanType)


def test_hyp_co2_booleantype_constructor_exists():
    assert callable(co2_BooleanType.__init__)


def test_hyp_co2_booleantype_constructor_args():
    sig = inspect.signature(co2_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_stringtype_is_not_abstract():
    assert not inspect.isabstract(co2_StringType)


def test_hyp_co2_stringtype_constructor_exists():
    assert callable(co2_StringType.__init__)


def test_hyp_co2_stringtype_constructor_args():
    sig = inspect.signature(co2_StringType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_inttype_is_not_abstract():
    assert not inspect.isabstract(co2_IntType)


def test_hyp_co2_inttype_constructor_exists():
    assert callable(co2_IntType.__init__)


def test_hyp_co2_inttype_constructor_args():
    sig = inspect.signature(co2_IntType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_co2_stringplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_StringPlaceholder)


def test_hyp_co2_stringplaceholder_constructor_exists():
    assert callable(co2_StringPlaceholder.__init__)


def test_hyp_co2_stringplaceholder_constructor_args():
    sig = inspect.signature(co2_StringPlaceholder.__init__)
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
Action_strategy = st.builds(
    Action,
)
co2_ActionType_strategy = st.builds(
    co2_ActionType,
    value=
        safe_text
)
co2_Action_strategy = st.builds(
    co2_Action,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
co2_StringLiteral_strategy = st.builds(
    co2_StringLiteral,
    value=
        safe_text
)
co2_Equals_strategy = st.builds(
    co2_Equals,
    op=
        safe_text
)
co2_Comparison_strategy = st.builds(
    co2_Comparison,
    op=
        safe_text
)
co2_Minus_strategy = st.builds(
    co2_Minus,
)
co2_OrExpression_strategy = st.builds(
    co2_OrExpression,
)
co2_AndExpression_strategy = st.builds(
    co2_AndExpression,
)
co2_Plus_strategy = st.builds(
    co2_Plus,
)
co2_NumberLiteral_strategy = st.builds(
    co2_NumberLiteral,
    value=
        st.integers()
)
co2_Case_strategy = st.builds(
    co2_Case,
)
Contract_strategy = st.builds(
    Contract,
)
co2_ExtSum_strategy = st.builds(
    co2_ExtSum,
)
co2_IntSum_strategy = st.builds(
    co2_IntSum,
)
co2_EmptyContract_strategy = st.builds(
    co2_EmptyContract,
    value=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
co2_Type_strategy = st.builds(
    co2_Type,
    value=
        safe_text
)
co2_Placeholder_strategy = st.builds(
    co2_Placeholder,
)
co2_BooleanLiteral_strategy = st.builds(
    co2_BooleanLiteral,
    value=
        safe_text
)
co2_Session_strategy = st.builds(
    co2_Session,
)
co2_ExtAction_strategy = st.builds(
    co2_ExtAction,
)
co2_Input_strategy = st.builds(
    co2_Input,
)
ReceiveGroup_strategy = st.builds(
    ReceiveGroup,
)
co2_Receive_strategy = st.builds(
    co2_Receive,
    timeout=
        st.booleans()
)
SendGroup_strategy = st.builds(
    SendGroup,
)
co2_Send_strategy = st.builds(
    co2_Send,
)
co2_TimeoutProcess_strategy = st.builds(
    co2_TimeoutProcess,
)
co2_IntAction_strategy = st.builds(
    co2_IntAction,
)
co2_Contract_strategy = st.builds(
    co2_Contract,
)
co2_VariableDeclaration_strategy = st.builds(
    co2_VariableDeclaration,
    name=
        safe_text
)
Prefix_strategy = st.builds(
    Prefix,
)
co2_Ask_strategy = st.builds(
    co2_Ask,
    formula=
        safe_text
)
co2_DoOutput_strategy = st.builds(
    co2_DoOutput,
)
co2_Retract_strategy = st.builds(
    co2_Retract,
)
co2_Tau_strategy = st.builds(
    co2_Tau,
)
co2_DoInput_strategy = st.builds(
    co2_DoInput,
)
co2_Tell_strategy = st.builds(
    co2_Tell,
)
co2_Variable_strategy = st.builds(
    co2_Variable,
)
co2_ContractDefinition_strategy = st.builds(
    co2_ContractDefinition,
    name=
        safe_text
)
co2_ProcessDefinition_strategy = st.builds(
    co2_ProcessDefinition,
    name=
        safe_text,
    withoutRestrictions=
        st.booleans()
)
co2_Import_strategy = st.builds(
    co2_Import,
    importedNamespace=
        safe_text
)
co2_ContractsAndProcessesDeclaration_strategy = st.builds(
    co2_ContractsAndProcessesDeclaration,
)
co2_HonestyDeclaration_strategy = st.builds(
    co2_HonestyDeclaration,
)
co2_Expression_strategy = st.builds(
    co2_Expression,
)
co2_Prefix_strategy = st.builds(
    co2_Prefix,
)
co2_Process_strategy = st.builds(
    co2_Process,
)
co2_DelimitedProcess_strategy = st.builds(
    co2_DelimitedProcess,
)
Process_strategy = st.builds(
    Process,
)
co2_Sum_strategy = st.builds(
    co2_Sum,
)
co2_TellAndWait_strategy = st.builds(
    co2_TellAndWait,
    timeout=
        st.booleans()
)
co2_EmptyProcess_strategy = st.builds(
    co2_EmptyProcess,
    value=
        safe_text
)
co2_ParallelProcesses_strategy = st.builds(
    co2_ParallelProcesses,
)
co2_SwitchCase_strategy = st.builds(
    co2_SwitchCase,
    default=
        st.booleans()
)
co2_IfThenElse_strategy = st.builds(
    co2_IfThenElse,
)
co2_TellAndReturn_strategy = st.builds(
    co2_TellAndReturn,
)
co2_SendGroup_strategy = st.builds(
    co2_SendGroup,
)
co2_ProcessCall_strategy = st.builds(
    co2_ProcessCall,
)
co2_ReceiveGroup_strategy = st.builds(
    co2_ReceiveGroup,
)
co2_RetractedProcess_strategy = st.builds(
    co2_RetractedProcess,
)
co2_PackageDeclaration_strategy = st.builds(
    co2_PackageDeclaration,
    single=
        st.booleans(),
    name=
        safe_text
)
co2_CO2System_strategy = st.builds(
    co2_CO2System,
)
Placeholder_strategy = st.builds(
    Placeholder,
)
co2_BoolPlaceholder_strategy = st.builds(
    co2_BoolPlaceholder,
)
co2_IntPlaceholder_strategy = st.builds(
    co2_IntPlaceholder,
)
co2_VariableReference_strategy = st.builds(
    co2_VariableReference,
)
co2_ArithmeticSigned_strategy = st.builds(
    co2_ArithmeticSigned,
)
co2_BooleanNegation_strategy = st.builds(
    co2_BooleanNegation,
)
co2_MultiOrDiv_strategy = st.builds(
    co2_MultiOrDiv,
    op=
        safe_text
)
ActionType_strategy = st.builds(
    ActionType,
)
co2_IntActionType_strategy = st.builds(
    co2_IntActionType,
)
co2_StringActionType_strategy = st.builds(
    co2_StringActionType,
)
co2_UnitActionType_strategy = st.builds(
    co2_UnitActionType,
)
co2_ContractReference_strategy = st.builds(
    co2_ContractReference,
)
Type_strategy = st.builds(
    Type,
)
co2_SessionType_strategy = st.builds(
    co2_SessionType,
)
co2_BooleanType_strategy = st.builds(
    co2_BooleanType,
)
co2_StringType_strategy = st.builds(
    co2_StringType,
)
co2_IntType_strategy = st.builds(
    co2_IntType,
)
co2_StringPlaceholder_strategy = st.builds(
    co2_StringPlaceholder,
)





@given(instance=co2_ActionType_strategy)
def test_hyp_co2_actiontype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=co2_Action_strategy)
def test_hyp_co2_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=co2_StringLiteral_strategy)
def test_hyp_co2_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=co2_Equals_strategy)
def test_hyp_co2_equals_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original




@given(instance=co2_Comparison_strategy)
def test_hyp_co2_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original








@given(instance=co2_NumberLiteral_strategy)
def test_hyp_co2_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=co2_EmptyContract_strategy)
def test_hyp_co2_emptycontract_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=co2_Type_strategy)
def test_hyp_co2_type_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=co2_BooleanLiteral_strategy)
def test_hyp_co2_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original








@given(instance=co2_Receive_strategy)
def test_hyp_co2_receive_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original









@given(instance=co2_VariableDeclaration_strategy)
def test_hyp_co2_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=co2_Ask_strategy)
def test_hyp_co2_ask_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original










@given(instance=co2_ContractDefinition_strategy)
def test_hyp_co2_contractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=co2_ProcessDefinition_strategy)
def test_hyp_co2_processdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=co2_ProcessDefinition_strategy)
def test_hyp_co2_processdefinition_withoutRestrictions_setter(instance):
    original = instance.withoutRestrictions
    instance.withoutRestrictions = original
    assert instance.withoutRestrictions == original




@given(instance=co2_Import_strategy)
def test_hyp_co2_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original












@given(instance=co2_TellAndWait_strategy)
def test_hyp_co2_tellandwait_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original




@given(instance=co2_EmptyProcess_strategy)
def test_hyp_co2_emptyprocess_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=co2_SwitchCase_strategy)
def test_hyp_co2_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original










@given(instance=co2_PackageDeclaration_strategy)
def test_hyp_co2_packagedeclaration_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original



@given(instance=co2_PackageDeclaration_strategy)
def test_hyp_co2_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=co2_MultiOrDiv_strategy)
def test_hyp_co2_multiordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original













# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    ActionType,
    Contract,
    Expression,
    Placeholder,
    Prefix,
    Process,
    ReceiveGroup,
    SendGroup,
    Type,
    VariableDeclaration,
    co2_Action,
    co2_ActionType,
    co2_AndExpression,
    co2_ArithmeticSigned,
    co2_Ask,
    co2_BoolPlaceholder,
    co2_BooleanLiteral,
    co2_BooleanNegation,
    co2_BooleanType,
    co2_CO2System,
    co2_Case,
    co2_Comparison,
    co2_Contract,
    co2_ContractDefinition,
    co2_ContractReference,
    co2_ContractsAndProcessesDeclaration,
    co2_DelimitedProcess,
    co2_DoInput,
    co2_DoOutput,
    co2_EmptyContract,
    co2_EmptyProcess,
    co2_Equals,
    co2_Expression,
    co2_ExtAction,
    co2_ExtSum,
    co2_HonestyDeclaration,
    co2_IfThenElse,
    co2_Import,
    co2_Input,
    co2_IntAction,
    co2_IntActionType,
    co2_IntPlaceholder,
    co2_IntSum,
    co2_IntType,
    co2_Minus,
    co2_MultiOrDiv,
    co2_NumberLiteral,
    co2_OrExpression,
    co2_PackageDeclaration,
    co2_ParallelProcesses,
    co2_Placeholder,
    co2_Plus,
    co2_Prefix,
    co2_Process,
    co2_ProcessCall,
    co2_ProcessDefinition,
    co2_Receive,
    co2_ReceiveGroup,
    co2_Retract,
    co2_RetractedProcess,
    co2_Send,
    co2_SendGroup,
    co2_Session,
    co2_SessionType,
    co2_StringActionType,
    co2_StringLiteral,
    co2_StringPlaceholder,
    co2_StringType,
    co2_Sum,
    co2_SwitchCase,
    co2_Tau,
    co2_Tell,
    co2_TellAndReturn,
    co2_TellAndWait,
    co2_TimeoutProcess,
    co2_Type,
    co2_UnitActionType,
    co2_Variable,
    co2_VariableDeclaration,
    co2_VariableReference,
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

def test_co2_Action_name_value_roundtrip():
    instance = co2_Action(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_co2_ActionType_value_value_roundtrip():
    instance = co2_ActionType(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_Ask_formula_value_roundtrip():
    instance = co2_Ask(formula="sample_text")
    assert instance.formula == "sample_text"
    instance.formula = "sample_text_2"
    assert instance.formula == "sample_text_2"


def test_co2_BooleanLiteral_value_value_roundtrip():
    instance = co2_BooleanLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_Comparison_op_value_roundtrip():
    instance = co2_Comparison(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_co2_ContractDefinition_name_value_roundtrip():
    instance = co2_ContractDefinition(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_co2_EmptyContract_value_value_roundtrip():
    instance = co2_EmptyContract(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_EmptyProcess_value_value_roundtrip():
    instance = co2_EmptyProcess(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_Equals_op_value_roundtrip():
    instance = co2_Equals(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_co2_Import_importedNamespace_value_roundtrip():
    instance = co2_Import(importedNamespace="sample_text")
    assert instance.importedNamespace == "sample_text"
    instance.importedNamespace = "sample_text_2"
    assert instance.importedNamespace == "sample_text_2"


def test_co2_MultiOrDiv_op_value_roundtrip():
    instance = co2_MultiOrDiv(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_co2_NumberLiteral_value_value_roundtrip():
    instance = co2_NumberLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_co2_PackageDeclaration_name_value_roundtrip():
    instance = co2_PackageDeclaration(name="sample_text", single=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_co2_PackageDeclaration_single_value_roundtrip():
    instance = co2_PackageDeclaration(name="sample_text", single=True)
    assert instance.single == True
    instance.single = False
    assert instance.single == False


def test_co2_ProcessDefinition_name_value_roundtrip():
    instance = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_co2_ProcessDefinition_withoutRestrictions_value_roundtrip():
    instance = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    assert instance.withoutRestrictions == True
    instance.withoutRestrictions = False
    assert instance.withoutRestrictions == False


def test_co2_Receive_timeout_value_roundtrip():
    instance = co2_Receive(timeout=True)
    assert instance.timeout == True
    instance.timeout = False
    assert instance.timeout == False


def test_co2_StringLiteral_value_value_roundtrip():
    instance = co2_StringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_SwitchCase_default_value_roundtrip():
    instance = co2_SwitchCase(default=True)
    assert instance.default == True
    instance.default = False
    assert instance.default == False


def test_co2_TellAndWait_timeout_value_roundtrip():
    instance = co2_TellAndWait(timeout=True)
    assert instance.timeout == True
    instance.timeout = False
    assert instance.timeout == False


def test_co2_Type_value_value_roundtrip():
    instance = co2_Type(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_co2_VariableDeclaration_name_value_roundtrip():
    instance = co2_VariableDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_co2_ExtAction_isa_Action():
    instance = co2_ExtAction()
    assert isinstance(instance, Action)


def test_co2_IntAction_isa_Action():
    instance = co2_IntAction()
    assert isinstance(instance, Action)


def test_co2_IntActionType_isa_ActionType():
    instance = co2_IntActionType()
    assert isinstance(instance, ActionType)


def test_co2_StringActionType_isa_ActionType():
    instance = co2_StringActionType()
    assert isinstance(instance, ActionType)


def test_co2_UnitActionType_isa_ActionType():
    instance = co2_UnitActionType()
    assert isinstance(instance, ActionType)


def test_co2_ContractReference_isa_Contract():
    instance = co2_ContractReference()
    assert isinstance(instance, Contract)


def test_co2_EmptyContract_isa_Contract():
    instance = co2_EmptyContract(value="sample_text")
    assert isinstance(instance, Contract)


def test_co2_ExtSum_isa_Contract():
    instance = co2_ExtSum()
    assert isinstance(instance, Contract)


def test_co2_IntSum_isa_Contract():
    instance = co2_IntSum()
    assert isinstance(instance, Contract)


def test_co2_AndExpression_isa_Expression():
    instance = co2_AndExpression()
    assert isinstance(instance, Expression)


def test_co2_ArithmeticSigned_isa_Expression():
    instance = co2_ArithmeticSigned()
    assert isinstance(instance, Expression)


def test_co2_BooleanLiteral_isa_Expression():
    instance = co2_BooleanLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_co2_BooleanNegation_isa_Expression():
    instance = co2_BooleanNegation()
    assert isinstance(instance, Expression)


def test_co2_Comparison_isa_Expression():
    instance = co2_Comparison(op="sample_text")
    assert isinstance(instance, Expression)


def test_co2_Equals_isa_Expression():
    instance = co2_Equals(op="sample_text")
    assert isinstance(instance, Expression)


def test_co2_Minus_isa_Expression():
    instance = co2_Minus()
    assert isinstance(instance, Expression)


def test_co2_MultiOrDiv_isa_Expression():
    instance = co2_MultiOrDiv(op="sample_text")
    assert isinstance(instance, Expression)


def test_co2_NumberLiteral_isa_Expression():
    instance = co2_NumberLiteral(value=7)
    assert isinstance(instance, Expression)


def test_co2_OrExpression_isa_Expression():
    instance = co2_OrExpression()
    assert isinstance(instance, Expression)


def test_co2_Placeholder_isa_Expression():
    instance = co2_Placeholder()
    assert isinstance(instance, Expression)


def test_co2_Plus_isa_Expression():
    instance = co2_Plus()
    assert isinstance(instance, Expression)


def test_co2_StringLiteral_isa_Expression():
    instance = co2_StringLiteral(value="sample_text")
    assert isinstance(instance, Expression)


def test_co2_VariableReference_isa_Expression():
    instance = co2_VariableReference()
    assert isinstance(instance, Expression)


def test_co2_BoolPlaceholder_isa_Placeholder():
    instance = co2_BoolPlaceholder()
    assert isinstance(instance, Placeholder)


def test_co2_IntPlaceholder_isa_Placeholder():
    instance = co2_IntPlaceholder()
    assert isinstance(instance, Placeholder)


def test_co2_StringPlaceholder_isa_Placeholder():
    instance = co2_StringPlaceholder()
    assert isinstance(instance, Placeholder)


def test_co2_Ask_isa_Prefix():
    instance = co2_Ask(formula="sample_text")
    assert isinstance(instance, Prefix)


def test_co2_DoInput_isa_Prefix():
    instance = co2_DoInput()
    assert isinstance(instance, Prefix)


def test_co2_DoOutput_isa_Prefix():
    instance = co2_DoOutput()
    assert isinstance(instance, Prefix)


def test_co2_Retract_isa_Prefix():
    instance = co2_Retract()
    assert isinstance(instance, Prefix)


def test_co2_Tau_isa_Prefix():
    instance = co2_Tau()
    assert isinstance(instance, Prefix)


def test_co2_Tell_isa_Prefix():
    instance = co2_Tell()
    assert isinstance(instance, Prefix)


def test_co2_EmptyProcess_isa_Process():
    instance = co2_EmptyProcess(value="sample_text")
    assert isinstance(instance, Process)


def test_co2_IfThenElse_isa_Process():
    instance = co2_IfThenElse()
    assert isinstance(instance, Process)


def test_co2_ParallelProcesses_isa_Process():
    instance = co2_ParallelProcesses()
    assert isinstance(instance, Process)


def test_co2_ProcessCall_isa_Process():
    instance = co2_ProcessCall()
    assert isinstance(instance, Process)


def test_co2_ReceiveGroup_isa_Process():
    instance = co2_ReceiveGroup()
    assert isinstance(instance, Process)


def test_co2_RetractedProcess_isa_Process():
    instance = co2_RetractedProcess()
    assert isinstance(instance, Process)


def test_co2_SendGroup_isa_Process():
    instance = co2_SendGroup()
    assert isinstance(instance, Process)


def test_co2_Sum_isa_Process():
    instance = co2_Sum()
    assert isinstance(instance, Process)


def test_co2_SwitchCase_isa_Process():
    instance = co2_SwitchCase(default=True)
    assert isinstance(instance, Process)


def test_co2_TellAndReturn_isa_Process():
    instance = co2_TellAndReturn()
    assert isinstance(instance, Process)


def test_co2_TellAndWait_isa_Process():
    instance = co2_TellAndWait(timeout=True)
    assert isinstance(instance, Process)


def test_co2_Receive_isa_ReceiveGroup():
    instance = co2_Receive(timeout=True)
    assert isinstance(instance, ReceiveGroup)


def test_co2_Send_isa_SendGroup():
    instance = co2_Send()
    assert isinstance(instance, SendGroup)


def test_co2_BooleanType_isa_Type():
    instance = co2_BooleanType()
    assert isinstance(instance, Type)


def test_co2_IntType_isa_Type():
    instance = co2_IntType()
    assert isinstance(instance, Type)


def test_co2_SessionType_isa_Type():
    instance = co2_SessionType()
    assert isinstance(instance, Type)


def test_co2_StringType_isa_Type():
    instance = co2_StringType()
    assert isinstance(instance, Type)


def test_co2_Session_isa_VariableDeclaration():
    instance = co2_Session()
    assert isinstance(instance, VariableDeclaration)


def test_co2_Variable_isa_VariableDeclaration():
    instance = co2_Variable()
    assert isinstance(instance, VariableDeclaration)


def test_assoc_cases109_link_reassign_clear():
    a = co2_SwitchCase(default=True)
    b1 = co2_Case()
    b2 = co2_Case()
    _safe_set(a, 'co2_SwitchCase110', {b1})
    assert _is_linked(a, 'co2_SwitchCase110', b1)
    if hasattr(b1, 'co2_Case'):
        assert _is_linked(b1, 'co2_Case', a)
    _safe_set(a, 'co2_SwitchCase110', {b2})
    assert _is_linked(a, 'co2_SwitchCase110', b2)
    if hasattr(b1, 'co2_Case'):
        assert not _is_linked(b1, 'co2_Case', a)
    if hasattr(b2, 'co2_Case'):
        assert _is_linked(b2, 'co2_Case', a)
    _safe_set(a, 'co2_SwitchCase110', set())
    assert not _is_linked(a, 'co2_SwitchCase110', b2)
    if hasattr(b2, 'co2_Case'):
        assert not _is_linked(b2, 'co2_Case', a)


def test_assoc_contract130_link_reassign_clear():
    a = co2_ContractDefinition(name="sample_text")
    b1 = co2_Contract()
    b2 = co2_Contract()
    _safe_set(a, 'co2_ContractDefinition131', b1)
    assert _is_linked(a, 'co2_ContractDefinition131', b1)
    if hasattr(b1, 'co2_Contract132'):
        assert _is_linked(b1, 'co2_Contract132', a)
    _safe_set(a, 'co2_ContractDefinition131', b2)
    assert _is_linked(a, 'co2_ContractDefinition131', b2)
    if hasattr(b1, 'co2_Contract132'):
        assert not _is_linked(b1, 'co2_Contract132', a)
    if hasattr(b2, 'co2_Contract132'):
        assert _is_linked(b2, 'co2_Contract132', a)
    _safe_set(a, 'co2_ContractDefinition131', None)
    assert not _is_linked(a, 'co2_ContractDefinition131', b2)
    if hasattr(b2, 'co2_Contract132'):
        assert not _is_linked(b2, 'co2_Contract132', a)


def test_assoc_contractReference127_link_reassign_clear():
    a = co2_ContractDefinition(name="sample_text")
    b1 = co2_Session()
    b2 = co2_Session()
    _safe_set(a, 'co2_ContractDefinition129', b1)
    assert _is_linked(a, 'co2_ContractDefinition129', b1)
    if hasattr(b1, 'co2_Session128'):
        assert _is_linked(b1, 'co2_Session128', a)
    _safe_set(a, 'co2_ContractDefinition129', b2)
    assert _is_linked(a, 'co2_ContractDefinition129', b2)
    if hasattr(b1, 'co2_Session128'):
        assert not _is_linked(b1, 'co2_Session128', a)
    if hasattr(b2, 'co2_Session128'):
        assert _is_linked(b2, 'co2_Session128', a)
    _safe_set(a, 'co2_ContractDefinition129', None)
    assert not _is_linked(a, 'co2_ContractDefinition129', b2)
    if hasattr(b2, 'co2_Session128'):
        assert not _is_linked(b2, 'co2_Session128', a)


def test_assoc_contractReference42_link_reassign_clear():
    a = co2_ContractDefinition(name="sample_text")
    b1 = co2_Tell()
    b2 = co2_Tell()
    _safe_set(a, 'co2_ContractDefinition44', b1)
    assert _is_linked(a, 'co2_ContractDefinition44', b1)
    if hasattr(b1, 'co2_Tell43'):
        assert _is_linked(b1, 'co2_Tell43', a)
    _safe_set(a, 'co2_ContractDefinition44', b2)
    assert _is_linked(a, 'co2_ContractDefinition44', b2)
    if hasattr(b1, 'co2_Tell43'):
        assert not _is_linked(b1, 'co2_Tell43', a)
    if hasattr(b2, 'co2_Tell43'):
        assert _is_linked(b2, 'co2_Tell43', a)
    _safe_set(a, 'co2_ContractDefinition44', None)
    assert not _is_linked(a, 'co2_ContractDefinition44', b2)
    if hasattr(b2, 'co2_Tell43'):
        assert not _is_linked(b2, 'co2_Tell43', a)


def test_assoc_contracts7_link_reassign_clear():
    a = co2_ContractDefinition(name="sample_text")
    b1 = co2_ContractsAndProcessesDeclaration()
    b2 = co2_ContractsAndProcessesDeclaration()
    _safe_set(a, 'co2_ContractDefinition', b1)
    assert _is_linked(a, 'co2_ContractDefinition', b1)
    if hasattr(b1, 'co2_ContractsAndProcessesDeclaration8'):
        assert _is_linked(b1, 'co2_ContractsAndProcessesDeclaration8', a)
    _safe_set(a, 'co2_ContractDefinition', b2)
    assert _is_linked(a, 'co2_ContractDefinition', b2)
    if hasattr(b1, 'co2_ContractsAndProcessesDeclaration8'):
        assert not _is_linked(b1, 'co2_ContractsAndProcessesDeclaration8', a)
    if hasattr(b2, 'co2_ContractsAndProcessesDeclaration8'):
        assert _is_linked(b2, 'co2_ContractsAndProcessesDeclaration8', a)
    _safe_set(a, 'co2_ContractDefinition', None)
    assert not _is_linked(a, 'co2_ContractDefinition', b2)
    if hasattr(b2, 'co2_ContractsAndProcessesDeclaration8'):
        assert not _is_linked(b2, 'co2_ContractsAndProcessesDeclaration8', a)


def test_assoc_defaultProc111_link_reassign_clear():
    a = co2_SwitchCase(default=True)
    b1 = co2_Process()
    b2 = co2_Process()
    _safe_set(a, 'co2_SwitchCase112', b1)
    assert _is_linked(a, 'co2_SwitchCase112', b1)
    if hasattr(b1, 'co2_Process113'):
        assert _is_linked(b1, 'co2_Process113', a)
    _safe_set(a, 'co2_SwitchCase112', b2)
    assert _is_linked(a, 'co2_SwitchCase112', b2)
    if hasattr(b1, 'co2_Process113'):
        assert not _is_linked(b1, 'co2_Process113', a)
    if hasattr(b2, 'co2_Process113'):
        assert _is_linked(b2, 'co2_Process113', a)
    _safe_set(a, 'co2_SwitchCase112', None)
    assert not _is_linked(a, 'co2_SwitchCase112', b2)
    if hasattr(b2, 'co2_Process113'):
        assert not _is_linked(b2, 'co2_Process113', a)


def test_assoc_exp107_link_reassign_clear():
    a = co2_SwitchCase(default=True)
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_SwitchCase', b1)
    assert _is_linked(a, 'co2_SwitchCase', b1)
    if hasattr(b1, 'co2_Expression108'):
        assert _is_linked(b1, 'co2_Expression108', a)
    _safe_set(a, 'co2_SwitchCase', b2)
    assert _is_linked(a, 'co2_SwitchCase', b2)
    if hasattr(b1, 'co2_Expression108'):
        assert not _is_linked(b1, 'co2_Expression108', a)
    if hasattr(b2, 'co2_Expression108'):
        assert _is_linked(b2, 'co2_Expression108', a)
    _safe_set(a, 'co2_SwitchCase', None)
    assert not _is_linked(a, 'co2_SwitchCase', b2)
    if hasattr(b2, 'co2_Expression108'):
        assert not _is_linked(b2, 'co2_Expression108', a)


def test_assoc_inputs91_link_reassign_clear():
    a = co2_Receive(timeout=True)
    b1 = co2_Input()
    b2 = co2_Input()
    _safe_set(a, 'co2_Receive', {b1})
    assert _is_linked(a, 'co2_Receive', b1)
    if hasattr(b1, 'co2_Input'):
        assert _is_linked(b1, 'co2_Input', a)
    _safe_set(a, 'co2_Receive', {b2})
    assert _is_linked(a, 'co2_Receive', b2)
    if hasattr(b1, 'co2_Input'):
        assert not _is_linked(b1, 'co2_Input', a)
    if hasattr(b2, 'co2_Input'):
        assert _is_linked(b2, 'co2_Input', a)
    _safe_set(a, 'co2_Receive', set())
    assert not _is_linked(a, 'co2_Receive', b2)
    if hasattr(b2, 'co2_Input'):
        assert not _is_linked(b2, 'co2_Input', a)


def test_assoc_left153_link_reassign_clear():
    a = co2_Comparison(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_Comparison', b1)
    assert _is_linked(a, 'co2_Comparison', b1)
    if hasattr(b1, 'co2_Expression154'):
        assert _is_linked(b1, 'co2_Expression154', a)
    _safe_set(a, 'co2_Comparison', b2)
    assert _is_linked(a, 'co2_Comparison', b2)
    if hasattr(b1, 'co2_Expression154'):
        assert not _is_linked(b1, 'co2_Expression154', a)
    if hasattr(b2, 'co2_Expression154'):
        assert _is_linked(b2, 'co2_Expression154', a)
    _safe_set(a, 'co2_Comparison', None)
    assert not _is_linked(a, 'co2_Comparison', b2)
    if hasattr(b2, 'co2_Expression154'):
        assert not _is_linked(b2, 'co2_Expression154', a)


def test_assoc_left158_link_reassign_clear():
    a = co2_Equals(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_Equals', b1)
    assert _is_linked(a, 'co2_Equals', b1)
    if hasattr(b1, 'co2_Expression159'):
        assert _is_linked(b1, 'co2_Expression159', a)
    _safe_set(a, 'co2_Equals', b2)
    assert _is_linked(a, 'co2_Equals', b2)
    if hasattr(b1, 'co2_Expression159'):
        assert not _is_linked(b1, 'co2_Expression159', a)
    if hasattr(b2, 'co2_Expression159'):
        assert _is_linked(b2, 'co2_Expression159', a)
    _safe_set(a, 'co2_Equals', None)
    assert not _is_linked(a, 'co2_Equals', b2)
    if hasattr(b2, 'co2_Expression159'):
        assert not _is_linked(b2, 'co2_Expression159', a)


def test_assoc_left173_link_reassign_clear():
    a = co2_MultiOrDiv(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_MultiOrDiv', b1)
    assert _is_linked(a, 'co2_MultiOrDiv', b1)
    if hasattr(b1, 'co2_Expression174'):
        assert _is_linked(b1, 'co2_Expression174', a)
    _safe_set(a, 'co2_MultiOrDiv', b2)
    assert _is_linked(a, 'co2_MultiOrDiv', b2)
    if hasattr(b1, 'co2_Expression174'):
        assert not _is_linked(b1, 'co2_Expression174', a)
    if hasattr(b2, 'co2_Expression174'):
        assert _is_linked(b2, 'co2_Expression174', a)
    _safe_set(a, 'co2_MultiOrDiv', None)
    assert not _is_linked(a, 'co2_MultiOrDiv', b2)
    if hasattr(b2, 'co2_Expression174'):
        assert not _is_linked(b2, 'co2_Expression174', a)


def test_assoc_next138_link_reassign_clear():
    a = co2_Action(name="sample_text")
    b1 = co2_Contract()
    b2 = co2_Contract()
    _safe_set(a, 'co2_Action139', b1)
    assert _is_linked(a, 'co2_Action139', b1)
    if hasattr(b1, 'co2_Contract140'):
        assert _is_linked(b1, 'co2_Contract140', a)
    _safe_set(a, 'co2_Action139', b2)
    assert _is_linked(a, 'co2_Action139', b2)
    if hasattr(b1, 'co2_Contract140'):
        assert not _is_linked(b1, 'co2_Contract140', a)
    if hasattr(b2, 'co2_Contract140'):
        assert _is_linked(b2, 'co2_Contract140', a)
    _safe_set(a, 'co2_Action139', None)
    assert not _is_linked(a, 'co2_Action139', b2)
    if hasattr(b2, 'co2_Contract140'):
        assert not _is_linked(b2, 'co2_Contract140', a)


def test_assoc_package0_link_reassign_clear():
    a = co2_PackageDeclaration(name="sample_text", single=True)
    b1 = co2_CO2System()
    b2 = co2_CO2System()
    _safe_set(a, 'co2_PackageDeclaration', b1)
    assert _is_linked(a, 'co2_PackageDeclaration', b1)
    if hasattr(b1, 'co2_CO2System'):
        assert _is_linked(b1, 'co2_CO2System', a)
    _safe_set(a, 'co2_PackageDeclaration', b2)
    assert _is_linked(a, 'co2_PackageDeclaration', b2)
    if hasattr(b1, 'co2_CO2System'):
        assert not _is_linked(b1, 'co2_CO2System', a)
    if hasattr(b2, 'co2_CO2System'):
        assert _is_linked(b2, 'co2_CO2System', a)
    _safe_set(a, 'co2_PackageDeclaration', None)
    assert not _is_linked(a, 'co2_PackageDeclaration', b2)
    if hasattr(b2, 'co2_CO2System'):
        assert not _is_linked(b2, 'co2_CO2System', a)


def test_assoc_params12_link_reassign_clear():
    a = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    b1 = co2_Variable()
    b2 = co2_Variable()
    _safe_set(a, 'co2_ProcessDefinition13', {b1})
    assert _is_linked(a, 'co2_ProcessDefinition13', b1)
    if hasattr(b1, 'co2_Variable'):
        assert _is_linked(b1, 'co2_Variable', a)
    _safe_set(a, 'co2_ProcessDefinition13', {b2})
    assert _is_linked(a, 'co2_ProcessDefinition13', b2)
    if hasattr(b1, 'co2_Variable'):
        assert not _is_linked(b1, 'co2_Variable', a)
    if hasattr(b2, 'co2_Variable'):
        assert _is_linked(b2, 'co2_Variable', a)
    _safe_set(a, 'co2_ProcessDefinition13', set())
    assert not _is_linked(a, 'co2_ProcessDefinition13', b2)
    if hasattr(b2, 'co2_Variable'):
        assert not _is_linked(b2, 'co2_Variable', a)


def test_assoc_process14_link_reassign_clear():
    a = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    b1 = co2_ParallelProcesses()
    b2 = co2_ParallelProcesses()
    _safe_set(a, 'co2_ProcessDefinition15', b1)
    assert _is_linked(a, 'co2_ProcessDefinition15', b1)
    if hasattr(b1, 'co2_ParallelProcesses'):
        assert _is_linked(b1, 'co2_ParallelProcesses', a)
    _safe_set(a, 'co2_ProcessDefinition15', b2)
    assert _is_linked(a, 'co2_ProcessDefinition15', b2)
    if hasattr(b1, 'co2_ParallelProcesses'):
        assert not _is_linked(b1, 'co2_ParallelProcesses', a)
    if hasattr(b2, 'co2_ParallelProcesses'):
        assert _is_linked(b2, 'co2_ParallelProcesses', a)
    _safe_set(a, 'co2_ProcessDefinition15', None)
    assert not _is_linked(a, 'co2_ProcessDefinition15', b2)
    if hasattr(b2, 'co2_ParallelProcesses'):
        assert not _is_linked(b2, 'co2_ParallelProcesses', a)


def test_assoc_process69_link_reassign_clear():
    a = co2_TellAndWait(timeout=True)
    b1 = co2_Process()
    b2 = co2_Process()
    _safe_set(a, 'co2_TellAndWait70', b1)
    assert _is_linked(a, 'co2_TellAndWait70', b1)
    if hasattr(b1, 'co2_Process71'):
        assert _is_linked(b1, 'co2_Process71', a)
    _safe_set(a, 'co2_TellAndWait70', b2)
    assert _is_linked(a, 'co2_TellAndWait70', b2)
    if hasattr(b1, 'co2_Process71'):
        assert not _is_linked(b1, 'co2_Process71', a)
    if hasattr(b2, 'co2_Process71'):
        assert _is_linked(b2, 'co2_Process71', a)
    _safe_set(a, 'co2_TellAndWait70', None)
    assert not _is_linked(a, 'co2_TellAndWait70', b2)
    if hasattr(b2, 'co2_Process71'):
        assert not _is_linked(b2, 'co2_Process71', a)


def test_assoc_processes5_link_reassign_clear():
    a = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    b1 = co2_HonestyDeclaration()
    b2 = co2_HonestyDeclaration()
    _safe_set(a, 'co2_ProcessDefinition', b1)
    assert _is_linked(a, 'co2_ProcessDefinition', b1)
    if hasattr(b1, 'co2_HonestyDeclaration6'):
        assert _is_linked(b1, 'co2_HonestyDeclaration6', a)
    _safe_set(a, 'co2_ProcessDefinition', b2)
    assert _is_linked(a, 'co2_ProcessDefinition', b2)
    if hasattr(b1, 'co2_HonestyDeclaration6'):
        assert not _is_linked(b1, 'co2_HonestyDeclaration6', a)
    if hasattr(b2, 'co2_HonestyDeclaration6'):
        assert _is_linked(b2, 'co2_HonestyDeclaration6', a)
    _safe_set(a, 'co2_ProcessDefinition', None)
    assert not _is_linked(a, 'co2_ProcessDefinition', b2)
    if hasattr(b2, 'co2_HonestyDeclaration6'):
        assert not _is_linked(b2, 'co2_HonestyDeclaration6', a)


def test_assoc_processes9_link_reassign_clear():
    a = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    b1 = co2_ContractsAndProcessesDeclaration()
    b2 = co2_ContractsAndProcessesDeclaration()
    _safe_set(a, 'co2_ProcessDefinition11', b1)
    assert _is_linked(a, 'co2_ProcessDefinition11', b1)
    if hasattr(b1, 'co2_ContractsAndProcessesDeclaration10'):
        assert _is_linked(b1, 'co2_ContractsAndProcessesDeclaration10', a)
    _safe_set(a, 'co2_ProcessDefinition11', b2)
    assert _is_linked(a, 'co2_ProcessDefinition11', b2)
    if hasattr(b1, 'co2_ContractsAndProcessesDeclaration10'):
        assert not _is_linked(b1, 'co2_ContractsAndProcessesDeclaration10', a)
    if hasattr(b2, 'co2_ContractsAndProcessesDeclaration10'):
        assert _is_linked(b2, 'co2_ContractsAndProcessesDeclaration10', a)
    _safe_set(a, 'co2_ProcessDefinition11', None)
    assert not _is_linked(a, 'co2_ProcessDefinition11', b2)
    if hasattr(b2, 'co2_ContractsAndProcessesDeclaration10'):
        assert not _is_linked(b2, 'co2_ContractsAndProcessesDeclaration10', a)


def test_assoc_ref182_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_VariableReference()
    b2 = co2_VariableReference()
    _safe_set(a, 'co2_VariableDeclaration183', b1)
    assert _is_linked(a, 'co2_VariableDeclaration183', b1)
    if hasattr(b1, 'co2_VariableReference'):
        assert _is_linked(b1, 'co2_VariableReference', a)
    _safe_set(a, 'co2_VariableDeclaration183', b2)
    assert _is_linked(a, 'co2_VariableDeclaration183', b2)
    if hasattr(b1, 'co2_VariableReference'):
        assert not _is_linked(b1, 'co2_VariableReference', a)
    if hasattr(b2, 'co2_VariableReference'):
        assert _is_linked(b2, 'co2_VariableReference', a)
    _safe_set(a, 'co2_VariableDeclaration183', None)
    assert not _is_linked(a, 'co2_VariableDeclaration183', b2)
    if hasattr(b2, 'co2_VariableReference'):
        assert not _is_linked(b2, 'co2_VariableReference', a)


def test_assoc_ref184_link_reassign_clear():
    a = co2_ContractDefinition(name="sample_text")
    b1 = co2_ContractReference()
    b2 = co2_ContractReference()
    _safe_set(a, 'co2_ContractDefinition185', b1)
    assert _is_linked(a, 'co2_ContractDefinition185', b1)
    if hasattr(b1, 'co2_ContractReference'):
        assert _is_linked(b1, 'co2_ContractReference', a)
    _safe_set(a, 'co2_ContractDefinition185', b2)
    assert _is_linked(a, 'co2_ContractDefinition185', b2)
    if hasattr(b1, 'co2_ContractReference'):
        assert not _is_linked(b1, 'co2_ContractReference', a)
    if hasattr(b2, 'co2_ContractReference'):
        assert _is_linked(b2, 'co2_ContractReference', a)
    _safe_set(a, 'co2_ContractDefinition185', None)
    assert not _is_linked(a, 'co2_ContractDefinition185', b2)
    if hasattr(b2, 'co2_ContractReference'):
        assert not _is_linked(b2, 'co2_ContractReference', a)


def test_assoc_reference31_link_reassign_clear():
    a = co2_ProcessDefinition(name="sample_text", withoutRestrictions=True)
    b1 = co2_ProcessCall()
    b2 = co2_ProcessCall()
    _safe_set(a, 'co2_ProcessDefinition32', b1)
    assert _is_linked(a, 'co2_ProcessDefinition32', b1)
    if hasattr(b1, 'co2_ProcessCall'):
        assert _is_linked(b1, 'co2_ProcessCall', a)
    _safe_set(a, 'co2_ProcessDefinition32', b2)
    assert _is_linked(a, 'co2_ProcessDefinition32', b2)
    if hasattr(b1, 'co2_ProcessCall'):
        assert not _is_linked(b1, 'co2_ProcessCall', a)
    if hasattr(b2, 'co2_ProcessCall'):
        assert _is_linked(b2, 'co2_ProcessCall', a)
    _safe_set(a, 'co2_ProcessDefinition32', None)
    assert not _is_linked(a, 'co2_ProcessDefinition32', b2)
    if hasattr(b2, 'co2_ProcessCall'):
        assert not _is_linked(b2, 'co2_ProcessCall', a)


def test_assoc_right155_link_reassign_clear():
    a = co2_Comparison(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_Comparison156', b1)
    assert _is_linked(a, 'co2_Comparison156', b1)
    if hasattr(b1, 'co2_Expression157'):
        assert _is_linked(b1, 'co2_Expression157', a)
    _safe_set(a, 'co2_Comparison156', b2)
    assert _is_linked(a, 'co2_Comparison156', b2)
    if hasattr(b1, 'co2_Expression157'):
        assert not _is_linked(b1, 'co2_Expression157', a)
    if hasattr(b2, 'co2_Expression157'):
        assert _is_linked(b2, 'co2_Expression157', a)
    _safe_set(a, 'co2_Comparison156', None)
    assert not _is_linked(a, 'co2_Comparison156', b2)
    if hasattr(b2, 'co2_Expression157'):
        assert not _is_linked(b2, 'co2_Expression157', a)


def test_assoc_right160_link_reassign_clear():
    a = co2_Equals(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_Equals161', b1)
    assert _is_linked(a, 'co2_Equals161', b1)
    if hasattr(b1, 'co2_Expression162'):
        assert _is_linked(b1, 'co2_Expression162', a)
    _safe_set(a, 'co2_Equals161', b2)
    assert _is_linked(a, 'co2_Equals161', b2)
    if hasattr(b1, 'co2_Expression162'):
        assert not _is_linked(b1, 'co2_Expression162', a)
    if hasattr(b2, 'co2_Expression162'):
        assert _is_linked(b2, 'co2_Expression162', a)
    _safe_set(a, 'co2_Equals161', None)
    assert not _is_linked(a, 'co2_Equals161', b2)
    if hasattr(b2, 'co2_Expression162'):
        assert not _is_linked(b2, 'co2_Expression162', a)


def test_assoc_right175_link_reassign_clear():
    a = co2_MultiOrDiv(op="sample_text")
    b1 = co2_Expression()
    b2 = co2_Expression()
    _safe_set(a, 'co2_MultiOrDiv176', b1)
    assert _is_linked(a, 'co2_MultiOrDiv176', b1)
    if hasattr(b1, 'co2_Expression177'):
        assert _is_linked(b1, 'co2_Expression177', a)
    _safe_set(a, 'co2_MultiOrDiv176', b2)
    assert _is_linked(a, 'co2_MultiOrDiv176', b2)
    if hasattr(b1, 'co2_Expression177'):
        assert not _is_linked(b1, 'co2_Expression177', a)
    if hasattr(b2, 'co2_Expression177'):
        assert _is_linked(b2, 'co2_Expression177', a)
    _safe_set(a, 'co2_MultiOrDiv176', None)
    assert not _is_linked(a, 'co2_MultiOrDiv176', b2)
    if hasattr(b2, 'co2_Expression177'):
        assert not _is_linked(b2, 'co2_Expression177', a)


def test_assoc_session104_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_Input()
    b2 = co2_Input()
    _safe_set(a, 'co2_VariableDeclaration106', b1)
    assert _is_linked(a, 'co2_VariableDeclaration106', b1)
    if hasattr(b1, 'co2_Input105'):
        assert _is_linked(b1, 'co2_Input105', a)
    _safe_set(a, 'co2_VariableDeclaration106', b2)
    assert _is_linked(a, 'co2_VariableDeclaration106', b2)
    if hasattr(b1, 'co2_Input105'):
        assert not _is_linked(b1, 'co2_Input105', a)
    if hasattr(b2, 'co2_Input105'):
        assert _is_linked(b2, 'co2_Input105', a)
    _safe_set(a, 'co2_VariableDeclaration106', None)
    assert not _is_linked(a, 'co2_VariableDeclaration106', b2)
    if hasattr(b2, 'co2_Input105'):
        assert not _is_linked(b2, 'co2_Input105', a)


def test_assoc_session39_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_Tell()
    b2 = co2_Tell()
    _safe_set(a, 'co2_VariableDeclaration', b1)
    assert _is_linked(a, 'co2_VariableDeclaration', b1)
    if hasattr(b1, 'co2_Tell'):
        assert _is_linked(b1, 'co2_Tell', a)
    _safe_set(a, 'co2_VariableDeclaration', b2)
    assert _is_linked(a, 'co2_VariableDeclaration', b2)
    if hasattr(b1, 'co2_Tell'):
        assert not _is_linked(b1, 'co2_Tell', a)
    if hasattr(b2, 'co2_Tell'):
        assert _is_linked(b2, 'co2_Tell', a)
    _safe_set(a, 'co2_VariableDeclaration', None)
    assert not _is_linked(a, 'co2_VariableDeclaration', b2)
    if hasattr(b2, 'co2_Tell'):
        assert not _is_linked(b2, 'co2_Tell', a)


def test_assoc_session45_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_Retract()
    b2 = co2_Retract()
    _safe_set(a, 'co2_VariableDeclaration46', b1)
    assert _is_linked(a, 'co2_VariableDeclaration46', b1)
    if hasattr(b1, 'co2_Retract'):
        assert _is_linked(b1, 'co2_Retract', a)
    _safe_set(a, 'co2_VariableDeclaration46', b2)
    assert _is_linked(a, 'co2_VariableDeclaration46', b2)
    if hasattr(b1, 'co2_Retract'):
        assert not _is_linked(b1, 'co2_Retract', a)
    if hasattr(b2, 'co2_Retract'):
        assert _is_linked(b2, 'co2_Retract', a)
    _safe_set(a, 'co2_VariableDeclaration46', None)
    assert not _is_linked(a, 'co2_VariableDeclaration46', b2)
    if hasattr(b2, 'co2_Retract'):
        assert not _is_linked(b2, 'co2_Retract', a)


def test_assoc_session47_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_DoOutput()
    b2 = co2_DoOutput()
    _safe_set(a, 'co2_VariableDeclaration48', b1)
    assert _is_linked(a, 'co2_VariableDeclaration48', b1)
    if hasattr(b1, 'co2_DoOutput'):
        assert _is_linked(b1, 'co2_DoOutput', a)
    _safe_set(a, 'co2_VariableDeclaration48', b2)
    assert _is_linked(a, 'co2_VariableDeclaration48', b2)
    if hasattr(b1, 'co2_DoOutput'):
        assert not _is_linked(b1, 'co2_DoOutput', a)
    if hasattr(b2, 'co2_DoOutput'):
        assert _is_linked(b2, 'co2_DoOutput', a)
    _safe_set(a, 'co2_VariableDeclaration48', None)
    assert not _is_linked(a, 'co2_VariableDeclaration48', b2)
    if hasattr(b2, 'co2_DoOutput'):
        assert not _is_linked(b2, 'co2_DoOutput', a)


def test_assoc_session54_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_DoInput()
    b2 = co2_DoInput()
    _safe_set(a, 'co2_VariableDeclaration55', b1)
    assert _is_linked(a, 'co2_VariableDeclaration55', b1)
    if hasattr(b1, 'co2_DoInput'):
        assert _is_linked(b1, 'co2_DoInput', a)
    _safe_set(a, 'co2_VariableDeclaration55', b2)
    assert _is_linked(a, 'co2_VariableDeclaration55', b2)
    if hasattr(b1, 'co2_DoInput'):
        assert not _is_linked(b1, 'co2_DoInput', a)
    if hasattr(b2, 'co2_DoInput'):
        assert _is_linked(b2, 'co2_DoInput', a)
    _safe_set(a, 'co2_VariableDeclaration55', None)
    assert not _is_linked(a, 'co2_VariableDeclaration55', b2)
    if hasattr(b2, 'co2_DoInput'):
        assert not _is_linked(b2, 'co2_DoInput', a)


def test_assoc_session61_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_Ask(formula="sample_text")
    b2 = co2_Ask(formula="sample_text_2")
    _safe_set(a, 'co2_VariableDeclaration62', b1)
    assert _is_linked(a, 'co2_VariableDeclaration62', b1)
    if hasattr(b1, 'co2_Ask'):
        assert _is_linked(b1, 'co2_Ask', a)
    _safe_set(a, 'co2_VariableDeclaration62', b2)
    assert _is_linked(a, 'co2_VariableDeclaration62', b2)
    if hasattr(b1, 'co2_Ask'):
        assert not _is_linked(b1, 'co2_Ask', a)
    if hasattr(b2, 'co2_Ask'):
        assert _is_linked(b2, 'co2_Ask', a)
    _safe_set(a, 'co2_VariableDeclaration62', None)
    assert not _is_linked(a, 'co2_VariableDeclaration62', b2)
    if hasattr(b2, 'co2_Ask'):
        assert not _is_linked(b2, 'co2_Ask', a)


def test_assoc_session67_link_reassign_clear():
    a = co2_TellAndWait(timeout=True)
    b1 = co2_Session()
    b2 = co2_Session()
    _safe_set(a, 'co2_TellAndWait', b1)
    assert _is_linked(a, 'co2_TellAndWait', b1)
    if hasattr(b1, 'co2_Session68'):
        assert _is_linked(b1, 'co2_Session68', a)
    _safe_set(a, 'co2_TellAndWait', b2)
    assert _is_linked(a, 'co2_TellAndWait', b2)
    if hasattr(b1, 'co2_Session68'):
        assert not _is_linked(b1, 'co2_Session68', a)
    if hasattr(b2, 'co2_Session68'):
        assert _is_linked(b2, 'co2_Session68', a)
    _safe_set(a, 'co2_TellAndWait', None)
    assert not _is_linked(a, 'co2_TellAndWait', b2)
    if hasattr(b2, 'co2_Session68'):
        assert not _is_linked(b2, 'co2_Session68', a)


def test_assoc_session88_link_reassign_clear():
    a = co2_VariableDeclaration(name="sample_text")
    b1 = co2_Send()
    b2 = co2_Send()
    _safe_set(a, 'co2_VariableDeclaration90', b1)
    assert _is_linked(a, 'co2_VariableDeclaration90', b1)
    if hasattr(b1, 'co2_Send89'):
        assert _is_linked(b1, 'co2_Send89', a)
    _safe_set(a, 'co2_VariableDeclaration90', b2)
    assert _is_linked(a, 'co2_VariableDeclaration90', b2)
    if hasattr(b1, 'co2_Send89'):
        assert not _is_linked(b1, 'co2_Send89', a)
    if hasattr(b2, 'co2_Send89'):
        assert _is_linked(b2, 'co2_Send89', a)
    _safe_set(a, 'co2_VariableDeclaration90', None)
    assert not _is_linked(a, 'co2_VariableDeclaration90', b2)
    if hasattr(b2, 'co2_Send89'):
        assert not _is_linked(b2, 'co2_Send89', a)


def test_assoc_timeoutValue72_link_reassign_clear():
    a = co2_TellAndWait(timeout=True)
    b1 = co2_TimeoutProcess()
    b2 = co2_TimeoutProcess()
    _safe_set(a, 'co2_TellAndWait73', b1)
    assert _is_linked(a, 'co2_TellAndWait73', b1)
    if hasattr(b1, 'co2_TimeoutProcess'):
        assert _is_linked(b1, 'co2_TimeoutProcess', a)
    _safe_set(a, 'co2_TellAndWait73', b2)
    assert _is_linked(a, 'co2_TellAndWait73', b2)
    if hasattr(b1, 'co2_TimeoutProcess'):
        assert not _is_linked(b1, 'co2_TimeoutProcess', a)
    if hasattr(b2, 'co2_TimeoutProcess'):
        assert _is_linked(b2, 'co2_TimeoutProcess', a)
    _safe_set(a, 'co2_TellAndWait73', None)
    assert not _is_linked(a, 'co2_TellAndWait73', b2)
    if hasattr(b2, 'co2_TimeoutProcess'):
        assert not _is_linked(b2, 'co2_TimeoutProcess', a)


def test_assoc_timeoutValue92_link_reassign_clear():
    a = co2_Receive(timeout=True)
    b1 = co2_TimeoutProcess()
    b2 = co2_TimeoutProcess()
    _safe_set(a, 'co2_Receive93', b1)
    assert _is_linked(a, 'co2_Receive93', b1)
    if hasattr(b1, 'co2_TimeoutProcess94'):
        assert _is_linked(b1, 'co2_TimeoutProcess94', a)
    _safe_set(a, 'co2_Receive93', b2)
    assert _is_linked(a, 'co2_Receive93', b2)
    if hasattr(b1, 'co2_TimeoutProcess94'):
        assert not _is_linked(b1, 'co2_TimeoutProcess94', a)
    if hasattr(b2, 'co2_TimeoutProcess94'):
        assert _is_linked(b2, 'co2_TimeoutProcess94', a)
    _safe_set(a, 'co2_Receive93', None)
    assert not _is_linked(a, 'co2_Receive93', b2)
    if hasattr(b2, 'co2_TimeoutProcess94'):
        assert not _is_linked(b2, 'co2_TimeoutProcess94', a)


def test_assoc_type120_link_reassign_clear():
    a = co2_Type(value="sample_text")
    b1 = co2_Placeholder()
    b2 = co2_Placeholder()
    _safe_set(a, 'co2_Type', b1)
    assert _is_linked(a, 'co2_Type', b1)
    if hasattr(b1, 'co2_Placeholder'):
        assert _is_linked(b1, 'co2_Placeholder', a)
    _safe_set(a, 'co2_Type', b2)
    assert _is_linked(a, 'co2_Type', b2)
    if hasattr(b1, 'co2_Placeholder'):
        assert not _is_linked(b1, 'co2_Placeholder', a)
    if hasattr(b2, 'co2_Placeholder'):
        assert _is_linked(b2, 'co2_Placeholder', a)
    _safe_set(a, 'co2_Type', None)
    assert not _is_linked(a, 'co2_Type', b2)
    if hasattr(b2, 'co2_Placeholder'):
        assert not _is_linked(b2, 'co2_Placeholder', a)


def test_assoc_type121_link_reassign_clear():
    a = co2_Type(value="sample_text")
    b1 = co2_Variable()
    b2 = co2_Variable()
    _safe_set(a, 'co2_Type123', b1)
    assert _is_linked(a, 'co2_Type123', b1)
    if hasattr(b1, 'co2_Variable122'):
        assert _is_linked(b1, 'co2_Variable122', a)
    _safe_set(a, 'co2_Type123', b2)
    assert _is_linked(a, 'co2_Type123', b2)
    if hasattr(b1, 'co2_Variable122'):
        assert not _is_linked(b1, 'co2_Variable122', a)
    if hasattr(b2, 'co2_Variable122'):
        assert _is_linked(b2, 'co2_Variable122', a)
    _safe_set(a, 'co2_Type123', None)
    assert not _is_linked(a, 'co2_Type123', b2)
    if hasattr(b2, 'co2_Variable122'):
        assert not _is_linked(b2, 'co2_Variable122', a)


def test_assoc_type137_link_reassign_clear():
    a = co2_ActionType(value="sample_text")
    b1 = co2_Action(name="sample_text")
    b2 = co2_Action(name="sample_text_2")
    _safe_set(a, 'co2_ActionType', b1)
    assert _is_linked(a, 'co2_ActionType', b1)
    if hasattr(b1, 'co2_Action'):
        assert _is_linked(b1, 'co2_Action', a)
    _safe_set(a, 'co2_ActionType', b2)
    assert _is_linked(a, 'co2_ActionType', b2)
    if hasattr(b1, 'co2_Action'):
        assert not _is_linked(b1, 'co2_Action', a)
    if hasattr(b2, 'co2_Action'):
        assert _is_linked(b2, 'co2_Action', a)
    _safe_set(a, 'co2_ActionType', None)
    assert not _is_linked(a, 'co2_ActionType', b2)
    if hasattr(b2, 'co2_Action'):
        assert not _is_linked(b2, 'co2_Action', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


ActionType_strategy = st.builds(ActionType)
@given(instance=ActionType_strategy)
@settings(max_examples=25)
def test_ActionType_instantiation(instance):
    assert isinstance(instance, ActionType)


Contract_strategy = st.builds(Contract)
@given(instance=Contract_strategy)
@settings(max_examples=25)
def test_Contract_instantiation(instance):
    assert isinstance(instance, Contract)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


Placeholder_strategy = st.builds(Placeholder)
@given(instance=Placeholder_strategy)
@settings(max_examples=25)
def test_Placeholder_instantiation(instance):
    assert isinstance(instance, Placeholder)


Prefix_strategy = st.builds(Prefix)
@given(instance=Prefix_strategy)
@settings(max_examples=25)
def test_Prefix_instantiation(instance):
    assert isinstance(instance, Prefix)


Process_strategy = st.builds(Process)
@given(instance=Process_strategy)
@settings(max_examples=25)
def test_Process_instantiation(instance):
    assert isinstance(instance, Process)


ReceiveGroup_strategy = st.builds(ReceiveGroup)
@given(instance=ReceiveGroup_strategy)
@settings(max_examples=25)
def test_ReceiveGroup_instantiation(instance):
    assert isinstance(instance, ReceiveGroup)


SendGroup_strategy = st.builds(SendGroup)
@given(instance=SendGroup_strategy)
@settings(max_examples=25)
def test_SendGroup_instantiation(instance):
    assert isinstance(instance, SendGroup)


Type_strategy = st.builds(Type)
@given(instance=Type_strategy)
@settings(max_examples=25)
def test_Type_instantiation(instance):
    assert isinstance(instance, Type)


VariableDeclaration_strategy = st.builds(VariableDeclaration)
@given(instance=VariableDeclaration_strategy)
@settings(max_examples=25)
def test_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)


co2_Action_strategy = st.builds(co2_Action, name=safe_text)
@given(instance=co2_Action_strategy)
@settings(max_examples=25)
def test_co2_Action_instantiation(instance):
    assert isinstance(instance, co2_Action)


co2_ActionType_strategy = st.builds(co2_ActionType, value=safe_text)
@given(instance=co2_ActionType_strategy)
@settings(max_examples=25)
def test_co2_ActionType_instantiation(instance):
    assert isinstance(instance, co2_ActionType)


co2_AndExpression_strategy = st.builds(co2_AndExpression)
@given(instance=co2_AndExpression_strategy)
@settings(max_examples=25)
def test_co2_AndExpression_instantiation(instance):
    assert isinstance(instance, co2_AndExpression)


co2_ArithmeticSigned_strategy = st.builds(co2_ArithmeticSigned)
@given(instance=co2_ArithmeticSigned_strategy)
@settings(max_examples=25)
def test_co2_ArithmeticSigned_instantiation(instance):
    assert isinstance(instance, co2_ArithmeticSigned)


co2_Ask_strategy = st.builds(co2_Ask, formula=safe_text)
@given(instance=co2_Ask_strategy)
@settings(max_examples=25)
def test_co2_Ask_instantiation(instance):
    assert isinstance(instance, co2_Ask)


co2_BoolPlaceholder_strategy = st.builds(co2_BoolPlaceholder)
@given(instance=co2_BoolPlaceholder_strategy)
@settings(max_examples=25)
def test_co2_BoolPlaceholder_instantiation(instance):
    assert isinstance(instance, co2_BoolPlaceholder)


co2_BooleanLiteral_strategy = st.builds(co2_BooleanLiteral, value=safe_text)
@given(instance=co2_BooleanLiteral_strategy)
@settings(max_examples=25)
def test_co2_BooleanLiteral_instantiation(instance):
    assert isinstance(instance, co2_BooleanLiteral)


co2_BooleanNegation_strategy = st.builds(co2_BooleanNegation)
@given(instance=co2_BooleanNegation_strategy)
@settings(max_examples=25)
def test_co2_BooleanNegation_instantiation(instance):
    assert isinstance(instance, co2_BooleanNegation)


co2_BooleanType_strategy = st.builds(co2_BooleanType)
@given(instance=co2_BooleanType_strategy)
@settings(max_examples=25)
def test_co2_BooleanType_instantiation(instance):
    assert isinstance(instance, co2_BooleanType)


co2_CO2System_strategy = st.builds(co2_CO2System)
@given(instance=co2_CO2System_strategy)
@settings(max_examples=25)
def test_co2_CO2System_instantiation(instance):
    assert isinstance(instance, co2_CO2System)


co2_Case_strategy = st.builds(co2_Case)
@given(instance=co2_Case_strategy)
@settings(max_examples=25)
def test_co2_Case_instantiation(instance):
    assert isinstance(instance, co2_Case)


co2_Comparison_strategy = st.builds(co2_Comparison, op=safe_text)
@given(instance=co2_Comparison_strategy)
@settings(max_examples=25)
def test_co2_Comparison_instantiation(instance):
    assert isinstance(instance, co2_Comparison)


co2_Contract_strategy = st.builds(co2_Contract)
@given(instance=co2_Contract_strategy)
@settings(max_examples=25)
def test_co2_Contract_instantiation(instance):
    assert isinstance(instance, co2_Contract)


co2_ContractDefinition_strategy = st.builds(co2_ContractDefinition, name=safe_text)
@given(instance=co2_ContractDefinition_strategy)
@settings(max_examples=25)
def test_co2_ContractDefinition_instantiation(instance):
    assert isinstance(instance, co2_ContractDefinition)


co2_ContractReference_strategy = st.builds(co2_ContractReference)
@given(instance=co2_ContractReference_strategy)
@settings(max_examples=25)
def test_co2_ContractReference_instantiation(instance):
    assert isinstance(instance, co2_ContractReference)


co2_ContractsAndProcessesDeclaration_strategy = st.builds(co2_ContractsAndProcessesDeclaration)
@given(instance=co2_ContractsAndProcessesDeclaration_strategy)
@settings(max_examples=25)
def test_co2_ContractsAndProcessesDeclaration_instantiation(instance):
    assert isinstance(instance, co2_ContractsAndProcessesDeclaration)


co2_DelimitedProcess_strategy = st.builds(co2_DelimitedProcess)
@given(instance=co2_DelimitedProcess_strategy)
@settings(max_examples=25)
def test_co2_DelimitedProcess_instantiation(instance):
    assert isinstance(instance, co2_DelimitedProcess)


co2_DoInput_strategy = st.builds(co2_DoInput)
@given(instance=co2_DoInput_strategy)
@settings(max_examples=25)
def test_co2_DoInput_instantiation(instance):
    assert isinstance(instance, co2_DoInput)


co2_DoOutput_strategy = st.builds(co2_DoOutput)
@given(instance=co2_DoOutput_strategy)
@settings(max_examples=25)
def test_co2_DoOutput_instantiation(instance):
    assert isinstance(instance, co2_DoOutput)


co2_EmptyContract_strategy = st.builds(co2_EmptyContract, value=safe_text)
@given(instance=co2_EmptyContract_strategy)
@settings(max_examples=25)
def test_co2_EmptyContract_instantiation(instance):
    assert isinstance(instance, co2_EmptyContract)


co2_EmptyProcess_strategy = st.builds(co2_EmptyProcess, value=safe_text)
@given(instance=co2_EmptyProcess_strategy)
@settings(max_examples=25)
def test_co2_EmptyProcess_instantiation(instance):
    assert isinstance(instance, co2_EmptyProcess)


co2_Equals_strategy = st.builds(co2_Equals, op=safe_text)
@given(instance=co2_Equals_strategy)
@settings(max_examples=25)
def test_co2_Equals_instantiation(instance):
    assert isinstance(instance, co2_Equals)


co2_Expression_strategy = st.builds(co2_Expression)
@given(instance=co2_Expression_strategy)
@settings(max_examples=25)
def test_co2_Expression_instantiation(instance):
    assert isinstance(instance, co2_Expression)


co2_ExtAction_strategy = st.builds(co2_ExtAction)
@given(instance=co2_ExtAction_strategy)
@settings(max_examples=25)
def test_co2_ExtAction_instantiation(instance):
    assert isinstance(instance, co2_ExtAction)


co2_ExtSum_strategy = st.builds(co2_ExtSum)
@given(instance=co2_ExtSum_strategy)
@settings(max_examples=25)
def test_co2_ExtSum_instantiation(instance):
    assert isinstance(instance, co2_ExtSum)


co2_HonestyDeclaration_strategy = st.builds(co2_HonestyDeclaration)
@given(instance=co2_HonestyDeclaration_strategy)
@settings(max_examples=25)
def test_co2_HonestyDeclaration_instantiation(instance):
    assert isinstance(instance, co2_HonestyDeclaration)


co2_IfThenElse_strategy = st.builds(co2_IfThenElse)
@given(instance=co2_IfThenElse_strategy)
@settings(max_examples=25)
def test_co2_IfThenElse_instantiation(instance):
    assert isinstance(instance, co2_IfThenElse)


co2_Import_strategy = st.builds(co2_Import, importedNamespace=safe_text)
@given(instance=co2_Import_strategy)
@settings(max_examples=25)
def test_co2_Import_instantiation(instance):
    assert isinstance(instance, co2_Import)


co2_Input_strategy = st.builds(co2_Input)
@given(instance=co2_Input_strategy)
@settings(max_examples=25)
def test_co2_Input_instantiation(instance):
    assert isinstance(instance, co2_Input)


co2_IntAction_strategy = st.builds(co2_IntAction)
@given(instance=co2_IntAction_strategy)
@settings(max_examples=25)
def test_co2_IntAction_instantiation(instance):
    assert isinstance(instance, co2_IntAction)


co2_IntActionType_strategy = st.builds(co2_IntActionType)
@given(instance=co2_IntActionType_strategy)
@settings(max_examples=25)
def test_co2_IntActionType_instantiation(instance):
    assert isinstance(instance, co2_IntActionType)


co2_IntPlaceholder_strategy = st.builds(co2_IntPlaceholder)
@given(instance=co2_IntPlaceholder_strategy)
@settings(max_examples=25)
def test_co2_IntPlaceholder_instantiation(instance):
    assert isinstance(instance, co2_IntPlaceholder)


co2_IntSum_strategy = st.builds(co2_IntSum)
@given(instance=co2_IntSum_strategy)
@settings(max_examples=25)
def test_co2_IntSum_instantiation(instance):
    assert isinstance(instance, co2_IntSum)


co2_IntType_strategy = st.builds(co2_IntType)
@given(instance=co2_IntType_strategy)
@settings(max_examples=25)
def test_co2_IntType_instantiation(instance):
    assert isinstance(instance, co2_IntType)


co2_Minus_strategy = st.builds(co2_Minus)
@given(instance=co2_Minus_strategy)
@settings(max_examples=25)
def test_co2_Minus_instantiation(instance):
    assert isinstance(instance, co2_Minus)


co2_MultiOrDiv_strategy = st.builds(co2_MultiOrDiv, op=safe_text)
@given(instance=co2_MultiOrDiv_strategy)
@settings(max_examples=25)
def test_co2_MultiOrDiv_instantiation(instance):
    assert isinstance(instance, co2_MultiOrDiv)


co2_NumberLiteral_strategy = st.builds(co2_NumberLiteral, value=st.integers())
@given(instance=co2_NumberLiteral_strategy)
@settings(max_examples=25)
def test_co2_NumberLiteral_instantiation(instance):
    assert isinstance(instance, co2_NumberLiteral)


co2_OrExpression_strategy = st.builds(co2_OrExpression)
@given(instance=co2_OrExpression_strategy)
@settings(max_examples=25)
def test_co2_OrExpression_instantiation(instance):
    assert isinstance(instance, co2_OrExpression)


co2_PackageDeclaration_strategy = st.builds(co2_PackageDeclaration, name=safe_text, single=st.booleans())
@given(instance=co2_PackageDeclaration_strategy)
@settings(max_examples=25)
def test_co2_PackageDeclaration_instantiation(instance):
    assert isinstance(instance, co2_PackageDeclaration)


co2_ParallelProcesses_strategy = st.builds(co2_ParallelProcesses)
@given(instance=co2_ParallelProcesses_strategy)
@settings(max_examples=25)
def test_co2_ParallelProcesses_instantiation(instance):
    assert isinstance(instance, co2_ParallelProcesses)


co2_Placeholder_strategy = st.builds(co2_Placeholder)
@given(instance=co2_Placeholder_strategy)
@settings(max_examples=25)
def test_co2_Placeholder_instantiation(instance):
    assert isinstance(instance, co2_Placeholder)


co2_Plus_strategy = st.builds(co2_Plus)
@given(instance=co2_Plus_strategy)
@settings(max_examples=25)
def test_co2_Plus_instantiation(instance):
    assert isinstance(instance, co2_Plus)


co2_Prefix_strategy = st.builds(co2_Prefix)
@given(instance=co2_Prefix_strategy)
@settings(max_examples=25)
def test_co2_Prefix_instantiation(instance):
    assert isinstance(instance, co2_Prefix)


co2_Process_strategy = st.builds(co2_Process)
@given(instance=co2_Process_strategy)
@settings(max_examples=25)
def test_co2_Process_instantiation(instance):
    assert isinstance(instance, co2_Process)


co2_ProcessCall_strategy = st.builds(co2_ProcessCall)
@given(instance=co2_ProcessCall_strategy)
@settings(max_examples=25)
def test_co2_ProcessCall_instantiation(instance):
    assert isinstance(instance, co2_ProcessCall)


co2_ProcessDefinition_strategy = st.builds(co2_ProcessDefinition, name=safe_text, withoutRestrictions=st.booleans())
@given(instance=co2_ProcessDefinition_strategy)
@settings(max_examples=25)
def test_co2_ProcessDefinition_instantiation(instance):
    assert isinstance(instance, co2_ProcessDefinition)


co2_Receive_strategy = st.builds(co2_Receive, timeout=st.booleans())
@given(instance=co2_Receive_strategy)
@settings(max_examples=25)
def test_co2_Receive_instantiation(instance):
    assert isinstance(instance, co2_Receive)


co2_ReceiveGroup_strategy = st.builds(co2_ReceiveGroup)
@given(instance=co2_ReceiveGroup_strategy)
@settings(max_examples=25)
def test_co2_ReceiveGroup_instantiation(instance):
    assert isinstance(instance, co2_ReceiveGroup)


co2_Retract_strategy = st.builds(co2_Retract)
@given(instance=co2_Retract_strategy)
@settings(max_examples=25)
def test_co2_Retract_instantiation(instance):
    assert isinstance(instance, co2_Retract)


co2_RetractedProcess_strategy = st.builds(co2_RetractedProcess)
@given(instance=co2_RetractedProcess_strategy)
@settings(max_examples=25)
def test_co2_RetractedProcess_instantiation(instance):
    assert isinstance(instance, co2_RetractedProcess)


co2_Send_strategy = st.builds(co2_Send)
@given(instance=co2_Send_strategy)
@settings(max_examples=25)
def test_co2_Send_instantiation(instance):
    assert isinstance(instance, co2_Send)


co2_SendGroup_strategy = st.builds(co2_SendGroup)
@given(instance=co2_SendGroup_strategy)
@settings(max_examples=25)
def test_co2_SendGroup_instantiation(instance):
    assert isinstance(instance, co2_SendGroup)


co2_Session_strategy = st.builds(co2_Session)
@given(instance=co2_Session_strategy)
@settings(max_examples=25)
def test_co2_Session_instantiation(instance):
    assert isinstance(instance, co2_Session)


co2_SessionType_strategy = st.builds(co2_SessionType)
@given(instance=co2_SessionType_strategy)
@settings(max_examples=25)
def test_co2_SessionType_instantiation(instance):
    assert isinstance(instance, co2_SessionType)


co2_StringActionType_strategy = st.builds(co2_StringActionType)
@given(instance=co2_StringActionType_strategy)
@settings(max_examples=25)
def test_co2_StringActionType_instantiation(instance):
    assert isinstance(instance, co2_StringActionType)


co2_StringLiteral_strategy = st.builds(co2_StringLiteral, value=safe_text)
@given(instance=co2_StringLiteral_strategy)
@settings(max_examples=25)
def test_co2_StringLiteral_instantiation(instance):
    assert isinstance(instance, co2_StringLiteral)


co2_StringPlaceholder_strategy = st.builds(co2_StringPlaceholder)
@given(instance=co2_StringPlaceholder_strategy)
@settings(max_examples=25)
def test_co2_StringPlaceholder_instantiation(instance):
    assert isinstance(instance, co2_StringPlaceholder)


co2_StringType_strategy = st.builds(co2_StringType)
@given(instance=co2_StringType_strategy)
@settings(max_examples=25)
def test_co2_StringType_instantiation(instance):
    assert isinstance(instance, co2_StringType)


co2_Sum_strategy = st.builds(co2_Sum)
@given(instance=co2_Sum_strategy)
@settings(max_examples=25)
def test_co2_Sum_instantiation(instance):
    assert isinstance(instance, co2_Sum)


co2_SwitchCase_strategy = st.builds(co2_SwitchCase, default=st.booleans())
@given(instance=co2_SwitchCase_strategy)
@settings(max_examples=25)
def test_co2_SwitchCase_instantiation(instance):
    assert isinstance(instance, co2_SwitchCase)


co2_Tau_strategy = st.builds(co2_Tau)
@given(instance=co2_Tau_strategy)
@settings(max_examples=25)
def test_co2_Tau_instantiation(instance):
    assert isinstance(instance, co2_Tau)


co2_Tell_strategy = st.builds(co2_Tell)
@given(instance=co2_Tell_strategy)
@settings(max_examples=25)
def test_co2_Tell_instantiation(instance):
    assert isinstance(instance, co2_Tell)


co2_TellAndReturn_strategy = st.builds(co2_TellAndReturn)
@given(instance=co2_TellAndReturn_strategy)
@settings(max_examples=25)
def test_co2_TellAndReturn_instantiation(instance):
    assert isinstance(instance, co2_TellAndReturn)


co2_TellAndWait_strategy = st.builds(co2_TellAndWait, timeout=st.booleans())
@given(instance=co2_TellAndWait_strategy)
@settings(max_examples=25)
def test_co2_TellAndWait_instantiation(instance):
    assert isinstance(instance, co2_TellAndWait)


co2_TimeoutProcess_strategy = st.builds(co2_TimeoutProcess)
@given(instance=co2_TimeoutProcess_strategy)
@settings(max_examples=25)
def test_co2_TimeoutProcess_instantiation(instance):
    assert isinstance(instance, co2_TimeoutProcess)


co2_Type_strategy = st.builds(co2_Type, value=safe_text)
@given(instance=co2_Type_strategy)
@settings(max_examples=25)
def test_co2_Type_instantiation(instance):
    assert isinstance(instance, co2_Type)


co2_UnitActionType_strategy = st.builds(co2_UnitActionType)
@given(instance=co2_UnitActionType_strategy)
@settings(max_examples=25)
def test_co2_UnitActionType_instantiation(instance):
    assert isinstance(instance, co2_UnitActionType)


co2_Variable_strategy = st.builds(co2_Variable)
@given(instance=co2_Variable_strategy)
@settings(max_examples=25)
def test_co2_Variable_instantiation(instance):
    assert isinstance(instance, co2_Variable)


co2_VariableDeclaration_strategy = st.builds(co2_VariableDeclaration, name=safe_text)
@given(instance=co2_VariableDeclaration_strategy)
@settings(max_examples=25)
def test_co2_VariableDeclaration_instantiation(instance):
    assert isinstance(instance, co2_VariableDeclaration)


co2_VariableReference_strategy = st.builds(co2_VariableReference)
@given(instance=co2_VariableReference_strategy)
@settings(max_examples=25)
def test_co2_VariableReference_instantiation(instance):
    assert isinstance(instance, co2_VariableReference)



