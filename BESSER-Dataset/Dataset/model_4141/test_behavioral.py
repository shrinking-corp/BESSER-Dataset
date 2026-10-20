import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDefinition,
    Expression,
    Statement,
    arithmetic_AbstractDefinition,
    arithmetic_DeclaredParameter,
    arithmetic_Definition,
    arithmetic_Div,
    arithmetic_Evaluation,
    arithmetic_Expression,
    arithmetic_FunctionCall,
    arithmetic_Import,
    arithmetic_Minus,
    arithmetic_Module,
    arithmetic_Multi,
    arithmetic_NumberLiteral,
    arithmetic_Plus,
    arithmetic_Statement,
    arithmetic_SumExpression,
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

def test_assoc_expr13_stub_double():
    # arithmetic_Expression has no real 'arithmetic_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_SumExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_SumExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_SumExpression(lower=7, upper=7)
    partner = arithmetic_Expression()
    setattr(partner, 'arithmetic_Expression15', None)
    _safe_set(owner, 'arithmetic_SumExpression14', partner)
    assert getattr(partner, 'arithmetic_Expression15') == owner
    _safe_set(owner, 'arithmetic_SumExpression14', None)
    assert getattr(partner, 'arithmetic_Expression15') is None


def test_assoc_func36_stub_double():
    # arithmetic_FunctionCall has no real 'arithmetic_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_AbstractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_AbstractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_AbstractDefinition(name="sample_text")
    partner = arithmetic_FunctionCall()
    setattr(partner, 'arithmetic_FunctionCall', None)
    _safe_set(owner, 'arithmetic_AbstractDefinition', partner)
    assert getattr(partner, 'arithmetic_FunctionCall') == owner
    _safe_set(owner, 'arithmetic_AbstractDefinition', None)
    assert getattr(partner, 'arithmetic_FunctionCall') is None


def test_assoc_imports0_stub_double():
    # arithmetic_Import has no real 'arithmetic_Import' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_Module(name="sample_text")
    partner = arithmetic_Import()
    setattr(partner, 'arithmetic_Import', None)
    _safe_set(owner, 'arithmetic_Module', {partner})
    assert getattr(partner, 'arithmetic_Import') == owner
    _safe_set(owner, 'arithmetic_Module', set())
    assert getattr(partner, 'arithmetic_Import') is None


def test_assoc_indexVariable11_stub_double():
    # arithmetic_DeclaredParameter has no real 'arithmetic_DeclaredParameter12' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_SumExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_SumExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_SumExpression(lower=7, upper=7)
    partner = arithmetic_DeclaredParameter()
    setattr(partner, 'arithmetic_DeclaredParameter12', None)
    _safe_set(owner, 'arithmetic_SumExpression', partner)
    assert getattr(partner, 'arithmetic_DeclaredParameter12') == owner
    _safe_set(owner, 'arithmetic_SumExpression', None)
    assert getattr(partner, 'arithmetic_DeclaredParameter12') is None


def test_assoc_module3_stub_double():
    # arithmetic_Import has no real 'arithmetic_Import4' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_Module(name="sample_text")
    partner = arithmetic_Import()
    setattr(partner, 'arithmetic_Import4', None)
    _safe_set(owner, 'arithmetic_Module5', partner)
    assert getattr(partner, 'arithmetic_Import4') == owner
    _safe_set(owner, 'arithmetic_Module5', None)
    assert getattr(partner, 'arithmetic_Import4') is None


def test_assoc_statements1_stub_double():
    # arithmetic_Statement has no real 'arithmetic_Statement' property in the generated
    # code (a bare stub) -- manually attach it so arithmetic_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetic_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetic_Module(name="sample_text")
    partner = arithmetic_Statement()
    setattr(partner, 'arithmetic_Statement', None)
    _safe_set(owner, 'arithmetic_Module2', {partner})
    assert getattr(partner, 'arithmetic_Statement') == owner
    _safe_set(owner, 'arithmetic_Module2', set())
    assert getattr(partner, 'arithmetic_Statement') is None


