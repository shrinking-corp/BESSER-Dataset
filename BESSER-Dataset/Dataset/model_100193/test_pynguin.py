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
    ABC,
    BaseTable,
    BehaviouralComponent,
    BinaryStringTypes,
    BooleanTypes,
    CharacterStringTypes,
    CollectionType,
    ColumnConstraint,
    ConstructedType,
    DataType,
    DatetimeFeatures,
    DatetimeTypes,
    DerivedTable,
    Enum,
    Feature,
    IntervalFeatures,
    IntervalTypes,
    MatchTypes,
    Multiplier,
    NumericFeatures,
    NumericRadix,
    NumericTypes,
    Parameter,
    ParameterMode,
    PredefinedType,
    ReferentialAction,
    Restriction,
    SQL2003_evo_ARRAY,
    SQL2003_evo_Attribute,
    SQL2003_evo_BaseTable,
    SQL2003_evo_BehaviouralComponent,
    SQL2003_evo_BinaryStringType,
    SQL2003_evo_BooleanType,
    SQL2003_evo_CharacterStringType,
    SQL2003_evo_CollectionType,
    SQL2003_evo_Column,
    SQL2003_evo_ColumnConstraint,
    SQL2003_evo_ConstructedType,
    SQL2003_evo_DataType,
    SQL2003_evo_DatetimeFeature,
    SQL2003_evo_DatetimeType,
    SQL2003_evo_DerivedTable,
    SQL2003_evo_DistinctType,
    SQL2003_evo_Feature,
    SQL2003_evo_Field,
    SQL2003_evo_Function,
    SQL2003_evo_IntervalFeature,
    SQL2003_evo_IntervalType,
    SQL2003_evo_MULTISET,
    SQL2003_evo_Method,
    SQL2003_evo_MethodParameter,
    SQL2003_evo_NotNull,
    SQL2003_evo_NumericFeature,
    SQL2003_evo_NumericType,
    SQL2003_evo_Parameter,
    SQL2003_evo_ParameterWithMode,
    SQL2003_evo_PredefinedType,
    SQL2003_evo_PrimaryKey,
    SQL2003_evo_Procedure,
    SQL2003_evo_ROW,
    SQL2003_evo_ReferenceType,
    SQL2003_evo_ReferentialConstraint,
    SQL2003_evo_Restriction,
    SQL2003_evo_Schema,
    SQL2003_evo_StringFeature,
    SQL2003_evo_StructuralComponent,
    SQL2003_evo_StructuredType,
    SQL2003_evo_Table,
    SQL2003_evo_TableCheckConstraint,
    SQL2003_evo_TableConstraint,
    SQL2003_evo_Trigger,
    SQL2003_evo_TriggerDescriptor,
    SQL2003_evo_TypedTable,
    SQL2003_evo_UniqueConstraint,
    SQL2003_evo_UserDefinedType,
    SQL2003_evo_View,
    SQL2003_evo_XMLType,
    StringFeatures,
    StructuralComponent,
    Table,
    TableConstraint,
    TriggerActionTime,
    TriggerEvent,
    TriggerLevel,
    UniqueConstraint,
    Unit,
    UserDefinedType,
    XMLTypes,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_42 = "TQ)^G"
    var_44 = "DTN0\rn~*s"
    var_45 = python_code_.SQL2003_evo_TriggerDescriptor(
        event={-1433, True},
        actionTime=var_42,
        triggeredAction=var_42,
        level=var_44,
        TriggerDescriptor=var_44,
    )
    assert isinstance(var_45, python_code_.SQL2003_evo_TriggerDescriptor)


def test_1():
    var_0 = python_code_.SQL2003_evo_Field()
    var_1 = 'XqbJKv8"}_l'
    var_2 = python_code_.SQL2003_evo_ReferentialConstraint(
        delete_action=var_1,
        update_action=var_0,
        match=var_1,
        SQL2003_evo_ReferentialConstraint=var_0,
    )
    assert isinstance(var_2, python_code_.SQL2003_evo_ReferentialConstraint)


@pytest.mark.xfail(strict=True)
def test_2():
    var_0 = python_code_.SQL2003_evo_DistinctType()
    var_1 = "[3x=bfmJ/"
    var_2 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=var_1, parametersWithMode=var_1
    )
    assert isinstance(var_2, python_code_.SQL2003_evo_ParameterWithMode)
    var_5 = python_code_.UniqueConstraint
    var_6 = python_code_.SQL2003_evo_ConstructedType(name=var_5)
    assert isinstance(var_6, python_code_.SQL2003_evo_ConstructedType)
    python_code_.SQL2003_evo_ParameterWithMode(mode=var_1)
    var_12 = python_code_.SQL2003_evo_DistinctType()
    var_14 = python_code_.MatchTypes.TOTAL
    var_15 = python_code_.SQL2003_evo_Restriction()
    var_16 = {var_15, var_15, var_15, var_15}
    var_17 = set()
    var_18 = python_code_.SQL2003_evo_Table(
        name=var_5, Table38=var_15, table72=var_16, table=var_17, Table87=var_14
    )
    assert isinstance(var_18, python_code_.SQL2003_evo_Table)
    var_19 = python_code_.SQL2003_evo_CharacterStringType(
        descriptor=var_1, length_def=var_12
    )
    assert isinstance(var_19, python_code_.SQL2003_evo_CharacterStringType)
    var_20 = "BINARYK_SQL2003_evo_Method__Method62KlengthK_SQL2003_evo_Table__Table47"
    var_21 = "^Wsoq\x0c\x0b=AM|P<i"
    var_22 = python_code_.SQL2003_evo_ReferentialConstraint(
        delete_action=var_20, update_action=var_14, match=var_21
    )
    assert isinstance(var_22, python_code_.SQL2003_evo_ReferentialConstraint)
    var_23 = python_code_.SQL2003_evo_BehaviouralComponent(name=var_1, body=var_21)
    assert isinstance(var_23, python_code_.SQL2003_evo_BehaviouralComponent)
    var_25 = "#DzW1;HzGma\x0b/pNT\x0c"
    python_code_.SQL2003_evo_Schema(
        name=var_25, schema=var_0, schema44=var_5, schema46=var_16, Schema66=var_18
    )


def test_3():
    var_48 = abs
    var_49 = python_code_.SQL2003_evo_BooleanType(descriptor=var_48)
    assert isinstance(var_49, python_code_.SQL2003_evo_BooleanType)
    var_51 = "\r@]\n%fE,ub/H K'\x0c3"
    var_52 = python_code_.SQL2003_evo_DataType()
    var_53 = set()
    var_58 = "4P{Dfpt8R7\\o<H)"
    var_59 = python_code_.SQL2003_evo_StringFeature(key=var_58, value=var_51)
    assert isinstance(var_59, python_code_.SQL2003_evo_StringFeature)
    var_60 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=".TvFMW(6LvJ\r", ParameterWithMode=None, parametersWithMode=var_58
    )
    assert isinstance(var_60, python_code_.SQL2003_evo_ParameterWithMode)
    var_71 = "SQL2003_evo_Restriction"
    var_72 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_71)
    assert isinstance(var_72, python_code_.SQL2003_evo_DerivedTable)
    var_77 = python_code_.SQL2003_evo_Table(
        name=var_71, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )
    assert isinstance(var_77, python_code_.SQL2003_evo_Table)
    var_81 = python_code_.SQL2003_evo_StructuralComponent(
        name=var_71, SQL2003_evo_StructuralComponent=var_52, components=var_53
    )
    assert isinstance(var_81, python_code_.SQL2003_evo_StructuralComponent)


def test_4():
    var_7 = python_code_.SQL2003_evo_Feature()
    var_8 = {var_7, var_7, var_7, var_7, var_7}
    var_9 = python_code_.SQL2003_evo_StructuralComponent(
        name=None, SQL2003_evo_StructuralComponent54=var_8
    )
    assert isinstance(var_9, python_code_.SQL2003_evo_StructuralComponent)


@pytest.mark.xfail(strict=True)
def test_5():
    var_0 = ')cJX\x0b"e\nB-o'
    var_1 = python_code_.SQL2003_evo_StringFeature(key=var_0, value=var_0)
    assert isinstance(var_1, python_code_.SQL2003_evo_StringFeature)
    var_3 = python_code_.SQL2003_evo_BinaryStringType(
        descriptor=var_1, length_def="G.P._SQL2003_evo_Table__tables.trigger"
    )
    assert isinstance(var_3, python_code_.SQL2003_evo_BinaryStringType)
    var_4 = python_code_.SQL2003_evo_XMLType(descriptor=[0, -2172, 0])
    assert isinstance(var_4, python_code_.SQL2003_evo_XMLType)
    var_7 = lambda *args, **kwargs: True
    python_code_.SQL2003_evo_Method(
        name=True,
        body=var_0,
        SQL2003_evo_Method20=b"5\xca\xc5",
        method=-1139.58,
        Method62=var_7,
    )


def test_6():
    var_2 = abs
    var_3 = python_code_.SQL2003_evo_BooleanType(descriptor=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_BooleanType)
    var_6 = python_code_.SQL2003_evo_Attribute(
        default="K|.u.7k3=9;xeG*\\L,", attributes=None
    )
    assert isinstance(var_6, python_code_.SQL2003_evo_Attribute)
    python_code_.SQL2003_evo_Method(
        name=var_3,
        body={
            -1989,
            "OUTMPM_SQL2003_evo_StructuralComponent__SQL2003_evo_StructuralComponent",
        },
    )
    var_80 = 'TD"+'
    var_81 = python_code_.SQL2003_evo_ConstructedType(name=var_80)
    assert isinstance(var_81, python_code_.SQL2003_evo_ConstructedType)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.SQL2003_evo_CollectionType()
    var_2 = abs
    var_3 = python_code_.SQL2003_evo_BooleanType(descriptor=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_BooleanType)
    var_6 = python_code_.SQL2003_evo_Attribute(default="Suh.?", Attribute=None)
    assert isinstance(var_6, python_code_.SQL2003_evo_Attribute)
    var_8 = "TriggerDescriptorKSQL2003_evo_UniqueConstraint"
    var_9 = python_code_.SQL2003_evo_Method(
        name=var_3,
        body={
            -1989,
            "OUTMPM_SQL2003_evo_StructuralComponent__SQL2003_evo_StructuralComponent",
        },
    )
    python_code_.SQL2003_evo_Method(
        name=b"\xe3\x198.\xf9h#",
        body=var_8,
        SQL2003_evo_Method=var_9,
        SQL2003_evo_Method15=var_0,
        Method62=var_2,
    )


def test_8():
    var_0 = python_code_.SQL2003_evo_ARRAY(num_elements=-3292)
    assert isinstance(var_0, python_code_.SQL2003_evo_ARRAY)
    var_1 = python_code_.SQL2003_evo_TableConstraint(name=var_0)
    assert isinstance(var_1, python_code_.SQL2003_evo_TableConstraint)
    var_4 = python_code_.SQL2003_evo_Restriction()
    var_5 = python_code_.SQL2003_evo_View()
    var_6 = {var_5, var_5, var_5}
    var_7 = python_code_.SQL2003_evo_Table(
        name={
            "m]%zl^WvHG&:`aBV_di": 444.77,
            "DATEPINOUTPSQL2003_evo_StructuredType58PTIMESTAMPWITHOUTTIMEZONE": 4634,
        },
        Table38=var_4,
        tables69=var_6,
        table72=set(),
        Table87=var_5,
    )
    assert isinstance(var_7, python_code_.SQL2003_evo_Table)


def test_9():
    var_4 = "syFmlDg"
    var_5 = python_code_.SQL2003_evo_ConstructedType(name=var_4)
    assert isinstance(var_5, python_code_.SQL2003_evo_ConstructedType)
    var_10 = python_code_.SQL2003_evo_Table(
        name=var_4, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )
    assert isinstance(var_10, python_code_.SQL2003_evo_Table)


@pytest.mark.xfail(strict=True)
def test_10():
    var_1 = "IN"
    var_2 = python_code_.SQL2003_evo_ARRAY(num_elements=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_ARRAY)
    var_3 = python_code_.SQL2003_evo_ParameterWithMode(
        mode="WVPT.awD@", parametersWithMode=None
    )
    assert isinstance(var_3, python_code_.SQL2003_evo_ParameterWithMode)
    var_4 = python_code_.SQL2003_evo_DataType
    var_5 = {var_3, var_3, var_3, var_3, var_4}
    var_6 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_4,
        body=(False, "#[r5PUbZOC/Vo4]", False),
        behaviouralComponent=var_5,
        BehaviouralComponent=var_4,
    )
    assert isinstance(var_6, python_code_.SQL2003_evo_BehaviouralComponent)
    var_8 = python_code_.SQL2003_evo_Column(default=None)
    assert isinstance(var_8, python_code_.SQL2003_evo_Column)
    python_code_.SQL2003_evo_Table(
        name=complex(-1478.0, -1746.0),
        Table=var_8,
        Table38=var_4,
        Table47=var_4,
        table72=var_2,
        table=var_5,
        Table87=complex(-3535.11, 2075.643382),
    )


@pytest.mark.xfail(strict=True)
def test_11():
    var_1 = "IN"
    var_2 = python_code_.SQL2003_evo_ARRAY(num_elements=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_ARRAY)
    var_3 = python_code_.SQL2003_evo_ParameterWithMode(mode=var_1)
    assert isinstance(var_3, python_code_.SQL2003_evo_ParameterWithMode)
    var_4 = python_code_.SQL2003_evo_DataType
    var_5 = {var_3, var_3, var_3, var_3}
    var_6 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_4,
        body=(False, "#[r5PUbZOC/Vo4]", False),
        behaviouralComponent=var_5,
        BehaviouralComponent=var_4,
    )
    assert isinstance(var_6, python_code_.SQL2003_evo_BehaviouralComponent)
    var_7 = python_code_.SQL2003_evo_ParameterWithMode(mode=[], ParameterWithMode=var_6)
    var_8 = python_code_.SQL2003_evo_Column(default="\tX\rc{bcRK+W", Column=var_7)
    assert isinstance(var_8, python_code_.SQL2003_evo_Column)
    python_code_.SQL2003_evo_Table(
        name=complex(-1478.0, -1746.0),
        Table=var_8,
        Table38=var_4,
        Table47=var_4,
        table72=var_2,
        table=var_5,
        Table87=complex(-3535.11, 2075.643382),
    )


def test_12():
    var_1 = "IN"
    var_2 = python_code_.SQL2003_evo_ARRAY(num_elements=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_ARRAY)
    var_3 = python_code_.SQL2003_evo_ParameterWithMode(mode=var_1)
    assert isinstance(var_3, python_code_.SQL2003_evo_ParameterWithMode)


def test_13():
    var_1 = "IN"
    var_2 = python_code_.SQL2003_evo_ARRAY(num_elements=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_ARRAY)
    var_3 = python_code_.SQL2003_evo_ParameterWithMode(mode=var_1)
    assert isinstance(var_3, python_code_.SQL2003_evo_ParameterWithMode)
    var_4 = python_code_.SQL2003_evo_DataType
    var_5 = {var_3, var_3, var_3, var_3}
    var_6 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_4,
        body=(False, "#[r5PUbZOC/Vo4]", False),
        behaviouralComponent=var_5,
        BehaviouralComponent=var_4,
    )
    assert isinstance(var_6, python_code_.SQL2003_evo_BehaviouralComponent)
    var_21 = python_code_.SQL2003_evo_ConstructedType(name=var_1)
    assert isinstance(var_21, python_code_.SQL2003_evo_ConstructedType)


def test_14():
    var_2 = abs
    var_3 = python_code_.SQL2003_evo_BooleanType(descriptor=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_BooleanType)
    var_7 = "\r@]\n%fE,ub/H K'\x0c3"
    var_25 = "4P{Dfpt8R7\\o<H)"
    var_26 = python_code_.SQL2003_evo_StringFeature(key=var_25, value=var_7)
    assert isinstance(var_26, python_code_.SQL2003_evo_StringFeature)
    var_27 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=".TvFMW(6LvJ\r", ParameterWithMode=None, parametersWithMode=var_25
    )
    assert isinstance(var_27, python_code_.SQL2003_evo_ParameterWithMode)
    var_83 = python_code_.SQL2003_evo_ConstructedType(name=var_25)
    assert isinstance(var_83, python_code_.SQL2003_evo_ConstructedType)


def test_15():
    var_1 = "e%/{eU\\bB"
    var_13 = python_code_.SQL2003_evo_NumericFeature(key=var_1, value=var_1)
    assert isinstance(var_13, python_code_.SQL2003_evo_NumericFeature)
    var_14 = {988.27}
    var_15 = python_code_.SQL2003_evo_Table(
        name=complex(1768.9767, -1886.8708), table72=var_14
    )
    assert isinstance(var_15, python_code_.SQL2003_evo_Table)
    var_16 = python_code_.SQL2003_evo_Column(default="")
    assert isinstance(var_16, python_code_.SQL2003_evo_Column)
    var_17 = "_SQL2003_evo_Table__Table"
    var_18 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_17, body=var_17, behaviouralComponents=var_1
    )
    assert isinstance(var_18, python_code_.SQL2003_evo_BehaviouralComponent)
    var_20 = True
    var_21 = python_code_.SQL2003_evo_StructuredType(
        is_final=var_20,
        is_instantiable=var_20,
        SQL2003_evo_StructuredType=var_1,
        StructuredType79=var_17,
    )
    assert isinstance(var_21, python_code_.SQL2003_evo_StructuredType)
    python_code_.SQL2003_evo_Schema(name="dhN8y`WxE9ls-", schema=var_14)


@pytest.mark.xfail(strict=True)
def test_16():
    var_4 = "Z4ew]VreQs&55<,:"
    var_5 = "_SQL2003_evo_Method__method MethodParameter OUT views89"
    var_6 = "SQL2003_evo_BehaviouralComponentKSQL2003_evo_Feature55K_SQL2003_evo_StructuralComponent__columns52KYEAR"
    var_7 = "MethodParameterK_SQL2003_evo_StructuredType__structuredK_SQL2003_evo_Attribute__Attribute"
    var_8 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_5,
        body=var_7,
        behaviouralComponents=var_6,
        BehaviouralComponent=(
            -1438,
            "SQL2003_evo_BehaviouralComponentP_SQL2003_evo_Column__Column",
        ),
    )
    assert isinstance(var_8, python_code_.SQL2003_evo_BehaviouralComponent)
    var_9 = {var_8, var_8, var_8}
    var_10 = python_code_.SQL2003_evo_Schema(name=var_6, schema=var_9)
    python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_4, body=var_5, behaviouralComponents=var_10, behaviouralComponent=var_9
    )


def test_17():
    var_8 = python_code_.SQL2003_evo_Column(default=None)
    assert isinstance(var_8, python_code_.SQL2003_evo_Column)


def test_18():
    var_2 = abs
    var_3 = python_code_.SQL2003_evo_BooleanType(descriptor=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_BooleanType)
    var_6 = python_code_.SQL2003_evo_Attribute(default="Suh.?", Attribute=None)
    assert isinstance(var_6, python_code_.SQL2003_evo_Attribute)
    var_88 = "TQ)^G"
    var_90 = "DTN0\rn~*s"
    var_91 = python_code_.SQL2003_evo_TriggerDescriptor(
        event={-1433, True},
        actionTime=var_88,
        triggeredAction=var_88,
        level=var_90,
        TriggerDescriptor=var_90,
    )
    assert isinstance(var_91, python_code_.SQL2003_evo_TriggerDescriptor)


def test_19():
    var_8 = python_code_.SQL2003_evo_Column(default=None)
    assert isinstance(var_8, python_code_.SQL2003_evo_Column)
    var_26 = "6]H4>Ss2SV$,"
    var_27 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_26)
    assert isinstance(var_27, python_code_.SQL2003_evo_DerivedTable)
    var_33 = python_code_.DerivedTable()
    var_35 = "b(j,Dt-MhFWles"
    var_36 = python_code_.SQL2003_evo_NumericType(descriptor=var_35)
    assert isinstance(var_36, python_code_.SQL2003_evo_NumericType)
    var_41 = python_code_.SQL2003_evo_Attribute(default="table", attributes=var_33)
    assert isinstance(var_41, python_code_.SQL2003_evo_Attribute)


def test_20():
    python_code_.SQL2003_evo_ColumnConstraint()


def test_21():
    var_8 = python_code_.SQL2003_evo_Column(default=None)
    assert isinstance(var_8, python_code_.SQL2003_evo_Column)
    var_19 = "j\n=7"
    var_20 = "{#E\"'kh|I\x0b1y791C%[m"
    var_21 = python_code_.SQL2003_evo_StringFeature(key=var_19, value=var_20)
    assert isinstance(var_21, python_code_.SQL2003_evo_StringFeature)
    var_22 = "TQ)^G"
    var_23 = "DTN0\rn~*s"
    var_24 = python_code_.SQL2003_evo_TriggerDescriptor(
        event={-1433, True},
        actionTime=var_22,
        triggeredAction=var_22,
        level=var_23,
        TriggerDescriptor=var_23,
    )
    assert isinstance(var_24, python_code_.SQL2003_evo_TriggerDescriptor)


def test_22():
    var_4 = python_code_.SQL2003_evo_Column(default=None)
    assert isinstance(var_4, python_code_.SQL2003_evo_Column)
    var_6 = "syqmlDg"
    var_7 = python_code_.SQL2003_evo_ConstructedType(name=var_6)
    assert isinstance(var_7, python_code_.SQL2003_evo_ConstructedType)


def test_23():
    var_4 = python_code_.SQL2003_evo_XMLType(descriptor=[0, -2172, 0])
    assert isinstance(var_4, python_code_.SQL2003_evo_XMLType)
    var_13 = "q>E,"
    var_14 = python_code_.SQL2003_evo_TableConstraint(name=var_13)
    assert isinstance(var_14, python_code_.SQL2003_evo_TableConstraint)


def test_24():
    var_2 = lambda *args, **kwargs: 827
    var_3 = "^2{zfEF"
    var_4 = python_code_.SQL2003_evo_CharacterStringType(
        descriptor=var_2, length_def=var_3
    )
    assert isinstance(var_4, python_code_.SQL2003_evo_CharacterStringType)


def test_25():
    var_4 = '%jG\x0c"ZKd_)\x0c>'
    var_35 = python_code_.SQL2003_evo_ARRAY(num_elements=var_4)
    assert isinstance(var_35, python_code_.SQL2003_evo_ARRAY)
    var_36 = "L;,J!lE5.C"
    var_40 = python_code_.SQL2003_evo_CollectionType()
    var_41 = python_code_.SQL2003_evo_BinaryStringType(
        descriptor=complex(-779.5158, -290.72), length_def=var_40
    )
    assert isinstance(var_41, python_code_.SQL2003_evo_BinaryStringType)
    var_59 = "j\n=7"
    var_60 = "{#E\"'kh|I\x0b1y791C%[m"
    var_61 = python_code_.SQL2003_evo_StringFeature(key=var_59, value=var_60)
    assert isinstance(var_61, python_code_.SQL2003_evo_StringFeature)
    var_62 = "TQ)^G"
    var_63 = "DTN0\rn~*s"
    var_64 = python_code_.SQL2003_evo_TriggerDescriptor(
        event={-1433, True},
        actionTime=var_36,
        triggeredAction=var_62,
        level=var_63,
        TriggerDescriptor=var_63,
    )
    assert isinstance(var_64, python_code_.SQL2003_evo_TriggerDescriptor)


def test_26():
    var_0 = "\t,Z[ C7n_"
    var_1 = python_code_.SQL2003_evo_BooleanType(descriptor=var_0)
    assert isinstance(var_1, python_code_.SQL2003_evo_BooleanType)


def test_27():
    var_0 = python_code_.SQL2003_evo_Field()
    var_1 = 'XqbJKv8"}_l'
    var_2 = python_code_.SQL2003_evo_ReferentialConstraint(
        delete_action=var_1,
        update_action=var_0,
        match=var_1,
        SQL2003_evo_ReferentialConstraint=var_0,
    )
    assert isinstance(var_2, python_code_.SQL2003_evo_ReferentialConstraint)
    var_3 = python_code_.Parameter()
    var_12 = "typed,_SQL2003_evo_StructuredType__SQL2003_evo_StructuredType56"
    var_13 = set
    var_14 = python_code_.SQL2003_evo_TriggerDescriptor(
        event=var_1,
        actionTime=var_12,
        triggeredAction="_SQL2003_evo_Trigger__SQL2003_evo_Trigger,TIMESTAMPWITHTIMEZONE",
        level=var_3,
        description=var_13,
    )
    assert isinstance(var_14, python_code_.SQL2003_evo_TriggerDescriptor)


def test_28():
    var_1 = "{{"
    var_2 = python_code_.SQL2003_evo_ARRAY(num_elements=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_ARRAY)
    var_26 = python_code_.SQL2003_evo_Trigger(name=var_1, trigger=39)
    assert isinstance(var_26, python_code_.SQL2003_evo_Trigger)


def test_29():
    var_6 = "SQL2003_evo_BehaviouralComponentKSQL2003_evo_Feature55K_SQL2003_evo_StructuralComponent__columns52KYEAR"
    var_7 = "MethodParameterK_SQL2003_evo_StructuredType__structuredK_SQL2003_evo_Attribute__Attribute"
    var_14 = python_code_.SQL2003_evo_UserDefinedType(name=var_7)
    assert isinstance(var_14, python_code_.SQL2003_evo_UserDefinedType)
    var_19 = python_code_.SQL2003_evo_Trigger(name=False, Trigger=True)
    assert isinstance(var_19, python_code_.SQL2003_evo_Trigger)
    var_30 = python_code_.SQL2003_evo_Table(
        name=var_6, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )
    assert isinstance(var_30, python_code_.SQL2003_evo_Table)


def test_30():
    var_1 = 'XqbJKvh8"}_l'
    var_15 = python_code_.SQL2003_evo_Trigger(
        name="SQL2003_evo_BehaviouralComponentTTIMEWITHOUTTIMEZONETMethodParameter"
    )
    assert isinstance(var_15, python_code_.SQL2003_evo_Trigger)
    var_18 = python_code_.SQL2003_evo_Table(
        name=var_1, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )
    assert isinstance(var_18, python_code_.SQL2003_evo_Table)


def test_31():
    python_code_.SQL2003_evo_Schema(
        name=b"\x9dG\xbe\xeb\xb3\xa0CL\xfc\x0b\xee}\xbb\x87\xa1\xab\x0f\x15="
    )
    var_46 = "SQL2003_evo_Restriction"
    var_47 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_46)
    assert isinstance(var_47, python_code_.SQL2003_evo_DerivedTable)
    var_52 = python_code_.SQL2003_evo_Table(
        name=var_46, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )
    assert isinstance(var_52, python_code_.SQL2003_evo_Table)


@pytest.mark.xfail(strict=True)
def test_32():
    var_14 = python_code_.SQL2003_evo_UserDefinedType(name=[True])
    assert isinstance(var_14, python_code_.SQL2003_evo_UserDefinedType)
    var_19 = python_code_.SQL2003_evo_Trigger(name=False, Trigger=True)
    assert isinstance(var_19, python_code_.SQL2003_evo_Trigger)
    var_21 = 'TD"+'
    var_22 = python_code_.SQL2003_evo_ConstructedType(name=var_21)
    assert isinstance(var_22, python_code_.SQL2003_evo_ConstructedType)
    var_26 = False
    var_27 = lambda *args, **kwargs: []
    python_code_.SQL2003_evo_StructuredType(
        is_final=var_26,
        is_instantiable=var_27,
        structured=var_27,
        structured61={
            "OCTETS _SQL2003_evo_Table__table72 SQL2003_evo_Method P": True,
            'p;"': 334.53,
            "_SQL2003_evo_StructuredType__StructuredType18": True,
        },
        structured64=var_19,
    )


def test_33():
    var_1 = 'XbJKv8"}_l'
    var_13 = python_code_.SQL2003_evo_NumericFeature(key=var_1, value=var_1)
    assert isinstance(var_13, python_code_.SQL2003_evo_NumericFeature)
    var_14 = set()
    var_15 = python_code_.SQL2003_evo_Table(
        name=complex(1768.9767, -1886.8708), table72=var_14
    )
    assert isinstance(var_15, python_code_.SQL2003_evo_Table)
    var_16 = python_code_.SQL2003_evo_Column(default="")
    assert isinstance(var_16, python_code_.SQL2003_evo_Column)
    var_17 = "_SQL2003_evo_Table__Table"
    var_18 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_17, body=var_17, behaviouralComponents=var_1
    )
    assert isinstance(var_18, python_code_.SQL2003_evo_BehaviouralComponent)
    var_20 = True
    var_21 = python_code_.SQL2003_evo_StructuredType(
        is_final=var_20,
        is_instantiable=var_20,
        SQL2003_evo_StructuredType=var_1,
        StructuredType79=var_17,
    )
    assert isinstance(var_21, python_code_.SQL2003_evo_StructuredType)
    var_24 = python_code_.SQL2003_evo_DataType()
    python_code_.SQL2003_evo_Schema(name=var_1, Schema9=var_24, schema44=set())
    var_33 = "SQL2003_evo_Restriction"
    var_34 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_33)
    assert isinstance(var_34, python_code_.SQL2003_evo_DerivedTable)
    python_code_.SQL2003_evo_Table(
        name=var_33, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )


def test_34():
    var_1 = 'XqbJKv8"}_l'
    var_13 = python_code_.SQL2003_evo_NumericFeature(key=var_1, value=var_1)
    assert isinstance(var_13, python_code_.SQL2003_evo_NumericFeature)
    var_14 = {var_13}
    var_15 = python_code_.SQL2003_evo_Table(
        name=complex(1768.9767, -1886.8708), table72=var_14
    )
    assert isinstance(var_15, python_code_.SQL2003_evo_Table)
    var_16 = python_code_.SQL2003_evo_Column(default=None, Column=var_15)
    assert isinstance(var_16, python_code_.SQL2003_evo_Column)
    var_46 = "SQL2003_evo_BehaviouralComponentKSQL2003_evo_Feature55K_SQL2003_evo_StructuralComponent__columns52KYEAR"
    var_47 = "MethodParameterK_SQL2003_evo_StructuredType__structuredK_SQL2003_evo_Attribute__Attribute"
    var_49 = python_code_.SQL2003_evo_UserDefinedType(name=var_47)
    assert isinstance(var_49, python_code_.SQL2003_evo_UserDefinedType)
    var_53 = python_code_.SQL2003_evo_Trigger(name=False, Trigger=True)
    assert isinstance(var_53, python_code_.SQL2003_evo_Trigger)
    python_code_.SQL2003_evo_Table(
        name=var_46, tables=b"\xa4\xd0W\xafh\xa1\xf1\xf6\xf3\xcc\xbcWzJ\xce"
    )


@pytest.mark.xfail(strict=True)
def test_35():
    var_0 = repr
    var_1 = python_code_.SQL2003_evo_TableConstraint(name=var_0)
    assert isinstance(var_1, python_code_.SQL2003_evo_TableConstraint)
    var_3 = "Z"
    var_4 = python_code_.SQL2003_evo_IntervalFeature(
        key=var_3, value=b"\xbd\xe7;\xf4\x90\xb6\x0ba\xc1\xb9\xa5^[&"
    )
    assert isinstance(var_4, python_code_.SQL2003_evo_IntervalFeature)
    var_6 = python_code_.XMLTypes.XMLTYPE
    var_7 = "=`;DIQM'U'XEHc\x0b)VU"
    var_8 = python_code_.SQL2003_evo_BinaryStringType(
        descriptor=var_6, length_def=var_7
    )
    assert isinstance(var_8, python_code_.SQL2003_evo_BinaryStringType)
    var_9 = python_code_.SQL2003_evo_XMLType(descriptor=var_0)
    assert isinstance(var_9, python_code_.SQL2003_evo_XMLType)
    var_13 = python_code_.SQL2003_evo_NumericFeature(key=var_7, value=var_3)
    assert isinstance(var_13, python_code_.SQL2003_evo_NumericFeature)
    var_14 = set()
    var_15 = python_code_.SQL2003_evo_Table(
        name=complex(1768.9767, -1886.8708), table72=var_14
    )
    assert isinstance(var_15, python_code_.SQL2003_evo_Table)
    var_16 = python_code_.SQL2003_evo_Column(default=None, Column=var_15)
    assert isinstance(var_16, python_code_.SQL2003_evo_Column)
    python_code_.SQL2003_evo_TriggerDescriptor(
        event=var_8,
        actionTime=var_7,
        triggeredAction=[],
        level=var_7,
        description=var_8,
    )
    var_18 = "_SQL2003_evo_Table__Table"
    var_19 = python_code_.SQL2003_evo_BehaviouralComponent(
        name=var_18, body=var_18, behaviouralComponents=var_3
    )
    assert isinstance(var_19, python_code_.SQL2003_evo_BehaviouralComponent)
    var_20 = python_code_.SQL2003_evo_ConstructedType(name=var_3)
    assert isinstance(var_20, python_code_.SQL2003_evo_ConstructedType)
    var_21 = True
    var_22 = python_code_.SQL2003_evo_StructuredType(
        is_final=var_21,
        is_instantiable=var_21,
        SQL2003_evo_StructuredType=var_7,
        StructuredType79=var_18,
    )
    assert isinstance(var_22, python_code_.SQL2003_evo_StructuredType)
    var_27 = python_code_.SQL2003_evo_Schema(
        name=b"\x9dG\xbe\xeb\xb3\xa0CL\xfc\x0b\xee}\xbb\x87\xa1\xab\x0f\x15="
    )
    python_code_.SQL2003_evo_Table(
        name=var_0, Table=var_16, Table38=(-1533, True, 1992.23), Table47=var_27
    )


def test_36():
    var_1 = python_code_.SQL2003_evo_DataType
    var_2 = python_code_.SQL2003_evo_UserDefinedType(name=var_1)
    assert isinstance(var_2, python_code_.SQL2003_evo_UserDefinedType)
    var_7 = python_code_.SQL2003_evo_IntervalType(descriptor=var_1)
    assert isinstance(var_7, python_code_.SQL2003_evo_IntervalType)


def test_37():
    var_2 = python_code_.SQL2003_evo_DataType()
    var_4 = "View70"
    var_5 = python_code_.SQL2003_evo_DatetimeFeature(key=var_4, value=var_2)
    assert isinstance(var_5, python_code_.SQL2003_evo_DatetimeFeature)
    var_8 = ",1)>"
    var_9 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_8)
    assert isinstance(var_9, python_code_.SQL2003_evo_DerivedTable)
    var_10 = python_code_.SQL2003_evo_TableCheckConstraint(expression=2796)
    assert isinstance(var_10, python_code_.SQL2003_evo_TableCheckConstraint)
    var_11 = "CHARACTER._SQL2003_evo_Method__method.SQL2003_evo_Feature.M"
    var_12 = python_code_.SQL2003_evo_NumericType(descriptor=var_11)
    assert isinstance(var_12, python_code_.SQL2003_evo_NumericType)


def test_38():
    var_1 = python_code_.NumericRadix.BINARY
    var_2 = abs
    var_3 = python_code_.SQL2003_evo_BooleanType(descriptor=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_BooleanType)
    var_5 = python_code_.SQL2003_evo_ReferenceType()
    var_6 = python_code_.SQL2003_evo_Attribute(default=var_5, attributes=var_1)
    assert isinstance(var_6, python_code_.SQL2003_evo_Attribute)
    var_7 = "\r@]\n%fE,ub/H K'\x0c3"
    var_12 = set()
    var_15 = True
    var_25 = "4P{Dfpt8R7\\o<H)"
    var_26 = python_code_.SQL2003_evo_StringFeature(key=var_25, value=var_7)
    assert isinstance(var_26, python_code_.SQL2003_evo_StringFeature)
    var_27 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=var_2, parametersWithMode=var_15
    )
    assert isinstance(var_27, python_code_.SQL2003_evo_ParameterWithMode)
    var_47 = python_code_.SQL2003_evo_MethodParameter()
    var_50 = python_code_.TriggerEvent.DELETE
    var_55 = "RestrictionKAttribute"
    var_56 = python_code_.SQL2003_evo_UserDefinedType(name=var_55)
    assert isinstance(var_56, python_code_.SQL2003_evo_UserDefinedType)
    var_57 = ""
    var_58 = python_code_.SQL2003_evo_NumericFeature(key=var_57, value=var_47)
    assert isinstance(var_58, python_code_.SQL2003_evo_NumericFeature)
    var_59 = python_code_.SQL2003_evo_View()
    var_60 = python_code_.SQL2003_evo_Table(
        name=var_6, Table=var_50, tables69=var_12, Table87=var_59
    )
    assert isinstance(var_60, python_code_.SQL2003_evo_Table)


@pytest.mark.xfail(strict=True)
def test_39():
    var_3 = python_code_.SQL2003_evo_ROW()
    var_4 = "Z4ew]VreQs&55<,:"
    var_14 = python_code_.SQL2003_evo_UserDefinedType(name=[True])
    assert isinstance(var_14, python_code_.SQL2003_evo_UserDefinedType)
    var_19 = python_code_.SQL2003_evo_Trigger(
        name=var_4, SQL2003_evo_Trigger=var_3, trigger=None
    )
    assert isinstance(var_19, python_code_.SQL2003_evo_Trigger)
    var_21 = 'TD"+'
    var_22 = python_code_.SQL2003_evo_ConstructedType(name=var_21)
    assert isinstance(var_22, python_code_.SQL2003_evo_ConstructedType)
    var_26 = True
    var_27 = lambda *args, **kwargs: []
    python_code_.SQL2003_evo_StructuredType(
        is_final=var_26,
        is_instantiable=var_27,
        structured=var_27,
        structured61={
            "OCTETS _SQL2003_evo_Table__table72 SQL2003_evo_Method P": True,
            'p;"': 334.53,
            "_SQL2003_evo_StructuredType__StructuredType18": True,
        },
        structured64=var_19,
    )


def test_40():
    var_18 = python_code_.SQL2003_evo_ConstructedType(name=())
    assert isinstance(var_18, python_code_.SQL2003_evo_ConstructedType)
    var_21 = python_code_.ReferentialAction.NO_ACTION
    var_22 = "kJ"
    var_26 = python_code_.SQL2003_evo_CharacterStringType(
        descriptor=var_22, length_def=var_18
    )
    assert isinstance(var_26, python_code_.SQL2003_evo_CharacterStringType)
    var_27 = python_code_.SQL2003_evo_Restriction()
    var_31 = python_code_.SQL2003_evo_XMLType(descriptor=var_27)
    assert isinstance(var_31, python_code_.SQL2003_evo_XMLType)
    var_32 = python_code_.PredefinedType()
    var_33 = python_code_.SQL2003_evo_ARRAY(num_elements=var_32)
    assert isinstance(var_33, python_code_.SQL2003_evo_ARRAY)
    var_35 = python_code_.SQL2003_evo_DatetimeType(descriptor=[])
    assert isinstance(var_35, python_code_.SQL2003_evo_DatetimeType)
    var_40 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_21)
    assert isinstance(var_40, python_code_.SQL2003_evo_DerivedTable)
    var_45 = python_code_.SQL2003_evo_StringFeature(key=None, value=True)
    assert isinstance(var_45, python_code_.SQL2003_evo_StringFeature)


def test_41():
    var_0 = "s)TIkSi!y@]QaRlh/>"
    var_1 = python_code_.SQL2003_evo_BooleanType(descriptor=var_0)
    assert isinstance(var_1, python_code_.SQL2003_evo_BooleanType)
    var_6 = python_code_.SQL2003_evo_DatetimeFeature(key=var_0, value=var_0)
    assert isinstance(var_6, python_code_.SQL2003_evo_DatetimeFeature)


def test_42():
    var_0 = python_code_.SQL2003_evo_XMLType(
        descriptor="DataType:_SQL2003_evo_Method__Method62"
    )
    assert isinstance(var_0, python_code_.SQL2003_evo_XMLType)
    var_2 = python_code_.BinaryStringTypes.BINARYLARGEOBJECT
    var_3 = python_code_.SQL2003_evo_NumericType
    var_4 = python_code_.SQL2003_evo_ConstructedType(name=var_3)
    assert isinstance(var_4, python_code_.SQL2003_evo_ConstructedType)
    var_13 = python_code_.ReferentialAction.NO_ACTION
    var_25 = python_code_.PredefinedType()
    var_26 = python_code_.SQL2003_evo_ARRAY(num_elements=var_25)
    assert isinstance(var_26, python_code_.SQL2003_evo_ARRAY)
    var_28 = python_code_.SQL2003_evo_DatetimeType(descriptor=[])
    assert isinstance(var_28, python_code_.SQL2003_evo_DatetimeType)
    var_33 = python_code_.SQL2003_evo_DerivedTable(query_expression=var_13)
    assert isinstance(var_33, python_code_.SQL2003_evo_DerivedTable)
    var_35 = "tJ0Jz^*"
    python_code_.SQL2003_evo_Schema(name=var_35, Schema66=var_2)
    var_39 = python_code_.SQL2003_evo_StringFeature(key=None, value=True)
    assert isinstance(var_39, python_code_.SQL2003_evo_StringFeature)


@pytest.mark.xfail(strict=True)
def test_43():
    var_2 = lambda *args, **kwargs: [-2311, 195, False]
    var_3 = python_code_.SQL2003_evo_Parameter(name=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_Parameter)
    var_41 = python_code_.SQL2003_evo_UserDefinedType(name=[True])
    assert isinstance(var_41, python_code_.SQL2003_evo_UserDefinedType)
    var_45 = python_code_.SQL2003_evo_Trigger(name=False, Trigger=True)
    assert isinstance(var_45, python_code_.SQL2003_evo_Trigger)
    var_47 = 'TD"+'
    var_48 = python_code_.SQL2003_evo_ConstructedType(name=var_47)
    assert isinstance(var_48, python_code_.SQL2003_evo_ConstructedType)
    var_52 = False
    var_53 = lambda *args, **kwargs: []
    python_code_.SQL2003_evo_StructuredType(
        is_final=var_52,
        is_instantiable=var_53,
        structured=var_53,
        structured61={
            "OCTETS _SQL2003_evo_Table__table72 SQL2003_evo_Method P": True,
            'p;"': 334.53,
            "_SQL2003_evo_StructuredType__StructuredType18": True,
        },
        structured64=var_45,
    )


@pytest.mark.xfail(strict=True)
def test_44():
    var_3 = python_code_.SQL2003_evo_ParameterWithMode(
        mode="WVPT.awD@", parametersWithMode=None
    )
    assert isinstance(var_3, python_code_.SQL2003_evo_ParameterWithMode)
    var_11 = "syqmlDg"
    var_12 = python_code_.SQL2003_evo_ConstructedType(name=var_11)
    assert isinstance(var_12, python_code_.SQL2003_evo_ConstructedType)
    var_18 = False
    var_19 = "Table47"
    var_20 = python_code_.SQL2003_evo_Attribute(default=var_19)
    assert isinstance(var_20, python_code_.SQL2003_evo_Attribute)
    python_code_.SQL2003_evo_StructuredType(
        is_final=True, is_instantiable=var_18, StructuredType=var_20
    )


@pytest.mark.xfail(strict=True)
def test_45():
    var_2 = lambda *args, **kwargs: [-2311, 195, False]
    var_3 = python_code_.SQL2003_evo_Parameter(name=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_Parameter)
    var_7 = python_code_.BehaviouralComponent()
    var_8 = python_code_.SQL2003_evo_NumericType(descriptor=var_7)
    assert isinstance(var_8, python_code_.SQL2003_evo_NumericType)
    var_9 = python_code_.Unit.OCTETS
    var_10 = "second_precision"
    var_11 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=var_10, ParameterWithMode=set()
    )
    assert isinstance(var_11, python_code_.SQL2003_evo_ParameterWithMode)
    var_15 = python_code_.SQL2003_evo_ConstructedType(name=var_9)
    assert isinstance(var_15, python_code_.SQL2003_evo_ConstructedType)
    var_18 = python_code_.SQL2003_evo_Attribute(default=-1237)
    assert isinstance(var_18, python_code_.SQL2003_evo_Attribute)
    python_code_.SQL2003_evo_Method(
        name=True,
        body=var_2,
        SQL2003_evo_Method15=var_2,
        SQL2003_evo_Method20={"h&3m2O8$e": -551},
    )
    var_23 = True
    var_24 = False
    var_25 = {var_18}
    python_code_.SQL2003_evo_StructuredType(
        is_final=var_23,
        is_instantiable=var_24,
        StructuredType=var_18,
        StructuredType18=complex(-4024.977, -3284.09),
        structured=var_25,
        structured61=var_2,
    )


@pytest.mark.xfail(strict=True)
def test_46():
    var_2 = lambda *args, **kwargs: [-2311, 195, False]
    var_3 = python_code_.SQL2003_evo_Parameter(name=var_2)
    assert isinstance(var_3, python_code_.SQL2003_evo_Parameter)
    var_7 = python_code_.BehaviouralComponent()
    var_8 = python_code_.SQL2003_evo_NumericType(descriptor=var_7)
    assert isinstance(var_8, python_code_.SQL2003_evo_NumericType)
    var_9 = python_code_.Unit.OCTETS
    var_10 = "second_precision"
    var_11 = python_code_.SQL2003_evo_ParameterWithMode(
        mode=var_10, ParameterWithMode=set()
    )
    assert isinstance(var_11, python_code_.SQL2003_evo_ParameterWithMode)
    var_15 = python_code_.SQL2003_evo_ConstructedType(name=var_9)
    assert isinstance(var_15, python_code_.SQL2003_evo_ConstructedType)
    var_18 = python_code_.SQL2003_evo_Attribute(default=-1237)
    assert isinstance(var_18, python_code_.SQL2003_evo_Attribute)
    var_23 = False
    var_24 = False
    var_25 = {var_18}
    python_code_.SQL2003_evo_StructuredType(
        is_final=var_23,
        is_instantiable=var_24,
        StructuredType=var_18,
        StructuredType18=complex(-4024.977, -3284.09),
        structured=var_25,
        structured61=var_2,
    )
