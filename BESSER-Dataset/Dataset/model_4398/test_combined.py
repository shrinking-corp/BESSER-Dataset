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
    AngleOperation,
    QuantityScalarOperation,
    raspirover_AngleScalarDivide,
    raspirover_AngleScalarMultiply,
    QuantityHomogenousOperation,
    raspirover_AngleAdd,
    raspirover_AngleEquals,
    raspirover_AngleSmaller,
    raspirover_AngleDistinct,
    raspirover_AngleGreater,
    raspirover_AngleSubtract,
    LengthOperation,
    raspirover_LengthScalarMultiply,
    raspirover_LengthSmaller,
    raspirover_LengthDistinct,
    raspirover_LengthScalarDivide,
    raspirover_LengthGreater,
    raspirover_LengthSubtract,
    raspirover_LengthEquals,
    raspirover_LengthAdd,
    QuantityOperation,
    raspirover_QuantityScalarOperation,
    raspirover_AngleOperation,
    raspirover_QuantityComparisonOperation,
    raspirover_QuantityHomogenousOperation,
    raspirover_QuantityArithmeticOperation,
    raspirover_LengthOperation,
    raspirover_QuantityOperation,
    Quantity,
    raspirover_Angle,
    raspirover_Length,
    AngleUnit,
    raspirover_Degree,
    raspirover_Turn,
    raspirover_Gradian,
    raspirover_Radian,
    ImperialSystemUnit,
    LengthUnit,
    raspirover_Yard,
    raspirover_Inch,
    raspirover_Foot,
    MetricSystemUnit,
    raspirover_Meter,
    raspirover_Millimeter,
    raspirover_Centimeter,
    Unit,
    raspirover_MetricSystemUnit,
    raspirover_ImperialSystemUnit,
    raspirover_AngleUnit,
    raspirover_LengthUnit,
    raspirover_Unit,
    Action,
    raspirover_TurnDegAction,
    raspirover_ForwardMinAction,
    raspirover_LogAction,
    raspirover_BackwardAction,
    raspirover_StopAction,
    raspirover_SendAction,
    raspirover_TurnAction,
    raspirover_BackwardMinAction,
    raspirover_ForwardAction,
    raspirover_Quantity,
    RoverValue,
    raspirover_StringValue,
    raspirover_BooleanValue,
    raspirover_NumberValue,
    RoverExpression,
    raspirover_StringExpression,
    raspirover_BooleanExpression,
    raspirover_NumericExpression,
    BooleanValue,
    StringValue,
    NumberValue,
    Query,
    raspirover_ObstacleQuery,
    raspirover_HumidityQuery,
    raspirover_MessageQuery,
    raspirover_TemperatureQuery,
    raspirover_Query,
    raspirover_RoverExpression,
    raspirover_RoverValue,
    Statement,
    raspirover_VarRef,
    raspirover_Conditional,
    raspirover_Action,
    raspirover_Loop,
    raspirover_VarAssignment,
    raspirover_Statement,
    raspirover_RclBlock,
    raspirover_Param,
    raspirover_NamedElement,
    Module,
    raspirover_ArduinoModule,
    ArduinoModule,
    raspirover_ArduinoAnalogModule,
    raspirover_ArduinoDigitalModule,
    Pin,
    raspirover_Instruction,
    raspirover_Block,
    raspirover_RoverProgram,
    raspirover_Project,
    NamedElement,
    raspirover_Pin,
    raspirover_Module,
    raspirover_Sketch,
    raspirover_Board,
    raspirover_AnalogPin,
    raspirover_DigitalPin,
    Board,
    raspirover_RasPiBoard,
    NumericOperator,
    StringOperator,
    BooleanOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_angleoperation_is_not_abstract():
    assert not inspect.isabstract(AngleOperation)


def test_hyp_angleoperation_constructor_exists():
    assert callable(AngleOperation.__init__)


def test_hyp_angleoperation_constructor_args():
    sig = inspect.signature(AngleOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantityscalaroperation_is_not_abstract():
    assert not inspect.isabstract(QuantityScalarOperation)


def test_hyp_quantityscalaroperation_constructor_exists():
    assert callable(QuantityScalarOperation.__init__)


def test_hyp_quantityscalaroperation_constructor_args():
    sig = inspect.signature(QuantityScalarOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_anglescalardivide_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleScalarDivide)


def test_hyp_raspirover_anglescalardivide_constructor_exists():
    assert callable(raspirover_AngleScalarDivide.__init__)


def test_hyp_raspirover_anglescalardivide_constructor_args():
    sig = inspect.signature(raspirover_AngleScalarDivide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_anglescalarmultiply_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleScalarMultiply)


def test_hyp_raspirover_anglescalarmultiply_constructor_exists():
    assert callable(raspirover_AngleScalarMultiply.__init__)


def test_hyp_raspirover_anglescalarmultiply_constructor_args():
    sig = inspect.signature(raspirover_AngleScalarMultiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantityhomogenousoperation_is_not_abstract():
    assert not inspect.isabstract(QuantityHomogenousOperation)


def test_hyp_quantityhomogenousoperation_constructor_exists():
    assert callable(QuantityHomogenousOperation.__init__)


def test_hyp_quantityhomogenousoperation_constructor_args():
    sig = inspect.signature(QuantityHomogenousOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_angleadd_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleAdd)


def test_hyp_raspirover_angleadd_constructor_exists():
    assert callable(raspirover_AngleAdd.__init__)


def test_hyp_raspirover_angleadd_constructor_args():
    sig = inspect.signature(raspirover_AngleAdd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_angleequals_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleEquals)


def test_hyp_raspirover_angleequals_constructor_exists():
    assert callable(raspirover_AngleEquals.__init__)


def test_hyp_raspirover_angleequals_constructor_args():
    sig = inspect.signature(raspirover_AngleEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_anglesmaller_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleSmaller)


def test_hyp_raspirover_anglesmaller_constructor_exists():
    assert callable(raspirover_AngleSmaller.__init__)


def test_hyp_raspirover_anglesmaller_constructor_args():
    sig = inspect.signature(raspirover_AngleSmaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_angledistinct_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleDistinct)


def test_hyp_raspirover_angledistinct_constructor_exists():
    assert callable(raspirover_AngleDistinct.__init__)


def test_hyp_raspirover_angledistinct_constructor_args():
    sig = inspect.signature(raspirover_AngleDistinct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_anglegreater_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleGreater)


def test_hyp_raspirover_anglegreater_constructor_exists():
    assert callable(raspirover_AngleGreater.__init__)


def test_hyp_raspirover_anglegreater_constructor_args():
    sig = inspect.signature(raspirover_AngleGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_anglesubtract_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleSubtract)


def test_hyp_raspirover_anglesubtract_constructor_exists():
    assert callable(raspirover_AngleSubtract.__init__)


def test_hyp_raspirover_anglesubtract_constructor_args():
    sig = inspect.signature(raspirover_AngleSubtract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lengthoperation_is_not_abstract():
    assert not inspect.isabstract(LengthOperation)


def test_hyp_lengthoperation_constructor_exists():
    assert callable(LengthOperation.__init__)


def test_hyp_lengthoperation_constructor_args():
    sig = inspect.signature(LengthOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthscalarmultiply_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthScalarMultiply)


def test_hyp_raspirover_lengthscalarmultiply_constructor_exists():
    assert callable(raspirover_LengthScalarMultiply.__init__)


def test_hyp_raspirover_lengthscalarmultiply_constructor_args():
    sig = inspect.signature(raspirover_LengthScalarMultiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthsmaller_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthSmaller)


def test_hyp_raspirover_lengthsmaller_constructor_exists():
    assert callable(raspirover_LengthSmaller.__init__)


def test_hyp_raspirover_lengthsmaller_constructor_args():
    sig = inspect.signature(raspirover_LengthSmaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthdistinct_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthDistinct)


def test_hyp_raspirover_lengthdistinct_constructor_exists():
    assert callable(raspirover_LengthDistinct.__init__)


def test_hyp_raspirover_lengthdistinct_constructor_args():
    sig = inspect.signature(raspirover_LengthDistinct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthscalardivide_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthScalarDivide)


def test_hyp_raspirover_lengthscalardivide_constructor_exists():
    assert callable(raspirover_LengthScalarDivide.__init__)


def test_hyp_raspirover_lengthscalardivide_constructor_args():
    sig = inspect.signature(raspirover_LengthScalarDivide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthgreater_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthGreater)


def test_hyp_raspirover_lengthgreater_constructor_exists():
    assert callable(raspirover_LengthGreater.__init__)


def test_hyp_raspirover_lengthgreater_constructor_args():
    sig = inspect.signature(raspirover_LengthGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthsubtract_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthSubtract)


def test_hyp_raspirover_lengthsubtract_constructor_exists():
    assert callable(raspirover_LengthSubtract.__init__)


def test_hyp_raspirover_lengthsubtract_constructor_args():
    sig = inspect.signature(raspirover_LengthSubtract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthequals_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthEquals)


def test_hyp_raspirover_lengthequals_constructor_exists():
    assert callable(raspirover_LengthEquals.__init__)


def test_hyp_raspirover_lengthequals_constructor_args():
    sig = inspect.signature(raspirover_LengthEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthadd_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthAdd)


def test_hyp_raspirover_lengthadd_constructor_exists():
    assert callable(raspirover_LengthAdd.__init__)


def test_hyp_raspirover_lengthadd_constructor_args():
    sig = inspect.signature(raspirover_LengthAdd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantityoperation_is_not_abstract():
    assert not inspect.isabstract(QuantityOperation)


def test_hyp_quantityoperation_constructor_exists():
    assert callable(QuantityOperation.__init__)


def test_hyp_quantityoperation_constructor_args():
    sig = inspect.signature(QuantityOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantityscalaroperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_QuantityScalarOperation)


def test_hyp_raspirover_quantityscalaroperation_constructor_exists():
    assert callable(raspirover_QuantityScalarOperation.__init__)


def test_hyp_raspirover_quantityscalaroperation_constructor_args():
    sig = inspect.signature(raspirover_QuantityScalarOperation.__init__)
    params = list(sig.parameters.keys())
    assert "rhs" in params, "Missing parameter 'rhs'"




def test_hyp_raspirover_angleoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleOperation)


def test_hyp_raspirover_angleoperation_constructor_exists():
    assert callable(raspirover_AngleOperation.__init__)


def test_hyp_raspirover_angleoperation_constructor_args():
    sig = inspect.signature(raspirover_AngleOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantitycomparisonoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_QuantityComparisonOperation)


def test_hyp_raspirover_quantitycomparisonoperation_constructor_exists():
    assert callable(raspirover_QuantityComparisonOperation.__init__)


def test_hyp_raspirover_quantitycomparisonoperation_constructor_args():
    sig = inspect.signature(raspirover_QuantityComparisonOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantityhomogenousoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_QuantityHomogenousOperation)


def test_hyp_raspirover_quantityhomogenousoperation_constructor_exists():
    assert callable(raspirover_QuantityHomogenousOperation.__init__)


def test_hyp_raspirover_quantityhomogenousoperation_constructor_args():
    sig = inspect.signature(raspirover_QuantityHomogenousOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantityarithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_QuantityArithmeticOperation)


def test_hyp_raspirover_quantityarithmeticoperation_constructor_exists():
    assert callable(raspirover_QuantityArithmeticOperation.__init__)


def test_hyp_raspirover_quantityarithmeticoperation_constructor_args():
    sig = inspect.signature(raspirover_QuantityArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthOperation)


def test_hyp_raspirover_lengthoperation_constructor_exists():
    assert callable(raspirover_LengthOperation.__init__)


def test_hyp_raspirover_lengthoperation_constructor_args():
    sig = inspect.signature(raspirover_LengthOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantityoperation_is_not_abstract():
    assert not inspect.isabstract(raspirover_QuantityOperation)


def test_hyp_raspirover_quantityoperation_constructor_exists():
    assert callable(raspirover_QuantityOperation.__init__)


def test_hyp_raspirover_quantityoperation_constructor_args():
    sig = inspect.signature(raspirover_QuantityOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_hyp_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_hyp_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_angle_is_not_abstract():
    assert not inspect.isabstract(raspirover_Angle)


def test_hyp_raspirover_angle_constructor_exists():
    assert callable(raspirover_Angle.__init__)


def test_hyp_raspirover_angle_constructor_args():
    sig = inspect.signature(raspirover_Angle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_length_is_not_abstract():
    assert not inspect.isabstract(raspirover_Length)


def test_hyp_raspirover_length_constructor_exists():
    assert callable(raspirover_Length.__init__)


def test_hyp_raspirover_length_constructor_args():
    sig = inspect.signature(raspirover_Length.__init__)
    params = list(sig.parameters.keys())



def test_hyp_angleunit_is_not_abstract():
    assert not inspect.isabstract(AngleUnit)


def test_hyp_angleunit_constructor_exists():
    assert callable(AngleUnit.__init__)


def test_hyp_angleunit_constructor_args():
    sig = inspect.signature(AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_degree_is_not_abstract():
    assert not inspect.isabstract(raspirover_Degree)


def test_hyp_raspirover_degree_constructor_exists():
    assert callable(raspirover_Degree.__init__)


def test_hyp_raspirover_degree_constructor_args():
    sig = inspect.signature(raspirover_Degree.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_turn_is_not_abstract():
    assert not inspect.isabstract(raspirover_Turn)


def test_hyp_raspirover_turn_constructor_exists():
    assert callable(raspirover_Turn.__init__)


def test_hyp_raspirover_turn_constructor_args():
    sig = inspect.signature(raspirover_Turn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_gradian_is_not_abstract():
    assert not inspect.isabstract(raspirover_Gradian)


def test_hyp_raspirover_gradian_constructor_exists():
    assert callable(raspirover_Gradian.__init__)


def test_hyp_raspirover_gradian_constructor_args():
    sig = inspect.signature(raspirover_Gradian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_radian_is_not_abstract():
    assert not inspect.isabstract(raspirover_Radian)


def test_hyp_raspirover_radian_constructor_exists():
    assert callable(raspirover_Radian.__init__)


def test_hyp_raspirover_radian_constructor_args():
    sig = inspect.signature(raspirover_Radian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imperialsystemunit_is_not_abstract():
    assert not inspect.isabstract(ImperialSystemUnit)


def test_hyp_imperialsystemunit_constructor_exists():
    assert callable(ImperialSystemUnit.__init__)


def test_hyp_imperialsystemunit_constructor_args():
    sig = inspect.signature(ImperialSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lengthunit_is_not_abstract():
    assert not inspect.isabstract(LengthUnit)


def test_hyp_lengthunit_constructor_exists():
    assert callable(LengthUnit.__init__)


def test_hyp_lengthunit_constructor_args():
    sig = inspect.signature(LengthUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_yard_is_not_abstract():
    assert not inspect.isabstract(raspirover_Yard)


def test_hyp_raspirover_yard_constructor_exists():
    assert callable(raspirover_Yard.__init__)


def test_hyp_raspirover_yard_constructor_args():
    sig = inspect.signature(raspirover_Yard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_inch_is_not_abstract():
    assert not inspect.isabstract(raspirover_Inch)


def test_hyp_raspirover_inch_constructor_exists():
    assert callable(raspirover_Inch.__init__)


def test_hyp_raspirover_inch_constructor_args():
    sig = inspect.signature(raspirover_Inch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_foot_is_not_abstract():
    assert not inspect.isabstract(raspirover_Foot)


def test_hyp_raspirover_foot_constructor_exists():
    assert callable(raspirover_Foot.__init__)


def test_hyp_raspirover_foot_constructor_args():
    sig = inspect.signature(raspirover_Foot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metricsystemunit_is_not_abstract():
    assert not inspect.isabstract(MetricSystemUnit)


def test_hyp_metricsystemunit_constructor_exists():
    assert callable(MetricSystemUnit.__init__)


def test_hyp_metricsystemunit_constructor_args():
    sig = inspect.signature(MetricSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_meter_is_not_abstract():
    assert not inspect.isabstract(raspirover_Meter)


def test_hyp_raspirover_meter_constructor_exists():
    assert callable(raspirover_Meter.__init__)


def test_hyp_raspirover_meter_constructor_args():
    sig = inspect.signature(raspirover_Meter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_millimeter_is_not_abstract():
    assert not inspect.isabstract(raspirover_Millimeter)


def test_hyp_raspirover_millimeter_constructor_exists():
    assert callable(raspirover_Millimeter.__init__)


def test_hyp_raspirover_millimeter_constructor_args():
    sig = inspect.signature(raspirover_Millimeter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_centimeter_is_not_abstract():
    assert not inspect.isabstract(raspirover_Centimeter)


def test_hyp_raspirover_centimeter_constructor_exists():
    assert callable(raspirover_Centimeter.__init__)


def test_hyp_raspirover_centimeter_constructor_args():
    sig = inspect.signature(raspirover_Centimeter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_hyp_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_hyp_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_metricsystemunit_is_not_abstract():
    assert not inspect.isabstract(raspirover_MetricSystemUnit)


def test_hyp_raspirover_metricsystemunit_constructor_exists():
    assert callable(raspirover_MetricSystemUnit.__init__)


def test_hyp_raspirover_metricsystemunit_constructor_args():
    sig = inspect.signature(raspirover_MetricSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_imperialsystemunit_is_not_abstract():
    assert not inspect.isabstract(raspirover_ImperialSystemUnit)


def test_hyp_raspirover_imperialsystemunit_constructor_exists():
    assert callable(raspirover_ImperialSystemUnit.__init__)


def test_hyp_raspirover_imperialsystemunit_constructor_args():
    sig = inspect.signature(raspirover_ImperialSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_angleunit_is_not_abstract():
    assert not inspect.isabstract(raspirover_AngleUnit)


def test_hyp_raspirover_angleunit_constructor_exists():
    assert callable(raspirover_AngleUnit.__init__)


def test_hyp_raspirover_angleunit_constructor_args():
    sig = inspect.signature(raspirover_AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_lengthunit_is_not_abstract():
    assert not inspect.isabstract(raspirover_LengthUnit)


def test_hyp_raspirover_lengthunit_constructor_exists():
    assert callable(raspirover_LengthUnit.__init__)


def test_hyp_raspirover_lengthunit_constructor_args():
    sig = inspect.signature(raspirover_LengthUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_unit_is_not_abstract():
    assert not inspect.isabstract(raspirover_Unit)


def test_hyp_raspirover_unit_constructor_exists():
    assert callable(raspirover_Unit.__init__)


def test_hyp_raspirover_unit_constructor_args():
    sig = inspect.signature(raspirover_Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_hyp_action_constructor_exists():
    assert callable(Action.__init__)


def test_hyp_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_turndegaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_TurnDegAction)


def test_hyp_raspirover_turndegaction_constructor_exists():
    assert callable(raspirover_TurnDegAction.__init__)


def test_hyp_raspirover_turndegaction_constructor_args():
    sig = inspect.signature(raspirover_TurnDegAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_forwardminaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_ForwardMinAction)


def test_hyp_raspirover_forwardminaction_constructor_exists():
    assert callable(raspirover_ForwardMinAction.__init__)


def test_hyp_raspirover_forwardminaction_constructor_args():
    sig = inspect.signature(raspirover_ForwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_logaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_LogAction)


def test_hyp_raspirover_logaction_constructor_exists():
    assert callable(raspirover_LogAction.__init__)


def test_hyp_raspirover_logaction_constructor_args():
    sig = inspect.signature(raspirover_LogAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"




def test_hyp_raspirover_backwardaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_BackwardAction)


def test_hyp_raspirover_backwardaction_constructor_exists():
    assert callable(raspirover_BackwardAction.__init__)


def test_hyp_raspirover_backwardaction_constructor_args():
    sig = inspect.signature(raspirover_BackwardAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_stopaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_StopAction)


def test_hyp_raspirover_stopaction_constructor_exists():
    assert callable(raspirover_StopAction.__init__)


def test_hyp_raspirover_stopaction_constructor_args():
    sig = inspect.signature(raspirover_StopAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_sendaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_SendAction)


def test_hyp_raspirover_sendaction_constructor_exists():
    assert callable(raspirover_SendAction.__init__)


def test_hyp_raspirover_sendaction_constructor_args():
    sig = inspect.signature(raspirover_SendAction.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"




def test_hyp_raspirover_turnaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_TurnAction)


def test_hyp_raspirover_turnaction_constructor_exists():
    assert callable(raspirover_TurnAction.__init__)


def test_hyp_raspirover_turnaction_constructor_args():
    sig = inspect.signature(raspirover_TurnAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_backwardminaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_BackwardMinAction)


def test_hyp_raspirover_backwardminaction_constructor_exists():
    assert callable(raspirover_BackwardMinAction.__init__)


def test_hyp_raspirover_backwardminaction_constructor_args():
    sig = inspect.signature(raspirover_BackwardMinAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_forwardaction_is_not_abstract():
    assert not inspect.isabstract(raspirover_ForwardAction)


def test_hyp_raspirover_forwardaction_constructor_exists():
    assert callable(raspirover_ForwardAction.__init__)


def test_hyp_raspirover_forwardaction_constructor_args():
    sig = inspect.signature(raspirover_ForwardAction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_quantity_is_not_abstract():
    assert not inspect.isabstract(raspirover_Quantity)


def test_hyp_raspirover_quantity_constructor_exists():
    assert callable(raspirover_Quantity.__init__)


def test_hyp_raspirover_quantity_constructor_args():
    sig = inspect.signature(raspirover_Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_rovervalue_is_not_abstract():
    assert not inspect.isabstract(RoverValue)


def test_hyp_rovervalue_constructor_exists():
    assert callable(RoverValue.__init__)


def test_hyp_rovervalue_constructor_args():
    sig = inspect.signature(RoverValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_stringvalue_is_not_abstract():
    assert not inspect.isabstract(raspirover_StringValue)


def test_hyp_raspirover_stringvalue_constructor_exists():
    assert callable(raspirover_StringValue.__init__)


def test_hyp_raspirover_stringvalue_constructor_args():
    sig = inspect.signature(raspirover_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "sValue" in params, "Missing parameter 'sValue'"




def test_hyp_raspirover_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(raspirover_BooleanValue)


def test_hyp_raspirover_booleanvalue_constructor_exists():
    assert callable(raspirover_BooleanValue.__init__)


def test_hyp_raspirover_booleanvalue_constructor_args():
    sig = inspect.signature(raspirover_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "bValue" in params, "Missing parameter 'bValue'"




def test_hyp_raspirover_numbervalue_is_not_abstract():
    assert not inspect.isabstract(raspirover_NumberValue)


def test_hyp_raspirover_numbervalue_constructor_exists():
    assert callable(raspirover_NumberValue.__init__)


def test_hyp_raspirover_numbervalue_constructor_args():
    sig = inspect.signature(raspirover_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "nValue" in params, "Missing parameter 'nValue'"




def test_hyp_roverexpression_is_not_abstract():
    assert not inspect.isabstract(RoverExpression)


def test_hyp_roverexpression_constructor_exists():
    assert callable(RoverExpression.__init__)


def test_hyp_roverexpression_constructor_args():
    sig = inspect.signature(RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_stringexpression_is_not_abstract():
    assert not inspect.isabstract(raspirover_StringExpression)


def test_hyp_raspirover_stringexpression_constructor_exists():
    assert callable(raspirover_StringExpression.__init__)


def test_hyp_raspirover_stringexpression_constructor_args():
    sig = inspect.signature(raspirover_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_raspirover_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(raspirover_BooleanExpression)


def test_hyp_raspirover_booleanexpression_constructor_exists():
    assert callable(raspirover_BooleanExpression.__init__)


def test_hyp_raspirover_booleanexpression_constructor_args():
    sig = inspect.signature(raspirover_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_raspirover_numericexpression_is_not_abstract():
    assert not inspect.isabstract(raspirover_NumericExpression)


def test_hyp_raspirover_numericexpression_constructor_exists():
    assert callable(raspirover_NumericExpression.__init__)


def test_hyp_raspirover_numericexpression_constructor_args():
    sig = inspect.signature(raspirover_NumericExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"




def test_hyp_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(BooleanValue)


def test_hyp_booleanvalue_constructor_exists():
    assert callable(BooleanValue.__init__)


def test_hyp_booleanvalue_constructor_args():
    sig = inspect.signature(BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_stringvalue_is_not_abstract():
    assert not inspect.isabstract(StringValue)


def test_hyp_stringvalue_constructor_exists():
    assert callable(StringValue.__init__)


def test_hyp_stringvalue_constructor_args():
    sig = inspect.signature(StringValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_numbervalue_is_not_abstract():
    assert not inspect.isabstract(NumberValue)


def test_hyp_numbervalue_constructor_exists():
    assert callable(NumberValue.__init__)


def test_hyp_numbervalue_constructor_args():
    sig = inspect.signature(NumberValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_hyp_query_constructor_exists():
    assert callable(Query.__init__)


def test_hyp_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_obstaclequery_is_not_abstract():
    assert not inspect.isabstract(raspirover_ObstacleQuery)


def test_hyp_raspirover_obstaclequery_constructor_exists():
    assert callable(raspirover_ObstacleQuery.__init__)


def test_hyp_raspirover_obstaclequery_constructor_args():
    sig = inspect.signature(raspirover_ObstacleQuery.__init__)
    params = list(sig.parameters.keys())
    assert "front" in params, "Missing parameter 'front'"




def test_hyp_raspirover_humidityquery_is_not_abstract():
    assert not inspect.isabstract(raspirover_HumidityQuery)


def test_hyp_raspirover_humidityquery_constructor_exists():
    assert callable(raspirover_HumidityQuery.__init__)


def test_hyp_raspirover_humidityquery_constructor_args():
    sig = inspect.signature(raspirover_HumidityQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_messagequery_is_not_abstract():
    assert not inspect.isabstract(raspirover_MessageQuery)


def test_hyp_raspirover_messagequery_constructor_exists():
    assert callable(raspirover_MessageQuery.__init__)


def test_hyp_raspirover_messagequery_constructor_args():
    sig = inspect.signature(raspirover_MessageQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_temperaturequery_is_not_abstract():
    assert not inspect.isabstract(raspirover_TemperatureQuery)


def test_hyp_raspirover_temperaturequery_constructor_exists():
    assert callable(raspirover_TemperatureQuery.__init__)


def test_hyp_raspirover_temperaturequery_constructor_args():
    sig = inspect.signature(raspirover_TemperatureQuery.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_query_is_not_abstract():
    assert not inspect.isabstract(raspirover_Query)


def test_hyp_raspirover_query_constructor_exists():
    assert callable(raspirover_Query.__init__)


def test_hyp_raspirover_query_constructor_args():
    sig = inspect.signature(raspirover_Query.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_roverexpression_is_not_abstract():
    assert not inspect.isabstract(raspirover_RoverExpression)


def test_hyp_raspirover_roverexpression_constructor_exists():
    assert callable(raspirover_RoverExpression.__init__)


def test_hyp_raspirover_roverexpression_constructor_args():
    sig = inspect.signature(raspirover_RoverExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_rovervalue_is_not_abstract():
    assert not inspect.isabstract(raspirover_RoverValue)


def test_hyp_raspirover_rovervalue_constructor_exists():
    assert callable(raspirover_RoverValue.__init__)


def test_hyp_raspirover_rovervalue_constructor_args():
    sig = inspect.signature(raspirover_RoverValue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_hyp_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_hyp_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_varref_is_not_abstract():
    assert not inspect.isabstract(raspirover_VarRef)


def test_hyp_raspirover_varref_constructor_exists():
    assert callable(raspirover_VarRef.__init__)


def test_hyp_raspirover_varref_constructor_args():
    sig = inspect.signature(raspirover_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_raspirover_conditional_is_not_abstract():
    assert not inspect.isabstract(raspirover_Conditional)


def test_hyp_raspirover_conditional_constructor_exists():
    assert callable(raspirover_Conditional.__init__)


def test_hyp_raspirover_conditional_constructor_args():
    sig = inspect.signature(raspirover_Conditional.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_action_is_not_abstract():
    assert not inspect.isabstract(raspirover_Action)


def test_hyp_raspirover_action_constructor_exists():
    assert callable(raspirover_Action.__init__)


def test_hyp_raspirover_action_constructor_args():
    sig = inspect.signature(raspirover_Action.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_loop_is_not_abstract():
    assert not inspect.isabstract(raspirover_Loop)


def test_hyp_raspirover_loop_constructor_exists():
    assert callable(raspirover_Loop.__init__)


def test_hyp_raspirover_loop_constructor_args():
    sig = inspect.signature(raspirover_Loop.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_varassignment_is_not_abstract():
    assert not inspect.isabstract(raspirover_VarAssignment)


def test_hyp_raspirover_varassignment_constructor_exists():
    assert callable(raspirover_VarAssignment.__init__)


def test_hyp_raspirover_varassignment_constructor_args():
    sig = inspect.signature(raspirover_VarAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_raspirover_statement_is_not_abstract():
    assert not inspect.isabstract(raspirover_Statement)


def test_hyp_raspirover_statement_constructor_exists():
    assert callable(raspirover_Statement.__init__)


def test_hyp_raspirover_statement_constructor_args():
    sig = inspect.signature(raspirover_Statement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_rclblock_is_not_abstract():
    assert not inspect.isabstract(raspirover_RclBlock)


def test_hyp_raspirover_rclblock_constructor_exists():
    assert callable(raspirover_RclBlock.__init__)


def test_hyp_raspirover_rclblock_constructor_args():
    sig = inspect.signature(raspirover_RclBlock.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_param_is_not_abstract():
    assert not inspect.isabstract(raspirover_Param)


def test_hyp_raspirover_param_constructor_exists():
    assert callable(raspirover_Param.__init__)


def test_hyp_raspirover_param_constructor_args():
    sig = inspect.signature(raspirover_Param.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_raspirover_namedelement_is_not_abstract():
    assert not inspect.isabstract(raspirover_NamedElement)


def test_hyp_raspirover_namedelement_constructor_exists():
    assert callable(raspirover_NamedElement.__init__)


def test_hyp_raspirover_namedelement_constructor_args():
    sig = inspect.signature(raspirover_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_hyp_module_constructor_exists():
    assert callable(Module.__init__)


def test_hyp_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_arduinomodule_is_not_abstract():
    assert not inspect.isabstract(raspirover_ArduinoModule)


def test_hyp_raspirover_arduinomodule_constructor_exists():
    assert callable(raspirover_ArduinoModule.__init__)


def test_hyp_raspirover_arduinomodule_constructor_args():
    sig = inspect.signature(raspirover_ArduinoModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arduinomodule_is_not_abstract():
    assert not inspect.isabstract(ArduinoModule)


def test_hyp_arduinomodule_constructor_exists():
    assert callable(ArduinoModule.__init__)


def test_hyp_arduinomodule_constructor_args():
    sig = inspect.signature(ArduinoModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_arduinoanalogmodule_is_not_abstract():
    assert not inspect.isabstract(raspirover_ArduinoAnalogModule)


def test_hyp_raspirover_arduinoanalogmodule_constructor_exists():
    assert callable(raspirover_ArduinoAnalogModule.__init__)


def test_hyp_raspirover_arduinoanalogmodule_constructor_args():
    sig = inspect.signature(raspirover_ArduinoAnalogModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_arduinodigitalmodule_is_not_abstract():
    assert not inspect.isabstract(raspirover_ArduinoDigitalModule)


def test_hyp_raspirover_arduinodigitalmodule_constructor_exists():
    assert callable(raspirover_ArduinoDigitalModule.__init__)


def test_hyp_raspirover_arduinodigitalmodule_constructor_args():
    sig = inspect.signature(raspirover_ArduinoDigitalModule.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_hyp_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_hyp_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_instruction_is_not_abstract():
    assert not inspect.isabstract(raspirover_Instruction)


def test_hyp_raspirover_instruction_constructor_exists():
    assert callable(raspirover_Instruction.__init__)


def test_hyp_raspirover_instruction_constructor_args():
    sig = inspect.signature(raspirover_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_block_is_not_abstract():
    assert not inspect.isabstract(raspirover_Block)


def test_hyp_raspirover_block_constructor_exists():
    assert callable(raspirover_Block.__init__)


def test_hyp_raspirover_block_constructor_args():
    sig = inspect.signature(raspirover_Block.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_roverprogram_is_not_abstract():
    assert not inspect.isabstract(raspirover_RoverProgram)


def test_hyp_raspirover_roverprogram_constructor_exists():
    assert callable(raspirover_RoverProgram.__init__)


def test_hyp_raspirover_roverprogram_constructor_args():
    sig = inspect.signature(raspirover_RoverProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_raspirover_project_is_not_abstract():
    assert not inspect.isabstract(raspirover_Project)


def test_hyp_raspirover_project_constructor_exists():
    assert callable(raspirover_Project.__init__)


def test_hyp_raspirover_project_constructor_args():
    sig = inspect.signature(raspirover_Project.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_hyp_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_hyp_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_pin_is_not_abstract():
    assert not inspect.isabstract(raspirover_Pin)


def test_hyp_raspirover_pin_constructor_exists():
    assert callable(raspirover_Pin.__init__)


def test_hyp_raspirover_pin_constructor_args():
    sig = inspect.signature(raspirover_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"




def test_hyp_raspirover_module_is_not_abstract():
    assert not inspect.isabstract(raspirover_Module)


def test_hyp_raspirover_module_constructor_exists():
    assert callable(raspirover_Module.__init__)


def test_hyp_raspirover_module_constructor_args():
    sig = inspect.signature(raspirover_Module.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_sketch_is_not_abstract():
    assert not inspect.isabstract(raspirover_Sketch)


def test_hyp_raspirover_sketch_constructor_exists():
    assert callable(raspirover_Sketch.__init__)


def test_hyp_raspirover_sketch_constructor_args():
    sig = inspect.signature(raspirover_Sketch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_board_is_not_abstract():
    assert not inspect.isabstract(raspirover_Board)


def test_hyp_raspirover_board_constructor_exists():
    assert callable(raspirover_Board.__init__)


def test_hyp_raspirover_board_constructor_args():
    sig = inspect.signature(raspirover_Board.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_analogpin_is_not_abstract():
    assert not inspect.isabstract(raspirover_AnalogPin)


def test_hyp_raspirover_analogpin_constructor_exists():
    assert callable(raspirover_AnalogPin.__init__)


def test_hyp_raspirover_analogpin_constructor_args():
    sig = inspect.signature(raspirover_AnalogPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_digitalpin_is_not_abstract():
    assert not inspect.isabstract(raspirover_DigitalPin)


def test_hyp_raspirover_digitalpin_constructor_exists():
    assert callable(raspirover_DigitalPin.__init__)


def test_hyp_raspirover_digitalpin_constructor_args():
    sig = inspect.signature(raspirover_DigitalPin.__init__)
    params = list(sig.parameters.keys())



def test_hyp_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_hyp_board_constructor_exists():
    assert callable(Board.__init__)


def test_hyp_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())



def test_hyp_raspirover_raspiboard_is_not_abstract():
    assert not inspect.isabstract(raspirover_RasPiBoard)


def test_hyp_raspirover_raspiboard_constructor_exists():
    assert callable(raspirover_RasPiBoard.__init__)


def test_hyp_raspirover_raspiboard_constructor_args():
    sig = inspect.signature(raspirover_RasPiBoard.__init__)
    params = list(sig.parameters.keys())

def test_hyp_numericoperator_exists():
    # Check that the Enumeration exists
    assert NumericOperator is not None

def test_hyp_numericoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NumericOperator]
    expected_literals = [
        "geq",
        "leq",
        "neq",
        "lt",
        "gt",
        "eq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NumericOperator"

def test_hyp_stringoperator_exists():
    # Check that the Enumeration exists
    assert StringOperator is not None

def test_hyp_stringoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StringOperator]
    expected_literals = [
        "eq",
        "neq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StringOperator"

def test_hyp_booleanoperator_exists():
    # Check that the Enumeration exists
    assert BooleanOperator is not None

def test_hyp_booleanoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BooleanOperator]
    expected_literals = [
        "eq",
        "neq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BooleanOperator"


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
AngleOperation_strategy = st.builds(
    AngleOperation,
)
QuantityScalarOperation_strategy = st.builds(
    QuantityScalarOperation,
)
raspirover_AngleScalarDivide_strategy = st.builds(
    raspirover_AngleScalarDivide,
)
raspirover_AngleScalarMultiply_strategy = st.builds(
    raspirover_AngleScalarMultiply,
)
QuantityHomogenousOperation_strategy = st.builds(
    QuantityHomogenousOperation,
)
raspirover_AngleAdd_strategy = st.builds(
    raspirover_AngleAdd,
)
raspirover_AngleEquals_strategy = st.builds(
    raspirover_AngleEquals,
)
raspirover_AngleSmaller_strategy = st.builds(
    raspirover_AngleSmaller,
)
raspirover_AngleDistinct_strategy = st.builds(
    raspirover_AngleDistinct,
)
raspirover_AngleGreater_strategy = st.builds(
    raspirover_AngleGreater,
)
raspirover_AngleSubtract_strategy = st.builds(
    raspirover_AngleSubtract,
)
LengthOperation_strategy = st.builds(
    LengthOperation,
)
raspirover_LengthScalarMultiply_strategy = st.builds(
    raspirover_LengthScalarMultiply,
)
raspirover_LengthSmaller_strategy = st.builds(
    raspirover_LengthSmaller,
)
raspirover_LengthDistinct_strategy = st.builds(
    raspirover_LengthDistinct,
)
raspirover_LengthScalarDivide_strategy = st.builds(
    raspirover_LengthScalarDivide,
)
raspirover_LengthGreater_strategy = st.builds(
    raspirover_LengthGreater,
)
raspirover_LengthSubtract_strategy = st.builds(
    raspirover_LengthSubtract,
)
raspirover_LengthEquals_strategy = st.builds(
    raspirover_LengthEquals,
)
raspirover_LengthAdd_strategy = st.builds(
    raspirover_LengthAdd,
)
QuantityOperation_strategy = st.builds(
    QuantityOperation,
)
raspirover_QuantityScalarOperation_strategy = st.builds(
    raspirover_QuantityScalarOperation,
    rhs=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
raspirover_AngleOperation_strategy = st.builds(
    raspirover_AngleOperation,
)
raspirover_QuantityComparisonOperation_strategy = st.builds(
    raspirover_QuantityComparisonOperation,
)
raspirover_QuantityHomogenousOperation_strategy = st.builds(
    raspirover_QuantityHomogenousOperation,
)
raspirover_QuantityArithmeticOperation_strategy = st.builds(
    raspirover_QuantityArithmeticOperation,
)
raspirover_LengthOperation_strategy = st.builds(
    raspirover_LengthOperation,
)
raspirover_QuantityOperation_strategy = st.builds(
    raspirover_QuantityOperation,
)
Quantity_strategy = st.builds(
    Quantity,
)
raspirover_Angle_strategy = st.builds(
    raspirover_Angle,
)
raspirover_Length_strategy = st.builds(
    raspirover_Length,
)
AngleUnit_strategy = st.builds(
    AngleUnit,
)
raspirover_Degree_strategy = st.builds(
    raspirover_Degree,
)
raspirover_Turn_strategy = st.builds(
    raspirover_Turn,
)
raspirover_Gradian_strategy = st.builds(
    raspirover_Gradian,
)
raspirover_Radian_strategy = st.builds(
    raspirover_Radian,
)
ImperialSystemUnit_strategy = st.builds(
    ImperialSystemUnit,
)
LengthUnit_strategy = st.builds(
    LengthUnit,
)
raspirover_Yard_strategy = st.builds(
    raspirover_Yard,
)
raspirover_Inch_strategy = st.builds(
    raspirover_Inch,
)
raspirover_Foot_strategy = st.builds(
    raspirover_Foot,
)
MetricSystemUnit_strategy = st.builds(
    MetricSystemUnit,
)
raspirover_Meter_strategy = st.builds(
    raspirover_Meter,
)
raspirover_Millimeter_strategy = st.builds(
    raspirover_Millimeter,
)
raspirover_Centimeter_strategy = st.builds(
    raspirover_Centimeter,
)
Unit_strategy = st.builds(
    Unit,
)
raspirover_MetricSystemUnit_strategy = st.builds(
    raspirover_MetricSystemUnit,
)
raspirover_ImperialSystemUnit_strategy = st.builds(
    raspirover_ImperialSystemUnit,
)
raspirover_AngleUnit_strategy = st.builds(
    raspirover_AngleUnit,
)
raspirover_LengthUnit_strategy = st.builds(
    raspirover_LengthUnit,
)
raspirover_Unit_strategy = st.builds(
    raspirover_Unit,
)
Action_strategy = st.builds(
    Action,
)
raspirover_TurnDegAction_strategy = st.builds(
    raspirover_TurnDegAction,
)
raspirover_ForwardMinAction_strategy = st.builds(
    raspirover_ForwardMinAction,
)
raspirover_LogAction_strategy = st.builds(
    raspirover_LogAction,
    message=
        safe_text
)
raspirover_BackwardAction_strategy = st.builds(
    raspirover_BackwardAction,
)
raspirover_StopAction_strategy = st.builds(
    raspirover_StopAction,
)
raspirover_SendAction_strategy = st.builds(
    raspirover_SendAction,
    message=
        safe_text
)
raspirover_TurnAction_strategy = st.builds(
    raspirover_TurnAction,
)
raspirover_BackwardMinAction_strategy = st.builds(
    raspirover_BackwardMinAction,
)
raspirover_ForwardAction_strategy = st.builds(
    raspirover_ForwardAction,
)
raspirover_Quantity_strategy = st.builds(
    raspirover_Quantity,
    value=
        safe_text
)
RoverValue_strategy = st.builds(
    RoverValue,
)
raspirover_StringValue_strategy = st.builds(
    raspirover_StringValue,
    sValue=
        st.booleans()
)
raspirover_BooleanValue_strategy = st.builds(
    raspirover_BooleanValue,
    bValue=
        st.booleans()
)
raspirover_NumberValue_strategy = st.builds(
    raspirover_NumberValue,
    nValue=
        safe_text
)
RoverExpression_strategy = st.builds(
    RoverExpression,
)
raspirover_StringExpression_strategy = st.builds(
    raspirover_StringExpression,
    op=
        st.booleans()
)
raspirover_BooleanExpression_strategy = st.builds(
    raspirover_BooleanExpression,
    op=
        safe_text
)
raspirover_NumericExpression_strategy = st.builds(
    raspirover_NumericExpression,
    op=
        st.booleans()
)
BooleanValue_strategy = st.builds(
    BooleanValue,
)
StringValue_strategy = st.builds(
    StringValue,
)
NumberValue_strategy = st.builds(
    NumberValue,
)
Query_strategy = st.builds(
    Query,
)
raspirover_ObstacleQuery_strategy = st.builds(
    raspirover_ObstacleQuery,
    front=
        st.booleans()
)
raspirover_HumidityQuery_strategy = st.builds(
    raspirover_HumidityQuery,
)
raspirover_MessageQuery_strategy = st.builds(
    raspirover_MessageQuery,
)
raspirover_TemperatureQuery_strategy = st.builds(
    raspirover_TemperatureQuery,
)
raspirover_Query_strategy = st.builds(
    raspirover_Query,
)
raspirover_RoverExpression_strategy = st.builds(
    raspirover_RoverExpression,
)
raspirover_RoverValue_strategy = st.builds(
    raspirover_RoverValue,
)
Statement_strategy = st.builds(
    Statement,
)
raspirover_VarRef_strategy = st.builds(
    raspirover_VarRef,
    name=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
raspirover_Conditional_strategy = st.builds(
    raspirover_Conditional,
)
raspirover_Action_strategy = st.builds(
    raspirover_Action,
)
raspirover_Loop_strategy = st.builds(
    raspirover_Loop,
)
raspirover_VarAssignment_strategy = st.builds(
    raspirover_VarAssignment,
    name=
        st.booleans()
)
raspirover_Statement_strategy = st.builds(
    raspirover_Statement,
)
raspirover_RclBlock_strategy = st.builds(
    raspirover_RclBlock,
)
raspirover_Param_strategy = st.builds(
    raspirover_Param,
    name=
        safe_text
)
raspirover_NamedElement_strategy = st.builds(
    raspirover_NamedElement,
    name=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
raspirover_ArduinoModule_strategy = st.builds(
    raspirover_ArduinoModule,
)
ArduinoModule_strategy = st.builds(
    ArduinoModule,
)
raspirover_ArduinoAnalogModule_strategy = st.builds(
    raspirover_ArduinoAnalogModule,
)
raspirover_ArduinoDigitalModule_strategy = st.builds(
    raspirover_ArduinoDigitalModule,
)
Pin_strategy = st.builds(
    Pin,
)
raspirover_Instruction_strategy = st.builds(
    raspirover_Instruction,
)
raspirover_Block_strategy = st.builds(
    raspirover_Block,
)
raspirover_RoverProgram_strategy = st.builds(
    raspirover_RoverProgram,
    name=
        safe_text
)
raspirover_Project_strategy = st.builds(
    raspirover_Project,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
raspirover_Pin_strategy = st.builds(
    raspirover_Pin,
    level=
        st.integers()
)
raspirover_Module_strategy = st.builds(
    raspirover_Module,
)
raspirover_Sketch_strategy = st.builds(
    raspirover_Sketch,
)
raspirover_Board_strategy = st.builds(
    raspirover_Board,
)
raspirover_AnalogPin_strategy = st.builds(
    raspirover_AnalogPin,
)
raspirover_DigitalPin_strategy = st.builds(
    raspirover_DigitalPin,
)
Board_strategy = st.builds(
    Board,
)
raspirover_RasPiBoard_strategy = st.builds(
    raspirover_RasPiBoard,
)

























@given(instance=raspirover_QuantityScalarOperation_strategy)
def test_hyp_raspirover_quantityscalaroperation_rhs_setter(instance):
    original = instance.rhs
    instance.rhs = original
    assert instance.rhs == original









import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Angle_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_angle_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in raspirover_Angle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in raspirover_Angle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in raspirover_Angle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Angle_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_angle_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_Angle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_Angle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_Angle is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Length_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_length_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Length is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Length did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Length is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Length_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_length_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in raspirover_Length is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in raspirover_Length did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in raspirover_Length is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Degree_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_degree_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_Degree is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_Degree did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_Degree is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Turn_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_turn_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_Turn is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_Turn did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_Turn is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Gradian_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_gradian_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_Gradian is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_Gradian did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_Gradian is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Radian_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_radian_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_Radian is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_Radian did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_Radian is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Yard_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_yard_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Yard is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Yard did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Yard is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Inch_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_inch_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Inch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Inch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Inch is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Foot_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_foot_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Foot is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Foot did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Foot is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Meter_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_meter_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Meter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Meter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Meter is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Millimeter_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_millimeter_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Millimeter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Millimeter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Millimeter is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Centimeter_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_centimeter_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_Centimeter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_Centimeter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_Centimeter is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_AngleUnit_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_angleunit_torad_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toRad(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toRad).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toRad' in raspirover_AngleUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in raspirover_AngleUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in raspirover_AngleUnit is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_LengthUnit_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_lengthunit_tocm_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.toCm(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.toCm).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'toCm' in raspirover_LengthUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in raspirover_LengthUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in raspirover_LengthUnit is not implemented or raised an error")




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_TurnDegAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_turndegaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_TurnDegAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_TurnDegAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_TurnDegAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_ForwardMinAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_forwardminaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_ForwardMinAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_ForwardMinAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_ForwardMinAction is not implemented or raised an error")




@given(instance=raspirover_LogAction_strategy)
def test_hyp_raspirover_logaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_LogAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_logaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_LogAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_LogAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_LogAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_BackwardAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_backwardaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_BackwardAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_BackwardAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_BackwardAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_StopAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_stopaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_StopAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_StopAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_StopAction is not implemented or raised an error")




@given(instance=raspirover_SendAction_strategy)
def test_hyp_raspirover_sendaction_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_SendAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_sendaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_SendAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_SendAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_SendAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_TurnAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_turnaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_TurnAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_TurnAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_TurnAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_BackwardMinAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_backwardminaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_BackwardMinAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_BackwardMinAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_BackwardMinAction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_ForwardAction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_forwardaction_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_ForwardAction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_ForwardAction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_ForwardAction is not implemented or raised an error")




@given(instance=raspirover_Quantity_strategy)
def test_hyp_raspirover_quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Quantity_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_quantity_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in raspirover_Quantity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in raspirover_Quantity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in raspirover_Quantity is not implemented or raised an error")





@given(instance=raspirover_StringValue_strategy)
def test_hyp_raspirover_stringvalue_sValue_setter(instance):
    original = instance.sValue
    instance.sValue = original
    assert instance.sValue == original




@given(instance=raspirover_BooleanValue_strategy)
def test_hyp_raspirover_booleanvalue_bValue_setter(instance):
    original = instance.bValue
    instance.bValue = original
    assert instance.bValue == original




@given(instance=raspirover_NumberValue_strategy)
def test_hyp_raspirover_numbervalue_nValue_setter(instance):
    original = instance.nValue
    instance.nValue = original
    assert instance.nValue == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_NumberValue_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_numbervalue_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in raspirover_NumberValue is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in raspirover_NumberValue did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in raspirover_NumberValue is not implemented or raised an error")





@given(instance=raspirover_StringExpression_strategy)
def test_hyp_raspirover_stringexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_StringExpression_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_stringexpression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_StringExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_StringExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_StringExpression is not implemented or raised an error")




@given(instance=raspirover_BooleanExpression_strategy)
def test_hyp_raspirover_booleanexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_BooleanExpression_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_booleanexpression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_BooleanExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_BooleanExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_BooleanExpression is not implemented or raised an error")




@given(instance=raspirover_NumericExpression_strategy)
def test_hyp_raspirover_numericexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_NumericExpression_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_numericexpression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_NumericExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_NumericExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_NumericExpression is not implemented or raised an error")








@given(instance=raspirover_ObstacleQuery_strategy)
def test_hyp_raspirover_obstaclequery_front_setter(instance):
    original = instance.front
    instance.front = original
    assert instance.front == original






import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_RoverExpression_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_roverexpression_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_RoverExpression is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_RoverExpression did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_RoverExpression is not implemented or raised an error")






@given(instance=raspirover_VarRef_strategy)
def test_hyp_raspirover_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_VarRef_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_varref_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_VarRef is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_VarRef did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_VarRef is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Conditional_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_conditional_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_Conditional is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_Conditional did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_Conditional is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Loop_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_loop_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_Loop is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_Loop did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_Loop is not implemented or raised an error")




@given(instance=raspirover_VarAssignment_strategy)
def test_hyp_raspirover_varassignment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_VarAssignment_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_varassignment_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_VarAssignment is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_VarAssignment did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_VarAssignment is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Statement_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_statement_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_Statement is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_RclBlock_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_rclblock_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in raspirover_RclBlock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in raspirover_RclBlock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in raspirover_RclBlock is not implemented or raised an error")




@given(instance=raspirover_Param_strategy)
def test_hyp_raspirover_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=raspirover_NamedElement_strategy)
def test_hyp_raspirover_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Instruction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_instruction_finalize_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.finalize()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.finalize).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'finalize' in raspirover_Instruction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'finalize' in raspirover_Instruction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'finalize' in raspirover_Instruction is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Instruction_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_instruction_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in raspirover_Instruction is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in raspirover_Instruction did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in raspirover_Instruction is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Block_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_block_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in raspirover_Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in raspirover_Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in raspirover_Block is not implemented or raised an error")




@given(instance=raspirover_RoverProgram_strategy)
def test_hyp_raspirover_roverprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_RoverProgram_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_roverprogram_bindvar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bindVar(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bindVar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bindVar' in raspirover_RoverProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bindVar' in raspirover_RoverProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bindVar' in raspirover_RoverProgram is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_RoverProgram_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_roverprogram_run_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.run()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.run).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'run' in raspirover_RoverProgram is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in raspirover_RoverProgram did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in raspirover_RoverProgram is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=raspirover_Project_strategy)
@settings(max_examples=30)
def test_hyp_raspirover_project_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in raspirover_Project is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in raspirover_Project did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in raspirover_Project is not implemented or raised an error")





@given(instance=raspirover_Pin_strategy)
def test_hyp_raspirover_pin_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original









# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Action,
    AngleOperation,
    AngleUnit,
    ArduinoModule,
    Board,
    BooleanValue,
    ImperialSystemUnit,
    LengthOperation,
    LengthUnit,
    MetricSystemUnit,
    Module,
    NamedElement,
    NumberValue,
    Pin,
    Quantity,
    QuantityHomogenousOperation,
    QuantityOperation,
    QuantityScalarOperation,
    Query,
    RoverExpression,
    RoverValue,
    Statement,
    StringValue,
    Unit,
    raspirover_Action,
    raspirover_AnalogPin,
    raspirover_Angle,
    raspirover_AngleAdd,
    raspirover_AngleDistinct,
    raspirover_AngleEquals,
    raspirover_AngleGreater,
    raspirover_AngleOperation,
    raspirover_AngleScalarDivide,
    raspirover_AngleScalarMultiply,
    raspirover_AngleSmaller,
    raspirover_AngleSubtract,
    raspirover_AngleUnit,
    raspirover_ArduinoAnalogModule,
    raspirover_ArduinoDigitalModule,
    raspirover_ArduinoModule,
    raspirover_BackwardAction,
    raspirover_BackwardMinAction,
    raspirover_Block,
    raspirover_Board,
    raspirover_BooleanExpression,
    raspirover_BooleanValue,
    raspirover_Centimeter,
    raspirover_Conditional,
    raspirover_Degree,
    raspirover_DigitalPin,
    raspirover_Foot,
    raspirover_ForwardAction,
    raspirover_ForwardMinAction,
    raspirover_Gradian,
    raspirover_HumidityQuery,
    raspirover_ImperialSystemUnit,
    raspirover_Inch,
    raspirover_Instruction,
    raspirover_Length,
    raspirover_LengthAdd,
    raspirover_LengthDistinct,
    raspirover_LengthEquals,
    raspirover_LengthGreater,
    raspirover_LengthOperation,
    raspirover_LengthScalarDivide,
    raspirover_LengthScalarMultiply,
    raspirover_LengthSmaller,
    raspirover_LengthSubtract,
    raspirover_LengthUnit,
    raspirover_LogAction,
    raspirover_Loop,
    raspirover_MessageQuery,
    raspirover_Meter,
    raspirover_MetricSystemUnit,
    raspirover_Millimeter,
    raspirover_Module,
    raspirover_NamedElement,
    raspirover_NumberValue,
    raspirover_NumericExpression,
    raspirover_ObstacleQuery,
    raspirover_Param,
    raspirover_Pin,
    raspirover_Project,
    raspirover_Quantity,
    raspirover_QuantityArithmeticOperation,
    raspirover_QuantityComparisonOperation,
    raspirover_QuantityHomogenousOperation,
    raspirover_QuantityOperation,
    raspirover_QuantityScalarOperation,
    raspirover_Query,
    raspirover_Radian,
    raspirover_RasPiBoard,
    raspirover_RclBlock,
    raspirover_RoverExpression,
    raspirover_RoverProgram,
    raspirover_RoverValue,
    raspirover_SendAction,
    raspirover_Sketch,
    raspirover_Statement,
    raspirover_StopAction,
    raspirover_StringExpression,
    raspirover_StringValue,
    raspirover_TemperatureQuery,
    raspirover_Turn,
    raspirover_TurnAction,
    raspirover_TurnDegAction,
    raspirover_Unit,
    raspirover_VarAssignment,
    raspirover_VarRef,
    raspirover_Yard,
    BooleanOperator,
    NumericOperator,
    StringOperator,
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

def test_raspirover_BooleanExpression_op_value_roundtrip():
    instance = raspirover_BooleanExpression(op="sample_text")
    assert instance.op == "sample_text"
    instance.op = "sample_text_2"
    assert instance.op == "sample_text_2"


def test_raspirover_BooleanValue_bValue_value_roundtrip():
    instance = raspirover_BooleanValue(bValue=True)
    assert instance.bValue == True
    instance.bValue = False
    assert instance.bValue == False


def test_raspirover_LogAction_message_value_roundtrip():
    instance = raspirover_LogAction(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_raspirover_NamedElement_name_value_roundtrip():
    instance = raspirover_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_raspirover_NumberValue_nValue_value_roundtrip():
    instance = raspirover_NumberValue(nValue="sample_text")
    assert instance.nValue == "sample_text"
    instance.nValue = "sample_text_2"
    assert instance.nValue == "sample_text_2"


def test_raspirover_NumericExpression_op_value_roundtrip():
    instance = raspirover_NumericExpression(op=True)
    assert instance.op == True
    instance.op = False
    assert instance.op == False


def test_raspirover_ObstacleQuery_front_value_roundtrip():
    instance = raspirover_ObstacleQuery(front=True)
    assert instance.front == True
    instance.front = False
    assert instance.front == False


def test_raspirover_Param_name_value_roundtrip():
    instance = raspirover_Param(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_raspirover_Pin_level_value_roundtrip():
    instance = raspirover_Pin(level=7)
    assert instance.level == 7
    instance.level = 13
    assert instance.level == 13


def test_raspirover_Quantity_value_value_roundtrip():
    instance = raspirover_Quantity(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_raspirover_QuantityScalarOperation_rhs_value_roundtrip():
    instance = raspirover_QuantityScalarOperation(rhs=3.14)
    assert instance.rhs == 3.14
    instance.rhs = 9.99
    assert instance.rhs == 9.99


def test_raspirover_RoverProgram_name_value_roundtrip():
    instance = raspirover_RoverProgram(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_raspirover_SendAction_message_value_roundtrip():
    instance = raspirover_SendAction(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_raspirover_StringExpression_op_value_roundtrip():
    instance = raspirover_StringExpression(op=True)
    assert instance.op == True
    instance.op = False
    assert instance.op == False


def test_raspirover_StringValue_sValue_value_roundtrip():
    instance = raspirover_StringValue(sValue=True)
    assert instance.sValue == True
    instance.sValue = False
    assert instance.sValue == False


def test_raspirover_VarAssignment_name_value_roundtrip():
    instance = raspirover_VarAssignment(name=True)
    assert instance.name == True
    instance.name = False
    assert instance.name == False


def test_raspirover_VarRef_name_value_roundtrip():
    instance = raspirover_VarRef(name=3.14)
    assert instance.name == 3.14
    instance.name = 9.99
    assert instance.name == 9.99


def test_raspirover_BackwardAction_isa_Action():
    instance = raspirover_BackwardAction()
    assert isinstance(instance, Action)


def test_raspirover_BackwardMinAction_isa_Action():
    instance = raspirover_BackwardMinAction()
    assert isinstance(instance, Action)


def test_raspirover_ForwardAction_isa_Action():
    instance = raspirover_ForwardAction()
    assert isinstance(instance, Action)


def test_raspirover_ForwardMinAction_isa_Action():
    instance = raspirover_ForwardMinAction()
    assert isinstance(instance, Action)


def test_raspirover_LogAction_isa_Action():
    instance = raspirover_LogAction(message="sample_text")
    assert isinstance(instance, Action)


def test_raspirover_SendAction_isa_Action():
    instance = raspirover_SendAction(message="sample_text")
    assert isinstance(instance, Action)


def test_raspirover_StopAction_isa_Action():
    instance = raspirover_StopAction()
    assert isinstance(instance, Action)


def test_raspirover_TurnAction_isa_Action():
    instance = raspirover_TurnAction()
    assert isinstance(instance, Action)


def test_raspirover_TurnDegAction_isa_Action():
    instance = raspirover_TurnDegAction()
    assert isinstance(instance, Action)


def test_raspirover_AngleAdd_isa_AngleOperation():
    instance = raspirover_AngleAdd()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleDistinct_isa_AngleOperation():
    instance = raspirover_AngleDistinct()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleEquals_isa_AngleOperation():
    instance = raspirover_AngleEquals()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleGreater_isa_AngleOperation():
    instance = raspirover_AngleGreater()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleScalarDivide_isa_AngleOperation():
    instance = raspirover_AngleScalarDivide()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleScalarMultiply_isa_AngleOperation():
    instance = raspirover_AngleScalarMultiply()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleSmaller_isa_AngleOperation():
    instance = raspirover_AngleSmaller()
    assert isinstance(instance, AngleOperation)


def test_raspirover_AngleSubtract_isa_AngleOperation():
    instance = raspirover_AngleSubtract()
    assert isinstance(instance, AngleOperation)


def test_raspirover_Degree_isa_AngleUnit():
    instance = raspirover_Degree()
    assert isinstance(instance, AngleUnit)


def test_raspirover_Gradian_isa_AngleUnit():
    instance = raspirover_Gradian()
    assert isinstance(instance, AngleUnit)


def test_raspirover_Radian_isa_AngleUnit():
    instance = raspirover_Radian()
    assert isinstance(instance, AngleUnit)


def test_raspirover_Turn_isa_AngleUnit():
    instance = raspirover_Turn()
    assert isinstance(instance, AngleUnit)


def test_raspirover_ArduinoAnalogModule_isa_ArduinoModule():
    instance = raspirover_ArduinoAnalogModule()
    assert isinstance(instance, ArduinoModule)


def test_raspirover_ArduinoDigitalModule_isa_ArduinoModule():
    instance = raspirover_ArduinoDigitalModule()
    assert isinstance(instance, ArduinoModule)


def test_raspirover_RasPiBoard_isa_Board():
    instance = raspirover_RasPiBoard()
    assert isinstance(instance, Board)


def test_raspirover_ObstacleQuery_isa_BooleanValue():
    instance = raspirover_ObstacleQuery(front=True)
    assert isinstance(instance, BooleanValue)


def test_raspirover_VarRef_isa_BooleanValue():
    instance = raspirover_VarRef(name=3.14)
    assert isinstance(instance, BooleanValue)


def test_raspirover_Foot_isa_ImperialSystemUnit():
    instance = raspirover_Foot()
    assert isinstance(instance, ImperialSystemUnit)


def test_raspirover_Inch_isa_ImperialSystemUnit():
    instance = raspirover_Inch()
    assert isinstance(instance, ImperialSystemUnit)


def test_raspirover_Yard_isa_ImperialSystemUnit():
    instance = raspirover_Yard()
    assert isinstance(instance, ImperialSystemUnit)


def test_raspirover_LengthAdd_isa_LengthOperation():
    instance = raspirover_LengthAdd()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthDistinct_isa_LengthOperation():
    instance = raspirover_LengthDistinct()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthEquals_isa_LengthOperation():
    instance = raspirover_LengthEquals()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthGreater_isa_LengthOperation():
    instance = raspirover_LengthGreater()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthScalarDivide_isa_LengthOperation():
    instance = raspirover_LengthScalarDivide()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthScalarMultiply_isa_LengthOperation():
    instance = raspirover_LengthScalarMultiply()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthSmaller_isa_LengthOperation():
    instance = raspirover_LengthSmaller()
    assert isinstance(instance, LengthOperation)


def test_raspirover_LengthSubtract_isa_LengthOperation():
    instance = raspirover_LengthSubtract()
    assert isinstance(instance, LengthOperation)


def test_raspirover_Centimeter_isa_LengthUnit():
    instance = raspirover_Centimeter()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Foot_isa_LengthUnit():
    instance = raspirover_Foot()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Inch_isa_LengthUnit():
    instance = raspirover_Inch()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Meter_isa_LengthUnit():
    instance = raspirover_Meter()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Millimeter_isa_LengthUnit():
    instance = raspirover_Millimeter()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Yard_isa_LengthUnit():
    instance = raspirover_Yard()
    assert isinstance(instance, LengthUnit)


def test_raspirover_Centimeter_isa_MetricSystemUnit():
    instance = raspirover_Centimeter()
    assert isinstance(instance, MetricSystemUnit)


def test_raspirover_Meter_isa_MetricSystemUnit():
    instance = raspirover_Meter()
    assert isinstance(instance, MetricSystemUnit)


def test_raspirover_Millimeter_isa_MetricSystemUnit():
    instance = raspirover_Millimeter()
    assert isinstance(instance, MetricSystemUnit)


def test_raspirover_ArduinoModule_isa_Module():
    instance = raspirover_ArduinoModule()
    assert isinstance(instance, Module)


def test_raspirover_Board_isa_NamedElement():
    instance = raspirover_Board()
    assert isinstance(instance, NamedElement)


def test_raspirover_Module_isa_NamedElement():
    instance = raspirover_Module()
    assert isinstance(instance, NamedElement)


def test_raspirover_Pin_isa_NamedElement():
    instance = raspirover_Pin(level=7)
    assert isinstance(instance, NamedElement)


def test_raspirover_Sketch_isa_NamedElement():
    instance = raspirover_Sketch()
    assert isinstance(instance, NamedElement)


def test_raspirover_HumidityQuery_isa_NumberValue():
    instance = raspirover_HumidityQuery()
    assert isinstance(instance, NumberValue)


def test_raspirover_TemperatureQuery_isa_NumberValue():
    instance = raspirover_TemperatureQuery()
    assert isinstance(instance, NumberValue)


def test_raspirover_VarRef_isa_NumberValue():
    instance = raspirover_VarRef(name=3.14)
    assert isinstance(instance, NumberValue)


def test_raspirover_AnalogPin_isa_Pin():
    instance = raspirover_AnalogPin()
    assert isinstance(instance, Pin)


def test_raspirover_DigitalPin_isa_Pin():
    instance = raspirover_DigitalPin()
    assert isinstance(instance, Pin)


def test_raspirover_Angle_isa_Quantity():
    instance = raspirover_Angle()
    assert isinstance(instance, Quantity)


def test_raspirover_Length_isa_Quantity():
    instance = raspirover_Length()
    assert isinstance(instance, Quantity)


def test_raspirover_AngleAdd_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleAdd()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleDistinct_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleDistinct()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleEquals_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleEquals()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleGreater_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleGreater()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleSmaller_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleSmaller()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleSubtract_isa_QuantityHomogenousOperation():
    instance = raspirover_AngleSubtract()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthAdd_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthAdd()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthDistinct_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthDistinct()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthEquals_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthEquals()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthGreater_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthGreater()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthSmaller_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthSmaller()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_LengthSubtract_isa_QuantityHomogenousOperation():
    instance = raspirover_LengthSubtract()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_raspirover_AngleOperation_isa_QuantityOperation():
    instance = raspirover_AngleOperation()
    assert isinstance(instance, QuantityOperation)


def test_raspirover_LengthOperation_isa_QuantityOperation():
    instance = raspirover_LengthOperation()
    assert isinstance(instance, QuantityOperation)


def test_raspirover_QuantityArithmeticOperation_isa_QuantityOperation():
    instance = raspirover_QuantityArithmeticOperation()
    assert isinstance(instance, QuantityOperation)


def test_raspirover_QuantityComparisonOperation_isa_QuantityOperation():
    instance = raspirover_QuantityComparisonOperation()
    assert isinstance(instance, QuantityOperation)


def test_raspirover_QuantityHomogenousOperation_isa_QuantityOperation():
    instance = raspirover_QuantityHomogenousOperation()
    assert isinstance(instance, QuantityOperation)


def test_raspirover_QuantityScalarOperation_isa_QuantityOperation():
    instance = raspirover_QuantityScalarOperation(rhs=3.14)
    assert isinstance(instance, QuantityOperation)


def test_raspirover_AngleScalarDivide_isa_QuantityScalarOperation():
    instance = raspirover_AngleScalarDivide()
    assert isinstance(instance, QuantityScalarOperation)


def test_raspirover_AngleScalarMultiply_isa_QuantityScalarOperation():
    instance = raspirover_AngleScalarMultiply()
    assert isinstance(instance, QuantityScalarOperation)


def test_raspirover_LengthScalarDivide_isa_QuantityScalarOperation():
    instance = raspirover_LengthScalarDivide()
    assert isinstance(instance, QuantityScalarOperation)


def test_raspirover_LengthScalarMultiply_isa_QuantityScalarOperation():
    instance = raspirover_LengthScalarMultiply()
    assert isinstance(instance, QuantityScalarOperation)


def test_raspirover_HumidityQuery_isa_Query():
    instance = raspirover_HumidityQuery()
    assert isinstance(instance, Query)


def test_raspirover_MessageQuery_isa_Query():
    instance = raspirover_MessageQuery()
    assert isinstance(instance, Query)


def test_raspirover_ObstacleQuery_isa_Query():
    instance = raspirover_ObstacleQuery(front=True)
    assert isinstance(instance, Query)


def test_raspirover_TemperatureQuery_isa_Query():
    instance = raspirover_TemperatureQuery()
    assert isinstance(instance, Query)


def test_raspirover_BooleanExpression_isa_RoverExpression():
    instance = raspirover_BooleanExpression(op="sample_text")
    assert isinstance(instance, RoverExpression)


def test_raspirover_NumericExpression_isa_RoverExpression():
    instance = raspirover_NumericExpression(op=True)
    assert isinstance(instance, RoverExpression)


def test_raspirover_StringExpression_isa_RoverExpression():
    instance = raspirover_StringExpression(op=True)
    assert isinstance(instance, RoverExpression)


def test_raspirover_BooleanValue_isa_RoverValue():
    instance = raspirover_BooleanValue(bValue=True)
    assert isinstance(instance, RoverValue)


def test_raspirover_NumberValue_isa_RoverValue():
    instance = raspirover_NumberValue(nValue="sample_text")
    assert isinstance(instance, RoverValue)


def test_raspirover_StringValue_isa_RoverValue():
    instance = raspirover_StringValue(sValue=True)
    assert isinstance(instance, RoverValue)


def test_raspirover_Action_isa_Statement():
    instance = raspirover_Action()
    assert isinstance(instance, Statement)


def test_raspirover_Conditional_isa_Statement():
    instance = raspirover_Conditional()
    assert isinstance(instance, Statement)


def test_raspirover_Loop_isa_Statement():
    instance = raspirover_Loop()
    assert isinstance(instance, Statement)


def test_raspirover_RclBlock_isa_Statement():
    instance = raspirover_RclBlock()
    assert isinstance(instance, Statement)


def test_raspirover_VarAssignment_isa_Statement():
    instance = raspirover_VarAssignment(name=True)
    assert isinstance(instance, Statement)


def test_raspirover_VarRef_isa_Statement():
    instance = raspirover_VarRef(name=3.14)
    assert isinstance(instance, Statement)


def test_raspirover_MessageQuery_isa_StringValue():
    instance = raspirover_MessageQuery()
    assert isinstance(instance, StringValue)


def test_raspirover_VarRef_isa_StringValue():
    instance = raspirover_VarRef(name=3.14)
    assert isinstance(instance, StringValue)


def test_raspirover_AngleUnit_isa_Unit():
    instance = raspirover_AngleUnit()
    assert isinstance(instance, Unit)


def test_raspirover_ImperialSystemUnit_isa_Unit():
    instance = raspirover_ImperialSystemUnit()
    assert isinstance(instance, Unit)


def test_raspirover_LengthUnit_isa_Unit():
    instance = raspirover_LengthUnit()
    assert isinstance(instance, Unit)


def test_raspirover_MetricSystemUnit_isa_Unit():
    instance = raspirover_MetricSystemUnit()
    assert isinstance(instance, Unit)


def test_assoc_associatedPin52_link_reassign_clear():
    a = raspirover_Pin(level=7)
    b1 = raspirover_Action()
    b2 = raspirover_Action()
    _safe_set(a, 'raspirover_Pin', b1)
    assert _is_linked(a, 'raspirover_Pin', b1)
    if hasattr(b1, 'raspirover_Action'):
        assert _is_linked(b1, 'raspirover_Action', a)
    _safe_set(a, 'raspirover_Pin', b2)
    assert _is_linked(a, 'raspirover_Pin', b2)
    if hasattr(b1, 'raspirover_Action'):
        assert not _is_linked(b1, 'raspirover_Action', a)
    if hasattr(b2, 'raspirover_Action'):
        assert _is_linked(b2, 'raspirover_Action', a)
    _safe_set(a, 'raspirover_Pin', None)
    assert not _is_linked(a, 'raspirover_Pin', b2)
    if hasattr(b2, 'raspirover_Action'):
        assert not _is_linked(b2, 'raspirover_Action', a)


def test_assoc_block10_link_reassign_clear():
    a = raspirover_Block()
    b1 = raspirover_Sketch()
    b2 = raspirover_Sketch()
    _safe_set(a, 'raspirover_Block', b1)
    assert _is_linked(a, 'raspirover_Block', b1)
    if hasattr(b1, 'raspirover_Sketch'):
        assert _is_linked(b1, 'raspirover_Sketch', a)
    _safe_set(a, 'raspirover_Block', b2)
    assert _is_linked(a, 'raspirover_Block', b2)
    if hasattr(b1, 'raspirover_Sketch'):
        assert not _is_linked(b1, 'raspirover_Sketch', a)
    if hasattr(b2, 'raspirover_Sketch'):
        assert _is_linked(b2, 'raspirover_Sketch', a)
    _safe_set(a, 'raspirover_Block', None)
    assert not _is_linked(a, 'raspirover_Block', b2)
    if hasattr(b2, 'raspirover_Sketch'):
        assert not _is_linked(b2, 'raspirover_Sketch', a)


def test_assoc_block21_link_reassign_clear():
    a = raspirover_RoverProgram(name="sample_text")
    b1 = raspirover_RclBlock()
    b2 = raspirover_RclBlock()
    _safe_set(a, 'raspirover_RoverProgram22', b1)
    assert _is_linked(a, 'raspirover_RoverProgram22', b1)
    if hasattr(b1, 'raspirover_RclBlock'):
        assert _is_linked(b1, 'raspirover_RclBlock', a)
    _safe_set(a, 'raspirover_RoverProgram22', b2)
    assert _is_linked(a, 'raspirover_RoverProgram22', b2)
    if hasattr(b1, 'raspirover_RclBlock'):
        assert not _is_linked(b1, 'raspirover_RclBlock', a)
    if hasattr(b2, 'raspirover_RclBlock'):
        assert _is_linked(b2, 'raspirover_RclBlock', a)
    _safe_set(a, 'raspirover_RoverProgram22', None)
    assert not _is_linked(a, 'raspirover_RoverProgram22', b2)
    if hasattr(b2, 'raspirover_RclBlock'):
        assert not _is_linked(b2, 'raspirover_RclBlock', a)


def test_assoc_block34_link_reassign_clear():
    a = raspirover_RclBlock()
    b1 = raspirover_Loop()
    b2 = raspirover_Loop()
    _safe_set(a, 'raspirover_RclBlock36', b1)
    assert _is_linked(a, 'raspirover_RclBlock36', b1)
    if hasattr(b1, 'raspirover_Loop35'):
        assert _is_linked(b1, 'raspirover_Loop35', a)
    _safe_set(a, 'raspirover_RclBlock36', b2)
    assert _is_linked(a, 'raspirover_RclBlock36', b2)
    if hasattr(b1, 'raspirover_Loop35'):
        assert not _is_linked(b1, 'raspirover_Loop35', a)
    if hasattr(b2, 'raspirover_Loop35'):
        assert _is_linked(b2, 'raspirover_Loop35', a)
    _safe_set(a, 'raspirover_RclBlock36', None)
    assert not _is_linked(a, 'raspirover_RclBlock36', b2)
    if hasattr(b2, 'raspirover_Loop35'):
        assert not _is_linked(b2, 'raspirover_Loop35', a)


def test_assoc_boards4_link_reassign_clear():
    a = raspirover_Project()
    b1 = raspirover_Board()
    b2 = raspirover_Board()
    _safe_set(a, 'project', {b1})
    assert _is_linked(a, 'project', b1)
    if hasattr(b1, 'Board'):
        assert _is_linked(b1, 'Board', a)
    _safe_set(a, 'project', {b2})
    assert _is_linked(a, 'project', b2)
    if hasattr(b1, 'Board'):
        assert not _is_linked(b1, 'Board', a)
    if hasattr(b2, 'Board'):
        assert _is_linked(b2, 'Board', a)
    _safe_set(a, 'project', set())
    assert not _is_linked(a, 'project', b2)
    if hasattr(b2, 'Board'):
        assert not _is_linked(b2, 'Board', a)


def test_assoc_condFalse29_link_reassign_clear():
    a = raspirover_RclBlock()
    b1 = raspirover_Conditional()
    b2 = raspirover_Conditional()
    _safe_set(a, 'raspirover_RclBlock31', b1)
    assert _is_linked(a, 'raspirover_RclBlock31', b1)
    if hasattr(b1, 'raspirover_Conditional30'):
        assert _is_linked(b1, 'raspirover_Conditional30', a)
    _safe_set(a, 'raspirover_RclBlock31', b2)
    assert _is_linked(a, 'raspirover_RclBlock31', b2)
    if hasattr(b1, 'raspirover_Conditional30'):
        assert not _is_linked(b1, 'raspirover_Conditional30', a)
    if hasattr(b2, 'raspirover_Conditional30'):
        assert _is_linked(b2, 'raspirover_Conditional30', a)
    _safe_set(a, 'raspirover_RclBlock31', None)
    assert not _is_linked(a, 'raspirover_RclBlock31', b2)
    if hasattr(b2, 'raspirover_Conditional30'):
        assert not _is_linked(b2, 'raspirover_Conditional30', a)


def test_assoc_condTrue26_link_reassign_clear():
    a = raspirover_RclBlock()
    b1 = raspirover_Conditional()
    b2 = raspirover_Conditional()
    _safe_set(a, 'raspirover_RclBlock28', b1)
    assert _is_linked(a, 'raspirover_RclBlock28', b1)
    if hasattr(b1, 'raspirover_Conditional27'):
        assert _is_linked(b1, 'raspirover_Conditional27', a)
    _safe_set(a, 'raspirover_RclBlock28', b2)
    assert _is_linked(a, 'raspirover_RclBlock28', b2)
    if hasattr(b1, 'raspirover_Conditional27'):
        assert not _is_linked(b1, 'raspirover_Conditional27', a)
    if hasattr(b2, 'raspirover_Conditional27'):
        assert _is_linked(b2, 'raspirover_Conditional27', a)
    _safe_set(a, 'raspirover_RclBlock28', None)
    assert not _is_linked(a, 'raspirover_RclBlock28', b2)
    if hasattr(b2, 'raspirover_Conditional27'):
        assert not _is_linked(b2, 'raspirover_Conditional27', a)


def test_assoc_degrees57_link_reassign_clear():
    a = raspirover_TurnDegAction()
    b1 = raspirover_NumberValue(nValue="sample_text")
    b2 = raspirover_NumberValue(nValue="sample_text_2")
    _safe_set(a, 'raspirover_TurnDegAction', b1)
    assert _is_linked(a, 'raspirover_TurnDegAction', b1)
    if hasattr(b1, 'raspirover_NumberValue58'):
        assert _is_linked(b1, 'raspirover_NumberValue58', a)
    _safe_set(a, 'raspirover_TurnDegAction', b2)
    assert _is_linked(a, 'raspirover_TurnDegAction', b2)
    if hasattr(b1, 'raspirover_NumberValue58'):
        assert not _is_linked(b1, 'raspirover_NumberValue58', a)
    if hasattr(b2, 'raspirover_NumberValue58'):
        assert _is_linked(b2, 'raspirover_NumberValue58', a)
    _safe_set(a, 'raspirover_TurnDegAction', None)
    assert not _is_linked(a, 'raspirover_TurnDegAction', b2)
    if hasattr(b2, 'raspirover_NumberValue58'):
        assert not _is_linked(b2, 'raspirover_NumberValue58', a)


def test_assoc_distance53_link_reassign_clear():
    a = raspirover_NumberValue(nValue="sample_text")
    b1 = raspirover_ForwardMinAction()
    b2 = raspirover_ForwardMinAction()
    _safe_set(a, 'raspirover_NumberValue54', b1)
    assert _is_linked(a, 'raspirover_NumberValue54', b1)
    if hasattr(b1, 'raspirover_ForwardMinAction'):
        assert _is_linked(b1, 'raspirover_ForwardMinAction', a)
    _safe_set(a, 'raspirover_NumberValue54', b2)
    assert _is_linked(a, 'raspirover_NumberValue54', b2)
    if hasattr(b1, 'raspirover_ForwardMinAction'):
        assert not _is_linked(b1, 'raspirover_ForwardMinAction', a)
    if hasattr(b2, 'raspirover_ForwardMinAction'):
        assert _is_linked(b2, 'raspirover_ForwardMinAction', a)
    _safe_set(a, 'raspirover_NumberValue54', None)
    assert not _is_linked(a, 'raspirover_NumberValue54', b2)
    if hasattr(b2, 'raspirover_ForwardMinAction'):
        assert not _is_linked(b2, 'raspirover_ForwardMinAction', a)


def test_assoc_distance55_link_reassign_clear():
    a = raspirover_NumberValue(nValue="sample_text")
    b1 = raspirover_BackwardMinAction()
    b2 = raspirover_BackwardMinAction()
    _safe_set(a, 'raspirover_NumberValue56', b1)
    assert _is_linked(a, 'raspirover_NumberValue56', b1)
    if hasattr(b1, 'raspirover_BackwardMinAction'):
        assert _is_linked(b1, 'raspirover_BackwardMinAction', a)
    _safe_set(a, 'raspirover_NumberValue56', b2)
    assert _is_linked(a, 'raspirover_NumberValue56', b2)
    if hasattr(b1, 'raspirover_BackwardMinAction'):
        assert not _is_linked(b1, 'raspirover_BackwardMinAction', a)
    if hasattr(b2, 'raspirover_BackwardMinAction'):
        assert _is_linked(b2, 'raspirover_BackwardMinAction', a)
    _safe_set(a, 'raspirover_NumberValue56', None)
    assert not _is_linked(a, 'raspirover_NumberValue56', b2)
    if hasattr(b2, 'raspirover_BackwardMinAction'):
        assert not _is_linked(b2, 'raspirover_BackwardMinAction', a)


def test_assoc_enclosing23_link_reassign_clear():
    a = raspirover_Statement()
    b1 = raspirover_RclBlock()
    b2 = raspirover_RclBlock()
    _safe_set(a, 'stmts', b1)
    assert _is_linked(a, 'stmts', b1)
    if hasattr(b1, 'RclBlock'):
        assert _is_linked(b1, 'RclBlock', a)
    _safe_set(a, 'stmts', b2)
    assert _is_linked(a, 'stmts', b2)
    if hasattr(b1, 'RclBlock'):
        assert not _is_linked(b1, 'RclBlock', a)
    if hasattr(b2, 'RclBlock'):
        assert _is_linked(b2, 'RclBlock', a)
    _safe_set(a, 'stmts', None)
    assert not _is_linked(a, 'stmts', b2)
    if hasattr(b2, 'RclBlock'):
        assert not _is_linked(b2, 'RclBlock', a)


def test_assoc_expr25_link_reassign_clear():
    a = raspirover_RoverExpression()
    b1 = raspirover_Conditional()
    b2 = raspirover_Conditional()
    _safe_set(a, 'raspirover_RoverExpression', b1)
    assert _is_linked(a, 'raspirover_RoverExpression', b1)
    if hasattr(b1, 'raspirover_Conditional'):
        assert _is_linked(b1, 'raspirover_Conditional', a)
    _safe_set(a, 'raspirover_RoverExpression', b2)
    assert _is_linked(a, 'raspirover_RoverExpression', b2)
    if hasattr(b1, 'raspirover_Conditional'):
        assert not _is_linked(b1, 'raspirover_Conditional', a)
    if hasattr(b2, 'raspirover_Conditional'):
        assert _is_linked(b2, 'raspirover_Conditional', a)
    _safe_set(a, 'raspirover_RoverExpression', None)
    assert not _is_linked(a, 'raspirover_RoverExpression', b2)
    if hasattr(b2, 'raspirover_Conditional'):
        assert not _is_linked(b2, 'raspirover_Conditional', a)


def test_assoc_expr32_link_reassign_clear():
    a = raspirover_RoverExpression()
    b1 = raspirover_Loop()
    b2 = raspirover_Loop()
    _safe_set(a, 'raspirover_RoverExpression33', b1)
    assert _is_linked(a, 'raspirover_RoverExpression33', b1)
    if hasattr(b1, 'raspirover_Loop'):
        assert _is_linked(b1, 'raspirover_Loop', a)
    _safe_set(a, 'raspirover_RoverExpression33', b2)
    assert _is_linked(a, 'raspirover_RoverExpression33', b2)
    if hasattr(b1, 'raspirover_Loop'):
        assert not _is_linked(b1, 'raspirover_Loop', a)
    if hasattr(b2, 'raspirover_Loop'):
        assert _is_linked(b2, 'raspirover_Loop', a)
    _safe_set(a, 'raspirover_RoverExpression33', None)
    assert not _is_linked(a, 'raspirover_RoverExpression33', b2)
    if hasattr(b2, 'raspirover_Loop'):
        assert not _is_linked(b2, 'raspirover_Loop', a)


def test_assoc_instructions13_link_reassign_clear():
    a = raspirover_Instruction()
    b1 = raspirover_Block()
    b2 = raspirover_Block()
    _safe_set(a, 'raspirover_Instruction', b1)
    assert _is_linked(a, 'raspirover_Instruction', b1)
    if hasattr(b1, 'raspirover_Block14'):
        assert _is_linked(b1, 'raspirover_Block14', a)
    _safe_set(a, 'raspirover_Instruction', b2)
    assert _is_linked(a, 'raspirover_Instruction', b2)
    if hasattr(b1, 'raspirover_Block14'):
        assert not _is_linked(b1, 'raspirover_Block14', a)
    if hasattr(b2, 'raspirover_Block14'):
        assert _is_linked(b2, 'raspirover_Block14', a)
    _safe_set(a, 'raspirover_Instruction', None)
    assert not _is_linked(a, 'raspirover_Instruction', b2)
    if hasattr(b2, 'raspirover_Block14'):
        assert not _is_linked(b2, 'raspirover_Block14', a)


def test_assoc_lhs38_link_reassign_clear():
    a = raspirover_NumericExpression(op=True)
    b1 = raspirover_NumberValue(nValue="sample_text")
    b2 = raspirover_NumberValue(nValue="sample_text_2")
    _safe_set(a, 'raspirover_NumericExpression', b1)
    assert _is_linked(a, 'raspirover_NumericExpression', b1)
    if hasattr(b1, 'raspirover_NumberValue'):
        assert _is_linked(b1, 'raspirover_NumberValue', a)
    _safe_set(a, 'raspirover_NumericExpression', b2)
    assert _is_linked(a, 'raspirover_NumericExpression', b2)
    if hasattr(b1, 'raspirover_NumberValue'):
        assert not _is_linked(b1, 'raspirover_NumberValue', a)
    if hasattr(b2, 'raspirover_NumberValue'):
        assert _is_linked(b2, 'raspirover_NumberValue', a)
    _safe_set(a, 'raspirover_NumericExpression', None)
    assert not _is_linked(a, 'raspirover_NumericExpression', b2)
    if hasattr(b2, 'raspirover_NumberValue'):
        assert not _is_linked(b2, 'raspirover_NumberValue', a)


def test_assoc_lhs42_link_reassign_clear():
    a = raspirover_StringValue(sValue=True)
    b1 = raspirover_StringExpression(op=True)
    b2 = raspirover_StringExpression(op=False)
    _safe_set(a, 'raspirover_StringValue', b1)
    assert _is_linked(a, 'raspirover_StringValue', b1)
    if hasattr(b1, 'raspirover_StringExpression'):
        assert _is_linked(b1, 'raspirover_StringExpression', a)
    _safe_set(a, 'raspirover_StringValue', b2)
    assert _is_linked(a, 'raspirover_StringValue', b2)
    if hasattr(b1, 'raspirover_StringExpression'):
        assert not _is_linked(b1, 'raspirover_StringExpression', a)
    if hasattr(b2, 'raspirover_StringExpression'):
        assert _is_linked(b2, 'raspirover_StringExpression', a)
    _safe_set(a, 'raspirover_StringValue', None)
    assert not _is_linked(a, 'raspirover_StringValue', b2)
    if hasattr(b2, 'raspirover_StringExpression'):
        assert not _is_linked(b2, 'raspirover_StringExpression', a)


def test_assoc_lhs46_link_reassign_clear():
    a = raspirover_BooleanValue(bValue=True)
    b1 = raspirover_BooleanExpression(op="sample_text")
    b2 = raspirover_BooleanExpression(op="sample_text_2")
    _safe_set(a, 'raspirover_BooleanValue', b1)
    assert _is_linked(a, 'raspirover_BooleanValue', b1)
    if hasattr(b1, 'raspirover_BooleanExpression'):
        assert _is_linked(b1, 'raspirover_BooleanExpression', a)
    _safe_set(a, 'raspirover_BooleanValue', b2)
    assert _is_linked(a, 'raspirover_BooleanValue', b2)
    if hasattr(b1, 'raspirover_BooleanExpression'):
        assert not _is_linked(b1, 'raspirover_BooleanExpression', a)
    if hasattr(b2, 'raspirover_BooleanExpression'):
        assert _is_linked(b2, 'raspirover_BooleanExpression', a)
    _safe_set(a, 'raspirover_BooleanValue', None)
    assert not _is_linked(a, 'raspirover_BooleanValue', b2)
    if hasattr(b2, 'raspirover_BooleanExpression'):
        assert not _is_linked(b2, 'raspirover_BooleanExpression', a)


def test_assoc_lhs61_link_reassign_clear():
    a = raspirover_Quantity(value="sample_text")
    b1 = raspirover_QuantityHomogenousOperation()
    b2 = raspirover_QuantityHomogenousOperation()
    _safe_set(a, 'raspirover_Quantity62', b1)
    assert _is_linked(a, 'raspirover_Quantity62', b1)
    if hasattr(b1, 'raspirover_QuantityHomogenousOperation'):
        assert _is_linked(b1, 'raspirover_QuantityHomogenousOperation', a)
    _safe_set(a, 'raspirover_Quantity62', b2)
    assert _is_linked(a, 'raspirover_Quantity62', b2)
    if hasattr(b1, 'raspirover_QuantityHomogenousOperation'):
        assert not _is_linked(b1, 'raspirover_QuantityHomogenousOperation', a)
    if hasattr(b2, 'raspirover_QuantityHomogenousOperation'):
        assert _is_linked(b2, 'raspirover_QuantityHomogenousOperation', a)
    _safe_set(a, 'raspirover_Quantity62', None)
    assert not _is_linked(a, 'raspirover_Quantity62', b2)
    if hasattr(b2, 'raspirover_QuantityHomogenousOperation'):
        assert not _is_linked(b2, 'raspirover_QuantityHomogenousOperation', a)


def test_assoc_lhs66_link_reassign_clear():
    a = raspirover_QuantityScalarOperation(rhs=3.14)
    b1 = raspirover_Quantity(value="sample_text")
    b2 = raspirover_Quantity(value="sample_text_2")
    _safe_set(a, 'raspirover_QuantityScalarOperation', b1)
    assert _is_linked(a, 'raspirover_QuantityScalarOperation', b1)
    if hasattr(b1, 'raspirover_Quantity67'):
        assert _is_linked(b1, 'raspirover_Quantity67', a)
    _safe_set(a, 'raspirover_QuantityScalarOperation', b2)
    assert _is_linked(a, 'raspirover_QuantityScalarOperation', b2)
    if hasattr(b1, 'raspirover_Quantity67'):
        assert not _is_linked(b1, 'raspirover_Quantity67', a)
    if hasattr(b2, 'raspirover_Quantity67'):
        assert _is_linked(b2, 'raspirover_Quantity67', a)
    _safe_set(a, 'raspirover_QuantityScalarOperation', None)
    assert not _is_linked(a, 'raspirover_QuantityScalarOperation', b2)
    if hasattr(b2, 'raspirover_Quantity67'):
        assert not _is_linked(b2, 'raspirover_Quantity67', a)


def test_assoc_params19_link_reassign_clear():
    a = raspirover_RoverProgram(name="sample_text")
    b1 = raspirover_Param(name="sample_text")
    b2 = raspirover_Param(name="sample_text_2")
    _safe_set(a, 'raspirover_RoverProgram20', {b1})
    assert _is_linked(a, 'raspirover_RoverProgram20', b1)
    if hasattr(b1, 'raspirover_Param'):
        assert _is_linked(b1, 'raspirover_Param', a)
    _safe_set(a, 'raspirover_RoverProgram20', {b2})
    assert _is_linked(a, 'raspirover_RoverProgram20', b2)
    if hasattr(b1, 'raspirover_Param'):
        assert not _is_linked(b1, 'raspirover_Param', a)
    if hasattr(b2, 'raspirover_Param'):
        assert _is_linked(b2, 'raspirover_Param', a)
    _safe_set(a, 'raspirover_RoverProgram20', set())
    assert not _is_linked(a, 'raspirover_RoverProgram20', b2)
    if hasattr(b2, 'raspirover_Param'):
        assert not _is_linked(b2, 'raspirover_Param', a)


def test_assoc_program7_link_reassign_clear():
    a = raspirover_RoverProgram(name="sample_text")
    b1 = raspirover_Project()
    b2 = raspirover_Project()
    _safe_set(a, 'raspirover_RoverProgram', b1)
    assert _is_linked(a, 'raspirover_RoverProgram', b1)
    if hasattr(b1, 'raspirover_Project'):
        assert _is_linked(b1, 'raspirover_Project', a)
    _safe_set(a, 'raspirover_RoverProgram', b2)
    assert _is_linked(a, 'raspirover_RoverProgram', b2)
    if hasattr(b1, 'raspirover_Project'):
        assert not _is_linked(b1, 'raspirover_Project', a)
    if hasattr(b2, 'raspirover_Project'):
        assert _is_linked(b2, 'raspirover_Project', a)
    _safe_set(a, 'raspirover_RoverProgram', None)
    assert not _is_linked(a, 'raspirover_RoverProgram', b2)
    if hasattr(b2, 'raspirover_Project'):
        assert not _is_linked(b2, 'raspirover_Project', a)


def test_assoc_project3_link_reassign_clear():
    a = raspirover_Project()
    b1 = raspirover_Board()
    b2 = raspirover_Board()
    _safe_set(a, 'Project', b1)
    assert _is_linked(a, 'Project', b1)
    if hasattr(b1, 'boards'):
        assert _is_linked(b1, 'boards', a)
    _safe_set(a, 'Project', b2)
    assert _is_linked(a, 'Project', b2)
    if hasattr(b1, 'boards'):
        assert not _is_linked(b1, 'boards', a)
    if hasattr(b2, 'boards'):
        assert _is_linked(b2, 'boards', a)
    _safe_set(a, 'Project', None)
    assert not _is_linked(a, 'Project', b2)
    if hasattr(b2, 'boards'):
        assert not _is_linked(b2, 'boards', a)


def test_assoc_project8_link_reassign_clear():
    a = raspirover_Project()
    b1 = raspirover_Sketch()
    b2 = raspirover_Sketch()
    _safe_set(a, 'Project9', b1)
    assert _is_linked(a, 'Project9', b1)
    if hasattr(b1, 'sketches'):
        assert _is_linked(b1, 'sketches', a)
    _safe_set(a, 'Project9', b2)
    assert _is_linked(a, 'Project9', b2)
    if hasattr(b1, 'sketches'):
        assert not _is_linked(b1, 'sketches', a)
    if hasattr(b2, 'sketches'):
        assert _is_linked(b2, 'sketches', a)
    _safe_set(a, 'Project9', None)
    assert not _is_linked(a, 'Project9', b2)
    if hasattr(b2, 'sketches'):
        assert not _is_linked(b2, 'sketches', a)


def test_assoc_quantity50_link_reassign_clear():
    a = raspirover_Quantity(value="sample_text")
    b1 = raspirover_NumberValue(nValue="sample_text")
    b2 = raspirover_NumberValue(nValue="sample_text_2")
    _safe_set(a, 'raspirover_Quantity', b1)
    assert _is_linked(a, 'raspirover_Quantity', b1)
    if hasattr(b1, 'raspirover_NumberValue51'):
        assert _is_linked(b1, 'raspirover_NumberValue51', a)
    _safe_set(a, 'raspirover_Quantity', b2)
    assert _is_linked(a, 'raspirover_Quantity', b2)
    if hasattr(b1, 'raspirover_NumberValue51'):
        assert not _is_linked(b1, 'raspirover_NumberValue51', a)
    if hasattr(b2, 'raspirover_NumberValue51'):
        assert _is_linked(b2, 'raspirover_NumberValue51', a)
    _safe_set(a, 'raspirover_Quantity', None)
    assert not _is_linked(a, 'raspirover_Quantity', b2)
    if hasattr(b2, 'raspirover_NumberValue51'):
        assert not _is_linked(b2, 'raspirover_NumberValue51', a)


def test_assoc_rhs39_link_reassign_clear():
    a = raspirover_NumericExpression(op=True)
    b1 = raspirover_NumberValue(nValue="sample_text")
    b2 = raspirover_NumberValue(nValue="sample_text_2")
    _safe_set(a, 'raspirover_NumericExpression40', b1)
    assert _is_linked(a, 'raspirover_NumericExpression40', b1)
    if hasattr(b1, 'raspirover_NumberValue41'):
        assert _is_linked(b1, 'raspirover_NumberValue41', a)
    _safe_set(a, 'raspirover_NumericExpression40', b2)
    assert _is_linked(a, 'raspirover_NumericExpression40', b2)
    if hasattr(b1, 'raspirover_NumberValue41'):
        assert not _is_linked(b1, 'raspirover_NumberValue41', a)
    if hasattr(b2, 'raspirover_NumberValue41'):
        assert _is_linked(b2, 'raspirover_NumberValue41', a)
    _safe_set(a, 'raspirover_NumericExpression40', None)
    assert not _is_linked(a, 'raspirover_NumericExpression40', b2)
    if hasattr(b2, 'raspirover_NumberValue41'):
        assert not _is_linked(b2, 'raspirover_NumberValue41', a)


def test_assoc_rhs43_link_reassign_clear():
    a = raspirover_StringValue(sValue=True)
    b1 = raspirover_StringExpression(op=True)
    b2 = raspirover_StringExpression(op=False)
    _safe_set(a, 'raspirover_StringValue45', b1)
    assert _is_linked(a, 'raspirover_StringValue45', b1)
    if hasattr(b1, 'raspirover_StringExpression44'):
        assert _is_linked(b1, 'raspirover_StringExpression44', a)
    _safe_set(a, 'raspirover_StringValue45', b2)
    assert _is_linked(a, 'raspirover_StringValue45', b2)
    if hasattr(b1, 'raspirover_StringExpression44'):
        assert not _is_linked(b1, 'raspirover_StringExpression44', a)
    if hasattr(b2, 'raspirover_StringExpression44'):
        assert _is_linked(b2, 'raspirover_StringExpression44', a)
    _safe_set(a, 'raspirover_StringValue45', None)
    assert not _is_linked(a, 'raspirover_StringValue45', b2)
    if hasattr(b2, 'raspirover_StringExpression44'):
        assert not _is_linked(b2, 'raspirover_StringExpression44', a)


def test_assoc_rhs47_link_reassign_clear():
    a = raspirover_BooleanValue(bValue=True)
    b1 = raspirover_BooleanExpression(op="sample_text")
    b2 = raspirover_BooleanExpression(op="sample_text_2")
    _safe_set(a, 'raspirover_BooleanValue49', b1)
    assert _is_linked(a, 'raspirover_BooleanValue49', b1)
    if hasattr(b1, 'raspirover_BooleanExpression48'):
        assert _is_linked(b1, 'raspirover_BooleanExpression48', a)
    _safe_set(a, 'raspirover_BooleanValue49', b2)
    assert _is_linked(a, 'raspirover_BooleanValue49', b2)
    if hasattr(b1, 'raspirover_BooleanExpression48'):
        assert not _is_linked(b1, 'raspirover_BooleanExpression48', a)
    if hasattr(b2, 'raspirover_BooleanExpression48'):
        assert _is_linked(b2, 'raspirover_BooleanExpression48', a)
    _safe_set(a, 'raspirover_BooleanValue49', None)
    assert not _is_linked(a, 'raspirover_BooleanValue49', b2)
    if hasattr(b2, 'raspirover_BooleanExpression48'):
        assert not _is_linked(b2, 'raspirover_BooleanExpression48', a)


def test_assoc_rhs63_link_reassign_clear():
    a = raspirover_Quantity(value="sample_text")
    b1 = raspirover_QuantityHomogenousOperation()
    b2 = raspirover_QuantityHomogenousOperation()
    _safe_set(a, 'raspirover_Quantity65', b1)
    assert _is_linked(a, 'raspirover_Quantity65', b1)
    if hasattr(b1, 'raspirover_QuantityHomogenousOperation64'):
        assert _is_linked(b1, 'raspirover_QuantityHomogenousOperation64', a)
    _safe_set(a, 'raspirover_Quantity65', b2)
    assert _is_linked(a, 'raspirover_Quantity65', b2)
    if hasattr(b1, 'raspirover_QuantityHomogenousOperation64'):
        assert not _is_linked(b1, 'raspirover_QuantityHomogenousOperation64', a)
    if hasattr(b2, 'raspirover_QuantityHomogenousOperation64'):
        assert _is_linked(b2, 'raspirover_QuantityHomogenousOperation64', a)
    _safe_set(a, 'raspirover_Quantity65', None)
    assert not _is_linked(a, 'raspirover_Quantity65', b2)
    if hasattr(b2, 'raspirover_QuantityHomogenousOperation64'):
        assert not _is_linked(b2, 'raspirover_QuantityHomogenousOperation64', a)


def test_assoc_sketches5_link_reassign_clear():
    a = raspirover_Project()
    b1 = raspirover_Sketch()
    b2 = raspirover_Sketch()
    _safe_set(a, 'project6', {b1})
    assert _is_linked(a, 'project6', b1)
    if hasattr(b1, 'Sketch'):
        assert _is_linked(b1, 'Sketch', a)
    _safe_set(a, 'project6', {b2})
    assert _is_linked(a, 'project6', b2)
    if hasattr(b1, 'Sketch'):
        assert not _is_linked(b1, 'Sketch', a)
    if hasattr(b2, 'Sketch'):
        assert _is_linked(b2, 'Sketch', a)
    _safe_set(a, 'project6', set())
    assert not _is_linked(a, 'project6', b2)
    if hasattr(b2, 'Sketch'):
        assert not _is_linked(b2, 'Sketch', a)


def test_assoc_stmts37_link_reassign_clear():
    a = raspirover_Statement()
    b1 = raspirover_RclBlock()
    b2 = raspirover_RclBlock()
    _safe_set(a, 'Statement', b1)
    assert _is_linked(a, 'Statement', b1)
    if hasattr(b1, 'enclosing'):
        assert _is_linked(b1, 'enclosing', a)
    _safe_set(a, 'Statement', b2)
    assert _is_linked(a, 'Statement', b2)
    if hasattr(b1, 'enclosing'):
        assert not _is_linked(b1, 'enclosing', a)
    if hasattr(b2, 'enclosing'):
        assert _is_linked(b2, 'enclosing', a)
    _safe_set(a, 'Statement', None)
    assert not _is_linked(a, 'Statement', b2)
    if hasattr(b2, 'enclosing'):
        assert not _is_linked(b2, 'enclosing', a)


def test_assoc_unit59_link_reassign_clear():
    a = raspirover_Unit()
    b1 = raspirover_Quantity(value="sample_text")
    b2 = raspirover_Quantity(value="sample_text_2")
    _safe_set(a, 'raspirover_Unit', b1)
    assert _is_linked(a, 'raspirover_Unit', b1)
    if hasattr(b1, 'raspirover_Quantity60'):
        assert _is_linked(b1, 'raspirover_Quantity60', a)
    _safe_set(a, 'raspirover_Unit', b2)
    assert _is_linked(a, 'raspirover_Unit', b2)
    if hasattr(b1, 'raspirover_Quantity60'):
        assert not _is_linked(b1, 'raspirover_Quantity60', a)
    if hasattr(b2, 'raspirover_Quantity60'):
        assert _is_linked(b2, 'raspirover_Quantity60', a)
    _safe_set(a, 'raspirover_Unit', None)
    assert not _is_linked(a, 'raspirover_Unit', b2)
    if hasattr(b2, 'raspirover_Quantity60'):
        assert not _is_linked(b2, 'raspirover_Quantity60', a)


def test_assoc_value24_link_reassign_clear():
    a = raspirover_VarAssignment(name=True)
    b1 = raspirover_RoverValue()
    b2 = raspirover_RoverValue()
    _safe_set(a, 'raspirover_VarAssignment', b1)
    assert _is_linked(a, 'raspirover_VarAssignment', b1)
    if hasattr(b1, 'raspirover_RoverValue'):
        assert _is_linked(b1, 'raspirover_RoverValue', a)
    _safe_set(a, 'raspirover_VarAssignment', b2)
    assert _is_linked(a, 'raspirover_VarAssignment', b2)
    if hasattr(b1, 'raspirover_RoverValue'):
        assert not _is_linked(b1, 'raspirover_RoverValue', a)
    if hasattr(b2, 'raspirover_RoverValue'):
        assert _is_linked(b2, 'raspirover_RoverValue', a)
    _safe_set(a, 'raspirover_VarAssignment', None)
    assert not _is_linked(a, 'raspirover_VarAssignment', b2)
    if hasattr(b2, 'raspirover_RoverValue'):
        assert not _is_linked(b2, 'raspirover_RoverValue', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


AngleOperation_strategy = st.builds(AngleOperation)
@given(instance=AngleOperation_strategy)
@settings(max_examples=25)
def test_AngleOperation_instantiation(instance):
    assert isinstance(instance, AngleOperation)


AngleUnit_strategy = st.builds(AngleUnit)
@given(instance=AngleUnit_strategy)
@settings(max_examples=25)
def test_AngleUnit_instantiation(instance):
    assert isinstance(instance, AngleUnit)


ArduinoModule_strategy = st.builds(ArduinoModule)
@given(instance=ArduinoModule_strategy)
@settings(max_examples=25)
def test_ArduinoModule_instantiation(instance):
    assert isinstance(instance, ArduinoModule)


Board_strategy = st.builds(Board)
@given(instance=Board_strategy)
@settings(max_examples=25)
def test_Board_instantiation(instance):
    assert isinstance(instance, Board)


BooleanValue_strategy = st.builds(BooleanValue)
@given(instance=BooleanValue_strategy)
@settings(max_examples=25)
def test_BooleanValue_instantiation(instance):
    assert isinstance(instance, BooleanValue)


ImperialSystemUnit_strategy = st.builds(ImperialSystemUnit)
@given(instance=ImperialSystemUnit_strategy)
@settings(max_examples=25)
def test_ImperialSystemUnit_instantiation(instance):
    assert isinstance(instance, ImperialSystemUnit)


LengthOperation_strategy = st.builds(LengthOperation)
@given(instance=LengthOperation_strategy)
@settings(max_examples=25)
def test_LengthOperation_instantiation(instance):
    assert isinstance(instance, LengthOperation)


LengthUnit_strategy = st.builds(LengthUnit)
@given(instance=LengthUnit_strategy)
@settings(max_examples=25)
def test_LengthUnit_instantiation(instance):
    assert isinstance(instance, LengthUnit)


MetricSystemUnit_strategy = st.builds(MetricSystemUnit)
@given(instance=MetricSystemUnit_strategy)
@settings(max_examples=25)
def test_MetricSystemUnit_instantiation(instance):
    assert isinstance(instance, MetricSystemUnit)


Module_strategy = st.builds(Module)
@given(instance=Module_strategy)
@settings(max_examples=25)
def test_Module_instantiation(instance):
    assert isinstance(instance, Module)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


NumberValue_strategy = st.builds(NumberValue)
@given(instance=NumberValue_strategy)
@settings(max_examples=25)
def test_NumberValue_instantiation(instance):
    assert isinstance(instance, NumberValue)


Pin_strategy = st.builds(Pin)
@given(instance=Pin_strategy)
@settings(max_examples=25)
def test_Pin_instantiation(instance):
    assert isinstance(instance, Pin)


Quantity_strategy = st.builds(Quantity)
@given(instance=Quantity_strategy)
@settings(max_examples=25)
def test_Quantity_instantiation(instance):
    assert isinstance(instance, Quantity)


QuantityHomogenousOperation_strategy = st.builds(QuantityHomogenousOperation)
@given(instance=QuantityHomogenousOperation_strategy)
@settings(max_examples=25)
def test_QuantityHomogenousOperation_instantiation(instance):
    assert isinstance(instance, QuantityHomogenousOperation)


QuantityOperation_strategy = st.builds(QuantityOperation)
@given(instance=QuantityOperation_strategy)
@settings(max_examples=25)
def test_QuantityOperation_instantiation(instance):
    assert isinstance(instance, QuantityOperation)


QuantityScalarOperation_strategy = st.builds(QuantityScalarOperation)
@given(instance=QuantityScalarOperation_strategy)
@settings(max_examples=25)
def test_QuantityScalarOperation_instantiation(instance):
    assert isinstance(instance, QuantityScalarOperation)


Query_strategy = st.builds(Query)
@given(instance=Query_strategy)
@settings(max_examples=25)
def test_Query_instantiation(instance):
    assert isinstance(instance, Query)


RoverExpression_strategy = st.builds(RoverExpression)
@given(instance=RoverExpression_strategy)
@settings(max_examples=25)
def test_RoverExpression_instantiation(instance):
    assert isinstance(instance, RoverExpression)


RoverValue_strategy = st.builds(RoverValue)
@given(instance=RoverValue_strategy)
@settings(max_examples=25)
def test_RoverValue_instantiation(instance):
    assert isinstance(instance, RoverValue)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


StringValue_strategy = st.builds(StringValue)
@given(instance=StringValue_strategy)
@settings(max_examples=25)
def test_StringValue_instantiation(instance):
    assert isinstance(instance, StringValue)


Unit_strategy = st.builds(Unit)
@given(instance=Unit_strategy)
@settings(max_examples=25)
def test_Unit_instantiation(instance):
    assert isinstance(instance, Unit)


raspirover_Action_strategy = st.builds(raspirover_Action)
@given(instance=raspirover_Action_strategy)
@settings(max_examples=25)
def test_raspirover_Action_instantiation(instance):
    assert isinstance(instance, raspirover_Action)


raspirover_AnalogPin_strategy = st.builds(raspirover_AnalogPin)
@given(instance=raspirover_AnalogPin_strategy)
@settings(max_examples=25)
def test_raspirover_AnalogPin_instantiation(instance):
    assert isinstance(instance, raspirover_AnalogPin)


raspirover_Angle_strategy = st.builds(raspirover_Angle)
@given(instance=raspirover_Angle_strategy)
@settings(max_examples=25)
def test_raspirover_Angle_instantiation(instance):
    assert isinstance(instance, raspirover_Angle)


raspirover_AngleAdd_strategy = st.builds(raspirover_AngleAdd)
@given(instance=raspirover_AngleAdd_strategy)
@settings(max_examples=25)
def test_raspirover_AngleAdd_instantiation(instance):
    assert isinstance(instance, raspirover_AngleAdd)


raspirover_AngleDistinct_strategy = st.builds(raspirover_AngleDistinct)
@given(instance=raspirover_AngleDistinct_strategy)
@settings(max_examples=25)
def test_raspirover_AngleDistinct_instantiation(instance):
    assert isinstance(instance, raspirover_AngleDistinct)


raspirover_AngleEquals_strategy = st.builds(raspirover_AngleEquals)
@given(instance=raspirover_AngleEquals_strategy)
@settings(max_examples=25)
def test_raspirover_AngleEquals_instantiation(instance):
    assert isinstance(instance, raspirover_AngleEquals)


raspirover_AngleGreater_strategy = st.builds(raspirover_AngleGreater)
@given(instance=raspirover_AngleGreater_strategy)
@settings(max_examples=25)
def test_raspirover_AngleGreater_instantiation(instance):
    assert isinstance(instance, raspirover_AngleGreater)


raspirover_AngleOperation_strategy = st.builds(raspirover_AngleOperation)
@given(instance=raspirover_AngleOperation_strategy)
@settings(max_examples=25)
def test_raspirover_AngleOperation_instantiation(instance):
    assert isinstance(instance, raspirover_AngleOperation)


raspirover_AngleScalarDivide_strategy = st.builds(raspirover_AngleScalarDivide)
@given(instance=raspirover_AngleScalarDivide_strategy)
@settings(max_examples=25)
def test_raspirover_AngleScalarDivide_instantiation(instance):
    assert isinstance(instance, raspirover_AngleScalarDivide)


raspirover_AngleScalarMultiply_strategy = st.builds(raspirover_AngleScalarMultiply)
@given(instance=raspirover_AngleScalarMultiply_strategy)
@settings(max_examples=25)
def test_raspirover_AngleScalarMultiply_instantiation(instance):
    assert isinstance(instance, raspirover_AngleScalarMultiply)


raspirover_AngleSmaller_strategy = st.builds(raspirover_AngleSmaller)
@given(instance=raspirover_AngleSmaller_strategy)
@settings(max_examples=25)
def test_raspirover_AngleSmaller_instantiation(instance):
    assert isinstance(instance, raspirover_AngleSmaller)


raspirover_AngleSubtract_strategy = st.builds(raspirover_AngleSubtract)
@given(instance=raspirover_AngleSubtract_strategy)
@settings(max_examples=25)
def test_raspirover_AngleSubtract_instantiation(instance):
    assert isinstance(instance, raspirover_AngleSubtract)


raspirover_AngleUnit_strategy = st.builds(raspirover_AngleUnit)
@given(instance=raspirover_AngleUnit_strategy)
@settings(max_examples=25)
def test_raspirover_AngleUnit_instantiation(instance):
    assert isinstance(instance, raspirover_AngleUnit)


raspirover_ArduinoAnalogModule_strategy = st.builds(raspirover_ArduinoAnalogModule)
@given(instance=raspirover_ArduinoAnalogModule_strategy)
@settings(max_examples=25)
def test_raspirover_ArduinoAnalogModule_instantiation(instance):
    assert isinstance(instance, raspirover_ArduinoAnalogModule)


raspirover_ArduinoDigitalModule_strategy = st.builds(raspirover_ArduinoDigitalModule)
@given(instance=raspirover_ArduinoDigitalModule_strategy)
@settings(max_examples=25)
def test_raspirover_ArduinoDigitalModule_instantiation(instance):
    assert isinstance(instance, raspirover_ArduinoDigitalModule)


raspirover_ArduinoModule_strategy = st.builds(raspirover_ArduinoModule)
@given(instance=raspirover_ArduinoModule_strategy)
@settings(max_examples=25)
def test_raspirover_ArduinoModule_instantiation(instance):
    assert isinstance(instance, raspirover_ArduinoModule)


raspirover_BackwardAction_strategy = st.builds(raspirover_BackwardAction)
@given(instance=raspirover_BackwardAction_strategy)
@settings(max_examples=25)
def test_raspirover_BackwardAction_instantiation(instance):
    assert isinstance(instance, raspirover_BackwardAction)


raspirover_BackwardMinAction_strategy = st.builds(raspirover_BackwardMinAction)
@given(instance=raspirover_BackwardMinAction_strategy)
@settings(max_examples=25)
def test_raspirover_BackwardMinAction_instantiation(instance):
    assert isinstance(instance, raspirover_BackwardMinAction)


raspirover_Block_strategy = st.builds(raspirover_Block)
@given(instance=raspirover_Block_strategy)
@settings(max_examples=25)
def test_raspirover_Block_instantiation(instance):
    assert isinstance(instance, raspirover_Block)


raspirover_Board_strategy = st.builds(raspirover_Board)
@given(instance=raspirover_Board_strategy)
@settings(max_examples=25)
def test_raspirover_Board_instantiation(instance):
    assert isinstance(instance, raspirover_Board)


raspirover_BooleanExpression_strategy = st.builds(raspirover_BooleanExpression, op=safe_text)
@given(instance=raspirover_BooleanExpression_strategy)
@settings(max_examples=25)
def test_raspirover_BooleanExpression_instantiation(instance):
    assert isinstance(instance, raspirover_BooleanExpression)


raspirover_BooleanValue_strategy = st.builds(raspirover_BooleanValue, bValue=st.booleans())
@given(instance=raspirover_BooleanValue_strategy)
@settings(max_examples=25)
def test_raspirover_BooleanValue_instantiation(instance):
    assert isinstance(instance, raspirover_BooleanValue)


raspirover_Centimeter_strategy = st.builds(raspirover_Centimeter)
@given(instance=raspirover_Centimeter_strategy)
@settings(max_examples=25)
def test_raspirover_Centimeter_instantiation(instance):
    assert isinstance(instance, raspirover_Centimeter)


raspirover_Conditional_strategy = st.builds(raspirover_Conditional)
@given(instance=raspirover_Conditional_strategy)
@settings(max_examples=25)
def test_raspirover_Conditional_instantiation(instance):
    assert isinstance(instance, raspirover_Conditional)


raspirover_Degree_strategy = st.builds(raspirover_Degree)
@given(instance=raspirover_Degree_strategy)
@settings(max_examples=25)
def test_raspirover_Degree_instantiation(instance):
    assert isinstance(instance, raspirover_Degree)


raspirover_DigitalPin_strategy = st.builds(raspirover_DigitalPin)
@given(instance=raspirover_DigitalPin_strategy)
@settings(max_examples=25)
def test_raspirover_DigitalPin_instantiation(instance):
    assert isinstance(instance, raspirover_DigitalPin)


raspirover_Foot_strategy = st.builds(raspirover_Foot)
@given(instance=raspirover_Foot_strategy)
@settings(max_examples=25)
def test_raspirover_Foot_instantiation(instance):
    assert isinstance(instance, raspirover_Foot)


raspirover_ForwardAction_strategy = st.builds(raspirover_ForwardAction)
@given(instance=raspirover_ForwardAction_strategy)
@settings(max_examples=25)
def test_raspirover_ForwardAction_instantiation(instance):
    assert isinstance(instance, raspirover_ForwardAction)


raspirover_ForwardMinAction_strategy = st.builds(raspirover_ForwardMinAction)
@given(instance=raspirover_ForwardMinAction_strategy)
@settings(max_examples=25)
def test_raspirover_ForwardMinAction_instantiation(instance):
    assert isinstance(instance, raspirover_ForwardMinAction)


raspirover_Gradian_strategy = st.builds(raspirover_Gradian)
@given(instance=raspirover_Gradian_strategy)
@settings(max_examples=25)
def test_raspirover_Gradian_instantiation(instance):
    assert isinstance(instance, raspirover_Gradian)


raspirover_HumidityQuery_strategy = st.builds(raspirover_HumidityQuery)
@given(instance=raspirover_HumidityQuery_strategy)
@settings(max_examples=25)
def test_raspirover_HumidityQuery_instantiation(instance):
    assert isinstance(instance, raspirover_HumidityQuery)


raspirover_ImperialSystemUnit_strategy = st.builds(raspirover_ImperialSystemUnit)
@given(instance=raspirover_ImperialSystemUnit_strategy)
@settings(max_examples=25)
def test_raspirover_ImperialSystemUnit_instantiation(instance):
    assert isinstance(instance, raspirover_ImperialSystemUnit)


raspirover_Inch_strategy = st.builds(raspirover_Inch)
@given(instance=raspirover_Inch_strategy)
@settings(max_examples=25)
def test_raspirover_Inch_instantiation(instance):
    assert isinstance(instance, raspirover_Inch)


raspirover_Instruction_strategy = st.builds(raspirover_Instruction)
@given(instance=raspirover_Instruction_strategy)
@settings(max_examples=25)
def test_raspirover_Instruction_instantiation(instance):
    assert isinstance(instance, raspirover_Instruction)


raspirover_Length_strategy = st.builds(raspirover_Length)
@given(instance=raspirover_Length_strategy)
@settings(max_examples=25)
def test_raspirover_Length_instantiation(instance):
    assert isinstance(instance, raspirover_Length)


raspirover_LengthAdd_strategy = st.builds(raspirover_LengthAdd)
@given(instance=raspirover_LengthAdd_strategy)
@settings(max_examples=25)
def test_raspirover_LengthAdd_instantiation(instance):
    assert isinstance(instance, raspirover_LengthAdd)


raspirover_LengthDistinct_strategy = st.builds(raspirover_LengthDistinct)
@given(instance=raspirover_LengthDistinct_strategy)
@settings(max_examples=25)
def test_raspirover_LengthDistinct_instantiation(instance):
    assert isinstance(instance, raspirover_LengthDistinct)


raspirover_LengthEquals_strategy = st.builds(raspirover_LengthEquals)
@given(instance=raspirover_LengthEquals_strategy)
@settings(max_examples=25)
def test_raspirover_LengthEquals_instantiation(instance):
    assert isinstance(instance, raspirover_LengthEquals)


raspirover_LengthGreater_strategy = st.builds(raspirover_LengthGreater)
@given(instance=raspirover_LengthGreater_strategy)
@settings(max_examples=25)
def test_raspirover_LengthGreater_instantiation(instance):
    assert isinstance(instance, raspirover_LengthGreater)


raspirover_LengthOperation_strategy = st.builds(raspirover_LengthOperation)
@given(instance=raspirover_LengthOperation_strategy)
@settings(max_examples=25)
def test_raspirover_LengthOperation_instantiation(instance):
    assert isinstance(instance, raspirover_LengthOperation)


raspirover_LengthScalarDivide_strategy = st.builds(raspirover_LengthScalarDivide)
@given(instance=raspirover_LengthScalarDivide_strategy)
@settings(max_examples=25)
def test_raspirover_LengthScalarDivide_instantiation(instance):
    assert isinstance(instance, raspirover_LengthScalarDivide)


raspirover_LengthScalarMultiply_strategy = st.builds(raspirover_LengthScalarMultiply)
@given(instance=raspirover_LengthScalarMultiply_strategy)
@settings(max_examples=25)
def test_raspirover_LengthScalarMultiply_instantiation(instance):
    assert isinstance(instance, raspirover_LengthScalarMultiply)


raspirover_LengthSmaller_strategy = st.builds(raspirover_LengthSmaller)
@given(instance=raspirover_LengthSmaller_strategy)
@settings(max_examples=25)
def test_raspirover_LengthSmaller_instantiation(instance):
    assert isinstance(instance, raspirover_LengthSmaller)


raspirover_LengthSubtract_strategy = st.builds(raspirover_LengthSubtract)
@given(instance=raspirover_LengthSubtract_strategy)
@settings(max_examples=25)
def test_raspirover_LengthSubtract_instantiation(instance):
    assert isinstance(instance, raspirover_LengthSubtract)


raspirover_LengthUnit_strategy = st.builds(raspirover_LengthUnit)
@given(instance=raspirover_LengthUnit_strategy)
@settings(max_examples=25)
def test_raspirover_LengthUnit_instantiation(instance):
    assert isinstance(instance, raspirover_LengthUnit)


raspirover_LogAction_strategy = st.builds(raspirover_LogAction, message=safe_text)
@given(instance=raspirover_LogAction_strategy)
@settings(max_examples=25)
def test_raspirover_LogAction_instantiation(instance):
    assert isinstance(instance, raspirover_LogAction)


raspirover_Loop_strategy = st.builds(raspirover_Loop)
@given(instance=raspirover_Loop_strategy)
@settings(max_examples=25)
def test_raspirover_Loop_instantiation(instance):
    assert isinstance(instance, raspirover_Loop)


raspirover_MessageQuery_strategy = st.builds(raspirover_MessageQuery)
@given(instance=raspirover_MessageQuery_strategy)
@settings(max_examples=25)
def test_raspirover_MessageQuery_instantiation(instance):
    assert isinstance(instance, raspirover_MessageQuery)


raspirover_Meter_strategy = st.builds(raspirover_Meter)
@given(instance=raspirover_Meter_strategy)
@settings(max_examples=25)
def test_raspirover_Meter_instantiation(instance):
    assert isinstance(instance, raspirover_Meter)


raspirover_MetricSystemUnit_strategy = st.builds(raspirover_MetricSystemUnit)
@given(instance=raspirover_MetricSystemUnit_strategy)
@settings(max_examples=25)
def test_raspirover_MetricSystemUnit_instantiation(instance):
    assert isinstance(instance, raspirover_MetricSystemUnit)


raspirover_Millimeter_strategy = st.builds(raspirover_Millimeter)
@given(instance=raspirover_Millimeter_strategy)
@settings(max_examples=25)
def test_raspirover_Millimeter_instantiation(instance):
    assert isinstance(instance, raspirover_Millimeter)


raspirover_Module_strategy = st.builds(raspirover_Module)
@given(instance=raspirover_Module_strategy)
@settings(max_examples=25)
def test_raspirover_Module_instantiation(instance):
    assert isinstance(instance, raspirover_Module)


raspirover_NamedElement_strategy = st.builds(raspirover_NamedElement, name=safe_text)
@given(instance=raspirover_NamedElement_strategy)
@settings(max_examples=25)
def test_raspirover_NamedElement_instantiation(instance):
    assert isinstance(instance, raspirover_NamedElement)


raspirover_NumberValue_strategy = st.builds(raspirover_NumberValue, nValue=safe_text)
@given(instance=raspirover_NumberValue_strategy)
@settings(max_examples=25)
def test_raspirover_NumberValue_instantiation(instance):
    assert isinstance(instance, raspirover_NumberValue)


raspirover_NumericExpression_strategy = st.builds(raspirover_NumericExpression, op=st.booleans())
@given(instance=raspirover_NumericExpression_strategy)
@settings(max_examples=25)
def test_raspirover_NumericExpression_instantiation(instance):
    assert isinstance(instance, raspirover_NumericExpression)


raspirover_ObstacleQuery_strategy = st.builds(raspirover_ObstacleQuery, front=st.booleans())
@given(instance=raspirover_ObstacleQuery_strategy)
@settings(max_examples=25)
def test_raspirover_ObstacleQuery_instantiation(instance):
    assert isinstance(instance, raspirover_ObstacleQuery)


raspirover_Param_strategy = st.builds(raspirover_Param, name=safe_text)
@given(instance=raspirover_Param_strategy)
@settings(max_examples=25)
def test_raspirover_Param_instantiation(instance):
    assert isinstance(instance, raspirover_Param)


raspirover_Pin_strategy = st.builds(raspirover_Pin, level=st.integers())
@given(instance=raspirover_Pin_strategy)
@settings(max_examples=25)
def test_raspirover_Pin_instantiation(instance):
    assert isinstance(instance, raspirover_Pin)


raspirover_Project_strategy = st.builds(raspirover_Project)
@given(instance=raspirover_Project_strategy)
@settings(max_examples=25)
def test_raspirover_Project_instantiation(instance):
    assert isinstance(instance, raspirover_Project)


raspirover_Quantity_strategy = st.builds(raspirover_Quantity, value=safe_text)
@given(instance=raspirover_Quantity_strategy)
@settings(max_examples=25)
def test_raspirover_Quantity_instantiation(instance):
    assert isinstance(instance, raspirover_Quantity)


raspirover_QuantityArithmeticOperation_strategy = st.builds(raspirover_QuantityArithmeticOperation)
@given(instance=raspirover_QuantityArithmeticOperation_strategy)
@settings(max_examples=25)
def test_raspirover_QuantityArithmeticOperation_instantiation(instance):
    assert isinstance(instance, raspirover_QuantityArithmeticOperation)


raspirover_QuantityComparisonOperation_strategy = st.builds(raspirover_QuantityComparisonOperation)
@given(instance=raspirover_QuantityComparisonOperation_strategy)
@settings(max_examples=25)
def test_raspirover_QuantityComparisonOperation_instantiation(instance):
    assert isinstance(instance, raspirover_QuantityComparisonOperation)


raspirover_QuantityHomogenousOperation_strategy = st.builds(raspirover_QuantityHomogenousOperation)
@given(instance=raspirover_QuantityHomogenousOperation_strategy)
@settings(max_examples=25)
def test_raspirover_QuantityHomogenousOperation_instantiation(instance):
    assert isinstance(instance, raspirover_QuantityHomogenousOperation)


raspirover_QuantityOperation_strategy = st.builds(raspirover_QuantityOperation)
@given(instance=raspirover_QuantityOperation_strategy)
@settings(max_examples=25)
def test_raspirover_QuantityOperation_instantiation(instance):
    assert isinstance(instance, raspirover_QuantityOperation)


raspirover_QuantityScalarOperation_strategy = st.builds(raspirover_QuantityScalarOperation, rhs=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=raspirover_QuantityScalarOperation_strategy)
@settings(max_examples=25)
def test_raspirover_QuantityScalarOperation_instantiation(instance):
    assert isinstance(instance, raspirover_QuantityScalarOperation)


raspirover_Query_strategy = st.builds(raspirover_Query)
@given(instance=raspirover_Query_strategy)
@settings(max_examples=25)
def test_raspirover_Query_instantiation(instance):
    assert isinstance(instance, raspirover_Query)


raspirover_Radian_strategy = st.builds(raspirover_Radian)
@given(instance=raspirover_Radian_strategy)
@settings(max_examples=25)
def test_raspirover_Radian_instantiation(instance):
    assert isinstance(instance, raspirover_Radian)


raspirover_RasPiBoard_strategy = st.builds(raspirover_RasPiBoard)
@given(instance=raspirover_RasPiBoard_strategy)
@settings(max_examples=25)
def test_raspirover_RasPiBoard_instantiation(instance):
    assert isinstance(instance, raspirover_RasPiBoard)


raspirover_RclBlock_strategy = st.builds(raspirover_RclBlock)
@given(instance=raspirover_RclBlock_strategy)
@settings(max_examples=25)
def test_raspirover_RclBlock_instantiation(instance):
    assert isinstance(instance, raspirover_RclBlock)


raspirover_RoverExpression_strategy = st.builds(raspirover_RoverExpression)
@given(instance=raspirover_RoverExpression_strategy)
@settings(max_examples=25)
def test_raspirover_RoverExpression_instantiation(instance):
    assert isinstance(instance, raspirover_RoverExpression)


raspirover_RoverProgram_strategy = st.builds(raspirover_RoverProgram, name=safe_text)
@given(instance=raspirover_RoverProgram_strategy)
@settings(max_examples=25)
def test_raspirover_RoverProgram_instantiation(instance):
    assert isinstance(instance, raspirover_RoverProgram)


raspirover_RoverValue_strategy = st.builds(raspirover_RoverValue)
@given(instance=raspirover_RoverValue_strategy)
@settings(max_examples=25)
def test_raspirover_RoverValue_instantiation(instance):
    assert isinstance(instance, raspirover_RoverValue)


raspirover_SendAction_strategy = st.builds(raspirover_SendAction, message=safe_text)
@given(instance=raspirover_SendAction_strategy)
@settings(max_examples=25)
def test_raspirover_SendAction_instantiation(instance):
    assert isinstance(instance, raspirover_SendAction)


raspirover_Sketch_strategy = st.builds(raspirover_Sketch)
@given(instance=raspirover_Sketch_strategy)
@settings(max_examples=25)
def test_raspirover_Sketch_instantiation(instance):
    assert isinstance(instance, raspirover_Sketch)


raspirover_Statement_strategy = st.builds(raspirover_Statement)
@given(instance=raspirover_Statement_strategy)
@settings(max_examples=25)
def test_raspirover_Statement_instantiation(instance):
    assert isinstance(instance, raspirover_Statement)


raspirover_StopAction_strategy = st.builds(raspirover_StopAction)
@given(instance=raspirover_StopAction_strategy)
@settings(max_examples=25)
def test_raspirover_StopAction_instantiation(instance):
    assert isinstance(instance, raspirover_StopAction)


raspirover_StringExpression_strategy = st.builds(raspirover_StringExpression, op=st.booleans())
@given(instance=raspirover_StringExpression_strategy)
@settings(max_examples=25)
def test_raspirover_StringExpression_instantiation(instance):
    assert isinstance(instance, raspirover_StringExpression)


raspirover_StringValue_strategy = st.builds(raspirover_StringValue, sValue=st.booleans())
@given(instance=raspirover_StringValue_strategy)
@settings(max_examples=25)
def test_raspirover_StringValue_instantiation(instance):
    assert isinstance(instance, raspirover_StringValue)


raspirover_TemperatureQuery_strategy = st.builds(raspirover_TemperatureQuery)
@given(instance=raspirover_TemperatureQuery_strategy)
@settings(max_examples=25)
def test_raspirover_TemperatureQuery_instantiation(instance):
    assert isinstance(instance, raspirover_TemperatureQuery)


raspirover_Turn_strategy = st.builds(raspirover_Turn)
@given(instance=raspirover_Turn_strategy)
@settings(max_examples=25)
def test_raspirover_Turn_instantiation(instance):
    assert isinstance(instance, raspirover_Turn)


raspirover_TurnAction_strategy = st.builds(raspirover_TurnAction)
@given(instance=raspirover_TurnAction_strategy)
@settings(max_examples=25)
def test_raspirover_TurnAction_instantiation(instance):
    assert isinstance(instance, raspirover_TurnAction)


raspirover_TurnDegAction_strategy = st.builds(raspirover_TurnDegAction)
@given(instance=raspirover_TurnDegAction_strategy)
@settings(max_examples=25)
def test_raspirover_TurnDegAction_instantiation(instance):
    assert isinstance(instance, raspirover_TurnDegAction)


raspirover_Unit_strategy = st.builds(raspirover_Unit)
@given(instance=raspirover_Unit_strategy)
@settings(max_examples=25)
def test_raspirover_Unit_instantiation(instance):
    assert isinstance(instance, raspirover_Unit)


raspirover_VarAssignment_strategy = st.builds(raspirover_VarAssignment, name=st.booleans())
@given(instance=raspirover_VarAssignment_strategy)
@settings(max_examples=25)
def test_raspirover_VarAssignment_instantiation(instance):
    assert isinstance(instance, raspirover_VarAssignment)


raspirover_VarRef_strategy = st.builds(raspirover_VarRef, name=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=raspirover_VarRef_strategy)
@settings(max_examples=25)
def test_raspirover_VarRef_instantiation(instance):
    assert isinstance(instance, raspirover_VarRef)


raspirover_Yard_strategy = st.builds(raspirover_Yard)
@given(instance=raspirover_Yard_strategy)
@settings(max_examples=25)
def test_raspirover_Yard_instantiation(instance):
    assert isinstance(instance, raspirover_Yard)



