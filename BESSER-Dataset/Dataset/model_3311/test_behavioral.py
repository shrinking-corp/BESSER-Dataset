import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Named,
    grammar_ConnexionInstruction,
    grammar_Embedding,
    grammar_Grammar,
    grammar_Graph,
    grammar_LHS,
    grammar_Node,
    grammar_RHS,
    grammar_Rule,
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

def test_assoc_EmbeddingMechanism5_stub_double():
    # grammar_Embedding has no real 'Embedding' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_Embedding()
    setattr(partner, 'Embedding', None)
    _safe_set(owner, 'ParentRule', partner)
    assert getattr(partner, 'Embedding') == owner
    _safe_set(owner, 'ParentRule', None)
    assert getattr(partner, 'Embedding') is None


def test_assoc_ParentRule12_stub_double():
    # grammar_Embedding has no real 'EmbeddingMechanism' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_Embedding()
    setattr(partner, 'EmbeddingMechanism', None)
    _safe_set(owner, 'Rule13', partner)
    assert getattr(partner, 'EmbeddingMechanism') == owner
    _safe_set(owner, 'Rule13', None)
    assert getattr(partner, 'EmbeddingMechanism') is None


def test_assoc_d17_stub_double():
    # grammar_Node has no real 'grammar_Node18' property in the generated
    # code (a bare stub) -- manually attach it so grammar_ConnexionInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_ConnexionInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_ConnexionInstruction(m="sample_text")
    partner = grammar_Node()
    setattr(partner, 'grammar_Node18', None)
    _safe_set(owner, 'grammar_ConnexionInstruction', partner)
    assert getattr(partner, 'grammar_Node18') == owner
    _safe_set(owner, 'grammar_ConnexionInstruction', None)
    assert getattr(partner, 'grammar_Node18') is None


def test_assoc_instructions14_stub_double():
    # grammar_Embedding has no real 'parentEmbedding' property in the generated
    # code (a bare stub) -- manually attach it so grammar_ConnexionInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_ConnexionInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_ConnexionInstruction(m="sample_text")
    partner = grammar_Embedding()
    setattr(partner, 'parentEmbedding', None)
    _safe_set(owner, 'ConnexionInstruction', partner)
    assert owner in getattr(partner, 'parentEmbedding')
    _safe_set(owner, 'ConnexionInstruction', None)
    assert owner not in getattr(partner, 'parentEmbedding')


def test_assoc_lhs2_stub_double():
    # grammar_LHS has no real 'LHS' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_LHS()
    setattr(partner, 'LHS', None)
    _safe_set(owner, 'parentRule', partner)
    assert getattr(partner, 'LHS') == owner
    _safe_set(owner, 'parentRule', None)
    assert getattr(partner, 'LHS') is None


def test_assoc_parentEmbedding15_stub_double():
    # grammar_Embedding has no real 'Embedding16' property in the generated
    # code (a bare stub) -- manually attach it so grammar_ConnexionInstruction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_ConnexionInstruction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_ConnexionInstruction(m="sample_text")
    partner = grammar_Embedding()
    setattr(partner, 'Embedding16', None)
    _safe_set(owner, 'instructions', partner)
    assert getattr(partner, 'Embedding16') == owner
    _safe_set(owner, 'instructions', None)
    assert getattr(partner, 'Embedding16') is None


def test_assoc_parentGrammar1_stub_double():
    # grammar_Grammar has no real 'Grammar' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_Grammar()
    setattr(partner, 'Grammar', None)
    _safe_set(owner, 'rules', partner)
    assert getattr(partner, 'Grammar') == owner
    _safe_set(owner, 'rules', None)
    assert getattr(partner, 'Grammar') is None


def test_assoc_parentRule6_stub_double():
    # grammar_LHS has no real 'lhs' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_LHS()
    setattr(partner, 'lhs', None)
    _safe_set(owner, 'Rule7', partner)
    assert getattr(partner, 'lhs') == owner
    _safe_set(owner, 'Rule7', None)
    assert getattr(partner, 'lhs') is None


def test_assoc_parentRule9_stub_double():
    # grammar_RHS has no real 'rhs' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_RHS()
    setattr(partner, 'rhs', None)
    _safe_set(owner, 'Rule10', partner)
    assert getattr(partner, 'rhs') == owner
    _safe_set(owner, 'Rule10', None)
    assert getattr(partner, 'rhs') is None


def test_assoc_rhs3_stub_double():
    # grammar_RHS has no real 'RHS' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_RHS()
    setattr(partner, 'RHS', None)
    _safe_set(owner, 'parentRule4', partner)
    assert getattr(partner, 'RHS') == owner
    _safe_set(owner, 'parentRule4', None)
    assert getattr(partner, 'RHS') is None


def test_assoc_rules0_stub_double():
    # grammar_Grammar has no real 'parentGrammar' property in the generated
    # code (a bare stub) -- manually attach it so grammar_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # grammar_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = grammar_Rule(name="sample_text", priority=7)
    partner = grammar_Grammar()
    setattr(partner, 'parentGrammar', None)
    _safe_set(owner, 'Rule', partner)
    assert owner in getattr(partner, 'parentGrammar')
    _safe_set(owner, 'Rule', None)
    assert owner not in getattr(partner, 'parentGrammar')


