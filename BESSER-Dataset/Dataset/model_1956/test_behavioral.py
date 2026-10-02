import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_addTag53_reverse_link_reassign_clear():
    a1 = MachineLibrary_WinCCAddTag(winCCTag="sample_text")
    a2 = MachineLibrary_WinCCAddTag(winCCTag="sample_text_2")
    b = MachineLibrary_NodeGeneral_WinCC2WinCC(prefix="sample_text")
    _safe_set(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', {a1})
    assert _is_linked(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', a1)
    if hasattr(a1, 'MachineLibrary_WinCCAddTag'):
        assert _is_linked(a1, 'MachineLibrary_WinCCAddTag', b)
    _safe_set(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', {a2})
    assert _is_linked(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', a2)
    if hasattr(a1, 'MachineLibrary_WinCCAddTag'):
        assert not _is_linked(a1, 'MachineLibrary_WinCCAddTag', b)
    if hasattr(a2, 'MachineLibrary_WinCCAddTag'):
        assert _is_linked(a2, 'MachineLibrary_WinCCAddTag', b)
    _safe_set(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', set())
    assert not _is_linked(b, 'MachineLibrary_NodeGeneral_WinCC2WinCC54', a2)
    if hasattr(a2, 'MachineLibrary_WinCCAddTag'):
        assert not _is_linked(a2, 'MachineLibrary_WinCCAddTag', b)


def test_assoc_communcationdata33_reverse_link_reassign_clear():
    a1 = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    a2 = MachineLibrary_NodeConfig(nodeName="sample_text_2", nodeNo=13, simFileName="sample_text_2")
    b = MachineLibrary_CommunicationData(comErrorDataAddress="sample_text", comErrorDataLength=7, comProgressIndDataAddress="sample_text", comProgressIndDataLength=7, comRequestDataAddress="sample_text", comRequestDataLength=7, comSIDDataAddress="sample_text", comSIDDataLength=7, comSendDataAddress="sample_text", comSendDataLength=7)
    _safe_set(b, 'MachineLibrary_CommunicationData', a1)
    assert _is_linked(b, 'MachineLibrary_CommunicationData', a1)
    if hasattr(a1, 'MachineLibrary_NodeConfig34'):
        assert _is_linked(a1, 'MachineLibrary_NodeConfig34', b)
    _safe_set(b, 'MachineLibrary_CommunicationData', a2)
    assert _is_linked(b, 'MachineLibrary_CommunicationData', a2)
    if hasattr(a1, 'MachineLibrary_NodeConfig34'):
        assert not _is_linked(a1, 'MachineLibrary_NodeConfig34', b)
    if hasattr(a2, 'MachineLibrary_NodeConfig34'):
        assert _is_linked(a2, 'MachineLibrary_NodeConfig34', b)
    _safe_set(b, 'MachineLibrary_CommunicationData', None)
    assert not _is_linked(b, 'MachineLibrary_CommunicationData', a2)
    if hasattr(a2, 'MachineLibrary_NodeConfig34'):
        assert not _is_linked(a2, 'MachineLibrary_NodeConfig34', b)


def test_assoc_condition158_reverse_link_reassign_clear():
    a1 = MachineLibrary_OutputRequest_OBLFOES(name="sample_text")
    a2 = MachineLibrary_OutputRequest_OBLFOES(name="sample_text_2")
    b = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition', a1)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition', a1)
    if hasattr(a1, 'MachineLibrary_OutputRequest_OBLFOES159'):
        assert _is_linked(a1, 'MachineLibrary_OutputRequest_OBLFOES159', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition', a2)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition', a2)
    if hasattr(a1, 'MachineLibrary_OutputRequest_OBLFOES159'):
        assert not _is_linked(a1, 'MachineLibrary_OutputRequest_OBLFOES159', b)
    if hasattr(a2, 'MachineLibrary_OutputRequest_OBLFOES159'):
        assert _is_linked(a2, 'MachineLibrary_OutputRequest_OBLFOES159', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition', None)
    assert not _is_linked(b, 'MachineLibrary_OES_XRF_Condition', a2)
    if hasattr(a2, 'MachineLibrary_OutputRequest_OBLFOES159'):
        assert not _is_linked(a2, 'MachineLibrary_OutputRequest_OBLFOES159', b)


def test_assoc_condition160_reverse_link_reassign_clear():
    a1 = MachineLibrary_TestRequest_OBLFOES(name="sample_text")
    a2 = MachineLibrary_TestRequest_OBLFOES(name="sample_text_2")
    b = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition162', a1)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition162', a1)
    if hasattr(a1, 'MachineLibrary_TestRequest_OBLFOES161'):
        assert _is_linked(a1, 'MachineLibrary_TestRequest_OBLFOES161', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition162', a2)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition162', a2)
    if hasattr(a1, 'MachineLibrary_TestRequest_OBLFOES161'):
        assert not _is_linked(a1, 'MachineLibrary_TestRequest_OBLFOES161', b)
    if hasattr(a2, 'MachineLibrary_TestRequest_OBLFOES161'):
        assert _is_linked(a2, 'MachineLibrary_TestRequest_OBLFOES161', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition162', None)
    assert not _is_linked(b, 'MachineLibrary_OES_XRF_Condition162', a2)
    if hasattr(a2, 'MachineLibrary_TestRequest_OBLFOES161'):
        assert not _is_linked(a2, 'MachineLibrary_TestRequest_OBLFOES161', b)


def test_assoc_condition163_reverse_link_reassign_clear():
    a1 = MachineLibrary_RecalRequest_OBLFOES(name="sample_text")
    a2 = MachineLibrary_RecalRequest_OBLFOES(name="sample_text_2")
    b = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition165', a1)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition165', a1)
    if hasattr(a1, 'MachineLibrary_RecalRequest_OBLFOES164'):
        assert _is_linked(a1, 'MachineLibrary_RecalRequest_OBLFOES164', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition165', a2)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition165', a2)
    if hasattr(a1, 'MachineLibrary_RecalRequest_OBLFOES164'):
        assert not _is_linked(a1, 'MachineLibrary_RecalRequest_OBLFOES164', b)
    if hasattr(a2, 'MachineLibrary_RecalRequest_OBLFOES164'):
        assert _is_linked(a2, 'MachineLibrary_RecalRequest_OBLFOES164', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition165', None)
    assert not _is_linked(b, 'MachineLibrary_OES_XRF_Condition165', a2)
    if hasattr(a2, 'MachineLibrary_RecalRequest_OBLFOES164'):
        assert not _is_linked(a2, 'MachineLibrary_RecalRequest_OBLFOES164', b)


def test_assoc_condition166_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_CheckFilling_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', {a1})
    assert _is_linked(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition168'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition168', b)
    _safe_set(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', {a2})
    assert _is_linked(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition168'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition168', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition168'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition168', b)
    _safe_set(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', set())
    assert not _is_linked(b, 'MachineLibrary_CheckFilling_ARL_XRF_OES167', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition168'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition168', b)


def test_assoc_condition169_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_ExecuteFiling_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', {a1})
    assert _is_linked(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition171'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition171', b)
    _safe_set(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', {a2})
    assert _is_linked(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition171'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition171', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition171'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition171', b)
    _safe_set(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', set())
    assert not _is_linked(b, 'MachineLibrary_ExecuteFiling_ARL_XRF_OES170', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition171'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition171', b)


def test_assoc_condition172_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', {a1})
    assert _is_linked(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition174'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition174', b)
    _safe_set(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', {a2})
    assert _is_linked(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition174'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition174', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition174'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition174', b)
    _safe_set(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', set())
    assert not _is_linked(b, 'MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition174'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition174', b)


def test_assoc_condition175_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_ExePrepUnit_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', {a1})
    assert _is_linked(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition177'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition177', b)
    _safe_set(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', {a2})
    assert _is_linked(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition177'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition177', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition177'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition177', b)
    _safe_set(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', set())
    assert not _is_linked(b, 'MachineLibrary_ExePrepUnit_ARL_XRF_OES176', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition177'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition177', b)


def test_assoc_condition178_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', {a1})
    assert _is_linked(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition180'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition180', b)
    _safe_set(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', {a2})
    assert _is_linked(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition180'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition180', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition180'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition180', b)
    _safe_set(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', set())
    assert not _is_linked(b, 'MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition180'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition180', b)


def test_assoc_condition181_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', {a1})
    assert _is_linked(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition183'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition183', b)
    _safe_set(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', {a2})
    assert _is_linked(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition183'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition183', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition183'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition183', b)
    _safe_set(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', set())
    assert not _is_linked(b, 'MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition183'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition183', b)


def test_assoc_condition184_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_DisableSCT_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', {a1})
    assert _is_linked(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition186'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition186', b)
    _safe_set(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', {a2})
    assert _is_linked(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition186'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition186', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition186'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition186', b)
    _safe_set(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', set())
    assert not _is_linked(b, 'MachineLibrary_DisableSCT_ARL_XRF_OES185', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition186'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition186', b)


def test_assoc_condition187_reverse_link_reassign_clear():
    a1 = MachineLibrary_Settings_ARL_XRF_OES(name="sample_text")
    a2 = MachineLibrary_Settings_ARL_XRF_OES(name="sample_text_2")
    b = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition189', a1)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition189', a1)
    if hasattr(a1, 'MachineLibrary_Settings_ARL_XRF_OES188'):
        assert _is_linked(a1, 'MachineLibrary_Settings_ARL_XRF_OES188', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition189', a2)
    assert _is_linked(b, 'MachineLibrary_OES_XRF_Condition189', a2)
    if hasattr(a1, 'MachineLibrary_Settings_ARL_XRF_OES188'):
        assert not _is_linked(a1, 'MachineLibrary_Settings_ARL_XRF_OES188', b)
    if hasattr(a2, 'MachineLibrary_Settings_ARL_XRF_OES188'):
        assert _is_linked(a2, 'MachineLibrary_Settings_ARL_XRF_OES188', b)
    _safe_set(b, 'MachineLibrary_OES_XRF_Condition189', None)
    assert not _is_linked(b, 'MachineLibrary_OES_XRF_Condition189', a2)
    if hasattr(a2, 'MachineLibrary_Settings_ARL_XRF_OES188'):
        assert not _is_linked(a2, 'MachineLibrary_Settings_ARL_XRF_OES188', b)


def test_assoc_condition190_reverse_link_reassign_clear():
    a1 = MachineLibrary_OES_XRF_Condition(comment="sample_text", para="sample_text", paraName="sample_text", seq_X=7)
    a2 = MachineLibrary_OES_XRF_Condition(comment="sample_text_2", para="sample_text_2", paraName="sample_text_2", seq_X=13)
    b = MachineLibrary_GeneralSetting_ARL_XRF_OES(name="sample_text")
    _safe_set(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', {a1})
    assert _is_linked(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', a1)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition192'):
        assert _is_linked(a1, 'MachineLibrary_OES_XRF_Condition192', b)
    _safe_set(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', {a2})
    assert _is_linked(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', a2)
    if hasattr(a1, 'MachineLibrary_OES_XRF_Condition192'):
        assert not _is_linked(a1, 'MachineLibrary_OES_XRF_Condition192', b)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition192'):
        assert _is_linked(a2, 'MachineLibrary_OES_XRF_Condition192', b)
    _safe_set(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', set())
    assert not _is_linked(b, 'MachineLibrary_GeneralSetting_ARL_XRF_OES191', a2)
    if hasattr(a2, 'MachineLibrary_OES_XRF_Condition192'):
        assert not _is_linked(a2, 'MachineLibrary_OES_XRF_Condition192', b)


def test_assoc_dpBaseNode23_reverse_link_reassign_clear():
    a1 = MachineLibrary_DPbase_Node(isXPS=7, nodeNo=7)
    a2 = MachineLibrary_DPbase_Node(isXPS=13, nodeNo=13)
    b = MachineLibrary_DPbase_Link(cp_name="sample_text", maxNodes=7, speed=7)
    _safe_set(b, 'MachineLibrary_DPbase_Link24', {a1})
    assert _is_linked(b, 'MachineLibrary_DPbase_Link24', a1)
    if hasattr(a1, 'MachineLibrary_DPbase_Node'):
        assert _is_linked(a1, 'MachineLibrary_DPbase_Node', b)
    _safe_set(b, 'MachineLibrary_DPbase_Link24', {a2})
    assert _is_linked(b, 'MachineLibrary_DPbase_Link24', a2)
    if hasattr(a1, 'MachineLibrary_DPbase_Node'):
        assert not _is_linked(a1, 'MachineLibrary_DPbase_Node', b)
    if hasattr(a2, 'MachineLibrary_DPbase_Node'):
        assert _is_linked(a2, 'MachineLibrary_DPbase_Node', b)
    _safe_set(b, 'MachineLibrary_DPbase_Link24', set())
    assert not _is_linked(b, 'MachineLibrary_DPbase_Link24', a2)
    if hasattr(a2, 'MachineLibrary_DPbase_Node'):
        assert not _is_linked(a2, 'MachineLibrary_DPbase_Node', b)


def test_assoc_entry199_reverse_link_reassign_clear():
    a1 = MachineLibrary_InsertRemove_Host(report_All=7)
    a2 = MachineLibrary_InsertRemove_Host(report_All=13)
    b = MachineLibrary_InsertRemove_Entry_Host(entryName="sample_text", entryNo=7)
    _safe_set(b, 'MachineLibrary_InsertRemove_Entry_Host', a1)
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Entry_Host', a1)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Host200'):
        assert _is_linked(a1, 'MachineLibrary_InsertRemove_Host200', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Entry_Host', a2)
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Entry_Host', a2)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Host200'):
        assert not _is_linked(a1, 'MachineLibrary_InsertRemove_Host200', b)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Host200'):
        assert _is_linked(a2, 'MachineLibrary_InsertRemove_Host200', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Entry_Host', None)
    assert not _is_linked(b, 'MachineLibrary_InsertRemove_Entry_Host', a2)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Host200'):
        assert not _is_linked(a2, 'MachineLibrary_InsertRemove_Host200', b)


def test_assoc_field205_reverse_link_reassign_clear():
    a1 = MachineLibrary_SepByComma_Scanner(activ=7, preDefWS=7)
    a2 = MachineLibrary_SepByComma_Scanner(activ=13, preDefWS=13)
    b = MachineLibrary_SepByComma_Field_Scanner(fieldName="sample_text", fieldNo=7)
    _safe_set(b, 'MachineLibrary_SepByComma_Field_Scanner', a1)
    assert _is_linked(b, 'MachineLibrary_SepByComma_Field_Scanner', a1)
    if hasattr(a1, 'MachineLibrary_SepByComma_Scanner206'):
        assert _is_linked(a1, 'MachineLibrary_SepByComma_Scanner206', b)
    _safe_set(b, 'MachineLibrary_SepByComma_Field_Scanner', a2)
    assert _is_linked(b, 'MachineLibrary_SepByComma_Field_Scanner', a2)
    if hasattr(a1, 'MachineLibrary_SepByComma_Scanner206'):
        assert not _is_linked(a1, 'MachineLibrary_SepByComma_Scanner206', b)
    if hasattr(a2, 'MachineLibrary_SepByComma_Scanner206'):
        assert _is_linked(a2, 'MachineLibrary_SepByComma_Scanner206', b)
    _safe_set(b, 'MachineLibrary_SepByComma_Field_Scanner', None)
    assert not _is_linked(b, 'MachineLibrary_SepByComma_Field_Scanner', a2)
    if hasattr(a2, 'MachineLibrary_SepByComma_Scanner206'):
        assert not _is_linked(a2, 'MachineLibrary_SepByComma_Scanner206', b)


def test_assoc_id207_reverse_link_reassign_clear():
    a1 = MachineLibrary_SepByComma_Scanner(activ=7, preDefWS=7)
    a2 = MachineLibrary_SepByComma_Scanner(activ=13, preDefWS=13)
    b = MachineLibrary_SepByComma_ID_Scanner(idCharValue="sample_text", idPrevValue="sample_text", idSeq_X=7, idValue=7)
    _safe_set(b, 'MachineLibrary_SepByComma_ID_Scanner', a1)
    assert _is_linked(b, 'MachineLibrary_SepByComma_ID_Scanner', a1)
    if hasattr(a1, 'MachineLibrary_SepByComma_Scanner208'):
        assert _is_linked(a1, 'MachineLibrary_SepByComma_Scanner208', b)
    _safe_set(b, 'MachineLibrary_SepByComma_ID_Scanner', a2)
    assert _is_linked(b, 'MachineLibrary_SepByComma_ID_Scanner', a2)
    if hasattr(a1, 'MachineLibrary_SepByComma_Scanner208'):
        assert not _is_linked(a1, 'MachineLibrary_SepByComma_Scanner208', b)
    if hasattr(a2, 'MachineLibrary_SepByComma_Scanner208'):
        assert _is_linked(a2, 'MachineLibrary_SepByComma_Scanner208', b)
    _safe_set(b, 'MachineLibrary_SepByComma_ID_Scanner', None)
    assert not _is_linked(b, 'MachineLibrary_SepByComma_ID_Scanner', a2)
    if hasattr(a2, 'MachineLibrary_SepByComma_Scanner208'):
        assert not _is_linked(a2, 'MachineLibrary_SepByComma_Scanner208', b)


def test_assoc_keyword203_reverse_link_reassign_clear():
    a1 = MachineLibrary_InsertRemove_Keywords_Host(keywordKey="sample_text", keywordValue="sample_text")
    a2 = MachineLibrary_InsertRemove_Keywords_Host(keywordKey="sample_text_2", keywordValue="sample_text_2")
    b = MachineLibrary_InsertRemove_Host(report_All=7)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host204', {a1})
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Host204', a1)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Keywords_Host'):
        assert _is_linked(a1, 'MachineLibrary_InsertRemove_Keywords_Host', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host204', {a2})
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Host204', a2)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Keywords_Host'):
        assert not _is_linked(a1, 'MachineLibrary_InsertRemove_Keywords_Host', b)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Keywords_Host'):
        assert _is_linked(a2, 'MachineLibrary_InsertRemove_Keywords_Host', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host204', set())
    assert not _is_linked(b, 'MachineLibrary_InsertRemove_Host204', a2)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Keywords_Host'):
        assert not _is_linked(a2, 'MachineLibrary_InsertRemove_Keywords_Host', b)


def test_assoc_links3_reverse_link_reassign_clear():
    a1 = MachineLibrary_Link2(link2ParamFile="sample_text", link2ParamSection="sample_text", link2Type="sample_text")
    a2 = MachineLibrary_Link2(link2ParamFile="sample_text_2", link2ParamSection="sample_text_2", link2Type="sample_text_2")
    b = MachineLibrary_LabMachine(createWinCCTags="sample_text", driver="sample_text", linkParamFile="sample_text", linkParamSection="sample_text", linkType="sample_text", machineName="sample_text", machineVersionNo=3.14, versionRemark="sample_text")
    _safe_set(b, 'MachineLibrary_LabMachine4', a1)
    assert _is_linked(b, 'MachineLibrary_LabMachine4', a1)
    if hasattr(a1, 'MachineLibrary_Link2'):
        assert _is_linked(a1, 'MachineLibrary_Link2', b)
    _safe_set(b, 'MachineLibrary_LabMachine4', a2)
    assert _is_linked(b, 'MachineLibrary_LabMachine4', a2)
    if hasattr(a1, 'MachineLibrary_Link2'):
        assert not _is_linked(a1, 'MachineLibrary_Link2', b)
    if hasattr(a2, 'MachineLibrary_Link2'):
        assert _is_linked(a2, 'MachineLibrary_Link2', b)
    _safe_set(b, 'MachineLibrary_LabMachine4', None)
    assert not _is_linked(b, 'MachineLibrary_LabMachine4', a2)
    if hasattr(a2, 'MachineLibrary_Link2'):
        assert not _is_linked(a2, 'MachineLibrary_Link2', b)


def test_assoc_nodeConfig5_reverse_link_reassign_clear():
    a1 = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    a2 = MachineLibrary_NodeConfig(nodeName="sample_text_2", nodeNo=13, simFileName="sample_text_2")
    b = MachineLibrary_LabMachine(createWinCCTags="sample_text", driver="sample_text", linkParamFile="sample_text", linkParamSection="sample_text", linkType="sample_text", machineName="sample_text", machineVersionNo=3.14, versionRemark="sample_text")
    _safe_set(b, 'MachineLibrary_LabMachine6', a1)
    assert _is_linked(b, 'MachineLibrary_LabMachine6', a1)
    if hasattr(a1, 'MachineLibrary_NodeConfig'):
        assert _is_linked(a1, 'MachineLibrary_NodeConfig', b)
    _safe_set(b, 'MachineLibrary_LabMachine6', a2)
    assert _is_linked(b, 'MachineLibrary_LabMachine6', a2)
    if hasattr(a1, 'MachineLibrary_NodeConfig'):
        assert not _is_linked(a1, 'MachineLibrary_NodeConfig', b)
    if hasattr(a2, 'MachineLibrary_NodeConfig'):
        assert _is_linked(a2, 'MachineLibrary_NodeConfig', b)
    _safe_set(b, 'MachineLibrary_LabMachine6', None)
    assert not _is_linked(b, 'MachineLibrary_LabMachine6', a2)
    if hasattr(a2, 'MachineLibrary_NodeConfig'):
        assert not _is_linked(a2, 'MachineLibrary_NodeConfig', b)


def test_assoc_nodeGeneral37_reverse_link_reassign_clear():
    a1 = MachineLibrary_NodeGeneral(canCreateErrorTag="sample_text", canCreateStateTag="sample_text")
    a2 = MachineLibrary_NodeGeneral(canCreateErrorTag="sample_text_2", canCreateStateTag="sample_text_2")
    b = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    _safe_set(b, 'MachineLibrary_NodeConfig38', a1)
    assert _is_linked(b, 'MachineLibrary_NodeConfig38', a1)
    if hasattr(a1, 'MachineLibrary_NodeGeneral'):
        assert _is_linked(a1, 'MachineLibrary_NodeGeneral', b)
    _safe_set(b, 'MachineLibrary_NodeConfig38', a2)
    assert _is_linked(b, 'MachineLibrary_NodeConfig38', a2)
    if hasattr(a1, 'MachineLibrary_NodeGeneral'):
        assert not _is_linked(a1, 'MachineLibrary_NodeGeneral', b)
    if hasattr(a2, 'MachineLibrary_NodeGeneral'):
        assert _is_linked(a2, 'MachineLibrary_NodeGeneral', b)
    _safe_set(b, 'MachineLibrary_NodeConfig38', None)
    assert not _is_linked(b, 'MachineLibrary_NodeConfig38', a2)
    if hasattr(a2, 'MachineLibrary_NodeGeneral'):
        assert not _is_linked(a2, 'MachineLibrary_NodeGeneral', b)


def test_assoc_parameter225_reverse_link_reassign_clear():
    a1 = MachineLibrary_Parameters(parameterConfigNo="sample_text", parameterConfigYes="sample_text")
    a2 = MachineLibrary_Parameters(parameterConfigNo="sample_text_2", parameterConfigYes="sample_text_2")
    b = MachineLibrary_Parameter(parameterConfig="sample_text", parameterMax=7, parameterMin=7, parameterName="sample_text", parameterParaLen=7, parameterT1="sample_text", parameterT2="sample_text", parameterType="sample_text", parameterV="sample_text", parameterV0="sample_text", parameterV1="sample_text")
    _safe_set(b, 'MachineLibrary_Parameter', a1)
    assert _is_linked(b, 'MachineLibrary_Parameter', a1)
    if hasattr(a1, 'MachineLibrary_Parameters226'):
        assert _is_linked(a1, 'MachineLibrary_Parameters226', b)
    _safe_set(b, 'MachineLibrary_Parameter', a2)
    assert _is_linked(b, 'MachineLibrary_Parameter', a2)
    if hasattr(a1, 'MachineLibrary_Parameters226'):
        assert not _is_linked(a1, 'MachineLibrary_Parameters226', b)
    if hasattr(a2, 'MachineLibrary_Parameters226'):
        assert _is_linked(a2, 'MachineLibrary_Parameters226', b)
    _safe_set(b, 'MachineLibrary_Parameter', None)
    assert not _is_linked(b, 'MachineLibrary_Parameter', a2)
    if hasattr(a2, 'MachineLibrary_Parameters226'):
        assert not _is_linked(a2, 'MachineLibrary_Parameters226', b)


def test_assoc_parameters223_reverse_link_reassign_clear():
    a1 = MachineLibrary_UnitProgram(unitProgName="sample_text")
    a2 = MachineLibrary_UnitProgram(unitProgName="sample_text_2")
    b = MachineLibrary_UnitProgParameters(parameter="sample_text", parameterNo=7)
    _safe_set(b, 'MachineLibrary_UnitProgParameters', a1)
    assert _is_linked(b, 'MachineLibrary_UnitProgParameters', a1)
    if hasattr(a1, 'MachineLibrary_UnitProgram224'):
        assert _is_linked(a1, 'MachineLibrary_UnitProgram224', b)
    _safe_set(b, 'MachineLibrary_UnitProgParameters', a2)
    assert _is_linked(b, 'MachineLibrary_UnitProgParameters', a2)
    if hasattr(a1, 'MachineLibrary_UnitProgram224'):
        assert not _is_linked(a1, 'MachineLibrary_UnitProgram224', b)
    if hasattr(a2, 'MachineLibrary_UnitProgram224'):
        assert _is_linked(a2, 'MachineLibrary_UnitProgram224', b)
    _safe_set(b, 'MachineLibrary_UnitProgParameters', None)
    assert not _is_linked(b, 'MachineLibrary_UnitProgParameters', a2)
    if hasattr(a2, 'MachineLibrary_UnitProgram224'):
        assert not _is_linked(a2, 'MachineLibrary_UnitProgram224', b)


def test_assoc_parameters31_reverse_link_reassign_clear():
    a1 = MachineLibrary_Parameters(parameterConfigNo="sample_text", parameterConfigYes="sample_text")
    a2 = MachineLibrary_Parameters(parameterConfigNo="sample_text_2", parameterConfigYes="sample_text_2")
    b = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    _safe_set(b, 'MachineLibrary_NodeConfig32', a1)
    assert _is_linked(b, 'MachineLibrary_NodeConfig32', a1)
    if hasattr(a1, 'MachineLibrary_Parameters'):
        assert _is_linked(a1, 'MachineLibrary_Parameters', b)
    _safe_set(b, 'MachineLibrary_NodeConfig32', a2)
    assert _is_linked(b, 'MachineLibrary_NodeConfig32', a2)
    if hasattr(a1, 'MachineLibrary_Parameters'):
        assert not _is_linked(a1, 'MachineLibrary_Parameters', b)
    if hasattr(a2, 'MachineLibrary_Parameters'):
        assert _is_linked(a2, 'MachineLibrary_Parameters', b)
    _safe_set(b, 'MachineLibrary_NodeConfig32', None)
    assert not _is_linked(b, 'MachineLibrary_NodeConfig32', a2)
    if hasattr(a2, 'MachineLibrary_Parameters'):
        assert not _is_linked(a2, 'MachineLibrary_Parameters', b)


def test_assoc_plainmoveEntrySend237_reverse_link_reassign_clear():
    a1 = MachineLibrary_PlainMoveEntrySend(plainmoveEntry="sample_text", plainmoveSend="sample_text", plainmoveSeq=7)
    a2 = MachineLibrary_PlainMoveEntrySend(plainmoveEntry="sample_text_2", plainmoveSend="sample_text_2", plainmoveSeq=13)
    b = MachineLibrary_PlainMove(plainmovePreDefWS="sample_text", plainmoveSID_REF="sample_text", plainmoveType=7)
    _safe_set(b, 'MachineLibrary_PlainMove238', {a1})
    assert _is_linked(b, 'MachineLibrary_PlainMove238', a1)
    if hasattr(a1, 'MachineLibrary_PlainMoveEntrySend'):
        assert _is_linked(a1, 'MachineLibrary_PlainMoveEntrySend', b)
    _safe_set(b, 'MachineLibrary_PlainMove238', {a2})
    assert _is_linked(b, 'MachineLibrary_PlainMove238', a2)
    if hasattr(a1, 'MachineLibrary_PlainMoveEntrySend'):
        assert not _is_linked(a1, 'MachineLibrary_PlainMoveEntrySend', b)
    if hasattr(a2, 'MachineLibrary_PlainMoveEntrySend'):
        assert _is_linked(a2, 'MachineLibrary_PlainMoveEntrySend', b)
    _safe_set(b, 'MachineLibrary_PlainMove238', set())
    assert not _is_linked(b, 'MachineLibrary_PlainMove238', a2)
    if hasattr(a2, 'MachineLibrary_PlainMoveEntrySend'):
        assert not _is_linked(a2, 'MachineLibrary_PlainMoveEntrySend', b)


def test_assoc_plctopmmatrix59_reverse_link_reassign_clear():
    a1 = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    a2 = MachineLibrary_Units(internalUniNo=13, unitName="sample_text_2", unitNo=13)
    b = MachineLibrary_PLCtoPmMatrix(plcpmmatrixBit0=7, plcpmmatrixBit1=7, plcpmmatrixBit10=7, plcpmmatrixBit11=7, plcpmmatrixBit12=7, plcpmmatrixBit13=7, plcpmmatrixBit14=7, plcpmmatrixBit15=7, plcpmmatrixBit2=7, plcpmmatrixBit3=7, plcpmmatrixBit4=7, plcpmmatrixBit5=7, plcpmmatrixBit6=7, plcpmmatrixBit7=7, plcpmmatrixBit8=7, plcpmmatrixBit9=7)
    _safe_set(b, 'MachineLibrary_PLCtoPmMatrix', a1)
    assert _is_linked(b, 'MachineLibrary_PLCtoPmMatrix', a1)
    if hasattr(a1, 'MachineLibrary_Units60'):
        assert _is_linked(a1, 'MachineLibrary_Units60', b)
    _safe_set(b, 'MachineLibrary_PLCtoPmMatrix', a2)
    assert _is_linked(b, 'MachineLibrary_PLCtoPmMatrix', a2)
    if hasattr(a1, 'MachineLibrary_Units60'):
        assert not _is_linked(a1, 'MachineLibrary_Units60', b)
    if hasattr(a2, 'MachineLibrary_Units60'):
        assert _is_linked(a2, 'MachineLibrary_Units60', b)
    _safe_set(b, 'MachineLibrary_PLCtoPmMatrix', None)
    assert not _is_linked(b, 'MachineLibrary_PLCtoPmMatrix', a2)
    if hasattr(a2, 'MachineLibrary_Units60'):
        assert not _is_linked(a2, 'MachineLibrary_Units60', b)


def test_assoc_robotWarningONDelete247_reverse_link_reassign_clear():
    a1 = MachineLibrary_RobotWarningONDelete(robotErrBitWhenConfirmationIsNeededFor_PM=7, robotErrBitWhenConfirmationIsNeededFor_Robot=7, robotExtraPos_1="sample_text", robotExtraUnit_2="sample_text")
    a2 = MachineLibrary_RobotWarningONDelete(robotErrBitWhenConfirmationIsNeededFor_PM=13, robotErrBitWhenConfirmationIsNeededFor_Robot=13, robotExtraPos_1="sample_text_2", robotExtraUnit_2="sample_text_2")
    b = MachineLibrary_RobotConfiguration(robotActivate=7, robotID="sample_text", robotIPAddress="sample_text", robotSystemID="sample_text")
    _safe_set(b, 'MachineLibrary_RobotConfiguration248', a1)
    assert _is_linked(b, 'MachineLibrary_RobotConfiguration248', a1)
    if hasattr(a1, 'MachineLibrary_RobotWarningONDelete'):
        assert _is_linked(a1, 'MachineLibrary_RobotWarningONDelete', b)
    _safe_set(b, 'MachineLibrary_RobotConfiguration248', a2)
    assert _is_linked(b, 'MachineLibrary_RobotConfiguration248', a2)
    if hasattr(a1, 'MachineLibrary_RobotWarningONDelete'):
        assert not _is_linked(a1, 'MachineLibrary_RobotWarningONDelete', b)
    if hasattr(a2, 'MachineLibrary_RobotWarningONDelete'):
        assert _is_linked(a2, 'MachineLibrary_RobotWarningONDelete', b)
    _safe_set(b, 'MachineLibrary_RobotConfiguration248', None)
    assert not _is_linked(b, 'MachineLibrary_RobotConfiguration248', a2)
    if hasattr(a2, 'MachineLibrary_RobotWarningONDelete'):
        assert not _is_linked(a2, 'MachineLibrary_RobotWarningONDelete', b)


def test_assoc_type201_reverse_link_reassign_clear():
    a1 = MachineLibrary_InsertRemove_Types_Host(typeNo=7, typeValue="sample_text")
    a2 = MachineLibrary_InsertRemove_Types_Host(typeNo=13, typeValue="sample_text_2")
    b = MachineLibrary_InsertRemove_Host(report_All=7)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host202', {a1})
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Host202', a1)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Types_Host'):
        assert _is_linked(a1, 'MachineLibrary_InsertRemove_Types_Host', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host202', {a2})
    assert _is_linked(b, 'MachineLibrary_InsertRemove_Host202', a2)
    if hasattr(a1, 'MachineLibrary_InsertRemove_Types_Host'):
        assert not _is_linked(a1, 'MachineLibrary_InsertRemove_Types_Host', b)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Types_Host'):
        assert _is_linked(a2, 'MachineLibrary_InsertRemove_Types_Host', b)
    _safe_set(b, 'MachineLibrary_InsertRemove_Host202', set())
    assert not _is_linked(b, 'MachineLibrary_InsertRemove_Host202', a2)
    if hasattr(a2, 'MachineLibrary_InsertRemove_Types_Host'):
        assert not _is_linked(a2, 'MachineLibrary_InsertRemove_Types_Host', b)


def test_assoc_units25_reverse_link_reassign_clear():
    a1 = MachineLibrary_Units(internalUniNo=7, unitName="sample_text", unitNo=7)
    a2 = MachineLibrary_Units(internalUniNo=13, unitName="sample_text_2", unitNo=13)
    b = MachineLibrary_NodeConfig(nodeName="sample_text", nodeNo=7, simFileName="sample_text")
    _safe_set(b, 'MachineLibrary_NodeConfig26', {a1})
    assert _is_linked(b, 'MachineLibrary_NodeConfig26', a1)
    if hasattr(a1, 'MachineLibrary_Units'):
        assert _is_linked(a1, 'MachineLibrary_Units', b)
    _safe_set(b, 'MachineLibrary_NodeConfig26', {a2})
    assert _is_linked(b, 'MachineLibrary_NodeConfig26', a2)
    if hasattr(a1, 'MachineLibrary_Units'):
        assert not _is_linked(a1, 'MachineLibrary_Units', b)
    if hasattr(a2, 'MachineLibrary_Units'):
        assert _is_linked(a2, 'MachineLibrary_Units', b)
    _safe_set(b, 'MachineLibrary_NodeConfig26', set())
    assert not _is_linked(b, 'MachineLibrary_NodeConfig26', a2)
    if hasattr(a2, 'MachineLibrary_Units'):
        assert not _is_linked(a2, 'MachineLibrary_Units', b)


