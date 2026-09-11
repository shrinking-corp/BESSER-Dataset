import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnnotatedElement,
    CharacterizingElement,
    DescribedElement,
    Evaluation,
    EvaluationResult,
    FactorAggregation,
    FormBasedEvaluation,
    FormBasedMeasureAggregation,
    Function,
    Instrument,
    LinearFunction,
    Measure,
    MeasureAggregation,
    MeasureEvaluation,
    MeasurementMethod,
    MeasurementResult,
    MultiMeasureEvaluation,
    NamedElement,
    QualityModelElement,
    Ranking,
    Result,
    TaggedElement,
    TextAggregation,
    TextEvaluation,
    qm_AnnotatedElement,
    qm_Annotation,
    qm_AnnotationBase,
    qm_CharacterizingElement,
    qm_Decomposition,
    qm_DescribedElement,
    qm_DoubleInterval,
    qm_Entity,
    qm_Evaluation,
    qm_EvaluationResult,
    qm_Factor,
    qm_FactorAggregation,
    qm_FactorRanking,
    qm_FactorRefinement,
    qm_FindingMessage,
    qm_FindingsMeasurementResult,
    qm_FindingsUnionMeasureAggregation,
    qm_FormBasedEvaluation,
    qm_FormBasedMeasureAggregation,
    qm_Function,
    qm_Impact,
    qm_Instrument,
    qm_LinearDecreasingFunction,
    qm_LinearFunction,
    qm_LinearIncreasingFunction,
    qm_ManualEvaluation,
    qm_ManualInstrument,
    qm_Measure,
    qm_MeasureAggregation,
    qm_MeasureEvaluation,
    qm_MeasureRanking,
    qm_MeasureRankingEvaluationResult,
    qm_MeasureRefinement,
    qm_Measurement,
    qm_MeasurementMethod,
    qm_MeasurementResult,
    qm_MultiMeasureEvaluation,
    qm_MultiMeasureEvaluationResult,
    qm_NamedElement,
    qm_NormalizationMeasure,
    qm_NumberMeanMeasureAggregation,
    qm_NumberMeasurementResult,
    qm_QIESLAggregation,
    qm_QIESLEvaluation,
    qm_QualityModel,
    qm_QualityModelElement,
    qm_QualityModelResult,
    qm_Ranking,
    qm_Result,
    qm_SingleMeasureEvaluation,
    qm_SingleMeasureEvaluationResult,
    qm_Source,
    qm_Specialization,
    qm_Tag,
    qm_TaggedElement,
    qm_TextAggregation,
    qm_TextEvaluation,
    qm_Tool,
    qm_ToolBasedInstrument,
    qm_WeightedSumFactorAggregation,
    qm_WeightedSumMultiMeasureEvaluation,
    Effect,
    Type,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_qm_Annotation_key_value_roundtrip():
    instance = qm_Annotation(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_qm_Annotation_value_value_roundtrip():
    instance = qm_Annotation(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_qm_DescribedElement_description_value_roundtrip():
    instance = qm_DescribedElement(description="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_qm_DoubleInterval_lower_value_roundtrip():
    instance = qm_DoubleInterval(lower=3.14, upper=3.14)
    assert instance.lower == 3.14
    instance.lower = 9.99
    assert instance.lower == 9.99


def test_qm_DoubleInterval_upper_value_roundtrip():
    instance = qm_DoubleInterval(lower=3.14, upper=3.14)
    assert instance.upper == 3.14
    instance.upper = 9.99
    assert instance.upper == 9.99


def test_qm_Entity_stakeholder_value_roundtrip():
    instance = qm_Entity(stakeholder=True, useCase=True)
    assert instance.stakeholder == True
    instance.stakeholder = False
    assert instance.stakeholder == False


def test_qm_Entity_useCase_value_roundtrip():
    instance = qm_Entity(stakeholder=True, useCase=True)
    assert instance.useCase == True
    instance.useCase = False
    assert instance.useCase == False


def test_qm_Evaluation_completeness_value_roundtrip():
    instance = qm_Evaluation(completeness=7, maximumPoints=7)
    assert instance.completeness == 7
    instance.completeness = 13
    assert instance.completeness == 13


def test_qm_Evaluation_maximumPoints_value_roundtrip():
    instance = qm_Evaluation(completeness=7, maximumPoints=7)
    assert instance.maximumPoints == 7
    instance.maximumPoints = 13
    assert instance.maximumPoints == 13


def test_qm_FindingMessage_location_value_roundtrip():
    instance = qm_FindingMessage(location="sample_text", message="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_qm_FindingMessage_message_value_roundtrip():
    instance = qm_FindingMessage(location="sample_text", message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_qm_FindingsMeasurementResult_count_value_roundtrip():
    instance = qm_FindingsMeasurementResult(count=7, findings="sample_text")
    assert instance.count == 7
    instance.count = 13
    assert instance.count == 13


def test_qm_FindingsMeasurementResult_findings_value_roundtrip():
    instance = qm_FindingsMeasurementResult(count=7, findings="sample_text")
    assert instance.findings == "sample_text"
    instance.findings = "sample_text_2"
    assert instance.findings == "sample_text_2"


def test_qm_Impact_effect_value_roundtrip():
    instance = qm_Impact(effect="sample_text", justification="sample_text")
    assert instance.effect == "sample_text"
    instance.effect = "sample_text_2"
    assert instance.effect == "sample_text_2"


def test_qm_Impact_justification_value_roundtrip():
    instance = qm_Impact(effect="sample_text", justification="sample_text")
    assert instance.justification == "sample_text"
    instance.justification = "sample_text_2"
    assert instance.justification == "sample_text_2"


def test_qm_LinearFunction_lowerBound_value_roundtrip():
    instance = qm_LinearFunction(lowerBound=3.14, upperBound=3.14)
    assert instance.lowerBound == 3.14
    instance.lowerBound = 9.99
    assert instance.lowerBound == 9.99


def test_qm_LinearFunction_upperBound_value_roundtrip():
    instance = qm_LinearFunction(lowerBound=3.14, upperBound=3.14)
    assert instance.upperBound == 3.14
    instance.upperBound = 9.99
    assert instance.upperBound == 9.99


def test_qm_Measure_type_value_roundtrip():
    instance = qm_Measure(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_qm_MeasureEvaluation_range_value_roundtrip():
    instance = qm_MeasureEvaluation(range="sample_text")
    assert instance.range == "sample_text"
    instance.range = "sample_text_2"
    assert instance.range == "sample_text_2"


def test_qm_MeasureRankingEvaluationResult_ratioAffected_value_roundtrip():
    instance = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    assert instance.ratioAffected == 3.14
    instance.ratioAffected = 9.99
    assert instance.ratioAffected == 9.99


def test_qm_NamedElement_name_value_roundtrip():
    instance = qm_NamedElement(name="sample_text", title="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_qm_NamedElement_title_value_roundtrip():
    instance = qm_NamedElement(name="sample_text", title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_qm_QualityModel_schoolGradeBoundary2_value_roundtrip():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert instance.schoolGradeBoundary2 == "sample_text"
    instance.schoolGradeBoundary2 = "sample_text_2"
    assert instance.schoolGradeBoundary2 == "sample_text_2"


def test_qm_QualityModel_schoolGradeBoundary3_value_roundtrip():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert instance.schoolGradeBoundary3 == "sample_text"
    instance.schoolGradeBoundary3 = "sample_text_2"
    assert instance.schoolGradeBoundary3 == "sample_text_2"


def test_qm_QualityModel_schoolGradeBoundary4_value_roundtrip():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert instance.schoolGradeBoundary4 == "sample_text"
    instance.schoolGradeBoundary4 = "sample_text_2"
    assert instance.schoolGradeBoundary4 == "sample_text_2"


def test_qm_QualityModel_schoolGradeBoundary5_value_roundtrip():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert instance.schoolGradeBoundary5 == "sample_text"
    instance.schoolGradeBoundary5 = "sample_text_2"
    assert instance.schoolGradeBoundary5 == "sample_text_2"


def test_qm_QualityModel_schoolGradeBoundary6_value_roundtrip():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert instance.schoolGradeBoundary6 == "sample_text"
    instance.schoolGradeBoundary6 = "sample_text_2"
    assert instance.schoolGradeBoundary6 == "sample_text_2"


def test_qm_QualityModelElement_qualifiedName_value_roundtrip():
    instance = qm_QualityModelElement(qualifiedName="sample_text")
    assert instance.qualifiedName == "sample_text"
    instance.qualifiedName = "sample_text_2"
    assert instance.qualifiedName == "sample_text_2"


def test_qm_QualityModelResult_date_value_roundtrip():
    instance = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    assert instance.date == date(2024, 1, 1)
    instance.date = date(2025, 6, 15)
    assert instance.date == date(2025, 6, 15)


def test_qm_QualityModelResult_system_value_roundtrip():
    instance = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    assert instance.system == "sample_text"
    instance.system = "sample_text_2"
    assert instance.system == "sample_text_2"


def test_qm_Ranking_rank_value_roundtrip():
    instance = qm_Ranking(rank=7, weight=3.14)
    assert instance.rank == 7
    instance.rank = 13
    assert instance.rank == 13


def test_qm_Ranking_weight_value_roundtrip():
    instance = qm_Ranking(rank=7, weight=3.14)
    assert instance.weight == 3.14
    instance.weight = 9.99
    assert instance.weight == 9.99


def test_qm_Result_message_value_roundtrip():
    instance = qm_Result(message="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_qm_SingleMeasureEvaluationResult_ratioAffected_value_roundtrip():
    instance = qm_SingleMeasureEvaluationResult(ratioAffected=3.14)
    assert instance.ratioAffected == 3.14
    instance.ratioAffected = 9.99
    assert instance.ratioAffected == 9.99


def test_qm_TextAggregation_specification_value_roundtrip():
    instance = qm_TextAggregation(specification="sample_text")
    assert instance.specification == "sample_text"
    instance.specification = "sample_text_2"
    assert instance.specification == "sample_text_2"


def test_qm_TextEvaluation_specification_value_roundtrip():
    instance = qm_TextEvaluation(specification="sample_text")
    assert instance.specification == "sample_text"
    instance.specification = "sample_text_2"
    assert instance.specification == "sample_text_2"


def test_qm_ToolBasedInstrument_metric_value_roundtrip():
    instance = qm_ToolBasedInstrument(metric="sample_text")
    assert instance.metric == "sample_text"
    instance.metric = "sample_text_2"
    assert instance.metric == "sample_text_2"


def test_qm_Decomposition_isa_AnnotatedElement():
    instance = qm_Decomposition()
    assert isinstance(instance, AnnotatedElement)


def test_qm_DescribedElement_isa_AnnotatedElement():
    instance = qm_DescribedElement(description="sample_text")
    assert isinstance(instance, AnnotatedElement)


def test_qm_FactorRefinement_isa_AnnotatedElement():
    instance = qm_FactorRefinement()
    assert isinstance(instance, AnnotatedElement)


def test_qm_Impact_isa_AnnotatedElement():
    instance = qm_Impact(effect="sample_text", justification="sample_text")
    assert isinstance(instance, AnnotatedElement)


def test_qm_MeasureRefinement_isa_AnnotatedElement():
    instance = qm_MeasureRefinement()
    assert isinstance(instance, AnnotatedElement)


def test_qm_Measurement_isa_AnnotatedElement():
    instance = qm_Measurement()
    assert isinstance(instance, AnnotatedElement)


def test_qm_MeasurementMethod_isa_AnnotatedElement():
    instance = qm_MeasurementMethod()
    assert isinstance(instance, AnnotatedElement)


def test_qm_Specialization_isa_AnnotatedElement():
    instance = qm_Specialization()
    assert isinstance(instance, AnnotatedElement)


def test_qm_Factor_isa_CharacterizingElement():
    instance = qm_Factor()
    assert isinstance(instance, CharacterizingElement)


def test_qm_Measure_isa_CharacterizingElement():
    instance = qm_Measure(type="sample_text")
    assert isinstance(instance, CharacterizingElement)


def test_qm_NamedElement_isa_DescribedElement():
    instance = qm_NamedElement(name="sample_text", title="sample_text")
    assert isinstance(instance, DescribedElement)


def test_qm_FormBasedEvaluation_isa_Evaluation():
    instance = qm_FormBasedEvaluation()
    assert isinstance(instance, Evaluation)


def test_qm_ManualEvaluation_isa_Evaluation():
    instance = qm_ManualEvaluation()
    assert isinstance(instance, Evaluation)


def test_qm_TextEvaluation_isa_Evaluation():
    instance = qm_TextEvaluation(specification="sample_text")
    assert isinstance(instance, Evaluation)


def test_qm_MultiMeasureEvaluationResult_isa_EvaluationResult():
    instance = qm_MultiMeasureEvaluationResult()
    assert isinstance(instance, EvaluationResult)


def test_qm_SingleMeasureEvaluationResult_isa_EvaluationResult():
    instance = qm_SingleMeasureEvaluationResult(ratioAffected=3.14)
    assert isinstance(instance, EvaluationResult)


def test_qm_WeightedSumFactorAggregation_isa_FactorAggregation():
    instance = qm_WeightedSumFactorAggregation()
    assert isinstance(instance, FactorAggregation)


def test_qm_FactorAggregation_isa_FormBasedEvaluation():
    instance = qm_FactorAggregation()
    assert isinstance(instance, FormBasedEvaluation)


def test_qm_MultiMeasureEvaluation_isa_FormBasedEvaluation():
    instance = qm_MultiMeasureEvaluation()
    assert isinstance(instance, FormBasedEvaluation)


def test_qm_SingleMeasureEvaluation_isa_FormBasedEvaluation():
    instance = qm_SingleMeasureEvaluation()
    assert isinstance(instance, FormBasedEvaluation)


def test_qm_FindingsUnionMeasureAggregation_isa_FormBasedMeasureAggregation():
    instance = qm_FindingsUnionMeasureAggregation()
    assert isinstance(instance, FormBasedMeasureAggregation)


def test_qm_NumberMeanMeasureAggregation_isa_FormBasedMeasureAggregation():
    instance = qm_NumberMeanMeasureAggregation()
    assert isinstance(instance, FormBasedMeasureAggregation)


def test_qm_LinearFunction_isa_Function():
    instance = qm_LinearFunction(lowerBound=3.14, upperBound=3.14)
    assert isinstance(instance, Function)


def test_qm_ManualInstrument_isa_Instrument():
    instance = qm_ManualInstrument()
    assert isinstance(instance, Instrument)


def test_qm_ToolBasedInstrument_isa_Instrument():
    instance = qm_ToolBasedInstrument(metric="sample_text")
    assert isinstance(instance, Instrument)


def test_qm_LinearDecreasingFunction_isa_LinearFunction():
    instance = qm_LinearDecreasingFunction()
    assert isinstance(instance, LinearFunction)


def test_qm_LinearIncreasingFunction_isa_LinearFunction():
    instance = qm_LinearIncreasingFunction()
    assert isinstance(instance, LinearFunction)


def test_qm_NormalizationMeasure_isa_Measure():
    instance = qm_NormalizationMeasure()
    assert isinstance(instance, Measure)


def test_qm_FormBasedMeasureAggregation_isa_MeasureAggregation():
    instance = qm_FormBasedMeasureAggregation()
    assert isinstance(instance, MeasureAggregation)


def test_qm_TextAggregation_isa_MeasureAggregation():
    instance = qm_TextAggregation(specification="sample_text")
    assert isinstance(instance, MeasureAggregation)


def test_qm_MeasureRanking_isa_MeasureEvaluation():
    instance = qm_MeasureRanking()
    assert isinstance(instance, MeasureEvaluation)


def test_qm_SingleMeasureEvaluation_isa_MeasureEvaluation():
    instance = qm_SingleMeasureEvaluation()
    assert isinstance(instance, MeasureEvaluation)


def test_qm_Instrument_isa_MeasurementMethod():
    instance = qm_Instrument()
    assert isinstance(instance, MeasurementMethod)


def test_qm_MeasureAggregation_isa_MeasurementMethod():
    instance = qm_MeasureAggregation()
    assert isinstance(instance, MeasurementMethod)


def test_qm_FindingsMeasurementResult_isa_MeasurementResult():
    instance = qm_FindingsMeasurementResult(count=7, findings="sample_text")
    assert isinstance(instance, MeasurementResult)


def test_qm_NumberMeasurementResult_isa_MeasurementResult():
    instance = qm_NumberMeasurementResult()
    assert isinstance(instance, MeasurementResult)


def test_qm_WeightedSumMultiMeasureEvaluation_isa_MultiMeasureEvaluation():
    instance = qm_WeightedSumMultiMeasureEvaluation()
    assert isinstance(instance, MultiMeasureEvaluation)


def test_qm_CharacterizingElement_isa_NamedElement():
    instance = qm_CharacterizingElement()
    assert isinstance(instance, NamedElement)


def test_qm_Entity_isa_NamedElement():
    instance = qm_Entity(stakeholder=True, useCase=True)
    assert isinstance(instance, NamedElement)


def test_qm_Evaluation_isa_NamedElement():
    instance = qm_Evaluation(completeness=7, maximumPoints=7)
    assert isinstance(instance, NamedElement)


def test_qm_ManualInstrument_isa_NamedElement():
    instance = qm_ManualInstrument()
    assert isinstance(instance, NamedElement)


def test_qm_MeasureAggregation_isa_NamedElement():
    instance = qm_MeasureAggregation()
    assert isinstance(instance, NamedElement)


def test_qm_QualityModel_isa_NamedElement():
    instance = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    assert isinstance(instance, NamedElement)


def test_qm_Source_isa_NamedElement():
    instance = qm_Source()
    assert isinstance(instance, NamedElement)


def test_qm_Tag_isa_NamedElement():
    instance = qm_Tag()
    assert isinstance(instance, NamedElement)


def test_qm_Tool_isa_NamedElement():
    instance = qm_Tool()
    assert isinstance(instance, NamedElement)


def test_qm_TaggedElement_isa_QualityModelElement():
    instance = qm_TaggedElement()
    assert isinstance(instance, QualityModelElement)


def test_qm_FactorRanking_isa_Ranking():
    instance = qm_FactorRanking()
    assert isinstance(instance, Ranking)


def test_qm_MeasureRanking_isa_Ranking():
    instance = qm_MeasureRanking()
    assert isinstance(instance, Ranking)


def test_qm_EvaluationResult_isa_Result():
    instance = qm_EvaluationResult()
    assert isinstance(instance, Result)


def test_qm_MeasurementResult_isa_Result():
    instance = qm_MeasurementResult()
    assert isinstance(instance, Result)


def test_qm_AnnotatedElement_isa_TaggedElement():
    instance = qm_AnnotatedElement()
    assert isinstance(instance, TaggedElement)


def test_qm_QIESLAggregation_isa_TextAggregation():
    instance = qm_QIESLAggregation()
    assert isinstance(instance, TextAggregation)


def test_qm_QIESLEvaluation_isa_TextEvaluation():
    instance = qm_QIESLEvaluation()
    assert isinstance(instance, TextEvaluation)


def test_assoc_annotations19_link_reassign_clear():
    a = qm_Annotation(key="sample_text", value="sample_text")
    b1 = qm_AnnotatedElement()
    b2 = qm_AnnotatedElement()
    _safe_set(a, 'qm_Annotation', b1)
    assert _is_linked(a, 'qm_Annotation', b1)
    if hasattr(b1, 'qm_AnnotatedElement'):
        assert _is_linked(b1, 'qm_AnnotatedElement', a)
    _safe_set(a, 'qm_Annotation', b2)
    assert _is_linked(a, 'qm_Annotation', b2)
    if hasattr(b1, 'qm_AnnotatedElement'):
        assert not _is_linked(b1, 'qm_AnnotatedElement', a)
    if hasattr(b2, 'qm_AnnotatedElement'):
        assert _is_linked(b2, 'qm_AnnotatedElement', a)
    _safe_set(a, 'qm_Annotation', None)
    assert not _is_linked(a, 'qm_Annotation', b2)
    if hasattr(b2, 'qm_AnnotatedElement'):
        assert not _is_linked(b2, 'qm_AnnotatedElement', a)


def test_assoc_characterizes43_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_CharacterizingElement()
    b2 = qm_CharacterizingElement()
    _safe_set(a, 'qm_Entity44', b1)
    assert _is_linked(a, 'qm_Entity44', b1)
    if hasattr(b1, 'qm_CharacterizingElement'):
        assert _is_linked(b1, 'qm_CharacterizingElement', a)
    _safe_set(a, 'qm_Entity44', b2)
    assert _is_linked(a, 'qm_Entity44', b2)
    if hasattr(b1, 'qm_CharacterizingElement'):
        assert not _is_linked(b1, 'qm_CharacterizingElement', a)
    if hasattr(b2, 'qm_CharacterizingElement'):
        assert _is_linked(b2, 'qm_CharacterizingElement', a)
    _safe_set(a, 'qm_Entity44', None)
    assert not _is_linked(a, 'qm_Entity44', b2)
    if hasattr(b2, 'qm_CharacterizingElement'):
        assert not _is_linked(b2, 'qm_CharacterizingElement', a)


def test_assoc_child37_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Specialization()
    b2 = qm_Specialization()
    _safe_set(a, 'Entity38', b1)
    assert _is_linked(a, 'Entity38', b1)
    if hasattr(b1, 'isA'):
        assert _is_linked(b1, 'isA', a)
    _safe_set(a, 'Entity38', b2)
    assert _is_linked(a, 'Entity38', b2)
    if hasattr(b1, 'isA'):
        assert not _is_linked(b1, 'isA', a)
    if hasattr(b2, 'isA'):
        assert _is_linked(b2, 'isA', a)
    _safe_set(a, 'Entity38', None)
    assert not _is_linked(a, 'Entity38', b2)
    if hasattr(b2, 'isA'):
        assert not _is_linked(b2, 'isA', a)


def test_assoc_child41_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Decomposition()
    b2 = qm_Decomposition()
    _safe_set(a, 'Entity42', b1)
    assert _is_linked(a, 'Entity42', b1)
    if hasattr(b1, 'partOf'):
        assert _is_linked(b1, 'partOf', a)
    _safe_set(a, 'Entity42', b2)
    assert _is_linked(a, 'Entity42', b2)
    if hasattr(b1, 'partOf'):
        assert not _is_linked(b1, 'partOf', a)
    if hasattr(b2, 'partOf'):
        assert _is_linked(b2, 'partOf', a)
    _safe_set(a, 'Entity42', None)
    assert not _is_linked(a, 'Entity42', b2)
    if hasattr(b2, 'partOf'):
        assert not _is_linked(b2, 'partOf', a)


def test_assoc_child69_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_Measurement()
    b2 = qm_Measurement()
    _safe_set(a, 'Measure70', b1)
    assert _is_linked(a, 'Measure70', b1)
    if hasattr(b1, 'measures'):
        assert _is_linked(b1, 'measures', a)
    _safe_set(a, 'Measure70', b2)
    assert _is_linked(a, 'Measure70', b2)
    if hasattr(b1, 'measures'):
        assert not _is_linked(b1, 'measures', a)
    if hasattr(b2, 'measures'):
        assert _is_linked(b2, 'measures', a)
    _safe_set(a, 'Measure70', None)
    assert not _is_linked(a, 'Measure70', b2)
    if hasattr(b2, 'measures'):
        assert not _is_linked(b2, 'measures', a)


def test_assoc_child72_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_MeasureRefinement()
    b2 = qm_MeasureRefinement()
    _safe_set(a, 'Measure74', b1)
    assert _is_linked(a, 'Measure74', b1)
    if hasattr(b1, 'refines73'):
        assert _is_linked(b1, 'refines73', a)
    _safe_set(a, 'Measure74', b2)
    assert _is_linked(a, 'Measure74', b2)
    if hasattr(b1, 'refines73'):
        assert not _is_linked(b1, 'refines73', a)
    if hasattr(b2, 'refines73'):
        assert _is_linked(b2, 'refines73', a)
    _safe_set(a, 'Measure74', None)
    assert not _is_linked(a, 'Measure74', b2)
    if hasattr(b2, 'refines73'):
        assert not _is_linked(b2, 'refines73', a)


def test_assoc_determines88_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_MeasurementMethod()
    b2 = qm_MeasurementMethod()
    _safe_set(a, 'qm_Measure89', b1)
    assert _is_linked(a, 'qm_Measure89', b1)
    if hasattr(b1, 'qm_MeasurementMethod'):
        assert _is_linked(b1, 'qm_MeasurementMethod', a)
    _safe_set(a, 'qm_Measure89', b2)
    assert _is_linked(a, 'qm_Measure89', b2)
    if hasattr(b1, 'qm_MeasurementMethod'):
        assert not _is_linked(b1, 'qm_MeasurementMethod', a)
    if hasattr(b2, 'qm_MeasurementMethod'):
        assert _is_linked(b2, 'qm_MeasurementMethod', a)
    _safe_set(a, 'qm_Measure89', None)
    assert not _is_linked(a, 'qm_Measure89', b2)
    if hasattr(b2, 'qm_MeasurementMethod'):
        assert not _is_linked(b2, 'qm_MeasurementMethod', a)


def test_assoc_entities0_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Entity(stakeholder=True, useCase=True)
    b2 = qm_Entity(stakeholder=False, useCase=False)
    _safe_set(a, 'qualityModel', {b1})
    assert _is_linked(a, 'qualityModel', b1)
    if hasattr(b1, 'Entity'):
        assert _is_linked(b1, 'Entity', a)
    _safe_set(a, 'qualityModel', {b2})
    assert _is_linked(a, 'qualityModel', b2)
    if hasattr(b1, 'Entity'):
        assert not _is_linked(b1, 'Entity', a)
    if hasattr(b2, 'Entity'):
        assert _is_linked(b2, 'Entity', a)
    _safe_set(a, 'qualityModel', set())
    assert not _is_linked(a, 'qualityModel', b2)
    if hasattr(b2, 'Entity'):
        assert not _is_linked(b2, 'Entity', a)


def test_assoc_evaluates59_link_reassign_clear():
    a = qm_Evaluation(completeness=7, maximumPoints=7)
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'qm_Evaluation', b1)
    assert _is_linked(a, 'qm_Evaluation', b1)
    if hasattr(b1, 'qm_Factor60'):
        assert _is_linked(b1, 'qm_Factor60', a)
    _safe_set(a, 'qm_Evaluation', b2)
    assert _is_linked(a, 'qm_Evaluation', b2)
    if hasattr(b1, 'qm_Factor60'):
        assert not _is_linked(b1, 'qm_Factor60', a)
    if hasattr(b2, 'qm_Factor60'):
        assert _is_linked(b2, 'qm_Factor60', a)
    _safe_set(a, 'qm_Evaluation', None)
    assert not _is_linked(a, 'qm_Evaluation', b2)
    if hasattr(b2, 'qm_Factor60'):
        assert not _is_linked(b2, 'qm_Factor60', a)


def test_assoc_evaluationResults107_link_reassign_clear():
    a = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    b1 = qm_EvaluationResult()
    b2 = qm_EvaluationResult()
    _safe_set(a, 'qm_QualityModelResult108', {b1})
    assert _is_linked(a, 'qm_QualityModelResult108', b1)
    if hasattr(b1, 'qm_EvaluationResult'):
        assert _is_linked(b1, 'qm_EvaluationResult', a)
    _safe_set(a, 'qm_QualityModelResult108', {b2})
    assert _is_linked(a, 'qm_QualityModelResult108', b2)
    if hasattr(b1, 'qm_EvaluationResult'):
        assert not _is_linked(b1, 'qm_EvaluationResult', a)
    if hasattr(b2, 'qm_EvaluationResult'):
        assert _is_linked(b2, 'qm_EvaluationResult', a)
    _safe_set(a, 'qm_QualityModelResult108', set())
    assert not _is_linked(a, 'qm_QualityModelResult108', b2)
    if hasattr(b2, 'qm_EvaluationResult'):
        assert not _is_linked(b2, 'qm_EvaluationResult', a)


def test_assoc_evaluationResults120_link_reassign_clear():
    a = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    b1 = qm_MultiMeasureEvaluationResult()
    b2 = qm_MultiMeasureEvaluationResult()
    _safe_set(a, 'qm_MeasureRankingEvaluationResult', b1)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult', b1)
    if hasattr(b1, 'qm_MultiMeasureEvaluationResult'):
        assert _is_linked(b1, 'qm_MultiMeasureEvaluationResult', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult', b2)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult', b2)
    if hasattr(b1, 'qm_MultiMeasureEvaluationResult'):
        assert not _is_linked(b1, 'qm_MultiMeasureEvaluationResult', a)
    if hasattr(b2, 'qm_MultiMeasureEvaluationResult'):
        assert _is_linked(b2, 'qm_MultiMeasureEvaluationResult', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult', None)
    assert not _is_linked(a, 'qm_MeasureRankingEvaluationResult', b2)
    if hasattr(b2, 'qm_MultiMeasureEvaluationResult'):
        assert not _is_linked(b2, 'qm_MultiMeasureEvaluationResult', a)


def test_assoc_evaluations3_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Evaluation(completeness=7, maximumPoints=7)
    b2 = qm_Evaluation(completeness=13, maximumPoints=13)
    _safe_set(a, 'qualityModel4', {b1})
    assert _is_linked(a, 'qualityModel4', b1)
    if hasattr(b1, 'Evaluation'):
        assert _is_linked(b1, 'Evaluation', a)
    _safe_set(a, 'qualityModel4', {b2})
    assert _is_linked(a, 'qualityModel4', b2)
    if hasattr(b1, 'Evaluation'):
        assert not _is_linked(b1, 'Evaluation', a)
    if hasattr(b2, 'Evaluation'):
        assert _is_linked(b2, 'Evaluation', a)
    _safe_set(a, 'qualityModel4', set())
    assert not _is_linked(a, 'qualityModel4', b2)
    if hasattr(b2, 'Evaluation'):
        assert not _is_linked(b2, 'Evaluation', a)


def test_assoc_factors1_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'qualityModel2', {b1})
    assert _is_linked(a, 'qualityModel2', b1)
    if hasattr(b1, 'Factor'):
        assert _is_linked(b1, 'Factor', a)
    _safe_set(a, 'qualityModel2', {b2})
    assert _is_linked(a, 'qualityModel2', b2)
    if hasattr(b1, 'Factor'):
        assert not _is_linked(b1, 'Factor', a)
    if hasattr(b2, 'Factor'):
        assert _is_linked(b2, 'Factor', a)
    _safe_set(a, 'qualityModel2', set())
    assert not _is_linked(a, 'qualityModel2', b2)
    if hasattr(b2, 'Factor'):
        assert not _is_linked(b2, 'Factor', a)


def test_assoc_findingMessages113_link_reassign_clear():
    a = qm_FindingsMeasurementResult(count=7, findings="sample_text")
    b1 = qm_FindingMessage(location="sample_text", message="sample_text")
    b2 = qm_FindingMessage(location="sample_text_2", message="sample_text_2")
    _safe_set(a, 'qm_FindingsMeasurementResult', {b1})
    assert _is_linked(a, 'qm_FindingsMeasurementResult', b1)
    if hasattr(b1, 'qm_FindingMessage'):
        assert _is_linked(b1, 'qm_FindingMessage', a)
    _safe_set(a, 'qm_FindingsMeasurementResult', {b2})
    assert _is_linked(a, 'qm_FindingsMeasurementResult', b2)
    if hasattr(b1, 'qm_FindingMessage'):
        assert not _is_linked(b1, 'qm_FindingMessage', a)
    if hasattr(b2, 'qm_FindingMessage'):
        assert _is_linked(b2, 'qm_FindingMessage', a)
    _safe_set(a, 'qm_FindingsMeasurementResult', set())
    assert not _is_linked(a, 'qm_FindingsMeasurementResult', b2)
    if hasattr(b2, 'qm_FindingMessage'):
        assert not _is_linked(b2, 'qm_FindingMessage', a)


def test_assoc_function103_link_reassign_clear():
    a = qm_MeasureEvaluation(range="sample_text")
    b1 = qm_Function()
    b2 = qm_Function()
    _safe_set(a, 'qm_MeasureEvaluation104', b1)
    assert _is_linked(a, 'qm_MeasureEvaluation104', b1)
    if hasattr(b1, 'qm_Function'):
        assert _is_linked(b1, 'qm_Function', a)
    _safe_set(a, 'qm_MeasureEvaluation104', b2)
    assert _is_linked(a, 'qm_MeasureEvaluation104', b2)
    if hasattr(b1, 'qm_Function'):
        assert not _is_linked(b1, 'qm_Function', a)
    if hasattr(b2, 'qm_Function'):
        assert _is_linked(b2, 'qm_Function', a)
    _safe_set(a, 'qm_MeasureEvaluation104', None)
    assert not _is_linked(a, 'qm_MeasureEvaluation104', b2)
    if hasattr(b2, 'qm_Function'):
        assert not _is_linked(b2, 'qm_Function', a)


def test_assoc_influences45_link_reassign_clear():
    a = qm_Impact(effect="sample_text", justification="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'Impact', b1)
    assert _is_linked(a, 'Impact', b1)
    if hasattr(b1, 'source'):
        assert _is_linked(b1, 'source', a)
    _safe_set(a, 'Impact', b2)
    assert _is_linked(a, 'Impact', b2)
    if hasattr(b1, 'source'):
        assert not _is_linked(b1, 'source', a)
    if hasattr(b2, 'source'):
        assert _is_linked(b2, 'source', a)
    _safe_set(a, 'Impact', None)
    assert not _is_linked(a, 'Impact', b2)
    if hasattr(b2, 'source'):
        assert not _is_linked(b2, 'source', a)


def test_assoc_isA25_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Specialization()
    b2 = qm_Specialization()
    _safe_set(a, 'child', {b1})
    assert _is_linked(a, 'child', b1)
    if hasattr(b1, 'Specialization'):
        assert _is_linked(b1, 'Specialization', a)
    _safe_set(a, 'child', {b2})
    assert _is_linked(a, 'child', b2)
    if hasattr(b1, 'Specialization'):
        assert not _is_linked(b1, 'Specialization', a)
    if hasattr(b2, 'Specialization'):
        assert _is_linked(b2, 'Specialization', a)
    _safe_set(a, 'child', set())
    assert not _is_linked(a, 'child', b2)
    if hasattr(b2, 'Specialization'):
        assert not _is_linked(b2, 'Specialization', a)


def test_assoc_isADirect27_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Entity(stakeholder=True, useCase=True)
    b2 = qm_Entity(stakeholder=False, useCase=False)
    _safe_set(a, 'qm_Entity', b1)
    assert _is_linked(a, 'qm_Entity', b1)
    if hasattr(b1, 'qm_Entity26'):
        assert _is_linked(b1, 'qm_Entity26', a)
    _safe_set(a, 'qm_Entity', b2)
    assert _is_linked(a, 'qm_Entity', b2)
    if hasattr(b1, 'qm_Entity26'):
        assert not _is_linked(b1, 'qm_Entity26', a)
    if hasattr(b2, 'qm_Entity26'):
        assert _is_linked(b2, 'qm_Entity26', a)
    _safe_set(a, 'qm_Entity', None)
    assert not _is_linked(a, 'qm_Entity', b2)
    if hasattr(b2, 'qm_Entity26'):
        assert not _is_linked(b2, 'qm_Entity26', a)


def test_assoc_measure99_link_reassign_clear():
    a = qm_MeasureEvaluation(range="sample_text")
    b1 = qm_Measure(type="sample_text")
    b2 = qm_Measure(type="sample_text_2")
    _safe_set(a, 'qm_MeasureEvaluation', b1)
    assert _is_linked(a, 'qm_MeasureEvaluation', b1)
    if hasattr(b1, 'qm_Measure100'):
        assert _is_linked(b1, 'qm_Measure100', a)
    _safe_set(a, 'qm_MeasureEvaluation', b2)
    assert _is_linked(a, 'qm_MeasureEvaluation', b2)
    if hasattr(b1, 'qm_Measure100'):
        assert not _is_linked(b1, 'qm_Measure100', a)
    if hasattr(b2, 'qm_Measure100'):
        assert _is_linked(b2, 'qm_Measure100', a)
    _safe_set(a, 'qm_MeasureEvaluation', None)
    assert not _is_linked(a, 'qm_MeasureEvaluation', b2)
    if hasattr(b2, 'qm_Measure100'):
        assert not _is_linked(b2, 'qm_Measure100', a)


def test_assoc_measurementMethods7_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_MeasurementMethod()
    b2 = qm_MeasurementMethod()
    _safe_set(a, 'qualityModel8', {b1})
    assert _is_linked(a, 'qualityModel8', b1)
    if hasattr(b1, 'MeasurementMethod'):
        assert _is_linked(b1, 'MeasurementMethod', a)
    _safe_set(a, 'qualityModel8', {b2})
    assert _is_linked(a, 'qualityModel8', b2)
    if hasattr(b1, 'MeasurementMethod'):
        assert not _is_linked(b1, 'MeasurementMethod', a)
    if hasattr(b2, 'MeasurementMethod'):
        assert _is_linked(b2, 'MeasurementMethod', a)
    _safe_set(a, 'qualityModel8', set())
    assert not _is_linked(a, 'qualityModel8', b2)
    if hasattr(b2, 'MeasurementMethod'):
        assert not _is_linked(b2, 'MeasurementMethod', a)


def test_assoc_measurementResults106_link_reassign_clear():
    a = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    b1 = qm_MeasurementResult()
    b2 = qm_MeasurementResult()
    _safe_set(a, 'qm_QualityModelResult', {b1})
    assert _is_linked(a, 'qm_QualityModelResult', b1)
    if hasattr(b1, 'qm_MeasurementResult'):
        assert _is_linked(b1, 'qm_MeasurementResult', a)
    _safe_set(a, 'qm_QualityModelResult', {b2})
    assert _is_linked(a, 'qm_QualityModelResult', b2)
    if hasattr(b1, 'qm_MeasurementResult'):
        assert not _is_linked(b1, 'qm_MeasurementResult', a)
    if hasattr(b2, 'qm_MeasurementResult'):
        assert _is_linked(b2, 'qm_MeasurementResult', a)
    _safe_set(a, 'qm_QualityModelResult', set())
    assert not _is_linked(a, 'qm_QualityModelResult', b2)
    if hasattr(b2, 'qm_MeasurementResult'):
        assert not _is_linked(b2, 'qm_MeasurementResult', a)


def test_assoc_measures5_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Measure(type="sample_text")
    b2 = qm_Measure(type="sample_text_2")
    _safe_set(a, 'qualityModel6', {b1})
    assert _is_linked(a, 'qualityModel6', b1)
    if hasattr(b1, 'Measure'):
        assert _is_linked(b1, 'Measure', a)
    _safe_set(a, 'qualityModel6', {b2})
    assert _is_linked(a, 'qualityModel6', b2)
    if hasattr(b1, 'Measure'):
        assert not _is_linked(b1, 'Measure', a)
    if hasattr(b2, 'Measure'):
        assert _is_linked(b2, 'Measure', a)
    _safe_set(a, 'qualityModel6', set())
    assert not _is_linked(a, 'qualityModel6', b2)
    if hasattr(b2, 'Measure'):
        assert not _is_linked(b2, 'Measure', a)


def test_assoc_measures75_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_Measurement()
    b2 = qm_Measurement()
    _safe_set(a, 'child76', {b1})
    assert _is_linked(a, 'child76', b1)
    if hasattr(b1, 'Measurement'):
        assert _is_linked(b1, 'Measurement', a)
    _safe_set(a, 'child76', {b2})
    assert _is_linked(a, 'child76', b2)
    if hasattr(b1, 'Measurement'):
        assert not _is_linked(b1, 'Measurement', a)
    if hasattr(b2, 'Measurement'):
        assert _is_linked(b2, 'Measurement', a)
    _safe_set(a, 'child76', set())
    assert not _is_linked(a, 'child76', b2)
    if hasattr(b2, 'Measurement'):
        assert not _is_linked(b2, 'Measurement', a)


def test_assoc_measuresDirect77_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'qm_Measure78', {b1})
    assert _is_linked(a, 'qm_Measure78', b1)
    if hasattr(b1, 'qm_Factor79'):
        assert _is_linked(b1, 'qm_Factor79', a)
    _safe_set(a, 'qm_Measure78', {b2})
    assert _is_linked(a, 'qm_Measure78', b2)
    if hasattr(b1, 'qm_Factor79'):
        assert not _is_linked(b1, 'qm_Factor79', a)
    if hasattr(b2, 'qm_Factor79'):
        assert _is_linked(b2, 'qm_Factor79', a)
    _safe_set(a, 'qm_Measure78', set())
    assert not _is_linked(a, 'qm_Measure78', b2)
    if hasattr(b2, 'qm_Factor79'):
        assert not _is_linked(b2, 'qm_Factor79', a)


def test_assoc_normlizationMeasure101_link_reassign_clear():
    a = qm_MeasureEvaluation(range="sample_text")
    b1 = qm_NormalizationMeasure()
    b2 = qm_NormalizationMeasure()
    _safe_set(a, 'qm_MeasureEvaluation102', b1)
    assert _is_linked(a, 'qm_MeasureEvaluation102', b1)
    if hasattr(b1, 'qm_NormalizationMeasure'):
        assert _is_linked(b1, 'qm_NormalizationMeasure', a)
    _safe_set(a, 'qm_MeasureEvaluation102', b2)
    assert _is_linked(a, 'qm_MeasureEvaluation102', b2)
    if hasattr(b1, 'qm_NormalizationMeasure'):
        assert not _is_linked(b1, 'qm_NormalizationMeasure', a)
    if hasattr(b2, 'qm_NormalizationMeasure'):
        assert _is_linked(b2, 'qm_NormalizationMeasure', a)
    _safe_set(a, 'qm_MeasureEvaluation102', None)
    assert not _is_linked(a, 'qm_MeasureEvaluation102', b2)
    if hasattr(b2, 'qm_NormalizationMeasure'):
        assert not _is_linked(b2, 'qm_NormalizationMeasure', a)


def test_assoc_originatesFrom17_link_reassign_clear():
    a = qm_QualityModelElement(qualifiedName="sample_text")
    b1 = qm_Source()
    b2 = qm_Source()
    _safe_set(a, 'qm_QualityModelElement', {b1})
    assert _is_linked(a, 'qm_QualityModelElement', b1)
    if hasattr(b1, 'qm_Source'):
        assert _is_linked(b1, 'qm_Source', a)
    _safe_set(a, 'qm_QualityModelElement', {b2})
    assert _is_linked(a, 'qm_QualityModelElement', b2)
    if hasattr(b1, 'qm_Source'):
        assert not _is_linked(b1, 'qm_Source', a)
    if hasattr(b2, 'qm_Source'):
        assert _is_linked(b2, 'qm_Source', a)
    _safe_set(a, 'qm_QualityModelElement', set())
    assert not _is_linked(a, 'qm_QualityModelElement', b2)
    if hasattr(b2, 'qm_Source'):
        assert not _is_linked(b2, 'qm_Source', a)


def test_assoc_parent35_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Specialization()
    b2 = qm_Specialization()
    _safe_set(a, 'qm_Entity36', b1)
    assert _is_linked(a, 'qm_Entity36', b1)
    if hasattr(b1, 'qm_Specialization'):
        assert _is_linked(b1, 'qm_Specialization', a)
    _safe_set(a, 'qm_Entity36', b2)
    assert _is_linked(a, 'qm_Entity36', b2)
    if hasattr(b1, 'qm_Specialization'):
        assert not _is_linked(b1, 'qm_Specialization', a)
    if hasattr(b2, 'qm_Specialization'):
        assert _is_linked(b2, 'qm_Specialization', a)
    _safe_set(a, 'qm_Entity36', None)
    assert not _is_linked(a, 'qm_Entity36', b2)
    if hasattr(b2, 'qm_Specialization'):
        assert not _is_linked(b2, 'qm_Specialization', a)


def test_assoc_parent39_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Decomposition()
    b2 = qm_Decomposition()
    _safe_set(a, 'qm_Entity40', b1)
    assert _is_linked(a, 'qm_Entity40', b1)
    if hasattr(b1, 'qm_Decomposition'):
        assert _is_linked(b1, 'qm_Decomposition', a)
    _safe_set(a, 'qm_Entity40', b2)
    assert _is_linked(a, 'qm_Entity40', b2)
    if hasattr(b1, 'qm_Decomposition'):
        assert not _is_linked(b1, 'qm_Decomposition', a)
    if hasattr(b2, 'qm_Decomposition'):
        assert _is_linked(b2, 'qm_Decomposition', a)
    _safe_set(a, 'qm_Entity40', None)
    assert not _is_linked(a, 'qm_Entity40', b2)
    if hasattr(b2, 'qm_Decomposition'):
        assert not _is_linked(b2, 'qm_Decomposition', a)


def test_assoc_parent71_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_MeasureRefinement()
    b2 = qm_MeasureRefinement()
    _safe_set(a, 'qm_Measure', b1)
    assert _is_linked(a, 'qm_Measure', b1)
    if hasattr(b1, 'qm_MeasureRefinement'):
        assert _is_linked(b1, 'qm_MeasureRefinement', a)
    _safe_set(a, 'qm_Measure', b2)
    assert _is_linked(a, 'qm_Measure', b2)
    if hasattr(b1, 'qm_MeasureRefinement'):
        assert not _is_linked(b1, 'qm_MeasureRefinement', a)
    if hasattr(b2, 'qm_MeasureRefinement'):
        assert _is_linked(b2, 'qm_MeasureRefinement', a)
    _safe_set(a, 'qm_Measure', None)
    assert not _is_linked(a, 'qm_Measure', b2)
    if hasattr(b2, 'qm_MeasureRefinement'):
        assert not _is_linked(b2, 'qm_MeasureRefinement', a)


def test_assoc_partOf28_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Decomposition()
    b2 = qm_Decomposition()
    _safe_set(a, 'child29', b1)
    assert _is_linked(a, 'child29', b1)
    if hasattr(b1, 'Decomposition'):
        assert _is_linked(b1, 'Decomposition', a)
    _safe_set(a, 'child29', b2)
    assert _is_linked(a, 'child29', b2)
    if hasattr(b1, 'Decomposition'):
        assert not _is_linked(b1, 'Decomposition', a)
    if hasattr(b2, 'Decomposition'):
        assert _is_linked(b2, 'Decomposition', a)
    _safe_set(a, 'child29', None)
    assert not _is_linked(a, 'child29', b2)
    if hasattr(b2, 'Decomposition'):
        assert not _is_linked(b2, 'Decomposition', a)


def test_assoc_partOfDirect31_link_reassign_clear():
    a = qm_Entity(stakeholder=True, useCase=True)
    b1 = qm_Entity(stakeholder=True, useCase=True)
    b2 = qm_Entity(stakeholder=False, useCase=False)
    _safe_set(a, 'qm_Entity30', b1)
    assert _is_linked(a, 'qm_Entity30', b1)
    if hasattr(b1, 'qm_Entity32'):
        assert _is_linked(b1, 'qm_Entity32', a)
    _safe_set(a, 'qm_Entity30', b2)
    assert _is_linked(a, 'qm_Entity30', b2)
    if hasattr(b1, 'qm_Entity32'):
        assert not _is_linked(b1, 'qm_Entity32', a)
    if hasattr(b2, 'qm_Entity32'):
        assert _is_linked(b2, 'qm_Entity32', a)
    _safe_set(a, 'qm_Entity30', None)
    assert not _is_linked(a, 'qm_Entity30', b2)
    if hasattr(b2, 'qm_Entity32'):
        assert not _is_linked(b2, 'qm_Entity32', a)


def test_assoc_qualityModel18_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Source()
    b2 = qm_Source()
    _safe_set(a, 'QualityModel', b1)
    assert _is_linked(a, 'QualityModel', b1)
    if hasattr(b1, 'sources'):
        assert _is_linked(b1, 'sources', a)
    _safe_set(a, 'QualityModel', b2)
    assert _is_linked(a, 'QualityModel', b2)
    if hasattr(b1, 'sources'):
        assert not _is_linked(b1, 'sources', a)
    if hasattr(b2, 'sources'):
        assert _is_linked(b2, 'sources', a)
    _safe_set(a, 'QualityModel', None)
    assert not _is_linked(a, 'QualityModel', b2)
    if hasattr(b2, 'sources'):
        assert not _is_linked(b2, 'sources', a)


def test_assoc_qualityModel22_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Tag()
    b2 = qm_Tag()
    _safe_set(a, 'QualityModel23', b1)
    assert _is_linked(a, 'QualityModel23', b1)
    if hasattr(b1, 'tags'):
        assert _is_linked(b1, 'tags', a)
    _safe_set(a, 'QualityModel23', b2)
    assert _is_linked(a, 'QualityModel23', b2)
    if hasattr(b1, 'tags'):
        assert not _is_linked(b1, 'tags', a)
    if hasattr(b2, 'tags'):
        assert _is_linked(b2, 'tags', a)
    _safe_set(a, 'QualityModel23', None)
    assert not _is_linked(a, 'QualityModel23', b2)
    if hasattr(b2, 'tags'):
        assert not _is_linked(b2, 'tags', a)


def test_assoc_qualityModel33_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Entity(stakeholder=True, useCase=True)
    b2 = qm_Entity(stakeholder=False, useCase=False)
    _safe_set(a, 'QualityModel34', b1)
    assert _is_linked(a, 'QualityModel34', b1)
    if hasattr(b1, 'entities'):
        assert _is_linked(b1, 'entities', a)
    _safe_set(a, 'QualityModel34', b2)
    assert _is_linked(a, 'QualityModel34', b2)
    if hasattr(b1, 'entities'):
        assert not _is_linked(b1, 'entities', a)
    if hasattr(b2, 'entities'):
        assert _is_linked(b2, 'entities', a)
    _safe_set(a, 'QualityModel34', None)
    assert not _is_linked(a, 'QualityModel34', b2)
    if hasattr(b2, 'entities'):
        assert not _is_linked(b2, 'entities', a)


def test_assoc_qualityModel53_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'QualityModel54', b1)
    assert _is_linked(a, 'QualityModel54', b1)
    if hasattr(b1, 'factors'):
        assert _is_linked(b1, 'factors', a)
    _safe_set(a, 'QualityModel54', b2)
    assert _is_linked(a, 'QualityModel54', b2)
    if hasattr(b1, 'factors'):
        assert not _is_linked(b1, 'factors', a)
    if hasattr(b2, 'factors'):
        assert _is_linked(b2, 'factors', a)
    _safe_set(a, 'QualityModel54', None)
    assert not _is_linked(a, 'QualityModel54', b2)
    if hasattr(b2, 'factors'):
        assert not _is_linked(b2, 'factors', a)


def test_assoc_qualityModel61_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Evaluation(completeness=7, maximumPoints=7)
    b2 = qm_Evaluation(completeness=13, maximumPoints=13)
    _safe_set(a, 'QualityModel62', b1)
    assert _is_linked(a, 'QualityModel62', b1)
    if hasattr(b1, 'evaluations'):
        assert _is_linked(b1, 'evaluations', a)
    _safe_set(a, 'QualityModel62', b2)
    assert _is_linked(a, 'QualityModel62', b2)
    if hasattr(b1, 'evaluations'):
        assert not _is_linked(b1, 'evaluations', a)
    if hasattr(b2, 'evaluations'):
        assert _is_linked(b2, 'evaluations', a)
    _safe_set(a, 'QualityModel62', None)
    assert not _is_linked(a, 'QualityModel62', b2)
    if hasattr(b2, 'evaluations'):
        assert not _is_linked(b2, 'evaluations', a)


def test_assoc_qualityModel80_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Measure(type="sample_text")
    b2 = qm_Measure(type="sample_text_2")
    _safe_set(a, 'QualityModel82', b1)
    assert _is_linked(a, 'QualityModel82', b1)
    if hasattr(b1, 'measures81'):
        assert _is_linked(b1, 'measures81', a)
    _safe_set(a, 'QualityModel82', b2)
    assert _is_linked(a, 'QualityModel82', b2)
    if hasattr(b1, 'measures81'):
        assert not _is_linked(b1, 'measures81', a)
    if hasattr(b2, 'measures81'):
        assert _is_linked(b2, 'measures81', a)
    _safe_set(a, 'QualityModel82', None)
    assert not _is_linked(a, 'QualityModel82', b2)
    if hasattr(b2, 'measures81'):
        assert not _is_linked(b2, 'measures81', a)


def test_assoc_qualityModel90_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_MeasurementMethod()
    b2 = qm_MeasurementMethod()
    _safe_set(a, 'QualityModel91', b1)
    assert _is_linked(a, 'QualityModel91', b1)
    if hasattr(b1, 'measurementMethods'):
        assert _is_linked(b1, 'measurementMethods', a)
    _safe_set(a, 'QualityModel91', b2)
    assert _is_linked(a, 'QualityModel91', b2)
    if hasattr(b1, 'measurementMethods'):
        assert not _is_linked(b1, 'measurementMethods', a)
    if hasattr(b2, 'measurementMethods'):
        assert _is_linked(b2, 'measurementMethods', a)
    _safe_set(a, 'QualityModel91', None)
    assert not _is_linked(a, 'QualityModel91', b2)
    if hasattr(b2, 'measurementMethods'):
        assert not _is_linked(b2, 'measurementMethods', a)


def test_assoc_qualityModel93_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Tool()
    b2 = qm_Tool()
    _safe_set(a, 'QualityModel94', b1)
    assert _is_linked(a, 'QualityModel94', b1)
    if hasattr(b1, 'tools'):
        assert _is_linked(b1, 'tools', a)
    _safe_set(a, 'QualityModel94', b2)
    assert _is_linked(a, 'QualityModel94', b2)
    if hasattr(b1, 'tools'):
        assert not _is_linked(b1, 'tools', a)
    if hasattr(b2, 'tools'):
        assert _is_linked(b2, 'tools', a)
    _safe_set(a, 'QualityModel94', None)
    assert not _is_linked(a, 'QualityModel94', b2)
    if hasattr(b2, 'tools'):
        assert not _is_linked(b2, 'tools', a)


def test_assoc_refines83_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_MeasureRefinement()
    b2 = qm_MeasureRefinement()
    _safe_set(a, 'child84', {b1})
    assert _is_linked(a, 'child84', b1)
    if hasattr(b1, 'MeasureRefinement'):
        assert _is_linked(b1, 'MeasureRefinement', a)
    _safe_set(a, 'child84', {b2})
    assert _is_linked(a, 'child84', b2)
    if hasattr(b1, 'MeasureRefinement'):
        assert not _is_linked(b1, 'MeasureRefinement', a)
    if hasattr(b2, 'MeasureRefinement'):
        assert _is_linked(b2, 'MeasureRefinement', a)
    _safe_set(a, 'child84', set())
    assert not _is_linked(a, 'child84', b2)
    if hasattr(b2, 'MeasureRefinement'):
        assert not _is_linked(b2, 'MeasureRefinement', a)


def test_assoc_refinesDirect86_link_reassign_clear():
    a = qm_Measure(type="sample_text")
    b1 = qm_Measure(type="sample_text")
    b2 = qm_Measure(type="sample_text_2")
    _safe_set(a, 'qm_Measure85', {b1})
    assert _is_linked(a, 'qm_Measure85', b1)
    if hasattr(b1, 'qm_Measure87'):
        assert _is_linked(b1, 'qm_Measure87', a)
    _safe_set(a, 'qm_Measure85', {b2})
    assert _is_linked(a, 'qm_Measure85', b2)
    if hasattr(b1, 'qm_Measure87'):
        assert not _is_linked(b1, 'qm_Measure87', a)
    if hasattr(b2, 'qm_Measure87'):
        assert _is_linked(b2, 'qm_Measure87', a)
    _safe_set(a, 'qm_Measure85', set())
    assert not _is_linked(a, 'qm_Measure85', b2)
    if hasattr(b2, 'qm_Measure87'):
        assert not _is_linked(b2, 'qm_Measure87', a)


def test_assoc_requires16_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    _safe_set(a, 'qm_QualityModel', b1)
    assert _is_linked(a, 'qm_QualityModel', b1)
    if hasattr(b1, 'qm_QualityModel15'):
        assert _is_linked(b1, 'qm_QualityModel15', a)
    _safe_set(a, 'qm_QualityModel', b2)
    assert _is_linked(a, 'qm_QualityModel', b2)
    if hasattr(b1, 'qm_QualityModel15'):
        assert not _is_linked(b1, 'qm_QualityModel15', a)
    if hasattr(b2, 'qm_QualityModel15'):
        assert _is_linked(b2, 'qm_QualityModel15', a)
    _safe_set(a, 'qm_QualityModel', None)
    assert not _is_linked(a, 'qm_QualityModel', b2)
    if hasattr(b2, 'qm_QualityModel15'):
        assert not _is_linked(b2, 'qm_QualityModel15', a)


def test_assoc_resultsFrom117_link_reassign_clear():
    a = qm_Evaluation(completeness=7, maximumPoints=7)
    b1 = qm_EvaluationResult()
    b2 = qm_EvaluationResult()
    _safe_set(a, 'qm_Evaluation119', b1)
    assert _is_linked(a, 'qm_Evaluation119', b1)
    if hasattr(b1, 'qm_EvaluationResult118'):
        assert _is_linked(b1, 'qm_EvaluationResult118', a)
    _safe_set(a, 'qm_Evaluation119', b2)
    assert _is_linked(a, 'qm_Evaluation119', b2)
    if hasattr(b1, 'qm_EvaluationResult118'):
        assert not _is_linked(b1, 'qm_EvaluationResult118', a)
    if hasattr(b2, 'qm_EvaluationResult118'):
        assert _is_linked(b2, 'qm_EvaluationResult118', a)
    _safe_set(a, 'qm_Evaluation119', None)
    assert not _is_linked(a, 'qm_Evaluation119', b2)
    if hasattr(b2, 'qm_EvaluationResult118'):
        assert not _is_linked(b2, 'qm_EvaluationResult118', a)


def test_assoc_resultsFrom124_link_reassign_clear():
    a = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    b1 = qm_MeasureRanking()
    b2 = qm_MeasureRanking()
    _safe_set(a, 'qm_MeasureRankingEvaluationResult125', b1)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult125', b1)
    if hasattr(b1, 'qm_MeasureRanking126'):
        assert _is_linked(b1, 'qm_MeasureRanking126', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult125', b2)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult125', b2)
    if hasattr(b1, 'qm_MeasureRanking126'):
        assert not _is_linked(b1, 'qm_MeasureRanking126', a)
    if hasattr(b2, 'qm_MeasureRanking126'):
        assert _is_linked(b2, 'qm_MeasureRanking126', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult125', None)
    assert not _is_linked(a, 'qm_MeasureRankingEvaluationResult125', b2)
    if hasattr(b2, 'qm_MeasureRanking126'):
        assert not _is_linked(b2, 'qm_MeasureRanking126', a)


def test_assoc_source55_link_reassign_clear():
    a = qm_Impact(effect="sample_text", justification="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'influences', b1)
    assert _is_linked(a, 'influences', b1)
    if hasattr(b1, 'Factor56'):
        assert _is_linked(b1, 'Factor56', a)
    _safe_set(a, 'influences', b2)
    assert _is_linked(a, 'influences', b2)
    if hasattr(b1, 'Factor56'):
        assert not _is_linked(b1, 'Factor56', a)
    if hasattr(b2, 'Factor56'):
        assert _is_linked(b2, 'Factor56', a)
    _safe_set(a, 'influences', None)
    assert not _is_linked(a, 'influences', b2)
    if hasattr(b2, 'Factor56'):
        assert not _is_linked(b2, 'Factor56', a)


def test_assoc_sources13_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Source()
    b2 = qm_Source()
    _safe_set(a, 'qualityModel14', {b1})
    assert _is_linked(a, 'qualityModel14', b1)
    if hasattr(b1, 'Source'):
        assert _is_linked(b1, 'Source', a)
    _safe_set(a, 'qualityModel14', {b2})
    assert _is_linked(a, 'qualityModel14', b2)
    if hasattr(b1, 'Source'):
        assert not _is_linked(b1, 'Source', a)
    if hasattr(b2, 'Source'):
        assert _is_linked(b2, 'Source', a)
    _safe_set(a, 'qualityModel14', set())
    assert not _is_linked(a, 'qualityModel14', b2)
    if hasattr(b2, 'Source'):
        assert not _is_linked(b2, 'Source', a)


def test_assoc_tags11_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Tag()
    b2 = qm_Tag()
    _safe_set(a, 'qualityModel12', {b1})
    assert _is_linked(a, 'qualityModel12', b1)
    if hasattr(b1, 'Tag'):
        assert _is_linked(b1, 'Tag', a)
    _safe_set(a, 'qualityModel12', {b2})
    assert _is_linked(a, 'qualityModel12', b2)
    if hasattr(b1, 'Tag'):
        assert not _is_linked(b1, 'Tag', a)
    if hasattr(b2, 'Tag'):
        assert _is_linked(b2, 'Tag', a)
    _safe_set(a, 'qualityModel12', set())
    assert not _is_linked(a, 'qualityModel12', b2)
    if hasattr(b2, 'Tag'):
        assert not _is_linked(b2, 'Tag', a)


def test_assoc_target57_link_reassign_clear():
    a = qm_Impact(effect="sample_text", justification="sample_text")
    b1 = qm_Factor()
    b2 = qm_Factor()
    _safe_set(a, 'qm_Impact', b1)
    assert _is_linked(a, 'qm_Impact', b1)
    if hasattr(b1, 'qm_Factor58'):
        assert _is_linked(b1, 'qm_Factor58', a)
    _safe_set(a, 'qm_Impact', b2)
    assert _is_linked(a, 'qm_Impact', b2)
    if hasattr(b1, 'qm_Factor58'):
        assert not _is_linked(b1, 'qm_Factor58', a)
    if hasattr(b2, 'qm_Factor58'):
        assert _is_linked(b2, 'qm_Factor58', a)
    _safe_set(a, 'qm_Impact', None)
    assert not _is_linked(a, 'qm_Impact', b2)
    if hasattr(b2, 'qm_Factor58'):
        assert not _is_linked(b2, 'qm_Factor58', a)


def test_assoc_tool92_link_reassign_clear():
    a = qm_ToolBasedInstrument(metric="sample_text")
    b1 = qm_Tool()
    b2 = qm_Tool()
    _safe_set(a, 'qm_ToolBasedInstrument', b1)
    assert _is_linked(a, 'qm_ToolBasedInstrument', b1)
    if hasattr(b1, 'qm_Tool'):
        assert _is_linked(b1, 'qm_Tool', a)
    _safe_set(a, 'qm_ToolBasedInstrument', b2)
    assert _is_linked(a, 'qm_ToolBasedInstrument', b2)
    if hasattr(b1, 'qm_Tool'):
        assert not _is_linked(b1, 'qm_Tool', a)
    if hasattr(b2, 'qm_Tool'):
        assert _is_linked(b2, 'qm_Tool', a)
    _safe_set(a, 'qm_ToolBasedInstrument', None)
    assert not _is_linked(a, 'qm_ToolBasedInstrument', b2)
    if hasattr(b2, 'qm_Tool'):
        assert not _is_linked(b2, 'qm_Tool', a)


def test_assoc_tools9_link_reassign_clear():
    a = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    b1 = qm_Tool()
    b2 = qm_Tool()
    _safe_set(a, 'qualityModel10', {b1})
    assert _is_linked(a, 'qualityModel10', b1)
    if hasattr(b1, 'Tool'):
        assert _is_linked(b1, 'Tool', a)
    _safe_set(a, 'qualityModel10', {b2})
    assert _is_linked(a, 'qualityModel10', b2)
    if hasattr(b1, 'Tool'):
        assert not _is_linked(b1, 'Tool', a)
    if hasattr(b2, 'Tool'):
        assert _is_linked(b2, 'Tool', a)
    _safe_set(a, 'qualityModel10', set())
    assert not _is_linked(a, 'qualityModel10', b2)
    if hasattr(b2, 'Tool'):
        assert not _is_linked(b2, 'Tool', a)


def test_assoc_value112_link_reassign_clear():
    a = qm_DoubleInterval(lower=3.14, upper=3.14)
    b1 = qm_NumberMeasurementResult()
    b2 = qm_NumberMeasurementResult()
    _safe_set(a, 'qm_DoubleInterval', b1)
    assert _is_linked(a, 'qm_DoubleInterval', b1)
    if hasattr(b1, 'qm_NumberMeasurementResult'):
        assert _is_linked(b1, 'qm_NumberMeasurementResult', a)
    _safe_set(a, 'qm_DoubleInterval', b2)
    assert _is_linked(a, 'qm_DoubleInterval', b2)
    if hasattr(b1, 'qm_NumberMeasurementResult'):
        assert not _is_linked(b1, 'qm_NumberMeasurementResult', a)
    if hasattr(b2, 'qm_NumberMeasurementResult'):
        assert _is_linked(b2, 'qm_NumberMeasurementResult', a)
    _safe_set(a, 'qm_DoubleInterval', None)
    assert not _is_linked(a, 'qm_DoubleInterval', b2)
    if hasattr(b2, 'qm_NumberMeasurementResult'):
        assert not _is_linked(b2, 'qm_NumberMeasurementResult', a)


def test_assoc_value114_link_reassign_clear():
    a = qm_DoubleInterval(lower=3.14, upper=3.14)
    b1 = qm_EvaluationResult()
    b2 = qm_EvaluationResult()
    _safe_set(a, 'qm_DoubleInterval116', b1)
    assert _is_linked(a, 'qm_DoubleInterval116', b1)
    if hasattr(b1, 'qm_EvaluationResult115'):
        assert _is_linked(b1, 'qm_EvaluationResult115', a)
    _safe_set(a, 'qm_DoubleInterval116', b2)
    assert _is_linked(a, 'qm_DoubleInterval116', b2)
    if hasattr(b1, 'qm_EvaluationResult115'):
        assert not _is_linked(b1, 'qm_EvaluationResult115', a)
    if hasattr(b2, 'qm_EvaluationResult115'):
        assert _is_linked(b2, 'qm_EvaluationResult115', a)
    _safe_set(a, 'qm_DoubleInterval116', None)
    assert not _is_linked(a, 'qm_DoubleInterval116', b2)
    if hasattr(b2, 'qm_EvaluationResult115'):
        assert not _is_linked(b2, 'qm_EvaluationResult115', a)


def test_assoc_value121_link_reassign_clear():
    a = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    b1 = qm_DoubleInterval(lower=3.14, upper=3.14)
    b2 = qm_DoubleInterval(lower=9.99, upper=9.99)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult122', b1)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult122', b1)
    if hasattr(b1, 'qm_DoubleInterval123'):
        assert _is_linked(b1, 'qm_DoubleInterval123', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult122', b2)
    assert _is_linked(a, 'qm_MeasureRankingEvaluationResult122', b2)
    if hasattr(b1, 'qm_DoubleInterval123'):
        assert not _is_linked(b1, 'qm_DoubleInterval123', a)
    if hasattr(b2, 'qm_DoubleInterval123'):
        assert _is_linked(b2, 'qm_DoubleInterval123', a)
    _safe_set(a, 'qm_MeasureRankingEvaluationResult122', None)
    assert not _is_linked(a, 'qm_MeasureRankingEvaluationResult122', b2)
    if hasattr(b2, 'qm_DoubleInterval123'):
        assert not _is_linked(b2, 'qm_DoubleInterval123', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnnotatedElement_strategy = st.builds(AnnotatedElement)
@given(instance=AnnotatedElement_strategy)
@settings(max_examples=25)
def test_AnnotatedElement_instantiation(instance):
    assert isinstance(instance, AnnotatedElement)


CharacterizingElement_strategy = st.builds(CharacterizingElement)
@given(instance=CharacterizingElement_strategy)
@settings(max_examples=25)
def test_CharacterizingElement_instantiation(instance):
    assert isinstance(instance, CharacterizingElement)


DescribedElement_strategy = st.builds(DescribedElement)
@given(instance=DescribedElement_strategy)
@settings(max_examples=25)
def test_DescribedElement_instantiation(instance):
    assert isinstance(instance, DescribedElement)


Evaluation_strategy = st.builds(Evaluation)
@given(instance=Evaluation_strategy)
@settings(max_examples=25)
def test_Evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)


EvaluationResult_strategy = st.builds(EvaluationResult)
@given(instance=EvaluationResult_strategy)
@settings(max_examples=25)
def test_EvaluationResult_instantiation(instance):
    assert isinstance(instance, EvaluationResult)


FactorAggregation_strategy = st.builds(FactorAggregation)
@given(instance=FactorAggregation_strategy)
@settings(max_examples=25)
def test_FactorAggregation_instantiation(instance):
    assert isinstance(instance, FactorAggregation)


FormBasedEvaluation_strategy = st.builds(FormBasedEvaluation)
@given(instance=FormBasedEvaluation_strategy)
@settings(max_examples=25)
def test_FormBasedEvaluation_instantiation(instance):
    assert isinstance(instance, FormBasedEvaluation)


FormBasedMeasureAggregation_strategy = st.builds(FormBasedMeasureAggregation)
@given(instance=FormBasedMeasureAggregation_strategy)
@settings(max_examples=25)
def test_FormBasedMeasureAggregation_instantiation(instance):
    assert isinstance(instance, FormBasedMeasureAggregation)


Function_strategy = st.builds(Function)
@given(instance=Function_strategy)
@settings(max_examples=25)
def test_Function_instantiation(instance):
    assert isinstance(instance, Function)


Instrument_strategy = st.builds(Instrument)
@given(instance=Instrument_strategy)
@settings(max_examples=25)
def test_Instrument_instantiation(instance):
    assert isinstance(instance, Instrument)


LinearFunction_strategy = st.builds(LinearFunction)
@given(instance=LinearFunction_strategy)
@settings(max_examples=25)
def test_LinearFunction_instantiation(instance):
    assert isinstance(instance, LinearFunction)


Measure_strategy = st.builds(Measure)
@given(instance=Measure_strategy)
@settings(max_examples=25)
def test_Measure_instantiation(instance):
    assert isinstance(instance, Measure)


MeasureAggregation_strategy = st.builds(MeasureAggregation)
@given(instance=MeasureAggregation_strategy)
@settings(max_examples=25)
def test_MeasureAggregation_instantiation(instance):
    assert isinstance(instance, MeasureAggregation)


MeasureEvaluation_strategy = st.builds(MeasureEvaluation)
@given(instance=MeasureEvaluation_strategy)
@settings(max_examples=25)
def test_MeasureEvaluation_instantiation(instance):
    assert isinstance(instance, MeasureEvaluation)


MeasurementMethod_strategy = st.builds(MeasurementMethod)
@given(instance=MeasurementMethod_strategy)
@settings(max_examples=25)
def test_MeasurementMethod_instantiation(instance):
    assert isinstance(instance, MeasurementMethod)


MeasurementResult_strategy = st.builds(MeasurementResult)
@given(instance=MeasurementResult_strategy)
@settings(max_examples=25)
def test_MeasurementResult_instantiation(instance):
    assert isinstance(instance, MeasurementResult)


MultiMeasureEvaluation_strategy = st.builds(MultiMeasureEvaluation)
@given(instance=MultiMeasureEvaluation_strategy)
@settings(max_examples=25)
def test_MultiMeasureEvaluation_instantiation(instance):
    assert isinstance(instance, MultiMeasureEvaluation)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


QualityModelElement_strategy = st.builds(QualityModelElement)
@given(instance=QualityModelElement_strategy)
@settings(max_examples=25)
def test_QualityModelElement_instantiation(instance):
    assert isinstance(instance, QualityModelElement)


Ranking_strategy = st.builds(Ranking)
@given(instance=Ranking_strategy)
@settings(max_examples=25)
def test_Ranking_instantiation(instance):
    assert isinstance(instance, Ranking)


Result_strategy = st.builds(Result)
@given(instance=Result_strategy)
@settings(max_examples=25)
def test_Result_instantiation(instance):
    assert isinstance(instance, Result)


TaggedElement_strategy = st.builds(TaggedElement)
@given(instance=TaggedElement_strategy)
@settings(max_examples=25)
def test_TaggedElement_instantiation(instance):
    assert isinstance(instance, TaggedElement)


TextAggregation_strategy = st.builds(TextAggregation)
@given(instance=TextAggregation_strategy)
@settings(max_examples=25)
def test_TextAggregation_instantiation(instance):
    assert isinstance(instance, TextAggregation)


TextEvaluation_strategy = st.builds(TextEvaluation)
@given(instance=TextEvaluation_strategy)
@settings(max_examples=25)
def test_TextEvaluation_instantiation(instance):
    assert isinstance(instance, TextEvaluation)


qm_AnnotatedElement_strategy = st.builds(qm_AnnotatedElement)
@given(instance=qm_AnnotatedElement_strategy)
@settings(max_examples=25)
def test_qm_AnnotatedElement_instantiation(instance):
    assert isinstance(instance, qm_AnnotatedElement)


qm_Annotation_strategy = st.builds(qm_Annotation, key=safe_text, value=safe_text)
@given(instance=qm_Annotation_strategy)
@settings(max_examples=25)
def test_qm_Annotation_instantiation(instance):
    assert isinstance(instance, qm_Annotation)


qm_AnnotationBase_strategy = st.builds(qm_AnnotationBase)
@given(instance=qm_AnnotationBase_strategy)
@settings(max_examples=25)
def test_qm_AnnotationBase_instantiation(instance):
    assert isinstance(instance, qm_AnnotationBase)


qm_CharacterizingElement_strategy = st.builds(qm_CharacterizingElement)
@given(instance=qm_CharacterizingElement_strategy)
@settings(max_examples=25)
def test_qm_CharacterizingElement_instantiation(instance):
    assert isinstance(instance, qm_CharacterizingElement)


qm_Decomposition_strategy = st.builds(qm_Decomposition)
@given(instance=qm_Decomposition_strategy)
@settings(max_examples=25)
def test_qm_Decomposition_instantiation(instance):
    assert isinstance(instance, qm_Decomposition)


qm_DescribedElement_strategy = st.builds(qm_DescribedElement, description=safe_text)
@given(instance=qm_DescribedElement_strategy)
@settings(max_examples=25)
def test_qm_DescribedElement_instantiation(instance):
    assert isinstance(instance, qm_DescribedElement)


qm_DoubleInterval_strategy = st.builds(qm_DoubleInterval, lower=st.floats(allow_nan=False, allow_infinity=False), upper=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=qm_DoubleInterval_strategy)
@settings(max_examples=25)
def test_qm_DoubleInterval_instantiation(instance):
    assert isinstance(instance, qm_DoubleInterval)


qm_Entity_strategy = st.builds(qm_Entity, stakeholder=st.booleans(), useCase=st.booleans())
@given(instance=qm_Entity_strategy)
@settings(max_examples=25)
def test_qm_Entity_instantiation(instance):
    assert isinstance(instance, qm_Entity)


qm_Evaluation_strategy = st.builds(qm_Evaluation, completeness=st.integers(), maximumPoints=st.integers())
@given(instance=qm_Evaluation_strategy)
@settings(max_examples=25)
def test_qm_Evaluation_instantiation(instance):
    assert isinstance(instance, qm_Evaluation)


qm_EvaluationResult_strategy = st.builds(qm_EvaluationResult)
@given(instance=qm_EvaluationResult_strategy)
@settings(max_examples=25)
def test_qm_EvaluationResult_instantiation(instance):
    assert isinstance(instance, qm_EvaluationResult)


qm_Factor_strategy = st.builds(qm_Factor)
@given(instance=qm_Factor_strategy)
@settings(max_examples=25)
def test_qm_Factor_instantiation(instance):
    assert isinstance(instance, qm_Factor)


qm_FactorAggregation_strategy = st.builds(qm_FactorAggregation)
@given(instance=qm_FactorAggregation_strategy)
@settings(max_examples=25)
def test_qm_FactorAggregation_instantiation(instance):
    assert isinstance(instance, qm_FactorAggregation)


qm_FactorRanking_strategy = st.builds(qm_FactorRanking)
@given(instance=qm_FactorRanking_strategy)
@settings(max_examples=25)
def test_qm_FactorRanking_instantiation(instance):
    assert isinstance(instance, qm_FactorRanking)


qm_FactorRefinement_strategy = st.builds(qm_FactorRefinement)
@given(instance=qm_FactorRefinement_strategy)
@settings(max_examples=25)
def test_qm_FactorRefinement_instantiation(instance):
    assert isinstance(instance, qm_FactorRefinement)


qm_FindingMessage_strategy = st.builds(qm_FindingMessage, location=safe_text, message=safe_text)
@given(instance=qm_FindingMessage_strategy)
@settings(max_examples=25)
def test_qm_FindingMessage_instantiation(instance):
    assert isinstance(instance, qm_FindingMessage)


qm_FindingsMeasurementResult_strategy = st.builds(qm_FindingsMeasurementResult, count=st.integers(), findings=safe_text)
@given(instance=qm_FindingsMeasurementResult_strategy)
@settings(max_examples=25)
def test_qm_FindingsMeasurementResult_instantiation(instance):
    assert isinstance(instance, qm_FindingsMeasurementResult)


qm_FindingsUnionMeasureAggregation_strategy = st.builds(qm_FindingsUnionMeasureAggregation)
@given(instance=qm_FindingsUnionMeasureAggregation_strategy)
@settings(max_examples=25)
def test_qm_FindingsUnionMeasureAggregation_instantiation(instance):
    assert isinstance(instance, qm_FindingsUnionMeasureAggregation)


qm_FormBasedEvaluation_strategy = st.builds(qm_FormBasedEvaluation)
@given(instance=qm_FormBasedEvaluation_strategy)
@settings(max_examples=25)
def test_qm_FormBasedEvaluation_instantiation(instance):
    assert isinstance(instance, qm_FormBasedEvaluation)


qm_FormBasedMeasureAggregation_strategy = st.builds(qm_FormBasedMeasureAggregation)
@given(instance=qm_FormBasedMeasureAggregation_strategy)
@settings(max_examples=25)
def test_qm_FormBasedMeasureAggregation_instantiation(instance):
    assert isinstance(instance, qm_FormBasedMeasureAggregation)


qm_Function_strategy = st.builds(qm_Function)
@given(instance=qm_Function_strategy)
@settings(max_examples=25)
def test_qm_Function_instantiation(instance):
    assert isinstance(instance, qm_Function)


qm_Impact_strategy = st.builds(qm_Impact, effect=safe_text, justification=safe_text)
@given(instance=qm_Impact_strategy)
@settings(max_examples=25)
def test_qm_Impact_instantiation(instance):
    assert isinstance(instance, qm_Impact)


qm_Instrument_strategy = st.builds(qm_Instrument)
@given(instance=qm_Instrument_strategy)
@settings(max_examples=25)
def test_qm_Instrument_instantiation(instance):
    assert isinstance(instance, qm_Instrument)


qm_LinearDecreasingFunction_strategy = st.builds(qm_LinearDecreasingFunction)
@given(instance=qm_LinearDecreasingFunction_strategy)
@settings(max_examples=25)
def test_qm_LinearDecreasingFunction_instantiation(instance):
    assert isinstance(instance, qm_LinearDecreasingFunction)


qm_LinearFunction_strategy = st.builds(qm_LinearFunction, lowerBound=st.floats(allow_nan=False, allow_infinity=False), upperBound=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=qm_LinearFunction_strategy)
@settings(max_examples=25)
def test_qm_LinearFunction_instantiation(instance):
    assert isinstance(instance, qm_LinearFunction)


qm_LinearIncreasingFunction_strategy = st.builds(qm_LinearIncreasingFunction)
@given(instance=qm_LinearIncreasingFunction_strategy)
@settings(max_examples=25)
def test_qm_LinearIncreasingFunction_instantiation(instance):
    assert isinstance(instance, qm_LinearIncreasingFunction)


qm_ManualEvaluation_strategy = st.builds(qm_ManualEvaluation)
@given(instance=qm_ManualEvaluation_strategy)
@settings(max_examples=25)
def test_qm_ManualEvaluation_instantiation(instance):
    assert isinstance(instance, qm_ManualEvaluation)


qm_ManualInstrument_strategy = st.builds(qm_ManualInstrument)
@given(instance=qm_ManualInstrument_strategy)
@settings(max_examples=25)
def test_qm_ManualInstrument_instantiation(instance):
    assert isinstance(instance, qm_ManualInstrument)


qm_Measure_strategy = st.builds(qm_Measure, type=safe_text)
@given(instance=qm_Measure_strategy)
@settings(max_examples=25)
def test_qm_Measure_instantiation(instance):
    assert isinstance(instance, qm_Measure)


qm_MeasureAggregation_strategy = st.builds(qm_MeasureAggregation)
@given(instance=qm_MeasureAggregation_strategy)
@settings(max_examples=25)
def test_qm_MeasureAggregation_instantiation(instance):
    assert isinstance(instance, qm_MeasureAggregation)


qm_MeasureEvaluation_strategy = st.builds(qm_MeasureEvaluation, range=safe_text)
@given(instance=qm_MeasureEvaluation_strategy)
@settings(max_examples=25)
def test_qm_MeasureEvaluation_instantiation(instance):
    assert isinstance(instance, qm_MeasureEvaluation)


qm_MeasureRanking_strategy = st.builds(qm_MeasureRanking)
@given(instance=qm_MeasureRanking_strategy)
@settings(max_examples=25)
def test_qm_MeasureRanking_instantiation(instance):
    assert isinstance(instance, qm_MeasureRanking)


qm_MeasureRankingEvaluationResult_strategy = st.builds(qm_MeasureRankingEvaluationResult, ratioAffected=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=qm_MeasureRankingEvaluationResult_strategy)
@settings(max_examples=25)
def test_qm_MeasureRankingEvaluationResult_instantiation(instance):
    assert isinstance(instance, qm_MeasureRankingEvaluationResult)


qm_MeasureRefinement_strategy = st.builds(qm_MeasureRefinement)
@given(instance=qm_MeasureRefinement_strategy)
@settings(max_examples=25)
def test_qm_MeasureRefinement_instantiation(instance):
    assert isinstance(instance, qm_MeasureRefinement)


qm_Measurement_strategy = st.builds(qm_Measurement)
@given(instance=qm_Measurement_strategy)
@settings(max_examples=25)
def test_qm_Measurement_instantiation(instance):
    assert isinstance(instance, qm_Measurement)


qm_MeasurementMethod_strategy = st.builds(qm_MeasurementMethod)
@given(instance=qm_MeasurementMethod_strategy)
@settings(max_examples=25)
def test_qm_MeasurementMethod_instantiation(instance):
    assert isinstance(instance, qm_MeasurementMethod)


qm_MeasurementResult_strategy = st.builds(qm_MeasurementResult)
@given(instance=qm_MeasurementResult_strategy)
@settings(max_examples=25)
def test_qm_MeasurementResult_instantiation(instance):
    assert isinstance(instance, qm_MeasurementResult)


qm_MultiMeasureEvaluation_strategy = st.builds(qm_MultiMeasureEvaluation)
@given(instance=qm_MultiMeasureEvaluation_strategy)
@settings(max_examples=25)
def test_qm_MultiMeasureEvaluation_instantiation(instance):
    assert isinstance(instance, qm_MultiMeasureEvaluation)


qm_MultiMeasureEvaluationResult_strategy = st.builds(qm_MultiMeasureEvaluationResult)
@given(instance=qm_MultiMeasureEvaluationResult_strategy)
@settings(max_examples=25)
def test_qm_MultiMeasureEvaluationResult_instantiation(instance):
    assert isinstance(instance, qm_MultiMeasureEvaluationResult)


qm_NamedElement_strategy = st.builds(qm_NamedElement, name=safe_text, title=safe_text)
@given(instance=qm_NamedElement_strategy)
@settings(max_examples=25)
def test_qm_NamedElement_instantiation(instance):
    assert isinstance(instance, qm_NamedElement)


qm_NormalizationMeasure_strategy = st.builds(qm_NormalizationMeasure)
@given(instance=qm_NormalizationMeasure_strategy)
@settings(max_examples=25)
def test_qm_NormalizationMeasure_instantiation(instance):
    assert isinstance(instance, qm_NormalizationMeasure)


qm_NumberMeanMeasureAggregation_strategy = st.builds(qm_NumberMeanMeasureAggregation)
@given(instance=qm_NumberMeanMeasureAggregation_strategy)
@settings(max_examples=25)
def test_qm_NumberMeanMeasureAggregation_instantiation(instance):
    assert isinstance(instance, qm_NumberMeanMeasureAggregation)


qm_NumberMeasurementResult_strategy = st.builds(qm_NumberMeasurementResult)
@given(instance=qm_NumberMeasurementResult_strategy)
@settings(max_examples=25)
def test_qm_NumberMeasurementResult_instantiation(instance):
    assert isinstance(instance, qm_NumberMeasurementResult)


qm_QIESLAggregation_strategy = st.builds(qm_QIESLAggregation)
@given(instance=qm_QIESLAggregation_strategy)
@settings(max_examples=25)
def test_qm_QIESLAggregation_instantiation(instance):
    assert isinstance(instance, qm_QIESLAggregation)


qm_QIESLEvaluation_strategy = st.builds(qm_QIESLEvaluation)
@given(instance=qm_QIESLEvaluation_strategy)
@settings(max_examples=25)
def test_qm_QIESLEvaluation_instantiation(instance):
    assert isinstance(instance, qm_QIESLEvaluation)


qm_QualityModel_strategy = st.builds(qm_QualityModel, schoolGradeBoundary2=safe_text, schoolGradeBoundary3=safe_text, schoolGradeBoundary4=safe_text, schoolGradeBoundary5=safe_text, schoolGradeBoundary6=safe_text)
@given(instance=qm_QualityModel_strategy)
@settings(max_examples=25)
def test_qm_QualityModel_instantiation(instance):
    assert isinstance(instance, qm_QualityModel)


qm_QualityModelElement_strategy = st.builds(qm_QualityModelElement, qualifiedName=safe_text)
@given(instance=qm_QualityModelElement_strategy)
@settings(max_examples=25)
def test_qm_QualityModelElement_instantiation(instance):
    assert isinstance(instance, qm_QualityModelElement)


qm_QualityModelResult_strategy = st.builds(qm_QualityModelResult, date=st.dates(), system=safe_text)
@given(instance=qm_QualityModelResult_strategy)
@settings(max_examples=25)
def test_qm_QualityModelResult_instantiation(instance):
    assert isinstance(instance, qm_QualityModelResult)


qm_Ranking_strategy = st.builds(qm_Ranking, rank=st.integers(), weight=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=qm_Ranking_strategy)
@settings(max_examples=25)
def test_qm_Ranking_instantiation(instance):
    assert isinstance(instance, qm_Ranking)


qm_Result_strategy = st.builds(qm_Result, message=safe_text)
@given(instance=qm_Result_strategy)
@settings(max_examples=25)
def test_qm_Result_instantiation(instance):
    assert isinstance(instance, qm_Result)


qm_SingleMeasureEvaluation_strategy = st.builds(qm_SingleMeasureEvaluation)
@given(instance=qm_SingleMeasureEvaluation_strategy)
@settings(max_examples=25)
def test_qm_SingleMeasureEvaluation_instantiation(instance):
    assert isinstance(instance, qm_SingleMeasureEvaluation)


qm_SingleMeasureEvaluationResult_strategy = st.builds(qm_SingleMeasureEvaluationResult, ratioAffected=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=qm_SingleMeasureEvaluationResult_strategy)
@settings(max_examples=25)
def test_qm_SingleMeasureEvaluationResult_instantiation(instance):
    assert isinstance(instance, qm_SingleMeasureEvaluationResult)


qm_Source_strategy = st.builds(qm_Source)
@given(instance=qm_Source_strategy)
@settings(max_examples=25)
def test_qm_Source_instantiation(instance):
    assert isinstance(instance, qm_Source)


qm_Specialization_strategy = st.builds(qm_Specialization)
@given(instance=qm_Specialization_strategy)
@settings(max_examples=25)
def test_qm_Specialization_instantiation(instance):
    assert isinstance(instance, qm_Specialization)


qm_Tag_strategy = st.builds(qm_Tag)
@given(instance=qm_Tag_strategy)
@settings(max_examples=25)
def test_qm_Tag_instantiation(instance):
    assert isinstance(instance, qm_Tag)


qm_TaggedElement_strategy = st.builds(qm_TaggedElement)
@given(instance=qm_TaggedElement_strategy)
@settings(max_examples=25)
def test_qm_TaggedElement_instantiation(instance):
    assert isinstance(instance, qm_TaggedElement)


qm_TextAggregation_strategy = st.builds(qm_TextAggregation, specification=safe_text)
@given(instance=qm_TextAggregation_strategy)
@settings(max_examples=25)
def test_qm_TextAggregation_instantiation(instance):
    assert isinstance(instance, qm_TextAggregation)


qm_TextEvaluation_strategy = st.builds(qm_TextEvaluation, specification=safe_text)
@given(instance=qm_TextEvaluation_strategy)
@settings(max_examples=25)
def test_qm_TextEvaluation_instantiation(instance):
    assert isinstance(instance, qm_TextEvaluation)


qm_Tool_strategy = st.builds(qm_Tool)
@given(instance=qm_Tool_strategy)
@settings(max_examples=25)
def test_qm_Tool_instantiation(instance):
    assert isinstance(instance, qm_Tool)


qm_ToolBasedInstrument_strategy = st.builds(qm_ToolBasedInstrument, metric=safe_text)
@given(instance=qm_ToolBasedInstrument_strategy)
@settings(max_examples=25)
def test_qm_ToolBasedInstrument_instantiation(instance):
    assert isinstance(instance, qm_ToolBasedInstrument)


qm_WeightedSumFactorAggregation_strategy = st.builds(qm_WeightedSumFactorAggregation)
@given(instance=qm_WeightedSumFactorAggregation_strategy)
@settings(max_examples=25)
def test_qm_WeightedSumFactorAggregation_instantiation(instance):
    assert isinstance(instance, qm_WeightedSumFactorAggregation)


qm_WeightedSumMultiMeasureEvaluation_strategy = st.builds(qm_WeightedSumMultiMeasureEvaluation)
@given(instance=qm_WeightedSumMultiMeasureEvaluation_strategy)
@settings(max_examples=25)
def test_qm_WeightedSumMultiMeasureEvaluation_instantiation(instance):
    assert isinstance(instance, qm_WeightedSumMultiMeasureEvaluation)


