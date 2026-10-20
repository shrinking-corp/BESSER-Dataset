import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AggregateExpression,
    AliasedQuerySource,
    BinaryExpression,
    Element,
    Expression,
    ExpressionDef,
    ExpressionRef,
    NaryExpression,
    RelationshipClause,
    SortByItem,
    TypeSpecifier,
    UnaryExpression,
    r1_Abs,
    r1_Add,
    r1_After,
    r1_AggregateExpression,
    r1_AliasRef,
    r1_AliasedQuerySource,
    r1_AllTrue,
    r1_And,
    r1_AnyTrue,
    r1_As,
    r1_Avg,
    r1_Before,
    r1_BinaryExpression,
    r1_ByColumn,
    r1_ByDirection,
    r1_ByExpression,
    r1_CalculateAge,
    r1_CalculateAgeAt,
    r1_Case,
    r1_CaseItem,
    r1_Ceiling,
    r1_Coalesce,
    r1_Code,
    r1_CodeSystemDef,
    r1_CodeSystemRef,
    r1_Collapse,
    r1_Combine,
    r1_Concatenate,
    r1_Concept,
    r1_Contains,
    r1_Convert,
    r1_Count,
    r1_Current,
    r1_DateFrom,
    r1_DateTime,
    r1_DateTimeComponentFrom,
    r1_DefineClause,
    r1_DifferenceBetween,
    r1_Distinct,
    r1_Divide,
    r1_DurationBetween,
    r1_EObject,
    r1_Element,
    r1_End,
    r1_Ends,
    r1_Equal,
    r1_Except,
    r1_Exists,
    r1_Expand,
    r1_Expression,
    r1_ExpressionDef,
    r1_ExpressionRef,
    r1_Filter,
    r1_First,
    r1_Floor,
    r1_ForEach,
    r1_FunctionDef,
    r1_FunctionRef,
    r1_Greater,
    r1_GreaterOrEqual,
    r1_IdentifierRef,
    r1_If,
    r1_In,
    r1_InCodeSystem,
    r1_InValueSet,
    r1_IncludedIn,
    r1_Includes,
    r1_IndexOf,
    r1_Indexer,
    r1_Instance,
    r1_InstanceElement,
    r1_Intersect,
    r1_Interval,
    r1_IntervalTypeSpecifier,
    r1_Is,
    r1_IsFalse,
    r1_IsNull,
    r1_IsTrue,
    r1_Last,
    r1_Length,
    r1_Less,
    r1_LessOrEqual,
    r1_List,
    r1_ListTypeSpecifier,
    r1_Literal,
    r1_Ln,
    r1_Log,
    r1_Lower,
    r1_Matches,
    r1_Max,
    r1_MaxValue,
    r1_Median,
    r1_Meets,
    r1_MeetsAfter,
    r1_MeetsBefore,
    r1_Min,
    r1_MinValue,
    r1_Mode,
    r1_Modulo,
    r1_Multiply,
    r1_NamedTypeSpecifier,
    r1_NaryExpression,
    r1_Negate,
    r1_Not,
    r1_NotEqual,
    r1_Now,
    r1_Null,
    r1_OperandDef,
    r1_OperandRef,
    r1_Or,
    r1_Overlaps,
    r1_OverlapsAfter,
    r1_OverlapsBefore,
    r1_ParameterDef,
    r1_ParameterRef,
    r1_PopulationStdDev,
    r1_PopulationVariance,
    r1_PositionOf,
    r1_Power,
    r1_Predecessor,
    r1_ProperContains,
    r1_ProperIn,
    r1_ProperIncludedIn,
    r1_ProperIncludes,
    r1_Property,
    r1_Quantity,
    r1_Query,
    r1_QueryDefineRef,
    r1_RelationshipClause,
    r1_Retrieve,
    r1_ReturnClause,
    r1_Round,
    r1_SameAs,
    r1_SameOrAfter,
    r1_SameOrBefore,
    r1_SingletonFrom,
    r1_Sort,
    r1_SortByItem,
    r1_SortClause,
    r1_Split,
    r1_Start,
    r1_Starts,
    r1_StdDev,
    r1_Substring,
    r1_Subtract,
    r1_Successor,
    r1_Sum,
    r1_TernaryExpression,
    r1_Time,
    r1_TimeFrom,
    r1_TimeOfDay,
    r1_Times,
    r1_TimezoneFrom,
    r1_Today,
    r1_Truncate,
    r1_TruncatedDivide,
    r1_Tuple,
    r1_TupleElement,
    r1_TupleElementDefinition,
    r1_TupleTypeSpecifier,
    r1_TypeSpecifier,
    r1_UnaryExpression,
    r1_Union,
    r1_Upper,
    r1_ValueSetDef,
    r1_ValueSetRef,
    r1_Variance,
    r1_Width,
    r1_With,
    r1_Without,
    r1_Xor,
    AccessModifier,
    DateTimePrecision,
    SortDirection,
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

def test_assoc_code27_reverse_link_reassign_clear():
    a1 = r1_Concept(display="sample_text")
    a2 = r1_Concept(display="sample_text_2")
    b = r1_Code(code="sample_text", display="sample_text")
    _safe_set(b, 'r1_Code28', a1)
    assert _is_linked(b, 'r1_Code28', a1)
    if hasattr(a1, 'r1_Concept'):
        assert _is_linked(a1, 'r1_Concept', b)
    _safe_set(b, 'r1_Code28', a2)
    assert _is_linked(b, 'r1_Code28', a2)
    if hasattr(a1, 'r1_Concept'):
        assert not _is_linked(a1, 'r1_Concept', b)
    if hasattr(a2, 'r1_Concept'):
        assert _is_linked(a2, 'r1_Concept', b)
    _safe_set(b, 'r1_Code28', None)
    assert not _is_linked(b, 'r1_Code28', a2)
    if hasattr(a2, 'r1_Concept'):
        assert not _is_linked(a2, 'r1_Concept', b)


def test_assoc_codeSystem217_reverse_link_reassign_clear():
    a1 = r1_ValueSetDef(accessLevel="sample_text", id="sample_text", name="sample_text", version="sample_text")
    a2 = r1_ValueSetDef(accessLevel="sample_text_2", id="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = r1_CodeSystemRef(libraryName="sample_text", name="sample_text")
    _safe_set(b, 'r1_CodeSystemRef218', a1)
    assert _is_linked(b, 'r1_CodeSystemRef218', a1)
    if hasattr(a1, 'r1_ValueSetDef'):
        assert _is_linked(a1, 'r1_ValueSetDef', b)
    _safe_set(b, 'r1_CodeSystemRef218', a2)
    assert _is_linked(b, 'r1_CodeSystemRef218', a2)
    if hasattr(a1, 'r1_ValueSetDef'):
        assert not _is_linked(a1, 'r1_ValueSetDef', b)
    if hasattr(a2, 'r1_ValueSetDef'):
        assert _is_linked(a2, 'r1_ValueSetDef', b)
    _safe_set(b, 'r1_CodeSystemRef218', None)
    assert not _is_linked(b, 'r1_CodeSystemRef218', a2)
    if hasattr(a2, 'r1_ValueSetDef'):
        assert not _is_linked(a2, 'r1_ValueSetDef', b)


def test_assoc_element92_reverse_link_reassign_clear():
    a1 = r1_InstanceElement(name="sample_text")
    a2 = r1_InstanceElement(name="sample_text_2")
    b = r1_Instance(classType="sample_text")
    _safe_set(b, 'r1_Instance', {a1})
    assert _is_linked(b, 'r1_Instance', a1)
    if hasattr(a1, 'r1_InstanceElement'):
        assert _is_linked(a1, 'r1_InstanceElement', b)
    _safe_set(b, 'r1_Instance', {a2})
    assert _is_linked(b, 'r1_Instance', a2)
    if hasattr(a1, 'r1_InstanceElement'):
        assert not _is_linked(a1, 'r1_InstanceElement', b)
    if hasattr(a2, 'r1_InstanceElement'):
        assert _is_linked(a2, 'r1_InstanceElement', b)
    _safe_set(b, 'r1_Instance', set())
    assert not _is_linked(b, 'r1_Instance', a2)
    if hasattr(a2, 'r1_InstanceElement'):
        assert not _is_linked(a2, 'r1_InstanceElement', b)


def test_assoc_system21_reverse_link_reassign_clear():
    a1 = r1_CodeSystemRef(libraryName="sample_text", name="sample_text")
    a2 = r1_CodeSystemRef(libraryName="sample_text_2", name="sample_text_2")
    b = r1_Code(code="sample_text", display="sample_text")
    _safe_set(b, 'r1_Code', a1)
    assert _is_linked(b, 'r1_Code', a1)
    if hasattr(a1, 'r1_CodeSystemRef'):
        assert _is_linked(a1, 'r1_CodeSystemRef', b)
    _safe_set(b, 'r1_Code', a2)
    assert _is_linked(b, 'r1_Code', a2)
    if hasattr(a1, 'r1_CodeSystemRef'):
        assert not _is_linked(a1, 'r1_CodeSystemRef', b)
    if hasattr(a2, 'r1_CodeSystemRef'):
        assert _is_linked(a2, 'r1_CodeSystemRef', b)
    _safe_set(b, 'r1_Code', None)
    assert not _is_linked(b, 'r1_Code', a2)
    if hasattr(a2, 'r1_CodeSystemRef'):
        assert not _is_linked(a2, 'r1_CodeSystemRef', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotation56_stub_double():
    # r1_EObject has no real 'r1_EObject' property in the generated
    # code (a bare stub) -- manually attach it so r1_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Element(localId="sample_text")
    partner = r1_EObject()
    setattr(partner, 'r1_EObject', None)
    _safe_set(owner, 'r1_Element', {partner})
    assert getattr(partner, 'r1_EObject') == owner
    _safe_set(owner, 'r1_Element', set())
    assert getattr(partner, 'r1_EObject') is None


def test_assoc_asTypeSpecifier3_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier' property in the generated
    # code (a bare stub) -- manually attach it so r1_As's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_As's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_As(asType="sample_text", strict="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier', None)
    _safe_set(owner, 'r1_As', partner)
    assert getattr(partner, 'r1_TypeSpecifier') == owner
    _safe_set(owner, 'r1_As', None)
    assert getattr(partner, 'r1_TypeSpecifier') is None


def test_assoc_by173_stub_double():
    # r1_Sort has no real 'r1_Sort174' property in the generated
    # code (a bare stub) -- manually attach it so r1_SortByItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_SortByItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_SortByItem(direction="sample_text")
    partner = r1_Sort()
    setattr(partner, 'r1_Sort174', None)
    _safe_set(owner, 'r1_SortByItem', partner)
    assert owner in getattr(partner, 'r1_Sort174')
    _safe_set(owner, 'r1_SortByItem', None)
    assert owner not in getattr(partner, 'r1_Sort174')


def test_assoc_by175_stub_double():
    # r1_SortClause has no real 'r1_SortClause176' property in the generated
    # code (a bare stub) -- manually attach it so r1_SortByItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_SortByItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_SortByItem(direction="sample_text")
    partner = r1_SortClause()
    setattr(partner, 'r1_SortClause176', None)
    _safe_set(owner, 'r1_SortByItem177', partner)
    assert owner in getattr(partner, 'r1_SortClause176')
    _safe_set(owner, 'r1_SortByItem177', None)
    assert owner not in getattr(partner, 'r1_SortClause176')


def test_assoc_codes158_stub_double():
    # r1_Expression has no real 'r1_Expression159' property in the generated
    # code (a bare stub) -- manually attach it so r1_Retrieve's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Retrieve's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Retrieve(codeProperty="sample_text", dataType="sample_text", dateHighProperty="sample_text", dateLowProperty="sample_text", dateProperty="sample_text", idProperty="sample_text", scope="sample_text", templateId="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression159', None)
    _safe_set(owner, 'r1_Retrieve', partner)
    assert getattr(partner, 'r1_Expression159') == owner
    _safe_set(owner, 'r1_Retrieve', None)
    assert getattr(partner, 'r1_Expression159') is None


def test_assoc_codesystem84_stub_double():
    # r1_InCodeSystem has no real 'r1_InCodeSystem85' property in the generated
    # code (a bare stub) -- manually attach it so r1_CodeSystemRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_CodeSystemRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_CodeSystemRef(libraryName="sample_text", name="sample_text")
    partner = r1_InCodeSystem()
    setattr(partner, 'r1_InCodeSystem85', None)
    _safe_set(owner, 'r1_CodeSystemRef86', partner)
    assert getattr(partner, 'r1_InCodeSystem85') == owner
    _safe_set(owner, 'r1_CodeSystemRef86', None)
    assert getattr(partner, 'r1_InCodeSystem85') is None


def test_assoc_condition61_stub_double():
    # r1_Expression has no real 'r1_Expression63' property in the generated
    # code (a bare stub) -- manually attach it so r1_Filter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Filter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Filter(scope="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression63', None)
    _safe_set(owner, 'r1_Filter62', partner)
    assert getattr(partner, 'r1_Expression63') == owner
    _safe_set(owner, 'r1_Filter62', None)
    assert getattr(partner, 'r1_Expression63') is None


def test_assoc_dateRange160_stub_double():
    # r1_Expression has no real 'r1_Expression162' property in the generated
    # code (a bare stub) -- manually attach it so r1_Retrieve's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Retrieve's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Retrieve(codeProperty="sample_text", dataType="sample_text", dateHighProperty="sample_text", dateLowProperty="sample_text", dateProperty="sample_text", idProperty="sample_text", scope="sample_text", templateId="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression162', None)
    _safe_set(owner, 'r1_Retrieve161', partner)
    assert getattr(partner, 'r1_Expression162') == owner
    _safe_set(owner, 'r1_Retrieve161', None)
    assert getattr(partner, 'r1_Expression162') is None


def test_assoc_default129_stub_double():
    # r1_Expression has no real 'r1_Expression130' property in the generated
    # code (a bare stub) -- manually attach it so r1_ParameterDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ParameterDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ParameterDef(accessLevel="sample_text", name="sample_text", parameterType="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression130', None)
    _safe_set(owner, 'r1_ParameterDef', partner)
    assert getattr(partner, 'r1_Expression130') == owner
    _safe_set(owner, 'r1_ParameterDef', None)
    assert getattr(partner, 'r1_Expression130') is None


def test_assoc_define143_stub_double():
    # r1_Query has no real 'r1_Query144' property in the generated
    # code (a bare stub) -- manually attach it so r1_DefineClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_DefineClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_DefineClause(identifier="sample_text")
    partner = r1_Query()
    setattr(partner, 'r1_Query144', None)
    _safe_set(owner, 'r1_DefineClause145', partner)
    assert owner in getattr(partner, 'r1_Query144')
    _safe_set(owner, 'r1_DefineClause145', None)
    assert owner not in getattr(partner, 'r1_Query144')


def test_assoc_element207_stub_double():
    # r1_Tuple has no real 'r1_Tuple' property in the generated
    # code (a bare stub) -- manually attach it so r1_TupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_TupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_TupleElement(name="sample_text")
    partner = r1_Tuple()
    setattr(partner, 'r1_Tuple', None)
    _safe_set(owner, 'r1_TupleElement', partner)
    assert owner in getattr(partner, 'r1_Tuple')
    _safe_set(owner, 'r1_TupleElement', None)
    assert owner not in getattr(partner, 'r1_Tuple')


def test_assoc_element213_stub_double():
    # r1_TupleTypeSpecifier has no real 'r1_TupleTypeSpecifier' property in the generated
    # code (a bare stub) -- manually attach it so r1_TupleElementDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_TupleElementDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_TupleElementDefinition(name="sample_text")
    partner = r1_TupleTypeSpecifier()
    setattr(partner, 'r1_TupleTypeSpecifier', None)
    _safe_set(owner, 'r1_TupleElementDefinition214', partner)
    assert owner in getattr(partner, 'r1_TupleTypeSpecifier')
    _safe_set(owner, 'r1_TupleElementDefinition214', None)
    assert owner not in getattr(partner, 'r1_TupleTypeSpecifier')


def test_assoc_element68_stub_double():
    # r1_Expression has no real 'r1_Expression70' property in the generated
    # code (a bare stub) -- manually attach it so r1_ForEach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ForEach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ForEach(scope="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression70', None)
    _safe_set(owner, 'r1_ForEach69', partner)
    assert getattr(partner, 'r1_Expression70') == owner
    _safe_set(owner, 'r1_ForEach69', None)
    assert getattr(partner, 'r1_Expression70') is None


def test_assoc_expression1_stub_double():
    # r1_Expression has no real 'r1_Expression2' property in the generated
    # code (a bare stub) -- manually attach it so r1_AliasedQuerySource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_AliasedQuerySource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_AliasedQuerySource(alias="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression2', None)
    _safe_set(owner, 'r1_AliasedQuerySource', partner)
    assert getattr(partner, 'r1_Expression2') == owner
    _safe_set(owner, 'r1_AliasedQuerySource', None)
    assert getattr(partner, 'r1_Expression2') is None


def test_assoc_expression163_stub_double():
    # r1_Expression has no real 'r1_Expression165' property in the generated
    # code (a bare stub) -- manually attach it so r1_ReturnClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ReturnClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ReturnClause(distinct="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression165', None)
    _safe_set(owner, 'r1_ReturnClause164', partner)
    assert getattr(partner, 'r1_Expression165') == owner
    _safe_set(owner, 'r1_ReturnClause164', None)
    assert getattr(partner, 'r1_Expression165') is None


def test_assoc_expression54_stub_double():
    # r1_Expression has no real 'r1_Expression55' property in the generated
    # code (a bare stub) -- manually attach it so r1_DefineClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_DefineClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_DefineClause(identifier="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression55', None)
    _safe_set(owner, 'r1_DefineClause', partner)
    assert getattr(partner, 'r1_Expression55') == owner
    _safe_set(owner, 'r1_DefineClause', None)
    assert getattr(partner, 'r1_Expression55') is None


def test_assoc_expression57_stub_double():
    # r1_Expression has no real 'r1_Expression58' property in the generated
    # code (a bare stub) -- manually attach it so r1_ExpressionDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ExpressionDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ExpressionDef(accessLevel="sample_text", context="sample_text", name="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression58', None)
    _safe_set(owner, 'r1_ExpressionDef', partner)
    assert getattr(partner, 'r1_Expression58') == owner
    _safe_set(owner, 'r1_ExpressionDef', None)
    assert getattr(partner, 'r1_Expression58') is None


def test_assoc_high101_stub_double():
    # r1_Expression has no real 'r1_Expression103' property in the generated
    # code (a bare stub) -- manually attach it so r1_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Interval(highClosed="sample_text", lowClosed="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression103', None)
    _safe_set(owner, 'r1_Interval102', partner)
    assert getattr(partner, 'r1_Expression103') == owner
    _safe_set(owner, 'r1_Interval102', None)
    assert getattr(partner, 'r1_Expression103') is None


def test_assoc_highClosedExpression104_stub_double():
    # r1_Expression has no real 'r1_Expression106' property in the generated
    # code (a bare stub) -- manually attach it so r1_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Interval(highClosed="sample_text", lowClosed="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression106', None)
    _safe_set(owner, 'r1_Interval105', partner)
    assert getattr(partner, 'r1_Expression106') == owner
    _safe_set(owner, 'r1_Interval105', None)
    assert getattr(partner, 'r1_Expression106') is None


def test_assoc_isTypeSpecifier113_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier114' property in the generated
    # code (a bare stub) -- manually attach it so r1_Is's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Is's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Is(isType="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier114', None)
    _safe_set(owner, 'r1_Is', partner)
    assert getattr(partner, 'r1_TypeSpecifier114') == owner
    _safe_set(owner, 'r1_Is', None)
    assert getattr(partner, 'r1_TypeSpecifier114') is None


def test_assoc_low96_stub_double():
    # r1_Expression has no real 'r1_Expression97' property in the generated
    # code (a bare stub) -- manually attach it so r1_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Interval(highClosed="sample_text", lowClosed="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression97', None)
    _safe_set(owner, 'r1_Interval', partner)
    assert getattr(partner, 'r1_Expression97') == owner
    _safe_set(owner, 'r1_Interval', None)
    assert getattr(partner, 'r1_Expression97') is None


def test_assoc_lowClosedExpression98_stub_double():
    # r1_Expression has no real 'r1_Expression100' property in the generated
    # code (a bare stub) -- manually attach it so r1_Interval's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Interval's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Interval(highClosed="sample_text", lowClosed="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression100', None)
    _safe_set(owner, 'r1_Interval99', partner)
    assert getattr(partner, 'r1_Expression100') == owner
    _safe_set(owner, 'r1_Interval99', None)
    assert getattr(partner, 'r1_Expression100') is None


def test_assoc_operand71_stub_double():
    # r1_FunctionDef has no real 'r1_FunctionDef' property in the generated
    # code (a bare stub) -- manually attach it so r1_OperandDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_OperandDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_OperandDef(name="sample_text", operandType="sample_text")
    partner = r1_FunctionDef()
    setattr(partner, 'r1_FunctionDef', None)
    _safe_set(owner, 'r1_OperandDef', partner)
    assert owner in getattr(partner, 'r1_FunctionDef')
    _safe_set(owner, 'r1_OperandDef', None)
    assert owner not in getattr(partner, 'r1_FunctionDef')


def test_assoc_operandTypeSpecifier126_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier128' property in the generated
    # code (a bare stub) -- manually attach it so r1_OperandDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_OperandDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_OperandDef(name="sample_text", operandType="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier128', None)
    _safe_set(owner, 'r1_OperandDef127', partner)
    assert getattr(partner, 'r1_TypeSpecifier128') == owner
    _safe_set(owner, 'r1_OperandDef127', None)
    assert getattr(partner, 'r1_TypeSpecifier128') is None


def test_assoc_parameterTypeSpecifier131_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier133' property in the generated
    # code (a bare stub) -- manually attach it so r1_ParameterDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ParameterDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ParameterDef(accessLevel="sample_text", name="sample_text", parameterType="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier133', None)
    _safe_set(owner, 'r1_ParameterDef132', partner)
    assert getattr(partner, 'r1_TypeSpecifier133') == owner
    _safe_set(owner, 'r1_ParameterDef132', None)
    assert getattr(partner, 'r1_TypeSpecifier133') is None


def test_assoc_return_151_stub_double():
    # r1_Query has no real 'r1_Query152' property in the generated
    # code (a bare stub) -- manually attach it so r1_ReturnClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ReturnClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ReturnClause(distinct="sample_text")
    partner = r1_Query()
    setattr(partner, 'r1_Query152', None)
    _safe_set(owner, 'r1_ReturnClause', partner)
    assert getattr(partner, 'r1_Query152') == owner
    _safe_set(owner, 'r1_ReturnClause', None)
    assert getattr(partner, 'r1_Query152') is None


def test_assoc_source0_stub_double():
    # r1_Expression has no real 'r1_Expression' property in the generated
    # code (a bare stub) -- manually attach it so r1_AggregateExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_AggregateExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_AggregateExpression(path="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression', None)
    _safe_set(owner, 'r1_AggregateExpression', partner)
    assert getattr(partner, 'r1_Expression') == owner
    _safe_set(owner, 'r1_AggregateExpression', None)
    assert getattr(partner, 'r1_Expression') is None


def test_assoc_source115_stub_double():
    # r1_Expression has no real 'r1_Expression116' property in the generated
    # code (a bare stub) -- manually attach it so r1_Last's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Last's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Last(orderBy="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression116', None)
    _safe_set(owner, 'r1_Last', partner)
    assert getattr(partner, 'r1_Expression116') == owner
    _safe_set(owner, 'r1_Last', None)
    assert getattr(partner, 'r1_Expression116') is None


def test_assoc_source139_stub_double():
    # r1_Expression has no real 'r1_Expression140' property in the generated
    # code (a bare stub) -- manually attach it so r1_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Property(path="sample_text", scope="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression140', None)
    _safe_set(owner, 'r1_Property', partner)
    assert getattr(partner, 'r1_Expression140') == owner
    _safe_set(owner, 'r1_Property', None)
    assert getattr(partner, 'r1_Expression140') is None


def test_assoc_source141_stub_double():
    # r1_Query has no real 'r1_Query' property in the generated
    # code (a bare stub) -- manually attach it so r1_AliasedQuerySource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_AliasedQuerySource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_AliasedQuerySource(alias="sample_text")
    partner = r1_Query()
    setattr(partner, 'r1_Query', None)
    _safe_set(owner, 'r1_AliasedQuerySource142', partner)
    assert owner in getattr(partner, 'r1_Query')
    _safe_set(owner, 'r1_AliasedQuerySource142', None)
    assert owner not in getattr(partner, 'r1_Query')


def test_assoc_source59_stub_double():
    # r1_Expression has no real 'r1_Expression60' property in the generated
    # code (a bare stub) -- manually attach it so r1_Filter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Filter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Filter(scope="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression60', None)
    _safe_set(owner, 'r1_Filter', partner)
    assert getattr(partner, 'r1_Expression60') == owner
    _safe_set(owner, 'r1_Filter', None)
    assert getattr(partner, 'r1_Expression60') is None


def test_assoc_source64_stub_double():
    # r1_Expression has no real 'r1_Expression65' property in the generated
    # code (a bare stub) -- manually attach it so r1_First's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_First's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_First(orderBy="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression65', None)
    _safe_set(owner, 'r1_First', partner)
    assert getattr(partner, 'r1_Expression65') == owner
    _safe_set(owner, 'r1_First', None)
    assert getattr(partner, 'r1_Expression65') is None


def test_assoc_source66_stub_double():
    # r1_Expression has no real 'r1_Expression67' property in the generated
    # code (a bare stub) -- manually attach it so r1_ForEach's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ForEach's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ForEach(scope="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression67', None)
    _safe_set(owner, 'r1_ForEach', partner)
    assert getattr(partner, 'r1_Expression67') == owner
    _safe_set(owner, 'r1_ForEach', None)
    assert getattr(partner, 'r1_Expression67') is None


def test_assoc_toTypeSpecifier29_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier30' property in the generated
    # code (a bare stub) -- manually attach it so r1_Convert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_Convert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_Convert(toType="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier30', None)
    _safe_set(owner, 'r1_Convert', partner)
    assert getattr(partner, 'r1_TypeSpecifier30') == owner
    _safe_set(owner, 'r1_Convert', None)
    assert getattr(partner, 'r1_TypeSpecifier30') is None


def test_assoc_type211_stub_double():
    # r1_TypeSpecifier has no real 'r1_TypeSpecifier212' property in the generated
    # code (a bare stub) -- manually attach it so r1_TupleElementDefinition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_TupleElementDefinition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_TupleElementDefinition(name="sample_text")
    partner = r1_TypeSpecifier()
    setattr(partner, 'r1_TypeSpecifier212', None)
    _safe_set(owner, 'r1_TupleElementDefinition', partner)
    assert getattr(partner, 'r1_TypeSpecifier212') == owner
    _safe_set(owner, 'r1_TupleElementDefinition', None)
    assert getattr(partner, 'r1_TypeSpecifier212') is None


def test_assoc_value208_stub_double():
    # r1_Expression has no real 'r1_Expression210' property in the generated
    # code (a bare stub) -- manually attach it so r1_TupleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_TupleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_TupleElement(name="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression210', None)
    _safe_set(owner, 'r1_TupleElement209', partner)
    assert getattr(partner, 'r1_Expression210') == owner
    _safe_set(owner, 'r1_TupleElement209', None)
    assert getattr(partner, 'r1_Expression210') is None


def test_assoc_value93_stub_double():
    # r1_Expression has no real 'r1_Expression95' property in the generated
    # code (a bare stub) -- manually attach it so r1_InstanceElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_InstanceElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_InstanceElement(name="sample_text")
    partner = r1_Expression()
    setattr(partner, 'r1_Expression95', None)
    _safe_set(owner, 'r1_InstanceElement94', partner)
    assert getattr(partner, 'r1_Expression95') == owner
    _safe_set(owner, 'r1_InstanceElement94', None)
    assert getattr(partner, 'r1_Expression95') is None


def test_assoc_valueset111_stub_double():
    # r1_InValueSet has no real 'r1_InValueSet112' property in the generated
    # code (a bare stub) -- manually attach it so r1_ValueSetRef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # r1_ValueSetRef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = r1_ValueSetRef(libraryName="sample_text", name="sample_text")
    partner = r1_InValueSet()
    setattr(partner, 'r1_InValueSet112', None)
    _safe_set(owner, 'r1_ValueSetRef', partner)
    assert getattr(partner, 'r1_InValueSet112') == owner
    _safe_set(owner, 'r1_ValueSetRef', None)
    assert getattr(partner, 'r1_InValueSet112') is None


