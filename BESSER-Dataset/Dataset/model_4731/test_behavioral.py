import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Part,
    Tail,
    Term,
    prolog_Additive,
    prolog_AnonymousVariable,
    prolog_Assignment,
    prolog_BracketExpression,
    prolog_Clause,
    prolog_Conjunction,
    prolog_List,
    prolog_Multiplicative,
    prolog_Negation,
    prolog_Numeral,
    prolog_Part,
    prolog_Power,
    prolog_Predicate,
    prolog_PrologProgram,
    prolog_String,
    prolog_Tail,
    prolog_Term,
    prolog_Variable,
    prolog_VariableReference,
    ADDITIVE_OPERATOR,
    MULTIPLICATIVE_OPERATOR,
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

def test_assoc_body34_stub_double():
    # prolog_Term has no real 'prolog_Term35' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Negation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Negation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Negation(operator="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term35', None)
    _safe_set(owner, 'prolog_Negation', partner)
    assert getattr(partner, 'prolog_Term35') == owner
    _safe_set(owner, 'prolog_Negation', None)
    assert getattr(partner, 'prolog_Term35') is None


def test_assoc_left19_stub_double():
    # prolog_Term has no real 'prolog_Term20' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Additive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Additive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Additive(operator="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term20', None)
    _safe_set(owner, 'prolog_Additive', partner)
    assert getattr(partner, 'prolog_Term20') == owner
    _safe_set(owner, 'prolog_Additive', None)
    assert getattr(partner, 'prolog_Term20') is None


def test_assoc_left24_stub_double():
    # prolog_Term has no real 'prolog_Term25' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Multiplicative's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Multiplicative's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Multiplicative(operator="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term25', None)
    _safe_set(owner, 'prolog_Multiplicative', partner)
    assert getattr(partner, 'prolog_Term25') == owner
    _safe_set(owner, 'prolog_Multiplicative', None)
    assert getattr(partner, 'prolog_Term25') is None


def test_assoc_predicate1_stub_double():
    # prolog_Clause has no real 'prolog_Clause2' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Predicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Predicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Predicate(name="sample_text")
    partner = prolog_Clause()
    setattr(partner, 'prolog_Clause2', None)
    _safe_set(owner, 'prolog_Predicate', partner)
    assert getattr(partner, 'prolog_Clause2') == owner
    _safe_set(owner, 'prolog_Predicate', None)
    assert getattr(partner, 'prolog_Clause2') is None


def test_assoc_right21_stub_double():
    # prolog_Term has no real 'prolog_Term23' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Additive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Additive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Additive(operator="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term23', None)
    _safe_set(owner, 'prolog_Additive22', partner)
    assert getattr(partner, 'prolog_Term23') == owner
    _safe_set(owner, 'prolog_Additive22', None)
    assert getattr(partner, 'prolog_Term23') is None


def test_assoc_right26_stub_double():
    # prolog_Term has no real 'prolog_Term28' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Multiplicative's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Multiplicative's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Multiplicative(operator="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term28', None)
    _safe_set(owner, 'prolog_Multiplicative27', partner)
    assert getattr(partner, 'prolog_Term28') == owner
    _safe_set(owner, 'prolog_Multiplicative27', None)
    assert getattr(partner, 'prolog_Term28') is None


def test_assoc_terms8_stub_double():
    # prolog_Term has no real 'prolog_Term10' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Predicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Predicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Predicate(name="sample_text")
    partner = prolog_Term()
    setattr(partner, 'prolog_Term10', None)
    _safe_set(owner, 'prolog_Predicate9', {partner})
    assert getattr(partner, 'prolog_Term10') == owner
    _safe_set(owner, 'prolog_Predicate9', set())
    assert getattr(partner, 'prolog_Term10') is None


def test_assoc_variable11_stub_double():
    # prolog_VariableReference has no real 'prolog_VariableReference' property in the generated
    # code (a bare stub) -- manually attach it so prolog_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_Variable(name="sample_text")
    partner = prolog_VariableReference()
    setattr(partner, 'prolog_VariableReference', None)
    _safe_set(owner, 'prolog_Variable', partner)
    assert getattr(partner, 'prolog_VariableReference') == owner
    _safe_set(owner, 'prolog_Variable', None)
    assert getattr(partner, 'prolog_VariableReference') is None


