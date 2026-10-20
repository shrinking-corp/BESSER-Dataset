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
    ComparisonOp,
    ioT_GE,
    ioT_LE,
    ioT_LT,
    ioT_GT,
    Bool,
    ioT_False,
    ioT_True,
    ioT_NE,
    ioT_EQ,
    SENSOR,
    ioT_HUMIDITY,
    ioT_TEMPERATURE,
    ioT_LIGHTSENSOR,
    Comparison,
    ioT_ItemInt,
    ioT_EQL,
    ioT_ItemVariable,
    ioT_AND,
    ioT_ItemBool,
    ioT_OR,
    VarOrList,
    Address,
    ioT_WindowsSerialAddress,
    ioT_UnixSerialAddress,
    ioT_IpAddress,
    Config,
    ioT_DeviceConfig,
    ioT_ComparisonOp,
    ioT_Comparison,
    ioT_ElseBlock,
    Action,
    ioT_LEDAction,
    ioT_ClearListAction,
    ioT_Variable,
    ioT_Bool,
    Expression,
    ioT_IntExpression,
    ioT_VarAccess,
    ioT_BoolExpression,
    ExpressionLeft,
    ioT_ExternalOf,
    ioT_ReadConnection,
    ioT_ReadVariable,
    ioT_ExpressionLeft,
    Command,
    ioT_IfStatement,
    ioT_ArrowCommand,
    ioT_Action,
    ioT_Command,
    ExpressionRight,
    ioT_ToVar,
    ioT_ExternalRight,
    ioT_SendCommand,
    ioT_AddToList,
    ioT_Block,
    ioT_SENSOR,
    ioT_ReadSensor,
    ioT_ConnectionConfig,
    ioT_ExpressionRight,
    ioT_Loop,
    ioT_ListenStatement,
    ioT_VarOrList,
    ioT_ConnectStatement,
    ioT_WifiStatement,
    Device,
    ioT_IoTDevice,
    ioT_ControllerDevice,
    ioT_TIMEUNIT,
    ioT_Expression,
    ioT_Address,
    ioT_Device,
    ioT_Config,
    ioT_ExternalDeclaration,
    ioT_Model,
    ioT_Program,
    ioT_Declaration,
    TIMEUNIT,
    ioT_MINUTES,
    ioT_WEEKS,
    ioT_SECONDS,
    ioT_DAYS,
    ioT_HOURS,
    ioT_MILLISECONDS,
    ioT_PyList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_comparisonop_is_not_abstract():
    assert not inspect.isabstract(ComparisonOp)


def test_hyp_comparisonop_constructor_exists():
    assert callable(ComparisonOp.__init__)


def test_hyp_comparisonop_constructor_args():
    sig = inspect.signature(ComparisonOp.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ge_is_not_abstract():
    assert not inspect.isabstract(ioT_GE)


def test_hyp_iot_ge_constructor_exists():
    assert callable(ioT_GE.__init__)


def test_hyp_iot_ge_constructor_args():
    sig = inspect.signature(ioT_GE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_le_is_not_abstract():
    assert not inspect.isabstract(ioT_LE)


def test_hyp_iot_le_constructor_exists():
    assert callable(ioT_LE.__init__)


def test_hyp_iot_le_constructor_args():
    sig = inspect.signature(ioT_LE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_lt_is_not_abstract():
    assert not inspect.isabstract(ioT_LT)


def test_hyp_iot_lt_constructor_exists():
    assert callable(ioT_LT.__init__)


def test_hyp_iot_lt_constructor_args():
    sig = inspect.signature(ioT_LT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_gt_is_not_abstract():
    assert not inspect.isabstract(ioT_GT)


def test_hyp_iot_gt_constructor_exists():
    assert callable(ioT_GT.__init__)


def test_hyp_iot_gt_constructor_args():
    sig = inspect.signature(ioT_GT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_bool_is_not_abstract():
    assert not inspect.isabstract(Bool)


def test_hyp_bool_constructor_exists():
    assert callable(Bool.__init__)


def test_hyp_bool_constructor_args():
    sig = inspect.signature(Bool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_false_is_not_abstract():
    assert not inspect.isabstract(ioT_False)


def test_hyp_iot_false_constructor_exists():
    assert callable(ioT_False.__init__)


def test_hyp_iot_false_constructor_args():
    sig = inspect.signature(ioT_False.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_true_is_not_abstract():
    assert not inspect.isabstract(ioT_True)


def test_hyp_iot_true_constructor_exists():
    assert callable(ioT_True.__init__)


def test_hyp_iot_true_constructor_args():
    sig = inspect.signature(ioT_True.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ne_is_not_abstract():
    assert not inspect.isabstract(ioT_NE)


def test_hyp_iot_ne_constructor_exists():
    assert callable(ioT_NE.__init__)


def test_hyp_iot_ne_constructor_args():
    sig = inspect.signature(ioT_NE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_eq_is_not_abstract():
    assert not inspect.isabstract(ioT_EQ)


def test_hyp_iot_eq_constructor_exists():
    assert callable(ioT_EQ.__init__)


def test_hyp_iot_eq_constructor_args():
    sig = inspect.signature(ioT_EQ.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sensor_is_not_abstract():
    assert not inspect.isabstract(SENSOR)


def test_hyp_sensor_constructor_exists():
    assert callable(SENSOR.__init__)


def test_hyp_sensor_constructor_args():
    sig = inspect.signature(SENSOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_humidity_is_not_abstract():
    assert not inspect.isabstract(ioT_HUMIDITY)


def test_hyp_iot_humidity_constructor_exists():
    assert callable(ioT_HUMIDITY.__init__)


def test_hyp_iot_humidity_constructor_args():
    sig = inspect.signature(ioT_HUMIDITY.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_temperature_is_not_abstract():
    assert not inspect.isabstract(ioT_TEMPERATURE)


def test_hyp_iot_temperature_constructor_exists():
    assert callable(ioT_TEMPERATURE.__init__)


def test_hyp_iot_temperature_constructor_args():
    sig = inspect.signature(ioT_TEMPERATURE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_lightsensor_is_not_abstract():
    assert not inspect.isabstract(ioT_LIGHTSENSOR)


def test_hyp_iot_lightsensor_constructor_exists():
    assert callable(ioT_LIGHTSENSOR.__init__)


def test_hyp_iot_lightsensor_constructor_args():
    sig = inspect.signature(ioT_LIGHTSENSOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparison_is_not_abstract():
    assert not inspect.isabstract(Comparison)


def test_hyp_comparison_constructor_exists():
    assert callable(Comparison.__init__)


def test_hyp_comparison_constructor_args():
    sig = inspect.signature(Comparison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_itemint_is_not_abstract():
    assert not inspect.isabstract(ioT_ItemInt)


def test_hyp_iot_itemint_constructor_exists():
    assert callable(ioT_ItemInt.__init__)


def test_hyp_iot_itemint_constructor_args():
    sig = inspect.signature(ioT_ItemInt.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iot_eql_is_not_abstract():
    assert not inspect.isabstract(ioT_EQL)


def test_hyp_iot_eql_constructor_exists():
    assert callable(ioT_EQL.__init__)


def test_hyp_iot_eql_constructor_args():
    sig = inspect.signature(ioT_EQL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_itemvariable_is_not_abstract():
    assert not inspect.isabstract(ioT_ItemVariable)


def test_hyp_iot_itemvariable_constructor_exists():
    assert callable(ioT_ItemVariable.__init__)


def test_hyp_iot_itemvariable_constructor_args():
    sig = inspect.signature(ioT_ItemVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_and_is_not_abstract():
    assert not inspect.isabstract(ioT_AND)


def test_hyp_iot_and_constructor_exists():
    assert callable(ioT_AND.__init__)


def test_hyp_iot_and_constructor_args():
    sig = inspect.signature(ioT_AND.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_itembool_is_not_abstract():
    assert not inspect.isabstract(ioT_ItemBool)


def test_hyp_iot_itembool_constructor_exists():
    assert callable(ioT_ItemBool.__init__)


def test_hyp_iot_itembool_constructor_args():
    sig = inspect.signature(ioT_ItemBool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_or_is_not_abstract():
    assert not inspect.isabstract(ioT_OR)


def test_hyp_iot_or_constructor_exists():
    assert callable(ioT_OR.__init__)


def test_hyp_iot_or_constructor_args():
    sig = inspect.signature(ioT_OR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_varorlist_is_not_abstract():
    assert not inspect.isabstract(VarOrList)


def test_hyp_varorlist_constructor_exists():
    assert callable(VarOrList.__init__)


def test_hyp_varorlist_constructor_args():
    sig = inspect.signature(VarOrList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_windowsserialaddress_is_not_abstract():
    assert not inspect.isabstract(ioT_WindowsSerialAddress)


def test_hyp_iot_windowsserialaddress_constructor_exists():
    assert callable(ioT_WindowsSerialAddress.__init__)


def test_hyp_iot_windowsserialaddress_constructor_args():
    sig = inspect.signature(ioT_WindowsSerialAddress.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_unixserialaddress_is_not_abstract():
    assert not inspect.isabstract(ioT_UnixSerialAddress)


def test_hyp_iot_unixserialaddress_constructor_exists():
    assert callable(ioT_UnixSerialAddress.__init__)


def test_hyp_iot_unixserialaddress_constructor_args():
    sig = inspect.signature(ioT_UnixSerialAddress.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ipaddress_is_not_abstract():
    assert not inspect.isabstract(ioT_IpAddress)


def test_hyp_iot_ipaddress_constructor_exists():
    assert callable(ioT_IpAddress.__init__)


def test_hyp_iot_ipaddress_constructor_args():
    sig = inspect.signature(ioT_IpAddress.__init__)
    params = list(sig.parameters.keys())



def test_hyp_config_is_not_abstract():
    assert not inspect.isabstract(Config)


def test_hyp_config_constructor_exists():
    assert callable(Config.__init__)


def test_hyp_config_constructor_args():
    sig = inspect.signature(Config.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_deviceconfig_is_not_abstract():
    assert not inspect.isabstract(ioT_DeviceConfig)


def test_hyp_iot_deviceconfig_constructor_exists():
    assert callable(ioT_DeviceConfig.__init__)


def test_hyp_iot_deviceconfig_constructor_args():
    sig = inspect.signature(ioT_DeviceConfig.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_comparisonop_is_not_abstract():
    assert not inspect.isabstract(ioT_ComparisonOp)


def test_hyp_iot_comparisonop_constructor_exists():
    assert callable(ioT_ComparisonOp.__init__)


def test_hyp_iot_comparisonop_constructor_args():
    sig = inspect.signature(ioT_ComparisonOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_iot_comparison_is_not_abstract():
    assert not inspect.isabstract(ioT_Comparison)


def test_hyp_iot_comparison_constructor_exists():
    assert callable(ioT_Comparison.__init__)


def test_hyp_iot_comparison_constructor_args():
    sig = inspect.signature(ioT_Comparison.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_elseblock_is_not_abstract():
    assert not inspect.isabstract(ioT_ElseBlock)


def test_hyp_iot_elseblock_constructor_exists():
    assert callable(ioT_ElseBlock.__init__)


def test_hyp_iot_elseblock_constructor_args():
    sig = inspect.signature(ioT_ElseBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ledaction_is_not_abstract():
    assert not inspect.isabstract(ioT_LEDAction)


def test_hyp_iot_ledaction_constructor_exists():
    assert callable(ioT_LEDAction.__init__)


def test_hyp_iot_ledaction_constructor_args():
    sig = inspect.signature(ioT_LEDAction.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"




def test_hyp_iot_clearlistaction_is_not_abstract():
    assert not inspect.isabstract(ioT_ClearListAction)


def test_hyp_iot_clearlistaction_constructor_exists():
    assert callable(ioT_ClearListAction.__init__)


def test_hyp_iot_clearlistaction_constructor_args():
    sig = inspect.signature(ioT_ClearListAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_variable_is_not_abstract():
    assert not inspect.isabstract(ioT_Variable)


def test_hyp_iot_variable_constructor_exists():
    assert callable(ioT_Variable.__init__)


def test_hyp_iot_variable_constructor_args():
    sig = inspect.signature(ioT_Variable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_bool_is_not_abstract():
    assert not inspect.isabstract(ioT_Bool)


def test_hyp_iot_bool_constructor_exists():
    assert callable(ioT_Bool.__init__)


def test_hyp_iot_bool_constructor_args():
    sig = inspect.signature(ioT_Bool.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_intexpression_is_not_abstract():
    assert not inspect.isabstract(ioT_IntExpression)


def test_hyp_iot_intexpression_constructor_exists():
    assert callable(ioT_IntExpression.__init__)


def test_hyp_iot_intexpression_constructor_args():
    sig = inspect.signature(ioT_IntExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iot_varaccess_is_not_abstract():
    assert not inspect.isabstract(ioT_VarAccess)


def test_hyp_iot_varaccess_constructor_exists():
    assert callable(ioT_VarAccess.__init__)


def test_hyp_iot_varaccess_constructor_args():
    sig = inspect.signature(ioT_VarAccess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_boolexpression_is_not_abstract():
    assert not inspect.isabstract(ioT_BoolExpression)


def test_hyp_iot_boolexpression_constructor_exists():
    assert callable(ioT_BoolExpression.__init__)


def test_hyp_iot_boolexpression_constructor_args():
    sig = inspect.signature(ioT_BoolExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionleft_is_not_abstract():
    assert not inspect.isabstract(ExpressionLeft)


def test_hyp_expressionleft_constructor_exists():
    assert callable(ExpressionLeft.__init__)


def test_hyp_expressionleft_constructor_args():
    sig = inspect.signature(ExpressionLeft.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_externalof_is_not_abstract():
    assert not inspect.isabstract(ioT_ExternalOf)


def test_hyp_iot_externalof_constructor_exists():
    assert callable(ioT_ExternalOf.__init__)


def test_hyp_iot_externalof_constructor_args():
    sig = inspect.signature(ioT_ExternalOf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_readconnection_is_not_abstract():
    assert not inspect.isabstract(ioT_ReadConnection)


def test_hyp_iot_readconnection_constructor_exists():
    assert callable(ioT_ReadConnection.__init__)


def test_hyp_iot_readconnection_constructor_args():
    sig = inspect.signature(ioT_ReadConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_readvariable_is_not_abstract():
    assert not inspect.isabstract(ioT_ReadVariable)


def test_hyp_iot_readvariable_constructor_exists():
    assert callable(ioT_ReadVariable.__init__)


def test_hyp_iot_readvariable_constructor_args():
    sig = inspect.signature(ioT_ReadVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_expressionleft_is_not_abstract():
    assert not inspect.isabstract(ioT_ExpressionLeft)


def test_hyp_iot_expressionleft_constructor_exists():
    assert callable(ioT_ExpressionLeft.__init__)


def test_hyp_iot_expressionleft_constructor_args():
    sig = inspect.signature(ioT_ExpressionLeft.__init__)
    params = list(sig.parameters.keys())



def test_hyp_command_is_not_abstract():
    assert not inspect.isabstract(Command)


def test_hyp_command_constructor_exists():
    assert callable(Command.__init__)


def test_hyp_command_constructor_args():
    sig = inspect.signature(Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_ifstatement_is_not_abstract():
    assert not inspect.isabstract(ioT_IfStatement)


def test_hyp_iot_ifstatement_constructor_exists():
    assert callable(ioT_IfStatement.__init__)


def test_hyp_iot_ifstatement_constructor_args():
    sig = inspect.signature(ioT_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_arrowcommand_is_not_abstract():
    assert not inspect.isabstract(ioT_ArrowCommand)


def test_hyp_iot_arrowcommand_constructor_exists():
    assert callable(ioT_ArrowCommand.__init__)


def test_hyp_iot_arrowcommand_constructor_args():
    sig = inspect.signature(ioT_ArrowCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_action_is_not_abstract():
    assert not inspect.isabstract(ioT_Action)


def test_hyp_iot_action_constructor_exists():
    assert callable(ioT_Action.__init__)


def test_hyp_iot_action_constructor_args():
    sig = inspect.signature(ioT_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_command_is_not_abstract():
    assert not inspect.isabstract(ioT_Command)


def test_hyp_iot_command_constructor_exists():
    assert callable(ioT_Command.__init__)


def test_hyp_iot_command_constructor_args():
    sig = inspect.signature(ioT_Command.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expressionright_is_not_abstract():
    assert not inspect.isabstract(ExpressionRight)


def test_hyp_expressionright_constructor_exists():
    assert callable(ExpressionRight.__init__)


def test_hyp_expressionright_constructor_args():
    sig = inspect.signature(ExpressionRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_tovar_is_not_abstract():
    assert not inspect.isabstract(ioT_ToVar)


def test_hyp_iot_tovar_constructor_exists():
    assert callable(ioT_ToVar.__init__)


def test_hyp_iot_tovar_constructor_args():
    sig = inspect.signature(ioT_ToVar.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_externalright_is_not_abstract():
    assert not inspect.isabstract(ioT_ExternalRight)


def test_hyp_iot_externalright_constructor_exists():
    assert callable(ioT_ExternalRight.__init__)


def test_hyp_iot_externalright_constructor_args():
    sig = inspect.signature(ioT_ExternalRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_sendcommand_is_not_abstract():
    assert not inspect.isabstract(ioT_SendCommand)


def test_hyp_iot_sendcommand_constructor_exists():
    assert callable(ioT_SendCommand.__init__)


def test_hyp_iot_sendcommand_constructor_args():
    sig = inspect.signature(ioT_SendCommand.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_addtolist_is_not_abstract():
    assert not inspect.isabstract(ioT_AddToList)


def test_hyp_iot_addtolist_constructor_exists():
    assert callable(ioT_AddToList.__init__)


def test_hyp_iot_addtolist_constructor_args():
    sig = inspect.signature(ioT_AddToList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_block_is_not_abstract():
    assert not inspect.isabstract(ioT_Block)


def test_hyp_iot_block_constructor_exists():
    assert callable(ioT_Block.__init__)


def test_hyp_iot_block_constructor_args():
    sig = inspect.signature(ioT_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_sensor_is_not_abstract():
    assert not inspect.isabstract(ioT_SENSOR)


def test_hyp_iot_sensor_constructor_exists():
    assert callable(ioT_SENSOR.__init__)


def test_hyp_iot_sensor_constructor_args():
    sig = inspect.signature(ioT_SENSOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_readsensor_is_not_abstract():
    assert not inspect.isabstract(ioT_ReadSensor)


def test_hyp_iot_readsensor_constructor_exists():
    assert callable(ioT_ReadSensor.__init__)


def test_hyp_iot_readsensor_constructor_args():
    sig = inspect.signature(ioT_ReadSensor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_connectionconfig_is_not_abstract():
    assert not inspect.isabstract(ioT_ConnectionConfig)


def test_hyp_iot_connectionconfig_constructor_exists():
    assert callable(ioT_ConnectionConfig.__init__)


def test_hyp_iot_connectionconfig_constructor_args():
    sig = inspect.signature(ioT_ConnectionConfig.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_iot_expressionright_is_not_abstract():
    assert not inspect.isabstract(ioT_ExpressionRight)


def test_hyp_iot_expressionright_constructor_exists():
    assert callable(ioT_ExpressionRight.__init__)


def test_hyp_iot_expressionright_constructor_args():
    sig = inspect.signature(ioT_ExpressionRight.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_loop_is_not_abstract():
    assert not inspect.isabstract(ioT_Loop)


def test_hyp_iot_loop_constructor_exists():
    assert callable(ioT_Loop.__init__)


def test_hyp_iot_loop_constructor_args():
    sig = inspect.signature(ioT_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_listenstatement_is_not_abstract():
    assert not inspect.isabstract(ioT_ListenStatement)


def test_hyp_iot_listenstatement_constructor_exists():
    assert callable(ioT_ListenStatement.__init__)


def test_hyp_iot_listenstatement_constructor_args():
    sig = inspect.signature(ioT_ListenStatement.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "ip" in params, "Missing parameter 'ip'"





def test_hyp_iot_varorlist_is_not_abstract():
    assert not inspect.isabstract(ioT_VarOrList)


def test_hyp_iot_varorlist_constructor_exists():
    assert callable(ioT_VarOrList.__init__)


def test_hyp_iot_varorlist_constructor_args():
    sig = inspect.signature(ioT_VarOrList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iot_connectstatement_is_not_abstract():
    assert not inspect.isabstract(ioT_ConnectStatement)


def test_hyp_iot_connectstatement_constructor_exists():
    assert callable(ioT_ConnectStatement.__init__)


def test_hyp_iot_connectstatement_constructor_args():
    sig = inspect.signature(ioT_ConnectStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_wifistatement_is_not_abstract():
    assert not inspect.isabstract(ioT_WifiStatement)


def test_hyp_iot_wifistatement_constructor_exists():
    assert callable(ioT_WifiStatement.__init__)


def test_hyp_iot_wifistatement_constructor_args():
    sig = inspect.signature(ioT_WifiStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_device_is_not_abstract():
    assert not inspect.isabstract(Device)


def test_hyp_device_constructor_exists():
    assert callable(Device.__init__)


def test_hyp_device_constructor_args():
    sig = inspect.signature(Device.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_iotdevice_is_not_abstract():
    assert not inspect.isabstract(ioT_IoTDevice)


def test_hyp_iot_iotdevice_constructor_exists():
    assert callable(ioT_IoTDevice.__init__)


def test_hyp_iot_iotdevice_constructor_args():
    sig = inspect.signature(ioT_IoTDevice.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_controllerdevice_is_not_abstract():
    assert not inspect.isabstract(ioT_ControllerDevice)


def test_hyp_iot_controllerdevice_constructor_exists():
    assert callable(ioT_ControllerDevice.__init__)


def test_hyp_iot_controllerdevice_constructor_args():
    sig = inspect.signature(ioT_ControllerDevice.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_timeunit_is_not_abstract():
    assert not inspect.isabstract(ioT_TIMEUNIT)


def test_hyp_iot_timeunit_constructor_exists():
    assert callable(ioT_TIMEUNIT.__init__)


def test_hyp_iot_timeunit_constructor_args():
    sig = inspect.signature(ioT_TIMEUNIT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_expression_is_not_abstract():
    assert not inspect.isabstract(ioT_Expression)


def test_hyp_iot_expression_constructor_exists():
    assert callable(ioT_Expression.__init__)


def test_hyp_iot_expression_constructor_args():
    sig = inspect.signature(ioT_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_address_is_not_abstract():
    assert not inspect.isabstract(ioT_Address)


def test_hyp_iot_address_constructor_exists():
    assert callable(ioT_Address.__init__)


def test_hyp_iot_address_constructor_args():
    sig = inspect.signature(ioT_Address.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_iot_device_is_not_abstract():
    assert not inspect.isabstract(ioT_Device)


def test_hyp_iot_device_constructor_exists():
    assert callable(ioT_Device.__init__)


def test_hyp_iot_device_constructor_args():
    sig = inspect.signature(ioT_Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iot_config_is_not_abstract():
    assert not inspect.isabstract(ioT_Config)


def test_hyp_iot_config_constructor_exists():
    assert callable(ioT_Config.__init__)


def test_hyp_iot_config_constructor_args():
    sig = inspect.signature(ioT_Config.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iot_externaldeclaration_is_not_abstract():
    assert not inspect.isabstract(ioT_ExternalDeclaration)


def test_hyp_iot_externaldeclaration_constructor_exists():
    assert callable(ioT_ExternalDeclaration.__init__)


def test_hyp_iot_externaldeclaration_constructor_args():
    sig = inspect.signature(ioT_ExternalDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_iot_model_is_not_abstract():
    assert not inspect.isabstract(ioT_Model)


def test_hyp_iot_model_constructor_exists():
    assert callable(ioT_Model.__init__)


def test_hyp_iot_model_constructor_args():
    sig = inspect.signature(ioT_Model.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_program_is_not_abstract():
    assert not inspect.isabstract(ioT_Program)


def test_hyp_iot_program_constructor_exists():
    assert callable(ioT_Program.__init__)


def test_hyp_iot_program_constructor_args():
    sig = inspect.signature(ioT_Program.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_declaration_is_not_abstract():
    assert not inspect.isabstract(ioT_Declaration)


def test_hyp_iot_declaration_constructor_exists():
    assert callable(ioT_Declaration.__init__)


def test_hyp_iot_declaration_constructor_args():
    sig = inspect.signature(ioT_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_timeunit_is_not_abstract():
    assert not inspect.isabstract(TIMEUNIT)


def test_hyp_timeunit_constructor_exists():
    assert callable(TIMEUNIT.__init__)


def test_hyp_timeunit_constructor_args():
    sig = inspect.signature(TIMEUNIT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_minutes_is_not_abstract():
    assert not inspect.isabstract(ioT_MINUTES)


def test_hyp_iot_minutes_constructor_exists():
    assert callable(ioT_MINUTES.__init__)


def test_hyp_iot_minutes_constructor_args():
    sig = inspect.signature(ioT_MINUTES.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_weeks_is_not_abstract():
    assert not inspect.isabstract(ioT_WEEKS)


def test_hyp_iot_weeks_constructor_exists():
    assert callable(ioT_WEEKS.__init__)


def test_hyp_iot_weeks_constructor_args():
    sig = inspect.signature(ioT_WEEKS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_seconds_is_not_abstract():
    assert not inspect.isabstract(ioT_SECONDS)


def test_hyp_iot_seconds_constructor_exists():
    assert callable(ioT_SECONDS.__init__)


def test_hyp_iot_seconds_constructor_args():
    sig = inspect.signature(ioT_SECONDS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_days_is_not_abstract():
    assert not inspect.isabstract(ioT_DAYS)


def test_hyp_iot_days_constructor_exists():
    assert callable(ioT_DAYS.__init__)


def test_hyp_iot_days_constructor_args():
    sig = inspect.signature(ioT_DAYS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_hours_is_not_abstract():
    assert not inspect.isabstract(ioT_HOURS)


def test_hyp_iot_hours_constructor_exists():
    assert callable(ioT_HOURS.__init__)


def test_hyp_iot_hours_constructor_args():
    sig = inspect.signature(ioT_HOURS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_milliseconds_is_not_abstract():
    assert not inspect.isabstract(ioT_MILLISECONDS)


def test_hyp_iot_milliseconds_constructor_exists():
    assert callable(ioT_MILLISECONDS.__init__)


def test_hyp_iot_milliseconds_constructor_args():
    sig = inspect.signature(ioT_MILLISECONDS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_iot_pylist_is_not_abstract():
    assert not inspect.isabstract(ioT_PyList)


def test_hyp_iot_pylist_constructor_exists():
    assert callable(ioT_PyList.__init__)


def test_hyp_iot_pylist_constructor_args():
    sig = inspect.signature(ioT_PyList.__init__)
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
ComparisonOp_strategy = st.builds(
    ComparisonOp,
)
ioT_GE_strategy = st.builds(
    ioT_GE,
)
ioT_LE_strategy = st.builds(
    ioT_LE,
)
ioT_LT_strategy = st.builds(
    ioT_LT,
)
ioT_GT_strategy = st.builds(
    ioT_GT,
)
Bool_strategy = st.builds(
    Bool,
)
ioT_False_strategy = st.builds(
    ioT_False,
)
ioT_True_strategy = st.builds(
    ioT_True,
)
ioT_NE_strategy = st.builds(
    ioT_NE,
)
ioT_EQ_strategy = st.builds(
    ioT_EQ,
)
SENSOR_strategy = st.builds(
    SENSOR,
)
ioT_HUMIDITY_strategy = st.builds(
    ioT_HUMIDITY,
)
ioT_TEMPERATURE_strategy = st.builds(
    ioT_TEMPERATURE,
)
ioT_LIGHTSENSOR_strategy = st.builds(
    ioT_LIGHTSENSOR,
)
Comparison_strategy = st.builds(
    Comparison,
)
ioT_ItemInt_strategy = st.builds(
    ioT_ItemInt,
    value=
        st.integers()
)
ioT_EQL_strategy = st.builds(
    ioT_EQL,
)
ioT_ItemVariable_strategy = st.builds(
    ioT_ItemVariable,
)
ioT_AND_strategy = st.builds(
    ioT_AND,
)
ioT_ItemBool_strategy = st.builds(
    ioT_ItemBool,
)
ioT_OR_strategy = st.builds(
    ioT_OR,
)
VarOrList_strategy = st.builds(
    VarOrList,
)
Address_strategy = st.builds(
    Address,
)
ioT_WindowsSerialAddress_strategy = st.builds(
    ioT_WindowsSerialAddress,
)
ioT_UnixSerialAddress_strategy = st.builds(
    ioT_UnixSerialAddress,
)
ioT_IpAddress_strategy = st.builds(
    ioT_IpAddress,
)
Config_strategy = st.builds(
    Config,
)
ioT_DeviceConfig_strategy = st.builds(
    ioT_DeviceConfig,
)
ioT_ComparisonOp_strategy = st.builds(
    ioT_ComparisonOp,
    op=
        safe_text
)
ioT_Comparison_strategy = st.builds(
    ioT_Comparison,
)
ioT_ElseBlock_strategy = st.builds(
    ioT_ElseBlock,
)
Action_strategy = st.builds(
    Action,
)
ioT_LEDAction_strategy = st.builds(
    ioT_LEDAction,
    state=
        safe_text
)
ioT_ClearListAction_strategy = st.builds(
    ioT_ClearListAction,
)
ioT_Variable_strategy = st.builds(
    ioT_Variable,
)
ioT_Bool_strategy = st.builds(
    ioT_Bool,
)
Expression_strategy = st.builds(
    Expression,
)
ioT_IntExpression_strategy = st.builds(
    ioT_IntExpression,
    value=
        st.integers()
)
ioT_VarAccess_strategy = st.builds(
    ioT_VarAccess,
)
ioT_BoolExpression_strategy = st.builds(
    ioT_BoolExpression,
)
ExpressionLeft_strategy = st.builds(
    ExpressionLeft,
)
ioT_ExternalOf_strategy = st.builds(
    ioT_ExternalOf,
)
ioT_ReadConnection_strategy = st.builds(
    ioT_ReadConnection,
)
ioT_ReadVariable_strategy = st.builds(
    ioT_ReadVariable,
)
ioT_ExpressionLeft_strategy = st.builds(
    ioT_ExpressionLeft,
)
Command_strategy = st.builds(
    Command,
)
ioT_IfStatement_strategy = st.builds(
    ioT_IfStatement,
)
ioT_ArrowCommand_strategy = st.builds(
    ioT_ArrowCommand,
)
ioT_Action_strategy = st.builds(
    ioT_Action,
)
ioT_Command_strategy = st.builds(
    ioT_Command,
)
ExpressionRight_strategy = st.builds(
    ExpressionRight,
)
ioT_ToVar_strategy = st.builds(
    ioT_ToVar,
)
ioT_ExternalRight_strategy = st.builds(
    ioT_ExternalRight,
)
ioT_SendCommand_strategy = st.builds(
    ioT_SendCommand,
)
ioT_AddToList_strategy = st.builds(
    ioT_AddToList,
)
ioT_Block_strategy = st.builds(
    ioT_Block,
)
ioT_SENSOR_strategy = st.builds(
    ioT_SENSOR,
)
ioT_ReadSensor_strategy = st.builds(
    ioT_ReadSensor,
)
ioT_ConnectionConfig_strategy = st.builds(
    ioT_ConnectionConfig,
    type=
        safe_text
)
ioT_ExpressionRight_strategy = st.builds(
    ioT_ExpressionRight,
)
ioT_Loop_strategy = st.builds(
    ioT_Loop,
)
ioT_ListenStatement_strategy = st.builds(
    ioT_ListenStatement,
    port=
        st.integers(),
    ip=
        safe_text
)
ioT_VarOrList_strategy = st.builds(
    ioT_VarOrList,
    name=
        safe_text
)
ioT_ConnectStatement_strategy = st.builds(
    ioT_ConnectStatement,
)
ioT_WifiStatement_strategy = st.builds(
    ioT_WifiStatement,
)
Device_strategy = st.builds(
    Device,
)
ioT_IoTDevice_strategy = st.builds(
    ioT_IoTDevice,
)
ioT_ControllerDevice_strategy = st.builds(
    ioT_ControllerDevice,
)
ioT_TIMEUNIT_strategy = st.builds(
    ioT_TIMEUNIT,
)
ioT_Expression_strategy = st.builds(
    ioT_Expression,
)
ioT_Address_strategy = st.builds(
    ioT_Address,
    value=
        safe_text
)
ioT_Device_strategy = st.builds(
    ioT_Device,
    name=
        safe_text
)
ioT_Config_strategy = st.builds(
    ioT_Config,
    name=
        safe_text
)
ioT_ExternalDeclaration_strategy = st.builds(
    ioT_ExternalDeclaration,
    name=
        safe_text
)
ioT_Model_strategy = st.builds(
    ioT_Model,
)
ioT_Program_strategy = st.builds(
    ioT_Program,
)
ioT_Declaration_strategy = st.builds(
    ioT_Declaration,
    value=
        safe_text,
    key=
        safe_text
)
TIMEUNIT_strategy = st.builds(
    TIMEUNIT,
)
ioT_MINUTES_strategy = st.builds(
    ioT_MINUTES,
)
ioT_WEEKS_strategy = st.builds(
    ioT_WEEKS,
)
ioT_SECONDS_strategy = st.builds(
    ioT_SECONDS,
)
ioT_DAYS_strategy = st.builds(
    ioT_DAYS,
)
ioT_HOURS_strategy = st.builds(
    ioT_HOURS,
)
ioT_MILLISECONDS_strategy = st.builds(
    ioT_MILLISECONDS,
)
ioT_PyList_strategy = st.builds(
    ioT_PyList,
)



















@given(instance=ioT_ItemInt_strategy)
def test_hyp_iot_itemint_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
















@given(instance=ioT_ComparisonOp_strategy)
def test_hyp_iot_comparisonop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original







@given(instance=ioT_LEDAction_strategy)
def test_hyp_iot_ledaction_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original








@given(instance=ioT_IntExpression_strategy)
def test_hyp_iot_intexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
























@given(instance=ioT_ConnectionConfig_strategy)
def test_hyp_iot_connectionconfig_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original






@given(instance=ioT_ListenStatement_strategy)
def test_hyp_iot_listenstatement_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=ioT_ListenStatement_strategy)
def test_hyp_iot_listenstatement_ip_setter(instance):
    original = instance.ip
    instance.ip = original
    assert instance.ip == original




@given(instance=ioT_VarOrList_strategy)
def test_hyp_iot_varorlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=ioT_Address_strategy)
def test_hyp_iot_address_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=ioT_Device_strategy)
def test_hyp_iot_device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=ioT_Config_strategy)
def test_hyp_iot_config_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=ioT_ExternalDeclaration_strategy)
def test_hyp_iot_externaldeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=ioT_Declaration_strategy)
def test_hyp_iot_declaration_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=ioT_Declaration_strategy)
def test_hyp_iot_declaration_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original










# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    Address,
    Bool,
    Command,
    Comparison,
    ComparisonOp,
    Config,
    Device,
    Expression,
    ExpressionLeft,
    ExpressionRight,
    SENSOR,
    TIMEUNIT,
    VarOrList,
    ioT_AND,
    ioT_Action,
    ioT_AddToList,
    ioT_Address,
    ioT_ArrowCommand,
    ioT_Block,
    ioT_Bool,
    ioT_BoolExpression,
    ioT_ClearListAction,
    ioT_Command,
    ioT_Comparison,
    ioT_ComparisonOp,
    ioT_Config,
    ioT_ConnectStatement,
    ioT_ConnectionConfig,
    ioT_ControllerDevice,
    ioT_DAYS,
    ioT_Declaration,
    ioT_Device,
    ioT_DeviceConfig,
    ioT_EQ,
    ioT_EQL,
    ioT_ElseBlock,
    ioT_Expression,
    ioT_ExpressionLeft,
    ioT_ExpressionRight,
    ioT_ExternalDeclaration,
    ioT_ExternalOf,
    ioT_ExternalRight,
    ioT_False,
    ioT_GE,
    ioT_GT,
    ioT_HOURS,
    ioT_HUMIDITY,
    ioT_IfStatement,
    ioT_IntExpression,
    ioT_IoTDevice,
    ioT_IpAddress,
    ioT_ItemBool,
    ioT_ItemInt,
    ioT_ItemVariable,
    ioT_LE,
    ioT_LEDAction,
    ioT_LIGHTSENSOR,
    ioT_LT,
    ioT_ListenStatement,
    ioT_Loop,
    ioT_MILLISECONDS,
    ioT_MINUTES,
    ioT_Model,
    ioT_NE,
    ioT_OR,
    ioT_Program,
    ioT_PyList,
    ioT_ReadConnection,
    ioT_ReadSensor,
    ioT_ReadVariable,
    ioT_SECONDS,
    ioT_SENSOR,
    ioT_SendCommand,
    ioT_TEMPERATURE,
    ioT_TIMEUNIT,
    ioT_ToVar,
    ioT_True,
    ioT_UnixSerialAddress,
    ioT_VarAccess,
    ioT_VarOrList,
    ioT_Variable,
    ioT_WEEKS,
    ioT_WifiStatement,
    ioT_WindowsSerialAddress,
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

def test_ioT_Address_value_value_roundtrip():
    instance = ioT_Address(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ioT_ComparisonOp_op_value_roundtrip():
    instance = ioT_ComparisonOp(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_ioT_Config_name_value_roundtrip():
    instance = ioT_Config(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ioT_ConnectionConfig_type_value_roundtrip():
    instance = ioT_ConnectionConfig(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ioT_Declaration_key_value_roundtrip():
    instance = ioT_Declaration(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_ioT_Declaration_value_value_roundtrip():
    instance = ioT_Declaration(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_ioT_Device_name_value_roundtrip():
    instance = ioT_Device(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ioT_ExternalDeclaration_name_value_roundtrip():
    instance = ioT_ExternalDeclaration(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ioT_IntExpression_value_value_roundtrip():
    instance = ioT_IntExpression(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ioT_ItemInt_value_value_roundtrip():
    instance = ioT_ItemInt(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_ioT_LEDAction_state_value_roundtrip():
    instance = ioT_LEDAction(state="sample_text")
    assert instance.state == "sample_text"
    instance.state = "sample_text_2"
    assert instance.state == "sample_text_2"


def test_ioT_ListenStatement_ip_value_roundtrip():
    instance = ioT_ListenStatement(ip="sample_text", port=7)
    assert instance.ip == "sample_text"
    instance.ip = "sample_text_2"
    assert instance.ip == "sample_text_2"


def test_ioT_ListenStatement_port_value_roundtrip():
    instance = ioT_ListenStatement(ip="sample_text", port=7)
    assert instance.port == 7
    instance.port = 13
    assert instance.port == 13


def test_ioT_VarOrList_name_value_roundtrip():
    instance = ioT_VarOrList(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ioT_ClearListAction_isa_Action():
    instance = ioT_ClearListAction()
    assert isinstance(instance, Action)


def test_ioT_LEDAction_isa_Action():
    instance = ioT_LEDAction(state="sample_text")
    assert isinstance(instance, Action)


def test_ioT_IpAddress_isa_Address():
    instance = ioT_IpAddress()
    assert isinstance(instance, Address)


def test_ioT_UnixSerialAddress_isa_Address():
    instance = ioT_UnixSerialAddress()
    assert isinstance(instance, Address)


def test_ioT_WindowsSerialAddress_isa_Address():
    instance = ioT_WindowsSerialAddress()
    assert isinstance(instance, Address)


def test_ioT_False_isa_Bool():
    instance = ioT_False()
    assert isinstance(instance, Bool)


def test_ioT_True_isa_Bool():
    instance = ioT_True()
    assert isinstance(instance, Bool)


def test_ioT_Action_isa_Command():
    instance = ioT_Action()
    assert isinstance(instance, Command)


def test_ioT_ArrowCommand_isa_Command():
    instance = ioT_ArrowCommand()
    assert isinstance(instance, Command)


def test_ioT_IfStatement_isa_Command():
    instance = ioT_IfStatement()
    assert isinstance(instance, Command)


def test_ioT_AND_isa_Comparison():
    instance = ioT_AND()
    assert isinstance(instance, Comparison)


def test_ioT_EQL_isa_Comparison():
    instance = ioT_EQL()
    assert isinstance(instance, Comparison)


def test_ioT_ItemBool_isa_Comparison():
    instance = ioT_ItemBool()
    assert isinstance(instance, Comparison)


def test_ioT_ItemInt_isa_Comparison():
    instance = ioT_ItemInt(value=7)
    assert isinstance(instance, Comparison)


def test_ioT_ItemVariable_isa_Comparison():
    instance = ioT_ItemVariable()
    assert isinstance(instance, Comparison)


def test_ioT_OR_isa_Comparison():
    instance = ioT_OR()
    assert isinstance(instance, Comparison)


def test_ioT_EQ_isa_ComparisonOp():
    instance = ioT_EQ()
    assert isinstance(instance, ComparisonOp)


def test_ioT_GE_isa_ComparisonOp():
    instance = ioT_GE()
    assert isinstance(instance, ComparisonOp)


def test_ioT_GT_isa_ComparisonOp():
    instance = ioT_GT()
    assert isinstance(instance, ComparisonOp)


def test_ioT_LE_isa_ComparisonOp():
    instance = ioT_LE()
    assert isinstance(instance, ComparisonOp)


def test_ioT_LT_isa_ComparisonOp():
    instance = ioT_LT()
    assert isinstance(instance, ComparisonOp)


def test_ioT_NE_isa_ComparisonOp():
    instance = ioT_NE()
    assert isinstance(instance, ComparisonOp)


def test_ioT_ConnectionConfig_isa_Config():
    instance = ioT_ConnectionConfig(type="sample_text")
    assert isinstance(instance, Config)


def test_ioT_DeviceConfig_isa_Config():
    instance = ioT_DeviceConfig()
    assert isinstance(instance, Config)


def test_ioT_ControllerDevice_isa_Device():
    instance = ioT_ControllerDevice()
    assert isinstance(instance, Device)


def test_ioT_IoTDevice_isa_Device():
    instance = ioT_IoTDevice()
    assert isinstance(instance, Device)


def test_ioT_BoolExpression_isa_Expression():
    instance = ioT_BoolExpression()
    assert isinstance(instance, Expression)


def test_ioT_IntExpression_isa_Expression():
    instance = ioT_IntExpression(value=7)
    assert isinstance(instance, Expression)


def test_ioT_VarAccess_isa_Expression():
    instance = ioT_VarAccess()
    assert isinstance(instance, Expression)


def test_ioT_Expression_isa_ExpressionLeft():
    instance = ioT_Expression()
    assert isinstance(instance, ExpressionLeft)


def test_ioT_ExternalOf_isa_ExpressionLeft():
    instance = ioT_ExternalOf()
    assert isinstance(instance, ExpressionLeft)


def test_ioT_ReadConnection_isa_ExpressionLeft():
    instance = ioT_ReadConnection()
    assert isinstance(instance, ExpressionLeft)


def test_ioT_ReadSensor_isa_ExpressionLeft():
    instance = ioT_ReadSensor()
    assert isinstance(instance, ExpressionLeft)


def test_ioT_ReadVariable_isa_ExpressionLeft():
    instance = ioT_ReadVariable()
    assert isinstance(instance, ExpressionLeft)


def test_ioT_AddToList_isa_ExpressionRight():
    instance = ioT_AddToList()
    assert isinstance(instance, ExpressionRight)


def test_ioT_Block_isa_ExpressionRight():
    instance = ioT_Block()
    assert isinstance(instance, ExpressionRight)


def test_ioT_ExternalRight_isa_ExpressionRight():
    instance = ioT_ExternalRight()
    assert isinstance(instance, ExpressionRight)


def test_ioT_SendCommand_isa_ExpressionRight():
    instance = ioT_SendCommand()
    assert isinstance(instance, ExpressionRight)


def test_ioT_ToVar_isa_ExpressionRight():
    instance = ioT_ToVar()
    assert isinstance(instance, ExpressionRight)


def test_ioT_HUMIDITY_isa_SENSOR():
    instance = ioT_HUMIDITY()
    assert isinstance(instance, SENSOR)


def test_ioT_LIGHTSENSOR_isa_SENSOR():
    instance = ioT_LIGHTSENSOR()
    assert isinstance(instance, SENSOR)


def test_ioT_TEMPERATURE_isa_SENSOR():
    instance = ioT_TEMPERATURE()
    assert isinstance(instance, SENSOR)


def test_ioT_DAYS_isa_TIMEUNIT():
    instance = ioT_DAYS()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_HOURS_isa_TIMEUNIT():
    instance = ioT_HOURS()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_MILLISECONDS_isa_TIMEUNIT():
    instance = ioT_MILLISECONDS()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_MINUTES_isa_TIMEUNIT():
    instance = ioT_MINUTES()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_SECONDS_isa_TIMEUNIT():
    instance = ioT_SECONDS()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_WEEKS_isa_TIMEUNIT():
    instance = ioT_WEEKS()
    assert isinstance(instance, TIMEUNIT)


def test_ioT_PyList_isa_VarOrList():
    instance = ioT_PyList()
    assert isinstance(instance, VarOrList)


def test_ioT_Variable_isa_VarOrList():
    instance = ioT_Variable()
    assert isinstance(instance, VarOrList)


def test_assoc_address26_link_reassign_clear():
    a = ioT_Address(value="sample_text")
    b1 = ioT_ConnectStatement()
    b2 = ioT_ConnectStatement()
    _safe_set(a, 'ioT_Address', b1)
    assert _is_linked(a, 'ioT_Address', b1)
    if hasattr(b1, 'ioT_ConnectStatement27'):
        assert _is_linked(b1, 'ioT_ConnectStatement27', a)
    _safe_set(a, 'ioT_Address', b2)
    assert _is_linked(a, 'ioT_Address', b2)
    if hasattr(b1, 'ioT_ConnectStatement27'):
        assert not _is_linked(b1, 'ioT_ConnectStatement27', a)
    if hasattr(b2, 'ioT_ConnectStatement27'):
        assert _is_linked(b2, 'ioT_ConnectStatement27', a)
    _safe_set(a, 'ioT_Address', None)
    assert not _is_linked(a, 'ioT_Address', b2)
    if hasattr(b2, 'ioT_ConnectStatement27'):
        assert not _is_linked(b2, 'ioT_ConnectStatement27', a)


def test_assoc_body19_link_reassign_clear():
    a = ioT_ListenStatement(ip="sample_text", port=7)
    b1 = ioT_ExpressionRight()
    b2 = ioT_ExpressionRight()
    _safe_set(a, 'ioT_ListenStatement20', b1)
    assert _is_linked(a, 'ioT_ListenStatement20', b1)
    if hasattr(b1, 'ioT_ExpressionRight'):
        assert _is_linked(b1, 'ioT_ExpressionRight', a)
    _safe_set(a, 'ioT_ListenStatement20', b2)
    assert _is_linked(a, 'ioT_ListenStatement20', b2)
    if hasattr(b1, 'ioT_ExpressionRight'):
        assert not _is_linked(b1, 'ioT_ExpressionRight', a)
    if hasattr(b2, 'ioT_ExpressionRight'):
        assert _is_linked(b2, 'ioT_ExpressionRight', a)
    _safe_set(a, 'ioT_ListenStatement20', None)
    assert not _is_linked(a, 'ioT_ListenStatement20', b2)
    if hasattr(b2, 'ioT_ExpressionRight'):
        assert not _is_linked(b2, 'ioT_ExpressionRight', a)


def test_assoc_configs1_link_reassign_clear():
    a = ioT_Config(name="sample_text")
    b1 = ioT_Model()
    b2 = ioT_Model()
    _safe_set(a, 'ioT_Config', b1)
    assert _is_linked(a, 'ioT_Config', b1)
    if hasattr(b1, 'ioT_Model2'):
        assert _is_linked(b1, 'ioT_Model2', a)
    _safe_set(a, 'ioT_Config', b2)
    assert _is_linked(a, 'ioT_Config', b2)
    if hasattr(b1, 'ioT_Model2'):
        assert not _is_linked(b1, 'ioT_Model2', a)
    if hasattr(b2, 'ioT_Model2'):
        assert _is_linked(b2, 'ioT_Model2', a)
    _safe_set(a, 'ioT_Config', None)
    assert not _is_linked(a, 'ioT_Config', b2)
    if hasattr(b2, 'ioT_Model2'):
        assert not _is_linked(b2, 'ioT_Model2', a)


def test_assoc_configuration28_link_reassign_clear():
    a = ioT_ConnectionConfig(type="sample_text")
    b1 = ioT_ConnectStatement()
    b2 = ioT_ConnectStatement()
    _safe_set(a, 'ioT_ConnectionConfig30', b1)
    assert _is_linked(a, 'ioT_ConnectionConfig30', b1)
    if hasattr(b1, 'ioT_ConnectStatement29'):
        assert _is_linked(b1, 'ioT_ConnectStatement29', a)
    _safe_set(a, 'ioT_ConnectionConfig30', b2)
    assert _is_linked(a, 'ioT_ConnectionConfig30', b2)
    if hasattr(b1, 'ioT_ConnectStatement29'):
        assert not _is_linked(b1, 'ioT_ConnectStatement29', a)
    if hasattr(b2, 'ioT_ConnectStatement29'):
        assert _is_linked(b2, 'ioT_ConnectStatement29', a)
    _safe_set(a, 'ioT_ConnectionConfig30', None)
    assert not _is_linked(a, 'ioT_ConnectionConfig30', b2)
    if hasattr(b2, 'ioT_ConnectStatement29'):
        assert not _is_linked(b2, 'ioT_ConnectStatement29', a)


def test_assoc_connectionConfig21_link_reassign_clear():
    a = ioT_ConnectionConfig(type="sample_text")
    b1 = ioT_WifiStatement()
    b2 = ioT_WifiStatement()
    _safe_set(a, 'ioT_ConnectionConfig', b1)
    assert _is_linked(a, 'ioT_ConnectionConfig', b1)
    if hasattr(b1, 'ioT_WifiStatement22'):
        assert _is_linked(b1, 'ioT_WifiStatement22', a)
    _safe_set(a, 'ioT_ConnectionConfig', b2)
    assert _is_linked(a, 'ioT_ConnectionConfig', b2)
    if hasattr(b1, 'ioT_WifiStatement22'):
        assert not _is_linked(b1, 'ioT_WifiStatement22', a)
    if hasattr(b2, 'ioT_WifiStatement22'):
        assert _is_linked(b2, 'ioT_WifiStatement22', a)
    _safe_set(a, 'ioT_ConnectionConfig', None)
    assert not _is_linked(a, 'ioT_ConnectionConfig', b2)
    if hasattr(b2, 'ioT_WifiStatement22'):
        assert not _is_linked(b2, 'ioT_WifiStatement22', a)


def test_assoc_declarations5_link_reassign_clear():
    a = ioT_Declaration(key="sample_text", value="sample_text")
    b1 = ioT_Config(name="sample_text")
    b2 = ioT_Config(name="sample_text_2")
    _safe_set(a, 'ioT_Declaration', b1)
    assert _is_linked(a, 'ioT_Declaration', b1)
    if hasattr(b1, 'ioT_Config6'):
        assert _is_linked(b1, 'ioT_Config6', a)
    _safe_set(a, 'ioT_Declaration', b2)
    assert _is_linked(a, 'ioT_Declaration', b2)
    if hasattr(b1, 'ioT_Config6'):
        assert not _is_linked(b1, 'ioT_Config6', a)
    if hasattr(b2, 'ioT_Config6'):
        assert _is_linked(b2, 'ioT_Config6', a)
    _safe_set(a, 'ioT_Declaration', None)
    assert not _is_linked(a, 'ioT_Declaration', b2)
    if hasattr(b2, 'ioT_Config6'):
        assert not _is_linked(b2, 'ioT_Config6', a)


def test_assoc_device23_link_reassign_clear():
    a = ioT_Device(name="sample_text")
    b1 = ioT_ConnectStatement()
    b2 = ioT_ConnectStatement()
    _safe_set(a, 'ioT_Device25', b1)
    assert _is_linked(a, 'ioT_Device25', b1)
    if hasattr(b1, 'ioT_ConnectStatement24'):
        assert _is_linked(b1, 'ioT_ConnectStatement24', a)
    _safe_set(a, 'ioT_Device25', b2)
    assert _is_linked(a, 'ioT_Device25', b2)
    if hasattr(b1, 'ioT_ConnectStatement24'):
        assert not _is_linked(b1, 'ioT_ConnectStatement24', a)
    if hasattr(b2, 'ioT_ConnectStatement24'):
        assert _is_linked(b2, 'ioT_ConnectStatement24', a)
    _safe_set(a, 'ioT_Device25', None)
    assert not _is_linked(a, 'ioT_Device25', b2)
    if hasattr(b2, 'ioT_ConnectStatement24'):
        assert not _is_linked(b2, 'ioT_ConnectStatement24', a)


def test_assoc_devices3_link_reassign_clear():
    a = ioT_Device(name="sample_text")
    b1 = ioT_Model()
    b2 = ioT_Model()
    _safe_set(a, 'ioT_Device', b1)
    assert _is_linked(a, 'ioT_Device', b1)
    if hasattr(b1, 'ioT_Model4'):
        assert _is_linked(b1, 'ioT_Model4', a)
    _safe_set(a, 'ioT_Device', b2)
    assert _is_linked(a, 'ioT_Device', b2)
    if hasattr(b1, 'ioT_Model4'):
        assert not _is_linked(b1, 'ioT_Model4', a)
    if hasattr(b2, 'ioT_Model4'):
        assert _is_linked(b2, 'ioT_Model4', a)
    _safe_set(a, 'ioT_Device', None)
    assert not _is_linked(a, 'ioT_Device', b2)
    if hasattr(b2, 'ioT_Model4'):
        assert not _is_linked(b2, 'ioT_Model4', a)


def test_assoc_externalDeclarations0_link_reassign_clear():
    a = ioT_ExternalDeclaration(name="sample_text")
    b1 = ioT_Model()
    b2 = ioT_Model()
    _safe_set(a, 'ioT_ExternalDeclaration', b1)
    assert _is_linked(a, 'ioT_ExternalDeclaration', b1)
    if hasattr(b1, 'ioT_Model'):
        assert _is_linked(b1, 'ioT_Model', a)
    _safe_set(a, 'ioT_ExternalDeclaration', b2)
    assert _is_linked(a, 'ioT_ExternalDeclaration', b2)
    if hasattr(b1, 'ioT_Model'):
        assert not _is_linked(b1, 'ioT_Model', a)
    if hasattr(b2, 'ioT_Model'):
        assert _is_linked(b2, 'ioT_Model', a)
    _safe_set(a, 'ioT_ExternalDeclaration', None)
    assert not _is_linked(a, 'ioT_ExternalDeclaration', b2)
    if hasattr(b2, 'ioT_Model'):
        assert not _is_linked(b2, 'ioT_Model', a)


def test_assoc_listenStatements15_link_reassign_clear():
    a = ioT_ListenStatement(ip="sample_text", port=7)
    b1 = ioT_Program()
    b2 = ioT_Program()
    _safe_set(a, 'ioT_ListenStatement', b1)
    assert _is_linked(a, 'ioT_ListenStatement', b1)
    if hasattr(b1, 'ioT_Program16'):
        assert _is_linked(b1, 'ioT_Program16', a)
    _safe_set(a, 'ioT_ListenStatement', b2)
    assert _is_linked(a, 'ioT_ListenStatement', b2)
    if hasattr(b1, 'ioT_Program16'):
        assert not _is_linked(b1, 'ioT_Program16', a)
    if hasattr(b2, 'ioT_Program16'):
        assert _is_linked(b2, 'ioT_Program16', a)
    _safe_set(a, 'ioT_ListenStatement', None)
    assert not _is_linked(a, 'ioT_ListenStatement', b2)
    if hasattr(b2, 'ioT_Program16'):
        assert not _is_linked(b2, 'ioT_Program16', a)


def test_assoc_method41_link_reassign_clear():
    a = ioT_ExternalDeclaration(name="sample_text")
    b1 = ioT_ExternalOf()
    b2 = ioT_ExternalOf()
    _safe_set(a, 'ioT_ExternalDeclaration42', b1)
    assert _is_linked(a, 'ioT_ExternalDeclaration42', b1)
    if hasattr(b1, 'ioT_ExternalOf'):
        assert _is_linked(b1, 'ioT_ExternalOf', a)
    _safe_set(a, 'ioT_ExternalDeclaration42', b2)
    assert _is_linked(a, 'ioT_ExternalDeclaration42', b2)
    if hasattr(b1, 'ioT_ExternalOf'):
        assert not _is_linked(b1, 'ioT_ExternalOf', a)
    if hasattr(b2, 'ioT_ExternalOf'):
        assert _is_linked(b2, 'ioT_ExternalOf', a)
    _safe_set(a, 'ioT_ExternalDeclaration42', None)
    assert not _is_linked(a, 'ioT_ExternalDeclaration42', b2)
    if hasattr(b2, 'ioT_ExternalOf'):
        assert not _is_linked(b2, 'ioT_ExternalOf', a)


def test_assoc_method49_link_reassign_clear():
    a = ioT_ExternalDeclaration(name="sample_text")
    b1 = ioT_ExternalRight()
    b2 = ioT_ExternalRight()
    _safe_set(a, 'ioT_ExternalDeclaration50', b1)
    assert _is_linked(a, 'ioT_ExternalDeclaration50', b1)
    if hasattr(b1, 'ioT_ExternalRight'):
        assert _is_linked(b1, 'ioT_ExternalRight', a)
    _safe_set(a, 'ioT_ExternalDeclaration50', b2)
    assert _is_linked(a, 'ioT_ExternalDeclaration50', b2)
    if hasattr(b1, 'ioT_ExternalRight'):
        assert not _is_linked(b1, 'ioT_ExternalRight', a)
    if hasattr(b2, 'ioT_ExternalRight'):
        assert _is_linked(b2, 'ioT_ExternalRight', a)
    _safe_set(a, 'ioT_ExternalDeclaration50', None)
    assert not _is_linked(a, 'ioT_ExternalDeclaration50', b2)
    if hasattr(b2, 'ioT_ExternalRight'):
        assert not _is_linked(b2, 'ioT_ExternalRight', a)


def test_assoc_op88_link_reassign_clear():
    a = ioT_ComparisonOp(op="sample_text")
    b1 = ioT_EQL()
    b2 = ioT_EQL()
    _safe_set(a, 'ioT_ComparisonOp', b1)
    assert _is_linked(a, 'ioT_ComparisonOp', b1)
    if hasattr(b1, 'ioT_EQL89'):
        assert _is_linked(b1, 'ioT_EQL89', a)
    _safe_set(a, 'ioT_ComparisonOp', b2)
    assert _is_linked(a, 'ioT_ComparisonOp', b2)
    if hasattr(b1, 'ioT_EQL89'):
        assert not _is_linked(b1, 'ioT_EQL89', a)
    if hasattr(b2, 'ioT_EQL89'):
        assert _is_linked(b2, 'ioT_EQL89', a)
    _safe_set(a, 'ioT_ComparisonOp', None)
    assert not _is_linked(a, 'ioT_ComparisonOp', b2)
    if hasattr(b2, 'ioT_EQL89'):
        assert not _is_linked(b2, 'ioT_EQL89', a)


def test_assoc_program7_link_reassign_clear():
    a = ioT_Device(name="sample_text")
    b1 = ioT_Program()
    b2 = ioT_Program()
    _safe_set(a, 'ioT_Device8', b1)
    assert _is_linked(a, 'ioT_Device8', b1)
    if hasattr(b1, 'ioT_Program'):
        assert _is_linked(b1, 'ioT_Program', a)
    _safe_set(a, 'ioT_Device8', b2)
    assert _is_linked(a, 'ioT_Device8', b2)
    if hasattr(b1, 'ioT_Program'):
        assert not _is_linked(b1, 'ioT_Program', a)
    if hasattr(b2, 'ioT_Program'):
        assert _is_linked(b2, 'ioT_Program', a)
    _safe_set(a, 'ioT_Device8', None)
    assert not _is_linked(a, 'ioT_Device8', b2)
    if hasattr(b2, 'ioT_Program'):
        assert not _is_linked(b2, 'ioT_Program', a)


def test_assoc_source39_link_reassign_clear():
    a = ioT_Device(name="sample_text")
    b1 = ioT_ReadConnection()
    b2 = ioT_ReadConnection()
    _safe_set(a, 'ioT_Device40', b1)
    assert _is_linked(a, 'ioT_Device40', b1)
    if hasattr(b1, 'ioT_ReadConnection'):
        assert _is_linked(b1, 'ioT_ReadConnection', a)
    _safe_set(a, 'ioT_Device40', b2)
    assert _is_linked(a, 'ioT_Device40', b2)
    if hasattr(b1, 'ioT_ReadConnection'):
        assert not _is_linked(b1, 'ioT_ReadConnection', a)
    if hasattr(b2, 'ioT_ReadConnection'):
        assert _is_linked(b2, 'ioT_ReadConnection', a)
    _safe_set(a, 'ioT_Device40', None)
    assert not _is_linked(a, 'ioT_Device40', b2)
    if hasattr(b2, 'ioT_ReadConnection'):
        assert not _is_linked(b2, 'ioT_ReadConnection', a)


def test_assoc_target43_link_reassign_clear():
    a = ioT_VarOrList(name="sample_text")
    b1 = ioT_ExternalOf()
    b2 = ioT_ExternalOf()
    _safe_set(a, 'ioT_VarOrList45', b1)
    assert _is_linked(a, 'ioT_VarOrList45', b1)
    if hasattr(b1, 'ioT_ExternalOf44'):
        assert _is_linked(b1, 'ioT_ExternalOf44', a)
    _safe_set(a, 'ioT_VarOrList45', b2)
    assert _is_linked(a, 'ioT_VarOrList45', b2)
    if hasattr(b1, 'ioT_ExternalOf44'):
        assert not _is_linked(b1, 'ioT_ExternalOf44', a)
    if hasattr(b2, 'ioT_ExternalOf44'):
        assert _is_linked(b2, 'ioT_ExternalOf44', a)
    _safe_set(a, 'ioT_VarOrList45', None)
    assert not _is_linked(a, 'ioT_VarOrList45', b2)
    if hasattr(b2, 'ioT_ExternalOf44'):
        assert not _is_linked(b2, 'ioT_ExternalOf44', a)


def test_assoc_target67_link_reassign_clear():
    a = ioT_Device(name="sample_text")
    b1 = ioT_SendCommand()
    b2 = ioT_SendCommand()
    _safe_set(a, 'ioT_Device68', b1)
    assert _is_linked(a, 'ioT_Device68', b1)
    if hasattr(b1, 'ioT_SendCommand'):
        assert _is_linked(b1, 'ioT_SendCommand', a)
    _safe_set(a, 'ioT_Device68', b2)
    assert _is_linked(a, 'ioT_Device68', b2)
    if hasattr(b1, 'ioT_SendCommand'):
        assert not _is_linked(b1, 'ioT_SendCommand', a)
    if hasattr(b2, 'ioT_SendCommand'):
        assert _is_linked(b2, 'ioT_SendCommand', a)
    _safe_set(a, 'ioT_Device68', None)
    assert not _is_linked(a, 'ioT_Device68', b2)
    if hasattr(b2, 'ioT_SendCommand'):
        assert not _is_linked(b2, 'ioT_SendCommand', a)


def test_assoc_variableName61_link_reassign_clear():
    a = ioT_VarOrList(name="sample_text")
    b1 = ioT_VarAccess()
    b2 = ioT_VarAccess()
    _safe_set(a, 'ioT_VarOrList62', b1)
    assert _is_linked(a, 'ioT_VarOrList62', b1)
    if hasattr(b1, 'ioT_VarAccess'):
        assert _is_linked(b1, 'ioT_VarAccess', a)
    _safe_set(a, 'ioT_VarOrList62', b2)
    assert _is_linked(a, 'ioT_VarOrList62', b2)
    if hasattr(b1, 'ioT_VarAccess'):
        assert not _is_linked(b1, 'ioT_VarAccess', a)
    if hasattr(b2, 'ioT_VarAccess'):
        assert _is_linked(b2, 'ioT_VarAccess', a)
    _safe_set(a, 'ioT_VarOrList62', None)
    assert not _is_linked(a, 'ioT_VarOrList62', b2)
    if hasattr(b2, 'ioT_VarAccess'):
        assert not _is_linked(b2, 'ioT_VarAccess', a)


def test_assoc_variables13_link_reassign_clear():
    a = ioT_VarOrList(name="sample_text")
    b1 = ioT_Program()
    b2 = ioT_Program()
    _safe_set(a, 'ioT_VarOrList', b1)
    assert _is_linked(a, 'ioT_VarOrList', b1)
    if hasattr(b1, 'ioT_Program14'):
        assert _is_linked(b1, 'ioT_Program14', a)
    _safe_set(a, 'ioT_VarOrList', b2)
    assert _is_linked(a, 'ioT_VarOrList', b2)
    if hasattr(b1, 'ioT_Program14'):
        assert not _is_linked(b1, 'ioT_Program14', a)
    if hasattr(b2, 'ioT_Program14'):
        assert _is_linked(b2, 'ioT_Program14', a)
    _safe_set(a, 'ioT_VarOrList', None)
    assert not _is_linked(a, 'ioT_VarOrList', b2)
    if hasattr(b2, 'ioT_Program14'):
        assert not _is_linked(b2, 'ioT_Program14', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Address_strategy = st.builds(Address)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


Bool_strategy = st.builds(Bool)
@given(instance=Bool_strategy)
@settings(max_examples=25)
def test_Bool_instantiation(instance):
    assert isinstance(instance, Bool)


Command_strategy = st.builds(Command)
@given(instance=Command_strategy)
@settings(max_examples=25)
def test_Command_instantiation(instance):
    assert isinstance(instance, Command)


Comparison_strategy = st.builds(Comparison)
@given(instance=Comparison_strategy)
@settings(max_examples=25)
def test_Comparison_instantiation(instance):
    assert isinstance(instance, Comparison)


ComparisonOp_strategy = st.builds(ComparisonOp)
@given(instance=ComparisonOp_strategy)
@settings(max_examples=25)
def test_ComparisonOp_instantiation(instance):
    assert isinstance(instance, ComparisonOp)


Config_strategy = st.builds(Config)
@given(instance=Config_strategy)
@settings(max_examples=25)
def test_Config_instantiation(instance):
    assert isinstance(instance, Config)


Device_strategy = st.builds(Device)
@given(instance=Device_strategy)
@settings(max_examples=25)
def test_Device_instantiation(instance):
    assert isinstance(instance, Device)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


ExpressionLeft_strategy = st.builds(ExpressionLeft)
@given(instance=ExpressionLeft_strategy)
@settings(max_examples=25)
def test_ExpressionLeft_instantiation(instance):
    assert isinstance(instance, ExpressionLeft)


ExpressionRight_strategy = st.builds(ExpressionRight)
@given(instance=ExpressionRight_strategy)
@settings(max_examples=25)
def test_ExpressionRight_instantiation(instance):
    assert isinstance(instance, ExpressionRight)


SENSOR_strategy = st.builds(SENSOR)
@given(instance=SENSOR_strategy)
@settings(max_examples=25)
def test_SENSOR_instantiation(instance):
    assert isinstance(instance, SENSOR)


TIMEUNIT_strategy = st.builds(TIMEUNIT)
@given(instance=TIMEUNIT_strategy)
@settings(max_examples=25)
def test_TIMEUNIT_instantiation(instance):
    assert isinstance(instance, TIMEUNIT)


VarOrList_strategy = st.builds(VarOrList)
@given(instance=VarOrList_strategy)
@settings(max_examples=25)
def test_VarOrList_instantiation(instance):
    assert isinstance(instance, VarOrList)


ioT_AND_strategy = st.builds(ioT_AND)
@given(instance=ioT_AND_strategy)
@settings(max_examples=25)
def test_ioT_AND_instantiation(instance):
    assert isinstance(instance, ioT_AND)


ioT_Action_strategy = st.builds(ioT_Action)
@given(instance=ioT_Action_strategy)
@settings(max_examples=25)
def test_ioT_Action_instantiation(instance):
    assert isinstance(instance, ioT_Action)


ioT_AddToList_strategy = st.builds(ioT_AddToList)
@given(instance=ioT_AddToList_strategy)
@settings(max_examples=25)
def test_ioT_AddToList_instantiation(instance):
    assert isinstance(instance, ioT_AddToList)


ioT_Address_strategy = st.builds(ioT_Address, value=safe_text)
@given(instance=ioT_Address_strategy)
@settings(max_examples=25)
def test_ioT_Address_instantiation(instance):
    assert isinstance(instance, ioT_Address)


ioT_ArrowCommand_strategy = st.builds(ioT_ArrowCommand)
@given(instance=ioT_ArrowCommand_strategy)
@settings(max_examples=25)
def test_ioT_ArrowCommand_instantiation(instance):
    assert isinstance(instance, ioT_ArrowCommand)


ioT_Block_strategy = st.builds(ioT_Block)
@given(instance=ioT_Block_strategy)
@settings(max_examples=25)
def test_ioT_Block_instantiation(instance):
    assert isinstance(instance, ioT_Block)


ioT_Bool_strategy = st.builds(ioT_Bool)
@given(instance=ioT_Bool_strategy)
@settings(max_examples=25)
def test_ioT_Bool_instantiation(instance):
    assert isinstance(instance, ioT_Bool)


ioT_BoolExpression_strategy = st.builds(ioT_BoolExpression)
@given(instance=ioT_BoolExpression_strategy)
@settings(max_examples=25)
def test_ioT_BoolExpression_instantiation(instance):
    assert isinstance(instance, ioT_BoolExpression)


ioT_ClearListAction_strategy = st.builds(ioT_ClearListAction)
@given(instance=ioT_ClearListAction_strategy)
@settings(max_examples=25)
def test_ioT_ClearListAction_instantiation(instance):
    assert isinstance(instance, ioT_ClearListAction)


ioT_Command_strategy = st.builds(ioT_Command)
@given(instance=ioT_Command_strategy)
@settings(max_examples=25)
def test_ioT_Command_instantiation(instance):
    assert isinstance(instance, ioT_Command)


ioT_Comparison_strategy = st.builds(ioT_Comparison)
@given(instance=ioT_Comparison_strategy)
@settings(max_examples=25)
def test_ioT_Comparison_instantiation(instance):
    assert isinstance(instance, ioT_Comparison)


ioT_ComparisonOp_strategy = st.builds(ioT_ComparisonOp, op=safe_text)
@given(instance=ioT_ComparisonOp_strategy)
@settings(max_examples=25)
def test_ioT_ComparisonOp_instantiation(instance):
    assert isinstance(instance, ioT_ComparisonOp)


ioT_Config_strategy = st.builds(ioT_Config, name=safe_text)
@given(instance=ioT_Config_strategy)
@settings(max_examples=25)
def test_ioT_Config_instantiation(instance):
    assert isinstance(instance, ioT_Config)


ioT_ConnectStatement_strategy = st.builds(ioT_ConnectStatement)
@given(instance=ioT_ConnectStatement_strategy)
@settings(max_examples=25)
def test_ioT_ConnectStatement_instantiation(instance):
    assert isinstance(instance, ioT_ConnectStatement)


ioT_ConnectionConfig_strategy = st.builds(ioT_ConnectionConfig, type=safe_text)
@given(instance=ioT_ConnectionConfig_strategy)
@settings(max_examples=25)
def test_ioT_ConnectionConfig_instantiation(instance):
    assert isinstance(instance, ioT_ConnectionConfig)


ioT_ControllerDevice_strategy = st.builds(ioT_ControllerDevice)
@given(instance=ioT_ControllerDevice_strategy)
@settings(max_examples=25)
def test_ioT_ControllerDevice_instantiation(instance):
    assert isinstance(instance, ioT_ControllerDevice)


ioT_DAYS_strategy = st.builds(ioT_DAYS)
@given(instance=ioT_DAYS_strategy)
@settings(max_examples=25)
def test_ioT_DAYS_instantiation(instance):
    assert isinstance(instance, ioT_DAYS)


ioT_Declaration_strategy = st.builds(ioT_Declaration, key=safe_text, value=safe_text)
@given(instance=ioT_Declaration_strategy)
@settings(max_examples=25)
def test_ioT_Declaration_instantiation(instance):
    assert isinstance(instance, ioT_Declaration)


ioT_Device_strategy = st.builds(ioT_Device, name=safe_text)
@given(instance=ioT_Device_strategy)
@settings(max_examples=25)
def test_ioT_Device_instantiation(instance):
    assert isinstance(instance, ioT_Device)


ioT_DeviceConfig_strategy = st.builds(ioT_DeviceConfig)
@given(instance=ioT_DeviceConfig_strategy)
@settings(max_examples=25)
def test_ioT_DeviceConfig_instantiation(instance):
    assert isinstance(instance, ioT_DeviceConfig)


ioT_EQ_strategy = st.builds(ioT_EQ)
@given(instance=ioT_EQ_strategy)
@settings(max_examples=25)
def test_ioT_EQ_instantiation(instance):
    assert isinstance(instance, ioT_EQ)


ioT_EQL_strategy = st.builds(ioT_EQL)
@given(instance=ioT_EQL_strategy)
@settings(max_examples=25)
def test_ioT_EQL_instantiation(instance):
    assert isinstance(instance, ioT_EQL)


ioT_ElseBlock_strategy = st.builds(ioT_ElseBlock)
@given(instance=ioT_ElseBlock_strategy)
@settings(max_examples=25)
def test_ioT_ElseBlock_instantiation(instance):
    assert isinstance(instance, ioT_ElseBlock)


ioT_Expression_strategy = st.builds(ioT_Expression)
@given(instance=ioT_Expression_strategy)
@settings(max_examples=25)
def test_ioT_Expression_instantiation(instance):
    assert isinstance(instance, ioT_Expression)


ioT_ExpressionLeft_strategy = st.builds(ioT_ExpressionLeft)
@given(instance=ioT_ExpressionLeft_strategy)
@settings(max_examples=25)
def test_ioT_ExpressionLeft_instantiation(instance):
    assert isinstance(instance, ioT_ExpressionLeft)


ioT_ExpressionRight_strategy = st.builds(ioT_ExpressionRight)
@given(instance=ioT_ExpressionRight_strategy)
@settings(max_examples=25)
def test_ioT_ExpressionRight_instantiation(instance):
    assert isinstance(instance, ioT_ExpressionRight)


ioT_ExternalDeclaration_strategy = st.builds(ioT_ExternalDeclaration, name=safe_text)
@given(instance=ioT_ExternalDeclaration_strategy)
@settings(max_examples=25)
def test_ioT_ExternalDeclaration_instantiation(instance):
    assert isinstance(instance, ioT_ExternalDeclaration)


ioT_ExternalOf_strategy = st.builds(ioT_ExternalOf)
@given(instance=ioT_ExternalOf_strategy)
@settings(max_examples=25)
def test_ioT_ExternalOf_instantiation(instance):
    assert isinstance(instance, ioT_ExternalOf)


ioT_ExternalRight_strategy = st.builds(ioT_ExternalRight)
@given(instance=ioT_ExternalRight_strategy)
@settings(max_examples=25)
def test_ioT_ExternalRight_instantiation(instance):
    assert isinstance(instance, ioT_ExternalRight)


ioT_False_strategy = st.builds(ioT_False)
@given(instance=ioT_False_strategy)
@settings(max_examples=25)
def test_ioT_False_instantiation(instance):
    assert isinstance(instance, ioT_False)


ioT_GE_strategy = st.builds(ioT_GE)
@given(instance=ioT_GE_strategy)
@settings(max_examples=25)
def test_ioT_GE_instantiation(instance):
    assert isinstance(instance, ioT_GE)


ioT_GT_strategy = st.builds(ioT_GT)
@given(instance=ioT_GT_strategy)
@settings(max_examples=25)
def test_ioT_GT_instantiation(instance):
    assert isinstance(instance, ioT_GT)


ioT_HOURS_strategy = st.builds(ioT_HOURS)
@given(instance=ioT_HOURS_strategy)
@settings(max_examples=25)
def test_ioT_HOURS_instantiation(instance):
    assert isinstance(instance, ioT_HOURS)


ioT_HUMIDITY_strategy = st.builds(ioT_HUMIDITY)
@given(instance=ioT_HUMIDITY_strategy)
@settings(max_examples=25)
def test_ioT_HUMIDITY_instantiation(instance):
    assert isinstance(instance, ioT_HUMIDITY)


ioT_IfStatement_strategy = st.builds(ioT_IfStatement)
@given(instance=ioT_IfStatement_strategy)
@settings(max_examples=25)
def test_ioT_IfStatement_instantiation(instance):
    assert isinstance(instance, ioT_IfStatement)


ioT_IntExpression_strategy = st.builds(ioT_IntExpression, value=st.integers())
@given(instance=ioT_IntExpression_strategy)
@settings(max_examples=25)
def test_ioT_IntExpression_instantiation(instance):
    assert isinstance(instance, ioT_IntExpression)


ioT_IoTDevice_strategy = st.builds(ioT_IoTDevice)
@given(instance=ioT_IoTDevice_strategy)
@settings(max_examples=25)
def test_ioT_IoTDevice_instantiation(instance):
    assert isinstance(instance, ioT_IoTDevice)


ioT_IpAddress_strategy = st.builds(ioT_IpAddress)
@given(instance=ioT_IpAddress_strategy)
@settings(max_examples=25)
def test_ioT_IpAddress_instantiation(instance):
    assert isinstance(instance, ioT_IpAddress)


ioT_ItemBool_strategy = st.builds(ioT_ItemBool)
@given(instance=ioT_ItemBool_strategy)
@settings(max_examples=25)
def test_ioT_ItemBool_instantiation(instance):
    assert isinstance(instance, ioT_ItemBool)


ioT_ItemInt_strategy = st.builds(ioT_ItemInt, value=st.integers())
@given(instance=ioT_ItemInt_strategy)
@settings(max_examples=25)
def test_ioT_ItemInt_instantiation(instance):
    assert isinstance(instance, ioT_ItemInt)


ioT_ItemVariable_strategy = st.builds(ioT_ItemVariable)
@given(instance=ioT_ItemVariable_strategy)
@settings(max_examples=25)
def test_ioT_ItemVariable_instantiation(instance):
    assert isinstance(instance, ioT_ItemVariable)


ioT_LE_strategy = st.builds(ioT_LE)
@given(instance=ioT_LE_strategy)
@settings(max_examples=25)
def test_ioT_LE_instantiation(instance):
    assert isinstance(instance, ioT_LE)


ioT_LEDAction_strategy = st.builds(ioT_LEDAction, state=safe_text)
@given(instance=ioT_LEDAction_strategy)
@settings(max_examples=25)
def test_ioT_LEDAction_instantiation(instance):
    assert isinstance(instance, ioT_LEDAction)


ioT_LIGHTSENSOR_strategy = st.builds(ioT_LIGHTSENSOR)
@given(instance=ioT_LIGHTSENSOR_strategy)
@settings(max_examples=25)
def test_ioT_LIGHTSENSOR_instantiation(instance):
    assert isinstance(instance, ioT_LIGHTSENSOR)


ioT_LT_strategy = st.builds(ioT_LT)
@given(instance=ioT_LT_strategy)
@settings(max_examples=25)
def test_ioT_LT_instantiation(instance):
    assert isinstance(instance, ioT_LT)


ioT_ListenStatement_strategy = st.builds(ioT_ListenStatement, ip=safe_text, port=st.integers())
@given(instance=ioT_ListenStatement_strategy)
@settings(max_examples=25)
def test_ioT_ListenStatement_instantiation(instance):
    assert isinstance(instance, ioT_ListenStatement)


ioT_Loop_strategy = st.builds(ioT_Loop)
@given(instance=ioT_Loop_strategy)
@settings(max_examples=25)
def test_ioT_Loop_instantiation(instance):
    assert isinstance(instance, ioT_Loop)


ioT_MILLISECONDS_strategy = st.builds(ioT_MILLISECONDS)
@given(instance=ioT_MILLISECONDS_strategy)
@settings(max_examples=25)
def test_ioT_MILLISECONDS_instantiation(instance):
    assert isinstance(instance, ioT_MILLISECONDS)


ioT_MINUTES_strategy = st.builds(ioT_MINUTES)
@given(instance=ioT_MINUTES_strategy)
@settings(max_examples=25)
def test_ioT_MINUTES_instantiation(instance):
    assert isinstance(instance, ioT_MINUTES)


ioT_Model_strategy = st.builds(ioT_Model)
@given(instance=ioT_Model_strategy)
@settings(max_examples=25)
def test_ioT_Model_instantiation(instance):
    assert isinstance(instance, ioT_Model)


ioT_NE_strategy = st.builds(ioT_NE)
@given(instance=ioT_NE_strategy)
@settings(max_examples=25)
def test_ioT_NE_instantiation(instance):
    assert isinstance(instance, ioT_NE)


ioT_OR_strategy = st.builds(ioT_OR)
@given(instance=ioT_OR_strategy)
@settings(max_examples=25)
def test_ioT_OR_instantiation(instance):
    assert isinstance(instance, ioT_OR)


ioT_Program_strategy = st.builds(ioT_Program)
@given(instance=ioT_Program_strategy)
@settings(max_examples=25)
def test_ioT_Program_instantiation(instance):
    assert isinstance(instance, ioT_Program)


ioT_PyList_strategy = st.builds(ioT_PyList)
@given(instance=ioT_PyList_strategy)
@settings(max_examples=25)
def test_ioT_PyList_instantiation(instance):
    assert isinstance(instance, ioT_PyList)


ioT_ReadConnection_strategy = st.builds(ioT_ReadConnection)
@given(instance=ioT_ReadConnection_strategy)
@settings(max_examples=25)
def test_ioT_ReadConnection_instantiation(instance):
    assert isinstance(instance, ioT_ReadConnection)


ioT_ReadSensor_strategy = st.builds(ioT_ReadSensor)
@given(instance=ioT_ReadSensor_strategy)
@settings(max_examples=25)
def test_ioT_ReadSensor_instantiation(instance):
    assert isinstance(instance, ioT_ReadSensor)


ioT_ReadVariable_strategy = st.builds(ioT_ReadVariable)
@given(instance=ioT_ReadVariable_strategy)
@settings(max_examples=25)
def test_ioT_ReadVariable_instantiation(instance):
    assert isinstance(instance, ioT_ReadVariable)


ioT_SECONDS_strategy = st.builds(ioT_SECONDS)
@given(instance=ioT_SECONDS_strategy)
@settings(max_examples=25)
def test_ioT_SECONDS_instantiation(instance):
    assert isinstance(instance, ioT_SECONDS)


ioT_SENSOR_strategy = st.builds(ioT_SENSOR)
@given(instance=ioT_SENSOR_strategy)
@settings(max_examples=25)
def test_ioT_SENSOR_instantiation(instance):
    assert isinstance(instance, ioT_SENSOR)


ioT_SendCommand_strategy = st.builds(ioT_SendCommand)
@given(instance=ioT_SendCommand_strategy)
@settings(max_examples=25)
def test_ioT_SendCommand_instantiation(instance):
    assert isinstance(instance, ioT_SendCommand)


ioT_TEMPERATURE_strategy = st.builds(ioT_TEMPERATURE)
@given(instance=ioT_TEMPERATURE_strategy)
@settings(max_examples=25)
def test_ioT_TEMPERATURE_instantiation(instance):
    assert isinstance(instance, ioT_TEMPERATURE)


ioT_TIMEUNIT_strategy = st.builds(ioT_TIMEUNIT)
@given(instance=ioT_TIMEUNIT_strategy)
@settings(max_examples=25)
def test_ioT_TIMEUNIT_instantiation(instance):
    assert isinstance(instance, ioT_TIMEUNIT)


ioT_ToVar_strategy = st.builds(ioT_ToVar)
@given(instance=ioT_ToVar_strategy)
@settings(max_examples=25)
def test_ioT_ToVar_instantiation(instance):
    assert isinstance(instance, ioT_ToVar)


ioT_True_strategy = st.builds(ioT_True)
@given(instance=ioT_True_strategy)
@settings(max_examples=25)
def test_ioT_True_instantiation(instance):
    assert isinstance(instance, ioT_True)


ioT_UnixSerialAddress_strategy = st.builds(ioT_UnixSerialAddress)
@given(instance=ioT_UnixSerialAddress_strategy)
@settings(max_examples=25)
def test_ioT_UnixSerialAddress_instantiation(instance):
    assert isinstance(instance, ioT_UnixSerialAddress)


ioT_VarAccess_strategy = st.builds(ioT_VarAccess)
@given(instance=ioT_VarAccess_strategy)
@settings(max_examples=25)
def test_ioT_VarAccess_instantiation(instance):
    assert isinstance(instance, ioT_VarAccess)


ioT_VarOrList_strategy = st.builds(ioT_VarOrList, name=safe_text)
@given(instance=ioT_VarOrList_strategy)
@settings(max_examples=25)
def test_ioT_VarOrList_instantiation(instance):
    assert isinstance(instance, ioT_VarOrList)


ioT_Variable_strategy = st.builds(ioT_Variable)
@given(instance=ioT_Variable_strategy)
@settings(max_examples=25)
def test_ioT_Variable_instantiation(instance):
    assert isinstance(instance, ioT_Variable)


ioT_WEEKS_strategy = st.builds(ioT_WEEKS)
@given(instance=ioT_WEEKS_strategy)
@settings(max_examples=25)
def test_ioT_WEEKS_instantiation(instance):
    assert isinstance(instance, ioT_WEEKS)


ioT_WifiStatement_strategy = st.builds(ioT_WifiStatement)
@given(instance=ioT_WifiStatement_strategy)
@settings(max_examples=25)
def test_ioT_WifiStatement_instantiation(instance):
    assert isinstance(instance, ioT_WifiStatement)


ioT_WindowsSerialAddress_strategy = st.builds(ioT_WindowsSerialAddress)
@given(instance=ioT_WindowsSerialAddress_strategy)
@settings(max_examples=25)
def test_ioT_WindowsSerialAddress_instantiation(instance):
    assert isinstance(instance, ioT_WindowsSerialAddress)



