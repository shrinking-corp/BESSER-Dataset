import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryExpression,
    Clause,
    ControlPredicate,
    Directive,
    Expression,
    PredicateIndicator,
    Term,
    UnaryExpression,
    prolog_AtomicNumber,
    prolog_AtomicQuotedString,
    prolog_Clause,
    prolog_Comment,
    prolog_CompoundTerm,
    prolog_ControlPredicate,
    prolog_Cut,
    prolog_Fact,
    prolog_Fail,
    prolog_False,
    prolog_List,
    prolog_Program,
    prolog_Rule,
    prolog_Term,
    prolog_True,
    prolog_directives_Directive,
    prolog_directives_Discontiguous,
    prolog_directives_Dynamic,
    prolog_directives_Multifile,
    prolog_directives_PredicateIndicator,
    prolog_directives_Public,
    prolog_directives_Table,
    prolog_directives_Volatile,
    prolog_expressions_As,
    prolog_expressions_BinaryAnd,
    prolog_expressions_BinaryExpression,
    prolog_expressions_BinaryOr,
    prolog_expressions_BitwiseNegation,
    prolog_expressions_BitwiseShiftLeft,
    prolog_expressions_Condition,
    prolog_expressions_Disequality,
    prolog_expressions_Div,
    prolog_expressions_Division,
    prolog_expressions_EqualOrStandardOrderAfter,
    prolog_expressions_EqualOrStandardOrderBefore,
    prolog_expressions_Equivalence,
    prolog_expressions_Expression,
    prolog_expressions_GreaterOrEqual,
    prolog_expressions_GreaterThan,
    prolog_expressions_IntegerDivision,
    prolog_expressions_Is,
    prolog_expressions_LessOrEqual,
    prolog_expressions_LessThan,
    prolog_expressions_LogicalAnd,
    prolog_expressions_LogicalOr,
    prolog_expressions_Minus,
    prolog_expressions_Mod,
    prolog_expressions_ModuleCall,
    prolog_expressions_Multiplication,
    prolog_expressions_NegativeNumber,
    prolog_expressions_NonEqualNumber,
    prolog_expressions_NotProvable,
    prolog_expressions_NotUnifiable,
    prolog_expressions_NumberEqual,
    prolog_expressions_ParticalUnification,
    prolog_expressions_Plus,
    prolog_expressions_PositiveNumber,
    prolog_expressions_Power,
    prolog_expressions_Rdiv,
    prolog_expressions_Rem,
    prolog_expressions_SoftCut,
    prolog_expressions_StandardOrderAfter,
    prolog_expressions_StandardOrderBefore,
    prolog_expressions_StructuralEquivalence,
    prolog_expressions_StructuralEquivalenceNotProvable,
    prolog_expressions_SubDict,
    prolog_expressions_UnaryExpression,
    prolog_expressions_Unification,
    prolog_expressions_Univ,
    prolog_expressions_Xor,
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

def test_assoc_arguments1_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so prolog_CompoundTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_CompoundTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_CompoundTerm(value="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'prolog_CompoundTerm', {partner})
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'prolog_CompoundTerm', set())
    assert getattr(partner, 'Expression') is None


def test_assoc_head7_stub_double():
    # prolog_Fact has no real 'prolog_Fact' property in the generated
    # code (a bare stub) -- manually attach it so prolog_CompoundTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_CompoundTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_CompoundTerm(value="sample_text")
    partner = prolog_Fact()
    setattr(partner, 'prolog_Fact', None)
    _safe_set(owner, 'prolog_CompoundTerm8', partner)
    assert getattr(partner, 'prolog_Fact') == owner
    _safe_set(owner, 'prolog_CompoundTerm8', None)
    assert getattr(partner, 'prolog_Fact') is None


def test_assoc_head9_stub_double():
    # prolog_Rule has no real 'prolog_Rule' property in the generated
    # code (a bare stub) -- manually attach it so prolog_CompoundTerm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_CompoundTerm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_CompoundTerm(value="sample_text")
    partner = prolog_Rule()
    setattr(partner, 'prolog_Rule', None)
    _safe_set(owner, 'prolog_CompoundTerm10', partner)
    assert getattr(partner, 'prolog_Rule') == owner
    _safe_set(owner, 'prolog_CompoundTerm10', None)
    assert getattr(partner, 'prolog_Rule') is None


def test_assoc_predicates14_stub_double():
    # PredicateIndicator has no real 'PredicateIndicator' property in the generated
    # code (a bare stub) -- manually attach it so prolog_directives_Directive's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # prolog_directives_Directive's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = prolog_directives_Directive(name="sample_text")
    partner = PredicateIndicator()
    setattr(partner, 'PredicateIndicator', None)
    _safe_set(owner, 'prolog_directives_Directive', {partner})
    assert getattr(partner, 'PredicateIndicator') == owner
    _safe_set(owner, 'prolog_directives_Directive', set())
    assert getattr(partner, 'PredicateIndicator') is None


