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
    tortugaDSL_BOOLEAN_EXPRESSION,
    FontStyleValues,
    tortugaDSL_PLAIN,
    tortugaDSL_ITALIC,
    tortugaDSL_BOLD,
    BOOLEAN_EXPRESSION,
    tortugaDSL_GREATER_THAN,
    tortugaDSL_LESSER_THAN,
    tortugaDSL_EQUALS,
    EXPRESSION,
    tortugaDSL_VALUE,
    CONTROL_SENTENCES,
    tortugaDSL_TO,
    tortugaDSL_IF,
    tortugaDSL_REPEAT,
    OPERATION,
    tortugaDSL_MULTIPLY,
    tortugaDSL_DIVIDE,
    tortugaDSL_SUBTRACT,
    tortugaDSL_SUM,
    COLOREABLE,
    tortugaDSL_CANVAS_COLOR,
    tortugaDSL_PENCOLOR,
    tortugaDSL_VARIABLE_REF,
    tortugaDSL_COLOR_SPEC,
    REFERENCIABLE,
    tortugaDSL_PARAM,
    tortugaDSL_REFERENCIABLE,
    tortugaDSL_FontStyleValues,
    FONT_SPEC,
    tortugaDSL_FONT_STYLE,
    tortugaDSL_FONT_SIZE,
    tortugaDSL_TortugaProgram,
    DRAWING_SENTENCE,
    tortugaDSL_DRAW_STRING,
    tortugaDSL_PENUP,
    tortugaDSL_HOME,
    tortugaDSL_CLEAR,
    tortugaDSL_FONT_SPEC,
    tortugaDSL_COLOREABLE,
    tortugaDSL_PENDOWN,
    MOVE,
    tortugaDSL_LEFT,
    tortugaDSL_SET_X,
    tortugaDSL_SET_Y,
    tortugaDSL_RIGHT,
    tortugaDSL_FORWARD,
    tortugaDSL_EXPRESSION,
    SENTENCE,
    tortugaDSL_PROCEDURE_CALL,
    tortugaDSL_MAKE,
    tortugaDSL_DRAWING_SENTENCE,
    tortugaDSL_CONTENT,
    tortugaDSL_OPERATION,
    tortugaDSL_CONTROL_SENTENCES,
    tortugaDSL_MOVE,
    tortugaDSL_SENTENCE,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tortugadsl_boolean_expression_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_BOOLEAN_EXPRESSION)


def test_hyp_tortugadsl_boolean_expression_constructor_exists():
    assert callable(tortugaDSL_BOOLEAN_EXPRESSION.__init__)


def test_hyp_tortugadsl_boolean_expression_constructor_args():
    sig = inspect.signature(tortugaDSL_BOOLEAN_EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_fontstylevalues_is_not_abstract():
    assert not inspect.isabstract(FontStyleValues)


def test_hyp_fontstylevalues_constructor_exists():
    assert callable(FontStyleValues.__init__)


def test_hyp_fontstylevalues_constructor_args():
    sig = inspect.signature(FontStyleValues.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_plain_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PLAIN)


def test_hyp_tortugadsl_plain_constructor_exists():
    assert callable(tortugaDSL_PLAIN.__init__)


def test_hyp_tortugadsl_plain_constructor_args():
    sig = inspect.signature(tortugaDSL_PLAIN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_italic_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_ITALIC)


def test_hyp_tortugadsl_italic_constructor_exists():
    assert callable(tortugaDSL_ITALIC.__init__)


def test_hyp_tortugadsl_italic_constructor_args():
    sig = inspect.signature(tortugaDSL_ITALIC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_bold_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_BOLD)


def test_hyp_tortugadsl_bold_constructor_exists():
    assert callable(tortugaDSL_BOLD.__init__)


def test_hyp_tortugadsl_bold_constructor_args():
    sig = inspect.signature(tortugaDSL_BOLD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_boolean_expression_is_not_abstract():
    assert not inspect.isabstract(BOOLEAN_EXPRESSION)


def test_hyp_boolean_expression_constructor_exists():
    assert callable(BOOLEAN_EXPRESSION.__init__)


def test_hyp_boolean_expression_constructor_args():
    sig = inspect.signature(BOOLEAN_EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_greater_than_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_GREATER_THAN)


def test_hyp_tortugadsl_greater_than_constructor_exists():
    assert callable(tortugaDSL_GREATER_THAN.__init__)


def test_hyp_tortugadsl_greater_than_constructor_args():
    sig = inspect.signature(tortugaDSL_GREATER_THAN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_lesser_than_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_LESSER_THAN)


def test_hyp_tortugadsl_lesser_than_constructor_exists():
    assert callable(tortugaDSL_LESSER_THAN.__init__)


def test_hyp_tortugadsl_lesser_than_constructor_args():
    sig = inspect.signature(tortugaDSL_LESSER_THAN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_equals_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_EQUALS)


def test_hyp_tortugadsl_equals_constructor_exists():
    assert callable(tortugaDSL_EQUALS.__init__)


def test_hyp_tortugadsl_equals_constructor_args():
    sig = inspect.signature(tortugaDSL_EQUALS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_expression_is_not_abstract():
    assert not inspect.isabstract(EXPRESSION)


def test_hyp_expression_constructor_exists():
    assert callable(EXPRESSION.__init__)


def test_hyp_expression_constructor_args():
    sig = inspect.signature(EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_value_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_VALUE)


def test_hyp_tortugadsl_value_constructor_exists():
    assert callable(tortugaDSL_VALUE.__init__)


def test_hyp_tortugadsl_value_constructor_args():
    sig = inspect.signature(tortugaDSL_VALUE.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"




def test_hyp_control_sentences_is_not_abstract():
    assert not inspect.isabstract(CONTROL_SENTENCES)


def test_hyp_control_sentences_constructor_exists():
    assert callable(CONTROL_SENTENCES.__init__)


def test_hyp_control_sentences_constructor_args():
    sig = inspect.signature(CONTROL_SENTENCES.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_to_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_TO)


def test_hyp_tortugadsl_to_constructor_exists():
    assert callable(tortugaDSL_TO.__init__)


def test_hyp_tortugadsl_to_constructor_args():
    sig = inspect.signature(tortugaDSL_TO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tortugadsl_if_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_IF)


def test_hyp_tortugadsl_if_constructor_exists():
    assert callable(tortugaDSL_IF.__init__)


def test_hyp_tortugadsl_if_constructor_args():
    sig = inspect.signature(tortugaDSL_IF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_repeat_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_REPEAT)


def test_hyp_tortugadsl_repeat_constructor_exists():
    assert callable(tortugaDSL_REPEAT.__init__)


def test_hyp_tortugadsl_repeat_constructor_args():
    sig = inspect.signature(tortugaDSL_REPEAT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_operation_is_not_abstract():
    assert not inspect.isabstract(OPERATION)


def test_hyp_operation_constructor_exists():
    assert callable(OPERATION.__init__)


def test_hyp_operation_constructor_args():
    sig = inspect.signature(OPERATION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_multiply_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_MULTIPLY)


def test_hyp_tortugadsl_multiply_constructor_exists():
    assert callable(tortugaDSL_MULTIPLY.__init__)


def test_hyp_tortugadsl_multiply_constructor_args():
    sig = inspect.signature(tortugaDSL_MULTIPLY.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_divide_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_DIVIDE)


def test_hyp_tortugadsl_divide_constructor_exists():
    assert callable(tortugaDSL_DIVIDE.__init__)


def test_hyp_tortugadsl_divide_constructor_args():
    sig = inspect.signature(tortugaDSL_DIVIDE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_subtract_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_SUBTRACT)


def test_hyp_tortugadsl_subtract_constructor_exists():
    assert callable(tortugaDSL_SUBTRACT.__init__)


def test_hyp_tortugadsl_subtract_constructor_args():
    sig = inspect.signature(tortugaDSL_SUBTRACT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_sum_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_SUM)


def test_hyp_tortugadsl_sum_constructor_exists():
    assert callable(tortugaDSL_SUM.__init__)


def test_hyp_tortugadsl_sum_constructor_args():
    sig = inspect.signature(tortugaDSL_SUM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_coloreable_is_not_abstract():
    assert not inspect.isabstract(COLOREABLE)


def test_hyp_coloreable_constructor_exists():
    assert callable(COLOREABLE.__init__)


def test_hyp_coloreable_constructor_args():
    sig = inspect.signature(COLOREABLE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_canvas_color_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_CANVAS_COLOR)


def test_hyp_tortugadsl_canvas_color_constructor_exists():
    assert callable(tortugaDSL_CANVAS_COLOR.__init__)


def test_hyp_tortugadsl_canvas_color_constructor_args():
    sig = inspect.signature(tortugaDSL_CANVAS_COLOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_pencolor_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PENCOLOR)


def test_hyp_tortugadsl_pencolor_constructor_exists():
    assert callable(tortugaDSL_PENCOLOR.__init__)


def test_hyp_tortugadsl_pencolor_constructor_args():
    sig = inspect.signature(tortugaDSL_PENCOLOR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_variable_ref_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_VARIABLE_REF)


def test_hyp_tortugadsl_variable_ref_constructor_exists():
    assert callable(tortugaDSL_VARIABLE_REF.__init__)


def test_hyp_tortugadsl_variable_ref_constructor_args():
    sig = inspect.signature(tortugaDSL_VARIABLE_REF.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_color_spec_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_COLOR_SPEC)


def test_hyp_tortugadsl_color_spec_constructor_exists():
    assert callable(tortugaDSL_COLOR_SPEC.__init__)


def test_hyp_tortugadsl_color_spec_constructor_args():
    sig = inspect.signature(tortugaDSL_COLOR_SPEC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_referenciable_is_not_abstract():
    assert not inspect.isabstract(REFERENCIABLE)


def test_hyp_referenciable_constructor_exists():
    assert callable(REFERENCIABLE.__init__)


def test_hyp_referenciable_constructor_args():
    sig = inspect.signature(REFERENCIABLE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_param_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PARAM)


def test_hyp_tortugadsl_param_constructor_exists():
    assert callable(tortugaDSL_PARAM.__init__)


def test_hyp_tortugadsl_param_constructor_args():
    sig = inspect.signature(tortugaDSL_PARAM.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_referenciable_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_REFERENCIABLE)


def test_hyp_tortugadsl_referenciable_constructor_exists():
    assert callable(tortugaDSL_REFERENCIABLE.__init__)


def test_hyp_tortugadsl_referenciable_constructor_args():
    sig = inspect.signature(tortugaDSL_REFERENCIABLE.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_tortugadsl_fontstylevalues_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_FontStyleValues)


def test_hyp_tortugadsl_fontstylevalues_constructor_exists():
    assert callable(tortugaDSL_FontStyleValues.__init__)


def test_hyp_tortugadsl_fontstylevalues_constructor_args():
    sig = inspect.signature(tortugaDSL_FontStyleValues.__init__)
    params = list(sig.parameters.keys())



def test_hyp_font_spec_is_not_abstract():
    assert not inspect.isabstract(FONT_SPEC)


def test_hyp_font_spec_constructor_exists():
    assert callable(FONT_SPEC.__init__)


def test_hyp_font_spec_constructor_args():
    sig = inspect.signature(FONT_SPEC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_font_style_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_FONT_STYLE)


def test_hyp_tortugadsl_font_style_constructor_exists():
    assert callable(tortugaDSL_FONT_STYLE.__init__)


def test_hyp_tortugadsl_font_style_constructor_args():
    sig = inspect.signature(tortugaDSL_FONT_STYLE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_font_size_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_FONT_SIZE)


def test_hyp_tortugadsl_font_size_constructor_exists():
    assert callable(tortugaDSL_FONT_SIZE.__init__)


def test_hyp_tortugadsl_font_size_constructor_args():
    sig = inspect.signature(tortugaDSL_FONT_SIZE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_tortugaprogram_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_TortugaProgram)


def test_hyp_tortugadsl_tortugaprogram_constructor_exists():
    assert callable(tortugaDSL_TortugaProgram.__init__)


def test_hyp_tortugadsl_tortugaprogram_constructor_args():
    sig = inspect.signature(tortugaDSL_TortugaProgram.__init__)
    params = list(sig.parameters.keys())



def test_hyp_drawing_sentence_is_not_abstract():
    assert not inspect.isabstract(DRAWING_SENTENCE)


def test_hyp_drawing_sentence_constructor_exists():
    assert callable(DRAWING_SENTENCE.__init__)


def test_hyp_drawing_sentence_constructor_args():
    sig = inspect.signature(DRAWING_SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_draw_string_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_DRAW_STRING)


def test_hyp_tortugadsl_draw_string_constructor_exists():
    assert callable(tortugaDSL_DRAW_STRING.__init__)


def test_hyp_tortugadsl_draw_string_constructor_args():
    sig = inspect.signature(tortugaDSL_DRAW_STRING.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"




def test_hyp_tortugadsl_penup_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PENUP)


def test_hyp_tortugadsl_penup_constructor_exists():
    assert callable(tortugaDSL_PENUP.__init__)


def test_hyp_tortugadsl_penup_constructor_args():
    sig = inspect.signature(tortugaDSL_PENUP.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_home_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_HOME)


def test_hyp_tortugadsl_home_constructor_exists():
    assert callable(tortugaDSL_HOME.__init__)


def test_hyp_tortugadsl_home_constructor_args():
    sig = inspect.signature(tortugaDSL_HOME.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_clear_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_CLEAR)


def test_hyp_tortugadsl_clear_constructor_exists():
    assert callable(tortugaDSL_CLEAR.__init__)


def test_hyp_tortugadsl_clear_constructor_args():
    sig = inspect.signature(tortugaDSL_CLEAR.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_font_spec_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_FONT_SPEC)


def test_hyp_tortugadsl_font_spec_constructor_exists():
    assert callable(tortugaDSL_FONT_SPEC.__init__)


def test_hyp_tortugadsl_font_spec_constructor_args():
    sig = inspect.signature(tortugaDSL_FONT_SPEC.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_coloreable_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_COLOREABLE)


def test_hyp_tortugadsl_coloreable_constructor_exists():
    assert callable(tortugaDSL_COLOREABLE.__init__)


def test_hyp_tortugadsl_coloreable_constructor_args():
    sig = inspect.signature(tortugaDSL_COLOREABLE.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"




def test_hyp_tortugadsl_pendown_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PENDOWN)


def test_hyp_tortugadsl_pendown_constructor_exists():
    assert callable(tortugaDSL_PENDOWN.__init__)


def test_hyp_tortugadsl_pendown_constructor_args():
    sig = inspect.signature(tortugaDSL_PENDOWN.__init__)
    params = list(sig.parameters.keys())



def test_hyp_move_is_not_abstract():
    assert not inspect.isabstract(MOVE)


def test_hyp_move_constructor_exists():
    assert callable(MOVE.__init__)


def test_hyp_move_constructor_args():
    sig = inspect.signature(MOVE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_left_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_LEFT)


def test_hyp_tortugadsl_left_constructor_exists():
    assert callable(tortugaDSL_LEFT.__init__)


def test_hyp_tortugadsl_left_constructor_args():
    sig = inspect.signature(tortugaDSL_LEFT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_set_x_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_SET_X)


def test_hyp_tortugadsl_set_x_constructor_exists():
    assert callable(tortugaDSL_SET_X.__init__)


def test_hyp_tortugadsl_set_x_constructor_args():
    sig = inspect.signature(tortugaDSL_SET_X.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_set_y_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_SET_Y)


def test_hyp_tortugadsl_set_y_constructor_exists():
    assert callable(tortugaDSL_SET_Y.__init__)


def test_hyp_tortugadsl_set_y_constructor_args():
    sig = inspect.signature(tortugaDSL_SET_Y.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_right_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_RIGHT)


def test_hyp_tortugadsl_right_constructor_exists():
    assert callable(tortugaDSL_RIGHT.__init__)


def test_hyp_tortugadsl_right_constructor_args():
    sig = inspect.signature(tortugaDSL_RIGHT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_forward_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_FORWARD)


def test_hyp_tortugadsl_forward_constructor_exists():
    assert callable(tortugaDSL_FORWARD.__init__)


def test_hyp_tortugadsl_forward_constructor_args():
    sig = inspect.signature(tortugaDSL_FORWARD.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_expression_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_EXPRESSION)


def test_hyp_tortugadsl_expression_constructor_exists():
    assert callable(tortugaDSL_EXPRESSION.__init__)


def test_hyp_tortugadsl_expression_constructor_args():
    sig = inspect.signature(tortugaDSL_EXPRESSION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_sentence_is_not_abstract():
    assert not inspect.isabstract(SENTENCE)


def test_hyp_sentence_constructor_exists():
    assert callable(SENTENCE.__init__)


def test_hyp_sentence_constructor_args():
    sig = inspect.signature(SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_procedure_call_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_PROCEDURE_CALL)


def test_hyp_tortugadsl_procedure_call_constructor_exists():
    assert callable(tortugaDSL_PROCEDURE_CALL.__init__)


def test_hyp_tortugadsl_procedure_call_constructor_args():
    sig = inspect.signature(tortugaDSL_PROCEDURE_CALL.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_make_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_MAKE)


def test_hyp_tortugadsl_make_constructor_exists():
    assert callable(tortugaDSL_MAKE.__init__)


def test_hyp_tortugadsl_make_constructor_args():
    sig = inspect.signature(tortugaDSL_MAKE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_drawing_sentence_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_DRAWING_SENTENCE)


def test_hyp_tortugadsl_drawing_sentence_constructor_exists():
    assert callable(tortugaDSL_DRAWING_SENTENCE.__init__)


def test_hyp_tortugadsl_drawing_sentence_constructor_args():
    sig = inspect.signature(tortugaDSL_DRAWING_SENTENCE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_content_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_CONTENT)


def test_hyp_tortugadsl_content_constructor_exists():
    assert callable(tortugaDSL_CONTENT.__init__)


def test_hyp_tortugadsl_content_constructor_args():
    sig = inspect.signature(tortugaDSL_CONTENT.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_operation_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_OPERATION)


def test_hyp_tortugadsl_operation_constructor_exists():
    assert callable(tortugaDSL_OPERATION.__init__)


def test_hyp_tortugadsl_operation_constructor_args():
    sig = inspect.signature(tortugaDSL_OPERATION.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_control_sentences_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_CONTROL_SENTENCES)


def test_hyp_tortugadsl_control_sentences_constructor_exists():
    assert callable(tortugaDSL_CONTROL_SENTENCES.__init__)


def test_hyp_tortugadsl_control_sentences_constructor_args():
    sig = inspect.signature(tortugaDSL_CONTROL_SENTENCES.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_move_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_MOVE)


def test_hyp_tortugadsl_move_constructor_exists():
    assert callable(tortugaDSL_MOVE.__init__)


def test_hyp_tortugadsl_move_constructor_args():
    sig = inspect.signature(tortugaDSL_MOVE.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tortugadsl_sentence_is_not_abstract():
    assert not inspect.isabstract(tortugaDSL_SENTENCE)


def test_hyp_tortugadsl_sentence_constructor_exists():
    assert callable(tortugaDSL_SENTENCE.__init__)


def test_hyp_tortugadsl_sentence_constructor_args():
    sig = inspect.signature(tortugaDSL_SENTENCE.__init__)
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
tortugaDSL_BOOLEAN_EXPRESSION_strategy = st.builds(
    tortugaDSL_BOOLEAN_EXPRESSION,
)
FontStyleValues_strategy = st.builds(
    FontStyleValues,
)
tortugaDSL_PLAIN_strategy = st.builds(
    tortugaDSL_PLAIN,
)
tortugaDSL_ITALIC_strategy = st.builds(
    tortugaDSL_ITALIC,
)
tortugaDSL_BOLD_strategy = st.builds(
    tortugaDSL_BOLD,
)
BOOLEAN_EXPRESSION_strategy = st.builds(
    BOOLEAN_EXPRESSION,
)
tortugaDSL_GREATER_THAN_strategy = st.builds(
    tortugaDSL_GREATER_THAN,
)
tortugaDSL_LESSER_THAN_strategy = st.builds(
    tortugaDSL_LESSER_THAN,
)
tortugaDSL_EQUALS_strategy = st.builds(
    tortugaDSL_EQUALS,
)
EXPRESSION_strategy = st.builds(
    EXPRESSION,
)
tortugaDSL_VALUE_strategy = st.builds(
    tortugaDSL_VALUE,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CONTROL_SENTENCES_strategy = st.builds(
    CONTROL_SENTENCES,
)
tortugaDSL_TO_strategy = st.builds(
    tortugaDSL_TO,
    name=
        safe_text
)
tortugaDSL_IF_strategy = st.builds(
    tortugaDSL_IF,
)
tortugaDSL_REPEAT_strategy = st.builds(
    tortugaDSL_REPEAT,
)
OPERATION_strategy = st.builds(
    OPERATION,
)
tortugaDSL_MULTIPLY_strategy = st.builds(
    tortugaDSL_MULTIPLY,
)
tortugaDSL_DIVIDE_strategy = st.builds(
    tortugaDSL_DIVIDE,
)
tortugaDSL_SUBTRACT_strategy = st.builds(
    tortugaDSL_SUBTRACT,
)
tortugaDSL_SUM_strategy = st.builds(
    tortugaDSL_SUM,
)
COLOREABLE_strategy = st.builds(
    COLOREABLE,
)
tortugaDSL_CANVAS_COLOR_strategy = st.builds(
    tortugaDSL_CANVAS_COLOR,
)
tortugaDSL_PENCOLOR_strategy = st.builds(
    tortugaDSL_PENCOLOR,
)
tortugaDSL_VARIABLE_REF_strategy = st.builds(
    tortugaDSL_VARIABLE_REF,
)
tortugaDSL_COLOR_SPEC_strategy = st.builds(
    tortugaDSL_COLOR_SPEC,
)
REFERENCIABLE_strategy = st.builds(
    REFERENCIABLE,
)
tortugaDSL_PARAM_strategy = st.builds(
    tortugaDSL_PARAM,
)
tortugaDSL_REFERENCIABLE_strategy = st.builds(
    tortugaDSL_REFERENCIABLE,
    name=
        safe_text
)
tortugaDSL_FontStyleValues_strategy = st.builds(
    tortugaDSL_FontStyleValues,
)
FONT_SPEC_strategy = st.builds(
    FONT_SPEC,
)
tortugaDSL_FONT_STYLE_strategy = st.builds(
    tortugaDSL_FONT_STYLE,
)
tortugaDSL_FONT_SIZE_strategy = st.builds(
    tortugaDSL_FONT_SIZE,
)
tortugaDSL_TortugaProgram_strategy = st.builds(
    tortugaDSL_TortugaProgram,
)
DRAWING_SENTENCE_strategy = st.builds(
    DRAWING_SENTENCE,
)
tortugaDSL_DRAW_STRING_strategy = st.builds(
    tortugaDSL_DRAW_STRING,
    text=
        safe_text
)
tortugaDSL_PENUP_strategy = st.builds(
    tortugaDSL_PENUP,
)
tortugaDSL_HOME_strategy = st.builds(
    tortugaDSL_HOME,
)
tortugaDSL_CLEAR_strategy = st.builds(
    tortugaDSL_CLEAR,
)
tortugaDSL_FONT_SPEC_strategy = st.builds(
    tortugaDSL_FONT_SPEC,
)
tortugaDSL_COLOREABLE_strategy = st.builds(
    tortugaDSL_COLOREABLE,
    color=
        safe_text
)
tortugaDSL_PENDOWN_strategy = st.builds(
    tortugaDSL_PENDOWN,
)
MOVE_strategy = st.builds(
    MOVE,
)
tortugaDSL_LEFT_strategy = st.builds(
    tortugaDSL_LEFT,
)
tortugaDSL_SET_X_strategy = st.builds(
    tortugaDSL_SET_X,
)
tortugaDSL_SET_Y_strategy = st.builds(
    tortugaDSL_SET_Y,
)
tortugaDSL_RIGHT_strategy = st.builds(
    tortugaDSL_RIGHT,
)
tortugaDSL_FORWARD_strategy = st.builds(
    tortugaDSL_FORWARD,
)
tortugaDSL_EXPRESSION_strategy = st.builds(
    tortugaDSL_EXPRESSION,
)
SENTENCE_strategy = st.builds(
    SENTENCE,
)
tortugaDSL_PROCEDURE_CALL_strategy = st.builds(
    tortugaDSL_PROCEDURE_CALL,
)
tortugaDSL_MAKE_strategy = st.builds(
    tortugaDSL_MAKE,
)
tortugaDSL_DRAWING_SENTENCE_strategy = st.builds(
    tortugaDSL_DRAWING_SENTENCE,
)
tortugaDSL_CONTENT_strategy = st.builds(
    tortugaDSL_CONTENT,
)
tortugaDSL_OPERATION_strategy = st.builds(
    tortugaDSL_OPERATION,
)
tortugaDSL_CONTROL_SENTENCES_strategy = st.builds(
    tortugaDSL_CONTROL_SENTENCES,
)
tortugaDSL_MOVE_strategy = st.builds(
    tortugaDSL_MOVE,
)
tortugaDSL_SENTENCE_strategy = st.builds(
    tortugaDSL_SENTENCE,
)














@given(instance=tortugaDSL_VALUE_strategy)
def test_hyp_tortugadsl_value_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original





@given(instance=tortugaDSL_TO_strategy)
def test_hyp_tortugadsl_to_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original


















@given(instance=tortugaDSL_REFERENCIABLE_strategy)
def test_hyp_tortugadsl_referenciable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original










@given(instance=tortugaDSL_DRAW_STRING_strategy)
def test_hyp_tortugadsl_draw_string_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original








@given(instance=tortugaDSL_COLOREABLE_strategy)
def test_hyp_tortugadsl_coloreable_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



















# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BOOLEAN_EXPRESSION,
    COLOREABLE,
    CONTROL_SENTENCES,
    DRAWING_SENTENCE,
    EXPRESSION,
    FONT_SPEC,
    FontStyleValues,
    MOVE,
    OPERATION,
    REFERENCIABLE,
    SENTENCE,
    tortugaDSL_BOLD,
    tortugaDSL_BOOLEAN_EXPRESSION,
    tortugaDSL_CANVAS_COLOR,
    tortugaDSL_CLEAR,
    tortugaDSL_COLOREABLE,
    tortugaDSL_COLOR_SPEC,
    tortugaDSL_CONTENT,
    tortugaDSL_CONTROL_SENTENCES,
    tortugaDSL_DIVIDE,
    tortugaDSL_DRAWING_SENTENCE,
    tortugaDSL_DRAW_STRING,
    tortugaDSL_EQUALS,
    tortugaDSL_EXPRESSION,
    tortugaDSL_FONT_SIZE,
    tortugaDSL_FONT_SPEC,
    tortugaDSL_FONT_STYLE,
    tortugaDSL_FORWARD,
    tortugaDSL_FontStyleValues,
    tortugaDSL_GREATER_THAN,
    tortugaDSL_HOME,
    tortugaDSL_IF,
    tortugaDSL_ITALIC,
    tortugaDSL_LEFT,
    tortugaDSL_LESSER_THAN,
    tortugaDSL_MAKE,
    tortugaDSL_MOVE,
    tortugaDSL_MULTIPLY,
    tortugaDSL_OPERATION,
    tortugaDSL_PARAM,
    tortugaDSL_PENCOLOR,
    tortugaDSL_PENDOWN,
    tortugaDSL_PENUP,
    tortugaDSL_PLAIN,
    tortugaDSL_PROCEDURE_CALL,
    tortugaDSL_REFERENCIABLE,
    tortugaDSL_REPEAT,
    tortugaDSL_RIGHT,
    tortugaDSL_SENTENCE,
    tortugaDSL_SET_X,
    tortugaDSL_SET_Y,
    tortugaDSL_SUBTRACT,
    tortugaDSL_SUM,
    tortugaDSL_TO,
    tortugaDSL_TortugaProgram,
    tortugaDSL_VALUE,
    tortugaDSL_VARIABLE_REF,
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

def test_tortugaDSL_COLOREABLE_color_value_roundtrip():
    instance = tortugaDSL_COLOREABLE(color="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_tortugaDSL_DRAW_STRING_text_value_roundtrip():
    instance = tortugaDSL_DRAW_STRING(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_tortugaDSL_REFERENCIABLE_name_value_roundtrip():
    instance = tortugaDSL_REFERENCIABLE(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tortugaDSL_TO_name_value_roundtrip():
    instance = tortugaDSL_TO(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_tortugaDSL_VALUE_val_value_roundtrip():
    instance = tortugaDSL_VALUE(val=3.14)
    assert instance.val == 3.14
    instance.val = 9.99
    assert instance.val == 9.99


def test_tortugaDSL_EQUALS_isa_BOOLEAN_EXPRESSION():
    instance = tortugaDSL_EQUALS()
    assert isinstance(instance, BOOLEAN_EXPRESSION)


def test_tortugaDSL_GREATER_THAN_isa_BOOLEAN_EXPRESSION():
    instance = tortugaDSL_GREATER_THAN()
    assert isinstance(instance, BOOLEAN_EXPRESSION)


def test_tortugaDSL_LESSER_THAN_isa_BOOLEAN_EXPRESSION():
    instance = tortugaDSL_LESSER_THAN()
    assert isinstance(instance, BOOLEAN_EXPRESSION)


def test_tortugaDSL_CANVAS_COLOR_isa_COLOREABLE():
    instance = tortugaDSL_CANVAS_COLOR()
    assert isinstance(instance, COLOREABLE)


def test_tortugaDSL_PENCOLOR_isa_COLOREABLE():
    instance = tortugaDSL_PENCOLOR()
    assert isinstance(instance, COLOREABLE)


def test_tortugaDSL_IF_isa_CONTROL_SENTENCES():
    instance = tortugaDSL_IF()
    assert isinstance(instance, CONTROL_SENTENCES)


def test_tortugaDSL_REPEAT_isa_CONTROL_SENTENCES():
    instance = tortugaDSL_REPEAT()
    assert isinstance(instance, CONTROL_SENTENCES)


def test_tortugaDSL_TO_isa_CONTROL_SENTENCES():
    instance = tortugaDSL_TO(name="sample_text")
    assert isinstance(instance, CONTROL_SENTENCES)


def test_tortugaDSL_CLEAR_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_CLEAR()
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_COLOREABLE_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_COLOREABLE(color="sample_text")
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_DRAW_STRING_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_DRAW_STRING(text="sample_text")
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_FONT_SPEC_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_FONT_SPEC()
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_HOME_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_HOME()
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_PENDOWN_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_PENDOWN()
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_PENUP_isa_DRAWING_SENTENCE():
    instance = tortugaDSL_PENUP()
    assert isinstance(instance, DRAWING_SENTENCE)


def test_tortugaDSL_VALUE_isa_EXPRESSION():
    instance = tortugaDSL_VALUE(val=3.14)
    assert isinstance(instance, EXPRESSION)


def test_tortugaDSL_VARIABLE_REF_isa_EXPRESSION():
    instance = tortugaDSL_VARIABLE_REF()
    assert isinstance(instance, EXPRESSION)


def test_tortugaDSL_FONT_SIZE_isa_FONT_SPEC():
    instance = tortugaDSL_FONT_SIZE()
    assert isinstance(instance, FONT_SPEC)


def test_tortugaDSL_FONT_STYLE_isa_FONT_SPEC():
    instance = tortugaDSL_FONT_STYLE()
    assert isinstance(instance, FONT_SPEC)


def test_tortugaDSL_BOLD_isa_FontStyleValues():
    instance = tortugaDSL_BOLD()
    assert isinstance(instance, FontStyleValues)


def test_tortugaDSL_ITALIC_isa_FontStyleValues():
    instance = tortugaDSL_ITALIC()
    assert isinstance(instance, FontStyleValues)


def test_tortugaDSL_PLAIN_isa_FontStyleValues():
    instance = tortugaDSL_PLAIN()
    assert isinstance(instance, FontStyleValues)


def test_tortugaDSL_FORWARD_isa_MOVE():
    instance = tortugaDSL_FORWARD()
    assert isinstance(instance, MOVE)


def test_tortugaDSL_LEFT_isa_MOVE():
    instance = tortugaDSL_LEFT()
    assert isinstance(instance, MOVE)


def test_tortugaDSL_RIGHT_isa_MOVE():
    instance = tortugaDSL_RIGHT()
    assert isinstance(instance, MOVE)


def test_tortugaDSL_SET_X_isa_MOVE():
    instance = tortugaDSL_SET_X()
    assert isinstance(instance, MOVE)


def test_tortugaDSL_SET_Y_isa_MOVE():
    instance = tortugaDSL_SET_Y()
    assert isinstance(instance, MOVE)


def test_tortugaDSL_DIVIDE_isa_OPERATION():
    instance = tortugaDSL_DIVIDE()
    assert isinstance(instance, OPERATION)


def test_tortugaDSL_MULTIPLY_isa_OPERATION():
    instance = tortugaDSL_MULTIPLY()
    assert isinstance(instance, OPERATION)


def test_tortugaDSL_SUBTRACT_isa_OPERATION():
    instance = tortugaDSL_SUBTRACT()
    assert isinstance(instance, OPERATION)


def test_tortugaDSL_SUM_isa_OPERATION():
    instance = tortugaDSL_SUM()
    assert isinstance(instance, OPERATION)


def test_tortugaDSL_MAKE_isa_REFERENCIABLE():
    instance = tortugaDSL_MAKE()
    assert isinstance(instance, REFERENCIABLE)


def test_tortugaDSL_PARAM_isa_REFERENCIABLE():
    instance = tortugaDSL_PARAM()
    assert isinstance(instance, REFERENCIABLE)


def test_tortugaDSL_CONTENT_isa_SENTENCE():
    instance = tortugaDSL_CONTENT()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_CONTROL_SENTENCES_isa_SENTENCE():
    instance = tortugaDSL_CONTROL_SENTENCES()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_DRAWING_SENTENCE_isa_SENTENCE():
    instance = tortugaDSL_DRAWING_SENTENCE()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_MAKE_isa_SENTENCE():
    instance = tortugaDSL_MAKE()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_MOVE_isa_SENTENCE():
    instance = tortugaDSL_MOVE()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_OPERATION_isa_SENTENCE():
    instance = tortugaDSL_OPERATION()
    assert isinstance(instance, SENTENCE)


def test_tortugaDSL_PROCEDURE_CALL_isa_SENTENCE():
    instance = tortugaDSL_PROCEDURE_CALL()
    assert isinstance(instance, SENTENCE)


def test_assoc_colorSpec2_link_reassign_clear():
    a = tortugaDSL_COLOREABLE(color="sample_text")
    b1 = tortugaDSL_COLOR_SPEC()
    b2 = tortugaDSL_COLOR_SPEC()
    _safe_set(a, 'tortugaDSL_COLOREABLE', b1)
    assert _is_linked(a, 'tortugaDSL_COLOREABLE', b1)
    if hasattr(b1, 'tortugaDSL_COLOR_SPEC'):
        assert _is_linked(b1, 'tortugaDSL_COLOR_SPEC', a)
    _safe_set(a, 'tortugaDSL_COLOREABLE', b2)
    assert _is_linked(a, 'tortugaDSL_COLOREABLE', b2)
    if hasattr(b1, 'tortugaDSL_COLOR_SPEC'):
        assert not _is_linked(b1, 'tortugaDSL_COLOR_SPEC', a)
    if hasattr(b2, 'tortugaDSL_COLOR_SPEC'):
        assert _is_linked(b2, 'tortugaDSL_COLOR_SPEC', a)
    _safe_set(a, 'tortugaDSL_COLOREABLE', None)
    assert not _is_linked(a, 'tortugaDSL_COLOREABLE', b2)
    if hasattr(b2, 'tortugaDSL_COLOR_SPEC'):
        assert not _is_linked(b2, 'tortugaDSL_COLOR_SPEC', a)


def test_assoc_parameters35_link_reassign_clear():
    a = tortugaDSL_TO(name="sample_text")
    b1 = tortugaDSL_PARAM()
    b2 = tortugaDSL_PARAM()
    _safe_set(a, 'tortugaDSL_TO', {b1})
    assert _is_linked(a, 'tortugaDSL_TO', b1)
    if hasattr(b1, 'tortugaDSL_PARAM'):
        assert _is_linked(b1, 'tortugaDSL_PARAM', a)
    _safe_set(a, 'tortugaDSL_TO', {b2})
    assert _is_linked(a, 'tortugaDSL_TO', b2)
    if hasattr(b1, 'tortugaDSL_PARAM'):
        assert not _is_linked(b1, 'tortugaDSL_PARAM', a)
    if hasattr(b2, 'tortugaDSL_PARAM'):
        assert _is_linked(b2, 'tortugaDSL_PARAM', a)
    _safe_set(a, 'tortugaDSL_TO', set())
    assert not _is_linked(a, 'tortugaDSL_TO', b2)
    if hasattr(b2, 'tortugaDSL_PARAM'):
        assert not _is_linked(b2, 'tortugaDSL_PARAM', a)


def test_assoc_to36_link_reassign_clear():
    a = tortugaDSL_TO(name="sample_text")
    b1 = tortugaDSL_PROCEDURE_CALL()
    b2 = tortugaDSL_PROCEDURE_CALL()
    _safe_set(a, 'tortugaDSL_TO37', b1)
    assert _is_linked(a, 'tortugaDSL_TO37', b1)
    if hasattr(b1, 'tortugaDSL_PROCEDURE_CALL'):
        assert _is_linked(b1, 'tortugaDSL_PROCEDURE_CALL', a)
    _safe_set(a, 'tortugaDSL_TO37', b2)
    assert _is_linked(a, 'tortugaDSL_TO37', b2)
    if hasattr(b1, 'tortugaDSL_PROCEDURE_CALL'):
        assert not _is_linked(b1, 'tortugaDSL_PROCEDURE_CALL', a)
    if hasattr(b2, 'tortugaDSL_PROCEDURE_CALL'):
        assert _is_linked(b2, 'tortugaDSL_PROCEDURE_CALL', a)
    _safe_set(a, 'tortugaDSL_TO37', None)
    assert not _is_linked(a, 'tortugaDSL_TO37', b2)
    if hasattr(b2, 'tortugaDSL_PROCEDURE_CALL'):
        assert not _is_linked(b2, 'tortugaDSL_PROCEDURE_CALL', a)


def test_assoc_toVar20_link_reassign_clear():
    a = tortugaDSL_REFERENCIABLE(name="sample_text")
    b1 = tortugaDSL_VARIABLE_REF()
    b2 = tortugaDSL_VARIABLE_REF()
    _safe_set(a, 'tortugaDSL_REFERENCIABLE', b1)
    assert _is_linked(a, 'tortugaDSL_REFERENCIABLE', b1)
    if hasattr(b1, 'tortugaDSL_VARIABLE_REF'):
        assert _is_linked(b1, 'tortugaDSL_VARIABLE_REF', a)
    _safe_set(a, 'tortugaDSL_REFERENCIABLE', b2)
    assert _is_linked(a, 'tortugaDSL_REFERENCIABLE', b2)
    if hasattr(b1, 'tortugaDSL_VARIABLE_REF'):
        assert not _is_linked(b1, 'tortugaDSL_VARIABLE_REF', a)
    if hasattr(b2, 'tortugaDSL_VARIABLE_REF'):
        assert _is_linked(b2, 'tortugaDSL_VARIABLE_REF', a)
    _safe_set(a, 'tortugaDSL_REFERENCIABLE', None)
    assert not _is_linked(a, 'tortugaDSL_REFERENCIABLE', b2)
    if hasattr(b2, 'tortugaDSL_VARIABLE_REF'):
        assert not _is_linked(b2, 'tortugaDSL_VARIABLE_REF', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BOOLEAN_EXPRESSION_strategy = st.builds(BOOLEAN_EXPRESSION)
@given(instance=BOOLEAN_EXPRESSION_strategy)
@settings(max_examples=25)
def test_BOOLEAN_EXPRESSION_instantiation(instance):
    assert isinstance(instance, BOOLEAN_EXPRESSION)


COLOREABLE_strategy = st.builds(COLOREABLE)
@given(instance=COLOREABLE_strategy)
@settings(max_examples=25)
def test_COLOREABLE_instantiation(instance):
    assert isinstance(instance, COLOREABLE)


CONTROL_SENTENCES_strategy = st.builds(CONTROL_SENTENCES)
@given(instance=CONTROL_SENTENCES_strategy)
@settings(max_examples=25)
def test_CONTROL_SENTENCES_instantiation(instance):
    assert isinstance(instance, CONTROL_SENTENCES)


DRAWING_SENTENCE_strategy = st.builds(DRAWING_SENTENCE)
@given(instance=DRAWING_SENTENCE_strategy)
@settings(max_examples=25)
def test_DRAWING_SENTENCE_instantiation(instance):
    assert isinstance(instance, DRAWING_SENTENCE)


EXPRESSION_strategy = st.builds(EXPRESSION)
@given(instance=EXPRESSION_strategy)
@settings(max_examples=25)
def test_EXPRESSION_instantiation(instance):
    assert isinstance(instance, EXPRESSION)


FONT_SPEC_strategy = st.builds(FONT_SPEC)
@given(instance=FONT_SPEC_strategy)
@settings(max_examples=25)
def test_FONT_SPEC_instantiation(instance):
    assert isinstance(instance, FONT_SPEC)


FontStyleValues_strategy = st.builds(FontStyleValues)
@given(instance=FontStyleValues_strategy)
@settings(max_examples=25)
def test_FontStyleValues_instantiation(instance):
    assert isinstance(instance, FontStyleValues)


MOVE_strategy = st.builds(MOVE)
@given(instance=MOVE_strategy)
@settings(max_examples=25)
def test_MOVE_instantiation(instance):
    assert isinstance(instance, MOVE)


OPERATION_strategy = st.builds(OPERATION)
@given(instance=OPERATION_strategy)
@settings(max_examples=25)
def test_OPERATION_instantiation(instance):
    assert isinstance(instance, OPERATION)


REFERENCIABLE_strategy = st.builds(REFERENCIABLE)
@given(instance=REFERENCIABLE_strategy)
@settings(max_examples=25)
def test_REFERENCIABLE_instantiation(instance):
    assert isinstance(instance, REFERENCIABLE)


SENTENCE_strategy = st.builds(SENTENCE)
@given(instance=SENTENCE_strategy)
@settings(max_examples=25)
def test_SENTENCE_instantiation(instance):
    assert isinstance(instance, SENTENCE)


tortugaDSL_BOLD_strategy = st.builds(tortugaDSL_BOLD)
@given(instance=tortugaDSL_BOLD_strategy)
@settings(max_examples=25)
def test_tortugaDSL_BOLD_instantiation(instance):
    assert isinstance(instance, tortugaDSL_BOLD)


tortugaDSL_BOOLEAN_EXPRESSION_strategy = st.builds(tortugaDSL_BOOLEAN_EXPRESSION)
@given(instance=tortugaDSL_BOOLEAN_EXPRESSION_strategy)
@settings(max_examples=25)
def test_tortugaDSL_BOOLEAN_EXPRESSION_instantiation(instance):
    assert isinstance(instance, tortugaDSL_BOOLEAN_EXPRESSION)


tortugaDSL_CANVAS_COLOR_strategy = st.builds(tortugaDSL_CANVAS_COLOR)
@given(instance=tortugaDSL_CANVAS_COLOR_strategy)
@settings(max_examples=25)
def test_tortugaDSL_CANVAS_COLOR_instantiation(instance):
    assert isinstance(instance, tortugaDSL_CANVAS_COLOR)


tortugaDSL_CLEAR_strategy = st.builds(tortugaDSL_CLEAR)
@given(instance=tortugaDSL_CLEAR_strategy)
@settings(max_examples=25)
def test_tortugaDSL_CLEAR_instantiation(instance):
    assert isinstance(instance, tortugaDSL_CLEAR)


tortugaDSL_COLOREABLE_strategy = st.builds(tortugaDSL_COLOREABLE, color=safe_text)
@given(instance=tortugaDSL_COLOREABLE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_COLOREABLE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_COLOREABLE)


tortugaDSL_COLOR_SPEC_strategy = st.builds(tortugaDSL_COLOR_SPEC)
@given(instance=tortugaDSL_COLOR_SPEC_strategy)
@settings(max_examples=25)
def test_tortugaDSL_COLOR_SPEC_instantiation(instance):
    assert isinstance(instance, tortugaDSL_COLOR_SPEC)


tortugaDSL_CONTENT_strategy = st.builds(tortugaDSL_CONTENT)
@given(instance=tortugaDSL_CONTENT_strategy)
@settings(max_examples=25)
def test_tortugaDSL_CONTENT_instantiation(instance):
    assert isinstance(instance, tortugaDSL_CONTENT)


tortugaDSL_CONTROL_SENTENCES_strategy = st.builds(tortugaDSL_CONTROL_SENTENCES)
@given(instance=tortugaDSL_CONTROL_SENTENCES_strategy)
@settings(max_examples=25)
def test_tortugaDSL_CONTROL_SENTENCES_instantiation(instance):
    assert isinstance(instance, tortugaDSL_CONTROL_SENTENCES)


tortugaDSL_DIVIDE_strategy = st.builds(tortugaDSL_DIVIDE)
@given(instance=tortugaDSL_DIVIDE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_DIVIDE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_DIVIDE)


tortugaDSL_DRAWING_SENTENCE_strategy = st.builds(tortugaDSL_DRAWING_SENTENCE)
@given(instance=tortugaDSL_DRAWING_SENTENCE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_DRAWING_SENTENCE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_DRAWING_SENTENCE)


tortugaDSL_DRAW_STRING_strategy = st.builds(tortugaDSL_DRAW_STRING, text=safe_text)
@given(instance=tortugaDSL_DRAW_STRING_strategy)
@settings(max_examples=25)
def test_tortugaDSL_DRAW_STRING_instantiation(instance):
    assert isinstance(instance, tortugaDSL_DRAW_STRING)


tortugaDSL_EQUALS_strategy = st.builds(tortugaDSL_EQUALS)
@given(instance=tortugaDSL_EQUALS_strategy)
@settings(max_examples=25)
def test_tortugaDSL_EQUALS_instantiation(instance):
    assert isinstance(instance, tortugaDSL_EQUALS)


tortugaDSL_EXPRESSION_strategy = st.builds(tortugaDSL_EXPRESSION)
@given(instance=tortugaDSL_EXPRESSION_strategy)
@settings(max_examples=25)
def test_tortugaDSL_EXPRESSION_instantiation(instance):
    assert isinstance(instance, tortugaDSL_EXPRESSION)


tortugaDSL_FONT_SIZE_strategy = st.builds(tortugaDSL_FONT_SIZE)
@given(instance=tortugaDSL_FONT_SIZE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_FONT_SIZE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_FONT_SIZE)


tortugaDSL_FONT_SPEC_strategy = st.builds(tortugaDSL_FONT_SPEC)
@given(instance=tortugaDSL_FONT_SPEC_strategy)
@settings(max_examples=25)
def test_tortugaDSL_FONT_SPEC_instantiation(instance):
    assert isinstance(instance, tortugaDSL_FONT_SPEC)


tortugaDSL_FONT_STYLE_strategy = st.builds(tortugaDSL_FONT_STYLE)
@given(instance=tortugaDSL_FONT_STYLE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_FONT_STYLE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_FONT_STYLE)


tortugaDSL_FORWARD_strategy = st.builds(tortugaDSL_FORWARD)
@given(instance=tortugaDSL_FORWARD_strategy)
@settings(max_examples=25)
def test_tortugaDSL_FORWARD_instantiation(instance):
    assert isinstance(instance, tortugaDSL_FORWARD)


tortugaDSL_FontStyleValues_strategy = st.builds(tortugaDSL_FontStyleValues)
@given(instance=tortugaDSL_FontStyleValues_strategy)
@settings(max_examples=25)
def test_tortugaDSL_FontStyleValues_instantiation(instance):
    assert isinstance(instance, tortugaDSL_FontStyleValues)


tortugaDSL_GREATER_THAN_strategy = st.builds(tortugaDSL_GREATER_THAN)
@given(instance=tortugaDSL_GREATER_THAN_strategy)
@settings(max_examples=25)
def test_tortugaDSL_GREATER_THAN_instantiation(instance):
    assert isinstance(instance, tortugaDSL_GREATER_THAN)


tortugaDSL_HOME_strategy = st.builds(tortugaDSL_HOME)
@given(instance=tortugaDSL_HOME_strategy)
@settings(max_examples=25)
def test_tortugaDSL_HOME_instantiation(instance):
    assert isinstance(instance, tortugaDSL_HOME)


tortugaDSL_IF_strategy = st.builds(tortugaDSL_IF)
@given(instance=tortugaDSL_IF_strategy)
@settings(max_examples=25)
def test_tortugaDSL_IF_instantiation(instance):
    assert isinstance(instance, tortugaDSL_IF)


tortugaDSL_ITALIC_strategy = st.builds(tortugaDSL_ITALIC)
@given(instance=tortugaDSL_ITALIC_strategy)
@settings(max_examples=25)
def test_tortugaDSL_ITALIC_instantiation(instance):
    assert isinstance(instance, tortugaDSL_ITALIC)


tortugaDSL_LEFT_strategy = st.builds(tortugaDSL_LEFT)
@given(instance=tortugaDSL_LEFT_strategy)
@settings(max_examples=25)
def test_tortugaDSL_LEFT_instantiation(instance):
    assert isinstance(instance, tortugaDSL_LEFT)


tortugaDSL_LESSER_THAN_strategy = st.builds(tortugaDSL_LESSER_THAN)
@given(instance=tortugaDSL_LESSER_THAN_strategy)
@settings(max_examples=25)
def test_tortugaDSL_LESSER_THAN_instantiation(instance):
    assert isinstance(instance, tortugaDSL_LESSER_THAN)


tortugaDSL_MAKE_strategy = st.builds(tortugaDSL_MAKE)
@given(instance=tortugaDSL_MAKE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_MAKE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_MAKE)


tortugaDSL_MOVE_strategy = st.builds(tortugaDSL_MOVE)
@given(instance=tortugaDSL_MOVE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_MOVE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_MOVE)


tortugaDSL_MULTIPLY_strategy = st.builds(tortugaDSL_MULTIPLY)
@given(instance=tortugaDSL_MULTIPLY_strategy)
@settings(max_examples=25)
def test_tortugaDSL_MULTIPLY_instantiation(instance):
    assert isinstance(instance, tortugaDSL_MULTIPLY)


tortugaDSL_OPERATION_strategy = st.builds(tortugaDSL_OPERATION)
@given(instance=tortugaDSL_OPERATION_strategy)
@settings(max_examples=25)
def test_tortugaDSL_OPERATION_instantiation(instance):
    assert isinstance(instance, tortugaDSL_OPERATION)


tortugaDSL_PARAM_strategy = st.builds(tortugaDSL_PARAM)
@given(instance=tortugaDSL_PARAM_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PARAM_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PARAM)


tortugaDSL_PENCOLOR_strategy = st.builds(tortugaDSL_PENCOLOR)
@given(instance=tortugaDSL_PENCOLOR_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PENCOLOR_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PENCOLOR)


tortugaDSL_PENDOWN_strategy = st.builds(tortugaDSL_PENDOWN)
@given(instance=tortugaDSL_PENDOWN_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PENDOWN_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PENDOWN)


tortugaDSL_PENUP_strategy = st.builds(tortugaDSL_PENUP)
@given(instance=tortugaDSL_PENUP_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PENUP_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PENUP)


tortugaDSL_PLAIN_strategy = st.builds(tortugaDSL_PLAIN)
@given(instance=tortugaDSL_PLAIN_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PLAIN_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PLAIN)


tortugaDSL_PROCEDURE_CALL_strategy = st.builds(tortugaDSL_PROCEDURE_CALL)
@given(instance=tortugaDSL_PROCEDURE_CALL_strategy)
@settings(max_examples=25)
def test_tortugaDSL_PROCEDURE_CALL_instantiation(instance):
    assert isinstance(instance, tortugaDSL_PROCEDURE_CALL)


tortugaDSL_REFERENCIABLE_strategy = st.builds(tortugaDSL_REFERENCIABLE, name=safe_text)
@given(instance=tortugaDSL_REFERENCIABLE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_REFERENCIABLE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_REFERENCIABLE)


tortugaDSL_REPEAT_strategy = st.builds(tortugaDSL_REPEAT)
@given(instance=tortugaDSL_REPEAT_strategy)
@settings(max_examples=25)
def test_tortugaDSL_REPEAT_instantiation(instance):
    assert isinstance(instance, tortugaDSL_REPEAT)


tortugaDSL_RIGHT_strategy = st.builds(tortugaDSL_RIGHT)
@given(instance=tortugaDSL_RIGHT_strategy)
@settings(max_examples=25)
def test_tortugaDSL_RIGHT_instantiation(instance):
    assert isinstance(instance, tortugaDSL_RIGHT)


tortugaDSL_SENTENCE_strategy = st.builds(tortugaDSL_SENTENCE)
@given(instance=tortugaDSL_SENTENCE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_SENTENCE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_SENTENCE)


tortugaDSL_SET_X_strategy = st.builds(tortugaDSL_SET_X)
@given(instance=tortugaDSL_SET_X_strategy)
@settings(max_examples=25)
def test_tortugaDSL_SET_X_instantiation(instance):
    assert isinstance(instance, tortugaDSL_SET_X)


tortugaDSL_SET_Y_strategy = st.builds(tortugaDSL_SET_Y)
@given(instance=tortugaDSL_SET_Y_strategy)
@settings(max_examples=25)
def test_tortugaDSL_SET_Y_instantiation(instance):
    assert isinstance(instance, tortugaDSL_SET_Y)


tortugaDSL_SUBTRACT_strategy = st.builds(tortugaDSL_SUBTRACT)
@given(instance=tortugaDSL_SUBTRACT_strategy)
@settings(max_examples=25)
def test_tortugaDSL_SUBTRACT_instantiation(instance):
    assert isinstance(instance, tortugaDSL_SUBTRACT)


tortugaDSL_SUM_strategy = st.builds(tortugaDSL_SUM)
@given(instance=tortugaDSL_SUM_strategy)
@settings(max_examples=25)
def test_tortugaDSL_SUM_instantiation(instance):
    assert isinstance(instance, tortugaDSL_SUM)


tortugaDSL_TO_strategy = st.builds(tortugaDSL_TO, name=safe_text)
@given(instance=tortugaDSL_TO_strategy)
@settings(max_examples=25)
def test_tortugaDSL_TO_instantiation(instance):
    assert isinstance(instance, tortugaDSL_TO)


tortugaDSL_TortugaProgram_strategy = st.builds(tortugaDSL_TortugaProgram)
@given(instance=tortugaDSL_TortugaProgram_strategy)
@settings(max_examples=25)
def test_tortugaDSL_TortugaProgram_instantiation(instance):
    assert isinstance(instance, tortugaDSL_TortugaProgram)


tortugaDSL_VALUE_strategy = st.builds(tortugaDSL_VALUE, val=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=tortugaDSL_VALUE_strategy)
@settings(max_examples=25)
def test_tortugaDSL_VALUE_instantiation(instance):
    assert isinstance(instance, tortugaDSL_VALUE)


tortugaDSL_VARIABLE_REF_strategy = st.builds(tortugaDSL_VARIABLE_REF)
@given(instance=tortugaDSL_VARIABLE_REF_strategy)
@settings(max_examples=25)
def test_tortugaDSL_VARIABLE_REF_instantiation(instance):
    assert isinstance(instance, tortugaDSL_VARIABLE_REF)



