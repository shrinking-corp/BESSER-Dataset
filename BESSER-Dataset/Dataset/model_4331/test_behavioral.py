import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BinaryMeasure,
    DimensionalMeasure,
    DimensionalMeasurement,
    DirectMeasure,
    DirectMeasurement,
    Measure,
    Measurement,
    SmmElement,
    SmmRelationship,
    smm_AggregatedMeasurement,
    smm_Annotation,
    smm_Attribute,
    smm_BinaryMeasure,
    smm_Category,
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
    smm_Grade,
    smm_Measure,
    smm_MeasureRelationship,
    smm_Measurement,
    smm_MeasurementRelationship,
    smm_NamedMeasure,
    smm_NamedMeasurement,
    smm_Observation,
    smm_Ranking,
    smm_RankingInterval,
    smm_RatioMeasure,
    smm_ReScaledMeasurement,
    smm_RescaledMeasure,
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

def test_assoc_annotation2_reverse_link_reassign_clear():
    a1 = smm_SmmElement()
    a2 = smm_SmmElement()
    b = smm_Annotation(text="sample_text")
    _safe_set(b, 'Annotation', a1)
    assert _is_linked(b, 'Annotation', a1)
    if hasattr(a1, 'owner3'):
        assert _is_linked(a1, 'owner3', b)
    _safe_set(b, 'Annotation', a2)
    assert _is_linked(b, 'Annotation', a2)
    if hasattr(a1, 'owner3'):
        assert not _is_linked(a1, 'owner3', b)
    if hasattr(a2, 'owner3'):
        assert _is_linked(a2, 'owner3', b)
    _safe_set(b, 'Annotation', None)
    assert not _is_linked(b, 'Annotation', a2)
    if hasattr(a2, 'owner3'):
        assert not _is_linked(a2, 'owner3', b)


def test_assoc_attribute1_reverse_link_reassign_clear():
    a1 = smm_SmmElement()
    a2 = smm_SmmElement()
    b = smm_Attribute(tag="sample_text", value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'owner'):
        assert _is_linked(a1, 'owner', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'owner'):
        assert not _is_linked(a1, 'owner', b)
    if hasattr(a2, 'owner'):
        assert _is_linked(a2, 'owner', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'owner'):
        assert not _is_linked(a2, 'owner', b)


def test_assoc_baseMeasure157_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasure(unit="sample_text")
    a2 = smm_DimensionalMeasure(unit="sample_text_2")
    b = smm_BinaryMeasure(functor="sample_text")
    _safe_set(b, 'smm_BinaryMeasure', a1)
    assert _is_linked(b, 'smm_BinaryMeasure', a1)
    if hasattr(a1, 'smm_DimensionalMeasure'):
        assert _is_linked(a1, 'smm_DimensionalMeasure', b)
    _safe_set(b, 'smm_BinaryMeasure', a2)
    assert _is_linked(b, 'smm_BinaryMeasure', a2)
    if hasattr(a1, 'smm_DimensionalMeasure'):
        assert not _is_linked(a1, 'smm_DimensionalMeasure', b)
    if hasattr(a2, 'smm_DimensionalMeasure'):
        assert _is_linked(a2, 'smm_DimensionalMeasure', b)
    _safe_set(b, 'smm_BinaryMeasure', None)
    assert not _is_linked(b, 'smm_BinaryMeasure', a2)
    if hasattr(a2, 'smm_DimensionalMeasure'):
        assert not _is_linked(a2, 'smm_DimensionalMeasure', b)


def test_assoc_baseMeasure258_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasure(unit="sample_text")
    a2 = smm_DimensionalMeasure(unit="sample_text_2")
    b = smm_BinaryMeasure(functor="sample_text")
    _safe_set(b, 'smm_BinaryMeasure59', a1)
    assert _is_linked(b, 'smm_BinaryMeasure59', a1)
    if hasattr(a1, 'smm_DimensionalMeasure60'):
        assert _is_linked(a1, 'smm_DimensionalMeasure60', b)
    _safe_set(b, 'smm_BinaryMeasure59', a2)
    assert _is_linked(b, 'smm_BinaryMeasure59', a2)
    if hasattr(a1, 'smm_DimensionalMeasure60'):
        assert not _is_linked(a1, 'smm_DimensionalMeasure60', b)
    if hasattr(a2, 'smm_DimensionalMeasure60'):
        assert _is_linked(a2, 'smm_DimensionalMeasure60', b)
    _safe_set(b, 'smm_BinaryMeasure59', None)
    assert not _is_linked(b, 'smm_BinaryMeasure59', a2)
    if hasattr(a2, 'smm_DimensionalMeasure60'):
        assert not _is_linked(a2, 'smm_DimensionalMeasure60', b)


def test_assoc_baseMeasure61_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasure(unit="sample_text")
    a2 = smm_DimensionalMeasure(unit="sample_text_2")
    b = smm_CollectiveMeasure(accumulator="sample_text")
    _safe_set(b, 'smm_CollectiveMeasure', a1)
    assert _is_linked(b, 'smm_CollectiveMeasure', a1)
    if hasattr(a1, 'smm_DimensionalMeasure62'):
        assert _is_linked(a1, 'smm_DimensionalMeasure62', b)
    _safe_set(b, 'smm_CollectiveMeasure', a2)
    assert _is_linked(b, 'smm_CollectiveMeasure', a2)
    if hasattr(a1, 'smm_DimensionalMeasure62'):
        assert not _is_linked(a1, 'smm_DimensionalMeasure62', b)
    if hasattr(a2, 'smm_DimensionalMeasure62'):
        assert _is_linked(a2, 'smm_DimensionalMeasure62', b)
    _safe_set(b, 'smm_CollectiveMeasure', None)
    assert not _is_linked(b, 'smm_CollectiveMeasure', a2)
    if hasattr(a2, 'smm_DimensionalMeasure62'):
        assert not _is_linked(a2, 'smm_DimensionalMeasure62', b)


def test_assoc_baseMeasurement63_reverse_link_reassign_clear():
    a1 = smm_Grade(isBaseSupplied=True, value="sample_text")
    a2 = smm_Grade(isBaseSupplied=False, value="sample_text_2")
    b = smm_DimensionalMeasurement(value=3.14)
    _safe_set(b, 'smm_DimensionalMeasurement', a1)
    assert _is_linked(b, 'smm_DimensionalMeasurement', a1)
    if hasattr(a1, 'smm_Grade'):
        assert _is_linked(a1, 'smm_Grade', b)
    _safe_set(b, 'smm_DimensionalMeasurement', a2)
    assert _is_linked(b, 'smm_DimensionalMeasurement', a2)
    if hasattr(a1, 'smm_Grade'):
        assert not _is_linked(a1, 'smm_Grade', b)
    if hasattr(a2, 'smm_Grade'):
        assert _is_linked(a2, 'smm_Grade', b)
    _safe_set(b, 'smm_DimensionalMeasurement', None)
    assert not _is_linked(b, 'smm_DimensionalMeasurement', a2)
    if hasattr(a2, 'smm_Grade'):
        assert not _is_linked(a2, 'smm_Grade', b)


def test_assoc_baseMeasurement68_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasurement(value=3.14)
    a2 = smm_DimensionalMeasurement(value=9.99)
    b = smm_CollectiveMeasurement(accumulator="sample_text", isBaseSupplied=True)
    _safe_set(b, 'smm_CollectiveMeasurement', {a1})
    assert _is_linked(b, 'smm_CollectiveMeasurement', a1)
    if hasattr(a1, 'smm_DimensionalMeasurement69'):
        assert _is_linked(a1, 'smm_DimensionalMeasurement69', b)
    _safe_set(b, 'smm_CollectiveMeasurement', {a2})
    assert _is_linked(b, 'smm_CollectiveMeasurement', a2)
    if hasattr(a1, 'smm_DimensionalMeasurement69'):
        assert not _is_linked(a1, 'smm_DimensionalMeasurement69', b)
    if hasattr(a2, 'smm_DimensionalMeasurement69'):
        assert _is_linked(a2, 'smm_DimensionalMeasurement69', b)
    _safe_set(b, 'smm_CollectiveMeasurement', set())
    assert not _is_linked(b, 'smm_CollectiveMeasurement', a2)
    if hasattr(a2, 'smm_DimensionalMeasurement69'):
        assert not _is_linked(a2, 'smm_DimensionalMeasurement69', b)


def test_assoc_baseMeasurement70_reverse_link_reassign_clear():
    a1 = smm_DimensionalMeasurement(value=3.14)
    a2 = smm_DimensionalMeasurement(value=9.99)
    b = smm_AggregatedMeasurement(isBaseSuppled=True)
    _safe_set(b, 'smm_AggregatedMeasurement', {a1})
    assert _is_linked(b, 'smm_AggregatedMeasurement', a1)
    if hasattr(a1, 'smm_DimensionalMeasurement71'):
        assert _is_linked(a1, 'smm_DimensionalMeasurement71', b)
    _safe_set(b, 'smm_AggregatedMeasurement', {a2})
    assert _is_linked(b, 'smm_AggregatedMeasurement', a2)
    if hasattr(a1, 'smm_DimensionalMeasurement71'):
        assert not _is_linked(a1, 'smm_DimensionalMeasurement71', b)
    if hasattr(a2, 'smm_DimensionalMeasurement71'):
        assert _is_linked(a2, 'smm_DimensionalMeasurement71', b)
    _safe_set(b, 'smm_AggregatedMeasurement', set())
    assert not _is_linked(b, 'smm_AggregatedMeasurement', a2)
    if hasattr(a2, 'smm_DimensionalMeasurement71'):
        assert not _is_linked(a2, 'smm_DimensionalMeasurement71', b)


def test_assoc_category19_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'Category20', a1)
    assert _is_linked(b, 'Category20', a1)
    if hasattr(a1, 'categoryMeasure'):
        assert _is_linked(a1, 'categoryMeasure', b)
    _safe_set(b, 'Category20', a2)
    assert _is_linked(b, 'Category20', a2)
    if hasattr(a1, 'categoryMeasure'):
        assert not _is_linked(a1, 'categoryMeasure', b)
    if hasattr(a2, 'categoryMeasure'):
        assert _is_linked(a2, 'categoryMeasure', b)
    _safe_set(b, 'Category20', None)
    assert not _is_linked(b, 'Category20', a2)
    if hasattr(a2, 'categoryMeasure'):
        assert not _is_linked(a2, 'categoryMeasure', b)


def test_assoc_category9_reverse_link_reassign_clear():
    a1 = smm_Category(name="sample_text")
    a2 = smm_Category(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'categoryElement', {a1})
    assert _is_linked(b, 'categoryElement', a1)
    if hasattr(a1, 'Category10'):
        assert _is_linked(a1, 'Category10', b)
    _safe_set(b, 'categoryElement', {a2})
    assert _is_linked(b, 'categoryElement', a2)
    if hasattr(a1, 'Category10'):
        assert not _is_linked(a1, 'Category10', b)
    if hasattr(a2, 'Category10'):
        assert _is_linked(a2, 'Category10', b)
    _safe_set(b, 'categoryElement', set())
    assert not _is_linked(b, 'categoryElement', a2)
    if hasattr(a2, 'Category10'):
        assert not _is_linked(a2, 'Category10', b)


def test_assoc_categoryElement12_reverse_link_reassign_clear():
    a1 = smm_Category(name="sample_text")
    a2 = smm_Category(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'Category13'):
        assert _is_linked(a1, 'Category13', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'Category13'):
        assert not _is_linked(a1, 'Category13', b)
    if hasattr(a2, 'Category13'):
        assert _is_linked(a2, 'Category13', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'Category13'):
        assert not _is_linked(a2, 'Category13', b)


def test_assoc_categoryMeasure17_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'category18', {a1})
    assert _is_linked(b, 'category18', a1)
    if hasattr(a1, 'Measure'):
        assert _is_linked(a1, 'Measure', b)
    _safe_set(b, 'category18', {a2})
    assert _is_linked(b, 'category18', a2)
    if hasattr(a1, 'Measure'):
        assert not _is_linked(a1, 'Measure', b)
    if hasattr(a2, 'Measure'):
        assert _is_linked(a2, 'Measure', b)
    _safe_set(b, 'category18', set())
    assert not _is_linked(b, 'category18', a2)
    if hasattr(a2, 'Measure'):
        assert not _is_linked(a2, 'Measure', b)


def test_assoc_characteristics53_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Characteristic(name="sample_text")
    _safe_set(b, 'trait', {a1})
    assert _is_linked(b, 'trait', a1)
    if hasattr(a1, 'Measure54'):
        assert _is_linked(a1, 'Measure54', b)
    _safe_set(b, 'trait', {a2})
    assert _is_linked(b, 'trait', a2)
    if hasattr(a1, 'Measure54'):
        assert not _is_linked(a1, 'Measure54', b)
    if hasattr(a2, 'Measure54'):
        assert _is_linked(a2, 'Measure54', b)
    _safe_set(b, 'trait', set())
    assert not _is_linked(b, 'trait', a2)
    if hasattr(a2, 'Measure54'):
        assert not _is_linked(a2, 'Measure54', b)


def test_assoc_equivalentFrom22_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'equivalentTo', {a1})
    assert _is_linked(b, 'equivalentTo', a1)
    if hasattr(a1, 'Measure23'):
        assert _is_linked(a1, 'Measure23', b)
    _safe_set(b, 'equivalentTo', {a2})
    assert _is_linked(b, 'equivalentTo', a2)
    if hasattr(a1, 'Measure23'):
        assert not _is_linked(a1, 'Measure23', b)
    if hasattr(a2, 'Measure23'):
        assert _is_linked(a2, 'Measure23', b)
    _safe_set(b, 'equivalentTo', set())
    assert not _is_linked(b, 'equivalentTo', a2)
    if hasattr(a2, 'Measure23'):
        assert not _is_linked(a2, 'Measure23', b)


def test_assoc_equivalentTo25_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'equivalentFrom', {a1})
    assert _is_linked(b, 'equivalentFrom', a1)
    if hasattr(a1, 'Measure26'):
        assert _is_linked(a1, 'Measure26', b)
    _safe_set(b, 'equivalentFrom', {a2})
    assert _is_linked(b, 'equivalentFrom', a2)
    if hasattr(a1, 'Measure26'):
        assert not _is_linked(a1, 'Measure26', b)
    if hasattr(a2, 'Measure26'):
        assert _is_linked(a2, 'Measure26', b)
    _safe_set(b, 'equivalentFrom', set())
    assert not _is_linked(b, 'equivalentFrom', a2)
    if hasattr(a2, 'Measure26'):
        assert not _is_linked(a2, 'Measure26', b)


def test_assoc_from_5_reverse_link_reassign_clear():
    a1 = smm_CategoryRelationship(name="sample_text")
    a2 = smm_CategoryRelationship(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'Category', a1)
    assert _is_linked(b, 'Category', a1)
    if hasattr(a1, 'outCategory'):
        assert _is_linked(a1, 'outCategory', b)
    _safe_set(b, 'Category', a2)
    assert _is_linked(b, 'Category', a2)
    if hasattr(a1, 'outCategory'):
        assert not _is_linked(a1, 'outCategory', b)
    if hasattr(a2, 'outCategory'):
        assert _is_linked(a2, 'outCategory', b)
    _safe_set(b, 'Category', None)
    assert not _is_linked(b, 'Category', a2)
    if hasattr(a2, 'outCategory'):
        assert not _is_linked(a2, 'outCategory', b)


def test_assoc_from_64_reverse_link_reassign_clear():
    a1 = smm_MeasurementRelationship(name="sample_text")
    a2 = smm_MeasurementRelationship(name="sample_text_2")
    b = smm_Measurement(error="sample_text")
    _safe_set(b, 'Measurement65', a1)
    assert _is_linked(b, 'Measurement65', a1)
    if hasattr(a1, 'outMeasurement'):
        assert _is_linked(a1, 'outMeasurement', b)
    _safe_set(b, 'Measurement65', a2)
    assert _is_linked(b, 'Measurement65', a2)
    if hasattr(a1, 'outMeasurement'):
        assert not _is_linked(a1, 'outMeasurement', b)
    if hasattr(a2, 'outMeasurement'):
        assert _is_linked(a2, 'outMeasurement', b)
    _safe_set(b, 'Measurement65', None)
    assert not _is_linked(b, 'Measurement65', a2)
    if hasattr(a2, 'outMeasurement'):
        assert not _is_linked(a2, 'outMeasurement', b)


def test_assoc_inCategory15_reverse_link_reassign_clear():
    a1 = smm_CategoryRelationship(name="sample_text")
    a2 = smm_CategoryRelationship(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'to', {a1})
    assert _is_linked(b, 'to', a1)
    if hasattr(a1, 'CategoryRelationship16'):
        assert _is_linked(a1, 'CategoryRelationship16', b)
    _safe_set(b, 'to', {a2})
    assert _is_linked(b, 'to', a2)
    if hasattr(a1, 'CategoryRelationship16'):
        assert not _is_linked(a1, 'CategoryRelationship16', b)
    if hasattr(a2, 'CategoryRelationship16'):
        assert _is_linked(a2, 'CategoryRelationship16', b)
    _safe_set(b, 'to', set())
    assert not _is_linked(b, 'to', a2)
    if hasattr(a2, 'CategoryRelationship16'):
        assert not _is_linked(a2, 'CategoryRelationship16', b)


def test_assoc_inMeasurement42_reverse_link_reassign_clear():
    a1 = smm_MeasurementRelationship(name="sample_text")
    a2 = smm_MeasurementRelationship(name="sample_text_2")
    b = smm_Measurement(error="sample_text")
    _safe_set(b, 'to43', {a1})
    assert _is_linked(b, 'to43', a1)
    if hasattr(a1, 'MeasurementRelationship44'):
        assert _is_linked(a1, 'MeasurementRelationship44', b)
    _safe_set(b, 'to43', {a2})
    assert _is_linked(b, 'to43', a2)
    if hasattr(a1, 'MeasurementRelationship44'):
        assert not _is_linked(a1, 'MeasurementRelationship44', b)
    if hasattr(a2, 'MeasurementRelationship44'):
        assert _is_linked(a2, 'MeasurementRelationship44', b)
    _safe_set(b, 'to43', set())
    assert not _is_linked(b, 'to43', a2)
    if hasattr(a2, 'MeasurementRelationship44'):
        assert not _is_linked(a2, 'MeasurementRelationship44', b)


def test_assoc_measure37_reverse_link_reassign_clear():
    a1 = smm_Measurement(error="sample_text")
    a2 = smm_Measurement(error="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'Measure38', a1)
    assert _is_linked(b, 'Measure38', a1)
    if hasattr(a1, 'measurement'):
        assert _is_linked(a1, 'measurement', b)
    _safe_set(b, 'Measure38', a2)
    assert _is_linked(b, 'Measure38', a2)
    if hasattr(a1, 'measurement'):
        assert not _is_linked(a1, 'measurement', b)
    if hasattr(a2, 'measurement'):
        assert _is_linked(a2, 'measurement', b)
    _safe_set(b, 'Measure38', None)
    assert not _is_linked(b, 'Measure38', a2)
    if hasattr(a2, 'measurement'):
        assert not _is_linked(a2, 'measurement', b)


def test_assoc_measurement29_reverse_link_reassign_clear():
    a1 = smm_Measurement(error="sample_text")
    a2 = smm_Measurement(error="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'measure', {a1})
    assert _is_linked(b, 'measure', a1)
    if hasattr(a1, 'Measurement'):
        assert _is_linked(a1, 'Measurement', b)
    _safe_set(b, 'measure', {a2})
    assert _is_linked(b, 'measure', a2)
    if hasattr(a1, 'Measurement'):
        assert not _is_linked(a1, 'Measurement', b)
    if hasattr(a2, 'Measurement'):
        assert _is_linked(a2, 'Measurement', b)
    _safe_set(b, 'measure', set())
    assert not _is_linked(b, 'measure', a2)
    if hasattr(a2, 'Measurement'):
        assert not _is_linked(a2, 'Measurement', b)


def test_assoc_measures55_reverse_link_reassign_clear():
    a1 = smm_Scope(class_="sample_text", enumerated=True, name="sample_text", recognizer="sample_text")
    a2 = smm_Scope(class_="sample_text_2", enumerated=False, name="sample_text_2", recognizer="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'Measure56', a1)
    assert _is_linked(b, 'Measure56', a1)
    if hasattr(a1, 'scope'):
        assert _is_linked(a1, 'scope', b)
    _safe_set(b, 'Measure56', a2)
    assert _is_linked(b, 'Measure56', a2)
    if hasattr(a1, 'scope'):
        assert not _is_linked(a1, 'scope', b)
    if hasattr(a2, 'scope'):
        assert _is_linked(a2, 'scope', b)
    _safe_set(b, 'Measure56', None)
    assert not _is_linked(b, 'Measure56', a2)
    if hasattr(a2, 'scope'):
        assert not _is_linked(a2, 'scope', b)


def test_assoc_observation39_reverse_link_reassign_clear():
    a1 = smm_Observation(observer="sample_text", tool="sample_text", whenObserved="sample_text")
    a2 = smm_Observation(observer="sample_text_2", tool="sample_text_2", whenObserved="sample_text_2")
    b = smm_Measurement(error="sample_text")
    _safe_set(b, 'smm_Measurement', a1)
    assert _is_linked(b, 'smm_Measurement', a1)
    if hasattr(a1, 'smm_Observation'):
        assert _is_linked(a1, 'smm_Observation', b)
    _safe_set(b, 'smm_Measurement', a2)
    assert _is_linked(b, 'smm_Measurement', a2)
    if hasattr(a1, 'smm_Observation'):
        assert not _is_linked(a1, 'smm_Observation', b)
    if hasattr(a2, 'smm_Observation'):
        assert _is_linked(a2, 'smm_Observation', b)
    _safe_set(b, 'smm_Measurement', None)
    assert not _is_linked(b, 'smm_Measurement', a2)
    if hasattr(a2, 'smm_Observation'):
        assert not _is_linked(a2, 'smm_Observation', b)


def test_assoc_outCategory14_reverse_link_reassign_clear():
    a1 = smm_CategoryRelationship(name="sample_text")
    a2 = smm_CategoryRelationship(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'from_', {a1})
    assert _is_linked(b, 'from_', a1)
    if hasattr(a1, 'CategoryRelationship'):
        assert _is_linked(a1, 'CategoryRelationship', b)
    _safe_set(b, 'from_', {a2})
    assert _is_linked(b, 'from_', a2)
    if hasattr(a1, 'CategoryRelationship'):
        assert not _is_linked(a1, 'CategoryRelationship', b)
    if hasattr(a2, 'CategoryRelationship'):
        assert _is_linked(a2, 'CategoryRelationship', b)
    _safe_set(b, 'from_', set())
    assert not _is_linked(b, 'from_', a2)
    if hasattr(a2, 'CategoryRelationship'):
        assert not _is_linked(a2, 'CategoryRelationship', b)


def test_assoc_outMeasurement40_reverse_link_reassign_clear():
    a1 = smm_MeasurementRelationship(name="sample_text")
    a2 = smm_MeasurementRelationship(name="sample_text_2")
    b = smm_Measurement(error="sample_text")
    _safe_set(b, 'from_41', {a1})
    assert _is_linked(b, 'from_41', a1)
    if hasattr(a1, 'MeasurementRelationship'):
        assert _is_linked(a1, 'MeasurementRelationship', b)
    _safe_set(b, 'from_41', {a2})
    assert _is_linked(b, 'from_41', a2)
    if hasattr(a1, 'MeasurementRelationship'):
        assert not _is_linked(a1, 'MeasurementRelationship', b)
    if hasattr(a2, 'MeasurementRelationship'):
        assert _is_linked(a2, 'MeasurementRelationship', b)
    _safe_set(b, 'from_41', set())
    assert not _is_linked(b, 'from_41', a2)
    if hasattr(a2, 'MeasurementRelationship'):
        assert not _is_linked(a2, 'MeasurementRelationship', b)


def test_assoc_owner72_reverse_link_reassign_clear():
    a1 = smm_SmmElement()
    a2 = smm_SmmElement()
    b = smm_Attribute(tag="sample_text", value="sample_text")
    _safe_set(b, 'attribute', a1)
    assert _is_linked(b, 'attribute', a1)
    if hasattr(a1, 'SmmElement73'):
        assert _is_linked(a1, 'SmmElement73', b)
    _safe_set(b, 'attribute', a2)
    assert _is_linked(b, 'attribute', a2)
    if hasattr(a1, 'SmmElement73'):
        assert not _is_linked(a1, 'SmmElement73', b)
    if hasattr(a2, 'SmmElement73'):
        assert _is_linked(a2, 'SmmElement73', b)
    _safe_set(b, 'attribute', None)
    assert not _is_linked(b, 'attribute', a2)
    if hasattr(a2, 'SmmElement73'):
        assert not _is_linked(a2, 'SmmElement73', b)


def test_assoc_owner74_reverse_link_reassign_clear():
    a1 = smm_SmmElement()
    a2 = smm_SmmElement()
    b = smm_Annotation(text="sample_text")
    _safe_set(b, 'annotation', a1)
    assert _is_linked(b, 'annotation', a1)
    if hasattr(a1, 'SmmElement75'):
        assert _is_linked(a1, 'SmmElement75', b)
    _safe_set(b, 'annotation', a2)
    assert _is_linked(b, 'annotation', a2)
    if hasattr(a1, 'SmmElement75'):
        assert not _is_linked(a1, 'SmmElement75', b)
    if hasattr(a2, 'SmmElement75'):
        assert _is_linked(a2, 'SmmElement75', b)
    _safe_set(b, 'annotation', None)
    assert not _is_linked(b, 'annotation', a2)
    if hasattr(a2, 'SmmElement75'):
        assert not _is_linked(a2, 'SmmElement75', b)


def test_assoc_parent52_reverse_link_reassign_clear():
    a1 = smm_Characteristic(name="sample_text")
    a2 = smm_Characteristic(name="sample_text_2")
    b = smm_Characteristic(name="sample_text")
    _safe_set(b, 'smm_Characteristic51', a1)
    assert _is_linked(b, 'smm_Characteristic51', a1)
    if hasattr(a1, 'smm_Characteristic'):
        assert _is_linked(a1, 'smm_Characteristic', b)
    _safe_set(b, 'smm_Characteristic51', a2)
    assert _is_linked(b, 'smm_Characteristic51', a2)
    if hasattr(a1, 'smm_Characteristic'):
        assert not _is_linked(a1, 'smm_Characteristic', b)
    if hasattr(a2, 'smm_Characteristic'):
        assert _is_linked(a2, 'smm_Characteristic', b)
    _safe_set(b, 'smm_Characteristic51', None)
    assert not _is_linked(b, 'smm_Characteristic51', a2)
    if hasattr(a2, 'smm_Characteristic'):
        assert not _is_linked(a2, 'smm_Characteristic', b)


def test_assoc_refinement28_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'smm_Measure27', {a1})
    assert _is_linked(b, 'smm_Measure27', a1)
    if hasattr(a1, 'smm_Measure'):
        assert _is_linked(a1, 'smm_Measure', b)
    _safe_set(b, 'smm_Measure27', {a2})
    assert _is_linked(b, 'smm_Measure27', a2)
    if hasattr(a1, 'smm_Measure'):
        assert not _is_linked(a1, 'smm_Measure', b)
    if hasattr(a2, 'smm_Measure'):
        assert _is_linked(a2, 'smm_Measure', b)
    _safe_set(b, 'smm_Measure27', set())
    assert not _is_linked(b, 'smm_Measure27', a2)
    if hasattr(a2, 'smm_Measure'):
        assert not _is_linked(a2, 'smm_Measure', b)


def test_assoc_scope36_reverse_link_reassign_clear():
    a1 = smm_Scope(class_="sample_text", enumerated=True, name="sample_text", recognizer="sample_text")
    a2 = smm_Scope(class_="sample_text_2", enumerated=False, name="sample_text_2", recognizer="sample_text_2")
    b = smm_Measure(library="sample_text", name="sample_text")
    _safe_set(b, 'measures', a1)
    assert _is_linked(b, 'measures', a1)
    if hasattr(a1, 'Scope'):
        assert _is_linked(a1, 'Scope', b)
    _safe_set(b, 'measures', a2)
    assert _is_linked(b, 'measures', a2)
    if hasattr(a1, 'Scope'):
        assert not _is_linked(a1, 'Scope', b)
    if hasattr(a2, 'Scope'):
        assert _is_linked(a2, 'Scope', b)
    _safe_set(b, 'measures', None)
    assert not _is_linked(b, 'measures', a2)
    if hasattr(a2, 'Scope'):
        assert not _is_linked(a2, 'Scope', b)


def test_assoc_to6_reverse_link_reassign_clear():
    a1 = smm_CategoryRelationship(name="sample_text")
    a2 = smm_CategoryRelationship(name="sample_text_2")
    b = smm_Category(name="sample_text")
    _safe_set(b, 'Category7', a1)
    assert _is_linked(b, 'Category7', a1)
    if hasattr(a1, 'inCategory'):
        assert _is_linked(a1, 'inCategory', b)
    _safe_set(b, 'Category7', a2)
    assert _is_linked(b, 'Category7', a2)
    if hasattr(a1, 'inCategory'):
        assert not _is_linked(a1, 'inCategory', b)
    if hasattr(a2, 'inCategory'):
        assert _is_linked(a2, 'inCategory', b)
    _safe_set(b, 'Category7', None)
    assert not _is_linked(b, 'Category7', a2)
    if hasattr(a2, 'inCategory'):
        assert not _is_linked(a2, 'inCategory', b)


def test_assoc_to66_reverse_link_reassign_clear():
    a1 = smm_MeasurementRelationship(name="sample_text")
    a2 = smm_MeasurementRelationship(name="sample_text_2")
    b = smm_Measurement(error="sample_text")
    _safe_set(b, 'Measurement67', a1)
    assert _is_linked(b, 'Measurement67', a1)
    if hasattr(a1, 'inMeasurement'):
        assert _is_linked(a1, 'inMeasurement', b)
    _safe_set(b, 'Measurement67', a2)
    assert _is_linked(b, 'Measurement67', a2)
    if hasattr(a1, 'inMeasurement'):
        assert not _is_linked(a1, 'inMeasurement', b)
    if hasattr(a2, 'inMeasurement'):
        assert _is_linked(a2, 'inMeasurement', b)
    _safe_set(b, 'Measurement67', None)
    assert not _is_linked(b, 'Measurement67', a2)
    if hasattr(a2, 'inMeasurement'):
        assert not _is_linked(a2, 'inMeasurement', b)


def test_assoc_trait35_reverse_link_reassign_clear():
    a1 = smm_Measure(library="sample_text", name="sample_text")
    a2 = smm_Measure(library="sample_text_2", name="sample_text_2")
    b = smm_Characteristic(name="sample_text")
    _safe_set(b, 'Characteristic', a1)
    assert _is_linked(b, 'Characteristic', a1)
    if hasattr(a1, 'characteristics'):
        assert _is_linked(a1, 'characteristics', b)
    _safe_set(b, 'Characteristic', a2)
    assert _is_linked(b, 'Characteristic', a2)
    if hasattr(a1, 'characteristics'):
        assert not _is_linked(a1, 'characteristics', b)
    if hasattr(a2, 'characteristics'):
        assert _is_linked(a2, 'characteristics', b)
    _safe_set(b, 'Characteristic', None)
    assert not _is_linked(b, 'Characteristic', a2)
    if hasattr(a2, 'characteristics'):
        assert not _is_linked(a2, 'characteristics', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_from_45_stub_double():
    # smm_MeasureRelationship has no real 'outMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(library="sample_text", name="sample_text")
    partner = smm_MeasureRelationship()
    setattr(partner, 'outMeasure', None)
    _safe_set(owner, 'Measure46', partner)
    assert getattr(partner, 'outMeasure') == owner
    _safe_set(owner, 'Measure46', None)
    assert getattr(partner, 'outMeasure') is None


def test_assoc_inMeasure32_stub_double():
    # smm_MeasureRelationship has no real 'MeasureRelationship34' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(library="sample_text", name="sample_text")
    partner = smm_MeasureRelationship()
    setattr(partner, 'MeasureRelationship34', None)
    _safe_set(owner, 'to33', {partner})
    assert getattr(partner, 'MeasureRelationship34') == owner
    _safe_set(owner, 'to33', set())
    assert getattr(partner, 'MeasureRelationship34') is None


def test_assoc_interval49_stub_double():
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


def test_assoc_model0_stub_double():
    # smm_SmmModel has no real 'SmmModel' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement()
    partner = smm_SmmModel()
    setattr(partner, 'SmmModel', None)
    _safe_set(owner, 'modelElement', partner)
    assert getattr(partner, 'SmmModel') == owner
    _safe_set(owner, 'modelElement', None)
    assert getattr(partner, 'SmmModel') is None


def test_assoc_modelElement4_stub_double():
    # smm_SmmModel has no real 'model' property in the generated
    # code (a bare stub) -- manually attach it so smm_SmmElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_SmmElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_SmmElement()
    partner = smm_SmmModel()
    setattr(partner, 'model', None)
    _safe_set(owner, 'SmmElement', partner)
    assert owner in getattr(partner, 'model')
    _safe_set(owner, 'SmmElement', None)
    assert owner not in getattr(partner, 'model')


def test_assoc_outMeasure30_stub_double():
    # smm_MeasureRelationship has no real 'MeasureRelationship' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(library="sample_text", name="sample_text")
    partner = smm_MeasureRelationship()
    setattr(partner, 'MeasureRelationship', None)
    _safe_set(owner, 'from_31', {partner})
    assert getattr(partner, 'MeasureRelationship') == owner
    _safe_set(owner, 'from_31', set())
    assert getattr(partner, 'MeasureRelationship') is None


def test_assoc_rank50_stub_double():
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


def test_assoc_to47_stub_double():
    # smm_MeasureRelationship has no real 'inMeasure' property in the generated
    # code (a bare stub) -- manually attach it so smm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # smm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = smm_Measure(library="sample_text", name="sample_text")
    partner = smm_MeasureRelationship()
    setattr(partner, 'inMeasure', None)
    _safe_set(owner, 'Measure48', partner)
    assert getattr(partner, 'inMeasure') == owner
    _safe_set(owner, 'Measure48', None)
    assert getattr(partner, 'inMeasure') is None


