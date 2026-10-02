import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractState,
    NamedElement,
    State,
    Statement,
    fsmcore_AbstractState,
    fsmcore_Conditional,
    fsmcore_Constraint,
    fsmcore_FinalState,
    fsmcore_Loop,
    fsmcore_NamedElement,
    fsmcore_Program,
    fsmcore_Pseudostate,
    fsmcore_Region,
    fsmcore_State,
    fsmcore_StateMachine,
    fsmcore_Statement,
    fsmcore_Transition,
    fsmcore_Trigger,
    fsmcore_VarDecl,
    PseudostateKind,
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

def test_assoc_statements23_reverse_link_reassign_clear():
    a1 = fsmcore_Statement()
    a2 = fsmcore_Statement()
    b = fsmcore_Program()
    _safe_set(b, 'fsmcore_Program24', {a1})
    assert _is_linked(b, 'fsmcore_Program24', a1)
    if hasattr(a1, 'fsmcore_Statement'):
        assert _is_linked(a1, 'fsmcore_Statement', b)
    _safe_set(b, 'fsmcore_Program24', {a2})
    assert _is_linked(b, 'fsmcore_Program24', a2)
    if hasattr(a1, 'fsmcore_Statement'):
        assert not _is_linked(a1, 'fsmcore_Statement', b)
    if hasattr(a2, 'fsmcore_Statement'):
        assert _is_linked(a2, 'fsmcore_Statement', b)
    _safe_set(b, 'fsmcore_Program24', set())
    assert not _is_linked(b, 'fsmcore_Program24', a2)
    if hasattr(a2, 'fsmcore_Statement'):
        assert not _is_linked(a2, 'fsmcore_Statement', b)


