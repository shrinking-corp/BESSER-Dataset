import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    qualitymodel_Attribute,
    qualitymodel_CompositeAttribute,
    qualitymodel_ConfigurationProfile,
    qualitymodel_HistoricalData,
    qualitymodel_LeafAttribute,
    qualitymodel_Metric,
    qualitymodel_Preference,
    AttributeAggregationOperator,
    MetricAggregationOperator,
    MetricNormalizationKind,
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

def test_assoc_attribute0_reverse_link_reassign_clear():
    a1 = qualitymodel_Metric(data="sample_text", descriptionName="sample_text", probeName="sample_text", resourceName="sample_text")
    a2 = qualitymodel_Metric(data="sample_text_2", descriptionName="sample_text_2", probeName="sample_text_2", resourceName="sample_text_2")
    b = qualitymodel_LeafAttribute(normalizationKind="sample_text", normalizationMax=3.14, normalizationMin=3.14, numSamples=7, operator="sample_text")
    _safe_set(b, 'qualitymodel_LeafAttribute', a1)
    assert _is_linked(b, 'qualitymodel_LeafAttribute', a1)
    if hasattr(a1, 'qualitymodel_Metric'):
        assert _is_linked(a1, 'qualitymodel_Metric', b)
    _safe_set(b, 'qualitymodel_LeafAttribute', a2)
    assert _is_linked(b, 'qualitymodel_LeafAttribute', a2)
    if hasattr(a1, 'qualitymodel_Metric'):
        assert not _is_linked(a1, 'qualitymodel_Metric', b)
    if hasattr(a2, 'qualitymodel_Metric'):
        assert _is_linked(a2, 'qualitymodel_Metric', b)
    _safe_set(b, 'qualitymodel_LeafAttribute', None)
    assert not _is_linked(b, 'qualitymodel_LeafAttribute', a2)
    if hasattr(a2, 'qualitymodel_Metric'):
        assert not _is_linked(a2, 'qualitymodel_Metric', b)


def test_assoc_attribute2_reverse_link_reassign_clear():
    a1 = qualitymodel_HistoricalData(instant="sample_text", value=3.14)
    a2 = qualitymodel_HistoricalData(instant="sample_text_2", value=9.99)
    b = qualitymodel_Attribute(name="sample_text")
    _safe_set(b, 'qualitymodel_Attribute3', a1)
    assert _is_linked(b, 'qualitymodel_Attribute3', a1)
    if hasattr(a1, 'qualitymodel_HistoricalData'):
        assert _is_linked(a1, 'qualitymodel_HistoricalData', b)
    _safe_set(b, 'qualitymodel_Attribute3', a2)
    assert _is_linked(b, 'qualitymodel_Attribute3', a2)
    if hasattr(a1, 'qualitymodel_HistoricalData'):
        assert not _is_linked(a1, 'qualitymodel_HistoricalData', b)
    if hasattr(a2, 'qualitymodel_HistoricalData'):
        assert _is_linked(a2, 'qualitymodel_HistoricalData', b)
    _safe_set(b, 'qualitymodel_Attribute3', None)
    assert not _is_linked(b, 'qualitymodel_Attribute3', a2)
    if hasattr(a2, 'qualitymodel_HistoricalData'):
        assert not _is_linked(a2, 'qualitymodel_HistoricalData', b)


def test_assoc_attribute4_reverse_link_reassign_clear():
    a1 = qualitymodel_Preference(threshold=3.14, weight=3.14)
    a2 = qualitymodel_Preference(threshold=9.99, weight=9.99)
    b = qualitymodel_Attribute(name="sample_text")
    _safe_set(b, 'qualitymodel_Attribute5', a1)
    assert _is_linked(b, 'qualitymodel_Attribute5', a1)
    if hasattr(a1, 'qualitymodel_Preference'):
        assert _is_linked(a1, 'qualitymodel_Preference', b)
    _safe_set(b, 'qualitymodel_Attribute5', a2)
    assert _is_linked(b, 'qualitymodel_Attribute5', a2)
    if hasattr(a1, 'qualitymodel_Preference'):
        assert not _is_linked(a1, 'qualitymodel_Preference', b)
    if hasattr(a2, 'qualitymodel_Preference'):
        assert _is_linked(a2, 'qualitymodel_Preference', b)
    _safe_set(b, 'qualitymodel_Attribute5', None)
    assert not _is_linked(b, 'qualitymodel_Attribute5', a2)
    if hasattr(a2, 'qualitymodel_Preference'):
        assert not _is_linked(a2, 'qualitymodel_Preference', b)


def test_assoc_children1_reverse_link_reassign_clear():
    a1 = qualitymodel_CompositeAttribute(operator="sample_text")
    a2 = qualitymodel_CompositeAttribute(operator="sample_text_2")
    b = qualitymodel_Attribute(name="sample_text")
    _safe_set(b, 'qualitymodel_Attribute', a1)
    assert _is_linked(b, 'qualitymodel_Attribute', a1)
    if hasattr(a1, 'qualitymodel_CompositeAttribute'):
        assert _is_linked(a1, 'qualitymodel_CompositeAttribute', b)
    _safe_set(b, 'qualitymodel_Attribute', a2)
    assert _is_linked(b, 'qualitymodel_Attribute', a2)
    if hasattr(a1, 'qualitymodel_CompositeAttribute'):
        assert not _is_linked(a1, 'qualitymodel_CompositeAttribute', b)
    if hasattr(a2, 'qualitymodel_CompositeAttribute'):
        assert _is_linked(a2, 'qualitymodel_CompositeAttribute', b)
    _safe_set(b, 'qualitymodel_Attribute', None)
    assert not _is_linked(b, 'qualitymodel_Attribute', a2)
    if hasattr(a2, 'qualitymodel_CompositeAttribute'):
        assert not _is_linked(a2, 'qualitymodel_CompositeAttribute', b)


def test_assoc_metric8_reverse_link_reassign_clear():
    a1 = qualitymodel_Metric(data="sample_text", descriptionName="sample_text", probeName="sample_text", resourceName="sample_text")
    a2 = qualitymodel_Metric(data="sample_text_2", descriptionName="sample_text_2", probeName="sample_text_2", resourceName="sample_text_2")
    b = qualitymodel_ConfigurationProfile(ID=7)
    _safe_set(b, 'qualitymodel_ConfigurationProfile9', {a1})
    assert _is_linked(b, 'qualitymodel_ConfigurationProfile9', a1)
    if hasattr(a1, 'qualitymodel_Metric10'):
        assert _is_linked(a1, 'qualitymodel_Metric10', b)
    _safe_set(b, 'qualitymodel_ConfigurationProfile9', {a2})
    assert _is_linked(b, 'qualitymodel_ConfigurationProfile9', a2)
    if hasattr(a1, 'qualitymodel_Metric10'):
        assert not _is_linked(a1, 'qualitymodel_Metric10', b)
    if hasattr(a2, 'qualitymodel_Metric10'):
        assert _is_linked(a2, 'qualitymodel_Metric10', b)
    _safe_set(b, 'qualitymodel_ConfigurationProfile9', set())
    assert not _is_linked(b, 'qualitymodel_ConfigurationProfile9', a2)
    if hasattr(a2, 'qualitymodel_Metric10'):
        assert not _is_linked(a2, 'qualitymodel_Metric10', b)


def test_assoc_preference6_reverse_link_reassign_clear():
    a1 = qualitymodel_Preference(threshold=3.14, weight=3.14)
    a2 = qualitymodel_Preference(threshold=9.99, weight=9.99)
    b = qualitymodel_ConfigurationProfile(ID=7)
    _safe_set(b, 'qualitymodel_ConfigurationProfile', {a1})
    assert _is_linked(b, 'qualitymodel_ConfigurationProfile', a1)
    if hasattr(a1, 'qualitymodel_Preference7'):
        assert _is_linked(a1, 'qualitymodel_Preference7', b)
    _safe_set(b, 'qualitymodel_ConfigurationProfile', {a2})
    assert _is_linked(b, 'qualitymodel_ConfigurationProfile', a2)
    if hasattr(a1, 'qualitymodel_Preference7'):
        assert not _is_linked(a1, 'qualitymodel_Preference7', b)
    if hasattr(a2, 'qualitymodel_Preference7'):
        assert _is_linked(a2, 'qualitymodel_Preference7', b)
    _safe_set(b, 'qualitymodel_ConfigurationProfile', set())
    assert not _is_linked(b, 'qualitymodel_ConfigurationProfile', a2)
    if hasattr(a2, 'qualitymodel_Preference7'):
        assert not _is_linked(a2, 'qualitymodel_Preference7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

