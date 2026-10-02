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
    MachineLibrary_Button,
    MachineLibrary_Buttons,
    MachineLibrary_CheckAddSID_PM2PM,
    MachineLibrary_CheckAddSID_Values_PM2PM,
    MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES,
    MachineLibrary_CheckFilling_ARL_XRF_OES,
    MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES,
    MachineLibrary_CheckSampleConfig_SuperQXRF,
    MachineLibrary_CheckSampleRunTimeParams_SuperQXRF,
    MachineLibrary_CheckSampleRunTime_SuperQXRF,
    MachineLibrary_CheckSample_SuperQXRF,
    MachineLibrary_Command,
    MachineLibrary_Commands,
    MachineLibrary_CommunicationData,
    MachineLibrary_Communication_SuperQXRF,
    MachineLibrary_Compac_Link,
    MachineLibrary_ControlSamples_SuperQXRF,
    MachineLibrary_DPbase_Link,
    MachineLibrary_DPbase_Node,
    MachineLibrary_DisableSCT_ARL_XRF_OES,
    MachineLibrary_ErrorMessage_OBLFOES,
    MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES,
    MachineLibrary_ExePrepUnit_ARL_XRF_OES,
    MachineLibrary_ExecuteFiling_ARL_XRF_OES,
    MachineLibrary_FileTransfer_Link,
    MachineLibrary_File_Sample_ARL_XRF_OES,
    MachineLibrary_GeneralParameter_SuperQXRF,
    MachineLibrary_GeneralSetting_ARL_XRF_OES,
    MachineLibrary_HistoryConfig_AccuPyc,
    MachineLibrary_History_AccuPycMeter,
    MachineLibrary_IBMWebsphereMQ,
    MachineLibrary_InsertRemove_Entry_Host,
    MachineLibrary_InsertRemove_Host,
    MachineLibrary_InsertRemove_Keywords_Host,
    MachineLibrary_InsertRemove_Types_Host,
    MachineLibrary_LabMachine,
    MachineLibrary_LabMachines,
    MachineLibrary_Link2,
    MachineLibrary_LinkConfig,
    MachineLibrary_Moved_Host,
    MachineLibrary_NodeConfig,
    MachineLibrary_NodeGeneral,
    MachineLibrary_NodeGeneralSpecial,
    MachineLibrary_NodeGeneral_AccuPycMeter,
    MachineLibrary_NodeGeneral_PM2PM,
    MachineLibrary_NodeGeneral_RemotePM,
    MachineLibrary_NodeGeneral_RigakuXRF,
    MachineLibrary_NodeGeneral_Terminal,
    MachineLibrary_NodeGeneral_WinCC2WinCC,
    MachineLibrary_NodeProgram,
    MachineLibrary_NodePrograms,
    MachineLibrary_NodeSpecialConfiguration,
    MachineLibrary_OES_XRF_Condition,
    MachineLibrary_OutputRequest_OBLFOES,
    MachineLibrary_PLCtoPmMatrix,
    MachineLibrary_PMMachineLibrary,
    MachineLibrary_PS_Process_Finished_ARL_XRF_OES,
    MachineLibrary_ParamPrint,
    MachineLibrary_Parameter,
    MachineLibrary_Parameters,
    MachineLibrary_PlainMove,
    MachineLibrary_PlainMoveEntrySend,
    MachineLibrary_Position,
    MachineLibrary_Positions,
    MachineLibrary_RecalRequest_OBLFOES,
    MachineLibrary_Report_Host,
    MachineLibrary_RobotConfSendOrder,
    MachineLibrary_RobotConfSendOrders,
    MachineLibrary_RobotConfiguration,
    MachineLibrary_RobotToWinCC,
    MachineLibrary_RobotToWinccs,
    MachineLibrary_RobotVarToBusyCodes,
    MachineLibrary_RobotVarToBusycode,
    MachineLibrary_RobotVarToErrorbit,
    MachineLibrary_RobotVarToErrorbits,
    MachineLibrary_RobotWarningONDelete,
    MachineLibrary_RobotWinCCToRobot,
    MachineLibrary_RobotWinCCToRobots,
    MachineLibrary_SepByComma_Field_Scanner,
    MachineLibrary_SepByComma_ID_Scanner,
    MachineLibrary_SepByComma_Scanner,
    MachineLibrary_Serial_Link,
    MachineLibrary_Settings_ARL_XRF_OES,
    MachineLibrary_StatusBit,
    MachineLibrary_StausBits,
    MachineLibrary_TCPIP_Link,
    MachineLibrary_TestRequest_OBLFOES,
    MachineLibrary_Transfer,
    MachineLibrary_TransferFileSection,
    MachineLibrary_Translate_Terminal,
    MachineLibrary_UnitConfig_ARL_XRF_OES,
    MachineLibrary_UnitConfig_Host,
    MachineLibrary_UnitConfig_OBLF_OES,
    MachineLibrary_UnitConfig_SuperQ_XRF,
    MachineLibrary_UnitConfig_Terminal,
    MachineLibrary_UnitGeneral,
    MachineLibrary_UnitGeneralParameters,
    MachineLibrary_UnitGeneralSpecial,
    MachineLibrary_UnitGeneral_AccPyc,
    MachineLibrary_UnitGeneral_HostPC,
    MachineLibrary_UnitGeneral_PM2PM,
    MachineLibrary_UnitGeneral_Remote,
    MachineLibrary_UnitGeneral_RigakuXRF,
    MachineLibrary_UnitGeneral_Scanner,
    MachineLibrary_UnitGeneral_SuperQ,
    MachineLibrary_UnitGeneral_Terminal,
    MachineLibrary_UnitProgParameters,
    MachineLibrary_UnitProgram,
    MachineLibrary_UnitPrograms,
    MachineLibrary_UnitSpecialConfiguration,
    MachineLibrary_Units,
    MachineLibrary_WS_Update_Host,
    MachineLibrary_WinCCAddTag,
    MachineLibrary_WinCCLnk,
    date,
    datetime,
    time,
)


def test_0():
    var_0 = "*i<\x0c,]I*m."
    var_1 = lambda *args, **kwargs: [False, True, -3884.26]
    var_2 = python_code_.MachineLibrary_Command(
        commandName=var_0,
        commandNo=[1, "{pBv(za:\r", 783.96],
        commandProgParameter=var_1,
    )
    var_3 = python_code_.MachineLibrary_Link2(
        link2Type=b"a${\r", link2ParamFile=var_1, link2ParamSection=var_1
    )
    var_4 = ';Neo]fiL*3T_3KMU"T'
    python_code_.MachineLibrary_UnitProgParameters(parameter=var_4, parameterNo=var_3)
    var_6 = -612
    var_7 = 1567
    var_8 = -1026
    var_9 = -1927
    var_10 = 1
    var_11 = python_code_.MachineLibrary_RobotToWinccs
    python_code_.MachineLibrary_Compac_Link(
        port=var_4,
        commConfig=var_1,
        params=var_0,
        byteCount=var_6,
        bytecountcode=var_7,
        checksum=var_3,
        checksumCode=[],
        retry=var_8,
        timeout=var_7,
        bcc=var_9,
        maxDataLength=var_10,
        splitLongMessage=var_10,
        useNotENQ=[],
        useNotACK_NAK=var_1,
        MachineLibrary_Compac_Link=var_11,
    )
    var_13 = python_code_.MachineLibrary_NodeGeneral(
        canCreateStateTag=var_4, canCreateErrorTag=var_4
    )
    var_14 = "e6 87"
    var_15 = "?^mR,gCe"
    var_16 = python_code_.MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(
        name=var_13, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES=617.59
    )
    var_17 = python_code_.MachineLibrary_UnitConfig_ARL_XRF_OES()
    var_18 = python_code_.MachineLibrary_GeneralSetting_ARL_XRF_OES(
        name=var_0, MachineLibrary_GeneralSetting_ARL_XRF_OES=var_17
    )
    var_19 = python_code_.MachineLibrary_OES_XRF_Condition(
        paraName=var_15,
        para=var_1,
        comment=var_9,
        seq_X=var_10,
        MachineLibrary_OES_XRF_Condition168=var_10,
        MachineLibrary_OES_XRF_Condition174=var_9,
        MachineLibrary_OES_XRF_Condition177=var_2,
        MachineLibrary_OES_XRF_Condition183=var_16,
        MachineLibrary_OES_XRF_Condition192=var_18,
    )
    var_20 = {var_19, var_19, var_19}
    python_code_.MachineLibrary_RecalRequest_OBLFOES(
        name=var_14, MachineLibrary_RecalRequest_OBLFOES164=var_20
    )
    var_22 = python_code_.MachineLibrary_CheckSample_SuperQXRF()
    python_code_.MachineLibrary_InsertRemove_Keywords_Host(
        keywordKey=var_14,
        keywordValue=var_1,
        MachineLibrary_InsertRemove_Keywords_Host=var_11,
    )
    python_code_.MachineLibrary_RobotToWinCC(
        robotToWinccTo_X=var_10,
        robotToWinccType_X=var_14,
        robotToWinccSeq_X=b"U\x90\xb7\x92\x11\x85\x95\x0e\x86\xa1%\x14\xbf\xfdT\xf2\xd6",
        robotToWinccFrom_X=None,
    )
    var_27 = -792
    var_28 = "MachineLibrary_WinCCAddTag MachineLibrary_NodeGeneralSpecial46 _MachineLibrary_Compac_Link__MachineLibrary_Compac_Link"
    python_code_.MachineLibrary_NodeGeneral_Terminal(
        terminalType=var_1,
        maxXValue=var_10,
        maxYValue=var_8,
        maxScreens=-1703.37,
        displayTime=var_4,
        customTimer1=var_9,
        customTimer2=var_27,
        signalCarrierPresent=var_8,
        keyBoardSignalCarrierPresent=var_22,
        stationAuto=var_14,
        steelCarrier=var_28,
        stationReady=var_1,
        lenOfPlanID=var_8,
        stationType=None,
        name_1=None,
        name_2=[4548],
        name_3=var_0,
        name_4=var_14,
        name_5=var_1,
        name_6=var_1,
    )


def test_1():
    var_0 = "=e)co'A\nG!."
    var_1 = "!kDlO_|2"
    var_2 = lambda *args, **kwargs: "MachineLibrary_UnitConfig_SuperQ_XRF116"
    var_3 = python_code_.MachineLibrary_RobotConfSendOrder(
        robotconfsendorderVar_X=var_0,
        robotconfsendorderFrom_X=var_1,
        robotconfsendorderType_X=None,
        robotconfsendorderSeq_X=var_2,
    )
    var_4 = 3863
    var_5 = python_code_.MachineLibrary_UnitGeneral_Remote(
        editWSDB=var_3, handshakeT=var_4, handshakeQ=var_2, handshakeA=var_0
    )
    var_6 = "f+!-2*Jx>!\x0b"
    var_7 = 2246
    python_code_.MachineLibrary_IBMWebsphereMQ(
        qName=False,
        readQueName=complex(808.591389, 1387.649977),
        readQueMgrName=var_0,
        readDynamicQueName=var_3,
        sendQueName=-332.46,
        sendQueMgrName=var_4,
        sendDynamicQueName=var_6,
        sendBuffer=var_2,
        receiveBuffer=var_7,
        maxDataSize=var_7,
    )
    var_9 = python_code_.MachineLibrary_UnitConfig_SuperQ_XRF()
    python_code_.MachineLibrary_ControlSamples_SuperQXRF(
        outOfControl=var_4, MachineLibrary_ControlSamples_SuperQXRF=var_9
    )
    var_11 = -1974
    var_12 = python_code_.MachineLibrary_RobotConfSendOrder(
        robotconfsendorderVar_X=var_4,
        robotconfsendorderFrom_X=var_5,
        robotconfsendorderType_X=var_6,
        robotconfsendorderSeq_X=var_11,
        MachineLibrary_RobotConfSendOrder=b"s\x00m\x00-i\xe1\x16\xa8\xcd0\xa5",
    )
    assert isinstance(var_12, python_code_.MachineLibrary_RobotConfSendOrder)
    python_code_.MachineLibrary_InsertRemove_Entry_Host(
        entryNo=var_7, entryName=var_0, MachineLibrary_InsertRemove_Entry_Host=var_2
    )
    var_16 = bool
    python_code_.MachineLibrary_NodeGeneral_AccuPycMeter(
        polling=var_16,
        runTimout=var_9,
        expectSampleWeight=var_0,
        sendSampleWeight=complex(-237.75113, -1854.095),
    )
    var_18 = python_code_.MachineLibrary_UnitConfig_OBLF_OES()
    var_19 = "]"
    var_20 = python_code_.MachineLibrary_TestRequest_OBLFOES(
        name=var_3, MachineLibrary_TestRequest_OBLFOES=var_18
    )
    var_21 = python_code_.MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(name=[2522.63])
    var_22 = python_code_.MachineLibrary_DisableSCT_ARL_XRF_OES(name=var_1)
    var_23 = python_code_.MachineLibrary_OES_XRF_Condition(
        paraName=var_6,
        para=var_19,
        comment=(False, 3749, -803),
        seq_X=[False],
        MachineLibrary_OES_XRF_Condition=False,
        MachineLibrary_OES_XRF_Condition162=var_20,
        MachineLibrary_OES_XRF_Condition171={True, False, -2486.7},
        MachineLibrary_OES_XRF_Condition180=var_21,
        MachineLibrary_OES_XRF_Condition186=var_22,
        MachineLibrary_OES_XRF_Condition192=True,
    )
    assert isinstance(var_23, python_code_.MachineLibrary_OES_XRF_Condition)
    var_24 = 'nuS"E['
    var_25 = python_code_.MachineLibrary_UnitConfig_ARL_XRF_OES()
    var_26 = python_code_.MachineLibrary_ExecuteFiling_ARL_XRF_OES(
        name=var_24, MachineLibrary_ExecuteFiling_ARL_XRF_OES=var_25
    )
    var_27 = python_code_.MachineLibrary_OES_XRF_Condition(
        paraName=var_19,
        para={},
        comment=var_4,
        seq_X=var_4,
        MachineLibrary_OES_XRF_Condition171=var_26,
    )
    var_28 = {var_23, var_27, var_27}
    python_code_.MachineLibrary_GeneralSetting_ARL_XRF_OES(
        name=var_1,
        MachineLibrary_GeneralSetting_ARL_XRF_OES=var_2,
        MachineLibrary_GeneralSetting_ARL_XRF_OES191=var_28,
    )


def test_2():
    var_0 = -259
    python_code_.MachineLibrary_DPbase_Node(nodeNo=var_0, isXPS=var_0)
    var_2 = python_code_.MachineLibrary_UnitPrograms()
    var_3 = python_code_.MachineLibrary_ParamPrint
    python_code_.MachineLibrary_SepByComma_Scanner(activ=var_0, preDefWS=var_3)
    python_code_.MachineLibrary_NodeGeneral_PM2PM(timeServer=var_2, type=var_0)
    var_7 = ',<41OI"OBGYSt\x0c'
    python_code_.MachineLibrary_LabMachine(
        machineName=var_7,
        machineVersionNo=var_3,
        versionRemark=var_7,
        driver="P^xm|H[^we",
        linkType=var_7,
        linkParamFile=var_0,
        linkParamSection=var_3,
        createWinCCTags=var_7,
        MachineLibrary_LabMachine4={
            ";": "MachineLibrary_InsertRemove_Entry_Host,_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration242,_MachineLibrary_Translate_Terminal__MachineLibrary_Translate_Terminal",
            "p": 1,
        },
        MachineLibrary_LabMachine6=var_0,
    )
    python_code_.MachineLibrary_NodeGeneral_AccuPycMeter(
        polling=var_3,
        runTimout=b"\xb8W\xe2}\x805\xa1[\x8f\x97\xbb\x10",
        expectSampleWeight=var_0,
        sendSampleWeight=var_0,
    )
    var_10 = 1422
    var_11 = python_code_.MachineLibrary_UnitProgParameters
    var_12 = -93
    var_13 = python_code_.MachineLibrary_UnitGeneralSpecial()
    python_code_.MachineLibrary_UnitGeneral_Scanner(
        forcedSampleType=var_10,
        registerSample=var_11,
        start=var_12,
        length={"P4 79WO57QPO": -1148},
        fillWith=var_0,
        addString=116.96,
        preString=var_3,
        MachineLibrary_UnitGeneral_Scanner=var_13,
    )
    python_code_.MachineLibrary_UnitProgParameters(parameter=var_3, parameterNo=var_3)
    var_16 = -1934
    var_17 = "_MachineLibrary_NodeGeneral_RemotePM__MachineLibrary_NodeGeneral_RemotePM"
    var_18 = -1960
    python_code_.MachineLibrary_RobotVarToErrorbit(
        robotvartoerrorbitVar_X=var_3,
        robotvartoerrorbitBit_X=var_7,
        robotvartoerrorbitInv_X=var_16,
        robotvartoerrorbitType_X=var_17,
        robotvartoerrorbitSeq_X=var_18,
    )
    var_20 = "QJ-TxW"
    python_code_.MachineLibrary_DisableSCT_ARL_XRF_OES(name=var_20)
    var_23 = 136
    python_code_.MachineLibrary_UnitGeneral_HostPC(
        maxIndex=var_12, index=var_18, replyOnLink=var_23, writeDumyIfNoDataExist=var_3
    )
    var_29 = "_MachineLibrary_Parameter__MachineLibrary_Parameter"
    python_code_.MachineLibrary_DisableSCT_ARL_XRF_OES(
        name=var_29, MachineLibrary_DisableSCT_ARL_XRF_OES=var_12
    )


def test_3():
    var_0 = 2118.44
    var_1 = python_code_.MachineLibrary_UnitGeneral_AccPyc(
        cupWeight=var_0, minSampleWeight=b"\x90X~\xcf.h\xa6\xbf\x91\x03-\xc4#"
    )
    python_code_.MachineLibrary_UnitGeneral_SuperQ(
        lastPosInInstrument=var_1, lastPosAnalysing=-5072.76
    )
    var_3 = 1
    var_4 = 125
    python_code_.MachineLibrary_Moved_Host(
        report_ALL=var_3, pos0=var_4, type0=var_3, writePositionNameInFile=var_3
    )
    var_6 = python_code_.MachineLibrary_RobotVarToBusyCodes
    var_7 = "i{\x0c/>1\x0c"
    var_8 = python_code_.MachineLibrary_PS_Process_Finished_ARL_XRF_OES
    python_code_.MachineLibrary_Translate_Terminal(
        auto_Ready=var_6, auto_Busy=var_7, man_Ready=set(), man_Busy=var_8
    )
    var_10 = -5041
    var_11 = 1825
    var_12 = 2827
    python_code_.MachineLibrary_Compac_Link(
        port=var_0,
        commConfig=var_7,
        params=var_4,
        byteCount=var_10,
        bytecountcode=b"\x131\xf3 \xb1B\xa8\x7fK\xbd*&",
        checksum=None,
        checksumCode=b"\xce",
        retry=var_11,
        timeout=var_10,
        bcc=complex(191.76155, 685.91254),
        maxDataLength=var_1,
        splitLongMessage=var_6,
        useNotENQ=var_8,
        useNotACK_NAK=var_12,
    )
    python_code_.MachineLibrary_ControlSamples_SuperQXRF(outOfControl=var_6)
    var_16 = python_code_.MachineLibrary_InsertRemove_Host(
        report_All=b"\x02\xda\xff\x85\xc8\xda\x02\xac\xe7\xaf\xfc\x90q\xb9\x10Y\xd6\x07",
        MachineLibrary_InsertRemove_Host200="_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition189",
    )
    var_17 = python_code_.MachineLibrary_InsertRemove_Types_Host(
        typeNo=var_11, typeValue=var_0, MachineLibrary_InsertRemove_Types_Host=var_16
    )
    assert isinstance(var_17, python_code_.MachineLibrary_InsertRemove_Types_Host)
    var_18 = 268
    python_code_.MachineLibrary_TransferFileSection(
        transferFile=var_3, transferSection=var_7, transferSeq=var_18
    )
    var_20 = -1067.43
    python_code_.MachineLibrary_PMMachineLibrary(
        libraryVersion=var_20, libraryVersionRemark=var_7
    )


@pytest.mark.xfail(strict=True)
def test_4():
    var_0 = 22
    var_1 = -41
    var_2 = -1
    var_3 = '&6"HZOU]@"t'
    var_4 = "_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig40:MachineLibrary_CommunicationData"
    var_5 = "#$/"
    var_6 = "_MachineLibrary_UnitGeneral_HostPC__MachineLibrary_UnitGeneral_HostPC:_MachineLibrary_GeneralSetting_ARL_XRF_OES__MachineLibrary_GeneralSetting_ARL_XRF_OES:MachineLibrary_UnitGeneralSpecial"
    var_7 = python_code_.MachineLibrary_NodeGeneralSpecial()
    var_8 = python_code_.MachineLibrary_NodeGeneral_Terminal(
        terminalType=var_0,
        maxXValue=var_0,
        maxYValue=var_0,
        maxScreens=var_0,
        displayTime=var_0,
        customTimer1={124},
        customTimer2=var_1,
        signalCarrierPresent=var_2,
        keyBoardSignalCarrierPresent=var_1,
        stationAuto=var_3,
        steelCarrier=var_4,
        stationReady=var_5,
        lenOfPlanID=(3097,),
        stationType=var_0,
        name_1=var_5,
        name_2=var_4,
        name_3=True,
        name_4=var_6,
        name_5=complex(328.0929413, -382.4894),
        name_6=var_5,
        MachineLibrary_NodeGeneral_Terminal=var_7,
    )
    var_9 = "wk\r-U`BL]F}$"
    var_10 = python_code_.MachineLibrary_FileTransfer_Link(
        writePath=var_3,
        readPath="uOzP.O\x0b`c0[aX/",
        flagDelAfterReading={},
        flagWriteAfterReading=var_1,
        flagToWriteWaitForDeleted=None,
        flagToWriteWaitFor=complex(994.5128199, 2201.441),
        delimter=var_7,
        writeAfterReading={"4 iUR..D7 x4", ""},
        toWriteWaitFor=var_3,
        translation=var_2,
        delimiter=True,
        sendBuffer=var_0,
        receiveBuffer={
            -1471.58,
            False,
            "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179",
        },
        maxDataLength=var_8,
        timeoutwrite=var_9,
        pollTime=var_8,
    )
    var_11 = python_code_.MachineLibrary_LabMachines()
    var_12 = 153
    var_13 = -813
    var_14 = 502
    var_15 = 731
    var_16 = 3921
    var_17 = 2
    var_18 = -1732
    var_19 = 2166
    var_20 = -2441
    var_21 = "qHaj=H"
    var_22 = lambda *args, **kwargs: False
    python_code_.MachineLibrary_NodeGeneral_Terminal(
        terminalType=var_12,
        maxXValue=var_13,
        maxYValue=var_12,
        maxScreens="MachineLibrary_PlainMoveEntrySend",
        displayTime=var_14,
        customTimer1=var_15,
        customTimer2=var_16,
        signalCarrierPresent=var_17,
        keyBoardSignalCarrierPresent=var_18,
        stationAuto=var_17,
        steelCarrier=var_10,
        stationReady=(True, 1282, 3520.82),
        lenOfPlanID=var_19,
        stationType=var_20,
        name_1=var_8,
        name_2=var_4,
        name_3=var_21,
        name_4=(True, -382, 4379.16),
        name_5=var_22,
        name_6=None,
    )
    var_24 = "0m 2"
    var_25 = python_code_.MachineLibrary_OutputRequest_OBLFOES(name=var_24)
    var_26 = "&(S\rhReMlpP\\|W"
    var_27 = python_code_.MachineLibrary_Serial_Link(
        port=var_22,
        commConfig=var_17,
        params=var_11,
        endChar=-766.7,
        maxCharDelay=var_6,
        bufferLenght=var_26,
        startChar=-1466.89,
        logging=var_16,
    )
    python_code_.MachineLibrary_TransferFileSection(
        transferFile=var_9,
        transferSection=var_22,
        transferSeq=complex(2471.906, 1022.0),
        MachineLibrary_TransferFileSection=var_25,
    )
    python_code_.MachineLibrary_RecalRequest_OBLFOES(name=var_27)
    python_code_.MachineLibrary_ExePrepUnit_ARL_XRF_OES(
        name=False, MachineLibrary_ExePrepUnit_ARL_XRF_OES=var_6
    )
    python_code_.MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(
        name=2, MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179=var_22
    )


def test_5():
    var_0 = python_code_.MachineLibrary_Transfer()
    var_1 = "_MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES-_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition186-MachineLibrary_Units-_MachineLibrary_PlainMove__MachineLibrary_PlainMove238"
    python_code_.MachineLibrary_UnitGeneral_Remote(
        editWSDB=complex(-448.4667, 1777.65),
        handshakeT=var_0,
        handshakeQ=var_0,
        handshakeA=var_1,
    )
    var_3 = lambda *args, **kwargs: False
    var_4 = "SlQ35_oB/"
    var_5 = -812
    var_6 = -218
    var_7 = python_code_.MachineLibrary_LinkConfig()
    python_code_.MachineLibrary_IBMWebsphereMQ(
        qName=var_0,
        readQueName=var_3,
        readQueMgrName={},
        readDynamicQueName=var_4,
        sendQueName=var_1,
        sendQueMgrName="wc\x0bp7Sz~=PJyyh\t6",
        sendDynamicQueName=var_3,
        sendBuffer=var_5,
        receiveBuffer=var_3,
        maxDataSize=var_6,
        MachineLibrary_IBMWebsphereMQ=var_7,
    )
    var_9 = python_code_.MachineLibrary_CheckSampleRunTime_SuperQXRF()
    var_10 = python_code_.MachineLibrary_PlainMove(
        plainmoveType=var_7,
        plainmoveSID_REF=complex(-448.3, -2602.805),
        plainmovePreDefWS="MachineLibrary_OES_XRF_Condition183,MachineLibrary_RobotConfSendOrders,_MachineLibrary_InsertRemove_Keywords_Host__MachineLibrary_InsertRemove_Keywords_Host,MachineLibrary_UnitConfig_ARL_XRF_OES130",
    )
    assert isinstance(var_10, python_code_.MachineLibrary_PlainMove)
    var_11 = python_code_.MachineLibrary_Transfer()
    var_12 = "\n*r[R"
    var_13 = "\x0b;QgcQ2I]-qF$"
    var_14 = "lX,E1B`[H*9Jp<"
    python_code_.MachineLibrary_Parameter(
        parameterName="h6r\raT&VW,X2oGYg",
        parameterT1=var_12,
        parameterT2=True,
        parameterV={"MachineLibrary_UnitConfig_ARL_XRF_OES136": 3},
        parameterType=var_13,
        parameterV0=var_14,
        parameterV1=None,
        parameterMin=var_6,
        parameterMax=var_6,
        parameterParaLen=var_6,
        parameterConfig=1525.29,
    )
    var_16 = -446
    python_code_.MachineLibrary_CommunicationData(
        comErrorDataLength=[],
        comSIDDataAddress=var_1,
        comSIDDataLength=None,
        comProgressIndDataAddress=var_1,
        comProgressIndDataLength=var_16,
        comSendDataAddress=var_1,
        comSendDataLength=var_16,
        comRequestDataAddress=var_13,
        comRequestDataLength=var_16,
        comErrorDataAddress=2748,
    )
    var_20 = -1254
    python_code_.MachineLibrary_UnitGeneral_SuperQ(
        lastPosInInstrument=var_3, lastPosAnalysing=var_20
    )
    var_22 = "MachineLibrary_UnitConfig_Host"
    var_23 = python_code_.MachineLibrary_UnitGeneralSpecial()
    python_code_.MachineLibrary_UnitGeneral_Terminal(
        station3=var_1,
        station4=b"\xb9\xa5\xbf\x86\xf5%\xfa\x8e\xa8\xf1&s\xa7P\x8fY\x00",
        station5=var_9,
        thisStation=var_12,
        station1=var_9,
        station2=var_22,
        MachineLibrary_UnitGeneral_Terminal=var_23,
    )
    var_25 = python_code_.MachineLibrary_UnitProgram(
        unitProgName=b"\xde-\xddF\x16\x15\x99z\xae\xa7o\x0e+"
    )
    assert isinstance(var_25, python_code_.MachineLibrary_UnitProgram)
    var_26 = 3
    python_code_.MachineLibrary_ControlSamples_SuperQXRF(outOfControl=var_26)
    python_code_.MachineLibrary_HistoryConfig_AccuPyc(
        currentSample=[],
        currentSampleID=var_13,
        sampleCupWeight=complex(3861.1668907, 1968.7872424),
    )
    var_30 = "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES"
    var_31 = -1237
    var_32 = -1251
    var_33 = 1444
    var_34 = -434
    var_35 = python_code_.MachineLibrary_Compac_Link
    python_code_.MachineLibrary_Compac_Link(
        port=var_11,
        commConfig=complex(2026.6234512, -341.524574),
        params=var_30,
        byteCount=b"\x9cM\xe9\xea\xc0]Mj\x06D\xba\xac\x13)N",
        bytecountcode=var_3,
        checksum=b"\x17\x866,(xo\x06x\x87",
        checksumCode=var_31,
        retry=var_32,
        timeout=var_32,
        bcc=complex(-1107.4489, -1848.2125765),
        maxDataLength=var_33,
        splitLongMessage=var_20,
        useNotENQ=var_34,
        useNotACK_NAK=var_35,
    )


def test_6():
    python_code_.MachineLibrary_ErrorMessage_OBLFOES(errorMessage=[])
    var_1 = python_code_.MachineLibrary_RobotWinCCToRobots()
    var_2 = "_MachineLibrary_File_Sample_ARL_XRF_OES__MachineLibrary_File_Sample_ARL_XRF_OES"
    var_3 = 421
    python_code_.MachineLibrary_StatusBit(bitName=var_2, bitNo=var_3)
    var_5 = python_code_.MachineLibrary_NodeGeneralSpecial()
    python_code_.MachineLibrary_NodeGeneral_PM2PM(
        timeServer=(-1231.65, 407.52, ".^E|;A $E#z!t"),
        type=var_3,
        MachineLibrary_NodeGeneral_PM2PM=var_5,
    )
    var_7 = "_MachineLibrary_RobotWinCCToRobot__MachineLibrary_RobotWinCCToRobot"
    python_code_.MachineLibrary_CheckAddSID_Values_PM2PM(
        optionNo=var_3, optonValue=var_7
    )
    python_code_.MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES(name=var_7)
    python_code_.MachineLibrary_GeneralParameter_SuperQXRF(
        switchRemote="_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig34",
        startList=var_1,
        listName=True,
    )
    var_11 = 1400
    python_code_.MachineLibrary_WS_Update_Host(
        checkUnit=var_11, AllowUnit0=var_3, MachineLibrary_WS_Update_Host=var_11
    )


def test_7():
    var_0 = (
        lambda *args, **kwargs: "MachineLibrary_RobotWarningONDelete,MachineLibrary_NodeGeneralSpecial46,_MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES,_MachineLibrary_NodeGeneral_WinCC2WinCC__MachineLibrary_NodeGeneral_WinCC2WinCC54"
    )
    python_code_.MachineLibrary_ExePrepUnit_ARL_XRF_OES(name=var_0)
    var_2 = -3435.9
    var_3 = -3480.29
    python_code_.MachineLibrary_UnitGeneral_AccPyc(
        cupWeight=var_2, minSampleWeight=var_3
    )
    var_5 = ";Y"
    python_code_.MachineLibrary_SepByComma_ID_Scanner(
        idSeq_X=3364.89,
        idValue=var_2,
        idPrevValue=var_5,
        idCharValue={"}>dYF", 568.12, "$E3v,$:%8n'"},
        MachineLibrary_SepByComma_ID_Scanner=var_0,
    )
    python_code_.MachineLibrary_NodeGeneral(
        canCreateStateTag=var_5, canCreateErrorTag=var_0
    )
    var_8 = -776
    var_9 = ":}E"
    python_code_.MachineLibrary_UnitGeneral_Scanner(
        forcedSampleType=var_8,
        registerSample=var_0,
        start=-1396,
        length=var_8,
        fillWith=complex(-575.46, -51.4144),
        addString=var_5,
        preString=var_9,
    )
    var_11 = "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179.MachineLibrary_UnitConfig_ARL_XRF_OES142.MachineLibrary_UnitConfig_OBLF_OES108._MachineLibrary_NodeConfig__MachineLibrary_NodeConfig28"
    var_12 = python_code_.MachineLibrary_InsertRemove_Types_Host(
        typeNo=var_8, typeValue=var_11
    )
    var_14 = 2
    python_code_.MachineLibrary_NodeGeneral_PM2PM(timeServer=var_14, type=-1562)
    python_code_.MachineLibrary_RecalRequest_OBLFOES(name=var_12)


@pytest.mark.xfail(strict=True)
def test_8():
    var_1 = python_code_.MachineLibrary_UnitProgram
    var_2 = 2371
    python_code_.MachineLibrary_UnitGeneral_RigakuXRF(
        lastPoHAG_SIInstrument=None,
        lastPosAnalyHAG_SIg={"crP}ZZf"},
        lastPosInInstrument=var_1,
        separator=var_2,
        MachineLibrary_UnitGeneral_RigakuXRF=b"\x8aw\\>O\xa9>\xd9\xeah<1\x98\xc61",
    )
    var_5 = "{"
    python_code_.MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(
        name=var_5, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182=var_1
    )


def test_9():
    python_code_.MachineLibrary_Communication_SuperQXRF(
        enq_ACK_Protocol=(True, 4003.89, 1266)
    )
    var_1 = 2767
    var_2 = "wk1fk\x0bL#U@OiP"
    var_3 = -668
    var_4 = python_code_.MachineLibrary_ExePrepUnit_ARL_XRF_OES
    var_5 = python_code_.MachineLibrary_CommunicationData(
        comErrorDataLength=var_1,
        comSIDDataAddress=var_2,
        comSIDDataLength=var_3,
        comProgressIndDataAddress=var_2,
        comProgressIndDataLength=b"\x99\x93X\xee\xde+\x9d",
        comSendDataAddress=var_4,
        comSendDataLength=var_1,
        comRequestDataAddress=-1782,
        comRequestDataLength=var_1,
        comErrorDataAddress=var_2,
        MachineLibrary_CommunicationData=var_4,
    )
    var_6 = 824
    var_7 = 3
    var_8 = "Kk*%fM"
    var_9 = -1427
    var_10 = "W\\#X\x0bmlGN}"
    python_code_.MachineLibrary_FileTransfer_Link(
        writePath=None,
        readPath=True,
        flagDelAfterReading=False,
        flagWriteAfterReading=var_1,
        flagToWriteWaitForDeleted=var_6,
        flagToWriteWaitFor=var_6,
        delimter=var_4,
        writeAfterReading=var_7,
        toWriteWaitFor=var_8,
        translation=var_3,
        delimiter=b"\xfd\x128\x19<\\J\xd6\x87.J\xad9",
        sendBuffer=var_1,
        receiveBuffer=var_9,
        maxDataLength={1707.13},
        timeoutwrite=var_10,
        pollTime=var_5,
    )
    var_12 = "MachineLibrary_InsertRemove_Host200MachineLibrary_UnitConfig_ARL_XRF_OES142MachineLibrary_UnitGeneral"
    var_13 = 2
    var_14 = "MachineLibrary_UnitGeneralSpecial88"
    python_code_.MachineLibrary_CommunicationData(
        comErrorDataLength=var_4,
        comSIDDataAddress=var_3,
        comSIDDataLength=var_7,
        comProgressIndDataAddress=var_12,
        comProgressIndDataLength=var_1,
        comSendDataAddress=var_4,
        comSendDataLength=var_13,
        comRequestDataAddress=var_14,
        comRequestDataLength=var_4,
        comErrorDataAddress=var_4,
    )
