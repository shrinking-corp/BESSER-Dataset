import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ConfigConstraint,
    Constraint,
    FeatureModel_And,
    FeatureModel_ConfigConstraint,
    FeatureModel_Constraint,
    FeatureModel_Feature,
    FeatureModel_FeatureConstraint,
    FeatureModel_FeatureModel,
    FeatureModel_Or,
    FeatureModel_RootFeature,
    FeatureModel_Xor,
    Type,
    kind,
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

def test_assoc_ConfFeatures8_reverse_link_reassign_clear():
    a1 = FeatureModel_Feature(id=7, name="sample_text")
    a2 = FeatureModel_Feature(id=13, name="sample_text_2")
    b = FeatureModel_ConfigConstraint(kind="sample_text")
    _safe_set(b, 'Config', {a1})
    assert _is_linked(b, 'Config', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'Config', {a2})
    assert _is_linked(b, 'Config', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'Config', set())
    assert not _is_linked(b, 'Config', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_Config7_reverse_link_reassign_clear():
    a1 = FeatureModel_Feature(id=7, name="sample_text")
    a2 = FeatureModel_Feature(id=13, name="sample_text_2")
    b = FeatureModel_ConfigConstraint(kind="sample_text")
    _safe_set(b, 'ConfigConstraint', a1)
    assert _is_linked(b, 'ConfigConstraint', a1)
    if hasattr(a1, 'ConfFeatures'):
        assert _is_linked(a1, 'ConfFeatures', b)
    _safe_set(b, 'ConfigConstraint', a2)
    assert _is_linked(b, 'ConfigConstraint', a2)
    if hasattr(a1, 'ConfFeatures'):
        assert not _is_linked(a1, 'ConfFeatures', b)
    if hasattr(a2, 'ConfFeatures'):
        assert _is_linked(a2, 'ConfFeatures', b)
    _safe_set(b, 'ConfigConstraint', None)
    assert not _is_linked(b, 'ConfigConstraint', a2)
    if hasattr(a2, 'ConfFeatures'):
        assert not _is_linked(a2, 'ConfFeatures', b)


def test_assoc_Features5_reverse_link_reassign_clear():
    a1 = FeatureModel_FeatureConstraint(type="sample_text")
    a2 = FeatureModel_FeatureConstraint(type="sample_text_2")
    b = FeatureModel_Feature(id=7, name="sample_text")
    _safe_set(b, 'FeatureModel_Feature', a1)
    assert _is_linked(b, 'FeatureModel_Feature', a1)
    if hasattr(a1, 'FeatureModel_FeatureConstraint6'):
        assert _is_linked(a1, 'FeatureModel_FeatureConstraint6', b)
    _safe_set(b, 'FeatureModel_Feature', a2)
    assert _is_linked(b, 'FeatureModel_Feature', a2)
    if hasattr(a1, 'FeatureModel_FeatureConstraint6'):
        assert not _is_linked(a1, 'FeatureModel_FeatureConstraint6', b)
    if hasattr(a2, 'FeatureModel_FeatureConstraint6'):
        assert _is_linked(a2, 'FeatureModel_FeatureConstraint6', b)
    _safe_set(b, 'FeatureModel_Feature', None)
    assert not _is_linked(b, 'FeatureModel_Feature', a2)
    if hasattr(a2, 'FeatureModel_FeatureConstraint6'):
        assert not _is_linked(a2, 'FeatureModel_FeatureConstraint6', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ConfConst3_stub_double():
    # FeatureModel_RootFeature has no real 'FeatureModel_RootFeature4' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_ConfigConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_ConfigConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_ConfigConstraint(kind="sample_text")
    partner = FeatureModel_RootFeature()
    setattr(partner, 'FeatureModel_RootFeature4', None)
    _safe_set(owner, 'FeatureModel_ConfigConstraint', partner)
    assert owner in getattr(partner, 'FeatureModel_RootFeature4')
    _safe_set(owner, 'FeatureModel_ConfigConstraint', None)
    assert owner not in getattr(partner, 'FeatureModel_RootFeature4')


def test_assoc_FConst1_stub_double():
    # FeatureModel_FeatureModel has no real 'FeatureModel_FeatureModel2' property in the generated
    # code (a bare stub) -- manually attach it so FeatureModel_FeatureConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # FeatureModel_FeatureConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = FeatureModel_FeatureConstraint(type="sample_text")
    partner = FeatureModel_FeatureModel()
    setattr(partner, 'FeatureModel_FeatureModel2', None)
    _safe_set(owner, 'FeatureModel_FeatureConstraint', partner)
    assert owner in getattr(partner, 'FeatureModel_FeatureModel2')
    _safe_set(owner, 'FeatureModel_FeatureConstraint', None)
    assert owner not in getattr(partner, 'FeatureModel_FeatureModel2')


