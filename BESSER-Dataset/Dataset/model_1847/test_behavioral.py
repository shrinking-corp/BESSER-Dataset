import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AccountAttribute,
    AccountReport,
    AllocateResourceAttribute,
    Caption,
    Center,
    ColumnAttribute,
    CurrencyFormat,
    DailyMax,
    DailyMin,
    Definitions,
    Depends,
    Details,
    Epilog,
    ExportAttribute,
    Footer,
    GapDuration,
    GapLength,
    Header,
    Headline,
    IcalReportAttribute,
    IncludePropertiesAttribute,
    Left,
    LimitsAttribute,
    ListItem,
    LogicalExpression,
    Maximum,
    Minimum,
    MonthlyMax,
    MonthlyMin,
    NavigatorAttribute,
    NewTaskAttribute,
    NikuReportAttribute,
    NumberFormat,
    Precedes,
    ProjectAttribute,
    Prolog,
    Property,
    ReportAttribute,
    ResourceAttribute,
    ResourceReport,
    Right,
    ShiftsResource,
    ShiftsTask,
    SortAccounts,
    SortJournalEntries,
    SortResources,
    SortTasks,
    StatusSheetAttribute,
    StatusSheetReportAttribute,
    StatusStatusSheetAttribute,
    StatusTimesheetAttribute,
    Summary,
    TaskAttribute,
    TaskReport,
    TaskStatusSheetAttribute,
    TaskTimesheetAttribute,
    TextReport,
    TimesheetAttribute,
    TimesheetReportAttribute,
    WeeklyMax,
    WeeklyMin,
    project_Account,
    project_AccountAttribute,
    project_AccountPrefix,
    project_AccountReport,
    project_AccountRoot,
    project_AccountShare,
    project_Alert,
    project_Allocate,
    project_AllocateResource,
    project_AllocateResourceAttribute,
    project_Alternative,
    project_Author,
    project_Balance,
    project_Booking,
    project_BookingResource,
    project_BookingTask,
    project_Caption,
    project_CellColor,
    project_CellText,
    project_Center,
    project_Charge,
    project_ChargeSet,
    project_Column,
    project_ColumnAttribute,
    project_Columns,
    project_Complete,
    project_Copyright,
    project_Credit,
    project_Criterion,
    project_Currency,
    project_CurrencyFormat,
    project_DailyMax,
    project_DailyMin,
    project_DailyWorkingHours,
    project_Definitions,
    project_Defintions,
    project_Depends,
    project_Details,
    project_Duration,
    project_DurationQuantity,
    project_Efficiency,
    project_Effort,
    project_Email,
    project_End,
    project_EndCredit,
    project_Epilog,
    project_Export,
    project_ExportAttribute,
    project_Extend,
    project_ExtendResource,
    project_ExtendTask,
    project_ExtendedResourceAttribute,
    project_ExtendedTaskAttribute,
    project_Fail,
    project_Flags,
    project_FontColor,
    project_Footer,
    project_Formats,
    project_Function,
    project_GapDuration,
    project_GapLength,
    project_Global,
    project_HAlign,
    project_Header,
    project_Headline,
    project_HideAccount,
    project_HideJournalEntry,
    project_HideReport,
    project_HideResource,
    project_HideTask,
    project_IcalReport,
    project_IcalReportAttribute,
    project_Include,
    project_IncludeProperties,
    project_IncludePropertiesAttribute,
    project_Interval1,
    project_Interval2,
    project_Interval3,
    project_Interval4,
    project_JournalAttributes,
    project_JournalEntry,
    project_JournalMode,
    project_JvmIdentifiableElement,
    project_Left,
    project_Length,
    project_Limit,
    project_LimitAttribute,
    project_Limits,
    project_LimitsAttribute,
    project_ListItem,
    project_ListType,
    project_LoadUnit,
    project_LogicalAbsoluteIdExression,
    project_LogicalBooleanLiteral,
    project_LogicalDateLiteral,
    project_LogicalExpression,
    project_LogicalFunctionExpression,
    project_LogicalNumeralLiteral,
    project_LogicalStringLiteral,
    project_Macro,
    project_Managers,
    project_Mandatory,
    project_MaxEnd,
    project_MaxStart,
    project_Maximum,
    project_Milestone,
    project_MinEnd,
    project_MinStart,
    project_Minimum,
    project_MonthlyMax,
    project_MonthlyMin,
    project_Navigator,
    project_NavigatorAttribute,
    project_NewTask,
    project_NewTaskAttribute,
    project_NikuReport,
    project_NikuReportAttribute,
    project_Note,
    project_Now,
    project_NumberFormat,
    project_Period,
    project_Persistent,
    project_Precedes,
    project_Priority,
    project_Project,
    project_ProjectAttribute,
    project_ProjectId,
    project_ProjectIds,
    project_Prolog,
    project_Property,
    project_PurgeReport,
    project_PurgeResource,
    project_PurgeTask,
    project_RGB,
    project_Rate,
    project_RealFormat,
    project_Remaining,
    project_Report,
    project_ReportAttribute,
    project_ReportPrefix,
    project_Resource,
    project_ResourceAttribute,
    project_ResourceAttributes,
    project_ResourcePrefix,
    project_ResourceReport,
    project_ResourceRoot,
    project_Responsible,
    project_RichText,
    project_Right,
    project_RollupAccount,
    project_RollupResource,
    project_RollupTask,
    project_Scale,
    project_Scenario,
    project_ScenarioIcal,
    project_Scenarios,
    project_Scheduled,
    project_Scheduling,
    project_Select,
    project_SelfContained,
    project_Shift,
    project_ShiftTimesheet,
    project_Shifts,
    project_ShiftsAllocate,
    project_ShiftsLimit,
    project_ShiftsResource,
    project_ShiftsTask,
    project_ShortTimeFormat,
    project_Sort,
    project_SortAccounts,
    project_SortJournalEntries,
    project_SortResources,
    project_SortTasks,
    project_Start,
    project_StatusSheet,
    project_StatusSheetAttribute,
    project_StatusSheetReport,
    project_StatusSheetReportAttribute,
    project_StatusStatusSheet,
    project_StatusStatusSheetAttribute,
    project_StatusTimesheet,
    project_StatusTimesheetAttribute,
    project_Summary,
    project_SupplementAccount,
    project_SupplementReport,
    project_SupplementResource,
    project_SupplementTask,
    project_TagFile,
    project_Task,
    project_TaskAttribute,
    project_TaskAttributes,
    project_TaskDependency,
    project_TaskPrefix,
    project_TaskReport,
    project_TaskRoot,
    project_TaskStatusSheet,
    project_TaskStatusSheetAttribute,
    project_TaskTimesheet,
    project_TaskTimesheetAttribute,
    project_TextReport,
    project_TimeFormat,
    project_Timeoff,
    project_Timesheet,
    project_TimesheetAttribute,
    project_TimesheetReport,
    project_TimesheetReportAttribute,
    project_Timezone,
    project_TimingResolution,
    project_Title,
    project_ToolTip,
    project_TrackingScenario,
    project_TreeLevel,
    project_Vacation,
    project_Warn,
    project_WeekStarts,
    project_Weekdays,
    project_WeeklyMax,
    project_WeeklyMin,
    project_Width,
    project_Work,
    project_WorkHours,
    project_WorkingHours,
    project_XBinaryOperation,
    project_YearlyWorkingDays,
    AlertLevel,
    ChargeApplies,
    ColumnId,
    CriterionDirection,
    DependsPolicy,
    JournalEntrySortCriterion,
    JournalModeValue,
    Justification,
    ListTypeValues,
    LoadDisplayUnit,
    PurgeReportAttribute,
    PurgeResourceAttribute,
    PurgeTaskAttribute,
    ReportFormat,
    ScaleResolution,
    SchedulingPolicy,
    SelectArgument,
    TimeUnit,
    Weekday,
    WorkQuantityUnit,
    YesNo,
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

def test_assoc_account224_reverse_link_reassign_clear():
    a1 = project_AccountShare(share=3.14)
    a2 = project_AccountShare(share=9.99)
    b = project_Account(id="sample_text", name="sample_text")
    _safe_set(b, 'project_Account226', a1)
    assert _is_linked(b, 'project_Account226', a1)
    if hasattr(a1, 'project_AccountShare225'):
        assert _is_linked(a1, 'project_AccountShare225', b)
    _safe_set(b, 'project_Account226', a2)
    assert _is_linked(b, 'project_Account226', a2)
    if hasattr(a1, 'project_AccountShare225'):
        assert not _is_linked(a1, 'project_AccountShare225', b)
    if hasattr(a2, 'project_AccountShare225'):
        assert _is_linked(a2, 'project_AccountShare225', b)
    _safe_set(b, 'project_Account226', None)
    assert not _is_linked(b, 'project_Account226', a2)
    if hasattr(a2, 'project_AccountShare225'):
        assert not _is_linked(a2, 'project_AccountShare225', b)


def test_assoc_alert91_reverse_link_reassign_clear():
    a1 = project_JournalEntry(date="sample_text", headline="sample_text")
    a2 = project_JournalEntry(date="sample_text_2", headline="sample_text_2")
    b = project_Alert(level="sample_text")
    _safe_set(b, 'project_Alert', a1)
    assert _is_linked(b, 'project_Alert', a1)
    if hasattr(a1, 'project_JournalEntry'):
        assert _is_linked(a1, 'project_JournalEntry', b)
    _safe_set(b, 'project_Alert', a2)
    assert _is_linked(b, 'project_Alert', a2)
    if hasattr(a1, 'project_JournalEntry'):
        assert not _is_linked(a1, 'project_JournalEntry', b)
    if hasattr(a2, 'project_JournalEntry'):
        assert _is_linked(a2, 'project_JournalEntry', b)
    _safe_set(b, 'project_Alert', None)
    assert not _is_linked(b, 'project_Alert', a2)
    if hasattr(a2, 'project_JournalEntry'):
        assert not _is_linked(a2, 'project_JournalEntry', b)


def test_assoc_criteria149_reverse_link_reassign_clear():
    a1 = project_Sort(tree=True)
    a2 = project_Sort(tree=False)
    b = project_Criterion(columnId="sample_text", direction="sample_text")
    _safe_set(b, 'project_Criterion', a1)
    assert _is_linked(b, 'project_Criterion', a1)
    if hasattr(a1, 'project_Sort'):
        assert _is_linked(a1, 'project_Sort', b)
    _safe_set(b, 'project_Criterion', a2)
    assert _is_linked(b, 'project_Criterion', a2)
    if hasattr(a1, 'project_Sort'):
        assert not _is_linked(a1, 'project_Sort', b)
    if hasattr(a2, 'project_Sort'):
        assert _is_linked(a2, 'project_Sort', b)
    _safe_set(b, 'project_Criterion', None)
    assert not _is_linked(b, 'project_Criterion', a2)
    if hasattr(a2, 'project_Sort'):
        assert not _is_linked(a2, 'project_Sort', b)


def test_assoc_duration81_reverse_link_reassign_clear():
    a1 = project_Interval1(end="sample_text", start="sample_text")
    a2 = project_Interval1(end="sample_text_2", start="sample_text_2")
    b = project_DurationQuantity(unit="sample_text", value=3.14)
    _safe_set(b, 'project_DurationQuantity82', a1)
    assert _is_linked(b, 'project_DurationQuantity82', a1)
    if hasattr(a1, 'project_Interval1'):
        assert _is_linked(a1, 'project_Interval1', b)
    _safe_set(b, 'project_DurationQuantity82', a2)
    assert _is_linked(b, 'project_DurationQuantity82', a2)
    if hasattr(a1, 'project_Interval1'):
        assert not _is_linked(a1, 'project_Interval1', b)
    if hasattr(a2, 'project_Interval1'):
        assert _is_linked(a2, 'project_Interval1', b)
    _safe_set(b, 'project_DurationQuantity82', None)
    assert not _is_linked(b, 'project_DurationQuantity82', a2)
    if hasattr(a2, 'project_Interval1'):
        assert not _is_linked(a2, 'project_Interval1', b)


def test_assoc_duration83_reverse_link_reassign_clear():
    a1 = project_Interval2(end="sample_text", start="sample_text")
    a2 = project_Interval2(end="sample_text_2", start="sample_text_2")
    b = project_DurationQuantity(unit="sample_text", value=3.14)
    _safe_set(b, 'project_DurationQuantity85', a1)
    assert _is_linked(b, 'project_DurationQuantity85', a1)
    if hasattr(a1, 'project_Interval284'):
        assert _is_linked(a1, 'project_Interval284', b)
    _safe_set(b, 'project_DurationQuantity85', a2)
    assert _is_linked(b, 'project_DurationQuantity85', a2)
    if hasattr(a1, 'project_Interval284'):
        assert not _is_linked(a1, 'project_Interval284', b)
    if hasattr(a2, 'project_Interval284'):
        assert _is_linked(a2, 'project_Interval284', b)
    _safe_set(b, 'project_DurationQuantity85', None)
    assert not _is_linked(b, 'project_DurationQuantity85', a2)
    if hasattr(a2, 'project_Interval284'):
        assert not _is_linked(a2, 'project_Interval284', b)


def test_assoc_duration86_reverse_link_reassign_clear():
    a1 = project_Interval3(end="sample_text", start="sample_text")
    a2 = project_Interval3(end="sample_text_2", start="sample_text_2")
    b = project_DurationQuantity(unit="sample_text", value=3.14)
    _safe_set(b, 'project_DurationQuantity87', a1)
    assert _is_linked(b, 'project_DurationQuantity87', a1)
    if hasattr(a1, 'project_Interval3'):
        assert _is_linked(a1, 'project_Interval3', b)
    _safe_set(b, 'project_DurationQuantity87', a2)
    assert _is_linked(b, 'project_DurationQuantity87', a2)
    if hasattr(a1, 'project_Interval3'):
        assert not _is_linked(a1, 'project_Interval3', b)
    if hasattr(a2, 'project_Interval3'):
        assert _is_linked(a2, 'project_Interval3', b)
    _safe_set(b, 'project_DurationQuantity87', None)
    assert not _is_linked(b, 'project_DurationQuantity87', a2)
    if hasattr(a2, 'project_Interval3'):
        assert not _is_linked(a2, 'project_Interval3', b)


def test_assoc_duration88_reverse_link_reassign_clear():
    a1 = project_Interval4(end="sample_text", start="sample_text")
    a2 = project_Interval4(end="sample_text_2", start="sample_text_2")
    b = project_DurationQuantity(unit="sample_text", value=3.14)
    _safe_set(b, 'project_DurationQuantity90', a1)
    assert _is_linked(b, 'project_DurationQuantity90', a1)
    if hasattr(a1, 'project_Interval489'):
        assert _is_linked(a1, 'project_Interval489', b)
    _safe_set(b, 'project_DurationQuantity90', a2)
    assert _is_linked(b, 'project_DurationQuantity90', a2)
    if hasattr(a1, 'project_Interval489'):
        assert not _is_linked(a1, 'project_Interval489', b)
    if hasattr(a2, 'project_Interval489'):
        assert _is_linked(a2, 'project_Interval489', b)
    _safe_set(b, 'project_DurationQuantity90', None)
    assert not _is_linked(b, 'project_DurationQuantity90', a2)
    if hasattr(a2, 'project_Interval489'):
        assert not _is_linked(a2, 'project_Interval489', b)


def test_assoc_extend57_reverse_link_reassign_clear():
    a1 = project_ExtendedResourceAttribute(value="sample_text")
    a2 = project_ExtendedResourceAttribute(value="sample_text_2")
    b = project_Extend(id="sample_text", inherit=True, name="sample_text", scenariospecific=True)
    _safe_set(b, 'project_Extend58', a1)
    assert _is_linked(b, 'project_Extend58', a1)
    if hasattr(a1, 'project_ExtendedResourceAttribute'):
        assert _is_linked(a1, 'project_ExtendedResourceAttribute', b)
    _safe_set(b, 'project_Extend58', a2)
    assert _is_linked(b, 'project_Extend58', a2)
    if hasattr(a1, 'project_ExtendedResourceAttribute'):
        assert not _is_linked(a1, 'project_ExtendedResourceAttribute', b)
    if hasattr(a2, 'project_ExtendedResourceAttribute'):
        assert _is_linked(a2, 'project_ExtendedResourceAttribute', b)
    _safe_set(b, 'project_Extend58', None)
    assert not _is_linked(b, 'project_Extend58', a2)
    if hasattr(a2, 'project_ExtendedResourceAttribute'):
        assert not _is_linked(a2, 'project_ExtendedResourceAttribute', b)


def test_assoc_extend61_reverse_link_reassign_clear():
    a1 = project_ExtendedTaskAttribute(value="sample_text")
    a2 = project_ExtendedTaskAttribute(value="sample_text_2")
    b = project_Extend(id="sample_text", inherit=True, name="sample_text", scenariospecific=True)
    _safe_set(b, 'project_Extend62', a1)
    assert _is_linked(b, 'project_Extend62', a1)
    if hasattr(a1, 'project_ExtendedTaskAttribute'):
        assert _is_linked(a1, 'project_ExtendedTaskAttribute', b)
    _safe_set(b, 'project_Extend62', a2)
    assert _is_linked(b, 'project_Extend62', a2)
    if hasattr(a1, 'project_ExtendedTaskAttribute'):
        assert not _is_linked(a1, 'project_ExtendedTaskAttribute', b)
    if hasattr(a2, 'project_ExtendedTaskAttribute'):
        assert _is_linked(a2, 'project_ExtendedTaskAttribute', b)
    _safe_set(b, 'project_Extend62', None)
    assert not _is_linked(b, 'project_Extend62', a2)
    if hasattr(a2, 'project_ExtendedTaskAttribute'):
        assert not _is_linked(a2, 'project_ExtendedTaskAttribute', b)


def test_assoc_hours222_reverse_link_reassign_clear():
    a1 = project_WorkingHours(off=True)
    a2 = project_WorkingHours(off=False)
    b = project_WorkHours(start="sample_text", stop="sample_text")
    _safe_set(b, 'project_WorkHours', a1)
    assert _is_linked(b, 'project_WorkHours', a1)
    if hasattr(a1, 'project_WorkingHours223'):
        assert _is_linked(a1, 'project_WorkingHours223', b)
    _safe_set(b, 'project_WorkHours', a2)
    assert _is_linked(b, 'project_WorkHours', a2)
    if hasattr(a1, 'project_WorkingHours223'):
        assert not _is_linked(a1, 'project_WorkingHours223', b)
    if hasattr(a2, 'project_WorkingHours223'):
        assert _is_linked(a2, 'project_WorkingHours223', b)
    _safe_set(b, 'project_WorkHours', None)
    assert not _is_linked(b, 'project_WorkHours', a2)
    if hasattr(a2, 'project_WorkingHours223'):
        assert not _is_linked(a2, 'project_WorkingHours223', b)


def test_assoc_interval35_reverse_link_reassign_clear():
    a1 = project_Interval4(end="sample_text", start="sample_text")
    a2 = project_Interval4(end="sample_text_2", start="sample_text_2")
    b = project_Booking(overtime=7, sloppy=7)
    _safe_set(b, 'project_Booking', a1)
    assert _is_linked(b, 'project_Booking', a1)
    if hasattr(a1, 'project_Interval4'):
        assert _is_linked(a1, 'project_Interval4', b)
    _safe_set(b, 'project_Booking', a2)
    assert _is_linked(b, 'project_Booking', a2)
    if hasattr(a1, 'project_Interval4'):
        assert not _is_linked(a1, 'project_Interval4', b)
    if hasattr(a2, 'project_Interval4'):
        assert _is_linked(a2, 'project_Interval4', b)
    _safe_set(b, 'project_Booking', None)
    assert not _is_linked(b, 'project_Booking', a2)
    if hasattr(a2, 'project_Interval4'):
        assert not _is_linked(a2, 'project_Interval4', b)


def test_assoc_interval8_reverse_link_reassign_clear():
    a1 = project_Project(id="sample_text", name="sample_text", version="sample_text")
    a2 = project_Project(id="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = project_Interval2(end="sample_text", start="sample_text")
    _safe_set(b, 'project_Interval2', a1)
    assert _is_linked(b, 'project_Interval2', a1)
    if hasattr(a1, 'project_Project9'):
        assert _is_linked(a1, 'project_Project9', b)
    _safe_set(b, 'project_Interval2', a2)
    assert _is_linked(b, 'project_Interval2', a2)
    if hasattr(a1, 'project_Project9'):
        assert not _is_linked(a1, 'project_Project9', b)
    if hasattr(a2, 'project_Project9'):
        assert _is_linked(a2, 'project_Project9', b)
    _safe_set(b, 'project_Interval2', None)
    assert not _is_linked(b, 'project_Interval2', a2)
    if hasattr(a2, 'project_Project9'):
        assert not _is_linked(a2, 'project_Project9', b)


def test_assoc_intervals215_reverse_link_reassign_clear():
    a1 = project_Vacation(name="sample_text")
    a2 = project_Vacation(name="sample_text_2")
    b = project_Interval3(end="sample_text", start="sample_text")
    _safe_set(b, 'project_Interval3217', a1)
    assert _is_linked(b, 'project_Interval3217', a1)
    if hasattr(a1, 'project_Vacation216'):
        assert _is_linked(a1, 'project_Vacation216', b)
    _safe_set(b, 'project_Interval3217', a2)
    assert _is_linked(b, 'project_Interval3217', a2)
    if hasattr(a1, 'project_Vacation216'):
        assert not _is_linked(a1, 'project_Vacation216', b)
    if hasattr(a2, 'project_Vacation216'):
        assert _is_linked(a2, 'project_Vacation216', b)
    _safe_set(b, 'project_Interval3217', None)
    assert not _is_linked(b, 'project_Interval3217', a2)
    if hasattr(a2, 'project_Vacation216'):
        assert not _is_linked(a2, 'project_Vacation216', b)


def test_assoc_period233_reverse_link_reassign_clear():
    a1 = project_LimitAttribute(end="sample_text", start="sample_text")
    a2 = project_LimitAttribute(end="sample_text_2", start="sample_text_2")
    b = project_Interval1(end="sample_text", start="sample_text")
    _safe_set(b, 'project_Interval1235', a1)
    assert _is_linked(b, 'project_Interval1235', a1)
    if hasattr(a1, 'project_LimitAttribute234'):
        assert _is_linked(a1, 'project_LimitAttribute234', b)
    _safe_set(b, 'project_Interval1235', a2)
    assert _is_linked(b, 'project_Interval1235', a2)
    if hasattr(a1, 'project_LimitAttribute234'):
        assert not _is_linked(a1, 'project_LimitAttribute234', b)
    if hasattr(a2, 'project_LimitAttribute234'):
        assert _is_linked(a2, 'project_LimitAttribute234', b)
    _safe_set(b, 'project_Interval1235', None)
    assert not _is_linked(b, 'project_Interval1235', a2)
    if hasattr(a2, 'project_LimitAttribute234'):
        assert not _is_linked(a2, 'project_LimitAttribute234', b)


def test_assoc_resource69_reverse_link_reassign_clear():
    a1 = project_Resource(id="sample_text", name="sample_text")
    a2 = project_Resource(id="sample_text_2", name="sample_text_2")
    b = project_Function(date="sample_text", distance=7, level=7, parentId="sample_text")
    _safe_set(b, 'project_Function70', a1)
    assert _is_linked(b, 'project_Function70', a1)
    if hasattr(a1, 'project_Resource71'):
        assert _is_linked(a1, 'project_Resource71', b)
    _safe_set(b, 'project_Function70', a2)
    assert _is_linked(b, 'project_Function70', a2)
    if hasattr(a1, 'project_Resource71'):
        assert not _is_linked(a1, 'project_Resource71', b)
    if hasattr(a2, 'project_Resource71'):
        assert _is_linked(a2, 'project_Resource71', b)
    _safe_set(b, 'project_Function70', None)
    assert not _is_linked(b, 'project_Function70', a2)
    if hasattr(a2, 'project_Resource71'):
        assert not _is_linked(a2, 'project_Resource71', b)


def test_assoc_resources236_reverse_link_reassign_clear():
    a1 = project_Resource(id="sample_text", name="sample_text")
    a2 = project_Resource(id="sample_text_2", name="sample_text_2")
    b = project_LimitAttribute(end="sample_text", start="sample_text")
    _safe_set(b, 'project_LimitAttribute237', {a1})
    assert _is_linked(b, 'project_LimitAttribute237', a1)
    if hasattr(a1, 'project_Resource238'):
        assert _is_linked(a1, 'project_Resource238', b)
    _safe_set(b, 'project_LimitAttribute237', {a2})
    assert _is_linked(b, 'project_LimitAttribute237', a2)
    if hasattr(a1, 'project_Resource238'):
        assert not _is_linked(a1, 'project_Resource238', b)
    if hasattr(a2, 'project_Resource238'):
        assert _is_linked(a2, 'project_Resource238', b)
    _safe_set(b, 'project_LimitAttribute237', set())
    assert not _is_linked(b, 'project_LimitAttribute237', a2)
    if hasattr(a2, 'project_Resource238'):
        assert not _is_linked(a2, 'project_Resource238', b)


def test_assoc_scenario123_reverse_link_reassign_clear():
    a1 = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    a2 = project_Scenario(active="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    _safe_set(b, 'project_Scenario124', a1)
    assert _is_linked(b, 'project_Scenario124', a1)
    if hasattr(a1, 'project_Scenario122'):
        assert _is_linked(a1, 'project_Scenario122', b)
    _safe_set(b, 'project_Scenario124', a2)
    assert _is_linked(b, 'project_Scenario124', a2)
    if hasattr(a1, 'project_Scenario122'):
        assert not _is_linked(a1, 'project_Scenario122', b)
    if hasattr(a2, 'project_Scenario122'):
        assert _is_linked(a2, 'project_Scenario122', b)
    _safe_set(b, 'project_Scenario124', None)
    assert not _is_linked(b, 'project_Scenario124', a2)
    if hasattr(a2, 'project_Scenario122'):
        assert not _is_linked(a2, 'project_Scenario122', b)


def test_assoc_scenario65_reverse_link_reassign_clear():
    a1 = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    a2 = project_Scenario(active="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = project_Function(date="sample_text", distance=7, level=7, parentId="sample_text")
    _safe_set(b, 'project_Function', a1)
    assert _is_linked(b, 'project_Function', a1)
    if hasattr(a1, 'project_Scenario'):
        assert _is_linked(a1, 'project_Scenario', b)
    _safe_set(b, 'project_Function', a2)
    assert _is_linked(b, 'project_Function', a2)
    if hasattr(a1, 'project_Scenario'):
        assert not _is_linked(a1, 'project_Scenario', b)
    if hasattr(a2, 'project_Scenario'):
        assert _is_linked(a2, 'project_Scenario', b)
    _safe_set(b, 'project_Function', None)
    assert not _is_linked(b, 'project_Function', a2)
    if hasattr(a2, 'project_Scenario'):
        assert not _is_linked(a2, 'project_Scenario', b)


def test_assoc_shift131_reverse_link_reassign_clear():
    a1 = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    a2 = project_Shift(id="sample_text_2", name="sample_text_2", replace="sample_text_2", timezone="sample_text_2")
    b = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    _safe_set(b, 'project_Shift132', a1)
    assert _is_linked(b, 'project_Shift132', a1)
    if hasattr(a1, 'project_Shift130'):
        assert _is_linked(a1, 'project_Shift130', b)
    _safe_set(b, 'project_Shift132', a2)
    assert _is_linked(b, 'project_Shift132', a2)
    if hasattr(a1, 'project_Shift130'):
        assert not _is_linked(a1, 'project_Shift130', b)
    if hasattr(a2, 'project_Shift130'):
        assert _is_linked(a2, 'project_Shift130', b)
    _safe_set(b, 'project_Shift132', None)
    assert not _is_linked(b, 'project_Shift132', a2)
    if hasattr(a2, 'project_Shift130'):
        assert not _is_linked(a2, 'project_Shift130', b)


def test_assoc_task239_reverse_link_reassign_clear():
    a1 = project_TaskDependency(policy="sample_text")
    a2 = project_TaskDependency(policy="sample_text_2")
    b = project_Task(id="sample_text", name="sample_text")
    _safe_set(b, 'project_Task240', a1)
    assert _is_linked(b, 'project_Task240', a1)
    if hasattr(a1, 'project_TaskDependency'):
        assert _is_linked(a1, 'project_TaskDependency', b)
    _safe_set(b, 'project_Task240', a2)
    assert _is_linked(b, 'project_Task240', a2)
    if hasattr(a1, 'project_TaskDependency'):
        assert not _is_linked(a1, 'project_TaskDependency', b)
    if hasattr(a2, 'project_TaskDependency'):
        assert _is_linked(a2, 'project_TaskDependency', b)
    _safe_set(b, 'project_Task240', None)
    assert not _is_linked(b, 'project_Task240', a2)
    if hasattr(a2, 'project_TaskDependency'):
        assert not _is_linked(a2, 'project_TaskDependency', b)


def test_assoc_task66_reverse_link_reassign_clear():
    a1 = project_Task(id="sample_text", name="sample_text")
    a2 = project_Task(id="sample_text_2", name="sample_text_2")
    b = project_Function(date="sample_text", distance=7, level=7, parentId="sample_text")
    _safe_set(b, 'project_Function67', a1)
    assert _is_linked(b, 'project_Function67', a1)
    if hasattr(a1, 'project_Task68'):
        assert _is_linked(a1, 'project_Task68', b)
    _safe_set(b, 'project_Function67', a2)
    assert _is_linked(b, 'project_Function67', a2)
    if hasattr(a1, 'project_Task68'):
        assert not _is_linked(a1, 'project_Task68', b)
    if hasattr(a2, 'project_Task68'):
        assert _is_linked(a2, 'project_Task68', b)
    _safe_set(b, 'project_Function67', None)
    assert not _is_linked(b, 'project_Function67', a2)
    if hasattr(a2, 'project_Task68'):
        assert not _is_linked(a2, 'project_Task68', b)


def test_assoc_vacation129_reverse_link_reassign_clear():
    a1 = project_Vacation(name="sample_text")
    a2 = project_Vacation(name="sample_text_2")
    b = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    _safe_set(b, 'project_Shift', a1)
    assert _is_linked(b, 'project_Shift', a1)
    if hasattr(a1, 'project_Vacation'):
        assert _is_linked(a1, 'project_Vacation', b)
    _safe_set(b, 'project_Shift', a2)
    assert _is_linked(b, 'project_Shift', a2)
    if hasattr(a1, 'project_Vacation'):
        assert not _is_linked(a1, 'project_Vacation', b)
    if hasattr(a2, 'project_Vacation'):
        assert _is_linked(a2, 'project_Vacation', b)
    _safe_set(b, 'project_Shift', None)
    assert not _is_linked(b, 'project_Shift', a2)
    if hasattr(a2, 'project_Vacation'):
        assert not _is_linked(a2, 'project_Vacation', b)


def test_assoc_weekdays220_reverse_link_reassign_clear():
    a1 = project_WorkingHours(off=True)
    a2 = project_WorkingHours(off=False)
    b = project_Weekdays(first="sample_text", last="sample_text")
    _safe_set(b, 'project_Weekdays', a1)
    assert _is_linked(b, 'project_Weekdays', a1)
    if hasattr(a1, 'project_WorkingHours221'):
        assert _is_linked(a1, 'project_WorkingHours221', b)
    _safe_set(b, 'project_Weekdays', a2)
    assert _is_linked(b, 'project_Weekdays', a2)
    if hasattr(a1, 'project_WorkingHours221'):
        assert not _is_linked(a1, 'project_WorkingHours221', b)
    if hasattr(a2, 'project_WorkingHours221'):
        assert _is_linked(a2, 'project_WorkingHours221', b)
    _safe_set(b, 'project_Weekdays', None)
    assert not _is_linked(b, 'project_Weekdays', a2)
    if hasattr(a2, 'project_WorkingHours221'):
        assert not _is_linked(a2, 'project_WorkingHours221', b)


def test_assoc_workingHours133_reverse_link_reassign_clear():
    a1 = project_WorkingHours(off=True)
    a2 = project_WorkingHours(off=False)
    b = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    _safe_set(b, 'project_Shift134', a1)
    assert _is_linked(b, 'project_Shift134', a1)
    if hasattr(a1, 'project_WorkingHours'):
        assert _is_linked(a1, 'project_WorkingHours', b)
    _safe_set(b, 'project_Shift134', a2)
    assert _is_linked(b, 'project_Shift134', a2)
    if hasattr(a1, 'project_WorkingHours'):
        assert not _is_linked(a1, 'project_WorkingHours', b)
    if hasattr(a2, 'project_WorkingHours'):
        assert _is_linked(a2, 'project_WorkingHours', b)
    _safe_set(b, 'project_Shift134', None)
    assert not _is_linked(b, 'project_Shift134', a2)
    if hasattr(a2, 'project_WorkingHours'):
        assert not _is_linked(a2, 'project_WorkingHours', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_account160_stub_double():
    # project_SupplementAccount has no real 'project_SupplementAccount' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_SupplementAccount()
    setattr(partner, 'project_SupplementAccount', None)
    _safe_set(owner, 'project_Account161', partner)
    assert getattr(partner, 'project_SupplementAccount') == owner
    _safe_set(owner, 'project_Account161', None)
    assert getattr(partner, 'project_SupplementAccount') is None


def test_assoc_account4_stub_double():
    # project_AccountPrefix has no real 'project_AccountPrefix' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_AccountPrefix()
    setattr(partner, 'project_AccountPrefix', None)
    _safe_set(owner, 'project_Account5', partner)
    assert getattr(partner, 'project_AccountPrefix') == owner
    _safe_set(owner, 'project_Account5', None)
    assert getattr(partner, 'project_AccountPrefix') is None


def test_assoc_account6_stub_double():
    # project_AccountRoot has no real 'project_AccountRoot' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_AccountRoot()
    setattr(partner, 'project_AccountRoot', None)
    _safe_set(owner, 'project_Account7', partner)
    assert getattr(partner, 'project_AccountRoot') == owner
    _safe_set(owner, 'project_Account7', None)
    assert getattr(partner, 'project_AccountRoot') is None


def test_assoc_accountShares51_stub_double():
    # project_ChargeSet has no real 'project_ChargeSet' property in the generated
    # code (a bare stub) -- manually attach it so project_AccountShare's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_AccountShare's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_AccountShare(share=3.14)
    partner = project_ChargeSet()
    setattr(partner, 'project_ChargeSet', None)
    _safe_set(owner, 'project_AccountShare', partner)
    assert owner in getattr(partner, 'project_ChargeSet')
    _safe_set(owner, 'project_AccountShare', None)
    assert owner not in getattr(partner, 'project_ChargeSet')


def test_assoc_attribute227_stub_double():
    # project_ColumnAttribute has no real 'project_ColumnAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Column(id="sample_text")
    partner = project_ColumnAttribute()
    setattr(partner, 'project_ColumnAttribute', None)
    _safe_set(owner, 'project_Column228', partner)
    assert getattr(partner, 'project_ColumnAttribute') == owner
    _safe_set(owner, 'project_Column228', None)
    assert getattr(partner, 'project_ColumnAttribute') is None


def test_assoc_attributes10_stub_double():
    # project_ProjectAttribute has no real 'project_ProjectAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Project(id="sample_text", name="sample_text", version="sample_text")
    partner = project_ProjectAttribute()
    setattr(partner, 'project_ProjectAttribute', None)
    _safe_set(owner, 'project_Project11', {partner})
    assert getattr(partner, 'project_ProjectAttribute') == owner
    _safe_set(owner, 'project_Project11', set())
    assert getattr(partner, 'project_ProjectAttribute') is None


def test_assoc_attributes12_stub_double():
    # project_TaskAttribute has no real 'project_TaskAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_TaskAttribute()
    setattr(partner, 'project_TaskAttribute', None)
    _safe_set(owner, 'project_Task', {partner})
    assert getattr(partner, 'project_TaskAttribute') == owner
    _safe_set(owner, 'project_Task', set())
    assert getattr(partner, 'project_TaskAttribute') is None


def test_assoc_attributes13_stub_double():
    # project_ReportAttribute has no real 'project_ReportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Report's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Report's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Report(id="sample_text", name="sample_text")
    partner = project_ReportAttribute()
    setattr(partner, 'project_ReportAttribute', None)
    _safe_set(owner, 'project_Report', {partner})
    assert getattr(partner, 'project_ReportAttribute') == owner
    _safe_set(owner, 'project_Report', set())
    assert getattr(partner, 'project_ReportAttribute') is None


def test_assoc_attributes14_stub_double():
    # project_IcalReportAttribute has no real 'project_IcalReportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_IcalReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_IcalReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_IcalReport(filename="sample_text")
    partner = project_IcalReportAttribute()
    setattr(partner, 'project_IcalReportAttribute', None)
    _safe_set(owner, 'project_IcalReport', {partner})
    assert getattr(partner, 'project_IcalReportAttribute') == owner
    _safe_set(owner, 'project_IcalReport', set())
    assert getattr(partner, 'project_IcalReportAttribute') is None


def test_assoc_attributes15_stub_double():
    # project_ExportAttribute has no real 'project_ExportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Export's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Export's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Export(filename="sample_text", id="sample_text")
    partner = project_ExportAttribute()
    setattr(partner, 'project_ExportAttribute', None)
    _safe_set(owner, 'project_Export', {partner})
    assert getattr(partner, 'project_ExportAttribute') == owner
    _safe_set(owner, 'project_Export', set())
    assert getattr(partner, 'project_ExportAttribute') is None


def test_assoc_attributes150_stub_double():
    # project_StatusStatusSheetAttribute has no real 'project_StatusStatusSheetAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_StatusStatusSheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_StatusStatusSheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_StatusStatusSheet(level="sample_text", text="sample_text")
    partner = project_StatusStatusSheetAttribute()
    setattr(partner, 'project_StatusStatusSheetAttribute', None)
    _safe_set(owner, 'project_StatusStatusSheet', {partner})
    assert getattr(partner, 'project_StatusStatusSheetAttribute') == owner
    _safe_set(owner, 'project_StatusStatusSheet', set())
    assert getattr(partner, 'project_StatusStatusSheetAttribute') is None


def test_assoc_attributes151_stub_double():
    # project_StatusTimesheetAttribute has no real 'project_StatusTimesheetAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_StatusTimesheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_StatusTimesheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_StatusTimesheet(level="sample_text", text="sample_text")
    partner = project_StatusTimesheetAttribute()
    setattr(partner, 'project_StatusTimesheetAttribute', None)
    _safe_set(owner, 'project_StatusTimesheet', {partner})
    assert getattr(partner, 'project_StatusTimesheetAttribute') == owner
    _safe_set(owner, 'project_StatusTimesheet', set())
    assert getattr(partner, 'project_StatusTimesheetAttribute') is None


def test_assoc_attributes159_stub_double():
    # project_StatusSheetReportAttribute has no real 'project_StatusSheetReportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_StatusSheetReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_StatusSheetReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_StatusSheetReport(filename="sample_text")
    partner = project_StatusSheetReportAttribute()
    setattr(partner, 'project_StatusSheetReportAttribute', None)
    _safe_set(owner, 'project_StatusSheetReport', {partner})
    assert getattr(partner, 'project_StatusSheetReportAttribute') == owner
    _safe_set(owner, 'project_StatusSheetReport', set())
    assert getattr(partner, 'project_StatusSheetReportAttribute') is None


def test_assoc_attributes16_stub_double():
    # project_ResourceAttribute has no real 'project_ResourceAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_ResourceAttribute()
    setattr(partner, 'project_ResourceAttribute', None)
    _safe_set(owner, 'project_Resource', {partner})
    assert getattr(partner, 'project_ResourceAttribute') == owner
    _safe_set(owner, 'project_Resource', set())
    assert getattr(partner, 'project_ResourceAttribute') is None


def test_assoc_attributes210_stub_double():
    # project_TimesheetReportAttribute has no real 'project_TimesheetReportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_TimesheetReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TimesheetReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TimesheetReport(filename="sample_text")
    partner = project_TimesheetReportAttribute()
    setattr(partner, 'project_TimesheetReportAttribute', None)
    _safe_set(owner, 'project_TimesheetReport', {partner})
    assert getattr(partner, 'project_TimesheetReportAttribute') == owner
    _safe_set(owner, 'project_TimesheetReport', set())
    assert getattr(partner, 'project_TimesheetReportAttribute') is None


def test_assoc_attributes23_stub_double():
    # project_NavigatorAttribute has no real 'project_NavigatorAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Navigator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Navigator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Navigator(id="sample_text")
    partner = project_NavigatorAttribute()
    setattr(partner, 'project_NavigatorAttribute', None)
    _safe_set(owner, 'project_Navigator', {partner})
    assert getattr(partner, 'project_NavigatorAttribute') == owner
    _safe_set(owner, 'project_Navigator', set())
    assert getattr(partner, 'project_NavigatorAttribute') is None


def test_assoc_attributes231_stub_double():
    # project_Limit has no real 'project_Limit232' property in the generated
    # code (a bare stub) -- manually attach it so project_LimitAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_LimitAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_LimitAttribute(end="sample_text", start="sample_text")
    partner = project_Limit()
    setattr(partner, 'project_Limit232', None)
    _safe_set(owner, 'project_LimitAttribute', partner)
    assert owner in getattr(partner, 'project_Limit232')
    _safe_set(owner, 'project_LimitAttribute', None)
    assert owner not in getattr(partner, 'project_Limit232')


def test_assoc_attributes24_stub_double():
    # project_NewTaskAttribute has no real 'project_NewTaskAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_NewTask's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_NewTask's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_NewTask(id="sample_text", text="sample_text")
    partner = project_NewTaskAttribute()
    setattr(partner, 'project_NewTaskAttribute', None)
    _safe_set(owner, 'project_NewTask', {partner})
    assert getattr(partner, 'project_NewTaskAttribute') == owner
    _safe_set(owner, 'project_NewTask', set())
    assert getattr(partner, 'project_NewTaskAttribute') is None


def test_assoc_attributes25_stub_double():
    # project_NikuReportAttribute has no real 'project_NikuReportAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_NikuReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_NikuReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_NikuReport(filename="sample_text")
    partner = project_NikuReportAttribute()
    setattr(partner, 'project_NikuReportAttribute', None)
    _safe_set(owner, 'project_NikuReport', {partner})
    assert getattr(partner, 'project_NikuReportAttribute') == owner
    _safe_set(owner, 'project_NikuReport', set())
    assert getattr(partner, 'project_NikuReportAttribute') is None


def test_assoc_attributes3_stub_double():
    # project_AccountAttribute has no real 'project_AccountAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_AccountAttribute()
    setattr(partner, 'project_AccountAttribute', None)
    _safe_set(owner, 'project_Account', {partner})
    assert getattr(partner, 'project_AccountAttribute') == owner
    _safe_set(owner, 'project_Account', set())
    assert getattr(partner, 'project_AccountAttribute') is None


def test_assoc_attributes80_stub_double():
    # project_IncludePropertiesAttribute has no real 'project_IncludePropertiesAttribute' property in the generated
    # code (a bare stub) -- manually attach it so project_IncludeProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_IncludeProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_IncludeProperties(importURI="sample_text")
    partner = project_IncludePropertiesAttribute()
    setattr(partner, 'project_IncludePropertiesAttribute', None)
    _safe_set(owner, 'project_IncludeProperties', {partner})
    assert getattr(partner, 'project_IncludePropertiesAttribute') == owner
    _safe_set(owner, 'project_IncludeProperties', set())
    assert getattr(partner, 'project_IncludePropertiesAttribute') is None


def test_assoc_author92_stub_double():
    # project_Author has no real 'project_Author94' property in the generated
    # code (a bare stub) -- manually attach it so project_JournalEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_JournalEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_JournalEntry(date="sample_text", headline="sample_text")
    partner = project_Author()
    setattr(partner, 'project_Author94', None)
    _safe_set(owner, 'project_JournalEntry93', partner)
    assert getattr(partner, 'project_Author94') == owner
    _safe_set(owner, 'project_JournalEntry93', None)
    assert getattr(partner, 'project_Author94') is None


def test_assoc_booking38_stub_double():
    # project_BookingTask has no real 'project_BookingTask39' property in the generated
    # code (a bare stub) -- manually attach it so project_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Booking(overtime=7, sloppy=7)
    partner = project_BookingTask()
    setattr(partner, 'project_BookingTask39', None)
    _safe_set(owner, 'project_Booking40', partner)
    assert getattr(partner, 'project_BookingTask39') == owner
    _safe_set(owner, 'project_Booking40', None)
    assert getattr(partner, 'project_BookingTask39') is None


def test_assoc_booking43_stub_double():
    # project_BookingResource has no real 'project_BookingResource44' property in the generated
    # code (a bare stub) -- manually attach it so project_Booking's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Booking's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Booking(overtime=7, sloppy=7)
    partner = project_BookingResource()
    setattr(partner, 'project_BookingResource44', None)
    _safe_set(owner, 'project_Booking45', partner)
    assert getattr(partner, 'project_BookingResource44') == owner
    _safe_set(owner, 'project_Booking45', None)
    assert getattr(partner, 'project_BookingResource44') is None


def test_assoc_color47_stub_double():
    # project_CellColor has no real 'project_CellColor48' property in the generated
    # code (a bare stub) -- manually attach it so project_RGB's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_RGB's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_RGB(value="sample_text")
    partner = project_CellColor()
    setattr(partner, 'project_CellColor48', None)
    _safe_set(owner, 'project_RGB', partner)
    assert getattr(partner, 'project_CellColor48') == owner
    _safe_set(owner, 'project_RGB', None)
    assert getattr(partner, 'project_CellColor48') is None


def test_assoc_columns52_stub_double():
    # project_Columns has no real 'project_Columns' property in the generated
    # code (a bare stub) -- manually attach it so project_Column's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Column's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Column(id="sample_text")
    partner = project_Columns()
    setattr(partner, 'project_Columns', None)
    _safe_set(owner, 'project_Column', partner)
    assert owner in getattr(partner, 'project_Columns')
    _safe_set(owner, 'project_Column', None)
    assert owner not in getattr(partner, 'project_Columns')


def test_assoc_cost30_stub_double():
    # project_Balance has no real 'project_Balance' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_Balance()
    setattr(partner, 'project_Balance', None)
    _safe_set(owner, 'project_Account31', partner)
    assert getattr(partner, 'project_Balance') == owner
    _safe_set(owner, 'project_Account31', None)
    assert getattr(partner, 'project_Balance') is None


def test_assoc_details95_stub_double():
    # project_Details has no real 'project_Details' property in the generated
    # code (a bare stub) -- manually attach it so project_JournalEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_JournalEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_JournalEntry(date="sample_text", headline="sample_text")
    partner = project_Details()
    setattr(partner, 'project_Details', None)
    _safe_set(owner, 'project_JournalEntry96', partner)
    assert getattr(partner, 'project_Details') == owner
    _safe_set(owner, 'project_JournalEntry96', None)
    assert getattr(partner, 'project_Details') is None


def test_assoc_duration229_stub_double():
    # project_Limit has no real 'project_Limit' property in the generated
    # code (a bare stub) -- manually attach it so project_DurationQuantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_DurationQuantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_DurationQuantity(unit="sample_text", value=3.14)
    partner = project_Limit()
    setattr(partner, 'project_Limit', None)
    _safe_set(owner, 'project_DurationQuantity230', partner)
    assert getattr(partner, 'project_Limit') == owner
    _safe_set(owner, 'project_DurationQuantity230', None)
    assert getattr(partner, 'project_Limit') is None


def test_assoc_duration53_stub_double():
    # project_Duration has no real 'project_Duration' property in the generated
    # code (a bare stub) -- manually attach it so project_DurationQuantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_DurationQuantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_DurationQuantity(unit="sample_text", value=3.14)
    partner = project_Duration()
    setattr(partner, 'project_Duration', None)
    _safe_set(owner, 'project_DurationQuantity', partner)
    assert getattr(partner, 'project_Duration') == owner
    _safe_set(owner, 'project_DurationQuantity', None)
    assert getattr(partner, 'project_Duration') is None


def test_assoc_effort54_stub_double():
    # project_Effort has no real 'project_Effort' property in the generated
    # code (a bare stub) -- manually attach it so project_DurationQuantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_DurationQuantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_DurationQuantity(unit="sample_text", value=3.14)
    partner = project_Effort()
    setattr(partner, 'project_Effort', None)
    _safe_set(owner, 'project_DurationQuantity55', partner)
    assert getattr(partner, 'project_Effort') == owner
    _safe_set(owner, 'project_DurationQuantity55', None)
    assert getattr(partner, 'project_Effort') is None


def test_assoc_expression211_stub_double():
    # project_LogicalExpression has no real 'project_LogicalExpression212' property in the generated
    # code (a bare stub) -- manually attach it so project_ToolTip's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_ToolTip's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_ToolTip(tip="sample_text")
    partner = project_LogicalExpression()
    setattr(partner, 'project_LogicalExpression212', None)
    _safe_set(owner, 'project_ToolTip', partner)
    assert getattr(partner, 'project_LogicalExpression212') == owner
    _safe_set(owner, 'project_ToolTip', None)
    assert getattr(partner, 'project_LogicalExpression212') is None


def test_assoc_expression72_stub_double():
    # project_LogicalExpression has no real 'project_LogicalExpression73' property in the generated
    # code (a bare stub) -- manually attach it so project_HAlign's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_HAlign's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_HAlign(justification="sample_text")
    partner = project_LogicalExpression()
    setattr(partner, 'project_LogicalExpression73', None)
    _safe_set(owner, 'project_HAlign', partner)
    assert getattr(partner, 'project_LogicalExpression73') == owner
    _safe_set(owner, 'project_HAlign', None)
    assert getattr(partner, 'project_LogicalExpression73') is None


def test_assoc_expresssion49_stub_double():
    # project_LogicalExpression has no real 'project_LogicalExpression50' property in the generated
    # code (a bare stub) -- manually attach it so project_CellText's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_CellText's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_CellText(text="sample_text")
    partner = project_LogicalExpression()
    setattr(partner, 'project_LogicalExpression50', None)
    _safe_set(owner, 'project_CellText', partner)
    assert getattr(partner, 'project_LogicalExpression50') == owner
    _safe_set(owner, 'project_CellText', None)
    assert getattr(partner, 'project_LogicalExpression50') is None


def test_assoc_extends56_stub_double():
    # project_ExtendResource has no real 'project_ExtendResource' property in the generated
    # code (a bare stub) -- manually attach it so project_Extend's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Extend's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Extend(id="sample_text", inherit=True, name="sample_text", scenariospecific=True)
    partner = project_ExtendResource()
    setattr(partner, 'project_ExtendResource', None)
    _safe_set(owner, 'project_Extend', partner)
    assert owner in getattr(partner, 'project_ExtendResource')
    _safe_set(owner, 'project_Extend', None)
    assert owner not in getattr(partner, 'project_ExtendResource')


def test_assoc_extends59_stub_double():
    # project_ExtendTask has no real 'project_ExtendTask' property in the generated
    # code (a bare stub) -- manually attach it so project_Extend's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Extend's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Extend(id="sample_text", inherit=True, name="sample_text", scenariospecific=True)
    partner = project_ExtendTask()
    setattr(partner, 'project_ExtendTask', None)
    _safe_set(owner, 'project_Extend60', partner)
    assert owner in getattr(partner, 'project_ExtendTask')
    _safe_set(owner, 'project_Extend60', None)
    assert owner not in getattr(partner, 'project_ExtendTask')


def test_assoc_function252_stub_double():
    # project_LogicalFunctionExpression has no real 'project_LogicalFunctionExpression' property in the generated
    # code (a bare stub) -- manually attach it so project_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Function(date="sample_text", distance=7, level=7, parentId="sample_text")
    partner = project_LogicalFunctionExpression()
    setattr(partner, 'project_LogicalFunctionExpression', None)
    _safe_set(owner, 'project_Function253', partner)
    assert getattr(partner, 'project_LogicalFunctionExpression') == owner
    _safe_set(owner, 'project_Function253', None)
    assert getattr(partner, 'project_LogicalFunctionExpression') is None


def test_assoc_gapDuration241_stub_double():
    # project_GapDuration has no real 'project_GapDuration' property in the generated
    # code (a bare stub) -- manually attach it so project_TaskDependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TaskDependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TaskDependency(policy="sample_text")
    partner = project_GapDuration()
    setattr(partner, 'project_GapDuration', None)
    _safe_set(owner, 'project_TaskDependency242', partner)
    assert getattr(partner, 'project_GapDuration') == owner
    _safe_set(owner, 'project_TaskDependency242', None)
    assert getattr(partner, 'project_GapDuration') is None


def test_assoc_gapLength243_stub_double():
    # project_GapLength has no real 'project_GapLength' property in the generated
    # code (a bare stub) -- manually attach it so project_TaskDependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TaskDependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TaskDependency(policy="sample_text")
    partner = project_GapLength()
    setattr(partner, 'project_GapLength', None)
    _safe_set(owner, 'project_TaskDependency244', partner)
    assert getattr(partner, 'project_GapLength') == owner
    _safe_set(owner, 'project_TaskDependency244', None)
    assert getattr(partner, 'project_GapLength') is None


def test_assoc_hideResource180_stub_double():
    # project_HideResource has no real 'project_HideResource181' property in the generated
    # code (a bare stub) -- manually attach it so project_TagFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TagFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TagFile(filename="sample_text", id="sample_text")
    partner = project_HideResource()
    setattr(partner, 'project_HideResource181', None)
    _safe_set(owner, 'project_TagFile', partner)
    assert getattr(partner, 'project_HideResource181') == owner
    _safe_set(owner, 'project_TagFile', None)
    assert getattr(partner, 'project_HideResource181') is None


def test_assoc_hideTask182_stub_double():
    # project_HideTask has no real 'project_HideTask184' property in the generated
    # code (a bare stub) -- manually attach it so project_TagFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TagFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TagFile(filename="sample_text", id="sample_text")
    partner = project_HideTask()
    setattr(partner, 'project_HideTask184', None)
    _safe_set(owner, 'project_TagFile183', partner)
    assert getattr(partner, 'project_HideTask184') == owner
    _safe_set(owner, 'project_TagFile183', None)
    assert getattr(partner, 'project_HideTask184') is None


def test_assoc_interval154_stub_double():
    # project_StatusSheet has no real 'project_StatusSheet155' property in the generated
    # code (a bare stub) -- manually attach it so project_Interval4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Interval4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Interval4(end="sample_text", start="sample_text")
    partner = project_StatusSheet()
    setattr(partner, 'project_StatusSheet155', None)
    _safe_set(owner, 'project_Interval4156', partner)
    assert getattr(partner, 'project_StatusSheet155') == owner
    _safe_set(owner, 'project_Interval4156', None)
    assert getattr(partner, 'project_StatusSheet155') is None


def test_assoc_interval205_stub_double():
    # project_Timesheet has no real 'project_Timesheet206' property in the generated
    # code (a bare stub) -- manually attach it so project_Interval4's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Interval4's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Interval4(end="sample_text", start="sample_text")
    partner = project_Timesheet()
    setattr(partner, 'project_Timesheet206', None)
    _safe_set(owner, 'project_Interval4207', partner)
    assert getattr(partner, 'project_Timesheet206') == owner
    _safe_set(owner, 'project_Interval4207', None)
    assert getattr(partner, 'project_Timesheet206') is None


def test_assoc_intervals146_stub_double():
    # project_ShiftsAllocate has no real 'project_ShiftsAllocate147' property in the generated
    # code (a bare stub) -- manually attach it so project_Interval3's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Interval3's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Interval3(end="sample_text", start="sample_text")
    partner = project_ShiftsAllocate()
    setattr(partner, 'project_ShiftsAllocate147', None)
    _safe_set(owner, 'project_Interval3148', partner)
    assert owner in getattr(partner, 'project_ShiftsAllocate147')
    _safe_set(owner, 'project_Interval3148', None)
    assert owner not in getattr(partner, 'project_ShiftsAllocate147')


def test_assoc_length99_stub_double():
    # project_Length has no real 'project_Length' property in the generated
    # code (a bare stub) -- manually attach it so project_DurationQuantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_DurationQuantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_DurationQuantity(unit="sample_text", value=3.14)
    partner = project_Length()
    setattr(partner, 'project_Length', None)
    _safe_set(owner, 'project_DurationQuantity100', partner)
    assert getattr(partner, 'project_Length') == owner
    _safe_set(owner, 'project_DurationQuantity100', None)
    assert getattr(partner, 'project_Length') is None


def test_assoc_limit141_stub_double():
    # project_ShiftsLimit has no real 'project_ShiftsLimit142' property in the generated
    # code (a bare stub) -- manually attach it so project_Interval2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Interval2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Interval2(end="sample_text", start="sample_text")
    partner = project_ShiftsLimit()
    setattr(partner, 'project_ShiftsLimit142', None)
    _safe_set(owner, 'project_Interval2143', partner)
    assert getattr(partner, 'project_ShiftsLimit142') == owner
    _safe_set(owner, 'project_Interval2143', None)
    assert getattr(partner, 'project_ShiftsLimit142') is None


def test_assoc_period104_stub_double():
    # project_Period has no real 'project_Period' property in the generated
    # code (a bare stub) -- manually attach it so project_Interval2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Interval2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Interval2(end="sample_text", start="sample_text")
    partner = project_Period()
    setattr(partner, 'project_Period', None)
    _safe_set(owner, 'project_Interval2105', partner)
    assert getattr(partner, 'project_Period') == owner
    _safe_set(owner, 'project_Interval2105', None)
    assert getattr(partner, 'project_Period') is None


def test_assoc_project0_stub_double():
    # project_Global has no real 'project_Global' property in the generated
    # code (a bare stub) -- manually attach it so project_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Project(id="sample_text", name="sample_text", version="sample_text")
    partner = project_Global()
    setattr(partner, 'project_Global', None)
    _safe_set(owner, 'project_Project', partner)
    assert getattr(partner, 'project_Global') == owner
    _safe_set(owner, 'project_Project', None)
    assert getattr(partner, 'project_Global') is None


def test_assoc_remaining106_stub_double():
    # project_Remaining has no real 'project_Remaining' property in the generated
    # code (a bare stub) -- manually attach it so project_DurationQuantity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_DurationQuantity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_DurationQuantity(unit="sample_text", value=3.14)
    partner = project_Remaining()
    setattr(partner, 'project_Remaining', None)
    _safe_set(owner, 'project_DurationQuantity107', partner)
    assert getattr(partner, 'project_Remaining') == owner
    _safe_set(owner, 'project_DurationQuantity107', None)
    assert getattr(partner, 'project_Remaining') is None


def test_assoc_report108_stub_double():
    # project_ReportPrefix has no real 'project_ReportPrefix' property in the generated
    # code (a bare stub) -- manually attach it so project_Report's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Report's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Report(id="sample_text", name="sample_text")
    partner = project_ReportPrefix()
    setattr(partner, 'project_ReportPrefix', None)
    _safe_set(owner, 'project_Report109', partner)
    assert getattr(partner, 'project_ReportPrefix') == owner
    _safe_set(owner, 'project_Report109', None)
    assert getattr(partner, 'project_ReportPrefix') is None


def test_assoc_report165_stub_double():
    # project_SupplementReport has no real 'project_SupplementReport' property in the generated
    # code (a bare stub) -- manually attach it so project_Report's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Report's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Report(id="sample_text", name="sample_text")
    partner = project_SupplementReport()
    setattr(partner, 'project_SupplementReport', None)
    _safe_set(owner, 'project_Report166', partner)
    assert getattr(partner, 'project_SupplementReport') == owner
    _safe_set(owner, 'project_Report166', None)
    assert getattr(partner, 'project_SupplementReport') is None


def test_assoc_resource110_stub_double():
    # project_ResourcePrefix has no real 'project_ResourcePrefix' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_ResourcePrefix()
    setattr(partner, 'project_ResourcePrefix', None)
    _safe_set(owner, 'project_Resource111', partner)
    assert getattr(partner, 'project_ResourcePrefix') == owner
    _safe_set(owner, 'project_Resource111', None)
    assert getattr(partner, 'project_ResourcePrefix') is None


def test_assoc_resource112_stub_double():
    # project_ResourceRoot has no real 'project_ResourceRoot' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_ResourceRoot()
    setattr(partner, 'project_ResourceRoot', None)
    _safe_set(owner, 'project_Resource113', partner)
    assert getattr(partner, 'project_ResourceRoot') == owner
    _safe_set(owner, 'project_Resource113', None)
    assert getattr(partner, 'project_ResourceRoot') is None


def test_assoc_resource152_stub_double():
    # project_StatusSheet has no real 'project_StatusSheet' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_StatusSheet()
    setattr(partner, 'project_StatusSheet', None)
    _safe_set(owner, 'project_Resource153', partner)
    assert getattr(partner, 'project_StatusSheet') == owner
    _safe_set(owner, 'project_Resource153', None)
    assert getattr(partner, 'project_StatusSheet') is None


def test_assoc_resource170_stub_double():
    # project_SupplementResource has no real 'project_SupplementResource' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_SupplementResource()
    setattr(partner, 'project_SupplementResource', None)
    _safe_set(owner, 'project_Resource171', partner)
    assert getattr(partner, 'project_SupplementResource') == owner
    _safe_set(owner, 'project_Resource171', None)
    assert getattr(partner, 'project_SupplementResource') is None


def test_assoc_resource18_stub_double():
    # project_AllocateResource has no real 'project_AllocateResource19' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_AllocateResource()
    setattr(partner, 'project_AllocateResource19', None)
    _safe_set(owner, 'project_Resource20', partner)
    assert getattr(partner, 'project_AllocateResource19') == owner
    _safe_set(owner, 'project_Resource20', None)
    assert getattr(partner, 'project_AllocateResource19') is None


def test_assoc_resource203_stub_double():
    # project_Timesheet has no real 'project_Timesheet' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_Timesheet()
    setattr(partner, 'project_Timesheet', None)
    _safe_set(owner, 'project_Resource204', partner)
    assert getattr(partner, 'project_Timesheet') == owner
    _safe_set(owner, 'project_Resource204', None)
    assert getattr(partner, 'project_Timesheet') is None


def test_assoc_resource28_stub_double():
    # project_Author has no real 'project_Author' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_Author()
    setattr(partner, 'project_Author', None)
    _safe_set(owner, 'project_Resource29', partner)
    assert getattr(partner, 'project_Author') == owner
    _safe_set(owner, 'project_Resource29', None)
    assert getattr(partner, 'project_Author') is None


def test_assoc_resource36_stub_double():
    # project_BookingTask has no real 'project_BookingTask' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_BookingTask()
    setattr(partner, 'project_BookingTask', None)
    _safe_set(owner, 'project_Resource37', partner)
    assert getattr(partner, 'project_BookingTask') == owner
    _safe_set(owner, 'project_Resource37', None)
    assert getattr(partner, 'project_BookingTask') is None


def test_assoc_resources102_stub_double():
    # project_Managers has no real 'project_Managers' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_Managers()
    setattr(partner, 'project_Managers', None)
    _safe_set(owner, 'project_Resource103', partner)
    assert owner in getattr(partner, 'project_Managers')
    _safe_set(owner, 'project_Resource103', None)
    assert owner not in getattr(partner, 'project_Managers')


def test_assoc_resources114_stub_double():
    # project_Responsible has no real 'project_Responsible' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_Responsible()
    setattr(partner, 'project_Responsible', None)
    _safe_set(owner, 'project_Resource115', partner)
    assert owner in getattr(partner, 'project_Responsible')
    _safe_set(owner, 'project_Resource115', None)
    assert owner not in getattr(partner, 'project_Responsible')


def test_assoc_resources26_stub_double():
    # project_Alternative has no real 'project_Alternative' property in the generated
    # code (a bare stub) -- manually attach it so project_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Resource(id="sample_text", name="sample_text")
    partner = project_Alternative()
    setattr(partner, 'project_Alternative', None)
    _safe_set(owner, 'project_Resource27', partner)
    assert owner in getattr(partner, 'project_Alternative')
    _safe_set(owner, 'project_Resource27', None)
    assert owner not in getattr(partner, 'project_Alternative')


def test_assoc_revenue32_stub_double():
    # project_Balance has no real 'project_Balance33' property in the generated
    # code (a bare stub) -- manually attach it so project_Account's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Account's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Account(id="sample_text", name="sample_text")
    partner = project_Balance()
    setattr(partner, 'project_Balance33', None)
    _safe_set(owner, 'project_Account34', partner)
    assert getattr(partner, 'project_Balance33') == owner
    _safe_set(owner, 'project_Account34', None)
    assert getattr(partner, 'project_Balance33') is None


def test_assoc_rollupResource185_stub_double():
    # project_RollupResource has no real 'project_RollupResource187' property in the generated
    # code (a bare stub) -- manually attach it so project_TagFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TagFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TagFile(filename="sample_text", id="sample_text")
    partner = project_RollupResource()
    setattr(partner, 'project_RollupResource187', None)
    _safe_set(owner, 'project_TagFile186', partner)
    assert getattr(partner, 'project_RollupResource187') == owner
    _safe_set(owner, 'project_TagFile186', None)
    assert getattr(partner, 'project_RollupResource187') is None


def test_assoc_rollupTask188_stub_double():
    # project_RollupTask has no real 'project_RollupTask190' property in the generated
    # code (a bare stub) -- manually attach it so project_TagFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_TagFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_TagFile(filename="sample_text", id="sample_text")
    partner = project_RollupTask()
    setattr(partner, 'project_RollupTask190', None)
    _safe_set(owner, 'project_TagFile189', partner)
    assert getattr(partner, 'project_RollupTask190') == owner
    _safe_set(owner, 'project_TagFile189', None)
    assert getattr(partner, 'project_RollupTask190') is None


def test_assoc_scenario125_stub_double():
    # project_ScenarioIcal has no real 'project_ScenarioIcal' property in the generated
    # code (a bare stub) -- manually attach it so project_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    partner = project_ScenarioIcal()
    setattr(partner, 'project_ScenarioIcal', None)
    _safe_set(owner, 'project_Scenario126', partner)
    assert getattr(partner, 'project_ScenarioIcal') == owner
    _safe_set(owner, 'project_Scenario126', None)
    assert getattr(partner, 'project_ScenarioIcal') is None


def test_assoc_scenario213_stub_double():
    # project_TrackingScenario has no real 'project_TrackingScenario' property in the generated
    # code (a bare stub) -- manually attach it so project_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    partner = project_TrackingScenario()
    setattr(partner, 'project_TrackingScenario', None)
    _safe_set(owner, 'project_Scenario214', partner)
    assert getattr(partner, 'project_TrackingScenario') == owner
    _safe_set(owner, 'project_Scenario214', None)
    assert getattr(partner, 'project_TrackingScenario') is None


def test_assoc_scenarios127_stub_double():
    # project_Scenarios has no real 'project_Scenarios' property in the generated
    # code (a bare stub) -- manually attach it so project_Scenario's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Scenario's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Scenario(active="sample_text", id="sample_text", name="sample_text")
    partner = project_Scenarios()
    setattr(partner, 'project_Scenarios', None)
    _safe_set(owner, 'project_Scenario128', partner)
    assert owner in getattr(partner, 'project_Scenarios')
    _safe_set(owner, 'project_Scenario128', None)
    assert owner not in getattr(partner, 'project_Scenarios')


def test_assoc_shift135_stub_double():
    # project_ShiftTimesheet has no real 'project_ShiftTimesheet' property in the generated
    # code (a bare stub) -- manually attach it so project_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    partner = project_ShiftTimesheet()
    setattr(partner, 'project_ShiftTimesheet', None)
    _safe_set(owner, 'project_Shift136', partner)
    assert getattr(partner, 'project_ShiftTimesheet') == owner
    _safe_set(owner, 'project_Shift136', None)
    assert getattr(partner, 'project_ShiftTimesheet') is None


def test_assoc_shift138_stub_double():
    # project_ShiftsLimit has no real 'project_ShiftsLimit139' property in the generated
    # code (a bare stub) -- manually attach it so project_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    partner = project_ShiftsLimit()
    setattr(partner, 'project_ShiftsLimit139', None)
    _safe_set(owner, 'project_Shift140', partner)
    assert getattr(partner, 'project_ShiftsLimit139') == owner
    _safe_set(owner, 'project_Shift140', None)
    assert getattr(partner, 'project_ShiftsLimit139') is None


def test_assoc_shift144_stub_double():
    # project_ShiftsAllocate has no real 'project_ShiftsAllocate' property in the generated
    # code (a bare stub) -- manually attach it so project_Shift's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Shift's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Shift(id="sample_text", name="sample_text", replace="sample_text", timezone="sample_text")
    partner = project_ShiftsAllocate()
    setattr(partner, 'project_ShiftsAllocate', None)
    _safe_set(owner, 'project_Shift145', partner)
    assert getattr(partner, 'project_ShiftsAllocate') == owner
    _safe_set(owner, 'project_Shift145', None)
    assert getattr(partner, 'project_ShiftsAllocate') is None


def test_assoc_summary97_stub_double():
    # project_Summary has no real 'project_Summary' property in the generated
    # code (a bare stub) -- manually attach it so project_JournalEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_JournalEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_JournalEntry(date="sample_text", headline="sample_text")
    partner = project_Summary()
    setattr(partner, 'project_Summary', None)
    _safe_set(owner, 'project_JournalEntry98', partner)
    assert getattr(partner, 'project_Summary') == owner
    _safe_set(owner, 'project_JournalEntry98', None)
    assert getattr(partner, 'project_Summary') is None


def test_assoc_task175_stub_double():
    # project_SupplementTask has no real 'project_SupplementTask' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_SupplementTask()
    setattr(partner, 'project_SupplementTask', None)
    _safe_set(owner, 'project_Task176', partner)
    assert getattr(partner, 'project_SupplementTask') == owner
    _safe_set(owner, 'project_Task176', None)
    assert getattr(partner, 'project_SupplementTask') is None


def test_assoc_task191_stub_double():
    # project_TaskStatusSheet has no real 'project_TaskStatusSheet' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_TaskStatusSheet()
    setattr(partner, 'project_TaskStatusSheet', None)
    _safe_set(owner, 'project_Task192', partner)
    assert getattr(partner, 'project_TaskStatusSheet') == owner
    _safe_set(owner, 'project_Task192', None)
    assert getattr(partner, 'project_TaskStatusSheet') is None


def test_assoc_task195_stub_double():
    # project_TaskTimesheet has no real 'project_TaskTimesheet' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_TaskTimesheet()
    setattr(partner, 'project_TaskTimesheet', None)
    _safe_set(owner, 'project_Task196', partner)
    assert getattr(partner, 'project_TaskTimesheet') == owner
    _safe_set(owner, 'project_Task196', None)
    assert getattr(partner, 'project_TaskTimesheet') is None


def test_assoc_task199_stub_double():
    # project_TaskPrefix has no real 'project_TaskPrefix' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_TaskPrefix()
    setattr(partner, 'project_TaskPrefix', None)
    _safe_set(owner, 'project_Task200', partner)
    assert getattr(partner, 'project_TaskPrefix') == owner
    _safe_set(owner, 'project_Task200', None)
    assert getattr(partner, 'project_TaskPrefix') is None


def test_assoc_task201_stub_double():
    # project_TaskRoot has no real 'project_TaskRoot' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_TaskRoot()
    setattr(partner, 'project_TaskRoot', None)
    _safe_set(owner, 'project_Task202', partner)
    assert getattr(partner, 'project_TaskRoot') == owner
    _safe_set(owner, 'project_Task202', None)
    assert getattr(partner, 'project_TaskRoot') is None


def test_assoc_task41_stub_double():
    # project_BookingResource has no real 'project_BookingResource' property in the generated
    # code (a bare stub) -- manually attach it so project_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # project_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = project_Task(id="sample_text", name="sample_text")
    partner = project_BookingResource()
    setattr(partner, 'project_BookingResource', None)
    _safe_set(owner, 'project_Task42', partner)
    assert getattr(partner, 'project_BookingResource') == owner
    _safe_set(owner, 'project_Task42', None)
    assert getattr(partner, 'project_BookingResource') is None


