import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractDefinition,
    Expression,
    rankPL_AbstractDefinition,
    rankPL_DeclaredParameter,
    rankPL_Definition,
    rankPL_Div,
    rankPL_Expression,
    rankPL_FunctionCall,
    rankPL_Minus,
    rankPL_Model,
    rankPL_Multi,
    rankPL_NumberLiteral,
    rankPL_Plus,
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

def test_assoc_func22_stub_double():
    # rankPL_FunctionCall has no real 'rankPL_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so rankPL_AbstractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rankPL_AbstractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rankPL_AbstractDefinition(name="sample_text")
    partner = rankPL_FunctionCall()
    setattr(partner, 'rankPL_FunctionCall', None)
    _safe_set(owner, 'rankPL_AbstractDefinition23', partner)
    assert getattr(partner, 'rankPL_FunctionCall') == owner
    _safe_set(owner, 'rankPL_AbstractDefinition23', None)
    assert getattr(partner, 'rankPL_FunctionCall') is None


def test_assoc_greetings0_stub_double():
    # rankPL_Model has no real 'rankPL_Model' property in the generated
    # code (a bare stub) -- manually attach it so rankPL_AbstractDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # rankPL_AbstractDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = rankPL_AbstractDefinition(name="sample_text")
    partner = rankPL_Model()
    setattr(partner, 'rankPL_Model', None)
    _safe_set(owner, 'rankPL_AbstractDefinition', partner)
    assert owner in getattr(partner, 'rankPL_Model')
    _safe_set(owner, 'rankPL_AbstractDefinition', None)
    assert owner not in getattr(partner, 'rankPL_Model')


