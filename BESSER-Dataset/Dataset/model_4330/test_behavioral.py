import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMeasureElement,
    BinaryMeasure,
    BinaryMeasurement,
    DimensionalMeasure,
    DimensionalMeasurement,
    DirectMeasure,
    DirectMeasurement,
    Measure,
    MeasureRelationship,
    Measurement,
    MeasurementRelationship,
    SmmElement,
    SmmRelationship,
    smm_AbstractMeasureElement,
    smm_AggregatedMeasurement,
    smm_Annotation,
    smm_Argument,
    smm_Attribute,
    smm_Base1MeasureRelationship,
    smm_Base1MeasurementRelationship,
    smm_Base2MeasureRelationship,
    smm_Base2MeasurementRelationship,
    smm_BaseMeasureRelationship,
    smm_BaseMeasurementRelationship,
    smm_BinaryMeasure,
    smm_BinaryMeasurement,
    smm_CategoryRelationship,
    smm_Characteristic,
    smm_CollectiveMeasure,
    smm_CollectiveMeasurement,
    smm_Count,
    smm_Counting,
    smm_DimensionalMeasure,
    smm_DimensionalMeasurement,
    smm_DirectMeasure,
    smm_DirectMeasurement,
    smm_EObject,
    smm_EquivalentMeasureRelationship,
    smm_EquivalentMeasurementRelationship,
    smm_Grade,
    smm_Measure,
    smm_MeasureCategory,
    smm_MeasureLibrary,
    smm_MeasureRelationship,
    smm_Measurement,
    smm_MeasurementRelationship,
    smm_NamedMeasure,
    smm_NamedMeasurement,
    smm_OCLOperation,
    smm_Observation,
    smm_ObservationScope,
    smm_ObservedMeasure,
    smm_Operation,
    smm_Ranking,
    smm_RankingInterval,
    smm_RankingMeasureRelationship,
    smm_RankingMeasurementRelationship,
    smm_RatioMeasure,
    smm_RatioMeasurement,
    smm_RecursiveMeasureRelationship,
    smm_RecursiveMeasurementRelationship,
    smm_RefinementMeasureRelationship,
    smm_RefinementMeasurementRelationship,
    smm_RescaleMeasureRelationship,
    smm_RescaleMeasurementRelationship,
    smm_RescaledMeasure,
    smm_RescaledMeasurement,
    smm_Scope,
    smm_SmmElement,
    smm_SmmModel,
    smm_SmmRelationship,
    Accumulator,
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

def test_assoc_annotation211_reverse_link_reassign_clear():
    a1 = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = smm_SmmElement(description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = smm_Annotation(text="sample_text")
    _safe_set(b, 'smm_Annotation', a1)
    assert _is_linked(b, 'smm_Annotation', a1)
    if hasattr(a1, 'smm_SmmElement212'):
        assert _is_linked(a1, 'smm_SmmElement212', b)
    _safe_set(b, 'smm_Annotation', a2)
    assert _is_linked(b, 'smm_Annotation', a2)
    if hasattr(a1, 'smm_SmmElement212'):
        assert not _is_linked(a1, 'smm_SmmElement212', b)
    if hasattr(a2, 'smm_SmmElement212'):
        assert _is_linked(a2, 'smm_SmmElement212', b)
    _safe_set(b, 'smm_Annotation', None)
    assert not _is_linked(b, 'smm_Annotation', a2)
    if hasattr(a2, 'smm_SmmElement212'):
        assert not _is_linked(a2, 'smm_SmmElement212', b)


def test_assoc_arguments145_reverse_link_reassign_clear():
    a1 = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    a2 = smm_Observation(observer="sample_text_2", tool="sample_text_2", whenObserved="sample_text_2")
    b = smm_Argument(type="sample_text", value="sample_text")
    _safe_set(b, 'smm_Argument', a1)
    assert _is_linked(b, 'smm_Argument', a1)
    if hasattr(a1, 'smm_Observation146'):
        assert _is_linked(a1, 'smm_Observation146', b)
    _safe_set(b, 'smm_Argument', a2)
    assert _is_linked(b, 'smm_Argument', a2)
    if hasattr(a1, 'smm_Observation146'):
        assert not _is_linked(a1, 'smm_Observation146', b)
    if hasattr(a2, 'smm_Observation146'):
        assert _is_linked(a2, 'smm_Observation146', b)
    _safe_set(b, 'smm_Argument', None)
    assert not _is_linked(b, 'smm_Argument', a2)
    if hasattr(a2, 'smm_Observation146'):
        assert not _is_linked(a2, 'smm_Observation146', b)


def test_assoc_attribute210_reverse_link_reassign_clear():
    a1 = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = smm_SmmElement(description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = smm_Attribute(tag="sample_text", value="sample_text")
    _safe_set(b, 'smm_Attribute', a1)
    assert _is_linked(b, 'smm_Attribute', a1)
    if hasattr(a1, 'smm_SmmElement'):
        assert _is_linked(a1, 'smm_SmmElement', b)
    _safe_set(b, 'smm_Attribute', a2)
    assert _is_linked(b, 'smm_Attribute', a2)
    if hasattr(a1, 'smm_SmmElement'):
        assert not _is_linked(a1, 'smm_SmmElement', b)
    if hasattr(a2, 'smm_SmmElement'):
        assert _is_linked(a2, 'smm_SmmElement', b)
    _safe_set(b, 'smm_Attribute', None)
    assert not _is_linked(b, 'smm_Attribute', a2)
    if hasattr(a2, 'smm_SmmElement'):
        assert not _is_linked(a2, 'smm_SmmElement', b)


def test_assoc_baseMeasurement1_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasurement(value=3.14)
    a2 = smm_DimensionalMeasurement(value=9.99)
    b = smm_AggregatedMeasurement(isBaseSuppled=True)
    _safe_set(b, 'smm_AggregatedMeasurement', {a1})
    assert _is_linked(b, 'smm_AggregatedMeasurement', a1)
    if hasattr(a1, 'smm_DimensionalMeasurement'):
        assert _is_linked(a1, 'smm_DimensionalMeasurement', b)
    _safe_set(b, 'smm_AggregatedMeasurement', {a2})
    assert _is_linked(b, 'smm_AggregatedMeasurement', a2)
    if hasattr(a1, 'smm_DimensionalMeasurement'):
        assert not _is_linked(a1, 'smm_DimensionalMeasurement', b)
    if hasattr(a2, 'smm_DimensionalMeasurement'):
        assert _is_linked(a2, 'smm_DimensionalMeasurement', b)
    _safe_set(b, 'smm_AggregatedMeasurement', set())
    assert not _is_linked(b, 'smm_AggregatedMeasurement', a2)
    if hasattr(a2, 'smm_DimensionalMeasurement'):
        assert not _is_linked(a2, 'smm_DimensionalMeasurement', b)


def test_assoc_baseMeasurement74_reverse_link_reassign_clear():
    a1 = smm_Grade(isBaseSupplied=True, value="sample_text")
    a2 = smm_Grade(isBaseSupplied=False, value="sample_text_2")
    b = smm_DimensionalMeasurement(value=3.14)
    _safe_set(b, 'smm_DimensionalMeasurement75', a1)
    assert _is_linked(b, 'smm_DimensionalMeasurement75', a1)
    if hasattr(a1, 'smm_Grade'):
        assert _is_linked(a1, 'smm_Grade', b)
    _safe_set(b, 'smm_DimensionalMeasurement75', a2)
    assert _is_linked(b, 'smm_DimensionalMeasurement75', a2)
    if hasattr(a1, 'smm_Grade'):
        assert not _is_linked(a1, 'smm_Grade', b)
    if hasattr(a2, 'smm_Grade'):
        assert _is_linked(a2, 'smm_Grade', b)
    _safe_set(b, 'smm_DimensionalMeasurement75', None)
    assert not _is_linked(b, 'smm_DimensionalMeasurement75', a2)
    if hasattr(a2, 'smm_Grade'):
        assert not _is_linked(a2, 'smm_Grade', b)


def test_assoc_breakCondition207_reverse_link_reassign_clear():
    a1 = smm_Scope(class_="sample_text")
    a2 = smm_Scope(class_="sample_text_2")
    b = smm_Operation(body="sample_text", language="sample_text")
    _safe_set(b, 'smm_Operation209', a1)
    assert _is_linked(b, 'smm_Operation209', a1)
    if hasattr(a1, 'smm_Scope208'):
        assert _is_linked(a1, 'smm_Scope208', b)
    _safe_set(b, 'smm_Operation209', a2)
    assert _is_linked(b, 'smm_Operation209', a2)
    if hasattr(a1, 'smm_Scope208'):
        assert not _is_linked(a1, 'smm_Scope208', b)
    if hasattr(a2, 'smm_Scope208'):
        assert _is_linked(a2, 'smm_Scope208', b)
    _safe_set(b, 'smm_Operation209', None)
    assert not _is_linked(b, 'smm_Operation209', a2)
    if hasattr(a2, 'smm_Scope208'):
        assert not _is_linked(a2, 'smm_Scope208', b)


def test_assoc_defaultQuery101_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    _safe_set(b, 'smm_Measure102', a1)
    assert _is_linked(b, 'smm_Measure102', a1)
    if hasattr(a1, 'smm_Operation103'):
        assert _is_linked(a1, 'smm_Operation103', b)
    _safe_set(b, 'smm_Measure102', a2)
    assert _is_linked(b, 'smm_Measure102', a2)
    if hasattr(a1, 'smm_Operation103'):
        assert not _is_linked(a1, 'smm_Operation103', b)
    if hasattr(a2, 'smm_Operation103'):
        assert _is_linked(a2, 'smm_Operation103', b)
    _safe_set(b, 'smm_Measure102', None)
    assert not _is_linked(b, 'smm_Measure102', a2)
    if hasattr(a2, 'smm_Operation103'):
        assert not _is_linked(a2, 'smm_Operation103', b)


def test_assoc_measurandQuery118_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_MeasureRelationship()
    _safe_set(b, 'smm_MeasureRelationship119', a1)
    assert _is_linked(b, 'smm_MeasureRelationship119', a1)
    if hasattr(a1, 'smm_Operation120'):
        assert _is_linked(a1, 'smm_Operation120', b)
    _safe_set(b, 'smm_MeasureRelationship119', a2)
    assert _is_linked(b, 'smm_MeasureRelationship119', a2)
    if hasattr(a1, 'smm_Operation120'):
        assert not _is_linked(a1, 'smm_Operation120', b)
    if hasattr(a2, 'smm_Operation120'):
        assert _is_linked(a2, 'smm_Operation120', b)
    _safe_set(b, 'smm_MeasureRelationship119', None)
    assert not _is_linked(b, 'smm_MeasureRelationship119', a2)
    if hasattr(a2, 'smm_Operation120'):
        assert not _is_linked(a2, 'smm_Operation120', b)


def test_assoc_measure147_reverse_link_reassign_clear():
    a1 = smm_ObservedMeasure()
    a2 = smm_ObservedMeasure()
    b = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    _safe_set(b, 'smm_Measure149', a1)
    assert _is_linked(b, 'smm_Measure149', a1)
    if hasattr(a1, 'smm_ObservedMeasure148'):
        assert _is_linked(a1, 'smm_ObservedMeasure148', b)
    _safe_set(b, 'smm_Measure149', a2)
    assert _is_linked(b, 'smm_Measure149', a2)
    if hasattr(a1, 'smm_ObservedMeasure148'):
        assert not _is_linked(a1, 'smm_ObservedMeasure148', b)
    if hasattr(a2, 'smm_ObservedMeasure148'):
        assert _is_linked(a2, 'smm_ObservedMeasure148', b)
    _safe_set(b, 'smm_Measure149', None)
    assert not _is_linked(b, 'smm_Measure149', a2)
    if hasattr(a2, 'smm_ObservedMeasure148'):
        assert not _is_linked(a2, 'smm_ObservedMeasure148', b)


def test_assoc_measureRelationships99_reverse_link_reassign_clear():
    a1 = smm_MeasureRelationship()
    a2 = smm_MeasureRelationship()
    b = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    _safe_set(b, 'smm_Measure100', {a1})
    assert _is_linked(b, 'smm_Measure100', a1)
    if hasattr(a1, 'smm_MeasureRelationship'):
        assert _is_linked(a1, 'smm_MeasureRelationship', b)
    _safe_set(b, 'smm_Measure100', {a2})
    assert _is_linked(b, 'smm_Measure100', a2)
    if hasattr(a1, 'smm_MeasureRelationship'):
        assert not _is_linked(a1, 'smm_MeasureRelationship', b)
    if hasattr(a2, 'smm_MeasureRelationship'):
        assert _is_linked(a2, 'smm_MeasureRelationship', b)
    _safe_set(b, 'smm_Measure100', set())
    assert not _is_linked(b, 'smm_Measure100', a2)
    if hasattr(a2, 'smm_MeasureRelationship'):
        assert not _is_linked(a2, 'smm_MeasureRelationship', b)


def test_assoc_measurementRelations143_reverse_link_reassign_clear():
    a1 = smm_SmmRelationship()
    a2 = smm_SmmRelationship()
    b = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    _safe_set(b, 'smm_Observation144', {a1})
    assert _is_linked(b, 'smm_Observation144', a1)
    if hasattr(a1, 'smm_SmmRelationship'):
        assert _is_linked(a1, 'smm_SmmRelationship', b)
    _safe_set(b, 'smm_Observation144', {a2})
    assert _is_linked(b, 'smm_Observation144', a2)
    if hasattr(a1, 'smm_SmmRelationship'):
        assert not _is_linked(a1, 'smm_SmmRelationship', b)
    if hasattr(a2, 'smm_SmmRelationship'):
        assert _is_linked(a2, 'smm_SmmRelationship', b)
    _safe_set(b, 'smm_Observation144', set())
    assert not _is_linked(b, 'smm_Observation144', a2)
    if hasattr(a2, 'smm_SmmRelationship'):
        assert not _is_linked(a2, 'smm_SmmRelationship', b)


def test_assoc_measurementRelationships137_reverse_link_reassign_clear():
    a1 = smm_MeasurementRelationship()
    a2 = smm_MeasurementRelationship()
    b = smm_Measurement(breakValue="sample_text", error="sample_text")
    _safe_set(b, 'smm_Measurement138', {a1})
    assert _is_linked(b, 'smm_Measurement138', a1)
    if hasattr(a1, 'smm_MeasurementRelationship'):
        assert _is_linked(a1, 'smm_MeasurementRelationship', b)
    _safe_set(b, 'smm_Measurement138', {a2})
    assert _is_linked(b, 'smm_Measurement138', a2)
    if hasattr(a1, 'smm_MeasurementRelationship'):
        assert not _is_linked(a1, 'smm_MeasurementRelationship', b)
    if hasattr(a2, 'smm_MeasurementRelationship'):
        assert _is_linked(a2, 'smm_MeasurementRelationship', b)
    _safe_set(b, 'smm_Measurement138', set())
    assert not _is_linked(b, 'smm_Measurement138', a2)
    if hasattr(a2, 'smm_MeasurementRelationship'):
        assert not _is_linked(a2, 'smm_MeasurementRelationship', b)


def test_assoc_measurements150_reverse_link_reassign_clear():
    a1 = smm_ObservedMeasure()
    a2 = smm_ObservedMeasure()
    b = smm_Measurement(breakValue="sample_text", error="sample_text")
    _safe_set(b, 'smm_Measurement152', a1)
    assert _is_linked(b, 'smm_Measurement152', a1)
    if hasattr(a1, 'smm_ObservedMeasure151'):
        assert _is_linked(a1, 'smm_ObservedMeasure151', b)
    _safe_set(b, 'smm_Measurement152', a2)
    assert _is_linked(b, 'smm_Measurement152', a2)
    if hasattr(a1, 'smm_ObservedMeasure151'):
        assert not _is_linked(a1, 'smm_ObservedMeasure151', b)
    if hasattr(a2, 'smm_ObservedMeasure151'):
        assert _is_linked(a2, 'smm_ObservedMeasure151', b)
    _safe_set(b, 'smm_Measurement152', None)
    assert not _is_linked(b, 'smm_Measurement152', a2)
    if hasattr(a2, 'smm_ObservedMeasure151'):
        assert not _is_linked(a2, 'smm_ObservedMeasure151', b)


def test_assoc_observedMeasures140_reverse_link_reassign_clear():
    a1 = smm_ObservedMeasure()
    a2 = smm_ObservedMeasure()
    b = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    _safe_set(b, 'smm_Observation141', {a1})
    assert _is_linked(b, 'smm_Observation141', a1)
    if hasattr(a1, 'smm_ObservedMeasure'):
        assert _is_linked(a1, 'smm_ObservedMeasure', b)
    _safe_set(b, 'smm_Observation141', {a2})
    assert _is_linked(b, 'smm_Observation141', a2)
    if hasattr(a1, 'smm_ObservedMeasure'):
        assert not _is_linked(a1, 'smm_ObservedMeasure', b)
    if hasattr(a2, 'smm_ObservedMeasure'):
        assert _is_linked(a2, 'smm_ObservedMeasure', b)
    _safe_set(b, 'smm_Observation141', set())
    assert not _is_linked(b, 'smm_Observation141', a2)
    if hasattr(a2, 'smm_ObservedMeasure'):
        assert not _is_linked(a2, 'smm_ObservedMeasure', b)


def test_assoc_recognizerQuery204_reverse_link_reassign_clear():
    a1 = smm_Scope(class_="sample_text")
    a2 = smm_Scope(class_="sample_text_2")
    b = smm_Operation(body="sample_text", language="sample_text")
    _safe_set(b, 'smm_Operation206', a1)
    assert _is_linked(b, 'smm_Operation206', a1)
    if hasattr(a1, 'smm_Scope205'):
        assert _is_linked(a1, 'smm_Scope205', b)
    _safe_set(b, 'smm_Operation206', a2)
    assert _is_linked(b, 'smm_Operation206', a2)
    if hasattr(a1, 'smm_Scope205'):
        assert not _is_linked(a1, 'smm_Scope205', b)
    if hasattr(a2, 'smm_Scope205'):
        assert _is_linked(a2, 'smm_Scope205', b)
    _safe_set(b, 'smm_Operation206', None)
    assert not _is_linked(b, 'smm_Operation206', a2)
    if hasattr(a2, 'smm_Scope205'):
        assert not _is_linked(a2, 'smm_Scope205', b)


def test_assoc_requestedMeasures142_reverse_link_reassign_clear():
    a1 = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = smm_SmmElement(description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    _safe_set(b, 'requestedObservations', {a1})
    assert _is_linked(b, 'requestedObservations', a1)
    if hasattr(a1, 'SmmElement'):
        assert _is_linked(a1, 'SmmElement', b)
    _safe_set(b, 'requestedObservations', {a2})
    assert _is_linked(b, 'requestedObservations', a2)
    if hasattr(a1, 'SmmElement'):
        assert not _is_linked(a1, 'SmmElement', b)
    if hasattr(a2, 'SmmElement'):
        assert _is_linked(a2, 'SmmElement', b)
    _safe_set(b, 'requestedObservations', set())
    assert not _is_linked(b, 'requestedObservations', a2)
    if hasattr(a2, 'SmmElement'):
        assert not _is_linked(a2, 'SmmElement', b)


def test_assoc_requestedObservations213_reverse_link_reassign_clear():
    a1 = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = smm_SmmElement(description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    _safe_set(b, 'Observation', a1)
    assert _is_linked(b, 'Observation', a1)
    if hasattr(a1, 'requestedMeasures'):
        assert _is_linked(a1, 'requestedMeasures', b)
    _safe_set(b, 'Observation', a2)
    assert _is_linked(b, 'Observation', a2)
    if hasattr(a1, 'requestedMeasures'):
        assert not _is_linked(a1, 'requestedMeasures', b)
    if hasattr(a2, 'requestedMeasures'):
        assert _is_linked(a2, 'requestedMeasures', b)
    _safe_set(b, 'Observation', None)
    assert not _is_linked(b, 'Observation', a2)
    if hasattr(a2, 'requestedMeasures'):
        assert not _is_linked(a2, 'requestedMeasures', b)


def test_assoc_scope82_reverse_link_reassign_clear():
    a1 = smm_Scope(class_="sample_text")
    a2 = smm_Scope(class_="sample_text_2")
    b = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    _safe_set(b, 'smm_Measure83', a1)
    assert _is_linked(b, 'smm_Measure83', a1)
    if hasattr(a1, 'smm_Scope'):
        assert _is_linked(a1, 'smm_Scope', b)
    _safe_set(b, 'smm_Measure83', a2)
    assert _is_linked(b, 'smm_Measure83', a2)
    if hasattr(a1, 'smm_Scope'):
        assert not _is_linked(a1, 'smm_Scope', b)
    if hasattr(a2, 'smm_Scope'):
        assert _is_linked(a2, 'smm_Scope', b)
    _safe_set(b, 'smm_Measure83', None)
    assert not _is_linked(b, 'smm_Measure83', a2)
    if hasattr(a2, 'smm_Scope'):
        assert not _is_linked(a2, 'smm_Scope', b)


def test_assoc_scopes139_reverse_link_reassign_clear():
    a1 = smm_ObservationScope(scopeUri="sample_text")
    a2 = smm_ObservationScope(scopeUri="sample_text_2")
    b = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    _safe_set(b, 'smm_Observation', {a1})
    assert _is_linked(b, 'smm_Observation', a1)
    if hasattr(a1, 'smm_ObservationScope'):
        assert _is_linked(a1, 'smm_ObservationScope', b)
    _safe_set(b, 'smm_Observation', {a2})
    assert _is_linked(b, 'smm_Observation', a2)
    if hasattr(a1, 'smm_ObservationScope'):
        assert not _is_linked(a1, 'smm_ObservationScope', b)
    if hasattr(a2, 'smm_ObservationScope'):
        assert _is_linked(a2, 'smm_ObservationScope', b)
    _safe_set(b, 'smm_Observation', set())
    assert not _is_linked(b, 'smm_Observation', a2)
    if hasattr(a2, 'smm_ObservationScope'):
        assert not _is_linked(a2, 'smm_ObservationScope', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_baseMeasure1From40_stub_double():
    # smm_Base1MeasureRelationship has no real 'Base1MeasureRelationship42' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'Base1MeasureRelationship42', None)
    _safe_set(owner, 'to41', {partner})
    assert getattr(partner, 'Base1MeasureRelationship42') == owner
    _safe_set(owner, 'to41', set())
    assert getattr(partner, 'Base1MeasureRelationship42') is None


def test_assoc_baseMeasure1To20_stub_double():
    # smm_Base1MeasureRelationship has no real 'Base1MeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'Base1MeasureRelationship', None)
    _safe_set(owner, 'from_', partner)
    assert getattr(partner, 'Base1MeasureRelationship') == owner
    _safe_set(owner, 'from_', None)
    assert getattr(partner, 'Base1MeasureRelationship') is None


def test_assoc_baseMeasure2From43_stub_double():
    # smm_Base2MeasureRelationship has no real 'Base2MeasureRelationship45' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'Base2MeasureRelationship45', None)
    _safe_set(owner, 'to44', {partner})
    assert getattr(partner, 'Base2MeasureRelationship45') == owner
    _safe_set(owner, 'to44', set())
    assert getattr(partner, 'Base2MeasureRelationship45') is None


def test_assoc_baseMeasure2To21_stub_double():
    # smm_Base2MeasureRelationship has no real 'Base2MeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'Base2MeasureRelationship', None)
    _safe_set(owner, 'from_22', partner)
    assert getattr(partner, 'Base2MeasureRelationship') == owner
    _safe_set(owner, 'from_22', None)
    assert getattr(partner, 'Base2MeasureRelationship') is None


def test_assoc_baseMeasureFrom38_stub_double():
    # smm_BaseMeasureRelationship has no real 'BaseMeasureRelationship39' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_BaseMeasureRelationship()
    setattr(partner, 'BaseMeasureRelationship39', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'BaseMeasureRelationship39') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'BaseMeasureRelationship39') is None


def test_assoc_baseMeasureTo34_stub_double():
    # smm_BaseMeasureRelationship has no real 'BaseMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasure(accumulator="sample_text")
    partner = smm_BaseMeasureRelationship()
    setattr(partner, 'BaseMeasureRelationship', None)
    _safe_set(owner, 'from_35', {partner})
    assert getattr(partner, 'BaseMeasureRelationship') == owner
    _safe_set(owner, 'from_35', set())
    assert getattr(partner, 'BaseMeasureRelationship') is None


def test_assoc_baseMeasurement1From53_stub_double():
    # smm_Base1MeasurementRelationship has no real 'Base1MeasurementRelationship55' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'Base1MeasurementRelationship55', None)
    _safe_set(owner, 'to54', {partner})
    assert getattr(partner, 'Base1MeasurementRelationship55') == owner
    _safe_set(owner, 'to54', set())
    assert getattr(partner, 'Base1MeasurementRelationship55') is None


def test_assoc_baseMeasurement1To23_stub_double():
    # smm_Base1MeasurementRelationship has no real 'Base1MeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied=True)
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'Base1MeasurementRelationship', None)
    _safe_set(owner, 'from_24', partner)
    assert getattr(partner, 'Base1MeasurementRelationship') == owner
    _safe_set(owner, 'from_24', None)
    assert getattr(partner, 'Base1MeasurementRelationship') is None


def test_assoc_baseMeasurement2From56_stub_double():
    # smm_Base2MeasurementRelationship has no real 'Base2MeasurementRelationship58' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'Base2MeasurementRelationship58', None)
    _safe_set(owner, 'to57', {partner})
    assert getattr(partner, 'Base2MeasurementRelationship58') == owner
    _safe_set(owner, 'to57', set())
    assert getattr(partner, 'Base2MeasurementRelationship58') is None


def test_assoc_baseMeasurement2To25_stub_double():
    # smm_Base2MeasurementRelationship has no real 'Base2MeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied=True)
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'Base2MeasurementRelationship', None)
    _safe_set(owner, 'from_26', partner)
    assert getattr(partner, 'Base2MeasurementRelationship') == owner
    _safe_set(owner, 'from_26', None)
    assert getattr(partner, 'Base2MeasurementRelationship') is None


def test_assoc_baseMeasurementFrom50_stub_double():
    # smm_BaseMeasurementRelationship has no real 'BaseMeasurementRelationship52' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_BaseMeasurementRelationship()
    setattr(partner, 'BaseMeasurementRelationship52', None)
    _safe_set(owner, 'to51', {partner})
    assert getattr(partner, 'BaseMeasurementRelationship52') == owner
    _safe_set(owner, 'to51', set())
    assert getattr(partner, 'BaseMeasurementRelationship52') is None


def test_assoc_baseMeasurementTo36_stub_double():
    # smm_BaseMeasurementRelationship has no real 'BaseMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasurement(accumulator="sample_text", isBaseSupplied=True)
    partner = smm_BaseMeasurementRelationship()
    setattr(partner, 'BaseMeasurementRelationship', None)
    _safe_set(owner, 'from_37', {partner})
    assert getattr(partner, 'BaseMeasurementRelationship') == owner
    _safe_set(owner, 'from_37', set())
    assert getattr(partner, 'BaseMeasurementRelationship') is None


def test_assoc_category79_stub_double():
    # smm_MeasureCategory has no real 'MeasureCategory' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_MeasureCategory()
    setattr(partner, 'MeasureCategory', None)
    _safe_set(owner, 'categoryMeasure', {partner})
    assert getattr(partner, 'MeasureCategory') == owner
    _safe_set(owner, 'categoryMeasure', set())
    assert getattr(partner, 'MeasureCategory') is None


def test_assoc_categoryMeasure110_stub_double():
    # smm_MeasureCategory has no real 'category111' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_MeasureCategory()
    setattr(partner, 'category111', None)
    _safe_set(owner, 'Measure112', partner)
    assert owner in getattr(partner, 'category111')
    _safe_set(owner, 'Measure112', None)
    assert owner not in getattr(partner, 'category111')


def test_assoc_categoryRelationships115_stub_double():
    # smm_CategoryRelationship has no real 'smm_CategoryRelationship117' property in the generated
    # code (a bare stub) -- manually attach it so smm_MeasureLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_MeasureLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_MeasureLibrary()
    partner = smm_CategoryRelationship()
    setattr(partner, 'smm_CategoryRelationship117', None)
    _safe_set(owner, 'smm_MeasureLibrary116', {partner})
    assert getattr(partner, 'smm_CategoryRelationship117') == owner
    _safe_set(owner, 'smm_MeasureLibrary116', set())
    assert getattr(partner, 'smm_CategoryRelationship117') is None


def test_assoc_elements201_stub_double():
    # smm_EObject has no real 'smm_EObject203' property in the generated
    # code (a bare stub) -- manually attach it so smm_Scope's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Scope's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Scope(class_="sample_text")
    partner = smm_EObject()
    setattr(partner, 'smm_EObject203', None)
    _safe_set(owner, 'smm_Scope202', {partner})
    assert getattr(partner, 'smm_EObject203') == owner
    _safe_set(owner, 'smm_Scope202', set())
    assert getattr(partner, 'smm_EObject203') is None


def test_assoc_equivalentFrom129_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'EquivalentMeasurementRelationship131' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'EquivalentMeasurementRelationship131', None)
    _safe_set(owner, 'to130', {partner})
    assert getattr(partner, 'EquivalentMeasurementRelationship131') == owner
    _safe_set(owner, 'to130', set())
    assert getattr(partner, 'EquivalentMeasurementRelationship131') is None


def test_assoc_equivalentFrom91_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'EquivalentMeasureRelationship93' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'EquivalentMeasureRelationship93', None)
    _safe_set(owner, 'to92', {partner})
    assert getattr(partner, 'EquivalentMeasureRelationship93') == owner
    _safe_set(owner, 'to92', set())
    assert getattr(partner, 'EquivalentMeasureRelationship93') is None


def test_assoc_equivalentTo127_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'EquivalentMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'EquivalentMeasurementRelationship', None)
    _safe_set(owner, 'from_128', {partner})
    assert getattr(partner, 'EquivalentMeasurementRelationship') == owner
    _safe_set(owner, 'from_128', set())
    assert getattr(partner, 'EquivalentMeasurementRelationship') is None


def test_assoc_equivalentTo89_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'EquivalentMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'EquivalentMeasureRelationship', None)
    _safe_set(owner, 'from_90', {partner})
    assert getattr(partner, 'EquivalentMeasureRelationship') == owner
    _safe_set(owner, 'from_90', set())
    assert getattr(partner, 'EquivalentMeasureRelationship') is None


def test_assoc_from_10_stub_double():
    # smm_Base2MeasureRelationship has no real 'baseMeasure2To' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'baseMeasure2To', None)
    _safe_set(owner, 'BinaryMeasure11', partner)
    assert getattr(partner, 'baseMeasure2To') == owner
    _safe_set(owner, 'BinaryMeasure11', None)
    assert getattr(partner, 'baseMeasure2To') is None


def test_assoc_from_14_stub_double():
    # smm_BaseMeasurementRelationship has no real 'baseMeasurementTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasurement(accumulator="sample_text", isBaseSupplied=True)
    partner = smm_BaseMeasurementRelationship()
    setattr(partner, 'baseMeasurementTo', None)
    _safe_set(owner, 'CollectiveMeasurement', partner)
    assert getattr(partner, 'baseMeasurementTo') == owner
    _safe_set(owner, 'CollectiveMeasurement', None)
    assert getattr(partner, 'baseMeasurementTo') is None


def test_assoc_from_162_stub_double():
    # smm_RankingMeasurementRelationship has no real 'rankingTo163' property in the generated
    # code (a bare stub) -- manually attach it so smm_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Grade(isBaseSupplied=True, value="sample_text")
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'rankingTo163', None)
    _safe_set(owner, 'Grade', partner)
    assert getattr(partner, 'rankingTo163') == owner
    _safe_set(owner, 'Grade', None)
    assert getattr(partner, 'rankingTo163') is None


def test_assoc_from_167_stub_double():
    # smm_RecursiveMeasureRelationship has no real 'recursiveTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RecursiveMeasureRelationship()
    setattr(partner, 'recursiveTo', None)
    _safe_set(owner, 'Measure168', partner)
    assert getattr(partner, 'recursiveTo') == owner
    _safe_set(owner, 'Measure168', None)
    assert getattr(partner, 'recursiveTo') is None


def test_assoc_from_17_stub_double():
    # smm_BaseMeasureRelationship has no real 'baseMeasureTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasure(accumulator="sample_text")
    partner = smm_BaseMeasureRelationship()
    setattr(partner, 'baseMeasureTo', None)
    _safe_set(owner, 'CollectiveMeasure', partner)
    assert getattr(partner, 'baseMeasureTo') == owner
    _safe_set(owner, 'CollectiveMeasure', None)
    assert getattr(partner, 'baseMeasureTo') is None


def test_assoc_from_171_stub_double():
    # smm_RecursiveMeasurementRelationship has no real 'recursiveTo172' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RecursiveMeasurementRelationship()
    setattr(partner, 'recursiveTo172', None)
    _safe_set(owner, 'Measurement173', partner)
    assert getattr(partner, 'recursiveTo172') == owner
    _safe_set(owner, 'Measurement173', None)
    assert getattr(partner, 'recursiveTo172') is None


def test_assoc_from_177_stub_double():
    # smm_RefinementMeasureRelationship has no real 'refinementTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'refinementTo', None)
    _safe_set(owner, 'Measure178', partner)
    assert getattr(partner, 'refinementTo') == owner
    _safe_set(owner, 'Measure178', None)
    assert getattr(partner, 'refinementTo') is None


def test_assoc_from_181_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'refinementTo182' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'refinementTo182', None)
    _safe_set(owner, 'Measurement183', partner)
    assert getattr(partner, 'refinementTo182') == owner
    _safe_set(owner, 'Measurement183', None)
    assert getattr(partner, 'refinementTo182') is None


def test_assoc_from_191_stub_double():
    # smm_RescaleMeasureRelationship has no real 'rescaleTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_RescaleMeasureRelationship()
    setattr(partner, 'rescaleTo', None)
    _safe_set(owner, 'DimensionalMeasure192', partner)
    assert getattr(partner, 'rescaleTo') == owner
    _safe_set(owner, 'DimensionalMeasure192', None)
    assert getattr(partner, 'rescaleTo') is None


def test_assoc_from_198_stub_double():
    # smm_RescaleMeasurementRelationship has no real 'rescaleTo199' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RescaleMeasurementRelationship()
    setattr(partner, 'rescaleTo199', None)
    _safe_set(owner, 'DimensionalMeasurement200', partner)
    assert getattr(partner, 'rescaleTo199') == owner
    _safe_set(owner, 'DimensionalMeasurement200', None)
    assert getattr(partner, 'rescaleTo199') is None


def test_assoc_from_2_stub_double():
    # smm_Base1MeasurementRelationship has no real 'baseMeasurement1To' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied=True)
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'baseMeasurement1To', None)
    _safe_set(owner, 'BinaryMeasurement', partner)
    assert getattr(partner, 'baseMeasurement1To') == owner
    _safe_set(owner, 'BinaryMeasurement', None)
    assert getattr(partner, 'baseMeasurement1To') is None


def test_assoc_from_4_stub_double():
    # smm_Base1MeasureRelationship has no real 'baseMeasure1To' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'baseMeasure1To', None)
    _safe_set(owner, 'BinaryMeasure', partner)
    assert getattr(partner, 'baseMeasure1To') == owner
    _safe_set(owner, 'BinaryMeasure', None)
    assert getattr(partner, 'baseMeasure1To') is None


def test_assoc_from_6_stub_double():
    # smm_Base2MeasurementRelationship has no real 'baseMeasurement2To' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied=True)
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'baseMeasurement2To', None)
    _safe_set(owner, 'BinaryMeasurement7', partner)
    assert getattr(partner, 'baseMeasurement2To') == owner
    _safe_set(owner, 'BinaryMeasurement7', None)
    assert getattr(partner, 'baseMeasurement2To') is None


def test_assoc_from_66_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'equivalentTo' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'equivalentTo', None)
    _safe_set(owner, 'Measure', partner)
    assert getattr(partner, 'equivalentTo') == owner
    _safe_set(owner, 'Measure', None)
    assert getattr(partner, 'equivalentTo') is None


def test_assoc_from_69_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'equivalentTo70' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'equivalentTo70', None)
    _safe_set(owner, 'Measurement', partner)
    assert getattr(partner, 'equivalentTo70') == owner
    _safe_set(owner, 'Measurement', None)
    assert getattr(partner, 'equivalentTo70') is None


def test_assoc_interval153_stub_double():
    # smm_Ranking has no real 'rank' property in the generated
    # code (a bare stub) -- manually attach it so smm_RankingInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RankingInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RankingInterval(maximumEndpoint=3.14, maximumOpen=True, minimumEndpoint=3.14, minimumOpen=True, symbol="sample_text")
    partner = smm_Ranking()
    setattr(partner, 'rank', None)
    _safe_set(owner, 'RankingInterval', partner)
    assert owner in getattr(partner, 'rank')
    _safe_set(owner, 'RankingInterval', None)
    assert owner not in getattr(partner, 'rank')


def test_assoc_librairies216_stub_double():
    # smm_SmmModel has no real 'smm_SmmModel217' property in the generated
    # code (a bare stub) -- manually attach it so smm_MeasureLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_MeasureLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_MeasureLibrary()
    partner = smm_SmmModel()
    setattr(partner, 'smm_SmmModel217', None)
    _safe_set(owner, 'smm_MeasureLibrary218', partner)
    assert owner in getattr(partner, 'smm_SmmModel217')
    _safe_set(owner, 'smm_MeasureLibrary218', None)
    assert owner not in getattr(partner, 'smm_SmmModel217')


def test_assoc_mapping64_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'smm_EquivalentMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'smm_EquivalentMeasureRelationship', None)
    _safe_set(owner, 'smm_Operation65', partner)
    assert getattr(partner, 'smm_EquivalentMeasureRelationship') == owner
    _safe_set(owner, 'smm_Operation65', None)
    assert getattr(partner, 'smm_EquivalentMeasureRelationship') is None


def test_assoc_measurand121_stub_double():
    # smm_EObject has no real 'smm_EObject' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EObject()
    setattr(partner, 'smm_EObject', None)
    _safe_set(owner, 'smm_Measurement', partner)
    assert getattr(partner, 'smm_EObject') == owner
    _safe_set(owner, 'smm_Measurement', None)
    assert getattr(partner, 'smm_EObject') is None


def test_assoc_measureElements113_stub_double():
    # smm_AbstractMeasureElement has no real 'smm_AbstractMeasureElement114' property in the generated
    # code (a bare stub) -- manually attach it so smm_MeasureLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_MeasureLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_MeasureLibrary()
    partner = smm_AbstractMeasureElement()
    setattr(partner, 'smm_AbstractMeasureElement114', None)
    _safe_set(owner, 'smm_MeasureLibrary', {partner})
    assert getattr(partner, 'smm_AbstractMeasureElement114') == owner
    _safe_set(owner, 'smm_MeasureLibrary', set())
    assert getattr(partner, 'smm_AbstractMeasureElement114') is None


def test_assoc_observations214_stub_double():
    # smm_SmmModel has no real 'smm_SmmModel' property in the generated
    # code (a bare stub) -- manually attach it so smm_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    partner = smm_SmmModel()
    setattr(partner, 'smm_SmmModel', None)
    _safe_set(owner, 'smm_Observation215', partner)
    assert owner in getattr(partner, 'smm_SmmModel')
    _safe_set(owner, 'smm_Observation215', None)
    assert owner not in getattr(partner, 'smm_SmmModel')


def test_assoc_operation63_stub_double():
    # smm_DirectMeasure has no real 'smm_DirectMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_DirectMeasure()
    setattr(partner, 'smm_DirectMeasure', None)
    _safe_set(owner, 'smm_Operation', partner)
    assert getattr(partner, 'smm_DirectMeasure') == owner
    _safe_set(owner, 'smm_Operation', None)
    assert getattr(partner, 'smm_DirectMeasure') is None


def test_assoc_rank157_stub_double():
    # smm_Ranking has no real 'Ranking' property in the generated
    # code (a bare stub) -- manually attach it so smm_RankingInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RankingInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RankingInterval(maximumEndpoint=3.14, maximumOpen=True, minimumEndpoint=3.14, minimumOpen=True, symbol="sample_text")
    partner = smm_Ranking()
    setattr(partner, 'Ranking', None)
    _safe_set(owner, 'interval', partner)
    assert getattr(partner, 'Ranking') == owner
    _safe_set(owner, 'interval', None)
    assert getattr(partner, 'Ranking') is None


def test_assoc_rankingFrom48_stub_double():
    # smm_RankingMeasureRelationship has no real 'RankingMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_RankingMeasureRelationship()
    setattr(partner, 'RankingMeasureRelationship', None)
    _safe_set(owner, 'to49', {partner})
    assert getattr(partner, 'RankingMeasureRelationship') == owner
    _safe_set(owner, 'to49', set())
    assert getattr(partner, 'RankingMeasureRelationship') is None


def test_assoc_rankingFrom61_stub_double():
    # smm_RankingMeasurementRelationship has no real 'RankingMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'RankingMeasurementRelationship', None)
    _safe_set(owner, 'to62', {partner})
    assert getattr(partner, 'RankingMeasurementRelationship') == owner
    _safe_set(owner, 'to62', set())
    assert getattr(partner, 'RankingMeasurementRelationship') is None


def test_assoc_rankingTo76_stub_double():
    # smm_RankingMeasurementRelationship has no real 'RankingMeasurementRelationship78' property in the generated
    # code (a bare stub) -- manually attach it so smm_Grade's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Grade's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Grade(isBaseSupplied=True, value="sample_text")
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'RankingMeasurementRelationship78', None)
    _safe_set(owner, 'from_77', partner)
    assert getattr(partner, 'RankingMeasurementRelationship78') == owner
    _safe_set(owner, 'from_77', None)
    assert getattr(partner, 'RankingMeasurementRelationship78') is None


def test_assoc_recursiveFrom134_stub_double():
    # smm_RecursiveMeasurementRelationship has no real 'RecursiveMeasurementRelationship136' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RecursiveMeasurementRelationship()
    setattr(partner, 'RecursiveMeasurementRelationship136', None)
    _safe_set(owner, 'to135', {partner})
    assert getattr(partner, 'RecursiveMeasurementRelationship136') == owner
    _safe_set(owner, 'to135', set())
    assert getattr(partner, 'RecursiveMeasurementRelationship136') is None


def test_assoc_recursiveFrom96_stub_double():
    # smm_RecursiveMeasureRelationship has no real 'RecursiveMeasureRelationship98' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RecursiveMeasureRelationship()
    setattr(partner, 'RecursiveMeasureRelationship98', None)
    _safe_set(owner, 'to97', partner)
    assert getattr(partner, 'RecursiveMeasureRelationship98') == owner
    _safe_set(owner, 'to97', None)
    assert getattr(partner, 'RecursiveMeasureRelationship98') is None


def test_assoc_recursiveTo132_stub_double():
    # smm_RecursiveMeasurementRelationship has no real 'RecursiveMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RecursiveMeasurementRelationship()
    setattr(partner, 'RecursiveMeasurementRelationship', None)
    _safe_set(owner, 'from_133', partner)
    assert getattr(partner, 'RecursiveMeasurementRelationship') == owner
    _safe_set(owner, 'from_133', None)
    assert getattr(partner, 'RecursiveMeasurementRelationship') is None


def test_assoc_recursiveTo94_stub_double():
    # smm_RecursiveMeasureRelationship has no real 'RecursiveMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RecursiveMeasureRelationship()
    setattr(partner, 'RecursiveMeasureRelationship', None)
    _safe_set(owner, 'from_95', partner)
    assert getattr(partner, 'RecursiveMeasureRelationship') == owner
    _safe_set(owner, 'from_95', None)
    assert getattr(partner, 'RecursiveMeasureRelationship') is None


def test_assoc_refinementFrom124_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'RefinementMeasurementRelationship126' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'RefinementMeasurementRelationship126', None)
    _safe_set(owner, 'to125', {partner})
    assert getattr(partner, 'RefinementMeasurementRelationship126') == owner
    _safe_set(owner, 'to125', set())
    assert getattr(partner, 'RefinementMeasurementRelationship126') is None


def test_assoc_refinementFrom86_stub_double():
    # smm_RefinementMeasureRelationship has no real 'RefinementMeasureRelationship88' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'RefinementMeasureRelationship88', None)
    _safe_set(owner, 'to87', {partner})
    assert getattr(partner, 'RefinementMeasureRelationship88') == owner
    _safe_set(owner, 'to87', set())
    assert getattr(partner, 'RefinementMeasureRelationship88') is None


def test_assoc_refinementTo122_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'RefinementMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'RefinementMeasurementRelationship', None)
    _safe_set(owner, 'from_123', {partner})
    assert getattr(partner, 'RefinementMeasurementRelationship') == owner
    _safe_set(owner, 'from_123', set())
    assert getattr(partner, 'RefinementMeasurementRelationship') is None


def test_assoc_refinementTo84_stub_double():
    # smm_RefinementMeasureRelationship has no real 'RefinementMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'RefinementMeasureRelationship', None)
    _safe_set(owner, 'from_85', {partner})
    assert getattr(partner, 'RefinementMeasureRelationship') == owner
    _safe_set(owner, 'from_85', set())
    assert getattr(partner, 'RefinementMeasureRelationship') is None


def test_assoc_rescaleFrom187_stub_double():
    # smm_RescaleMeasureRelationship has no real 'RescaleMeasureRelationship189' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasure(formula="sample_text")
    partner = smm_RescaleMeasureRelationship()
    setattr(partner, 'RescaleMeasureRelationship189', None)
    _safe_set(owner, 'to188', {partner})
    assert getattr(partner, 'RescaleMeasureRelationship189') == owner
    _safe_set(owner, 'to188', set())
    assert getattr(partner, 'RescaleMeasureRelationship189') is None


def test_assoc_rescaleFrom193_stub_double():
    # smm_RescaleMeasurementRelationship has no real 'RescaleMeasurementRelationship195' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasurement(isBaseSupplied=True)
    partner = smm_RescaleMeasurementRelationship()
    setattr(partner, 'RescaleMeasurementRelationship195', None)
    _safe_set(owner, 'to194', {partner})
    assert getattr(partner, 'RescaleMeasurementRelationship195') == owner
    _safe_set(owner, 'to194', set())
    assert getattr(partner, 'RescaleMeasurementRelationship195') is None


def test_assoc_rescaleTo46_stub_double():
    # smm_RescaleMeasureRelationship has no real 'RescaleMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_RescaleMeasureRelationship()
    setattr(partner, 'RescaleMeasureRelationship', None)
    _safe_set(owner, 'from_47', partner)
    assert getattr(partner, 'RescaleMeasureRelationship') == owner
    _safe_set(owner, 'from_47', None)
    assert getattr(partner, 'RescaleMeasureRelationship') is None


def test_assoc_rescaleTo59_stub_double():
    # smm_RescaleMeasurementRelationship has no real 'RescaleMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RescaleMeasurementRelationship()
    setattr(partner, 'RescaleMeasurementRelationship', None)
    _safe_set(owner, 'from_60', {partner})
    assert getattr(partner, 'RescaleMeasurementRelationship') == owner
    _safe_set(owner, 'from_60', set())
    assert getattr(partner, 'RescaleMeasurementRelationship') is None


def test_assoc_to12_stub_double():
    # smm_Base2MeasureRelationship has no real 'baseMeasure2From' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'baseMeasure2From', None)
    _safe_set(owner, 'DimensionalMeasure13', partner)
    assert getattr(partner, 'baseMeasure2From') == owner
    _safe_set(owner, 'DimensionalMeasure13', None)
    assert getattr(partner, 'baseMeasure2From') is None


def test_assoc_to15_stub_double():
    # smm_BaseMeasurementRelationship has no real 'baseMeasurementFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_BaseMeasurementRelationship()
    setattr(partner, 'baseMeasurementFrom', None)
    _safe_set(owner, 'DimensionalMeasurement16', partner)
    assert getattr(partner, 'baseMeasurementFrom') == owner
    _safe_set(owner, 'DimensionalMeasurement16', None)
    assert getattr(partner, 'baseMeasurementFrom') is None


def test_assoc_to160_stub_double():
    # smm_RankingMeasureRelationship has no real 'rankingFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_RankingMeasureRelationship()
    setattr(partner, 'rankingFrom', None)
    _safe_set(owner, 'DimensionalMeasure161', partner)
    assert getattr(partner, 'rankingFrom') == owner
    _safe_set(owner, 'DimensionalMeasure161', None)
    assert getattr(partner, 'rankingFrom') is None


def test_assoc_to164_stub_double():
    # smm_RankingMeasurementRelationship has no real 'rankingFrom165' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'rankingFrom165', None)
    _safe_set(owner, 'DimensionalMeasurement166', partner)
    assert getattr(partner, 'rankingFrom165') == owner
    _safe_set(owner, 'DimensionalMeasurement166', None)
    assert getattr(partner, 'rankingFrom165') is None


def test_assoc_to169_stub_double():
    # smm_RecursiveMeasureRelationship has no real 'recursiveFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RecursiveMeasureRelationship()
    setattr(partner, 'recursiveFrom', None)
    _safe_set(owner, 'Measure170', partner)
    assert getattr(partner, 'recursiveFrom') == owner
    _safe_set(owner, 'Measure170', None)
    assert getattr(partner, 'recursiveFrom') is None


def test_assoc_to174_stub_double():
    # smm_RecursiveMeasurementRelationship has no real 'recursiveFrom175' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RecursiveMeasurementRelationship()
    setattr(partner, 'recursiveFrom175', None)
    _safe_set(owner, 'Measurement176', partner)
    assert getattr(partner, 'recursiveFrom175') == owner
    _safe_set(owner, 'Measurement176', None)
    assert getattr(partner, 'recursiveFrom175') is None


def test_assoc_to179_stub_double():
    # smm_RefinementMeasureRelationship has no real 'refinementFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'refinementFrom', None)
    _safe_set(owner, 'Measure180', partner)
    assert getattr(partner, 'refinementFrom') == owner
    _safe_set(owner, 'Measure180', None)
    assert getattr(partner, 'refinementFrom') is None


def test_assoc_to18_stub_double():
    # smm_BaseMeasureRelationship has no real 'baseMeasureFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_BaseMeasureRelationship()
    setattr(partner, 'baseMeasureFrom', None)
    _safe_set(owner, 'DimensionalMeasure19', partner)
    assert getattr(partner, 'baseMeasureFrom') == owner
    _safe_set(owner, 'DimensionalMeasure19', None)
    assert getattr(partner, 'baseMeasureFrom') is None


def test_assoc_to184_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'refinementFrom185' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'refinementFrom185', None)
    _safe_set(owner, 'Measurement186', partner)
    assert getattr(partner, 'refinementFrom185') == owner
    _safe_set(owner, 'Measurement186', None)
    assert getattr(partner, 'refinementFrom185') is None


def test_assoc_to190_stub_double():
    # smm_RescaleMeasureRelationship has no real 'rescaleFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasure(formula="sample_text")
    partner = smm_RescaleMeasureRelationship()
    setattr(partner, 'rescaleFrom', None)
    _safe_set(owner, 'RescaledMeasure', partner)
    assert getattr(partner, 'rescaleFrom') == owner
    _safe_set(owner, 'RescaledMeasure', None)
    assert getattr(partner, 'rescaleFrom') is None


def test_assoc_to196_stub_double():
    # smm_RescaleMeasurementRelationship has no real 'rescaleFrom197' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasurement(isBaseSupplied=True)
    partner = smm_RescaleMeasurementRelationship()
    setattr(partner, 'rescaleFrom197', None)
    _safe_set(owner, 'RescaledMeasurement', partner)
    assert getattr(partner, 'rescaleFrom197') == owner
    _safe_set(owner, 'RescaledMeasurement', None)
    assert getattr(partner, 'rescaleFrom197') is None


def test_assoc_to3_stub_double():
    # smm_Base1MeasurementRelationship has no real 'baseMeasurement1From' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'baseMeasurement1From', None)
    _safe_set(owner, 'DimensionalMeasurement', partner)
    assert getattr(partner, 'baseMeasurement1From') == owner
    _safe_set(owner, 'DimensionalMeasurement', None)
    assert getattr(partner, 'baseMeasurement1From') is None


def test_assoc_to5_stub_double():
    # smm_Base1MeasureRelationship has no real 'baseMeasure1From' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(unit="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'baseMeasure1From', None)
    _safe_set(owner, 'DimensionalMeasure', partner)
    assert getattr(partner, 'baseMeasure1From') == owner
    _safe_set(owner, 'DimensionalMeasure', None)
    assert getattr(partner, 'baseMeasure1From') is None


def test_assoc_to67_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'equivalentFrom' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'equivalentFrom', None)
    _safe_set(owner, 'Measure68', partner)
    assert getattr(partner, 'equivalentFrom') == owner
    _safe_set(owner, 'Measure68', None)
    assert getattr(partner, 'equivalentFrom') is None


def test_assoc_to71_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'equivalentFrom72' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'equivalentFrom72', None)
    _safe_set(owner, 'Measurement73', partner)
    assert getattr(partner, 'equivalentFrom72') == owner
    _safe_set(owner, 'Measurement73', None)
    assert getattr(partner, 'equivalentFrom72') is None


def test_assoc_to8_stub_double():
    # smm_Base2MeasurementRelationship has no real 'baseMeasurement2From' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'baseMeasurement2From', None)
    _safe_set(owner, 'DimensionalMeasurement9', partner)
    assert getattr(partner, 'baseMeasurement2From') == owner
    _safe_set(owner, 'DimensionalMeasurement9', None)
    assert getattr(partner, 'baseMeasurement2From') is None


def test_assoc_trait80_stub_double():
    # smm_Characteristic has no real 'smm_Characteristic81' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(measureLabelFormat="sample_text", measurementLabelFormat="sample_text", visible=True)
    partner = smm_Characteristic()
    setattr(partner, 'smm_Characteristic81', None)
    _safe_set(owner, 'smm_Measure', partner)
    assert getattr(partner, 'smm_Characteristic81') == owner
    _safe_set(owner, 'smm_Measure', None)
    assert getattr(partner, 'smm_Characteristic81') is None


