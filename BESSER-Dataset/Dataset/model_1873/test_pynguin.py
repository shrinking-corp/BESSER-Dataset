#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    AccountAttribute,
    AccountReport,
    AlertLevel,
    AllocateResourceAttribute,
    BuildInMacro,
    Caption,
    Center,
    ChargeApplies,
    ColumnAttribute,
    ColumnId,
    CriterionDirection,
    CurrencyFormat,
    DailyMax,
    DailyMin,
    Definitions,
    DependsPolicy,
    Details,
    End,
    Enum,
    Epilog,
    ExportAttribute,
    ExtDate,
    Footer,
    GapDuration,
    GapLength,
    Header,
    Headline,
    IcalReportAttribute,
    IncludePropertiesAttribute,
    JournalAttributeValues,
    JournalEntrySortCriterion,
    JournalModeValue,
    Justification,
    LeaveType,
    Left,
    LimitsAttribute,
    ListItem,
    ListTypeValues,
    LoadDisplayUnit,
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
    PurgeReportAttribute,
    PurgeResourceAttribute,
    PurgeTaskAttribute,
    ReportAttribute,
    ReportFormat,
    ResourceAttribute,
    ResourceReport,
    Right,
    ScaleResolution,
    SchedulingPolicy,
    SelectArgument,
    ShiftsResource,
    ShiftsTask,
    SortAccounts,
    SortJournalEntries,
    SortResources,
    SortTasks,
    Start,
    StatusSheetAttribute,
    StatusSheetReportAttribute,
    StatusStatusSheetAttribute,
    StatusTimesheetAttribute,
    Summary,
    TaskReport,
    TaskStatusSheetAttribute,
    TaskTimesheetAttribute,
    TextReport,
    TimeUnit,
    TimesheetAttribute,
    TimesheetReportAttribute,
    Weekday,
    WeeklyMax,
    WeeklyMin,
    WorkQuantityUnit,
    YesNo,
    date,
    datetime,
    eTJ_Account,
    eTJ_AccountAttribute,
    eTJ_AccountPrefix,
    eTJ_AccountReport,
    eTJ_AccountRoot,
    eTJ_AccountShare,
    eTJ_Alert,
    eTJ_Allocate,
    eTJ_AllocateResource,
    eTJ_AllocateResourceAttribute,
    eTJ_Alternative,
    eTJ_Author,
    eTJ_Balance,
    eTJ_Booking,
    eTJ_BookingResource,
    eTJ_BookingTask,
    eTJ_Caption,
    eTJ_CellColor,
    eTJ_CellText,
    eTJ_Center,
    eTJ_Charge,
    eTJ_ChargeSet,
    eTJ_Column,
    eTJ_ColumnAttribute,
    eTJ_Columns,
    eTJ_Complete,
    eTJ_Copyright,
    eTJ_Credit,
    eTJ_Criterion,
    eTJ_Currency,
    eTJ_CurrencyFormat,
    eTJ_DailyMax,
    eTJ_DailyMin,
    eTJ_DailyWorkingHours,
    eTJ_Definitions,
    eTJ_Defintions,
    eTJ_Depends,
    eTJ_Details,
    eTJ_Duration,
    eTJ_DurationQuantity,
    eTJ_EObject,
    eTJ_Efficiency,
    eTJ_Effort,
    eTJ_Email,
    eTJ_End,
    eTJ_EndCredit,
    eTJ_Epilog,
    eTJ_Export,
    eTJ_ExportAttribute,
    eTJ_ExtDate,
    eTJ_Extend,
    eTJ_ExtendResource,
    eTJ_ExtendTask,
    eTJ_ExtendedResourceAttribute,
    eTJ_ExtendedResourceAttributeColumn,
    eTJ_ExtendedTaskAttribute,
    eTJ_Fail,
    eTJ_Flags,
    eTJ_FontColor,
    eTJ_Footer,
    eTJ_Formats,
    eTJ_Function,
    eTJ_GapDuration,
    eTJ_GapLength,
    eTJ_Global,
    eTJ_HAlign,
    eTJ_Header,
    eTJ_Headline,
    eTJ_HideAccount,
    eTJ_HideJournalEntry,
    eTJ_HideReport,
    eTJ_HideResource,
    eTJ_HideTask,
    eTJ_ISODATE,
    eTJ_IcalReport,
    eTJ_IcalReportAttribute,
    eTJ_Include,
    eTJ_IncludeProperties,
    eTJ_IncludePropertiesAttribute,
    eTJ_Interval1,
    eTJ_Interval2,
    eTJ_Interval3,
    eTJ_Interval4,
    eTJ_JournalAttributes,
    eTJ_JournalEntry,
    eTJ_JournalMode,
    eTJ_LeaveDetails,
    eTJ_Leaves,
    eTJ_Left,
    eTJ_Length,
    eTJ_Limit,
    eTJ_LimitAttribute,
    eTJ_Limits,
    eTJ_LimitsAttribute,
    eTJ_ListItem,
    eTJ_ListType,
    eTJ_LoadUnit,
    eTJ_LogicalAbsoluteIdExression,
    eTJ_LogicalBooleanLiteral,
    eTJ_LogicalDateLiteral,
    eTJ_LogicalExpression,
    eTJ_LogicalFlagExpression,
    eTJ_LogicalFunctionExpression,
    eTJ_LogicalNumeralLiteral,
    eTJ_LogicalStringLiteral,
    eTJ_Macro,
    eTJ_MacroCall,
    eTJ_Managers,
    eTJ_Mandatory,
    eTJ_MaxEnd,
    eTJ_MaxStart,
    eTJ_Maximum,
    eTJ_Milestone,
    eTJ_MinEnd,
    eTJ_MinStart,
    eTJ_Minimum,
    eTJ_MonthlyMax,
    eTJ_MonthlyMin,
    eTJ_Navigator,
    eTJ_NavigatorAttribute,
    eTJ_NewTask,
    eTJ_NewTaskAttribute,
    eTJ_NikuReport,
    eTJ_NikuReportAttribute,
    eTJ_Note,
    eTJ_Now,
    eTJ_NumberFormat,
    eTJ_Period,
    eTJ_Persistent,
    eTJ_Precedes,
    eTJ_Priority,
    eTJ_Project,
    eTJ_ProjectAttribute,
    eTJ_ProjectId,
    eTJ_ProjectIds,
    eTJ_Prolog,
    eTJ_Property,
    eTJ_PurgeReport,
    eTJ_PurgeResource,
    eTJ_PurgeTask,
    eTJ_RGB,
    eTJ_Rate,
    eTJ_RealFormat,
    eTJ_Remaining,
    eTJ_Report,
    eTJ_ReportAttribute,
    eTJ_ReportPrefix,
    eTJ_Resource,
    eTJ_ResourceAttribute,
    eTJ_ResourceAttributes,
    eTJ_ResourcePrefix,
    eTJ_ResourceReport,
    eTJ_ResourceRoot,
    eTJ_Responsible,
    eTJ_RichText,
    eTJ_Right,
    eTJ_RollupAccount,
    eTJ_RollupResource,
    eTJ_RollupTask,
    eTJ_Scale,
    eTJ_Scenario,
    eTJ_ScenarioIcal,
    eTJ_Scenarios,
    eTJ_Scheduled,
    eTJ_Scheduling,
    eTJ_Select,
    eTJ_SelfContained,
    eTJ_Shift,
    eTJ_ShiftTimesheet,
    eTJ_Shifts,
    eTJ_ShiftsAllocate,
    eTJ_ShiftsLimit,
    eTJ_ShiftsResource,
    eTJ_ShiftsTask,
    eTJ_ShortTimeFormat,
    eTJ_Sort,
    eTJ_SortAccounts,
    eTJ_SortJournalEntries,
    eTJ_SortResources,
    eTJ_SortTasks,
    eTJ_Start,
    eTJ_StatusSheet,
    eTJ_StatusSheetAttribute,
    eTJ_StatusSheetReport,
    eTJ_StatusSheetReportAttribute,
    eTJ_StatusStatusSheet,
    eTJ_StatusStatusSheetAttribute,
    eTJ_StatusTimesheet,
    eTJ_StatusTimesheetAttribute,
    eTJ_Summary,
    eTJ_SupplementAccount,
    eTJ_SupplementReport,
    eTJ_SupplementResource,
    eTJ_SupplementTask,
    eTJ_TagFile,
    eTJ_Task,
    eTJ_TaskAttribute,
    eTJ_TaskAttributes,
    eTJ_TaskDependency,
    eTJ_TaskPrefix,
    eTJ_TaskReport,
    eTJ_TaskRoot,
    eTJ_TaskStatusSheet,
    eTJ_TaskStatusSheetAttribute,
    eTJ_TaskTimesheet,
    eTJ_TaskTimesheetAttribute,
    eTJ_TextReport,
    eTJ_TimeFormat,
    eTJ_Timeoff,
    eTJ_Timesheet,
    eTJ_TimesheetAttribute,
    eTJ_TimesheetReport,
    eTJ_TimesheetReportAttribute,
    eTJ_Timezone,
    eTJ_TimingResolution,
    eTJ_Title,
    eTJ_ToolTip,
    eTJ_TrackingScenario,
    eTJ_TreeLevel,
    eTJ_Vacation,
    eTJ_Warn,
    eTJ_WeekStarts,
    eTJ_Weekdays,
    eTJ_WeeklyMax,
    eTJ_WeeklyMin,
    eTJ_Width,
    eTJ_Work,
    eTJ_WorkHours,
    eTJ_WorkingHours,
    eTJ_YearlyWorkingDays,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_2 = "KK$BiXsP\x0bX._*ZOO g"
    var_3 = '#AAC"F{qdUt=|<&wQn'
    var_4 = python_code_.eTJ_SupplementReport()
    var_5 = python_code_.eTJ_Report(id=var_2, name=var_3, eTJ_Report231=var_4)
    assert isinstance(var_5, python_code_.eTJ_Report)
    var_7 = python_code_.eTJ_AccountRoot()
    var_8 = "eTJ_StatusSheet eTJ_TimesheetReportAttribute"
    var_9 = "Xkc"
    var_10 = ";umYzcecKZb1UI"
    var_11 = python_code_.eTJ_RealFormat(
        negativeSuffix=var_8,
        thousandsSeparator=var_9,
        fractionSeparator=var_10,
        fractionDigits=None,
        negativePrefix=var_8,
    )
    assert isinstance(var_11, python_code_.eTJ_RealFormat)
    var_13 = 349
    var_14 = python_code_.eTJ_YearlyWorkingDays(yearlyWorkingDays=var_13)
    assert isinstance(var_14, python_code_.eTJ_YearlyWorkingDays)
    var_16 = "fgD1pam/3Xp3~D"
    var_17 = python_code_.eTJ_SupplementTask()
    var_18 = python_code_.eTJ_Task(
        id=var_7, name=var_16, eTJ_Task320=var_13, eTJ_Task241=var_17
    )
    assert isinstance(var_18, python_code_.eTJ_Task)
    python_code_.eTJ_Function(
        level=var_13, parentId=var_14, distance=var_13, eTJ_Function83=var_18
    )


def test_1():
    var_0 = python_code_.IncludePropertiesAttribute()
    var_2 = python_code_.eTJ_ProjectAttribute
    var_3 = "7jhQjmg\x0cT{zn"
    var_4 = True
    var_5 = python_code_.eTJ_Extend(
        name=var_2,
        description=var_3,
        inherit=var_4,
        scenariospecific=var_0,
        eTJ_Extend72=[-2833.91, False],
    )
    assert isinstance(var_5, python_code_.eTJ_Extend)
    var_7 = 1834.73
    var_8 = python_code_.eTJ_ISODATE()
    var_9 = python_code_.eTJ_DurationQuantity(
        value=var_7,
        unit=var_3,
        eTJ_DurationQuantity131=complex(209.267, 2226.66),
        eTJ_DurationQuantity={"o?ay+w-9BF '0(rX)"},
        eTJ_DurationQuantity329=var_8,
    )
    assert isinstance(var_9, python_code_.eTJ_DurationQuantity)
    python_code_.eTJ_PurgeTask(listAttribute=set())
    var_13 = -988.77
    var_14 = python_code_.eTJ_Width(width=var_13)
    assert isinstance(var_14, python_code_.eTJ_Width)
    var_15 = python_code_.TaskTimesheetAttribute
    python_code_.eTJ_Extend(
        name=var_15, description=var_15, inherit=var_9, scenariospecific=var_4
    )
    var_23 = python_code_.eTJ_Work(
        value=var_7, unit=b"Yt<\xa4\xfc\x9eV\x1bN\xc6Q5 \xd6"
    )
    assert isinstance(var_23, python_code_.eTJ_Work)


def test_2():
    var_1 = python_code_.eTJ_Remaining()
    python_code_.eTJ_RGB(value=set())
    var_6 = 3
    var_7 = python_code_.eTJ_Priority(priority=var_6)
    assert isinstance(var_7, python_code_.eTJ_Priority)
    var_8 = False
    var_9 = python_code_.eTJ_Scheduled(scheduled=var_8)
    var_10 = python_code_.eTJ_ReportPrefix()
    var_11 = python_code_.eTJ_Report(id=var_7, name=var_9)
    assert isinstance(var_11, python_code_.eTJ_Report)
    var_14 = python_code_.Details()
    var_15 = False
    var_16 = python_code_.eTJ_Remaining
    var_17 = False
    var_18 = False
    var_19 = False
    var_20 = python_code_.eTJ_TaskAttributes(
        all=var_14,
        none=var_8,
        responsible=var_15,
        flags=var_16,
        maxstart=var_17,
        maxend=var_10,
        priority=var_1,
        booking=None,
        note=[1406.0],
        minstart={},
        minend=var_18,
        complete=var_8,
        depends=var_19,
    )
    assert isinstance(var_20, python_code_.eTJ_TaskAttributes)
    var_29 = python_code_.eTJ_Select(argument={True, -752.27})
    assert isinstance(var_29, python_code_.eTJ_Select)
    var_30 = lambda *args, **kwargs: False
    var_31 = python_code_.eTJ_Scale(scale=var_30)
    assert isinstance(var_31, python_code_.eTJ_Scale)
    python_code_.eTJ_ProjectId(projectId={True, -2054, 486.99})
    var_35 = python_code_.eTJ_Mandatory(mandatory=var_30)
    assert isinstance(var_35, python_code_.eTJ_Mandatory)
    var_38 = 2027.81
    python_code_.eTJ_EndCredit(credit=var_38)


def test_3():
    var_0 = python_code_.eTJ_CellText(text=(), eTJ_CellText='\nSJ\x0clTfU"mUj%YiJ`')
    assert isinstance(var_0, python_code_.eTJ_CellText)
    var_3 = "CY$qwwlvi#"
    var_4 = python_code_.eTJ_IncludeProperties(importURI=var_3)
    assert isinstance(var_4, python_code_.eTJ_IncludeProperties)


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = python_code_.ColumnId.balance
    var_1 = python_code_.eTJ_Limits()
    var_5 = python_code_.eTJ_Efficiency(efficiency=var_0)
    assert isinstance(var_5, python_code_.eTJ_Efficiency)
    var_8 = python_code_.eTJ_Persistent(persistent=[True, 782.92, -1342.12])
    assert isinstance(var_8, python_code_.eTJ_Persistent)
    var_9 = "HOUR:SORTRESOURCES:JOURNAL_SUB:_eTJ_ExtendedResourceAttribute__eTJ_ExtendedResourceAttribute"
    python_code_.eTJ_PurgeTask(listAttribute=var_9)
    var_14 = python_code_.eTJ_WeekStarts(sunday=var_8, monday=var_0)
    assert isinstance(var_14, python_code_.eTJ_WeekStarts)
    var_16 = python_code_.eTJ_Vacation(name=var_1)
    assert isinstance(var_16, python_code_.eTJ_Vacation)
    var_22 = "note"
    var_23 = python_code_.eTJ_SupplementReport()
    var_24 = python_code_.eTJ_Report(
        id=b"nP\xb0+[\xdb\xfe\x0c\xac;0\xaf:t\xffK\xa6",
        name=var_22,
        eTJ_Report231=var_23,
    )
    assert isinstance(var_24, python_code_.eTJ_Report)
    var_26 = python_code_.eTJ_HAlign(justification=",Oy\tN$xfJ^k/OLclOn")
    assert isinstance(var_26, python_code_.eTJ_HAlign)
    var_27 = python_code_.eTJ_BookingResource()
    var_28 = python_code_.eTJ_TaskPrefix()
    var_29 = python_code_.eTJ_TaskRoot()
    var_30 = python_code_.eTJ_Task(
        id=var_9,
        name=5472.41,
        eTJ_Task50=var_27,
        eTJ_Task265=var_28,
        eTJ_Task267=var_29,
    )
    assert isinstance(var_30, python_code_.eTJ_Task)
    python_code_.eTJ_TaskDependency(policy=var_22, eTJ_TaskDependency319=var_30)


def test_5():
    var_2 = True
    var_3 = False
    var_4 = True
    var_5 = True
    var_6 = python_code_.eTJ_ResourceAttributes(
        all=var_2, none=var_3, vacation=var_3, booking=var_4, workingHours=var_5
    )
    assert isinstance(var_6, python_code_.eTJ_ResourceAttributes)
    var_11 = python_code_.eTJ_ShiftsLimit()
    var_13 = ""
    python_code_.eTJ_WorkHours(start=1150.23, stop=var_13)
    var_16 = "v][kow<%\x0bl\x0cRJ"
    var_17 = python_code_.eTJ_StatusStatusSheet(level=var_16, text=var_16)
    assert isinstance(var_17, python_code_.eTJ_StatusStatusSheet)
    var_21 = python_code_.ExportAttribute
    python_code_.eTJ_Account(id=var_13, name=var_11, eTJ_Account39=var_21)
    python_code_.eTJ_IcalReport(filename=118.87)
    var_26 = python_code_.eTJ_GapDuration()
    var_27 = "eTJ_LogicalExpression58:eTJ_Author:COMMA"
    var_28 = python_code_.eTJ_Report(id=var_27, name=var_13, eTJ_Report231=var_26)
    assert isinstance(var_28, python_code_.eTJ_Report)


def test_6():
    var_1 = python_code_.eTJ_JournalAttributes(args=-929.69)
    assert isinstance(var_1, python_code_.eTJ_JournalAttributes)
    var_3 = python_code_.IncludePropertiesAttribute()
    var_5 = "activetasks eTJ_Warn _eTJ_Scenario__eTJ_Scenario191"
    var_6 = python_code_.eTJ_Navigator(id=var_5)
    var_7 = "=qY]4"
    python_code_.eTJ_Project(id=var_3, name=var_7, version=var_5, eTJ_Project12=var_7)
    python_code_.eTJ_Rate(rate=None)
    var_15 = "ZZ^JZZZi'~ E\"F"
    python_code_.eTJ_Copyright(text=var_15)
    var_17 = python_code_.eTJ_Columns()
    var_18 = python_code_.eTJ_TimeFormat(timeformat=var_15)
    assert isinstance(var_18, python_code_.eTJ_TimeFormat)
    var_19 = python_code_.eTJ_JournalEntry(headline=var_5, eTJ_JournalEntry142=var_17)
    assert isinstance(var_19, python_code_.eTJ_JournalEntry)
    var_21 = python_code_.eTJ_ScenarioIcal()
    var_22 = "eTJ_HideResource246-ONSTART"
    var_23 = python_code_.ExtDate
    var_24 = python_code_.eTJ_RealFormat(
        negativeSuffix=var_15,
        thousandsSeparator=var_22,
        fractionSeparator=var_23,
        fractionDigits=var_23,
        negativePrefix=var_5,
    )
    assert isinstance(var_24, python_code_.eTJ_RealFormat)
    python_code_.eTJ_Flags(flags=var_21)
    python_code_.eTJ_ProjectIds(ids=var_6)


def test_7():
    var_3 = python_code_.eTJ_Epilog()
    python_code_.eTJ_Milestone(milestone=None)
    var_7 = python_code_.eTJ_SelfContained(selfcontained=var_3)
    assert isinstance(var_7, python_code_.eTJ_SelfContained)
    var_11 = python_code_.eTJ_ResourceReport()
    var_12 = python_code_.ScaleResolution.DAY
    var_16 = python_code_.eTJ_Select(argument=var_12)
    assert isinstance(var_16, python_code_.eTJ_Select)
    var_24 = python_code_.eTJ_ToolTip(tip="35Y?")
    assert isinstance(var_24, python_code_.eTJ_ToolTip)
    var_27 = 2845.5
    python_code_.eTJ_Complete(complete=var_27)
    var_33 = python_code_.eTJ_ListType(type=var_11)
    assert isinstance(var_33, python_code_.eTJ_ListType)
    var_34 = "eTJ_LogicalStringLiteral"
    python_code_.eTJ_Project(id=[], name=var_34, version=None)
    var_36 = lambda *args, **kwargs: "ts.e8'\"5w1^"
    python_code_.eTJ_Navigator(id=var_36)


def test_8():
    var_0 = "eTJ_LimitAttribute"
    var_1 = python_code_.eTJ_FontColor(color=var_0)
    assert isinstance(var_1, python_code_.eTJ_FontColor)


def test_9():
    var_1 = python_code_.eTJ_SupplementTask()
    var_3 = python_code_.ColumnId.minstart
    var_7 = "complete.line"
    var_8 = python_code_.eTJ_TimeFormat(timeformat=var_7)
    assert isinstance(var_8, python_code_.eTJ_TimeFormat)
    var_10 = python_code_.eTJ_StatusStatusSheetAttribute()
    var_11 = python_code_.SortResources
    var_12 = True
    var_13 = python_code_.eTJ_TaskAttributes(
        all=var_10,
        none=var_3,
        responsible=var_11,
        flags=1999.37,
        maxstart=complex(-582.605, -592.28188),
        maxend=var_12,
        priority=(1004.0,),
        booking=var_3,
        note=var_12,
        minstart=var_1,
        minend=var_12,
        complete=var_12,
        depends=377.22,
    )
    assert isinstance(var_13, python_code_.eTJ_TaskAttributes)
