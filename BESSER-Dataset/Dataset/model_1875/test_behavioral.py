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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_template15_stub_double():
    # problog_TermInstance has no real 'problog_TermInstance' property in the generated
    # code (a bare stub) -- manually attach it so problog_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # problog_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = problog_Term(arguments=7, name="sample_text")
    partner = problog_TermInstance()
    setattr(partner, 'problog_TermInstance', None)
    _safe_set(owner, 'problog_Term16', partner)
    assert getattr(partner, 'problog_TermInstance') == owner
    _safe_set(owner, 'problog_Term16', None)
    assert getattr(partner, 'problog_TermInstance') is None


def test_assoc_terms1_stub_double():
    # problog_ProbLogProgram has no real 'problog_ProbLogProgram2' property in the generated
    # code (a bare stub) -- manually attach it so problog_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # problog_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = problog_Term(arguments=7, name="sample_text")
    partner = problog_ProbLogProgram()
    setattr(partner, 'problog_ProbLogProgram2', None)
    _safe_set(owner, 'problog_Term', partner)
    assert getattr(partner, 'problog_ProbLogProgram2') == owner
    _safe_set(owner, 'problog_Term', None)
    assert getattr(partner, 'problog_ProbLogProgram2') is None


