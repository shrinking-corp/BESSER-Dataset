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
    Base,
    BaseExpressionResult,
    BaseResource,
    Company,
    Component,
    Enum,
    LevelKind,
    RangeKind,
    RedundancyType,
    StateType,
    date,
    datetime,
    library_BaseExpressionResult,
    library_BaseResource,
    library_Component,
    library_DiagramInfo,
    library_EObject,
    library_Equipment,
    library_EquipmentGroup,
    library_EquipmentRelationship,
    library_Expression,
    library_ExpressionResult,
    library_Function,
    library_FunctionRelationship,
    library_LastEvaluationExpressionResult,
    library_Library,
    library_Lifecycle,
    library_Meta,
    library_Metric,
    library_MetricSource,
    library_MetricValueRange,
    library_MultiImage,
    library_NetXResource,
    library_NodeType,
    library_Parameter,
    library_ProductInfo,
    library_Protocol,
    library_Tolerance,
    library_Unit,
    library_Value,
    library_Vendor,
    time,
)


@pytest.mark.xfail(strict=True)
def test_0():
    var_0 = "1\rbYTs/vBS]:\x0ckz8"
    var_39 = python_code_.library_Unit(code=var_0, description=var_0, name=var_0)
    assert isinstance(var_39, python_code_.library_Unit)
    python_code_.library_BaseResource(
        detailDisplay=None,
        expressionName=["bc/m(v3d~SfZg", True, 825.68],
        longName='"x@HT>hzY<?a>-*w',
        shortName=var_0,
        summaryDisplay=var_0,
        library_BaseResource=var_39,
        library_BaseResource55=['wnubp\x0bht"', -356.93, "muJ\nHjn]$y\"i+fH'@s\r"],
    )


def test_1():
    var_0 = python_code_.library_Function()
    var_1 = "METRICn_library_Equipment__library_Equipment27"
    var_2 = "library_Vendor,IDLE,library_EquipmentGroup50,_library_NodeType__library_NodeType116"
    var_3 = python_code_.library_Unit(code=var_1, description=var_0, name=var_2)
    assert isinstance(var_3, python_code_.library_Unit)


def test_2():
    var_1 = "n{*DaLyxxSP"
    var_2 = python_code_.library_Value
    var_3 = python_code_.library_Expression(
        expressionLines=(),
        name=var_1,
        library_Expression=var_2,
        library_Expression85=var_1,
        library_Expression53=[" z&d\x0bi'c<7", 4224.59],
    )
    assert isinstance(var_3, python_code_.library_Expression)
    var_18 = "f9{`\x0cuG"
    var_19 = python_code_.library_Tolerance(level=var_2, name=var_18)
    assert isinstance(var_19, python_code_.library_Tolerance)
    var_21 = "library_Prot}coln_library_Equipment__library_Equipment117nFORECAST"
    var_22 = "library_EquipmentGroup44"
    var_23 = python_code_.library_Unit(
        code=var_2,
        description=var_21,
        name=var_22,
        library_Unit={"_library_Library__library_Library84,library_Equipment117": True},
    )
    assert isinstance(var_23, python_code_.library_Unit)


def test_3():
    var_0 = "E\nR"
    var_1 = python_code_.RangeKind
    var_2 = python_code_.library_Expression(
        expressionLines=var_0,
        name=var_0,
        library_Expression=-1371.25,
        library_Expression9=var_1,
    )
    assert isinstance(var_2, python_code_.library_Expression)
    var_4 = python_code_.library_Protocol()
    var_6 = python_code_.library_Meta()
    var_7 = python_code_.library_Unit(
        code=var_6, description=var_4, name=var_2, library_Unit88=var_0
    )
    assert isinstance(var_7, python_code_.library_Unit)
    var_8 = {var_7, var_7, var_7, var_7}
    var_9 = python_code_.library_Library(
        protocols=-1038.19,
        name=var_0,
        library_Library90=var_6,
        library_Library87=var_8,
        library_Library73=var_8,
        library_Library78=var_8,
    )
    assert isinstance(var_9, python_code_.library_Library)
    var_12 = "E{1++n3"
    var_13 = python_code_.library_Unit(code=var_12, description=2762.52, name=var_0)
    var_17 = python_code_.library_DiagramInfo()
    var_18 = python_code_.library_Metric()
    var_40 = python_code_.library_ProductInfo(
        availableDate=var_0,
        endOfSalesDate=var_12,
        endOfSupportDate=complex(-257.5679, 1613.647036),
        productCode=var_1,
        salesCode=var_1,
        underDevelopmentDate=var_12,
        library_ProductInfo133=var_7,
    )
    assert isinstance(var_40, python_code_.library_ProductInfo)
    var_42 = python_code_.library_Value()
    var_45 = python_code_.library_Tolerance(
        level=var_12,
        name={},
        library_Tolerance={True, False, 1068},
        library_Tolerance127=var_12,
    )
    assert isinstance(var_45, python_code_.library_Tolerance)
    var_47 = "AYz5i_d=dF<Y\x0c\x0cmB*^_"
    python_code_.library_Unit(
        code=var_12, description=var_47, name=var_17, library_Unit=var_13
    )
    var_51 = "_library_Library__library_Library73"
    var_52 = "_library_Equipment__library_Equipment28nlibrary_EquipmentGroup44n_library_EquipmentGroup__library_EquipmentGroup41"
    var_53 = python_code_.library_BaseResource(
        detailDisplay=var_18,
        expressionName=var_51,
        longName=var_42,
        shortName=var_52,
        summaryDisplay=var_40,
    )
    assert isinstance(var_53, python_code_.library_BaseResource)
    var_57 = "\rLL"
    var_58 = python_code_.library_Component(
        description=var_57,
        duration=set(),
        name=var_47,
        library_Component=None,
        library_Component17=var_1,
    )
    assert isinstance(var_58, python_code_.library_Component)


def test_4():
    var_1 = "{ilJ\x0b(c!qX"
    var_5 = lambda *args, **kwargs: -429
    var_6 = python_code_.library_Expression(
        expressionLines=var_1, name=var_5, library_Expression128=None
    )
    assert isinstance(var_6, python_code_.library_Expression)


def test_5():
    var_1 = "n{*DaLyxxSP"
    var_2 = python_code_.library_Value
    var_3 = python_code_.library_Expression(
        expressionLines=(),
        name=var_1,
        library_Expression=var_2,
        library_Expression85=var_1,
        library_Expression53=[" z&d\x0bi'c<7", 4224.59],
    )
    assert isinstance(var_3, python_code_.library_Expression)


def test_6():
    var_1 = "{ilmJ\x0b(c!qX"
    var_6 = python_code_.library_Expression(
        expressionLines="D\ng\x0c]", name=var_1, library_Expression=var_1
    )
    assert isinstance(var_6, python_code_.library_Expression)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = "1\rbYTs/vBS]:\x0ckz8"
    var_14 = lambda *args, **kwargs: -429
    var_15 = "_library_Expression__library_Expression9"
    var_16 = python_code_.library_NetXResource()
    var_17 = python_code_.library_Expression(expressionLines=var_14, name=var_15)
    assert isinstance(var_17, python_code_.library_Expression)
    var_18 = python_code_.library_MultiImage()
    python_code_.library_Component(
        description=var_0,
        duration=var_15,
        name=var_15,
        Component=var_16,
        library_Component8=var_17,
        library_Component21=var_18,
    )


def test_8():
    var_2 = python_code_.Company()
    var_5 = python_code_.Component()
    var_7 = python_code_.BaseExpressionResult()
    var_8 = python_code_.library_LastEvaluationExpressionResult(lastEvalResult=None)
    assert isinstance(var_8, python_code_.library_LastEvaluationExpressionResult)
    var_9 = "_library_Equipment__library_Equipment71"
    var_10 = "_library_Expression__library_Expression85n_library_Tolerance__library_Tolerancenlibrary_Equipmentnlibrary_Equipment51"
    var_11 = python_code_.library_Parameter(
        description=var_9,
        expressionName=var_5,
        modifiable=var_10,
        name=None,
        value=var_10,
    )
    assert isinstance(var_11, python_code_.library_Parameter)
    var_13 = python_code_.library_Vendor()
    var_15 = str
    var_16 = python_code_.library_ProductInfo(
        availableDate=var_2,
        endOfSalesDate=var_9,
        endOfSupportDate=var_9,
        productCode=[True, -1636.9, False],
        salesCode=var_15,
        underDevelopmentDate=var_13,
    )
    assert isinstance(var_16, python_code_.library_ProductInfo)
    var_19 = python_code_.library_ExpressionResult(
        targetRange=var_10,
        targetIntervalHint=var_7,
        targetKindHint=complex(1392.15584, 1128.1),
    )
    assert isinstance(var_19, python_code_.library_ExpressionResult)
    var_22 = python_code_.library_Protocol()
    var_23 = python_code_.library_Protocol()
    var_24 = {var_22, var_23, var_23, var_23}
    var_25 = python_code_.library_Component(
        description=var_15,
        duration=var_10,
        name=complex(-23.634422, 691.90232),
        library_Component13=var_24,
    )
    assert isinstance(var_25, python_code_.library_Component)
    var_26 = "library_Value"
    var_27 = '>m;!h;JVL4--`W"'
    python_code_.library_ProductInfo(
        availableDate=var_10,
        endOfSalesDate=var_26,
        endOfSupportDate=var_27,
        productCode=var_22,
        salesCode=False,
        underDevelopmentDate=b'bO\x14\xf5\xfeH\\\xa8UzT\xac$\x1b"',
        library_ProductInfo133=var_13,
    )


@pytest.mark.xfail(strict=True)
def test_9():
    var_1 = python_code_.Company()
    var_2 = "-ERo2\rT2o6|"
    var_3 = python_code_.library_BaseResource(
        detailDisplay=var_2,
        expressionName=var_2,
        longName=var_2,
        shortName=(),
        summaryDisplay=var_2,
        library_BaseResource55=var_2,
    )
    assert isinstance(var_3, python_code_.library_BaseResource)
    var_6 = python_code_.library_EquipmentRelationship()
    var_12 = "_library_Component__library_Component_library_ProductInfo__library_ProductInfo133_library_Unit__library_Unit"
    var_13 = python_code_.library_Lifecycle
    var_14 = "_EEV08"
    var_15 = "?/G!oFAxD.9*y\\"
    var_16 = "AEn. \r#fhlwDP^y,6"
    var_17 = set()
    var_18 = python_code_.library_EquipmentGroup(
        count=var_2,
        description=var_15,
        name=var_16,
        library_EquipmentGroup=var_6,
        library_EquipmentGroup47=var_17,
    )
    assert isinstance(var_18, python_code_.library_EquipmentGroup)
    var_19 = {var_18, var_18, var_18, var_18}
    var_20 = python_code_.library_Equipment(
        count=var_12,
        equipmentCode=var_13,
        position=var_12,
        redundancy=complex(503.591019, -1654.82575),
        state=var_14,
        library_Equipment117=var_13,
        library_Equipment=(),
        library_Equipment25=var_19,
    )
    assert isinstance(var_20, python_code_.library_Equipment)
    var_24 = "_library_Component__library_Component19_library_Equipment__library_Equipment117_library_NodeType__library_NodeType125"
    python_code_.library_Equipment(
        count=var_24,
        equipmentCode=var_2,
        position=var_12,
        redundancy=var_16,
        state=var_12,
        library_Equipment25=var_1,
        library_Equipment27=var_13,
        library_Equipment42=var_18,
    )


@pytest.mark.xfail(strict=True)
def test_10():
    var_0 = python_code_.library_MetricSource()
    var_1 = "{ilJ\x0b(c!qX"
    var_5 = lambda *args, **kwargs: -429
    var_8 = python_code_.library_Value
    var_9 = python_code_.library_BaseResource(
        detailDisplay=var_5,
        expressionName=set(),
        longName=var_0,
        shortName=var_0,
        summaryDisplay=704,
        library_BaseResource55=var_1,
    )
    assert isinstance(var_9, python_code_.library_BaseResource)
    python_code_.library_ExpressionResult(
        targetRange=var_5,
        targetIntervalHint=var_8,
        targetKindHint=b"\xb3",
        library_ExpressionResult=var_9,
    )


def test_11():
    var_2 = python_code_.library_Value
    var_5 = "library_Expression39"
    var_6 = "4P2Z"
    var_7 = python_code_.library_ProductInfo(
        availableDate=var_5,
        endOfSalesDate=var_5,
        endOfSupportDate=var_6,
        productCode=complex(1106.8001, -4262.685),
        salesCode=var_2,
        underDevelopmentDate={
            "6\\S|!^g?b\n\tzr": "_library_Component__library_Component13nTOLERANCEn_library_ProductInfo__library_ProductInfo124nlibrary_Library84",
            "|dREQ_Qo5\r,q": "",
        },
        library_ProductInfo121="kj@3t3~?\x0cSOv[xc]46b",
    )
    assert isinstance(var_7, python_code_.library_ProductInfo)


def test_12():
    var_0 = ",y{8+J9Oh#\x0bNP"
    var_1 = python_code_.library_Tolerance(
        level=var_0, name=var_0, library_Tolerance=var_0
    )
    assert isinstance(var_1, python_code_.library_Tolerance)
    var_2 = lambda *args, **kwargs: False
    var_3 = python_code_.library_LastEvaluationExpressionResult(lastEvalResult=var_2)
    assert isinstance(var_3, python_code_.library_LastEvaluationExpressionResult)
    var_4 = python_code_.library_Meta()
    var_5 = python_code_.library_Function()
    var_6 = python_code_.library_MultiImage()
    var_8 = python_code_.library_MetricSource()
    var_15 = "_11nlibrary_DiagramInfon_library_Unit__library_Unit88"
    var_16 = "_library_Component__library_Component13n_library_Equipment__library_Equipment51nlibrary_EquipmentRelationshipn_11"
    var_17 = "resourceRefsn_library_Unit__library_Unit130nUTILIZATIONnn1"
    var_18 = "W4[<%aTq|C2*6&"
    var_19 = python_code_.library_Equipment(
        count=var_8,
        equipmentCode=complex(749.11, 1176.0236),
        position=var_8,
        redundancy=var_17,
        state=var_18,
        library_Equipment119=var_2,
    )
    assert isinstance(var_19, python_code_.library_Equipment)
    var_20 = set()
    python_code_.library_Equipment(
        count=var_15,
        equipmentCode=var_1,
        position=var_16,
        redundancy=var_1,
        state=var_2,
        library_Equipment117=var_4,
        library_Equipment30=var_19,
        library_Equipment28=var_20,
        library_Equipment119=var_4,
    )
    var_22 = "_library_Library__library_Librarynlibrary_ProductInfo"
    var_23 = python_code_.library_ProductInfo(
        availableDate=var_5,
        endOfSalesDate=var_0,
        endOfSupportDate=var_6,
        productCode=var_17,
        salesCode=var_22,
        underDevelopmentDate=[],
        library_ProductInfo121=var_20,
        library_ProductInfo124="library_Expression128",
        library_ProductInfo133=-1629.87,
    )
    assert isinstance(var_23, python_code_.library_ProductInfo)


def test_13():
    var_3 = python_code_.library_DiagramInfo()
    var_4 = '5S%Y"c?s"t\x0byn'
    var_5 = "MTRIC"
    var_6 = python_code_.library_Tolerance(
        level=var_5, name=-2526.07, library_Tolerance=False
    )
    assert isinstance(var_6, python_code_.library_Tolerance)
    var_7 = {var_6, var_6, var_6, var_6, var_6}
    var_8 = python_code_.library_Library(
        protocols=var_4,
        name=var_3,
        library_Library81=var_7,
        library_Library70=var_7,
        library_Library76=var_7,
        library_Library=set(),
    )
    assert isinstance(var_8, python_code_.library_Library)


def test_14():
    var_9 = "library_Expression-_library_Expression__library_Expression39-_library_Library__library_Library-_library_EquipmentGroup__library_EquipmentGroup32"
    var_10 = len
    var_11 = python_code_.library_NodeType(
        leafNode=var_9,
        name=var_10,
        library_NodeType113=b"\xeav\xce",
        library_NodeType125=complex(3126.4, 557.28),
    )
    assert isinstance(var_11, python_code_.library_NodeType)


def test_15():
    var_22 = python_code_.library_EquipmentGroup
    var_24 = "_library_Equipment__library_Equipment71"
    var_25 = python_code_.library_ExpressionResult(
        targetRange=var_24,
        targetIntervalHint=var_22,
        targetKindHint=var_24,
        library_ExpressionResult=var_24,
    )
    assert isinstance(var_25, python_code_.library_ExpressionResult)


def test_16():
    var_3 = python_code_.library_DiagramInfo()
    var_5 = "METRIC"
    var_6 = python_code_.library_Tolerance(
        level=var_5, name=var_5, library_Tolerance=var_3
    )
    assert isinstance(var_6, python_code_.library_Tolerance)
    var_9 = python_code_.Company()
    var_15 = "library_BaseResource library_Equipment28"
    var_16 = python_code_.library_ExpressionResult(
        targetRange=var_9,
        targetIntervalHint=var_6,
        targetKindHint=var_15,
        library_ExpressionResult57=var_5,
    )
    assert isinstance(var_16, python_code_.library_ExpressionResult)


def test_17():
    var_0 = python_code_.library_MetricSource()
    var_1 = "{ilJ\x0b(c!qX"
    var_5 = lambda *args, **kwargs: -429
    var_6 = python_code_.library_Expression(
        expressionLines=var_1, name=var_5, library_Expression128=None
    )
    assert isinstance(var_6, python_code_.library_Expression)
    var_7 = python_code_.library_EquipmentGroup(
        count=var_1,
        description=var_1,
        name="\x0c{F!8}yLH{j8*",
        library_EquipmentGroup41={var_0},
        library_EquipmentGroup44={"9Jn+4P"},
        library_EquipmentGroup47={-1778.08},
    )
    assert isinstance(var_7, python_code_.library_EquipmentGroup)


def test_18():
    var_0 = python_code_.library_MetricSource()
    var_1 = "{ilJ\x0b(c!qX"
    var_2 = lambda *args, **kwargs: -429
    var_4 = python_code_.library_EquipmentGroup(
        count=var_0, description=var_2, name=var_1
    )
    assert isinstance(var_4, python_code_.library_EquipmentGroup)


def test_19():
    var_1 = "{ilJ\x0b(c!qk"
    var_2 = lambda *args, **kwargs: -429
    var_3 = python_code_.library_Expression(
        expressionLines=var_1, name=var_2, library_Expression128=None
    )
    assert isinstance(var_3, python_code_.library_Expression)
    var_4 = python_code_.library_EquipmentGroup(
        count="uP",
        description=var_1,
        name=var_1,
        library_EquipmentGroup50={var_3},
        library_EquipmentGroup35=set(),
        library_EquipmentGroup38=set(),
    )
    assert isinstance(var_4, python_code_.library_EquipmentGroup)


def test_20():
    var_1 = python_code_.library_Vendor()
    var_2 = ">8CO3vZ^j"
    var_3 = "#H[)Qcx'829Z3~+Gl"
    var_4 = "=a'e\x0c47VDzr"
    var_5 = lambda *args, **kwargs: [False, True, "VXfbb\rzSI4z4B"]
    var_6 = python_code_.library_ProductInfo(
        availableDate=var_2,
        endOfSalesDate=var_3,
        endOfSupportDate=var_4,
        productCode=var_5,
        salesCode=var_3,
        underDevelopmentDate=None,
        library_ProductInfo133=-2267,
    )
    assert isinstance(var_6, python_code_.library_ProductInfo)
    var_12 = python_code_.library_Expression(expressionLines=-1215, name=var_5)
    assert isinstance(var_12, python_code_.library_Expression)
    var_13 = "\nghn--c"
    var_14 = 'sHB"T)/#m'
    var_15 = python_code_.library_DiagramInfo()
    var_16 = {var_15, var_15}
    var_17 = python_code_.library_EquipmentGroup(
        count=var_12,
        description=var_1,
        name=var_1,
        library_EquipmentGroup50=var_2,
        library_EquipmentGroup32=var_16,
        library_EquipmentGroup35=var_16,
    )
    assert isinstance(var_17, python_code_.library_EquipmentGroup)
    var_18 = python_code_.library_Parameter(
        description=var_3,
        expressionName=var_13,
        modifiable=var_14,
        name=var_3,
        value=var_2,
        library_Parameter45=var_17,
    )
    assert isinstance(var_18, python_code_.library_Parameter)
    var_21 = "u[t]E__Na\t$)\t.J"
    var_22 = python_code_.library_LastEvaluationExpressionResult(lastEvalResult=var_21)
    assert isinstance(var_22, python_code_.library_LastEvaluationExpressionResult)
    var_28 = python_code_.library_Tolerance(level="library_Component15", name=22.46)
    assert isinstance(var_28, python_code_.library_Tolerance)


@pytest.mark.xfail(strict=True)
def test_21():
    var_2 = "-ERo2\rT2o6|"
    var_3 = python_code_.library_BaseResource(
        detailDisplay=var_2,
        expressionName=var_2,
        longName=var_2,
        shortName=(),
        summaryDisplay=var_2,
        library_BaseResource55=var_2,
    )
    assert isinstance(var_3, python_code_.library_BaseResource)
    var_6 = python_code_.library_EquipmentRelationship()
    var_8 = python_code_.library_Function()
    var_13 = python_code_.library_Lifecycle
    var_14 = "_EEV08"
    var_15 = "?/G!oFAxD.9*y\\"
    var_16 = "AEn. \r#fhlwDP^y,6"
    var_17 = set()
    var_18 = python_code_.library_EquipmentGroup(
        count=var_2,
        description=var_15,
        name=var_16,
        library_EquipmentGroup=var_6,
        library_EquipmentGroup47=var_17,
    )
    assert isinstance(var_18, python_code_.library_EquipmentGroup)
    var_30 = "library_Expression39"
    var_31 = "library_Function"
    var_32 = python_code_.library_ProductInfo(
        availableDate=var_30,
        endOfSalesDate=var_30,
        endOfSupportDate=var_31,
        productCode=complex(1106.8001, -4262.685),
        salesCode=var_13,
        underDevelopmentDate={
            "6\\S|!^g?b\n\tzr": "_library_Component__library_Component13nTOLERANCEn_library_ProductInfo__library_ProductInfo124nlibrary_Library84",
            "|dREQ_Qo5\r,q": "",
        },
        library_ProductInfo121="kj@3t3~?\x0cSOv[xc]46b",
    )
    assert isinstance(var_32, python_code_.library_ProductInfo)
    var_34 = "IMh$o1Nm,NG)\r.U=P"
    var_35 = python_code_.library_MultiImage()
    var_36 = python_code_.library_Component(
        description=var_34,
        duration=var_8,
        name=var_16,
        library_Component17=var_17,
        library_Component21=var_35,
        library_Component15=var_17,
    )
    assert isinstance(var_36, python_code_.library_Component)
    var_37 = python_code_.library_Library(
        protocols=set(),
        name=[-1146, -2429.9, 793.34],
        library_Library68=None,
        library_Library73=var_17,
    )
    python_code_.library_Expression(
        expressionLines=var_31,
        name=var_31,
        library_Expression=var_36,
        library_Expression85=var_37,
        library_Expression53=var_14,
    )


def test_22():
    var_2 = lambda *args, **kwargs: False
    var_3 = python_code_.library_LastEvaluationExpressionResult(lastEvalResult=var_2)
    assert isinstance(var_3, python_code_.library_LastEvaluationExpressionResult)
    var_8 = python_code_.library_MetricSource()
    var_10 = python_code_.library_MultiImage()
    var_12 = "library_Library70library_DiagramInfolibrary_DiagramInfo33"
    var_15 = "_11nlibrary_DiagramInfon_library_Unit__library_Unit88"
    var_17 = "resourceRefsn_library_Unit__library_Unit130nUTILIZAIONnn1"
    var_18 = "W4[<%aTq|C2*6&"
    var_19 = python_code_.library_Equipment(
        count="l:Ag*E,omLrGmubuS\t",
        equipmentCode=var_18,
        position="3*#>_*F5a-o6M>43L`e",
        redundancy=var_12,
        state=var_17,
        library_Equipment117=None,
        library_Equipment30=None,
        library_Equipment28={True, "fD:4%", -535},
        library_Equipment22={
            var_10,
            "library_Unit.library_Value.library_Equipment119._library_Tolerance__library_Tolerance",
            var_17,
        },
        library_Equipment27={-2895.7},
        library_Equipment42=var_8,
        library_Equipment51=var_15,
        library_Equipment71=var_3,
        library_Equipment119=var_2,
    )
    assert isinstance(var_19, python_code_.library_Equipment)


@pytest.mark.xfail(strict=True)
def test_23():
    var_15 = lambda *args, **kwargs: -429
    var_20 = (
        "_library_ProductInfo__library_ProductInfo124nlibrary_Equipment42nMETRICREMOVE"
    )
    var_21 = python_code_.library_LastEvaluationExpressionResult
    var_22 = "__#O^=\\o^4)`\x0bA2B"
    var_23 = lambda *args, **kwargs: True
    var_24 = python_code_.library_Function()
    var_25 = {var_24, var_24, var_24, var_24, var_24}
    var_26 = python_code_.library_NodeType(
        leafNode=var_15, name=var_23, library_NodeType113=var_25
    )
    assert isinstance(var_26, python_code_.library_NodeType)
    python_code_.library_Equipment(
        count=var_20,
        equipmentCode=var_21,
        position=var_22,
        redundancy=var_20,
        state=(980, -100),
        library_Equipment117=var_26,
        library_Equipment30=complex(-2465.5716464, -139.696),
        library_Equipment22=b"\xf1\xc3",
        library_Equipment25=var_25,
        library_Equipment27=complex(-2804.241021, -516.286),
    )


@pytest.mark.xfail(strict=True)
def test_24():
    var_5 = "METRIC"
    var_14 = lambda *args, **kwargs: -429
    var_18 = "AEn. \r#hlwDP^y,6"
    var_20 = python_code_.library_Meta()
    var_21 = "_library_Parameter__library_Parameter45,library_NetXResource48"
    var_22 = python_code_.library_Value
    python_code_.library_Equipment(
        count=var_21,
        equipmentCode=var_18,
        position=var_21,
        redundancy=var_14,
        state=-78,
        library_Equipment117=[],
        library_Equipment30=var_5,
        library_Equipment25=var_22,
        library_Equipment42=var_22,
        library_Equipment51=var_20,
    )


def test_25():
    var_1 = "{ilmJ\x0b(c!qX@"
    var_5 = lambda *args, **kwargs: -429
    var_6 = python_code_.library_Expression(
        expressionLines=var_1, name=var_1, library_Expression=None
    )
    assert isinstance(var_6, python_code_.library_Expression)
    var_8 = "f{t:Ub 99'$\""
    var_9 = python_code_.library_Parameter(
        description=var_1,
        expressionName=var_5,
        modifiable=var_8,
        name=var_8,
        value=var_8,
    )
    assert isinstance(var_9, python_code_.library_Parameter)


def test_26():
    var_3 = python_code_.library_DiagramInfo()
    var_6 = python_code_.library_Tolerance(
        level="_library_BaseResource__library_BaseResource",
        name="QoKZITb",
        library_Tolerance82=None,
        library_Tolerance127=var_3,
    )
    assert isinstance(var_6, python_code_.library_Tolerance)


def test_27():
    var_5 = "MTRIC"
    var_6 = python_code_.library_Tolerance(
        level=var_5, name=-2526.07, library_Tolerance=False
    )
    assert isinstance(var_6, python_code_.library_Tolerance)


def test_28():
    python_code_.library_MetricSource()


def test_29():
    var_1 = "{ilJ\x0b(c!qX"
    var_5 = python_code_.library_Tolerance(
        level=var_1, name=-2526.07, library_Tolerance=False
    )
    assert isinstance(var_5, python_code_.library_Tolerance)
    var_6 = {var_5, var_5, var_5, var_5, var_5}
    var_8 = python_code_.library_Expression(
        expressionLines=b"\x84\x08h\x8f\xa4W\xbd2f\xdeh\x07[\x84D\xe9",
        name=var_1,
        library_Expression128=var_6,
    )
    assert isinstance(var_8, python_code_.library_Expression)


@pytest.mark.xfail(strict=True)
def test_30():
    var_9 = python_code_.library_Function()
    var_14 = python_code_.library_Lifecycle
    var_15 = "_EEV08"
    var_17 = "AEn. \r#fhlwDP^y,6"
    var_18 = set()
    var_19 = "library_Expression39"
    var_20 = "library_Function"
    var_21 = python_code_.library_ProductInfo(
        availableDate=var_19,
        endOfSalesDate=var_19,
        endOfSupportDate=var_20,
        productCode=complex(1106.8001, -4262.685),
        salesCode=var_14,
        underDevelopmentDate={
            "6\\S|!^g?b\n\tzr": "_library_Component__library_Component13nTOLERANCEn_library_ProductInfo__library_ProductInfo124nlibrary_Library84",
            "|dREQ_Qo5\r,q": "",
        },
        library_ProductInfo121="kj@3t3~?\x0cSOv[xc]46b",
    )
    assert isinstance(var_21, python_code_.library_ProductInfo)
    var_23 = "IMh$o1Nm,NG)\r.U=P"
    var_24 = python_code_.library_MultiImage()
    var_25 = python_code_.library_Component(
        description=var_23,
        duration=var_9,
        name=var_17,
        library_Component17=var_18,
        library_Component21=var_24,
        library_Component15=var_18,
    )
    assert isinstance(var_25, python_code_.library_Component)
    var_26 = python_code_.library_Library(
        protocols=set(),
        name=[-1146, -2429.9, 793.34],
        library_Library68=None,
        library_Library73=var_18,
    )
    python_code_.library_Expression(
        expressionLines=var_20,
        name=var_20,
        library_Expression=var_25,
        library_Expression85=var_26,
        library_Expression53=var_15,
    )


@pytest.mark.xfail(strict=True)
def test_31():
    var_0 = ",y{8+J9Oh#\x0bNP"
    var_1 = python_code_.library_Tolerance(
        level=var_0, name=var_0, library_Tolerance=var_0
    )
    assert isinstance(var_1, python_code_.library_Tolerance)
    var_2 = lambda *args, **kwargs: False
    var_3 = python_code_.library_LastEvaluationExpressionResult(lastEvalResult=var_2)
    assert isinstance(var_3, python_code_.library_LastEvaluationExpressionResult)
    var_29 = python_code_.Component()
    var_35 = python_code_.library_NetXResource()
    python_code_.library_Library(
        protocols=var_35,
        name=var_29,
        library_Library81='JK3|"T]0oQn1L',
        library_Library84=var_0,
        library_Library68=var_29,
        library_Library70=var_29,
        library_Library76=var_35,
        library_Library78=280.66,
    )


def test_32():
    var_1 = "n{*DaLyxxSP"
    var_2 = python_code_.library_Value
    var_3 = python_code_.library_Expression(
        expressionLines=(),
        name=var_1,
        library_Expression=var_2,
        library_Expression85=var_1,
        library_Expression53=[" z&d\x0bi'c<7", 4224.59],
    )
    assert isinstance(var_3, python_code_.library_Expression)
    var_11 = "_library_Component__library_Component19_library_Equipment__library_Equipment117_library_NodeType__library_NodeType125"
    var_15 = python_code_.library_NodeType(
        leafNode={"library_Metric": 853.79, "uo(@\x0c[g<=CA_'#h%(Yb": -2139, "h": 1624},
        name=var_2,
        library_NodeType=(),
    )
    assert isinstance(var_15, python_code_.library_NodeType)
    var_16 = python_code_.library_ExpressionResult(
        targetRange=var_2,
        targetIntervalHint=b"nE\xda\xbb~G\xc6\x83Y\xbb\xa9e",
        targetKindHint=var_11,
        library_ExpressionResult=var_2,
    )
    assert isinstance(var_16, python_code_.library_ExpressionResult)


def test_33():
    var_0 = '! \x0c7.]"N@KL1 S2'
    var_1 = python_code_.library_Function()
    var_2 = {var_1, var_1, var_1}
    var_3 = python_code_.library_NodeType(
        leafNode=set(), name=var_0, library_NodeType113=var_2
    )
    assert isinstance(var_3, python_code_.library_NodeType)
    var_5 = "library_Expression-_library_Expression__library_Expression39-_library_Library__library_Library-_library_EquipmentGroup__library_EquipmentGroup32"
    var_6 = len
    python_code_.library_NodeType(
        leafNode=var_5,
        name=var_6,
        library_NodeType113=b"\xeav\xce",
        library_NodeType125=complex(3126.4, 557.28),
    )


def test_34():
    var_47 = python_code_.library_MetricValueRange()
    var_48 = "library_Equipmentn_library_Library__library_Library87"
    var_51 = "_library_EquipmentGroup__library_EquipmentGroup47n_library_Equipment__library_Equipment27nlibrary_Equipment119nlibrary_Expression85"
    var_53 = python_code_.library_EquipmentGroup(
        count="_library_Equipment__library_Equipment27 _library_Component__library_Component4 _library_Library__library_Library",
        description=var_48,
        name=var_51,
        library_EquipmentGroup=None,
        library_EquipmentGroup50=set(),
    )
    assert isinstance(var_53, python_code_.library_EquipmentGroup)
    var_54 = python_code_.library_Expression(
        expressionLines=var_47, name=var_51, library_Expression39=var_53
    )
    assert isinstance(var_54, python_code_.library_Expression)


def test_35():
    var_0 = python_code_.library_MultiImage()
    var_12 = 'D"Iw&sEg|'
    var_13 = python_code_.library_Component
    var_14 = "{+Vb\x0b24R+ lc]{SnQJ"
    var_15 = python_code_.library_Unit(
        code=var_12, description=var_13, name=var_14, library_Unit130=var_0
    )
    assert isinstance(var_15, python_code_.library_Unit)


@pytest.mark.xfail(strict=True)
def test_36():
    var_5 = "METRIC"
    var_14 = lambda *args, **kwargs: -429
    var_18 = "AEn. \r#hlwDP^y,6"
    var_20 = python_code_.library_Meta()
    var_25 = "library_Library68"
    var_26 = "-)[u@pfJBj7aBRmN\x0b"
    var_27 = python_code_.library_Vendor()
    python_code_.library_ProductInfo(
        availableDate=var_5,
        endOfSalesDate=var_18,
        endOfSupportDate=var_25,
        productCode=var_14,
        salesCode=var_26,
        underDevelopmentDate=var_20,
        library_ProductInfo=var_14,
        library_ProductInfo133=var_27,
    )
