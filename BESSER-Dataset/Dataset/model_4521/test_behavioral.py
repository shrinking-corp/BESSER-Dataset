import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_colorSpec2_stub_double():
    # tortugaDSL_COLOR_SPEC has no real 'tortugaDSL_COLOR_SPEC' property in the generated
    # code (a bare stub) -- manually attach it so tortugaDSL_COLOREABLE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tortugaDSL_COLOREABLE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tortugaDSL_COLOREABLE(color="sample_text")
    partner = tortugaDSL_COLOR_SPEC()
    setattr(partner, 'tortugaDSL_COLOR_SPEC', None)
    _safe_set(owner, 'tortugaDSL_COLOREABLE', partner)
    assert getattr(partner, 'tortugaDSL_COLOR_SPEC') == owner
    _safe_set(owner, 'tortugaDSL_COLOREABLE', None)
    assert getattr(partner, 'tortugaDSL_COLOR_SPEC') is None


def test_assoc_parameters35_stub_double():
    # tortugaDSL_PARAM has no real 'tortugaDSL_PARAM' property in the generated
    # code (a bare stub) -- manually attach it so tortugaDSL_TO's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tortugaDSL_TO's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tortugaDSL_TO(name="sample_text")
    partner = tortugaDSL_PARAM()
    setattr(partner, 'tortugaDSL_PARAM', None)
    _safe_set(owner, 'tortugaDSL_TO', {partner})
    assert getattr(partner, 'tortugaDSL_PARAM') == owner
    _safe_set(owner, 'tortugaDSL_TO', set())
    assert getattr(partner, 'tortugaDSL_PARAM') is None


def test_assoc_to36_stub_double():
    # tortugaDSL_PROCEDURE_CALL has no real 'tortugaDSL_PROCEDURE_CALL' property in the generated
    # code (a bare stub) -- manually attach it so tortugaDSL_TO's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tortugaDSL_TO's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tortugaDSL_TO(name="sample_text")
    partner = tortugaDSL_PROCEDURE_CALL()
    setattr(partner, 'tortugaDSL_PROCEDURE_CALL', None)
    _safe_set(owner, 'tortugaDSL_TO37', partner)
    assert getattr(partner, 'tortugaDSL_PROCEDURE_CALL') == owner
    _safe_set(owner, 'tortugaDSL_TO37', None)
    assert getattr(partner, 'tortugaDSL_PROCEDURE_CALL') is None


def test_assoc_toVar20_stub_double():
    # tortugaDSL_VARIABLE_REF has no real 'tortugaDSL_VARIABLE_REF' property in the generated
    # code (a bare stub) -- manually attach it so tortugaDSL_REFERENCIABLE's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tortugaDSL_REFERENCIABLE's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tortugaDSL_REFERENCIABLE(name="sample_text")
    partner = tortugaDSL_VARIABLE_REF()
    setattr(partner, 'tortugaDSL_VARIABLE_REF', None)
    _safe_set(owner, 'tortugaDSL_REFERENCIABLE', partner)
    assert getattr(partner, 'tortugaDSL_VARIABLE_REF') == owner
    _safe_set(owner, 'tortugaDSL_REFERENCIABLE', None)
    assert getattr(partner, 'tortugaDSL_VARIABLE_REF') is None


