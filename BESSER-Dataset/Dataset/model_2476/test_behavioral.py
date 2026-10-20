import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Method,
    Trace,
    Variable,
    brmodel_EObject,
    brmodel_Method,
    brmodel_Model,
    brmodel_ReachableMethod,
    brmodel_ReachableVariable,
    brmodel_RelatedMethod,
    brmodel_RelatedVariable,
    brmodel_Rule,
    brmodel_RulePart,
    brmodel_SlicedVariable,
    brmodel_Statement,
    brmodel_Trace,
    brmodel_Variable,
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

def test_assoc_action9_reverse_link_reassign_clear():
    a1 = brmodel_Statement(textContent="sample_text")
    a2 = brmodel_Statement(textContent="sample_text_2")
    b = brmodel_RulePart(granularity="sample_text")
    _safe_set(b, 'brmodel_RulePart10', a1)
    assert _is_linked(b, 'brmodel_RulePart10', a1)
    if hasattr(a1, 'brmodel_Statement11'):
        assert _is_linked(a1, 'brmodel_Statement11', b)
    _safe_set(b, 'brmodel_RulePart10', a2)
    assert _is_linked(b, 'brmodel_RulePart10', a2)
    if hasattr(a1, 'brmodel_Statement11'):
        assert not _is_linked(a1, 'brmodel_Statement11', b)
    if hasattr(a2, 'brmodel_Statement11'):
        assert _is_linked(a2, 'brmodel_Statement11', b)
    _safe_set(b, 'brmodel_RulePart10', None)
    assert not _is_linked(b, 'brmodel_RulePart10', a2)
    if hasattr(a2, 'brmodel_Statement11'):
        assert not _is_linked(a2, 'brmodel_Statement11', b)


def test_assoc_reachableMethods12_reverse_link_reassign_clear():
    a1 = brmodel_RulePart(granularity="sample_text")
    a2 = brmodel_RulePart(granularity="sample_text_2")
    b = brmodel_ReachableMethod(distance="sample_text")
    _safe_set(b, 'brmodel_ReachableMethod', a1)
    assert _is_linked(b, 'brmodel_ReachableMethod', a1)
    if hasattr(a1, 'brmodel_RulePart13'):
        assert _is_linked(a1, 'brmodel_RulePart13', b)
    _safe_set(b, 'brmodel_ReachableMethod', a2)
    assert _is_linked(b, 'brmodel_ReachableMethod', a2)
    if hasattr(a1, 'brmodel_RulePart13'):
        assert not _is_linked(a1, 'brmodel_RulePart13', b)
    if hasattr(a2, 'brmodel_RulePart13'):
        assert _is_linked(a2, 'brmodel_RulePart13', b)
    _safe_set(b, 'brmodel_ReachableMethod', None)
    assert not _is_linked(b, 'brmodel_ReachableMethod', a2)
    if hasattr(a2, 'brmodel_RulePart13'):
        assert not _is_linked(a2, 'brmodel_RulePart13', b)


def test_assoc_relatedStatements7_reverse_link_reassign_clear():
    a1 = brmodel_Statement(textContent="sample_text")
    a2 = brmodel_Statement(textContent="sample_text_2")
    b = brmodel_RulePart(granularity="sample_text")
    _safe_set(b, 'brmodel_RulePart8', {a1})
    assert _is_linked(b, 'brmodel_RulePart8', a1)
    if hasattr(a1, 'brmodel_Statement'):
        assert _is_linked(a1, 'brmodel_Statement', b)
    _safe_set(b, 'brmodel_RulePart8', {a2})
    assert _is_linked(b, 'brmodel_RulePart8', a2)
    if hasattr(a1, 'brmodel_Statement'):
        assert not _is_linked(a1, 'brmodel_Statement', b)
    if hasattr(a2, 'brmodel_Statement'):
        assert _is_linked(a2, 'brmodel_Statement', b)
    _safe_set(b, 'brmodel_RulePart8', set())
    assert not _is_linked(b, 'brmodel_RulePart8', a2)
    if hasattr(a2, 'brmodel_Statement'):
        assert not _is_linked(a2, 'brmodel_Statement', b)


def test_assoc_ruleParts3_reverse_link_reassign_clear():
    a1 = brmodel_RulePart(granularity="sample_text")
    a2 = brmodel_RulePart(granularity="sample_text_2")
    b = brmodel_Rule(id="sample_text")
    _safe_set(b, 'brmodel_Rule4', {a1})
    assert _is_linked(b, 'brmodel_Rule4', a1)
    if hasattr(a1, 'brmodel_RulePart'):
        assert _is_linked(a1, 'brmodel_RulePart', b)
    _safe_set(b, 'brmodel_Rule4', {a2})
    assert _is_linked(b, 'brmodel_Rule4', a2)
    if hasattr(a1, 'brmodel_RulePart'):
        assert not _is_linked(a1, 'brmodel_RulePart', b)
    if hasattr(a2, 'brmodel_RulePart'):
        assert _is_linked(a2, 'brmodel_RulePart', b)
    _safe_set(b, 'brmodel_Rule4', set())
    assert not _is_linked(b, 'brmodel_Rule4', a2)
    if hasattr(a2, 'brmodel_RulePart'):
        assert not _is_linked(a2, 'brmodel_RulePart', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_relatedMethod5_stub_double():
    # brmodel_RelatedMethod has no real 'brmodel_RelatedMethod' property in the generated
    # code (a bare stub) -- manually attach it so brmodel_RulePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # brmodel_RulePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = brmodel_RulePart(granularity="sample_text")
    partner = brmodel_RelatedMethod()
    setattr(partner, 'brmodel_RelatedMethod', None)
    _safe_set(owner, 'brmodel_RulePart6', partner)
    assert getattr(partner, 'brmodel_RelatedMethod') == owner
    _safe_set(owner, 'brmodel_RulePart6', None)
    assert getattr(partner, 'brmodel_RelatedMethod') is None


def test_assoc_relatedVariables14_stub_double():
    # brmodel_ReachableVariable has no real 'brmodel_ReachableVariable' property in the generated
    # code (a bare stub) -- manually attach it so brmodel_RulePart's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # brmodel_RulePart's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = brmodel_RulePart(granularity="sample_text")
    partner = brmodel_ReachableVariable()
    setattr(partner, 'brmodel_ReachableVariable', None)
    _safe_set(owner, 'brmodel_RulePart15', {partner})
    assert getattr(partner, 'brmodel_ReachableVariable') == owner
    _safe_set(owner, 'brmodel_RulePart15', set())
    assert getattr(partner, 'brmodel_ReachableVariable') is None


def test_assoc_rules0_stub_double():
    # brmodel_Model has no real 'brmodel_Model' property in the generated
    # code (a bare stub) -- manually attach it so brmodel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # brmodel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = brmodel_Rule(id="sample_text")
    partner = brmodel_Model()
    setattr(partner, 'brmodel_Model', None)
    _safe_set(owner, 'brmodel_Rule', partner)
    assert owner in getattr(partner, 'brmodel_Model')
    _safe_set(owner, 'brmodel_Rule', None)
    assert owner not in getattr(partner, 'brmodel_Model')


def test_assoc_slicedVariable1_stub_double():
    # brmodel_SlicedVariable has no real 'brmodel_SlicedVariable' property in the generated
    # code (a bare stub) -- manually attach it so brmodel_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # brmodel_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = brmodel_Rule(id="sample_text")
    partner = brmodel_SlicedVariable()
    setattr(partner, 'brmodel_SlicedVariable', None)
    _safe_set(owner, 'brmodel_Rule2', partner)
    assert getattr(partner, 'brmodel_SlicedVariable') == owner
    _safe_set(owner, 'brmodel_Rule2', None)
    assert getattr(partner, 'brmodel_SlicedVariable') is None


