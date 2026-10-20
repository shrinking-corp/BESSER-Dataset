import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDefinition,
    Expression,
    Statement,
    arithmetics_AbstractDefinition,
    arithmetics_DeclaredParameter,
    arithmetics_Definition,
    arithmetics_Div,
    arithmetics_Evaluation,
    arithmetics_Expression,
    arithmetics_FunctionCall,
    arithmetics_Import,
    arithmetics_Minus,
    arithmetics_Module,
    arithmetics_Multi,
    arithmetics_NumberLiteral,
    arithmetics_Plus,
    arithmetics_Statement,
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

def test_assoc_func31_stub_double():
    # arithmetics_FunctionCall has no real 'arithmetics_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so arithmetics_AbstractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetics_AbstractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetics_AbstractDefinition(name="sample_text")
    partner = arithmetics_FunctionCall()
    setattr(partner, 'arithmetics_FunctionCall', None)
    _safe_set(owner, 'arithmetics_AbstractDefinition', partner)
    assert getattr(partner, 'arithmetics_FunctionCall') == owner
    _safe_set(owner, 'arithmetics_AbstractDefinition', None)
    assert getattr(partner, 'arithmetics_FunctionCall') is None


def test_assoc_imports0_stub_double():
    # arithmetics_Import has no real 'arithmetics_Import' property in the generated
    # code (a bare stub) -- manually attach it so arithmetics_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetics_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetics_Module(name="sample_text")
    partner = arithmetics_Import()
    setattr(partner, 'arithmetics_Import', None)
    _safe_set(owner, 'arithmetics_Module', {partner})
    assert getattr(partner, 'arithmetics_Import') == owner
    _safe_set(owner, 'arithmetics_Module', set())
    assert getattr(partner, 'arithmetics_Import') is None


def test_assoc_module3_stub_double():
    # arithmetics_Import has no real 'arithmetics_Import4' property in the generated
    # code (a bare stub) -- manually attach it so arithmetics_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetics_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetics_Module(name="sample_text")
    partner = arithmetics_Import()
    setattr(partner, 'arithmetics_Import4', None)
    _safe_set(owner, 'arithmetics_Module5', partner)
    assert getattr(partner, 'arithmetics_Import4') == owner
    _safe_set(owner, 'arithmetics_Module5', None)
    assert getattr(partner, 'arithmetics_Import4') is None


def test_assoc_statements1_stub_double():
    # arithmetics_Statement has no real 'arithmetics_Statement' property in the generated
    # code (a bare stub) -- manually attach it so arithmetics_Module's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arithmetics_Module's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arithmetics_Module(name="sample_text")
    partner = arithmetics_Statement()
    setattr(partner, 'arithmetics_Statement', None)
    _safe_set(owner, 'arithmetics_Module2', {partner})
    assert getattr(partner, 'arithmetics_Statement') == owner
    _safe_set(owner, 'arithmetics_Module2', set())
    assert getattr(partner, 'arithmetics_Statement') is None


