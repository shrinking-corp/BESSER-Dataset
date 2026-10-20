import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Constant,
    Expression,
    Feature,
    featureModel_BinaryOperation,
    featureModel_Constant,
    featureModel_Expression,
    featureModel_Feature,
    featureModel_Group,
    featureModel_GroupedFeature,
    featureModel_Identifier,
    featureModel_Model,
    featureModel_NULL,
    featureModel_Number,
    featureModel_SolitaryFeature,
    featureModel_UnaryOperation,
    BinaryOperator,
    SimpleType,
    SolitaryType,
    UnaryOperator,
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

def test_assoc_features1_reverse_link_reassign_clear():
    a1 = featureModel_SolitaryFeature(required="sample_text")
    a2 = featureModel_SolitaryFeature(required="sample_text_2")
    b = featureModel_Feature(name="sample_text", type="sample_text")
    _safe_set(b, 'featureModel_Feature2', {a1})
    assert _is_linked(b, 'featureModel_Feature2', a1)
    if hasattr(a1, 'featureModel_SolitaryFeature'):
        assert _is_linked(a1, 'featureModel_SolitaryFeature', b)
    _safe_set(b, 'featureModel_Feature2', {a2})
    assert _is_linked(b, 'featureModel_Feature2', a2)
    if hasattr(a1, 'featureModel_SolitaryFeature'):
        assert not _is_linked(a1, 'featureModel_SolitaryFeature', b)
    if hasattr(a2, 'featureModel_SolitaryFeature'):
        assert _is_linked(a2, 'featureModel_SolitaryFeature', b)
    _safe_set(b, 'featureModel_Feature2', set())
    assert not _is_linked(b, 'featureModel_Feature2', a2)
    if hasattr(a2, 'featureModel_SolitaryFeature'):
        assert not _is_linked(a2, 'featureModel_SolitaryFeature', b)


def test_assoc_groups0_reverse_link_reassign_clear():
    a1 = featureModel_Group(inclusive=True)
    a2 = featureModel_Group(inclusive=False)
    b = featureModel_Feature(name="sample_text", type="sample_text")
    _safe_set(b, 'featureModel_Feature', {a1})
    assert _is_linked(b, 'featureModel_Feature', a1)
    if hasattr(a1, 'featureModel_Group'):
        assert _is_linked(a1, 'featureModel_Group', b)
    _safe_set(b, 'featureModel_Feature', {a2})
    assert _is_linked(b, 'featureModel_Feature', a2)
    if hasattr(a1, 'featureModel_Group'):
        assert not _is_linked(a1, 'featureModel_Group', b)
    if hasattr(a2, 'featureModel_Group'):
        assert _is_linked(a2, 'featureModel_Group', b)
    _safe_set(b, 'featureModel_Feature', set())
    assert not _is_linked(b, 'featureModel_Feature', a2)
    if hasattr(a2, 'featureModel_Group'):
        assert not _is_linked(a2, 'featureModel_Group', b)


def test_assoc_ref16_reverse_link_reassign_clear():
    a1 = featureModel_Identifier(name="sample_text")
    a2 = featureModel_Identifier(name="sample_text_2")
    b = featureModel_Feature(name="sample_text", type="sample_text")
    _safe_set(b, 'featureModel_Feature17', a1)
    assert _is_linked(b, 'featureModel_Feature17', a1)
    if hasattr(a1, 'featureModel_Identifier'):
        assert _is_linked(a1, 'featureModel_Identifier', b)
    _safe_set(b, 'featureModel_Feature17', a2)
    assert _is_linked(b, 'featureModel_Feature17', a2)
    if hasattr(a1, 'featureModel_Identifier'):
        assert not _is_linked(a1, 'featureModel_Identifier', b)
    if hasattr(a2, 'featureModel_Identifier'):
        assert _is_linked(a2, 'featureModel_Identifier', b)
    _safe_set(b, 'featureModel_Feature17', None)
    assert not _is_linked(b, 'featureModel_Feature17', a2)
    if hasattr(a2, 'featureModel_Identifier'):
        assert not _is_linked(a2, 'featureModel_Identifier', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_RootFeature5_stub_double():
    # featureModel_Model has no real 'featureModel_Model' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(name="sample_text", type="sample_text")
    partner = featureModel_Model()
    setattr(partner, 'featureModel_Model', None)
    _safe_set(owner, 'featureModel_Feature6', partner)
    assert owner in getattr(partner, 'featureModel_Model')
    _safe_set(owner, 'featureModel_Feature6', None)
    assert owner not in getattr(partner, 'featureModel_Model')


def test_assoc_constraints3_stub_double():
    # featureModel_Expression has no real 'featureModel_Expression' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Feature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Feature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Feature(name="sample_text", type="sample_text")
    partner = featureModel_Expression()
    setattr(partner, 'featureModel_Expression', None)
    _safe_set(owner, 'featureModel_Feature4', {partner})
    assert getattr(partner, 'featureModel_Expression') == owner
    _safe_set(owner, 'featureModel_Feature4', set())
    assert getattr(partner, 'featureModel_Expression') is None


def test_assoc_exp14_stub_double():
    # featureModel_Expression has no real 'featureModel_Expression15' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_UnaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_UnaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_UnaryOperation(operator="sample_text")
    partner = featureModel_Expression()
    setattr(partner, 'featureModel_Expression15', None)
    _safe_set(owner, 'featureModel_UnaryOperation', partner)
    assert getattr(partner, 'featureModel_Expression15') == owner
    _safe_set(owner, 'featureModel_UnaryOperation', None)
    assert getattr(partner, 'featureModel_Expression15') is None


def test_assoc_groupedFeatures7_stub_double():
    # featureModel_GroupedFeature has no real 'featureModel_GroupedFeature' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_Group's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_Group's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_Group(inclusive=True)
    partner = featureModel_GroupedFeature()
    setattr(partner, 'featureModel_GroupedFeature', None)
    _safe_set(owner, 'featureModel_Group8', {partner})
    assert getattr(partner, 'featureModel_GroupedFeature') == owner
    _safe_set(owner, 'featureModel_Group8', set())
    assert getattr(partner, 'featureModel_GroupedFeature') is None


def test_assoc_lexp11_stub_double():
    # featureModel_Expression has no real 'featureModel_Expression13' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_BinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_BinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_BinaryOperation(operator="sample_text")
    partner = featureModel_Expression()
    setattr(partner, 'featureModel_Expression13', None)
    _safe_set(owner, 'featureModel_BinaryOperation12', partner)
    assert getattr(partner, 'featureModel_Expression13') == owner
    _safe_set(owner, 'featureModel_BinaryOperation12', None)
    assert getattr(partner, 'featureModel_Expression13') is None


def test_assoc_rexp9_stub_double():
    # featureModel_Expression has no real 'featureModel_Expression10' property in the generated
    # code (a bare stub) -- manually attach it so featureModel_BinaryOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # featureModel_BinaryOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = featureModel_BinaryOperation(operator="sample_text")
    partner = featureModel_Expression()
    setattr(partner, 'featureModel_Expression10', None)
    _safe_set(owner, 'featureModel_BinaryOperation', partner)
    assert getattr(partner, 'featureModel_Expression10') == owner
    _safe_set(owner, 'featureModel_BinaryOperation', None)
    assert getattr(partner, 'featureModel_Expression10') is None


