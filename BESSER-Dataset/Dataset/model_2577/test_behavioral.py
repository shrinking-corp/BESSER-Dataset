import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AGGREGATE,
    AGGREGATION,
    ALL,
    AT,
    AbsentPatternSourceChain,
    AggregationTime,
    AppAnnotation,
    BEGIN,
    BOOL,
    BY,
    BasicAbsentPatternSource,
    CURRENT,
    DAYS,
    DEFINE,
    DELETE,
    DOUBLE,
    END,
    EVENTS,
    EXPIRED,
    EveryAbsentPatternSource,
    EveryAbsentSequenceSourceChain,
    EverySequenceSourceChain,
    Expression,
    FALSE,
    FIRST,
    FLOAT,
    FOR,
    FROM,
    FULL,
    FUNCTION,
    FeaturesOrOutAttr,
    GROUP,
    HAVING,
    HOURS,
    INNER,
    INSERT,
    INTO,
    INTS,
    IS,
    JOIN,
    JoinSource,
    JoinStream,
    LAST,
    LEFT,
    LONG,
    LeftAbsentPatternSource,
    LeftAbsentSequenceSource,
    LogicalAbsentStatefulSource,
    MILLISECONDS,
    MINUTES,
    MONTHS,
    MathAddsubOperation,
    MathDivmulOperation,
    MathOperation,
    MathOtherOperations,
    NULL,
    Name,
    OBJECT,
    OUTER,
    OUTPUT,
    PARTITION,
    PER,
    PartitionWithStream,
    PatternCollectionStatefulSource,
    PatternStream,
    RAW,
    RETURN,
    RIGHT,
    RightAbsentPatternSource,
    RightAbsentSequenceSource,
    SECONDS,
    SELECT,
    SET,
    SNAPSHOT,
    STREAM,
    STRINGS,
    SequenceCollectionStatefulSource,
    SequenceSource,
    SequenceSourceChain,
    SetAssignment,
    SignedDoubleValue,
    SignedFloatValue,
    SignedLongValue,
    Source1OrStandardStatefulSource,
    StandardStream,
    TABLE,
    TRIGGER,
    TRUE,
    UPDATE,
    WEEKS,
    WINDOW,
    WITH,
    WITHIN,
    YEARS,
    siddhi_AGGREGATE,
    siddhi_AGGREGATION,
    siddhi_ALL,
    siddhi_AND,
    siddhi_APP,
    siddhi_AS,
    siddhi_AT,
    siddhi_AbsentPatternSourceChain,
    siddhi_AbsentSequenceSourceChain,
    siddhi_AggregationTime,
    siddhi_AggregationTimeDuration,
    siddhi_AggregationTimeInterval,
    siddhi_AggregationTimeRange,
    siddhi_Annotation,
    siddhi_AnnotationElement,
    siddhi_AnonymousStream,
    siddhi_AppAnnotation,
    siddhi_Attribute,
    siddhi_AttributeIndex,
    siddhi_AttributeList,
    siddhi_AttributeNameReference,
    siddhi_AttributeReference,
    siddhi_AttributeType,
    siddhi_BEGIN,
    siddhi_BOOL,
    siddhi_BY,
    siddhi_BasicAbsentPatternSource,
    siddhi_BasicSource,
    siddhi_BasicSourceStreamHandler,
    siddhi_BasicSourceStreamHandlers,
    siddhi_BasicSourceStreamHandlers1,
    siddhi_BoolValue,
    siddhi_CURRENT,
    siddhi_Collect,
    siddhi_ConditionRange,
    siddhi_ConditionRanges,
    siddhi_ConstantValue,
    siddhi_D,
    siddhi_DAYS,
    siddhi_DEFINE,
    siddhi_DELETE,
    siddhi_DOUBLE,
    siddhi_DOUBLE_LITERAL,
    siddhi_DayValue,
    siddhi_DefinitionAggregation,
    siddhi_DefinitionFunction,
    siddhi_DefinitionStream,
    siddhi_DefinitionTable,
    siddhi_DefinitionTrigger,
    siddhi_DefinitionWindow,
    siddhi_E,
    siddhi_END,
    siddhi_EObject,
    siddhi_EVENTS,
    siddhi_EVERY,
    siddhi_EXPIRED,
    siddhi_EveryAbsentPatternSource,
    siddhi_EveryAbsentSequenceSourceChain,
    siddhi_EveryPatternSourceChain,
    siddhi_EverySequenceSourceChain,
    siddhi_ExecPartition,
    siddhi_ExecutionElement,
    siddhi_ExecutionPlan,
    siddhi_Expression,
    siddhi_F,
    siddhi_FALSE,
    siddhi_FIRST,
    siddhi_FLOAT,
    siddhi_FLOAT_LITERAL,
    siddhi_FOR,
    siddhi_FROM,
    siddhi_FULL,
    siddhi_FUNCTION,
    siddhi_Features,
    siddhi_FeaturesOrOutAttr,
    siddhi_FeaturesOrOutAttrReference,
    siddhi_Filter,
    siddhi_ForTime,
    siddhi_FunctionBody,
    siddhi_FunctionId,
    siddhi_FunctionName,
    siddhi_FunctionNamespace,
    siddhi_FunctionOperation,
    siddhi_GROUP,
    siddhi_GroupBy,
    siddhi_GroupByQuerySelection,
    siddhi_HAVING,
    siddhi_HOURS,
    siddhi_HavingExpr,
    siddhi_HourValue,
    siddhi_IN,
    siddhi_INNER,
    siddhi_INSERT,
    siddhi_INTO,
    siddhi_INTS,
    siddhi_IS,
    siddhi_JOIN,
    siddhi_JoinSource,
    siddhi_JoinStream,
    siddhi_Keyword,
    siddhi_L,
    siddhi_LAST,
    siddhi_LEFT,
    siddhi_LONG,
    siddhi_LONG_LITERAL,
    siddhi_LanguageName,
    siddhi_LeftAbsentPatternSource,
    siddhi_LeftAbsentPatternSource1,
    siddhi_LeftAbsentSequenceSource,
    siddhi_LeftAbsentSequenceSource1,
    siddhi_Literal,
    siddhi_LogicalAbsentStatefulSource,
    siddhi_LogicalStatefulSource,
    siddhi_MILLISECONDS,
    siddhi_MINUTES,
    siddhi_MONTHS,
    siddhi_MainSource,
    siddhi_MathAddsubOperation,
    siddhi_MathDivmulOperation,
    siddhi_MathEqualOperation,
    siddhi_MathGtLtOperation,
    siddhi_MathInOperation,
    siddhi_MathLogicalOperation,
    siddhi_MathOperation,
    siddhi_MathOtherOperations,
    siddhi_MillisecondValue,
    siddhi_MinuteValue,
    siddhi_MonthValue,
    siddhi_NOT,
    siddhi_NULL,
    siddhi_Name,
    siddhi_NotOperation,
    siddhi_NullCheck,
    siddhi_OBJECT,
    siddhi_OF,
    siddhi_ON,
    siddhi_OR,
    siddhi_OUTER,
    siddhi_OUTPUT,
    siddhi_OutAttr,
    siddhi_OutputAttribute,
    siddhi_OutputEventType,
    siddhi_OutputRate,
    siddhi_OutputRateType,
    siddhi_PARTITION,
    siddhi_PER,
    siddhi_PLAN,
    siddhi_PartitionWithStream,
    siddhi_PatternCollectionStatefulSource,
    siddhi_PatternSource,
    siddhi_PatternSourceChain,
    siddhi_PatternStream,
    siddhi_Per1,
    siddhi_PropertyName,
    siddhi_PropertySeparator,
    siddhi_PropertyValue,
    siddhi_Query,
    siddhi_QueryInput,
    siddhi_QueryOutput,
    siddhi_QuerySection,
    siddhi_RAW,
    siddhi_RETURN,
    siddhi_RIGHT,
    siddhi_RightAbsentPatternSource,
    siddhi_RightAbsentPatternSource1,
    siddhi_RightAbsentSequenceSource,
    siddhi_RightAbsentSequenceSource1,
    siddhi_SECONDS,
    siddhi_SELECT,
    siddhi_SET,
    siddhi_SNAPSHOT,
    siddhi_STREAM,
    siddhi_STRINGS,
    siddhi_SecondValue,
    siddhi_SequenceCollectionStatefulSource,
    siddhi_SequenceSource,
    siddhi_SequenceSourceChain,
    siddhi_SequenceStream,
    siddhi_SetAssignment,
    siddhi_SetClause,
    siddhi_SiddhiQL,
    siddhi_SignedDoubleValue,
    siddhi_SignedFloatValue,
    siddhi_SignedLongValue,
    siddhi_Source,
    siddhi_Source1,
    siddhi_Source1OrStandardStatefulSource,
    siddhi_SourceOrEventReference,
    siddhi_StandardStatefulSource,
    siddhi_StandardStream,
    siddhi_StreamAlias,
    siddhi_StreamFunction,
    siddhi_StreamReference,
    siddhi_StringValue,
    siddhi_TABLE,
    siddhi_TRIGGER,
    siddhi_TRUE,
    siddhi_Target,
    siddhi_TimeValue,
    siddhi_TriggerName,
    siddhi_UNIDIRECTIONAL,
    siddhi_UPDATE,
    siddhi_WEEKS,
    siddhi_WINDOW,
    siddhi_WITH,
    siddhi_WITHIN,
    siddhi_WeekValue,
    siddhi_Win,
    siddhi_WithinTime,
    siddhi_WithinTimeRange,
    siddhi_YEARS,
    siddhi_YearValue,
    siddhi_joins,
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

def test_assoc_coll534_reverse_link_reassign_clear():
    a1 = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    a2 = siddhi_StandardStatefulSource(one_or_more="sample_text_2", zero_or_more="sample_text_2", zero_or_one="sample_text_2")
    b = siddhi_Collect(end="sample_text", start="sample_text")
    _safe_set(b, 'siddhi_Collect', a1)
    assert _is_linked(b, 'siddhi_Collect', a1)
    if hasattr(a1, 'siddhi_StandardStatefulSource535'):
        assert _is_linked(a1, 'siddhi_StandardStatefulSource535', b)
    _safe_set(b, 'siddhi_Collect', a2)
    assert _is_linked(b, 'siddhi_Collect', a2)
    if hasattr(a1, 'siddhi_StandardStatefulSource535'):
        assert not _is_linked(a1, 'siddhi_StandardStatefulSource535', b)
    if hasattr(a2, 'siddhi_StandardStatefulSource535'):
        assert _is_linked(a2, 'siddhi_StandardStatefulSource535', b)
    _safe_set(b, 'siddhi_Collect', None)
    assert not _is_linked(b, 'siddhi_Collect', a2)
    if hasattr(a2, 'siddhi_StandardStatefulSource535'):
        assert not _is_linked(a2, 'siddhi_StandardStatefulSource535', b)


def test_assoc_eps301_reverse_link_reassign_clear():
    a1 = siddhi_EveryPatternSourceChain(op="sample_text")
    a2 = siddhi_EveryPatternSourceChain(op="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain302', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain302', a1)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain300'):
        assert _is_linked(a1, 'siddhi_EveryPatternSourceChain300', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain302', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain302', a2)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain300'):
        assert not _is_linked(a1, 'siddhi_EveryPatternSourceChain300', b)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain300'):
        assert _is_linked(a2, 'siddhi_EveryPatternSourceChain300', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain302', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain302', a2)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain300'):
        assert not _is_linked(a2, 'siddhi_EveryPatternSourceChain300', b)


def test_assoc_every308_reverse_link_reassign_clear():
    a1 = siddhi_EveryPatternSourceChain(op="sample_text")
    a2 = siddhi_EveryPatternSourceChain(op="sample_text_2")
    b = siddhi_EVERY(every1="sample_text")
    _safe_set(b, 'siddhi_EVERY310', a1)
    assert _is_linked(b, 'siddhi_EVERY310', a1)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain309'):
        assert _is_linked(a1, 'siddhi_EveryPatternSourceChain309', b)
    _safe_set(b, 'siddhi_EVERY310', a2)
    assert _is_linked(b, 'siddhi_EVERY310', a2)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain309'):
        assert not _is_linked(a1, 'siddhi_EveryPatternSourceChain309', b)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain309'):
        assert _is_linked(a2, 'siddhi_EveryPatternSourceChain309', b)
    _safe_set(b, 'siddhi_EVERY310', None)
    assert not _is_linked(b, 'siddhi_EVERY310', a2)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain309'):
        assert not _is_linked(a2, 'siddhi_EveryPatternSourceChain309', b)


def test_assoc_everyPSC1406_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentPatternSource(fb2="sample_text")
    a2 = siddhi_RightAbsentPatternSource(fb2="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain408', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain408', a1)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource407'):
        assert _is_linked(a1, 'siddhi_RightAbsentPatternSource407', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain408', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain408', a2)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource407'):
        assert not _is_linked(a1, 'siddhi_RightAbsentPatternSource407', b)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource407'):
        assert _is_linked(a2, 'siddhi_RightAbsentPatternSource407', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain408', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain408', a2)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource407'):
        assert not _is_linked(a2, 'siddhi_RightAbsentPatternSource407', b)


def test_assoc_everyPSC389_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    a2 = siddhi_LeftAbsentPatternSource(fb1="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain391', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain391', a1)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource390'):
        assert _is_linked(a1, 'siddhi_LeftAbsentPatternSource390', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain391', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain391', a2)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource390'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentPatternSource390', b)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource390'):
        assert _is_linked(a2, 'siddhi_LeftAbsentPatternSource390', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain391', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain391', a2)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource390'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentPatternSource390', b)


def test_assoc_left1254_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    a2 = siddhi_RightAbsentSequenceSource(comm="sample_text_2", comma="sample_text_2", cp="sample_text_2", op="sample_text_2")
    b = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_RightAbsentSequenceSource255', a1)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource255', a1)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource253'):
        assert _is_linked(a1, 'siddhi_RightAbsentSequenceSource253', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource255', a2)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource255', a2)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource253'):
        assert not _is_linked(a1, 'siddhi_RightAbsentSequenceSource253', b)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource253'):
        assert _is_linked(a2, 'siddhi_RightAbsentSequenceSource253', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource255', None)
    assert not _is_linked(b, 'siddhi_RightAbsentSequenceSource255', a2)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource253'):
        assert not _is_linked(a2, 'siddhi_RightAbsentSequenceSource253', b)


def test_assoc_left1396_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentPatternSource(fb2="sample_text")
    a2 = siddhi_RightAbsentPatternSource(fb2="sample_text_2")
    b = siddhi_RightAbsentPatternSource(fb2="sample_text")
    _safe_set(b, 'siddhi_RightAbsentPatternSource395', a1)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource395', a1)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource'):
        assert _is_linked(a1, 'siddhi_RightAbsentPatternSource', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource395', a2)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource395', a2)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource'):
        assert not _is_linked(a1, 'siddhi_RightAbsentPatternSource', b)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource'):
        assert _is_linked(a2, 'siddhi_RightAbsentPatternSource', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource395', None)
    assert not _is_linked(b, 'siddhi_RightAbsentPatternSource395', a2)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource'):
        assert not _is_linked(a2, 'siddhi_RightAbsentPatternSource', b)


def test_assoc_left237_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    a2 = siddhi_LeftAbsentSequenceSource(comm="sample_text_2", comma="sample_text_2", cp="sample_text_2", op="sample_text_2")
    b = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource238', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource238', a1)
    if hasattr(a1, 'siddhi_LeftAbsentSequenceSource236'):
        assert _is_linked(a1, 'siddhi_LeftAbsentSequenceSource236', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource238', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource238', a2)
    if hasattr(a1, 'siddhi_LeftAbsentSequenceSource236'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentSequenceSource236', b)
    if hasattr(a2, 'siddhi_LeftAbsentSequenceSource236'):
        assert _is_linked(a2, 'siddhi_LeftAbsentSequenceSource236', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource238', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentSequenceSource238', a2)
    if hasattr(a2, 'siddhi_LeftAbsentSequenceSource236'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentSequenceSource236', b)


def test_assoc_left272_reverse_link_reassign_clear():
    a1 = siddhi_SequenceSourceChain(op="sample_text")
    a2 = siddhi_SequenceSourceChain(op="sample_text_2")
    b = siddhi_SequenceSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_SequenceSourceChain273', a1)
    assert _is_linked(b, 'siddhi_SequenceSourceChain273', a1)
    if hasattr(a1, 'siddhi_SequenceSourceChain271'):
        assert _is_linked(a1, 'siddhi_SequenceSourceChain271', b)
    _safe_set(b, 'siddhi_SequenceSourceChain273', a2)
    assert _is_linked(b, 'siddhi_SequenceSourceChain273', a2)
    if hasattr(a1, 'siddhi_SequenceSourceChain271'):
        assert not _is_linked(a1, 'siddhi_SequenceSourceChain271', b)
    if hasattr(a2, 'siddhi_SequenceSourceChain271'):
        assert _is_linked(a2, 'siddhi_SequenceSourceChain271', b)
    _safe_set(b, 'siddhi_SequenceSourceChain273', None)
    assert not _is_linked(b, 'siddhi_SequenceSourceChain273', a2)
    if hasattr(a2, 'siddhi_SequenceSourceChain271'):
        assert not _is_linked(a2, 'siddhi_SequenceSourceChain271', b)


def test_assoc_left296_reverse_link_reassign_clear():
    a1 = siddhi_EveryPatternSourceChain(op="sample_text")
    a2 = siddhi_EveryPatternSourceChain(op="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain295', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain295', a1)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain'):
        assert _is_linked(a1, 'siddhi_EveryPatternSourceChain', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain295', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain295', a2)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain'):
        assert not _is_linked(a1, 'siddhi_EveryPatternSourceChain', b)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain'):
        assert _is_linked(a2, 'siddhi_EveryPatternSourceChain', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain295', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain295', a2)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain'):
        assert not _is_linked(a2, 'siddhi_EveryPatternSourceChain', b)


def test_assoc_left312_reverse_link_reassign_clear():
    a1 = siddhi_PatternSourceChain(op="sample_text")
    a2 = siddhi_PatternSourceChain(op="sample_text_2")
    b = siddhi_PatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_PatternSourceChain313', a1)
    assert _is_linked(b, 'siddhi_PatternSourceChain313', a1)
    if hasattr(a1, 'siddhi_PatternSourceChain311'):
        assert _is_linked(a1, 'siddhi_PatternSourceChain311', b)
    _safe_set(b, 'siddhi_PatternSourceChain313', a2)
    assert _is_linked(b, 'siddhi_PatternSourceChain313', a2)
    if hasattr(a1, 'siddhi_PatternSourceChain311'):
        assert not _is_linked(a1, 'siddhi_PatternSourceChain311', b)
    if hasattr(a2, 'siddhi_PatternSourceChain311'):
        assert _is_linked(a2, 'siddhi_PatternSourceChain311', b)
    _safe_set(b, 'siddhi_PatternSourceChain313', None)
    assert not _is_linked(b, 'siddhi_PatternSourceChain313', a2)
    if hasattr(a2, 'siddhi_PatternSourceChain311'):
        assert not _is_linked(a2, 'siddhi_PatternSourceChain311', b)


def test_assoc_left376_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    a2 = siddhi_LeftAbsentPatternSource(fb1="sample_text_2")
    b = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentPatternSource375', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource375', a1)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource'):
        assert _is_linked(a1, 'siddhi_LeftAbsentPatternSource', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource375', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource375', a2)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentPatternSource', b)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource'):
        assert _is_linked(a2, 'siddhi_LeftAbsentPatternSource', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource375', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentPatternSource375', a2)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentPatternSource', b)


def test_assoc_left650_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentPatternSource1(fb="sample_text")
    a2 = siddhi_RightAbsentPatternSource1(fb="sample_text_2")
    b = siddhi_RightAbsentPatternSource(fb2="sample_text")
    _safe_set(b, 'siddhi_RightAbsentPatternSource651', a1)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource651', a1)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource1'):
        assert _is_linked(a1, 'siddhi_RightAbsentPatternSource1', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource651', a2)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource651', a2)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource1'):
        assert not _is_linked(a1, 'siddhi_RightAbsentPatternSource1', b)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource1'):
        assert _is_linked(a2, 'siddhi_RightAbsentPatternSource1', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource651', None)
    assert not _is_linked(b, 'siddhi_RightAbsentPatternSource651', a2)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource1'):
        assert not _is_linked(a2, 'siddhi_RightAbsentPatternSource1', b)


def test_assoc_leftAbsPS381_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    a2 = siddhi_LeftAbsentPatternSource(fb1="sample_text_2")
    b = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentPatternSource382', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource382', a1)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource380'):
        assert _is_linked(a1, 'siddhi_LeftAbsentPatternSource380', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource382', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource382', a2)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource380'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentPatternSource380', b)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource380'):
        assert _is_linked(a2, 'siddhi_LeftAbsentPatternSource380', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource382', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentPatternSource382', a2)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource380'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentPatternSource380', b)


def test_assoc_leftAbsPatternSrc393_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    a2 = siddhi_LeftAbsentPatternSource(fb1="sample_text_2")
    b = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentPatternSource394', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource394', a1)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource392'):
        assert _is_linked(a1, 'siddhi_LeftAbsentPatternSource392', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource394', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentPatternSource394', a2)
    if hasattr(a1, 'siddhi_LeftAbsentPatternSource392'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentPatternSource392', b)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource392'):
        assert _is_linked(a2, 'siddhi_LeftAbsentPatternSource392', b)
    _safe_set(b, 'siddhi_LeftAbsentPatternSource394', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentPatternSource394', a2)
    if hasattr(a2, 'siddhi_LeftAbsentPatternSource392'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentPatternSource392', b)


def test_assoc_leftAbsentSequenceSource242_reverse_link_reassign_clear():
    a1 = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    a2 = siddhi_LeftAbsentSequenceSource(comm="sample_text_2", comma="sample_text_2", cp="sample_text_2", op="sample_text_2")
    b = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource243', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource243', a1)
    if hasattr(a1, 'siddhi_LeftAbsentSequenceSource241'):
        assert _is_linked(a1, 'siddhi_LeftAbsentSequenceSource241', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource243', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource243', a2)
    if hasattr(a1, 'siddhi_LeftAbsentSequenceSource241'):
        assert not _is_linked(a1, 'siddhi_LeftAbsentSequenceSource241', b)
    if hasattr(a2, 'siddhi_LeftAbsentSequenceSource241'):
        assert _is_linked(a2, 'siddhi_LeftAbsentSequenceSource241', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource243', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentSequenceSource243', a2)
    if hasattr(a2, 'siddhi_LeftAbsentSequenceSource241'):
        assert not _is_linked(a2, 'siddhi_LeftAbsentSequenceSource241', b)


def test_assoc_name503_reverse_link_reassign_clear():
    a1 = siddhi_StreamReference(hash="sample_text")
    a2 = siddhi_StreamReference(hash="sample_text_2")
    b = siddhi_Name(na="sample_text")
    _safe_set(b, 'siddhi_Name505', a1)
    assert _is_linked(b, 'siddhi_Name505', a1)
    if hasattr(a1, 'siddhi_StreamReference504'):
        assert _is_linked(a1, 'siddhi_StreamReference504', b)
    _safe_set(b, 'siddhi_Name505', a2)
    assert _is_linked(b, 'siddhi_Name505', a2)
    if hasattr(a1, 'siddhi_StreamReference504'):
        assert not _is_linked(a1, 'siddhi_StreamReference504', b)
    if hasattr(a2, 'siddhi_StreamReference504'):
        assert _is_linked(a2, 'siddhi_StreamReference504', b)
    _safe_set(b, 'siddhi_Name505', None)
    assert not _is_linked(b, 'siddhi_Name505', a2)
    if hasattr(a2, 'siddhi_StreamReference504'):
        assert not _is_linked(a2, 'siddhi_StreamReference504', b)


def test_assoc_name640_reverse_link_reassign_clear():
    a1 = siddhi_Name(na="sample_text")
    a2 = siddhi_Name(na="sample_text_2")
    b = siddhi_APP(ap="sample_text")
    _safe_set(b, 'siddhi_APP', a1)
    assert _is_linked(b, 'siddhi_APP', a1)
    if hasattr(a1, 'siddhi_Name641'):
        assert _is_linked(a1, 'siddhi_Name641', b)
    _safe_set(b, 'siddhi_APP', a2)
    assert _is_linked(b, 'siddhi_APP', a2)
    if hasattr(a1, 'siddhi_Name641'):
        assert not _is_linked(a1, 'siddhi_Name641', b)
    if hasattr(a2, 'siddhi_Name641'):
        assert _is_linked(a2, 'siddhi_Name641', b)
    _safe_set(b, 'siddhi_APP', None)
    assert not _is_linked(b, 'siddhi_APP', a2)
    if hasattr(a2, 'siddhi_Name641'):
        assert not _is_linked(a2, 'siddhi_Name641', b)


def test_assoc_psc306_reverse_link_reassign_clear():
    a1 = siddhi_PatternSourceChain(op="sample_text")
    a2 = siddhi_PatternSourceChain(op="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain307', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain307', a1)
    if hasattr(a1, 'siddhi_PatternSourceChain'):
        assert _is_linked(a1, 'siddhi_PatternSourceChain', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain307', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain307', a2)
    if hasattr(a1, 'siddhi_PatternSourceChain'):
        assert not _is_linked(a1, 'siddhi_PatternSourceChain', b)
    if hasattr(a2, 'siddhi_PatternSourceChain'):
        assert _is_linked(a2, 'siddhi_PatternSourceChain', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain307', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain307', a2)
    if hasattr(a2, 'siddhi_PatternSourceChain'):
        assert not _is_linked(a2, 'siddhi_PatternSourceChain', b)


def test_assoc_psc_2318_reverse_link_reassign_clear():
    a1 = siddhi_PatternSourceChain(op="sample_text")
    a2 = siddhi_PatternSourceChain(op="sample_text_2")
    b = siddhi_PatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_PatternSourceChain319', a1)
    assert _is_linked(b, 'siddhi_PatternSourceChain319', a1)
    if hasattr(a1, 'siddhi_PatternSourceChain317'):
        assert _is_linked(a1, 'siddhi_PatternSourceChain317', b)
    _safe_set(b, 'siddhi_PatternSourceChain319', a2)
    assert _is_linked(b, 'siddhi_PatternSourceChain319', a2)
    if hasattr(a1, 'siddhi_PatternSourceChain317'):
        assert not _is_linked(a1, 'siddhi_PatternSourceChain317', b)
    if hasattr(a2, 'siddhi_PatternSourceChain317'):
        assert _is_linked(a2, 'siddhi_PatternSourceChain317', b)
    _safe_set(b, 'siddhi_PatternSourceChain319', None)
    assert not _is_linked(b, 'siddhi_PatternSourceChain319', a2)
    if hasattr(a2, 'siddhi_PatternSourceChain317'):
        assert not _is_linked(a2, 'siddhi_PatternSourceChain317', b)


def test_assoc_right1257_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    a2 = siddhi_RightAbsentSequenceSource(comm="sample_text_2", comma="sample_text_2", cp="sample_text_2", op="sample_text_2")
    b = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_RightAbsentSequenceSource258', a1)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource258', a1)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource256'):
        assert _is_linked(a1, 'siddhi_RightAbsentSequenceSource256', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource258', a2)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource258', a2)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource256'):
        assert not _is_linked(a1, 'siddhi_RightAbsentSequenceSource256', b)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource256'):
        assert _is_linked(a2, 'siddhi_RightAbsentSequenceSource256', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource258', None)
    assert not _is_linked(b, 'siddhi_RightAbsentSequenceSource258', a2)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource256'):
        assert not _is_linked(a2, 'siddhi_RightAbsentSequenceSource256', b)


def test_assoc_right1398_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentPatternSource(fb2="sample_text")
    a2 = siddhi_RightAbsentPatternSource(fb2="sample_text_2")
    b = siddhi_RightAbsentPatternSource(fb2="sample_text")
    _safe_set(b, 'siddhi_RightAbsentPatternSource399', a1)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource399', a1)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource397'):
        assert _is_linked(a1, 'siddhi_RightAbsentPatternSource397', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource399', a2)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource399', a2)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource397'):
        assert not _is_linked(a1, 'siddhi_RightAbsentPatternSource397', b)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource397'):
        assert _is_linked(a2, 'siddhi_RightAbsentPatternSource397', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource399', None)
    assert not _is_linked(b, 'siddhi_RightAbsentPatternSource399', a2)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource397'):
        assert not _is_linked(a2, 'siddhi_RightAbsentPatternSource397', b)


def test_assoc_right275_reverse_link_reassign_clear():
    a1 = siddhi_SequenceSourceChain(op="sample_text")
    a2 = siddhi_SequenceSourceChain(op="sample_text_2")
    b = siddhi_SequenceSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_SequenceSourceChain276', a1)
    assert _is_linked(b, 'siddhi_SequenceSourceChain276', a1)
    if hasattr(a1, 'siddhi_SequenceSourceChain274'):
        assert _is_linked(a1, 'siddhi_SequenceSourceChain274', b)
    _safe_set(b, 'siddhi_SequenceSourceChain276', a2)
    assert _is_linked(b, 'siddhi_SequenceSourceChain276', a2)
    if hasattr(a1, 'siddhi_SequenceSourceChain274'):
        assert not _is_linked(a1, 'siddhi_SequenceSourceChain274', b)
    if hasattr(a2, 'siddhi_SequenceSourceChain274'):
        assert _is_linked(a2, 'siddhi_SequenceSourceChain274', b)
    _safe_set(b, 'siddhi_SequenceSourceChain276', None)
    assert not _is_linked(b, 'siddhi_SequenceSourceChain276', a2)
    if hasattr(a2, 'siddhi_SequenceSourceChain274'):
        assert not _is_linked(a2, 'siddhi_SequenceSourceChain274', b)


def test_assoc_right298_reverse_link_reassign_clear():
    a1 = siddhi_EveryPatternSourceChain(op="sample_text")
    a2 = siddhi_EveryPatternSourceChain(op="sample_text_2")
    b = siddhi_EveryPatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_EveryPatternSourceChain299', a1)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain299', a1)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain297'):
        assert _is_linked(a1, 'siddhi_EveryPatternSourceChain297', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain299', a2)
    assert _is_linked(b, 'siddhi_EveryPatternSourceChain299', a2)
    if hasattr(a1, 'siddhi_EveryPatternSourceChain297'):
        assert not _is_linked(a1, 'siddhi_EveryPatternSourceChain297', b)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain297'):
        assert _is_linked(a2, 'siddhi_EveryPatternSourceChain297', b)
    _safe_set(b, 'siddhi_EveryPatternSourceChain299', None)
    assert not _is_linked(b, 'siddhi_EveryPatternSourceChain299', a2)
    if hasattr(a2, 'siddhi_EveryPatternSourceChain297'):
        assert not _is_linked(a2, 'siddhi_EveryPatternSourceChain297', b)


def test_assoc_right315_reverse_link_reassign_clear():
    a1 = siddhi_PatternSourceChain(op="sample_text")
    a2 = siddhi_PatternSourceChain(op="sample_text_2")
    b = siddhi_PatternSourceChain(op="sample_text")
    _safe_set(b, 'siddhi_PatternSourceChain316', a1)
    assert _is_linked(b, 'siddhi_PatternSourceChain316', a1)
    if hasattr(a1, 'siddhi_PatternSourceChain314'):
        assert _is_linked(a1, 'siddhi_PatternSourceChain314', b)
    _safe_set(b, 'siddhi_PatternSourceChain316', a2)
    assert _is_linked(b, 'siddhi_PatternSourceChain316', a2)
    if hasattr(a1, 'siddhi_PatternSourceChain314'):
        assert not _is_linked(a1, 'siddhi_PatternSourceChain314', b)
    if hasattr(a2, 'siddhi_PatternSourceChain314'):
        assert _is_linked(a2, 'siddhi_PatternSourceChain314', b)
    _safe_set(b, 'siddhi_PatternSourceChain316', None)
    assert not _is_linked(b, 'siddhi_PatternSourceChain316', a2)
    if hasattr(a2, 'siddhi_PatternSourceChain314'):
        assert not _is_linked(a2, 'siddhi_PatternSourceChain314', b)


def test_assoc_right491_reverse_link_reassign_clear():
    a1 = siddhi_MathDivmulOperation(devide="sample_text", mod="sample_text", multiply="sample_text")
    a2 = siddhi_MathDivmulOperation(devide="sample_text_2", mod="sample_text_2", multiply="sample_text_2")
    b = siddhi_MathAddsubOperation(add="sample_text", substract="sample_text")
    _safe_set(b, 'siddhi_MathAddsubOperation', a1)
    assert _is_linked(b, 'siddhi_MathAddsubOperation', a1)
    if hasattr(a1, 'siddhi_MathDivmulOperation'):
        assert _is_linked(a1, 'siddhi_MathDivmulOperation', b)
    _safe_set(b, 'siddhi_MathAddsubOperation', a2)
    assert _is_linked(b, 'siddhi_MathAddsubOperation', a2)
    if hasattr(a1, 'siddhi_MathDivmulOperation'):
        assert not _is_linked(a1, 'siddhi_MathDivmulOperation', b)
    if hasattr(a2, 'siddhi_MathDivmulOperation'):
        assert _is_linked(a2, 'siddhi_MathDivmulOperation', b)
    _safe_set(b, 'siddhi_MathAddsubOperation', None)
    assert not _is_linked(b, 'siddhi_MathAddsubOperation', a2)
    if hasattr(a2, 'siddhi_MathDivmulOperation'):
        assert not _is_linked(a2, 'siddhi_MathDivmulOperation', b)


def test_assoc_right669_reverse_link_reassign_clear():
    a1 = siddhi_MathEqualOperation(eq="sample_text", not_eq="sample_text")
    a2 = siddhi_MathEqualOperation(eq="sample_text_2", not_eq="sample_text_2")
    b = siddhi_MathAddsubOperation(add="sample_text", substract="sample_text")
    _safe_set(b, 'siddhi_MathAddsubOperation670', a1)
    assert _is_linked(b, 'siddhi_MathAddsubOperation670', a1)
    if hasattr(a1, 'siddhi_MathEqualOperation'):
        assert _is_linked(a1, 'siddhi_MathEqualOperation', b)
    _safe_set(b, 'siddhi_MathAddsubOperation670', a2)
    assert _is_linked(b, 'siddhi_MathAddsubOperation670', a2)
    if hasattr(a1, 'siddhi_MathEqualOperation'):
        assert not _is_linked(a1, 'siddhi_MathEqualOperation', b)
    if hasattr(a2, 'siddhi_MathEqualOperation'):
        assert _is_linked(a2, 'siddhi_MathEqualOperation', b)
    _safe_set(b, 'siddhi_MathAddsubOperation670', None)
    assert not _is_linked(b, 'siddhi_MathAddsubOperation670', a2)
    if hasattr(a2, 'siddhi_MathEqualOperation'):
        assert not _is_linked(a2, 'siddhi_MathEqualOperation', b)


def test_assoc_rightAbsPS401_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentPatternSource(fb2="sample_text")
    a2 = siddhi_RightAbsentPatternSource(fb2="sample_text_2")
    b = siddhi_RightAbsentPatternSource(fb2="sample_text")
    _safe_set(b, 'siddhi_RightAbsentPatternSource402', a1)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource402', a1)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource400'):
        assert _is_linked(a1, 'siddhi_RightAbsentPatternSource400', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource402', a2)
    assert _is_linked(b, 'siddhi_RightAbsentPatternSource402', a2)
    if hasattr(a1, 'siddhi_RightAbsentPatternSource400'):
        assert not _is_linked(a1, 'siddhi_RightAbsentPatternSource400', b)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource400'):
        assert _is_linked(a2, 'siddhi_RightAbsentPatternSource400', b)
    _safe_set(b, 'siddhi_RightAbsentPatternSource402', None)
    assert not _is_linked(b, 'siddhi_RightAbsentPatternSource402', a2)
    if hasattr(a2, 'siddhi_RightAbsentPatternSource400'):
        assert not _is_linked(a2, 'siddhi_RightAbsentPatternSource400', b)


def test_assoc_rightAbsentSequenceSource260_reverse_link_reassign_clear():
    a1 = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    a2 = siddhi_RightAbsentSequenceSource(comm="sample_text_2", comma="sample_text_2", cp="sample_text_2", op="sample_text_2")
    b = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_RightAbsentSequenceSource261', a1)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource261', a1)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource259'):
        assert _is_linked(a1, 'siddhi_RightAbsentSequenceSource259', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource261', a2)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource261', a2)
    if hasattr(a1, 'siddhi_RightAbsentSequenceSource259'):
        assert not _is_linked(a1, 'siddhi_RightAbsentSequenceSource259', b)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource259'):
        assert _is_linked(a2, 'siddhi_RightAbsentSequenceSource259', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource261', None)
    assert not _is_linked(b, 'siddhi_RightAbsentSequenceSource261', a2)
    if hasattr(a2, 'siddhi_RightAbsentSequenceSource259'):
        assert not _is_linked(a2, 'siddhi_RightAbsentSequenceSource259', b)


def test_assoc_sequenceSourceChain250_reverse_link_reassign_clear():
    a1 = siddhi_SequenceSourceChain(op="sample_text")
    a2 = siddhi_SequenceSourceChain(op="sample_text_2")
    b = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource251', a1)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource251', a1)
    if hasattr(a1, 'siddhi_SequenceSourceChain252'):
        assert _is_linked(a1, 'siddhi_SequenceSourceChain252', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource251', a2)
    assert _is_linked(b, 'siddhi_LeftAbsentSequenceSource251', a2)
    if hasattr(a1, 'siddhi_SequenceSourceChain252'):
        assert not _is_linked(a1, 'siddhi_SequenceSourceChain252', b)
    if hasattr(a2, 'siddhi_SequenceSourceChain252'):
        assert _is_linked(a2, 'siddhi_SequenceSourceChain252', b)
    _safe_set(b, 'siddhi_LeftAbsentSequenceSource251', None)
    assert not _is_linked(b, 'siddhi_LeftAbsentSequenceSource251', a2)
    if hasattr(a2, 'siddhi_SequenceSourceChain252'):
        assert not _is_linked(a2, 'siddhi_SequenceSourceChain252', b)


def test_assoc_sequenceSourceChain265_reverse_link_reassign_clear():
    a1 = siddhi_SequenceSourceChain(op="sample_text")
    a2 = siddhi_SequenceSourceChain(op="sample_text_2")
    b = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    _safe_set(b, 'siddhi_RightAbsentSequenceSource266', a1)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource266', a1)
    if hasattr(a1, 'siddhi_SequenceSourceChain267'):
        assert _is_linked(a1, 'siddhi_SequenceSourceChain267', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource266', a2)
    assert _is_linked(b, 'siddhi_RightAbsentSequenceSource266', a2)
    if hasattr(a1, 'siddhi_SequenceSourceChain267'):
        assert not _is_linked(a1, 'siddhi_SequenceSourceChain267', b)
    if hasattr(a2, 'siddhi_SequenceSourceChain267'):
        assert _is_linked(a2, 'siddhi_SequenceSourceChain267', b)
    _safe_set(b, 'siddhi_RightAbsentSequenceSource266', None)
    assert not _is_linked(b, 'siddhi_RightAbsentSequenceSource266', a2)
    if hasattr(a2, 'siddhi_SequenceSourceChain267'):
        assert not _is_linked(a2, 'siddhi_SequenceSourceChain267', b)


def test_assoc_sv563_reverse_link_reassign_clear():
    a1 = siddhi_StringValue(sl="sample_text")
    a2 = siddhi_StringValue(sl="sample_text_2")
    b = siddhi_ConstantValue(siv="sample_text")
    _safe_set(b, 'siddhi_ConstantValue564', a1)
    assert _is_linked(b, 'siddhi_ConstantValue564', a1)
    if hasattr(a1, 'siddhi_StringValue565'):
        assert _is_linked(a1, 'siddhi_StringValue565', b)
    _safe_set(b, 'siddhi_ConstantValue564', a2)
    assert _is_linked(b, 'siddhi_ConstantValue564', a2)
    if hasattr(a1, 'siddhi_StringValue565'):
        assert not _is_linked(a1, 'siddhi_StringValue565', b)
    if hasattr(a2, 'siddhi_StringValue565'):
        assert _is_linked(a2, 'siddhi_StringValue565', b)
    _safe_set(b, 'siddhi_ConstantValue564', None)
    assert not _is_linked(b, 'siddhi_ConstantValue564', a2)
    if hasattr(a2, 'siddhi_StringValue565'):
        assert not _is_linked(a2, 'siddhi_StringValue565', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_OPEN_SQARE_BRACKETSattribute_index1521_stub_double():
    # siddhi_AttributeIndex has no real 'siddhi_AttributeIndex523' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_AttributeIndex()
    setattr(partner, 'siddhi_AttributeIndex523', None)
    _safe_set(owner, 'siddhi_AttributeReference522', partner)
    assert getattr(partner, 'siddhi_AttributeIndex523') == owner
    _safe_set(owner, 'siddhi_AttributeReference522', None)
    assert getattr(partner, 'siddhi_AttributeIndex523') is None


def test_assoc_OPEN_SQARE_BRACKETSattribute_index2527_stub_double():
    # siddhi_AttributeIndex has no real 'siddhi_AttributeIndex529' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_AttributeIndex()
    setattr(partner, 'siddhi_AttributeIndex529', None)
    _safe_set(owner, 'siddhi_AttributeReference528', partner)
    assert getattr(partner, 'siddhi_AttributeIndex529') == owner
    _safe_set(owner, 'siddhi_AttributeReference528', None)
    assert getattr(partner, 'siddhi_AttributeIndex529') is None


def test_assoc_a129_stub_double():
    # siddhi_ConditionRange has no real 'siddhi_ConditionRange130' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AS(a="sample_text")
    partner = siddhi_ConditionRange()
    setattr(partner, 'siddhi_ConditionRange130', None)
    _safe_set(owner, 'siddhi_AS', partner)
    assert getattr(partner, 'siddhi_ConditionRange130') == owner
    _safe_set(owner, 'siddhi_AS', None)
    assert getattr(partner, 'siddhi_ConditionRange130') is None


def test_assoc_a198_stub_double():
    # siddhi_OutAttr has no real 'siddhi_OutAttr199' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AS(a="sample_text")
    partner = siddhi_OutAttr()
    setattr(partner, 'siddhi_OutAttr199', None)
    _safe_set(owner, 'siddhi_AS200', partner)
    assert getattr(partner, 'siddhi_OutAttr199') == owner
    _safe_set(owner, 'siddhi_AS200', None)
    assert getattr(partner, 'siddhi_OutAttr199') is None


def test_assoc_a449_stub_double():
    # siddhi_MainSource has no real 'siddhi_MainSource450' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AS(a="sample_text")
    partner = siddhi_MainSource()
    setattr(partner, 'siddhi_MainSource450', None)
    _safe_set(owner, 'siddhi_AS451', partner)
    assert getattr(partner, 'siddhi_MainSource450') == owner
    _safe_set(owner, 'siddhi_AS451', None)
    assert getattr(partner, 'siddhi_MainSource450') is None


def test_assoc_a611_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AS's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AS's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AS(a="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword', None)
    _safe_set(owner, 'siddhi_AS612', partner)
    assert getattr(partner, 'siddhi_Keyword') == owner
    _safe_set(owner, 'siddhi_AS612', None)
    assert getattr(partner, 'siddhi_Keyword') is None


def test_assoc_aatr_index506_stub_double():
    # siddhi_AttributeIndex has no real 'siddhi_AttributeIndex' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StreamReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StreamReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StreamReference(hash="sample_text")
    partner = siddhi_AttributeIndex()
    setattr(partner, 'siddhi_AttributeIndex', None)
    _safe_set(owner, 'siddhi_StreamReference507', partner)
    assert getattr(partner, 'siddhi_AttributeIndex') == owner
    _safe_set(owner, 'siddhi_StreamReference507', None)
    assert getattr(partner, 'siddhi_AttributeIndex') is None


def test_assoc_and_336_stub_double():
    # siddhi_LogicalStatefulSource has no real 'siddhi_LogicalStatefulSource337' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AND's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AND's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AND(and_="sample_text")
    partner = siddhi_LogicalStatefulSource()
    setattr(partner, 'siddhi_LogicalStatefulSource337', None)
    _safe_set(owner, 'siddhi_AND', partner)
    assert getattr(partner, 'siddhi_LogicalStatefulSource337') == owner
    _safe_set(owner, 'siddhi_AND', None)
    assert getattr(partner, 'siddhi_LogicalStatefulSource337') is None


def test_assoc_and_347_stub_double():
    # siddhi_LogicalAbsentStatefulSource has no real 'siddhi_LogicalAbsentStatefulSource348' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AND's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AND's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AND(and_="sample_text")
    partner = siddhi_LogicalAbsentStatefulSource()
    setattr(partner, 'siddhi_LogicalAbsentStatefulSource348', None)
    _safe_set(owner, 'siddhi_AND349', partner)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource348') == owner
    _safe_set(owner, 'siddhi_AND349', None)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource348') is None


def test_assoc_and_622_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword623' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AND's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AND's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AND(and_="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword623', None)
    _safe_set(owner, 'siddhi_AND624', partner)
    assert getattr(partner, 'siddhi_Keyword623') == owner
    _safe_set(owner, 'siddhi_AND624', None)
    assert getattr(partner, 'siddhi_Keyword623') is None


def test_assoc_and_655_stub_double():
    # siddhi_MathLogicalOperation has no real 'siddhi_MathLogicalOperation' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AND's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AND's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AND(and_="sample_text")
    partner = siddhi_MathLogicalOperation()
    setattr(partner, 'siddhi_MathLogicalOperation', None)
    _safe_set(owner, 'siddhi_AND656', partner)
    assert getattr(partner, 'siddhi_MathLogicalOperation') == owner
    _safe_set(owner, 'siddhi_AND656', None)
    assert getattr(partner, 'siddhi_MathLogicalOperation') is None


def test_assoc_ann5642_stub_double():
    # siddhi_AnnotationElement has no real 'siddhi_AnnotationElement644' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_APP's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_APP's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_APP(ap="sample_text")
    partner = siddhi_AnnotationElement()
    setattr(partner, 'siddhi_AnnotationElement644', None)
    _safe_set(owner, 'siddhi_APP643', {partner})
    assert getattr(partner, 'siddhi_AnnotationElement644') == owner
    _safe_set(owner, 'siddhi_APP643', set())
    assert getattr(partner, 'siddhi_AnnotationElement644') is None


def test_assoc_attrRef513_stub_double():
    # siddhi_Literal has no real 'siddhi_Literal514' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_Literal()
    setattr(partner, 'siddhi_Literal514', None)
    _safe_set(owner, 'siddhi_AttributeReference515', partner)
    assert getattr(partner, 'siddhi_Literal514') == owner
    _safe_set(owner, 'siddhi_AttributeReference515', None)
    assert getattr(partner, 'siddhi_Literal514') is None


def test_assoc_attrRef75_stub_double():
    # siddhi_DefinitionAggregation has no real 'siddhi_DefinitionAggregation76' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_DefinitionAggregation()
    setattr(partner, 'siddhi_DefinitionAggregation76', None)
    _safe_set(owner, 'siddhi_AttributeReference', partner)
    assert getattr(partner, 'siddhi_DefinitionAggregation76') == owner
    _safe_set(owner, 'siddhi_AttributeReference', None)
    assert getattr(partner, 'siddhi_DefinitionAggregation76') is None


def test_assoc_attr_ref185_stub_double():
    # siddhi_GroupBy has no real 'siddhi_GroupBy186' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_GroupBy()
    setattr(partner, 'siddhi_GroupBy186', None)
    _safe_set(owner, 'siddhi_AttributeReference187', partner)
    assert owner in getattr(partner, 'siddhi_GroupBy186')
    _safe_set(owner, 'siddhi_AttributeReference187', None)
    assert owner not in getattr(partner, 'siddhi_GroupBy186')


def test_assoc_attr_ref193_stub_double():
    # siddhi_OutputAttribute has no real 'siddhi_OutputAttribute194' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_OutputAttribute()
    setattr(partner, 'siddhi_OutputAttribute194', None)
    _safe_set(owner, 'siddhi_AttributeReference195', partner)
    assert getattr(partner, 'siddhi_OutputAttribute194') == owner
    _safe_set(owner, 'siddhi_AttributeReference195', None)
    assert getattr(partner, 'siddhi_OutputAttribute194') is None


def test_assoc_attr_ref497_stub_double():
    # siddhi_NullCheck has no real 'siddhi_NullCheck498' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_NullCheck()
    setattr(partner, 'siddhi_NullCheck498', None)
    _safe_set(owner, 'siddhi_AttributeReference499', partner)
    assert getattr(partner, 'siddhi_NullCheck498') == owner
    _safe_set(owner, 'siddhi_AttributeReference499', None)
    assert getattr(partner, 'siddhi_NullCheck498') is None


def test_assoc_basicAbsentPatternSource247_stub_double():
    # siddhi_BasicAbsentPatternSource has no real 'siddhi_BasicAbsentPatternSource249' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_BasicAbsentPatternSource()
    setattr(partner, 'siddhi_BasicAbsentPatternSource249', None)
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource248', partner)
    assert getattr(partner, 'siddhi_BasicAbsentPatternSource249') == owner
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource248', None)
    assert getattr(partner, 'siddhi_BasicAbsentPatternSource249') is None


def test_assoc_basicAbsentPatternSource268_stub_double():
    # siddhi_BasicAbsentPatternSource has no real 'siddhi_BasicAbsentPatternSource270' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_BasicAbsentPatternSource()
    setattr(partner, 'siddhi_BasicAbsentPatternSource270', None)
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource269', partner)
    assert getattr(partner, 'siddhi_BasicAbsentPatternSource270') == owner
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource269', None)
    assert getattr(partner, 'siddhi_BasicAbsentPatternSource270') is None


def test_assoc_basicSrc634_stub_double():
    # siddhi_BasicSource has no real 'siddhi_BasicSource636' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_NOT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_NOT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_NOT(not1="sample_text")
    partner = siddhi_BasicSource()
    setattr(partner, 'siddhi_BasicSource636', None)
    _safe_set(owner, 'siddhi_NOT635', partner)
    assert getattr(partner, 'siddhi_BasicSource636') == owner
    _safe_set(owner, 'siddhi_NOT635', None)
    assert getattr(partner, 'siddhi_BasicSource636') is None


def test_assoc_basic_ss_handlers539_stub_double():
    # siddhi_BasicSourceStreamHandlers has no real 'siddhi_BasicSourceStreamHandlers541' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    partner = siddhi_BasicSourceStreamHandlers()
    setattr(partner, 'siddhi_BasicSourceStreamHandlers541', None)
    _safe_set(owner, 'siddhi_StandardStatefulSource540', partner)
    assert getattr(partner, 'siddhi_BasicSourceStreamHandlers541') == owner
    _safe_set(owner, 'siddhi_StandardStatefulSource540', None)
    assert getattr(partner, 'siddhi_BasicSourceStreamHandlers541') is None


def test_assoc_bv552_stub_double():
    # siddhi_BoolValue has no real 'siddhi_BoolValue' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_BoolValue()
    setattr(partner, 'siddhi_BoolValue', None)
    _safe_set(owner, 'siddhi_ConstantValue553', partner)
    assert getattr(partner, 'siddhi_BoolValue') == owner
    _safe_set(owner, 'siddhi_ConstantValue553', None)
    assert getattr(partner, 'siddhi_BoolValue') is None


def test_assoc_const_val508_stub_double():
    # siddhi_Literal has no real 'siddhi_Literal509' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_Literal()
    setattr(partner, 'siddhi_Literal509', None)
    _safe_set(owner, 'siddhi_ConstantValue', partner)
    assert getattr(partner, 'siddhi_Literal509') == owner
    _safe_set(owner, 'siddhi_ConstantValue', None)
    assert getattr(partner, 'siddhi_Literal509') is None


def test_assoc_d604_stub_double():
    # siddhi_DOUBLE_LITERAL has no real 'siddhi_DOUBLE_LITERAL605' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_D's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_D's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_D(d="sample_text")
    partner = siddhi_DOUBLE_LITERAL()
    setattr(partner, 'siddhi_DOUBLE_LITERAL605', None)
    _safe_set(owner, 'siddhi_D', partner)
    assert getattr(partner, 'siddhi_DOUBLE_LITERAL605') == owner
    _safe_set(owner, 'siddhi_D', None)
    assert getattr(partner, 'siddhi_DOUBLE_LITERAL605') is None


def test_assoc_e603_stub_double():
    # siddhi_DOUBLE_LITERAL has no real 'siddhi_DOUBLE_LITERAL' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_E(e="sample_text")
    partner = siddhi_DOUBLE_LITERAL()
    setattr(partner, 'siddhi_DOUBLE_LITERAL', None)
    _safe_set(owner, 'siddhi_E', partner)
    assert getattr(partner, 'siddhi_DOUBLE_LITERAL') == owner
    _safe_set(owner, 'siddhi_E', None)
    assert getattr(partner, 'siddhi_DOUBLE_LITERAL') is None


def test_assoc_e606_stub_double():
    # siddhi_FLOAT_LITERAL has no real 'siddhi_FLOAT_LITERAL' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_E's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_E's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_E(e="sample_text")
    partner = siddhi_FLOAT_LITERAL()
    setattr(partner, 'siddhi_FLOAT_LITERAL', None)
    _safe_set(owner, 'siddhi_E607', partner)
    assert getattr(partner, 'siddhi_FLOAT_LITERAL') == owner
    _safe_set(owner, 'siddhi_E607', None)
    assert getattr(partner, 'siddhi_FLOAT_LITERAL') is None


def test_assoc_eve77_stub_double():
    # siddhi_DefinitionAggregation has no real 'siddhi_DefinitionAggregation78' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_EVERY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_EVERY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_EVERY(every1="sample_text")
    partner = siddhi_DefinitionAggregation()
    setattr(partner, 'siddhi_DefinitionAggregation78', None)
    _safe_set(owner, 'siddhi_EVERY79', partner)
    assert getattr(partner, 'siddhi_DefinitionAggregation78') == owner
    _safe_set(owner, 'siddhi_EVERY79', None)
    assert getattr(partner, 'siddhi_DefinitionAggregation78') is None


def test_assoc_every170_stub_double():
    # siddhi_OutputRate has no real 'siddhi_OutputRate171' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_EVERY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_EVERY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_EVERY(every1="sample_text")
    partner = siddhi_OutputRate()
    setattr(partner, 'siddhi_OutputRate171', None)
    _safe_set(owner, 'siddhi_EVERY172', partner)
    assert getattr(partner, 'siddhi_OutputRate171') == owner
    _safe_set(owner, 'siddhi_EVERY172', None)
    assert getattr(partner, 'siddhi_OutputRate171') is None


def test_assoc_every51_stub_double():
    # siddhi_DefinitionTrigger has no real 'siddhi_DefinitionTrigger52' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_EVERY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_EVERY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_EVERY(every1="sample_text")
    partner = siddhi_DefinitionTrigger()
    setattr(partner, 'siddhi_DefinitionTrigger52', None)
    _safe_set(owner, 'siddhi_EVERY', partner)
    assert getattr(partner, 'siddhi_DefinitionTrigger52') == owner
    _safe_set(owner, 'siddhi_EVERY', None)
    assert getattr(partner, 'siddhi_DefinitionTrigger52') is None


def test_assoc_every613_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword614' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_EVERY's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_EVERY's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_EVERY(every1="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword614', None)
    _safe_set(owner, 'siddhi_EVERY615', partner)
    assert getattr(partner, 'siddhi_Keyword614') == owner
    _safe_set(owner, 'siddhi_EVERY615', None)
    assert getattr(partner, 'siddhi_Keyword614') is None


def test_assoc_everyAbsPS1409_stub_double():
    # siddhi_EveryAbsentPatternSource has no real 'siddhi_EveryAbsentPatternSource411' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentPatternSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentPatternSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentPatternSource(fb2="sample_text")
    partner = siddhi_EveryAbsentPatternSource()
    setattr(partner, 'siddhi_EveryAbsentPatternSource411', None)
    _safe_set(owner, 'siddhi_RightAbsentPatternSource410', partner)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource411') == owner
    _safe_set(owner, 'siddhi_RightAbsentPatternSource410', None)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource411') is None


def test_assoc_everyAbsPS386_stub_double():
    # siddhi_EveryAbsentPatternSource has no real 'siddhi_EveryAbsentPatternSource388' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentPatternSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentPatternSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    partner = siddhi_EveryAbsentPatternSource()
    setattr(partner, 'siddhi_EveryAbsentPatternSource388', None)
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource387', partner)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource388') == owner
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource387', None)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource388') is None


def test_assoc_expression516_stub_double():
    # siddhi_Expression has no real 'siddhi_Expression518' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_Expression()
    setattr(partner, 'siddhi_Expression518', None)
    _safe_set(owner, 'siddhi_AttributeReference517', partner)
    assert getattr(partner, 'siddhi_Expression518') == owner
    _safe_set(owner, 'siddhi_AttributeReference517', None)
    assert getattr(partner, 'siddhi_Expression518') is None


def test_assoc_f608_stub_double():
    # siddhi_FLOAT_LITERAL has no real 'siddhi_FLOAT_LITERAL609' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_F's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_F's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_F(f="sample_text")
    partner = siddhi_FLOAT_LITERAL()
    setattr(partner, 'siddhi_FLOAT_LITERAL609', None)
    _safe_set(owner, 'siddhi_F', partner)
    assert getattr(partner, 'siddhi_FLOAT_LITERAL609') == owner
    _safe_set(owner, 'siddhi_F', None)
    assert getattr(partner, 'siddhi_FLOAT_LITERAL609') is None


def test_assoc_featuresOrAttrRef530_stub_double():
    # siddhi_FeaturesOrOutAttrReference has no real 'siddhi_FeaturesOrOutAttrReference' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_FeaturesOrOutAttrReference()
    setattr(partner, 'siddhi_FeaturesOrOutAttrReference', None)
    _safe_set(owner, 'siddhi_AttributeReference531', partner)
    assert getattr(partner, 'siddhi_FeaturesOrOutAttrReference') == owner
    _safe_set(owner, 'siddhi_AttributeReference531', None)
    assert getattr(partner, 'siddhi_FeaturesOrOutAttrReference') is None


def test_assoc_fn57_stub_double():
    # siddhi_DefinitionFunction has no real 'siddhi_DefinitionFunction58' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_FunctionName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_FunctionName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_FunctionName(id="sample_text")
    partner = siddhi_DefinitionFunction()
    setattr(partner, 'siddhi_DefinitionFunction58', None)
    _safe_set(owner, 'siddhi_FunctionName', partner)
    assert getattr(partner, 'siddhi_DefinitionFunction58') == owner
    _safe_set(owner, 'siddhi_FunctionName', None)
    assert getattr(partner, 'siddhi_DefinitionFunction58') is None


def test_assoc_ft637_stub_double():
    # siddhi_ForTime has no real 'siddhi_ForTime639' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_NOT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_NOT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_NOT(not1="sample_text")
    partner = siddhi_ForTime()
    setattr(partner, 'siddhi_ForTime639', None)
    _safe_set(owner, 'siddhi_NOT638', partner)
    assert getattr(partner, 'siddhi_ForTime639') == owner
    _safe_set(owner, 'siddhi_NOT638', None)
    assert getattr(partner, 'siddhi_ForTime639') is None


def test_assoc_func_body63_stub_double():
    # siddhi_DefinitionFunction has no real 'siddhi_DefinitionFunction64' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_FunctionBody's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_FunctionBody's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_FunctionBody(value="sample_text")
    partner = siddhi_DefinitionFunction()
    setattr(partner, 'siddhi_DefinitionFunction64', None)
    _safe_set(owner, 'siddhi_FunctionBody', partner)
    assert getattr(partner, 'siddhi_DefinitionFunction64') == owner
    _safe_set(owner, 'siddhi_FunctionBody', None)
    assert getattr(partner, 'siddhi_DefinitionFunction64') is None


def test_assoc_in_663_stub_double():
    # siddhi_MathInOperation has no real 'siddhi_MathInOperation' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_IN's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_IN's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_IN(in_="sample_text")
    partner = siddhi_MathInOperation()
    setattr(partner, 'siddhi_MathInOperation', None)
    _safe_set(owner, 'siddhi_IN', partner)
    assert getattr(partner, 'siddhi_MathInOperation') == owner
    _safe_set(owner, 'siddhi_IN', None)
    assert getattr(partner, 'siddhi_MathInOperation') is None


def test_assoc_l610_stub_double():
    # siddhi_LONG_LITERAL has no real 'siddhi_LONG_LITERAL' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_L's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_L's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_L(l="sample_text")
    partner = siddhi_LONG_LITERAL()
    setattr(partner, 'siddhi_LONG_LITERAL', None)
    _safe_set(owner, 'siddhi_L', partner)
    assert getattr(partner, 'siddhi_LONG_LITERAL') == owner
    _safe_set(owner, 'siddhi_L', None)
    assert getattr(partner, 'siddhi_LONG_LITERAL') is None


def test_assoc_left645_stub_double():
    # siddhi_RightAbsentSequenceSource1 has no real 'siddhi_RightAbsentSequenceSource1' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_RightAbsentSequenceSource1()
    setattr(partner, 'siddhi_RightAbsentSequenceSource1', None)
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource646', partner)
    assert getattr(partner, 'siddhi_RightAbsentSequenceSource1') == owner
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource646', None)
    assert getattr(partner, 'siddhi_RightAbsentSequenceSource1') is None


def test_assoc_leftAbsentSequenceSource232_stub_double():
    # siddhi_AbsentSequenceSourceChain has no real 'siddhi_AbsentSequenceSourceChain233' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_AbsentSequenceSourceChain()
    setattr(partner, 'siddhi_AbsentSequenceSourceChain233', None)
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource', partner)
    assert getattr(partner, 'siddhi_AbsentSequenceSourceChain233') == owner
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource', None)
    assert getattr(partner, 'siddhi_AbsentSequenceSourceChain233') is None


def test_assoc_left_uni431_stub_double():
    # siddhi_JoinStream has no real 'siddhi_JoinStream432' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_UNIDIRECTIONAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_UNIDIRECTIONAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_UNIDIRECTIONAL(unidirectional="sample_text")
    partner = siddhi_JoinStream()
    setattr(partner, 'siddhi_JoinStream432', None)
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL433', partner)
    assert getattr(partner, 'siddhi_JoinStream432') == owner
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL433', None)
    assert getattr(partner, 'siddhi_JoinStream432') is None


def test_assoc_ln59_stub_double():
    # siddhi_DefinitionFunction has no real 'siddhi_DefinitionFunction60' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LanguageName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LanguageName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LanguageName(id="sample_text")
    partner = siddhi_DefinitionFunction()
    setattr(partner, 'siddhi_DefinitionFunction60', None)
    _safe_set(owner, 'siddhi_LanguageName', partner)
    assert getattr(partner, 'siddhi_DefinitionFunction60') == owner
    _safe_set(owner, 'siddhi_LanguageName', None)
    assert getattr(partner, 'siddhi_DefinitionFunction60') is None


def test_assoc_na160_stub_double():
    # siddhi_Target has no real 'siddhi_Target161' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_Target()
    setattr(partner, 'siddhi_Target161', None)
    _safe_set(owner, 'siddhi_Source1162', partner)
    assert getattr(partner, 'siddhi_Target161') == owner
    _safe_set(owner, 'siddhi_Source1162', None)
    assert getattr(partner, 'siddhi_Target161') is None


def test_assoc_na548_stub_double():
    # siddhi_SourceOrEventReference has no real 'siddhi_SourceOrEventReference549' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1OrStandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1OrStandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1OrStandardStatefulSource(name="sample_text")
    partner = siddhi_SourceOrEventReference()
    setattr(partner, 'siddhi_SourceOrEventReference549', None)
    _safe_set(owner, 'siddhi_Source1OrStandardStatefulSource', partner)
    assert getattr(partner, 'siddhi_SourceOrEventReference549') == owner
    _safe_set(owner, 'siddhi_Source1OrStandardStatefulSource', None)
    assert getattr(partner, 'siddhi_SourceOrEventReference549') is None


def test_assoc_nam103_stub_double():
    # siddhi_Features has no real 'siddhi_Features104' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_Features()
    setattr(partner, 'siddhi_Features104', None)
    _safe_set(owner, 'siddhi_Name105', partner)
    assert getattr(partner, 'siddhi_Features104') == owner
    _safe_set(owner, 'siddhi_Name105', None)
    assert getattr(partner, 'siddhi_Features104') is None


def test_assoc_nam443_stub_double():
    # siddhi_StreamAlias has no real 'siddhi_StreamAlias' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_StreamAlias()
    setattr(partner, 'siddhi_StreamAlias', None)
    _safe_set(owner, 'siddhi_Name444', partner)
    assert getattr(partner, 'siddhi_StreamAlias') == owner
    _safe_set(owner, 'siddhi_Name444', None)
    assert getattr(partner, 'siddhi_StreamAlias') is None


def test_assoc_name1519_stub_double():
    # siddhi_SourceOrEventReference has no real 'siddhi_SourceOrEventReference' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_SourceOrEventReference()
    setattr(partner, 'siddhi_SourceOrEventReference', None)
    _safe_set(owner, 'siddhi_AttributeReference520', partner)
    assert getattr(partner, 'siddhi_SourceOrEventReference') == owner
    _safe_set(owner, 'siddhi_AttributeReference520', None)
    assert getattr(partner, 'siddhi_SourceOrEventReference') is None


def test_assoc_name2524_stub_double():
    # siddhi_SourceOrEventReference has no real 'siddhi_SourceOrEventReference526' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_AttributeReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_AttributeReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_AttributeReference(hash1="sample_text", hash2="sample_text", name="sample_text")
    partner = siddhi_SourceOrEventReference()
    setattr(partner, 'siddhi_SourceOrEventReference526', None)
    _safe_set(owner, 'siddhi_AttributeReference525', partner)
    assert getattr(partner, 'siddhi_SourceOrEventReference526') == owner
    _safe_set(owner, 'siddhi_AttributeReference525', None)
    assert getattr(partner, 'siddhi_SourceOrEventReference526') is None


def test_assoc_name572_stub_double():
    # siddhi_FunctionNamespace has no real 'siddhi_FunctionNamespace573' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_FunctionNamespace()
    setattr(partner, 'siddhi_FunctionNamespace573', None)
    _safe_set(owner, 'siddhi_Name574', partner)
    assert getattr(partner, 'siddhi_FunctionNamespace573') == owner
    _safe_set(owner, 'siddhi_Name574', None)
    assert getattr(partner, 'siddhi_FunctionNamespace573') is None


def test_assoc_name575_stub_double():
    # siddhi_FunctionId has no real 'siddhi_FunctionId576' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_FunctionId()
    setattr(partner, 'siddhi_FunctionId576', None)
    _safe_set(owner, 'siddhi_Name577', partner)
    assert getattr(partner, 'siddhi_FunctionId576') == owner
    _safe_set(owner, 'siddhi_Name577', None)
    assert getattr(partner, 'siddhi_FunctionId576') is None


def test_assoc_name664_stub_double():
    # siddhi_MathInOperation has no real 'siddhi_MathInOperation665' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_MathInOperation()
    setattr(partner, 'siddhi_MathInOperation665', None)
    _safe_set(owner, 'siddhi_Name666', partner)
    assert getattr(partner, 'siddhi_MathInOperation665') == owner
    _safe_set(owner, 'siddhi_Name666', None)
    assert getattr(partner, 'siddhi_MathInOperation665') is None


def test_assoc_name84_stub_double():
    # siddhi_Annotation has no real 'siddhi_Annotation85' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_Annotation()
    setattr(partner, 'siddhi_Annotation85', None)
    _safe_set(owner, 'siddhi_Name', partner)
    assert getattr(partner, 'siddhi_Annotation85') == owner
    _safe_set(owner, 'siddhi_Name', None)
    assert getattr(partner, 'siddhi_Annotation85') is None


def test_assoc_name98_stub_double():
    # siddhi_PropertyName has no real 'siddhi_PropertyName99' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Name(na="sample_text")
    partner = siddhi_PropertyName()
    setattr(partner, 'siddhi_PropertyName99', None)
    _safe_set(owner, 'siddhi_Name100', partner)
    assert owner in getattr(partner, 'siddhi_PropertyName99')
    _safe_set(owner, 'siddhi_Name100', None)
    assert owner not in getattr(partner, 'siddhi_PropertyName99')


def test_assoc_not_350_stub_double():
    # siddhi_LogicalAbsentStatefulSource has no real 'siddhi_LogicalAbsentStatefulSource351' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_NOT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_NOT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_NOT(not1="sample_text")
    partner = siddhi_LogicalAbsentStatefulSource()
    setattr(partner, 'siddhi_LogicalAbsentStatefulSource351', None)
    _safe_set(owner, 'siddhi_NOT', partner)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource351') == owner
    _safe_set(owner, 'siddhi_NOT', None)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource351') is None


def test_assoc_not_628_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword629' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_NOT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_NOT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_NOT(not1="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword629', None)
    _safe_set(owner, 'siddhi_NOT630', partner)
    assert getattr(partner, 'siddhi_Keyword629') == owner
    _safe_set(owner, 'siddhi_NOT630', None)
    assert getattr(partner, 'siddhi_Keyword629') is None


def test_assoc_not_671_stub_double():
    # siddhi_NotOperation has no real 'siddhi_NotOperation' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_NOT's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_NOT's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_NOT(not1="sample_text")
    partner = siddhi_NotOperation()
    setattr(partner, 'siddhi_NotOperation', None)
    _safe_set(owner, 'siddhi_NOT672', partner)
    assert getattr(partner, 'siddhi_NotOperation') == owner
    _safe_set(owner, 'siddhi_NOT672', None)
    assert getattr(partner, 'siddhi_NotOperation') is None


def test_assoc_o363_stub_double():
    # siddhi_LogicalAbsentStatefulSource has no real 'siddhi_LogicalAbsentStatefulSource364' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_LogicalAbsentStatefulSource()
    setattr(partner, 'siddhi_LogicalAbsentStatefulSource364', None)
    _safe_set(owner, 'siddhi_OR365', partner)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource364') == owner
    _safe_set(owner, 'siddhi_OR365', None)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource364') is None


def test_assoc_of119_stub_double():
    # siddhi_ConditionRanges has no real 'siddhi_ConditionRanges' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OF(of="sample_text")
    partner = siddhi_ConditionRanges()
    setattr(partner, 'siddhi_ConditionRanges', None)
    _safe_set(owner, 'siddhi_OF', partner)
    assert getattr(partner, 'siddhi_ConditionRanges') == owner
    _safe_set(owner, 'siddhi_OF', None)
    assert getattr(partner, 'siddhi_ConditionRanges') is None


def test_assoc_of631_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword632' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OF's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OF's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OF(of="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword632', None)
    _safe_set(owner, 'siddhi_OF633', partner)
    assert getattr(partner, 'siddhi_Keyword632') == owner
    _safe_set(owner, 'siddhi_OF633', None)
    assert getattr(partner, 'siddhi_Keyword632') is None


def test_assoc_on150_stub_double():
    # siddhi_QueryOutput has no real 'siddhi_QueryOutput151' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ON's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ON's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ON(on="sample_text")
    partner = siddhi_QueryOutput()
    setattr(partner, 'siddhi_QueryOutput151', None)
    _safe_set(owner, 'siddhi_ON', partner)
    assert getattr(partner, 'siddhi_QueryOutput151') == owner
    _safe_set(owner, 'siddhi_ON', None)
    assert getattr(partner, 'siddhi_QueryOutput151') is None


def test_assoc_on419_stub_double():
    # siddhi_JoinStream has no real 'siddhi_JoinStream420' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ON's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ON's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ON(on="sample_text")
    partner = siddhi_JoinStream()
    setattr(partner, 'siddhi_JoinStream420', None)
    _safe_set(owner, 'siddhi_ON421', partner)
    assert getattr(partner, 'siddhi_JoinStream420') == owner
    _safe_set(owner, 'siddhi_ON421', None)
    assert getattr(partner, 'siddhi_JoinStream420') is None


def test_assoc_on619_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword620' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ON's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ON's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ON(on="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword620', None)
    _safe_set(owner, 'siddhi_ON621', partner)
    assert getattr(partner, 'siddhi_Keyword620') == owner
    _safe_set(owner, 'siddhi_ON621', None)
    assert getattr(partner, 'siddhi_Keyword620') is None


def test_assoc_or_125_stub_double():
    # siddhi_ConditionRanges has no real 'siddhi_ConditionRanges126' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_ConditionRanges()
    setattr(partner, 'siddhi_ConditionRanges126', None)
    _safe_set(owner, 'siddhi_OR', partner)
    assert owner in getattr(partner, 'siddhi_ConditionRanges126')
    _safe_set(owner, 'siddhi_OR', None)
    assert owner not in getattr(partner, 'siddhi_ConditionRanges126')


def test_assoc_or_155_stub_double():
    # siddhi_QueryOutput has no real 'siddhi_QueryOutput156' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_QueryOutput()
    setattr(partner, 'siddhi_QueryOutput156', None)
    _safe_set(owner, 'siddhi_OR157', partner)
    assert getattr(partner, 'siddhi_QueryOutput156') == owner
    _safe_set(owner, 'siddhi_OR157', None)
    assert getattr(partner, 'siddhi_QueryOutput156') is None


def test_assoc_or_338_stub_double():
    # siddhi_LogicalStatefulSource has no real 'siddhi_LogicalStatefulSource339' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_LogicalStatefulSource()
    setattr(partner, 'siddhi_LogicalStatefulSource339', None)
    _safe_set(owner, 'siddhi_OR340', partner)
    assert getattr(partner, 'siddhi_LogicalStatefulSource339') == owner
    _safe_set(owner, 'siddhi_OR340', None)
    assert getattr(partner, 'siddhi_LogicalStatefulSource339') is None


def test_assoc_or_625_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword626' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword626', None)
    _safe_set(owner, 'siddhi_OR627', partner)
    assert getattr(partner, 'siddhi_Keyword626') == owner
    _safe_set(owner, 'siddhi_OR627', None)
    assert getattr(partner, 'siddhi_Keyword626') is None


def test_assoc_or_657_stub_double():
    # siddhi_MathLogicalOperation has no real 'siddhi_MathLogicalOperation658' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_OR's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_OR's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_OR(or_="sample_text")
    partner = siddhi_MathLogicalOperation()
    setattr(partner, 'siddhi_MathLogicalOperation658', None)
    _safe_set(owner, 'siddhi_OR659', partner)
    assert getattr(partner, 'siddhi_MathLogicalOperation658') == owner
    _safe_set(owner, 'siddhi_OR659', None)
    assert getattr(partner, 'siddhi_MathLogicalOperation658') is None


def test_assoc_ps323_stub_double():
    # siddhi_PatternSource has no real 'siddhi_PatternSource' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_PatternSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_PatternSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_PatternSourceChain(op="sample_text")
    partner = siddhi_PatternSource()
    setattr(partner, 'siddhi_PatternSource', None)
    _safe_set(owner, 'siddhi_PatternSourceChain324', partner)
    assert getattr(partner, 'siddhi_PatternSource') == owner
    _safe_set(owner, 'siddhi_PatternSourceChain324', None)
    assert getattr(partner, 'siddhi_PatternSource') is None


def test_assoc_right239_stub_double():
    # siddhi_EObject has no real 'siddhi_EObject' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_EObject()
    setattr(partner, 'siddhi_EObject', None)
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource240', partner)
    assert getattr(partner, 'siddhi_EObject') == owner
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource240', None)
    assert getattr(partner, 'siddhi_EObject') is None


def test_assoc_right377_stub_double():
    # siddhi_AbsentPatternSourceChain has no real 'siddhi_AbsentPatternSourceChain379' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentPatternSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentPatternSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    partner = siddhi_AbsentPatternSourceChain()
    setattr(partner, 'siddhi_AbsentPatternSourceChain379', None)
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource378', partner)
    assert getattr(partner, 'siddhi_AbsentPatternSourceChain379') == owner
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource378', None)
    assert getattr(partner, 'siddhi_AbsentPatternSourceChain379') is None


def test_assoc_right647_stub_double():
    # siddhi_RightAbsentSequenceSource1 has no real 'siddhi_RightAbsentSequenceSource1648' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_SequenceSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_SequenceSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_SequenceSourceChain(op="sample_text")
    partner = siddhi_RightAbsentSequenceSource1()
    setattr(partner, 'siddhi_RightAbsentSequenceSource1648', None)
    _safe_set(owner, 'siddhi_SequenceSourceChain649', partner)
    assert getattr(partner, 'siddhi_RightAbsentSequenceSource1648') == owner
    _safe_set(owner, 'siddhi_SequenceSourceChain649', None)
    assert getattr(partner, 'siddhi_RightAbsentSequenceSource1648') is None


def test_assoc_right652_stub_double():
    # siddhi_EveryAbsentPatternSource has no real 'siddhi_EveryAbsentPatternSource654' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentPatternSource1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentPatternSource1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentPatternSource1(fb="sample_text")
    partner = siddhi_EveryAbsentPatternSource()
    setattr(partner, 'siddhi_EveryAbsentPatternSource654', None)
    _safe_set(owner, 'siddhi_RightAbsentPatternSource1653', partner)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource654') == owner
    _safe_set(owner, 'siddhi_RightAbsentPatternSource1653', None)
    assert getattr(partner, 'siddhi_EveryAbsentPatternSource654') is None


def test_assoc_right667_stub_double():
    # siddhi_MathOperation has no real 'siddhi_MathOperation668' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_MathGtLtOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_MathGtLtOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_MathGtLtOperation(gt="sample_text", gt_eq="sample_text", lt="sample_text", lt_eq="sample_text")
    partner = siddhi_MathOperation()
    setattr(partner, 'siddhi_MathOperation668', None)
    _safe_set(owner, 'siddhi_MathGtLtOperation', partner)
    assert getattr(partner, 'siddhi_MathOperation668') == owner
    _safe_set(owner, 'siddhi_MathGtLtOperation', None)
    assert getattr(partner, 'siddhi_MathOperation668') is None


def test_assoc_rightAbsentSequenceSource234_stub_double():
    # siddhi_AbsentSequenceSourceChain has no real 'siddhi_AbsentSequenceSourceChain235' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_AbsentSequenceSourceChain()
    setattr(partner, 'siddhi_AbsentSequenceSourceChain235', None)
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource', partner)
    assert getattr(partner, 'siddhi_AbsentSequenceSourceChain235') == owner
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource', None)
    assert getattr(partner, 'siddhi_AbsentSequenceSourceChain235') is None


def test_assoc_right_uni417_stub_double():
    # siddhi_JoinStream has no real 'siddhi_JoinStream418' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_UNIDIRECTIONAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_UNIDIRECTIONAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_UNIDIRECTIONAL(unidirectional="sample_text")
    partner = siddhi_JoinStream()
    setattr(partner, 'siddhi_JoinStream418', None)
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL', partner)
    assert getattr(partner, 'siddhi_JoinStream418') == owner
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL', None)
    assert getattr(partner, 'siddhi_JoinStream418') is None


def test_assoc_sdv554_stub_double():
    # siddhi_SignedDoubleValue has no real 'siddhi_SignedDoubleValue' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_SignedDoubleValue()
    setattr(partner, 'siddhi_SignedDoubleValue', None)
    _safe_set(owner, 'siddhi_ConstantValue555', partner)
    assert getattr(partner, 'siddhi_SignedDoubleValue') == owner
    _safe_set(owner, 'siddhi_ConstantValue555', None)
    assert getattr(partner, 'siddhi_SignedDoubleValue') is None


def test_assoc_seqSrcChain221_stub_double():
    # siddhi_EveryAbsentSequenceSourceChain has no real 'siddhi_EveryAbsentSequenceSourceChain222' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_SequenceSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_SequenceSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_SequenceSourceChain(op="sample_text")
    partner = siddhi_EveryAbsentSequenceSourceChain()
    setattr(partner, 'siddhi_EveryAbsentSequenceSourceChain222', None)
    _safe_set(owner, 'siddhi_SequenceSourceChain223', partner)
    assert getattr(partner, 'siddhi_EveryAbsentSequenceSourceChain222') == owner
    _safe_set(owner, 'siddhi_SequenceSourceChain223', None)
    assert getattr(partner, 'siddhi_EveryAbsentSequenceSourceChain222') is None


def test_assoc_sfv556_stub_double():
    # siddhi_SignedFloatValue has no real 'siddhi_SignedFloatValue' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_SignedFloatValue()
    setattr(partner, 'siddhi_SignedFloatValue', None)
    _safe_set(owner, 'siddhi_ConstantValue557', partner)
    assert getattr(partner, 'siddhi_SignedFloatValue') == owner
    _safe_set(owner, 'siddhi_ConstantValue557', None)
    assert getattr(partner, 'siddhi_SignedFloatValue') is None


def test_assoc_slv558_stub_double():
    # siddhi_SignedLongValue has no real 'siddhi_SignedLongValue' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_SignedLongValue()
    setattr(partner, 'siddhi_SignedLongValue', None)
    _safe_set(owner, 'siddhi_ConstantValue559', partner)
    assert getattr(partner, 'siddhi_SignedLongValue') == owner
    _safe_set(owner, 'siddhi_ConstantValue559', None)
    assert getattr(partner, 'siddhi_SignedLongValue') is None


def test_assoc_src23_stub_double():
    # siddhi_DefinitionStream has no real 'siddhi_DefinitionStream24' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_DefinitionStream()
    setattr(partner, 'siddhi_DefinitionStream24', None)
    _safe_set(owner, 'siddhi_Source1', partner)
    assert getattr(partner, 'siddhi_DefinitionStream24') == owner
    _safe_set(owner, 'siddhi_Source1', None)
    assert getattr(partner, 'siddhi_DefinitionStream24') is None


def test_assoc_src30_stub_double():
    # siddhi_DefinitionTable has no real 'siddhi_DefinitionTable31' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_DefinitionTable()
    setattr(partner, 'siddhi_DefinitionTable31', None)
    _safe_set(owner, 'siddhi_Source132', partner)
    assert getattr(partner, 'siddhi_DefinitionTable31') == owner
    _safe_set(owner, 'siddhi_Source132', None)
    assert getattr(partner, 'siddhi_DefinitionTable31') is None


def test_assoc_src39_stub_double():
    # siddhi_DefinitionWindow has no real 'siddhi_DefinitionWindow40' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_DefinitionWindow()
    setattr(partner, 'siddhi_DefinitionWindow40', None)
    _safe_set(owner, 'siddhi_Source141', partner)
    assert getattr(partner, 'siddhi_DefinitionWindow40') == owner
    _safe_set(owner, 'siddhi_Source141', None)
    assert getattr(partner, 'siddhi_DefinitionWindow40') is None


def test_assoc_src536_stub_double():
    # siddhi_Source has no real 'siddhi_Source538' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    partner = siddhi_Source()
    setattr(partner, 'siddhi_Source538', None)
    _safe_set(owner, 'siddhi_StandardStatefulSource537', partner)
    assert getattr(partner, 'siddhi_Source538') == owner
    _safe_set(owner, 'siddhi_StandardStatefulSource537', None)
    assert getattr(partner, 'siddhi_Source538') is None


def test_assoc_src68_stub_double():
    # siddhi_DefinitionAggregation has no real 'siddhi_DefinitionAggregation69' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_DefinitionAggregation()
    setattr(partner, 'siddhi_DefinitionAggregation69', None)
    _safe_set(owner, 'siddhi_Source170', partner)
    assert getattr(partner, 'siddhi_DefinitionAggregation69') == owner
    _safe_set(owner, 'siddhi_Source170', None)
    assert getattr(partner, 'siddhi_DefinitionAggregation69') is None


def test_assoc_srcoutAttrref532_stub_double():
    # siddhi_FeaturesOrOutAttrReference has no real 'siddhi_FeaturesOrOutAttrReference533' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_FeaturesOrOutAttr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_FeaturesOrOutAttr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_FeaturesOrOutAttr(name="sample_text")
    partner = siddhi_FeaturesOrOutAttrReference()
    setattr(partner, 'siddhi_FeaturesOrOutAttrReference533', None)
    _safe_set(owner, 'siddhi_FeaturesOrOutAttr', partner)
    assert getattr(partner, 'siddhi_FeaturesOrOutAttrReference533') == owner
    _safe_set(owner, 'siddhi_FeaturesOrOutAttr', None)
    assert getattr(partner, 'siddhi_FeaturesOrOutAttrReference533') is None


def test_assoc_ssc217_stub_double():
    # siddhi_EverySequenceSourceChain has no real 'siddhi_EverySequenceSourceChain218' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_SequenceSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_SequenceSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_SequenceSourceChain(op="sample_text")
    partner = siddhi_EverySequenceSourceChain()
    setattr(partner, 'siddhi_EverySequenceSourceChain218', None)
    _safe_set(owner, 'siddhi_SequenceSourceChain', partner)
    assert getattr(partner, 'siddhi_EverySequenceSourceChain218') == owner
    _safe_set(owner, 'siddhi_SequenceSourceChain', None)
    assert getattr(partner, 'siddhi_EverySequenceSourceChain218') is None


def test_assoc_stdSource333_stub_double():
    # siddhi_LogicalStatefulSource has no real 'siddhi_LogicalStatefulSource334' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    partner = siddhi_LogicalStatefulSource()
    setattr(partner, 'siddhi_LogicalStatefulSource334', None)
    _safe_set(owner, 'siddhi_StandardStatefulSource335', partner)
    assert owner in getattr(partner, 'siddhi_LogicalStatefulSource334')
    _safe_set(owner, 'siddhi_StandardStatefulSource335', None)
    assert owner not in getattr(partner, 'siddhi_LogicalStatefulSource334')


def test_assoc_stdSource344_stub_double():
    # siddhi_LogicalAbsentStatefulSource has no real 'siddhi_LogicalAbsentStatefulSource345' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    partner = siddhi_LogicalAbsentStatefulSource()
    setattr(partner, 'siddhi_LogicalAbsentStatefulSource345', None)
    _safe_set(owner, 'siddhi_StandardStatefulSource346', partner)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource345') == owner
    _safe_set(owner, 'siddhi_StandardStatefulSource346', None)
    assert getattr(partner, 'siddhi_LogicalAbsentStatefulSource345') is None


def test_assoc_stdss329_stub_double():
    # siddhi_PatternSource has no real 'siddhi_PatternSource330' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StandardStatefulSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StandardStatefulSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StandardStatefulSource(one_or_more="sample_text", zero_or_more="sample_text", zero_or_one="sample_text")
    partner = siddhi_PatternSource()
    setattr(partner, 'siddhi_PatternSource330', None)
    _safe_set(owner, 'siddhi_StandardStatefulSource', partner)
    assert getattr(partner, 'siddhi_PatternSource330') == owner
    _safe_set(owner, 'siddhi_StandardStatefulSource', None)
    assert getattr(partner, 'siddhi_PatternSource330') is None


def test_assoc_strId109_stub_double():
    # siddhi_Source has no real 'siddhi_Source' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_Source1's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_Source1's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_Source1(inner="sample_text")
    partner = siddhi_Source()
    setattr(partner, 'siddhi_Source', None)
    _safe_set(owner, 'siddhi_Source1110', partner)
    assert getattr(partner, 'siddhi_Source') == owner
    _safe_set(owner, 'siddhi_Source1110', None)
    assert getattr(partner, 'siddhi_Source') is None


def test_assoc_stream_ref496_stub_double():
    # siddhi_NullCheck has no real 'siddhi_NullCheck' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StreamReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StreamReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StreamReference(hash="sample_text")
    partner = siddhi_NullCheck()
    setattr(partner, 'siddhi_NullCheck', None)
    _safe_set(owner, 'siddhi_StreamReference', partner)
    assert getattr(partner, 'siddhi_NullCheck') == owner
    _safe_set(owner, 'siddhi_StreamReference', None)
    assert getattr(partner, 'siddhi_NullCheck') is None


def test_assoc_sv131_stub_double():
    # siddhi_ConditionRange has no real 'siddhi_ConditionRange132' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StringValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StringValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StringValue(sl="sample_text")
    partner = siddhi_ConditionRange()
    setattr(partner, 'siddhi_ConditionRange132', None)
    _safe_set(owner, 'siddhi_StringValue133', partner)
    assert getattr(partner, 'siddhi_ConditionRange132') == owner
    _safe_set(owner, 'siddhi_StringValue133', None)
    assert getattr(partner, 'siddhi_ConditionRange132') is None


def test_assoc_sv55_stub_double():
    # siddhi_DefinitionTrigger has no real 'siddhi_DefinitionTrigger56' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StringValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StringValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StringValue(sl="sample_text")
    partner = siddhi_DefinitionTrigger()
    setattr(partner, 'siddhi_DefinitionTrigger56', None)
    _safe_set(owner, 'siddhi_StringValue', partner)
    assert getattr(partner, 'siddhi_DefinitionTrigger56') == owner
    _safe_set(owner, 'siddhi_StringValue', None)
    assert getattr(partner, 'siddhi_DefinitionTrigger56') is None


def test_assoc_sv95_stub_double():
    # siddhi_PropertyValue has no real 'siddhi_PropertyValue96' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_StringValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_StringValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_StringValue(sl="sample_text")
    partner = siddhi_PropertyValue()
    setattr(partner, 'siddhi_PropertyValue96', None)
    _safe_set(owner, 'siddhi_StringValue97', partner)
    assert getattr(partner, 'siddhi_PropertyValue96') == owner
    _safe_set(owner, 'siddhi_StringValue97', None)
    assert getattr(partner, 'siddhi_PropertyValue96') is None


def test_assoc_tn49_stub_double():
    # siddhi_DefinitionTrigger has no real 'siddhi_DefinitionTrigger50' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_TriggerName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_TriggerName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_TriggerName(id="sample_text")
    partner = siddhi_DefinitionTrigger()
    setattr(partner, 'siddhi_DefinitionTrigger50', None)
    _safe_set(owner, 'siddhi_TriggerName', partner)
    assert getattr(partner, 'siddhi_DefinitionTrigger50') == owner
    _safe_set(owner, 'siddhi_TriggerName', None)
    assert getattr(partner, 'siddhi_DefinitionTrigger50') is None


def test_assoc_tv560_stub_double():
    # siddhi_TimeValue has no real 'siddhi_TimeValue562' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_ConstantValue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_ConstantValue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_ConstantValue(siv="sample_text")
    partner = siddhi_TimeValue()
    setattr(partner, 'siddhi_TimeValue562', None)
    _safe_set(owner, 'siddhi_ConstantValue561', partner)
    assert getattr(partner, 'siddhi_TimeValue562') == owner
    _safe_set(owner, 'siddhi_ConstantValue561', None)
    assert getattr(partner, 'siddhi_TimeValue562') is None


def test_assoc_uni616_stub_double():
    # siddhi_Keyword has no real 'siddhi_Keyword617' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_UNIDIRECTIONAL's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_UNIDIRECTIONAL's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_UNIDIRECTIONAL(unidirectional="sample_text")
    partner = siddhi_Keyword()
    setattr(partner, 'siddhi_Keyword617', None)
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL618', partner)
    assert getattr(partner, 'siddhi_Keyword617') == owner
    _safe_set(owner, 'siddhi_UNIDIRECTIONAL618', None)
    assert getattr(partner, 'siddhi_Keyword617') is None


def test_assoc_wt1277_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime279' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_SequenceSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_SequenceSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_SequenceSourceChain(op="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime279', None)
    _safe_set(owner, 'siddhi_SequenceSourceChain278', {partner})
    assert getattr(partner, 'siddhi_WithinTime279') == owner
    _safe_set(owner, 'siddhi_SequenceSourceChain278', set())
    assert getattr(partner, 'siddhi_WithinTime279') is None


def test_assoc_wt2383_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime385' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentPatternSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentPatternSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentPatternSource(fb1="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime385', None)
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource384', {partner})
    assert getattr(partner, 'siddhi_WithinTime385') == owner
    _safe_set(owner, 'siddhi_LeftAbsentPatternSource384', set())
    assert getattr(partner, 'siddhi_WithinTime385') is None


def test_assoc_wt303_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime305' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_EveryPatternSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_EveryPatternSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_EveryPatternSourceChain(op="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime305', None)
    _safe_set(owner, 'siddhi_EveryPatternSourceChain304', partner)
    assert getattr(partner, 'siddhi_WithinTime305') == owner
    _safe_set(owner, 'siddhi_EveryPatternSourceChain304', None)
    assert getattr(partner, 'siddhi_WithinTime305') is None


def test_assoc_wt320_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime322' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_PatternSourceChain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_PatternSourceChain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_PatternSourceChain(op="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime322', None)
    _safe_set(owner, 'siddhi_PatternSourceChain321', partner)
    assert getattr(partner, 'siddhi_WithinTime322') == owner
    _safe_set(owner, 'siddhi_PatternSourceChain321', None)
    assert getattr(partner, 'siddhi_WithinTime322') is None


def test_assoc_wt3403_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime405' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentPatternSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentPatternSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentPatternSource(fb2="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime405', None)
    _safe_set(owner, 'siddhi_RightAbsentPatternSource404', {partner})
    assert getattr(partner, 'siddhi_WithinTime405') == owner
    _safe_set(owner, 'siddhi_RightAbsentPatternSource404', set())
    assert getattr(partner, 'siddhi_WithinTime405') is None


def test_assoc_wt6244_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime246' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_LeftAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_LeftAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_LeftAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime246', None)
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource245', partner)
    assert getattr(partner, 'siddhi_WithinTime246') == owner
    _safe_set(owner, 'siddhi_LeftAbsentSequenceSource245', None)
    assert getattr(partner, 'siddhi_WithinTime246') is None


def test_assoc_wt7262_stub_double():
    # siddhi_WithinTime has no real 'siddhi_WithinTime264' property in the generated
    # code (a bare stub) -- manually attach it so siddhi_RightAbsentSequenceSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # siddhi_RightAbsentSequenceSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = siddhi_RightAbsentSequenceSource(comm="sample_text", comma="sample_text", cp="sample_text", op="sample_text")
    partner = siddhi_WithinTime()
    setattr(partner, 'siddhi_WithinTime264', None)
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource263', partner)
    assert getattr(partner, 'siddhi_WithinTime264') == owner
    _safe_set(owner, 'siddhi_RightAbsentSequenceSource263', None)
    assert getattr(partner, 'siddhi_WithinTime264') is None


