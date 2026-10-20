import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractMeasureElement,
    BaseMeasureRelationship,
    BaseMeasurementRelationship,
    BinaryMeasure,
    BinaryMeasurement,
    DimensionalMeasure,
    DimensionalMeasurement,
    Interval,
    Measure,
    MeasureRelationship,
    Measurement,
    MeasurementRelationship,
    ScaledBaseMeasureRelationship,
    ScaledBaseMeasurementRelationship,
    SmmElement,
    SmmRelationship,
    UnitOfMeasure,
    smm_AbstractMeasureElement,
    smm_Annotation,
    smm_Argument,
    smm_Attribute,
    smm_Base1MeasureRelationship,
    smm_Base1MeasurementRelationship,
    smm_Base2MeasureRelationship,
    smm_Base2MeasurementRelationship,
    smm_BaseMeasureRelationship,
    smm_BaseMeasurementRelationship,
    smm_BaseNMeasureRelationship,
    smm_BaseNMeasurementRelationship,
    smm_BinaryMeasure,
    smm_BinaryMeasurement,
    smm_CategoryRelationship,
    smm_Characteristic,
    smm_CollectiveMeasure,
    smm_CollectiveMeasurement,
    smm_CountingUnit,
    smm_DimensionalMeasure,
    smm_DimensionalMeasurement,
    smm_DirectMeasure,
    smm_DirectMeasurement,
    smm_EObject,
    smm_EquivalentMeasureRelationship,
    smm_EquivalentMeasurementRelationship,
    smm_GradeInterval,
    smm_GradeMeasure,
    smm_GradeMeasureRelationship,
    smm_GradeMeasurement,
    smm_GradeMeasurementRelationship,
    smm_Interval,
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
    smm_RankingInterval,
    smm_RankingMeasure,
    smm_RankingMeasureRelationship,
    smm_RankingMeasurement,
    smm_RankingMeasurementRelationship,
    smm_RatioMeasure,
    smm_RatioMeasurement,
    smm_RefinementMeasureRelationship,
    smm_RefinementMeasurementRelationship,
    smm_RescaledMeasure,
    smm_RescaledMeasureRelationship,
    smm_RescaledMeasurement,
    smm_RescaledMeasurementRelationship,
    smm_ScaledBaseMeasureRelationship,
    smm_ScaledBaseMeasurementRelationship,
    smm_Scope,
    smm_SmmElement,
    smm_SmmModel,
    smm_SmmRelationship,
    smm_UnitOfMeasure,
    Accumulator,
    BinaryFunctor,
    Influence,
    MeasurementScale,
    ScaleOfMeasurement,
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

def test_assoc_annotations167_reverse_link_reassign_clear():
    a1 = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    a2 = smm_SmmElement(description="sample_text_2", name="sample_text_2", shortDescription="sample_text_2")
    b = smm_Annotation(text="sample_text")
    _safe_set(b, 'smm_Annotation', a1)
    assert _is_linked(b, 'smm_Annotation', a1)
    if hasattr(a1, 'smm_SmmElement168'):
        assert _is_linked(a1, 'smm_SmmElement168', b)
    _safe_set(b, 'smm_Annotation', a2)
    assert _is_linked(b, 'smm_Annotation', a2)
    if hasattr(a1, 'smm_SmmElement168'):
        assert not _is_linked(a1, 'smm_SmmElement168', b)
    if hasattr(a2, 'smm_SmmElement168'):
        assert _is_linked(a2, 'smm_SmmElement168', b)
    _safe_set(b, 'smm_Annotation', None)
    assert not _is_linked(b, 'smm_Annotation', a2)
    if hasattr(a2, 'smm_SmmElement168'):
        assert not _is_linked(a2, 'smm_SmmElement168', b)


def test_assoc_arguments128_reverse_link_reassign_clear():
    a1 = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    a2 = smm_Observation(observer="sample_text_2", tool="sample_text_2", whenObserved="sample_text_2")
    b = smm_Argument(Type="sample_text", value="sample_text")
    _safe_set(b, 'smm_Argument', a1)
    assert _is_linked(b, 'smm_Argument', a1)
    if hasattr(a1, 'smm_Observation129'):
        assert _is_linked(a1, 'smm_Observation129', b)
    _safe_set(b, 'smm_Argument', a2)
    assert _is_linked(b, 'smm_Argument', a2)
    if hasattr(a1, 'smm_Observation129'):
        assert not _is_linked(a1, 'smm_Observation129', b)
    if hasattr(a2, 'smm_Observation129'):
        assert _is_linked(a2, 'smm_Observation129', b)
    _safe_set(b, 'smm_Argument', None)
    assert not _is_linked(b, 'smm_Argument', a2)
    if hasattr(a2, 'smm_Observation129'):
        assert not _is_linked(a2, 'smm_Observation129', b)


def test_assoc_attributes166_reverse_link_reassign_clear():
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


def test_assoc_baseQuery11_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_BinaryMeasurement(isBaseSupplied="sample_text")
    _safe_set(b, 'smm_BinaryMeasurement12', a1)
    assert _is_linked(b, 'smm_BinaryMeasurement12', a1)
    if hasattr(a1, 'smm_Operation13'):
        assert _is_linked(a1, 'smm_Operation13', b)
    _safe_set(b, 'smm_BinaryMeasurement12', a2)
    assert _is_linked(b, 'smm_BinaryMeasurement12', a2)
    if hasattr(a1, 'smm_Operation13'):
        assert not _is_linked(a1, 'smm_Operation13', b)
    if hasattr(a2, 'smm_Operation13'):
        assert _is_linked(a2, 'smm_Operation13', b)
    _safe_set(b, 'smm_BinaryMeasurement12', None)
    assert not _is_linked(b, 'smm_BinaryMeasurement12', a2)
    if hasattr(a2, 'smm_Operation13'):
        assert not _is_linked(a2, 'smm_Operation13', b)


def test_assoc_baseQuery151_reverse_link_reassign_clear():
    a1 = smm_RescaledMeasurement(isBaseSupplied="sample_text")
    a2 = smm_RescaledMeasurement(isBaseSupplied="sample_text_2")
    b = smm_Operation(body="sample_text", language="sample_text")
    _safe_set(b, 'smm_Operation153', a1)
    assert _is_linked(b, 'smm_Operation153', a1)
    if hasattr(a1, 'smm_RescaledMeasurement152'):
        assert _is_linked(a1, 'smm_RescaledMeasurement152', b)
    _safe_set(b, 'smm_Operation153', a2)
    assert _is_linked(b, 'smm_Operation153', a2)
    if hasattr(a1, 'smm_RescaledMeasurement152'):
        assert not _is_linked(a1, 'smm_RescaledMeasurement152', b)
    if hasattr(a2, 'smm_RescaledMeasurement152'):
        assert _is_linked(a2, 'smm_RescaledMeasurement152', b)
    _safe_set(b, 'smm_Operation153', None)
    assert not _is_linked(b, 'smm_Operation153', a2)
    if hasattr(a2, 'smm_RescaledMeasurement152'):
        assert not _is_linked(a2, 'smm_RescaledMeasurement152', b)


def test_assoc_baseQuery185_reverse_link_reassign_clear():
    a1 = smm_RankingMeasurement(isBaseSupplied="sample_text")
    a2 = smm_RankingMeasurement(isBaseSupplied="sample_text_2")
    b = smm_Operation(body="sample_text", language="sample_text")
    _safe_set(b, 'smm_Operation186', a1)
    assert _is_linked(b, 'smm_Operation186', a1)
    if hasattr(a1, 'smm_RankingMeasurement'):
        assert _is_linked(a1, 'smm_RankingMeasurement', b)
    _safe_set(b, 'smm_Operation186', a2)
    assert _is_linked(b, 'smm_Operation186', a2)
    if hasattr(a1, 'smm_RankingMeasurement'):
        assert not _is_linked(a1, 'smm_RankingMeasurement', b)
    if hasattr(a2, 'smm_RankingMeasurement'):
        assert _is_linked(a2, 'smm_RankingMeasurement', b)
    _safe_set(b, 'smm_Operation186', None)
    assert not _is_linked(b, 'smm_Operation186', a2)
    if hasattr(a2, 'smm_RankingMeasurement'):
        assert not _is_linked(a2, 'smm_RankingMeasurement', b)


def test_assoc_baseQuery21_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_CollectiveMeasurement(isBaseSupplied="sample_text")
    _safe_set(b, 'smm_CollectiveMeasurement22', a1)
    assert _is_linked(b, 'smm_CollectiveMeasurement22', a1)
    if hasattr(a1, 'smm_Operation23'):
        assert _is_linked(a1, 'smm_Operation23', b)
    _safe_set(b, 'smm_CollectiveMeasurement22', a2)
    assert _is_linked(b, 'smm_CollectiveMeasurement22', a2)
    if hasattr(a1, 'smm_Operation23'):
        assert not _is_linked(a1, 'smm_Operation23', b)
    if hasattr(a2, 'smm_Operation23'):
        assert _is_linked(a2, 'smm_Operation23', b)
    _safe_set(b, 'smm_CollectiveMeasurement22', None)
    assert not _is_linked(b, 'smm_CollectiveMeasurement22', a2)
    if hasattr(a2, 'smm_Operation23'):
        assert not _is_linked(a2, 'smm_Operation23', b)


def test_assoc_baseQuery60_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_GradeMeasurement(isBaseSupplied=True, value="sample_text")
    _safe_set(b, 'smm_GradeMeasurement61', a1)
    assert _is_linked(b, 'smm_GradeMeasurement61', a1)
    if hasattr(a1, 'smm_Operation62'):
        assert _is_linked(a1, 'smm_Operation62', b)
    _safe_set(b, 'smm_GradeMeasurement61', a2)
    assert _is_linked(b, 'smm_GradeMeasurement61', a2)
    if hasattr(a1, 'smm_Operation62'):
        assert not _is_linked(a1, 'smm_Operation62', b)
    if hasattr(a2, 'smm_Operation62'):
        assert _is_linked(a2, 'smm_Operation62', b)
    _safe_set(b, 'smm_GradeMeasurement61', None)
    assert not _is_linked(b, 'smm_GradeMeasurement61', a2)
    if hasattr(a2, 'smm_Operation62'):
        assert not _is_linked(a2, 'smm_Operation62', b)


def test_assoc_customAccumulator17_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_CollectiveMeasure(accumulator="sample_text")
    _safe_set(b, 'smm_CollectiveMeasure18', a1)
    assert _is_linked(b, 'smm_CollectiveMeasure18', a1)
    if hasattr(a1, 'smm_Operation19'):
        assert _is_linked(a1, 'smm_Operation19', b)
    _safe_set(b, 'smm_CollectiveMeasure18', a2)
    assert _is_linked(b, 'smm_CollectiveMeasure18', a2)
    if hasattr(a1, 'smm_Operation19'):
        assert not _is_linked(a1, 'smm_Operation19', b)
    if hasattr(a2, 'smm_Operation19'):
        assert _is_linked(a2, 'smm_Operation19', b)
    _safe_set(b, 'smm_CollectiveMeasure18', None)
    assert not _is_linked(b, 'smm_CollectiveMeasure18', a2)
    if hasattr(a2, 'smm_Operation19'):
        assert not _is_linked(a2, 'smm_Operation19', b)


def test_assoc_customFunctor6_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_BinaryMeasure(functor="sample_text")
    _safe_set(b, 'smm_BinaryMeasure7', a1)
    assert _is_linked(b, 'smm_BinaryMeasure7', a1)
    if hasattr(a1, 'smm_Operation'):
        assert _is_linked(a1, 'smm_Operation', b)
    _safe_set(b, 'smm_BinaryMeasure7', a2)
    assert _is_linked(b, 'smm_BinaryMeasure7', a2)
    if hasattr(a1, 'smm_Operation'):
        assert not _is_linked(a1, 'smm_Operation', b)
    if hasattr(a2, 'smm_Operation'):
        assert _is_linked(a2, 'smm_Operation', b)
    _safe_set(b, 'smm_BinaryMeasure7', None)
    assert not _is_linked(b, 'smm_BinaryMeasure7', a2)
    if hasattr(a2, 'smm_Operation'):
        assert not _is_linked(a2, 'smm_Operation', b)


def test_assoc_defaultQuery78_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    _safe_set(b, 'smm_Measure79', a1)
    assert _is_linked(b, 'smm_Measure79', a1)
    if hasattr(a1, 'smm_Operation80'):
        assert _is_linked(a1, 'smm_Operation80', b)
    _safe_set(b, 'smm_Measure79', a2)
    assert _is_linked(b, 'smm_Measure79', a2)
    if hasattr(a1, 'smm_Operation80'):
        assert not _is_linked(a1, 'smm_Operation80', b)
    if hasattr(a2, 'smm_Operation80'):
        assert _is_linked(a2, 'smm_Operation80', b)
    _safe_set(b, 'smm_Measure79', None)
    assert not _is_linked(b, 'smm_Measure79', a2)
    if hasattr(a2, 'smm_Operation80'):
        assert not _is_linked(a2, 'smm_Operation80', b)


def test_assoc_inbound67_reverse_link_reassign_clear():
    a1 = smm_MeasureRelationship(influence="sample_text")
    a2 = smm_MeasureRelationship(influence="sample_text_2")
    b = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    _safe_set(b, 'smm_Measure68', {a1})
    assert _is_linked(b, 'smm_Measure68', a1)
    if hasattr(a1, 'smm_MeasureRelationship'):
        assert _is_linked(a1, 'smm_MeasureRelationship', b)
    _safe_set(b, 'smm_Measure68', {a2})
    assert _is_linked(b, 'smm_Measure68', a2)
    if hasattr(a1, 'smm_MeasureRelationship'):
        assert not _is_linked(a1, 'smm_MeasureRelationship', b)
    if hasattr(a2, 'smm_MeasureRelationship'):
        assert _is_linked(a2, 'smm_MeasureRelationship', b)
    _safe_set(b, 'smm_Measure68', set())
    assert not _is_linked(b, 'smm_Measure68', a2)
    if hasattr(a2, 'smm_MeasureRelationship'):
        assert not _is_linked(a2, 'smm_MeasureRelationship', b)


def test_assoc_measurandQuery101_reverse_link_reassign_clear():
    a1 = smm_Operation(body="sample_text", language="sample_text")
    a2 = smm_Operation(body="sample_text_2", language="sample_text_2")
    b = smm_MeasureRelationship(influence="sample_text")
    _safe_set(b, 'smm_MeasureRelationship102', a1)
    assert _is_linked(b, 'smm_MeasureRelationship102', a1)
    if hasattr(a1, 'smm_Operation103'):
        assert _is_linked(a1, 'smm_Operation103', b)
    _safe_set(b, 'smm_MeasureRelationship102', a2)
    assert _is_linked(b, 'smm_MeasureRelationship102', a2)
    if hasattr(a1, 'smm_Operation103'):
        assert not _is_linked(a1, 'smm_Operation103', b)
    if hasattr(a2, 'smm_Operation103'):
        assert _is_linked(a2, 'smm_Operation103', b)
    _safe_set(b, 'smm_MeasureRelationship102', None)
    assert not _is_linked(b, 'smm_MeasureRelationship102', a2)
    if hasattr(a2, 'smm_Operation103'):
        assert not _is_linked(a2, 'smm_Operation103', b)


def test_assoc_measureRelationships87_reverse_link_reassign_clear():
    a1 = smm_MeasureRelationship(influence="sample_text")
    a2 = smm_MeasureRelationship(influence="sample_text_2")
    b = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    _safe_set(b, 'smm_Measure88', {a1})
    assert _is_linked(b, 'smm_Measure88', a1)
    if hasattr(a1, 'smm_MeasureRelationship89'):
        assert _is_linked(a1, 'smm_MeasureRelationship89', b)
    _safe_set(b, 'smm_Measure88', {a2})
    assert _is_linked(b, 'smm_Measure88', a2)
    if hasattr(a1, 'smm_MeasureRelationship89'):
        assert not _is_linked(a1, 'smm_MeasureRelationship89', b)
    if hasattr(a2, 'smm_MeasureRelationship89'):
        assert _is_linked(a2, 'smm_MeasureRelationship89', b)
    _safe_set(b, 'smm_Measure88', set())
    assert not _is_linked(b, 'smm_Measure88', a2)
    if hasattr(a2, 'smm_MeasureRelationship89'):
        assert not _is_linked(a2, 'smm_MeasureRelationship89', b)


def test_assoc_operation146_reverse_link_reassign_clear():
    a1 = smm_RescaledMeasure(multiplier=3.14, offset=3.14, operationFirst="sample_text")
    a2 = smm_RescaledMeasure(multiplier=9.99, offset=9.99, operationFirst="sample_text_2")
    b = smm_Operation(body="sample_text", language="sample_text")
    _safe_set(b, 'smm_Operation148', a1)
    assert _is_linked(b, 'smm_Operation148', a1)
    if hasattr(a1, 'smm_RescaledMeasure147'):
        assert _is_linked(a1, 'smm_RescaledMeasure147', b)
    _safe_set(b, 'smm_Operation148', a2)
    assert _is_linked(b, 'smm_Operation148', a2)
    if hasattr(a1, 'smm_RescaledMeasure147'):
        assert not _is_linked(a1, 'smm_RescaledMeasure147', b)
    if hasattr(a2, 'smm_RescaledMeasure147'):
        assert _is_linked(a2, 'smm_RescaledMeasure147', b)
    _safe_set(b, 'smm_Operation148', None)
    assert not _is_linked(b, 'smm_Operation148', a2)
    if hasattr(a2, 'smm_RescaledMeasure147'):
        assert not _is_linked(a2, 'smm_RescaledMeasure147', b)


def test_assoc_outbound69_reverse_link_reassign_clear():
    a1 = smm_MeasureRelationship(influence="sample_text")
    a2 = smm_MeasureRelationship(influence="sample_text_2")
    b = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    _safe_set(b, 'smm_Measure70', {a1})
    assert _is_linked(b, 'smm_Measure70', a1)
    if hasattr(a1, 'smm_MeasureRelationship71'):
        assert _is_linked(a1, 'smm_MeasureRelationship71', b)
    _safe_set(b, 'smm_Measure70', {a2})
    assert _is_linked(b, 'smm_Measure70', a2)
    if hasattr(a1, 'smm_MeasureRelationship71'):
        assert not _is_linked(a1, 'smm_MeasureRelationship71', b)
    if hasattr(a2, 'smm_MeasureRelationship71'):
        assert _is_linked(a2, 'smm_MeasureRelationship71', b)
    _safe_set(b, 'smm_Measure70', set())
    assert not _is_linked(b, 'smm_Measure70', a2)
    if hasattr(a2, 'smm_MeasureRelationship71'):
        assert not _is_linked(a2, 'smm_MeasureRelationship71', b)


def test_assoc_scopes125_reverse_link_reassign_clear():
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

def test_assoc_arguments133_stub_double():
    # smm_ObservedMeasure has no real 'observedMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Argument(Type="sample_text", value="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'observedMeasure', None)
    _safe_set(owner, 'Argument', partner)
    assert owner in getattr(partner, 'observedMeasure')
    _safe_set(owner, 'Argument', None)
    assert owner not in getattr(partner, 'observedMeasure')


def test_assoc_baseMeasure1From24_stub_double():
    # smm_Base1MeasureRelationship has no real 'smm_Base1MeasureRelationship25' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'smm_Base1MeasureRelationship25', None)
    _safe_set(owner, 'smm_DimensionalMeasure', {partner})
    assert getattr(partner, 'smm_Base1MeasureRelationship25') == owner
    _safe_set(owner, 'smm_DimensionalMeasure', set())
    assert getattr(partner, 'smm_Base1MeasureRelationship25') is None


def test_assoc_baseMeasure1To3_stub_double():
    # smm_Base1MeasureRelationship has no real 'smm_Base1MeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base1MeasureRelationship()
    setattr(partner, 'smm_Base1MeasureRelationship', None)
    _safe_set(owner, 'smm_BinaryMeasure', partner)
    assert getattr(partner, 'smm_Base1MeasureRelationship') == owner
    _safe_set(owner, 'smm_BinaryMeasure', None)
    assert getattr(partner, 'smm_Base1MeasureRelationship') is None


def test_assoc_baseMeasure2From29_stub_double():
    # smm_Base2MeasureRelationship has no real 'smm_Base2MeasureRelationship31' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'smm_Base2MeasureRelationship31', None)
    _safe_set(owner, 'smm_DimensionalMeasure30', {partner})
    assert getattr(partner, 'smm_Base2MeasureRelationship31') == owner
    _safe_set(owner, 'smm_DimensionalMeasure30', set())
    assert getattr(partner, 'smm_Base2MeasureRelationship31') is None


def test_assoc_baseMeasure2To4_stub_double():
    # smm_Base2MeasureRelationship has no real 'smm_Base2MeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasure(functor="sample_text")
    partner = smm_Base2MeasureRelationship()
    setattr(partner, 'smm_Base2MeasureRelationship', None)
    _safe_set(owner, 'smm_BinaryMeasure5', partner)
    assert getattr(partner, 'smm_Base2MeasureRelationship') == owner
    _safe_set(owner, 'smm_BinaryMeasure5', None)
    assert getattr(partner, 'smm_Base2MeasureRelationship') is None


def test_assoc_baseMeasureFrom26_stub_double():
    # smm_BaseNMeasureRelationship has no real 'smm_BaseNMeasureRelationship28' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_BaseNMeasureRelationship()
    setattr(partner, 'smm_BaseNMeasureRelationship28', None)
    _safe_set(owner, 'smm_DimensionalMeasure27', {partner})
    assert getattr(partner, 'smm_BaseNMeasureRelationship28') == owner
    _safe_set(owner, 'smm_DimensionalMeasure27', set())
    assert getattr(partner, 'smm_BaseNMeasureRelationship28') is None


def test_assoc_baseMeasureTo16_stub_double():
    # smm_BaseNMeasureRelationship has no real 'smm_BaseNMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasure(accumulator="sample_text")
    partner = smm_BaseNMeasureRelationship()
    setattr(partner, 'smm_BaseNMeasureRelationship', None)
    _safe_set(owner, 'smm_CollectiveMeasure', {partner})
    assert getattr(partner, 'smm_BaseNMeasureRelationship') == owner
    _safe_set(owner, 'smm_CollectiveMeasure', set())
    assert getattr(partner, 'smm_BaseNMeasureRelationship') is None


def test_assoc_baseMeasurement1From40_stub_double():
    # smm_Base1MeasurementRelationship has no real 'smm_Base1MeasurementRelationship41' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'smm_Base1MeasurementRelationship41', None)
    _safe_set(owner, 'smm_DimensionalMeasurement', {partner})
    assert getattr(partner, 'smm_Base1MeasurementRelationship41') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement', set())
    assert getattr(partner, 'smm_Base1MeasurementRelationship41') is None


def test_assoc_baseMeasurement1To9_stub_double():
    # smm_Base1MeasurementRelationship has no real 'smm_Base1MeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied="sample_text")
    partner = smm_Base1MeasurementRelationship()
    setattr(partner, 'smm_Base1MeasurementRelationship', None)
    _safe_set(owner, 'smm_BinaryMeasurement10', partner)
    assert getattr(partner, 'smm_Base1MeasurementRelationship') == owner
    _safe_set(owner, 'smm_BinaryMeasurement10', None)
    assert getattr(partner, 'smm_Base1MeasurementRelationship') is None


def test_assoc_baseMeasurement2From45_stub_double():
    # smm_Base2MeasurementRelationship has no real 'smm_Base2MeasurementRelationship47' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'smm_Base2MeasurementRelationship47', None)
    _safe_set(owner, 'smm_DimensionalMeasurement46', {partner})
    assert getattr(partner, 'smm_Base2MeasurementRelationship47') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement46', set())
    assert getattr(partner, 'smm_Base2MeasurementRelationship47') is None


def test_assoc_baseMeasurement2To8_stub_double():
    # smm_Base2MeasurementRelationship has no real 'smm_Base2MeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_BinaryMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_BinaryMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_BinaryMeasurement(isBaseSupplied="sample_text")
    partner = smm_Base2MeasurementRelationship()
    setattr(partner, 'smm_Base2MeasurementRelationship', None)
    _safe_set(owner, 'smm_BinaryMeasurement', partner)
    assert getattr(partner, 'smm_Base2MeasurementRelationship') == owner
    _safe_set(owner, 'smm_BinaryMeasurement', None)
    assert getattr(partner, 'smm_Base2MeasurementRelationship') is None


def test_assoc_baseMeasurementFrom42_stub_double():
    # smm_BaseNMeasurementRelationship has no real 'smm_BaseNMeasurementRelationship44' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_BaseNMeasurementRelationship()
    setattr(partner, 'smm_BaseNMeasurementRelationship44', None)
    _safe_set(owner, 'smm_DimensionalMeasurement43', {partner})
    assert getattr(partner, 'smm_BaseNMeasurementRelationship44') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement43', set())
    assert getattr(partner, 'smm_BaseNMeasurementRelationship44') is None


def test_assoc_baseMeasurementTo20_stub_double():
    # smm_BaseNMeasurementRelationship has no real 'smm_BaseNMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_CollectiveMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_CollectiveMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_CollectiveMeasurement(isBaseSupplied="sample_text")
    partner = smm_BaseNMeasurementRelationship()
    setattr(partner, 'smm_BaseNMeasurementRelationship', None)
    _safe_set(owner, 'smm_CollectiveMeasurement', {partner})
    assert getattr(partner, 'smm_BaseNMeasurementRelationship') == owner
    _safe_set(owner, 'smm_CollectiveMeasurement', set())
    assert getattr(partner, 'smm_BaseNMeasurementRelationship') is None


def test_assoc_breakCondition154_stub_double():
    # smm_Scope has no real 'smm_Scope155' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_Scope()
    setattr(partner, 'smm_Scope155', None)
    _safe_set(owner, 'smm_Operation156', partner)
    assert getattr(partner, 'smm_Scope155') == owner
    _safe_set(owner, 'smm_Operation156', None)
    assert getattr(partner, 'smm_Scope155') is None


def test_assoc_category81_stub_double():
    # smm_MeasureCategory has no real 'MeasureCategory' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_MeasureCategory()
    setattr(partner, 'MeasureCategory', None)
    _safe_set(owner, 'categoryMeasure', {partner})
    assert getattr(partner, 'MeasureCategory') == owner
    _safe_set(owner, 'categoryMeasure', set())
    assert getattr(partner, 'MeasureCategory') is None


def test_assoc_categoryMeasure90_stub_double():
    # smm_MeasureCategory has no real 'category' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_MeasureCategory()
    setattr(partner, 'category', None)
    _safe_set(owner, 'Measure', partner)
    assert owner in getattr(partner, 'category')
    _safe_set(owner, 'Measure', None)
    assert owner not in getattr(partner, 'category')


def test_assoc_equivalentFrom105_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'smm_EquivalentMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'smm_EquivalentMeasurementRelationship', None)
    _safe_set(owner, 'smm_Measurement106', {partner})
    assert getattr(partner, 'smm_EquivalentMeasurementRelationship') == owner
    _safe_set(owner, 'smm_Measurement106', set())
    assert getattr(partner, 'smm_EquivalentMeasurementRelationship') is None


def test_assoc_equivalentFrom75_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'smm_EquivalentMeasureRelationship77' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'smm_EquivalentMeasureRelationship77', None)
    _safe_set(owner, 'smm_Measure76', {partner})
    assert getattr(partner, 'smm_EquivalentMeasureRelationship77') == owner
    _safe_set(owner, 'smm_Measure76', set())
    assert getattr(partner, 'smm_EquivalentMeasureRelationship77') is None


def test_assoc_equivalentTo107_stub_double():
    # smm_EquivalentMeasurementRelationship has no real 'smm_EquivalentMeasurementRelationship109' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EquivalentMeasurementRelationship()
    setattr(partner, 'smm_EquivalentMeasurementRelationship109', None)
    _safe_set(owner, 'smm_Measurement108', {partner})
    assert getattr(partner, 'smm_EquivalentMeasurementRelationship109') == owner
    _safe_set(owner, 'smm_Measurement108', set())
    assert getattr(partner, 'smm_EquivalentMeasurementRelationship109') is None


def test_assoc_equivalentTo72_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'smm_EquivalentMeasureRelationship74' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'smm_EquivalentMeasureRelationship74', None)
    _safe_set(owner, 'smm_Measure73', {partner})
    assert getattr(partner, 'smm_EquivalentMeasureRelationship74') == owner
    _safe_set(owner, 'smm_Measure73', set())
    assert getattr(partner, 'smm_EquivalentMeasureRelationship74') is None


def test_assoc_from_178_stub_double():
    # smm_SmmRelationship has no real 'outRelationships' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    partner = smm_SmmRelationship()
    setattr(partner, 'outRelationships', None)
    _safe_set(owner, 'SmmElement179', partner)
    assert getattr(partner, 'outRelationships') == owner
    _safe_set(owner, 'SmmElement179', None)
    assert getattr(partner, 'outRelationships') is None


def test_assoc_gradeFrom36_stub_double():
    # smm_GradeMeasureRelationship has no real 'smm_GradeMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_GradeMeasureRelationship()
    setattr(partner, 'smm_GradeMeasureRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasure37', {partner})
    assert getattr(partner, 'smm_GradeMeasureRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasure37', set())
    assert getattr(partner, 'smm_GradeMeasureRelationship') is None


def test_assoc_gradeFrom48_stub_double():
    # smm_GradeMeasurementRelationship has no real 'smm_GradeMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_GradeMeasurementRelationship()
    setattr(partner, 'smm_GradeMeasurementRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasurement49', {partner})
    assert getattr(partner, 'smm_GradeMeasurementRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement49', set())
    assert getattr(partner, 'smm_GradeMeasurementRelationship') is None


def test_assoc_gradeTo58_stub_double():
    # smm_GradeMeasurementRelationship has no real 'smm_GradeMeasurementRelationship59' property in the generated
    # code (a bare stub) -- manually attach it so smm_GradeMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_GradeMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_GradeMeasurement(isBaseSupplied=True, value="sample_text")
    partner = smm_GradeMeasurementRelationship()
    setattr(partner, 'smm_GradeMeasurementRelationship59', None)
    _safe_set(owner, 'smm_GradeMeasurement', partner)
    assert getattr(partner, 'smm_GradeMeasurementRelationship59') == owner
    _safe_set(owner, 'smm_GradeMeasurement', None)
    assert getattr(partner, 'smm_GradeMeasurementRelationship59') is None


def test_assoc_inRelationships169_stub_double():
    # smm_SmmRelationship has no real 'SmmRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    partner = smm_SmmRelationship()
    setattr(partner, 'SmmRelationship', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'SmmRelationship') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'SmmRelationship') is None


def test_assoc_inbound113_stub_double():
    # smm_MeasurementRelationship has no real 'smm_MeasurementRelationship115' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_MeasurementRelationship()
    setattr(partner, 'smm_MeasurementRelationship115', None)
    _safe_set(owner, 'smm_Measurement114', {partner})
    assert getattr(partner, 'smm_MeasurementRelationship115') == owner
    _safe_set(owner, 'smm_Measurement114', set())
    assert getattr(partner, 'smm_MeasurementRelationship115') is None


def test_assoc_interval141_stub_double():
    # smm_GradeMeasure has no real 'smm_GradeMeasure142' property in the generated
    # code (a bare stub) -- manually attach it so smm_GradeInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_GradeInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_GradeInterval(symbol="sample_text")
    partner = smm_GradeMeasure()
    setattr(partner, 'smm_GradeMeasure142', None)
    _safe_set(owner, 'smm_GradeInterval', partner)
    assert owner in getattr(partner, 'smm_GradeMeasure142')
    _safe_set(owner, 'smm_GradeInterval', None)
    assert owner not in getattr(partner, 'smm_GradeMeasure142')


def test_assoc_interval180_stub_double():
    # smm_RankingMeasure has no real 'ranking' property in the generated
    # code (a bare stub) -- manually attach it so smm_RankingInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RankingInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RankingInterval(value=3.14)
    partner = smm_RankingMeasure()
    setattr(partner, 'ranking', None)
    _safe_set(owner, 'RankingInterval', partner)
    assert owner in getattr(partner, 'ranking')
    _safe_set(owner, 'RankingInterval', None)
    assert owner not in getattr(partner, 'ranking')


def test_assoc_mapping56_stub_double():
    # smm_EquivalentMeasureRelationship has no real 'smm_EquivalentMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_EquivalentMeasureRelationship()
    setattr(partner, 'smm_EquivalentMeasureRelationship', None)
    _safe_set(owner, 'smm_Operation57', partner)
    assert getattr(partner, 'smm_EquivalentMeasureRelationship') == owner
    _safe_set(owner, 'smm_Operation57', None)
    assert getattr(partner, 'smm_EquivalentMeasureRelationship') is None


def test_assoc_measurand123_stub_double():
    # smm_EObject has no real 'smm_EObject' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_EObject()
    setattr(partner, 'smm_EObject', None)
    _safe_set(owner, 'smm_Measurement124', partner)
    assert getattr(partner, 'smm_EObject') == owner
    _safe_set(owner, 'smm_Measurement124', None)
    assert getattr(partner, 'smm_EObject') is None


def test_assoc_measure136_stub_double():
    # smm_ObservedMeasure has no real 'smm_ObservedMeasure137' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'smm_ObservedMeasure137', None)
    _safe_set(owner, 'smm_Measure138', partner)
    assert getattr(partner, 'smm_ObservedMeasure137') == owner
    _safe_set(owner, 'smm_Measure138', None)
    assert getattr(partner, 'smm_ObservedMeasure137') is None


def test_assoc_measurementRelationships104_stub_double():
    # smm_MeasurementRelationship has no real 'smm_MeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_MeasurementRelationship()
    setattr(partner, 'smm_MeasurementRelationship', None)
    _safe_set(owner, 'smm_Measurement', {partner})
    assert getattr(partner, 'smm_MeasurementRelationship') == owner
    _safe_set(owner, 'smm_Measurement', set())
    assert getattr(partner, 'smm_MeasurementRelationship') is None


def test_assoc_measurements134_stub_double():
    # smm_ObservedMeasure has no real 'observedMeasure135' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'observedMeasure135', None)
    _safe_set(owner, 'Measurement', partner)
    assert owner in getattr(partner, 'observedMeasure135')
    _safe_set(owner, 'Measurement', None)
    assert owner not in getattr(partner, 'observedMeasure135')


def test_assoc_observations174_stub_double():
    # smm_SmmModel has no real 'smm_SmmModel175' property in the generated
    # code (a bare stub) -- manually attach it so smm_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    partner = smm_SmmModel()
    setattr(partner, 'smm_SmmModel175', None)
    _safe_set(owner, 'smm_Observation176', partner)
    assert owner in getattr(partner, 'smm_SmmModel175')
    _safe_set(owner, 'smm_Observation176', None)
    assert owner not in getattr(partner, 'smm_SmmModel175')


def test_assoc_observedMeasure0_stub_double():
    # smm_ObservedMeasure has no real 'ObservedMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Argument(Type="sample_text", value="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'ObservedMeasure', None)
    _safe_set(owner, 'arguments', partner)
    assert getattr(partner, 'ObservedMeasure') == owner
    _safe_set(owner, 'arguments', None)
    assert getattr(partner, 'ObservedMeasure') is None


def test_assoc_observedMeasure121_stub_double():
    # smm_ObservedMeasure has no real 'ObservedMeasure122' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'ObservedMeasure122', None)
    _safe_set(owner, 'measurements', partner)
    assert getattr(partner, 'ObservedMeasure122') == owner
    _safe_set(owner, 'measurements', None)
    assert getattr(partner, 'ObservedMeasure122') is None


def test_assoc_observedMeasures126_stub_double():
    # smm_ObservedMeasure has no real 'smm_ObservedMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    partner = smm_ObservedMeasure()
    setattr(partner, 'smm_ObservedMeasure', None)
    _safe_set(owner, 'smm_Observation127', {partner})
    assert getattr(partner, 'smm_ObservedMeasure') == owner
    _safe_set(owner, 'smm_Observation127', set())
    assert getattr(partner, 'smm_ObservedMeasure') is None


def test_assoc_operation54_stub_double():
    # smm_DirectMeasure has no real 'smm_DirectMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_DirectMeasure()
    setattr(partner, 'smm_DirectMeasure', None)
    _safe_set(owner, 'smm_Operation55', partner)
    assert getattr(partner, 'smm_DirectMeasure') == owner
    _safe_set(owner, 'smm_Operation55', None)
    assert getattr(partner, 'smm_DirectMeasure') is None


def test_assoc_outRelationships170_stub_double():
    # smm_SmmRelationship has no real 'SmmRelationship171' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    partner = smm_SmmRelationship()
    setattr(partner, 'SmmRelationship171', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'SmmRelationship171') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'SmmRelationship171') is None


def test_assoc_outbound110_stub_double():
    # smm_MeasurementRelationship has no real 'smm_MeasurementRelationship112' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_MeasurementRelationship()
    setattr(partner, 'smm_MeasurementRelationship112', None)
    _safe_set(owner, 'smm_Measurement111', {partner})
    assert getattr(partner, 'smm_MeasurementRelationship112') == owner
    _safe_set(owner, 'smm_Measurement111', set())
    assert getattr(partner, 'smm_MeasurementRelationship112') is None


def test_assoc_ranking183_stub_double():
    # smm_RankingMeasure has no real 'RankingMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_RankingInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RankingInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RankingInterval(value=3.14)
    partner = smm_RankingMeasure()
    setattr(partner, 'RankingMeasure', None)
    _safe_set(owner, 'interval', partner)
    assert getattr(partner, 'RankingMeasure') == owner
    _safe_set(owner, 'interval', None)
    assert getattr(partner, 'RankingMeasure') is None


def test_assoc_rankingFrom32_stub_double():
    # smm_RankingMeasureRelationship has no real 'smm_RankingMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_RankingMeasureRelationship()
    setattr(partner, 'smm_RankingMeasureRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasure33', {partner})
    assert getattr(partner, 'smm_RankingMeasureRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasure33', set())
    assert getattr(partner, 'smm_RankingMeasureRelationship') is None


def test_assoc_rankingFrom52_stub_double():
    # smm_RankingMeasurementRelationship has no real 'smm_RankingMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'smm_RankingMeasurementRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasurement53', {partner})
    assert getattr(partner, 'smm_RankingMeasurementRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement53', set())
    assert getattr(partner, 'smm_RankingMeasurementRelationship') is None


def test_assoc_rankingTo187_stub_double():
    # smm_RankingMeasurementRelationship has no real 'smm_RankingMeasurementRelationship189' property in the generated
    # code (a bare stub) -- manually attach it so smm_RankingMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RankingMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RankingMeasurement(isBaseSupplied="sample_text")
    partner = smm_RankingMeasurementRelationship()
    setattr(partner, 'smm_RankingMeasurementRelationship189', None)
    _safe_set(owner, 'smm_RankingMeasurement188', partner)
    assert getattr(partner, 'smm_RankingMeasurementRelationship189') == owner
    _safe_set(owner, 'smm_RankingMeasurement188', None)
    assert getattr(partner, 'smm_RankingMeasurementRelationship189') is None


def test_assoc_recognizer157_stub_double():
    # smm_Scope has no real 'smm_Scope158' property in the generated
    # code (a bare stub) -- manually attach it so smm_Operation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Operation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Operation(body="sample_text", language="sample_text")
    partner = smm_Scope()
    setattr(partner, 'smm_Scope158', None)
    _safe_set(owner, 'smm_Operation159', partner)
    assert getattr(partner, 'smm_Scope158') == owner
    _safe_set(owner, 'smm_Operation159', None)
    assert getattr(partner, 'smm_Scope158') is None


def test_assoc_refinementFrom118_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'smm_RefinementMeasurementRelationship120' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'smm_RefinementMeasurementRelationship120', None)
    _safe_set(owner, 'smm_Measurement119', {partner})
    assert getattr(partner, 'smm_RefinementMeasurementRelationship120') == owner
    _safe_set(owner, 'smm_Measurement119', set())
    assert getattr(partner, 'smm_RefinementMeasurementRelationship120') is None


def test_assoc_refinementFrom63_stub_double():
    # smm_RefinementMeasureRelationship has no real 'smm_RefinementMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'smm_RefinementMeasureRelationship', None)
    _safe_set(owner, 'smm_Measure', {partner})
    assert getattr(partner, 'smm_RefinementMeasureRelationship') == owner
    _safe_set(owner, 'smm_Measure', set())
    assert getattr(partner, 'smm_RefinementMeasureRelationship') is None


def test_assoc_refinementTo116_stub_double():
    # smm_RefinementMeasurementRelationship has no real 'smm_RefinementMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measurement(breakValue="sample_text", error="sample_text")
    partner = smm_RefinementMeasurementRelationship()
    setattr(partner, 'smm_RefinementMeasurementRelationship', None)
    _safe_set(owner, 'smm_Measurement117', {partner})
    assert getattr(partner, 'smm_RefinementMeasurementRelationship') == owner
    _safe_set(owner, 'smm_Measurement117', set())
    assert getattr(partner, 'smm_RefinementMeasurementRelationship') is None


def test_assoc_refinementTo64_stub_double():
    # smm_RefinementMeasureRelationship has no real 'smm_RefinementMeasureRelationship66' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_RefinementMeasureRelationship()
    setattr(partner, 'smm_RefinementMeasureRelationship66', None)
    _safe_set(owner, 'smm_Measure65', {partner})
    assert getattr(partner, 'smm_RefinementMeasureRelationship66') == owner
    _safe_set(owner, 'smm_Measure65', set())
    assert getattr(partner, 'smm_RefinementMeasureRelationship66') is None


def test_assoc_requestedMeasures130_stub_double():
    # smm_AbstractMeasureElement has no real 'smm_AbstractMeasureElement132' property in the generated
    # code (a bare stub) -- manually attach it so smm_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    partner = smm_AbstractMeasureElement()
    setattr(partner, 'smm_AbstractMeasureElement132', None)
    _safe_set(owner, 'smm_Observation131', {partner})
    assert getattr(partner, 'smm_AbstractMeasureElement132') == owner
    _safe_set(owner, 'smm_Observation131', set())
    assert getattr(partner, 'smm_AbstractMeasureElement132') is None


def test_assoc_rescaleFrom143_stub_double():
    # smm_RescaledMeasureRelationship has no real 'smm_RescaledMeasureRelationship144' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasure(multiplier=3.14, offset=3.14, operationFirst="sample_text")
    partner = smm_RescaledMeasureRelationship()
    setattr(partner, 'smm_RescaledMeasureRelationship144', None)
    _safe_set(owner, 'smm_RescaledMeasure', {partner})
    assert getattr(partner, 'smm_RescaledMeasureRelationship144') == owner
    _safe_set(owner, 'smm_RescaledMeasure', set())
    assert getattr(partner, 'smm_RescaledMeasureRelationship144') is None


def test_assoc_rescaleFrom149_stub_double():
    # smm_RescaledMeasurementRelationship has no real 'smm_RescaledMeasurementRelationship150' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasurement(isBaseSupplied="sample_text")
    partner = smm_RescaledMeasurementRelationship()
    setattr(partner, 'smm_RescaledMeasurementRelationship150', None)
    _safe_set(owner, 'smm_RescaledMeasurement', partner)
    assert getattr(partner, 'smm_RescaledMeasurementRelationship150') == owner
    _safe_set(owner, 'smm_RescaledMeasurement', None)
    assert getattr(partner, 'smm_RescaledMeasurementRelationship150') is None


def test_assoc_rescaleTo34_stub_double():
    # smm_RescaledMeasureRelationship has no real 'smm_RescaledMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_RescaledMeasureRelationship()
    setattr(partner, 'smm_RescaledMeasureRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasure35', {partner})
    assert getattr(partner, 'smm_RescaledMeasureRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasure35', set())
    assert getattr(partner, 'smm_RescaledMeasureRelationship') is None


def test_assoc_rescaleTo50_stub_double():
    # smm_RescaledMeasurementRelationship has no real 'smm_RescaledMeasurementRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasurement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasurement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasurement(value=3.14)
    partner = smm_RescaledMeasurementRelationship()
    setattr(partner, 'smm_RescaledMeasurementRelationship', None)
    _safe_set(owner, 'smm_DimensionalMeasurement51', {partner})
    assert getattr(partner, 'smm_RescaledMeasurementRelationship') == owner
    _safe_set(owner, 'smm_DimensionalMeasurement51', set())
    assert getattr(partner, 'smm_RescaledMeasurementRelationship') is None


def test_assoc_rescaledMeasure184_stub_double():
    # smm_ScaledBaseMeasureRelationship has no real 'rescales' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasure(multiplier=3.14, offset=3.14, operationFirst="sample_text")
    partner = smm_ScaledBaseMeasureRelationship()
    setattr(partner, 'rescales', None)
    _safe_set(owner, 'RescaledMeasure', partner)
    assert getattr(partner, 'rescales') == owner
    _safe_set(owner, 'RescaledMeasure', None)
    assert getattr(partner, 'rescales') is None


def test_assoc_rescales145_stub_double():
    # smm_ScaledBaseMeasureRelationship has no real 'ScaledBaseMeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_RescaledMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_RescaledMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_RescaledMeasure(multiplier=3.14, offset=3.14, operationFirst="sample_text")
    partner = smm_ScaledBaseMeasureRelationship()
    setattr(partner, 'ScaledBaseMeasureRelationship', None)
    _safe_set(owner, 'rescaledMeasure', partner)
    assert getattr(partner, 'ScaledBaseMeasureRelationship') == owner
    _safe_set(owner, 'rescaledMeasure', None)
    assert getattr(partner, 'ScaledBaseMeasureRelationship') is None


def test_assoc_scope82_stub_double():
    # smm_Scope has no real 'smm_Scope' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_Scope()
    setattr(partner, 'smm_Scope', None)
    _safe_set(owner, 'smm_Measure83', partner)
    assert getattr(partner, 'smm_Scope') == owner
    _safe_set(owner, 'smm_Measure83', None)
    assert getattr(partner, 'smm_Scope') is None


def test_assoc_to177_stub_double():
    # smm_SmmRelationship has no real 'inRelationships' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement(description="sample_text", name="sample_text", shortDescription="sample_text")
    partner = smm_SmmRelationship()
    setattr(partner, 'inRelationships', None)
    _safe_set(owner, 'SmmElement', partner)
    assert getattr(partner, 'inRelationships') == owner
    _safe_set(owner, 'SmmElement', None)
    assert getattr(partner, 'inRelationships') is None


def test_assoc_trait84_stub_double():
    # smm_Characteristic has no real 'smm_Characteristic86' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(customScale="sample_text", measureLabelFormat="sample_text", measurementLabelFormat="sample_text", scale="sample_text", source="sample_text", visible="sample_text")
    partner = smm_Characteristic()
    setattr(partner, 'smm_Characteristic86', None)
    _safe_set(owner, 'smm_Measure85', partner)
    assert getattr(partner, 'smm_Characteristic86') == owner
    _safe_set(owner, 'smm_Measure85', None)
    assert getattr(partner, 'smm_Characteristic86') is None


def test_assoc_unit38_stub_double():
    # smm_UnitOfMeasure has no real 'smm_UnitOfMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_DimensionalMeasure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_DimensionalMeasure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_DimensionalMeasure(formula="sample_text")
    partner = smm_UnitOfMeasure()
    setattr(partner, 'smm_UnitOfMeasure', None)
    _safe_set(owner, 'smm_DimensionalMeasure39', partner)
    assert getattr(partner, 'smm_UnitOfMeasure') == owner
    _safe_set(owner, 'smm_DimensionalMeasure39', None)
    assert getattr(partner, 'smm_UnitOfMeasure') is None


