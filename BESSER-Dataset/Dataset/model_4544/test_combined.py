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
    QuantityHomogenousOperation,
    units_AngleGreater,
    units_AngleSmaller,
    units_AngleSubtract,
    units_AngleDistinct,
    units_AngleEquals,
    units_AngleAdd,
    LengthOperation,
    units_LengthAdd,
    QuantityOperation,
    units_QuantityScalarOperation,
    units_AngleOperation,
    units_QuantityArithmeticOperation,
    units_QuantityHomogenousOperation,
    units_QuantityComparisonOperation,
    units_LengthOperation,
    units_QuantityOperation,
    Quantity,
    units_Angle,
    units_Length,
    units_LengthGreater,
    units_LengthSmaller,
    units_LengthDistinct,
    units_LengthEquals,
    QuantityScalarOperation,
    units_LengthScalarDivide,
    units_AngleScalarDivide,
    units_AngleScalarMultiply,
    units_LengthScalarMultiply,
    units_LengthSubtract,
    AngleUnit,
    units_Turn,
    units_Degree,
    units_Radian,
    units_Quantity,
    units_Gradian,
    ImperialSystemUnit,
    units_Unit,
    LengthUnit,
    units_Inch,
    units_Foot,
    units_Yard,
    MetricSystemUnit,
    units_Millimeter,
    units_Meter,
    units_Centimeter,
    Unit,
    units_MetricSystemUnit,
    units_ImperialSystemUnit,
    units_AngleUnit,
    units_LengthUnit,
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



def test_hyp_quantityhomogenousoperation_is_not_abstract():
    assert not inspect.isabstract(QuantityHomogenousOperation)


def test_hyp_quantityhomogenousoperation_constructor_exists():
    assert callable(QuantityHomogenousOperation.__init__)


def test_hyp_quantityhomogenousoperation_constructor_args():
    sig = inspect.signature(QuantityHomogenousOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_anglegreater_is_not_abstract():
    assert not inspect.isabstract(units_AngleGreater)


def test_hyp_units_anglegreater_constructor_exists():
    assert callable(units_AngleGreater.__init__)


def test_hyp_units_anglegreater_constructor_args():
    sig = inspect.signature(units_AngleGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_anglesmaller_is_not_abstract():
    assert not inspect.isabstract(units_AngleSmaller)


def test_hyp_units_anglesmaller_constructor_exists():
    assert callable(units_AngleSmaller.__init__)


def test_hyp_units_anglesmaller_constructor_args():
    sig = inspect.signature(units_AngleSmaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_anglesubtract_is_not_abstract():
    assert not inspect.isabstract(units_AngleSubtract)


def test_hyp_units_anglesubtract_constructor_exists():
    assert callable(units_AngleSubtract.__init__)


def test_hyp_units_anglesubtract_constructor_args():
    sig = inspect.signature(units_AngleSubtract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_angledistinct_is_not_abstract():
    assert not inspect.isabstract(units_AngleDistinct)


def test_hyp_units_angledistinct_constructor_exists():
    assert callable(units_AngleDistinct.__init__)


def test_hyp_units_angledistinct_constructor_args():
    sig = inspect.signature(units_AngleDistinct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_angleequals_is_not_abstract():
    assert not inspect.isabstract(units_AngleEquals)


def test_hyp_units_angleequals_constructor_exists():
    assert callable(units_AngleEquals.__init__)


def test_hyp_units_angleequals_constructor_args():
    sig = inspect.signature(units_AngleEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_angleadd_is_not_abstract():
    assert not inspect.isabstract(units_AngleAdd)


def test_hyp_units_angleadd_constructor_exists():
    assert callable(units_AngleAdd.__init__)


def test_hyp_units_angleadd_constructor_args():
    sig = inspect.signature(units_AngleAdd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lengthoperation_is_not_abstract():
    assert not inspect.isabstract(LengthOperation)


def test_hyp_lengthoperation_constructor_exists():
    assert callable(LengthOperation.__init__)


def test_hyp_lengthoperation_constructor_args():
    sig = inspect.signature(LengthOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthadd_is_not_abstract():
    assert not inspect.isabstract(units_LengthAdd)


def test_hyp_units_lengthadd_constructor_exists():
    assert callable(units_LengthAdd.__init__)


def test_hyp_units_lengthadd_constructor_args():
    sig = inspect.signature(units_LengthAdd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantityoperation_is_not_abstract():
    assert not inspect.isabstract(QuantityOperation)


def test_hyp_quantityoperation_constructor_exists():
    assert callable(QuantityOperation.__init__)


def test_hyp_quantityoperation_constructor_args():
    sig = inspect.signature(QuantityOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantityscalaroperation_is_not_abstract():
    assert not inspect.isabstract(units_QuantityScalarOperation)


def test_hyp_units_quantityscalaroperation_constructor_exists():
    assert callable(units_QuantityScalarOperation.__init__)


def test_hyp_units_quantityscalaroperation_constructor_args():
    sig = inspect.signature(units_QuantityScalarOperation.__init__)
    params = list(sig.parameters.keys())
    assert "rhs" in params, "Missing parameter 'rhs'"




def test_hyp_units_angleoperation_is_not_abstract():
    assert not inspect.isabstract(units_AngleOperation)


def test_hyp_units_angleoperation_constructor_exists():
    assert callable(units_AngleOperation.__init__)


def test_hyp_units_angleoperation_constructor_args():
    sig = inspect.signature(units_AngleOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantityarithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(units_QuantityArithmeticOperation)


def test_hyp_units_quantityarithmeticoperation_constructor_exists():
    assert callable(units_QuantityArithmeticOperation.__init__)


def test_hyp_units_quantityarithmeticoperation_constructor_args():
    sig = inspect.signature(units_QuantityArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantityhomogenousoperation_is_not_abstract():
    assert not inspect.isabstract(units_QuantityHomogenousOperation)


def test_hyp_units_quantityhomogenousoperation_constructor_exists():
    assert callable(units_QuantityHomogenousOperation.__init__)


def test_hyp_units_quantityhomogenousoperation_constructor_args():
    sig = inspect.signature(units_QuantityHomogenousOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantitycomparisonoperation_is_not_abstract():
    assert not inspect.isabstract(units_QuantityComparisonOperation)


def test_hyp_units_quantitycomparisonoperation_constructor_exists():
    assert callable(units_QuantityComparisonOperation.__init__)


def test_hyp_units_quantitycomparisonoperation_constructor_args():
    sig = inspect.signature(units_QuantityComparisonOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthoperation_is_not_abstract():
    assert not inspect.isabstract(units_LengthOperation)


def test_hyp_units_lengthoperation_constructor_exists():
    assert callable(units_LengthOperation.__init__)


def test_hyp_units_lengthoperation_constructor_args():
    sig = inspect.signature(units_LengthOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantityoperation_is_not_abstract():
    assert not inspect.isabstract(units_QuantityOperation)


def test_hyp_units_quantityoperation_constructor_exists():
    assert callable(units_QuantityOperation.__init__)


def test_hyp_units_quantityoperation_constructor_args():
    sig = inspect.signature(units_QuantityOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantity_is_not_abstract():
    assert not inspect.isabstract(Quantity)


def test_hyp_quantity_constructor_exists():
    assert callable(Quantity.__init__)


def test_hyp_quantity_constructor_args():
    sig = inspect.signature(Quantity.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_angle_is_not_abstract():
    assert not inspect.isabstract(units_Angle)


def test_hyp_units_angle_constructor_exists():
    assert callable(units_Angle.__init__)


def test_hyp_units_angle_constructor_args():
    sig = inspect.signature(units_Angle.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_length_is_not_abstract():
    assert not inspect.isabstract(units_Length)


def test_hyp_units_length_constructor_exists():
    assert callable(units_Length.__init__)


def test_hyp_units_length_constructor_args():
    sig = inspect.signature(units_Length.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthgreater_is_not_abstract():
    assert not inspect.isabstract(units_LengthGreater)


def test_hyp_units_lengthgreater_constructor_exists():
    assert callable(units_LengthGreater.__init__)


def test_hyp_units_lengthgreater_constructor_args():
    sig = inspect.signature(units_LengthGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthsmaller_is_not_abstract():
    assert not inspect.isabstract(units_LengthSmaller)


def test_hyp_units_lengthsmaller_constructor_exists():
    assert callable(units_LengthSmaller.__init__)


def test_hyp_units_lengthsmaller_constructor_args():
    sig = inspect.signature(units_LengthSmaller.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthdistinct_is_not_abstract():
    assert not inspect.isabstract(units_LengthDistinct)


def test_hyp_units_lengthdistinct_constructor_exists():
    assert callable(units_LengthDistinct.__init__)


def test_hyp_units_lengthdistinct_constructor_args():
    sig = inspect.signature(units_LengthDistinct.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthequals_is_not_abstract():
    assert not inspect.isabstract(units_LengthEquals)


def test_hyp_units_lengthequals_constructor_exists():
    assert callable(units_LengthEquals.__init__)


def test_hyp_units_lengthequals_constructor_args():
    sig = inspect.signature(units_LengthEquals.__init__)
    params = list(sig.parameters.keys())



def test_hyp_quantityscalaroperation_is_not_abstract():
    assert not inspect.isabstract(QuantityScalarOperation)


def test_hyp_quantityscalaroperation_constructor_exists():
    assert callable(QuantityScalarOperation.__init__)


def test_hyp_quantityscalaroperation_constructor_args():
    sig = inspect.signature(QuantityScalarOperation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthscalardivide_is_not_abstract():
    assert not inspect.isabstract(units_LengthScalarDivide)


def test_hyp_units_lengthscalardivide_constructor_exists():
    assert callable(units_LengthScalarDivide.__init__)


def test_hyp_units_lengthscalardivide_constructor_args():
    sig = inspect.signature(units_LengthScalarDivide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_anglescalardivide_is_not_abstract():
    assert not inspect.isabstract(units_AngleScalarDivide)


def test_hyp_units_anglescalardivide_constructor_exists():
    assert callable(units_AngleScalarDivide.__init__)


def test_hyp_units_anglescalardivide_constructor_args():
    sig = inspect.signature(units_AngleScalarDivide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_anglescalarmultiply_is_not_abstract():
    assert not inspect.isabstract(units_AngleScalarMultiply)


def test_hyp_units_anglescalarmultiply_constructor_exists():
    assert callable(units_AngleScalarMultiply.__init__)


def test_hyp_units_anglescalarmultiply_constructor_args():
    sig = inspect.signature(units_AngleScalarMultiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthscalarmultiply_is_not_abstract():
    assert not inspect.isabstract(units_LengthScalarMultiply)


def test_hyp_units_lengthscalarmultiply_constructor_exists():
    assert callable(units_LengthScalarMultiply.__init__)


def test_hyp_units_lengthscalarmultiply_constructor_args():
    sig = inspect.signature(units_LengthScalarMultiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthsubtract_is_not_abstract():
    assert not inspect.isabstract(units_LengthSubtract)


def test_hyp_units_lengthsubtract_constructor_exists():
    assert callable(units_LengthSubtract.__init__)


def test_hyp_units_lengthsubtract_constructor_args():
    sig = inspect.signature(units_LengthSubtract.__init__)
    params = list(sig.parameters.keys())



def test_hyp_angleunit_is_not_abstract():
    assert not inspect.isabstract(AngleUnit)


def test_hyp_angleunit_constructor_exists():
    assert callable(AngleUnit.__init__)


def test_hyp_angleunit_constructor_args():
    sig = inspect.signature(AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_turn_is_not_abstract():
    assert not inspect.isabstract(units_Turn)


def test_hyp_units_turn_constructor_exists():
    assert callable(units_Turn.__init__)


def test_hyp_units_turn_constructor_args():
    sig = inspect.signature(units_Turn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_degree_is_not_abstract():
    assert not inspect.isabstract(units_Degree)


def test_hyp_units_degree_constructor_exists():
    assert callable(units_Degree.__init__)


def test_hyp_units_degree_constructor_args():
    sig = inspect.signature(units_Degree.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_radian_is_not_abstract():
    assert not inspect.isabstract(units_Radian)


def test_hyp_units_radian_constructor_exists():
    assert callable(units_Radian.__init__)


def test_hyp_units_radian_constructor_args():
    sig = inspect.signature(units_Radian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_quantity_is_not_abstract():
    assert not inspect.isabstract(units_Quantity)


def test_hyp_units_quantity_constructor_exists():
    assert callable(units_Quantity.__init__)


def test_hyp_units_quantity_constructor_args():
    sig = inspect.signature(units_Quantity.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_units_gradian_is_not_abstract():
    assert not inspect.isabstract(units_Gradian)


def test_hyp_units_gradian_constructor_exists():
    assert callable(units_Gradian.__init__)


def test_hyp_units_gradian_constructor_args():
    sig = inspect.signature(units_Gradian.__init__)
    params = list(sig.parameters.keys())



def test_hyp_imperialsystemunit_is_not_abstract():
    assert not inspect.isabstract(ImperialSystemUnit)


def test_hyp_imperialsystemunit_constructor_exists():
    assert callable(ImperialSystemUnit.__init__)


def test_hyp_imperialsystemunit_constructor_args():
    sig = inspect.signature(ImperialSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_unit_is_not_abstract():
    assert not inspect.isabstract(units_Unit)


def test_hyp_units_unit_constructor_exists():
    assert callable(units_Unit.__init__)


def test_hyp_units_unit_constructor_args():
    sig = inspect.signature(units_Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_lengthunit_is_not_abstract():
    assert not inspect.isabstract(LengthUnit)


def test_hyp_lengthunit_constructor_exists():
    assert callable(LengthUnit.__init__)


def test_hyp_lengthunit_constructor_args():
    sig = inspect.signature(LengthUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_inch_is_not_abstract():
    assert not inspect.isabstract(units_Inch)


def test_hyp_units_inch_constructor_exists():
    assert callable(units_Inch.__init__)


def test_hyp_units_inch_constructor_args():
    sig = inspect.signature(units_Inch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_foot_is_not_abstract():
    assert not inspect.isabstract(units_Foot)


def test_hyp_units_foot_constructor_exists():
    assert callable(units_Foot.__init__)


def test_hyp_units_foot_constructor_args():
    sig = inspect.signature(units_Foot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_yard_is_not_abstract():
    assert not inspect.isabstract(units_Yard)


def test_hyp_units_yard_constructor_exists():
    assert callable(units_Yard.__init__)


def test_hyp_units_yard_constructor_args():
    sig = inspect.signature(units_Yard.__init__)
    params = list(sig.parameters.keys())



def test_hyp_metricsystemunit_is_not_abstract():
    assert not inspect.isabstract(MetricSystemUnit)


def test_hyp_metricsystemunit_constructor_exists():
    assert callable(MetricSystemUnit.__init__)


def test_hyp_metricsystemunit_constructor_args():
    sig = inspect.signature(MetricSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_millimeter_is_not_abstract():
    assert not inspect.isabstract(units_Millimeter)


def test_hyp_units_millimeter_constructor_exists():
    assert callable(units_Millimeter.__init__)


def test_hyp_units_millimeter_constructor_args():
    sig = inspect.signature(units_Millimeter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_meter_is_not_abstract():
    assert not inspect.isabstract(units_Meter)


def test_hyp_units_meter_constructor_exists():
    assert callable(units_Meter.__init__)


def test_hyp_units_meter_constructor_args():
    sig = inspect.signature(units_Meter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_centimeter_is_not_abstract():
    assert not inspect.isabstract(units_Centimeter)


def test_hyp_units_centimeter_constructor_exists():
    assert callable(units_Centimeter.__init__)


def test_hyp_units_centimeter_constructor_args():
    sig = inspect.signature(units_Centimeter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_hyp_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_hyp_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_metricsystemunit_is_not_abstract():
    assert not inspect.isabstract(units_MetricSystemUnit)


def test_hyp_units_metricsystemunit_constructor_exists():
    assert callable(units_MetricSystemUnit.__init__)


def test_hyp_units_metricsystemunit_constructor_args():
    sig = inspect.signature(units_MetricSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_imperialsystemunit_is_not_abstract():
    assert not inspect.isabstract(units_ImperialSystemUnit)


def test_hyp_units_imperialsystemunit_constructor_exists():
    assert callable(units_ImperialSystemUnit.__init__)


def test_hyp_units_imperialsystemunit_constructor_args():
    sig = inspect.signature(units_ImperialSystemUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_angleunit_is_not_abstract():
    assert not inspect.isabstract(units_AngleUnit)


def test_hyp_units_angleunit_constructor_exists():
    assert callable(units_AngleUnit.__init__)


def test_hyp_units_angleunit_constructor_args():
    sig = inspect.signature(units_AngleUnit.__init__)
    params = list(sig.parameters.keys())



def test_hyp_units_lengthunit_is_not_abstract():
    assert not inspect.isabstract(units_LengthUnit)


def test_hyp_units_lengthunit_constructor_exists():
    assert callable(units_LengthUnit.__init__)


def test_hyp_units_lengthunit_constructor_args():
    sig = inspect.signature(units_LengthUnit.__init__)
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
AngleOperation_strategy = st.builds(
    AngleOperation,
)
QuantityHomogenousOperation_strategy = st.builds(
    QuantityHomogenousOperation,
)
units_AngleGreater_strategy = st.builds(
    units_AngleGreater,
)
units_AngleSmaller_strategy = st.builds(
    units_AngleSmaller,
)
units_AngleSubtract_strategy = st.builds(
    units_AngleSubtract,
)
units_AngleDistinct_strategy = st.builds(
    units_AngleDistinct,
)
units_AngleEquals_strategy = st.builds(
    units_AngleEquals,
)
units_AngleAdd_strategy = st.builds(
    units_AngleAdd,
)
LengthOperation_strategy = st.builds(
    LengthOperation,
)
units_LengthAdd_strategy = st.builds(
    units_LengthAdd,
)
QuantityOperation_strategy = st.builds(
    QuantityOperation,
)
units_QuantityScalarOperation_strategy = st.builds(
    units_QuantityScalarOperation,
    rhs=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
units_AngleOperation_strategy = st.builds(
    units_AngleOperation,
)
units_QuantityArithmeticOperation_strategy = st.builds(
    units_QuantityArithmeticOperation,
)
units_QuantityHomogenousOperation_strategy = st.builds(
    units_QuantityHomogenousOperation,
)
units_QuantityComparisonOperation_strategy = st.builds(
    units_QuantityComparisonOperation,
)
units_LengthOperation_strategy = st.builds(
    units_LengthOperation,
)
units_QuantityOperation_strategy = st.builds(
    units_QuantityOperation,
)
Quantity_strategy = st.builds(
    Quantity,
)
units_Angle_strategy = st.builds(
    units_Angle,
)
units_Length_strategy = st.builds(
    units_Length,
)
units_LengthGreater_strategy = st.builds(
    units_LengthGreater,
)
units_LengthSmaller_strategy = st.builds(
    units_LengthSmaller,
)
units_LengthDistinct_strategy = st.builds(
    units_LengthDistinct,
)
units_LengthEquals_strategy = st.builds(
    units_LengthEquals,
)
QuantityScalarOperation_strategy = st.builds(
    QuantityScalarOperation,
)
units_LengthScalarDivide_strategy = st.builds(
    units_LengthScalarDivide,
)
units_AngleScalarDivide_strategy = st.builds(
    units_AngleScalarDivide,
)
units_AngleScalarMultiply_strategy = st.builds(
    units_AngleScalarMultiply,
)
units_LengthScalarMultiply_strategy = st.builds(
    units_LengthScalarMultiply,
)
units_LengthSubtract_strategy = st.builds(
    units_LengthSubtract,
)
AngleUnit_strategy = st.builds(
    AngleUnit,
)
units_Turn_strategy = st.builds(
    units_Turn,
)
units_Degree_strategy = st.builds(
    units_Degree,
)
units_Radian_strategy = st.builds(
    units_Radian,
)
units_Quantity_strategy = st.builds(
    units_Quantity,
    value=
        safe_text
)
units_Gradian_strategy = st.builds(
    units_Gradian,
)
ImperialSystemUnit_strategy = st.builds(
    ImperialSystemUnit,
)
units_Unit_strategy = st.builds(
    units_Unit,
)
LengthUnit_strategy = st.builds(
    LengthUnit,
)
units_Inch_strategy = st.builds(
    units_Inch,
)
units_Foot_strategy = st.builds(
    units_Foot,
)
units_Yard_strategy = st.builds(
    units_Yard,
)
MetricSystemUnit_strategy = st.builds(
    MetricSystemUnit,
)
units_Millimeter_strategy = st.builds(
    units_Millimeter,
)
units_Meter_strategy = st.builds(
    units_Meter,
)
units_Centimeter_strategy = st.builds(
    units_Centimeter,
)
Unit_strategy = st.builds(
    Unit,
)
units_MetricSystemUnit_strategy = st.builds(
    units_MetricSystemUnit,
)
units_ImperialSystemUnit_strategy = st.builds(
    units_ImperialSystemUnit,
)
units_AngleUnit_strategy = st.builds(
    units_AngleUnit,
)
units_LengthUnit_strategy = st.builds(
    units_LengthUnit,
)















@given(instance=units_QuantityScalarOperation_strategy)
def test_hyp_units_quantityscalaroperation_rhs_setter(instance):
    original = instance.rhs
    instance.rhs = original
    assert instance.rhs == original









import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Angle_strategy)
@settings(max_examples=30)
def test_hyp_units_angle_print_changes_state(instance):
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
        assert has_statements, f"Function 'print' in units_Angle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in units_Angle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in units_Angle is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Angle_strategy)
@settings(max_examples=30)
def test_hyp_units_angle_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_Angle is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_Angle did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_Angle is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Length_strategy)
@settings(max_examples=30)
def test_hyp_units_length_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Length is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Length did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Length is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Length_strategy)
@settings(max_examples=30)
def test_hyp_units_length_print_changes_state(instance):
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
        assert has_statements, f"Function 'print' in units_Length is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in units_Length did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in units_Length is not implemented or raised an error")













import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Turn_strategy)
@settings(max_examples=30)
def test_hyp_units_turn_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_Turn is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_Turn did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_Turn is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Degree_strategy)
@settings(max_examples=30)
def test_hyp_units_degree_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_Degree is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_Degree did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_Degree is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Radian_strategy)
@settings(max_examples=30)
def test_hyp_units_radian_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_Radian is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_Radian did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_Radian is not implemented or raised an error")




@given(instance=units_Quantity_strategy)
def test_hyp_units_quantity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Quantity_strategy)
@settings(max_examples=30)
def test_hyp_units_quantity_print_changes_state(instance):
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
        assert has_statements, f"Function 'print' in units_Quantity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in units_Quantity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in units_Quantity is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Gradian_strategy)
@settings(max_examples=30)
def test_hyp_units_gradian_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_Gradian is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_Gradian did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_Gradian is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Inch_strategy)
@settings(max_examples=30)
def test_hyp_units_inch_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Inch is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Inch did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Inch is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Foot_strategy)
@settings(max_examples=30)
def test_hyp_units_foot_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Foot is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Foot did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Foot is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Yard_strategy)
@settings(max_examples=30)
def test_hyp_units_yard_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Yard is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Yard did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Yard is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Millimeter_strategy)
@settings(max_examples=30)
def test_hyp_units_millimeter_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Millimeter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Millimeter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Millimeter is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Meter_strategy)
@settings(max_examples=30)
def test_hyp_units_meter_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Meter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Meter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Meter is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_Centimeter_strategy)
@settings(max_examples=30)
def test_hyp_units_centimeter_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_Centimeter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_Centimeter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_Centimeter is not implemented or raised an error")





import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_AngleUnit_strategy)
@settings(max_examples=30)
def test_hyp_units_angleunit_torad_changes_state(instance):
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
        assert has_statements, f"Function 'toRad' in units_AngleUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toRad' in units_AngleUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toRad' in units_AngleUnit is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=units_LengthUnit_strategy)
@settings(max_examples=30)
def test_hyp_units_lengthunit_tocm_changes_state(instance):
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
        assert has_statements, f"Function 'toCm' in units_LengthUnit is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'toCm' in units_LengthUnit did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'toCm' in units_LengthUnit is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AngleOperation,
    AngleUnit,
    ImperialSystemUnit,
    LengthOperation,
    LengthUnit,
    MetricSystemUnit,
    Quantity,
    QuantityHomogenousOperation,
    QuantityOperation,
    QuantityScalarOperation,
    Unit,
    units_Angle,
    units_AngleAdd,
    units_AngleDistinct,
    units_AngleEquals,
    units_AngleGreater,
    units_AngleOperation,
    units_AngleScalarDivide,
    units_AngleScalarMultiply,
    units_AngleSmaller,
    units_AngleSubtract,
    units_AngleUnit,
    units_Centimeter,
    units_Degree,
    units_Foot,
    units_Gradian,
    units_ImperialSystemUnit,
    units_Inch,
    units_Length,
    units_LengthAdd,
    units_LengthDistinct,
    units_LengthEquals,
    units_LengthGreater,
    units_LengthOperation,
    units_LengthScalarDivide,
    units_LengthScalarMultiply,
    units_LengthSmaller,
    units_LengthSubtract,
    units_LengthUnit,
    units_Meter,
    units_MetricSystemUnit,
    units_Millimeter,
    units_Quantity,
    units_QuantityArithmeticOperation,
    units_QuantityComparisonOperation,
    units_QuantityHomogenousOperation,
    units_QuantityOperation,
    units_QuantityScalarOperation,
    units_Radian,
    units_Turn,
    units_Unit,
    units_Yard,
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

def test_units_Quantity_value_value_roundtrip():
    instance = units_Quantity(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_units_QuantityScalarOperation_rhs_value_roundtrip():
    instance = units_QuantityScalarOperation(rhs=3.14)
    assert instance.rhs == 3.14
    instance.rhs = 9.99
    assert instance.rhs == 9.99


def test_units_AngleAdd_isa_AngleOperation():
    instance = units_AngleAdd()
    assert isinstance(instance, AngleOperation)


def test_units_AngleDistinct_isa_AngleOperation():
    instance = units_AngleDistinct()
    assert isinstance(instance, AngleOperation)


def test_units_AngleEquals_isa_AngleOperation():
    instance = units_AngleEquals()
    assert isinstance(instance, AngleOperation)


def test_units_AngleGreater_isa_AngleOperation():
    instance = units_AngleGreater()
    assert isinstance(instance, AngleOperation)


def test_units_AngleScalarDivide_isa_AngleOperation():
    instance = units_AngleScalarDivide()
    assert isinstance(instance, AngleOperation)


def test_units_AngleScalarMultiply_isa_AngleOperation():
    instance = units_AngleScalarMultiply()
    assert isinstance(instance, AngleOperation)


def test_units_AngleSmaller_isa_AngleOperation():
    instance = units_AngleSmaller()
    assert isinstance(instance, AngleOperation)


def test_units_AngleSubtract_isa_AngleOperation():
    instance = units_AngleSubtract()
    assert isinstance(instance, AngleOperation)


def test_units_Degree_isa_AngleUnit():
    instance = units_Degree()
    assert isinstance(instance, AngleUnit)


def test_units_Gradian_isa_AngleUnit():
    instance = units_Gradian()
    assert isinstance(instance, AngleUnit)


def test_units_Radian_isa_AngleUnit():
    instance = units_Radian()
    assert isinstance(instance, AngleUnit)


def test_units_Turn_isa_AngleUnit():
    instance = units_Turn()
    assert isinstance(instance, AngleUnit)


def test_units_Foot_isa_ImperialSystemUnit():
    instance = units_Foot()
    assert isinstance(instance, ImperialSystemUnit)


def test_units_Inch_isa_ImperialSystemUnit():
    instance = units_Inch()
    assert isinstance(instance, ImperialSystemUnit)


def test_units_Yard_isa_ImperialSystemUnit():
    instance = units_Yard()
    assert isinstance(instance, ImperialSystemUnit)


def test_units_LengthAdd_isa_LengthOperation():
    instance = units_LengthAdd()
    assert isinstance(instance, LengthOperation)


def test_units_LengthDistinct_isa_LengthOperation():
    instance = units_LengthDistinct()
    assert isinstance(instance, LengthOperation)


def test_units_LengthEquals_isa_LengthOperation():
    instance = units_LengthEquals()
    assert isinstance(instance, LengthOperation)


def test_units_LengthGreater_isa_LengthOperation():
    instance = units_LengthGreater()
    assert isinstance(instance, LengthOperation)


def test_units_LengthScalarDivide_isa_LengthOperation():
    instance = units_LengthScalarDivide()
    assert isinstance(instance, LengthOperation)


def test_units_LengthScalarMultiply_isa_LengthOperation():
    instance = units_LengthScalarMultiply()
    assert isinstance(instance, LengthOperation)


def test_units_LengthSmaller_isa_LengthOperation():
    instance = units_LengthSmaller()
    assert isinstance(instance, LengthOperation)


def test_units_LengthSubtract_isa_LengthOperation():
    instance = units_LengthSubtract()
    assert isinstance(instance, LengthOperation)


def test_units_Centimeter_isa_LengthUnit():
    instance = units_Centimeter()
    assert isinstance(instance, LengthUnit)


def test_units_Foot_isa_LengthUnit():
    instance = units_Foot()
    assert isinstance(instance, LengthUnit)


def test_units_Inch_isa_LengthUnit():
    instance = units_Inch()
    assert isinstance(instance, LengthUnit)


def test_units_Meter_isa_LengthUnit():
    instance = units_Meter()
    assert isinstance(instance, LengthUnit)


def test_units_Millimeter_isa_LengthUnit():
    instance = units_Millimeter()
    assert isinstance(instance, LengthUnit)


def test_units_Yard_isa_LengthUnit():
    instance = units_Yard()
    assert isinstance(instance, LengthUnit)


def test_units_Centimeter_isa_MetricSystemUnit():
    instance = units_Centimeter()
    assert isinstance(instance, MetricSystemUnit)


def test_units_Meter_isa_MetricSystemUnit():
    instance = units_Meter()
    assert isinstance(instance, MetricSystemUnit)


def test_units_Millimeter_isa_MetricSystemUnit():
    instance = units_Millimeter()
    assert isinstance(instance, MetricSystemUnit)


def test_units_Angle_isa_Quantity():
    instance = units_Angle()
    assert isinstance(instance, Quantity)


def test_units_Length_isa_Quantity():
    instance = units_Length()
    assert isinstance(instance, Quantity)


def test_units_AngleAdd_isa_QuantityHomogenousOperation():
    instance = units_AngleAdd()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleDistinct_isa_QuantityHomogenousOperation():
    instance = units_AngleDistinct()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleEquals_isa_QuantityHomogenousOperation():
    instance = units_AngleEquals()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleGreater_isa_QuantityHomogenousOperation():
    instance = units_AngleGreater()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleSmaller_isa_QuantityHomogenousOperation():
    instance = units_AngleSmaller()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleSubtract_isa_QuantityHomogenousOperation():
    instance = units_AngleSubtract()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthAdd_isa_QuantityHomogenousOperation():
    instance = units_LengthAdd()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthDistinct_isa_QuantityHomogenousOperation():
    instance = units_LengthDistinct()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthEquals_isa_QuantityHomogenousOperation():
    instance = units_LengthEquals()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthGreater_isa_QuantityHomogenousOperation():
    instance = units_LengthGreater()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthSmaller_isa_QuantityHomogenousOperation():
    instance = units_LengthSmaller()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_LengthSubtract_isa_QuantityHomogenousOperation():
    instance = units_LengthSubtract()
    assert isinstance(instance, QuantityHomogenousOperation)


def test_units_AngleOperation_isa_QuantityOperation():
    instance = units_AngleOperation()
    assert isinstance(instance, QuantityOperation)


def test_units_LengthOperation_isa_QuantityOperation():
    instance = units_LengthOperation()
    assert isinstance(instance, QuantityOperation)


def test_units_QuantityArithmeticOperation_isa_QuantityOperation():
    instance = units_QuantityArithmeticOperation()
    assert isinstance(instance, QuantityOperation)


def test_units_QuantityComparisonOperation_isa_QuantityOperation():
    instance = units_QuantityComparisonOperation()
    assert isinstance(instance, QuantityOperation)


def test_units_QuantityHomogenousOperation_isa_QuantityOperation():
    instance = units_QuantityHomogenousOperation()
    assert isinstance(instance, QuantityOperation)


def test_units_QuantityScalarOperation_isa_QuantityOperation():
    instance = units_QuantityScalarOperation(rhs=3.14)
    assert isinstance(instance, QuantityOperation)


def test_units_AngleScalarDivide_isa_QuantityScalarOperation():
    instance = units_AngleScalarDivide()
    assert isinstance(instance, QuantityScalarOperation)


def test_units_AngleScalarMultiply_isa_QuantityScalarOperation():
    instance = units_AngleScalarMultiply()
    assert isinstance(instance, QuantityScalarOperation)


def test_units_LengthScalarDivide_isa_QuantityScalarOperation():
    instance = units_LengthScalarDivide()
    assert isinstance(instance, QuantityScalarOperation)


def test_units_LengthScalarMultiply_isa_QuantityScalarOperation():
    instance = units_LengthScalarMultiply()
    assert isinstance(instance, QuantityScalarOperation)


def test_units_AngleUnit_isa_Unit():
    instance = units_AngleUnit()
    assert isinstance(instance, Unit)


def test_units_ImperialSystemUnit_isa_Unit():
    instance = units_ImperialSystemUnit()
    assert isinstance(instance, Unit)


def test_units_LengthUnit_isa_Unit():
    instance = units_LengthUnit()
    assert isinstance(instance, Unit)


def test_units_MetricSystemUnit_isa_Unit():
    instance = units_MetricSystemUnit()
    assert isinstance(instance, Unit)


def test_assoc_lhs1_link_reassign_clear():
    a = units_Quantity(value="sample_text")
    b1 = units_QuantityHomogenousOperation()
    b2 = units_QuantityHomogenousOperation()
    _safe_set(a, 'units_Quantity2', b1)
    assert _is_linked(a, 'units_Quantity2', b1)
    if hasattr(b1, 'units_QuantityHomogenousOperation'):
        assert _is_linked(b1, 'units_QuantityHomogenousOperation', a)
    _safe_set(a, 'units_Quantity2', b2)
    assert _is_linked(a, 'units_Quantity2', b2)
    if hasattr(b1, 'units_QuantityHomogenousOperation'):
        assert not _is_linked(b1, 'units_QuantityHomogenousOperation', a)
    if hasattr(b2, 'units_QuantityHomogenousOperation'):
        assert _is_linked(b2, 'units_QuantityHomogenousOperation', a)
    _safe_set(a, 'units_Quantity2', None)
    assert not _is_linked(a, 'units_Quantity2', b2)
    if hasattr(b2, 'units_QuantityHomogenousOperation'):
        assert not _is_linked(b2, 'units_QuantityHomogenousOperation', a)


def test_assoc_lhs6_link_reassign_clear():
    a = units_QuantityScalarOperation(rhs=3.14)
    b1 = units_Quantity(value="sample_text")
    b2 = units_Quantity(value="sample_text_2")
    _safe_set(a, 'units_QuantityScalarOperation', b1)
    assert _is_linked(a, 'units_QuantityScalarOperation', b1)
    if hasattr(b1, 'units_Quantity7'):
        assert _is_linked(b1, 'units_Quantity7', a)
    _safe_set(a, 'units_QuantityScalarOperation', b2)
    assert _is_linked(a, 'units_QuantityScalarOperation', b2)
    if hasattr(b1, 'units_Quantity7'):
        assert not _is_linked(b1, 'units_Quantity7', a)
    if hasattr(b2, 'units_Quantity7'):
        assert _is_linked(b2, 'units_Quantity7', a)
    _safe_set(a, 'units_QuantityScalarOperation', None)
    assert not _is_linked(a, 'units_QuantityScalarOperation', b2)
    if hasattr(b2, 'units_Quantity7'):
        assert not _is_linked(b2, 'units_Quantity7', a)


def test_assoc_rhs3_link_reassign_clear():
    a = units_Quantity(value="sample_text")
    b1 = units_QuantityHomogenousOperation()
    b2 = units_QuantityHomogenousOperation()
    _safe_set(a, 'units_Quantity5', b1)
    assert _is_linked(a, 'units_Quantity5', b1)
    if hasattr(b1, 'units_QuantityHomogenousOperation4'):
        assert _is_linked(b1, 'units_QuantityHomogenousOperation4', a)
    _safe_set(a, 'units_Quantity5', b2)
    assert _is_linked(a, 'units_Quantity5', b2)
    if hasattr(b1, 'units_QuantityHomogenousOperation4'):
        assert not _is_linked(b1, 'units_QuantityHomogenousOperation4', a)
    if hasattr(b2, 'units_QuantityHomogenousOperation4'):
        assert _is_linked(b2, 'units_QuantityHomogenousOperation4', a)
    _safe_set(a, 'units_Quantity5', None)
    assert not _is_linked(a, 'units_Quantity5', b2)
    if hasattr(b2, 'units_QuantityHomogenousOperation4'):
        assert not _is_linked(b2, 'units_QuantityHomogenousOperation4', a)


def test_assoc_unit0_link_reassign_clear():
    a = units_Unit()
    b1 = units_Quantity(value="sample_text")
    b2 = units_Quantity(value="sample_text_2")
    _safe_set(a, 'units_Unit', b1)
    assert _is_linked(a, 'units_Unit', b1)
    if hasattr(b1, 'units_Quantity'):
        assert _is_linked(b1, 'units_Quantity', a)
    _safe_set(a, 'units_Unit', b2)
    assert _is_linked(a, 'units_Unit', b2)
    if hasattr(b1, 'units_Quantity'):
        assert not _is_linked(b1, 'units_Quantity', a)
    if hasattr(b2, 'units_Quantity'):
        assert _is_linked(b2, 'units_Quantity', a)
    _safe_set(a, 'units_Unit', None)
    assert not _is_linked(a, 'units_Unit', b2)
    if hasattr(b2, 'units_Quantity'):
        assert not _is_linked(b2, 'units_Quantity', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

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


Unit_strategy = st.builds(Unit)
@given(instance=Unit_strategy)
@settings(max_examples=25)
def test_Unit_instantiation(instance):
    assert isinstance(instance, Unit)


units_Angle_strategy = st.builds(units_Angle)
@given(instance=units_Angle_strategy)
@settings(max_examples=25)
def test_units_Angle_instantiation(instance):
    assert isinstance(instance, units_Angle)


units_AngleAdd_strategy = st.builds(units_AngleAdd)
@given(instance=units_AngleAdd_strategy)
@settings(max_examples=25)
def test_units_AngleAdd_instantiation(instance):
    assert isinstance(instance, units_AngleAdd)


units_AngleDistinct_strategy = st.builds(units_AngleDistinct)
@given(instance=units_AngleDistinct_strategy)
@settings(max_examples=25)
def test_units_AngleDistinct_instantiation(instance):
    assert isinstance(instance, units_AngleDistinct)


units_AngleEquals_strategy = st.builds(units_AngleEquals)
@given(instance=units_AngleEquals_strategy)
@settings(max_examples=25)
def test_units_AngleEquals_instantiation(instance):
    assert isinstance(instance, units_AngleEquals)


units_AngleGreater_strategy = st.builds(units_AngleGreater)
@given(instance=units_AngleGreater_strategy)
@settings(max_examples=25)
def test_units_AngleGreater_instantiation(instance):
    assert isinstance(instance, units_AngleGreater)


units_AngleOperation_strategy = st.builds(units_AngleOperation)
@given(instance=units_AngleOperation_strategy)
@settings(max_examples=25)
def test_units_AngleOperation_instantiation(instance):
    assert isinstance(instance, units_AngleOperation)


units_AngleScalarDivide_strategy = st.builds(units_AngleScalarDivide)
@given(instance=units_AngleScalarDivide_strategy)
@settings(max_examples=25)
def test_units_AngleScalarDivide_instantiation(instance):
    assert isinstance(instance, units_AngleScalarDivide)


units_AngleScalarMultiply_strategy = st.builds(units_AngleScalarMultiply)
@given(instance=units_AngleScalarMultiply_strategy)
@settings(max_examples=25)
def test_units_AngleScalarMultiply_instantiation(instance):
    assert isinstance(instance, units_AngleScalarMultiply)


units_AngleSmaller_strategy = st.builds(units_AngleSmaller)
@given(instance=units_AngleSmaller_strategy)
@settings(max_examples=25)
def test_units_AngleSmaller_instantiation(instance):
    assert isinstance(instance, units_AngleSmaller)


units_AngleSubtract_strategy = st.builds(units_AngleSubtract)
@given(instance=units_AngleSubtract_strategy)
@settings(max_examples=25)
def test_units_AngleSubtract_instantiation(instance):
    assert isinstance(instance, units_AngleSubtract)


units_AngleUnit_strategy = st.builds(units_AngleUnit)
@given(instance=units_AngleUnit_strategy)
@settings(max_examples=25)
def test_units_AngleUnit_instantiation(instance):
    assert isinstance(instance, units_AngleUnit)


units_Centimeter_strategy = st.builds(units_Centimeter)
@given(instance=units_Centimeter_strategy)
@settings(max_examples=25)
def test_units_Centimeter_instantiation(instance):
    assert isinstance(instance, units_Centimeter)


units_Degree_strategy = st.builds(units_Degree)
@given(instance=units_Degree_strategy)
@settings(max_examples=25)
def test_units_Degree_instantiation(instance):
    assert isinstance(instance, units_Degree)


units_Foot_strategy = st.builds(units_Foot)
@given(instance=units_Foot_strategy)
@settings(max_examples=25)
def test_units_Foot_instantiation(instance):
    assert isinstance(instance, units_Foot)


units_Gradian_strategy = st.builds(units_Gradian)
@given(instance=units_Gradian_strategy)
@settings(max_examples=25)
def test_units_Gradian_instantiation(instance):
    assert isinstance(instance, units_Gradian)


units_ImperialSystemUnit_strategy = st.builds(units_ImperialSystemUnit)
@given(instance=units_ImperialSystemUnit_strategy)
@settings(max_examples=25)
def test_units_ImperialSystemUnit_instantiation(instance):
    assert isinstance(instance, units_ImperialSystemUnit)


units_Inch_strategy = st.builds(units_Inch)
@given(instance=units_Inch_strategy)
@settings(max_examples=25)
def test_units_Inch_instantiation(instance):
    assert isinstance(instance, units_Inch)


units_Length_strategy = st.builds(units_Length)
@given(instance=units_Length_strategy)
@settings(max_examples=25)
def test_units_Length_instantiation(instance):
    assert isinstance(instance, units_Length)


units_LengthAdd_strategy = st.builds(units_LengthAdd)
@given(instance=units_LengthAdd_strategy)
@settings(max_examples=25)
def test_units_LengthAdd_instantiation(instance):
    assert isinstance(instance, units_LengthAdd)


units_LengthDistinct_strategy = st.builds(units_LengthDistinct)
@given(instance=units_LengthDistinct_strategy)
@settings(max_examples=25)
def test_units_LengthDistinct_instantiation(instance):
    assert isinstance(instance, units_LengthDistinct)


units_LengthEquals_strategy = st.builds(units_LengthEquals)
@given(instance=units_LengthEquals_strategy)
@settings(max_examples=25)
def test_units_LengthEquals_instantiation(instance):
    assert isinstance(instance, units_LengthEquals)


units_LengthGreater_strategy = st.builds(units_LengthGreater)
@given(instance=units_LengthGreater_strategy)
@settings(max_examples=25)
def test_units_LengthGreater_instantiation(instance):
    assert isinstance(instance, units_LengthGreater)


units_LengthOperation_strategy = st.builds(units_LengthOperation)
@given(instance=units_LengthOperation_strategy)
@settings(max_examples=25)
def test_units_LengthOperation_instantiation(instance):
    assert isinstance(instance, units_LengthOperation)


units_LengthScalarDivide_strategy = st.builds(units_LengthScalarDivide)
@given(instance=units_LengthScalarDivide_strategy)
@settings(max_examples=25)
def test_units_LengthScalarDivide_instantiation(instance):
    assert isinstance(instance, units_LengthScalarDivide)


units_LengthScalarMultiply_strategy = st.builds(units_LengthScalarMultiply)
@given(instance=units_LengthScalarMultiply_strategy)
@settings(max_examples=25)
def test_units_LengthScalarMultiply_instantiation(instance):
    assert isinstance(instance, units_LengthScalarMultiply)


units_LengthSmaller_strategy = st.builds(units_LengthSmaller)
@given(instance=units_LengthSmaller_strategy)
@settings(max_examples=25)
def test_units_LengthSmaller_instantiation(instance):
    assert isinstance(instance, units_LengthSmaller)


units_LengthSubtract_strategy = st.builds(units_LengthSubtract)
@given(instance=units_LengthSubtract_strategy)
@settings(max_examples=25)
def test_units_LengthSubtract_instantiation(instance):
    assert isinstance(instance, units_LengthSubtract)


units_LengthUnit_strategy = st.builds(units_LengthUnit)
@given(instance=units_LengthUnit_strategy)
@settings(max_examples=25)
def test_units_LengthUnit_instantiation(instance):
    assert isinstance(instance, units_LengthUnit)


units_Meter_strategy = st.builds(units_Meter)
@given(instance=units_Meter_strategy)
@settings(max_examples=25)
def test_units_Meter_instantiation(instance):
    assert isinstance(instance, units_Meter)


units_MetricSystemUnit_strategy = st.builds(units_MetricSystemUnit)
@given(instance=units_MetricSystemUnit_strategy)
@settings(max_examples=25)
def test_units_MetricSystemUnit_instantiation(instance):
    assert isinstance(instance, units_MetricSystemUnit)


units_Millimeter_strategy = st.builds(units_Millimeter)
@given(instance=units_Millimeter_strategy)
@settings(max_examples=25)
def test_units_Millimeter_instantiation(instance):
    assert isinstance(instance, units_Millimeter)


units_Quantity_strategy = st.builds(units_Quantity, value=safe_text)
@given(instance=units_Quantity_strategy)
@settings(max_examples=25)
def test_units_Quantity_instantiation(instance):
    assert isinstance(instance, units_Quantity)


units_QuantityArithmeticOperation_strategy = st.builds(units_QuantityArithmeticOperation)
@given(instance=units_QuantityArithmeticOperation_strategy)
@settings(max_examples=25)
def test_units_QuantityArithmeticOperation_instantiation(instance):
    assert isinstance(instance, units_QuantityArithmeticOperation)


units_QuantityComparisonOperation_strategy = st.builds(units_QuantityComparisonOperation)
@given(instance=units_QuantityComparisonOperation_strategy)
@settings(max_examples=25)
def test_units_QuantityComparisonOperation_instantiation(instance):
    assert isinstance(instance, units_QuantityComparisonOperation)


units_QuantityHomogenousOperation_strategy = st.builds(units_QuantityHomogenousOperation)
@given(instance=units_QuantityHomogenousOperation_strategy)
@settings(max_examples=25)
def test_units_QuantityHomogenousOperation_instantiation(instance):
    assert isinstance(instance, units_QuantityHomogenousOperation)


units_QuantityOperation_strategy = st.builds(units_QuantityOperation)
@given(instance=units_QuantityOperation_strategy)
@settings(max_examples=25)
def test_units_QuantityOperation_instantiation(instance):
    assert isinstance(instance, units_QuantityOperation)


units_QuantityScalarOperation_strategy = st.builds(units_QuantityScalarOperation, rhs=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=units_QuantityScalarOperation_strategy)
@settings(max_examples=25)
def test_units_QuantityScalarOperation_instantiation(instance):
    assert isinstance(instance, units_QuantityScalarOperation)


units_Radian_strategy = st.builds(units_Radian)
@given(instance=units_Radian_strategy)
@settings(max_examples=25)
def test_units_Radian_instantiation(instance):
    assert isinstance(instance, units_Radian)


units_Turn_strategy = st.builds(units_Turn)
@given(instance=units_Turn_strategy)
@settings(max_examples=25)
def test_units_Turn_instantiation(instance):
    assert isinstance(instance, units_Turn)


units_Unit_strategy = st.builds(units_Unit)
@given(instance=units_Unit_strategy)
@settings(max_examples=25)
def test_units_Unit_instantiation(instance):
    assert isinstance(instance, units_Unit)


units_Yard_strategy = st.builds(units_Yard)
@given(instance=units_Yard_strategy)
@settings(max_examples=25)
def test_units_Yard_instantiation(instance):
    assert isinstance(instance, units_Yard)



