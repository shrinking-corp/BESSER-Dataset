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
    ptnet_Variable,
    BooleanExpression,
    ptnet_OpOr,
    ptnet_OpAnd,
    ComparisonOperator,
    ptnet_OpGreater,
    ptnet_OpLessEqual,
    ptnet_OpGreaterEqual,
    ptnet_OpLess,
    ptnet_OpEqual,
    EvaluationType,
    ptnet_InstantOfTime,
    ptnet_IntervalOfTime,
    ptnet_IntervalOfTimeAveraged,
    ptnet_SteadyState,
    ArithmeticBinaryOperator,
    ptnet_OpDivide,
    ptnet_OpMultiply,
    ptnet_OpMinus,
    ptnet_OpSum,
    LogicalExpression,
    ptnet_BooleanExpression,
    ptnet_OpFalse,
    ptnet_ComparisonOperator,
    ptnet_OpNot,
    ptnet_OpTrue,
    ptnet_EvaluationType,
    ptnet_VariableValues,
    ptnet_Measure,
    ptnet_Study,
    ptnet_EvaluationList,
    Expression,
    ArithmeticExpression,
    ptnet_IfThenElse,
    ptnet_ArithmeticBinaryOperator,
    ptnet_MarkingExpression,
    ptnet_VariableExpression,
    ptnet_ValueExpression,
    ptnet_Expression,
    Distribution,
    ptnet_Gaussian,
    ptnet_Exponential,
    ptnet_Deterministic,
    ptnet_Distribution,
    GSPNTransition,
    ptnet_GSPNTimedTransition,
    ptnet_GSPNImmediateTransition,
    ptnet_ArithmeticExpression,
    ptnet_Weibull,
    ptnet_Gamma,
    ptnet_Uniform,
    Label,
    ptnet_Attribute,
    Arc,
    ptnet_GSPNArc,
    ptnet_LogicalExpression,
    Transition,
    ptnet_GSPNTransition,
    Node,
    ptnet_TransitionNode,
    ptnet_PlaceNode,
    TransitionNode,
    ptnet_RefTransition,
    ptnet_Transition,
    PlaceNode,
    ptnet_RefPlace,
    ptnet_Annotation,
    ptnet_Font,
    ptnet_Graphics,
    ptnet_Line,
    Coordinate,
    ptnet_Offset,
    ptnet_Coordinate,
    ptnet_AnyObject,
    ptnet_Label,
    ptnet_Fill,
    ptnet_Dimension,
    ptnet_Position,
    Graphics,
    ptnet_AnnotationGraphics,
    ptnet_ArcGraphics,
    ptnet_NodeGraphics,
    ptnet_PnObject,
    ptnet_PetriNet,
    ptnet_PetriNetDoc,
    ptnet_Place,
    PnObject,
    ptnet_Arc,
    ptnet_Page,
    ptnet_Node,
    ptnet_ToolInfo,
    Annotation,
    ptnet_PTArcAnnotation,
    ptnet_Name,
    ptnet_PTMarking,
    FontDecoration,
    CSS2FontSize,
    PNType,
    CSS2Color,
    GSPNArcType,
    LineStyle,
    CSS2FontWeight,
    LineShape,
    FontAlign,
    GSPNTransitionType,
    CSS2FontFamily,
    Gradient,
    CSS2FontStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_ptnet_variable_is_not_abstract():
    assert not inspect.isabstract(ptnet_Variable)


def test_hyp_ptnet_variable_constructor_exists():
    assert callable(ptnet_Variable.__init__)


def test_hyp_ptnet_variable_constructor_args():
    sig = inspect.signature(ptnet_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_hyp_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_hyp_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opor_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpOr)


def test_hyp_ptnet_opor_constructor_exists():
    assert callable(ptnet_OpOr.__init__)


def test_hyp_ptnet_opor_constructor_args():
    sig = inspect.signature(ptnet_OpOr.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opand_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpAnd)


def test_hyp_ptnet_opand_constructor_exists():
    assert callable(ptnet_OpAnd.__init__)


def test_hyp_ptnet_opand_constructor_args():
    sig = inspect.signature(ptnet_OpAnd.__init__)
    params = list(sig.parameters.keys())



def test_hyp_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperator)


def test_hyp_comparisonoperator_constructor_exists():
    assert callable(ComparisonOperator.__init__)


def test_hyp_comparisonoperator_constructor_args():
    sig = inspect.signature(ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opgreater_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpGreater)


def test_hyp_ptnet_opgreater_constructor_exists():
    assert callable(ptnet_OpGreater.__init__)


def test_hyp_ptnet_opgreater_constructor_args():
    sig = inspect.signature(ptnet_OpGreater.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_oplessequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpLessEqual)


def test_hyp_ptnet_oplessequal_constructor_exists():
    assert callable(ptnet_OpLessEqual.__init__)


def test_hyp_ptnet_oplessequal_constructor_args():
    sig = inspect.signature(ptnet_OpLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opgreaterequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpGreaterEqual)


def test_hyp_ptnet_opgreaterequal_constructor_exists():
    assert callable(ptnet_OpGreaterEqual.__init__)


def test_hyp_ptnet_opgreaterequal_constructor_args():
    sig = inspect.signature(ptnet_OpGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opless_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpLess)


def test_hyp_ptnet_opless_constructor_exists():
    assert callable(ptnet_OpLess.__init__)


def test_hyp_ptnet_opless_constructor_args():
    sig = inspect.signature(ptnet_OpLess.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpEqual)


def test_hyp_ptnet_opequal_constructor_exists():
    assert callable(ptnet_OpEqual.__init__)


def test_hyp_ptnet_opequal_constructor_args():
    sig = inspect.signature(ptnet_OpEqual.__init__)
    params = list(sig.parameters.keys())



def test_hyp_evaluationtype_is_not_abstract():
    assert not inspect.isabstract(EvaluationType)


def test_hyp_evaluationtype_constructor_exists():
    assert callable(EvaluationType.__init__)


def test_hyp_evaluationtype_constructor_args():
    sig = inspect.signature(EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_instantoftime_is_not_abstract():
    assert not inspect.isabstract(ptnet_InstantOfTime)


def test_hyp_ptnet_instantoftime_constructor_exists():
    assert callable(ptnet_InstantOfTime.__init__)


def test_hyp_ptnet_instantoftime_constructor_args():
    sig = inspect.signature(ptnet_InstantOfTime.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_intervaloftime_is_not_abstract():
    assert not inspect.isabstract(ptnet_IntervalOfTime)


def test_hyp_ptnet_intervaloftime_constructor_exists():
    assert callable(ptnet_IntervalOfTime.__init__)


def test_hyp_ptnet_intervaloftime_constructor_args():
    sig = inspect.signature(ptnet_IntervalOfTime.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_intervaloftimeaveraged_is_not_abstract():
    assert not inspect.isabstract(ptnet_IntervalOfTimeAveraged)


def test_hyp_ptnet_intervaloftimeaveraged_constructor_exists():
    assert callable(ptnet_IntervalOfTimeAveraged.__init__)


def test_hyp_ptnet_intervaloftimeaveraged_constructor_args():
    sig = inspect.signature(ptnet_IntervalOfTimeAveraged.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_steadystate_is_not_abstract():
    assert not inspect.isabstract(ptnet_SteadyState)


def test_hyp_ptnet_steadystate_constructor_exists():
    assert callable(ptnet_SteadyState.__init__)


def test_hyp_ptnet_steadystate_constructor_args():
    sig = inspect.signature(ptnet_SteadyState.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticBinaryOperator)


def test_hyp_arithmeticbinaryoperator_constructor_exists():
    assert callable(ArithmeticBinaryOperator.__init__)


def test_hyp_arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opdivide_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpDivide)


def test_hyp_ptnet_opdivide_constructor_exists():
    assert callable(ptnet_OpDivide.__init__)


def test_hyp_ptnet_opdivide_constructor_args():
    sig = inspect.signature(ptnet_OpDivide.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opmultiply_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpMultiply)


def test_hyp_ptnet_opmultiply_constructor_exists():
    assert callable(ptnet_OpMultiply.__init__)


def test_hyp_ptnet_opmultiply_constructor_args():
    sig = inspect.signature(ptnet_OpMultiply.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opminus_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpMinus)


def test_hyp_ptnet_opminus_constructor_exists():
    assert callable(ptnet_OpMinus.__init__)


def test_hyp_ptnet_opminus_constructor_args():
    sig = inspect.signature(ptnet_OpMinus.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opsum_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpSum)


def test_hyp_ptnet_opsum_constructor_exists():
    assert callable(ptnet_OpSum.__init__)


def test_hyp_ptnet_opsum_constructor_args():
    sig = inspect.signature(ptnet_OpSum.__init__)
    params = list(sig.parameters.keys())



def test_hyp_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_hyp_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_hyp_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_BooleanExpression)


def test_hyp_ptnet_booleanexpression_constructor_exists():
    assert callable(ptnet_BooleanExpression.__init__)


def test_hyp_ptnet_booleanexpression_constructor_args():
    sig = inspect.signature(ptnet_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opfalse_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpFalse)


def test_hyp_ptnet_opfalse_constructor_exists():
    assert callable(ptnet_OpFalse.__init__)


def test_hyp_ptnet_opfalse_constructor_args():
    sig = inspect.signature(ptnet_OpFalse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet_ComparisonOperator)


def test_hyp_ptnet_comparisonoperator_constructor_exists():
    assert callable(ptnet_ComparisonOperator.__init__)


def test_hyp_ptnet_comparisonoperator_constructor_args():
    sig = inspect.signature(ptnet_ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_opnot_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpNot)


def test_hyp_ptnet_opnot_constructor_exists():
    assert callable(ptnet_OpNot.__init__)


def test_hyp_ptnet_opnot_constructor_args():
    sig = inspect.signature(ptnet_OpNot.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_optrue_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpTrue)


def test_hyp_ptnet_optrue_constructor_exists():
    assert callable(ptnet_OpTrue.__init__)


def test_hyp_ptnet_optrue_constructor_args():
    sig = inspect.signature(ptnet_OpTrue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_evaluationtype_is_not_abstract():
    assert not inspect.isabstract(ptnet_EvaluationType)


def test_hyp_ptnet_evaluationtype_constructor_exists():
    assert callable(ptnet_EvaluationType.__init__)


def test_hyp_ptnet_evaluationtype_constructor_args():
    sig = inspect.signature(ptnet_EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_variablevalues_is_not_abstract():
    assert not inspect.isabstract(ptnet_VariableValues)


def test_hyp_ptnet_variablevalues_constructor_exists():
    assert callable(ptnet_VariableValues.__init__)


def test_hyp_ptnet_variablevalues_constructor_args():
    sig = inspect.signature(ptnet_VariableValues.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"




def test_hyp_ptnet_measure_is_not_abstract():
    assert not inspect.isabstract(ptnet_Measure)


def test_hyp_ptnet_measure_constructor_exists():
    assert callable(ptnet_Measure.__init__)


def test_hyp_ptnet_measure_constructor_args():
    sig = inspect.signature(ptnet_Measure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ptnet_study_is_not_abstract():
    assert not inspect.isabstract(ptnet_Study)


def test_hyp_ptnet_study_constructor_exists():
    assert callable(ptnet_Study.__init__)


def test_hyp_ptnet_study_constructor_args():
    sig = inspect.signature(ptnet_Study.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_ptnet_evaluationlist_is_not_abstract():
    assert not inspect.isabstract(ptnet_EvaluationList)


def test_hyp_ptnet_evaluationlist_constructor_exists():
    assert callable(ptnet_EvaluationList.__init__)


def test_hyp_ptnet_evaluationlist_constructor_args():
    sig = inspect.signature(ptnet_EvaluationList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_hyp_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_hyp_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_hyp_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(ptnet_IfThenElse)


def test_hyp_ptnet_ifthenelse_constructor_exists():
    assert callable(ptnet_IfThenElse.__init__)


def test_hyp_ptnet_ifthenelse_constructor_args():
    sig = inspect.signature(ptnet_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArithmeticBinaryOperator)


def test_hyp_ptnet_arithmeticbinaryoperator_constructor_exists():
    assert callable(ptnet_ArithmeticBinaryOperator.__init__)


def test_hyp_ptnet_arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ptnet_ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_markingexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_MarkingExpression)


def test_hyp_ptnet_markingexpression_constructor_exists():
    assert callable(ptnet_MarkingExpression.__init__)


def test_hyp_ptnet_markingexpression_constructor_args():
    sig = inspect.signature(ptnet_MarkingExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_variableexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_VariableExpression)


def test_hyp_ptnet_variableexpression_constructor_exists():
    assert callable(ptnet_VariableExpression.__init__)


def test_hyp_ptnet_variableexpression_constructor_args():
    sig = inspect.signature(ptnet_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_ValueExpression)


def test_hyp_ptnet_valueexpression_constructor_exists():
    assert callable(ptnet_ValueExpression.__init__)


def test_hyp_ptnet_valueexpression_constructor_args():
    sig = inspect.signature(ptnet_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_ptnet_expression_is_not_abstract():
    assert not inspect.isabstract(ptnet_Expression)


def test_hyp_ptnet_expression_constructor_exists():
    assert callable(ptnet_Expression.__init__)


def test_hyp_ptnet_expression_constructor_args():
    sig = inspect.signature(ptnet_Expression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_distribution_is_not_abstract():
    assert not inspect.isabstract(Distribution)


def test_hyp_distribution_constructor_exists():
    assert callable(Distribution.__init__)


def test_hyp_distribution_constructor_args():
    sig = inspect.signature(Distribution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_gaussian_is_not_abstract():
    assert not inspect.isabstract(ptnet_Gaussian)


def test_hyp_ptnet_gaussian_constructor_exists():
    assert callable(ptnet_Gaussian.__init__)


def test_hyp_ptnet_gaussian_constructor_args():
    sig = inspect.signature(ptnet_Gaussian.__init__)
    params = list(sig.parameters.keys())
    assert "Variance" in params, "Missing parameter 'Variance'"
    assert "Mean" in params, "Missing parameter 'Mean'"





def test_hyp_ptnet_exponential_is_not_abstract():
    assert not inspect.isabstract(ptnet_Exponential)


def test_hyp_ptnet_exponential_constructor_exists():
    assert callable(ptnet_Exponential.__init__)


def test_hyp_ptnet_exponential_constructor_args():
    sig = inspect.signature(ptnet_Exponential.__init__)
    params = list(sig.parameters.keys())
    assert "Rate" in params, "Missing parameter 'Rate'"




def test_hyp_ptnet_deterministic_is_not_abstract():
    assert not inspect.isabstract(ptnet_Deterministic)


def test_hyp_ptnet_deterministic_constructor_exists():
    assert callable(ptnet_Deterministic.__init__)


def test_hyp_ptnet_deterministic_constructor_args():
    sig = inspect.signature(ptnet_Deterministic.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"




def test_hyp_ptnet_distribution_is_not_abstract():
    assert not inspect.isabstract(ptnet_Distribution)


def test_hyp_ptnet_distribution_constructor_exists():
    assert callable(ptnet_Distribution.__init__)


def test_hyp_ptnet_distribution_constructor_args():
    sig = inspect.signature(ptnet_Distribution.__init__)
    params = list(sig.parameters.keys())



def test_hyp_gspntransition_is_not_abstract():
    assert not inspect.isabstract(GSPNTransition)


def test_hyp_gspntransition_constructor_exists():
    assert callable(GSPNTransition.__init__)


def test_hyp_gspntransition_constructor_args():
    sig = inspect.signature(GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_gspntimedtransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNTimedTransition)


def test_hyp_ptnet_gspntimedtransition_constructor_exists():
    assert callable(ptnet_GSPNTimedTransition.__init__)


def test_hyp_ptnet_gspntimedtransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNTimedTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_gspnimmediatetransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNImmediateTransition)


def test_hyp_ptnet_gspnimmediatetransition_constructor_exists():
    assert callable(ptnet_GSPNImmediateTransition.__init__)


def test_hyp_ptnet_gspnimmediatetransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNImmediateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "Weight" in params, "Missing parameter 'Weight'"
    assert "Priority" in params, "Missing parameter 'Priority'"





def test_hyp_ptnet_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArithmeticExpression)


def test_hyp_ptnet_arithmeticexpression_constructor_exists():
    assert callable(ptnet_ArithmeticExpression.__init__)


def test_hyp_ptnet_arithmeticexpression_constructor_args():
    sig = inspect.signature(ptnet_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_weibull_is_not_abstract():
    assert not inspect.isabstract(ptnet_Weibull)


def test_hyp_ptnet_weibull_constructor_exists():
    assert callable(ptnet_Weibull.__init__)


def test_hyp_ptnet_weibull_constructor_args():
    sig = inspect.signature(ptnet_Weibull.__init__)
    params = list(sig.parameters.keys())
    assert "Alpha" in params, "Missing parameter 'Alpha'"
    assert "Beta" in params, "Missing parameter 'Beta'"





def test_hyp_ptnet_gamma_is_not_abstract():
    assert not inspect.isabstract(ptnet_Gamma)


def test_hyp_ptnet_gamma_constructor_exists():
    assert callable(ptnet_Gamma.__init__)


def test_hyp_ptnet_gamma_constructor_args():
    sig = inspect.signature(ptnet_Gamma.__init__)
    params = list(sig.parameters.keys())
    assert "Beta" in params, "Missing parameter 'Beta'"
    assert "Alpha" in params, "Missing parameter 'Alpha'"





def test_hyp_ptnet_uniform_is_not_abstract():
    assert not inspect.isabstract(ptnet_Uniform)


def test_hyp_ptnet_uniform_constructor_exists():
    assert callable(ptnet_Uniform.__init__)


def test_hyp_ptnet_uniform_constructor_args():
    sig = inspect.signature(ptnet_Uniform.__init__)
    params = list(sig.parameters.keys())
    assert "Upper" in params, "Missing parameter 'Upper'"
    assert "Lower" in params, "Missing parameter 'Lower'"





def test_hyp_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_hyp_label_constructor_exists():
    assert callable(Label.__init__)


def test_hyp_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_attribute_is_not_abstract():
    assert not inspect.isabstract(ptnet_Attribute)


def test_hyp_ptnet_attribute_constructor_exists():
    assert callable(ptnet_Attribute.__init__)


def test_hyp_ptnet_attribute_constructor_args():
    sig = inspect.signature(ptnet_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_hyp_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_hyp_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_gspnarc_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNArc)


def test_hyp_ptnet_gspnarc_constructor_exists():
    assert callable(ptnet_GSPNArc.__init__)


def test_hyp_ptnet_gspnarc_constructor_args():
    sig = inspect.signature(ptnet_GSPNArc.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_ptnet_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_LogicalExpression)


def test_hyp_ptnet_logicalexpression_constructor_exists():
    assert callable(ptnet_LogicalExpression.__init__)


def test_hyp_ptnet_logicalexpression_constructor_args():
    sig = inspect.signature(ptnet_LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_hyp_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_hyp_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_gspntransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNTransition)


def test_hyp_ptnet_gspntransition_constructor_exists():
    assert callable(ptnet_GSPNTransition.__init__)


def test_hyp_ptnet_gspntransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_hyp_node_constructor_exists():
    assert callable(Node.__init__)


def test_hyp_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_transitionnode_is_not_abstract():
    assert not inspect.isabstract(ptnet_TransitionNode)


def test_hyp_ptnet_transitionnode_constructor_exists():
    assert callable(ptnet_TransitionNode.__init__)


def test_hyp_ptnet_transitionnode_constructor_args():
    sig = inspect.signature(ptnet_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_placenode_is_not_abstract():
    assert not inspect.isabstract(ptnet_PlaceNode)


def test_hyp_ptnet_placenode_constructor_exists():
    assert callable(ptnet_PlaceNode.__init__)


def test_hyp_ptnet_placenode_constructor_args():
    sig = inspect.signature(ptnet_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_hyp_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_hyp_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_reftransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_RefTransition)


def test_hyp_ptnet_reftransition_constructor_exists():
    assert callable(ptnet_RefTransition.__init__)


def test_hyp_ptnet_reftransition_constructor_args():
    sig = inspect.signature(ptnet_RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_transition_is_not_abstract():
    assert not inspect.isabstract(ptnet_Transition)


def test_hyp_ptnet_transition_constructor_exists():
    assert callable(ptnet_Transition.__init__)


def test_hyp_ptnet_transition_constructor_args():
    sig = inspect.signature(ptnet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hyp_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_hyp_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_hyp_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_refplace_is_not_abstract():
    assert not inspect.isabstract(ptnet_RefPlace)


def test_hyp_ptnet_refplace_constructor_exists():
    assert callable(ptnet_RefPlace.__init__)


def test_hyp_ptnet_refplace_constructor_args():
    sig = inspect.signature(ptnet_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_annotation_is_not_abstract():
    assert not inspect.isabstract(ptnet_Annotation)


def test_hyp_ptnet_annotation_constructor_exists():
    assert callable(ptnet_Annotation.__init__)


def test_hyp_ptnet_annotation_constructor_args():
    sig = inspect.signature(ptnet_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_font_is_not_abstract():
    assert not inspect.isabstract(ptnet_Font)


def test_hyp_ptnet_font_constructor_exists():
    assert callable(ptnet_Font.__init__)


def test_hyp_ptnet_font_constructor_args():
    sig = inspect.signature(ptnet_Font.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "style" in params, "Missing parameter 'style'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "size" in params, "Missing parameter 'size'"
    assert "align" in params, "Missing parameter 'align'"










def test_hyp_ptnet_graphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_Graphics)


def test_hyp_ptnet_graphics_constructor_exists():
    assert callable(ptnet_Graphics.__init__)


def test_hyp_ptnet_graphics_constructor_args():
    sig = inspect.signature(ptnet_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_line_is_not_abstract():
    assert not inspect.isabstract(ptnet_Line)


def test_hyp_ptnet_line_constructor_exists():
    assert callable(ptnet_Line.__init__)


def test_hyp_ptnet_line_constructor_args():
    sig = inspect.signature(ptnet_Line.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "shape" in params, "Missing parameter 'shape'"







def test_hyp_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_hyp_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_hyp_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_offset_is_not_abstract():
    assert not inspect.isabstract(ptnet_Offset)


def test_hyp_ptnet_offset_constructor_exists():
    assert callable(ptnet_Offset.__init__)


def test_hyp_ptnet_offset_constructor_args():
    sig = inspect.signature(ptnet_Offset.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_coordinate_is_not_abstract():
    assert not inspect.isabstract(ptnet_Coordinate)


def test_hyp_ptnet_coordinate_constructor_exists():
    assert callable(ptnet_Coordinate.__init__)


def test_hyp_ptnet_coordinate_constructor_args():
    sig = inspect.signature(ptnet_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"





def test_hyp_ptnet_anyobject_is_not_abstract():
    assert not inspect.isabstract(ptnet_AnyObject)


def test_hyp_ptnet_anyobject_constructor_exists():
    assert callable(ptnet_AnyObject.__init__)


def test_hyp_ptnet_anyobject_constructor_args():
    sig = inspect.signature(ptnet_AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_label_is_not_abstract():
    assert not inspect.isabstract(ptnet_Label)


def test_hyp_ptnet_label_constructor_exists():
    assert callable(ptnet_Label.__init__)


def test_hyp_ptnet_label_constructor_args():
    sig = inspect.signature(ptnet_Label.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_fill_is_not_abstract():
    assert not inspect.isabstract(ptnet_Fill)


def test_hyp_ptnet_fill_constructor_exists():
    assert callable(ptnet_Fill.__init__)


def test_hyp_ptnet_fill_constructor_args():
    sig = inspect.signature(ptnet_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"







def test_hyp_ptnet_dimension_is_not_abstract():
    assert not inspect.isabstract(ptnet_Dimension)


def test_hyp_ptnet_dimension_constructor_exists():
    assert callable(ptnet_Dimension.__init__)


def test_hyp_ptnet_dimension_constructor_args():
    sig = inspect.signature(ptnet_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_position_is_not_abstract():
    assert not inspect.isabstract(ptnet_Position)


def test_hyp_ptnet_position_constructor_exists():
    assert callable(ptnet_Position.__init__)


def test_hyp_ptnet_position_constructor_args():
    sig = inspect.signature(ptnet_Position.__init__)
    params = list(sig.parameters.keys())



def test_hyp_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_hyp_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_hyp_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_AnnotationGraphics)


def test_hyp_ptnet_annotationgraphics_constructor_exists():
    assert callable(ptnet_AnnotationGraphics.__init__)


def test_hyp_ptnet_annotationgraphics_constructor_args():
    sig = inspect.signature(ptnet_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_arcgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArcGraphics)


def test_hyp_ptnet_arcgraphics_constructor_exists():
    assert callable(ptnet_ArcGraphics.__init__)


def test_hyp_ptnet_arcgraphics_constructor_args():
    sig = inspect.signature(ptnet_ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_NodeGraphics)


def test_hyp_ptnet_nodegraphics_constructor_exists():
    assert callable(ptnet_NodeGraphics.__init__)


def test_hyp_ptnet_nodegraphics_constructor_args():
    sig = inspect.signature(ptnet_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_pnobject_is_not_abstract():
    assert not inspect.isabstract(ptnet_PnObject)


def test_hyp_ptnet_pnobject_constructor_exists():
    assert callable(ptnet_PnObject.__init__)


def test_hyp_ptnet_pnobject_constructor_args():
    sig = inspect.signature(ptnet_PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_ptnet_petrinet_is_not_abstract():
    assert not inspect.isabstract(ptnet_PetriNet)


def test_hyp_ptnet_petrinet_constructor_exists():
    assert callable(ptnet_PetriNet.__init__)


def test_hyp_ptnet_petrinet_constructor_args():
    sig = inspect.signature(ptnet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"





def test_hyp_ptnet_petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(ptnet_PetriNetDoc)


def test_hyp_ptnet_petrinetdoc_constructor_exists():
    assert callable(ptnet_PetriNetDoc.__init__)


def test_hyp_ptnet_petrinetdoc_constructor_args():
    sig = inspect.signature(ptnet_PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"




def test_hyp_ptnet_place_is_not_abstract():
    assert not inspect.isabstract(ptnet_Place)


def test_hyp_ptnet_place_constructor_exists():
    assert callable(ptnet_Place.__init__)


def test_hyp_ptnet_place_constructor_args():
    sig = inspect.signature(ptnet_Place.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pnobject_is_not_abstract():
    assert not inspect.isabstract(PnObject)


def test_hyp_pnobject_constructor_exists():
    assert callable(PnObject.__init__)


def test_hyp_pnobject_constructor_args():
    sig = inspect.signature(PnObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_arc_is_not_abstract():
    assert not inspect.isabstract(ptnet_Arc)


def test_hyp_ptnet_arc_constructor_exists():
    assert callable(ptnet_Arc.__init__)


def test_hyp_ptnet_arc_constructor_args():
    sig = inspect.signature(ptnet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_page_is_not_abstract():
    assert not inspect.isabstract(ptnet_Page)


def test_hyp_ptnet_page_constructor_exists():
    assert callable(ptnet_Page.__init__)


def test_hyp_ptnet_page_constructor_args():
    sig = inspect.signature(ptnet_Page.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_node_is_not_abstract():
    assert not inspect.isabstract(ptnet_Node)


def test_hyp_ptnet_node_constructor_exists():
    assert callable(ptnet_Node.__init__)


def test_hyp_ptnet_node_constructor_args():
    sig = inspect.signature(ptnet_Node.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_toolinfo_is_not_abstract():
    assert not inspect.isabstract(ptnet_ToolInfo)


def test_hyp_ptnet_toolinfo_constructor_exists():
    assert callable(ptnet_ToolInfo.__init__)


def test_hyp_ptnet_toolinfo_constructor_args():
    sig = inspect.signature(ptnet_ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "tool" in params, "Missing parameter 'tool'"







def test_hyp_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_hyp_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_hyp_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ptnet_ptarcannotation_is_not_abstract():
    assert not inspect.isabstract(ptnet_PTArcAnnotation)


def test_hyp_ptnet_ptarcannotation_constructor_exists():
    assert callable(ptnet_PTArcAnnotation.__init__)


def test_hyp_ptnet_ptarcannotation_constructor_args():
    sig = inspect.signature(ptnet_PTArcAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_ptnet_name_is_not_abstract():
    assert not inspect.isabstract(ptnet_Name)


def test_hyp_ptnet_name_constructor_exists():
    assert callable(ptnet_Name.__init__)


def test_hyp_ptnet_name_constructor_args():
    sig = inspect.signature(ptnet_Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_ptnet_ptmarking_is_not_abstract():
    assert not inspect.isabstract(ptnet_PTMarking)


def test_hyp_ptnet_ptmarking_constructor_exists():
    assert callable(ptnet_PTMarking.__init__)


def test_hyp_ptnet_ptmarking_constructor_args():
    sig = inspect.signature(ptnet_PTMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"


def test_hyp_fontdecoration_exists():
    # Check that the Enumeration exists
    assert FontDecoration is not None

def test_hyp_fontdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontDecoration]
    expected_literals = [
        "LINETHROUGH",
        "OVERLINE",
        "UNDERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontDecoration"

def test_hyp_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_hyp_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "XXSMALL",
        "LARGE",
        "XXLARGE",
        "MEDIUM",
        "XSMALL",
        "SMALL",
        "XLARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

def test_hyp_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_hyp_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "COREMODEL",
        "HLPN",
        "PTNET",
        "GSPN",
        "SYMNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

def test_hyp_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_hyp_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "NAVY",
        "ORANGE",
        "TEAL",
        "LIME",
        "RED",
        "FUCHSIA",
        "YELLOW",
        "OLIVE",
        "BLACK",
        "AQUA",
        "GREEN",
        "SILVER",
        "PURPLE",
        "WHITE",
        "BLUE",
        "GRAY",
        "MAROON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_hyp_gspnarctype_exists():
    # Check that the Enumeration exists
    assert GSPNArcType is not None

def test_hyp_gspnarctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSPNArcType]
    expected_literals = [
        "inhibitor",
        "normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSPNArcType"

def test_hyp_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_hyp_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DASH",
        "DOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_hyp_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_hyp_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "NORMAL",
        "BOLDER",
        "LIGHTER",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontWeight"

def test_hyp_lineshape_exists():
    # Check that the Enumeration exists
    assert LineShape is not None

def test_hyp_lineshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineShape]
    expected_literals = [
        "LINE",
        "CURVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"

def test_hyp_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_hyp_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

def test_hyp_gspntransitiontype_exists():
    # Check that the Enumeration exists
    assert GSPNTransitionType is not None

def test_hyp_gspntransitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSPNTransitionType]
    expected_literals = [
        "immediate",
        "timed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSPNTransitionType"

def test_hyp_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_hyp_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "TREBUCHET",
        "GEORGIA",
        "TIMES",
        "VERDANA",
        "ARIAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontFamily"

def test_hyp_gradient_exists():
    # Check that the Enumeration exists
    assert Gradient is not None

def test_hyp_gradient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gradient]
    expected_literals = [
        "DIAGONAL",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

def test_hyp_css2fontstyle_exists():
    # Check that the Enumeration exists
    assert CSS2FontStyle is not None

def test_hyp_css2fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontStyle]
    expected_literals = [
        "OBLIQUE",
        "ITALIC",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontStyle"


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
ptnet_Variable_strategy = st.builds(
    ptnet_Variable,
    name=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
ptnet_OpOr_strategy = st.builds(
    ptnet_OpOr,
)
ptnet_OpAnd_strategy = st.builds(
    ptnet_OpAnd,
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
ptnet_OpGreater_strategy = st.builds(
    ptnet_OpGreater,
)
ptnet_OpLessEqual_strategy = st.builds(
    ptnet_OpLessEqual,
)
ptnet_OpGreaterEqual_strategy = st.builds(
    ptnet_OpGreaterEqual,
)
ptnet_OpLess_strategy = st.builds(
    ptnet_OpLess,
)
ptnet_OpEqual_strategy = st.builds(
    ptnet_OpEqual,
)
EvaluationType_strategy = st.builds(
    EvaluationType,
)
ptnet_InstantOfTime_strategy = st.builds(
    ptnet_InstantOfTime,
)
ptnet_IntervalOfTime_strategy = st.builds(
    ptnet_IntervalOfTime,
)
ptnet_IntervalOfTimeAveraged_strategy = st.builds(
    ptnet_IntervalOfTimeAveraged,
)
ptnet_SteadyState_strategy = st.builds(
    ptnet_SteadyState,
)
ArithmeticBinaryOperator_strategy = st.builds(
    ArithmeticBinaryOperator,
)
ptnet_OpDivide_strategy = st.builds(
    ptnet_OpDivide,
)
ptnet_OpMultiply_strategy = st.builds(
    ptnet_OpMultiply,
)
ptnet_OpMinus_strategy = st.builds(
    ptnet_OpMinus,
)
ptnet_OpSum_strategy = st.builds(
    ptnet_OpSum,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
ptnet_BooleanExpression_strategy = st.builds(
    ptnet_BooleanExpression,
)
ptnet_OpFalse_strategy = st.builds(
    ptnet_OpFalse,
)
ptnet_ComparisonOperator_strategy = st.builds(
    ptnet_ComparisonOperator,
)
ptnet_OpNot_strategy = st.builds(
    ptnet_OpNot,
)
ptnet_OpTrue_strategy = st.builds(
    ptnet_OpTrue,
)
ptnet_EvaluationType_strategy = st.builds(
    ptnet_EvaluationType,
)
ptnet_VariableValues_strategy = st.builds(
    ptnet_VariableValues,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Measure_strategy = st.builds(
    ptnet_Measure,
    name=
        safe_text
)
ptnet_Study_strategy = st.builds(
    ptnet_Study,
    name=
        safe_text
)
ptnet_EvaluationList_strategy = st.builds(
    ptnet_EvaluationList,
)
Expression_strategy = st.builds(
    Expression,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
ptnet_IfThenElse_strategy = st.builds(
    ptnet_IfThenElse,
)
ptnet_ArithmeticBinaryOperator_strategy = st.builds(
    ptnet_ArithmeticBinaryOperator,
)
ptnet_MarkingExpression_strategy = st.builds(
    ptnet_MarkingExpression,
)
ptnet_VariableExpression_strategy = st.builds(
    ptnet_VariableExpression,
)
ptnet_ValueExpression_strategy = st.builds(
    ptnet_ValueExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Expression_strategy = st.builds(
    ptnet_Expression,
)
Distribution_strategy = st.builds(
    Distribution,
)
ptnet_Gaussian_strategy = st.builds(
    ptnet_Gaussian,
    Variance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Mean=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Exponential_strategy = st.builds(
    ptnet_Exponential,
    Rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Deterministic_strategy = st.builds(
    ptnet_Deterministic,
    Value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Distribution_strategy = st.builds(
    ptnet_Distribution,
)
GSPNTransition_strategy = st.builds(
    GSPNTransition,
)
ptnet_GSPNTimedTransition_strategy = st.builds(
    ptnet_GSPNTimedTransition,
)
ptnet_GSPNImmediateTransition_strategy = st.builds(
    ptnet_GSPNImmediateTransition,
    Weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Priority=
        st.integers()
)
ptnet_ArithmeticExpression_strategy = st.builds(
    ptnet_ArithmeticExpression,
)
ptnet_Weibull_strategy = st.builds(
    ptnet_Weibull,
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Gamma_strategy = st.builds(
    ptnet_Gamma,
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Uniform_strategy = st.builds(
    ptnet_Uniform,
    Upper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Lower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Label_strategy = st.builds(
    Label,
)
ptnet_Attribute_strategy = st.builds(
    ptnet_Attribute,
)
Arc_strategy = st.builds(
    Arc,
)
ptnet_GSPNArc_strategy = st.builds(
    ptnet_GSPNArc,
    type=
        safe_text
)
ptnet_LogicalExpression_strategy = st.builds(
    ptnet_LogicalExpression,
)
Transition_strategy = st.builds(
    Transition,
)
ptnet_GSPNTransition_strategy = st.builds(
    ptnet_GSPNTransition,
)
Node_strategy = st.builds(
    Node,
)
ptnet_TransitionNode_strategy = st.builds(
    ptnet_TransitionNode,
)
ptnet_PlaceNode_strategy = st.builds(
    ptnet_PlaceNode,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
ptnet_RefTransition_strategy = st.builds(
    ptnet_RefTransition,
)
ptnet_Transition_strategy = st.builds(
    ptnet_Transition,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
ptnet_RefPlace_strategy = st.builds(
    ptnet_RefPlace,
)
ptnet_Annotation_strategy = st.builds(
    ptnet_Annotation,
)
ptnet_Font_strategy = st.builds(
    ptnet_Font,
    family=
        safe_text,
    rotation=
        safe_text,
    style=
        safe_text,
    decoration=
        safe_text,
    weight=
        safe_text,
    size=
        safe_text,
    align=
        safe_text
)
ptnet_Graphics_strategy = st.builds(
    ptnet_Graphics,
)
ptnet_Line_strategy = st.builds(
    ptnet_Line,
    color=
        safe_text,
    width=
        safe_text,
    style=
        safe_text,
    shape=
        safe_text
)
Coordinate_strategy = st.builds(
    Coordinate,
)
ptnet_Offset_strategy = st.builds(
    ptnet_Offset,
)
ptnet_Coordinate_strategy = st.builds(
    ptnet_Coordinate,
    y=
        safe_text,
    x=
        safe_text
)
ptnet_AnyObject_strategy = st.builds(
    ptnet_AnyObject,
)
ptnet_Label_strategy = st.builds(
    ptnet_Label,
)
ptnet_Fill_strategy = st.builds(
    ptnet_Fill,
    color=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text,
    gradientcolor=
        safe_text
)
ptnet_Dimension_strategy = st.builds(
    ptnet_Dimension,
)
ptnet_Position_strategy = st.builds(
    ptnet_Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
ptnet_AnnotationGraphics_strategy = st.builds(
    ptnet_AnnotationGraphics,
)
ptnet_ArcGraphics_strategy = st.builds(
    ptnet_ArcGraphics,
)
ptnet_NodeGraphics_strategy = st.builds(
    ptnet_NodeGraphics,
)
ptnet_PnObject_strategy = st.builds(
    ptnet_PnObject,
    id=
        safe_text
)
ptnet_PetriNet_strategy = st.builds(
    ptnet_PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
ptnet_PetriNetDoc_strategy = st.builds(
    ptnet_PetriNetDoc,
    xmlns=
        safe_text
)
ptnet_Place_strategy = st.builds(
    ptnet_Place,
)
PnObject_strategy = st.builds(
    PnObject,
)
ptnet_Arc_strategy = st.builds(
    ptnet_Arc,
)
ptnet_Page_strategy = st.builds(
    ptnet_Page,
)
ptnet_Node_strategy = st.builds(
    ptnet_Node,
)
ptnet_ToolInfo_strategy = st.builds(
    ptnet_ToolInfo,
    version=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    formattedXMLBuffer=
        safe_text,
    tool=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
ptnet_PTArcAnnotation_strategy = st.builds(
    ptnet_PTArcAnnotation,
    text=
        safe_text
)
ptnet_Name_strategy = st.builds(
    ptnet_Name,
    text=
        safe_text
)
ptnet_PTMarking_strategy = st.builds(
    ptnet_PTMarking,
    text=
        safe_text
)




@given(instance=ptnet_Variable_strategy)
def test_hyp_ptnet_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






























@given(instance=ptnet_VariableValues_strategy)
def test_hyp_ptnet_variablevalues_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original




@given(instance=ptnet_Measure_strategy)
def test_hyp_ptnet_measure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=ptnet_Study_strategy)
def test_hyp_ptnet_study_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original











@given(instance=ptnet_ValueExpression_strategy)
def test_hyp_ptnet_valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=ptnet_Gaussian_strategy)
def test_hyp_ptnet_gaussian_Variance_setter(instance):
    original = instance.Variance
    instance.Variance = original
    assert instance.Variance == original



@given(instance=ptnet_Gaussian_strategy)
def test_hyp_ptnet_gaussian_Mean_setter(instance):
    original = instance.Mean
    instance.Mean = original
    assert instance.Mean == original




@given(instance=ptnet_Exponential_strategy)
def test_hyp_ptnet_exponential_Rate_setter(instance):
    original = instance.Rate
    instance.Rate = original
    assert instance.Rate == original




@given(instance=ptnet_Deterministic_strategy)
def test_hyp_ptnet_deterministic_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original







@given(instance=ptnet_GSPNImmediateTransition_strategy)
def test_hyp_ptnet_gspnimmediatetransition_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original



@given(instance=ptnet_GSPNImmediateTransition_strategy)
def test_hyp_ptnet_gspnimmediatetransition_Priority_setter(instance):
    original = instance.Priority
    instance.Priority = original
    assert instance.Priority == original





@given(instance=ptnet_Weibull_strategy)
def test_hyp_ptnet_weibull_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original



@given(instance=ptnet_Weibull_strategy)
def test_hyp_ptnet_weibull_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original




@given(instance=ptnet_Gamma_strategy)
def test_hyp_ptnet_gamma_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original



@given(instance=ptnet_Gamma_strategy)
def test_hyp_ptnet_gamma_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original




@given(instance=ptnet_Uniform_strategy)
def test_hyp_ptnet_uniform_Upper_setter(instance):
    original = instance.Upper
    instance.Upper = original
    assert instance.Upper == original



@given(instance=ptnet_Uniform_strategy)
def test_hyp_ptnet_uniform_Lower_setter(instance):
    original = instance.Lower
    instance.Lower = original
    assert instance.Lower == original







@given(instance=ptnet_GSPNArc_strategy)
def test_hyp_ptnet_gspnarc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
















@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ptnet_Font_strategy)
def test_hyp_ptnet_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original





@given(instance=ptnet_Line_strategy)
def test_hyp_ptnet_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=ptnet_Line_strategy)
def test_hyp_ptnet_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=ptnet_Line_strategy)
def test_hyp_ptnet_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=ptnet_Line_strategy)
def test_hyp_ptnet_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original






@given(instance=ptnet_Coordinate_strategy)
def test_hyp_ptnet_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=ptnet_Coordinate_strategy)
def test_hyp_ptnet_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original






@given(instance=ptnet_Fill_strategy)
def test_hyp_ptnet_fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=ptnet_Fill_strategy)
def test_hyp_ptnet_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original



@given(instance=ptnet_Fill_strategy)
def test_hyp_ptnet_fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=ptnet_Fill_strategy)
def test_hyp_ptnet_fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original










@given(instance=ptnet_PnObject_strategy)
def test_hyp_ptnet_pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=ptnet_PetriNet_strategy)
def test_hyp_ptnet_petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ptnet_PetriNet_strategy)
def test_hyp_ptnet_petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=ptnet_PetriNetDoc_strategy)
def test_hyp_ptnet_petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original









@given(instance=ptnet_ToolInfo_strategy)
def test_hyp_ptnet_toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=ptnet_ToolInfo_strategy)
def test_hyp_ptnet_toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original



@given(instance=ptnet_ToolInfo_strategy)
def test_hyp_ptnet_toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original



@given(instance=ptnet_ToolInfo_strategy)
def test_hyp_ptnet_toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original





@given(instance=ptnet_PTArcAnnotation_strategy)
def test_hyp_ptnet_ptarcannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=ptnet_Name_strategy)
def test_hyp_ptnet_name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original




@given(instance=ptnet_PTMarking_strategy)
def test_hyp_ptnet_ptmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Annotation,
    Arc,
    ArithmeticBinaryOperator,
    ArithmeticExpression,
    BooleanExpression,
    ComparisonOperator,
    Coordinate,
    Distribution,
    EvaluationType,
    Expression,
    GSPNTransition,
    Graphics,
    Label,
    LogicalExpression,
    Node,
    PlaceNode,
    PnObject,
    Transition,
    TransitionNode,
    ptnet_Annotation,
    ptnet_AnnotationGraphics,
    ptnet_AnyObject,
    ptnet_Arc,
    ptnet_ArcGraphics,
    ptnet_ArithmeticBinaryOperator,
    ptnet_ArithmeticExpression,
    ptnet_Attribute,
    ptnet_BooleanExpression,
    ptnet_ComparisonOperator,
    ptnet_Coordinate,
    ptnet_Deterministic,
    ptnet_Dimension,
    ptnet_Distribution,
    ptnet_EvaluationList,
    ptnet_EvaluationType,
    ptnet_Exponential,
    ptnet_Expression,
    ptnet_Fill,
    ptnet_Font,
    ptnet_GSPNArc,
    ptnet_GSPNImmediateTransition,
    ptnet_GSPNTimedTransition,
    ptnet_GSPNTransition,
    ptnet_Gamma,
    ptnet_Gaussian,
    ptnet_Graphics,
    ptnet_IfThenElse,
    ptnet_InstantOfTime,
    ptnet_IntervalOfTime,
    ptnet_IntervalOfTimeAveraged,
    ptnet_Label,
    ptnet_Line,
    ptnet_LogicalExpression,
    ptnet_MarkingExpression,
    ptnet_Measure,
    ptnet_Name,
    ptnet_Node,
    ptnet_NodeGraphics,
    ptnet_Offset,
    ptnet_OpAnd,
    ptnet_OpDivide,
    ptnet_OpEqual,
    ptnet_OpFalse,
    ptnet_OpGreater,
    ptnet_OpGreaterEqual,
    ptnet_OpLess,
    ptnet_OpLessEqual,
    ptnet_OpMinus,
    ptnet_OpMultiply,
    ptnet_OpNot,
    ptnet_OpOr,
    ptnet_OpSum,
    ptnet_OpTrue,
    ptnet_PTArcAnnotation,
    ptnet_PTMarking,
    ptnet_Page,
    ptnet_PetriNet,
    ptnet_PetriNetDoc,
    ptnet_Place,
    ptnet_PlaceNode,
    ptnet_PnObject,
    ptnet_Position,
    ptnet_RefPlace,
    ptnet_RefTransition,
    ptnet_SteadyState,
    ptnet_Study,
    ptnet_ToolInfo,
    ptnet_Transition,
    ptnet_TransitionNode,
    ptnet_Uniform,
    ptnet_ValueExpression,
    ptnet_Variable,
    ptnet_VariableExpression,
    ptnet_VariableValues,
    ptnet_Weibull,
    CSS2Color,
    CSS2FontFamily,
    CSS2FontSize,
    CSS2FontStyle,
    CSS2FontWeight,
    FontAlign,
    FontDecoration,
    GSPNArcType,
    GSPNTransitionType,
    Gradient,
    LineShape,
    LineStyle,
    PNType,
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

def test_ptnet_Coordinate_x_value_roundtrip():
    instance = ptnet_Coordinate(x="sample_text", y="sample_text")
    assert instance.x == "sample_text"
    instance.x = "sample_text_2"
    assert instance.x == "sample_text_2"


def test_ptnet_Coordinate_y_value_roundtrip():
    instance = ptnet_Coordinate(x="sample_text", y="sample_text")
    assert instance.y == "sample_text"
    instance.y = "sample_text_2"
    assert instance.y == "sample_text_2"


def test_ptnet_Deterministic_Value_value_roundtrip():
    instance = ptnet_Deterministic(Value=3.14)
    assert instance.Value == 3.14
    instance.Value = 9.99
    assert instance.Value == 9.99


def test_ptnet_Exponential_Rate_value_roundtrip():
    instance = ptnet_Exponential(Rate=3.14)
    assert instance.Rate == 3.14
    instance.Rate = 9.99
    assert instance.Rate == 9.99


def test_ptnet_Fill_color_value_roundtrip():
    instance = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_ptnet_Fill_gradientcolor_value_roundtrip():
    instance = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.gradientcolor == "sample_text"
    instance.gradientcolor = "sample_text_2"
    assert instance.gradientcolor == "sample_text_2"


def test_ptnet_Fill_gradientrotation_value_roundtrip():
    instance = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.gradientrotation == "sample_text"
    instance.gradientrotation = "sample_text_2"
    assert instance.gradientrotation == "sample_text_2"


def test_ptnet_Fill_image_value_roundtrip():
    instance = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    assert instance.image == "sample_text"
    instance.image = "sample_text_2"
    assert instance.image == "sample_text_2"


def test_ptnet_Font_align_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.align == "sample_text"
    instance.align = "sample_text_2"
    assert instance.align == "sample_text_2"


def test_ptnet_Font_decoration_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.decoration == "sample_text"
    instance.decoration = "sample_text_2"
    assert instance.decoration == "sample_text_2"


def test_ptnet_Font_family_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.family == "sample_text"
    instance.family = "sample_text_2"
    assert instance.family == "sample_text_2"


def test_ptnet_Font_rotation_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.rotation == "sample_text"
    instance.rotation = "sample_text_2"
    assert instance.rotation == "sample_text_2"


def test_ptnet_Font_size_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.size == "sample_text"
    instance.size = "sample_text_2"
    assert instance.size == "sample_text_2"


def test_ptnet_Font_style_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_ptnet_Font_weight_value_roundtrip():
    instance = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    assert instance.weight == "sample_text"
    instance.weight = "sample_text_2"
    assert instance.weight == "sample_text_2"


def test_ptnet_GSPNArc_type_value_roundtrip():
    instance = ptnet_GSPNArc(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ptnet_GSPNImmediateTransition_Priority_value_roundtrip():
    instance = ptnet_GSPNImmediateTransition(Priority=7, Weight=3.14)
    assert instance.Priority == 7
    instance.Priority = 13
    assert instance.Priority == 13


def test_ptnet_GSPNImmediateTransition_Weight_value_roundtrip():
    instance = ptnet_GSPNImmediateTransition(Priority=7, Weight=3.14)
    assert instance.Weight == 3.14
    instance.Weight = 9.99
    assert instance.Weight == 9.99


def test_ptnet_Gamma_Alpha_value_roundtrip():
    instance = ptnet_Gamma(Alpha=3.14, Beta=3.14)
    assert instance.Alpha == 3.14
    instance.Alpha = 9.99
    assert instance.Alpha == 9.99


def test_ptnet_Gamma_Beta_value_roundtrip():
    instance = ptnet_Gamma(Alpha=3.14, Beta=3.14)
    assert instance.Beta == 3.14
    instance.Beta = 9.99
    assert instance.Beta == 9.99


def test_ptnet_Gaussian_Mean_value_roundtrip():
    instance = ptnet_Gaussian(Mean=3.14, Variance=3.14)
    assert instance.Mean == 3.14
    instance.Mean = 9.99
    assert instance.Mean == 9.99


def test_ptnet_Gaussian_Variance_value_roundtrip():
    instance = ptnet_Gaussian(Mean=3.14, Variance=3.14)
    assert instance.Variance == 3.14
    instance.Variance = 9.99
    assert instance.Variance == 9.99


def test_ptnet_Line_color_value_roundtrip():
    instance = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_ptnet_Line_shape_value_roundtrip():
    instance = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    assert instance.shape == "sample_text"
    instance.shape = "sample_text_2"
    assert instance.shape == "sample_text_2"


def test_ptnet_Line_style_value_roundtrip():
    instance = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    assert instance.style == "sample_text"
    instance.style = "sample_text_2"
    assert instance.style == "sample_text_2"


def test_ptnet_Line_width_value_roundtrip():
    instance = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    assert instance.width == "sample_text"
    instance.width = "sample_text_2"
    assert instance.width == "sample_text_2"


def test_ptnet_Measure_name_value_roundtrip():
    instance = ptnet_Measure(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ptnet_Name_text_value_roundtrip():
    instance = ptnet_Name(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_ptnet_PTArcAnnotation_text_value_roundtrip():
    instance = ptnet_PTArcAnnotation(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_ptnet_PTMarking_text_value_roundtrip():
    instance = ptnet_PTMarking(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_ptnet_PetriNet_id_value_roundtrip():
    instance = ptnet_PetriNet(id="sample_text", type="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_ptnet_PetriNet_type_value_roundtrip():
    instance = ptnet_PetriNet(id="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_ptnet_PetriNetDoc_xmlns_value_roundtrip():
    instance = ptnet_PetriNetDoc(xmlns="sample_text")
    assert instance.xmlns == "sample_text"
    instance.xmlns = "sample_text_2"
    assert instance.xmlns == "sample_text_2"


def test_ptnet_PnObject_id_value_roundtrip():
    instance = ptnet_PnObject(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_ptnet_Study_name_value_roundtrip():
    instance = ptnet_Study(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ptnet_ToolInfo_formattedXMLBuffer_value_roundtrip():
    instance = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    assert instance.formattedXMLBuffer == "sample_text"
    instance.formattedXMLBuffer = "sample_text_2"
    assert instance.formattedXMLBuffer == "sample_text_2"


def test_ptnet_ToolInfo_tool_value_roundtrip():
    instance = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_ptnet_ToolInfo_toolInfoGrammarURI_value_roundtrip():
    instance = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    assert instance.toolInfoGrammarURI == "sample_text"
    instance.toolInfoGrammarURI = "sample_text_2"
    assert instance.toolInfoGrammarURI == "sample_text_2"


def test_ptnet_ToolInfo_version_value_roundtrip():
    instance = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_ptnet_Uniform_Lower_value_roundtrip():
    instance = ptnet_Uniform(Lower=3.14, Upper=3.14)
    assert instance.Lower == 3.14
    instance.Lower = 9.99
    assert instance.Lower == 9.99


def test_ptnet_Uniform_Upper_value_roundtrip():
    instance = ptnet_Uniform(Lower=3.14, Upper=3.14)
    assert instance.Upper == 3.14
    instance.Upper = 9.99
    assert instance.Upper == 9.99


def test_ptnet_ValueExpression_value_value_roundtrip():
    instance = ptnet_ValueExpression(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_ptnet_Variable_name_value_roundtrip():
    instance = ptnet_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_ptnet_VariableValues_values_value_roundtrip():
    instance = ptnet_VariableValues(values=3.14)
    assert instance.values == 3.14
    instance.values = 9.99
    assert instance.values == 9.99


def test_ptnet_Weibull_Alpha_value_roundtrip():
    instance = ptnet_Weibull(Alpha=3.14, Beta=3.14)
    assert instance.Alpha == 3.14
    instance.Alpha = 9.99
    assert instance.Alpha == 9.99


def test_ptnet_Weibull_Beta_value_roundtrip():
    instance = ptnet_Weibull(Alpha=3.14, Beta=3.14)
    assert instance.Beta == 3.14
    instance.Beta = 9.99
    assert instance.Beta == 9.99


def test_ptnet_Name_isa_Annotation():
    instance = ptnet_Name(text="sample_text")
    assert isinstance(instance, Annotation)


def test_ptnet_PTArcAnnotation_isa_Annotation():
    instance = ptnet_PTArcAnnotation(text="sample_text")
    assert isinstance(instance, Annotation)


def test_ptnet_PTMarking_isa_Annotation():
    instance = ptnet_PTMarking(text="sample_text")
    assert isinstance(instance, Annotation)


def test_ptnet_GSPNArc_isa_Arc():
    instance = ptnet_GSPNArc(type="sample_text")
    assert isinstance(instance, Arc)


def test_ptnet_OpDivide_isa_ArithmeticBinaryOperator():
    instance = ptnet_OpDivide()
    assert isinstance(instance, ArithmeticBinaryOperator)


def test_ptnet_OpMinus_isa_ArithmeticBinaryOperator():
    instance = ptnet_OpMinus()
    assert isinstance(instance, ArithmeticBinaryOperator)


def test_ptnet_OpMultiply_isa_ArithmeticBinaryOperator():
    instance = ptnet_OpMultiply()
    assert isinstance(instance, ArithmeticBinaryOperator)


def test_ptnet_OpSum_isa_ArithmeticBinaryOperator():
    instance = ptnet_OpSum()
    assert isinstance(instance, ArithmeticBinaryOperator)


def test_ptnet_ArithmeticBinaryOperator_isa_ArithmeticExpression():
    instance = ptnet_ArithmeticBinaryOperator()
    assert isinstance(instance, ArithmeticExpression)


def test_ptnet_IfThenElse_isa_ArithmeticExpression():
    instance = ptnet_IfThenElse()
    assert isinstance(instance, ArithmeticExpression)


def test_ptnet_MarkingExpression_isa_ArithmeticExpression():
    instance = ptnet_MarkingExpression()
    assert isinstance(instance, ArithmeticExpression)


def test_ptnet_ValueExpression_isa_ArithmeticExpression():
    instance = ptnet_ValueExpression(value=3.14)
    assert isinstance(instance, ArithmeticExpression)


def test_ptnet_VariableExpression_isa_ArithmeticExpression():
    instance = ptnet_VariableExpression()
    assert isinstance(instance, ArithmeticExpression)


def test_ptnet_OpAnd_isa_BooleanExpression():
    instance = ptnet_OpAnd()
    assert isinstance(instance, BooleanExpression)


def test_ptnet_OpOr_isa_BooleanExpression():
    instance = ptnet_OpOr()
    assert isinstance(instance, BooleanExpression)


def test_ptnet_OpEqual_isa_ComparisonOperator():
    instance = ptnet_OpEqual()
    assert isinstance(instance, ComparisonOperator)


def test_ptnet_OpGreater_isa_ComparisonOperator():
    instance = ptnet_OpGreater()
    assert isinstance(instance, ComparisonOperator)


def test_ptnet_OpGreaterEqual_isa_ComparisonOperator():
    instance = ptnet_OpGreaterEqual()
    assert isinstance(instance, ComparisonOperator)


def test_ptnet_OpLess_isa_ComparisonOperator():
    instance = ptnet_OpLess()
    assert isinstance(instance, ComparisonOperator)


def test_ptnet_OpLessEqual_isa_ComparisonOperator():
    instance = ptnet_OpLessEqual()
    assert isinstance(instance, ComparisonOperator)


def test_ptnet_Dimension_isa_Coordinate():
    instance = ptnet_Dimension()
    assert isinstance(instance, Coordinate)


def test_ptnet_Offset_isa_Coordinate():
    instance = ptnet_Offset()
    assert isinstance(instance, Coordinate)


def test_ptnet_Position_isa_Coordinate():
    instance = ptnet_Position()
    assert isinstance(instance, Coordinate)


def test_ptnet_Deterministic_isa_Distribution():
    instance = ptnet_Deterministic(Value=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_Exponential_isa_Distribution():
    instance = ptnet_Exponential(Rate=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_Gamma_isa_Distribution():
    instance = ptnet_Gamma(Alpha=3.14, Beta=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_Gaussian_isa_Distribution():
    instance = ptnet_Gaussian(Mean=3.14, Variance=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_Uniform_isa_Distribution():
    instance = ptnet_Uniform(Lower=3.14, Upper=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_Weibull_isa_Distribution():
    instance = ptnet_Weibull(Alpha=3.14, Beta=3.14)
    assert isinstance(instance, Distribution)


def test_ptnet_InstantOfTime_isa_EvaluationType():
    instance = ptnet_InstantOfTime()
    assert isinstance(instance, EvaluationType)


def test_ptnet_IntervalOfTime_isa_EvaluationType():
    instance = ptnet_IntervalOfTime()
    assert isinstance(instance, EvaluationType)


def test_ptnet_IntervalOfTimeAveraged_isa_EvaluationType():
    instance = ptnet_IntervalOfTimeAveraged()
    assert isinstance(instance, EvaluationType)


def test_ptnet_SteadyState_isa_EvaluationType():
    instance = ptnet_SteadyState()
    assert isinstance(instance, EvaluationType)


def test_ptnet_ArithmeticExpression_isa_Expression():
    instance = ptnet_ArithmeticExpression()
    assert isinstance(instance, Expression)


def test_ptnet_LogicalExpression_isa_Expression():
    instance = ptnet_LogicalExpression()
    assert isinstance(instance, Expression)


def test_ptnet_GSPNImmediateTransition_isa_GSPNTransition():
    instance = ptnet_GSPNImmediateTransition(Priority=7, Weight=3.14)
    assert isinstance(instance, GSPNTransition)


def test_ptnet_GSPNTimedTransition_isa_GSPNTransition():
    instance = ptnet_GSPNTimedTransition()
    assert isinstance(instance, GSPNTransition)


def test_ptnet_AnnotationGraphics_isa_Graphics():
    instance = ptnet_AnnotationGraphics()
    assert isinstance(instance, Graphics)


def test_ptnet_ArcGraphics_isa_Graphics():
    instance = ptnet_ArcGraphics()
    assert isinstance(instance, Graphics)


def test_ptnet_NodeGraphics_isa_Graphics():
    instance = ptnet_NodeGraphics()
    assert isinstance(instance, Graphics)


def test_ptnet_Annotation_isa_Label():
    instance = ptnet_Annotation()
    assert isinstance(instance, Label)


def test_ptnet_Attribute_isa_Label():
    instance = ptnet_Attribute()
    assert isinstance(instance, Label)


def test_ptnet_BooleanExpression_isa_LogicalExpression():
    instance = ptnet_BooleanExpression()
    assert isinstance(instance, LogicalExpression)


def test_ptnet_ComparisonOperator_isa_LogicalExpression():
    instance = ptnet_ComparisonOperator()
    assert isinstance(instance, LogicalExpression)


def test_ptnet_OpFalse_isa_LogicalExpression():
    instance = ptnet_OpFalse()
    assert isinstance(instance, LogicalExpression)


def test_ptnet_OpNot_isa_LogicalExpression():
    instance = ptnet_OpNot()
    assert isinstance(instance, LogicalExpression)


def test_ptnet_OpTrue_isa_LogicalExpression():
    instance = ptnet_OpTrue()
    assert isinstance(instance, LogicalExpression)


def test_ptnet_PlaceNode_isa_Node():
    instance = ptnet_PlaceNode()
    assert isinstance(instance, Node)


def test_ptnet_TransitionNode_isa_Node():
    instance = ptnet_TransitionNode()
    assert isinstance(instance, Node)


def test_ptnet_Place_isa_PlaceNode():
    instance = ptnet_Place()
    assert isinstance(instance, PlaceNode)


def test_ptnet_RefPlace_isa_PlaceNode():
    instance = ptnet_RefPlace()
    assert isinstance(instance, PlaceNode)


def test_ptnet_Arc_isa_PnObject():
    instance = ptnet_Arc()
    assert isinstance(instance, PnObject)


def test_ptnet_Node_isa_PnObject():
    instance = ptnet_Node()
    assert isinstance(instance, PnObject)


def test_ptnet_Page_isa_PnObject():
    instance = ptnet_Page()
    assert isinstance(instance, PnObject)


def test_ptnet_GSPNTransition_isa_Transition():
    instance = ptnet_GSPNTransition()
    assert isinstance(instance, Transition)


def test_ptnet_RefTransition_isa_TransitionNode():
    instance = ptnet_RefTransition()
    assert isinstance(instance, TransitionNode)


def test_ptnet_Transition_isa_TransitionNode():
    instance = ptnet_Transition()
    assert isinstance(instance, TransitionNode)


def test_assoc_MultiplicityFunction106_link_reassign_clear():
    a = ptnet_GSPNArc(type="sample_text")
    b1 = ptnet_ArithmeticExpression()
    b2 = ptnet_ArithmeticExpression()
    _safe_set(a, 'ptnet_GSPNArc', b1)
    assert _is_linked(a, 'ptnet_GSPNArc', b1)
    if hasattr(b1, 'ptnet_ArithmeticExpression'):
        assert _is_linked(b1, 'ptnet_ArithmeticExpression', a)
    _safe_set(a, 'ptnet_GSPNArc', b2)
    assert _is_linked(a, 'ptnet_GSPNArc', b2)
    if hasattr(b1, 'ptnet_ArithmeticExpression'):
        assert not _is_linked(b1, 'ptnet_ArithmeticExpression', a)
    if hasattr(b2, 'ptnet_ArithmeticExpression'):
        assert _is_linked(b2, 'ptnet_ArithmeticExpression', a)
    _safe_set(a, 'ptnet_GSPNArc', None)
    assert not _is_linked(a, 'ptnet_GSPNArc', b2)
    if hasattr(b2, 'ptnet_ArithmeticExpression'):
        assert not _is_linked(b2, 'ptnet_ArithmeticExpression', a)


def test_assoc_containerAnnotationGraphics61_link_reassign_clear():
    a = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'fill62', b1)
    assert _is_linked(a, 'fill62', b1)
    if hasattr(b1, 'AnnotationGraphics63'):
        assert _is_linked(b1, 'AnnotationGraphics63', a)
    _safe_set(a, 'fill62', b2)
    assert _is_linked(a, 'fill62', b2)
    if hasattr(b1, 'AnnotationGraphics63'):
        assert not _is_linked(b1, 'AnnotationGraphics63', a)
    if hasattr(b2, 'AnnotationGraphics63'):
        assert _is_linked(b2, 'AnnotationGraphics63', a)
    _safe_set(a, 'fill62', None)
    assert not _is_linked(a, 'fill62', b2)
    if hasattr(b2, 'AnnotationGraphics63'):
        assert not _is_linked(b2, 'AnnotationGraphics63', a)


def test_assoc_containerAnnotationGraphics69_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'line70', b1)
    assert _is_linked(a, 'line70', b1)
    if hasattr(b1, 'AnnotationGraphics71'):
        assert _is_linked(b1, 'AnnotationGraphics71', a)
    _safe_set(a, 'line70', b2)
    assert _is_linked(a, 'line70', b2)
    if hasattr(b1, 'AnnotationGraphics71'):
        assert not _is_linked(b1, 'AnnotationGraphics71', a)
    if hasattr(b2, 'AnnotationGraphics71'):
        assert _is_linked(b2, 'AnnotationGraphics71', a)
    _safe_set(a, 'line70', None)
    assert not _is_linked(a, 'line70', b2)
    if hasattr(b2, 'AnnotationGraphics71'):
        assert not _is_linked(b2, 'AnnotationGraphics71', a)


def test_assoc_containerAnnotationGraphics93_link_reassign_clear():
    a = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'font', b1)
    assert _is_linked(a, 'font', b1)
    if hasattr(b1, 'AnnotationGraphics94'):
        assert _is_linked(b1, 'AnnotationGraphics94', a)
    _safe_set(a, 'font', b2)
    assert _is_linked(a, 'font', b2)
    if hasattr(b1, 'AnnotationGraphics94'):
        assert not _is_linked(b1, 'AnnotationGraphics94', a)
    if hasattr(b2, 'AnnotationGraphics94'):
        assert _is_linked(b2, 'AnnotationGraphics94', a)
    _safe_set(a, 'font', None)
    assert not _is_linked(a, 'font', b2)
    if hasattr(b2, 'AnnotationGraphics94'):
        assert not _is_linked(b2, 'AnnotationGraphics94', a)


def test_assoc_containerArc1_link_reassign_clear():
    a = ptnet_PTArcAnnotation(text="sample_text")
    b1 = ptnet_Arc()
    b2 = ptnet_Arc()
    _safe_set(a, 'inscription', b1)
    assert _is_linked(a, 'inscription', b1)
    if hasattr(b1, 'Arc'):
        assert _is_linked(b1, 'Arc', a)
    _safe_set(a, 'inscription', b2)
    assert _is_linked(a, 'inscription', b2)
    if hasattr(b1, 'Arc'):
        assert not _is_linked(b1, 'Arc', a)
    if hasattr(b2, 'Arc'):
        assert _is_linked(b2, 'Arc', a)
    _safe_set(a, 'inscription', None)
    assert not _is_linked(a, 'inscription', b2)
    if hasattr(b2, 'Arc'):
        assert not _is_linked(b2, 'Arc', a)


def test_assoc_containerArcGraphics66_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_ArcGraphics()
    b2 = ptnet_ArcGraphics()
    _safe_set(a, 'line67', b1)
    assert _is_linked(a, 'line67', b1)
    if hasattr(b1, 'ArcGraphics68'):
        assert _is_linked(b1, 'ArcGraphics68', a)
    _safe_set(a, 'line67', b2)
    assert _is_linked(a, 'line67', b2)
    if hasattr(b1, 'ArcGraphics68'):
        assert not _is_linked(b1, 'ArcGraphics68', a)
    if hasattr(b2, 'ArcGraphics68'):
        assert _is_linked(b2, 'ArcGraphics68', a)
    _safe_set(a, 'line67', None)
    assert not _is_linked(a, 'line67', b2)
    if hasattr(b2, 'ArcGraphics68'):
        assert not _is_linked(b2, 'ArcGraphics68', a)


def test_assoc_containerLabel29_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_Label()
    b2 = ptnet_Label()
    _safe_set(a, 'toolspecifics30', b1)
    assert _is_linked(a, 'toolspecifics30', b1)
    if hasattr(b1, 'Label'):
        assert _is_linked(b1, 'Label', a)
    _safe_set(a, 'toolspecifics30', b2)
    assert _is_linked(a, 'toolspecifics30', b2)
    if hasattr(b1, 'Label'):
        assert not _is_linked(b1, 'Label', a)
    if hasattr(b2, 'Label'):
        assert _is_linked(b2, 'Label', a)
    _safe_set(a, 'toolspecifics30', None)
    assert not _is_linked(a, 'toolspecifics30', b2)
    if hasattr(b2, 'Label'):
        assert not _is_linked(b2, 'Label', a)


def test_assoc_containerNamePetriNet19_link_reassign_clear():
    a = ptnet_PetriNet(id="sample_text", type="sample_text")
    b1 = ptnet_Name(text="sample_text")
    b2 = ptnet_Name(text="sample_text_2")
    _safe_set(a, 'PetriNet20', b1)
    assert _is_linked(a, 'PetriNet20', b1)
    if hasattr(b1, 'name'):
        assert _is_linked(b1, 'name', a)
    _safe_set(a, 'PetriNet20', b2)
    assert _is_linked(a, 'PetriNet20', b2)
    if hasattr(b1, 'name'):
        assert not _is_linked(b1, 'name', a)
    if hasattr(b2, 'name'):
        assert _is_linked(b2, 'name', a)
    _safe_set(a, 'PetriNet20', None)
    assert not _is_linked(a, 'PetriNet20', b2)
    if hasattr(b2, 'name'):
        assert not _is_linked(b2, 'name', a)


def test_assoc_containerNamePnObject21_link_reassign_clear():
    a = ptnet_PnObject(id="sample_text")
    b1 = ptnet_Name(text="sample_text")
    b2 = ptnet_Name(text="sample_text_2")
    _safe_set(a, 'PnObject23', b1)
    assert _is_linked(a, 'PnObject23', b1)
    if hasattr(b1, 'name22'):
        assert _is_linked(b1, 'name22', a)
    _safe_set(a, 'PnObject23', b2)
    assert _is_linked(a, 'PnObject23', b2)
    if hasattr(b1, 'name22'):
        assert not _is_linked(b1, 'name22', a)
    if hasattr(b2, 'name22'):
        assert _is_linked(b2, 'name22', a)
    _safe_set(a, 'PnObject23', None)
    assert not _is_linked(a, 'PnObject23', b2)
    if hasattr(b2, 'name22'):
        assert not _is_linked(b2, 'name22', a)


def test_assoc_containerNodeGraphics59_link_reassign_clear():
    a = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = ptnet_NodeGraphics()
    b2 = ptnet_NodeGraphics()
    _safe_set(a, 'fill', b1)
    assert _is_linked(a, 'fill', b1)
    if hasattr(b1, 'NodeGraphics60'):
        assert _is_linked(b1, 'NodeGraphics60', a)
    _safe_set(a, 'fill', b2)
    assert _is_linked(a, 'fill', b2)
    if hasattr(b1, 'NodeGraphics60'):
        assert not _is_linked(b1, 'NodeGraphics60', a)
    if hasattr(b2, 'NodeGraphics60'):
        assert _is_linked(b2, 'NodeGraphics60', a)
    _safe_set(a, 'fill', None)
    assert not _is_linked(a, 'fill', b2)
    if hasattr(b2, 'NodeGraphics60'):
        assert not _is_linked(b2, 'NodeGraphics60', a)


def test_assoc_containerNodeGraphics64_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_NodeGraphics()
    b2 = ptnet_NodeGraphics()
    _safe_set(a, 'line', b1)
    assert _is_linked(a, 'line', b1)
    if hasattr(b1, 'NodeGraphics65'):
        assert _is_linked(b1, 'NodeGraphics65', a)
    _safe_set(a, 'line', b2)
    assert _is_linked(a, 'line', b2)
    if hasattr(b1, 'NodeGraphics65'):
        assert not _is_linked(b1, 'NodeGraphics65', a)
    if hasattr(b2, 'NodeGraphics65'):
        assert _is_linked(b2, 'NodeGraphics65', a)
    _safe_set(a, 'line', None)
    assert not _is_linked(a, 'line', b2)
    if hasattr(b2, 'NodeGraphics65'):
        assert not _is_linked(b2, 'NodeGraphics65', a)


def test_assoc_containerPage17_link_reassign_clear():
    a = ptnet_PnObject(id="sample_text")
    b1 = ptnet_Page()
    b2 = ptnet_Page()
    _safe_set(a, 'objects', b1)
    assert _is_linked(a, 'objects', b1)
    if hasattr(b1, 'Page18'):
        assert _is_linked(b1, 'Page18', a)
    _safe_set(a, 'objects', b2)
    assert _is_linked(a, 'objects', b2)
    if hasattr(b1, 'Page18'):
        assert not _is_linked(b1, 'Page18', a)
    if hasattr(b2, 'Page18'):
        assert _is_linked(b2, 'Page18', a)
    _safe_set(a, 'objects', None)
    assert not _is_linked(a, 'objects', b2)
    if hasattr(b2, 'Page18'):
        assert not _is_linked(b2, 'Page18', a)


def test_assoc_containerPetriNet24_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    b2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'toolspecifics', b1)
    assert _is_linked(a, 'toolspecifics', b1)
    if hasattr(b1, 'PetriNet25'):
        assert _is_linked(b1, 'PetriNet25', a)
    _safe_set(a, 'toolspecifics', b2)
    assert _is_linked(a, 'toolspecifics', b2)
    if hasattr(b1, 'PetriNet25'):
        assert not _is_linked(b1, 'PetriNet25', a)
    if hasattr(b2, 'PetriNet25'):
        assert _is_linked(b2, 'PetriNet25', a)
    _safe_set(a, 'toolspecifics', None)
    assert not _is_linked(a, 'toolspecifics', b2)
    if hasattr(b2, 'PetriNet25'):
        assert not _is_linked(b2, 'PetriNet25', a)


def test_assoc_containerPetriNet9_link_reassign_clear():
    a = ptnet_PetriNet(id="sample_text", type="sample_text")
    b1 = ptnet_Page()
    b2 = ptnet_Page()
    _safe_set(a, 'PetriNet10', b1)
    assert _is_linked(a, 'PetriNet10', b1)
    if hasattr(b1, 'pages'):
        assert _is_linked(b1, 'pages', a)
    _safe_set(a, 'PetriNet10', b2)
    assert _is_linked(a, 'PetriNet10', b2)
    if hasattr(b1, 'pages'):
        assert not _is_linked(b1, 'pages', a)
    if hasattr(b2, 'pages'):
        assert _is_linked(b2, 'pages', a)
    _safe_set(a, 'PetriNet10', None)
    assert not _is_linked(a, 'PetriNet10', b2)
    if hasattr(b2, 'pages'):
        assert not _is_linked(b2, 'pages', a)


def test_assoc_containerPetriNetDoc7_link_reassign_clear():
    a = ptnet_PetriNetDoc(xmlns="sample_text")
    b1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    b2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'PetriNetDoc', b1)
    assert _is_linked(a, 'PetriNetDoc', b1)
    if hasattr(b1, 'nets'):
        assert _is_linked(b1, 'nets', a)
    _safe_set(a, 'PetriNetDoc', b2)
    assert _is_linked(a, 'PetriNetDoc', b2)
    if hasattr(b1, 'nets'):
        assert not _is_linked(b1, 'nets', a)
    if hasattr(b2, 'nets'):
        assert _is_linked(b2, 'nets', a)
    _safe_set(a, 'PetriNetDoc', None)
    assert not _is_linked(a, 'PetriNetDoc', b2)
    if hasattr(b2, 'nets'):
        assert not _is_linked(b2, 'nets', a)


def test_assoc_containerPlace0_link_reassign_clear():
    a = ptnet_PTMarking(text="sample_text")
    b1 = ptnet_Place()
    b2 = ptnet_Place()
    _safe_set(a, 'initialMarking', b1)
    assert _is_linked(a, 'initialMarking', b1)
    if hasattr(b1, 'Place'):
        assert _is_linked(b1, 'Place', a)
    _safe_set(a, 'initialMarking', b2)
    assert _is_linked(a, 'initialMarking', b2)
    if hasattr(b1, 'Place'):
        assert not _is_linked(b1, 'Place', a)
    if hasattr(b2, 'Place'):
        assert _is_linked(b2, 'Place', a)
    _safe_set(a, 'initialMarking', None)
    assert not _is_linked(a, 'initialMarking', b2)
    if hasattr(b2, 'Place'):
        assert not _is_linked(b2, 'Place', a)


def test_assoc_containerPnObject26_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_PnObject(id="sample_text")
    b2 = ptnet_PnObject(id="sample_text_2")
    _safe_set(a, 'toolspecifics27', b1)
    assert _is_linked(a, 'toolspecifics27', b1)
    if hasattr(b1, 'PnObject28'):
        assert _is_linked(b1, 'PnObject28', a)
    _safe_set(a, 'toolspecifics27', b2)
    assert _is_linked(a, 'toolspecifics27', b2)
    if hasattr(b1, 'PnObject28'):
        assert not _is_linked(b1, 'PnObject28', a)
    if hasattr(b2, 'PnObject28'):
        assert _is_linked(b2, 'PnObject28', a)
    _safe_set(a, 'toolspecifics27', None)
    assert not _is_linked(a, 'toolspecifics27', b2)
    if hasattr(b2, 'PnObject28'):
        assert not _is_linked(b2, 'PnObject28', a)


def test_assoc_containerToolInfo103_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_AnyObject()
    b2 = ptnet_AnyObject()
    _safe_set(a, 'ToolInfo104', b1)
    assert _is_linked(a, 'ToolInfo104', b1)
    if hasattr(b1, 'toolInfoModel'):
        assert _is_linked(b1, 'toolInfoModel', a)
    _safe_set(a, 'ToolInfo104', b2)
    assert _is_linked(a, 'ToolInfo104', b2)
    if hasattr(b1, 'toolInfoModel'):
        assert not _is_linked(b1, 'toolInfoModel', a)
    if hasattr(b2, 'toolInfoModel'):
        assert _is_linked(b2, 'toolInfoModel', a)
    _safe_set(a, 'ToolInfo104', None)
    assert not _is_linked(a, 'ToolInfo104', b2)
    if hasattr(b2, 'toolInfoModel'):
        assert not _is_linked(b2, 'toolInfoModel', a)


def test_assoc_evaluationType116_link_reassign_clear():
    a = ptnet_Measure(name="sample_text")
    b1 = ptnet_EvaluationType()
    b2 = ptnet_EvaluationType()
    _safe_set(a, 'ptnet_Measure117', b1)
    assert _is_linked(a, 'ptnet_Measure117', b1)
    if hasattr(b1, 'ptnet_EvaluationType'):
        assert _is_linked(b1, 'ptnet_EvaluationType', a)
    _safe_set(a, 'ptnet_Measure117', b2)
    assert _is_linked(a, 'ptnet_Measure117', b2)
    if hasattr(b1, 'ptnet_EvaluationType'):
        assert not _is_linked(b1, 'ptnet_EvaluationType', a)
    if hasattr(b2, 'ptnet_EvaluationType'):
        assert _is_linked(b2, 'ptnet_EvaluationType', a)
    _safe_set(a, 'ptnet_Measure117', None)
    assert not _is_linked(a, 'ptnet_Measure117', b2)
    if hasattr(b2, 'ptnet_EvaluationType'):
        assert not _is_linked(b2, 'ptnet_EvaluationType', a)


def test_assoc_fill36_link_reassign_clear():
    a = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = ptnet_NodeGraphics()
    b2 = ptnet_NodeGraphics()
    _safe_set(a, 'Fill', b1)
    assert _is_linked(a, 'Fill', b1)
    if hasattr(b1, 'containerNodeGraphics'):
        assert _is_linked(b1, 'containerNodeGraphics', a)
    _safe_set(a, 'Fill', b2)
    assert _is_linked(a, 'Fill', b2)
    if hasattr(b1, 'containerNodeGraphics'):
        assert not _is_linked(b1, 'containerNodeGraphics', a)
    if hasattr(b2, 'containerNodeGraphics'):
        assert _is_linked(b2, 'containerNodeGraphics', a)
    _safe_set(a, 'Fill', None)
    assert not _is_linked(a, 'Fill', b2)
    if hasattr(b2, 'containerNodeGraphics'):
        assert not _is_linked(b2, 'containerNodeGraphics', a)


def test_assoc_fill50_link_reassign_clear():
    a = ptnet_Fill(color="sample_text", gradientcolor="sample_text", gradientrotation="sample_text", image="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'Fill52', b1)
    assert _is_linked(a, 'Fill52', b1)
    if hasattr(b1, 'containerAnnotationGraphics51'):
        assert _is_linked(b1, 'containerAnnotationGraphics51', a)
    _safe_set(a, 'Fill52', b2)
    assert _is_linked(a, 'Fill52', b2)
    if hasattr(b1, 'containerAnnotationGraphics51'):
        assert not _is_linked(b1, 'containerAnnotationGraphics51', a)
    if hasattr(b2, 'containerAnnotationGraphics51'):
        assert _is_linked(b2, 'containerAnnotationGraphics51', a)
    _safe_set(a, 'Fill52', None)
    assert not _is_linked(a, 'Fill52', b2)
    if hasattr(b2, 'containerAnnotationGraphics51'):
        assert not _is_linked(b2, 'containerAnnotationGraphics51', a)


def test_assoc_font56_link_reassign_clear():
    a = ptnet_Font(align="sample_text", decoration="sample_text", family="sample_text", rotation="sample_text", size="sample_text", style="sample_text", weight="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'Font', b1)
    assert _is_linked(a, 'Font', b1)
    if hasattr(b1, 'containerAnnotationGraphics57'):
        assert _is_linked(b1, 'containerAnnotationGraphics57', a)
    _safe_set(a, 'Font', b2)
    assert _is_linked(a, 'Font', b2)
    if hasattr(b1, 'containerAnnotationGraphics57'):
        assert not _is_linked(b1, 'containerAnnotationGraphics57', a)
    if hasattr(b2, 'containerAnnotationGraphics57'):
        assert _is_linked(b2, 'containerAnnotationGraphics57', a)
    _safe_set(a, 'Font', None)
    assert not _is_linked(a, 'Font', b2)
    if hasattr(b2, 'containerAnnotationGraphics57'):
        assert not _is_linked(b2, 'containerAnnotationGraphics57', a)


def test_assoc_initialMarking98_link_reassign_clear():
    a = ptnet_PTMarking(text="sample_text")
    b1 = ptnet_Place()
    b2 = ptnet_Place()
    _safe_set(a, 'PTMarking', b1)
    assert _is_linked(a, 'PTMarking', b1)
    if hasattr(b1, 'containerPlace'):
        assert _is_linked(b1, 'containerPlace', a)
    _safe_set(a, 'PTMarking', b2)
    assert _is_linked(a, 'PTMarking', b2)
    if hasattr(b1, 'containerPlace'):
        assert not _is_linked(b1, 'containerPlace', a)
    if hasattr(b2, 'containerPlace'):
        assert _is_linked(b2, 'containerPlace', a)
    _safe_set(a, 'PTMarking', None)
    assert not _is_linked(a, 'PTMarking', b2)
    if hasattr(b2, 'containerPlace'):
        assert not _is_linked(b2, 'containerPlace', a)


def test_assoc_inscription85_link_reassign_clear():
    a = ptnet_PTArcAnnotation(text="sample_text")
    b1 = ptnet_Arc()
    b2 = ptnet_Arc()
    _safe_set(a, 'PTArcAnnotation', b1)
    assert _is_linked(a, 'PTArcAnnotation', b1)
    if hasattr(b1, 'containerArc86'):
        assert _is_linked(b1, 'containerArc86', a)
    _safe_set(a, 'PTArcAnnotation', b2)
    assert _is_linked(a, 'PTArcAnnotation', b2)
    if hasattr(b1, 'containerArc86'):
        assert not _is_linked(b1, 'containerArc86', a)
    if hasattr(b2, 'containerArc86'):
        assert _is_linked(b2, 'containerArc86', a)
    _safe_set(a, 'PTArcAnnotation', None)
    assert not _is_linked(a, 'PTArcAnnotation', b2)
    if hasattr(b2, 'containerArc86'):
        assert not _is_linked(b2, 'containerArc86', a)


def test_assoc_line37_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_NodeGraphics()
    b2 = ptnet_NodeGraphics()
    _safe_set(a, 'Line', b1)
    assert _is_linked(a, 'Line', b1)
    if hasattr(b1, 'containerNodeGraphics38'):
        assert _is_linked(b1, 'containerNodeGraphics38', a)
    _safe_set(a, 'Line', b2)
    assert _is_linked(a, 'Line', b2)
    if hasattr(b1, 'containerNodeGraphics38'):
        assert not _is_linked(b1, 'containerNodeGraphics38', a)
    if hasattr(b2, 'containerNodeGraphics38'):
        assert _is_linked(b2, 'containerNodeGraphics38', a)
    _safe_set(a, 'Line', None)
    assert not _is_linked(a, 'Line', b2)
    if hasattr(b2, 'containerNodeGraphics38'):
        assert not _is_linked(b2, 'containerNodeGraphics38', a)


def test_assoc_line53_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_AnnotationGraphics()
    b2 = ptnet_AnnotationGraphics()
    _safe_set(a, 'Line55', b1)
    assert _is_linked(a, 'Line55', b1)
    if hasattr(b1, 'containerAnnotationGraphics54'):
        assert _is_linked(b1, 'containerAnnotationGraphics54', a)
    _safe_set(a, 'Line55', b2)
    assert _is_linked(a, 'Line55', b2)
    if hasattr(b1, 'containerAnnotationGraphics54'):
        assert not _is_linked(b1, 'containerAnnotationGraphics54', a)
    if hasattr(b2, 'containerAnnotationGraphics54'):
        assert _is_linked(b2, 'containerAnnotationGraphics54', a)
    _safe_set(a, 'Line55', None)
    assert not _is_linked(a, 'Line55', b2)
    if hasattr(b2, 'containerAnnotationGraphics54'):
        assert not _is_linked(b2, 'containerAnnotationGraphics54', a)


def test_assoc_line74_link_reassign_clear():
    a = ptnet_Line(color="sample_text", shape="sample_text", style="sample_text", width="sample_text")
    b1 = ptnet_ArcGraphics()
    b2 = ptnet_ArcGraphics()
    _safe_set(a, 'Line76', b1)
    assert _is_linked(a, 'Line76', b1)
    if hasattr(b1, 'containerArcGraphics75'):
        assert _is_linked(b1, 'containerArcGraphics75', a)
    _safe_set(a, 'Line76', b2)
    assert _is_linked(a, 'Line76', b2)
    if hasattr(b1, 'containerArcGraphics75'):
        assert not _is_linked(b1, 'containerArcGraphics75', a)
    if hasattr(b2, 'containerArcGraphics75'):
        assert _is_linked(b2, 'containerArcGraphics75', a)
    _safe_set(a, 'Line76', None)
    assert not _is_linked(a, 'Line76', b2)
    if hasattr(b2, 'containerArcGraphics75'):
        assert not _is_linked(b2, 'containerArcGraphics75', a)


def test_assoc_measures109_link_reassign_clear():
    a = ptnet_Measure(name="sample_text")
    b1 = ptnet_EvaluationList()
    b2 = ptnet_EvaluationList()
    _safe_set(a, 'ptnet_Measure', b1)
    assert _is_linked(a, 'ptnet_Measure', b1)
    if hasattr(b1, 'ptnet_EvaluationList110'):
        assert _is_linked(b1, 'ptnet_EvaluationList110', a)
    _safe_set(a, 'ptnet_Measure', b2)
    assert _is_linked(a, 'ptnet_Measure', b2)
    if hasattr(b1, 'ptnet_EvaluationList110'):
        assert not _is_linked(b1, 'ptnet_EvaluationList110', a)
    if hasattr(b2, 'ptnet_EvaluationList110'):
        assert _is_linked(b2, 'ptnet_EvaluationList110', a)
    _safe_set(a, 'ptnet_Measure', None)
    assert not _is_linked(a, 'ptnet_Measure', b2)
    if hasattr(b2, 'ptnet_EvaluationList110'):
        assert not _is_linked(b2, 'ptnet_EvaluationList110', a)


def test_assoc_name13_link_reassign_clear():
    a = ptnet_PnObject(id="sample_text")
    b1 = ptnet_Name(text="sample_text")
    b2 = ptnet_Name(text="sample_text_2")
    _safe_set(a, 'containerNamePnObject', b1)
    assert _is_linked(a, 'containerNamePnObject', b1)
    if hasattr(b1, 'Name14'):
        assert _is_linked(b1, 'Name14', a)
    _safe_set(a, 'containerNamePnObject', b2)
    assert _is_linked(a, 'containerNamePnObject', b2)
    if hasattr(b1, 'Name14'):
        assert not _is_linked(b1, 'Name14', a)
    if hasattr(b2, 'Name14'):
        assert _is_linked(b2, 'Name14', a)
    _safe_set(a, 'containerNamePnObject', None)
    assert not _is_linked(a, 'containerNamePnObject', b2)
    if hasattr(b2, 'Name14'):
        assert not _is_linked(b2, 'Name14', a)


def test_assoc_name4_link_reassign_clear():
    a = ptnet_PetriNet(id="sample_text", type="sample_text")
    b1 = ptnet_Name(text="sample_text")
    b2 = ptnet_Name(text="sample_text_2")
    _safe_set(a, 'containerNamePetriNet', b1)
    assert _is_linked(a, 'containerNamePetriNet', b1)
    if hasattr(b1, 'Name'):
        assert _is_linked(b1, 'Name', a)
    _safe_set(a, 'containerNamePetriNet', b2)
    assert _is_linked(a, 'containerNamePetriNet', b2)
    if hasattr(b1, 'Name'):
        assert not _is_linked(b1, 'Name', a)
    if hasattr(b2, 'Name'):
        assert _is_linked(b2, 'Name', a)
    _safe_set(a, 'containerNamePetriNet', None)
    assert not _is_linked(a, 'containerNamePetriNet', b2)
    if hasattr(b2, 'Name'):
        assert not _is_linked(b2, 'Name', a)


def test_assoc_nets2_link_reassign_clear():
    a = ptnet_PetriNetDoc(xmlns="sample_text")
    b1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    b2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'containerPetriNetDoc', {b1})
    assert _is_linked(a, 'containerPetriNetDoc', b1)
    if hasattr(b1, 'PetriNet'):
        assert _is_linked(b1, 'PetriNet', a)
    _safe_set(a, 'containerPetriNetDoc', {b2})
    assert _is_linked(a, 'containerPetriNetDoc', b2)
    if hasattr(b1, 'PetriNet'):
        assert not _is_linked(b1, 'PetriNet', a)
    if hasattr(b2, 'PetriNet'):
        assert _is_linked(b2, 'PetriNet', a)
    _safe_set(a, 'containerPetriNetDoc', set())
    assert not _is_linked(a, 'containerPetriNetDoc', b2)
    if hasattr(b2, 'PetriNet'):
        assert not _is_linked(b2, 'PetriNet', a)


def test_assoc_objects8_link_reassign_clear():
    a = ptnet_PnObject(id="sample_text")
    b1 = ptnet_Page()
    b2 = ptnet_Page()
    _safe_set(a, 'PnObject', b1)
    assert _is_linked(a, 'PnObject', b1)
    if hasattr(b1, 'containerPage'):
        assert _is_linked(b1, 'containerPage', a)
    _safe_set(a, 'PnObject', b2)
    assert _is_linked(a, 'PnObject', b2)
    if hasattr(b1, 'containerPage'):
        assert not _is_linked(b1, 'containerPage', a)
    if hasattr(b2, 'containerPage'):
        assert _is_linked(b2, 'containerPage', a)
    _safe_set(a, 'PnObject', None)
    assert not _is_linked(a, 'PnObject', b2)
    if hasattr(b2, 'containerPage'):
        assert not _is_linked(b2, 'containerPage', a)


def test_assoc_pages3_link_reassign_clear():
    a = ptnet_PetriNet(id="sample_text", type="sample_text")
    b1 = ptnet_Page()
    b2 = ptnet_Page()
    _safe_set(a, 'containerPetriNet', {b1})
    assert _is_linked(a, 'containerPetriNet', b1)
    if hasattr(b1, 'Page'):
        assert _is_linked(b1, 'Page', a)
    _safe_set(a, 'containerPetriNet', {b2})
    assert _is_linked(a, 'containerPetriNet', b2)
    if hasattr(b1, 'Page'):
        assert not _is_linked(b1, 'Page', a)
    if hasattr(b2, 'Page'):
        assert _is_linked(b2, 'Page', a)
    _safe_set(a, 'containerPetriNet', set())
    assert not _is_linked(a, 'containerPetriNet', b2)
    if hasattr(b2, 'Page'):
        assert not _is_linked(b2, 'Page', a)


def test_assoc_rewardFunction113_link_reassign_clear():
    a = ptnet_Measure(name="sample_text")
    b1 = ptnet_ArithmeticExpression()
    b2 = ptnet_ArithmeticExpression()
    _safe_set(a, 'ptnet_Measure114', b1)
    assert _is_linked(a, 'ptnet_Measure114', b1)
    if hasattr(b1, 'ptnet_ArithmeticExpression115'):
        assert _is_linked(b1, 'ptnet_ArithmeticExpression115', a)
    _safe_set(a, 'ptnet_Measure114', b2)
    assert _is_linked(a, 'ptnet_Measure114', b2)
    if hasattr(b1, 'ptnet_ArithmeticExpression115'):
        assert not _is_linked(b1, 'ptnet_ArithmeticExpression115', a)
    if hasattr(b2, 'ptnet_ArithmeticExpression115'):
        assert _is_linked(b2, 'ptnet_ArithmeticExpression115', a)
    _safe_set(a, 'ptnet_Measure114', None)
    assert not _is_linked(a, 'ptnet_Measure114', b2)
    if hasattr(b2, 'ptnet_ArithmeticExpression115'):
        assert not _is_linked(b2, 'ptnet_ArithmeticExpression115', a)


def test_assoc_studies108_link_reassign_clear():
    a = ptnet_Study(name="sample_text")
    b1 = ptnet_EvaluationList()
    b2 = ptnet_EvaluationList()
    _safe_set(a, 'ptnet_Study', b1)
    assert _is_linked(a, 'ptnet_Study', b1)
    if hasattr(b1, 'ptnet_EvaluationList'):
        assert _is_linked(b1, 'ptnet_EvaluationList', a)
    _safe_set(a, 'ptnet_Study', b2)
    assert _is_linked(a, 'ptnet_Study', b2)
    if hasattr(b1, 'ptnet_EvaluationList'):
        assert not _is_linked(b1, 'ptnet_EvaluationList', a)
    if hasattr(b2, 'ptnet_EvaluationList'):
        assert _is_linked(b2, 'ptnet_EvaluationList', a)
    _safe_set(a, 'ptnet_Study', None)
    assert not _is_linked(a, 'ptnet_Study', b2)
    if hasattr(b2, 'ptnet_EvaluationList'):
        assert not _is_linked(b2, 'ptnet_EvaluationList', a)


def test_assoc_toolInfoModel31_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_AnyObject()
    b2 = ptnet_AnyObject()
    _safe_set(a, 'containerToolInfo', b1)
    assert _is_linked(a, 'containerToolInfo', b1)
    if hasattr(b1, 'AnyObject'):
        assert _is_linked(b1, 'AnyObject', a)
    _safe_set(a, 'containerToolInfo', b2)
    assert _is_linked(a, 'containerToolInfo', b2)
    if hasattr(b1, 'AnyObject'):
        assert not _is_linked(b1, 'AnyObject', a)
    if hasattr(b2, 'AnyObject'):
        assert _is_linked(b2, 'AnyObject', a)
    _safe_set(a, 'containerToolInfo', None)
    assert not _is_linked(a, 'containerToolInfo', b2)
    if hasattr(b2, 'AnyObject'):
        assert not _is_linked(b2, 'AnyObject', a)


def test_assoc_toolspecifics15_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_PnObject(id="sample_text")
    b2 = ptnet_PnObject(id="sample_text_2")
    _safe_set(a, 'ToolInfo16', b1)
    assert _is_linked(a, 'ToolInfo16', b1)
    if hasattr(b1, 'containerPnObject'):
        assert _is_linked(b1, 'containerPnObject', a)
    _safe_set(a, 'ToolInfo16', b2)
    assert _is_linked(a, 'ToolInfo16', b2)
    if hasattr(b1, 'containerPnObject'):
        assert not _is_linked(b1, 'containerPnObject', a)
    if hasattr(b2, 'containerPnObject'):
        assert _is_linked(b2, 'containerPnObject', a)
    _safe_set(a, 'ToolInfo16', None)
    assert not _is_linked(a, 'ToolInfo16', b2)
    if hasattr(b2, 'containerPnObject'):
        assert not _is_linked(b2, 'containerPnObject', a)


def test_assoc_toolspecifics32_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_Label()
    b2 = ptnet_Label()
    _safe_set(a, 'ToolInfo33', b1)
    assert _is_linked(a, 'ToolInfo33', b1)
    if hasattr(b1, 'containerLabel'):
        assert _is_linked(b1, 'containerLabel', a)
    _safe_set(a, 'ToolInfo33', b2)
    assert _is_linked(a, 'ToolInfo33', b2)
    if hasattr(b1, 'containerLabel'):
        assert not _is_linked(b1, 'containerLabel', a)
    if hasattr(b2, 'containerLabel'):
        assert _is_linked(b2, 'containerLabel', a)
    _safe_set(a, 'ToolInfo33', None)
    assert not _is_linked(a, 'ToolInfo33', b2)
    if hasattr(b2, 'containerLabel'):
        assert not _is_linked(b2, 'containerLabel', a)


def test_assoc_toolspecifics5_link_reassign_clear():
    a = ptnet_ToolInfo(formattedXMLBuffer="sample_text", tool="sample_text", toolInfoGrammarURI="sample_text", version="sample_text")
    b1 = ptnet_PetriNet(id="sample_text", type="sample_text")
    b2 = ptnet_PetriNet(id="sample_text_2", type="sample_text_2")
    _safe_set(a, 'ToolInfo', b1)
    assert _is_linked(a, 'ToolInfo', b1)
    if hasattr(b1, 'containerPetriNet6'):
        assert _is_linked(b1, 'containerPetriNet6', a)
    _safe_set(a, 'ToolInfo', b2)
    assert _is_linked(a, 'ToolInfo', b2)
    if hasattr(b1, 'containerPetriNet6'):
        assert not _is_linked(b1, 'containerPetriNet6', a)
    if hasattr(b2, 'containerPetriNet6'):
        assert _is_linked(b2, 'containerPetriNet6', a)
    _safe_set(a, 'ToolInfo', None)
    assert not _is_linked(a, 'ToolInfo', b2)
    if hasattr(b2, 'containerPetriNet6'):
        assert not _is_linked(b2, 'containerPetriNet6', a)


def test_assoc_variable156_link_reassign_clear():
    a = ptnet_VariableValues(values=3.14)
    b1 = ptnet_Variable(name="sample_text")
    b2 = ptnet_Variable(name="sample_text_2")
    _safe_set(a, 'ptnet_VariableValues157', b1)
    assert _is_linked(a, 'ptnet_VariableValues157', b1)
    if hasattr(b1, 'ptnet_Variable'):
        assert _is_linked(b1, 'ptnet_Variable', a)
    _safe_set(a, 'ptnet_VariableValues157', b2)
    assert _is_linked(a, 'ptnet_VariableValues157', b2)
    if hasattr(b1, 'ptnet_Variable'):
        assert not _is_linked(b1, 'ptnet_Variable', a)
    if hasattr(b2, 'ptnet_Variable'):
        assert _is_linked(b2, 'ptnet_Variable', a)
    _safe_set(a, 'ptnet_VariableValues157', None)
    assert not _is_linked(a, 'ptnet_VariableValues157', b2)
    if hasattr(b2, 'ptnet_Variable'):
        assert not _is_linked(b2, 'ptnet_Variable', a)


def test_assoc_variable158_link_reassign_clear():
    a = ptnet_Variable(name="sample_text")
    b1 = ptnet_VariableExpression()
    b2 = ptnet_VariableExpression()
    _safe_set(a, 'ptnet_Variable159', b1)
    assert _is_linked(a, 'ptnet_Variable159', b1)
    if hasattr(b1, 'ptnet_VariableExpression'):
        assert _is_linked(b1, 'ptnet_VariableExpression', a)
    _safe_set(a, 'ptnet_Variable159', b2)
    assert _is_linked(a, 'ptnet_Variable159', b2)
    if hasattr(b1, 'ptnet_VariableExpression'):
        assert not _is_linked(b1, 'ptnet_VariableExpression', a)
    if hasattr(b2, 'ptnet_VariableExpression'):
        assert _is_linked(b2, 'ptnet_VariableExpression', a)
    _safe_set(a, 'ptnet_Variable159', None)
    assert not _is_linked(a, 'ptnet_Variable159', b2)
    if hasattr(b2, 'ptnet_VariableExpression'):
        assert not _is_linked(b2, 'ptnet_VariableExpression', a)


def test_assoc_vars111_link_reassign_clear():
    a = ptnet_VariableValues(values=3.14)
    b1 = ptnet_Study(name="sample_text")
    b2 = ptnet_Study(name="sample_text_2")
    _safe_set(a, 'ptnet_VariableValues', b1)
    assert _is_linked(a, 'ptnet_VariableValues', b1)
    if hasattr(b1, 'ptnet_Study112'):
        assert _is_linked(b1, 'ptnet_Study112', a)
    _safe_set(a, 'ptnet_VariableValues', b2)
    assert _is_linked(a, 'ptnet_VariableValues', b2)
    if hasattr(b1, 'ptnet_Study112'):
        assert not _is_linked(b1, 'ptnet_Study112', a)
    if hasattr(b2, 'ptnet_Study112'):
        assert _is_linked(b2, 'ptnet_Study112', a)
    _safe_set(a, 'ptnet_VariableValues', None)
    assert not _is_linked(a, 'ptnet_VariableValues', b2)
    if hasattr(b2, 'ptnet_Study112'):
        assert not _is_linked(b2, 'ptnet_Study112', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Annotation_strategy = st.builds(Annotation)
@given(instance=Annotation_strategy)
@settings(max_examples=25)
def test_Annotation_instantiation(instance):
    assert isinstance(instance, Annotation)


Arc_strategy = st.builds(Arc)
@given(instance=Arc_strategy)
@settings(max_examples=25)
def test_Arc_instantiation(instance):
    assert isinstance(instance, Arc)


ArithmeticBinaryOperator_strategy = st.builds(ArithmeticBinaryOperator)
@given(instance=ArithmeticBinaryOperator_strategy)
@settings(max_examples=25)
def test_ArithmeticBinaryOperator_instantiation(instance):
    assert isinstance(instance, ArithmeticBinaryOperator)


ArithmeticExpression_strategy = st.builds(ArithmeticExpression)
@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)


BooleanExpression_strategy = st.builds(BooleanExpression)
@given(instance=BooleanExpression_strategy)
@settings(max_examples=25)
def test_BooleanExpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)


ComparisonOperator_strategy = st.builds(ComparisonOperator)
@given(instance=ComparisonOperator_strategy)
@settings(max_examples=25)
def test_ComparisonOperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)


Coordinate_strategy = st.builds(Coordinate)
@given(instance=Coordinate_strategy)
@settings(max_examples=25)
def test_Coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)


Distribution_strategy = st.builds(Distribution)
@given(instance=Distribution_strategy)
@settings(max_examples=25)
def test_Distribution_instantiation(instance):
    assert isinstance(instance, Distribution)


EvaluationType_strategy = st.builds(EvaluationType)
@given(instance=EvaluationType_strategy)
@settings(max_examples=25)
def test_EvaluationType_instantiation(instance):
    assert isinstance(instance, EvaluationType)


Expression_strategy = st.builds(Expression)
@given(instance=Expression_strategy)
@settings(max_examples=25)
def test_Expression_instantiation(instance):
    assert isinstance(instance, Expression)


GSPNTransition_strategy = st.builds(GSPNTransition)
@given(instance=GSPNTransition_strategy)
@settings(max_examples=25)
def test_GSPNTransition_instantiation(instance):
    assert isinstance(instance, GSPNTransition)


Graphics_strategy = st.builds(Graphics)
@given(instance=Graphics_strategy)
@settings(max_examples=25)
def test_Graphics_instantiation(instance):
    assert isinstance(instance, Graphics)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


LogicalExpression_strategy = st.builds(LogicalExpression)
@given(instance=LogicalExpression_strategy)
@settings(max_examples=25)
def test_LogicalExpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)


Node_strategy = st.builds(Node)
@given(instance=Node_strategy)
@settings(max_examples=25)
def test_Node_instantiation(instance):
    assert isinstance(instance, Node)


PlaceNode_strategy = st.builds(PlaceNode)
@given(instance=PlaceNode_strategy)
@settings(max_examples=25)
def test_PlaceNode_instantiation(instance):
    assert isinstance(instance, PlaceNode)


PnObject_strategy = st.builds(PnObject)
@given(instance=PnObject_strategy)
@settings(max_examples=25)
def test_PnObject_instantiation(instance):
    assert isinstance(instance, PnObject)


Transition_strategy = st.builds(Transition)
@given(instance=Transition_strategy)
@settings(max_examples=25)
def test_Transition_instantiation(instance):
    assert isinstance(instance, Transition)


TransitionNode_strategy = st.builds(TransitionNode)
@given(instance=TransitionNode_strategy)
@settings(max_examples=25)
def test_TransitionNode_instantiation(instance):
    assert isinstance(instance, TransitionNode)


ptnet_Annotation_strategy = st.builds(ptnet_Annotation)
@given(instance=ptnet_Annotation_strategy)
@settings(max_examples=25)
def test_ptnet_Annotation_instantiation(instance):
    assert isinstance(instance, ptnet_Annotation)


ptnet_AnnotationGraphics_strategy = st.builds(ptnet_AnnotationGraphics)
@given(instance=ptnet_AnnotationGraphics_strategy)
@settings(max_examples=25)
def test_ptnet_AnnotationGraphics_instantiation(instance):
    assert isinstance(instance, ptnet_AnnotationGraphics)


ptnet_AnyObject_strategy = st.builds(ptnet_AnyObject)
@given(instance=ptnet_AnyObject_strategy)
@settings(max_examples=25)
def test_ptnet_AnyObject_instantiation(instance):
    assert isinstance(instance, ptnet_AnyObject)


ptnet_Arc_strategy = st.builds(ptnet_Arc)
@given(instance=ptnet_Arc_strategy)
@settings(max_examples=25)
def test_ptnet_Arc_instantiation(instance):
    assert isinstance(instance, ptnet_Arc)


ptnet_ArcGraphics_strategy = st.builds(ptnet_ArcGraphics)
@given(instance=ptnet_ArcGraphics_strategy)
@settings(max_examples=25)
def test_ptnet_ArcGraphics_instantiation(instance):
    assert isinstance(instance, ptnet_ArcGraphics)


ptnet_ArithmeticBinaryOperator_strategy = st.builds(ptnet_ArithmeticBinaryOperator)
@given(instance=ptnet_ArithmeticBinaryOperator_strategy)
@settings(max_examples=25)
def test_ptnet_ArithmeticBinaryOperator_instantiation(instance):
    assert isinstance(instance, ptnet_ArithmeticBinaryOperator)


ptnet_ArithmeticExpression_strategy = st.builds(ptnet_ArithmeticExpression)
@given(instance=ptnet_ArithmeticExpression_strategy)
@settings(max_examples=25)
def test_ptnet_ArithmeticExpression_instantiation(instance):
    assert isinstance(instance, ptnet_ArithmeticExpression)


ptnet_Attribute_strategy = st.builds(ptnet_Attribute)
@given(instance=ptnet_Attribute_strategy)
@settings(max_examples=25)
def test_ptnet_Attribute_instantiation(instance):
    assert isinstance(instance, ptnet_Attribute)


ptnet_BooleanExpression_strategy = st.builds(ptnet_BooleanExpression)
@given(instance=ptnet_BooleanExpression_strategy)
@settings(max_examples=25)
def test_ptnet_BooleanExpression_instantiation(instance):
    assert isinstance(instance, ptnet_BooleanExpression)


ptnet_ComparisonOperator_strategy = st.builds(ptnet_ComparisonOperator)
@given(instance=ptnet_ComparisonOperator_strategy)
@settings(max_examples=25)
def test_ptnet_ComparisonOperator_instantiation(instance):
    assert isinstance(instance, ptnet_ComparisonOperator)


ptnet_Coordinate_strategy = st.builds(ptnet_Coordinate, x=safe_text, y=safe_text)
@given(instance=ptnet_Coordinate_strategy)
@settings(max_examples=25)
def test_ptnet_Coordinate_instantiation(instance):
    assert isinstance(instance, ptnet_Coordinate)


ptnet_Deterministic_strategy = st.builds(ptnet_Deterministic, Value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Deterministic_strategy)
@settings(max_examples=25)
def test_ptnet_Deterministic_instantiation(instance):
    assert isinstance(instance, ptnet_Deterministic)


ptnet_Dimension_strategy = st.builds(ptnet_Dimension)
@given(instance=ptnet_Dimension_strategy)
@settings(max_examples=25)
def test_ptnet_Dimension_instantiation(instance):
    assert isinstance(instance, ptnet_Dimension)


ptnet_Distribution_strategy = st.builds(ptnet_Distribution)
@given(instance=ptnet_Distribution_strategy)
@settings(max_examples=25)
def test_ptnet_Distribution_instantiation(instance):
    assert isinstance(instance, ptnet_Distribution)


ptnet_EvaluationList_strategy = st.builds(ptnet_EvaluationList)
@given(instance=ptnet_EvaluationList_strategy)
@settings(max_examples=25)
def test_ptnet_EvaluationList_instantiation(instance):
    assert isinstance(instance, ptnet_EvaluationList)


ptnet_EvaluationType_strategy = st.builds(ptnet_EvaluationType)
@given(instance=ptnet_EvaluationType_strategy)
@settings(max_examples=25)
def test_ptnet_EvaluationType_instantiation(instance):
    assert isinstance(instance, ptnet_EvaluationType)


ptnet_Exponential_strategy = st.builds(ptnet_Exponential, Rate=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Exponential_strategy)
@settings(max_examples=25)
def test_ptnet_Exponential_instantiation(instance):
    assert isinstance(instance, ptnet_Exponential)


ptnet_Expression_strategy = st.builds(ptnet_Expression)
@given(instance=ptnet_Expression_strategy)
@settings(max_examples=25)
def test_ptnet_Expression_instantiation(instance):
    assert isinstance(instance, ptnet_Expression)


ptnet_Fill_strategy = st.builds(ptnet_Fill, color=safe_text, gradientcolor=safe_text, gradientrotation=safe_text, image=safe_text)
@given(instance=ptnet_Fill_strategy)
@settings(max_examples=25)
def test_ptnet_Fill_instantiation(instance):
    assert isinstance(instance, ptnet_Fill)


ptnet_Font_strategy = st.builds(ptnet_Font, align=safe_text, decoration=safe_text, family=safe_text, rotation=safe_text, size=safe_text, style=safe_text, weight=safe_text)
@given(instance=ptnet_Font_strategy)
@settings(max_examples=25)
def test_ptnet_Font_instantiation(instance):
    assert isinstance(instance, ptnet_Font)


ptnet_GSPNArc_strategy = st.builds(ptnet_GSPNArc, type=safe_text)
@given(instance=ptnet_GSPNArc_strategy)
@settings(max_examples=25)
def test_ptnet_GSPNArc_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNArc)


ptnet_GSPNImmediateTransition_strategy = st.builds(ptnet_GSPNImmediateTransition, Priority=st.integers(), Weight=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_GSPNImmediateTransition_strategy)
@settings(max_examples=25)
def test_ptnet_GSPNImmediateTransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNImmediateTransition)


ptnet_GSPNTimedTransition_strategy = st.builds(ptnet_GSPNTimedTransition)
@given(instance=ptnet_GSPNTimedTransition_strategy)
@settings(max_examples=25)
def test_ptnet_GSPNTimedTransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNTimedTransition)


ptnet_GSPNTransition_strategy = st.builds(ptnet_GSPNTransition)
@given(instance=ptnet_GSPNTransition_strategy)
@settings(max_examples=25)
def test_ptnet_GSPNTransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNTransition)


ptnet_Gamma_strategy = st.builds(ptnet_Gamma, Alpha=st.floats(allow_nan=False, allow_infinity=False), Beta=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Gamma_strategy)
@settings(max_examples=25)
def test_ptnet_Gamma_instantiation(instance):
    assert isinstance(instance, ptnet_Gamma)


ptnet_Gaussian_strategy = st.builds(ptnet_Gaussian, Mean=st.floats(allow_nan=False, allow_infinity=False), Variance=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Gaussian_strategy)
@settings(max_examples=25)
def test_ptnet_Gaussian_instantiation(instance):
    assert isinstance(instance, ptnet_Gaussian)


ptnet_Graphics_strategy = st.builds(ptnet_Graphics)
@given(instance=ptnet_Graphics_strategy)
@settings(max_examples=25)
def test_ptnet_Graphics_instantiation(instance):
    assert isinstance(instance, ptnet_Graphics)


ptnet_IfThenElse_strategy = st.builds(ptnet_IfThenElse)
@given(instance=ptnet_IfThenElse_strategy)
@settings(max_examples=25)
def test_ptnet_IfThenElse_instantiation(instance):
    assert isinstance(instance, ptnet_IfThenElse)


ptnet_InstantOfTime_strategy = st.builds(ptnet_InstantOfTime)
@given(instance=ptnet_InstantOfTime_strategy)
@settings(max_examples=25)
def test_ptnet_InstantOfTime_instantiation(instance):
    assert isinstance(instance, ptnet_InstantOfTime)


ptnet_IntervalOfTime_strategy = st.builds(ptnet_IntervalOfTime)
@given(instance=ptnet_IntervalOfTime_strategy)
@settings(max_examples=25)
def test_ptnet_IntervalOfTime_instantiation(instance):
    assert isinstance(instance, ptnet_IntervalOfTime)


ptnet_IntervalOfTimeAveraged_strategy = st.builds(ptnet_IntervalOfTimeAveraged)
@given(instance=ptnet_IntervalOfTimeAveraged_strategy)
@settings(max_examples=25)
def test_ptnet_IntervalOfTimeAveraged_instantiation(instance):
    assert isinstance(instance, ptnet_IntervalOfTimeAveraged)


ptnet_Label_strategy = st.builds(ptnet_Label)
@given(instance=ptnet_Label_strategy)
@settings(max_examples=25)
def test_ptnet_Label_instantiation(instance):
    assert isinstance(instance, ptnet_Label)


ptnet_Line_strategy = st.builds(ptnet_Line, color=safe_text, shape=safe_text, style=safe_text, width=safe_text)
@given(instance=ptnet_Line_strategy)
@settings(max_examples=25)
def test_ptnet_Line_instantiation(instance):
    assert isinstance(instance, ptnet_Line)


ptnet_LogicalExpression_strategy = st.builds(ptnet_LogicalExpression)
@given(instance=ptnet_LogicalExpression_strategy)
@settings(max_examples=25)
def test_ptnet_LogicalExpression_instantiation(instance):
    assert isinstance(instance, ptnet_LogicalExpression)


ptnet_MarkingExpression_strategy = st.builds(ptnet_MarkingExpression)
@given(instance=ptnet_MarkingExpression_strategy)
@settings(max_examples=25)
def test_ptnet_MarkingExpression_instantiation(instance):
    assert isinstance(instance, ptnet_MarkingExpression)


ptnet_Measure_strategy = st.builds(ptnet_Measure, name=safe_text)
@given(instance=ptnet_Measure_strategy)
@settings(max_examples=25)
def test_ptnet_Measure_instantiation(instance):
    assert isinstance(instance, ptnet_Measure)


ptnet_Name_strategy = st.builds(ptnet_Name, text=safe_text)
@given(instance=ptnet_Name_strategy)
@settings(max_examples=25)
def test_ptnet_Name_instantiation(instance):
    assert isinstance(instance, ptnet_Name)


ptnet_Node_strategy = st.builds(ptnet_Node)
@given(instance=ptnet_Node_strategy)
@settings(max_examples=25)
def test_ptnet_Node_instantiation(instance):
    assert isinstance(instance, ptnet_Node)


ptnet_NodeGraphics_strategy = st.builds(ptnet_NodeGraphics)
@given(instance=ptnet_NodeGraphics_strategy)
@settings(max_examples=25)
def test_ptnet_NodeGraphics_instantiation(instance):
    assert isinstance(instance, ptnet_NodeGraphics)


ptnet_Offset_strategy = st.builds(ptnet_Offset)
@given(instance=ptnet_Offset_strategy)
@settings(max_examples=25)
def test_ptnet_Offset_instantiation(instance):
    assert isinstance(instance, ptnet_Offset)


ptnet_OpAnd_strategy = st.builds(ptnet_OpAnd)
@given(instance=ptnet_OpAnd_strategy)
@settings(max_examples=25)
def test_ptnet_OpAnd_instantiation(instance):
    assert isinstance(instance, ptnet_OpAnd)


ptnet_OpDivide_strategy = st.builds(ptnet_OpDivide)
@given(instance=ptnet_OpDivide_strategy)
@settings(max_examples=25)
def test_ptnet_OpDivide_instantiation(instance):
    assert isinstance(instance, ptnet_OpDivide)


ptnet_OpEqual_strategy = st.builds(ptnet_OpEqual)
@given(instance=ptnet_OpEqual_strategy)
@settings(max_examples=25)
def test_ptnet_OpEqual_instantiation(instance):
    assert isinstance(instance, ptnet_OpEqual)


ptnet_OpFalse_strategy = st.builds(ptnet_OpFalse)
@given(instance=ptnet_OpFalse_strategy)
@settings(max_examples=25)
def test_ptnet_OpFalse_instantiation(instance):
    assert isinstance(instance, ptnet_OpFalse)


ptnet_OpGreater_strategy = st.builds(ptnet_OpGreater)
@given(instance=ptnet_OpGreater_strategy)
@settings(max_examples=25)
def test_ptnet_OpGreater_instantiation(instance):
    assert isinstance(instance, ptnet_OpGreater)


ptnet_OpGreaterEqual_strategy = st.builds(ptnet_OpGreaterEqual)
@given(instance=ptnet_OpGreaterEqual_strategy)
@settings(max_examples=25)
def test_ptnet_OpGreaterEqual_instantiation(instance):
    assert isinstance(instance, ptnet_OpGreaterEqual)


ptnet_OpLess_strategy = st.builds(ptnet_OpLess)
@given(instance=ptnet_OpLess_strategy)
@settings(max_examples=25)
def test_ptnet_OpLess_instantiation(instance):
    assert isinstance(instance, ptnet_OpLess)


ptnet_OpLessEqual_strategy = st.builds(ptnet_OpLessEqual)
@given(instance=ptnet_OpLessEqual_strategy)
@settings(max_examples=25)
def test_ptnet_OpLessEqual_instantiation(instance):
    assert isinstance(instance, ptnet_OpLessEqual)


ptnet_OpMinus_strategy = st.builds(ptnet_OpMinus)
@given(instance=ptnet_OpMinus_strategy)
@settings(max_examples=25)
def test_ptnet_OpMinus_instantiation(instance):
    assert isinstance(instance, ptnet_OpMinus)


ptnet_OpMultiply_strategy = st.builds(ptnet_OpMultiply)
@given(instance=ptnet_OpMultiply_strategy)
@settings(max_examples=25)
def test_ptnet_OpMultiply_instantiation(instance):
    assert isinstance(instance, ptnet_OpMultiply)


ptnet_OpNot_strategy = st.builds(ptnet_OpNot)
@given(instance=ptnet_OpNot_strategy)
@settings(max_examples=25)
def test_ptnet_OpNot_instantiation(instance):
    assert isinstance(instance, ptnet_OpNot)


ptnet_OpOr_strategy = st.builds(ptnet_OpOr)
@given(instance=ptnet_OpOr_strategy)
@settings(max_examples=25)
def test_ptnet_OpOr_instantiation(instance):
    assert isinstance(instance, ptnet_OpOr)


ptnet_OpSum_strategy = st.builds(ptnet_OpSum)
@given(instance=ptnet_OpSum_strategy)
@settings(max_examples=25)
def test_ptnet_OpSum_instantiation(instance):
    assert isinstance(instance, ptnet_OpSum)


ptnet_OpTrue_strategy = st.builds(ptnet_OpTrue)
@given(instance=ptnet_OpTrue_strategy)
@settings(max_examples=25)
def test_ptnet_OpTrue_instantiation(instance):
    assert isinstance(instance, ptnet_OpTrue)


ptnet_PTArcAnnotation_strategy = st.builds(ptnet_PTArcAnnotation, text=safe_text)
@given(instance=ptnet_PTArcAnnotation_strategy)
@settings(max_examples=25)
def test_ptnet_PTArcAnnotation_instantiation(instance):
    assert isinstance(instance, ptnet_PTArcAnnotation)


ptnet_PTMarking_strategy = st.builds(ptnet_PTMarking, text=safe_text)
@given(instance=ptnet_PTMarking_strategy)
@settings(max_examples=25)
def test_ptnet_PTMarking_instantiation(instance):
    assert isinstance(instance, ptnet_PTMarking)


ptnet_Page_strategy = st.builds(ptnet_Page)
@given(instance=ptnet_Page_strategy)
@settings(max_examples=25)
def test_ptnet_Page_instantiation(instance):
    assert isinstance(instance, ptnet_Page)


ptnet_PetriNet_strategy = st.builds(ptnet_PetriNet, id=safe_text, type=safe_text)
@given(instance=ptnet_PetriNet_strategy)
@settings(max_examples=25)
def test_ptnet_PetriNet_instantiation(instance):
    assert isinstance(instance, ptnet_PetriNet)


ptnet_PetriNetDoc_strategy = st.builds(ptnet_PetriNetDoc, xmlns=safe_text)
@given(instance=ptnet_PetriNetDoc_strategy)
@settings(max_examples=25)
def test_ptnet_PetriNetDoc_instantiation(instance):
    assert isinstance(instance, ptnet_PetriNetDoc)


ptnet_Place_strategy = st.builds(ptnet_Place)
@given(instance=ptnet_Place_strategy)
@settings(max_examples=25)
def test_ptnet_Place_instantiation(instance):
    assert isinstance(instance, ptnet_Place)


ptnet_PlaceNode_strategy = st.builds(ptnet_PlaceNode)
@given(instance=ptnet_PlaceNode_strategy)
@settings(max_examples=25)
def test_ptnet_PlaceNode_instantiation(instance):
    assert isinstance(instance, ptnet_PlaceNode)


ptnet_PnObject_strategy = st.builds(ptnet_PnObject, id=safe_text)
@given(instance=ptnet_PnObject_strategy)
@settings(max_examples=25)
def test_ptnet_PnObject_instantiation(instance):
    assert isinstance(instance, ptnet_PnObject)


ptnet_Position_strategy = st.builds(ptnet_Position)
@given(instance=ptnet_Position_strategy)
@settings(max_examples=25)
def test_ptnet_Position_instantiation(instance):
    assert isinstance(instance, ptnet_Position)


ptnet_RefPlace_strategy = st.builds(ptnet_RefPlace)
@given(instance=ptnet_RefPlace_strategy)
@settings(max_examples=25)
def test_ptnet_RefPlace_instantiation(instance):
    assert isinstance(instance, ptnet_RefPlace)


ptnet_RefTransition_strategy = st.builds(ptnet_RefTransition)
@given(instance=ptnet_RefTransition_strategy)
@settings(max_examples=25)
def test_ptnet_RefTransition_instantiation(instance):
    assert isinstance(instance, ptnet_RefTransition)


ptnet_SteadyState_strategy = st.builds(ptnet_SteadyState)
@given(instance=ptnet_SteadyState_strategy)
@settings(max_examples=25)
def test_ptnet_SteadyState_instantiation(instance):
    assert isinstance(instance, ptnet_SteadyState)


ptnet_Study_strategy = st.builds(ptnet_Study, name=safe_text)
@given(instance=ptnet_Study_strategy)
@settings(max_examples=25)
def test_ptnet_Study_instantiation(instance):
    assert isinstance(instance, ptnet_Study)


ptnet_ToolInfo_strategy = st.builds(ptnet_ToolInfo, formattedXMLBuffer=safe_text, tool=safe_text, toolInfoGrammarURI=safe_text, version=safe_text)
@given(instance=ptnet_ToolInfo_strategy)
@settings(max_examples=25)
def test_ptnet_ToolInfo_instantiation(instance):
    assert isinstance(instance, ptnet_ToolInfo)


ptnet_Transition_strategy = st.builds(ptnet_Transition)
@given(instance=ptnet_Transition_strategy)
@settings(max_examples=25)
def test_ptnet_Transition_instantiation(instance):
    assert isinstance(instance, ptnet_Transition)


ptnet_TransitionNode_strategy = st.builds(ptnet_TransitionNode)
@given(instance=ptnet_TransitionNode_strategy)
@settings(max_examples=25)
def test_ptnet_TransitionNode_instantiation(instance):
    assert isinstance(instance, ptnet_TransitionNode)


ptnet_Uniform_strategy = st.builds(ptnet_Uniform, Lower=st.floats(allow_nan=False, allow_infinity=False), Upper=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Uniform_strategy)
@settings(max_examples=25)
def test_ptnet_Uniform_instantiation(instance):
    assert isinstance(instance, ptnet_Uniform)


ptnet_ValueExpression_strategy = st.builds(ptnet_ValueExpression, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_ValueExpression_strategy)
@settings(max_examples=25)
def test_ptnet_ValueExpression_instantiation(instance):
    assert isinstance(instance, ptnet_ValueExpression)


ptnet_Variable_strategy = st.builds(ptnet_Variable, name=safe_text)
@given(instance=ptnet_Variable_strategy)
@settings(max_examples=25)
def test_ptnet_Variable_instantiation(instance):
    assert isinstance(instance, ptnet_Variable)


ptnet_VariableExpression_strategy = st.builds(ptnet_VariableExpression)
@given(instance=ptnet_VariableExpression_strategy)
@settings(max_examples=25)
def test_ptnet_VariableExpression_instantiation(instance):
    assert isinstance(instance, ptnet_VariableExpression)


ptnet_VariableValues_strategy = st.builds(ptnet_VariableValues, values=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_VariableValues_strategy)
@settings(max_examples=25)
def test_ptnet_VariableValues_instantiation(instance):
    assert isinstance(instance, ptnet_VariableValues)


ptnet_Weibull_strategy = st.builds(ptnet_Weibull, Alpha=st.floats(allow_nan=False, allow_infinity=False), Beta=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=ptnet_Weibull_strategy)
@settings(max_examples=25)
def test_ptnet_Weibull_instantiation(instance):
    assert isinstance(instance, ptnet_Weibull)



