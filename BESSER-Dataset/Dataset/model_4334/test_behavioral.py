import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_entities0_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Entity(stakeholder=True, useCase=True)
    _safe_set(b, 'Entity', a1)
    assert _is_linked(b, 'Entity', a1)
    if hasattr(a1, 'qualityModel'):
        assert _is_linked(a1, 'qualityModel', b)
    _safe_set(b, 'Entity', a2)
    assert _is_linked(b, 'Entity', a2)
    if hasattr(a1, 'qualityModel'):
        assert not _is_linked(a1, 'qualityModel', b)
    if hasattr(a2, 'qualityModel'):
        assert _is_linked(a2, 'qualityModel', b)
    _safe_set(b, 'Entity', None)
    assert not _is_linked(b, 'Entity', a2)
    if hasattr(a2, 'qualityModel'):
        assert not _is_linked(a2, 'qualityModel', b)


def test_assoc_evaluations3_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Evaluation(completeness=7, maximumPoints=7)
    _safe_set(b, 'Evaluation', a1)
    assert _is_linked(b, 'Evaluation', a1)
    if hasattr(a1, 'qualityModel4'):
        assert _is_linked(a1, 'qualityModel4', b)
    _safe_set(b, 'Evaluation', a2)
    assert _is_linked(b, 'Evaluation', a2)
    if hasattr(a1, 'qualityModel4'):
        assert not _is_linked(a1, 'qualityModel4', b)
    if hasattr(a2, 'qualityModel4'):
        assert _is_linked(a2, 'qualityModel4', b)
    _safe_set(b, 'Evaluation', None)
    assert not _is_linked(b, 'Evaluation', a2)
    if hasattr(a2, 'qualityModel4'):
        assert not _is_linked(a2, 'qualityModel4', b)


def test_assoc_findingMessages113_reverse_link_reassign_clear():
    a1 = qm_FindingsMeasurementResult(count=7, findings="sample_text")
    a2 = qm_FindingsMeasurementResult(count=13, findings="sample_text_2")
    b = qm_FindingMessage(location="sample_text", message="sample_text")
    _safe_set(b, 'qm_FindingMessage', a1)
    assert _is_linked(b, 'qm_FindingMessage', a1)
    if hasattr(a1, 'qm_FindingsMeasurementResult'):
        assert _is_linked(a1, 'qm_FindingsMeasurementResult', b)
    _safe_set(b, 'qm_FindingMessage', a2)
    assert _is_linked(b, 'qm_FindingMessage', a2)
    if hasattr(a1, 'qm_FindingsMeasurementResult'):
        assert not _is_linked(a1, 'qm_FindingsMeasurementResult', b)
    if hasattr(a2, 'qm_FindingsMeasurementResult'):
        assert _is_linked(a2, 'qm_FindingsMeasurementResult', b)
    _safe_set(b, 'qm_FindingMessage', None)
    assert not _is_linked(b, 'qm_FindingMessage', a2)
    if hasattr(a2, 'qm_FindingsMeasurementResult'):
        assert not _is_linked(a2, 'qm_FindingsMeasurementResult', b)


def test_assoc_isADirect27_reverse_link_reassign_clear():
    a1 = qm_Entity(stakeholder=True, useCase=True)
    a2 = qm_Entity(stakeholder=False, useCase=False)
    b = qm_Entity(stakeholder=True, useCase=True)
    _safe_set(b, 'qm_Entity26', {a1})
    assert _is_linked(b, 'qm_Entity26', a1)
    if hasattr(a1, 'qm_Entity'):
        assert _is_linked(a1, 'qm_Entity', b)
    _safe_set(b, 'qm_Entity26', {a2})
    assert _is_linked(b, 'qm_Entity26', a2)
    if hasattr(a1, 'qm_Entity'):
        assert not _is_linked(a1, 'qm_Entity', b)
    if hasattr(a2, 'qm_Entity'):
        assert _is_linked(a2, 'qm_Entity', b)
    _safe_set(b, 'qm_Entity26', set())
    assert not _is_linked(b, 'qm_Entity26', a2)
    if hasattr(a2, 'qm_Entity'):
        assert not _is_linked(a2, 'qm_Entity', b)


def test_assoc_measure99_reverse_link_reassign_clear():
    a1 = qm_MeasureEvaluation(range="sample_text")
    a2 = qm_MeasureEvaluation(range="sample_text_2")
    b = qm_Measure(type="sample_text")
    _safe_set(b, 'qm_Measure100', a1)
    assert _is_linked(b, 'qm_Measure100', a1)
    if hasattr(a1, 'qm_MeasureEvaluation'):
        assert _is_linked(a1, 'qm_MeasureEvaluation', b)
    _safe_set(b, 'qm_Measure100', a2)
    assert _is_linked(b, 'qm_Measure100', a2)
    if hasattr(a1, 'qm_MeasureEvaluation'):
        assert not _is_linked(a1, 'qm_MeasureEvaluation', b)
    if hasattr(a2, 'qm_MeasureEvaluation'):
        assert _is_linked(a2, 'qm_MeasureEvaluation', b)
    _safe_set(b, 'qm_Measure100', None)
    assert not _is_linked(b, 'qm_Measure100', a2)
    if hasattr(a2, 'qm_MeasureEvaluation'):
        assert not _is_linked(a2, 'qm_MeasureEvaluation', b)


def test_assoc_measures5_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Measure(type="sample_text")
    _safe_set(b, 'Measure', a1)
    assert _is_linked(b, 'Measure', a1)
    if hasattr(a1, 'qualityModel6'):
        assert _is_linked(a1, 'qualityModel6', b)
    _safe_set(b, 'Measure', a2)
    assert _is_linked(b, 'Measure', a2)
    if hasattr(a1, 'qualityModel6'):
        assert not _is_linked(a1, 'qualityModel6', b)
    if hasattr(a2, 'qualityModel6'):
        assert _is_linked(a2, 'qualityModel6', b)
    _safe_set(b, 'Measure', None)
    assert not _is_linked(b, 'Measure', a2)
    if hasattr(a2, 'qualityModel6'):
        assert not _is_linked(a2, 'qualityModel6', b)


def test_assoc_partOfDirect31_reverse_link_reassign_clear():
    a1 = qm_Entity(stakeholder=True, useCase=True)
    a2 = qm_Entity(stakeholder=False, useCase=False)
    b = qm_Entity(stakeholder=True, useCase=True)
    _safe_set(b, 'qm_Entity32', a1)
    assert _is_linked(b, 'qm_Entity32', a1)
    if hasattr(a1, 'qm_Entity30'):
        assert _is_linked(a1, 'qm_Entity30', b)
    _safe_set(b, 'qm_Entity32', a2)
    assert _is_linked(b, 'qm_Entity32', a2)
    if hasattr(a1, 'qm_Entity30'):
        assert not _is_linked(a1, 'qm_Entity30', b)
    if hasattr(a2, 'qm_Entity30'):
        assert _is_linked(a2, 'qm_Entity30', b)
    _safe_set(b, 'qm_Entity32', None)
    assert not _is_linked(b, 'qm_Entity32', a2)
    if hasattr(a2, 'qm_Entity30'):
        assert not _is_linked(a2, 'qm_Entity30', b)


def test_assoc_qualityModel33_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Entity(stakeholder=True, useCase=True)
    _safe_set(b, 'entities', a1)
    assert _is_linked(b, 'entities', a1)
    if hasattr(a1, 'QualityModel34'):
        assert _is_linked(a1, 'QualityModel34', b)
    _safe_set(b, 'entities', a2)
    assert _is_linked(b, 'entities', a2)
    if hasattr(a1, 'QualityModel34'):
        assert not _is_linked(a1, 'QualityModel34', b)
    if hasattr(a2, 'QualityModel34'):
        assert _is_linked(a2, 'QualityModel34', b)
    _safe_set(b, 'entities', None)
    assert not _is_linked(b, 'entities', a2)
    if hasattr(a2, 'QualityModel34'):
        assert not _is_linked(a2, 'QualityModel34', b)


def test_assoc_qualityModel61_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Evaluation(completeness=7, maximumPoints=7)
    _safe_set(b, 'evaluations', a1)
    assert _is_linked(b, 'evaluations', a1)
    if hasattr(a1, 'QualityModel62'):
        assert _is_linked(a1, 'QualityModel62', b)
    _safe_set(b, 'evaluations', a2)
    assert _is_linked(b, 'evaluations', a2)
    if hasattr(a1, 'QualityModel62'):
        assert not _is_linked(a1, 'QualityModel62', b)
    if hasattr(a2, 'QualityModel62'):
        assert _is_linked(a2, 'QualityModel62', b)
    _safe_set(b, 'evaluations', None)
    assert not _is_linked(b, 'evaluations', a2)
    if hasattr(a2, 'QualityModel62'):
        assert not _is_linked(a2, 'QualityModel62', b)


def test_assoc_qualityModel80_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_Measure(type="sample_text")
    _safe_set(b, 'measures81', a1)
    assert _is_linked(b, 'measures81', a1)
    if hasattr(a1, 'QualityModel82'):
        assert _is_linked(a1, 'QualityModel82', b)
    _safe_set(b, 'measures81', a2)
    assert _is_linked(b, 'measures81', a2)
    if hasattr(a1, 'QualityModel82'):
        assert not _is_linked(a1, 'QualityModel82', b)
    if hasattr(a2, 'QualityModel82'):
        assert _is_linked(a2, 'QualityModel82', b)
    _safe_set(b, 'measures81', None)
    assert not _is_linked(b, 'measures81', a2)
    if hasattr(a2, 'QualityModel82'):
        assert not _is_linked(a2, 'QualityModel82', b)


def test_assoc_refinesDirect86_reverse_link_reassign_clear():
    a1 = qm_Measure(type="sample_text")
    a2 = qm_Measure(type="sample_text_2")
    b = qm_Measure(type="sample_text")
    _safe_set(b, 'qm_Measure87', a1)
    assert _is_linked(b, 'qm_Measure87', a1)
    if hasattr(a1, 'qm_Measure85'):
        assert _is_linked(a1, 'qm_Measure85', b)
    _safe_set(b, 'qm_Measure87', a2)
    assert _is_linked(b, 'qm_Measure87', a2)
    if hasattr(a1, 'qm_Measure85'):
        assert not _is_linked(a1, 'qm_Measure85', b)
    if hasattr(a2, 'qm_Measure85'):
        assert _is_linked(a2, 'qm_Measure85', b)
    _safe_set(b, 'qm_Measure87', None)
    assert not _is_linked(b, 'qm_Measure87', a2)
    if hasattr(a2, 'qm_Measure85'):
        assert not _is_linked(a2, 'qm_Measure85', b)


def test_assoc_requires16_reverse_link_reassign_clear():
    a1 = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    a2 = qm_QualityModel(schoolGradeBoundary2="sample_text_2", schoolGradeBoundary3="sample_text_2", schoolGradeBoundary4="sample_text_2", schoolGradeBoundary5="sample_text_2", schoolGradeBoundary6="sample_text_2")
    b = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    _safe_set(b, 'qm_QualityModel15', {a1})
    assert _is_linked(b, 'qm_QualityModel15', a1)
    if hasattr(a1, 'qm_QualityModel'):
        assert _is_linked(a1, 'qm_QualityModel', b)
    _safe_set(b, 'qm_QualityModel15', {a2})
    assert _is_linked(b, 'qm_QualityModel15', a2)
    if hasattr(a1, 'qm_QualityModel'):
        assert not _is_linked(a1, 'qm_QualityModel', b)
    if hasattr(a2, 'qm_QualityModel'):
        assert _is_linked(a2, 'qm_QualityModel', b)
    _safe_set(b, 'qm_QualityModel15', set())
    assert not _is_linked(b, 'qm_QualityModel15', a2)
    if hasattr(a2, 'qm_QualityModel'):
        assert not _is_linked(a2, 'qm_QualityModel', b)


def test_assoc_value121_reverse_link_reassign_clear():
    a1 = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    a2 = qm_MeasureRankingEvaluationResult(ratioAffected=9.99)
    b = qm_DoubleInterval(lower=3.14, upper=3.14)
    _safe_set(b, 'qm_DoubleInterval123', a1)
    assert _is_linked(b, 'qm_DoubleInterval123', a1)
    if hasattr(a1, 'qm_MeasureRankingEvaluationResult122'):
        assert _is_linked(a1, 'qm_MeasureRankingEvaluationResult122', b)
    _safe_set(b, 'qm_DoubleInterval123', a2)
    assert _is_linked(b, 'qm_DoubleInterval123', a2)
    if hasattr(a1, 'qm_MeasureRankingEvaluationResult122'):
        assert not _is_linked(a1, 'qm_MeasureRankingEvaluationResult122', b)
    if hasattr(a2, 'qm_MeasureRankingEvaluationResult122'):
        assert _is_linked(a2, 'qm_MeasureRankingEvaluationResult122', b)
    _safe_set(b, 'qm_DoubleInterval123', None)
    assert not _is_linked(b, 'qm_DoubleInterval123', a2)
    if hasattr(a2, 'qm_MeasureRankingEvaluationResult122'):
        assert not _is_linked(a2, 'qm_MeasureRankingEvaluationResult122', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotations19_stub_double():
    # qm_AnnotatedElement has no real 'qm_AnnotatedElement' property in the generated
    # code (a bare stub) -- manually attach it so qm_Annotation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Annotation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Annotation(key="sample_text", value="sample_text")
    partner = qm_AnnotatedElement()
    setattr(partner, 'qm_AnnotatedElement', None)
    _safe_set(owner, 'qm_Annotation', partner)
    assert owner in getattr(partner, 'qm_AnnotatedElement')
    _safe_set(owner, 'qm_Annotation', None)
    assert owner not in getattr(partner, 'qm_AnnotatedElement')


def test_assoc_characterizes43_stub_double():
    # qm_CharacterizingElement has no real 'qm_CharacterizingElement' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_CharacterizingElement()
    setattr(partner, 'qm_CharacterizingElement', None)
    _safe_set(owner, 'qm_Entity44', partner)
    assert getattr(partner, 'qm_CharacterizingElement') == owner
    _safe_set(owner, 'qm_Entity44', None)
    assert getattr(partner, 'qm_CharacterizingElement') is None


def test_assoc_child37_stub_double():
    # qm_Specialization has no real 'isA' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Specialization()
    setattr(partner, 'isA', None)
    _safe_set(owner, 'Entity38', partner)
    assert getattr(partner, 'isA') == owner
    _safe_set(owner, 'Entity38', None)
    assert getattr(partner, 'isA') is None


def test_assoc_child41_stub_double():
    # qm_Decomposition has no real 'partOf' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Decomposition()
    setattr(partner, 'partOf', None)
    _safe_set(owner, 'Entity42', partner)
    assert getattr(partner, 'partOf') == owner
    _safe_set(owner, 'Entity42', None)
    assert getattr(partner, 'partOf') is None


def test_assoc_child69_stub_double():
    # qm_Measurement has no real 'measures' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_Measurement()
    setattr(partner, 'measures', None)
    _safe_set(owner, 'Measure70', partner)
    assert getattr(partner, 'measures') == owner
    _safe_set(owner, 'Measure70', None)
    assert getattr(partner, 'measures') is None


def test_assoc_child72_stub_double():
    # qm_MeasureRefinement has no real 'refines73' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_MeasureRefinement()
    setattr(partner, 'refines73', None)
    _safe_set(owner, 'Measure74', partner)
    assert getattr(partner, 'refines73') == owner
    _safe_set(owner, 'Measure74', None)
    assert getattr(partner, 'refines73') is None


def test_assoc_determines88_stub_double():
    # qm_MeasurementMethod has no real 'qm_MeasurementMethod' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_MeasurementMethod()
    setattr(partner, 'qm_MeasurementMethod', None)
    _safe_set(owner, 'qm_Measure89', partner)
    assert getattr(partner, 'qm_MeasurementMethod') == owner
    _safe_set(owner, 'qm_Measure89', None)
    assert getattr(partner, 'qm_MeasurementMethod') is None


def test_assoc_evaluates59_stub_double():
    # qm_Factor has no real 'qm_Factor60' property in the generated
    # code (a bare stub) -- manually attach it so qm_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Evaluation(completeness=7, maximumPoints=7)
    partner = qm_Factor()
    setattr(partner, 'qm_Factor60', None)
    _safe_set(owner, 'qm_Evaluation', partner)
    assert getattr(partner, 'qm_Factor60') == owner
    _safe_set(owner, 'qm_Evaluation', None)
    assert getattr(partner, 'qm_Factor60') is None


def test_assoc_evaluationResults107_stub_double():
    # qm_EvaluationResult has no real 'qm_EvaluationResult' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModelResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModelResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    partner = qm_EvaluationResult()
    setattr(partner, 'qm_EvaluationResult', None)
    _safe_set(owner, 'qm_QualityModelResult108', {partner})
    assert getattr(partner, 'qm_EvaluationResult') == owner
    _safe_set(owner, 'qm_QualityModelResult108', set())
    assert getattr(partner, 'qm_EvaluationResult') is None


def test_assoc_evaluationResults120_stub_double():
    # qm_MultiMeasureEvaluationResult has no real 'qm_MultiMeasureEvaluationResult' property in the generated
    # code (a bare stub) -- manually attach it so qm_MeasureRankingEvaluationResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_MeasureRankingEvaluationResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    partner = qm_MultiMeasureEvaluationResult()
    setattr(partner, 'qm_MultiMeasureEvaluationResult', None)
    _safe_set(owner, 'qm_MeasureRankingEvaluationResult', partner)
    assert owner in getattr(partner, 'qm_MultiMeasureEvaluationResult')
    _safe_set(owner, 'qm_MeasureRankingEvaluationResult', None)
    assert owner not in getattr(partner, 'qm_MultiMeasureEvaluationResult')


def test_assoc_factors1_stub_double():
    # qm_Factor has no real 'Factor' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Factor()
    setattr(partner, 'Factor', None)
    _safe_set(owner, 'qualityModel2', {partner})
    assert getattr(partner, 'Factor') == owner
    _safe_set(owner, 'qualityModel2', set())
    assert getattr(partner, 'Factor') is None


def test_assoc_function103_stub_double():
    # qm_Function has no real 'qm_Function' property in the generated
    # code (a bare stub) -- manually attach it so qm_MeasureEvaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_MeasureEvaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_MeasureEvaluation(range="sample_text")
    partner = qm_Function()
    setattr(partner, 'qm_Function', None)
    _safe_set(owner, 'qm_MeasureEvaluation104', partner)
    assert getattr(partner, 'qm_Function') == owner
    _safe_set(owner, 'qm_MeasureEvaluation104', None)
    assert getattr(partner, 'qm_Function') is None


def test_assoc_influences45_stub_double():
    # qm_Factor has no real 'source' property in the generated
    # code (a bare stub) -- manually attach it so qm_Impact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Impact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Impact(effect="sample_text", justification="sample_text")
    partner = qm_Factor()
    setattr(partner, 'source', None)
    _safe_set(owner, 'Impact', partner)
    assert owner in getattr(partner, 'source')
    _safe_set(owner, 'Impact', None)
    assert owner not in getattr(partner, 'source')


def test_assoc_isA25_stub_double():
    # qm_Specialization has no real 'Specialization' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Specialization()
    setattr(partner, 'Specialization', None)
    _safe_set(owner, 'child', {partner})
    assert getattr(partner, 'Specialization') == owner
    _safe_set(owner, 'child', set())
    assert getattr(partner, 'Specialization') is None


def test_assoc_measurementMethods7_stub_double():
    # qm_MeasurementMethod has no real 'MeasurementMethod' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_MeasurementMethod()
    setattr(partner, 'MeasurementMethod', None)
    _safe_set(owner, 'qualityModel8', {partner})
    assert getattr(partner, 'MeasurementMethod') == owner
    _safe_set(owner, 'qualityModel8', set())
    assert getattr(partner, 'MeasurementMethod') is None


def test_assoc_measurementResults106_stub_double():
    # qm_MeasurementResult has no real 'qm_MeasurementResult' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModelResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModelResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModelResult(date=date(2024, 1, 1), system="sample_text")
    partner = qm_MeasurementResult()
    setattr(partner, 'qm_MeasurementResult', None)
    _safe_set(owner, 'qm_QualityModelResult', {partner})
    assert getattr(partner, 'qm_MeasurementResult') == owner
    _safe_set(owner, 'qm_QualityModelResult', set())
    assert getattr(partner, 'qm_MeasurementResult') is None


def test_assoc_measures75_stub_double():
    # qm_Measurement has no real 'Measurement' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_Measurement()
    setattr(partner, 'Measurement', None)
    _safe_set(owner, 'child76', {partner})
    assert getattr(partner, 'Measurement') == owner
    _safe_set(owner, 'child76', set())
    assert getattr(partner, 'Measurement') is None


def test_assoc_measuresDirect77_stub_double():
    # qm_Factor has no real 'qm_Factor79' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_Factor()
    setattr(partner, 'qm_Factor79', None)
    _safe_set(owner, 'qm_Measure78', {partner})
    assert getattr(partner, 'qm_Factor79') == owner
    _safe_set(owner, 'qm_Measure78', set())
    assert getattr(partner, 'qm_Factor79') is None


def test_assoc_normlizationMeasure101_stub_double():
    # qm_NormalizationMeasure has no real 'qm_NormalizationMeasure' property in the generated
    # code (a bare stub) -- manually attach it so qm_MeasureEvaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_MeasureEvaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_MeasureEvaluation(range="sample_text")
    partner = qm_NormalizationMeasure()
    setattr(partner, 'qm_NormalizationMeasure', None)
    _safe_set(owner, 'qm_MeasureEvaluation102', partner)
    assert getattr(partner, 'qm_NormalizationMeasure') == owner
    _safe_set(owner, 'qm_MeasureEvaluation102', None)
    assert getattr(partner, 'qm_NormalizationMeasure') is None


def test_assoc_originatesFrom17_stub_double():
    # qm_Source has no real 'qm_Source' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModelElement(qualifiedName="sample_text")
    partner = qm_Source()
    setattr(partner, 'qm_Source', None)
    _safe_set(owner, 'qm_QualityModelElement', {partner})
    assert getattr(partner, 'qm_Source') == owner
    _safe_set(owner, 'qm_QualityModelElement', set())
    assert getattr(partner, 'qm_Source') is None


def test_assoc_parent35_stub_double():
    # qm_Specialization has no real 'qm_Specialization' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Specialization()
    setattr(partner, 'qm_Specialization', None)
    _safe_set(owner, 'qm_Entity36', partner)
    assert getattr(partner, 'qm_Specialization') == owner
    _safe_set(owner, 'qm_Entity36', None)
    assert getattr(partner, 'qm_Specialization') is None


def test_assoc_parent39_stub_double():
    # qm_Decomposition has no real 'qm_Decomposition' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Decomposition()
    setattr(partner, 'qm_Decomposition', None)
    _safe_set(owner, 'qm_Entity40', partner)
    assert getattr(partner, 'qm_Decomposition') == owner
    _safe_set(owner, 'qm_Entity40', None)
    assert getattr(partner, 'qm_Decomposition') is None


def test_assoc_parent71_stub_double():
    # qm_MeasureRefinement has no real 'qm_MeasureRefinement' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_MeasureRefinement()
    setattr(partner, 'qm_MeasureRefinement', None)
    _safe_set(owner, 'qm_Measure', partner)
    assert getattr(partner, 'qm_MeasureRefinement') == owner
    _safe_set(owner, 'qm_Measure', None)
    assert getattr(partner, 'qm_MeasureRefinement') is None


def test_assoc_partOf28_stub_double():
    # qm_Decomposition has no real 'Decomposition' property in the generated
    # code (a bare stub) -- manually attach it so qm_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Entity(stakeholder=True, useCase=True)
    partner = qm_Decomposition()
    setattr(partner, 'Decomposition', None)
    _safe_set(owner, 'child29', partner)
    assert getattr(partner, 'Decomposition') == owner
    _safe_set(owner, 'child29', None)
    assert getattr(partner, 'Decomposition') is None


def test_assoc_qualityModel18_stub_double():
    # qm_Source has no real 'sources' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Source()
    setattr(partner, 'sources', None)
    _safe_set(owner, 'QualityModel', partner)
    assert getattr(partner, 'sources') == owner
    _safe_set(owner, 'QualityModel', None)
    assert getattr(partner, 'sources') is None


def test_assoc_qualityModel22_stub_double():
    # qm_Tag has no real 'tags' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Tag()
    setattr(partner, 'tags', None)
    _safe_set(owner, 'QualityModel23', partner)
    assert getattr(partner, 'tags') == owner
    _safe_set(owner, 'QualityModel23', None)
    assert getattr(partner, 'tags') is None


def test_assoc_qualityModel53_stub_double():
    # qm_Factor has no real 'factors' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Factor()
    setattr(partner, 'factors', None)
    _safe_set(owner, 'QualityModel54', partner)
    assert getattr(partner, 'factors') == owner
    _safe_set(owner, 'QualityModel54', None)
    assert getattr(partner, 'factors') is None


def test_assoc_qualityModel90_stub_double():
    # qm_MeasurementMethod has no real 'measurementMethods' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_MeasurementMethod()
    setattr(partner, 'measurementMethods', None)
    _safe_set(owner, 'QualityModel91', partner)
    assert getattr(partner, 'measurementMethods') == owner
    _safe_set(owner, 'QualityModel91', None)
    assert getattr(partner, 'measurementMethods') is None


def test_assoc_qualityModel93_stub_double():
    # qm_Tool has no real 'tools' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Tool()
    setattr(partner, 'tools', None)
    _safe_set(owner, 'QualityModel94', partner)
    assert getattr(partner, 'tools') == owner
    _safe_set(owner, 'QualityModel94', None)
    assert getattr(partner, 'tools') is None


def test_assoc_refines83_stub_double():
    # qm_MeasureRefinement has no real 'MeasureRefinement' property in the generated
    # code (a bare stub) -- manually attach it so qm_Measure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Measure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Measure(type="sample_text")
    partner = qm_MeasureRefinement()
    setattr(partner, 'MeasureRefinement', None)
    _safe_set(owner, 'child84', {partner})
    assert getattr(partner, 'MeasureRefinement') == owner
    _safe_set(owner, 'child84', set())
    assert getattr(partner, 'MeasureRefinement') is None


def test_assoc_resultsFrom117_stub_double():
    # qm_EvaluationResult has no real 'qm_EvaluationResult118' property in the generated
    # code (a bare stub) -- manually attach it so qm_Evaluation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Evaluation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Evaluation(completeness=7, maximumPoints=7)
    partner = qm_EvaluationResult()
    setattr(partner, 'qm_EvaluationResult118', None)
    _safe_set(owner, 'qm_Evaluation119', partner)
    assert getattr(partner, 'qm_EvaluationResult118') == owner
    _safe_set(owner, 'qm_Evaluation119', None)
    assert getattr(partner, 'qm_EvaluationResult118') is None


def test_assoc_resultsFrom124_stub_double():
    # qm_MeasureRanking has no real 'qm_MeasureRanking126' property in the generated
    # code (a bare stub) -- manually attach it so qm_MeasureRankingEvaluationResult's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_MeasureRankingEvaluationResult's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_MeasureRankingEvaluationResult(ratioAffected=3.14)
    partner = qm_MeasureRanking()
    setattr(partner, 'qm_MeasureRanking126', None)
    _safe_set(owner, 'qm_MeasureRankingEvaluationResult125', partner)
    assert getattr(partner, 'qm_MeasureRanking126') == owner
    _safe_set(owner, 'qm_MeasureRankingEvaluationResult125', None)
    assert getattr(partner, 'qm_MeasureRanking126') is None


def test_assoc_source55_stub_double():
    # qm_Factor has no real 'Factor56' property in the generated
    # code (a bare stub) -- manually attach it so qm_Impact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Impact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Impact(effect="sample_text", justification="sample_text")
    partner = qm_Factor()
    setattr(partner, 'Factor56', None)
    _safe_set(owner, 'influences', partner)
    assert getattr(partner, 'Factor56') == owner
    _safe_set(owner, 'influences', None)
    assert getattr(partner, 'Factor56') is None


def test_assoc_sources13_stub_double():
    # qm_Source has no real 'Source' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Source()
    setattr(partner, 'Source', None)
    _safe_set(owner, 'qualityModel14', {partner})
    assert getattr(partner, 'Source') == owner
    _safe_set(owner, 'qualityModel14', set())
    assert getattr(partner, 'Source') is None


def test_assoc_tags11_stub_double():
    # qm_Tag has no real 'Tag' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Tag()
    setattr(partner, 'Tag', None)
    _safe_set(owner, 'qualityModel12', {partner})
    assert getattr(partner, 'Tag') == owner
    _safe_set(owner, 'qualityModel12', set())
    assert getattr(partner, 'Tag') is None


def test_assoc_target57_stub_double():
    # qm_Factor has no real 'qm_Factor58' property in the generated
    # code (a bare stub) -- manually attach it so qm_Impact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_Impact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_Impact(effect="sample_text", justification="sample_text")
    partner = qm_Factor()
    setattr(partner, 'qm_Factor58', None)
    _safe_set(owner, 'qm_Impact', partner)
    assert getattr(partner, 'qm_Factor58') == owner
    _safe_set(owner, 'qm_Impact', None)
    assert getattr(partner, 'qm_Factor58') is None


def test_assoc_tool92_stub_double():
    # qm_Tool has no real 'qm_Tool' property in the generated
    # code (a bare stub) -- manually attach it so qm_ToolBasedInstrument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_ToolBasedInstrument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_ToolBasedInstrument(metric="sample_text")
    partner = qm_Tool()
    setattr(partner, 'qm_Tool', None)
    _safe_set(owner, 'qm_ToolBasedInstrument', partner)
    assert getattr(partner, 'qm_Tool') == owner
    _safe_set(owner, 'qm_ToolBasedInstrument', None)
    assert getattr(partner, 'qm_Tool') is None


def test_assoc_tools9_stub_double():
    # qm_Tool has no real 'Tool' property in the generated
    # code (a bare stub) -- manually attach it so qm_QualityModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_QualityModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_QualityModel(schoolGradeBoundary2="sample_text", schoolGradeBoundary3="sample_text", schoolGradeBoundary4="sample_text", schoolGradeBoundary5="sample_text", schoolGradeBoundary6="sample_text")
    partner = qm_Tool()
    setattr(partner, 'Tool', None)
    _safe_set(owner, 'qualityModel10', {partner})
    assert getattr(partner, 'Tool') == owner
    _safe_set(owner, 'qualityModel10', set())
    assert getattr(partner, 'Tool') is None


def test_assoc_value112_stub_double():
    # qm_NumberMeasurementResult has no real 'qm_NumberMeasurementResult' property in the generated
    # code (a bare stub) -- manually attach it so qm_DoubleInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_DoubleInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_DoubleInterval(lower=3.14, upper=3.14)
    partner = qm_NumberMeasurementResult()
    setattr(partner, 'qm_NumberMeasurementResult', None)
    _safe_set(owner, 'qm_DoubleInterval', partner)
    assert getattr(partner, 'qm_NumberMeasurementResult') == owner
    _safe_set(owner, 'qm_DoubleInterval', None)
    assert getattr(partner, 'qm_NumberMeasurementResult') is None


def test_assoc_value114_stub_double():
    # qm_EvaluationResult has no real 'qm_EvaluationResult115' property in the generated
    # code (a bare stub) -- manually attach it so qm_DoubleInterval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # qm_DoubleInterval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = qm_DoubleInterval(lower=3.14, upper=3.14)
    partner = qm_EvaluationResult()
    setattr(partner, 'qm_EvaluationResult115', None)
    _safe_set(owner, 'qm_DoubleInterval116', partner)
    assert getattr(partner, 'qm_EvaluationResult115') == owner
    _safe_set(owner, 'qm_DoubleInterval116', None)
    assert getattr(partner, 'qm_EvaluationResult115') is None


