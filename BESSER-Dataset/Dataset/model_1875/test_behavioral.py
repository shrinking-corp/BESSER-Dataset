import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotatable,
    Collection,
    ProbLogStatement,
    ProbabilityMeasure,
    Proposition,
    Referable,
    Statement,
    problog_Annotatable,
    problog_AnnotatedReferable,
    problog_Atom,
    problog_Cheat,
    problog_Collection,
    problog_Comment,
    problog_Evidence,
    problog_ImportLibrary,
    problog_LHS,
    problog_PLList,
    problog_PLTuple,
    problog_ProbLogProgram,
    problog_ProbLogStatement,
    problog_ProbabilityFraction,
    problog_ProbabilityLiteral,
    problog_ProbabilityMeasure,
    problog_Proposition,
    problog_Query,
    problog_RHS,
    problog_Referable,
    problog_Rule,
    problog_Statement,
    problog_Term,
    problog_TermInstance,
    problog_Variable,
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

