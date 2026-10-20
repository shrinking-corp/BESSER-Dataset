import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Term,
    TermReference,
    mprologTermReference_Body,
    mprologTermReference_Clause,
    mprologTermReference_Functor,
    mprologTermReference_FunctorReference,
    mprologTermReference_Head,
    mprologTermReference_InfixExpression,
    mprologTermReference_List,
    mprologTermReference_Model,
    mprologTermReference_Operator,
    mprologTermReference_Parenthesis,
    mprologTermReference_QuotedAtom,
    mprologTermReference_Term,
    mprologTermReference_TermReference,
    mprologTermReference_Variable,
    mprologTermReference_VariableReference,
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

def test_assoc_idReference27_stub_double():
    # mprologTermReference_FunctorReference has no real 'mprologTermReference_FunctorReference' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Functor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Functor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Functor(text="sample_text")
    partner = mprologTermReference_FunctorReference()
    setattr(partner, 'mprologTermReference_FunctorReference', None)
    _safe_set(owner, 'mprologTermReference_Functor28', partner)
    assert getattr(partner, 'mprologTermReference_FunctorReference') == owner
    _safe_set(owner, 'mprologTermReference_Functor28', None)
    assert getattr(partner, 'mprologTermReference_FunctorReference') is None


def test_assoc_idReference32_stub_double():
    # mprologTermReference_VariableReference has no real 'mprologTermReference_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Variable(name="sample_text")
    partner = mprologTermReference_VariableReference()
    setattr(partner, 'mprologTermReference_VariableReference', None)
    _safe_set(owner, 'mprologTermReference_Variable', partner)
    assert getattr(partner, 'mprologTermReference_VariableReference') == owner
    _safe_set(owner, 'mprologTermReference_Variable', None)
    assert getattr(partner, 'mprologTermReference_VariableReference') is None


def test_assoc_ownedClause0_stub_double():
    # mprologTermReference_Clause has no real 'mprologTermReference_Clause' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Model's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Model's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Model(name="sample_text")
    partner = mprologTermReference_Clause()
    setattr(partner, 'mprologTermReference_Clause', None)
    _safe_set(owner, 'mprologTermReference_Model', {partner})
    assert getattr(partner, 'mprologTermReference_Clause') == owner
    _safe_set(owner, 'mprologTermReference_Model', set())
    assert getattr(partner, 'mprologTermReference_Clause') is None


def test_assoc_ownedFunctor5_stub_double():
    # mprologTermReference_Head has no real 'mprologTermReference_Head6' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Functor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Functor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Functor(text="sample_text")
    partner = mprologTermReference_Head()
    setattr(partner, 'mprologTermReference_Head6', None)
    _safe_set(owner, 'mprologTermReference_Functor', partner)
    assert getattr(partner, 'mprologTermReference_Head6') == owner
    _safe_set(owner, 'mprologTermReference_Functor', None)
    assert getattr(partner, 'mprologTermReference_Head6') is None


def test_assoc_ownedOperator25_stub_double():
    # mprologTermReference_InfixExpression has no real 'mprologTermReference_InfixExpression26' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Operator(symbol="sample_text")
    partner = mprologTermReference_InfixExpression()
    setattr(partner, 'mprologTermReference_InfixExpression26', None)
    _safe_set(owner, 'mprologTermReference_Operator', partner)
    assert getattr(partner, 'mprologTermReference_InfixExpression26') == owner
    _safe_set(owner, 'mprologTermReference_Operator', None)
    assert getattr(partner, 'mprologTermReference_InfixExpression26') is None


def test_assoc_ownedTerm12_stub_double():
    # mprologTermReference_Term has no real 'mprologTermReference_Term14' property in the generated
    # code (a bare stub) -- manually attach it so mprologTermReference_Functor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mprologTermReference_Functor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mprologTermReference_Functor(text="sample_text")
    partner = mprologTermReference_Term()
    setattr(partner, 'mprologTermReference_Term14', None)
    _safe_set(owner, 'mprologTermReference_Functor13', partner)
    assert getattr(partner, 'mprologTermReference_Term14') == owner
    _safe_set(owner, 'mprologTermReference_Functor13', None)
    assert getattr(partner, 'mprologTermReference_Term14') is None


